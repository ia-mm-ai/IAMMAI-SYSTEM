"""Resolve one local relevance medium second bounded relevance receipt.

This module records one small inspectable receipt object for one clean
LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION artifact. It does
not expand the second reception and does not create orientation, index,
multiplicity, relation, comparison, permission, feed, source, authority,
runtime, interface, distributed, deployment, or follow-on behavior.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumSecondBoundedRelevanceReceiptV0MinError(Exception):
    """Bounded error for malformed request path reads."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_second_bounded_relevance_receipt_v0_min"

SECOND_RECEIPT_TYPE = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT"
SECOND_RECEIPT_SCOPE = "SECOND_INSPECTABLE_RECEIPT_ONLY"
SECOND_RECEPTION_TYPE = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
SECOND_RECEPTION_SCOPE = "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY"
SECOND_RECEPTION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_RECORDED"
)

DEFAULT_SECOND_RECEIPT_ID = "local_relevance_medium_second_bounded_relevance_receipt_001"
DEFAULT_REQUEST_ID = "local_relevance_medium_second_bounded_relevance_receipt_reference_review_001"
DEFAULT_SECOND_RECEPTION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min/"
    "local_relevance_medium_second_bounded_relevance_reception_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_reception_v0_min_result.json"
)

DEFAULT_SECOND_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_002"
DEFAULT_SECOND_RELEVANCE_BASIS_ID = "bounded_relevance_basis_002"
DEFAULT_SECOND_RELEVANCE_SCOPE_ID = "bounded_relevance_scope_002"
DEFAULT_SECOND_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_002"
DEFAULT_SECOND_RECEPTION_ENVELOPE_ID = "bounded_relevance_reception_envelope_002"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min"
)

SUPPORTED_SECOND_RECEIPT_SCOPE_VALUES = (SECOND_RECEIPT_SCOPE,)
SUPPORTED_SECOND_RECEIPT_TYPE_VALUES = (SECOND_RECEIPT_TYPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_orientation_view_created",
    "second_index_entry_created",
    "local_medium_multiplicity_result_created",
    "relation_view_created",
    "comparison_view_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
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
    "artifact_existence_treated_as_second_receipt_authority",
    "latest_file_posture_treated_as_second_receipt_authority",
    "repo_local_availability_treated_as_second_receipt_authority",
    "hidden_repo_state_used_as_second_receipt_content",
    "hidden_repo_state_used_as_second_receipt_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_second_bounded_relevance_receipt_recorded",
    "basis_second_bounded_relevance_reception_artifact_preserved",
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
    "second_received_signal_id_preserved",
    "second_relevance_basis_id_preserved",
    "second_relevance_scope_id_preserved",
    "second_carrier_context_id_preserved",
    "second_reception_envelope_id_preserved",
    "second_receipt_scope_inspectable_only",
    "second_receipt_does_not_expand_reception",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_OBJECT_MISSING",
    "SECOND_RECEPTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
    "SECOND_RECEPTION_SCOPE_NOT_SECOND_ONLY",
    "SECOND_RECEIVED_SIGNAL_ID_MISSING",
    "SECOND_RECEIVED_SIGNAL_ID_EQUALS_EXISTING_SIGNAL",
    "SECOND_RELEVANCE_BASIS_ID_MISSING",
    "SECOND_RELEVANCE_SCOPE_ID_MISSING",
    "SECOND_CARRIER_CONTEXT_ID_MISSING",
    "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
    "SECOND_RECEIPT_SCOPE_MISSING",
    "SECOND_RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
    "SECOND_RECEIPT_TYPE_MISSING",
    "SECOND_RECEIPT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT",
    "SECOND_RECEPTION_ARTIFACT_MISSING",
    "SECOND_RECEIVED_IDENTIFIERS_NOT_PRESERVED",
    "SECOND_RECEIPT_EXPANDS_SECOND_RECEPTION",
    "SECOND_ORIENTATION_VIEW_CREATED",
    "SECOND_INDEX_ENTRY_CREATED",
    "LOCAL_MEDIUM_MULTIPLICITY_RESULT_CREATED",
    "RELATION_VIEW_CREATED",
    "COMPARISON_VIEW_CREATED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_RECEIPT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_SECOND_RECEIPT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEIPT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEIPT_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_second_receipt_body",
    "raw_second_bounded_relevance_receipt_body",
    "raw_second_reception_body",
    "raw_successor_candidate_admission_body",
    "raw_successor_reception_request_body",
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
    "second_receipt_body",
    "second_bounded_relevance_receipt_body",
    "second_reception_body",
    "successor_candidate_admission_body",
    "successor_reception_request_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = frozenset(
    (
        SECOND_RECEIPT_TYPE,
        SECOND_RECEIPT_SCOPE,
        SECOND_RECEPTION_TYPE,
        SECOND_RECEPTION_SCOPE,
        SECOND_RECEPTION_RECORDED_OUTCOME,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
        RESULT_VERSION,
        RESOLVER_MODULE,
        DEFAULT_SECOND_RECEIVED_SIGNAL_ID,
        DEFAULT_SECOND_RELEVANCE_BASIS_ID,
        DEFAULT_SECOND_RELEVANCE_SCOPE_ID,
        DEFAULT_SECOND_CARRIER_CONTEXT_ID,
        DEFAULT_SECOND_RECEPTION_ENVELOPE_ID,
    )
    + OUTCOME_FAMILY
    + BLOCK_CODES
    + REQUIRED_FALSE_NON_CLAIMS
    + ALLOWED_TRUE_RECORDED_FIELDS
)

