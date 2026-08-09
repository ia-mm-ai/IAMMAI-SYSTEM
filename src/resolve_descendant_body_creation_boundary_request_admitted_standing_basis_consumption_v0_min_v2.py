"""Resolve one exact admitted-standing-basis consumption event.

This executable is governed by the additive V2 articulation for
DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION.
It compares one closed in-memory envelope only.  It performs no filesystem
access, hashing, persistence, upstream resolution, target-boundary
consideration, invocation, execution, standing work, applicability work, or
authority work.
"""

from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2 as _applicability
import resolve_descendant_body_creation_boundary_request_admission_v0_min_v2 as _request_admission
import resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2 as _pre_consumption
import resolve_descendant_body_creation_boundary_request_v0_min as _request_formation
import resolve_matter_bound_selected_surface_standing_basis_admission_v0_min as _standing_basis


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_v0_min_v2"
)
GOVERNING_SPECIFICATION = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_V0_MIN_V2_SPEC.md"
)

CONSUMPTION_TYPE = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION"
)
CONSUMPTION_VERSION = "0.1.0"
CONSUMPTION_SCOPE = (
    "ONE_EXACT_ADMITTED_STANDING_BASIS_ONE_EXACT_ADMITTED_DESCENDANT_BODY_"
    "CREATION_BOUNDARY_REQUEST_ONE_SHOT_CONSUMPTION_AND_EXHAUSTION_ONLY"
)
CONSUMPTION_QUESTION = (
    "May one exact caller-supplied actual-consumption request, identified by "
    "descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_request_001, consume exactly once the exact already-admitted "
    "standing basis matter_bound_selected_surface_standing_basis_admission_001 "
    "into exact admitted request descendant_body_creation_boundary_request_001, "
    "under exact request admission descendant_body_creation_boundary_request_"
    "admission_001 and exact recorded pre-consumption boundary descendant_body_"
    "creation_boundary_request_admitted_standing_basis_consumption_boundary_"
    "request_001, while preserving the complete Candidate A/B pair, source "
    "semantic ownership, declared use, target contract, lineage, custody, rank, "
    "scope, freshness, historical non-replay, and non-claims?"
)

INTENT_RECORD = (
    "RECORD_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
    "BASIS_CONSUMPTION"
)
INTENT_BLOCK = (
    "BLOCK_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_REVIEW"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTCOME_CONSUMED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMED"
)
OUTCOME_NOT_CONSUMED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_NOT_"
    "CONSUMED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_CONSUMED,
    OUTCOME_NOT_CONSUMED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

DEFAULT_REQUEST_CONSUMPTION_REQUEST_ID = (
    "descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_request_001"
)
PRE_CONSUMPTION_RESULT_REFERENCE = (
    "artifacts/descendant_body_creation_boundary_request_admitted_standing_"
    "basis_consumption_boundary_v0_min_v2/descendant_body_creation_boundary_"
    "request_admitted_standing_basis_consumption_boundary_request_001__"
    "descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_boundary_v0_min_v2_result.json"
)
REQUEST_RESULT_REFERENCE = _request_admission.SOURCE_REQUEST_RESULT_REFERENCE
REQUEST_RESULT_CONTENT_IDENTITY = (
    _request_admission.SOURCE_REQUEST_RESULT_CONTENT_IDENTITY
)
REQUEST_ADMISSION_RESULT_REFERENCE = (
    "artifacts/descendant_body_creation_boundary_request_admission_v0_min_v2/"
    "descendant_body_creation_boundary_request_admission_001__"
    "descendant_body_creation_boundary_request_admission_v0_min_v2_result.json"
)
REQUEST_ADMISSION_RESULT_CONTENT_IDENTITY = (
    "57c3272f7a0f3f36678397162573bae0836cf77f1db11ac2bb874efa66ff778d"
)
STANDING_BASIS_ADMISSION_RESULT_REFERENCE = (
    _request_formation.STANDING_BASIS_ADMISSION_REFERENCE
)
STANDING_BASIS_ADMISSION_RESULT_CONTENT_IDENTITY = (
    _request_formation.STANDING_BASIS_ADMISSION_CONTENT_IDENTITY
)

REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _request_formation.REQUIRED_FALSE_NON_CLAIMS
)
REQUEST_ADMISSION_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _request_admission.REQUIRED_FALSE_NON_CLAIMS
)
PRE_CONSUMPTION_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _pre_consumption.REQUIRED_FALSE_NON_CLAIMS
)
STANDING_BASIS_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _standing_basis.REQUIRED_FALSE_NON_CLAIMS
)
SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _applicability.REQUIRED_FALSE_NON_CLAIMS
)
SOURCE_FAMILY_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _applicability.SOURCE_REQUIRED_FALSE_NON_CLAIMS
)

