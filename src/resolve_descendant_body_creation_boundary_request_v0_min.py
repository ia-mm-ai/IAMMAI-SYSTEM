"""Pure formation resolver for one descendant-body-creation boundary request.

This module records only the exact request object fixed by
DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_V0_MIN_SPEC.  The request remains
distinct from the resolver-owned result wrapper.  No request admission, basis
consumption, authorization, invocation, execution, or standing operation is
performed here.
"""

from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any

import resolve_matter_bound_selected_surface_standing_basis_admission_v0_min as _admission


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_creation_boundary_request_v0_min"

REQUEST_ID = "descendant_body_creation_boundary_request_001"
REQUEST_TYPE = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"
REQUEST_VERSION = "0.1.0"
REQUEST_SCOPE = (
    "ONE_FRESH_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_"
    "ONE_EXACT_ADMITTED_STANDING_BASIS_ONLY"
)
REQUEST_QUESTION = (
    "May one exact fresh, uniquely identified descendant-body-creation boundary "
    "request be formed and recorded, referencing one exact already-admitted "
    "standing-basis result and the exact existing descendant-body-creation "
    "boundary contract for one exact declared use, without admitting the request, "
    "consuming or exhausting the basis, authorizing boundary consideration or "
    "invocation, replaying the historical completed request, or creating standing, "
    "applicability, authority, execution force, reuse, or successor permission?"
)
REQUEST_INTENT = "RECORD_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"
DECLARED_MATTER_USE = (
    "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
)

TARGET_BOUNDARY_ID = "descendant_body_creation_boundary_001"
TARGET_BOUNDARY_TYPE = "DESCENDANT_BODY_CREATION_BOUNDARY"
TARGET_BOUNDARY_VERSION = "0.1.0"
TARGET_BOUNDARY_SCOPE = (
    "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY"
)
TARGET_BOUNDARY_CONTRACT_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_V0_MIN_SPEC.md"
)
TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY = (
    "0b66c2419a1fe4e480192755858268aab0d7f8d109822a99fcf83e3d785be273"
)
TARGET_BOUNDARY_ADMISSIBLE_FUTURE_ROUTE = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_THEN_DESCENDANT_BODY_CREATION_OPERATION_ONLY"
)

STANDING_BASIS_ADMISSION_ID = (
    "matter_bound_selected_surface_standing_basis_admission_001"
)
STANDING_BASIS_ADMISSION_TYPE = (
    "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION"
)
STANDING_BASIS_ADMISSION_VERSION = "0.1.0"
STANDING_BASIS_ADMISSION_SCOPE = (
    "ONE_SELECTED_SURFACE_ONE_EXPLICIT_DOWNSTREAM_MATTER_USE_"
    "ONE_EXACT_FAMILY_OWNED_STANDING_BASIS_ONLY"
)
STANDING_BASIS_ADMISSION_OUTCOME = "SELECTED_SURFACE_STANDING_BASIS_ADMITTED"
STANDING_BASIS_ADMISSION_FAILED_CHECK_COUNT = 0
STANDING_BASIS_ADMISSION_REVIEW_EXHAUSTED = True
STANDING_BASIS_ADMISSION_REFERENCE = (
    "artifacts/matter_bound_selected_surface_standing_basis_admission_v0_min/"
    "matter_bound_selected_surface_standing_basis_admission_001__"
    "matter_bound_selected_surface_standing_basis_admission_v0_min_result.json"
)
STANDING_BASIS_ADMISSION_CONTENT_IDENTITY = (
    "e53cb86c1b76eec212bbd90c1247da7adc0cd4c4cc26da82b4a3edd2c4aa639f"
)