FALSE_REQUEST_BLOCKS = (
    ("second_orientation_view_created", "SECOND_ORIENTATION_VIEW_CREATED"),
    ("second_index_entry_created", "SECOND_INDEX_ENTRY_CREATED"),
    ("local_medium_multiplicity_result_created", "LOCAL_MEDIUM_MULTIPLICITY_RESULT_CREATED"),
    ("relation_view_created", "RELATION_VIEW_CREATED"),
    ("comparison_view_created", "COMPARISON_VIEW_CREATED"),
    ("repeated_reception_permission_created", "REPEATED_RECEPTION_PERMISSION_CREATED"),
    ("arbitrary_reception_created", "ARBITRARY_RECEPTION_CREATED"),
    ("feed_created", "FEED_CREATED"),
    ("index_system_created", "INDEX_SYSTEM_CREATED"),
    ("registry_created", "REGISTRY_CREATED"),
    ("search_surface_created", "SEARCH_SURFACE_CREATED"),
    ("ranking_surface_created", "RANKING_SURFACE_CREATED"),
    ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
    ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
    ("source_created", "SOURCE_CREATED"),
    ("authority_created", "AUTHORITY_CREATED"),
    ("currentness_created", "CURRENTNESS_CREATED"),
    ("truth_created", "TRUTH_CREATED"),
    ("action_created", "ACTION_CREATED"),
    ("synchronization_created", "SYNCHRONIZATION_CREATED"),
    ("participation_authorized", "PARTICIPATION_AUTHORIZED"),
    ("participant_role_created", "PARTICIPANT_ROLE_CREATED"),
    ("runtime_permission_created", "RUNTIME_PERMISSION_CREATED"),
    ("public_api_created", "PUBLIC_API_CREATED"),
    ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
    ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("broader_reusable_permission_created", "BROADER_REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("adoption_created", "ADOPTION_CREATED"),
    ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
    ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    (
        "artifact_existence_treated_as_second_receipt_authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_RECEIPT_AUTHORITY",
    ),
    (
        "latest_file_posture_treated_as_second_receipt_authority",
        "LATEST_FILE_POSTURE_TREATED_AS_SECOND_RECEIPT_AUTHORITY",
    ),
    (
        "repo_local_availability_treated_as_second_receipt_authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_RECEIPT_AUTHORITY",
    ),
    (
        "hidden_repo_state_used_as_second_receipt_content",
        "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEIPT_CONTENT",
    ),
    (
        "hidden_repo_state_used_as_second_receipt_authority",
        "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEIPT_AUTHORITY",
    ),
    ("prior_artifacts_mutated", "PRIOR_ARTIFACTS_MUTATED"),
    ("predecessor_failure_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("predecessor_failure_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("predecessor_failure_claimed_passed", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _is_sensitive_key(key: str) -> bool:
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if parent_key is not None and _is_sensitive_key(parent_key):
        return "[REDACTED_RAW_BODY_CONTENT]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_HOSTILE_SENTINEL]")
        return sanitized
    if isinstance(value, Mapping):
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    failure_code = None if passed else code
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": failure_code,
        "failure_code": failure_code,
    }


def _checks_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None]:
    if not path_value:
        return None, "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING"
    try:
        path = Path(str(path_value))
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return None, "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE"
    if not isinstance(loaded, Mapping):
        return None, "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT"
    return dict(loaded), None


def _failed_check_count_from_artifact(artifact: Mapping[str, Any], summary: Mapping[str, Any]) -> Any:
    metadata = _as_mapping(
        artifact.get("local_relevance_medium_second_bounded_relevance_reception_metadata")
    )
    checks = artifact.get("local_relevance_medium_second_bounded_relevance_reception_checks")
    explicit = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        artifact.get("failed_check_count"),
    )
    if explicit is not None:
        return explicit
    if isinstance(checks, list):
        return sum(1 for check in checks if _as_mapping(check).get("passed") is not True)
    return None


