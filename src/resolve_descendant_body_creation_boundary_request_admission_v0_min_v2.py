"""Resolve one exact descendant-body-creation boundary request admission.

This V2 executable follows
DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_V0_MIN_V2_SPEC.  It
preserves the constitutional family version ``0.1.0`` and implements the V2
blocked-first allocation rule.  The resolver compares one closed supplied
envelope only.  It performs no filesystem access, hashing, request formation,
basis consumption, token work, target consideration, invocation, execution,
standing creation, applicability creation, or authority creation.
"""

from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any

import resolve_descendant_body_creation_boundary_request_v0_min as _formation


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_creation_boundary_request_admission_v0_min_v2"
)

REQUEST_ADMISSION_ID = "descendant_body_creation_boundary_request_admission_001"
REQUEST_ADMISSION_TYPE = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION"
REQUEST_ADMISSION_VERSION = "0.1.0"
REQUEST_ADMISSION_SCOPE = (
    "ONE_EXACT_RECORDED_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_ONLY"
)
REQUEST_ADMISSION_QUESTION = (
    "May the exact already-recorded request "
    "descendant_body_creation_boundary_request_001 be admitted for later "
    "separate one-shot consumption review of its already-referenced standing "
    "basis, while preserving the request identity, unchanged target boundary "
    "contract, exact admitted-standing-basis reference and content identity, "
    "complete pair-preserved selected surface, source-family semantic ownership, "
    "exact declared use, freshness and non-replay posture, and all request "
    "non-claims, without consuming or exhausting the basis, closing a consumption "
    "token, authorizing boundary consideration, authorizing invocation, replaying "
    "historical material, or creating standing, applicability, authority, execution "
    "force, descendant-body creation, reuse, continuation, or successor permission?"
)

INTENT_ADMIT = (
    "ADMIT_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_FOR_LATER_ONE_SHOT_"
    "STANDING_BASIS_CONSUMPTION_REVIEW_ONLY"
)
INTENT_DO_NOT_ADMIT = "DO_NOT_ADMIT_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_REVIEW"
SUPPORTED_INTENTS = (INTENT_ADMIT, INTENT_DO_NOT_ADMIT, INTENT_BLOCK)

OUTCOME_ADMITTED = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED"
OUTCOME_NOT_ADMITTED = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_NOT_ADMITTED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_REVIEW_BLOCKED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_REVIEW_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_ADMITTED,
    OUTCOME_NOT_ADMITTED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_REVIEW_BLOCKED,
)

SOURCE_REQUEST_RESULT_REFERENCE = (
    "artifacts/descendant_body_creation_boundary_request_v0_min/"
    "descendant_body_creation_boundary_request_001__"
    "descendant_body_creation_boundary_request_v0_min_result.json"
)
SOURCE_REQUEST_RESULT_CONTENT_IDENTITY = (
    "00ae4d23b703ac57f6eecf684e8c64d8bb7ca7fb0ff418b4d6a453813ffc5ef8"
)

SOURCE_REQUEST_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _formation.REQUIRED_FALSE_NON_CLAIMS
)
SOURCE_RESULT_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _formation.REQUIRED_FALSE_NON_CLAIMS
)