SELECTED_SURFACE_IDENTITY = "descendant_body_candidate_standing_operation_001"
SELECTED_SURFACE_TYPE = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
SELECTED_SURFACE_VERSION = "0.1.0"
SELECTED_SURFACE_SCOPE = (
    "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
)
SELECTED_SURFACE_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_"
    "descendant_body_candidate_standing_operation_v0_min/"
    "descendant_body_candidate_standing_operation_001__"
    "candidate_standing_operation_v0_min_result.json"
)
SELECTED_SURFACE_CONTENT_IDENTITY = (
    "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961"
)
SOURCE_FAMILY = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
SOURCE_FAMILY_SEMANTIC_OWNER = SOURCE_FAMILY
CANDIDATE_RECORD_IDS = (
    "descendant_body_basis_candidate_a_001",
    "descendant_body_basis_candidate_b_001",
)
CANDIDATE_BASIS_IDS = (
    "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
    "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
)

SOURCE_STANDING_CONTRACT_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
)
SOURCE_STANDING_CONTRACT_CONTENT_IDENTITY = (
    "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3"
)
SOURCE_STANDING_RESULT = "CANDIDATE_STANDING_SUPPORTED"
SOURCE_APPLICABILITY_ARTIFACT_REFERENCE = (
    "artifacts/descendant_body_candidate_standing_effect_applicability_"
    "boundary_v0_min_v2/descendant_body_candidate_standing_effect_"
    "applicability_boundary_001__descendant_body_candidate_standing_effect_"
    "applicability_boundary_v0_min_v2_result.json"
)
SOURCE_APPLICABILITY_BOUNDARY_ID = (
    "descendant_body_candidate_standing_effect_applicability_boundary_001"
)
SOURCE_APPLICABILITY_OUTCOME = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED"
)
SOURCE_ROUTE = DECLARED_MATTER_USE

HISTORICAL_BOUNDARY_RESULT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_"
    "descendant_body_creation_boundary_v0_min/"
    "descendant_body_creation_boundary_001__"
    "descendant_body_creation_boundary_v0_min_result.json"
)
HISTORICAL_BOUNDARY_RESULT_CONTENT_IDENTITY = (
    "9598594605e6ae20040cfea67cd6bff74263246aaa3139d0b356eef90b3752c0"
)
HISTORICAL_BOUNDARY_OUTCOME = "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"
HISTORICAL_BOUNDARY_RESULT = (
    "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"
)

OUTCOME_RECORDED = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_RECORDED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

REQUEST_OBJECT_KEYS = frozenset(
    {
        "request_id",
        "request_type",
        "request_version",
        "request_scope",
        "request_question",
        "request_intent",
        "target_boundary",
        "declared_matter_use",
        "intended_admitted_standing_basis",
        "basis_reference_posture",
        "freshness_and_non_replay",
        "declared_non_claims",
    }
)
ENVELOPE_KEYS = frozenset({"request_object", "historical_completed_lineage"})

REQUIRED_FALSE_NON_CLAIMS = (
    "request_admitted",
    "request_admission_recorded",
    "admitted_standing_basis_consumed",
    "admitted_standing_basis_exhausted",
    "consumption_token_closed",
    "consumption_authorized",
    "basis_reuse_permission_created",
    "request_reuse_permission_created",
    "selected_surface_standing_basis_admission_created",
    "standing_basis_admission_reperformed",
    "source_applicability_created",
    "standing_created",
    "standing_renewed",
    "standing_extended",
    "standing_reinterpreted",
    "standing_transferred",
    "standing_generalized",
    "authority_created",
    "semantic_ownership_transferred",
    "custody_transferred",
    "rank_upgraded",
    "candidate_pair_split",
    "candidate_pair_ranked",
    "candidate_a_independently_selected",
    "candidate_b_independently_selected",
    "correspondence_applicability_created",
    "descendant_body_creation_boundary_created",
    "descendant_body_creation_boundary_modified",
    "boundary_consideration_allowed",
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
    "runtime_created",
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

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_creation_boundary_request_recorded",
    "fresh_request_identity_declared",
    "target_boundary_contract_preserved",
    "admitted_standing_basis_referenced",
    "admitted_standing_basis_intended_for_later_separate_consumption_review",
    "selected_surface_complete_pair_preserved",
    "source_family_semantic_ownership_preserved",
    "declared_matter_use_exact",
    "historical_completed_lineage_preserved",
    "result_level_non_claims_canonical_false",
)

