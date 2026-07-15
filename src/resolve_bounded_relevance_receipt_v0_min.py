"""Bounded relevance receipt resolver V0 minimum.

This module records one small bounded relevance receipt object only. The
receipt object points to a clean bounded relevance reception artifact and
preserves selected received identifiers without expanding the upstream
reception.

This resolver is object-shaped, not boundary-shaped. It does not create source
transfer, source receipt, reception authorization, source, authority,
currentness, truth, action, synchronization, participation authorization,
participant role, runtime permission, public API, participant-facing interface,
distributed network behavior, deployment, public release, operation permission,
broader reusable permission, derivative reception, vessel relation, adoption,
receiving-context governance, publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class BoundedRelevanceReceiptV0MinError(Exception):
    """Raised when bounded relevance receipt resolver IO cannot proceed."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_bounded_relevance_receipt_v0_min"

OUTCOME_RECORDED = "BOUNDED_RELEVANCE_RECEIPT_RECORDED"
OUTCOME_NOT_RECORDED = "BOUNDED_RELEVANCE_RECEIPT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = "BOUNDED_RELEVANCE_RECEIPT_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "BOUNDED_RELEVANCE_RECEIPT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_BOUNDED_RELEVANCE_RECEIPT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_BOUNDED_RELEVANCE_RECEIPT"
INTENT_BLOCK = "BLOCK_BOUNDED_RELEVANCE_RECEIPT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

RECEIPT_SCOPE_INSPECTABLE_ONLY = "INSPECTABLE_RECEIPT_ONLY"
SUPPORTED_RECEIPT_SCOPE_VALUES = (RECEIPT_SCOPE_INSPECTABLE_ONLY,)

OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min")

DEFAULT_RECEIVED_RELEVANCE_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
    "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
)
DEFAULT_RECEIVED_ARTIFACT_OUTCOME = "BOUNDED_RELEVANCE_RECEPTION_RECORDED"
DEFAULT_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_001"
DEFAULT_RECEIVED_BASIS_ID = "bounded_relevance_basis_001"
DEFAULT_RECEIVED_SCOPE_ID = "bounded_relevance_scope_001"
DEFAULT_RECEIVED_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_001"
DEFAULT_RECEIVED_ENVELOPE_ID = "bounded_relevance_reception_envelope_v0"