REQUIRED_FALSE_NON_CLAIMS = (
    "consumption_token_created",
    "basis_consumed_twice",
    "basis_exhausted_twice",
    "second_consumption_created",
    "replay_performed",
    "replay_permission_created",
    "sibling_consumption_identity_authorized",
    "distinct_consumption_attempt_authorized",
    "consumption_identity_substituted",
    "request_substituted",
    "request_admission_substituted",
    "pre_consumption_boundary_substituted",
    "standing_basis_substituted",
    "selected_surface_substituted",
    "candidate_pair_split",
    "candidate_pair_ranked",
    "candidate_a_independently_selected",
    "candidate_b_independently_selected",
    "semantic_ownership_transferred",
    "custody_transferred",
    "rank_upgraded",
    "source_route_widened",
    "boundary_consideration_allowed",
    "boundary_consideration_performed",
    "descendant_body_creation_operation_consideration_allowed",
    "invocation_request_admitted",
    "invocation_authorized",
    "invocation_performed",
    "execution_permission_created",
    "execution_performed",
    "descendant_body_creation_authorized",
    "descendant_body_creation_executed",
    "descendant_body_creation_performed",
    "descendant_body_created",
    "standing_created",
    "standing_renewed",
    "standing_extended",
    "standing_reinterpreted",
    "standing_transferred",
    "standing_generalized",
    "source_applicability_created",
    "authority_created",
    "runtime_created",
    "basis_reuse_permission_created",
    "request_reuse_permission_created",
    "repeat_permission_created",
    "continuation_permission_created",
    "follow_on_permission_created",
    "follow_on_work_authorized",
    "automatic_successor_created",
    "registry_created",
    "catalogue_created",
    "ontology_created",
    "generic_consumption_framework_created",
    "cross_family_adapter_created",
    "repository_scan_performed",
    "file_discovery_performed",
    "global_uniqueness_inferred",
    "artifact_existence_treated_as_consumption_law",
)
CANONICAL_NON_CLAIMS = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}

ALLOWED_TRUE_CONSUMED_FIELDS = (
    "basis_consumed",
    "basis_exhausted",
    "basis_consumption_performed",
    "basis_exhaustion_performed",
    "one_shot_consumption_preserved",
    "one_shot_availability_closed",
    "consumed_request_basis_recorded",
    "consumption_token_closed",
    "exact_consumption_identity_preserved",
    "exact_request_preserved",
    "exact_request_admission_preserved",
    "exact_pre_consumption_boundary_preserved",
    "exact_standing_basis_admission_preserved",
    "selected_surface_complete_pair_preserved",
    "source_family_semantic_ownership_preserved",
    "declared_matter_use_preserved",
    "freshness_and_non_replay_preserved",
    "target_boundary_consideration_requires_separate_review",
    "invocation_and_execution_require_separate_review",
    "result_level_non_claims_canonical_false",
)

REQUEST_CONSUMPTION_SCOPE_FAMILY = (
    "REQUEST_CONSUMPTION_ONLY",
    "ADMITTED_STANDING_BASIS_CONSUMED_INTO_ADMITTED_REQUEST_ONLY",
    "ONE_SHOT_CONSUMPTION_AND_EXHAUSTION_ONLY",
    "CONSUMED_BASIS_FOR_LATER_TARGET_BOUNDARY_CONSIDERATION_REVIEW_ONLY",
    "TARGET_BOUNDARY_CONSIDERATION_REQUIRES_SEPARATE_REVIEW",
    "INVOCATION_AND_EXECUTION_REQUIRE_SEPARATE_REVIEW",
    "SELECTED_COMPLETE_PAIR_PRESERVED",
    "SOURCE_SEMANTIC_OWNERSHIP_PRESERVED",
    "REFERENCE_SHAPED_BASIS_REQUIRED",
    "NO_STANDING_CREATED",
    "NO_APPLICABILITY_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_REUSE_OR_REPEAT_PERMISSION_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_AUTOMATIC_SUCCESSOR_CREATED",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
)

PRE_CONSUMPTION_SUPPORTING_CHECK_RECORDS = (
    {
        "check_id": "blocked_condition_precedence_review",
        "passed": True,
        "failure_code": None,
    },
    {
        "check_id": "ordinary_structural_basis_review",
        "passed": True,
        "failure_code": None,
    },
    {
        "check_id": "terminal_outcome_allocation",
        "passed": True,
        "failure_code": None,
    },
)

ENVELOPE_KEYS = frozenset(
    {
        "request_consumption_request_id",
        "declared_request_consumption_question",
        "selected_consumption_boundary_result",
        "selected_request_formation_result",
        "selected_request_admission_result",
        "selected_standing_basis_admission_result",
        "selected_surface_binding",
        "selected_source_applicability_binding",
        "selected_target_boundary_binding",
        "freshness_and_non_replay_posture",
        "one_shot_availability_posture",
        "declared_non_claims",
    }
)
RESULT_KEYS = frozenset(
    {
        "metadata",
        "declared_request_consumption_question",
        "selected_consumption_boundary_result",
        "selected_request_formation_result",
        "selected_request_admission_result",
        "selected_standing_basis_admission_result",
        "selected_surface_binding",
        "selected_source_applicability_binding",
        "selected_target_boundary_binding",
        "freshness_and_non_replay_posture",
        "one_shot_availability_posture",
        "consumption_result",
        "checks",
        "passed_check_count",
        "failed_check_count",
        "review_exhausted",
        "non_claims",
        "outcome",
        "block",
        "what_remains_open",
    }
)