CODE_RECORDED = "REQUEST_FORMATION_RECORDED"
CODE_ADDITIONAL_BASIS = "REQUIRED_REQUEST_FORMATION_BASIS_MISSING"
CODE_MALFORMED = "REQUEST_FORMATION_ENVELOPE_MALFORMED"
CODE_SCHEMA = "REQUEST_FORMATION_SCHEMA_INVALID"
CODE_FIXED_IDENTITY = "FIXED_REQUEST_IDENTITY_CONTRADICTED"
CODE_IDENTITY_REPLAY = "REQUEST_IDENTITY_REPLAY_ATTEMPTED"
CODE_TARGET_NOT_SUPPORTED = "TARGET_BOUNDARY_NOT_SUPPORTED"
CODE_DECLARED_USE_NOT_SUPPORTED = "DECLARED_MATTER_USE_NOT_SUPPORTED"
CODE_ADMITTED_BASIS_MISMATCH = "ADMITTED_STANDING_BASIS_MISMATCH"
CODE_BASIS_REFERENCE_POSTURE = "BASIS_REFERENCE_POSTURE_VIOLATION"
CODE_FRESHNESS_POSTURE = "FRESHNESS_OR_NON_REPLAY_POSTURE_VIOLATION"
CODE_HISTORICAL_LINEAGE = "HISTORICAL_COMPLETED_LINEAGE_MISMATCH"
CODE_NON_CLAIM = "REQUIRED_NON_CLAIM_MISSING_OR_FLIPPED"

BLOCK_CODES = frozenset(
    {
        CODE_RECORDED,
        CODE_ADDITIONAL_BASIS,
        CODE_MALFORMED,
        CODE_SCHEMA,
        CODE_FIXED_IDENTITY,
        CODE_IDENTITY_REPLAY,
        CODE_TARGET_NOT_SUPPORTED,
        CODE_DECLARED_USE_NOT_SUPPORTED,
        CODE_ADMITTED_BASIS_MISMATCH,
        CODE_BASIS_REFERENCE_POSTURE,
        CODE_FRESHNESS_POSTURE,
        CODE_HISTORICAL_LINEAGE,
        CODE_NON_CLAIM,
    }
)


def _canonical_selected_surface() -> dict[str, Any]:
    return {
        "selected_surface_identity": SELECTED_SURFACE_IDENTITY,
        "selected_surface_type": SELECTED_SURFACE_TYPE,
        "selected_surface_version": SELECTED_SURFACE_VERSION,
        "selected_surface_scope": SELECTED_SURFACE_SCOPE,
        "selected_surface_reference": SELECTED_SURFACE_REFERENCE,
        "selected_surface_content_identity": SELECTED_SURFACE_CONTENT_IDENTITY,
        "complete_pair_preserved": True,
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_FAMILY_SEMANTIC_OWNER,
        "candidate_record_ids": list(CANDIDATE_RECORD_IDS),
        "candidate_basis_ids": list(CANDIDATE_BASIS_IDS),
    }


def _canonical_target_boundary() -> dict[str, Any]:
    return {
        "target_boundary_id": TARGET_BOUNDARY_ID,
        "target_boundary_type": TARGET_BOUNDARY_TYPE,
        "target_boundary_version": TARGET_BOUNDARY_VERSION,
        "target_boundary_scope": TARGET_BOUNDARY_SCOPE,
        "target_boundary_contract_reference": TARGET_BOUNDARY_CONTRACT_REFERENCE,
        "target_boundary_contract_content_identity": (
            TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY
        ),
        "target_boundary_admissible_future_route": (
            TARGET_BOUNDARY_ADMISSIBLE_FUTURE_ROUTE
        ),
    }