CORE_QUESTION = (
    "Given a clean bounded relevance reception artifact, may one bounded "
    "relevance receipt object be recorded that points to that artifact, "
    "preserves its received signal id, relevance basis id, relevance scope id, "
    "carrier context id, and bounded relevance reception envelope id, and makes "
    "the already-recorded reception inspectable without expanding it?"
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
    "receipt_expanded_reception",
    "receipt_created_new_signal",
    "receipt_created_new_relevance_basis",
    "receipt_created_new_relevance_scope",
    "receipt_created_new_carrier_context",
    "artifact_existence_treated_as_receipt_authority",
    "latest_file_posture_treated_as_receipt_authority",
    "repo_local_availability_treated_as_receipt_authority",
    "hidden_repo_state_used_as_receipt_content",
    "hidden_repo_state_used_as_receipt_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "bounded_relevance_receipt_recorded",
    "received_relevance_artifact_preserved",
    "received_signal_id_preserved",
    "received_relevance_basis_id_preserved",
    "received_relevance_scope_id_preserved",
    "received_carrier_context_id_preserved",
    "received_reception_envelope_id_preserved",
    "receipt_scope_inspectable_only",
    "receipt_does_not_expand_reception",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
    "BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
    "BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
    "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
    "RECEIPT_SCOPE_MISSING",
    "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
    "RECEIPT_EXPANDS_RECEPTION",
    "RECEIPT_CREATED_NEW_SIGNAL",
    "RECEIPT_CREATED_NEW_RELEVANCE_BASIS",
    "RECEIPT_CREATED_NEW_RELEVANCE_SCOPE",
    "RECEIPT_CREATED_NEW_CARRIER_CONTEXT",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RECEIPT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
    "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
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

RAW_SENTINELS = (
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

OFFICIAL_SECTION_NAMES = (
    "bounded_relevance_receipt_metadata",
    "declared_bounded_relevance_receipt_question",
    "selected_bounded_relevance_reception_artifact_basis",
    "receipt_object",
    "bounded_relevance_receipt_checks",
    "bounded_relevance_receipt_statement",
    "bounded_relevance_receipt_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "bounded_relevance_receipt_summary",
)

OFFICIAL_BOOLEAN_FIELD_NAMES = REQUIRED_FALSE_NON_CLAIMS + ALLOWED_TRUE_RECORDED_FIELDS
OFFICIAL_STRINGS = (
    set(SUPPORTED_RECEIPT_SCOPE_VALUES)
    | set(OUTCOME_FAMILY)
    | set(BLOCK_CODES)
    | set(OFFICIAL_SECTION_NAMES)
    | set(OFFICIAL_BOOLEAN_FIELD_NAMES)
    | {
        RESULT_VERSION,
        RESOLVER_MODULE,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
        DEFAULT_RECEIVED_ARTIFACT_OUTCOME,
        DEFAULT_RECEIVED_SIGNAL_ID,
        DEFAULT_RECEIVED_BASIS_ID,
        DEFAULT_RECEIVED_SCOPE_ID,
        DEFAULT_RECEIVED_CARRIER_CONTEXT_ID,
        DEFAULT_RECEIVED_ENVELOPE_ID,
    }
)

RECEIPT_OBJECT_FALSE_FIELDS = (
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
    "follow_on_work_authorized",
)

WHAT_REMAINS_OPEN = (
    "bounded relevance receipt resolver tests",
    "bounded relevance receipt live artifact",
    "bounded relevance receipt terminal summary, if needed",
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
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _deepcopy_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def _sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _contains_raw_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in RAW_SENTINELS)


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _sensitive_key(key):
        if value in (None, "", [], {}):
            return value
        if isinstance(value, str) and value in OFFICIAL_STRINGS:
            return value
        if isinstance(value, (list, tuple)) and all(isinstance(item, str) and item in OFFICIAL_STRINGS for item in value):
            return list(value)
        return "[REDACTED_BOUNDED_RELEVANCE_RECEIPT_RAW_BODY]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if _contains_raw_sentinel(value):
            return "[REDACTED_BOUNDED_RELEVANCE_RECEIPT_RAW_BODY]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    return value


def _declared(value: Any) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def _flag(request: Mapping[str, Any], key: str, default: bool = False) -> bool:
    return bool(request.get(key, default))


def _as_int(value: Any) -> int | None:
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


def _safe_request_id(request: Mapping[str, Any]) -> str:
    value = str(request.get("bounded_relevance_receipt_request_id") or "bounded_relevance_receipt_v0_min_request")
    cleaned = "".join(character if character.isalnum() or character in ("-", "_") else "_" for character in value)
    return cleaned.strip("_") or "bounded_relevance_receipt_v0_min_request"


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    check: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": _sanitize(actual_posture),
    }
    if passed:
        check["block_code"] = None
        check["failure_code"] = None
    else:
        check["block_code"] = code
        check["failure_code"] = None
    return check


def _not_flag_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    check_name: str,
    code: str,
) -> None:
    checks.append(
        _make_check(
            check_name,
            not _flag(request, key),
            "false",
            request.get(key, False),
            code,
        )
    )


def _declared_non_claim_failures(request: Mapping[str, Any]) -> list[str]:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return list(REQUIRED_FALSE_NON_CLAIMS)
    failures: list[str] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if declared.get(key) is not False:
            failures.append(key)
    return failures