def _extract_second_reception_facts(
    artifact: Mapping[str, Any] | None,
    artifact_path: str | None,
) -> dict[str, Any]:
    if artifact is None:
        return {"basis_second_bounded_relevance_reception_artifact": artifact_path}

    metadata = _as_mapping(
        artifact.get("local_relevance_medium_second_bounded_relevance_reception_metadata")
    )
    summary = _as_mapping(
        artifact.get("local_relevance_medium_second_bounded_relevance_reception_summary")
    )
    second_object = _as_mapping(artifact.get("second_bounded_relevance_reception_object"))

    return {
        "basis_second_bounded_relevance_reception_artifact": artifact_path,
        "basis_second_bounded_relevance_reception_outcome": artifact.get("outcome"),
        "basis_second_bounded_relevance_reception_result_version": _first_present(
            metadata.get("local_relevance_medium_second_bounded_relevance_reception_version"),
            metadata.get("result_version"),
            summary.get("result_version"),
            second_object.get("second_reception_version"),
            artifact.get("result_version"),
        ),
        "basis_second_bounded_relevance_reception_failed_check_count": (
            _failed_check_count_from_artifact(artifact, summary)
        ),
        "second_bounded_relevance_reception_object": second_object,
        "basis_successor_candidate_admission_artifact": second_object.get(
            "basis_successor_candidate_admission_artifact"
        ),
        "basis_successor_reception_request_artifact": second_object.get(
            "basis_successor_reception_request_artifact"
        ),
        "basis_index_entry_artifact": second_object.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": second_object.get(
            "existing_orientation_view_artifact"
        ),
        "existing_source_receipt_artifact": second_object.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": second_object.get(
            "existing_referenced_reception_artifact"
        ),
        "existing_received_signal_id": second_object.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": second_object.get(
            "existing_received_relevance_basis_id"
        ),
        "existing_received_relevance_scope_id": second_object.get(
            "existing_received_relevance_scope_id"
        ),
        "existing_received_carrier_context_id": second_object.get(
            "existing_received_carrier_context_id"
        ),
        "existing_received_reception_envelope_id": second_object.get(
            "existing_received_reception_envelope_id"
        ),
        "admitted_successor_candidate_id": second_object.get("admitted_successor_candidate_id"),
        "second_reception_type": second_object.get("second_reception_type"),
        "second_reception_scope": second_object.get("second_reception_scope"),
        "second_received_signal_id": second_object.get("second_received_signal_id"),
        "second_relevance_basis_id": second_object.get("second_relevance_basis_id"),
        "second_relevance_scope_id": second_object.get("second_relevance_scope_id"),
        "second_carrier_context_id": second_object.get("second_carrier_context_id"),
        "second_reception_envelope_id": second_object.get("second_reception_envelope_id"),
    }