REQUIRED_FALSE_NON_CLAIMS = (
    "admitted_standing_basis_consumed",
    "admitted_standing_basis_exhausted",
    "basis_consumption_performed",
    "basis_exhaustion_performed",
    "consumption_token_created",
    "consumption_token_closed",
    "consumption_authorized",
    "basis_reuse_permission_created",
    "request_reuse_permission_created",
    "later_one_shot_basis_consumption_review_authorized",
    "later_one_shot_basis_consumption_review_scheduled",
    "boundary_consideration_allowed",
    "boundary_consideration_performed",
    "descendant_body_creation_operation_consideration_allowed",
    "descendant_body_creation_authorized",
    "descendant_body_creation_executed",
    "descendant_body_creation_performed",
    "descendant_body_created",
    "invocation_request_admitted",
    "invocation_authorized",
    "invocation_token_created",
    "invocation_performed",
    "execution_permission_created",
    "execution_performed",
    "runtime_created",
    "standing_created",
    "standing_renewed",
    "standing_extended",
    "standing_reinterpreted",
    "standing_transferred",
    "standing_generalized",
    "source_applicability_created",
    "authority_created",
    "semantic_ownership_transferred",
    "custody_transferred",
    "rank_upgraded",
    "candidate_pair_split",
    "candidate_pair_ranked",
    "candidate_a_independently_selected",
    "candidate_b_independently_selected",
    "correspondence_applicability_created",
    "historical_request_identity_reused",
    "historical_request_material_reused",
    "historical_request_reopened",
    "historical_request_mutated",
    "historical_request_replayed",
    "historical_standing_basis_substituted",
    "historical_success_treated_as_fresh_permission",
    "repeat_permission_created",
    "continuation_permission_created",
    "follow_on_permission_created",
    "automatic_successor_created",
    "follow_on_work_authorized",
)
CANONICAL_NON_CLAIMS = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}

ALLOWED_TRUE_ADMISSION_FIELDS = (
    "request_admission_recorded",
    "request_admitted",
    "source_request_result_preserved",
    "recorded_request_object_preserved",
    "request_identity_preserved",
    "target_boundary_contract_preserved",
    "admitted_standing_basis_reference_preserved",
    "basis_reference_posture_preserved",
    "selected_surface_complete_pair_preserved",
    "source_family_semantic_ownership_preserved",
    "declared_matter_use_preserved",
    "freshness_and_non_replay_preserved",
    "historical_completed_lineage_preserved",
    "source_non_claims_preserved",
    "eligible_for_later_separate_one_shot_basis_consumption_review",
    "result_level_non_claims_canonical_false",
)

ENVELOPE_KEYS = frozenset(
    {
        "request_admission_id",
        "request_admission_type",
        "request_admission_version",
        "request_admission_scope",
        "request_admission_question",
        "request_admission_intent",
        "source_request_result_reference",
        "source_request_result_content_identity",
        "source_request_result",
        "recorded_request_object",
        "request_result_binding",
        "admission_declared_matter_use",
        "declared_non_claims",
    }
)

RESULT_KEYS = frozenset(
    {
        "resolver_module",
        "result_version",
        "outcome",
        "request_admission",
        "admitted_request",
        "source_request_result_binding",
        "checks",
        "passed_check_count",
        "failed_check_count",
        "block",
        "review_exhausted",
        "non_claims",
        "what_remains_open",
    }
)

CODE_ADMITTED = "REQUEST_ADMISSION_RECORDED"
CODE_NOT_ADMITTED = "REQUEST_NOT_ADMITTED_BY_EXACT_INTENT"
CODE_ADDITIONAL_BASIS = "ORDINARY_STRUCTURAL_BASIS_MISSING"
CODE_REVIEW_BLOCKED = "REQUEST_ADMISSION_REVIEW_BLOCKED"
CODE_MALFORMED = "REQUEST_ADMISSION_ENVELOPE_MALFORMED"
CODE_SCHEMA = "REQUEST_ADMISSION_SCHEMA_INVALID"
CODE_INTENT_BLOCKED = "REQUEST_ADMISSION_EXPLICITLY_BLOCKED"
CODE_INTENT_UNSUPPORTED = "REQUEST_ADMISSION_INTENT_UNSUPPORTED"
CODE_NON_CLAIM_MISSING = "REQUIRED_NON_CLAIM_MISSING"
CODE_NON_CLAIM_NON_BOOLEAN = "REQUIRED_NON_CLAIM_NON_BOOLEAN"
CODE_NON_CLAIM_TRUE = "REQUIRED_NON_CLAIM_TRUE"
CODE_CONTRADICTION = "REQUEST_ADMISSION_CONTRADICTION"
CODE_BINDING = "REQUEST_RESULT_BINDING_CONTRADICTED"
CODE_PAIR = "PAIR_PRESERVATION_CONTRADICTED"
CODE_SEMANTIC_OWNER = "SEMANTIC_OWNERSHIP_CONTRADICTED"