def _canonical_intended_admitted_standing_basis() -> dict[str, Any]:
    supplied = (
        _admission
        .build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request()
    )
    selected_surface = copy.deepcopy(supplied["selected_surface"])
    if selected_surface != _canonical_selected_surface():
        raise ValueError("canonical admitted material does not match the fixed selected surface")

    admission_binding = copy.deepcopy(supplied["admission_level_binding"])
    fixed_binding = {
        "selected_surface_identity": SELECTED_SURFACE_IDENTITY,
        "selected_surface_type": SELECTED_SURFACE_TYPE,
        "selected_surface_reference": SELECTED_SURFACE_REFERENCE,
        "selected_surface_content_identity": SELECTED_SURFACE_CONTENT_IDENTITY,
        "complete_pair_preserved": True,
        "candidate_record_ids": list(CANDIDATE_RECORD_IDS),
        "candidate_basis_ids": list(CANDIDATE_BASIS_IDS),
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_FAMILY_SEMANTIC_OWNER,
        "source_standing_contract_reference": SOURCE_STANDING_CONTRACT_REFERENCE,
        "source_standing_contract_content_identity": (
            SOURCE_STANDING_CONTRACT_CONTENT_IDENTITY
        ),
        "source_standing_result": SOURCE_STANDING_RESULT,
        "source_applicability_artifact_reference": (
            SOURCE_APPLICABILITY_ARTIFACT_REFERENCE
        ),
        "source_applicability_boundary_id": SOURCE_APPLICABILITY_BOUNDARY_ID,
        "source_applicability_outcome": SOURCE_APPLICABILITY_OUTCOME,
        "source_route": SOURCE_ROUTE,
        "declared_matter_use": DECLARED_MATTER_USE,
    }
    for key, expected in fixed_binding.items():
        if admission_binding.get(key) != expected:
            raise ValueError(
                f"canonical admitted material does not match fixed binding field {key}"
            )

    return {
        "standing_basis_admission_id": STANDING_BASIS_ADMISSION_ID,
        "standing_basis_admission_type": STANDING_BASIS_ADMISSION_TYPE,
        "standing_basis_admission_version": STANDING_BASIS_ADMISSION_VERSION,
        "standing_basis_admission_scope": STANDING_BASIS_ADMISSION_SCOPE,
        "standing_basis_admission_outcome": STANDING_BASIS_ADMISSION_OUTCOME,
        "standing_basis_admission_failed_check_count": (
            STANDING_BASIS_ADMISSION_FAILED_CHECK_COUNT
        ),
        "standing_basis_admission_review_exhausted": (
            STANDING_BASIS_ADMISSION_REVIEW_EXHAUSTED
        ),
        "standing_basis_admission_reference": STANDING_BASIS_ADMISSION_REFERENCE,
        "standing_basis_admission_content_identity": (
            STANDING_BASIS_ADMISSION_CONTENT_IDENTITY
        ),
        "standing_basis_admission_declared_use": DECLARED_MATTER_USE,
        "selected_surface": selected_surface,
        "source_standing_contract_reference": SOURCE_STANDING_CONTRACT_REFERENCE,
        "source_standing_contract_content_identity": (
            SOURCE_STANDING_CONTRACT_CONTENT_IDENTITY
        ),
        "source_standing_result": SOURCE_STANDING_RESULT,
        "source_applicability_artifact_reference": (
            SOURCE_APPLICABILITY_ARTIFACT_REFERENCE
        ),
        "source_applicability_boundary_id": SOURCE_APPLICABILITY_BOUNDARY_ID,
        "source_applicability_outcome": SOURCE_APPLICABILITY_OUTCOME,
        "source_route": SOURCE_ROUTE,
        "source_applicability_result": copy.deepcopy(
            supplied["source_applicability_result"]
        ),
        "admission_level_binding": admission_binding,
    }