def _declared_non_claims_are_clean(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if declared.get(key) is not False:
            return False
    return True


def _request_flag(request: Mapping[str, Any], key: str) -> bool:
    return request.get(key) is True


def _declared_or_request_flag(request: Mapping[str, Any], key: str) -> bool:
    declared = request.get("declared_non_claims")
    return _request_flag(request, key) or (isinstance(declared, Mapping) and declared.get(key) is True)


def _build_checks(
    request: Mapping[str, Any],
    artifact: Mapping[str, Any] | None,
    read_error: str | None,
    facts: Mapping[str, Any],
) -> list[dict[str, Any]]:
    question = request.get("local_relevance_medium_second_bounded_relevance_receipt_question")
    intent = request.get("local_relevance_medium_second_bounded_relevance_receipt_intent")
    selected_path = request.get("selected_second_bounded_relevance_reception_artifact")
    second_receipt_scope = request.get("second_receipt_scope")
    second_receipt_type = request.get("second_receipt_type")
    second_reception_object = facts.get("second_bounded_relevance_reception_object")
    checks: list[dict[str, Any]] = []

    checks.append(
        _check(
            "second_receipt_question_declared",
            isinstance(question, str) and bool(question.strip()),
            "declared second receipt question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent_supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block_intent_not_requested",
            intent != INTENT_BLOCK,
            "block intent absent",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
        )
    )
    path_declared = bool(selected_path) and not _request_flag(
        request, "selected_second_bounded_relevance_reception_artifact_missing"
    )
    checks.append(
        _check(
            "selected_second_bounded_relevance_reception_artifact_path_declared",
            path_declared,
            "selected second reception artifact path declared",
            selected_path,
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected_second_bounded_relevance_reception_artifact_readable_json",
            read_error not in {
                "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE",
                "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING",
            },
            "readable JSON object",
            read_error or "readable",
            (
                "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING"
                if read_error == "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING"
                else "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE"
            ),
        )
    )
    checks.append(
        _check(
            "selected_second_bounded_relevance_reception_artifact_json_object",
            read_error != "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
            "JSON object",
            read_error or "JSON object",
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
        )
    )

    artifact_not_recorded = _request_flag(
        request, "selected_second_bounded_relevance_reception_artifact_not_recorded"
    )
    checks.append(
        _check(
            "second_bounded_relevance_reception_artifact_outcome_recorded",
            (
                facts.get("basis_second_bounded_relevance_reception_outcome")
                == SECOND_RECEPTION_RECORDED_OUTCOME
                and not artifact_not_recorded
            ),
            SECOND_RECEPTION_RECORDED_OUTCOME,
            facts.get("basis_second_bounded_relevance_reception_outcome"),
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
        )
    )
    version_not_clean = _request_flag(
        request, "selected_second_bounded_relevance_reception_artifact_version_not_0_1_0"
    )
    checks.append(
        _check(
            "second_bounded_relevance_reception_artifact_result_version_0_1_0",
            (
                facts.get("basis_second_bounded_relevance_reception_result_version")
                == RESULT_VERSION
                and not version_not_clean
            ),
            RESULT_VERSION,
            facts.get("basis_second_bounded_relevance_reception_result_version"),
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    failed_checks_present = _request_flag(
        request, "selected_second_bounded_relevance_reception_artifact_failed_checks_present"
    )
    failed_count = facts.get("basis_second_bounded_relevance_reception_failed_check_count")
    checks.append(
        _check(
            "second_bounded_relevance_reception_artifact_failed_check_count_zero",
            failed_count == 0 and not failed_checks_present,
            0,
            failed_count,
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "second_bounded_relevance_reception_object_present",
            bool(second_reception_object)
            and not _request_flag(request, "second_bounded_relevance_reception_object_missing"),
            "one second bounded relevance reception object",
            "present" if second_reception_object else "missing",
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_OBJECT_MISSING",
        )
    )
    checks.append(
        _check(
            "second_reception_type_exact",
            facts.get("second_reception_type") == SECOND_RECEPTION_TYPE
            and not _request_flag(request, "second_reception_type_not_second_bounded_relevance_reception"),
            SECOND_RECEPTION_TYPE,
            facts.get("second_reception_type"),
            "SECOND_RECEPTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
        )
    )
    checks.append(
        _check(
            "second_reception_scope_second_only",
            facts.get("second_reception_scope") == SECOND_RECEPTION_SCOPE
            and not _request_flag(request, "second_reception_scope_not_second_only"),
            SECOND_RECEPTION_SCOPE,
            facts.get("second_reception_scope"),
            "SECOND_RECEPTION_SCOPE_NOT_SECOND_ONLY",
        )
    )
    checks.append(
        _check(
            "second_received_signal_id_present",
            bool(facts.get("second_received_signal_id"))
            and not _request_flag(request, "second_received_signal_id_missing"),
            "second received signal id present",
            facts.get("second_received_signal_id"),
            "SECOND_RECEIVED_SIGNAL_ID_MISSING",
        )
    )
    second_signal_equals_existing = (
        facts.get("second_received_signal_id") == facts.get("existing_received_signal_id")
    )
    checks.append(
        _check(
            "second_received_signal_differs_from_existing_signal",
            bool(facts.get("second_received_signal_id"))
            and not second_signal_equals_existing
            and not _request_flag(request, "second_received_signal_id_equals_existing_signal"),
            "second received signal differs from existing signal",
            {
                "existing_received_signal_id": facts.get("existing_received_signal_id"),
                "second_received_signal_id": facts.get("second_received_signal_id"),
            },
            "SECOND_RECEIVED_SIGNAL_ID_EQUALS_EXISTING_SIGNAL",
        )
    )
    checks.append(
        _check(
            "second_relevance_basis_id_present",
            bool(facts.get("second_relevance_basis_id"))
            and not _request_flag(request, "second_relevance_basis_id_missing"),
            "second relevance basis id present",
            facts.get("second_relevance_basis_id"),
            "SECOND_RELEVANCE_BASIS_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second_relevance_scope_id_present",
            bool(facts.get("second_relevance_scope_id"))
            and not _request_flag(request, "second_relevance_scope_id_missing"),
            "second relevance scope id present",
            facts.get("second_relevance_scope_id"),
            "SECOND_RELEVANCE_SCOPE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second_carrier_context_id_present",
            bool(facts.get("second_carrier_context_id"))
            and not _request_flag(request, "second_carrier_context_id_missing"),
            "second carrier context id present",
            facts.get("second_carrier_context_id"),
            "SECOND_CARRIER_CONTEXT_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second_reception_envelope_id_present",
            bool(facts.get("second_reception_envelope_id"))
            and not _request_flag(request, "second_reception_envelope_id_missing"),
            "second reception envelope id present",
            facts.get("second_reception_envelope_id"),
            "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second_receipt_type_declared",
            bool(second_receipt_type),
            SECOND_RECEIPT_TYPE,
            second_receipt_type,
            "SECOND_RECEIPT_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "second_receipt_type_exact",
            second_receipt_type == SECOND_RECEIPT_TYPE
            and not _request_flag(
                request, "second_receipt_type_not_local_relevance_medium_second_bounded_relevance_receipt"
            ),
            SECOND_RECEIPT_TYPE,
            second_receipt_type,
            "SECOND_RECEIPT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT",
        )
    )
    checks.append(
        _check(
            "second_receipt_scope_declared",
            bool(second_receipt_scope),
            SECOND_RECEIPT_SCOPE,
            second_receipt_scope,
            "SECOND_RECEIPT_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "second_receipt_scope_inspectable_only",
            second_receipt_scope == SECOND_RECEIPT_SCOPE
            and not _request_flag(request, "second_receipt_scope_not_inspectable_only"),
            SECOND_RECEIPT_SCOPE,
            second_receipt_scope,
            "SECOND_RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
        )
    )
    checks.append(
        _check(
            "second_reception_artifact_preserved",
            bool(facts.get("basis_second_bounded_relevance_reception_artifact"))
            and not _request_flag(request, "second_reception_artifact_missing"),
            "second reception artifact preserved",
            facts.get("basis_second_bounded_relevance_reception_artifact"),
            "SECOND_RECEPTION_ARTIFACT_MISSING",
        )
    )
    identifiers_preserved = (
        facts.get("second_received_signal_id") == DEFAULT_SECOND_RECEIVED_SIGNAL_ID
        and facts.get("second_relevance_basis_id") == DEFAULT_SECOND_RELEVANCE_BASIS_ID
        and facts.get("second_relevance_scope_id") == DEFAULT_SECOND_RELEVANCE_SCOPE_ID
        and facts.get("second_carrier_context_id") == DEFAULT_SECOND_CARRIER_CONTEXT_ID
        and facts.get("second_reception_envelope_id") == DEFAULT_SECOND_RECEPTION_ENVELOPE_ID
    )
    checks.append(
        _check(
            "second_received_identifiers_preserved",
            identifiers_preserved
            and not _request_flag(request, "second_received_identifiers_not_preserved"),
            {
                "second_received_signal_id": DEFAULT_SECOND_RECEIVED_SIGNAL_ID,
                "second_relevance_basis_id": DEFAULT_SECOND_RELEVANCE_BASIS_ID,
                "second_relevance_scope_id": DEFAULT_SECOND_RELEVANCE_SCOPE_ID,
                "second_carrier_context_id": DEFAULT_SECOND_CARRIER_CONTEXT_ID,
                "second_reception_envelope_id": DEFAULT_SECOND_RECEPTION_ENVELOPE_ID,
            },
            {
                "second_received_signal_id": facts.get("second_received_signal_id"),
                "second_relevance_basis_id": facts.get("second_relevance_basis_id"),
                "second_relevance_scope_id": facts.get("second_relevance_scope_id"),
                "second_carrier_context_id": facts.get("second_carrier_context_id"),
                "second_reception_envelope_id": facts.get("second_reception_envelope_id"),
            },
            "SECOND_RECEIVED_IDENTIFIERS_NOT_PRESERVED",
        )
    )
    checks.append(
        _check(
            "second_receipt_does_not_expand_second_reception",
            not _request_flag(request, "second_receipt_expands_second_reception"),
            "second receipt does not expand second reception",
            request.get("second_receipt_expands_second_reception", False),
            "SECOND_RECEIPT_EXPANDS_SECOND_RECEPTION",
        )
    )

    for field_name, block_code in FALSE_REQUEST_BLOCKS:
        checks.append(
            _check(
                f"{field_name}_false",
                not _declared_or_request_flag(request, field_name),
                False,
                _declared_or_request_flag(request, field_name),
                block_code,
            )
        )

    checks.append(
        _check(
            "predecessor_failure_evidence_preserved",
            not (
                _request_flag(request, "predecessor_failure_repaired")
                or _request_flag(request, "predecessor_failure_hidden")
                or _request_flag(request, "predecessor_failure_claimed_passed")
            ),
            "predecessor failure evidence preserved",
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
            "result_level_required_false_non_claims_canonical_false",
            all(value is False for value in _canonical_non_claims().values()),
            "result-level non-claims canonical false",
            _canonical_non_claims(),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _check(
            "required_declared_non_claims_false",
            _declared_non_claims_are_clean(request),
            "declared required non-claims present and false",
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _build_second_bounded_relevance_receipt_object(
    receipt_id: str,
    facts: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "second_receipt_id": receipt_id,
        "second_receipt_type": SECOND_RECEIPT_TYPE,
        "second_receipt_version": RESULT_VERSION,
        "second_receipt_scope": SECOND_RECEIPT_SCOPE,
        "basis_second_bounded_relevance_reception_artifact": facts.get(
            "basis_second_bounded_relevance_reception_artifact"
        ),
        "basis_second_bounded_relevance_reception_outcome": facts.get(
            "basis_second_bounded_relevance_reception_outcome"
        ),
        "basis_second_bounded_relevance_reception_result_version": facts.get(
            "basis_second_bounded_relevance_reception_result_version"
        ),
        "basis_second_bounded_relevance_reception_failed_check_count": facts.get(
            "basis_second_bounded_relevance_reception_failed_check_count"
        ),
        "basis_successor_candidate_admission_artifact": facts.get(
            "basis_successor_candidate_admission_artifact"
        ),
        "basis_successor_reception_request_artifact": facts.get(
            "basis_successor_reception_request_artifact"
        ),
        "basis_index_entry_artifact": facts.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": facts.get("existing_orientation_view_artifact"),
        "existing_source_receipt_artifact": facts.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": facts.get(
            "existing_referenced_reception_artifact"
        ),
        "existing_received_signal_id": facts.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": facts.get("existing_received_relevance_basis_id"),
        "existing_received_relevance_scope_id": facts.get("existing_received_relevance_scope_id"),
        "existing_received_carrier_context_id": facts.get("existing_received_carrier_context_id"),
        "existing_received_reception_envelope_id": facts.get(
            "existing_received_reception_envelope_id"
        ),
        "admitted_successor_candidate_id": facts.get("admitted_successor_candidate_id"),
        "second_received_signal_id": facts.get("second_received_signal_id"),
        "second_relevance_basis_id": facts.get("second_relevance_basis_id"),
        "second_relevance_scope_id": facts.get("second_relevance_scope_id"),
        "second_carrier_context_id": facts.get("second_carrier_context_id"),
        "second_reception_envelope_id": facts.get("second_reception_envelope_id"),
        "second_reception_artifact_preserved": True,
        "second_received_identifiers_preserved": True,
        "second_receipt_does_not_expand_reception": True,
        "second_orientation_view_created": False,
        "second_index_entry_created": False,
        "local_medium_multiplicity_result_created": False,
        "relation_view_created": False,
        "comparison_view_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
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


def _build_statement(
    recorded: bool,
    receipt_object: Mapping[str, Any],
    facts: Mapping[str, Any],
) -> dict[str, bool]:
    if recorded:
        return {key: True for key in ALLOWED_TRUE_RECORDED_FIELDS}
    return {
        "local_relevance_medium_second_bounded_relevance_receipt_recorded": False,
        "basis_second_bounded_relevance_reception_artifact_preserved": bool(
            facts.get("basis_second_bounded_relevance_reception_artifact")
        ),
        "basis_successor_candidate_admission_artifact_preserved": bool(
            facts.get("basis_successor_candidate_admission_artifact")
        ),
        "basis_successor_reception_request_artifact_preserved": bool(
            facts.get("basis_successor_reception_request_artifact")
        ),
        "basis_index_entry_artifact_preserved": bool(facts.get("basis_index_entry_artifact")),
        "existing_orientation_view_artifact_preserved": bool(
            facts.get("existing_orientation_view_artifact")
        ),
        "existing_source_receipt_artifact_preserved": bool(
            facts.get("existing_source_receipt_artifact")
        ),
        "existing_referenced_reception_artifact_preserved": bool(
            facts.get("existing_referenced_reception_artifact")
        ),
        "existing_received_signal_id_preserved": bool(facts.get("existing_received_signal_id")),
        "existing_received_relevance_basis_id_preserved": bool(
            facts.get("existing_received_relevance_basis_id")
        ),
        "existing_received_relevance_scope_id_preserved": bool(
            facts.get("existing_received_relevance_scope_id")
        ),
        "existing_received_carrier_context_id_preserved": bool(
            facts.get("existing_received_carrier_context_id")
        ),
        "existing_received_reception_envelope_id_preserved": bool(
            facts.get("existing_received_reception_envelope_id")
        ),
        "second_received_signal_id_preserved": bool(receipt_object.get("second_received_signal_id")),
        "second_relevance_basis_id_preserved": bool(receipt_object.get("second_relevance_basis_id")),
        "second_relevance_scope_id_preserved": bool(receipt_object.get("second_relevance_scope_id")),
        "second_carrier_context_id_preserved": bool(receipt_object.get("second_carrier_context_id")),
        "second_reception_envelope_id_preserved": bool(
            receipt_object.get("second_reception_envelope_id")
        ),
        "second_receipt_scope_inspectable_only": receipt_object.get("second_receipt_scope")
        == SECOND_RECEIPT_SCOPE,
        "second_receipt_does_not_expand_reception": receipt_object.get(
            "second_receipt_does_not_expand_reception"
        )
        is True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "second_orientation_view_created": False,
        "second_index_entry_created": False,
        "local_medium_multiplicity_result_created": False,
        "relation_view_created": False,
        "comparison_view_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
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
        "operation_permission_created": False,
        "follow_on_work_authorized": False,
    }


def _build_open_items() -> list[str]:
    return [
        "second relevance orientation view",
        "second local relevance orientation index entry",
        "local medium multiplicity result",
        "relation view",
        "comparison view",
        "local relevance orientation index system",
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
        "follow-on work",
    ]


def build_local_relevance_medium_second_bounded_relevance_receipt_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_second_bounded_relevance_receipt_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count, failed_count = _checks_counts(checks)
    metadata = _as_mapping(
        result.get("local_relevance_medium_second_bounded_relevance_receipt_metadata")
    )
    block = _as_mapping(result.get("block"))
    statement = _as_mapping(
        result.get("local_relevance_medium_second_bounded_relevance_receipt_statement")
    )
    receipt_object = _as_mapping(result.get("second_bounded_relevance_receipt_object"))
    question = result.get("declared_local_relevance_medium_second_bounded_relevance_receipt_question")

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "second_receipt_id": receipt_object.get("second_receipt_id")
        or metadata.get("local_relevance_medium_second_bounded_relevance_receipt_id"),
        "question": question,
        "intent": metadata.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("local_relevance_medium_second_bounded_relevance_receipt_version")
        or RESULT_VERSION,
        "resolver_module": metadata.get("resolver_module") or RESOLVER_MODULE,
        "second_receipt_recorded": statement.get(
            "local_relevance_medium_second_bounded_relevance_receipt_recorded", False
        ),
        "basis_second_bounded_relevance_reception_artifact_preserved": statement.get(
            "basis_second_bounded_relevance_reception_artifact_preserved", False
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
        "second_received_signal_id_preserved": statement.get(
            "second_received_signal_id_preserved", False
        ),
        "second_relevance_basis_id_preserved": statement.get(
            "second_relevance_basis_id_preserved", False
        ),
        "second_relevance_scope_id_preserved": statement.get(
            "second_relevance_scope_id_preserved", False
        ),
        "second_carrier_context_id_preserved": statement.get(
            "second_carrier_context_id_preserved", False
        ),
        "second_reception_envelope_id_preserved": statement.get(
            "second_reception_envelope_id_preserved", False
        ),
        "second_receipt_scope_inspectable_only": statement.get(
            "second_receipt_scope_inspectable_only", False
        ),
        "second_receipt_does_not_expand_reception": statement.get(
            "second_receipt_does_not_expand_reception", False
        ),
        "second_receipt_object_summary": {
            "second_receipt_type": receipt_object.get("second_receipt_type"),
            "second_receipt_scope": receipt_object.get("second_receipt_scope"),
            "second_received_signal_id": receipt_object.get("second_received_signal_id"),
            "second_relevance_basis_id": receipt_object.get("second_relevance_basis_id"),
            "second_relevance_scope_id": receipt_object.get("second_relevance_scope_id"),
            "second_carrier_context_id": receipt_object.get("second_carrier_context_id"),
            "second_reception_envelope_id": receipt_object.get(
                "second_reception_envelope_id"
            ),
        },
        "second_orientation_view_and_second_index_entry_not_created": True,
        "local_medium_multiplicity_result_not_created": True,
        "relation_view_and_comparison_view_not_created": True,
        "repeated_reception_permission_arbitrary_reception_feed_not_created": True,
        "index_system_registry_search_ranking_not_created": True,
        "source_authority_currentness_truth_action_synchronization_participation_runtime_not_created": True,
        "public_api_participant_facing_interface_distributed_network_not_created": True,
        "operation_permission_follow_on_not_created": True,
        "key_non_claims": _canonical_non_claims(),
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false", False
        ),
    }


def _assemble_result(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    passed_count, failed_count = _checks_counts(checks)
    requested_outcome = request.get("requested_local_relevance_medium_second_bounded_relevance_receipt_outcome")
    intent = request.get("local_relevance_medium_second_bounded_relevance_receipt_intent")

    if failed_count:
        outcome = OUTCOME_BLOCKED
    elif requested_outcome in OUTCOME_FAMILY and requested_outcome != OUTCOME_RECORDED:
        outcome = requested_outcome
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif request.get("additional_basis_context"):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED and failed_count == 0
    receipt_id = str(
        request.get("local_relevance_medium_second_bounded_relevance_receipt_id")
        or DEFAULT_SECOND_RECEIPT_ID
    )
    receipt_object = (
        _build_second_bounded_relevance_receipt_object(receipt_id, facts) if recorded else {}
    )
    statement = _build_statement(recorded, receipt_object, facts)
    first_failed_code = _first_failed_code(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": first_failed_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": first_failed_code if outcome == OUTCOME_BLOCKED else None,
        "reason": _sanitize(request.get("block_reason"))
        if outcome == OUTCOME_BLOCKED and request.get("block_reason")
        else (
            "local relevance medium second bounded relevance receipt blocked"
            if outcome == OUTCOME_BLOCKED
            else None
        ),
    }

    result: dict[str, Any] = {
        "local_relevance_medium_second_bounded_relevance_receipt_metadata": {
            "local_relevance_medium_second_bounded_relevance_receipt_id": receipt_id,
            "local_relevance_medium_second_bounded_relevance_receipt_type": SECOND_RECEIPT_TYPE,
            "local_relevance_medium_second_bounded_relevance_receipt_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "intent": intent,
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
        },
        "declared_local_relevance_medium_second_bounded_relevance_receipt_question": _sanitize(
            request.get("local_relevance_medium_second_bounded_relevance_receipt_question")
        ),
        "selected_second_bounded_relevance_reception_artifact_basis": {
            "selected_second_bounded_relevance_reception_artifact": _sanitize(
                request.get("selected_second_bounded_relevance_reception_artifact")
            ),
            "basis_second_bounded_relevance_reception_artifact": _sanitize(
                facts.get("basis_second_bounded_relevance_reception_artifact")
            ),
            "basis_second_bounded_relevance_reception_outcome": facts.get(
                "basis_second_bounded_relevance_reception_outcome"
            ),
            "basis_second_bounded_relevance_reception_result_version": facts.get(
                "basis_second_bounded_relevance_reception_result_version"
            ),
            "basis_second_bounded_relevance_reception_failed_check_count": facts.get(
                "basis_second_bounded_relevance_reception_failed_check_count"
            ),
        },
        "second_bounded_relevance_receipt_object": _sanitize(receipt_object),
        "local_relevance_medium_second_bounded_relevance_receipt_checks": _sanitize(checks),
        "local_relevance_medium_second_bounded_relevance_receipt_statement": statement,
        "local_relevance_medium_second_bounded_relevance_receipt_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context") or []),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis") or []),
        "what_remains_open": _build_open_items(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_second_bounded_relevance_receipt_summary"] = (
        build_local_relevance_medium_second_bounded_relevance_receipt_v0_min_summary(result)
    )
    return result


def resolve_local_relevance_medium_second_bounded_relevance_receipt_v0_min(
    declared_local_relevance_medium_second_bounded_relevance_receipt: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_second_bounded_relevance_receipt is None:
        request = build_declared_local_relevance_medium_second_bounded_relevance_receipt_v0_min_request()
    elif isinstance(declared_local_relevance_medium_second_bounded_relevance_receipt, Mapping):
        request = copy.deepcopy(dict(declared_local_relevance_medium_second_bounded_relevance_receipt))
    else:
        request = {
            "local_relevance_medium_second_bounded_relevance_receipt_id": DEFAULT_SECOND_RECEIPT_ID,
            "local_relevance_medium_second_bounded_relevance_receipt_question": None,
            "local_relevance_medium_second_bounded_relevance_receipt_intent": None,
            "selected_second_bounded_relevance_reception_artifact": None,
            "second_receipt_scope": None,
            "second_receipt_type": None,
            "declared_non_claims": {},
            "block_reason": "declared request was not a mapping",
        }
        facts = _extract_second_reception_facts(None, None)
        checks = [
            _check(
                "declared_request_mapping",
                False,
                "mapping request",
                type(declared_local_relevance_medium_second_bounded_relevance_receipt).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
            )
        ]
        checks.extend(_build_checks(request, None, None, facts))
        return _assemble_result(request, facts, checks)

    selected_path = request.get("selected_second_bounded_relevance_reception_artifact")
    if _request_flag(request, "selected_second_bounded_relevance_reception_artifact_missing"):
        artifact, read_error = None, "SECOND_BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING"
    else:
        artifact, read_error = _read_json_object(selected_path)
    facts = _extract_second_reception_facts(artifact, str(selected_path) if selected_path else None)
    checks = _build_checks(request, artifact, read_error, facts)
    return _assemble_result(request, facts, checks)


def resolve_local_relevance_medium_second_bounded_relevance_receipt_v0_min_from_path(
    declared_local_relevance_medium_second_bounded_relevance_receipt_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_local_relevance_medium_second_bounded_relevance_receipt_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise LocalRelevanceMediumSecondBoundedRelevanceReceiptV0MinError(
            "declared local relevance medium second bounded relevance receipt request unreadable"
        ) from exc
    if not isinstance(loaded, Mapping):
        request = {
            "local_relevance_medium_second_bounded_relevance_receipt_id": DEFAULT_SECOND_RECEIPT_ID,
            "local_relevance_medium_second_bounded_relevance_receipt_question": None,
            "local_relevance_medium_second_bounded_relevance_receipt_intent": None,
            "selected_second_bounded_relevance_reception_artifact": None,
            "second_receipt_scope": None,
            "second_receipt_type": None,
            "declared_non_claims": {},
            "block_reason": "declared request JSON was not an object",
        }
        facts = _extract_second_reception_facts(None, None)
        checks = [
            _check(
                "declared_request_json_object",
                False,
                "JSON object request",
                type(loaded).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
            )
        ]
        checks.extend(_build_checks(request, None, None, facts))
        return _assemble_result(request, facts, checks)
    return resolve_local_relevance_medium_second_bounded_relevance_receipt_v0_min(loaded)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_local_relevance_medium_second_bounded_relevance_receipt_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    result_copy = copy.deepcopy(dict(result))
    metadata = _as_mapping(
        result_copy.get("local_relevance_medium_second_bounded_relevance_receipt_metadata")
    )
    receipt_id = str(
        metadata.get("local_relevance_medium_second_bounded_relevance_receipt_id")
        or DEFAULT_SECOND_RECEIPT_ID
    )
    if output_path is None:
        target = OUTPUT_ROOT / (
            f"{receipt_id}__local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
        )
    else:
        target = Path(output_path)
        if target.is_dir() or str(output_path).endswith("/"):
            target = target / (
                f"{receipt_id}__local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
            )
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_output_path(target)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(result_copy), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_declared_local_relevance_medium_second_bounded_relevance_receipt_v0_min_request(
    local_relevance_medium_second_bounded_relevance_receipt_id: str = DEFAULT_SECOND_RECEIPT_ID,
    selected_second_bounded_relevance_reception_artifact: Path | str = DEFAULT_SECOND_RECEPTION_ARTIFACT,
    second_receipt_type: str = SECOND_RECEIPT_TYPE,
    second_receipt_scope: str = SECOND_RECEIPT_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(copy.deepcopy(dict(declared_non_claims)))

    request: dict[str, Any] = {
        "local_relevance_medium_second_bounded_relevance_receipt_id": (
            local_relevance_medium_second_bounded_relevance_receipt_id
        ),
        "local_relevance_medium_second_bounded_relevance_receipt_question": (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION, "
            "may one LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT be recorded "
            "that records one inspectable receipt object for the second bounded relevance "
            "reception, preserving the second received identifiers without creating "
            "orientation, index, multiplicity, relation, comparison, permission, feed, "
            "source, authority, runtime, interface, distributed behavior, operation "
            "permission, or follow-on work?"
        ),
        "local_relevance_medium_second_bounded_relevance_receipt_intent": intent,
        "selected_second_bounded_relevance_reception_artifact": str(
            selected_second_bounded_relevance_reception_artifact
        ),
        "second_receipt_scope": second_receipt_scope,
        "second_receipt_type": second_receipt_type,
        "declared_non_claims": non_claims,
    }
    for key, value in overrides.items():
        request[key] = value
    return request