BLOCK_CODES = frozenset(
    {
        CODE_ADMITTED,
        CODE_NOT_ADMITTED,
        CODE_ADDITIONAL_BASIS,
        CODE_REVIEW_BLOCKED,
        CODE_MALFORMED,
        CODE_SCHEMA,
        CODE_INTENT_BLOCKED,
        CODE_INTENT_UNSUPPORTED,
        CODE_NON_CLAIM_MISSING,
        CODE_NON_CLAIM_NON_BOOLEAN,
        CODE_NON_CLAIM_TRUE,
        CODE_CONTRADICTION,
        CODE_BINDING,
        CODE_PAIR,
        CODE_SEMANTIC_OWNER,
    }
)

CHECK_IDS = frozenset(
    {
        "blocked_condition_precedence_review",
        "ordinary_structural_basis_review",
        "terminal_outcome_allocation",
    }
)

_NON_CLAIM_MAP_PATHS = frozenset(
    {
        ("recorded_request_object", "declared_non_claims"),
        (
            "source_request_result",
            "recorded_request_object",
            "declared_non_claims",
        ),
        ("source_request_result", "non_claims"),
        ("declared_non_claims",),
    }
)

_PAIR_LIST_NAMES = frozenset({"candidate_record_ids", "candidate_basis_ids"})


def _canonical_source_result() -> dict[str, Any]:
    """Reproduce the fixed source result from immutable in-memory fixture material."""

    source_envelope = (
        _formation.build_declared_descendant_body_creation_boundary_request_v0_min_request()
    )
    request_object = copy.deepcopy(source_envelope["request_object"])
    return {
        "resolver_module": _formation.RESOLVER_MODULE,
        "result_version": _formation.RESULT_VERSION,
        "outcome": _formation.OUTCOME_RECORDED,
        "recorded_request_object": request_object,
        "request_formation": {
            key: True for key in _formation.ALLOWED_TRUE_RECORDED_FIELDS
        },
        "historical_completed_lineage": copy.deepcopy(
            source_envelope["historical_completed_lineage"]
        ),
        "checks": [
            {
                "check_id": "closed_request_formation_envelope",
                "passed": True,
                "failure_code": None,
            }
        ],
        "passed_check_count": 1,
        "failed_check_count": 0,
        "block": {
            "blocked": False,
            "code": _formation.CODE_RECORDED,
            "reason": "one exact fresh request object was formed and recorded only",
        },
        "review_exhausted": True,
        "request_admission_performed": False,
        "basis_consumption_performed": False,
        "consumption_token_closed": False,
        "boundary_consideration_performed": False,
        "invocation_performed": False,
        "execution_performed": False,
        "non_claims": copy.deepcopy(_formation.CANONICAL_NON_CLAIMS),
    }


def _canonical_positive_envelope() -> dict[str, Any]:
    source_result = _canonical_source_result()
    request_object = copy.deepcopy(source_result["recorded_request_object"])
    return {
        "request_admission_id": REQUEST_ADMISSION_ID,
        "request_admission_type": REQUEST_ADMISSION_TYPE,
        "request_admission_version": REQUEST_ADMISSION_VERSION,
        "request_admission_scope": REQUEST_ADMISSION_SCOPE,
        "request_admission_question": REQUEST_ADMISSION_QUESTION,
        "request_admission_intent": INTENT_ADMIT,
        "source_request_result_reference": SOURCE_REQUEST_RESULT_REFERENCE,
        "source_request_result_content_identity": (
            SOURCE_REQUEST_RESULT_CONTENT_IDENTITY
        ),
        "source_request_result": source_result,
        "recorded_request_object": request_object,
        "request_result_binding": {
            "request_id": _formation.REQUEST_ID,
            "source_request_result_reference": SOURCE_REQUEST_RESULT_REFERENCE,
            "source_request_result_content_identity": (
                SOURCE_REQUEST_RESULT_CONTENT_IDENTITY
            ),
            "source_request_result_outcome": _formation.OUTCOME_RECORDED,
            "recorded_request_object_matches_source_result": True,
        },
        "admission_declared_matter_use": _formation.DECLARED_MATTER_USE,
        "declared_non_claims": copy.deepcopy(CANONICAL_NON_CLAIMS),
    }