CODE_CONSUMED = "ADMITTED_STANDING_BASIS_CONSUMED"
CODE_NOT_CONSUMED = "ADMITTED_STANDING_BASIS_NOT_CONSUMED_BY_EXACT_INTENT"
CODE_ADDITIONAL_BASIS = "ORDINARY_STRUCTURAL_BASIS_MISSING"
CODE_BLOCKED = "ADMITTED_STANDING_BASIS_CONSUMPTION_BLOCKED"
CODE_MALFORMED = "CONSUMPTION_ENVELOPE_MALFORMED"
CODE_SCHEMA = "CONSUMPTION_ENVELOPE_SCHEMA_INVALID"
CODE_CONTROL = "CONSUMPTION_CONTROL_INVALID"
CODE_INTENT_BLOCKED = "CONSUMPTION_REVIEW_EXPLICITLY_BLOCKED"
CODE_INTENT_UNSUPPORTED = "CONSUMPTION_INTENT_UNSUPPORTED"
CODE_OUTCOME_SELECTION = "CALLER_OUTCOME_SELECTION_BLOCKED"
CODE_REFUSAL_FIELD = "UNDEFINED_REFUSAL_CONTROL_BLOCKED"
CODE_IDENTITY = "ACTUAL_CONSUMPTION_IDENTITY_INVALID"
CODE_IDENTITY_COLLISION = "ACTUAL_CONSUMPTION_IDENTITY_COLLISION"
CODE_EVENT_KEY_MISSING = "CONSTITUTIONAL_EVENT_KEY_MEMBER_MISSING"
CODE_EVENT_KEY_CONTRADICTED = "CONSTITUTIONAL_EVENT_KEY_CONTRADICTED"
CODE_BINDING = "EXACT_EVENT_BINDING_CONTRADICTED"
CODE_PAIR = "COMPLETE_CANDIDATE_PAIR_CONTRADICTED"
CODE_SEMANTIC_OWNER = "SOURCE_SEMANTIC_OWNERSHIP_CONTRADICTED"
CODE_ROUTE = "DECLARED_USE_OR_ROUTE_CONTRADICTED"
CODE_REPLAY = "FRESHNESS_OR_NON_REPLAY_CONTRADICTED"
CODE_NON_CLAIM_MISSING = "REQUIRED_NON_CLAIM_MISSING"
CODE_NON_CLAIM_NON_BOOLEAN = "REQUIRED_NON_CLAIM_NON_BOOLEAN"
CODE_NON_CLAIM_TRUE = "REQUIRED_NON_CLAIM_TRUE"
CODE_ORDINARY_BASIS_INVALID = "ORDINARY_STRUCTURAL_BASIS_INVALID"
CODE_OVERREACH = "ACTUAL_CONSUMPTION_OVERREACH"

BLOCK_CODES = frozenset(
    {
        CODE_CONSUMED,
        CODE_NOT_CONSUMED,
        CODE_ADDITIONAL_BASIS,
        CODE_BLOCKED,
        CODE_MALFORMED,
        CODE_SCHEMA,
        CODE_CONTROL,
        CODE_INTENT_BLOCKED,
        CODE_INTENT_UNSUPPORTED,
        CODE_OUTCOME_SELECTION,
        CODE_REFUSAL_FIELD,
        CODE_IDENTITY,
        CODE_IDENTITY_COLLISION,
        CODE_EVENT_KEY_MISSING,
        CODE_EVENT_KEY_CONTRADICTED,
        CODE_BINDING,
        CODE_PAIR,
        CODE_SEMANTIC_OWNER,
        CODE_ROUTE,
        CODE_REPLAY,
        CODE_NON_CLAIM_MISSING,
        CODE_NON_CLAIM_NON_BOOLEAN,
        CODE_NON_CLAIM_TRUE,
        CODE_ORDINARY_BASIS_INVALID,
        CODE_OVERREACH,
    }
)
CHECK_IDS = frozenset(
    {
        "blocked_condition_precedence_review",
        "ordinary_structural_basis_review",
        "terminal_outcome_allocation",
    }
)

ORDINARY_STRUCTURAL_BASIS_PATHS = (
    ("selected_consumption_boundary_result", "checks"),
)

