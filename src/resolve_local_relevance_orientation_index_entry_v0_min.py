"""Minimum resolver for one local relevance orientation index entry.

This module records one small local locator object from one clean relevance
orientation view artifact.  It is object-shaped, not index-system-shaped: it
does not create a registry, search surface, ranking surface, authority,
currentness, truth, action, synchronization, participation authorization,
runtime permission, public API, distributed behavior, operation permission, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceOrientationIndexEntryV0MinError(Exception):
    """Raised for unreadable local relevance orientation index entry requests."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_orientation_index_entry_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

INDEX_ENTRY_TYPE = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
INDEX_ENTRY_SCOPE_LOCAL_ONLY = "LOCAL_INDEX_ENTRY_ONLY"
ORIENTATION_SCOPE_LOCAL_ONLY = "LOCAL_ORIENTATION_ONLY"
SUPPORTED_INDEX_ENTRY_SCOPE_VALUES = (INDEX_ENTRY_SCOPE_LOCAL_ONLY,)
SUPPORTED_INDEX_ENTRY_TYPE_VALUES = (INDEX_ENTRY_TYPE,)

ORIENTATION_VIEW_OUTCOME_RECORDED = "RELEVANCE_ORIENTATION_VIEW_RECORDED"
ORIENTATION_VIEW_RESULT_VERSION = "0.1.0"

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"
)
DEFAULT_RELEVANCE_ORIENTATION_VIEW_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
    "relevance_orientation_view_reference_review_001__"
    "relevance_orientation_view_v0_min_result.json"
)

