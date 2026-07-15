"""Minimum resolver for one local relevance orientation view.

This module records an instrument-shaped local orientation view from one clean
bounded relevance receipt v2 artifact and its referenced bounded relevance
reception artifact.  It does not create a boundary, authority, currentness,
truth, action, synchronization, participation authorization, runtime permission,
public API, distributed behavior, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RelevanceOrientationViewV0MinError(Exception):
    """Raised for unreadable declared relevance orientation view requests."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_relevance_orientation_view_v0_min"

OUTCOME_RECORDED = "RELEVANCE_ORIENTATION_VIEW_RECORDED"
OUTCOME_NOT_RECORDED = "RELEVANCE_ORIENTATION_VIEW_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "RELEVANCE_ORIENTATION_VIEW_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "RELEVANCE_ORIENTATION_VIEW_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_RELEVANCE_ORIENTATION_VIEW"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RELEVANCE_ORIENTATION_VIEW"
INTENT_BLOCK = "BLOCK_RELEVANCE_ORIENTATION_VIEW"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

ORIENTATION_SCOPE_LOCAL_ONLY = "LOCAL_ORIENTATION_ONLY"
RECEIPT_SCOPE_INSPECTABLE_ONLY = "INSPECTABLE_RECEIPT_ONLY"
SUPPORTED_ORIENTATION_SCOPE_VALUES = (ORIENTATION_SCOPE_LOCAL_ONLY,)

RECEIPT_OUTCOME_RECORDED = "BOUNDED_RELEVANCE_RECEIPT_RECORDED"
RECEIPT_RESULT_VERSION = "0.2.0"

OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"
)
DEFAULT_RECEIPT_V2_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/"
    "bounded_relevance_receipt_reference_review_001__"
    "bounded_relevance_receipt_v0_min_v2_result.json"
)