_MISSING = object()
_DYNAMIC_PATHS = frozenset(
    {
        (
            "declared_request_consumption_question",
            "request_consumption_intent",
        ),
    }
)
_CONTROL_ROOT = ("declared_request_consumption_question",)
_PAIR_LIST_FIELDS = frozenset({"candidate_record_ids", "candidate_basis_ids"})
_OUTCOME_SELECTOR_KEYS = frozenset(
    {
        "requested_terminal_outcome",
        "requested_request_consumption_outcome",
        "requested_consumption_outcome",
        "requested_outcome",
        "desired_outcome",
        "expected_outcome",
        "caller_selected_outcome",
    }
)
_REFUSAL_KEYS = frozenset(
    {
        "not_consumed_basis",
        "lawful_refusal_basis",
        "refusal_basis",
        "refusal_object",
        "refusal_reason",
        "not_consumed_reason",
        "reason_for_not_consuming",
        "free_text_refusal",
    }
)


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _canonical_question(intent: str) -> dict[str, Any]:
    return {
        "request_consumption_type": CONSUMPTION_TYPE,
        "request_consumption_version": CONSUMPTION_VERSION,
        "request_consumption_question": CONSUMPTION_QUESTION,
        "request_consumption_intent": intent,
        "request_consumption_scope_family": list(
            REQUEST_CONSUMPTION_SCOPE_FAMILY
        ),
    }


def _canonical_positive_envelope() -> dict[str, Any]:
    pre = _pre_consumption.build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2_request()
    formation = pre["selected_request_formation_result"]
    request = formation["recorded_request_object"]
    admission = pre["selected_request_admission_result"]
    admission_object = admission["request_admission"]
    standing = pre["selected_standing_basis_admission_result"]
    standing_boundary = standing["boundary"]
    surface = pre["selected_surface_binding"]
    applicability = pre["selected_source_applicability_binding"]
    binding = standing["admission_level_binding"]

    selected_consumption_boundary_result = {
        "result_reference": PRE_CONSUMPTION_RESULT_REFERENCE,
        "consumption_boundary_request_id": (
            _pre_consumption.DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID
        ),
        "consumption_boundary_type": _pre_consumption.CONSUMPTION_BOUNDARY_TYPE,
        "consumption_boundary_version": (
            _pre_consumption.CONSUMPTION_BOUNDARY_VERSION
        ),
        "consumption_boundary_scope": (
            _pre_consumption.CONSUMPTION_BOUNDARY_SCOPE
        ),
        "consumption_boundary_outcome": _pre_consumption.OUTCOME_RECORDED,
        "passed_check_count": 3,
        "failed_check_count": 0,
        "review_exhausted": True,
        "one_shot_consumption_posture": _copy(
            pre["one_shot_consumption_posture"]
        ),
        "checks": _copy(list(PRE_CONSUMPTION_SUPPORTING_CHECK_RECORDS)),
        "non_claims": _copy(_pre_consumption.CANONICAL_NON_CLAIMS),
    }
    selected_request_formation_result = {
        "result_reference": REQUEST_RESULT_REFERENCE,
        "result_content_identity": REQUEST_RESULT_CONTENT_IDENTITY,
        "outcome": formation["outcome"],
        "recorded_request_object": {
            "request_id": request["request_id"],
            "request_type": request["request_type"],
            "request_version": request["request_version"],
            "request_scope": request["request_scope"],
            "declared_matter_use": request["declared_matter_use"],
            "declared_non_claims": _copy(request["declared_non_claims"]),
        },
        "non_claims": _copy(formation["non_claims"]),
    }
    selected_request_admission_result = {
        "result_reference": REQUEST_ADMISSION_RESULT_REFERENCE,
        "result_content_identity": REQUEST_ADMISSION_RESULT_CONTENT_IDENTITY,
        "request_admission_id": admission_object["request_admission_id"],
        "request_admission_type": admission_object["request_admission_type"],
        "request_admission_version": admission_object[
            "request_admission_version"
        ],
        "request_admission_scope": admission_object["request_admission_scope"],
        "request_admission_outcome": admission["outcome"],
        "request_admitted": admission_object["request_admitted"],
        "eligible_for_later_separate_one_shot_basis_consumption_review": (
            admission_object[
                "eligible_for_later_separate_one_shot_basis_consumption_review"
            ]
        ),
        "passed_check_count": admission["passed_check_count"],
        "failed_check_count": admission["failed_check_count"],
        "review_exhausted": admission["review_exhausted"],
        "non_claims": _copy(admission["non_claims"]),
    }
    selected_standing_basis_admission_result = {
        "result_reference": STANDING_BASIS_ADMISSION_RESULT_REFERENCE,
        "result_content_identity": (
            STANDING_BASIS_ADMISSION_RESULT_CONTENT_IDENTITY
        ),
        "standing_basis_admission_id": standing_boundary[
            "matter_bound_selected_surface_standing_basis_admission_id"
        ],
        "standing_basis_admission_type": standing_boundary[
            "matter_bound_selected_surface_standing_basis_admission_type"
        ],
        "standing_basis_admission_version": standing_boundary[
            "matter_bound_selected_surface_standing_basis_admission_version"
        ],
        "standing_basis_admission_scope": standing_boundary[
            "matter_bound_selected_surface_standing_basis_admission_scope"
        ],
        "standing_basis_admission_outcome": standing["outcome"],
        "standing_basis_admission_failed_check_count": standing[
            "failed_check_count"
        ],
        "standing_basis_admission_review_exhausted": standing[
            "review_exhausted"
        ],
        "standing_basis_admission_declared_use": (
            _request_formation.DECLARED_MATTER_USE
        ),
        "non_claims": _copy(standing["non_claims"]),
    }
    selected_surface_binding = {
        key: _copy(surface[key])
        for key in (
            "selected_surface_identity",
            "selected_surface_reference",
            "selected_surface_content_identity",
            "selected_surface_type",
            "selected_surface_version",
            "selected_surface_scope",
            "complete_pair_preserved",
            "candidate_record_ids",
            "candidate_basis_ids",
            "source_family",
            "source_family_semantic_owner",
        )
    }
    selected_surface_binding.update(
        {
            "source_standing_contract_reference": binding[
                "source_standing_contract_reference"
            ],
            "source_standing_contract_content_identity": binding[
                "source_standing_contract_content_identity"
            ],
            "source_standing_result": binding["source_standing_result"],
            "source_lineage": _copy(binding["source_lineage"]),
            "source_custody": _copy(binding["source_custody"]),
            "source_rank": _copy(binding["source_rank"]),
            "source_scope": _copy(binding["source_scope"]),
        }
    )
    selected_source_applicability_binding = {
        "source_applicability_boundary_id": applicability["boundary"][
            "descendant_body_candidate_standing_effect_applicability_boundary_id"
        ],
        "source_applicability_outcome": applicability["outcome"],
        "admissible_future_route": applicability["applicability"][
            "admissible_future_route"
        ],
        "result_reference": applicability["applicability_artifact_reference"],
        "non_claims": _copy(applicability["non_claims"]),
        "source_family_non_claims": _copy(
            applicability["source_family_non_claims"]
        ),
    }

    return {
        "request_consumption_request_id": (
            DEFAULT_REQUEST_CONSUMPTION_REQUEST_ID
        ),
        "declared_request_consumption_question": _canonical_question(
            INTENT_RECORD
        ),
        "selected_consumption_boundary_result": (
            selected_consumption_boundary_result
        ),
        "selected_request_formation_result": selected_request_formation_result,
        "selected_request_admission_result": selected_request_admission_result,
        "selected_standing_basis_admission_result": (
            selected_standing_basis_admission_result
        ),
        "selected_surface_binding": selected_surface_binding,
        "selected_source_applicability_binding": (
            selected_source_applicability_binding
        ),
        "selected_target_boundary_binding": _copy(
            pre["selected_target_boundary_binding"]
        ),
        "freshness_and_non_replay_posture": _copy(
            pre["freshness_and_non_replay_posture"]
        ),
        "one_shot_availability_posture": _copy(
            pre["one_shot_consumption_posture"]
        ),
        "declared_non_claims": _copy(CANONICAL_NON_CLAIMS),
    }


