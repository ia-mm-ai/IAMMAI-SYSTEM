"""Resolve one descendant-body-creation pre-consumption boundary review.

This executable is governed by
DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_BOUNDARY_V0_MIN_V2_SPEC.
It compares one closed in-memory envelope and allocates one boundary-owned
terminal outcome.  It performs no filesystem access, hashing, persistence,
upstream resolution, consumption, token work, exhaustion, target-boundary
consideration, invocation, execution, standing creation, applicability
creation, or authority creation.
"""

from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2 as _applicability
import resolve_descendant_body_creation_boundary_request_admission_v0_min_v2 as _request_admission
import resolve_descendant_body_creation_boundary_request_v0_min as _request_formation
import resolve_matter_bound_selected_surface_standing_basis_admission_v0_min as _standing_basis


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_boundary_v0_min_v2"
)
GOVERNING_SPECIFICATION = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY_V0_MIN_V2_SPEC.md"
)

CONSUMPTION_BOUNDARY_TYPE = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY"
)
CONSUMPTION_BOUNDARY_VERSION = "0.1.0"
CONSUMPTION_BOUNDARY_SCOPE = (
    "ONE_EXACT_ADMITTED_STANDING_BASIS_ONE_EXACT_ADMITTED_DESCENDANT_BODY_"
    "CREATION_BOUNDARY_REQUEST_ONE_FUTURE_CONSUMPTION_REVIEW_ONLY"
)
CONSUMPTION_BOUNDARY_QUESTION = (
    "May the exact already-admitted standing basis referenced by exact admitted "
    "request descendant_body_creation_boundary_request_001 be bounded for one "
    "later one-shot consumption review under exact request-admission result "
    "descendant_body_creation_boundary_request_admission_001, while preserving "
    "the exact request, basis, complete Candidate A/B pair, source semantic "
    "ownership, declared use, target contract, lineage, custody, rank, scope, "
    "freshness, historical non-replay, and non-claims?"
)

INTENT_RECORD = (
    "RECORD_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
    "BASIS_CONSUMPTION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY_REVIEW"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTCOME_RECORDED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_REVIEW_BLOCKED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
    "CONSUMPTION_BOUNDARY_REVIEW_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_REVIEW_BLOCKED,
)

DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID = (
    "descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_boundary_request_001"
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
SOURCE_APPLICABILITY_RESULT_REFERENCE = (
    _request_formation.SOURCE_APPLICABILITY_ARTIFACT_REFERENCE
)
TARGET_BOUNDARY_CONTRACT_REFERENCE = (
    _request_formation.TARGET_BOUNDARY_CONTRACT_REFERENCE
)
TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY = (
    _request_formation.TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY
)

REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _request_formation.REQUIRED_FALSE_NON_CLAIMS
)
REQUEST_ADMISSION_REQUIRED_FALSE_NON_CLAIMS = tuple(
    _request_admission.REQUIRED_FALSE_NON_CLAIMS
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
    "follow_on_work_authorized",
    "automatic_successor_created",
    "runtime_created",
    "registry_created",
    "catalogue_created",
    "ontology_created",
    "generic_consumption_framework_created",
    "cross_family_adapter_created",
)
CANONICAL_NON_CLAIMS = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}

ALLOWED_TRUE_RECORDED_FIELDS = (
    "consumption_boundary_recorded",
    "exact_request_preserved",
    "exact_request_admission_preserved",
    "exact_standing_basis_admission_preserved",
    "selected_surface_complete_pair_preserved",
    "source_family_semantic_ownership_preserved",
    "declared_matter_use_preserved",
    "target_boundary_contract_preserved",
    "freshness_and_non_replay_preserved",
    "single_future_consumption_review_conditions_declared",
    "one_shot_consumption_posture_declared",
    "actual_consumption_requires_separate_review",
    "target_boundary_consideration_requires_separate_review",
    "result_level_non_claims_canonical_false",
)