_CANONICAL_POSITIVE_ENVELOPE = _canonical_positive_envelope()


def build_declared_descendant_body_creation_boundary_request_admission_v0_min_v2_request(
    request_admission_intent: str = INTENT_ADMIT,
) -> dict[str, Any]:
    """Return the exact closed in-memory V2 admission envelope."""

    envelope = copy.deepcopy(_CANONICAL_POSITIVE_ENVELOPE)
    envelope["request_admission_intent"] = request_admission_intent
    return envelope


def _path_text(path: tuple[str, ...]) -> str:
    return ".".join(path) if path else "envelope"


def _lookup(root: Any, path: tuple[str, ...]) -> Any:
    current = root
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return _MISSING
        current = current[key]
    return current


_MISSING = object()


def _validate_non_claim_map(
    envelope: Mapping[str, Any],
    parent_path: tuple[str, ...],
    field: str,
    required_keys: tuple[str, ...],
    blocked: list[tuple[str, str]],
) -> None:
    parent = _lookup(envelope, parent_path)
    if parent is _MISSING:
        return
    if not isinstance(parent, Mapping):
        return
    map_path = parent_path + (field,)
    if field not in parent:
        blocked.append(
            (CODE_NON_CLAIM_MISSING, f"required non-claim map absent: {_path_text(map_path)}")
        )
        return
    actual = parent[field]
    if not isinstance(actual, Mapping):
        blocked.append(
            (
                CODE_NON_CLAIM_NON_BOOLEAN,
                f"required non-claim map is not a mapping: {_path_text(map_path)}",
            )
        )
        return

    required = set(required_keys)
    actual_keys = set(actual)
    missing = sorted(required - actual_keys)
    extra = sorted(actual_keys - required)
    if missing:
        blocked.append(
            (
                CODE_NON_CLAIM_MISSING,
                f"required non-claim absent: {_path_text(map_path + (missing[0],))}",
            )
        )
    if extra:
        blocked.append(
            (
                CODE_SCHEMA,
                f"unknown non-claim field: {_path_text(map_path + (extra[0],))}",
            )
        )
    for key in required_keys:
        if key not in actual:
            continue
        value = actual[key]
        if type(value) is not bool:
            blocked.append(
                (
                    CODE_NON_CLAIM_NON_BOOLEAN,
                    f"non-claim must be Boolean: {_path_text(map_path + (key,))}",
                )
            )
        elif value:
            blocked.append(
                (
                    CODE_NON_CLAIM_TRUE,
                    f"prohibited posture claimed: {_path_text(map_path + (key,))}",
                )
            )


