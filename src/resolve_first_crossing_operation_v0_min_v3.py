"""Pure current-line resolver for one FIRST_CROSSING_OPERATION event."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_first_crossing_operation_v0_min_v3"
RESULT_VERSION = "0.3.0"

OPERATION_ID = "first_crossing_operation_001"
OPERATION_TYPE = "FIRST_CROSSING_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
OPERATION_CONTRACT_REFERENCE = "spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md"
OPERATION_CONTRACT_SHA256 = (
    "047460dc058b8d6a8655d0fef03a422e2330fd832dd4b2045b45968517896549"
)
ADMISSIBLE_FUTURE_ROUTE = (
    "FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY"
)

CURRENT_BOUNDARY_RESULT_REFERENCE = (
    "artifacts/first_crossing_boundary_v0_min_v2/"
    "first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json"
)
CURRENT_BOUNDARY_RESULT_SHA256 = (
    "bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1"
)
CURRENT_BOUNDARY_RESULT_VERSION = "0.2.0"
CURRENT_BOUNDARY_RESOLVER_MODULE = "resolve_first_crossing_boundary_v0_min_v2"

BOUNDARY_ID = "first_crossing_boundary_001"
BOUNDARY_TYPE = "FIRST_CROSSING_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_FIRST_CROSSING_AFTER_DESCENDANT_BODY_CREATION_ONLY"
BOUNDARY_CONTRACT_REFERENCE = "spec/FIRST_CROSSING_BOUNDARY_V0_MIN_SPEC.md"
BOUNDARY_CONTRACT_SHA256 = (
    "87680155b33852d3b5bca2848df8b68a50c053878c5b49eeeb2fba61e3a007e2"
)
BOUNDARY_FUTURE_ROUTE = (
    "FIRST_CROSSING_BOUNDARY_THEN_FIRST_CROSSING_OPERATION_ONLY"
)

CREATION_OPERATION_ID = "descendant_body_creation_operation_001"
CREATION_OPERATION_REQUEST_ID = "descendant_body_creation_operation_request_001"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"
FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
FIRST_CROSSING_PAIR_SCOPE = "SEPARATE_FIRST_CROSSING_RECORDS_ONLY"

CANDIDATE_A_STANDING_SOURCE_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_A_STANDING_LABEL = "CANDIDATE_A_STANDING"
CANDIDATE_A_BASIS_ID = (
    "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
)
CANDIDATE_A_BASIS_LABEL = (
    "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
)
CANDIDATE_A_BASIS_SCOPE = "Motion-side admissible variation"

CANDIDATE_B_STANDING_SOURCE_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_B_STANDING_LABEL = "CANDIDATE_B_STANDING"
CANDIDATE_B_BASIS_ID = (
    "descendant_body_basis_candidate_b_001__"
    "regulation_side_admissibility_bounds_basis"
)
CANDIDATE_B_BASIS_LABEL = (
    "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
)
CANDIDATE_B_BASIS_SCOPE = "Regulation-side admissibility bounds"

INTENT_RECORD = "RECORD_FIRST_CROSSING_OPERATION"
OPERATION_QUESTION = (
    "Given the exact current FIRST_CROSSING_BOUNDARY result permitting separately "
    "bounded first-crossing operation consideration over pair-preserved "
    "descendant_body_a_001 and descendant_body_b_001, may mature "
    "FIRST_CROSSING_OPERATION evaluate both and, only when its ordinary support "
    "is true, authorize, perform, and record First Crossing A and First Crossing B "
    "without creating standing descendant, relation, currentness, authority, "
    "presence, identity, coupling, runtime, or downstream authorization?"
)

OUTCOME_BLOCKED = "FIRST_CROSSING_OPERATION_BLOCKED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = (
    "FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
)
OUTCOME_NOT_RECORDED = "FIRST_CROSSING_OPERATION_NOT_RECORDED"
OUTCOME_RECORDED = "FIRST_CROSSING_OPERATION_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_NOT_RECORDED,
    OUTCOME_RECORDED,
)

RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_REQUIRES_BOUNDARY_ALLOWANCE = "REQUIRES_BOUNDARY_ALLOWANCE"
RESULT_NOT_SUPPORTED = "FIRST_CROSSING_NOT_SUPPORTED"
RESULT_SUPPORTED = "FIRST_CROSSING_SUPPORTED"

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INPUT",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
        "ORDINARY_BOUNDARY_ALLOWANCE_INVALID",
    }
)

POSITIVE_OPERATION_BOOLEAN_FIELDS = tuple(
    """
    first_crossing_operation_recorded
    first_crossing_evaluation_performed
    first_crossing_result_recorded
    first_crossing_a_evaluated
    first_crossing_b_evaluated
    first_crossing_a_supported
    first_crossing_b_supported
    first_crossing_supported
    first_crossing_authorized
    crossing_authorized
    first_crossing_performed
    crossing_performed
    first_crossing_a_recorded
    first_crossing_b_recorded
    """.split()
)

SOURCE_BOUNDARY_NON_CLAIM_KEYS = tuple(
    """
    first_crossing_authorized
    crossing_authorized
    first_crossing_performed
    crossing_performed
    relation_created
    coupling_created
    presence_established
    identity_created
    follow_on_authorized
    """.split()
)

OPERATION_LOCAL_NON_CLAIM_KEYS = tuple(
    """
    relation_created
    field_machinery_created
    runtime_created
    api_created
    currentness_created
    authority_created
    standing_created
    output_authorized
    action_authorized
    derivative_reception_authorized
    synchronization_authorized
    coupling_assigned_to_descendant_body_a
    coupling_assigned_to_descendant_body_b
    coupling_assigned_to_candidate_a
    coupling_assigned_to_candidate_b
    coupling_created
    third_candidate_created
    third_model_admitted
    presence_established
    identity_created
    standing_descendant_created
    descendant_standing_check_performed
    follow_on_authorized
    follow_on_work_authorized
    prior_unsupported_candidate_a_claim_validated
    prior_unsupported_candidate_b_claim_validated
    prior_unsupported_derivation_event_claim_validated
    valid_derivation_event_recorded
    affected_file_repaired
    affected_file_edited
    affected_file_deleted
    affected_file_overwritten
    affected_file_replaced
    affected_file_redeemed
    affected_file_treated_as_clean_basis
    contaminated_lineage_treated_as_clean_basis
    first_crossing_boundary_overridden
    first_crossing_boundary_bypassed
    descendant_body_creation_operation_overridden
    descendant_body_creation_operation_bypassed
    scan_performed
    repository_scan_performed
    file_discovery_performed
    repair_performed
    validation_enforced
    hidden_repair_performed
    silent_overwrite_performed
    direct_first_crossing_operation_spec_to_first_crossing_operation_completion
    direct_boundary_allowance_to_first_crossing_without_operation
    direct_descendant_body_creation_to_first_crossing_without_boundary_and_operation
    direct_first_crossing_to_relation
    direct_first_crossing_to_runtime
    direct_first_crossing_to_authority_currentness
    direct_first_crossing_to_coupling_creation
    direct_first_crossing_to_third_candidate_route
    direct_first_crossing_to_third_model_route
    direct_first_crossing_to_presence
    direct_first_crossing_to_identity
    direct_first_crossing_to_standing_descendant
    direct_first_crossing_to_descendant_standing
    direct_first_crossing_to_output_action
    direct_first_crossing_to_follow_on_work
    """.split()
)

EXPECTED_CONSTITUTIONAL_EVENT_KEY = {
    "target": {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "operation_contract_reference": OPERATION_CONTRACT_REFERENCE,
        "operation_contract_sha256": OPERATION_CONTRACT_SHA256,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    },
    "current_boundary_result": {
        "result_reference": CURRENT_BOUNDARY_RESULT_REFERENCE,
        "result_sha256": CURRENT_BOUNDARY_RESULT_SHA256,
        "result_version": CURRENT_BOUNDARY_RESULT_VERSION,
        "resolver_module": CURRENT_BOUNDARY_RESOLVER_MODULE,
        "blocked": False,
        "block_code": None,
        "block_issue_path": None,
        "requires_descendant_body_creation": False,
    },
    "boundary": {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "boundary_contract_reference": BOUNDARY_CONTRACT_REFERENCE,
        "boundary_contract_sha256": BOUNDARY_CONTRACT_SHA256,
        "admissible_future_route": BOUNDARY_FUTURE_ROUTE,
    },
    "operation_event": {
        "persistent_operation_id": OPERATION_ID,
        "persistent_boundary_id": BOUNDARY_ID,
        "current_boundary_result_reference": CURRENT_BOUNDARY_RESULT_REFERENCE,
        "current_boundary_result_sha256": CURRENT_BOUNDARY_RESULT_SHA256,
        "persistent_creation_operation_id": CREATION_OPERATION_ID,
        "fresh_creation_operation_request_id": CREATION_OPERATION_REQUEST_ID,
        "descendant_body_a_id": DESCENDANT_BODY_A_ID,
        "descendant_body_b_id": DESCENDANT_BODY_B_ID,
        "same_identity_same_binding_is_deterministic_rerender": True,
        "resolver_call_count_is_event_count": False,
        "sibling_event_identity_allocated": False,
    },
    "creation_operation": {
        "operation_family": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_id": CREATION_OPERATION_ID,
        "operation_type": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_version": "0.1.0",
        "operation_scope": (
            "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
        ),
    },
    "creation_operation_event": {
        "fresh_operation_request_id": CREATION_OPERATION_REQUEST_ID,
        "persistent_operation_id": CREATION_OPERATION_ID,
        "operation_request_result_reference": (
            "artifacts/descendant_body_creation_operation_request_v0_min/"
            "descendant_body_creation_operation_request_001__"
            "descendant_body_creation_operation_request_v0_min_result.json"
        ),
        "operation_request_result_sha256": (
            "dd95b114773c8ff1b1f0a271530f282c2360b3aa58c07231886f111808d6e744"
        ),
        "same_identity_same_binding_is_deterministic_rerender": True,
        "resolver_call_count_is_event_count": False,
    },
    "descendant_body_a": {
        "descendant_body_id": DESCENDANT_BODY_A_ID,
        "candidate_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
        "candidate_role": CANDIDATE_A_ROLE,
        "candidate_standing_label": CANDIDATE_A_STANDING_LABEL,
        "candidate_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_basis_scope": CANDIDATE_A_BASIS_SCOPE,
    },
    "descendant_body_b": {
        "descendant_body_id": DESCENDANT_BODY_B_ID,
        "candidate_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
        "candidate_role": CANDIDATE_B_ROLE,
        "candidate_standing_label": CANDIDATE_B_STANDING_LABEL,
        "candidate_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_basis_label": CANDIDATE_B_BASIS_LABEL,
        "candidate_basis_scope": CANDIDATE_B_BASIS_SCOPE,
    },
    "pair": {
        "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
        "complete_pair_preserved": True,
        "descendant_bodies_remain_sibling": True,
        "descendant_body_non_hierarchy_preserved": True,
        "candidate_standing_non_hierarchy_preserved": True,
        "candidate_basis_non_hierarchy_preserved": True,
        "motion_does_not_erase_regulation": True,
        "regulation_not_sovereign_over_motion": True,
    },
    "source": {
        "selected_surface_identity": "descendant_body_candidate_standing_operation_001",
        "selected_surface_type": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "selected_surface_version": "0.1.0",
        "selected_surface_scope": (
            "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
        ),
        "selected_surface_family": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "selected_surface_semantic_owner": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
        ),
        "selected_surface_result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_"
            "descendant_body_candidate_standing_operation_v0_min/"
            "descendant_body_candidate_standing_operation_001__"
            "candidate_standing_operation_v0_min_result.json"
        ),
        "selected_surface_result_sha256": (
            "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961"
        ),
        "source_standing_contract_reference": (
            "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
        ),
        "source_standing_contract_sha256": (
            "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3"
        ),
        "source_standing_contract_version": "0.1.0",
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
            "ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_ONE_EXACT_"
            "DECLARED_DOWNSTREAM_USE_ONLY"
        ),
        "source_applicability_outcome": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED"
        ),
        "result_reference": (
            "artifacts/descendant_body_candidate_standing_effect_applicability_"
            "boundary_v0_min_v2/"
            "descendant_body_candidate_standing_effect_applicability_boundary_001__"
            "descendant_body_candidate_standing_effect_applicability_"
            "boundary_v0_min_v2_result.json"
        ),
        "source_route": (
            "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
        ),
        "source_declared_matter_use": (
            "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
        ),
        "complete_review_reached": True,
    },
    "freshness": {
        "fresh_operation_request_identity_declared": True,
        "operation_request_identity_distinct_from_operation_identity": True,
        "operation_request_identity_distinct_from_historical_occurrence": True,
        "historical_operation_result_is_current_permission": False,
        "historical_operation_result_is_current_source": False,
        "historical_operation_result_is_current_occurrence": False,
        "historical_operation_occurrence_reused": False,
        "historical_operation_material_reused": False,
        "historical_operation_result_replayed": False,
        "historical_success_treated_as_fresh_permission": False,
    },
    "historical_operation": {
        "historical_operation_id": OPERATION_ID,
        "result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_"
            "first_crossing_operation_v0_min_v2/first_crossing_operation_001__"
            "first_crossing_operation_v0_min_v2_result.json"
        ),
        "result_sha256": (
            "8b66349ff6d75670d91f4e9b202d0a4210dfb8d47065258a1103600d8dd99871"
        ),
        "outcome": OUTCOME_RECORDED,
        "first_crossing_result": RESULT_SUPPORTED,
        "result_is_current_permission": False,
        "result_is_current_source": False,
        "result_is_current_occurrence": False,
        "result_replayed": False,
        "success_treated_as_fresh_permission": False,
    },
    "non_claim_attribution": {
        "source_boundary": {"owner": BOUNDARY_TYPE},
        "source_creation_operation": {"owner": "DESCENDANT_BODY_CREATION_OPERATION"},
        "source_family": {"owner": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"},
        "target_local": {"owner": OPERATION_TYPE},
    },
}

EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE = {
    "source_outcome": "FIRST_CROSSING_BOUNDARY_ALLOWED",
    "source_boundary_result": "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",
    "first_crossing_operation_consideration_allowed": True,
    "descendant_body_creation_referenced": True,
    "descendant_body_a_referenced": True,
    "descendant_body_b_referenced": True,
    "descendant_body_created_referenced": True,
}

EXPECTED_REQUIRED_NON_CLAIMS = {
    "source_boundary": {key: False for key in SOURCE_BOUNDARY_NON_CLAIM_KEYS},
    "operation_local": {key: False for key in OPERATION_LOCAL_NON_CLAIM_KEYS},
}


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


CONTROL_PATHS = frozenset({"$::mapping_cardinality", "intent", "operation_question"})
CONSTITUTIONAL_EVENT_KEY_PATHS = frozenset(
    _leaf_paths(EXPECTED_CONSTITUTIONAL_EVENT_KEY, "constitutional_event_key")
)
ORDINARY_BOUNDARY_ALLOWANCE_PATHS = frozenset(
    f"ordinary_operation_basis.{key}"
    for key in EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE
)
ORDINARY_FIRST_CROSSING_BASIS_PATHS = frozenset(
    {"ordinary_operation_basis.first_crossing_support_found"}
)
SOURCE_BOUNDARY_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_boundary.{key}"
    for key in SOURCE_BOUNDARY_NON_CLAIM_KEYS
)
OPERATION_LOCAL_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.operation_local.{key}"
    for key in OPERATION_LOCAL_NON_CLAIM_KEYS
)
REQUIRED_NON_CLAIM_PATHS = (
    SOURCE_BOUNDARY_NON_CLAIM_PATHS | OPERATION_LOCAL_NON_CLAIM_PATHS
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_BOUNDARY_ALLOWANCE": ORDINARY_BOUNDARY_ALLOWANCE_PATHS,
    "ORDINARY_FIRST_CROSSING_BASIS": ORDINARY_FIRST_CROSSING_BASIS_PATHS,
    "REQUIRED_NON_CLAIM": REQUIRED_NON_CLAIM_PATHS,
}
ALL_REQUIRED_PATHS = frozenset().union(*CLASS_PATHS.values())
EXECUTABLE_ROOT_KEYS = frozenset(
    {
        "intent",
        "operation_question",
        "constitutional_event_key",
        "ordinary_operation_basis",
        "required_non_claims",
    }
)

assert len(CONTROL_PATHS) == 3
assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 114
assert len(ORDINARY_BOUNDARY_ALLOWANCE_PATHS) == 7
assert len(ORDINARY_FIRST_CROSSING_BASIS_PATHS) == 1
assert len(SOURCE_BOUNDARY_NON_CLAIM_PATHS) == 9
assert len(OPERATION_LOCAL_NON_CLAIM_PATHS) == 62
assert len(REQUIRED_NON_CLAIM_PATHS) == 71
assert len(ALL_REQUIRED_PATHS) == 196
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & _other_paths
        for _other_name, _other_paths in CLASS_PATHS.items()
        if _other_name != _class_name
    )
assert not (set(POSITIVE_OPERATION_BOOLEAN_FIELDS) & set(OPERATION_LOCAL_NON_CLAIM_KEYS))


def build_declared_first_crossing_operation_v0_min_v3_request() -> dict[str, Any]:
    """Return the exact canonical envelope without creating an event or artifact."""

    return {
        "intent": INTENT_RECORD,
        "operation_question": OPERATION_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_operation_basis": {
            **deepcopy(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE),
            "first_crossing_support_found": True,
        },
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


build_first_crossing_operation_v0_min_v3_request = (
    build_declared_first_crossing_operation_v0_min_v3_request
)


def _same_exact_value(actual: Any, expected: Any) -> bool:
    return type(actual) is type(expected) and actual == expected


def _check(
    check_id: str,
    classification: str,
    path: str,
    passed: bool,
    failure_code: str | None = None,
) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "classification": classification,
        "path": path,
        "passed": bool(passed),
        "failure_code": failure_code if not passed else None,
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
                f"{classification.lower()}_mapping_{prefix.replace('.', '_')}",
                classification,
                prefix,
                False,
                failure_code,
            )
        )
        return False, checks, prefix

    actual_keys = set(actual)
    expected_keys = set(expected)
    extras = sorted(actual_keys - expected_keys)
    missing = sorted(expected_keys - actual_keys)
    shape_valid = not extras and not missing
    checks.append(
        _check(
            f"{classification.lower()}_shape_{prefix.replace('.', '_')}",
            classification,
            prefix,
            shape_valid,
            failure_code,
        )
    )
    issue_path = (
        f"{prefix}.{extras[0]}"
        if extras
        else f"{prefix}.{missing[0]}"
        if missing
        else None
    )
    valid = shape_valid

    for key in sorted(actual_keys & expected_keys):
        path = f"{prefix}.{key}"
        actual_value = actual[key]
        expected_value = expected[key]
        if isinstance(expected_value, Mapping):
            child_valid, child_checks, child_issue = _validate_exact_mapping(
                actual_value,
                expected_value,
                path,
                classification,
                failure_code,
            )
            checks.extend(child_checks)
            valid = valid and child_valid
            if issue_path is None and child_issue is not None:
                issue_path = child_issue
            continue

        leaf_valid = _same_exact_value(actual_value, expected_value)
        checks.append(
            _check(
                f"{classification.lower()}_{path.replace('.', '_')}",
                classification,
                path,
                leaf_valid,
                failure_code,
            )
        )
        valid = valid and leaf_valid
        if issue_path is None and not leaf_valid:
            issue_path = path
    return valid, checks, issue_path


def _control_review(
    envelope: Any,
) -> tuple[bool, list[dict[str, Any]], str | None, str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(envelope, Mapping):
        checks.append(
            _check(
                "control_single_mapping",
                "CONTROL",
                "$::mapping_cardinality",
                False,
                "REQUEST_NOT_MAPPING",
            )
        )
        return False, checks, "$::mapping_cardinality", "REQUEST_NOT_MAPPING"

    root_keys = set(envelope)
    extras = sorted(root_keys - EXECUTABLE_ROOT_KEYS)
    missing = sorted(EXECUTABLE_ROOT_KEYS - root_keys)
    root_valid = not extras and not missing
    root_code = "UNSUPPORTED_INPUT" if extras else "CONTROL_INVALID"
    checks.append(
        _check(
            "control_root_mapping_cardinality",
            "CONTROL",
            "$::mapping_cardinality",
            root_valid,
            root_code,
        )
    )
    if not root_valid:
        issue = extras[0] if extras else missing[0]
        return False, checks, issue, root_code

    intent_valid = _same_exact_value(envelope["intent"], INTENT_RECORD)
    checks.append(
        _check(
            "control_intent_exact",
            "CONTROL",
            "intent",
            intent_valid,
            "CONTROL_INVALID",
        )
    )
    if not intent_valid:
        return False, checks, "intent", "CONTROL_INVALID"

    question_valid = _same_exact_value(
        envelope["operation_question"], OPERATION_QUESTION
    )
    checks.append(
        _check(
            "control_operation_question_exact",
            "CONTROL",
            "operation_question",
            question_valid,
            "CONTROL_INVALID",
        )
    )
    if not question_valid:
        return False, checks, "operation_question", "CONTROL_INVALID"
    return True, checks, None, None


def _ordinary_review(
    ordinary: Any,
) -> tuple[
    str,
    list[dict[str, Any]],
    tuple[str, ...],
    str | None,
]:
    checks: list[dict[str, Any]] = []
    prefix = "ordinary_operation_basis"
    expected_keys = set(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE) | {
        "first_crossing_support_found"
    }
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_operation_basis_mapping",
                "ORDINARY_BOUNDARY_ALLOWANCE",
                prefix,
                False,
                "ORDINARY_BOUNDARY_ALLOWANCE_INVALID",
            )
        )
        return "blocked", checks, (), prefix

    actual_keys = set(ordinary)
    extras = sorted(actual_keys - expected_keys)
    if extras:
        path = f"{prefix}.{extras[0]}"
        checks.append(
            _check(
                "ordinary_operation_basis_no_unsupported_fields",
                "ORDINARY_BOUNDARY_ALLOWANCE",
                path,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return "blocked", checks, (), path

    allowance_keys = set(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE)
    missing_keys = sorted(allowance_keys - actual_keys)
    missing_paths = tuple(f"{prefix}.{key}" for key in missing_keys)
    checks.append(
        _check(
            "ordinary_boundary_allowance_complete",
            "ORDINARY_BOUNDARY_ALLOWANCE",
            prefix,
            not missing_paths,
        )
    )

    issue_path: str | None = None
    contradictory = False
    for key in sorted(actual_keys & allowance_keys):
        path = f"{prefix}.{key}"
        exact = _same_exact_value(
            ordinary[key], EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE[key]
        )
        checks.append(
            _check(
                f"ordinary_boundary_allowance_{key}",
                "ORDINARY_BOUNDARY_ALLOWANCE",
                path,
                exact,
                "ORDINARY_BOUNDARY_ALLOWANCE_INVALID",
            )
        )
        contradictory = contradictory or not exact
        if issue_path is None and not exact:
            issue_path = path

    if contradictory:
        return "blocked", checks, missing_paths, issue_path
    if missing_paths:
        return "requires", checks, missing_paths, missing_paths[0]

    support_path = f"{prefix}.first_crossing_support_found"
    support_exact = (
        "first_crossing_support_found" in ordinary
        and _same_exact_value(ordinary["first_crossing_support_found"], True)
    )
    checks.append(
        _check(
            "ordinary_first_crossing_support_exact_true",
            "ORDINARY_FIRST_CROSSING_BASIS",
            support_path,
            support_exact,
            "FIRST_CROSSING_NOT_SUPPORTED",
        )
    )
    if not support_exact:
        return "not_recorded", checks, (), support_path
    return "recorded", checks, (), None


def _derive_pair_support(support: Any) -> tuple[bool, bool]:
    supported = _same_exact_value(support, True)
    return supported, supported


def _event_projection(event_valid: bool, key: str) -> Any:
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[key]) if event_valid else None


def _result_value(outcome: str) -> str:
    if outcome == OUTCOME_RECORDED:
        return RESULT_SUPPORTED
    if outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
        return RESULT_REQUIRES_BOUNDARY_ALLOWANCE
    if outcome == OUTCOME_NOT_RECORDED:
        return RESULT_NOT_SUPPORTED
    return RESULT_NOT_EVALUATED


def _operation_object(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "operation_contract_reference": OPERATION_CONTRACT_REFERENCE,
        "operation_contract_sha256": OPERATION_CONTRACT_SHA256,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "descendant_body_a_id": DESCENDANT_BODY_A_ID,
        "descendant_body_b_id": DESCENDANT_BODY_B_ID,
        "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
        "first_crossing_a_id": FIRST_CROSSING_A_ID,
        "first_crossing_b_id": FIRST_CROSSING_B_ID,
        "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
        "first_crossing_result": _result_value(outcome),
        **{field: False for field in POSITIVE_OPERATION_BOOLEAN_FIELDS},
        **{field: False for field in OPERATION_LOCAL_NON_CLAIM_KEYS},
    }
    if recorded:
        operation.update({field: True for field in POSITIVE_OPERATION_BOOLEAN_FIELDS})
    return operation


def _body_material(
    *,
    first_crossing_id: str,
    descendant_body_id: str,
    candidate_standing_source_id: str,
    candidate_role: str,
    candidate_standing_label: str,
    candidate_basis_id: str,
    candidate_basis_label: str,
    candidate_basis_scope: str,
) -> dict[str, Any]:
    return {
        "first_crossing_id": first_crossing_id,
        "descendant_body_id": descendant_body_id,
        "candidate_standing_source_id": candidate_standing_source_id,
        "candidate_role": candidate_role,
        "candidate_standing_label": candidate_standing_label,
        "candidate_basis_id": candidate_basis_id,
        "candidate_basis_label": candidate_basis_label,
        "candidate_basis_scope": candidate_basis_scope,
        "descendant_body_created": True,
        "descendant_body_is_first_crossing": False,
        "first_crossing_supported": True,
        "first_crossing_authorized": True,
        "crossing_authorized": True,
        "first_crossing_performed": True,
        "crossing_performed": True,
        "first_crossing_recorded": True,
        "relation_created": False,
        "coupling_created": False,
        "presence_established": False,
        "identity_created": False,
    }


def _operation_material(outcome: str) -> dict[str, Any] | None:
    if outcome != OUTCOME_RECORDED:
        return None
    return {
        "first_crossing_a_evaluation": _body_material(
            first_crossing_id=FIRST_CROSSING_A_ID,
            descendant_body_id=DESCENDANT_BODY_A_ID,
            candidate_standing_source_id=CANDIDATE_A_STANDING_SOURCE_ID,
            candidate_role=CANDIDATE_A_ROLE,
            candidate_standing_label=CANDIDATE_A_STANDING_LABEL,
            candidate_basis_id=CANDIDATE_A_BASIS_ID,
            candidate_basis_label=CANDIDATE_A_BASIS_LABEL,
            candidate_basis_scope=CANDIDATE_A_BASIS_SCOPE,
        ),
        "first_crossing_b_evaluation": _body_material(
            first_crossing_id=FIRST_CROSSING_B_ID,
            descendant_body_id=DESCENDANT_BODY_B_ID,
            candidate_standing_source_id=CANDIDATE_B_STANDING_SOURCE_ID,
            candidate_role=CANDIDATE_B_ROLE,
            candidate_standing_label=CANDIDATE_B_STANDING_LABEL,
            candidate_basis_id=CANDIDATE_B_BASIS_ID,
            candidate_basis_label=CANDIDATE_B_BASIS_LABEL,
            candidate_basis_scope=CANDIDATE_B_BASIS_SCOPE,
        ),
        "first_crossing_pair_evaluation": {
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "both_first_crossings_supported": True,
            "both_first_crossings_authorized": True,
            "both_first_crossings_performed": True,
            "both_first_crossings_recorded": True,
            "first_crossing_a_recorded": True,
            "first_crossing_b_recorded": True,
            "crossing_authorized": True,
            "crossing_performed": True,
            "descendant_bodies_remain_sibling": True,
            "descendant_body_non_hierarchy_preserved": True,
            "candidate_standing_non_hierarchy_preserved": True,
            "motion_does_not_erase_regulation": True,
            "regulation_not_sovereign_over_motion": True,
            "relation_created": False,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "presence_established": False,
            "identity_created": False,
            "standing_descendant_created": False,
            "descendant_standing_check_performed": False,
            "follow_on_authorized": False,
        },
    }


def _build_result(
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    event_valid: bool,
    block_code: str | None = None,
    issue_path: str | None = None,
    missing_allowance_paths: tuple[str, ...] = (),
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    requires = outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    operation = _operation_object(outcome)
    material = _operation_material(outcome)
    failed_check_count = sum(check["passed"] is False for check in checks)
    passed_check_count = len(checks) - failed_check_count

    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "operation_question": OPERATION_QUESTION,
        "current_operation_event": {
            "persistent_operation_id": OPERATION_ID,
            "persistent_boundary_id": BOUNDARY_ID,
            "current_boundary_result_reference": CURRENT_BOUNDARY_RESULT_REFERENCE,
            "current_boundary_result_sha256": CURRENT_BOUNDARY_RESULT_SHA256,
            "persistent_creation_operation_id": CREATION_OPERATION_ID,
            "fresh_creation_operation_request_id": CREATION_OPERATION_REQUEST_ID,
            "descendant_body_a_id": DESCENDANT_BODY_A_ID,
            "descendant_body_b_id": DESCENDANT_BODY_B_ID,
            "one_shared_operation_event": True,
            "separate_operation_occurrences_created": False,
            "same_identity_same_binding_is_deterministic_rerender": True,
            "resolver_call_count_is_event_count": False,
            "sibling_event_identity_allocated": False,
        },
        "current_boundary_result_binding": _event_projection(
            event_valid, "current_boundary_result"
        ),
        "persistent_operation_contract": _event_projection(event_valid, "target"),
        "persistent_boundary_identity": _event_projection(event_valid, "boundary"),
        "creation_operation": _event_projection(event_valid, "creation_operation"),
        "creation_operation_event": _event_projection(
            event_valid, "creation_operation_event"
        ),
        "descendant_body_subject": (
            {
                "descendant_body_a": _event_projection(
                    event_valid, "descendant_body_a"
                ),
                "descendant_body_b": _event_projection(
                    event_valid, "descendant_body_b"
                ),
                "pair": _event_projection(event_valid, "pair"),
                "one_shared_operation_event": True,
                "separate_operation_occurrences_created": False,
                "bodies_merged": False,
                "bodies_ranked": False,
                "coupling_created": False,
                "source_semantic_owner_transferred": False,
            }
            if event_valid
            else None
        ),
        "source_binding": _event_projection(event_valid, "source"),
        "source_applicability": _event_projection(event_valid, "source_applicability"),
        "freshness_and_history": (
            {
                "freshness": _event_projection(event_valid, "freshness"),
                "historical_operation": _event_projection(
                    event_valid, "historical_operation"
                ),
            }
            if event_valid
            else None
        ),
        "non_claim_attribution": _event_projection(
            event_valid, "non_claim_attribution"
        ),
        "ordinary_boundary_allowance_review": {
            "complete": recorded or not_recorded,
            "missing_paths": list(missing_allowance_paths),
            "issue_path": (
                issue_path
                if issue_path
                and issue_path in ORDINARY_BOUNDARY_ALLOWANCE_PATHS
                else None
            ),
            "requires_boundary_allowance_creates_retry_permission": False,
            "requires_boundary_allowance_creates_successor_permission": False,
        },
        "ordinary_first_crossing_support_review": {
            "support_found": recorded,
            "issue_path": (
                "ordinary_operation_basis.first_crossing_support_found"
                if not_recorded
                else None
            ),
            "not_recorded_creates_retry_permission": False,
            "not_recorded_creates_repair_permission": False,
            "not_recorded_creates_resubmission_permission": False,
            "not_recorded_creates_continuation_permission": False,
            "not_recorded_creates_successor_permission": False,
        },
        "first_crossing_operation": operation,
        "first_crossing_operation_material": material,
        "source_boundary_non_claims": {
            key: False for key in SOURCE_BOUNDARY_NON_CLAIM_KEYS
        },
        "operation_local_non_claims": {
            key: False for key in OPERATION_LOCAL_NON_CLAIM_KEYS
        },
        "first_crossing_operation_checks": checks,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requires_boundary_allowance": requires,
            "not_recorded": not_recorded,
        },
        "downstream_stopping_point": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "next_separately_bounded_rank": "RELATION_BOUNDARY",
            "relation_boundary_invoked": False,
            "relation_created": False,
            "standing_descendant_created": False,
            "standing_created": False,
            "descendant_standing_check_performed": False,
            "currentness_created": False,
            "authority_created": False,
            "presence_established": False,
            "identity_created": False,
            "coupling_created": False,
            "runtime_created": False,
            "api_created": False,
            "output_authorized": False,
            "action_authorized": False,
            "follow_on_work_authorized": False,
            "automatic_successor_created": False,
        },
    }


def resolve_first_crossing_operation_v0_min_v3(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Resolve one exact current operation event without I/O or persistence."""

    checks: list[dict[str, Any]] = []
    control_valid, control_checks, issue_path, block_code = _control_review(
        supplied_envelope
    )
    checks.extend(control_checks)
    if not control_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=False,
            block_code=block_code,
            issue_path=issue_path,
        )

    event_valid, event_checks, event_issue = _validate_exact_mapping(
        supplied_envelope["constitutional_event_key"],
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
            event_valid=False,
            block_code="CONSTITUTIONAL_EVENT_KEY_INVALID",
            issue_path=event_issue,
        )

    non_claims_valid, non_claim_checks, non_claim_issue = _validate_exact_mapping(
        supplied_envelope["required_non_claims"],
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
            event_valid=True,
            block_code="REQUIRED_NON_CLAIM_INVALID",
            issue_path=non_claim_issue,
        )

    ordinary_state, ordinary_checks, missing_paths, ordinary_issue = _ordinary_review(
        supplied_envelope["ordinary_operation_basis"]
    )
    checks.extend(ordinary_checks)
    if ordinary_state == "blocked":
        code = (
            "UNSUPPORTED_INPUT"
            if ordinary_issue
            and ordinary_issue.rsplit(".", 1)[-1]
            not in (
                set(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE)
                | {"first_crossing_support_found"}
            )
            else "ORDINARY_BOUNDARY_ALLOWANCE_INVALID"
        )
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code=code,
            issue_path=ordinary_issue,
            missing_allowance_paths=missing_paths,
        )
    if ordinary_state == "requires":
        return _build_result(
            OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            checks,
            event_valid=True,
            missing_allowance_paths=missing_paths,
        )
    if ordinary_state == "not_recorded":
        return _build_result(
            OUTCOME_NOT_RECORDED,
            checks,
            event_valid=True,
        )

    support_a, support_b = _derive_pair_support(
        supplied_envelope["ordinary_operation_basis"]["first_crossing_support_found"]
    )
    if support_a is not support_b:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code="ORDINARY_BOUNDARY_ALLOWANCE_INVALID",
            issue_path="ordinary_operation_basis.first_crossing_support_found",
        )
    return _build_result(OUTCOME_RECORDED, checks, event_valid=True)
