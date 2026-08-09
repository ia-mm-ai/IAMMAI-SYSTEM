"""Pure resolver for one bounded descendant-body-creation operation request."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_descendant_body_creation_operation_request_v0_min"
RESULT_VERSION = "0.1.0"

OPERATION_FAMILY = "DESCENDANT_BODY_CREATION_OPERATION"
OPERATION_ID = "descendant_body_creation_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CREATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"

OPERATION_REQUEST_ID = "descendant_body_creation_operation_request_001"
OPERATION_REQUEST_TYPE = "DESCENDANT_BODY_CREATION_OPERATION_REQUEST"
OPERATION_REQUEST_VERSION = "0.1.0"
OPERATION_REQUEST_SCOPE = (
    "ONE_FRESH_DESCENDANT_BODY_CREATION_OPERATION_REQUEST_ONE_CURRENT_V3_"
    "BOUNDARY_RESULT_ONLY"
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CREATION_OPERATION_REQUEST"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CREATION_OPERATION_REQUEST"
INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD)

REQUEST_QUESTION = (
    "May one exact fresh DESCENDANT_BODY_CREATION_OPERATION_REQUEST, identified as "
    "descendant_body_creation_operation_request_001, address persistent operation "
    "descendant_body_creation_operation_001 under the exact current V3 target-boundary "
    "result recording DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED, while "
    "preserving the exact request, admission, and actual-consumption lineage, complete "
    "Candidate A/B pair, source semantic ownership, source applicability, operation "
    "contract, declared use, freshness and historical non-replay, without performing or "
    "authorizing the operation?"
)

OUTCOME_BLOCKED = "DESCENDANT_BODY_CREATION_OPERATION_REQUEST_BLOCKED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CREATION_OPERATION_REQUEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CREATION_OPERATION_REQUEST_NOT_RECORDED"
OUTCOME_RECORDED = "DESCENDANT_BODY_CREATION_OPERATION_REQUEST_RECORDED"
OUTCOMES = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
    OUTCOME_RECORDED,
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INPUT",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
        "ORDINARY_REQUEST_BASIS_INVALID",
    }
)
REQUIREMENT_CODE_ORDINARY_ABSENT = "ORDINARY_REQUEST_BASIS_ABSENT"

CURRENT_BOUNDARY_RESULT_REFERENCE = (
    "artifacts/descendant_body_creation_boundary_v0_min_v3/"
    "descendant_body_creation_boundary_001__"
    "descendant_body_creation_boundary_v0_min_v3_result.json"
)
CURRENT_BOUNDARY_RESULT_SHA256 = (
    "49f053a7deba05fdb18dc914a5be7d3a7dfef90aa6e81e16cc2f8de47d6952da"
)
OPERATION_CONTRACT_REFERENCE = "spec/DESCENDANT_BODY_CREATION_OPERATION_V0_MIN_SPEC.md"
OPERATION_CONTRACT_SHA256 = (
    "82cf281c103c53742dc963435df1a0efdb62037f591db926f9ea7a63dc33f6f4"
)
SOURCE_DECLARED_MATTER_USE = (
    "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
)
TARGET_ROUTE = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_THEN_DESCENDANT_BODY_CREATION_OPERATION_ONLY"
)
LATER_OPEN_RANK = "DESCENDANT_BODY_CREATION_OPERATION"


EXPECTED_CONSTITUTIONAL_EVENT_KEY = {
    "operation_request": {
        "operation_request_id": OPERATION_REQUEST_ID,
        "operation_request_type": OPERATION_REQUEST_TYPE,
        "operation_request_version": OPERATION_REQUEST_VERSION,
        "operation_request_scope": OPERATION_REQUEST_SCOPE,
    },
    "operation": {
        "operation_family": OPERATION_FAMILY,
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
    },
    "current_request": {
        "request_id": "descendant_body_creation_boundary_request_001",
        "request_type": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST",
        "request_version": "0.1.0",
        "request_scope": (
            "ONE_FRESH_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ONE_EXACT_"
            "ADMITTED_STANDING_BASIS_ONLY"
        ),
        "request_outcome": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_RECORDED",
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_v0_min/"
            "descendant_body_creation_boundary_request_001__"
            "descendant_body_creation_boundary_request_v0_min_result.json"
        ),
        "result_sha256": (
            "00ae4d23b703ac57f6eecf684e8c64d8bb7ca7fb0ff418b4d6a453813ffc5ef8"
        ),
        "declared_matter_use": SOURCE_DECLARED_MATTER_USE,
        "requested_target_boundary_id": "descendant_body_creation_boundary_001",
    },
    "current_request_admission": {
        "request_admission_id": "descendant_body_creation_boundary_request_admission_001",
        "request_admission_type": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION",
        "request_admission_version": "0.1.0",
        "request_admission_scope": (
            "ONE_EXACT_RECORDED_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_"
            "ADMISSION_ONLY"
        ),
        "request_admission_outcome": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED"
        ),
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_admission_v0_min_v2/"
            "descendant_body_creation_boundary_request_admission_001__"
            "descendant_body_creation_boundary_request_admission_v0_min_v2_result.json"
        ),
        "result_sha256": (
            "57c3272f7a0f3f36678397162573bae0836cf77f1db11ac2bb874efa66ff778d"
        ),
        "request_admitted": True,
        "bound_request_id": "descendant_body_creation_boundary_request_001",
        "bound_standing_basis_admission_id": (
            "matter_bound_selected_surface_standing_basis_admission_001"
        ),
    },
    "actual_consumption": {
        "actual_consumption_id": (
            "descendant_body_creation_boundary_request_admitted_standing_basis_"
            "consumption_request_001"
        ),
        "actual_consumption_type": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
            "CONSUMPTION"
        ),
        "actual_consumption_version": "0.1.0",
        "actual_consumption_scope": (
            "ONE_EXACT_ADMITTED_STANDING_BASIS_ONE_EXACT_ADMITTED_DESCENDANT_BODY_"
            "CREATION_BOUNDARY_REQUEST_ONE_SHOT_CONSUMPTION_AND_EXHAUSTION_ONLY"
        ),
        "actual_consumption_outcome": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
            "CONSUMED"
        ),
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_admitted_standing_"
            "basis_consumption_v0_min_v2/descendant_body_creation_boundary_request_"
            "admitted_standing_basis_consumption_request_001__descendant_body_creation_"
            "boundary_request_admitted_standing_basis_consumption_v0_min_v2_result.json"
        ),
        "result_sha256": (
            "b50484a89aeb06e4e903b66e1a48d00f77cd12575a99af55c33ebcbe01f1abd5"
        ),
        "basis_consumed": True,
        "basis_exhausted": True,
        "basis_consumption_performed": True,
        "basis_exhaustion_performed": True,
        "one_shot_consumption_preserved": True,
        "one_shot_availability_closed": True,
        "consumed_request_basis_recorded": True,
        "consumption_token_closed": True,
        "exact_consumption_identity_preserved": True,
        "exact_request_preserved": True,
        "exact_request_admission_preserved": True,
        "exact_pre_consumption_boundary_preserved": True,
        "exact_standing_basis_admission_preserved": True,
        "selected_surface_complete_pair_preserved": True,
        "source_family_semantic_ownership_preserved": True,
        "declared_matter_use_preserved": True,
        "freshness_and_non_replay_preserved": True,
        "target_boundary_consideration_requires_separate_review": True,
        "invocation_and_execution_require_separate_review": True,
        "result_level_non_claims_canonical_false": True,
    },
    "current_boundary": {
        "boundary_id": "descendant_body_creation_boundary_001",
        "boundary_type": "DESCENDANT_BODY_CREATION_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": (
            "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY"
        ),
        "result_reference": CURRENT_BOUNDARY_RESULT_REFERENCE,
        "result_sha256": CURRENT_BOUNDARY_RESULT_SHA256,
        "outcome": "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
        "boundary_result": "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
        "result_version": "0.3.0",
        "resolver_module": "resolve_descendant_body_creation_boundary_v0_min_v3",
        "review_terminal": True,
        "review_exhausted": True,
        "operation_consideration_is_only_positive_consequence": True,
        "blocked": False,
        "block_code": None,
        "block_issue_path": None,
        "block_requirement_code": None,
        "target_boundary_contract_reference": (
            "spec/DESCENDANT_BODY_CREATION_BOUNDARY_V0_MIN_SPEC.md"
        ),
        "target_boundary_contract_sha256": (
            "0b66c2419a1fe4e480192755858268aab0d7f8d109822a99fcf83e3d785be273"
        ),
        "source_declared_matter_use": SOURCE_DECLARED_MATTER_USE,
        "target_route": TARGET_ROUTE,
    },
    "operation_contract": {
        "operation_contract_reference": OPERATION_CONTRACT_REFERENCE,
        "operation_contract_sha256": OPERATION_CONTRACT_SHA256,
        "operation_contract_family": OPERATION_FAMILY,
        "operation_contract_operation_id": OPERATION_ID,
        "operation_contract_type": OPERATION_TYPE,
        "operation_contract_version": OPERATION_VERSION,
        "operation_contract_scope": OPERATION_SCOPE,
        "operation_contract_future_route": (
            "DESCENDANT_BODY_CREATION_OPERATION_THEN_FIRST_CROSSING_BOUNDARY_ONLY"
        ),
    },
    "selected_surface": {
        "selected_surface_identity": "descendant_body_candidate_standing_operation_001",
        "selected_surface_type": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "selected_surface_version": "0.1.0",
        "selected_surface_scope": (
            "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
        ),
        "selected_surface_result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_"
            "standing_operation_v0_min/descendant_body_candidate_standing_operation_"
            "001__candidate_standing_operation_v0_min_result.json"
        ),
        "selected_surface_result_sha256": (
            "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961"
        ),
        "selected_surface_family": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "selected_surface_semantic_owner": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
        ),
        "source_standing_contract_reference": (
            "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
        ),
        "source_standing_contract_sha256": (
            "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3"
        ),
        "source_standing_contract_version": "0.1.0",
        "candidate_a_record_id": "descendant_body_basis_candidate_a_001",
        "candidate_a_role": "CANDIDATE_A",
        "candidate_a_basis_id": (
            "descendant_body_basis_candidate_a_001__motion_side_admissible_"
            "variation_basis"
        ),
        "candidate_a_basis_label": (
            "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
        ),
        "candidate_b_record_id": "descendant_body_basis_candidate_b_001",
        "candidate_b_role": "CANDIDATE_B",
        "candidate_b_basis_id": (
            "descendant_body_basis_candidate_b_001__regulation_side_"
            "admissibility_bounds_basis"
        ),
        "candidate_b_basis_label": (
            "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
        ),
        "basis_pair_scope": "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
        "complete_pair_preserved": True,
        "candidate_records_remain_sibling": True,
        "candidate_record_non_hierarchy_preserved": True,
        "candidate_basis_non_hierarchy_preserved": True,
        "source_custody_preserved": True,
        "source_lineage_preserved": True,
        "source_rank_preserved": True,
        "source_scope_preserved": True,
    },
    "source_applicability": {
        "source_applicability_id": (
            "descendant_body_candidate_standing_effect_applicability_boundary_001"
        ),
        "source_applicability_type": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY"
        ),
        "source_applicability_version": "0.1.0",
        "source_applicability_scope": (
            "ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_ONE_EXACT_DECLARED_"
            "DOWNSTREAM_USE_ONLY"
        ),
        "source_applicability_outcome": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED"
        ),
        "result_reference": (
            "artifacts/descendant_body_candidate_standing_effect_applicability_"
            "boundary_v0_min_v2/descendant_body_candidate_standing_effect_"
            "applicability_boundary_001__descendant_body_candidate_standing_effect_"
            "applicability_boundary_v0_min_v2_result.json"
        ),
        "complete_review_reached": True,
        "source_route": SOURCE_DECLARED_MATTER_USE,
        "source_declared_matter_use": SOURCE_DECLARED_MATTER_USE,
    },
    "declared_use": {
        "operation_request_declared_use": TARGET_ROUTE,
        "target_route": TARGET_ROUTE,
    },
    "freshness": {
        "fresh_operation_request_identity_declared": True,
        "operation_request_identity_distinct_from_operation_identity": True,
        "operation_request_identity_distinct_from_historical_occurrence": True,
        "historical_operation_result_is_current_permission": False,
        "historical_operation_result_is_current_request": False,
        "historical_operation_result_is_current_occurrence": False,
        "historical_operation_occurrence_reused": False,
        "historical_operation_material_reused": False,
        "historical_operation_result_replayed": False,
        "historical_success_treated_as_fresh_permission": False,
    },
    "historical_operation": {
        "historical_operation_id": OPERATION_ID,
        "result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_creation_"
            "operation_v0_min/descendant_body_creation_operation_001__"
            "descendant_body_creation_operation_v0_min_result.json"
        ),
        "result_sha256": (
            "8a19e961d1a27ed0ce9898d545b3e2f790a3cd16ac1ebb09177dfd3b07bc7d15"
        ),
        "outcome": "DESCENDANT_BODY_CREATION_OPERATION_CREATED",
        "operation_result": "DESCENDANT_BODY_CREATION_SUPPORTED",
    },
    "non_claim_attribution": {
        "request_formation_declared": {
            "owner": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"
        },
        "request_formation_result": {
            "owner": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"
        },
        "request_admission": {
            "owner": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION"
        },
        "pre_consumption": {
            "owner": (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
                "CONSUMPTION_BOUNDARY"
            )
        },
        "standing_basis_admission": {
            "owner": "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION"
        },
        "source_applicability": {
            "owner": (
                "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY"
            )
        },
        "source_family": {
            "owner": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
        },
        "actual_consumption": {
            "owner": (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
                "CONSUMPTION"
            )
        },
        "target_local": {"owner": "DESCENDANT_BODY_CREATION_BOUNDARY"},
        "operation_request_local": {"owner": OPERATION_REQUEST_TYPE},
    },
}


EXPECTED_ORDINARY_REQUEST_BASIS = {
    "source_outcome": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED",
    "source_standing_result": "CANDIDATE_STANDING_SUPPORTED",
    "candidate_standing_supported": True,
    "candidate_standing_authorized": True,
    "candidate_standing_created": True,
    "candidate_a_standing_created": True,
    "candidate_b_standing_created": True,
    "candidate_standing_effect_applicability_recorded": True,
    "candidate_standing_effect_applicable_to_declared_use": True,
    "declared_use_exactly_matches_source_route": True,
    "source_family_semantic_ownership_preserved": True,
}


LOCAL_NON_CLAIM_KEYS = tuple(
    """
    operation_request_admitted operation_request_authorized operation_request_reused
    operation_authorized operation_performed operation_occurrence_established
    operation_result_created invocation_request_admitted invocation_authorized
    invocation_performed execution_permission_created execution_performed
    descendant_body_creation_authorized descendant_body_creation_executed
    descendant_body_creation_performed descendant_body_a_created
    descendant_body_b_created descendant_body_created standing_created
    standing_descendant_created source_applicability_created authority_created
    currentness_created relation_created presence_established identity_created
    coupling_created crossing_authorized runtime_created
    historical_operation_occurrence_reused historical_operation_material_reused
    historical_operation_result_replayed historical_success_treated_as_fresh_permission
    candidate_pair_split candidate_pair_ranked semantic_ownership_transferred
    source_route_widened request_reuse_permission_created repeat_permission_created
    continuation_permission_created follow_on_permission_created
    automatic_successor_created follow_on_work_authorized registry_created
    catalogue_created ontology_created repository_scan_performed
    file_discovery_performed artifact_existence_treated_as_operation_permission
    resolver_call_count_treated_as_event_count
    """.split()
)
EXPECTED_REQUIRED_NON_CLAIMS = {
    "operation_request_local": {key: False for key in LOCAL_NON_CLAIM_KEYS}
}

POSITIVE_REQUEST_FIELDS = (
    "descendant_body_creation_operation_request_recorded",
    "exact_operation_request_identity_preserved",
    "persistent_operation_target_preserved",
    "current_v3_boundary_result_preserved",
    "current_lineage_binding_preserved",
    "operation_contract_preserved",
    "selected_surface_complete_pair_preserved",
    "source_family_semantic_ownership_preserved",
    "source_applicability_preserved",
    "declared_matter_use_preserved",
    "freshness_and_non_replay_preserved",
    "result_level_non_claims_canonical_false",
)


def _leaf_paths(value: Mapping[str, Any], prefix: str) -> tuple[str, ...]:
    paths: list[str] = []
    for key in sorted(value):
        path = f"{prefix}.{key}"
        child = value[key]
        if isinstance(child, Mapping):
            paths.extend(_leaf_paths(child, path))
        else:
            paths.append(path)
    return tuple(paths)


CONTROL_PATHS = frozenset({"$::mapping_cardinality", "intent", "request_question"})
CONSTITUTIONAL_EVENT_KEY_PATHS = frozenset(
    _leaf_paths(EXPECTED_CONSTITUTIONAL_EVENT_KEY, "constitutional_event_key")
)
ORDINARY_REQUEST_BASIS_PATHS = frozenset(
    f"ordinary_request_basis.{key}" for key in EXPECTED_ORDINARY_REQUEST_BASIS
)
REQUIRED_NON_CLAIM_OWNER_PATHS = frozenset(
    {"required_non_claims.operation_request_local"}
)
REQUIRED_NON_CLAIM_PATHS = REQUIRED_NON_CLAIM_OWNER_PATHS | frozenset(
    f"required_non_claims.operation_request_local.{key}" for key in LOCAL_NON_CLAIM_KEYS
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_REQUEST_BASIS": ORDINARY_REQUEST_BASIS_PATHS,
    "REQUIRED_NON_CLAIM": REQUIRED_NON_CLAIM_PATHS,
}
ALL_REQUIRED_PATHS = frozenset().union(*CLASS_PATHS.values())
EXECUTABLE_ROOT_KEYS = frozenset(
    {
        "intent",
        "request_question",
        "constitutional_event_key",
        "ordinary_request_basis",
        "required_non_claims",
    }
)


assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 148
assert len(ORDINARY_REQUEST_BASIS_PATHS) == 11
assert len(LOCAL_NON_CLAIM_KEYS) == 50
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & other_paths
        for other_name, other_paths in CLASS_PATHS.items()
        if other_name != _class_name
    )


def build_descendant_body_creation_operation_request_v0_min_envelope() -> dict[str, Any]:
    """Return the canonical in-memory request envelope without external effects."""

    return {
        "intent": INTENT_RECORD,
        "request_question": REQUEST_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_request_basis": deepcopy(EXPECTED_ORDINARY_REQUEST_BASIS),
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


def _same_exact_value(actual: Any, expected: Any) -> bool:
    return type(actual) is type(expected) and actual == expected


def _check(
    check_id: str,
    classification: str,
    passed: bool,
    path: str,
    failure_code: str | None = None,
    requirement_code: str | None = None,
) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "classification": classification,
        "path": path,
        "passed": bool(passed),
        "failure_code": failure_code if not passed else None,
        "requirement_code": requirement_code if not passed else None,
    }


def _validate_exact_mapping(
    actual: Any,
    expected: Mapping[str, Any],
    prefix: str,
    classification: str,
    failure_code: str,
) -> tuple[bool, list[dict[str, Any]], str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(actual, Mapping):
        checks.append(
            _check(
                f"{classification.lower()}_mapping",
                classification,
                False,
                prefix,
                failure_code,
            )
        )
        return False, checks, prefix

    actual_keys = set(actual)
    expected_keys = set(expected)
    extras = sorted(actual_keys - expected_keys)
    missing = sorted(expected_keys - actual_keys)
    shape_passed = not extras and not missing
    checks.append(
        _check(
            f"{classification.lower()}_shape_{prefix.replace('.', '_')}",
            classification,
            shape_passed,
            prefix,
            failure_code,
        )
    )
    first_error = (
        f"{prefix}.{extras[0]}"
        if extras
        else f"{prefix}.{missing[0]}"
        if missing
        else None
    )

    valid = shape_passed
    for key in sorted(expected_keys & actual_keys):
        expected_value = expected[key]
        actual_value = actual[key]
        path = f"{prefix}.{key}"
        if isinstance(expected_value, Mapping):
            child_valid, child_checks, child_error = _validate_exact_mapping(
                actual_value,
                expected_value,
                path,
                classification,
                failure_code,
            )
            checks.extend(child_checks)
            valid = valid and child_valid
            if first_error is None and child_error is not None:
                first_error = child_error
        else:
            passed = _same_exact_value(actual_value, expected_value)
            checks.append(
                _check(
                    f"{classification.lower()}_{path.replace('.', '_')}",
                    classification,
                    passed,
                    path,
                    failure_code,
                )
            )
            valid = valid and passed
            if first_error is None and not passed:
                first_error = path
    return valid, checks, first_error


def _control_review(
    envelope: Any,
) -> tuple[bool, list[dict[str, Any]], str | None, str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(envelope, Mapping):
        checks.append(
            _check(
                "control_single_mapping",
                "CONTROL",
                False,
                "$::mapping_cardinality",
                "REQUEST_NOT_MAPPING",
            )
        )
        return False, checks, "$::mapping_cardinality", "REQUEST_NOT_MAPPING"

    checks.append(_check("control_single_mapping", "CONTROL", True, "$::mapping_cardinality"))
    unknown = sorted(set(envelope) - EXECUTABLE_ROOT_KEYS)
    checks.append(
        _check(
            "control_root_has_no_unsupported_fields",
            "CONTROL",
            not unknown,
            "$",
            "UNSUPPORTED_INPUT",
        )
    )
    if unknown:
        return False, checks, unknown[0], "UNSUPPORTED_INPUT"

    intent_valid = "intent" in envelope and any(
        _same_exact_value(envelope["intent"], intent) for intent in INTENTS
    )
    checks.append(
        _check("control_intent_is_exact", "CONTROL", intent_valid, "intent", "CONTROL_INVALID")
    )
    if not intent_valid:
        return False, checks, "intent", "CONTROL_INVALID"

    question_valid = "request_question" in envelope and _same_exact_value(
        envelope["request_question"], REQUEST_QUESTION
    )
    checks.append(
        _check(
            "control_request_question_is_exact",
            "CONTROL",
            question_valid,
            "request_question",
            "CONTROL_INVALID",
        )
    )
    if not question_valid:
        return False, checks, "request_question", "CONTROL_INVALID"
    return True, checks, None, None


def _ordinary_review(
    envelope: Mapping[str, Any],
) -> tuple[str, list[dict[str, Any]], tuple[str, ...], str | None]:
    checks: list[dict[str, Any]] = []
    if "ordinary_request_basis" not in envelope:
        missing = tuple(sorted(ORDINARY_REQUEST_BASIS_PATHS))
        for path in missing:
            checks.append(
                _check(
                    f"ordinary_{path.rsplit('.', 1)[-1]}",
                    "ORDINARY_REQUEST_BASIS",
                    False,
                    path,
                    requirement_code=REQUIREMENT_CODE_ORDINARY_ABSENT,
                )
            )
        return "missing", checks, missing, "ordinary_request_basis"

    ordinary = envelope["ordinary_request_basis"]
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_mapping",
                "ORDINARY_REQUEST_BASIS",
                False,
                "ordinary_request_basis",
                "ORDINARY_REQUEST_BASIS_INVALID",
            )
        )
        return "invalid", checks, (), "ordinary_request_basis"

    extras = sorted(set(ordinary) - set(EXPECTED_ORDINARY_REQUEST_BASIS))
    checks.append(
        _check(
            "ordinary_has_no_unsupported_fields",
            "ORDINARY_REQUEST_BASIS",
            not extras,
            "ordinary_request_basis",
            "ORDINARY_REQUEST_BASIS_INVALID",
        )
    )
    if extras:
        return "invalid", checks, (), f"ordinary_request_basis.{extras[0]}"

    missing: list[str] = []
    invalid: list[str] = []
    for key, expected in EXPECTED_ORDINARY_REQUEST_BASIS.items():
        path = f"ordinary_request_basis.{key}"
        if key not in ordinary:
            missing.append(path)
            checks.append(
                _check(
                    f"ordinary_{key}",
                    "ORDINARY_REQUEST_BASIS",
                    False,
                    path,
                    requirement_code=REQUIREMENT_CODE_ORDINARY_ABSENT,
                )
            )
            continue
        passed = _same_exact_value(ordinary[key], expected)
        if not passed:
            invalid.append(path)
        checks.append(
            _check(
                f"ordinary_{key}",
                "ORDINARY_REQUEST_BASIS",
                passed,
                path,
                "ORDINARY_REQUEST_BASIS_INVALID",
            )
        )
    if invalid:
        return "invalid", checks, (), invalid[0]
    if missing:
        return "missing", checks, tuple(missing), missing[0]
    return "exact", checks, (), None


def _event_projection(event_valid: bool, section: str) -> dict[str, Any] | None:
    if not event_valid:
        return None
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[section])


def _build_result(
    outcome: str,
    checks: list[dict[str, Any]],
    block_code: str | None,
    issue_path: str | None,
    event_valid: bool,
    missing_ordinary_paths: tuple[str, ...] = (),
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    request_posture = {field: recorded for field in POSITIVE_REQUEST_FIELDS}
    request_posture.update(
        {
            "operation_request_id": OPERATION_REQUEST_ID,
            "operation_request_type": OPERATION_REQUEST_TYPE,
            "operation_request_version": OPERATION_REQUEST_VERSION,
            "operation_request_scope": OPERATION_REQUEST_SCOPE,
            "result_level_non_claims_canonical_false": True,
        }
    )
    failed_checks = sum(not check["passed"] for check in checks)
    passed_checks = len(checks) - failed_checks

    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "descendant_body_creation_operation_request_metadata": {
            "operation_request_id": OPERATION_REQUEST_ID,
            "operation_request_type": OPERATION_REQUEST_TYPE,
            "operation_request_version": OPERATION_REQUEST_VERSION,
            "operation_request_scope": OPERATION_REQUEST_SCOPE,
            "persistent_operation_family": OPERATION_FAMILY,
            "persistent_operation_id": OPERATION_ID,
            "governing_executable_specification": (
                "spec/DESCENDANT_BODY_CREATION_OPERATION_REQUEST_V0_MIN_SPEC.md"
            ),
        },
        "request_question": REQUEST_QUESTION,
        "constitutional_event_binding": (
            deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY) if event_valid else None
        ),
        "persistent_operation_target": _event_projection(event_valid, "operation"),
        "current_precursor_boundary": _event_projection(event_valid, "current_boundary"),
        "current_lineage": (
            {
                "current_request": _event_projection(event_valid, "current_request"),
                "current_request_admission": _event_projection(
                    event_valid, "current_request_admission"
                ),
                "actual_consumption": _event_projection(event_valid, "actual_consumption"),
            }
            if event_valid
            else None
        ),
        "operation_contract": _event_projection(event_valid, "operation_contract"),
        "selected_source_complete_pair": _event_projection(
            event_valid, "selected_surface"
        ),
        "source_applicability": _event_projection(event_valid, "source_applicability"),
        "declared_use": _event_projection(event_valid, "declared_use"),
        "historical_and_freshness_posture": (
            {
                "freshness": _event_projection(event_valid, "freshness"),
                "historical_operation_evidence_only": _event_projection(
                    event_valid, "historical_operation"
                ),
            }
            if event_valid
            else None
        ),
        "ordinary_request_basis_review": {
            "complete": not missing_ordinary_paths and outcome not in (
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                OUTCOME_BLOCKED,
            ),
            "missing_paths": list(missing_ordinary_paths),
            "additional_basis_creates_no_retry_or_successor_permission": True,
        },
        "descendant_body_creation_operation_request": request_posture,
        "request_preservation_posture": {
            field: request_posture[field] for field in POSITIVE_REQUEST_FIELDS
        },
        "non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS["operation_request_local"]),
        "descendant_body_creation_operation_request_checks": checks,
        "passed_check_count": passed_checks,
        "failed_check_count": failed_checks,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requirement_code": (
                REQUIREMENT_CODE_ORDINARY_ABSENT
                if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
                else None
            ),
        },
        "what_remains_open": {
            "only_later_rank": LATER_OPEN_RANK,
            "later_rank_invoked": False,
            "operation_authorized": False,
            "operation_performed": False,
            "operation_occurrence_established": False,
            "descendant_body_created": False,
            "open_means_next": False,
        },
    }


def resolve_descendant_body_creation_operation_request_v0_min(
    envelope: Any,
) -> dict[str, Any]:
    """Resolve one supplied envelope without I/O, persistence, or upstream calls."""

    checks: list[dict[str, Any]] = []
    control_valid, control_checks, issue_path, block_code = _control_review(envelope)
    checks.extend(control_checks)
    if not control_valid:
        return _build_result(
            OUTCOME_BLOCKED, checks, block_code, issue_path, event_valid=False
        )

    event_valid, event_checks, event_issue = _validate_exact_mapping(
        envelope.get("constitutional_event_key"),
        EXPECTED_CONSTITUTIONAL_EVENT_KEY,
        "constitutional_event_key",
        "CONSTITUTIONAL_EVENT_KEY",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
    )
    checks.extend(event_checks)
    if not event_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            "CONSTITUTIONAL_EVENT_KEY_INVALID",
            event_issue,
            event_valid=False,
        )

    non_claims_valid, non_claim_checks, non_claim_issue = _validate_exact_mapping(
        envelope.get("required_non_claims"),
        EXPECTED_REQUIRED_NON_CLAIMS,
        "required_non_claims",
        "REQUIRED_NON_CLAIM",
        "REQUIRED_NON_CLAIM_INVALID",
    )
    checks.extend(non_claim_checks)
    if not non_claims_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            "REQUIRED_NON_CLAIM_INVALID",
            non_claim_issue,
            event_valid=True,
        )

    ordinary_state, ordinary_checks, missing_paths, ordinary_issue = _ordinary_review(
        envelope
    )
    checks.extend(ordinary_checks)
    if ordinary_state == "invalid":
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            "ORDINARY_REQUEST_BASIS_INVALID",
            ordinary_issue,
            event_valid=True,
        )
    if ordinary_state == "missing":
        return _build_result(
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            checks,
            None,
            ordinary_issue,
            event_valid=True,
            missing_ordinary_paths=missing_paths,
        )

    outcome = (
        OUTCOME_RECORDED
        if envelope["intent"] == INTENT_RECORD
        else OUTCOME_NOT_RECORDED
    )
    return _build_result(outcome, checks, None, None, event_valid=True)
