"""Resolve one local relevance medium relation view.

This resolver reads one clean local relevance medium multiplicity result
artifact and records one small relation-readable local view.  The view preserves
the multiplicity result basis, first and second local locator artifacts, first
and second orientation/receipt/reception artifacts, successor lineage, and
received identifiers.  It records bounded co-presence only.  It does not
compare, rank, search, index, authorize reception, create source transfer or
source receipt, create authority/currentness/truth/action/synchronization,
create runtime/API/distributed behavior, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumRelationViewV0MinError(Exception):
    """Bounded error for relation-view resolver path loading."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_relation_view_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"
)
DEFAULT_MULTIPLICITY_RESULT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min/"
    "local_relevance_medium_multiplicity_result_reference_review_001__"
    "local_relevance_medium_multiplicity_result_v0_min_result.json"
)

RELATION_VIEW_TYPE = "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
RELATION_VIEW_SCOPE = "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY"
RELATION_FRAME = "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY"
MULTIPLICITY_RESULT_TYPE = "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
MULTIPLICITY_RESULT_SCOPE = "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY"
MULTIPLICITY_RESULT_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED"
)
DEFAULT_RELATION_VIEW_ID = "local_relevance_medium_relation_view_001"

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

SUPPORTED_RELATION_VIEW_SCOPE_VALUES = (RELATION_VIEW_SCOPE,)
SUPPORTED_RELATION_VIEW_TYPE_VALUES = (RELATION_VIEW_TYPE,)
SUPPORTED_RELATION_FRAME_VALUES = (RELATION_FRAME,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT, may one "
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW be recorded that makes bounded "
    "relation-readable co-presence available for exactly two locally "
    "discoverable orientation objects, preserving multiplicity result basis, "
    "first and second locator artifacts, first and second orientation artifacts, "
    "and first and second received identifiers, without creating comparison "
    "view, index system, registry, search, ranking, repeated reception "
    "permission, arbitrary reception, feed, source transfer, source receipt, "
    "authority, currentness, truth, action, synchronization, participation "
    "authorization, participant role, runtime permission, public API, "
    "participant-facing interface, distributed network behavior, operation "
    "permission, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "comparison_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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
    "artifact_existence_treated_as_relation_view_authority",
    "latest_file_posture_treated_as_relation_view_authority",
    "repo_local_availability_treated_as_relation_view_authority",
    "hidden_repo_state_used_as_relation_view_content",
    "hidden_repo_state_used_as_relation_view_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_relation_view_recorded",
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
    "relation_view_scope_local_only",
    "relation_frame_bounded_co_presence_only",
    "relation_pair_count_is_one",
    "relation_readable_co_presence_recorded",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BLOCK_REQUESTED",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_PATH_MISSING",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_UNREADABLE",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_OBJECT_MISSING",
    "MULTIPLICITY_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
    "MULTIPLICITY_RESULT_SCOPE_NOT_TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
    "MULTIPLICITY_COUNT_NOT_TWO",
    "FIRST_LOCATOR_ARTIFACT_MISSING",
    "SECOND_LOCATOR_ARTIFACT_MISSING",
    "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "FIRST_RECEIPT_ARTIFACT_MISSING",
    "SECOND_RECEIPT_ARTIFACT_MISSING",
    "FIRST_RECEPTION_ARTIFACT_MISSING",
    "SECOND_RECEPTION_ARTIFACT_MISSING",
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
    "RELATION_VIEW_SCOPE_MISSING",
    "RELATION_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    "RELATION_VIEW_TYPE_MISSING",
    "RELATION_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
    "RELATION_FRAME_MISSING",
    "RELATION_FRAME_NOT_BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
    "RELATION_PAIR_COUNT_NOT_ONE",
    "RELATION_READABLE_CO_PRESENCE_NOT_RECORDED",
    "RELATION_VIEW_NOT_RECORDED",
    "COMPARISON_VIEW_CREATED",
    "INDEX_SYSTEM_CREATED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "RANKING_SURFACE_CREATED",
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
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_RELATION_VIEW_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RELATION_VIEW_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RELATION_VIEW_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RELATION_VIEW_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RELATION_VIEW_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUEST_UNREADABLE",
)

