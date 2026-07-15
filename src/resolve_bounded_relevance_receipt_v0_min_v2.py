"""Bounded relevance receipt resolver V0 minimum, v2.

This module records one small bounded relevance receipt object only. It is the
v2 receipt resolver because it reads the selected bounded relevance reception
JSON artifact and derives the received identifiers from that artifact instead
of relying on declared request fields as the source of those identifiers.

The v1 bounded relevance receipt resolver, tests, and live artifact remain
preserved predecessor evidence. This resolver does not repair, hide, overwrite,
or rename v1.

The resolver is object-shaped, not boundary-shaped. The receipt object points
to the bounded relevance reception artifact, preserves the extracted signal,
basis, scope, carrier-context, and envelope ids, and does not expand reception.
It does not create source transfer, source receipt, reception authorization,
source, authority, currentness, truth, action, synchronization, participation
authorization, participant role, runtime permission, public API,
participant-facing interface, distributed network behavior, deployment, public
release, operation permission, broader reusable permission, derivative
reception, vessel relation, adoption, receiving-context governance,
publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class BoundedRelevanceReceiptV0MinV2Error(Exception):
    """Raised when bounded relevance receipt v2 resolver IO cannot proceed."""


RESULT_VERSION = "0.2.0"
RECEPTION_ARTIFACT_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_bounded_relevance_receipt_v0_min_v2"

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

OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2")

DEFAULT_RECEIVED_RELEVANCE_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
    "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
)
DEFAULT_RECEIVED_ARTIFACT_OUTCOME = "BOUNDED_RELEVANCE_RECEPTION_RECORDED"

CORE_QUESTION = (
    "Given a clean bounded relevance reception artifact, may one bounded "
    "relevance receipt object be recorded by reading that artifact and "
    "extracting its actual received signal id, relevance basis id, relevance "
    "scope id, carrier context id, and bounded relevance reception envelope id, "
    "so the receipt preserves what was actually received without expanding the "
    "reception?"
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
    "artifact_values_extracted_from_reception_artifact",
    "declared_extracted_values_correspond",
    "v1_receipt_artifact_preserved_as_predecessor_evidence",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
    "BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
    "BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_EXTRACTION_FAILED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
    "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_AMBIGUOUS",
    "DECLARED_EXTRACTED_OUTCOME_MISMATCH",
    "DECLARED_EXTRACTED_RESULT_VERSION_MISMATCH",
    "DECLARED_EXTRACTED_FAILED_CHECK_COUNT_MISMATCH",
    "DECLARED_EXTRACTED_SIGNAL_ID_MISMATCH",
    "DECLARED_EXTRACTED_RELEVANCE_BASIS_ID_MISMATCH",
    "DECLARED_EXTRACTED_RELEVANCE_SCOPE_ID_MISMATCH",
    "DECLARED_EXTRACTED_CARRIER_CONTEXT_ID_MISMATCH",
    "DECLARED_EXTRACTED_RECEPTION_ENVELOPE_ID_MISMATCH",
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
    "V1_RECEIPT_ARTIFACT_NOT_PRESERVED_AS_PREDECESSOR_EVIDENCE",
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
    "extracted_bounded_relevance_reception_artifact_facts",
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
        RECEPTION_ARTIFACT_RESULT_VERSION,
        RESOLVER_MODULE,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
        DEFAULT_RECEIVED_ARTIFACT_OUTCOME,
        "bounded_relevance_reception_envelope_001",
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

DECLARED_EXTRACTED_FIELDS = (
    (
        "selected_bounded_relevance_reception_artifact_outcome",
        "received_relevance_artifact_outcome",
        "DECLARED_EXTRACTED_OUTCOME_MISMATCH",
        "declared/extracted outcome correspondence",
    ),
    (
        "selected_bounded_relevance_reception_artifact_result_version",
        "received_relevance_artifact_result_version",
        "DECLARED_EXTRACTED_RESULT_VERSION_MISMATCH",
        "declared/extracted result version correspondence",
    ),
    (
        "selected_bounded_relevance_reception_artifact_failed_check_count",
        "received_relevance_artifact_failed_check_count",
        "DECLARED_EXTRACTED_FAILED_CHECK_COUNT_MISMATCH",
        "declared/extracted failed check count correspondence",
    ),
    (
        "selected_bounded_relevance_reception_signal_id",
        "received_signal_id",
        "DECLARED_EXTRACTED_SIGNAL_ID_MISMATCH",
        "declared/extracted signal id correspondence",
    ),
    (
        "selected_bounded_relevance_reception_basis_id",
        "received_relevance_basis_id",
        "DECLARED_EXTRACTED_RELEVANCE_BASIS_ID_MISMATCH",
        "declared/extracted relevance basis id correspondence",
    ),
    (
        "selected_bounded_relevance_reception_scope_id",
        "received_relevance_scope_id",
        "DECLARED_EXTRACTED_RELEVANCE_SCOPE_ID_MISMATCH",
        "declared/extracted relevance scope id correspondence",
    ),
    (
        "selected_bounded_relevance_reception_carrier_context_id",
        "received_carrier_context_id",
        "DECLARED_EXTRACTED_CARRIER_CONTEXT_ID_MISMATCH",
        "declared/extracted carrier context id correspondence",
    ),
    (
        "selected_bounded_relevance_reception_envelope_id",
        "received_reception_envelope_id",
        "DECLARED_EXTRACTED_RECEPTION_ENVELOPE_ID_MISMATCH",
        "declared/extracted reception envelope id correspondence",
    ),
)

EXTRACTION_ISSUE_CODES_BY_FACT = {
    "received_signal_id": (
        "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
        "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_AMBIGUOUS",
    ),
    "received_relevance_basis_id": (
        "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
        "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_AMBIGUOUS",
    ),
    "received_relevance_scope_id": (
        "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
        "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_AMBIGUOUS",
    ),
    "received_carrier_context_id": (
        "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
        "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_AMBIGUOUS",
    ),
    "received_reception_envelope_id": (
        "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
        "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_AMBIGUOUS",
    ),
}

WHAT_REMAINS_OPEN = (
    "bounded relevance receipt v2 tests",
    "bounded relevance receipt v2 live artifact",
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
    value = str(request.get("bounded_relevance_receipt_request_id") or "bounded_relevance_receipt_v0_min_v2_request")
    cleaned = "".join(character if character.isalnum() or character in ("-", "_") else "_" for character in value)
    return cleaned.strip("_") or "bounded_relevance_receipt_v0_min_v2_request"


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


def _get_path(value: Mapping[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = value
    for part in path:
        if not isinstance(current, Mapping) or part not in current:
            return None
        current = current[part]
    return current


def _path_text(path: tuple[str, ...]) -> str:
    return ".".join(str(part).lower() for part in path)


def _candidate_string(value: Any, prefix: str | None = None) -> str | None:
    if not isinstance(value, str):
        return None
    candidate = value.strip()
    if not candidate:
        return None
    if prefix is not None and not candidate.startswith(prefix):
        return None
    if _contains_raw_sentinel(candidate):
        return None
    return candidate


def _candidate_version(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _candidate_failed_count(value: Any) -> int | None:
    return _as_int(value)


def _walk_candidates(
    value: Any,
    keys: tuple[str, ...],
    predicate: Any,
    path: tuple[str, ...] = (),
    depth: int = 0,
) -> list[Any]:
    if depth > 12:
        return []
    candidates: list[Any] = []
    if isinstance(value, Mapping):
        for raw_key, raw_child in value.items():
            key = str(raw_key)
            lowered_key = key.lower()
            child_path = path + (key,)
            if _sensitive_key(key):
                continue
            if lowered_key in keys:
                candidate = predicate(child_path, raw_child)
                if candidate is not None:
                    candidates.append(candidate)
            candidates.extend(_walk_candidates(raw_child, keys, predicate, child_path, depth + 1))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            candidates.extend(_walk_candidates(item, keys, predicate, path + (str(index),), depth + 1))
    return candidates


def _unique_candidates(candidates: list[Any]) -> list[Any]:
    unique: list[Any] = []
    for candidate in candidates:
        if candidate not in unique:
            unique.append(candidate)
    return unique


def _select_candidate(
    candidates: list[Any],
    missing_code: str,
    ambiguous_code: str,
) -> tuple[Any | None, dict[str, Any] | None]:
    unique = _unique_candidates([candidate for candidate in candidates if candidate is not None])
    if len(unique) == 1:
        return unique[0], None
    if not unique:
        return None, {"code": missing_code, "candidates": []}
    return None, {"code": ambiguous_code, "candidates": _sanitize(unique)}


def _extract_string_fact(
    artifact: Mapping[str, Any],
    paths: tuple[tuple[str, ...], ...],
    keys: tuple[str, ...],
    prefix: str | None,
    missing_code: str,
    ambiguous_code: str,
    context_terms: tuple[str, ...] = (),
    excluded_terms: tuple[str, ...] = (),
) -> tuple[str | None, dict[str, Any] | None]:
    candidates: list[str] = []
    for path in paths:
        value = _candidate_string(_get_path(artifact, path), prefix)
        if value is not None:
            candidates.append(value)

    lowered_keys = tuple(key.lower() for key in keys)

    def predicate(path: tuple[str, ...], value: Any) -> str | None:
        text = _path_text(path)
        if any(term in text for term in excluded_terms):
            return None
        if context_terms and not any(term in text for term in context_terms):
            value_text = value if isinstance(value, str) else ""
            if prefix is None or not value_text.startswith(prefix):
                return None
        return _candidate_string(value, prefix)

    candidates.extend(_walk_candidates(artifact, lowered_keys, predicate))
    selected, issue = _select_candidate(candidates, missing_code, ambiguous_code)
    if isinstance(selected, str) or selected is None:
        return selected, issue
    return None, issue or {"code": missing_code, "candidates": []}


def _extract_failed_count(artifact: Mapping[str, Any]) -> tuple[int | None, dict[str, Any] | None]:
    candidates: list[int] = []
    for path in (
        ("bounded_relevance_reception_summary", "failed_check_count"),
        ("failed_check_count",),
        ("bounded_relevance_reception_metadata", "failed_check_count"),
    ):
        value = _candidate_failed_count(_get_path(artifact, path))
        if value is not None:
            candidates.append(value)

    def predicate(path: tuple[str, ...], value: Any) -> int | None:
        text = _path_text(path)
        if "runtime_loop" in text:
            return None
        return _candidate_failed_count(value)

    candidates.extend(_walk_candidates(artifact, ("failed_check_count",), predicate))
    selected, issue = _select_candidate(
        candidates,
        "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
        "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    if isinstance(selected, int) or selected is None:
        return selected, issue
    return None, issue


def _extract_artifact_facts(artifact: Mapping[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Extract only small receipt-relevant facts from a reception artifact."""

    facts: dict[str, Any] = {}
    issues: list[dict[str, Any]] = []

    outcome_candidates: list[str] = []
    for path in (("outcome",), ("bounded_relevance_reception_summary", "outcome")):
        value = _candidate_string(_get_path(artifact, path))
        if value is not None:
            outcome_candidates.append(value)
    outcome, issue = _select_candidate(
        outcome_candidates,
        "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
        "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
    )
    if outcome is not None:
        facts["received_relevance_artifact_outcome"] = outcome
    elif issue is not None:
        issues.append(issue)

    version_candidates: list[str] = []
    for path in (
        ("bounded_relevance_reception_metadata", "bounded_relevance_reception_version"),
        ("bounded_relevance_reception_metadata", "result_version"),
        ("result_version",),
        ("bounded_relevance_reception_summary", "result_version"),
    ):
        value = _candidate_version(_get_path(artifact, path))
        if value is not None:
            version_candidates.append(value)
    version, issue = _select_candidate(
        version_candidates,
        "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
        "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    if version is not None:
        facts["received_relevance_artifact_result_version"] = version
    elif issue is not None:
        issues.append(issue)

    failed_count, issue = _extract_failed_count(artifact)
    if failed_count is not None:
        facts["received_relevance_artifact_failed_check_count"] = failed_count
    elif issue is not None:
        issues.append(issue)

    extraction_specs = (
        (
            "received_signal_id",
            (
                ("bounded_relevance_signal", "signal_id"),
                ("bounded_relevance_signal", "bounded_relevance_signal_id"),
                ("bounded_relevance_reception_summary", "bounded_relevance_signal_summary", "signal_id"),
            ),
            ("signal_id", "bounded_relevance_signal_id", "relevance_signal_id"),
            "bounded_relevance_signal_",
            "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
            "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_AMBIGUOUS",
            ("bounded_relevance_signal", "relevance_signal"),
            (),
        ),
        (
            "received_relevance_basis_id",
            (
                ("relevance_basis", "basis_id"),
                ("relevance_basis", "relevance_basis_id"),
                ("bounded_relevance_reception_summary", "relevance_basis_summary", "basis_id"),
            ),
            ("basis_id", "relevance_basis_id", "bounded_relevance_basis_id"),
            "bounded_relevance_basis_",
            "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
            "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_AMBIGUOUS",
            ("relevance_basis",),
            (),
        ),
        (
            "received_relevance_scope_id",
            (
                ("relevance_scope", "scope_id"),
                ("relevance_scope", "relevance_scope_id"),
                ("bounded_relevance_reception_summary", "relevance_scope_summary", "scope_id"),
            ),
            ("scope_id", "relevance_scope_id", "bounded_relevance_scope_id"),
            "bounded_relevance_scope_",
            "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
            "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_AMBIGUOUS",
            ("relevance_scope",),
            (),
        ),
        (
            "received_carrier_context_id",
            (
                ("relevance_signal_carrier_context", "context_id"),
                ("relevance_signal_carrier_context", "carrier_context_id"),
                ("relevance_signal_carrier_context", "relevance_signal_carrier_context_id"),
                ("bounded_relevance_reception_summary", "carrier_context_summary", "context_id"),
            ),
            ("context_id", "carrier_context_id", "relevance_signal_carrier_context_id", "received_carrier_context_id"),
            "bounded_relevance_signal_carrier_context_",
            "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
            "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_AMBIGUOUS",
            ("carrier_context",),
            (),
        ),
        (
            "received_reception_envelope_id",
            (
                ("bounded_relevance_reception_envelope", "envelope_id"),
                ("bounded_relevance_reception_envelope", "bounded_relevance_reception_envelope_id"),
                ("bounded_relevance_reception_summary", "bounded_relevance_reception_envelope_summary", "envelope_id"),
            ),
            ("envelope_id", "bounded_relevance_reception_envelope_id", "received_reception_envelope_id"),
            "bounded_relevance_reception_envelope_",
            "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
            "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_AMBIGUOUS",
            ("bounded_relevance_reception_envelope",),
            ("bounded_runtime_loop_envelope", "runtime_loop"),
        ),
    )
    for fact_key, paths, keys, prefix, missing_code, ambiguous_code, context_terms, excluded_terms in extraction_specs:
        selected, issue = _extract_string_fact(
            artifact,
            paths,
            keys,
            prefix,
            missing_code,
            ambiguous_code,
            context_terms,
            excluded_terms,
        )
        if selected is not None:
            facts[fact_key] = selected
        elif issue is not None:
            issues.append(issue)

    return facts, issues


def _read_selected_artifact(request: Mapping[str, Any]) -> tuple[Mapping[str, Any] | None, dict[str, Any], str | None, str | None]:
    artifact_path_value = request.get("selected_bounded_relevance_reception_artifact")
    if not _declared(artifact_path_value) or _flag(request, "selected_bounded_relevance_reception_artifact_missing"):
        return None, {}, "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING", "selected artifact path missing"
    try:
        path = Path(str(artifact_path_value))
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, {}, "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE", f"selected artifact unreadable: {exc}"
    if not isinstance(loaded, Mapping):
        return None, {}, "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT", "selected artifact is not a JSON object"
    facts, issues = _extract_artifact_facts(loaded)
    facts["artifact_extraction_issues"] = issues
    return loaded, facts, None, None


def _issue_code_for_fact(facts: Mapping[str, Any], fact_key: str) -> str | None:
    for issue in facts.get("artifact_extraction_issues", []):
        if isinstance(issue, Mapping) and issue.get("code") in BLOCK_CODES:
            missing_code, ambiguous_code = EXTRACTION_ISSUE_CODES_BY_FACT.get(fact_key, (None, None))
            if issue.get("code") in (missing_code, ambiguous_code):
                return str(issue.get("code"))
    return None


def _declared_matches_extracted(declared_value: Any, extracted_value: Any) -> bool:
    if not _declared(declared_value):
        return True
    if isinstance(extracted_value, int):
        return _as_int(declared_value) == extracted_value
    return str(declared_value) == str(extracted_value)


def _build_checks(
    request: Mapping[str, Any],
    artifact_read_code: str | None,
    artifact_read_reason: str | None,
    facts: Mapping[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    intent = request.get("bounded_relevance_receipt_intent")
    receipt_scope = request.get("receipt_scope")
    extraction_issues = facts.get("artifact_extraction_issues", [])
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
            "bounded relevance receipt block intent not requested",
            intent != INTENT_BLOCK and request.get("requested_bounded_relevance_receipt_outcome") != OUTCOME_BLOCKED,
            "not BLOCK_BOUNDED_RELEVANCE_RECEIPT",
            {
                "bounded_relevance_receipt_intent": intent,
                "requested_bounded_relevance_receipt_outcome": request.get("requested_bounded_relevance_receipt_outcome"),
            },
            "BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact path declared",
            _declared(request.get("selected_bounded_relevance_reception_artifact"))
            and not _flag(request, "selected_bounded_relevance_reception_artifact_missing"),
            "declared bounded relevance reception artifact path",
            request.get("selected_bounded_relevance_reception_artifact"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact readable JSON",
            artifact_read_code is None or artifact_read_code == "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
            "readable JSON artifact",
            artifact_read_reason or "readable JSON artifact",
            artifact_read_code or "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _make_check(
            "selected bounded relevance reception artifact is JSON object",
            artifact_read_code is None,
            "JSON object artifact",
            artifact_read_reason or "JSON object artifact",
            artifact_read_code or "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _make_check(
            "artifact extraction succeeded",
            artifact_read_code is None and not extraction_issues,
            "single unambiguous extracted artifact facts",
            {"artifact_extraction_issues": extraction_issues},
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_EXTRACTION_FAILED",
        )
    )
    checks.append(
        _make_check(
            "extracted artifact outcome recorded",
            facts.get("received_relevance_artifact_outcome") == DEFAULT_RECEIVED_ARTIFACT_OUTCOME
            and not _flag(request, "selected_bounded_relevance_reception_artifact_not_recorded"),
            DEFAULT_RECEIVED_ARTIFACT_OUTCOME,
            facts.get("received_relevance_artifact_outcome"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "extracted artifact version 0.1.0",
            facts.get("received_relevance_artifact_result_version") == RECEPTION_ARTIFACT_RESULT_VERSION
            and not _flag(request, "selected_bounded_relevance_reception_artifact_version_not_0_1_0"),
            RECEPTION_ARTIFACT_RESULT_VERSION,
            facts.get("received_relevance_artifact_result_version"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _make_check(
            "extracted artifact failed check count zero",
            facts.get("received_relevance_artifact_failed_check_count") == 0
            and not _flag(request, "selected_bounded_relevance_reception_artifact_failed_checks_present"),
            "0",
            facts.get("received_relevance_artifact_failed_check_count"),
            "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )

    field_checks = (
        (
            "extracted signal id present",
            "received_signal_id",
            "selected_bounded_relevance_reception_missing_signal_id",
            "one received signal id",
            "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
        ),
        (
            "extracted relevance basis id present",
            "received_relevance_basis_id",
            "selected_bounded_relevance_reception_missing_basis_id",
            "one received relevance basis id",
            "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
        ),
        (
            "extracted relevance scope id present",
            "received_relevance_scope_id",
            "selected_bounded_relevance_reception_missing_scope_id",
            "one received relevance scope id",
            "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
        ),
        (
            "extracted carrier context id present",
            "received_carrier_context_id",
            "selected_bounded_relevance_reception_missing_carrier_context_id",
            "one received carrier context id",
            "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "extracted reception envelope id present",
            "received_reception_envelope_id",
            "selected_bounded_relevance_reception_missing_envelope_id",
            "one received reception envelope id",
            "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
        ),
    )
    for check_name, fact_key, shortcut_key, expected, missing_code in field_checks:
        issue_code = _issue_code_for_fact(facts, fact_key)
        checks.append(
            _make_check(
                check_name,
                _declared(facts.get(fact_key)) and not _flag(request, shortcut_key) and issue_code is None,
                expected,
                facts.get(fact_key),
                issue_code or missing_code,
            )
        )

    for request_key, fact_key, code, check_name in DECLARED_EXTRACTED_FIELDS:
        checks.append(
            _make_check(
                check_name,
                _declared_matches_extracted(request.get(request_key), facts.get(fact_key)),
                "declared value absent or matching extracted artifact value",
                {
                    "declared": request.get(request_key),
                    "extracted": facts.get(fact_key),
                },
                code,
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
    checks.append(
        _make_check(
            "v1 receipt artifact preserved as predecessor evidence",
            request.get("v1_receipt_artifact_preserved_as_predecessor_evidence", True) is True,
            "v1 receipt artifact preserved as predecessor evidence",
            request.get("v1_receipt_artifact_preserved_as_predecessor_evidence", True),
            "V1_RECEIPT_ARTIFACT_NOT_PRESERVED_AS_PREDECESSOR_EVIDENCE",
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
        "basis_role": "selected_bounded_relevance_reception_artifact_reference_only",
        "declared_received_relevance_artifact_outcome": _sanitize(
            request.get("selected_bounded_relevance_reception_artifact_outcome")
        ),
        "declared_received_relevance_artifact_result_version": _sanitize(
            request.get("selected_bounded_relevance_reception_artifact_result_version")
        ),
        "declared_received_relevance_artifact_failed_check_count": request.get(
            "selected_bounded_relevance_reception_artifact_failed_check_count"
        ),
        "declared_received_signal_id": _sanitize(request.get("selected_bounded_relevance_reception_signal_id")),
        "declared_received_relevance_basis_id": _sanitize(request.get("selected_bounded_relevance_reception_basis_id")),
        "declared_received_relevance_scope_id": _sanitize(request.get("selected_bounded_relevance_reception_scope_id")),
        "declared_received_carrier_context_id": _sanitize(
            request.get("selected_bounded_relevance_reception_carrier_context_id")
        ),
        "declared_received_reception_envelope_id": _sanitize(
            request.get("selected_bounded_relevance_reception_envelope_id")
        ),
        "v1_receipt_line_preserved_as_predecessor_evidence": bool(
            request.get("v1_receipt_artifact_preserved_as_predecessor_evidence", True)
        ),
    }


def _public_extracted_facts(facts: Mapping[str, Any]) -> dict[str, Any]:
    public_keys = (
        "received_relevance_artifact_outcome",
        "received_relevance_artifact_result_version",
        "received_relevance_artifact_failed_check_count",
        "received_signal_id",
        "received_relevance_basis_id",
        "received_relevance_scope_id",
        "received_carrier_context_id",
        "received_reception_envelope_id",
    )
    return {key: _sanitize(facts.get(key)) for key in public_keys if key in facts}


def _build_receipt_object(request: Mapping[str, Any], facts: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    if outcome != OUTCOME_RECORDED:
        return {}
    receipt_object: dict[str, Any] = {
        "receipt_id": str(request.get("receipt_id") or "bounded_relevance_receipt_001"),
        "receipt_type": "bounded_relevance_receipt",
        "receipt_version": RESULT_VERSION,
        "received_relevance_artifact": _sanitize(request.get("selected_bounded_relevance_reception_artifact")),
        "received_relevance_artifact_outcome": _sanitize(facts.get("received_relevance_artifact_outcome")),
        "received_relevance_artifact_result_version": _sanitize(facts.get("received_relevance_artifact_result_version")),
        "received_relevance_artifact_failed_check_count": facts.get("received_relevance_artifact_failed_check_count"),
        "received_signal_id": _sanitize(facts.get("received_signal_id")),
        "received_relevance_basis_id": _sanitize(facts.get("received_relevance_basis_id")),
        "received_relevance_scope_id": _sanitize(facts.get("received_relevance_scope_id")),
        "received_carrier_context_id": _sanitize(facts.get("received_carrier_context_id")),
        "received_reception_envelope_id": _sanitize(facts.get("received_reception_envelope_id")),
        "receipt_scope": RECEIPT_SCOPE_INSPECTABLE_ONLY,
        "does_not_expand_reception": True,
    }
    receipt_object.update({key: False for key in RECEIPT_OBJECT_FALSE_FIELDS})
    return receipt_object


def _base_result_from_request(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    request_id = _safe_request_id(request)
    statement = _result_statement(outcome)
    passed_check_count = sum(1 for check in checks if check.get("passed"))
    failed_check_count = len(checks) - passed_check_count
    result: dict[str, Any] = {
        "bounded_relevance_receipt_metadata": {
            "bounded_relevance_receipt_id": request_id,
            "bounded_relevance_receipt_type": "bounded_relevance_receipt_v0_min_v2_result",
            "bounded_relevance_receipt_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "bounded_relevance_receipt_intent": _sanitize(request.get("bounded_relevance_receipt_intent")),
            "passed_check_count": passed_check_count,
            "failed_check_count": failed_check_count,
        },
        "declared_bounded_relevance_receipt_question": _sanitize(request.get("bounded_relevance_receipt_question")),
        "selected_bounded_relevance_reception_artifact_basis": _build_selected_artifact_basis(request),
        "extracted_bounded_relevance_reception_artifact_facts": _public_extracted_facts(facts),
        "receipt_object": _build_receipt_object(request, facts, outcome),
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
            "receipt_object_is_boundary_universe": False,
        },
        "additional_basis_required": _sanitize(request.get("additional_basis_context") or []),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis") or []),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": _build_block(request, outcome, checks),
    }
    result["bounded_relevance_receipt_summary"] = build_bounded_relevance_receipt_v0_min_v2_summary(result)
    return result


def _blocked_malformed_result(code: str, reason: str) -> dict[str, Any]:
    request = {
        "bounded_relevance_receipt_request_id": "bounded_relevance_receipt_v0_min_v2_malformed_request",
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
    return _base_result_from_request(request, {}, checks, OUTCOME_BLOCKED)


def resolve_bounded_relevance_receipt_v0_min_v2(
    declared_bounded_relevance_receipt_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded relevance receipt object from an artifact-backed request."""

    if declared_bounded_relevance_receipt_request is None:
        request = build_declared_bounded_relevance_receipt_v0_min_v2_request()
    elif not isinstance(declared_bounded_relevance_receipt_request, Mapping):
        return _blocked_malformed_result(
            "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
            "declared bounded relevance receipt request is not a mapping",
        )
    else:
        request = _deepcopy_mapping(declared_bounded_relevance_receipt_request)

    _, facts, artifact_read_code, artifact_read_reason = _read_selected_artifact(request)
    checks = _build_checks(request, artifact_read_code, artifact_read_reason, facts)
    outcome = _determine_outcome(request, checks)
    return _base_result_from_request(request, facts, checks, outcome)


def resolve_bounded_relevance_receipt_v0_min_v2_from_path(
    declared_bounded_relevance_receipt_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared bounded relevance receipt v2 request from JSON and resolve it."""

    path = Path(declared_bounded_relevance_receipt_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
        loaded = json.loads(raw_text)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return _blocked_malformed_result(
            "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_UNREADABLE",
            f"declared bounded relevance receipt request unreadable: {exc}",
        )
    return resolve_bounded_relevance_receipt_v0_min_v2(loaded)


def write_bounded_relevance_receipt_v0_min_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded relevance receipt v2 result artifact without overwriting."""

    if not isinstance(result, Mapping):
        raise BoundedRelevanceReceiptV0MinV2Error("result must be a mapping")
    metadata = result.get("bounded_relevance_receipt_metadata", {})
    if isinstance(metadata, Mapping):
        request_id = str(metadata.get("bounded_relevance_receipt_id") or "bounded_relevance_receipt_v0_min_v2_request")
    else:
        request_id = "bounded_relevance_receipt_v0_min_v2_request"
    safe_request_id = "".join(character if character.isalnum() or character in ("-", "_") else "_" for character in request_id)
    filename = f"{safe_request_id}__bounded_relevance_receipt_v0_min_v2_result.json"
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


def build_bounded_relevance_receipt_v0_min_v2_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact bounded relevance receipt v2 summary from a result artifact."""

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
    facts = result.get("extracted_bounded_relevance_reception_artifact_facts", {})
    if not isinstance(facts, Mapping):
        facts = {}
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
        "artifact_values_extracted_from_reception_artifact": bool(
            statement.get("artifact_values_extracted_from_reception_artifact")
        ),
        "declared_extracted_values_correspond": bool(statement.get("declared_extracted_values_correspond")),
        "received_relevance_artifact_preserved": bool(statement.get("received_relevance_artifact_preserved")),
        "received_signal_id_preserved": bool(statement.get("received_signal_id_preserved")),
        "received_relevance_basis_id_preserved": bool(statement.get("received_relevance_basis_id_preserved")),
        "received_relevance_scope_id_preserved": bool(statement.get("received_relevance_scope_id_preserved")),
        "received_carrier_context_id_preserved": bool(statement.get("received_carrier_context_id_preserved")),
        "received_reception_envelope_id_preserved": bool(statement.get("received_reception_envelope_id_preserved")),
        "receipt_scope_inspectable_only": bool(statement.get("receipt_scope_inspectable_only")),
        "receipt_does_not_expand_reception": bool(statement.get("receipt_does_not_expand_reception")),
        "receipt_object_summary": _sanitize(dict(receipt_object)),
        "extracted_artifact_facts_summary": _sanitize(dict(facts)),
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
        "v1_receipt_artifact_preserved_as_predecessor_evidence": bool(
            statement.get("v1_receipt_artifact_preserved_as_predecessor_evidence")
        ),
        "result_level_non_claims_canonical_false": bool(statement.get("result_level_non_claims_canonical_false")),
    }


def build_declared_bounded_relevance_receipt_v0_min_v2_request(
    *,
    bounded_relevance_receipt_request_id: str = "bounded_relevance_receipt_reference_review_001",
    bounded_relevance_receipt_question: str = CORE_QUESTION,
    bounded_relevance_receipt_intent: str = INTENT_RECORD,
    receipt_id: str = "bounded_relevance_receipt_001",
    selected_bounded_relevance_reception_artifact: str = DEFAULT_RECEIVED_RELEVANCE_ARTIFACT,
    receipt_scope: str = RECEIPT_SCOPE_INSPECTABLE_ONLY,
    selected_bounded_relevance_reception_artifact_outcome: str | None = None,
    selected_bounded_relevance_reception_artifact_result_version: str | None = None,
    selected_bounded_relevance_reception_artifact_failed_check_count: int | None = None,
    selected_bounded_relevance_reception_signal_id: str | None = None,
    selected_bounded_relevance_reception_basis_id: str | None = None,
    selected_bounded_relevance_reception_scope_id: str | None = None,
    selected_bounded_relevance_reception_carrier_context_id: str | None = None,
    selected_bounded_relevance_reception_envelope_id: str | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared request for one artifact-backed receipt object."""

    request: dict[str, Any] = {
        "bounded_relevance_receipt_request_id": bounded_relevance_receipt_request_id,
        "bounded_relevance_receipt_question": bounded_relevance_receipt_question,
        "bounded_relevance_receipt_intent": bounded_relevance_receipt_intent,
        "receipt_id": receipt_id,
        "selected_bounded_relevance_reception_artifact": selected_bounded_relevance_reception_artifact,
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
        "v1_receipt_artifact_preserved_as_predecessor_evidence": True,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
    }
    optional_declared_values = {
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
    }
    for key, value in optional_declared_values.items():
        if value is not None:
            request[key] = value
    request.update(copy.deepcopy(overrides))
    return request
