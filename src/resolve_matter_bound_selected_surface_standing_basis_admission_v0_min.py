"""Resolve one matter-bound selected-surface standing-basis admission.

The resolver consumes one closed in-memory envelope.  Its first executable
proof treats the complete pair-preserved descendant-body candidate-standing
result as one atomic selected source surface and verifies the exact v2
source-owned applicability carrier for one exact declared use.  It performs
no filesystem access, hashing, persistence, source operation, applicability
operation, standing creation, semantic interpretation, or downstream action.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2 as _source


RESOLVER_MODULE = (
    "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min"
)
RESULT_VERSION = "0.1.0"

BOUNDARY_ID = "matter_bound_selected_surface_standing_basis_admission_001"
BOUNDARY_TYPE = "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "ONE_SELECTED_SURFACE_ONE_EXPLICIT_DOWNSTREAM_MATTER_USE_ONE_EXACT_"
    "FAMILY_OWNED_STANDING_BASIS_ONLY"
)

OUTCOME_ADMITTED = "SELECTED_SURFACE_STANDING_BASIS_ADMITTED"
OUTCOME_NOT_ADMITTED = "SELECTED_SURFACE_STANDING_BASIS_NOT_ADMITTED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SELECTED_SURFACE_STANDING_BASIS_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_REVIEW_BLOCKED = "SELECTED_SURFACE_STANDING_BASIS_REVIEW_BLOCKED"
OUTCOMES = (
    OUTCOME_ADMITTED,
    OUTCOME_NOT_ADMITTED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_REVIEW_BLOCKED,
)

SOURCE_FAMILY = _source.SOURCE_FAMILY
SOURCE_SEMANTIC_OWNER = _source.SOURCE_SEMANTIC_OWNER
SOURCE_OPERATION_ID = _source.SOURCE_OPERATION_ID
SOURCE_OPERATION_TYPE = _source.SOURCE_OPERATION_TYPE
SOURCE_OPERATION_VERSION = _source.SOURCE_OPERATION_VERSION
SOURCE_OPERATION_SCOPE = _source.SOURCE_OPERATION_SCOPE
SOURCE_CANDIDATE_STANDING_RESULT = _source.SOURCE_CANDIDATE_STANDING_RESULT
SOURCE_ARTIFACT_REFERENCE = _source.SOURCE_ARTIFACT_REFERENCE
SOURCE_ARTIFACT_CONTENT_IDENTITY = _source.SOURCE_ARTIFACT_CONTENT_IDENTITY
SOURCE_CONTRACT_REFERENCE = _source.SOURCE_CONTRACT_REFERENCE
SOURCE_CONTRACT_VERSION = _source.SOURCE_CONTRACT_VERSION
SOURCE_CONTRACT_CONTENT_IDENTITY = _source.SOURCE_CONTRACT_CONTENT_IDENTITY
SOURCE_OUTCOME = _source.SOURCE_OUTCOME
SOURCE_PASSED_CHECK_COUNT = _source.SOURCE_PASSED_CHECK_COUNT
SOURCE_FAILED_CHECK_COUNT = _source.SOURCE_FAILED_CHECK_COUNT
BASIS_PAIR_SCOPE = _source.BASIS_PAIR_SCOPE
ADMISSIBLE_FUTURE_ROUTE = _source.ADMISSIBLE_FUTURE_ROUTE

CANDIDATE_A_RECORD_ID = _source.CANDIDATE_A_RECORD_ID
CANDIDATE_A_BASIS_ID = _source.CANDIDATE_A_BASIS_ID
CANDIDATE_B_RECORD_ID = _source.CANDIDATE_B_RECORD_ID
CANDIDATE_B_BASIS_ID = _source.CANDIDATE_B_BASIS_ID

SOURCE_APPLICABILITY_ARTIFACT_REFERENCE = (
    "artifacts/descendant_body_candidate_standing_effect_applicability_"
    "boundary_v0_min_v2/descendant_body_candidate_standing_effect_"
    "applicability_boundary_001__descendant_body_candidate_standing_effect_"
    "applicability_boundary_v0_min_v2_result.json"
)
SOURCE_APPLICABILITY_RESULT_VERSION = "0.2.0"
SOURCE_APPLICABILITY_PASSED_CHECK_COUNT = 22
SOURCE_APPLICABILITY_FAILED_CHECK_COUNT = 0

SELECTED_SURFACE_FIELDS = (
    "selected_surface_identity",
    "selected_surface_reference",
    "selected_surface_content_identity",
    "selected_surface_type",
    "selected_surface_version",
    "selected_surface_scope",
    "source_family",
    "source_family_semantic_owner",
    "complete_pair_preserved",
    "candidate_record_ids",
    "candidate_basis_ids",
)
DECLARED_MATTER_USE_FIELDS = (
    "matter_id",
    "matter_scope",
    "use_id",
    "use_class",
    "use_purpose",
    "requested_standing_basis_use",
    "outside_boundary",
)
REQUEST_KEYS = frozenset(
    {
        "boundary_identity",
        "selected_surface",
        "declared_matter_use",
        "source_applicability_result",
        "admission_level_binding",
        "declared_non_claims",
    }
)

REQUIRED_FALSE_NON_CLAIMS = (
    "surface_standing_established",
    "surface_standing_renewed",
    "surface_standing_generalized",
    "global_standing_recognized",
    "standing_upgraded",
    "source_family_judgment_created",
    "authority_created",
    "authority_transferred",
    "source_transferred",
    "receiver_standing_created",
    "currentness_created",
    "registry_created",
    "catalogue_created",
    "inventory_created",
    "coverage_authority_created",
    "global_standing_ontology_created",
    "centralized_standing_vocabulary_allowlist_created",
    "canonicalization_performed",
    "correspondence_executed",
    "conformance_created",
    "whole_body_coherence_established",
    "presence_established",
    "threshold_met",
    "truth_created",
    "execution_authorized",
    "global_reuse_permission_created",
    "automatic_inheritance_created",
    "rank_upgraded",
    "custody_transferred",
    "recency_inference_used",
    "repository_presence_treated_as_admission_basis",
    "mutation_performed",
    "continuation_authorized",
    "automatic_next_step_created",
    "consciousness_created",
    "self_awareness_created",
    "agency_created",
    "sentience_created",
    "identity_created",
    "biological_status_created",
)
CANONICAL_NON_CLAIMS = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}

OUTSIDE_BOUNDARY_FIELDS = (
    "standing_creation_requested",
    "standing_renewal_requested",
    "standing_extension_requested",
    "standing_reinterpretation_requested",
    "standing_transfer_requested",
    "standing_generalization_requested",
    "candidate_pair_split_requested",
    "candidate_pair_ranking_requested",
    "candidate_singleton_selection_requested",
    "source_applicability_creation_requested",
    "descendant_body_creation_authorization_requested",
    "descendant_body_creation_execution_requested",
    "correspondence_applicability_requested",
    "downstream_authorization_requested",
    "runtime_or_operation_requested",
    "reuse_or_follow_on_requested",
)

STOP_REASONS = {
    "REQUEST_NOT_MAPPING": "The request must be one closed in-memory mapping.",
    "REQUEST_KEYS_INVALID": "The request contains a non-canonical top-level field.",
    "REQUEST_FIELDS_INCOMPLETE": "The closed request is missing a required section.",
    "BOUNDARY_IDENTITY_ADDITIONAL_BASIS_REQUIRED": "Exact boundary identity is required.",
    "BOUNDARY_IDENTITY_MALFORMED": "Boundary identity is contradictory or malformed.",
    "SELECTED_SURFACE_ADDITIONAL_BASIS_REQUIRED": "The exact atomic selected surface is incomplete.",
    "SELECTED_SURFACE_MALFORMED": "The selected surface is contradictory or not the complete source pair.",
    "DECLARED_MATTER_USE_ADDITIONAL_BASIS_REQUIRED": "Exact matter/use declarations are required.",
    "DECLARED_MATTER_USE_MALFORMED": "The matter/use declaration is malformed or internally contradictory.",
    "DECLARED_USE_NOT_APPLICABLE": "The exact selected source basis is not applicable to the declared use.",
    "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED": "The exact source-owned applicability carrier is incomplete.",
    "SOURCE_APPLICABILITY_MALFORMED": "The source-owned applicability carrier is contradictory or malformed.",
    "SOURCE_APPLICABILITY_NOT_APPLICABLE": "The supplied source applicability result is not applicable.",
    "SOURCE_APPLICABILITY_REQUIRES_ADDITIONAL_BASIS": "The supplied source applicability result requires additional basis.",
    "SOURCE_APPLICABILITY_REVIEW_BLOCKED": "The supplied source applicability result is blocked.",
    "PAIR_DECOMPOSITION_OR_HIERARCHY": "The complete source pair was split, ranked, coupled, or incompletely supplied.",
    "SOURCE_CONTRACT_OR_EFFECT_MISMATCH": "Source contract, effect locations, or standing result do not match.",
    "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH": "Source lineage, custody, rank, or scope was changed.",
    "SOURCE_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED": "The complete source-family non-claims are required.",
    "SOURCE_NON_CLAIMS_MALFORMED": "A source-family non-claim is unknown, non-boolean, or true.",
    "APPLICABILITY_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED": "The complete applicability non-claims are required.",
    "APPLICABILITY_NON_CLAIMS_MALFORMED": "An applicability non-claim is unknown, non-boolean, or true.",
    "ADMISSION_BINDING_ADDITIONAL_BASIS_REQUIRED": "The complete admission-level binding is required.",
    "ADMISSION_BINDING_MALFORMED": "The admission-level binding is contradictory or malformed.",
    "ADMISSION_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED": "The complete admission non-claims are required.",
    "ADMISSION_NON_CLAIMS_MALFORMED": "An admission non-claim is unknown, non-boolean, or true.",
}
STOP_CODES = frozenset(STOP_REASONS)
BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_KEYS_INVALID",
        "BOUNDARY_IDENTITY_MALFORMED",
        "SELECTED_SURFACE_MALFORMED",
        "DECLARED_MATTER_USE_MALFORMED",
        "SOURCE_APPLICABILITY_MALFORMED",
        "SOURCE_APPLICABILITY_REVIEW_BLOCKED",
        "PAIR_DECOMPOSITION_OR_HIERARCHY",
        "SOURCE_CONTRACT_OR_EFFECT_MISMATCH",
        "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH",
        "SOURCE_NON_CLAIMS_MALFORMED",
        "APPLICABILITY_NON_CLAIMS_MALFORMED",
        "ADMISSION_BINDING_MALFORMED",
        "ADMISSION_NON_CLAIMS_MALFORMED",
    }
)

OPEN_ITEMS = (
    "live_standing_basis_admission_result",
    "receipt",
    "terminal_summary",
    "correspondence_integration",
    "descendant_body_creation_authorization_or_execution",
    "runtime_or_operation_use",
    "other_standing_producing_families",
    "later_successor_work",
)


def _copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _copy(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_copy(item) for item in value]
    return value


def _canonical_boundary_identity() -> dict[str, Any]:
    return {
        "matter_bound_selected_surface_standing_basis_admission_id": BOUNDARY_ID,
        "matter_bound_selected_surface_standing_basis_admission_type": BOUNDARY_TYPE,
        "matter_bound_selected_surface_standing_basis_admission_version": BOUNDARY_VERSION,
        "matter_bound_selected_surface_standing_basis_admission_scope": BOUNDARY_SCOPE,
    }


def _canonical_selected_surface() -> dict[str, Any]:
    return {
        "selected_surface_identity": SOURCE_OPERATION_ID,
        "selected_surface_reference": SOURCE_ARTIFACT_REFERENCE,
        "selected_surface_content_identity": SOURCE_ARTIFACT_CONTENT_IDENTITY,
        "selected_surface_type": SOURCE_OPERATION_TYPE,
        "selected_surface_version": SOURCE_OPERATION_VERSION,
        "selected_surface_scope": SOURCE_OPERATION_SCOPE,
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
        "complete_pair_preserved": True,
        "candidate_record_ids": [CANDIDATE_A_RECORD_ID, CANDIDATE_B_RECORD_ID],
        "candidate_basis_ids": [CANDIDATE_A_BASIS_ID, CANDIDATE_B_BASIS_ID],
    }


def _canonical_outside_boundary() -> dict[str, bool]:
    return {key: False for key in OUTSIDE_BOUNDARY_FIELDS}


def _canonical_declared_matter_use(declared_use: str) -> dict[str, Any]:
    return {
        "matter_id": declared_use,
        "matter_scope": declared_use,
        "use_id": declared_use,
        "use_class": declared_use,
        "use_purpose": declared_use,
        "requested_standing_basis_use": declared_use,
        "outside_boundary": _canonical_outside_boundary(),
    }


def _canonical_source_applicability_result() -> dict[str, Any]:
    source_request = (
        _source.build_declared_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2_request()
    )
    source_operation = _copy(source_request["source_operation"])
    source_artifact = source_request["source_artifact"]
    contract = source_request["source_standing_contract"]
    pair = _copy(source_request["candidate_pair"])
    source_binding = {
        "basis_pair_scope": source_operation["basis_pair_scope"],
        "candidate_a_basis_id": pair["candidate_a"]["candidate_basis_id"],
        "candidate_a_basis_label": pair["candidate_a"]["candidate_basis_label"],
        "candidate_a_record_id": pair["candidate_a"]["candidate_record_id"],
        "candidate_a_role": pair["candidate_a"]["candidate_role"],
        "candidate_a_standing_created": source_operation[
            "candidate_a_standing_created"
        ],
        "candidate_b_basis_id": pair["candidate_b"]["candidate_basis_id"],
        "candidate_b_basis_label": pair["candidate_b"]["candidate_basis_label"],
        "candidate_b_record_id": pair["candidate_b"]["candidate_record_id"],
        "candidate_b_role": pair["candidate_b"]["candidate_role"],
        "candidate_b_standing_created": source_operation[
            "candidate_b_standing_created"
        ],
        "candidate_standing_authorized": source_operation[
            "candidate_standing_authorized"
        ],
        "candidate_standing_created": source_operation["candidate_standing_created"],
        "candidate_standing_operation_id": source_operation[
            "candidate_standing_operation_id"
        ],
        "candidate_standing_operation_scope": source_operation[
            "candidate_standing_operation_scope"
        ],
        "candidate_standing_operation_type": source_operation[
            "candidate_standing_operation_type"
        ],
        "candidate_standing_operation_version": source_operation[
            "candidate_standing_operation_version"
        ],
        "candidate_standing_result": source_operation["candidate_standing_result"],
        "candidate_standing_supported": source_operation[
            "candidate_standing_supported"
        ],
        "complete_pair_preserved": True,
        "source_artifact_content_identity": source_artifact[
            "source_artifact_content_identity"
        ],
        "source_artifact_reference": source_artifact["source_artifact_reference"],
        "source_custody_preserved": True,
        "source_failed_check_count": source_artifact["source_failed_check_count"],
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
        "source_lineage_preserved": True,
        "source_outcome": source_artifact["source_outcome"],
        "source_passed_check_count": source_artifact["source_passed_check_count"],
        "source_rank_preserved": True,
        "source_standing_contract_content_identity": contract[
            "source_standing_contract_content_identity"
        ],
        "source_standing_contract_reference": contract[
            "source_standing_contract_reference"
        ],
        "source_standing_contract_version": contract[
            "source_standing_contract_version"
        ],
        "source_standing_created": source_operation["candidate_standing_created"],
    }
    return {
        "applicability_artifact_reference": SOURCE_APPLICABILITY_ARTIFACT_REFERENCE,
        "result_version": SOURCE_APPLICABILITY_RESULT_VERSION,
        "resolver_module": _source.RESOLVER_MODULE,
        "outcome": _source.OUTCOME_RECORDED,
        "boundary": {
            **_copy(source_request["boundary_identity"]),
            "review_exhausted": True,
        },
        "block": {"blocked": False, "code": None},
        "applicability_check_posture": {
            "passed_check_count": SOURCE_APPLICABILITY_PASSED_CHECK_COUNT,
            "failed_check_count": SOURCE_APPLICABILITY_FAILED_CHECK_COUNT,
        },
        "applicability": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "candidate_a_altered": False,
            "candidate_b_altered": False,
            "candidate_standing_effect_applicability_recorded": True,
            "candidate_standing_effect_applicable_to_declared_use": True,
            "complete_review_reached": True,
            "correspondence_applicability_created": False,
            "declared_downstream_matter_use": ADMISSIBLE_FUTURE_ROUTE,
            "declared_use_exactly_matches_source_route": True,
            "descendant_body_creation_authorized": False,
            "descendant_body_creation_executed": False,
            "downstream_authorization_created": False,
            "lawful_terminal_outcome_recorded": True,
            "selected_surface_standing_basis_admission_created": False,
            "source_family_semantic_ownership_preserved": True,
            "source_result_invalidated": False,
            "source_standing_revoked": False,
            "standing_created": False,
        },
        "source_binding": source_binding,
        "standing_effect_locations": _copy(
            source_request["standing_effect_locations"]
        ),
        "source_operation": source_operation,
        "candidate_pair": pair,
        "candidate_standing_operation_material": _copy(
            source_request["candidate_standing_operation_material"]
        ),
        "standing_pair_evaluation": _copy(
            source_request["candidate_standing_operation_material"][
                "standing_pair_evaluation"
            ]
        ),
        "cross_object_binding": _copy(source_request["cross_object_binding"]),
        "source_lineage": _copy(source_request["source_lineage"]),
        "source_custody": _copy(source_request["source_custody"]),
        "source_rank": _copy(source_request["source_rank"]),
        "source_scope": _copy(source_request["source_scope"]),
        "source_family_non_claims": _copy(
            source_request["source_family_non_claims"]
        ),
        "non_claims": _copy(source_request["declared_non_claims"]),
    }


def _canonical_admission_binding(
    declared_use: str,
    source_applicability_outcome: str = _source.OUTCOME_RECORDED,
) -> dict[str, Any]:
    carrier = _canonical_source_applicability_result()
    return {
        "selected_surface_identity": SOURCE_OPERATION_ID,
        "selected_surface_reference": SOURCE_ARTIFACT_REFERENCE,
        "selected_surface_content_identity": SOURCE_ARTIFACT_CONTENT_IDENTITY,
        "selected_surface_type": SOURCE_OPERATION_TYPE,
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
        "source_standing_contract_reference": SOURCE_CONTRACT_REFERENCE,
        "source_standing_contract_content_identity": SOURCE_CONTRACT_CONTENT_IDENTITY,
        "source_standing_result": SOURCE_CANDIDATE_STANDING_RESULT,
        "source_applicability_artifact_reference": SOURCE_APPLICABILITY_ARTIFACT_REFERENCE,
        "source_applicability_boundary_id": _source.BOUNDARY_ID,
        "source_applicability_outcome": source_applicability_outcome,
        "candidate_record_ids": [CANDIDATE_A_RECORD_ID, CANDIDATE_B_RECORD_ID],
        "candidate_basis_ids": [CANDIDATE_A_BASIS_ID, CANDIDATE_B_BASIS_ID],
        "complete_pair_preserved": True,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "source_route": ADMISSIBLE_FUTURE_ROUTE,
        "declared_matter_use": declared_use,
        "source_lineage": _copy(carrier["source_lineage"]),
        "source_custody": _copy(carrier["source_custody"]),
        "source_rank": _copy(carrier["source_rank"]),
        "source_scope": _copy(carrier["source_scope"]),
    }


def build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request(
    declared_downstream_matter_use: str = ADMISSIBLE_FUTURE_ROUTE,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit closed in-memory request without reading artifacts."""

    request: dict[str, Any] = {
        "boundary_identity": _canonical_boundary_identity(),
        "selected_surface": _canonical_selected_surface(),
        "declared_matter_use": _canonical_declared_matter_use(
            declared_downstream_matter_use
        ),
        "source_applicability_result": _canonical_source_applicability_result(),
        "admission_level_binding": _canonical_admission_binding(
            declared_downstream_matter_use
        ),
        "declared_non_claims": dict(CANONICAL_NON_CLAIMS),
    }
    for key, value in overrides.items():
        request[key] = _copy(value)
    return request