def _canonical_basis_reference_posture() -> dict[str, bool]:
    return {
        "admitted_standing_basis_referenced": True,
        "admitted_standing_basis_intended_for_later_separate_consumption_review": True,
        "admitted_standing_basis_consumed": False,
        "admitted_standing_basis_exhausted": False,
        "consumption_token_closed": False,
        "consumption_authorized": False,
        "basis_reuse_permission_created": False,
    }


def _canonical_freshness_and_non_replay() -> dict[str, bool]:
    return {
        "fresh_request_identity_declared": True,
        "request_identity_distinct_from_target_boundary": True,
        "request_identity_distinct_from_historical_completed_lineage": True,
        "historical_request_identity_reused": False,
        "historical_request_material_reused": False,
        "historical_request_reopened": False,
        "historical_request_mutated": False,
        "historical_request_replayed": False,
        "historical_standing_basis_substituted": False,
        "historical_success_treated_as_fresh_permission": False,
    }


def _canonical_historical_completed_lineage() -> dict[str, str]:
    return {
        "historical_boundary_result_reference": HISTORICAL_BOUNDARY_RESULT_REFERENCE,
        "historical_boundary_result_content_identity": (
            HISTORICAL_BOUNDARY_RESULT_CONTENT_IDENTITY
        ),
        "historical_boundary_outcome": HISTORICAL_BOUNDARY_OUTCOME,
        "historical_boundary_result": HISTORICAL_BOUNDARY_RESULT,
    }


def build_declared_descendant_body_creation_boundary_request_v0_min_request() -> (
    dict[str, Any]
):
    """Build the one exact closed in-memory request-formation envelope."""

    request_object = {
        "request_id": REQUEST_ID,
        "request_type": REQUEST_TYPE,
        "request_version": REQUEST_VERSION,
        "request_scope": REQUEST_SCOPE,
        "request_question": REQUEST_QUESTION,
        "request_intent": REQUEST_INTENT,
        "target_boundary": _canonical_target_boundary(),
        "declared_matter_use": DECLARED_MATTER_USE,
        "intended_admitted_standing_basis": (
            _canonical_intended_admitted_standing_basis()
        ),
        "basis_reference_posture": _canonical_basis_reference_posture(),
        "freshness_and_non_replay": _canonical_freshness_and_non_replay(),
        "declared_non_claims": copy.deepcopy(CANONICAL_NON_CLAIMS),
    }
    return {
        "request_object": request_object,
        "historical_completed_lineage": _canonical_historical_completed_lineage(),
    }


def _compare_closed(actual: Any, expected: Any, path: str) -> tuple[str, str] | None:
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            return ("malformed", path)
        missing = set(expected) - set(actual)
        extra = set(actual) - set(expected)
        if missing and extra:
            return ("extra", path)
        if missing:
            return ("missing", f"{path}.{sorted(missing)[0]}")
        if extra:
            return ("extra", f"{path}.{sorted(extra)[0]}")
        for key in expected:
            mismatch = _compare_closed(actual[key], expected[key], f"{path}.{key}")
            if mismatch is not None:
                return mismatch
        return None

    if isinstance(expected, list):
        if not isinstance(actual, list):
            return ("malformed", path)
        if len(actual) != len(expected):
            return ("mismatch", path)
        for index, expected_item in enumerate(expected):
            mismatch = _compare_closed(
                actual[index], expected_item, f"{path}[{index}]"
            )
            if mismatch is not None:
                return mismatch
        return None

    if type(actual) is not type(expected):
        return ("malformed", path)
    if actual != expected:
        return ("mismatch", path)
    return None