ENVELOPE_KEYS = frozenset(
    {
        "consumption_boundary_request_id",
        "declared_consumption_boundary_question",
        "selected_request_formation_result",
        "selected_request_admission_result",
        "selected_standing_basis_admission_result",
        "selected_surface_binding",
        "selected_source_applicability_binding",
        "selected_target_boundary_binding",
        "freshness_and_non_replay_posture",
        "one_shot_consumption_posture",
        "declared_non_claims",
    }
)

RESULT_KEYS = frozenset(
    {
        "metadata",
        "declared_consumption_boundary_question",
        "selected_request_formation_result",
        "selected_request_admission_result",
        "selected_standing_basis_admission_result",
        "selected_surface_binding",
        "selected_source_applicability_binding",
        "selected_target_boundary_binding",
        "freshness_and_non_replay_posture",
        "one_shot_consumption_posture",
        "consumption_boundary",
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

CODE_RECORDED = "CONSUMPTION_BOUNDARY_RECORDED"
CODE_NOT_RECORDED = "CONSUMPTION_BOUNDARY_NOT_RECORDED_BY_EXACT_INTENT"
CODE_ADDITIONAL_BASIS = "ORDINARY_STRUCTURAL_BASIS_MISSING"
CODE_REVIEW_BLOCKED = "CONSUMPTION_BOUNDARY_REVIEW_BLOCKED"
CODE_MALFORMED = "CONSUMPTION_BOUNDARY_ENVELOPE_MALFORMED"
CODE_SCHEMA = "CONSUMPTION_BOUNDARY_SCHEMA_INVALID"
CODE_CONTROL = "CONSUMPTION_BOUNDARY_CONTROL_INVALID"
CODE_INTENT_BLOCKED = "CONSUMPTION_BOUNDARY_EXPLICITLY_BLOCKED"
CODE_INTENT_UNSUPPORTED = "CONSUMPTION_BOUNDARY_INTENT_UNSUPPORTED"
CODE_OUTCOME_SELECTION = "CALLER_OUTCOME_SELECTION_BLOCKED"
CODE_IDENTITY = "CONSUMPTION_BOUNDARY_REQUEST_ID_INVALID"
CODE_IDENTITY_COLLISION = "CONSUMPTION_BOUNDARY_REQUEST_ID_COLLISION"
CODE_NON_CLAIM_MISSING = "REQUIRED_NON_CLAIM_MISSING"
CODE_NON_CLAIM_NON_BOOLEAN = "REQUIRED_NON_CLAIM_NON_BOOLEAN"
CODE_NON_CLAIM_TRUE = "REQUIRED_NON_CLAIM_TRUE"
CODE_CONTRADICTION = "EXACT_BOUND_MATERIAL_CONTRADICTED"
CODE_BINDING = "EXACT_BINDING_CONTRADICTED"
CODE_ADMISSION = "REQUEST_ADMISSION_NOT_POSITIVE"
CODE_PAIR = "COMPLETE_CANDIDATE_PAIR_CONTRADICTED"
CODE_SEMANTIC_OWNER = "SOURCE_SEMANTIC_OWNERSHIP_CONTRADICTED"
CODE_ROUTE = "DECLARED_USE_OR_ROUTE_CONTRADICTED"
CODE_REPLAY = "FRESHNESS_OR_NON_REPLAY_CONTRADICTED"
CODE_OVERREACH = "PRE_CONSUMPTION_BOUNDARY_OVERREACH"

BLOCK_CODES = frozenset(
    {
        CODE_RECORDED,
        CODE_NOT_RECORDED,
        CODE_ADDITIONAL_BASIS,
        CODE_REVIEW_BLOCKED,
        CODE_MALFORMED,
        CODE_SCHEMA,
        CODE_CONTROL,
        CODE_INTENT_BLOCKED,
        CODE_INTENT_UNSUPPORTED,
        CODE_OUTCOME_SELECTION,
        CODE_IDENTITY,
        CODE_IDENTITY_COLLISION,
        CODE_NON_CLAIM_MISSING,
        CODE_NON_CLAIM_NON_BOOLEAN,
        CODE_NON_CLAIM_TRUE,
        CODE_CONTRADICTION,
        CODE_BINDING,
        CODE_ADMISSION,
        CODE_PAIR,
        CODE_SEMANTIC_OWNER,
        CODE_ROUTE,
        CODE_REPLAY,
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

_MISSING = object()
_DYNAMIC_PATHS = frozenset(
    {
        ("consumption_boundary_request_id",),
        (
            "declared_consumption_boundary_question",
            "consumption_boundary_intent",
        ),
    }
)
_CONTROL_ROOTS = frozenset(
    {"consumption_boundary_request_id", "declared_consumption_boundary_question"}
)
_PAIR_LIST_FIELDS = frozenset({"candidate_record_ids", "candidate_basis_ids"})
_OUTCOME_SELECTOR_KEYS = frozenset(
    {
        "requested_terminal_outcome",
        "requested_consumption_boundary_outcome",
        "requested_outcome",
        "desired_outcome",
        "expected_outcome",
        "caller_selected_outcome",
    }
)


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _canonical_request_formation_result() -> dict[str, Any]:
    formation_envelope = (
        _request_formation
        .build_declared_descendant_body_creation_boundary_request_v0_min_request()
    )
    request_object = _copy(formation_envelope["request_object"])
    return {
        "result_reference": REQUEST_RESULT_REFERENCE,
        "result_content_identity": REQUEST_RESULT_CONTENT_IDENTITY,
        "resolver_module": _request_formation.RESOLVER_MODULE,
        "result_version": _request_formation.RESULT_VERSION,
        "outcome": _request_formation.OUTCOME_RECORDED,
        "recorded_request_object": request_object,
        "request_formation": {
            key: True for key in _request_formation.ALLOWED_TRUE_RECORDED_FIELDS
        },
        "historical_completed_lineage": _copy(
            formation_envelope["historical_completed_lineage"]
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
            "code": _request_formation.CODE_RECORDED,
            "reason": "one exact fresh request object was formed and recorded only",
        },
        "review_exhausted": True,
        "request_admission_performed": False,
        "basis_consumption_performed": False,
        "consumption_token_closed": False,
        "boundary_consideration_performed": False,
        "invocation_performed": False,
        "execution_performed": False,
        "non_claims": _copy(_request_formation.CANONICAL_NON_CLAIMS),
    }


def _bounded_admitted_request(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request["intended_admitted_standing_basis"]
    standing_keys = (
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
        "target_boundary_binding": _copy(request["target_boundary"]),
        "standing_basis_admission_binding": {
            key: _copy(basis[key]) for key in standing_keys
        },
        "selected_surface_binding": _copy(basis["selected_surface"]),
        "basis_reference_posture": _copy(request["basis_reference_posture"]),
        "freshness_and_non_replay": _copy(request["freshness_and_non_replay"]),
    }


def _canonical_request_admission_result(
    formation_result: Mapping[str, Any],
) -> dict[str, Any]:
    request = formation_result["recorded_request_object"]
    positive = {
        key: True for key in _request_admission.ALLOWED_TRUE_ADMISSION_FIELDS
    }
    binding = {
        "request_id": _request_formation.REQUEST_ID,
        "source_request_result_reference": REQUEST_RESULT_REFERENCE,
        "source_request_result_content_identity": REQUEST_RESULT_CONTENT_IDENTITY,
        "source_request_result_outcome": _request_formation.OUTCOME_RECORDED,
        "recorded_request_object_matches_source_result": True,
        "source_request_result_resolver_module": _request_formation.RESOLVER_MODULE,
        "source_request_result_version": _request_formation.RESULT_VERSION,
        "source_request_result_review_exhausted": True,
        "source_request_result_failed_check_count": 0,
        "source_request_result_blocked": False,
        "source_request_declared_non_claims_preserved": True,
        "source_request_result_non_claims_preserved": True,
    }
    return {
        "result_reference": REQUEST_ADMISSION_RESULT_REFERENCE,
        "result_content_identity": REQUEST_ADMISSION_RESULT_CONTENT_IDENTITY,
        "resolver_module": _request_admission.RESOLVER_MODULE,
        "result_version": _request_admission.RESULT_VERSION,
        "outcome": _request_admission.OUTCOME_ADMITTED,
        "request_admission": {
            "request_admission_id": _request_admission.REQUEST_ADMISSION_ID,
            "request_admission_type": _request_admission.REQUEST_ADMISSION_TYPE,
            "request_admission_version": _request_admission.REQUEST_ADMISSION_VERSION,
            "request_admission_scope": _request_admission.REQUEST_ADMISSION_SCOPE,
            "request_admission_question": _request_admission.REQUEST_ADMISSION_QUESTION,
            "request_admission_intent": _request_admission.INTENT_ADMIT,
            "outcome": _request_admission.OUTCOME_ADMITTED,
            **positive,
        },
        "admitted_request": _bounded_admitted_request(request),
        "source_request_result_binding": binding,
        "checks": [
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
        ],
        "passed_check_count": 3,
        "failed_check_count": 0,
        "block": {
            "blocked": False,
            "code": _request_admission.CODE_ADMITTED,
            "reason": "one exact recorded request was admitted for later separate review only",
        },
        "review_exhausted": True,
        "non_claims": _copy(_request_admission.CANONICAL_NON_CLAIMS),
    }


def _canonical_standing_basis_admission_result() -> dict[str, Any]:
    request = (
        _standing_basis
        .build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request()
    )
    return {
        "result_reference": STANDING_BASIS_ADMISSION_RESULT_REFERENCE,
        "result_content_identity": STANDING_BASIS_ADMISSION_RESULT_CONTENT_IDENTITY,
        "metadata": {
            "matter_bound_selected_surface_standing_basis_admission_id": (
                _standing_basis.BOUNDARY_ID
            ),
            "matter_bound_selected_surface_standing_basis_admission_type": (
                _standing_basis.BOUNDARY_TYPE
            ),
            "matter_bound_selected_surface_standing_basis_admission_version": (
                _standing_basis.BOUNDARY_VERSION
            ),
            "matter_bound_selected_surface_standing_basis_admission_scope": (
                _standing_basis.BOUNDARY_SCOPE
            ),
            "result_version": _standing_basis.RESULT_VERSION,
            "resolver_module": _standing_basis.RESOLVER_MODULE,
        },
        "boundary": {
            **_copy(request["boundary_identity"]),
            "review_exhausted": True,
        },
        "outcome": _standing_basis.OUTCOME_ADMITTED,
        "result": {
            "outcome": _standing_basis.OUTCOME_ADMITTED,
            "lawful_terminal_outcome_recorded": True,
            "review_exhausted": True,
            "stopping_code": None,
        },
        "selected_surface": _copy(request["selected_surface"]),
        "declared_matter_use": _copy(request["declared_matter_use"]),
        "admission_level_binding": _copy(request["admission_level_binding"]),
        "admission": {
            "selected_surface_standing_basis_admitted": True,
            "standing_basis_admission_recorded": True,
            "selected_surface_is_complete_pair_preserved_source_result": True,
            "source_standing_created_upstream": True,
            "source_applicability_recorded_upstream": True,
            "surface_standing_established_here": False,
            "source_applicability_created_here": False,
            "candidate_a_independently_selected": False,
            "candidate_b_independently_selected": False,
            "candidate_pair_split": False,
            "candidate_pair_ranked": False,
            "descendant_body_creation_authorized": False,
            "descendant_body_creation_executed": False,
            "correspondence_applicability_created": False,
            "downstream_authorization_created": False,
            "runtime_created": False,
            "operation_created": False,
            "reuse_permission_created": False,
            "follow_on_permission_created": False,
            "automatic_successor_created": False,
            "source_family_semantic_owner": _standing_basis.SOURCE_SEMANTIC_OWNER,
            "result_level_non_claims_canonical_false": True,
        },
        "passed_check_count": 28,
        "failed_check_count": 0,
        "block": {"blocked": False, "code": None, "reason": None},
        "review_exhausted": True,
        "non_claims": _copy(_standing_basis.CANONICAL_NON_CLAIMS),
    }


def _canonical_question(intent: str) -> dict[str, Any]:
    return {
        "consumption_boundary_type": CONSUMPTION_BOUNDARY_TYPE,
        "consumption_boundary_version": CONSUMPTION_BOUNDARY_VERSION,
        "consumption_boundary_scope": CONSUMPTION_BOUNDARY_SCOPE,
        "consumption_boundary_question": CONSUMPTION_BOUNDARY_QUESTION,
        "consumption_boundary_intent": intent,
    }


def _canonical_target_binding() -> dict[str, Any]:
    return {
        "target_boundary_id": _request_formation.TARGET_BOUNDARY_ID,
        "target_boundary_type": _request_formation.TARGET_BOUNDARY_TYPE,
        "target_boundary_version": _request_formation.TARGET_BOUNDARY_VERSION,
        "target_boundary_scope": _request_formation.TARGET_BOUNDARY_SCOPE,
        "target_boundary_contract_reference": TARGET_BOUNDARY_CONTRACT_REFERENCE,
        "target_boundary_contract_content_identity": (
            TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY
        ),
        "target_boundary_admissible_future_route": (
            _request_formation.TARGET_BOUNDARY_ADMISSIBLE_FUTURE_ROUTE
        ),
        "declared_matter_use": _request_formation.DECLARED_MATTER_USE,
    }


def _canonical_freshness_posture(
    formation_result: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "request_freshness": _copy(
            formation_result["recorded_request_object"][
                "freshness_and_non_replay"
            ]
        ),
        "historical_completed_lineage": _copy(
            formation_result["historical_completed_lineage"]
        ),
        "explicitly_supplied_historical_result_identities": [
            _request_formation.HISTORICAL_BOUNDARY_RESULT_CONTENT_IDENTITY
        ],
    }


def _canonical_one_shot_posture() -> dict[str, bool]:
    return {
        "one_future_consumption_review_only": True,
        "single_consumption_only_if_separately_reviewed": True,
        "actual_consumption_requires_separate_review": True,
        "target_boundary_consideration_requires_separate_review": True,
        "invocation_and_execution_require_separate_review": True,
        "reference_shaped_input_posture": True,
        "actual_consumption_identity_created": False,
        "consumption_token_created": False,
        "consumption_token_closed": False,
        "basis_consumed": False,
        "basis_exhausted": False,
        "target_boundary_consideration_allowed": False,
        "invocation_authorized": False,
        "execution_performed": False,
    }


def _canonical_positive_envelope() -> dict[str, Any]:
    formation = _canonical_request_formation_result()
    admission = _canonical_request_admission_result(formation)
    standing = _canonical_standing_basis_admission_result()
    applicability_request = (
        _standing_basis
        .build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request()
    )
    applicability = _copy(applicability_request["source_applicability_result"])
    selected_surface = _copy(standing["selected_surface"])
    return {
        "consumption_boundary_request_id": DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID,
        "declared_consumption_boundary_question": _canonical_question(INTENT_RECORD),
        "selected_request_formation_result": formation,
        "selected_request_admission_result": admission,
        "selected_standing_basis_admission_result": standing,
        "selected_surface_binding": {
            **selected_surface,
            "declared_matter_use": _request_formation.DECLARED_MATTER_USE,
        },
        "selected_source_applicability_binding": applicability,
        "selected_target_boundary_binding": _canonical_target_binding(),
        "freshness_and_non_replay_posture": _canonical_freshness_posture(
            formation
        ),
        "one_shot_consumption_posture": _canonical_one_shot_posture(),
        "declared_non_claims": _copy(CANONICAL_NON_CLAIMS),
    }


_CANONICAL_POSITIVE_ENVELOPE = _canonical_positive_envelope()


def build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2_request(
    consumption_boundary_request_id: str = DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID,
    consumption_boundary_intent: str = INTENT_RECORD,
) -> dict[str, Any]:
    """Build one exact in-memory V2 pre-consumption review envelope."""

    envelope = _copy(_CANONICAL_POSITIVE_ENVELOPE)
    envelope["consumption_boundary_request_id"] = consumption_boundary_request_id
    envelope["declared_consumption_boundary_question"][
        "consumption_boundary_intent"
    ] = consumption_boundary_intent
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


def _validate_non_claim_map(
    envelope: Mapping[str, Any],
    path: tuple[str, ...],
    required_keys: tuple[str, ...],
    blocked: list[tuple[str, str]],
) -> None:
    parent = _lookup(envelope, path[:-1])
    if parent is _MISSING:
        return
    if not isinstance(parent, Mapping):
        return
    field = path[-1]
    if field not in parent:
        blocked.append(
            (CODE_NON_CLAIM_MISSING, f"required non-claim map absent: {_path_text(path)}")
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
            (CODE_SCHEMA, f"unknown non-claim field: {_path_text(path + (extra[0],))}")
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
        ("selected_standing_basis_admission_result", "non_claims"),
        STANDING_BASIS_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_source_applicability_binding", "non_claims"),
        SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (
        ("selected_source_applicability_binding", "source_family_non_claims"),
        SOURCE_FAMILY_REQUIRED_FALSE_NON_CLAIMS,
    ),
    (("declared_non_claims",), REQUIRED_FALSE_NON_CLAIMS),
)
_NON_CLAIM_PATHS = frozenset(path for path, _ in _NON_CLAIM_CONTRACTS)


def _scan_closed(
    actual: Any,
    expected: Any,
    path: tuple[str, ...],
    blocked: list[tuple[str, str]],
    missing: list[str],
) -> None:
    if path in _NON_CLAIM_PATHS:
        return

    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            blocked.append((CODE_MALFORMED, f"mapping required at {_path_text(path)}"))
            return
        expected_keys = set(expected)
        actual_keys = set(actual)
        for key in sorted(actual_keys - expected_keys):
            blocked.append((CODE_SCHEMA, f"unknown field: {_path_text(path + (key,))}"))
        for key in sorted(expected_keys - actual_keys):
            field_path = path + (key,)
            if field_path[0] in _CONTROL_ROOTS:
                blocked.append(
                    (CODE_CONTROL, f"required boundary control absent: {_path_text(field_path)}")
                )
            else:
                missing.append(_path_text(field_path))
        for key in expected:
            if key in actual:
                _scan_closed(actual[key], expected[key], path + (key,), blocked, missing)
        return

    if isinstance(expected, list):
        if not isinstance(actual, list):
            blocked.append((CODE_MALFORMED, f"list required at {_path_text(path)}"))
            return
        if len(actual) < len(expected):
            if path and path[-1] in _PAIR_LIST_FIELDS:
                blocked.append((CODE_PAIR, f"complete pair not preserved at {_path_text(path)}"))
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

    if path in _DYNAMIC_PATHS:
        return
    if type(actual) is not type(expected):
        blocked.append((CODE_MALFORMED, f"exact type required at {_path_text(path)}"))
        return
    if actual == expected:
        return

    last = path[-1] if path else ""
    code = CODE_CONTRADICTION
    if "admission" in last and last in {
        "outcome",
        "request_admitted",
        "eligible_for_later_separate_one_shot_basis_consumption_review",
        "failed_check_count",
        "review_exhausted",
    }:
        code = CODE_ADMISSION
    if last in {
        "recorded_request_object_matches_source_result",
        "result_reference",
        "result_content_identity",
        "source_request_result_reference",
        "source_request_result_content_identity",
    }:
        code = CODE_BINDING
    if last in {
        "complete_pair_preserved",
        "candidate_pair_split",
        "candidate_pair_ranked",
        "candidate_a_independently_selected",
        "candidate_b_independently_selected",
    }:
        code = CODE_PAIR
    if last in {
        "source_family",
        "source_family_semantic_owner",
        "semantic_ownership_transferred",
    }:
        code = CODE_SEMANTIC_OWNER
    if "route" in last or "declared_matter_use" in last:
        code = CODE_ROUTE
    if last.startswith("historical_") or last.startswith("fresh_"):
        code = CODE_REPLAY
    if last in REQUIRED_FALSE_NON_CLAIMS:
        code = CODE_OVERREACH
    blocked.append((code, f"exact value contradicted at {_path_text(path)}"))


def _contains_outcome_selector(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            normalized = str(key).lower()
            if normalized in _OUTCOME_SELECTOR_KEYS or (
                "outcome" in normalized
                and any(
                    token in normalized
                    for token in ("requested", "desired", "expected", "caller_selected")
                )
            ):
                return True
            if _contains_outcome_selector(item):
                return True
    elif isinstance(value, list):
        return any(_contains_outcome_selector(item) for item in value)
    return False


def _identity_issues(envelope: Mapping[str, Any]) -> list[tuple[str, str]]:
    value = envelope.get("consumption_boundary_request_id", _MISSING)
    if value is _MISSING:
        return [(CODE_IDENTITY, "consumption_boundary_request_id is absent")]
    if not isinstance(value, str) or not value.strip():
        return [(CODE_IDENTITY, "consumption_boundary_request_id must be one non-empty string")]

    collisions = {
        _request_formation.REQUEST_ID,
        _request_admission.REQUEST_ADMISSION_ID,
        _standing_basis.BOUNDARY_ID,
        _request_formation.SELECTED_SURFACE_IDENTITY,
        _request_formation.TARGET_BOUNDARY_ID,
        _request_formation.SOURCE_APPLICABILITY_BOUNDARY_ID,
    }
    freshness = envelope.get("freshness_and_non_replay_posture")
    if isinstance(freshness, Mapping):
        historical = freshness.get("explicitly_supplied_historical_result_identities")
        if isinstance(historical, list):
            collisions.update(item for item in historical if isinstance(item, str))
    if value in collisions:
        return [(CODE_IDENTITY_COLLISION, "pre-consumption review identity collides with a bound identity")]
    return []


def _open_posture() -> dict[str, Any]:
    return {
        "open_items": [
            "live_consumption_boundary_result",
            "artifact",
            "receipt",
            "terminal_summary",
            "actual_one_shot_standing_basis_consumption_and_exhaustion",
            "target_boundary_consideration",
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
    missing_issues: list[str],
    material_complete: bool,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    positive = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    safe_intent = supplied_intent if supplied_intent in SUPPORTED_INTENTS else None
    supplied_id = (
        supplied_envelope.get("consumption_boundary_request_id")
        if supplied_envelope is not None
        else None
    )
    safe_id = (
        supplied_id
        if isinstance(supplied_id, str)
        and supplied_id.strip()
        and not _identity_issues(supplied_envelope)
        else None
    )

    if outcome == OUTCOME_RECORDED:
        code = CODE_RECORDED
        reason = "one exact pre-consumption boundary was recorded only"
    elif outcome == OUTCOME_NOT_RECORDED:
        code = CODE_NOT_RECORDED
        reason = "complete exact material carried the exact negative intent"
    elif outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        code = CODE_ADDITIONAL_BASIS
        reason = f"ordinary structural basis absent: {missing_issues[0]}"
    else:
        code, reason = (
            blocked_issues[0]
            if blocked_issues
            else (CODE_REVIEW_BLOCKED, "pre-consumption boundary review blocked")
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

    projected = material_complete and supplied_envelope is not None
    section_names = (
        "selected_request_formation_result",
        "selected_request_admission_result",
        "selected_standing_basis_admission_result",
        "selected_surface_binding",
        "selected_source_applicability_binding",
        "selected_target_boundary_binding",
        "freshness_and_non_replay_posture",
        "one_shot_consumption_posture",
    )
    sections = {
        name: _copy(supplied_envelope[name]) if projected else None
        for name in section_names
    }

    result = {
        "metadata": {
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
            "governing_specification": GOVERNING_SPECIFICATION,
            "consumption_boundary_type": CONSUMPTION_BOUNDARY_TYPE,
            "consumption_boundary_version": CONSUMPTION_BOUNDARY_VERSION,
            "consumption_boundary_scope": CONSUMPTION_BOUNDARY_SCOPE,
        },
        "declared_consumption_boundary_question": {
            "consumption_boundary_request_id": safe_id,
            "consumption_boundary_question": CONSUMPTION_BOUNDARY_QUESTION,
            "consumption_boundary_intent": safe_intent,
        },
        **sections,
        "consumption_boundary": {
            "consumption_boundary_request_id": safe_id,
            "consumption_boundary_type": CONSUMPTION_BOUNDARY_TYPE,
            "consumption_boundary_version": CONSUMPTION_BOUNDARY_VERSION,
            "consumption_boundary_scope": CONSUMPTION_BOUNDARY_SCOPE,
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
            "blocked": outcome == OUTCOME_REVIEW_BLOCKED,
            "code": code,
            "reason": reason,
        },
        "what_remains_open": _open_posture(),
    }
    return result


def resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Allocate one deterministic V2 pre-consumption terminal outcome."""

    if not isinstance(supplied_envelope, Mapping):
        return _terminal(
            OUTCOME_REVIEW_BLOCKED,
            None,
            None,
            [(CODE_MALFORMED, "one supplied envelope mapping is required")],
            [],
            False,
        )

    blocked_issues: list[tuple[str, str]] = []
    missing_issues: list[str] = []

    if _contains_outcome_selector(supplied_envelope):
        blocked_issues.append(
            (CODE_OUTCOME_SELECTION, "caller-supplied terminal outcome selection is forbidden")
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
        missing_issues,
    )

    question = supplied_envelope.get("declared_consumption_boundary_question")
    supplied_intent = (
        question.get("consumption_boundary_intent", _MISSING)
        if isinstance(question, Mapping)
        else _MISSING
    )
    if supplied_intent is _MISSING:
        blocked_issues.append((CODE_CONTROL, "consumption_boundary_intent is absent"))
    elif not isinstance(supplied_intent, str):
        blocked_issues.append((CODE_CONTROL, "consumption_boundary_intent must be one string"))
    elif supplied_intent == INTENT_BLOCK:
        blocked_issues.append((CODE_INTENT_BLOCKED, "exact block intent supplied"))
    elif supplied_intent not in {INTENT_RECORD, INTENT_DO_NOT_RECORD}:
        blocked_issues.append((CODE_INTENT_UNSUPPORTED, "unsupported consumption-boundary intent"))

    material_complete = not blocked_issues and not missing_issues
    if blocked_issues:
        outcome = OUTCOME_REVIEW_BLOCKED
    elif missing_issues:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif supplied_intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    return _terminal(
        outcome,
        supplied_envelope,
        supplied_intent,
        blocked_issues,
        missing_issues,
        material_complete,
    )


__all__ = [
    "ALLOWED_TRUE_RECORDED_FIELDS",
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "CHECK_IDS",
    "CONSUMPTION_BOUNDARY_QUESTION",
    "CONSUMPTION_BOUNDARY_SCOPE",
    "CONSUMPTION_BOUNDARY_TYPE",
    "CONSUMPTION_BOUNDARY_VERSION",
    "DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID",
    "ENVELOPE_KEYS",
    "GOVERNING_SPECIFICATION",
    "INTENT_BLOCK",
    "INTENT_DO_NOT_RECORD",
    "INTENT_RECORD",
    "OUTCOME_FAMILY",
    "OUTCOME_NOT_RECORDED",
    "OUTCOME_RECORDED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "OUTCOME_REVIEW_BLOCKED",
    "REQUEST_ADMISSION_REQUIRED_FALSE_NON_CLAIMS",
    "REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_KEYS",
    "RESULT_VERSION",
    "SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS",
    "SOURCE_FAMILY_REQUIRED_FALSE_NON_CLAIMS",
    "STANDING_BASIS_REQUIRED_FALSE_NON_CLAIMS",
    "SUPPORTED_INTENTS",
    "build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2_request",
    "resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2",
]