def _contains_missing(actual: Any, expected: Any) -> bool:
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            return actual is None
        for key, value in expected.items():
            if key not in actual or _contains_missing(actual[key], value):
                return True
        return False
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return actual is None
        return len(actual) < len(expected)
    return actual is None


def _mapping_shape_state(actual: Any, expected: Mapping[str, Any]) -> str | None:
    if actual is None:
        return "missing"
    if not isinstance(actual, Mapping):
        return "invalid"
    actual_keys = frozenset(actual)
    expected_keys = frozenset(expected)
    if actual_keys - expected_keys:
        return "invalid"
    if expected_keys - actual_keys:
        return "missing"
    return None


def _non_claim_state(actual: Any, expected: Mapping[str, bool]) -> str | None:
    state = _mapping_shape_state(actual, expected)
    if state is not None:
        return state
    if any(actual.get(key) is not False for key in expected):
        return "invalid"
    return None


def _pair_projection_changed(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, Mapping) or not isinstance(expected, Mapping):
        return False
    for field in ("candidate_record_ids", "candidate_basis_ids"):
        if field in actual and field in expected and actual[field] != expected[field]:
            return True
    return False


def _build_result(
    *,
    outcome: str,
    checks: list[dict[str, Any]],
    stopping_code: str | None,
    selected_surface: Mapping[str, Any] | None,
    declared_matter_use: Mapping[str, Any] | None,
    source_applicability_result: Mapping[str, Any] | None,
    admission_level_binding: Mapping[str, Any] | None,
) -> dict[str, Any]:
    admitted = outcome == OUTCOME_ADMITTED
    selected = _copy(selected_surface) if selected_surface is not None else None
    declared = _copy(declared_matter_use) if declared_matter_use is not None else None
    carrier = (
        _copy(source_applicability_result)
        if source_applicability_result is not None
        else None
    )
    binding = (
        _copy(admission_level_binding)
        if admission_level_binding is not None
        else None
    )
    passed_check_count = sum(check["passed"] is True for check in checks)
    failed_check_count = sum(check["passed"] is False for check in checks)
    return {
        "metadata": {
            "matter_bound_selected_surface_standing_basis_admission_id": BOUNDARY_ID,
            "matter_bound_selected_surface_standing_basis_admission_type": BOUNDARY_TYPE,
            "matter_bound_selected_surface_standing_basis_admission_version": BOUNDARY_VERSION,
            "matter_bound_selected_surface_standing_basis_admission_scope": BOUNDARY_SCOPE,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
        },
        "boundary": {
            **_canonical_boundary_identity(),
            "review_exhausted": True,
        },
        "selected_surface": selected,
        "declared_matter_use": declared,
        "source_applicability_result": carrier,
        "admission_level_binding": binding,
        "admission": {
            "selected_surface_standing_basis_admitted": admitted,
            "standing_basis_admission_recorded": admitted,
            "selected_surface_is_complete_pair_preserved_source_result": admitted,
            "source_standing_created_upstream": (
                carrier is not None
                and isinstance(carrier.get("source_binding"), Mapping)
                and carrier["source_binding"].get("source_standing_created") is True
            ),
            "source_applicability_recorded_upstream": (
                carrier is not None
                and isinstance(carrier.get("applicability"), Mapping)
                and carrier["applicability"].get(
                    "candidate_standing_effect_applicability_recorded"
                )
                is True
            ),
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
            "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
            "result_level_non_claims_canonical_false": True,
        },
        "checks": [dict(check) for check in checks],
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result": {
            "outcome": outcome,
            "lawful_terminal_outcome_recorded": True,
            "review_exhausted": True,
            "stopping_code": stopping_code,
        },
        "non_claims": dict(CANONICAL_NON_CLAIMS),
        "what_remains_open": {
            "open_items": list(OPEN_ITEMS),
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next": True,
        },
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_REVIEW_BLOCKED,
            "code": stopping_code if outcome == OUTCOME_REVIEW_BLOCKED else None,
            "reason": (
                STOP_REASONS[stopping_code]
                if outcome == OUTCOME_REVIEW_BLOCKED and stopping_code is not None
                else None
            ),
        },
    }


def resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
    request: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Resolve one exact standing-basis admission by structural verification."""

    checks: list[dict[str, Any]] = []
    selected_surface: Mapping[str, Any] | None = None
    declared_matter_use: Mapping[str, Any] | None = None
    source_applicability_result: Mapping[str, Any] | None = None
    admission_level_binding: Mapping[str, Any] | None = None

    def passed(check_id: str) -> None:
        checks.append(
            {
                "check_id": check_id,
                "passed": True,
                "failure_code": None,
                "outcome_if_failed": None,
                "block_code": None,
            }
        )

    def stopped(check_id: str, outcome: str, code: str) -> dict[str, Any]:
        checks.append(
            {
                "check_id": check_id,
                "passed": False,
                "failure_code": code,
                "outcome_if_failed": outcome,
                "block_code": code if outcome == OUTCOME_REVIEW_BLOCKED else None,
            }
        )
        return _build_result(
            outcome=outcome,
            checks=checks,
            stopping_code=code,
            selected_surface=selected_surface,
            declared_matter_use=declared_matter_use,
            source_applicability_result=source_applicability_result,
            admission_level_binding=admission_level_binding,
        )

    if not isinstance(request, Mapping):
        return stopped(
            "request_is_one_mapping", OUTCOME_REVIEW_BLOCKED, "REQUEST_NOT_MAPPING"
        )

    request_keys = frozenset(request)
    if request_keys - REQUEST_KEYS:
        return stopped(
            "request_has_no_unknown_fields",
            OUTCOME_REVIEW_BLOCKED,
            "REQUEST_KEYS_INVALID",
        )
    if REQUEST_KEYS - request_keys:
        return stopped(
            "request_has_complete_closed_envelope",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "REQUEST_FIELDS_INCOMPLETE",
        )
    passed("request_has_complete_closed_envelope")

    expected_boundary = _canonical_boundary_identity()
    state = _mapping_shape_state(request.get("boundary_identity"), expected_boundary)
    if state == "missing":
        return stopped(
            "boundary_identity_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "BOUNDARY_IDENTITY_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid" or request["boundary_identity"] != expected_boundary:
        return stopped(
            "boundary_identity_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "BOUNDARY_IDENTITY_MALFORMED",
        )
    passed("boundary_identity_is_exact")

    expected_surface = _canonical_selected_surface()
    state = _mapping_shape_state(request.get("selected_surface"), expected_surface)
    if state == "missing":
        return stopped(
            "selected_surface_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SELECTED_SURFACE_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid" or request["selected_surface"] != expected_surface:
        return stopped(
            "selected_surface_is_exact_complete_pair",
            OUTCOME_REVIEW_BLOCKED,
            "SELECTED_SURFACE_MALFORMED",
        )
    selected_surface = request["selected_surface"]
    passed("selected_surface_is_exact_complete_pair")

    declared = request.get("declared_matter_use")
    expected_declared = _canonical_declared_matter_use(ADMISSIBLE_FUTURE_ROUTE)
    state = _mapping_shape_state(declared, expected_declared)
    if state == "missing":
        return stopped(
            "declared_matter_use_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "DECLARED_MATTER_USE_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid":
        return stopped(
            "declared_matter_use_is_well_formed",
            OUTCOME_REVIEW_BLOCKED,
            "DECLARED_MATTER_USE_MALFORMED",
        )
    declared_matter_use = declared
    declared_values = [
        declared[field]
        for field in DECLARED_MATTER_USE_FIELDS
        if field != "outside_boundary"
    ]
    if (
        any(not isinstance(value, str) or not value.strip() for value in declared_values)
        or len(set(declared_values)) != 1
        or declared["outside_boundary"] != _canonical_outside_boundary()
    ):
        return stopped(
            "declared_matter_use_is_internally_coherent",
            OUTCOME_REVIEW_BLOCKED,
            "DECLARED_MATTER_USE_MALFORMED",
        )
    declared_use = declared["requested_standing_basis_use"]
    passed("declared_matter_use_is_internally_coherent")

    expected_carrier = _canonical_source_applicability_result()
    carrier = request.get("source_applicability_result")
    state = _mapping_shape_state(carrier, expected_carrier)
    if state == "missing":
        return stopped(
            "source_applicability_result_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid":
        return stopped(
            "source_applicability_result_is_well_formed",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_APPLICABILITY_MALFORMED",
        )
    source_applicability_result = carrier

    source_outcome = carrier["outcome"]
    if source_outcome not in _source.OUTCOMES:
        return stopped(
            "source_applicability_outcome_is_public",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_APPLICABILITY_MALFORMED",
        )

    pair_fields = {
        "candidate_pair",
        "candidate_standing_operation_material",
        "standing_pair_evaluation",
    }
    lineage_fields = {"source_lineage", "source_custody", "source_rank", "source_scope"}
    for field, expected in expected_carrier.items():
        if field == "outcome":
            continue
        actual = carrier[field]
        if actual == expected:
            passed(f"source_applicability_{field}_is_exact")
            continue
        if field in pair_fields:
            return stopped(
                f"source_applicability_{field}_preserves_complete_pair",
                OUTCOME_REVIEW_BLOCKED,
                "PAIR_DECOMPOSITION_OR_HIERARCHY",
            )
        if field == "source_family_non_claims":
            code = (
                "SOURCE_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED"
                if _contains_missing(actual, expected)
                else "SOURCE_NON_CLAIMS_MALFORMED"
            )
            outcome = (
                OUTCOME_REQUIRES_ADDITIONAL_BASIS
                if code.endswith("ADDITIONAL_BASIS_REQUIRED")
                else OUTCOME_REVIEW_BLOCKED
            )
            return stopped("source_family_non_claims_are_exact", outcome, code)
        if field == "non_claims":
            code = (
                "APPLICABILITY_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED"
                if _contains_missing(actual, expected)
                else "APPLICABILITY_NON_CLAIMS_MALFORMED"
            )
            outcome = (
                OUTCOME_REQUIRES_ADDITIONAL_BASIS
                if code.endswith("ADDITIONAL_BASIS_REQUIRED")
                else OUTCOME_REVIEW_BLOCKED
            )
            return stopped("applicability_non_claims_are_exact", outcome, code)
        if field in lineage_fields:
            if _contains_missing(actual, expected):
                return stopped(
                    f"source_applicability_{field}_is_complete",
                    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
                )
            return stopped(
                f"source_applicability_{field}_is_exact",
                OUTCOME_REVIEW_BLOCKED,
                "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH",
            )
        if field in {"standing_effect_locations", "source_binding", "source_operation"}:
            if _contains_missing(actual, expected):
                return stopped(
                    f"source_applicability_{field}_is_complete",
                    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
                )
            return stopped(
                f"source_applicability_{field}_is_exact",
                OUTCOME_REVIEW_BLOCKED,
                "SOURCE_CONTRACT_OR_EFFECT_MISMATCH",
            )
        if field == "cross_object_binding":
            if _pair_projection_changed(actual, expected):
                return stopped(
                    "source_cross_object_binding_preserves_complete_pair",
                    OUTCOME_REVIEW_BLOCKED,
                    "PAIR_DECOMPOSITION_OR_HIERARCHY",
                )
            if _contains_missing(actual, expected):
                return stopped(
                    "source_cross_object_binding_is_complete",
                    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
                )
        return stopped(
            f"source_applicability_{field}_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_APPLICABILITY_MALFORMED",
        )
    passed("source_applicability_result_is_structurally_exact")

    declared_non_claims = request.get("declared_non_claims")
    state = _non_claim_state(declared_non_claims, CANONICAL_NON_CLAIMS)
    if state == "missing":
        return stopped(
            "admission_non_claims_are_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "ADMISSION_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid":
        return stopped(
            "admission_non_claims_are_canonical_false",
            OUTCOME_REVIEW_BLOCKED,
            "ADMISSION_NON_CLAIMS_MALFORMED",
        )
    passed("admission_non_claims_are_canonical_false")

    expected_binding = _canonical_admission_binding(declared_use, source_outcome)
    binding = request.get("admission_level_binding")
    state = _mapping_shape_state(binding, expected_binding)
    if _pair_projection_changed(binding, expected_binding):
        return stopped(
            "admission_level_binding_preserves_complete_pair",
            OUTCOME_REVIEW_BLOCKED,
            "PAIR_DECOMPOSITION_OR_HIERARCHY",
        )
    if state == "missing" or (
        isinstance(binding, Mapping)
        and _contains_missing(binding, expected_binding)
        and not any(key not in expected_binding for key in binding)
    ):
        return stopped(
            "admission_level_binding_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "ADMISSION_BINDING_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid" or binding != expected_binding:
        return stopped(
            "admission_level_binding_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "ADMISSION_BINDING_MALFORMED",
        )
    admission_level_binding = binding
    passed("admission_level_binding_is_exact")

    if source_outcome == _source.OUTCOME_NOT_APPLICABLE:
        return stopped(
            "source_applicability_is_positive",
            OUTCOME_NOT_ADMITTED,
            "SOURCE_APPLICABILITY_NOT_APPLICABLE",
        )
    if source_outcome == _source.OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return stopped(
            "source_applicability_has_complete_basis",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_APPLICABILITY_REQUIRES_ADDITIONAL_BASIS",
        )
    if source_outcome == _source.OUTCOME_REVIEW_BLOCKED:
        return stopped(
            "source_applicability_is_not_blocked",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_APPLICABILITY_REVIEW_BLOCKED",
        )

    if declared_use != ADMISSIBLE_FUTURE_ROUTE:
        return stopped(
            "declared_use_matches_exact_source_route",
            OUTCOME_NOT_ADMITTED,
            "DECLARED_USE_NOT_APPLICABLE",
        )
    passed("declared_use_matches_exact_source_route")

    return _build_result(
        outcome=OUTCOME_ADMITTED,
        checks=checks,
        stopping_code=None,
        selected_surface=selected_surface,
        declared_matter_use=declared_matter_use,
        source_applicability_result=source_applicability_result,
        admission_level_binding=admission_level_binding,
    )


__all__ = [
    "ADMISSIBLE_FUTURE_ROUTE",
    "BLOCK_CODES",
    "BOUNDARY_ID",
    "BOUNDARY_SCOPE",
    "BOUNDARY_TYPE",
    "BOUNDARY_VERSION",
    "CANONICAL_NON_CLAIMS",
    "OUTCOMES",
    "OUTCOME_ADMITTED",
    "OUTCOME_NOT_ADMITTED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "OUTCOME_REVIEW_BLOCKED",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_VERSION",
    "SOURCE_APPLICABILITY_ARTIFACT_REFERENCE",
    "SOURCE_FAILED_CHECK_COUNT",
    "SOURCE_FAMILY",
    "SOURCE_OPERATION_ID",
    "SOURCE_PASSED_CHECK_COUNT",
    "SOURCE_SEMANTIC_OWNER",
    "STOP_CODES",
    "build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request",
    "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min",
]