_FALSE_POSTURE_BLOCK_CODES = {
    "comparison_view_created": "COMPARISON_VIEW_CREATED",
    "index_system_created": "INDEX_SYSTEM_CREATED",
    "registry_created": "REGISTRY_CREATED",
    "search_surface_created": "SEARCH_SURFACE_CREATED",
    "ranking_surface_created": "RANKING_SURFACE_CREATED",
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
    "artifact_existence_treated_as_relation_view_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_RELATION_VIEW_AUTHORITY"
    ),
    "latest_file_posture_treated_as_relation_view_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_RELATION_VIEW_AUTHORITY"
    ),
    "repo_local_availability_treated_as_relation_view_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RELATION_VIEW_AUTHORITY"
    ),
    "hidden_repo_state_used_as_relation_view_content": (
        "HIDDEN_REPO_STATE_USED_AS_RELATION_VIEW_CONTENT"
    ),
    "hidden_repo_state_used_as_relation_view_authority": (
        "HIDDEN_REPO_STATE_USED_AS_RELATION_VIEW_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
    "predecessor_failure_repaired": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

_SENSITIVE_CONTENT_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "full_body",
        "artifact_body",
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

_HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BODY_MUST_NOT_RETURN",
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

_OFFICIAL_STRINGS = frozenset(
    (
        RESULT_VERSION,
        RESOLVER_MODULE,
        RELATION_VIEW_TYPE,
        RELATION_VIEW_SCOPE,
        RELATION_FRAME,
        MULTIPLICITY_RESULT_TYPE,
        MULTIPLICITY_RESULT_SCOPE,
        MULTIPLICITY_RESULT_RECORDED_OUTCOME,
        DEFAULT_RELATION_VIEW_ID,
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
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
    )
    + OUTCOME_FAMILY
    + BLOCK_CODES
    + REQUIRED_FALSE_NON_CLAIMS
    + ALLOWED_TRUE_RECORDED_FIELDS
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    normalized = str(key).lower()
    return normalized in _SENSITIVE_CONTENT_KEYS or normalized.endswith("_body")


def _sanitize_value(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_RAW_CONTENT]"
    if isinstance(value, str):
        if value in _OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in _HOSTILE_SENTINELS):
            return "[REDACTED_RAW_CONTENT]"
        return value
    if isinstance(value, Mapping):
        return {
            str(item_key): _sanitize_value(item_value, str(item_key))
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_value(item) for item in value]
    return value


def _mapping_or_empty(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and value == "":
        return False
    return True


def _first_present(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _to_int(value: Any) -> int | None:
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


def _request_flag(request: Mapping[str, Any], key: str) -> bool:
    return request.get(key) is True


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    record = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_value(expected_posture),
        "actual_posture": _sanitize_value(actual_posture),
    }
    if not passed:
        record["block_code"] = block_code
        record["failure_code"] = block_code
    return record


def _check_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is False)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None, str | None]:
    if not _present(path_value):
        return (
            None,
            None,
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_PATH_MISSING",
        )
    path = Path(str(path_value))
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return (
            None,
            str(path),
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_UNREADABLE",
        )
    if not isinstance(loaded, Mapping):
        return (
            None,
            str(path),
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_NOT_JSON_OBJECT",
        )
    return dict(loaded), str(path), None


def _failed_check_count_from_artifact(artifact: Mapping[str, Any]) -> int | None:
    metadata = _mapping_or_empty(
        artifact.get("local_relevance_medium_multiplicity_result_metadata")
    )
    summary = _mapping_or_empty(
        artifact.get("local_relevance_medium_multiplicity_result_summary")
    )
    direct = _first_present(
        summary.get("failed_check_count"),
        metadata.get("failed_check_count"),
        artifact.get("failed_check_count"),
    )
    direct_count = _to_int(direct)
    if direct_count is not None:
        return direct_count
    checks = artifact.get("local_relevance_medium_multiplicity_result_checks")
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is False
        )
    return None


def _extract_multiplicity_result_facts(
    artifact: Mapping[str, Any] | None,
    artifact_path: str | None,
) -> dict[str, Any]:
    if artifact is None:
        return {
            "basis_local_relevance_medium_multiplicity_result_artifact": artifact_path,
            "local_relevance_medium_multiplicity_result_object": {},
        }
    metadata = _mapping_or_empty(
        artifact.get("local_relevance_medium_multiplicity_result_metadata")
    )
    summary = _mapping_or_empty(
        artifact.get("local_relevance_medium_multiplicity_result_summary")
    )
    multiplicity_result = _mapping_or_empty(
        artifact.get("local_relevance_medium_multiplicity_result")
    )
    return {
        "basis_local_relevance_medium_multiplicity_result_artifact": artifact_path,
        "basis_local_relevance_medium_multiplicity_result_outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
            metadata.get("outcome"),
        ),
        "basis_local_relevance_medium_multiplicity_result_result_version": (
            _first_present(
                metadata.get("local_relevance_medium_multiplicity_result_version"),
                metadata.get("result_version"),
                summary.get("result_version"),
                artifact.get("result_version"),
                multiplicity_result.get("multiplicity_result_version"),
            )
        ),
        "basis_local_relevance_medium_multiplicity_result_failed_check_count": (
            _failed_check_count_from_artifact(artifact)
        ),
        "local_relevance_medium_multiplicity_result_object": dict(multiplicity_result),
        "multiplicity_result_type": multiplicity_result.get("multiplicity_result_type"),
        "multiplicity_result_scope": multiplicity_result.get("multiplicity_result_scope"),
        "basis_first_local_relevance_orientation_index_entry_artifact": (
            multiplicity_result.get(
                "basis_first_local_relevance_orientation_index_entry_artifact"
            )
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact": (
            multiplicity_result.get(
                "basis_second_local_relevance_orientation_index_entry_artifact"
            )
        ),
        "first_orientation_view_artifact": multiplicity_result.get(
            "first_orientation_view_artifact"
        ),
        "second_orientation_view_artifact": multiplicity_result.get(
            "second_orientation_view_artifact"
        ),
        "first_receipt_artifact": multiplicity_result.get("first_receipt_artifact"),
        "second_receipt_artifact": multiplicity_result.get("second_receipt_artifact"),
        "first_reception_artifact": multiplicity_result.get("first_reception_artifact"),
        "second_reception_artifact": multiplicity_result.get(
            "second_reception_artifact"
        ),
        "successor_candidate_admission_artifact": multiplicity_result.get(
            "successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": multiplicity_result.get(
            "successor_reception_request_artifact"
        ),
        "first_received_signal_id": multiplicity_result.get("first_received_signal_id"),
        "second_received_signal_id": multiplicity_result.get(
            "second_received_signal_id"
        ),
        "first_relevance_basis_id": multiplicity_result.get("first_relevance_basis_id"),
        "second_relevance_basis_id": multiplicity_result.get(
            "second_relevance_basis_id"
        ),
        "first_relevance_scope_id": multiplicity_result.get("first_relevance_scope_id"),
        "second_relevance_scope_id": multiplicity_result.get(
            "second_relevance_scope_id"
        ),
        "first_carrier_context_id": multiplicity_result.get(
            "first_carrier_context_id"
        ),
        "second_carrier_context_id": multiplicity_result.get(
            "second_carrier_context_id"
        ),
        "first_reception_envelope_id": multiplicity_result.get(
            "first_reception_envelope_id"
        ),
        "second_reception_envelope_id": multiplicity_result.get(
            "second_reception_envelope_id"
        ),
        "multiplicity_count": multiplicity_result.get("multiplicity_count"),
        "two_local_orientation_locators_present": multiplicity_result.get(
            "two_local_orientation_locators_present"
        ),
        "first_and_second_signals_distinct": multiplicity_result.get(
            "first_and_second_signals_distinct"
        ),
        "basis_lineage_preserved": multiplicity_result.get("basis_lineage_preserved"),
    }