CORE_QUESTION = (
    "Given one clean bounded relevance receipt v2 artifact and its referenced "
    "bounded relevance reception artifact, may one local relevance orientation "
    "view be recorded that reports what is inspectably present, what "
    "identifiers stand as received identifiers, what cannot be inferred, and "
    "what remains unavailable, without creating source, authority, currentness, "
    "truth, action, synchronization, participation authorization, participant "
    "role, runtime permission, public API, participant-facing interface, "
    "distributed network behavior, operation permission, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
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
    "orientation_added_new_signal",
    "orientation_added_new_relevance_basis",
    "orientation_added_new_relevance_scope",
    "orientation_added_new_carrier_context",
    "orientation_added_new_envelope",
    "artifact_existence_treated_as_orientation_authority",
    "latest_file_posture_treated_as_orientation_authority",
    "repo_local_availability_treated_as_orientation_authority",
    "hidden_repo_state_used_as_orientation_content",
    "hidden_repo_state_used_as_orientation_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "relevance_orientation_view_recorded",
    "source_receipt_artifact_preserved",
    "referenced_reception_artifact_preserved",
    "received_signal_id_preserved",
    "received_relevance_basis_id_preserved",
    "received_relevance_scope_id_preserved",
    "received_carrier_context_id_preserved",
    "received_reception_envelope_id_preserved",
    "orientation_scope_local_only",
    "orientation_does_not_expand_receipt",
    "orientation_does_not_expand_reception",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "RELEVANCE_ORIENTATION_VIEW_QUESTION_UNDECLARED",
    "RELEVANCE_ORIENTATION_VIEW_INTENT_UNSUPPORTED",
    "RELEVANCE_ORIENTATION_VIEW_BLOCK_REQUESTED",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_PATH_MISSING",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_UNREADABLE",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_JSON_OBJECT",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_FAILED_CHECKS_PRESENT",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_VERSION_NOT_0_2_0",
    "RECEIPT_OBJECT_MISSING",
    "REFERENCED_RECEPTION_ARTIFACT_MISSING",
    "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
    "RECEIPT_EXPANDS_RECEPTION",
    "RECEIVED_SIGNAL_ID_MISSING",
    "RECEIVED_RELEVANCE_BASIS_ID_MISSING",
    "RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
    "RECEIVED_CARRIER_CONTEXT_ID_MISSING",
    "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
    "ORIENTATION_SCOPE_MISSING",
    "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
    "ORIENTATION_ADDED_NEW_SIGNAL",
    "ORIENTATION_ADDED_NEW_RELEVANCE_BASIS",
    "ORIENTATION_ADDED_NEW_RELEVANCE_SCOPE",
    "ORIENTATION_ADDED_NEW_CARRIER_CONTEXT",
    "ORIENTATION_ADDED_NEW_ENVELOPE",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_ORIENTATION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_ORIENTATION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ORIENTATION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_MALFORMED",
    "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_RELEVANCE_ORIENTATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_RECEIPT_BODY_MUST_NOT_RETURN",
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
    "raw_orientation_body",
    "raw_relevance_orientation_view_body",
    "raw_bounded_relevance_receipt_body",
    "raw_bounded_relevance_reception_body",
    "raw_receipt_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "orientation_body",
    "relevance_orientation_view_body",
    "bounded_relevance_receipt_body",
    "bounded_relevance_reception_body",
    "receipt_body",
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

INSPECTABLY_PRESENT_VALUES = (
    "bounded relevance receipt v2 artifact",
    "referenced bounded relevance reception artifact",
    "received signal id",
    "received relevance basis id",
    "received relevance scope id",
    "received carrier context id",
    "received reception envelope id",
)

UNAVAILABLE_VALUES = (
    "source standing",
    "authority standing",
    "operative currentness",
    "truth claim",
    "action authorization",
    "synchronization authorization",
    "participation authorization",
    "participant role",
    "runtime permission",
    "public interface",
    "distributed network behavior",
    "follow-on work authorization",
)

NON_INFERENCE_KEYS = (
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
    "follow_on_work_authorized",
)

BOOLEAN_OVERREACH_CHECKS = (
    (
        "orientation view does not add new signal",
        "orientation_adds_new_signal",
        "ORIENTATION_ADDED_NEW_SIGNAL",
    ),
    (
        "orientation view does not add new relevance basis",
        "orientation_adds_new_relevance_basis",
        "ORIENTATION_ADDED_NEW_RELEVANCE_BASIS",
    ),
    (
        "orientation view does not add new relevance scope",
        "orientation_adds_new_relevance_scope",
        "ORIENTATION_ADDED_NEW_RELEVANCE_SCOPE",
    ),
    (
        "orientation view does not add new carrier context",
        "orientation_adds_new_carrier_context",
        "ORIENTATION_ADDED_NEW_CARRIER_CONTEXT",
    ),
    (
        "orientation view does not add new envelope",
        "orientation_adds_new_envelope",
        "ORIENTATION_ADDED_NEW_ENVELOPE",
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
    (
        "synchronization not created",
        "synchronization_created",
        "SYNCHRONIZATION_CREATED",
    ),
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
        "artifact existence not orientation authority",
        "artifact_existence_treated_as_orientation_authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_ORIENTATION_AUTHORITY",
    ),
    (
        "latest file posture not orientation authority",
        "latest_file_posture_treated_as_orientation_authority",
        "LATEST_FILE_POSTURE_TREATED_AS_ORIENTATION_AUTHORITY",
    ),
    (
        "repo-local availability not orientation authority",
        "repo_local_availability_treated_as_orientation_authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_ORIENTATION_AUTHORITY",
    ),
    (
        "hidden repo state not orientation content",
        "hidden_repo_state_used_as_orientation_content",
        "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_CONTENT",
    ),
    (
        "hidden repo state not orientation authority",
        "hidden_repo_state_used_as_orientation_authority",
        "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_AUTHORITY",
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
        return {str(item_key): _sanitize(item_value, str(item_key)) for item_key, item_value in value.items()}
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


def _get_nested(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


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


def _extract_receipt_facts(
    receipt_artifact: Mapping[str, Any],
    selected_receipt_path: str | None,
) -> dict[str, Any]:
    metadata = _as_mapping(receipt_artifact.get("bounded_relevance_receipt_metadata"))
    summary = _as_mapping(receipt_artifact.get("bounded_relevance_receipt_summary"))
    receipt_object = _as_mapping(receipt_artifact.get("receipt_object"))

    failed_count = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        receipt_artifact.get("failed_check_count"),
    )

    return {
        "source_receipt_artifact": selected_receipt_path,
        "receipt_outcome": _first_present(
            receipt_artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "receipt_result_version": _first_present(
            metadata.get("bounded_relevance_receipt_version"),
            metadata.get("result_version"),
            summary.get("result_version"),
            receipt_artifact.get("result_version"),
        ),
        "receipt_failed_check_count": failed_count,
        "receipt_object_present": isinstance(receipt_artifact.get("receipt_object"), Mapping),
        "referenced_reception_artifact": receipt_object.get("received_relevance_artifact"),
        "receipt_scope": receipt_object.get("receipt_scope"),
        "receipt_does_not_expand_reception": receipt_object.get("does_not_expand_reception"),
        "received_signal_id": receipt_object.get("received_signal_id"),
        "received_relevance_basis_id": receipt_object.get("received_relevance_basis_id"),
        "received_relevance_scope_id": receipt_object.get("received_relevance_scope_id"),
        "received_carrier_context_id": receipt_object.get("received_carrier_context_id"),
        "received_reception_envelope_id": receipt_object.get("received_reception_envelope_id"),
    }


def _build_orientation_view(
    facts: Mapping[str, Any],
    orientation_scope: str,
) -> dict[str, Any]:
    standing_identifiers = {
        "received_signal_id": facts.get("received_signal_id"),
        "received_relevance_basis_id": facts.get("received_relevance_basis_id"),
        "received_relevance_scope_id": facts.get("received_relevance_scope_id"),
        "received_carrier_context_id": facts.get("received_carrier_context_id"),
        "received_reception_envelope_id": facts.get("received_reception_envelope_id"),
    }

    return {
        "orientation_view_id": "relevance_orientation_view_001",
        "orientation_view_type": "relevance_orientation_view",
        "orientation_view_version": RESULT_VERSION,
        "orientation_scope": orientation_scope,
        "source_receipt_artifact": facts.get("source_receipt_artifact"),
        "referenced_reception_artifact": facts.get("referenced_reception_artifact"),
        "receipt_outcome": facts.get("receipt_outcome"),
        "receipt_result_version": facts.get("receipt_result_version"),
        "receipt_failed_check_count": facts.get("receipt_failed_check_count"),
        "receipt_scope": facts.get("receipt_scope"),
        "receipt_does_not_expand_reception": facts.get("receipt_does_not_expand_reception"),
        "received_signal_id": facts.get("received_signal_id"),
        "received_relevance_basis_id": facts.get("received_relevance_basis_id"),
        "received_relevance_scope_id": facts.get("received_relevance_scope_id"),
        "received_carrier_context_id": facts.get("received_carrier_context_id"),
        "received_reception_envelope_id": facts.get("received_reception_envelope_id"),
        "inspectably_present": list(INSPECTABLY_PRESENT_VALUES),
        "standing_identifiers": standing_identifiers,
        "non_inference": {key: False for key in NON_INFERENCE_KEYS},
        "unavailable": list(UNAVAILABLE_VALUES),
        "orientation_statement": (
            "One clean bounded relevance receipt v2 object and its referenced "
            "bounded relevance reception artifact are inspectably present. The "
            "view orients to preserved identifiers only and does not infer "
            "authority, currentness, truth, action, synchronization, "
            "participation, runtime permission, public interface, distributed "
            "behavior, or follow-on work."
        ),
    }


def _receipt_facts_are_sufficient(facts: Mapping[str, Any]) -> bool:
    return all(
        facts.get(key)
        for key in (
            "source_receipt_artifact",
            "referenced_reception_artifact",
            "received_signal_id",
            "received_relevance_basis_id",
            "received_relevance_scope_id",
            "received_carrier_context_id",
            "received_reception_envelope_id",
        )
    )


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
    receipt_readable: bool,
    receipt_json_object: bool,
    receipt_read_error: str | None,
    reception_readable: bool,
    reception_json_object: bool,
    reception_read_error: str | None,
) -> list[dict[str, Any]]:
    intent = request.get("relevance_orientation_view_intent")
    question = request.get("relevance_orientation_view_question")
    selected_receipt_path = request.get("selected_bounded_relevance_receipt_v2_artifact")
    orientation_scope = request.get("orientation_scope")
    checks: list[dict[str, Any]] = []

    checks.append(
        _check(
            "orientation question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared relevance orientation view question",
            question,
            "RELEVANCE_ORIENTATION_VIEW_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "RELEVANCE_ORIENTATION_VIEW_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block intent not requested",
            intent != INTENT_BLOCK,
            "not BLOCK_RELEVANCE_ORIENTATION_VIEW",
            intent,
            "RELEVANCE_ORIENTATION_VIEW_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "selected bounded relevance receipt v2 artifact path declared",
            bool(selected_receipt_path)
            and request.get("selected_bounded_relevance_receipt_v2_artifact_missing") is not True,
            "selected bounded relevance receipt v2 artifact path declared",
            selected_receipt_path,
            "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected bounded relevance receipt v2 artifact readable JSON",
            bool(selected_receipt_path) and receipt_readable,
            "readable JSON object",
            receipt_read_error or "readable",
            "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _check(
            "selected bounded relevance receipt v2 artifact JSON object",
            bool(selected_receipt_path) and receipt_json_object,
            "JSON object",
            "JSON object" if receipt_json_object else receipt_read_error,
            "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "receipt artifact outcome recorded",
            facts.get("receipt_outcome") == RECEIPT_OUTCOME_RECORDED
            and request.get("selected_bounded_relevance_receipt_v2_artifact_not_recorded") is not True,
            RECEIPT_OUTCOME_RECORDED,
            facts.get("receipt_outcome"),
            "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "receipt artifact result version 0.2.0",
            facts.get("receipt_result_version") == RECEIPT_RESULT_VERSION
            and request.get("selected_bounded_relevance_receipt_v2_artifact_version_not_0_2_0")
            is not True,
            RECEIPT_RESULT_VERSION,
            facts.get("receipt_result_version"),
            "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_VERSION_NOT_0_2_0",
        )
    )
    checks.append(
        _check(
            "receipt artifact failed check count zero",
            facts.get("receipt_failed_check_count") == 0
            and request.get("selected_bounded_relevance_receipt_v2_artifact_failed_checks_present")
            is not True,
            0,
            facts.get("receipt_failed_check_count"),
            "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "receipt object present",
            facts.get("receipt_object_present") is True
            and request.get("receipt_object_missing") is not True,
            "receipt_object mapping present",
            facts.get("receipt_object_present"),
            "RECEIPT_OBJECT_MISSING",
        )
    )
    checks.append(
        _check(
            "receipt object references reception artifact",
            bool(facts.get("referenced_reception_artifact"))
            and request.get("referenced_reception_artifact_missing") is not True,
            "referenced bounded relevance reception artifact path",
            facts.get("referenced_reception_artifact"),
            "REFERENCED_RECEPTION_ARTIFACT_MISSING",
        )
    )
    checks.append(
        _check(
            "referenced reception artifact readable reference",
            bool(facts.get("referenced_reception_artifact"))
            and reception_readable
            and reception_json_object
            and request.get("referenced_reception_artifact_missing") is not True,
            "referenced reception artifact readable JSON object",
            reception_read_error or "readable JSON object",
            "REFERENCED_RECEPTION_ARTIFACT_MISSING",
        )
    )
    checks.append(
        _check(
            "receipt scope inspectable only",
            facts.get("receipt_scope") == RECEIPT_SCOPE_INSPECTABLE_ONLY
            and request.get("receipt_scope_not_inspectable_only") is not True,
            RECEIPT_SCOPE_INSPECTABLE_ONLY,
            facts.get("receipt_scope"),
            "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
        )
    )
    checks.append(
        _check(
            "receipt does not expand reception",
            facts.get("receipt_does_not_expand_reception") is True
            and request.get("receipt_expands_reception") is not True,
            True,
            facts.get("receipt_does_not_expand_reception"),
            "RECEIPT_EXPANDS_RECEPTION",
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
            "orientation scope declared",
            bool(orientation_scope),
            "orientation scope declared",
            orientation_scope,
            "ORIENTATION_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "orientation scope local only",
            orientation_scope == ORIENTATION_SCOPE_LOCAL_ONLY,
            ORIENTATION_SCOPE_LOCAL_ONLY,
            orientation_scope,
            "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
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
                "predecessor_failure_repaired": request.get("predecessor_failure_repaired", False),
                "predecessor_failure_hidden": request.get("predecessor_failure_hidden", False),
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


def _build_block(outcome: str, checks: list[Mapping[str, Any]], request: Mapping[str, Any]) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }

    code = _first_failed_code(checks) or "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_MALFORMED"
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
    orientation_view: Mapping[str, Any],
    facts: Mapping[str, Any],
) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {
        "relevance_orientation_view_recorded": recorded,
        "source_receipt_artifact_preserved": recorded
        and bool(orientation_view.get("source_receipt_artifact")),
        "referenced_reception_artifact_preserved": recorded
        and bool(orientation_view.get("referenced_reception_artifact")),
        "received_signal_id_preserved": recorded
        and orientation_view.get("received_signal_id") == facts.get("received_signal_id"),
        "received_relevance_basis_id_preserved": recorded
        and orientation_view.get("received_relevance_basis_id")
        == facts.get("received_relevance_basis_id"),
        "received_relevance_scope_id_preserved": recorded
        and orientation_view.get("received_relevance_scope_id")
        == facts.get("received_relevance_scope_id"),
        "received_carrier_context_id_preserved": recorded
        and orientation_view.get("received_carrier_context_id")
        == facts.get("received_carrier_context_id"),
        "received_reception_envelope_id_preserved": recorded
        and orientation_view.get("received_reception_envelope_id")
        == facts.get("received_reception_envelope_id"),
        "orientation_scope_local_only": recorded
        and orientation_view.get("orientation_scope") == ORIENTATION_SCOPE_LOCAL_ONLY,
        "orientation_does_not_expand_receipt": recorded,
        "orientation_does_not_expand_reception": recorded
        and orientation_view.get("receipt_does_not_expand_reception") is True,
        "result_level_non_claims_canonical_false": True,
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        statement[key] = False
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
        "orientation_view_is_boundary": False,
        "orientation_view_is_next_layer_selection": False,
        "orientation_view_is_terminal_summary": False,
        "orientation_view_is_source": False,
        "orientation_view_is_authority": False,
        "orientation_view_is_currentness": False,
        "orientation_view_is_truth": False,
        "orientation_view_is_action": False,
        "orientation_view_is_synchronization": False,
        "orientation_view_is_participation_authorization": False,
        "orientation_view_is_runtime_permission": False,
        "orientation_view_is_public_api": False,
        "orientation_view_is_participant_facing_interface": False,
        "orientation_view_is_distributed_network_behavior": False,
        "orientation_view_authorizes_follow_on_work": False,
    }


def _build_what_remains_open() -> list[str]:
    return [
        "relevance orientation view test",
        "relevance orientation view live artifact",
        "relevance orientation view terminal summary, if needed",
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
    if request.get("requested_relevance_orientation_view_outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if request.get("relevance_orientation_view_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _result_from_parts(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    checks: list[dict[str, Any]],
    orientation_view: Mapping[str, Any],
    outcome: str,
    receipt_readable: bool,
    receipt_json_object: bool,
    reception_readable: bool,
    reception_json_object: bool,
) -> dict[str, Any]:
    request_id = str(
        request.get("relevance_orientation_view_request_id")
        or "relevance_orientation_view_request_unidentified"
    )
    block = _build_block(outcome, checks, request)
    failed_check_count = len(_failed_checks(checks))
    passed_check_count = _count_passed(checks)
    metadata = {
        "relevance_orientation_view_id": request_id,
        "relevance_orientation_view_type": "relevance_orientation_view_result",
        "relevance_orientation_view_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "relevance_orientation_view_intent": request.get("relevance_orientation_view_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
    }
    selected_basis = {
        "basis_role": "selected_bounded_relevance_receipt_v2_artifact_reference_only",
        "selected_bounded_relevance_receipt_v2_artifact": request.get(
            "selected_bounded_relevance_receipt_v2_artifact"
        ),
        "receipt_artifact_readable_json": receipt_readable,
        "receipt_artifact_json_object": receipt_json_object,
        "receipt_outcome": facts.get("receipt_outcome"),
        "receipt_result_version": facts.get("receipt_result_version"),
        "receipt_failed_check_count": facts.get("receipt_failed_check_count"),
        "raw_full_body_returned": False,
    }
    referenced_basis = {
        "basis_role": "referenced_bounded_relevance_reception_artifact_reference_only",
        "referenced_bounded_relevance_reception_artifact": facts.get(
            "referenced_reception_artifact"
        ),
        "referenced_reception_artifact_readable_json": reception_readable,
        "referenced_reception_artifact_json_object": reception_json_object,
        "raw_full_body_returned": False,
    }

    result = {
        "relevance_orientation_view_metadata": metadata,
        "declared_relevance_orientation_view_question": _sanitize(
            request.get("relevance_orientation_view_question")
        ),
        "selected_bounded_relevance_receipt_v2_artifact_basis": selected_basis,
        "referenced_bounded_relevance_reception_artifact_basis": referenced_basis,
        "orientation_view": dict(orientation_view),
        "relevance_orientation_view_checks": checks,
        "relevance_orientation_view_statement": _build_statement(
            outcome, orientation_view, facts
        ),
        "relevance_orientation_view_non_meaning": _build_non_meaning(),
        "additional_basis_required": (
            _sanitize(request.get("additional_basis_context"))
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": (
            _sanitize(
                request.get("not_recorded_basis")
                or ["declared intent did not record relevance orientation view"]
            )
            if outcome == OUTCOME_NOT_RECORDED
            else []
        ),
        "what_remains_open": _build_what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
        "relevance_orientation_view_summary": {},
    }
    result["relevance_orientation_view_summary"] = (
        build_relevance_orientation_view_v0_min_summary(result)
    )
    return result


def _malformed_request_result(actual_request: Any) -> dict[str, Any]:
    checks = [
        _check(
            "declared relevance orientation view request mapping",
            False,
            "mapping",
            type(actual_request).__name__,
            "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_MALFORMED",
        )
    ]
    request = {
        "relevance_orientation_view_request_id": "relevance_orientation_view_request_malformed",
        "relevance_orientation_view_question": None,
        "relevance_orientation_view_intent": None,
        "selected_bounded_relevance_receipt_v2_artifact": None,
        "orientation_scope": None,
        "declared_non_claims": {},
    }
    return _result_from_parts(
        request=request,
        facts={},
        checks=checks,
        orientation_view={},
        outcome=OUTCOME_BLOCKED,
        receipt_readable=False,
        receipt_json_object=False,
        reception_readable=False,
        reception_json_object=False,
    )


def resolve_relevance_orientation_view_v0_min(
    declared_relevance_orientation_view_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded local relevance orientation view request."""

    if declared_relevance_orientation_view_request is None:
        declared_relevance_orientation_view_request = (
            build_declared_relevance_orientation_view_v0_min_request()
        )
    if not isinstance(declared_relevance_orientation_view_request, Mapping):
        return _malformed_request_result(declared_relevance_orientation_view_request)

    request = copy.deepcopy(dict(declared_relevance_orientation_view_request))
    selected_receipt_path = request.get("selected_bounded_relevance_receipt_v2_artifact")

    receipt_artifact: Any = {}
    receipt_readable = False
    receipt_json_object = False
    receipt_read_error: str | None = None
    if selected_receipt_path and request.get("selected_bounded_relevance_receipt_v2_artifact_missing") is not True:
        receipt_artifact, receipt_readable, receipt_json_object, receipt_read_error = (
            _read_json_path(selected_receipt_path)
        )
    elif selected_receipt_path:
        receipt_read_error = "selected receipt artifact declared missing by request"
    else:
        receipt_read_error = "selected receipt artifact path missing"

    facts: dict[str, Any] = {}
    if isinstance(receipt_artifact, Mapping):
        facts = _extract_receipt_facts(receipt_artifact, str(selected_receipt_path))

    referenced_reception_path = facts.get("referenced_reception_artifact")
    reception_readable = False
    reception_json_object = False
    reception_read_error: str | None = None
    if referenced_reception_path and request.get("referenced_reception_artifact_missing") is not True:
        _reception_artifact, reception_readable, reception_json_object, reception_read_error = (
            _read_json_path(referenced_reception_path)
        )
    elif referenced_reception_path:
        reception_read_error = "referenced reception artifact declared missing by request"
    else:
        reception_read_error = "referenced reception artifact missing"

    checks = _build_checks(
        request=request,
        facts=facts,
        receipt_readable=receipt_readable,
        receipt_json_object=receipt_json_object,
        receipt_read_error=receipt_read_error,
        reception_readable=reception_readable,
        reception_json_object=reception_json_object,
        reception_read_error=reception_read_error,
    )
    outcome = _determine_outcome(request, checks)

    orientation_scope = request.get("orientation_scope")
    if (
        outcome == OUTCOME_RECORDED
        or (
            _receipt_facts_are_sufficient(facts)
            and orientation_scope == ORIENTATION_SCOPE_LOCAL_ONLY
        )
    ):
        orientation_view = _build_orientation_view(facts, ORIENTATION_SCOPE_LOCAL_ONLY)
    else:
        orientation_view = {}

    return _result_from_parts(
        request=request,
        facts=facts,
        checks=checks,
        orientation_view=orientation_view,
        outcome=outcome,
        receipt_readable=receipt_readable,
        receipt_json_object=receipt_json_object,
        reception_readable=reception_readable,
        reception_json_object=reception_json_object,
    )


def resolve_relevance_orientation_view_v0_min_from_path(
    declared_relevance_orientation_view_request_path: Path | str,
) -> dict:
    """Read a declared request JSON object from path and resolve it."""

    try:
        parsed = json.loads(
            Path(declared_relevance_orientation_view_request_path).read_text(
                encoding="utf-8"
            )
        )
    except OSError as exc:
        raise RelevanceOrientationViewV0MinError(
            f"declared relevance orientation view request unreadable: {exc}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise RelevanceOrientationViewV0MinError(
            f"declared relevance orientation view request is not JSON: {exc}"
        ) from exc

    if not isinstance(parsed, Mapping):
        return _malformed_request_result(parsed)
    return resolve_relevance_orientation_view_v0_min(parsed)


def build_relevance_orientation_view_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a small JSON-safe summary from a resolver result artifact."""

    metadata = _as_mapping(result.get("relevance_orientation_view_metadata"))
    block = _as_mapping(result.get("block"))
    statement = _as_mapping(result.get("relevance_orientation_view_statement"))
    orientation_view = _as_mapping(result.get("orientation_view"))
    selected_basis = _as_mapping(
        result.get("selected_bounded_relevance_receipt_v2_artifact_basis")
    )
    referenced_basis = _as_mapping(
        result.get("referenced_bounded_relevance_reception_artifact_basis")
    )
    non_claims = _as_mapping(result.get("non_claims"))
    checks_value = result.get("relevance_orientation_view_checks")
    checks = checks_value if isinstance(checks_value, list) else []
    passed_check_count = _count_passed(checks)
    failed_check_count = len(_failed_checks(checks))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("relevance_orientation_view_id"),
        "question": result.get("declared_relevance_orientation_view_question"),
        "intent": metadata.get("relevance_orientation_view_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("relevance_orientation_view_version"),
        "resolver_module": metadata.get("resolver_module"),
        "relevance_orientation_view_recorded": statement.get(
            "relevance_orientation_view_recorded", False
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
        "orientation_scope_local_only": statement.get(
            "orientation_scope_local_only", False
        ),
        "orientation_does_not_expand_receipt": statement.get(
            "orientation_does_not_expand_receipt", False
        ),
        "orientation_does_not_expand_reception": statement.get(
            "orientation_does_not_expand_reception", False
        ),
        "orientation_view_summary": {
            "orientation_view_id": orientation_view.get("orientation_view_id"),
            "orientation_view_type": orientation_view.get("orientation_view_type"),
            "orientation_view_version": orientation_view.get("orientation_view_version"),
            "orientation_scope": orientation_view.get("orientation_scope"),
            "source_receipt_artifact": orientation_view.get("source_receipt_artifact"),
            "referenced_reception_artifact": orientation_view.get(
                "referenced_reception_artifact"
            ),
            "receipt_scope": orientation_view.get("receipt_scope"),
            "receipt_does_not_expand_reception": orientation_view.get(
                "receipt_does_not_expand_reception"
            ),
        },
        "inspectably_present_summary": orientation_view.get("inspectably_present", []),
        "standing_identifiers_summary": orientation_view.get("standing_identifiers", {}),
        "non_inference_summary": orientation_view.get("non_inference", {}),
        "unavailable_summary": orientation_view.get("unavailable", []),
        "selected_bounded_relevance_receipt_v2_artifact_path": selected_basis.get(
            "selected_bounded_relevance_receipt_v2_artifact"
        ),
        "referenced_bounded_relevance_reception_artifact_path": referenced_basis.get(
            "referenced_bounded_relevance_reception_artifact"
        ),
        "source_authority_currentness_truth_action_synchronization_participation_runtime_permission_not_created": True,
        "public_api_participant_facing_interface_distributed_network_behavior_not_created": True,
        "operation_permission_follow_on_not_created": True,
        "key_non_claims": {
            key: non_claims.get(key, False)
            for key in (
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


def write_relevance_orientation_view_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result artifact as stable UTF-8 JSON."""

    metadata = _as_mapping(result.get("relevance_orientation_view_metadata"))
    request_id = str(
        metadata.get("relevance_orientation_view_id")
        or "relevance_orientation_view_request_unidentified"
    )

    if output_path is None:
        target_dir = Path(OUTPUT_ROOT)
        target_path = target_dir / f"{request_id}__relevance_orientation_view_v0_min_result.json"
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


def build_declared_relevance_orientation_view_v0_min_request(
    relevance_orientation_view_request_id: str = "relevance_orientation_view_reference_review_001",
    relevance_orientation_view_question: str = CORE_QUESTION,
    relevance_orientation_view_intent: str = INTENT_RECORD,
    selected_bounded_relevance_receipt_v2_artifact: Path | str = DEFAULT_RECEIPT_V2_ARTIFACT,
    orientation_scope: str = ORIENTATION_SCOPE_LOCAL_ONLY,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid declared relevance orientation view request."""

    request = {
        "relevance_orientation_view_request_id": relevance_orientation_view_request_id,
        "relevance_orientation_view_question": relevance_orientation_view_question,
        "relevance_orientation_view_intent": relevance_orientation_view_intent,
        "selected_bounded_relevance_receipt_v2_artifact": str(
            selected_bounded_relevance_receipt_v2_artifact
        ),
        "orientation_scope": orientation_scope,
        "declared_non_claims": (
            _canonical_non_claims()
            if declared_non_claims is None
            else copy.deepcopy(dict(declared_non_claims))
        ),
    }
    request.update(copy.deepcopy(overrides))
    return request