_CANONICAL_POSITIVE_ENVELOPE = _canonical_positive_envelope()


def build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2_request(
    request_consumption_intent: str = INTENT_RECORD,
) -> dict[str, Any]:
    """Build one exact closed in-memory actual-consumption envelope."""

    envelope = _copy(_CANONICAL_POSITIVE_ENVELOPE)
    envelope["declared_request_consumption_question"][
        "request_consumption_intent"
    ] = request_consumption_intent
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


_NON_CLAIM_CONTRACTS = (
    (
        (
            "selected_request_formation_result",
            "recorded_request_object",
            "declared_non_claims",
        ),
        REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_request_formation_result", "non_claims"),
        REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_request_admission_result", "non_claims"),
        REQUEST_ADMISSION_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_consumption_boundary_result", "non_claims"),
        PRE_CONSUMPTION_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_standing_basis_admission_result", "non_claims"),
        STANDING_BASIS_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_source_applicability_binding", "non_claims"),
        SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        (
            "selected_source_applicability_binding",
            "source_family_non_claims",
        ),
        SOURCE_FAMILY_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (("declared_non_claims",), REQUIRED_FALSE_NON_CLAIMS),
)
NON_CLAIM_CONTRACTS = _NON_CLAIM_CONTRACTS
_NON_CLAIM_PATHS = frozenset(path for path, _ in _NON_CLAIM_CONTRACTS)


def _validate_non_claim_map(
    envelope: Mapping[str, Any],
    path: tuple[str, ...],
    required_keys: tuple[str, ...],
    blocked: list[tuple[str, str]],
) -> None:
    parent = _lookup(envelope, path[:-1])
    if parent is _MISSING or not isinstance(parent, Mapping):
        return
    field = path[-1]
    if field not in parent:
        blocked.append(
            (
                CODE_NON_CLAIM_MISSING,
                f"required non-claim map absent: {_path_text(path)}",
            )
        )
        return
    actual = parent[field]
    if not isinstance(actual, Mapping):
        blocked.append(
            (
                CODE_NON_CLAIM_NON_BOOLEAN,
                f"required non-claim map is not a mapping: {_path_text(path)}",
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
                f"required non-claim absent: {_path_text(path + (missing[0],))}",
            )
        )
    if extra:
        blocked.append(
            (
                CODE_SCHEMA,
                f"unknown non-claim field: {_path_text(path + (extra[0],))}",
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
                    f"non-claim must be Boolean: {_path_text(path + (key,))}",
                )
            )
        elif value:
            blocked.append(
                (
                    CODE_NON_CLAIM_TRUE,
                    f"prohibited posture claimed: {_path_text(path + (key,))}",
                )
            )


def _within(path: tuple[str, ...], root: tuple[str, ...]) -> bool:
    return len(path) >= len(root) and path[: len(root)] == root


def _missing_code(path: tuple[str, ...]) -> str:
    if _within(path, _CONTROL_ROOT):
        return CODE_CONTROL
    return CODE_EVENT_KEY_MISSING


def _contradiction_code(path: tuple[str, ...]) -> str:
    last = path[-1] if path else ""
    if last in {
        "result_reference",
        "result_content_identity",
        "target_boundary_contract_reference",
        "target_boundary_contract_content_identity",
    }:
        return CODE_BINDING
    if last in {
        "complete_pair_preserved",
        "candidate_record_ids",
        "candidate_basis_ids",
    }:
        return CODE_PAIR
    if last in {"source_family", "source_family_semantic_owner"}:
        return CODE_SEMANTIC_OWNER
    if "route" in last or "declared_matter_use" in last:
        return CODE_ROUTE
    if last.startswith("historical_") or last.startswith("fresh_"):
        return CODE_REPLAY
    if last in REQUIRED_FALSE_NON_CLAIMS:
        return CODE_OVERREACH
    return CODE_EVENT_KEY_CONTRADICTED


def _scan_closed(
    actual: Any,
    expected: Any,
    path: tuple[str, ...],
    blocked: list[tuple[str, str]],
    missing_basis: list[str],
) -> None:
    if path in _NON_CLAIM_PATHS:
        return

    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            code = CODE_CONTROL if _within(path, _CONTROL_ROOT) else CODE_MALFORMED
            blocked.append((code, f"mapping required at {_path_text(path)}"))
            return
        expected_keys = set(expected)
        actual_keys = set(actual)
        for key in sorted(actual_keys - expected_keys):
            blocked.append(
                (CODE_SCHEMA, f"unknown field: {_path_text(path + (key,))}")
            )
        for key in sorted(expected_keys - actual_keys):
            field_path = path + (key,)
            if field_path in _NON_CLAIM_PATHS:
                continue
            if field_path in ORDINARY_STRUCTURAL_BASIS_PATHS:
                missing_basis.append(_path_text(field_path))
            else:
                blocked.append(
                    (
                        _missing_code(field_path),
                        f"required event material absent: {_path_text(field_path)}",
                    )
                )
        for key in expected:
            if key in actual:
                _scan_closed(
                    actual[key],
                    expected[key],
                    path + (key,),
                    blocked,
                    missing_basis,
                )
        return

    if isinstance(expected, list):
        if not isinstance(actual, list):
            code = (
                CODE_ORDINARY_BASIS_INVALID
                if path in ORDINARY_STRUCTURAL_BASIS_PATHS
                else CODE_MALFORMED
            )
            blocked.append((code, f"list required at {_path_text(path)}"))
            return
        if len(actual) != len(expected):
            if path in ORDINARY_STRUCTURAL_BASIS_PATHS:
                code = CODE_ORDINARY_BASIS_INVALID
            elif path and path[-1] in _PAIR_LIST_FIELDS:
                code = CODE_PAIR
            else:
                code = CODE_EVENT_KEY_CONTRADICTED
            blocked.append((code, f"exact list required at {_path_text(path)}"))
            return
        for index, expected_item in enumerate(expected):
            _scan_closed(
                actual[index],
                expected_item,
                path + (f"[{index}]",),
                blocked,
                missing_basis,
            )
        return

    if path in _DYNAMIC_PATHS:
        return
    if type(actual) is not type(expected):
        code = (
            CODE_ORDINARY_BASIS_INVALID
            if any(_within(path, root) for root in ORDINARY_STRUCTURAL_BASIS_PATHS)
            else CODE_MALFORMED
        )
        blocked.append((code, f"exact type required at {_path_text(path)}"))
        return
    if actual != expected:
        code = (
            CODE_ORDINARY_BASIS_INVALID
            if any(_within(path, root) for root in ORDINARY_STRUCTURAL_BASIS_PATHS)
            else _contradiction_code(path)
        )
        blocked.append((code, f"exact value contradicted at {_path_text(path)}"))


def _contains_named_key(value: Any, names: frozenset[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            normalized = str(key).lower()
            if normalized in names:
                return True
            if _contains_named_key(item, names):
                return True
    elif isinstance(value, list):
        return any(_contains_named_key(item, names) for item in value)
    return False


def _contains_outcome_selector(value: Any) -> bool:
    if _contains_named_key(value, _OUTCOME_SELECTOR_KEYS):
        return True
    if isinstance(value, Mapping):
        for key, item in value.items():
            normalized = str(key).lower()
            if "outcome" in normalized and any(
                token in normalized
                for token in ("requested", "desired", "expected", "caller_selected")
            ):
                return True
            if _contains_outcome_selector(item):
                return True
    elif isinstance(value, list):
        return any(_contains_outcome_selector(item) for item in value)
    return False


def _identity_issues(envelope: Mapping[str, Any]) -> list[tuple[str, str]]:
    value = envelope.get("request_consumption_request_id", _MISSING)
    if value is _MISSING:
        return [(CODE_IDENTITY, "request_consumption_request_id is absent")]
    if not isinstance(value, str) or not value.strip():
        return [
            (
                CODE_IDENTITY,
                "request_consumption_request_id must be one non-empty string",
            )
        ]

    collisions = {
        _request_formation.REQUEST_ID,
        _request_admission.REQUEST_ADMISSION_ID,
        _pre_consumption.DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID,
        _standing_basis.BOUNDARY_ID,
        _request_formation.SELECTED_SURFACE_IDENTITY,
        _request_formation.SOURCE_APPLICABILITY_BOUNDARY_ID,
        _request_formation.TARGET_BOUNDARY_ID,
        REQUEST_RESULT_CONTENT_IDENTITY,
        REQUEST_ADMISSION_RESULT_CONTENT_IDENTITY,
        STANDING_BASIS_ADMISSION_RESULT_CONTENT_IDENTITY,
        _request_formation.SELECTED_SURFACE_CONTENT_IDENTITY,
        _request_formation.TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY,
        _request_formation.HISTORICAL_BOUNDARY_RESULT_CONTENT_IDENTITY,
    }
    if value in collisions:
        return [
            (
                CODE_IDENTITY_COLLISION,
                "actual-consumption identity collides with bound or historical identity",
            )
        ]
    if value != DEFAULT_REQUEST_CONSUMPTION_REQUEST_ID:
        return [
            (
                CODE_IDENTITY,
                "sibling actual-consumption identity is not authorized by this lineage",
            )
        ]
    return []


def _open_posture() -> dict[str, Any]:
    return {
        "open_items": [
            "live_actual_consumption_result",
            "artifact",
            "receipt",
            "terminal_summary",
            "later_target_boundary_consideration",
            "invocation_request_admission_and_authorization",
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
    supplied_envelope: Mapping[str, Any] | None,
    supplied_intent: Any,
    blocked_issues: list[tuple[str, str]],
    missing_basis: list[str],
) -> dict[str, Any]:
    consumed = outcome == OUTCOME_CONSUMED
    positive = {key: consumed for key in ALLOWED_TRUE_CONSUMED_FIELDS}
    safe_intent = supplied_intent if supplied_intent in SUPPORTED_INTENTS else None
    safe_id = None
    if supplied_envelope is not None and not _identity_issues(supplied_envelope):
        safe_id = supplied_envelope.get("request_consumption_request_id")

    if outcome == OUTCOME_CONSUMED:
        code = CODE_CONSUMED
        reason = "one exact admitted standing basis was consumed and exhausted once"
    elif outcome == OUTCOME_NOT_CONSUMED:
        code = CODE_NOT_CONSUMED
        reason = "complete exact material carried the sole exact negative intent"
    elif outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        code = CODE_ADDITIONAL_BASIS
        reason = f"ordinary structural basis absent: {missing_basis[0]}"
    else:
        code, reason = (
            blocked_issues[0]
            if blocked_issues
            else (CODE_BLOCKED, "actual-consumption review blocked")
        )

    checks = [
        {
            "check_id": "blocked_condition_precedence_review",
            "passed": not blocked_issues,
            "failure_code": blocked_issues[0][0] if blocked_issues else None,
        },
        {
            "check_id": "ordinary_structural_basis_review",
            "passed": not missing_basis,
            "failure_code": CODE_ADDITIONAL_BASIS if missing_basis else None,
        },
        {
            "check_id": "terminal_outcome_allocation",
            "passed": outcome in OUTCOME_FAMILY,
            "failure_code": None,
        },
    ]

    project_sources = supplied_envelope is not None and not blocked_issues
    section_names = (
        "selected_consumption_boundary_result",
        "selected_request_formation_result",
        "selected_request_admission_result",
        "selected_standing_basis_admission_result",
        "selected_surface_binding",
        "selected_source_applicability_binding",
        "selected_target_boundary_binding",
        "freshness_and_non_replay_posture",
        "one_shot_availability_posture",
    )
    sections = {
        name: (
            _copy(supplied_envelope[name])
            if project_sources and name in supplied_envelope
            else None
        )
        for name in section_names
    }

    return {
        "metadata": {
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
            "governing_specification": GOVERNING_SPECIFICATION,
            "request_consumption_type": CONSUMPTION_TYPE,
            "request_consumption_version": CONSUMPTION_VERSION,
            "request_consumption_scope": CONSUMPTION_SCOPE,
        },
        "declared_request_consumption_question": {
            "request_consumption_request_id": safe_id,
            "request_consumption_question": CONSUMPTION_QUESTION,
            "request_consumption_intent": safe_intent,
            "request_consumption_scope_family": list(
                REQUEST_CONSUMPTION_SCOPE_FAMILY
            ),
        },
        **sections,
        "consumption_result": {
            "request_consumption_request_id": safe_id,
            "request_consumption_type": CONSUMPTION_TYPE,
            "request_consumption_version": CONSUMPTION_VERSION,
            "request_consumption_scope": CONSUMPTION_SCOPE,
            "outcome": outcome,
            **positive,
        },
        "checks": checks,
        "passed_check_count": sum(check["passed"] for check in checks),
        "failed_check_count": sum(not check["passed"] for check in checks),
        "review_exhausted": True,
        "non_claims": _copy(CANONICAL_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code,
            "reason": reason,
        },
        "what_remains_open": _open_posture(),
    }


def resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Allocate one deterministic actual-consumption terminal outcome."""

    if not isinstance(supplied_envelope, Mapping):
        return _terminal(
            OUTCOME_BLOCKED,
            None,
            None,
            [(CODE_MALFORMED, "one supplied envelope mapping is required")],
            [],
        )

    blocked_issues: list[tuple[str, str]] = []
    missing_basis: list[str] = []

    if _contains_outcome_selector(supplied_envelope):
        blocked_issues.append(
            (
                CODE_OUTCOME_SELECTION,
                "caller-supplied terminal outcome selection is forbidden",
            )
        )
    if _contains_named_key(supplied_envelope, _REFUSAL_KEYS):
        blocked_issues.append(
            (
                CODE_REFUSAL_FIELD,
                "undefined refusal-object or free-text refusal field is forbidden",
            )
        )

    blocked_issues.extend(_identity_issues(supplied_envelope))

    for path, required_keys in _NON_CLAIM_CONTRACTS:
        _validate_non_claim_map(
            supplied_envelope,
            path,
            required_keys,
            blocked_issues,
        )

    _scan_closed(
        supplied_envelope,
        _CANONICAL_POSITIVE_ENVELOPE,
        (),
        blocked_issues,
        missing_basis,
    )

    question = supplied_envelope.get("declared_request_consumption_question")
    supplied_intent = (
        question.get("request_consumption_intent", _MISSING)
        if isinstance(question, Mapping)
        else _MISSING
    )
    if supplied_intent is _MISSING:
        blocked_issues.append((CODE_CONTROL, "request_consumption_intent is absent"))
    elif not isinstance(supplied_intent, str):
        blocked_issues.append(
            (CODE_CONTROL, "request_consumption_intent must be one string")
        )
    elif supplied_intent == INTENT_BLOCK:
        blocked_issues.append((CODE_INTENT_BLOCKED, "exact block intent supplied"))
    elif supplied_intent not in {INTENT_RECORD, INTENT_DO_NOT_RECORD}:
        blocked_issues.append(
            (CODE_INTENT_UNSUPPORTED, "unsupported actual-consumption intent")
        )

    if blocked_issues:
        outcome = OUTCOME_BLOCKED
    elif missing_basis:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif supplied_intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_CONSUMED
    else:
        outcome = OUTCOME_CONSUMED

    return _terminal(
        outcome,
        supplied_envelope,
        supplied_intent,
        blocked_issues,
        missing_basis,
    )


__all__ = [
    "ALLOWED_TRUE_CONSUMED_FIELDS",
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "CHECK_IDS",
    "CONSUMPTION_QUESTION",
    "CONSUMPTION_SCOPE",
    "CONSUMPTION_TYPE",
    "CONSUMPTION_VERSION",
    "DEFAULT_REQUEST_CONSUMPTION_REQUEST_ID",
    "ENVELOPE_KEYS",
    "GOVERNING_SPECIFICATION",
    "INTENT_BLOCK",
    "INTENT_DO_NOT_RECORD",
    "INTENT_RECORD",
    "NON_CLAIM_CONTRACTS",
    "ORDINARY_STRUCTURAL_BASIS_PATHS",
    "OUTCOME_BLOCKED",
    "OUTCOME_CONSUMED",
    "OUTCOME_FAMILY",
    "OUTCOME_NOT_CONSUMED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "PRE_CONSUMPTION_REQUIRED_FALSE_NON_CLAIMS",
    "PRE_CONSUMPTION_SUPPORTING_CHECK_RECORDS",
    "REQUEST_ADMISSION_REQUIRED_FALSE_NON_CLAIMS",
    "REQUEST_CONSUMPTION_SCOPE_FAMILY",
    "REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_KEYS",
    "RESULT_VERSION",
    "SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS",
    "SOURCE_FAMILY_REQUIRED_FALSE_NON_CLAIMS",
    "STANDING_BASIS_REQUIRED_FALSE_NON_CLAIMS",
    "SUPPORTED_INTENTS",
    "build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2_request",
    "resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2",
]