def _scan_closed(
    actual: Any,
    expected: Any,
    path: tuple[str, ...],
    blocked: list[tuple[str, str]],
    missing: list[str],
) -> None:
    if path in _NON_CLAIM_MAP_PATHS:
        return

    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            blocked.append(
                (CODE_MALFORMED, f"mapping required at {_path_text(path)}")
            )
            return
        expected_keys = set(expected)
        actual_keys = set(actual)
        for key in sorted(actual_keys - expected_keys):
            blocked.append(
                (CODE_SCHEMA, f"unknown field: {_path_text(path + (key,))}")
            )
        for key in sorted(expected_keys - actual_keys):
            if path == () and key == "request_admission_intent":
                continue
            missing.append(_path_text(path + (key,)))
        for key in expected:
            if key not in actual:
                continue
            if path == () and key == "request_admission_intent":
                continue
            _scan_closed(actual[key], expected[key], path + (key,), blocked, missing)
        return

    if isinstance(expected, list):
        if not isinstance(actual, list):
            blocked.append(
                (CODE_MALFORMED, f"list required at {_path_text(path)}")
            )
            return
        if len(actual) < len(expected):
            if path and path[-1] in _PAIR_LIST_NAMES:
                blocked.append(
                    (CODE_PAIR, f"complete pair not preserved at {_path_text(path)}")
                )
            else:
                missing.append(_path_text(path))
            return
        if len(actual) > len(expected):
            blocked.append((CODE_SCHEMA, f"list widened at {_path_text(path)}"))
            return
        for index, expected_item in enumerate(expected):
            _scan_closed(
                actual[index],
                expected_item,
                path + (f"[{index}]",),
                blocked,
                missing,
            )
        return

    if type(actual) is not type(expected):
        blocked.append(
            (CODE_MALFORMED, f"exact type required at {_path_text(path)}")
        )
        return
    if actual != expected:
        code = CODE_CONTRADICTION
        if path and path[-1] in {
            "recorded_request_object_matches_source_result",
            "source_request_result_reference",
            "source_request_result_content_identity",
            "source_request_result_outcome",
        }:
            code = CODE_BINDING
        elif path and path[-1] in {
            "complete_pair_preserved",
            "candidate_pair_split",
            "candidate_pair_ranked",
            "candidate_a_independently_selected",
            "candidate_b_independently_selected",
        }:
            code = CODE_PAIR
        elif path and path[-1] in {
            "source_family",
            "source_family_semantic_owner",
            "semantic_ownership_transferred",
        }:
            code = CODE_SEMANTIC_OWNER
        blocked.append((code, f"exact value contradicted at {_path_text(path)}"))


def _bounded_admitted_request(envelope: Mapping[str, Any]) -> dict[str, Any]:
    request = envelope["recorded_request_object"]
    basis = request["intended_admitted_standing_basis"]
    standing_binding_keys = (
        "standing_basis_admission_id",
        "standing_basis_admission_type",
        "standing_basis_admission_version",
        "standing_basis_admission_scope",
        "standing_basis_admission_outcome",
        "standing_basis_admission_failed_check_count",
        "standing_basis_admission_review_exhausted",
        "standing_basis_admission_reference",
        "standing_basis_admission_content_identity",
        "standing_basis_admission_declared_use",
    )
    return {
        "request_id": request["request_id"],
        "request_type": request["request_type"],
        "request_version": request["request_version"],
        "request_scope": request["request_scope"],
        "declared_matter_use": request["declared_matter_use"],
        "target_boundary_binding": copy.deepcopy(request["target_boundary"]),
        "standing_basis_admission_binding": {
            key: copy.deepcopy(basis[key]) for key in standing_binding_keys
        },
        "selected_surface_binding": copy.deepcopy(basis["selected_surface"]),
        "basis_reference_posture": copy.deepcopy(
            request["basis_reference_posture"]
        ),
        "freshness_and_non_replay": copy.deepcopy(
            request["freshness_and_non_replay"]
        ),
    }


def _bounded_source_binding(envelope: Mapping[str, Any]) -> dict[str, Any]:
    source = envelope["source_request_result"]
    binding = copy.deepcopy(envelope["request_result_binding"])
    binding.update(
        {
            "source_request_result_resolver_module": source["resolver_module"],
            "source_request_result_version": source["result_version"],
            "source_request_result_review_exhausted": source["review_exhausted"],
            "source_request_result_failed_check_count": source["failed_check_count"],
            "source_request_result_blocked": source["block"]["blocked"],
            "source_request_declared_non_claims_preserved": True,
            "source_request_result_non_claims_preserved": True,
        }
    )
    return binding