def _terminal(
    outcome: str,
    code: str,
    reason: str,
    request_object: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    request_formation = {
        key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS
    }
    request_formation["result_level_non_claims_canonical_false"] = True
    checks = [
        {
            "check_id": "closed_request_formation_envelope",
            "passed": recorded,
            "failure_code": None if recorded else code,
        }
    ]
    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "recorded_request_object": (
            copy.deepcopy(dict(request_object)) if recorded else None
        ),
        "request_formation": request_formation,
        "historical_completed_lineage": (
            _canonical_historical_completed_lineage() if recorded else None
        ),
        "checks": checks,
        "passed_check_count": 1 if recorded else 0,
        "failed_check_count": 0 if recorded else 1,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code,
            "reason": reason,
        },
        "review_exhausted": True,
        "request_admission_performed": False,
        "basis_consumption_performed": False,
        "consumption_token_closed": False,
        "boundary_consideration_performed": False,
        "invocation_performed": False,
        "execution_performed": False,
        "non_claims": copy.deepcopy(CANONICAL_NON_CLAIMS),
    }


def _additional(reason: str) -> dict[str, Any]:
    return _terminal(OUTCOME_REQUIRES_ADDITIONAL_BASIS, CODE_ADDITIONAL_BASIS, reason)


def _blocked(code: str, reason: str) -> dict[str, Any]:
    return _terminal(OUTCOME_BLOCKED, code, reason)


def _not_recorded(code: str, reason: str) -> dict[str, Any]:
    return _terminal(OUTCOME_NOT_RECORDED, code, reason)


def _route_comparison(
    actual: Any,
    expected: Any,
    path: str,
    mismatch_outcome: str,
    mismatch_code: str,
) -> dict[str, Any] | None:
    mismatch = _compare_closed(actual, expected, path)
    if mismatch is None:
        return None
    kind, location = mismatch
    if kind == "missing":
        return _additional(f"required field absent: {location}")
    if kind in {"malformed", "extra"}:
        return _blocked(CODE_SCHEMA, f"closed shape violated at {location}")
    if mismatch_outcome == OUTCOME_NOT_RECORDED:
        return _not_recorded(mismatch_code, f"exact value not supported at {location}")
    return _blocked(mismatch_code, f"exact value contradicted at {location}")