CORE_QUESTION = (
    "Given one clean relevance orientation view artifact, may one "
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY be recorded that preserves the "
    "orientation view artifact path, source receipt artifact path, referenced "
    "reception artifact path, and received identifiers for local "
    "discoverability only, without creating an index system, registry, search, "
    "ranking, authority, currentness, truth, action, synchronization, "
    "participation authorization, participant role, runtime permission, public "
    "API, participant-facing interface, distributed network behavior, "
    "operation permission, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
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
    "index_entry_added_new_signal",
    "index_entry_added_new_relevance_basis",
    "index_entry_added_new_relevance_scope",
    "index_entry_added_new_carrier_context",
    "index_entry_added_new_envelope",
    "artifact_existence_treated_as_index_entry_authority",
    "latest_file_posture_treated_as_index_entry_authority",
    "repo_local_availability_treated_as_index_entry_authority",
    "hidden_repo_state_used_as_index_entry_content",
    "hidden_repo_state_used_as_index_entry_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_orientation_index_entry_recorded",
    "orientation_view_artifact_preserved",
    "source_receipt_artifact_preserved",
    "referenced_reception_artifact_preserved",
    "received_signal_id_preserved",
    "received_relevance_basis_id_preserved",
    "received_relevance_scope_id_preserved",
    "received_carrier_context_id_preserved",
    "received_reception_envelope_id_preserved",
    "index_entry_scope_local_only",
    "local_discoverability_preserved",
    "index_entry_does_not_create_index_system",
    "index_entry_does_not_create_registry",
    "index_entry_does_not_create_search",
    "index_entry_does_not_create_ranking",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BLOCK_REQUESTED",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_PATH_MISSING",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_UNREADABLE",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_JSON_OBJECT",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_RECORDED",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
    "ORIENTATION_VIEW_MISSING",
    "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
    "ORIENTATION_VIEW_SOURCE_RECEIPT_ARTIFACT_MISSING",
    "ORIENTATION_VIEW_REFERENCED_RECEPTION_ARTIFACT_MISSING",
    "RECEIVED_SIGNAL_ID_MISSING",
    "RECEIVED_RELEVANCE_BASIS_ID_MISSING",
    "RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
    "RECEIVED_CARRIER_CONTEXT_ID_MISSING",
    "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
    "INDEX_ENTRY_SCOPE_MISSING",
    "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
    "INDEX_ENTRY_TYPE_MISSING",
    "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
    "INDEX_ENTRY_CREATED_INDEX_SYSTEM",
    "INDEX_ENTRY_CREATED_REGISTRY",
    "INDEX_ENTRY_CREATED_SEARCH",
    "INDEX_ENTRY_CREATED_RANKING",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RELEVANCE_ORIENTATION_VIEW_BODY_MUST_NOT_RETURN",
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
    "raw_index_entry_body",
    "raw_local_relevance_orientation_index_entry_body",
    "raw_orientation_body",
    "raw_relevance_orientation_view_body",
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
    "index_entry_body",
    "local_relevance_orientation_index_entry_body",
    "orientation_body",
    "relevance_orientation_view_body",
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

INDEX_ENTRY_FIELDS = (
    "index_entry_id",
    "index_entry_type",
    "index_entry_version",
    "index_entry_scope",
    "orientation_view_artifact",
    "orientation_view_outcome",
    "orientation_view_result_version",
    "orientation_view_failed_check_count",
    "orientation_scope",
    "source_receipt_artifact",
    "referenced_reception_artifact",
    "received_signal_id",
    "received_relevance_basis_id",
    "received_relevance_scope_id",
    "received_carrier_context_id",
    "received_reception_envelope_id",
    "local_discoverability",
    "does_not_create_index_system",
    "does_not_create_registry",
    "does_not_create_search",
    "does_not_create_ranking",
    "authority_created",
    "currentness_created",
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
    (
        "index entry does not create index system",
        "index_entry_creates_index_system",
        "INDEX_ENTRY_CREATED_INDEX_SYSTEM",
    ),
    (
        "index entry does not create registry",
        "index_entry_creates_registry",
        "INDEX_ENTRY_CREATED_REGISTRY",
    ),
    (
        "index entry does not create search",
        "index_entry_creates_search",
        "INDEX_ENTRY_CREATED_SEARCH",
    ),
    (
        "index entry does not create ranking",
        "index_entry_creates_ranking",
        "INDEX_ENTRY_CREATED_RANKING",
    ),
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
        "artifact existence not index-entry authority",
        "artifact_existence_treated_as_index_entry_authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    ),
    (
        "latest file posture not index-entry authority",
        "latest_file_posture_treated_as_index_entry_authority",
        "LATEST_FILE_POSTURE_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    ),
    (
        "repo-local availability not index-entry authority",
        "repo_local_availability_treated_as_index_entry_authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    ),
    (
        "hidden repo state not index-entry content",
        "hidden_repo_state_used_as_index_entry_content",
        "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_CONTENT",
    ),
    (
        "hidden repo state not index-entry authority",
        "hidden_repo_state_used_as_index_entry_authority",
        "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_AUTHORITY",
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


def _extract_orientation_facts(
    orientation_artifact: Mapping[str, Any],
    selected_orientation_path: str | None,
) -> dict[str, Any]:
    metadata = _as_mapping(
        orientation_artifact.get("relevance_orientation_view_metadata")
    )
    summary = _as_mapping(
        orientation_artifact.get("relevance_orientation_view_summary")
    )
    orientation_view = _as_mapping(orientation_artifact.get("orientation_view"))

    failed_count = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        orientation_artifact.get("failed_check_count"),
    )

    return {
        "orientation_view_artifact": selected_orientation_path,
        "orientation_view_outcome": _first_present(
            orientation_artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "orientation_view_result_version": _first_present(
            metadata.get("relevance_orientation_view_version"),
            metadata.get("result_version"),
            summary.get("result_version"),
            orientation_artifact.get("result_version"),
            orientation_view.get("orientation_view_version"),
        ),
        "orientation_view_failed_check_count": failed_count,
        "orientation_view_present": isinstance(
            orientation_artifact.get("orientation_view"), Mapping
        ),
        "orientation_scope": orientation_view.get("orientation_scope"),
        "source_receipt_artifact": orientation_view.get("source_receipt_artifact"),
        "referenced_reception_artifact": orientation_view.get(
            "referenced_reception_artifact"
        ),
        "received_signal_id": orientation_view.get("received_signal_id"),
        "received_relevance_basis_id": orientation_view.get(
            "received_relevance_basis_id"
        ),
        "received_relevance_scope_id": orientation_view.get(
            "received_relevance_scope_id"
        ),
        "received_carrier_context_id": orientation_view.get(
            "received_carrier_context_id"
        ),
        "received_reception_envelope_id": orientation_view.get(
            "received_reception_envelope_id"
        ),
    }


def _facts_are_sufficient(facts: Mapping[str, Any]) -> bool:
    return all(
        facts.get(key)
        for key in (
            "orientation_view_artifact",
            "source_receipt_artifact",
            "referenced_reception_artifact",
            "received_signal_id",
            "received_relevance_basis_id",
            "received_relevance_scope_id",
            "received_carrier_context_id",
            "received_reception_envelope_id",
        )
    )


def _build_index_entry(
    facts: Mapping[str, Any],
    index_entry_scope: str,
    index_entry_type: str,
) -> dict[str, Any]:
    return {
        "index_entry_id": "local_relevance_orientation_index_entry_001",
        "index_entry_type": index_entry_type,
        "index_entry_version": RESULT_VERSION,
        "index_entry_scope": index_entry_scope,
        "orientation_view_artifact": facts.get("orientation_view_artifact"),
        "orientation_view_outcome": facts.get("orientation_view_outcome"),
        "orientation_view_result_version": facts.get(
            "orientation_view_result_version"
        ),
        "orientation_view_failed_check_count": facts.get(
            "orientation_view_failed_check_count"
        ),
        "orientation_scope": facts.get("orientation_scope"),
        "source_receipt_artifact": facts.get("source_receipt_artifact"),
        "referenced_reception_artifact": facts.get("referenced_reception_artifact"),
        "received_signal_id": facts.get("received_signal_id"),
        "received_relevance_basis_id": facts.get("received_relevance_basis_id"),
        "received_relevance_scope_id": facts.get("received_relevance_scope_id"),
        "received_carrier_context_id": facts.get("received_carrier_context_id"),
        "received_reception_envelope_id": facts.get(
            "received_reception_envelope_id"
        ),
        "local_discoverability": True,
        "does_not_create_index_system": True,
        "does_not_create_registry": True,
        "does_not_create_search": True,
        "does_not_create_ranking": True,
        "authority_created": False,
        "currentness_created": False,
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


def _declared_non_claims_false(declared_non_claims: Any) -> tuple[bool, dict[str, Any]]:
    if not isinstance(declared_non_claims, Mapping):
        return False, {
            "declared_non_claims_mapping": type(declared_non_claims).__name__,
            "missing_or_flipped": list(REQUIRED_FALSE_NON_CLAIMS),
        }

    missing_or_flipped: list[str] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared_non_claims or declared_non_claims.get(key) is not False:
            missing_or_flipped.append(key)

    return not missing_or_flipped, {
        "declared_non_claims_mapping": "mapping",
        "missing_or_flipped": missing_or_flipped,
    }


def _predecessor_failure_evidence_preserved(request: Mapping[str, Any]) -> bool:
    return not any(
        request.get(key) is True
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
    )


def _build_checks(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    orientation_readable: bool,
    orientation_json_object: bool,
    orientation_read_error: str | None,
) -> list[dict[str, Any]]:
    intent = request.get("local_relevance_orientation_index_entry_intent")
    question = request.get("local_relevance_orientation_index_entry_question")
    selected_orientation_path = request.get("selected_relevance_orientation_view_artifact")
    index_entry_scope = request.get("index_entry_scope")
    index_entry_type = request.get("index_entry_type")
    checks: list[dict[str, Any]] = []

    checks.append(
        _check(
            "index entry question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared local relevance orientation index entry question",
            question,
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block intent not requested",
            intent != INTENT_BLOCK,
            "not BLOCK_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
            intent,
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "selected relevance orientation view artifact path declared",
            bool(selected_orientation_path)
            and request.get("selected_relevance_orientation_view_artifact_missing")
            is not True,
            "selected relevance orientation view artifact path declared",
            selected_orientation_path,
            "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected relevance orientation view artifact readable JSON",
            bool(selected_orientation_path) and orientation_readable,
            "readable JSON object",
            orientation_read_error or "readable",
            "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _check(
            "selected relevance orientation view artifact JSON object",
            bool(selected_orientation_path) and orientation_json_object,
            "JSON object",
            "JSON object" if orientation_json_object else orientation_read_error,
            "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "orientation view artifact outcome recorded",
            facts.get("orientation_view_outcome") == ORIENTATION_VIEW_OUTCOME_RECORDED
            and request.get("selected_relevance_orientation_view_artifact_not_recorded")
            is not True,
            ORIENTATION_VIEW_OUTCOME_RECORDED,
            facts.get("orientation_view_outcome"),
            "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "orientation view artifact result version 0.1.0",
            facts.get("orientation_view_result_version")
            == ORIENTATION_VIEW_RESULT_VERSION
            and request.get(
                "selected_relevance_orientation_view_artifact_version_not_0_1_0"
            )
            is not True,
            ORIENTATION_VIEW_RESULT_VERSION,
            facts.get("orientation_view_result_version"),
            "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "orientation view artifact failed check count zero",
            facts.get("orientation_view_failed_check_count") == 0
            and request.get(
                "selected_relevance_orientation_view_artifact_failed_checks_present"
            )
            is not True,
            0,
            facts.get("orientation_view_failed_check_count"),
            "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "orientation view present",
            facts.get("orientation_view_present") is True
            and request.get("orientation_view_missing") is not True,
            "orientation_view mapping present",
            facts.get("orientation_view_present"),
            "ORIENTATION_VIEW_MISSING",
        )
    )
    checks.append(
        _check(
            "orientation scope local only",
            facts.get("orientation_scope") == ORIENTATION_SCOPE_LOCAL_ONLY
            and request.get("orientation_scope_not_local_only") is not True,
            ORIENTATION_SCOPE_LOCAL_ONLY,
            facts.get("orientation_scope"),
            "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
        )
    )
    checks.append(
        _check(
            "source receipt artifact present",
            bool(facts.get("source_receipt_artifact"))
            and request.get("orientation_view_source_receipt_artifact_missing")
            is not True,
            "source receipt artifact path",
            facts.get("source_receipt_artifact"),
            "ORIENTATION_VIEW_SOURCE_RECEIPT_ARTIFACT_MISSING",
        )
    )
    checks.append(
        _check(
            "referenced reception artifact present",
            bool(facts.get("referenced_reception_artifact"))
            and request.get("orientation_view_referenced_reception_artifact_missing")
            is not True,
            "referenced reception artifact path",
            facts.get("referenced_reception_artifact"),
            "ORIENTATION_VIEW_REFERENCED_RECEPTION_ARTIFACT_MISSING",
        )
    )
    checks.extend(
        [
            _check(
                "received signal id present",
                bool(facts.get("received_signal_id"))
                and request.get("received_signal_id_missing") is not True,
                "received signal id",
                facts.get("received_signal_id"),
                "RECEIVED_SIGNAL_ID_MISSING",
            ),
            _check(
                "received relevance basis id present",
                bool(facts.get("received_relevance_basis_id"))
                and request.get("received_relevance_basis_id_missing") is not True,
                "received relevance basis id",
                facts.get("received_relevance_basis_id"),
                "RECEIVED_RELEVANCE_BASIS_ID_MISSING",
            ),
            _check(
                "received relevance scope id present",
                bool(facts.get("received_relevance_scope_id"))
                and request.get("received_relevance_scope_id_missing") is not True,
                "received relevance scope id",
                facts.get("received_relevance_scope_id"),
                "RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
            ),
            _check(
                "received carrier context id present",
                bool(facts.get("received_carrier_context_id"))
                and request.get("received_carrier_context_id_missing") is not True,
                "received carrier context id",
                facts.get("received_carrier_context_id"),
                "RECEIVED_CARRIER_CONTEXT_ID_MISSING",
            ),
            _check(
                "received reception envelope id present",
                bool(facts.get("received_reception_envelope_id"))
                and request.get("received_reception_envelope_id_missing") is not True,
                "received reception envelope id",
                facts.get("received_reception_envelope_id"),
                "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
            ),
        ]
    )
    checks.append(
        _check(
            "index entry scope declared",
            bool(index_entry_scope),
            "index entry scope declared",
            index_entry_scope,
            "INDEX_ENTRY_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "index entry scope local only",
            index_entry_scope == INDEX_ENTRY_SCOPE_LOCAL_ONLY,
            INDEX_ENTRY_SCOPE_LOCAL_ONLY,
            index_entry_scope,
            "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
        )
    )
    checks.append(
        _check(
            "index entry type declared",
            bool(index_entry_type),
            "index entry type declared",
            index_entry_type,
            "INDEX_ENTRY_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "index entry type exact",
            index_entry_type == INDEX_ENTRY_TYPE,
            INDEX_ENTRY_TYPE,
            index_entry_type,
            "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
        )
    )
    checks.append(
        _check(
            "local discoverability preserved",
            request.get("local_discoverability") is not False,
            True,
            request.get("local_discoverability", True),
            "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
        )
    )

    for check_name, field_name, block_code in BOOLEAN_OVERREACH_CHECKS:
        checks.append(
            _check(
                check_name,
                request.get(field_name) is not True,
                False,
                request.get(field_name, False),
                block_code,
            )
        )

    predecessor_preserved = _predecessor_failure_evidence_preserved(request)
    checks.append(
        _check(
            "predecessor failure evidence preserved",
            predecessor_preserved,
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
        )
    )

    result_non_claims = _canonical_non_claims()
    checks.append(
        _check(
            "result-level required false non-claims canonical false",
            all(value is False for value in result_non_claims.values()),
            "all result-level non-claims false",
            result_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    declared_false, declared_detail = _declared_non_claims_false(
        request.get("declared_non_claims")
    )
    checks.append(
        _check(
            "required non-claims false",
            declared_false,
            "all declared required non-claims present and false",
            declared_detail,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _build_block(
    outcome: str, checks: list[Mapping[str, Any]], request: Mapping[str, Any]
) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }

    code = (
        _first_failed_code(checks)
        or "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_MALFORMED"
    )
    reason = request.get("block_reason") or code
    failed_codes = [
        check.get("block_code") or check.get("failure_code")
        for check in checks
        if check.get("passed") is not True
    ]
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason),
        "failed_block_codes": [item for item in failed_codes if item],
    }


def _build_statement(
    outcome: str,
    index_entry: Mapping[str, Any],
    facts: Mapping[str, Any],
) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {
        "local_relevance_orientation_index_entry_recorded": recorded,
        "orientation_view_artifact_preserved": recorded
        and index_entry.get("orientation_view_artifact")
        == facts.get("orientation_view_artifact"),
        "source_receipt_artifact_preserved": recorded
        and index_entry.get("source_receipt_artifact")
        == facts.get("source_receipt_artifact"),
        "referenced_reception_artifact_preserved": recorded
        and index_entry.get("referenced_reception_artifact")
        == facts.get("referenced_reception_artifact"),
        "received_signal_id_preserved": recorded
        and index_entry.get("received_signal_id") == facts.get("received_signal_id"),
        "received_relevance_basis_id_preserved": recorded
        and index_entry.get("received_relevance_basis_id")
        == facts.get("received_relevance_basis_id"),
        "received_relevance_scope_id_preserved": recorded
        and index_entry.get("received_relevance_scope_id")
        == facts.get("received_relevance_scope_id"),
        "received_carrier_context_id_preserved": recorded
        and index_entry.get("received_carrier_context_id")
        == facts.get("received_carrier_context_id"),
        "received_reception_envelope_id_preserved": recorded
        and index_entry.get("received_reception_envelope_id")
        == facts.get("received_reception_envelope_id"),
        "index_entry_scope_local_only": recorded
        and index_entry.get("index_entry_scope") == INDEX_ENTRY_SCOPE_LOCAL_ONLY,
        "local_discoverability_preserved": recorded
        and index_entry.get("local_discoverability") is True,
        "index_entry_does_not_create_index_system": recorded
        and index_entry.get("does_not_create_index_system") is True,
        "index_entry_does_not_create_registry": recorded
        and index_entry.get("does_not_create_registry") is True,
        "index_entry_does_not_create_search": recorded
        and index_entry.get("does_not_create_search") is True,
        "index_entry_does_not_create_ranking": recorded
        and index_entry.get("does_not_create_ranking") is True,
        "result_level_non_claims_canonical_false": True,
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        statement[key] = False
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
        "index_entry_is_index_system": False,
        "index_entry_is_registry": False,
        "index_entry_is_search_surface": False,
        "index_entry_is_ranking_surface": False,
        "index_entry_is_boundary": False,
        "index_entry_is_next_layer_selection": False,
        "index_entry_is_terminal_summary": False,
        "index_entry_is_source": False,
        "index_entry_is_authority": False,
        "index_entry_is_currentness": False,
        "index_entry_is_truth": False,
        "index_entry_is_action": False,
        "index_entry_is_synchronization": False,
        "index_entry_is_participation_authorization": False,
        "index_entry_is_runtime_permission": False,
        "index_entry_is_public_api": False,
        "index_entry_is_participant_facing_interface": False,
        "index_entry_is_distributed_network_behavior": False,
        "index_entry_authorizes_follow_on_work": False,
    }


def _build_what_remains_open() -> list[str]:
    return [
        "local relevance orientation index entry test",
        "local relevance orientation index entry live artifact",
        "local relevance orientation index entry terminal summary, if needed",
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
        "successor reception request",
        "follow-on work",
    ]


def _determine_outcome(
    request: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
) -> str:
    if _failed_checks(checks):
        return OUTCOME_BLOCKED
    if (
        request.get("requested_local_relevance_orientation_index_entry_outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if request.get("local_relevance_orientation_index_entry_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _result_from_parts(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    checks: list[dict[str, Any]],
    index_entry: Mapping[str, Any],
    outcome: str,
    orientation_readable: bool,
    orientation_json_object: bool,
) -> dict[str, Any]:
    request_id = str(
        request.get("local_relevance_orientation_index_entry_request_id")
        or "local_relevance_orientation_index_entry_request_unidentified"
    )
    block = _build_block(outcome, checks, request)
    failed_check_count = len(_failed_checks(checks))
    passed_check_count = _count_passed(checks)
    metadata = {
        "local_relevance_orientation_index_entry_id": request_id,
        "local_relevance_orientation_index_entry_type": (
            "local_relevance_orientation_index_entry_result"
        ),
        "local_relevance_orientation_index_entry_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "local_relevance_orientation_index_entry_intent": request.get(
            "local_relevance_orientation_index_entry_intent"
        ),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
    }
    selected_basis = {
        "basis_role": "selected_relevance_orientation_view_artifact_reference_only",
        "selected_relevance_orientation_view_artifact": request.get(
            "selected_relevance_orientation_view_artifact"
        ),
        "orientation_artifact_readable_json": orientation_readable,
        "orientation_artifact_json_object": orientation_json_object,
        "orientation_view_outcome": facts.get("orientation_view_outcome"),
        "orientation_view_result_version": facts.get(
            "orientation_view_result_version"
        ),
        "orientation_view_failed_check_count": facts.get(
            "orientation_view_failed_check_count"
        ),
        "orientation_scope": facts.get("orientation_scope"),
        "source_receipt_artifact": facts.get("source_receipt_artifact"),
        "referenced_reception_artifact": facts.get("referenced_reception_artifact"),
        "raw_full_body_returned": False,
    }

    result = {
        "local_relevance_orientation_index_entry_metadata": metadata,
        "declared_local_relevance_orientation_index_entry_question": _sanitize(
            request.get("local_relevance_orientation_index_entry_question")
        ),
        "selected_relevance_orientation_view_artifact_basis": selected_basis,
        "index_entry": dict(index_entry),
        "local_relevance_orientation_index_entry_checks": checks,
        "local_relevance_orientation_index_entry_statement": _build_statement(
            outcome, index_entry, facts
        ),
        "local_relevance_orientation_index_entry_non_meaning": _build_non_meaning(),
        "additional_basis_required": (
            _sanitize(request.get("additional_basis_context"))
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": (
            _sanitize(
                request.get("not_recorded_basis")
                or ["declared intent did not record local relevance orientation index entry"]
            )
            if outcome == OUTCOME_NOT_RECORDED
            else []
        ),
        "what_remains_open": _build_what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
        "local_relevance_orientation_index_entry_summary": {},
    }
    result["local_relevance_orientation_index_entry_summary"] = (
        build_local_relevance_orientation_index_entry_v0_min_summary(result)
    )
    return result


def _malformed_request_result(actual_request: Any) -> dict[str, Any]:
    checks = [
        _check(
            "declared local relevance orientation index entry request mapping",
            False,
            "mapping",
            type(actual_request).__name__,
            "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_MALFORMED",
        )
    ]
    request = {
        "local_relevance_orientation_index_entry_request_id": (
            "local_relevance_orientation_index_entry_request_malformed"
        ),
        "local_relevance_orientation_index_entry_question": None,
        "local_relevance_orientation_index_entry_intent": None,
        "selected_relevance_orientation_view_artifact": None,
        "index_entry_scope": None,
        "index_entry_type": None,
        "declared_non_claims": {},
    }
    return _result_from_parts(
        request=request,
        facts={},
        checks=checks,
        index_entry={},
        outcome=OUTCOME_BLOCKED,
        orientation_readable=False,
        orientation_json_object=False,
    )


def resolve_local_relevance_orientation_index_entry_v0_min(
    declared_local_relevance_orientation_index_entry_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one local relevance orientation index entry request."""

    if declared_local_relevance_orientation_index_entry_request is None:
        declared_local_relevance_orientation_index_entry_request = (
            build_declared_local_relevance_orientation_index_entry_v0_min_request()
        )
    if not isinstance(declared_local_relevance_orientation_index_entry_request, Mapping):
        return _malformed_request_result(
            declared_local_relevance_orientation_index_entry_request
        )

    request = copy.deepcopy(dict(declared_local_relevance_orientation_index_entry_request))
    selected_orientation_path = request.get("selected_relevance_orientation_view_artifact")

    orientation_artifact: Any = {}
    orientation_readable = False
    orientation_json_object = False
    orientation_read_error: str | None = None
    if (
        selected_orientation_path
        and request.get("selected_relevance_orientation_view_artifact_missing") is not True
    ):
        orientation_artifact, orientation_readable, orientation_json_object, orientation_read_error = (
            _read_json_path(selected_orientation_path)
        )
    elif selected_orientation_path:
        orientation_read_error = "selected orientation artifact declared missing by request"
    else:
        orientation_read_error = "selected orientation artifact path missing"

    facts: dict[str, Any] = {}
    if isinstance(orientation_artifact, Mapping):
        facts = _extract_orientation_facts(
            orientation_artifact,
            str(selected_orientation_path),
        )

    checks = _build_checks(
        request=request,
        facts=facts,
        orientation_readable=orientation_readable,
        orientation_json_object=orientation_json_object,
        orientation_read_error=orientation_read_error,
    )
    outcome = _determine_outcome(request, checks)

    index_entry_scope = request.get("index_entry_scope")
    index_entry_type = request.get("index_entry_type")
    if (
        outcome == OUTCOME_RECORDED
        or (
            _facts_are_sufficient(facts)
            and index_entry_scope == INDEX_ENTRY_SCOPE_LOCAL_ONLY
            and index_entry_type == INDEX_ENTRY_TYPE
        )
    ):
        index_entry = _build_index_entry(
            facts,
            INDEX_ENTRY_SCOPE_LOCAL_ONLY,
            INDEX_ENTRY_TYPE,
        )
    else:
        index_entry = {}

    return _result_from_parts(
        request=request,
        facts=facts,
        checks=checks,
        index_entry=index_entry,
        outcome=outcome,
        orientation_readable=orientation_readable,
        orientation_json_object=orientation_json_object,
    )


def resolve_local_relevance_orientation_index_entry_v0_min_from_path(
    declared_local_relevance_orientation_index_entry_request_path: Path | str,
) -> dict:
    """Read a declared request JSON object from path and resolve it."""

    try:
        parsed = json.loads(
            Path(declared_local_relevance_orientation_index_entry_request_path).read_text(
                encoding="utf-8"
            )
        )
    except OSError as exc:
        raise LocalRelevanceOrientationIndexEntryV0MinError(
            f"declared local relevance orientation index entry request unreadable: {exc}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise LocalRelevanceOrientationIndexEntryV0MinError(
            f"declared local relevance orientation index entry request is not JSON: {exc}"
        ) from exc

    if not isinstance(parsed, Mapping):
        return _malformed_request_result(parsed)
    return resolve_local_relevance_orientation_index_entry_v0_min(parsed)


def build_local_relevance_orientation_index_entry_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a small JSON-safe summary from a resolver result artifact."""

    metadata = _as_mapping(
        result.get("local_relevance_orientation_index_entry_metadata")
    )
    block = _as_mapping(result.get("block"))
    statement = _as_mapping(
        result.get("local_relevance_orientation_index_entry_statement")
    )
    index_entry = _as_mapping(result.get("index_entry"))
    selected_basis = _as_mapping(
        result.get("selected_relevance_orientation_view_artifact_basis")
    )
    non_claims = _as_mapping(result.get("non_claims"))
    checks_value = result.get("local_relevance_orientation_index_entry_checks")
    checks = checks_value if isinstance(checks_value, list) else []
    passed_check_count = _count_passed(checks)
    failed_check_count = len(_failed_checks(checks))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("local_relevance_orientation_index_entry_id"),
        "question": result.get(
            "declared_local_relevance_orientation_index_entry_question"
        ),
        "intent": metadata.get("local_relevance_orientation_index_entry_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get(
            "local_relevance_orientation_index_entry_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "local_relevance_orientation_index_entry_recorded": statement.get(
            "local_relevance_orientation_index_entry_recorded", False
        ),
        "orientation_view_artifact_preserved": statement.get(
            "orientation_view_artifact_preserved", False
        ),
        "source_receipt_artifact_preserved": statement.get(
            "source_receipt_artifact_preserved", False
        ),
        "referenced_reception_artifact_preserved": statement.get(
            "referenced_reception_artifact_preserved", False
        ),
        "received_signal_id_preserved": statement.get(
            "received_signal_id_preserved", False
        ),
        "received_relevance_basis_id_preserved": statement.get(
            "received_relevance_basis_id_preserved", False
        ),
        "received_relevance_scope_id_preserved": statement.get(
            "received_relevance_scope_id_preserved", False
        ),
        "received_carrier_context_id_preserved": statement.get(
            "received_carrier_context_id_preserved", False
        ),
        "received_reception_envelope_id_preserved": statement.get(
            "received_reception_envelope_id_preserved", False
        ),
        "index_entry_scope_local_only": statement.get(
            "index_entry_scope_local_only", False
        ),
        "local_discoverability_preserved": statement.get(
            "local_discoverability_preserved", False
        ),
        "index_entry_does_not_create_index_system": statement.get(
            "index_entry_does_not_create_index_system", False
        ),
        "index_entry_does_not_create_registry": statement.get(
            "index_entry_does_not_create_registry", False
        ),
        "index_entry_does_not_create_search": statement.get(
            "index_entry_does_not_create_search", False
        ),
        "index_entry_does_not_create_ranking": statement.get(
            "index_entry_does_not_create_ranking", False
        ),
        "index_entry_summary": {
            "index_entry_id": index_entry.get("index_entry_id"),
            "index_entry_type": index_entry.get("index_entry_type"),
            "index_entry_version": index_entry.get("index_entry_version"),
            "index_entry_scope": index_entry.get("index_entry_scope"),
            "orientation_view_artifact": index_entry.get("orientation_view_artifact"),
            "orientation_scope": index_entry.get("orientation_scope"),
            "source_receipt_artifact": index_entry.get("source_receipt_artifact"),
            "referenced_reception_artifact": index_entry.get(
                "referenced_reception_artifact"
            ),
            "local_discoverability": index_entry.get("local_discoverability"),
        },
        "selected_relevance_orientation_view_artifact_path": selected_basis.get(
            "selected_relevance_orientation_view_artifact"
        ),
        "source_authority_currentness_truth_action_synchronization_participation_runtime_permission_not_created": True,
        "public_api_participant_facing_interface_distributed_network_behavior_not_created": True,
        "operation_permission_follow_on_not_created": True,
        "key_non_claims": {
            key: non_claims.get(key, False)
            for key in (
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "truth_created",
                "action_created",
                "synchronization_created",
                "participation_authorized",
                "runtime_permission_created",
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
                "operation_permission_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": not any(
            non_claims.get(key) is True
            for key in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
        ),
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false", False
        ),
    }


def write_local_relevance_orientation_index_entry_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result artifact as stable UTF-8 JSON."""

    metadata = _as_mapping(
        result.get("local_relevance_orientation_index_entry_metadata")
    )
    request_id = str(
        metadata.get("local_relevance_orientation_index_entry_id")
        or "local_relevance_orientation_index_entry_request_unidentified"
    )

    if output_path is None:
        target_dir = Path(OUTPUT_ROOT)
        target_path = (
            target_dir
            / f"{request_id}__local_relevance_orientation_index_entry_v0_min_result.json"
        )
    else:
        target_path = Path(output_path)
        target_dir = target_path.parent

    target_dir.mkdir(parents=True, exist_ok=True)
    final_path = target_path
    suffix = 1
    while final_path.exists():
        final_path = target_path.with_name(
            f"{target_path.stem}_{suffix:03d}{target_path.suffix}"
        )
        suffix += 1

    final_path.write_text(
        json.dumps(_sanitize(dict(result)), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_local_relevance_orientation_index_entry_v0_min_request(
    local_relevance_orientation_index_entry_request_id: str = (
        "local_relevance_orientation_index_entry_reference_review_001"
    ),
    local_relevance_orientation_index_entry_question: str = CORE_QUESTION,
    local_relevance_orientation_index_entry_intent: str = INTENT_RECORD,
    selected_relevance_orientation_view_artifact: Path | str = (
        DEFAULT_RELEVANCE_ORIENTATION_VIEW_ARTIFACT
    ),
    index_entry_scope: str = INDEX_ENTRY_SCOPE_LOCAL_ONLY,
    index_entry_type: str = INDEX_ENTRY_TYPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid declared local relevance orientation index entry request."""

    request = {
        "local_relevance_orientation_index_entry_request_id": (
            local_relevance_orientation_index_entry_request_id
        ),
        "local_relevance_orientation_index_entry_question": (
            local_relevance_orientation_index_entry_question
        ),
        "local_relevance_orientation_index_entry_intent": (
            local_relevance_orientation_index_entry_intent
        ),
        "selected_relevance_orientation_view_artifact": str(
            selected_relevance_orientation_view_artifact
        ),
        "index_entry_scope": index_entry_scope,
        "index_entry_type": index_entry_type,
        "declared_non_claims": (
            _canonical_non_claims()
            if declared_non_claims is None
            else copy.deepcopy(dict(declared_non_claims))
        ),
    }
    request.update(copy.deepcopy(overrides))
    return request