def _open_posture() -> dict[str, Any]:
    return {
        "open_items": [
            "request_admission_live_result",
            "artifact",
            "receipt",
            "terminal_summary",
            "later_one_shot_admitted_standing_basis_consumption_review",
            "consumption_identity_or_token",
            "basis_consumption_and_exhaustion",
            "target_boundary_consideration",
            "invocation_request_and_authorization",
            "invocation_and_execution",
            "descendant_body_creation",
            "standing_applicability_or_authority_creation",
            "runtime",
            "successor_work",
        ],
        "open_means_selected": False,
        "open_means_admitted": False,
        "open_means_scheduled": False,
        "open_means_authorized": False,
        "open_means_required": False,
        "open_means_automatic": False,
    }


def _terminal(
    outcome: str,
    supplied_intent: Any,
    blocked_issues: list[tuple[str, str]],
    missing_issues: list[str],
    material_complete: bool,
    envelope: Mapping[str, Any] | None,
) -> dict[str, Any]:
    admitted = outcome == OUTCOME_ADMITTED
    positive = {key: admitted for key in ALLOWED_TRUE_ADMISSION_FIELDS}
    safe_intent = supplied_intent if isinstance(supplied_intent, str) else None

    if outcome == OUTCOME_ADMITTED:
        code = CODE_ADMITTED
        reason = "one exact recorded request was admitted for later separate review only"
    elif outcome == OUTCOME_NOT_ADMITTED:
        code = CODE_NOT_ADMITTED
        reason = "complete exact material carried the exact negative intent"
    elif outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        code = CODE_ADDITIONAL_BASIS
        reason = f"ordinary structural basis absent: {missing_issues[0]}"
    else:
        code, reason = (
            blocked_issues[0]
            if blocked_issues
            else (CODE_REVIEW_BLOCKED, "request-admission review blocked")
        )

    checks = [
        {
            "check_id": "blocked_condition_precedence_review",
            "passed": not blocked_issues,
            "failure_code": blocked_issues[0][0] if blocked_issues else None,
        },
        {
            "check_id": "ordinary_structural_basis_review",
            "passed": not missing_issues,
            "failure_code": CODE_ADDITIONAL_BASIS if missing_issues else None,
        },
        {
            "check_id": "terminal_outcome_allocation",
            "passed": outcome in OUTCOME_FAMILY,
            "failure_code": None,
        },
    ]

    result = {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "request_admission": {
            "request_admission_id": REQUEST_ADMISSION_ID,
            "request_admission_type": REQUEST_ADMISSION_TYPE,
            "request_admission_version": REQUEST_ADMISSION_VERSION,
            "request_admission_scope": REQUEST_ADMISSION_SCOPE,
            "request_admission_question": REQUEST_ADMISSION_QUESTION,
            "request_admission_intent": safe_intent,
            "outcome": outcome,
            **positive,
        },
        "admitted_request": (
            _bounded_admitted_request(envelope)
            if admitted and envelope is not None
            else None
        ),
        "source_request_result_binding": (
            _bounded_source_binding(envelope)
            if material_complete and envelope is not None
            else None
        ),
        "checks": checks,
        "passed_check_count": sum(check["passed"] for check in checks),
        "failed_check_count": sum(not check["passed"] for check in checks),
        "block": {
            "blocked": outcome == OUTCOME_REVIEW_BLOCKED,
            "code": code,
            "reason": reason,
        },
        "review_exhausted": True,
        "non_claims": copy.deepcopy(CANONICAL_NON_CLAIMS),
        "what_remains_open": _open_posture(),
    }
    return result