def resolve_descendant_body_creation_boundary_request_v0_min(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Resolve one supplied request-formation envelope without external effects."""

    if supplied_envelope is None:
        return _additional("request-formation envelope is absent")
    if not isinstance(supplied_envelope, Mapping):
        return _blocked(CODE_MALFORMED, "request-formation envelope must be a mapping")

    extra_envelope = set(supplied_envelope) - ENVELOPE_KEYS
    missing_envelope = ENVELOPE_KEYS - set(supplied_envelope)
    if missing_envelope and extra_envelope:
        return _blocked(CODE_SCHEMA, "envelope substitution or mixed schema detected")
    if extra_envelope:
        return _blocked(
            CODE_SCHEMA, f"unknown envelope section: {sorted(extra_envelope)[0]}"
        )
    if missing_envelope:
        return _additional(
            f"required envelope section absent: {sorted(missing_envelope)[0]}"
        )

    request_object = supplied_envelope["request_object"]
    if not isinstance(request_object, Mapping):
        return _blocked(CODE_MALFORMED, "request_object must be one mapping")

    extra_request = set(request_object) - REQUEST_OBJECT_KEYS
    missing_request = REQUEST_OBJECT_KEYS - set(request_object)
    if missing_request and extra_request:
        return _blocked(CODE_SCHEMA, "request-object substitution or mixed schema detected")
    if extra_request:
        return _blocked(
            CODE_SCHEMA, f"unknown request-object field: {sorted(extra_request)[0]}"
        )
    if missing_request:
        return _additional(
            f"required request field absent: {sorted(missing_request)[0]}"
        )

    fixed_request_fields = {
        "request_id": REQUEST_ID,
        "request_type": REQUEST_TYPE,
        "request_version": REQUEST_VERSION,
        "request_scope": REQUEST_SCOPE,
        "request_question": REQUEST_QUESTION,
        "request_intent": REQUEST_INTENT,
    }
    for key, expected in fixed_request_fields.items():
        actual = request_object[key]
        if type(actual) is not type(expected):
            return _blocked(CODE_MALFORMED, f"{key} must be one exact string")
        if actual != expected:
            if key == "request_id" and actual in {
                TARGET_BOUNDARY_ID,
                HISTORICAL_BOUNDARY_RESULT,
                HISTORICAL_BOUNDARY_OUTCOME,
            }:
                return _blocked(
                    CODE_IDENTITY_REPLAY,
                    "fresh request identity reuses target or historical identity",
                )
            return _blocked(CODE_FIXED_IDENTITY, f"fixed request field contradicted: {key}")

    routed = _route_comparison(
        request_object["target_boundary"],
        _canonical_target_boundary(),
        "request_object.target_boundary",
        OUTCOME_NOT_RECORDED,
        CODE_TARGET_NOT_SUPPORTED,
    )
    if routed is not None:
        return routed

    declared_use = request_object["declared_matter_use"]
    if not isinstance(declared_use, str):
        return _blocked(CODE_MALFORMED, "declared_matter_use must be one string")
    if declared_use != DECLARED_MATTER_USE:
        return _not_recorded(
            CODE_DECLARED_USE_NOT_SUPPORTED,
            "complete declared matter/use is incompatible with the fixed request",
        )

    intended_basis = request_object["intended_admitted_standing_basis"]
    routed = _route_comparison(
        intended_basis,
        _canonical_intended_admitted_standing_basis(),
        "request_object.intended_admitted_standing_basis",
        OUTCOME_BLOCKED,
        CODE_ADMITTED_BASIS_MISMATCH,
    )
    if routed is not None:
        return routed

    if intended_basis["standing_basis_admission_declared_use"] != declared_use:
        return _blocked(
            CODE_ADMITTED_BASIS_MISMATCH,
            "admission declared use does not bind to request declared use",
        )
    if intended_basis["source_route"] != declared_use:
        return _blocked(
            CODE_ADMITTED_BASIS_MISMATCH,
            "source route does not bind to request declared use",
        )

    routed = _route_comparison(
        request_object["basis_reference_posture"],
        _canonical_basis_reference_posture(),
        "request_object.basis_reference_posture",
        OUTCOME_BLOCKED,
        CODE_BASIS_REFERENCE_POSTURE,
    )
    if routed is not None:
        return routed

    routed = _route_comparison(
        request_object["freshness_and_non_replay"],
        _canonical_freshness_and_non_replay(),
        "request_object.freshness_and_non_replay",
        OUTCOME_BLOCKED,
        CODE_FRESHNESS_POSTURE,
    )
    if routed is not None:
        return routed

    routed = _route_comparison(
        supplied_envelope["historical_completed_lineage"],
        _canonical_historical_completed_lineage(),
        "historical_completed_lineage",
        OUTCOME_BLOCKED,
        CODE_HISTORICAL_LINEAGE,
    )
    if routed is not None:
        return routed

    routed = _route_comparison(
        request_object["declared_non_claims"],
        CANONICAL_NON_CLAIMS,
        "request_object.declared_non_claims",
        OUTCOME_BLOCKED,
        CODE_NON_CLAIM,
    )
    if routed is not None:
        return routed

    return _terminal(
        OUTCOME_RECORDED,
        CODE_RECORDED,
        "one exact fresh request object was formed and recorded only",
        request_object=request_object,
    )


__all__ = [
    "ALLOWED_TRUE_RECORDED_FIELDS",
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "DECLARED_MATTER_USE",
    "ENVELOPE_KEYS",
    "OUTCOME_BLOCKED",
    "OUTCOME_FAMILY",
    "OUTCOME_NOT_RECORDED",
    "OUTCOME_RECORDED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "REQUEST_ID",
    "REQUEST_INTENT",
    "REQUEST_OBJECT_KEYS",
    "REQUEST_SCOPE",
    "REQUEST_TYPE",
    "REQUEST_VERSION",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_VERSION",
    "build_declared_descendant_body_creation_boundary_request_v0_min_request",
    "resolve_descendant_body_creation_boundary_request_v0_min",
]