def _declared_non_claims_clean(request: Mapping[str, Any]) -> tuple[bool, dict[str, Any]]:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False, {"declared_non_claims": "missing_or_not_mapping"}
    problems: dict[str, Any] = {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared:
            problems[key] = "missing"
        elif declared.get(key) is not False:
            problems[key] = declared.get(key)
    return not problems, problems


def _build_checks(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    artifact_read_code: str | None,
    request_failure_code: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if request_failure_code is not None:
        checks.append(
            _check(
                "declared local relevance medium relation view request readable",
                False,
                "readable mapping request",
                request_failure_code,
                request_failure_code,
            )
        )

    question = request.get("local_relevance_medium_relation_view_question")
    intent = request.get("local_relevance_medium_relation_view_intent")
    selected_path = request.get("selected_local_relevance_medium_multiplicity_result_artifact")
    relation_view_type = request.get("relation_view_type")
    relation_view_scope = request.get("relation_view_scope")
    relation_frame = request.get("relation_frame")

    checks.extend(
        [
            _check(
                "relation view question declared",
                _present(question),
                "declared local relevance medium relation view question",
                question,
                "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_QUESTION_UNDECLARED",
            ),
            _check(
                "relation view intent supported",
                intent in SUPPORTED_INTENTS,
                SUPPORTED_INTENTS,
                intent,
                "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_INTENT_UNSUPPORTED",
            ),
            _check(
                "relation view block intent not requested",
                intent != INTENT_BLOCK,
                "not BLOCK_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
                intent,
                "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BLOCK_REQUESTED",
            ),
            _check(
                "selected local relevance medium multiplicity result artifact path declared",
                _present(selected_path)
                and not _request_flag(
                    request,
                    "selected_local_relevance_medium_multiplicity_result_artifact_missing",
                ),
                "selected multiplicity result artifact path",
                selected_path,
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_PATH_MISSING",
            ),
            _check(
                "selected local relevance medium multiplicity result artifact readable JSON",
                artifact_read_code
                not in {
                    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_PATH_MISSING",
                    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_UNREADABLE",
                },
                "readable JSON artifact",
                artifact_read_code or "readable JSON artifact",
                artifact_read_code
                or "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_UNREADABLE",
            ),
            _check(
                "selected local relevance medium multiplicity result artifact JSON object",
                artifact_read_code
                != "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_NOT_JSON_OBJECT",
                "JSON object artifact",
                artifact_read_code or "JSON object artifact",
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_NOT_JSON_OBJECT",
            ),
            _check(
                "local relevance medium multiplicity result artifact outcome recorded",
                facts.get("basis_local_relevance_medium_multiplicity_result_outcome")
                == MULTIPLICITY_RESULT_RECORDED_OUTCOME
                and not _request_flag(
                    request,
                    "local_relevance_medium_multiplicity_result_artifact_not_recorded",
                ),
                MULTIPLICITY_RESULT_RECORDED_OUTCOME,
                facts.get("basis_local_relevance_medium_multiplicity_result_outcome"),
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_NOT_RECORDED",
            ),
            _check(
                "local relevance medium multiplicity result artifact result version 0.1.0",
                facts.get("basis_local_relevance_medium_multiplicity_result_result_version")
                == RESULT_VERSION
                and not _request_flag(
                    request,
                    "local_relevance_medium_multiplicity_result_artifact_version_not_0_1_0",
                ),
                RESULT_VERSION,
                facts.get("basis_local_relevance_medium_multiplicity_result_result_version"),
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
            ),
            _check(
                "local relevance medium multiplicity result artifact failed check count zero",
                facts.get("basis_local_relevance_medium_multiplicity_result_failed_check_count")
                == 0
                and not _request_flag(
                    request,
                    "local_relevance_medium_multiplicity_result_artifact_failed_checks_present",
                ),
                0,
                facts.get("basis_local_relevance_medium_multiplicity_result_failed_check_count"),
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "local relevance medium multiplicity result object present",
                bool(facts.get("local_relevance_medium_multiplicity_result_object"))
                and not _request_flag(
                    request,
                    "local_relevance_medium_multiplicity_result_object_missing",
                ),
                "local relevance medium multiplicity result object present",
                bool(facts.get("local_relevance_medium_multiplicity_result_object")),
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_OBJECT_MISSING",
            ),
            _check(
                "multiplicity result type exact",
                facts.get("multiplicity_result_type") == MULTIPLICITY_RESULT_TYPE
                and not _request_flag(
                    request,
                    "multiplicity_result_type_not_local_relevance_medium_multiplicity_result",
                ),
                MULTIPLICITY_RESULT_TYPE,
                facts.get("multiplicity_result_type"),
                "MULTIPLICITY_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
            ),
            _check(
                "multiplicity result scope two local locators only",
                facts.get("multiplicity_result_scope") == MULTIPLICITY_RESULT_SCOPE
                and not _request_flag(
                    request,
                    "multiplicity_result_scope_not_two_local_orientation_locators_only",
                ),
                MULTIPLICITY_RESULT_SCOPE,
                facts.get("multiplicity_result_scope"),
                "MULTIPLICITY_RESULT_SCOPE_NOT_TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
            ),
            _check(
                "multiplicity count exactly two",
                facts.get("multiplicity_count") == 2
                and not _request_flag(request, "multiplicity_count_not_two"),
                2,
                facts.get("multiplicity_count"),
                "MULTIPLICITY_COUNT_NOT_TWO",
            ),
        ]
    )

    presence_checks = (
        (
            "first locator artifact preserved",
            "basis_first_local_relevance_orientation_index_entry_artifact",
            "first_locator_artifact_missing",
            "FIRST_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            "second locator artifact preserved",
            "basis_second_local_relevance_orientation_index_entry_artifact",
            "second_locator_artifact_missing",
            "SECOND_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            "first orientation view artifact preserved",
            "first_orientation_view_artifact",
            "first_orientation_view_artifact_missing",
            "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "second orientation view artifact preserved",
            "second_orientation_view_artifact",
            "second_orientation_view_artifact_missing",
            "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "first receipt artifact preserved",
            "first_receipt_artifact",
            "first_receipt_artifact_missing",
            "FIRST_RECEIPT_ARTIFACT_MISSING",
        ),
        (
            "second receipt artifact preserved",
            "second_receipt_artifact",
            "second_receipt_artifact_missing",
            "SECOND_RECEIPT_ARTIFACT_MISSING",
        ),
        (
            "first reception artifact preserved",
            "first_reception_artifact",
            "first_reception_artifact_missing",
            "FIRST_RECEPTION_ARTIFACT_MISSING",
        ),
        (
            "second reception artifact preserved",
            "second_reception_artifact",
            "second_reception_artifact_missing",
            "SECOND_RECEPTION_ARTIFACT_MISSING",
        ),
    )
    for check_name, fact_key, flag_key, code in presence_checks:
        checks.append(
            _check(
                check_name,
                _present(facts.get(fact_key)) and not _request_flag(request, flag_key),
                "artifact path preserved",
                facts.get(fact_key),
                code,
            )
        )

    exact_identifier_checks = (
        (
            "first received signal id preserved",
            "first_received_signal_id",
            FIRST_RECEIVED_SIGNAL_ID,
            "first_received_signal_id_missing",
            "FIRST_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "second received signal id preserved",
            "second_received_signal_id",
            SECOND_RECEIVED_SIGNAL_ID,
            "second_received_signal_id_missing",
            "SECOND_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "first relevance basis id preserved",
            "first_relevance_basis_id",
            FIRST_RELEVANCE_BASIS_ID,
            "first_relevance_basis_id_missing",
            "FIRST_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "second relevance basis id preserved",
            "second_relevance_basis_id",
            SECOND_RELEVANCE_BASIS_ID,
            "second_relevance_basis_id_missing",
            "SECOND_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "first relevance scope id preserved",
            "first_relevance_scope_id",
            FIRST_RELEVANCE_SCOPE_ID,
            "first_relevance_scope_id_missing",
            "FIRST_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "second relevance scope id preserved",
            "second_relevance_scope_id",
            SECOND_RELEVANCE_SCOPE_ID,
            "second_relevance_scope_id_missing",
            "SECOND_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "first carrier context id preserved",
            "first_carrier_context_id",
            FIRST_CARRIER_CONTEXT_ID,
            "first_carrier_context_id_missing",
            "FIRST_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "second carrier context id preserved",
            "second_carrier_context_id",
            SECOND_CARRIER_CONTEXT_ID,
            "second_carrier_context_id_missing",
            "SECOND_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "first reception envelope id preserved",
            "first_reception_envelope_id",
            FIRST_RECEPTION_ENVELOPE_ID,
            "first_reception_envelope_id_missing",
            "FIRST_RECEPTION_ENVELOPE_ID_MISSING",
        ),
        (
            "second reception envelope id preserved",
            "second_reception_envelope_id",
            SECOND_RECEPTION_ENVELOPE_ID,
            "second_reception_envelope_id_missing",
            "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
        ),
    )
    for check_name, fact_key, expected, flag_key, code in exact_identifier_checks:
        checks.append(
            _check(
                check_name,
                facts.get(fact_key) == expected and not _request_flag(request, flag_key),
                expected,
                facts.get(fact_key),
                code,
            )
        )

    checks.extend(
        [
            _check(
                "first and second received signal ids distinct",
                facts.get("first_received_signal_id")
                != facts.get("second_received_signal_id")
                and facts.get("first_and_second_signals_distinct") is True
                and not _request_flag(
                    request, "first_and_second_received_signal_ids_not_distinct"
                ),
                "distinct first and second received signal ids",
                {
                    "first_received_signal_id": facts.get("first_received_signal_id"),
                    "second_received_signal_id": facts.get("second_received_signal_id"),
                    "first_and_second_signals_distinct": facts.get(
                        "first_and_second_signals_distinct"
                    ),
                },
                "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
            ),
            _check(
                "relation view type declared",
                _present(relation_view_type),
                RELATION_VIEW_TYPE,
                relation_view_type,
                "RELATION_VIEW_TYPE_MISSING",
            ),
            _check(
                "relation view type exact",
                relation_view_type == RELATION_VIEW_TYPE
                and not _request_flag(
                    request, "relation_view_type_not_local_relevance_medium_relation_view"
                ),
                RELATION_VIEW_TYPE,
                relation_view_type,
                "RELATION_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
            ),
            _check(
                "relation view scope declared",
                _present(relation_view_scope),
                RELATION_VIEW_SCOPE,
                relation_view_scope,
                "RELATION_VIEW_SCOPE_MISSING",
            ),
            _check(
                "relation view scope two local orientation objects only",
                relation_view_scope == RELATION_VIEW_SCOPE
                and not _request_flag(
                    request,
                    "relation_view_scope_not_two_local_orientation_objects_only",
                ),
                RELATION_VIEW_SCOPE,
                relation_view_scope,
                "RELATION_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
            ),
            _check(
                "relation frame declared",
                _present(relation_frame),
                RELATION_FRAME,
                relation_frame,
                "RELATION_FRAME_MISSING",
            ),
            _check(
                "relation frame bounded co-presence only",
                relation_frame == RELATION_FRAME
                and not _request_flag(
                    request,
                    "relation_frame_not_bounded_co_present_local_orientation_objects_only",
                ),
                RELATION_FRAME,
                relation_frame,
                "RELATION_FRAME_NOT_BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
            ),
            _check(
                "relation pair count exactly one",
                request.get("relation_pair_count", 1) == 1
                and not _request_flag(request, "relation_pair_count_not_one"),
                1,
                request.get("relation_pair_count", 1),
                "RELATION_PAIR_COUNT_NOT_ONE",
            ),
            _check(
                "relation-readable co-presence recorded",
                request.get("relation_readable_co_presence_recorded", True) is True
                and not _request_flag(
                    request, "relation_readable_co_presence_not_recorded"
                ),
                True,
                request.get("relation_readable_co_presence_recorded", True),
                "RELATION_READABLE_CO_PRESENCE_NOT_RECORDED",
            ),
            _check(
                "relation view recorded",
                request.get("relation_view_recorded", True) is True
                and not _request_flag(request, "relation_view_not_recorded"),
                True,
                request.get("relation_view_recorded", True),
                "RELATION_VIEW_NOT_RECORDED",
            ),
        ]
    )

    for flag_key, code in _FALSE_POSTURE_BLOCK_CODES.items():
        checks.append(
            _check(
                f"{flag_key} false",
                not _request_flag(request, flag_key),
                False,
                request.get(flag_key, False),
                code,
            )
        )

    declared_non_claims_clean, declared_non_claim_problems = _declared_non_claims_clean(
        request
    )
    checks.extend(
        [
            _check(
                "predecessor failure evidence preserved",
                not (
                    _request_flag(request, "predecessor_failure_repaired")
                    or _request_flag(request, "predecessor_failure_hidden")
                    or _request_flag(request, "predecessor_failure_claimed_passed")
                ),
                "predecessor failure evidence preserved",
                {
                    "predecessor_failure_repaired": request.get(
                        "predecessor_failure_repaired", False
                    ),
                    "predecessor_failure_hidden": request.get(
                        "predecessor_failure_hidden", False
                    ),
                    "predecessor_failure_claimed_passed": request.get(
                        "predecessor_failure_claimed_passed", False
                    ),
                },
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            _check(
                "result-level required false non-claims canonical false",
                all(value is False for value in _canonical_non_claims().values()),
                "all result-level non-claims false",
                _canonical_non_claims(),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            _check(
                "required non-claims false",
                declared_non_claims_clean,
                "declared required non-claims all false bool",
                declared_non_claim_problems or "all false",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
    return checks


def _build_relation_view(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
) -> dict[str, Any]:
    relation_view = {
        "relation_view_id": _first_present(
            request.get("local_relevance_medium_relation_view_id"),
            DEFAULT_RELATION_VIEW_ID,
        ),
        "relation_view_type": RELATION_VIEW_TYPE,
        "relation_view_version": RESULT_VERSION,
        "relation_view_scope": RELATION_VIEW_SCOPE,
        "relation_frame": RELATION_FRAME,
        "basis_local_relevance_medium_multiplicity_result_artifact": facts.get(
            "basis_local_relevance_medium_multiplicity_result_artifact"
        ),
        "basis_local_relevance_medium_multiplicity_result_outcome": facts.get(
            "basis_local_relevance_medium_multiplicity_result_outcome"
        ),
        "basis_local_relevance_medium_multiplicity_result_result_version": facts.get(
            "basis_local_relevance_medium_multiplicity_result_result_version"
        ),
        "basis_local_relevance_medium_multiplicity_result_failed_check_count": facts.get(
            "basis_local_relevance_medium_multiplicity_result_failed_check_count"
        ),
        "basis_first_local_relevance_orientation_index_entry_artifact": facts.get(
            "basis_first_local_relevance_orientation_index_entry_artifact"
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact": facts.get(
            "basis_second_local_relevance_orientation_index_entry_artifact"
        ),
        "first_orientation_view_artifact": facts.get("first_orientation_view_artifact"),
        "second_orientation_view_artifact": facts.get(
            "second_orientation_view_artifact"
        ),
        "first_receipt_artifact": facts.get("first_receipt_artifact"),
        "second_receipt_artifact": facts.get("second_receipt_artifact"),
        "first_reception_artifact": facts.get("first_reception_artifact"),
        "second_reception_artifact": facts.get("second_reception_artifact"),
        "successor_candidate_admission_artifact": facts.get(
            "successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": facts.get(
            "successor_reception_request_artifact"
        ),
        "first_received_signal_id": FIRST_RECEIVED_SIGNAL_ID,
        "second_received_signal_id": SECOND_RECEIVED_SIGNAL_ID,
        "first_relevance_basis_id": FIRST_RELEVANCE_BASIS_ID,
        "second_relevance_basis_id": SECOND_RELEVANCE_BASIS_ID,
        "first_relevance_scope_id": FIRST_RELEVANCE_SCOPE_ID,
        "second_relevance_scope_id": SECOND_RELEVANCE_SCOPE_ID,
        "first_carrier_context_id": FIRST_CARRIER_CONTEXT_ID,
        "second_carrier_context_id": SECOND_CARRIER_CONTEXT_ID,
        "first_reception_envelope_id": FIRST_RECEPTION_ENVELOPE_ID,
        "second_reception_envelope_id": SECOND_RECEPTION_ENVELOPE_ID,
        "multiplicity_count": 2,
        "relation_pair_count": 1,
        "two_local_orientation_objects_preserved": True,
        "first_and_second_signals_distinct": True,
        "relation_readable_co_presence_recorded": True,
        "relation_view_recorded": True,
        "comparison_view_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
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
    return _sanitize_value(relation_view)


def _build_statement(recorded: bool) -> dict[str, bool]:
    statement = {field: bool(recorded) for field in ALLOWED_TRUE_RECORDED_FIELDS}
    statement["result_level_non_claims_canonical_false"] = True
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
        "comparison_view_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "source_created": False,
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
        "relation_view_is_comparison_view": False,
        "relation_view_is_index_system": False,
        "relation_view_is_registry": False,
        "relation_view_is_search": False,
        "relation_view_is_ranking": False,
        "relation_view_compares_orientation_objects": False,
        "relation_view_ranks_orientation_objects": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium relation view test",
        "local relevance medium relation view live artifact",
        "local relevance medium relation view terminal summary, if needed",
        "comparison view",
        "local relevance orientation index system, if separately selected",
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


def _resolve_outcome(
    request: Mapping[str, Any],
    failed_check_count: int,
) -> str:
    if failed_check_count:
        return OUTCOME_BLOCKED
    requested = request.get("requested_local_relevance_medium_relation_view_outcome")
    if requested in OUTCOME_FAMILY:
        return str(requested)
    if request.get("local_relevance_medium_relation_view_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if request.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return OUTCOME_RECORDED


def _build_block(
    outcome: str,
    block_code: str | None,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {"blocked": False, "code": None, "block_code": None, "reason": None}
    code = block_code or "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BLOCK_REQUESTED"
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize_value(request.get("block_reason") or code),
    }


def _build_selected_basis(facts: Mapping[str, Any]) -> dict[str, Any]:
    return _sanitize_value(
        {
            "basis_local_relevance_medium_multiplicity_result_artifact": facts.get(
                "basis_local_relevance_medium_multiplicity_result_artifact"
            ),
            "basis_local_relevance_medium_multiplicity_result_outcome": facts.get(
                "basis_local_relevance_medium_multiplicity_result_outcome"
            ),
            "basis_local_relevance_medium_multiplicity_result_result_version": facts.get(
                "basis_local_relevance_medium_multiplicity_result_result_version"
            ),
            "basis_local_relevance_medium_multiplicity_result_failed_check_count": facts.get(
                "basis_local_relevance_medium_multiplicity_result_failed_check_count"
            ),
            "multiplicity_result_type": facts.get("multiplicity_result_type"),
            "multiplicity_result_scope": facts.get("multiplicity_result_scope"),
            "multiplicity_count": facts.get("multiplicity_count"),
            "basis_first_local_relevance_orientation_index_entry_artifact": facts.get(
                "basis_first_local_relevance_orientation_index_entry_artifact"
            ),
            "basis_second_local_relevance_orientation_index_entry_artifact": facts.get(
                "basis_second_local_relevance_orientation_index_entry_artifact"
            ),
            "first_orientation_view_artifact": facts.get(
                "first_orientation_view_artifact"
            ),
            "second_orientation_view_artifact": facts.get(
                "second_orientation_view_artifact"
            ),
            "first_received_signal_id": facts.get("first_received_signal_id"),
            "second_received_signal_id": facts.get("second_received_signal_id"),
            "basis_lineage_preserved": facts.get("basis_lineage_preserved"),
        }
    )


def _assemble_result(
    request: Mapping[str, Any],
    request_failure_code: str | None = None,
) -> dict[str, Any]:
    artifact, artifact_path, artifact_read_code = _read_json_object(
        request.get("selected_local_relevance_medium_multiplicity_result_artifact")
    )
    facts = _extract_multiplicity_result_facts(artifact, artifact_path)
    checks = _build_checks(request, facts, artifact_read_code, request_failure_code)
    passed_check_count, failed_check_count = _check_counts(checks)
    outcome = _resolve_outcome(request, failed_check_count)
    recorded = outcome == OUTCOME_RECORDED and failed_check_count == 0
    relation_view = _build_relation_view(request, facts) if recorded else {}
    statement = _build_statement(recorded)
    block = _build_block(outcome, _first_failed_code(checks), request)

    metadata = {
        "local_relevance_medium_relation_view_id": _first_present(
            relation_view.get("relation_view_id") if relation_view else None,
            request.get("local_relevance_medium_relation_view_id"),
            DEFAULT_RELATION_VIEW_ID,
        ),
        "local_relevance_medium_relation_view_type": RELATION_VIEW_TYPE,
        "local_relevance_medium_relation_view_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }

    result: dict[str, Any] = {
        "local_relevance_medium_relation_view_metadata": metadata,
        "declared_local_relevance_medium_relation_view_question": _sanitize_value(
            {
                "question": request.get("local_relevance_medium_relation_view_question"),
                "intent": request.get("local_relevance_medium_relation_view_intent"),
                "relation_view_type": request.get("relation_view_type"),
                "relation_view_scope": request.get("relation_view_scope"),
                "relation_frame": request.get("relation_frame"),
            }
        ),
        "selected_local_relevance_medium_multiplicity_result_artifact_basis": (
            _build_selected_basis(facts)
        ),
        "local_relevance_medium_relation_view": relation_view,
        "local_relevance_medium_relation_view_checks": checks,
        "local_relevance_medium_relation_view_statement": statement,
        "local_relevance_medium_relation_view_non_meaning": _build_non_meaning(),
        "additional_basis_required": (
            [_sanitize_value(request.get("additional_basis_context"))]
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": (
            [
                _sanitize_value(
                    request.get("not_recorded_basis")
                    or "local relevance medium relation view not recorded"
                )
            ]
            if outcome == OUTCOME_NOT_RECORDED
            else []
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_relation_view_summary"] = (
        build_local_relevance_medium_relation_view_v0_min_summary(result)
    )
    return _sanitize_value(result)


def resolve_local_relevance_medium_relation_view_v0_min(
    declared_local_relevance_medium_relation_view: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one local relevance medium relation view request."""

    if declared_local_relevance_medium_relation_view is None:
        return _assemble_result({})
    if not isinstance(declared_local_relevance_medium_relation_view, Mapping):
        return _assemble_result(
            {},
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUEST_MALFORMED",
        )
    request = copy.deepcopy(dict(declared_local_relevance_medium_relation_view))
    return _assemble_result(request)


def resolve_local_relevance_medium_relation_view_v0_min_from_path(
    declared_local_relevance_medium_relation_view_path: Path | str,
) -> dict:
    """Read a declared relation-view request JSON object and resolve it."""

    try:
        loaded = json.loads(
            Path(declared_local_relevance_medium_relation_view_path).read_text(
                encoding="utf-8"
            )
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return _assemble_result(
            build_declared_local_relevance_medium_relation_view_v0_min_request(),
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUEST_UNREADABLE",
        )
    if not isinstance(loaded, Mapping):
        return _assemble_result(
            {},
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUEST_MALFORMED",
        )
    return resolve_local_relevance_medium_relation_view_v0_min(loaded)


def build_local_relevance_medium_relation_view_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded JSON-safe summary of a relation-view resolver result."""

    metadata = _mapping_or_empty(result.get("local_relevance_medium_relation_view_metadata"))
    declared = _mapping_or_empty(
        result.get("declared_local_relevance_medium_relation_view_question")
    )
    relation_view = _mapping_or_empty(result.get("local_relevance_medium_relation_view"))
    statement = _mapping_or_empty(
        result.get("local_relevance_medium_relation_view_statement")
    )
    non_claims = _mapping_or_empty(result.get("non_claims"))
    block = _mapping_or_empty(result.get("block"))
    checks = result.get("local_relevance_medium_relation_view_checks")
    check_list = checks if isinstance(checks, list) else []
    passed_check_count, failed_check_count = _check_counts(check_list)
    canonical_false = all(
        key in non_claims and non_claims.get(key) is False
        for key in REQUIRED_FALSE_NON_CLAIMS
    )

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "relation_view_id": _first_present(
            relation_view.get("relation_view_id"),
            metadata.get("local_relevance_medium_relation_view_id"),
        ),
        "question": declared.get("question"),
        "intent": declared.get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get(
            "local_relevance_medium_relation_view_version", RESULT_VERSION
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "relation_view_recorded": statement.get(
            "local_relevance_medium_relation_view_recorded", False
        ),
        "multiplicity_result_artifact_preserved": statement.get(
            "basis_local_relevance_medium_multiplicity_result_artifact_preserved",
            False,
        ),
        "first_locator_artifact_preserved": statement.get(
            "basis_first_local_relevance_orientation_index_entry_artifact_preserved",
            False,
        ),
        "second_locator_artifact_preserved": statement.get(
            "basis_second_local_relevance_orientation_index_entry_artifact_preserved",
            False,
        ),
        "first_orientation_view_artifact_preserved": statement.get(
            "first_orientation_view_artifact_preserved", False
        ),
        "second_orientation_view_artifact_preserved": statement.get(
            "second_orientation_view_artifact_preserved", False
        ),
        "first_receipt_artifact_preserved": statement.get(
            "first_receipt_artifact_preserved", False
        ),
        "second_receipt_artifact_preserved": statement.get(
            "second_receipt_artifact_preserved", False
        ),
        "first_reception_artifact_preserved": statement.get(
            "first_reception_artifact_preserved", False
        ),
        "second_reception_artifact_preserved": statement.get(
            "second_reception_artifact_preserved", False
        ),
        "successor_candidate_admission_artifact_preserved": statement.get(
            "successor_candidate_admission_artifact_preserved", False
        ),
        "successor_reception_request_artifact_preserved": statement.get(
            "successor_reception_request_artifact_preserved", False
        ),
        "first_received_signal_id_preserved": statement.get(
            "first_received_signal_id_preserved", False
        ),
        "second_received_signal_id_preserved": statement.get(
            "second_received_signal_id_preserved", False
        ),
        "first_and_second_signals_distinct": statement.get(
            "first_and_second_signals_distinct", False
        ),
        "first_relevance_basis_id_preserved": statement.get(
            "first_relevance_basis_id_preserved", False
        ),
        "second_relevance_basis_id_preserved": statement.get(
            "second_relevance_basis_id_preserved", False
        ),
        "first_relevance_scope_id_preserved": statement.get(
            "first_relevance_scope_id_preserved", False
        ),
        "second_relevance_scope_id_preserved": statement.get(
            "second_relevance_scope_id_preserved", False
        ),
        "first_carrier_context_id_preserved": statement.get(
            "first_carrier_context_id_preserved", False
        ),
        "second_carrier_context_id_preserved": statement.get(
            "second_carrier_context_id_preserved", False
        ),
        "first_reception_envelope_id_preserved": statement.get(
            "first_reception_envelope_id_preserved", False
        ),
        "second_reception_envelope_id_preserved": statement.get(
            "second_reception_envelope_id_preserved", False
        ),
        "relation_view_scope_local_only": statement.get(
            "relation_view_scope_local_only", False
        ),
        "relation_frame_bounded_co_presence_only": statement.get(
            "relation_frame_bounded_co_presence_only", False
        ),
        "relation_pair_count_is_one": statement.get(
            "relation_pair_count_is_one", False
        ),
        "relation_readable_co_presence_recorded": statement.get(
            "relation_readable_co_presence_recorded", False
        ),
        "relation_view_object_summary": {
            "relation_view_type": relation_view.get("relation_view_type"),
            "relation_view_scope": relation_view.get("relation_view_scope"),
            "relation_frame": relation_view.get("relation_frame"),
            "basis_local_relevance_medium_multiplicity_result_artifact": relation_view.get(
                "basis_local_relevance_medium_multiplicity_result_artifact"
            ),
            "first_received_signal_id": relation_view.get("first_received_signal_id"),
            "second_received_signal_id": relation_view.get("second_received_signal_id"),
            "multiplicity_count": relation_view.get("multiplicity_count"),
            "relation_pair_count": relation_view.get("relation_pair_count"),
        },
        "comparison_view_not_created": non_claims.get("comparison_view_created") is False,
        "index_system_registry_search_ranking_not_created": all(
            non_claims.get(key) is False
            for key in (
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
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
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "comparison_view_created",
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": all(
            non_claims.get(key) is False
            for key in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
        ),
        "result_level_non_claims_canonical_false": canonical_false,
    }
    return _sanitize_value(summary)


def _next_available_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 1000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise LocalRelevanceMediumRelationViewV0MinError(
        "could not allocate non-overwriting relation-view result path"
    )


def write_local_relevance_medium_relation_view_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a relation-view resolver result as stable UTF-8 JSON."""

    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumRelationViewV0MinError(
            "relation-view result must be a mapping"
        )
    metadata = _mapping_or_empty(result.get("local_relevance_medium_relation_view_metadata"))
    relation_view = _mapping_or_empty(result.get("local_relevance_medium_relation_view"))
    relation_view_id = _first_present(
        relation_view.get("relation_view_id"),
        metadata.get("local_relevance_medium_relation_view_id"),
        DEFAULT_RELATION_VIEW_ID,
    )
    if output_path is None:
        target = OUTPUT_ROOT / (
            f"{relation_view_id}__local_relevance_medium_relation_view_v0_min_result.json"
        )
    else:
        target = Path(output_path)
        if target.exists() and target.is_dir():
            target = target / (
                f"{relation_view_id}__local_relevance_medium_relation_view_v0_min_result.json"
            )
    target = _next_available_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(_sanitize_value(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_local_relevance_medium_relation_view_v0_min_request(
    *,
    local_relevance_medium_relation_view_id: str = DEFAULT_RELATION_VIEW_ID,
    selected_local_relevance_medium_multiplicity_result_artifact: Path | str = (
        DEFAULT_MULTIPLICITY_RESULT_ARTIFACT
    ),
    relation_view_type: str = RELATION_VIEW_TYPE,
    relation_view_scope: str = RELATION_VIEW_SCOPE,
    relation_frame: str = RELATION_FRAME,
    local_relevance_medium_relation_view_intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a valid declared relation-view request."""

    request: dict[str, Any] = {
        "local_relevance_medium_relation_view_id": local_relevance_medium_relation_view_id,
        "local_relevance_medium_relation_view_question": CORE_QUESTION,
        "local_relevance_medium_relation_view_intent": (
            local_relevance_medium_relation_view_intent
        ),
        "selected_local_relevance_medium_multiplicity_result_artifact": str(
            selected_local_relevance_medium_multiplicity_result_artifact
        ),
        "relation_view_scope": relation_view_scope,
        "relation_view_type": relation_view_type,
        "relation_frame": relation_frame,
        "declared_non_claims": (
            copy.deepcopy(dict(declared_non_claims))
            if isinstance(declared_non_claims, Mapping)
            else _canonical_non_claims()
        ),
    }
    request.update(copy.deepcopy(extra_fields))
    return request