def resolve_descendant_body_creation_boundary_request_admission_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Allocate exactly one V2 request-admission terminal outcome."""

    if not isinstance(supplied_envelope, Mapping):
        issue = (CODE_MALFORMED, "one supplied admission envelope mapping is required")
        return _terminal(
            OUTCOME_REVIEW_BLOCKED,
            None,
            [issue],
            [],
            False,
            None,
        )

    expected = _CANONICAL_POSITIVE_ENVELOPE
    blocked_issues: list[tuple[str, str]] = []
    missing_issues: list[str] = []

    # Required non-claims are reviewed first so V2 blocked precedence cannot be
    # displaced by an ordinary structural omission elsewhere in the envelope.
    _validate_non_claim_map(
        supplied_envelope,
        ("recorded_request_object",),
        "declared_non_claims",
        SOURCE_REQUEST_REQUIRED_FALSE_NON_CLAIMS,
        blocked_issues,
    )
    _validate_non_claim_map(
        supplied_envelope,
        ("source_request_result", "recorded_request_object"),
        "declared_non_claims",
        SOURCE_REQUEST_REQUIRED_FALSE_NON_CLAIMS,
        blocked_issues,
    )
    _validate_non_claim_map(
        supplied_envelope,
        ("source_request_result",),
        "non_claims",
        SOURCE_RESULT_REQUIRED_FALSE_NON_CLAIMS,
        blocked_issues,
    )
    _validate_non_claim_map(
        supplied_envelope,
        (),
        "declared_non_claims",
        REQUIRED_FALSE_NON_CLAIMS,
        blocked_issues,
    )

    _scan_closed(
        supplied_envelope,
        expected,
        (),
        blocked_issues,
        missing_issues,
    )

    separate_request = supplied_envelope.get("recorded_request_object", _MISSING)
    source_result = supplied_envelope.get("source_request_result", _MISSING)
    wrapped_request = (
        source_result.get("recorded_request_object", _MISSING)
        if isinstance(source_result, Mapping)
        else _MISSING
    )
    if separate_request is not _MISSING and wrapped_request is not _MISSING:
        if separate_request != wrapped_request:
            blocked_issues.append(
                (
                    CODE_BINDING,
                    "separately supplied request does not equal source wrapper request",
                )
            )

    supplied_intent = supplied_envelope.get("request_admission_intent", _MISSING)
    if supplied_intent is _MISSING:
        blocked_issues.append(
            (CODE_INTENT_UNSUPPORTED, "request_admission_intent is absent")
        )
    elif not isinstance(supplied_intent, str):
        blocked_issues.append(
            (CODE_INTENT_UNSUPPORTED, "request_admission_intent must be one exact string")
        )
    elif supplied_intent == INTENT_BLOCK:
        blocked_issues.append(
            (CODE_INTENT_BLOCKED, "exact block intent supplied")
        )
    elif supplied_intent not in {INTENT_ADMIT, INTENT_DO_NOT_ADMIT}:
        blocked_issues.append(
            (CODE_INTENT_UNSUPPORTED, "unsupported request-admission intent")
        )

    material_complete = not blocked_issues and not missing_issues
    if blocked_issues:
        outcome = OUTCOME_REVIEW_BLOCKED
    elif missing_issues:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif supplied_intent == INTENT_DO_NOT_ADMIT:
        outcome = OUTCOME_NOT_ADMITTED
    else:
        outcome = OUTCOME_ADMITTED

    return _terminal(
        outcome,
        supplied_intent,
        blocked_issues,
        missing_issues,
        material_complete,
        supplied_envelope,
    )


__all__ = [
    "ALLOWED_TRUE_ADMISSION_FIELDS",
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "ENVELOPE_KEYS",
    "INTENT_ADMIT",
    "INTENT_BLOCK",
    "INTENT_DO_NOT_ADMIT",
    "OUTCOME_ADMITTED",
    "OUTCOME_FAMILY",
    "OUTCOME_NOT_ADMITTED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "OUTCOME_REVIEW_BLOCKED",
    "REQUEST_ADMISSION_ID",
    "REQUEST_ADMISSION_QUESTION",
    "REQUEST_ADMISSION_SCOPE",
    "REQUEST_ADMISSION_TYPE",
    "REQUEST_ADMISSION_VERSION",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_KEYS",
    "RESULT_VERSION",
    "SOURCE_REQUEST_REQUIRED_FALSE_NON_CLAIMS",
    "SOURCE_RESULT_REQUIRED_FALSE_NON_CLAIMS",
    "SUPPORTED_INTENTS",
    "build_declared_descendant_body_creation_boundary_request_admission_v0_min_v2_request",
    "resolve_descendant_body_creation_boundary_request_admission_v0_min_v2",
]