def _result_statement(outcome: str) -> dict[str, bool]:
    statement = {key: outcome == OUTCOME_RECORDED for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update(_canonical_non_claims())
    return statement


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    intent = request.get("bounded_relevance_receipt_intent")
    receipt_scope = request.get("receipt_scope")
    failed_check_count = _as_int(request.get("selected_bounded_relevance_reception_artifact_failed_check_count"))
    non_claim_failures = _declared_non_claim_failures(request)

    checks.append(
        _make_check(
            "bounded relevance receipt question declared",
            _declared(request.get("bounded_relevance_receipt_question")),
            "declared bounded relevance receipt question",
            request.get("bounded_relevance_receipt_question"),
            "BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _make_check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            f"one of {SUPPORTED_INTENTS}",
            intent,
            "BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact declared",
            _declared(request.get("selected_bounded_relevance_reception_artifact"))
            and not _flag(request, "selected_bounded_relevance_reception_artifact_missing"),
            "declared bounded relevance reception artifact path",
            request.get("selected_bounded_relevance_reception_artifact"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_MISSING",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact outcome recorded",
            request.get("selected_bounded_relevance_reception_artifact_outcome") == DEFAULT_RECEIVED_ARTIFACT_OUTCOME
            and not _flag(request, "selected_bounded_relevance_reception_artifact_not_recorded"),
            DEFAULT_RECEIVED_ARTIFACT_OUTCOME,
            request.get("selected_bounded_relevance_reception_artifact_outcome"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact version 0.1.0",
            request.get("selected_bounded_relevance_reception_artifact_result_version") == RESULT_VERSION
            and not _flag(request, "selected_bounded_relevance_reception_artifact_version_not_0_1_0"),
            RESULT_VERSION,
            request.get("selected_bounded_relevance_reception_artifact_result_version"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact failed check count zero",
            failed_check_count == 0 and not _flag(request, "selected_bounded_relevance_reception_artifact_failed_checks_present"),
            "0",
            request.get("selected_bounded_relevance_reception_artifact_failed_check_count"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact has signal id",
            _declared(request.get("selected_bounded_relevance_reception_signal_id"))
            and not _flag(request, "selected_bounded_relevance_reception_missing_signal_id"),
            "one received signal id",
            request.get("selected_bounded_relevance_reception_signal_id"),
            "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact has relevance basis id",
            _declared(request.get("selected_bounded_relevance_reception_basis_id"))
            and not _flag(request, "selected_bounded_relevance_reception_missing_basis_id"),
            "one received relevance basis id",
            request.get("selected_bounded_relevance_reception_basis_id"),
            "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact has relevance scope id",
            _declared(request.get("selected_bounded_relevance_reception_scope_id"))
            and not _flag(request, "selected_bounded_relevance_reception_missing_scope_id"),
            "one received relevance scope id",
            request.get("selected_bounded_relevance_reception_scope_id"),
            "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact has carrier context id",
            _declared(request.get("selected_bounded_relevance_reception_carrier_context_id"))
            and not _flag(request, "selected_bounded_relevance_reception_missing_carrier_context_id"),
            "one received carrier context id",
            request.get("selected_bounded_relevance_reception_carrier_context_id"),
            "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact has reception envelope id",
            _declared(request.get("selected_bounded_relevance_reception_envelope_id"))
            and not _flag(request, "selected_bounded_relevance_reception_missing_envelope_id"),
            "one received reception envelope id",
            request.get("selected_bounded_relevance_reception_envelope_id"),
            "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
        )
    )
    checks.append(
        _make_check(
            "receipt scope declared",
            _declared(receipt_scope),
            "declared receipt scope",
            receipt_scope,
            "RECEIPT_SCOPE_MISSING",
        )
    )
    checks.append(
        _make_check(
            "receipt scope inspectable only",
            receipt_scope == RECEIPT_SCOPE_INSPECTABLE_ONLY,
            RECEIPT_SCOPE_INSPECTABLE_ONLY,
            receipt_scope,
            "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
        )
    )

    _not_flag_check(request, checks, "receipt_expands_reception", "receipt does not expand reception", "RECEIPT_EXPANDS_RECEPTION")
    _not_flag_check(request, checks, "receipt_creates_new_signal", "receipt does not create new signal", "RECEIPT_CREATED_NEW_SIGNAL")
    _not_flag_check(
        request,
        checks,
        "receipt_creates_new_relevance_basis",
        "receipt does not create new relevance basis",
        "RECEIPT_CREATED_NEW_RELEVANCE_BASIS",
    )
    _not_flag_check(
        request,
        checks,
        "receipt_creates_new_relevance_scope",
        "receipt does not create new relevance scope",
        "RECEIPT_CREATED_NEW_RELEVANCE_SCOPE",
    )
    _not_flag_check(
        request,
        checks,
        "receipt_creates_new_carrier_context",
        "receipt does not create new carrier context",
        "RECEIPT_CREATED_NEW_CARRIER_CONTEXT",
    )
    _not_flag_check(request, checks, "source_transfer_occurred", "source transfer not created", "SOURCE_TRANSFER_OCCURRED")
    _not_flag_check(request, checks, "source_receipt_occurred", "source receipt not created", "SOURCE_RECEIPT_OCCURRED")
    _not_flag_check(
        request,
        checks,
        "reception_authorization_created",
        "reception authorization not created",
        "RECEPTION_AUTHORIZATION_CREATED",
    )
    _not_flag_check(request, checks, "source_created", "source not created", "SOURCE_CREATED")
    _not_flag_check(request, checks, "authority_created", "authority not created", "AUTHORITY_CREATED")
    _not_flag_check(request, checks, "currentness_created", "currentness not created", "CURRENTNESS_CREATED")
    _not_flag_check(request, checks, "truth_created", "truth not created", "TRUTH_CREATED")
    _not_flag_check(request, checks, "action_created", "action not created", "ACTION_CREATED")
    _not_flag_check(request, checks, "synchronization_created", "synchronization not created", "SYNCHRONIZATION_CREATED")
    _not_flag_check(request, checks, "participation_authorized", "participation not authorized", "PARTICIPATION_AUTHORIZED")
    _not_flag_check(request, checks, "participant_role_created", "participant role not created", "PARTICIPANT_ROLE_CREATED")
    _not_flag_check(request, checks, "runtime_permission_created", "runtime permission not created", "RUNTIME_PERMISSION_CREATED")
    _not_flag_check(request, checks, "public_api_created", "public API not created", "PUBLIC_API_CREATED")
    _not_flag_check(
        request,
        checks,
        "participant_facing_interface_created",
        "participant-facing interface not created",
        "PARTICIPANT_FACING_INTERFACE_CREATED",
    )
    _not_flag_check(
        request,
        checks,
        "distributed_network_behavior_created",
        "distributed network behavior not created",
        "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    )
    _not_flag_check(request, checks, "deployment_created", "deployment not created", "DEPLOYMENT_CREATED")
    _not_flag_check(request, checks, "public_release_created", "public release not created", "PUBLIC_RELEASE_CREATED")
    _not_flag_check(request, checks, "operation_permission_created", "operation permission not created", "OPERATION_PERMISSION_CREATED")
    _not_flag_check(
        request,
        checks,
        "broader_reusable_permission_created",
        "broader reusable permission not created",
        "BROADER_REUSABLE_PERMISSION_CREATED",
    )
    _not_flag_check(request, checks, "follow_on_work_authorized", "follow-on work not authorized", "FOLLOW_ON_WORK_AUTHORIZED")
    _not_flag_check(
        request,
        checks,
        "artifact_existence_treated_as_receipt_authority",
        "artifact existence not receipt authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
    )
    _not_flag_check(
        request,
        checks,
        "latest_file_posture_treated_as_receipt_authority",
        "latest file posture not receipt authority",
        "LATEST_FILE_POSTURE_TREATED_AS_RECEIPT_AUTHORITY",
    )
    _not_flag_check(
        request,
        checks,
        "repo_local_availability_treated_as_receipt_authority",
        "repo-local availability not receipt authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
    )
    _not_flag_check(
        request,
        checks,
        "hidden_repo_state_used_as_receipt_content",
        "hidden repo state not receipt content",
        "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    )
    _not_flag_check(
        request,
        checks,
        "hidden_repo_state_used_as_receipt_authority",
        "hidden repo state not receipt authority",
        "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
    )
    checks.append(
        _make_check(
            "predecessor failure evidence preserved",
            not (
                _flag(request, "predecessor_failure_repaired")
                or _flag(request, "predecessor_failure_hidden")
                or _flag(request, "predecessor_failure_claimed_passed")
            ),
            "predecessor failure evidence visible and unrepaired",
            {
                "predecessor_failure_repaired": request.get("predecessor_failure_repaired", False),
                "predecessor_failure_hidden": request.get("predecessor_failure_hidden", False),
                "predecessor_failure_claimed_passed": request.get("predecessor_failure_claimed_passed", False),
            },
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    _not_flag_check(request, checks, "consumed_request_reopened", "consumed request remains closed", "CONSUMED_REQUEST_REOPENED")
    _not_flag_check(request, checks, "authorization_token_reused", "authorization token not reused", "AUTHORIZATION_TOKEN_REUSED")
    checks.append(
        _make_check(
            "result-level required false non-claims canonical false",
            all(value is False for value in _canonical_non_claims().values()),
            "all result-level required false non-claims are false",
            _canonical_non_claims(),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _make_check(
            "required non-claims false",
            not non_claim_failures,
            "declared required non-claims are present and false",
            {"non_claim_failures": non_claim_failures},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if any(not check.get("passed") and check.get("block_code") for check in checks):
        return OUTCOME_BLOCKED
    intent = request.get("bounded_relevance_receipt_intent")
    requested = request.get("requested_bounded_relevance_receipt_outcome")
    if intent == INTENT_BLOCK or requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED or _declared(request.get("not_recorded_basis")):
        return OUTCOME_NOT_RECORDED
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _declared(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return OUTCOME_RECORDED


def _build_block(request: Mapping[str, Any], outcome: str, checks: list[dict[str, Any]]) -> dict[str, Any]:
    failed_codes = [
        check.get("block_code")
        for check in checks
        if not check.get("passed") and check.get("block_code") in BLOCK_CODES
    ]
    if outcome == OUTCOME_BLOCKED and not failed_codes:
        failed_codes = ["BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED"]
    code = failed_codes[0] if failed_codes else None
    reason = request.get("block_reason") or code
    return {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": code,
        "reason": _sanitize(reason),
        "failed_block_codes": failed_codes,
    }


def _build_selected_artifact_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "received_relevance_artifact": _sanitize(request.get("selected_bounded_relevance_reception_artifact")),
        "received_relevance_artifact_outcome": _sanitize(request.get("selected_bounded_relevance_reception_artifact_outcome")),
        "received_relevance_artifact_result_version": _sanitize(
            request.get("selected_bounded_relevance_reception_artifact_result_version")
        ),
        "received_relevance_artifact_failed_check_count": request.get(
            "selected_bounded_relevance_reception_artifact_failed_check_count"
        ),
        "received_signal_id": _sanitize(request.get("selected_bounded_relevance_reception_signal_id")),
        "received_relevance_basis_id": _sanitize(request.get("selected_bounded_relevance_reception_basis_id")),
        "received_relevance_scope_id": _sanitize(request.get("selected_bounded_relevance_reception_scope_id")),
        "received_carrier_context_id": _sanitize(request.get("selected_bounded_relevance_reception_carrier_context_id")),
        "received_reception_envelope_id": _sanitize(request.get("selected_bounded_relevance_reception_envelope_id")),
        "basis_role": "clean_bounded_relevance_reception_artifact_reference_only",
    }


def _build_receipt_object(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    if outcome != OUTCOME_RECORDED:
        return {}
    receipt_object: dict[str, Any] = {
        "receipt_id": str(request.get("receipt_id") or "bounded_relevance_receipt_001"),
        "receipt_type": "bounded_relevance_receipt",
        "receipt_version": RESULT_VERSION,
        "received_relevance_artifact": _sanitize(request.get("selected_bounded_relevance_reception_artifact")),
        "received_relevance_artifact_outcome": _sanitize(request.get("selected_bounded_relevance_reception_artifact_outcome")),
        "received_relevance_artifact_result_version": _sanitize(
            request.get("selected_bounded_relevance_reception_artifact_result_version")
        ),
        "received_relevance_artifact_failed_check_count": request.get(
            "selected_bounded_relevance_reception_artifact_failed_check_count"
        ),
        "received_signal_id": _sanitize(request.get("selected_bounded_relevance_reception_signal_id")),
        "received_relevance_basis_id": _sanitize(request.get("selected_bounded_relevance_reception_basis_id")),
        "received_relevance_scope_id": _sanitize(request.get("selected_bounded_relevance_reception_scope_id")),
        "received_carrier_context_id": _sanitize(request.get("selected_bounded_relevance_reception_carrier_context_id")),
        "received_reception_envelope_id": _sanitize(request.get("selected_bounded_relevance_reception_envelope_id")),
        "receipt_scope": RECEIPT_SCOPE_INSPECTABLE_ONLY,
        "does_not_expand_reception": True,
    }
    receipt_object.update({key: False for key in RECEIPT_OBJECT_FALSE_FIELDS})
    return receipt_object


def _base_result_from_request(request: Mapping[str, Any], checks: list[dict[str, Any]], outcome: str) -> dict[str, Any]:
    request_id = _safe_request_id(request)
    statement = _result_statement(outcome)
    passed_check_count = sum(1 for check in checks if check.get("passed"))
    failed_check_count = len(checks) - passed_check_count
    result: dict[str, Any] = {
        "bounded_relevance_receipt_metadata": {
            "bounded_relevance_receipt_id": request_id,
            "bounded_relevance_receipt_type": "bounded_relevance_receipt_result",
            "bounded_relevance_receipt_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "bounded_relevance_receipt_intent": _sanitize(request.get("bounded_relevance_receipt_intent")),
            "passed_check_count": passed_check_count,
            "failed_check_count": failed_check_count,
        },
        "declared_bounded_relevance_receipt_question": _sanitize(request.get("bounded_relevance_receipt_question")),
        "selected_bounded_relevance_reception_artifact_basis": _build_selected_artifact_basis(request),
        "receipt_object": _build_receipt_object(request, outcome),
        "bounded_relevance_receipt_checks": checks,
        "bounded_relevance_receipt_statement": statement,
        "bounded_relevance_receipt_non_meaning": {
            "boundary_created": False,
            "source_transfer_created": False,
            "source_receipt_created": False,
            "reception_authorization_created": False,
            "authority_created": False,
            "currentness_created": False,
            "truth_created": False,
            "action_created": False,
            "synchronization_created": False,
            "participation_authorization_created": False,
            "participant_role_created": False,
            "runtime_permission_created": False,
            "public_api_created": False,
            "participant_facing_interface_created": False,
            "distributed_network_behavior_created": False,
            "follow_on_work_authorized": False,
        },
        "additional_basis_required": _sanitize(request.get("additional_basis_context") or []),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis") or []),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": _build_block(request, outcome, checks),
    }
    result["bounded_relevance_receipt_summary"] = build_bounded_relevance_receipt_v0_min_summary(result)
    return result


def _blocked_malformed_result(code: str, reason: str) -> dict[str, Any]:
    request = {
        "bounded_relevance_receipt_request_id": "bounded_relevance_receipt_v0_min_malformed_request",
        "bounded_relevance_receipt_question": CORE_QUESTION,
        "bounded_relevance_receipt_intent": INTENT_BLOCK,
        "block_reason": reason,
        "declared_non_claims": _canonical_non_claims(),
    }
    checks = [
        _make_check(
            "declared bounded relevance receipt request readable mapping",
            False,
            "readable mapping request",
            reason,
            code,
        )
    ]
    return _base_result_from_request(request, checks, OUTCOME_BLOCKED)


def resolve_bounded_relevance_receipt_v0_min(
    declared_bounded_relevance_receipt_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded relevance receipt object from a declared request."""

    if declared_bounded_relevance_receipt_request is None:
        request = build_declared_bounded_relevance_receipt_v0_min_request()
    elif not isinstance(declared_bounded_relevance_receipt_request, Mapping):
        return _blocked_malformed_result(
            "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
            "declared bounded relevance receipt request is not a mapping",
        )
    else:
        request = _deepcopy_mapping(declared_bounded_relevance_receipt_request)

    checks = _build_checks(request)
    outcome = _determine_outcome(request, checks)
    return _base_result_from_request(request, checks, outcome)


def resolve_bounded_relevance_receipt_v0_min_from_path(
    declared_bounded_relevance_receipt_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared bounded relevance receipt request from JSON and resolve it."""

    path = Path(declared_bounded_relevance_receipt_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
        loaded = json.loads(raw_text)
    except (OSError, json.JSONDecodeError) as exc:
        return _blocked_malformed_result(
            "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_UNREADABLE",
            f"declared bounded relevance receipt request unreadable: {exc}",
        )
    return resolve_bounded_relevance_receipt_v0_min(loaded)


def write_bounded_relevance_receipt_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded relevance receipt result artifact without overwriting."""

    if not isinstance(result, Mapping):
        raise BoundedRelevanceReceiptV0MinError("result must be a mapping")
    metadata = result.get("bounded_relevance_receipt_metadata", {})
    if isinstance(metadata, Mapping):
        request_id = str(metadata.get("bounded_relevance_receipt_id") or "bounded_relevance_receipt_v0_min_request")
    else:
        request_id = "bounded_relevance_receipt_v0_min_request"
    safe_request_id = "".join(character if character.isalnum() or character in ("-", "_") else "_" for character in request_id)
    filename = f"{safe_request_id}__bounded_relevance_receipt_v0_min_result.json"
    candidate = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    candidate.parent.mkdir(parents=True, exist_ok=True)
    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        parent = candidate.parent
        index = 1
        while True:
            suffixed = parent / f"{stem}_{index:03d}{suffix}"
            if not suffixed.exists():
                candidate = suffixed
                break
            index += 1
    candidate.write_text(json.dumps(_sanitize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return candidate


def build_bounded_relevance_receipt_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact bounded relevance receipt summary from a result artifact."""

    metadata = result.get("bounded_relevance_receipt_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    checks = result.get("bounded_relevance_receipt_checks", [])
    if not isinstance(checks, list):
        checks = []
    statement = result.get("bounded_relevance_receipt_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    block = result.get("block", {})
    if not isinstance(block, Mapping):
        block = {}
    receipt_object = result.get("receipt_object", {})
    if not isinstance(receipt_object, Mapping):
        receipt_object = {}
    selected_basis = result.get("selected_bounded_relevance_reception_artifact_basis", {})
    if not isinstance(selected_basis, Mapping):
        selected_basis = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    passed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed_check_count = len(checks) - passed_check_count
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("bounded_relevance_receipt_id"),
        "question": result.get("declared_bounded_relevance_receipt_question"),
        "intent": metadata.get("bounded_relevance_receipt_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("bounded_relevance_receipt_version"),
        "resolver_module": metadata.get("resolver_module"),
        "bounded_relevance_receipt_recorded": bool(statement.get("bounded_relevance_receipt_recorded")),
        "received_relevance_artifact_preserved": bool(statement.get("received_relevance_artifact_preserved")),
        "received_signal_id_preserved": bool(statement.get("received_signal_id_preserved")),
        "received_relevance_basis_id_preserved": bool(statement.get("received_relevance_basis_id_preserved")),
        "received_relevance_scope_id_preserved": bool(statement.get("received_relevance_scope_id_preserved")),
        "received_carrier_context_id_preserved": bool(statement.get("received_carrier_context_id_preserved")),
        "received_reception_envelope_id_preserved": bool(statement.get("received_reception_envelope_id_preserved")),
        "receipt_scope_inspectable_only": bool(statement.get("receipt_scope_inspectable_only")),
        "receipt_does_not_expand_reception": bool(statement.get("receipt_does_not_expand_reception")),
        "receipt_object_summary": _sanitize(dict(receipt_object)),
        "selected_bounded_relevance_reception_artifact_path": selected_basis.get("received_relevance_artifact"),
        "source_transfer_source_receipt_reception_authorization_not_created": all(
            non_claims.get(key) is False
            for key in ("source_transfer_occurred", "source_receipt_occurred", "reception_authorization_created")
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
        "public_api_interface_distributed_network_not_created": all(
            non_claims.get(key) is False
            for key in (
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
            )
        ),
        "deployment_public_release_operation_permission_follow_on_not_created": all(
            non_claims.get(key) is False
            for key in (
                "deployment_created",
                "public_release_created",
                "operation_permission_created",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": _canonical_non_claims(),
        "predecessor_failure_evidence_preserved": non_claims.get("predecessor_failure_repaired") is False
        and non_claims.get("predecessor_failure_hidden") is False
        and non_claims.get("predecessor_failure_claimed_passed") is False,
        "result_level_non_claims_canonical_false": bool(statement.get("result_level_non_claims_canonical_false")),
    }


def build_declared_bounded_relevance_receipt_v0_min_request(
    *,
    bounded_relevance_receipt_request_id: str = "bounded_relevance_receipt_reference_review_001",
    bounded_relevance_receipt_question: str = CORE_QUESTION,
    bounded_relevance_receipt_intent: str = INTENT_RECORD,
    receipt_id: str = "bounded_relevance_receipt_001",
    selected_bounded_relevance_reception_artifact: str = DEFAULT_RECEIVED_RELEVANCE_ARTIFACT,
    selected_bounded_relevance_reception_artifact_outcome: str = DEFAULT_RECEIVED_ARTIFACT_OUTCOME,
    selected_bounded_relevance_reception_artifact_result_version: str = RESULT_VERSION,
    selected_bounded_relevance_reception_artifact_failed_check_count: int = 0,
    selected_bounded_relevance_reception_signal_id: str = DEFAULT_RECEIVED_SIGNAL_ID,
    selected_bounded_relevance_reception_basis_id: str = DEFAULT_RECEIVED_BASIS_ID,
    selected_bounded_relevance_reception_scope_id: str = DEFAULT_RECEIVED_SCOPE_ID,
    selected_bounded_relevance_reception_carrier_context_id: str = DEFAULT_RECEIVED_CARRIER_CONTEXT_ID,
    selected_bounded_relevance_reception_envelope_id: str = DEFAULT_RECEIVED_ENVELOPE_ID,
    receipt_scope: str = RECEIPT_SCOPE_INSPECTABLE_ONLY,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared request for one bounded relevance receipt object."""

    request: dict[str, Any] = {
        "bounded_relevance_receipt_request_id": bounded_relevance_receipt_request_id,
        "bounded_relevance_receipt_question": bounded_relevance_receipt_question,
        "bounded_relevance_receipt_intent": bounded_relevance_receipt_intent,
        "receipt_id": receipt_id,
        "selected_bounded_relevance_reception_artifact": selected_bounded_relevance_reception_artifact,
        "selected_bounded_relevance_reception_artifact_outcome": selected_bounded_relevance_reception_artifact_outcome,
        "selected_bounded_relevance_reception_artifact_result_version": (
            selected_bounded_relevance_reception_artifact_result_version
        ),
        "selected_bounded_relevance_reception_artifact_failed_check_count": (
            selected_bounded_relevance_reception_artifact_failed_check_count
        ),
        "selected_bounded_relevance_reception_signal_id": selected_bounded_relevance_reception_signal_id,
        "selected_bounded_relevance_reception_basis_id": selected_bounded_relevance_reception_basis_id,
        "selected_bounded_relevance_reception_scope_id": selected_bounded_relevance_reception_scope_id,
        "selected_bounded_relevance_reception_carrier_context_id": selected_bounded_relevance_reception_carrier_context_id,
        "selected_bounded_relevance_reception_envelope_id": selected_bounded_relevance_reception_envelope_id,
        "receipt_scope": receipt_scope,
        "declared_non_claims": _canonical_non_claims(),
        "selected_bounded_relevance_reception_artifact_missing": False,
        "selected_bounded_relevance_reception_artifact_not_recorded": False,
        "selected_bounded_relevance_reception_artifact_failed_checks_present": False,
        "selected_bounded_relevance_reception_artifact_version_not_0_1_0": False,
        "selected_bounded_relevance_reception_missing_signal_id": False,
        "selected_bounded_relevance_reception_missing_basis_id": False,
        "selected_bounded_relevance_reception_missing_scope_id": False,
        "selected_bounded_relevance_reception_missing_carrier_context_id": False,
        "selected_bounded_relevance_reception_missing_envelope_id": False,
        "receipt_expands_reception": False,
        "receipt_creates_new_signal": False,
        "receipt_creates_new_relevance_basis": False,
        "receipt_creates_new_relevance_scope": False,
        "receipt_creates_new_carrier_context": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_created": False,
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
        "deployment_created": False,
        "public_release_created": False,
        "operation_permission_created": False,
        "broader_reusable_permission_created": False,
        "follow_on_work_authorized": False,
        "artifact_existence_treated_as_receipt_authority": False,
        "latest_file_posture_treated_as_receipt_authority": False,
        "repo_local_availability_treated_as_receipt_authority": False,
        "hidden_repo_state_used_as_receipt_content": False,
        "hidden_repo_state_used_as_receipt_authority": False,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
    }
    request.update(copy.deepcopy(overrides))
    return request
