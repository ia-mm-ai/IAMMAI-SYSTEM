"""Pure current-line resolver for one FIRST_CROSSING_BOUNDARY event."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_first_crossing_boundary_v0_min_v2"
RESULT_VERSION = "0.2.0"

BOUNDARY_ID = "first_crossing_boundary_001"
BOUNDARY_TYPE = "FIRST_CROSSING_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_FIRST_CROSSING_AFTER_DESCENDANT_BODY_CREATION_ONLY"
BOUNDARY_CONTRACT_REFERENCE = "spec/FIRST_CROSSING_BOUNDARY_V0_MIN_SPEC.md"
BOUNDARY_CONTRACT_SHA256 = (
    "87680155b33852d3b5bca2848df8b68a50c053878c5b49eeeb2fba61e3a007e2"
)
ADMISSIBLE_FUTURE_ROUTE = (
    "FIRST_CROSSING_BOUNDARY_THEN_FIRST_CROSSING_OPERATION_ONLY"
)

CURRENT_SOURCE_RESULT_REFERENCE = (
    "artifacts/descendant_body_creation_operation_v0_min_v2/"
    "descendant_body_creation_operation_001__"
    "descendant_body_creation_operation_v0_min_v2_result.json"
)
CURRENT_SOURCE_RESULT_SHA256 = (
    "4adc2e5b6557a29cb37fe682e4fef8af2832ed88625622e3ec5a986a93e27767"
)
CURRENT_SOURCE_RESULT_VERSION = "0.2.0"
CURRENT_SOURCE_RESOLVER_MODULE = (
    "resolve_descendant_body_creation_operation_v0_min_v2"
)

CREATION_OPERATION_ID = "descendant_body_creation_operation_001"
CREATION_OPERATION_REQUEST_ID = "descendant_body_creation_operation_request_001"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"

INTENT_RECORD = "RECORD_FIRST_CROSSING_BOUNDARY"
BOUNDARY_QUESTION = (
    "Given the exact current DESCENDANT_BODY_CREATION_OPERATION occurrence that "
    "created descendant_body_a_001 and descendant_body_b_001 as separate sibling "
    "descendant-body records, may the mature FIRST_CROSSING_BOUNDARY record that a "
    "separately bounded first-crossing operation may be considered, without "
    "converting creation into crossing, standing, relation, currentness, authority, "
    "presence, identity, coupling, or runtime?"
)

OUTCOME_BLOCKED = "FIRST_CROSSING_BOUNDARY_BLOCKED"
OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION = (
    "FIRST_CROSSING_BOUNDARY_REQUIRES_DESCENDANT_BODY_CREATION"
)
OUTCOME_ALLOWED = "FIRST_CROSSING_BOUNDARY_ALLOWED"
OUTCOME_FAMILY = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
    OUTCOME_ALLOWED,
)

BOUNDARY_RESULT_ALLOWED = "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"
BOUNDARY_RESULT_REQUIRES = "REQUIRES_DESCENDANT_BODY_CREATION"
BOUNDARY_RESULT_NOT_EVALUATED = "NOT_EVALUATED"

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INPUT",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
        "ORDINARY_DESCENDANT_BODY_CREATION_BASIS_INVALID",
    }
)

POSITIVE_BOUNDARY_BOOLEAN_FIELDS = (
    "first_crossing_boundary_recorded",
    "first_crossing_boundary_result_recorded",
    "first_crossing_operation_consideration_allowed",
    "descendant_body_creation_referenced",
    "descendant_body_a_referenced",
    "descendant_body_b_referenced",
    "descendant_body_created_referenced",
)

SOURCE_OPERATION_NON_CLAIM_KEYS = tuple(
    """
    standing_descendant_created
    descendant_standing_check_performed
    crossing_authorized
    first_crossing_authorized
    relation_created
    coupling_created
    presence_established
    identity_created
    follow_on_authorized
    automatic_successor_created
    """.split()
)

TARGET_LOCAL_NON_CLAIM_KEYS = tuple(
    """
    first_crossing_authorized
    crossing_authorized
    first_crossing_performed
    crossing_performed
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
    descendant_body_creation_operation_overridden
    descendant_body_creation_operation_bypassed
    scan_performed
    repository_scan_performed
    file_discovery_performed
    repair_performed
    validation_enforced
    hidden_repair_performed
    silent_overwrite_performed
    direct_first_crossing_boundary_to_first_crossing_operation_completion
    direct_descendant_body_creation_to_first_crossing_without_boundary_and_operation
    direct_descendant_body_to_first_crossing_without_boundary_and_operation
    direct_first_crossing_boundary_to_crossing_authorization
    direct_first_crossing_boundary_to_crossing
    direct_first_crossing_boundary_to_relation
    direct_first_crossing_boundary_to_runtime
    direct_first_crossing_boundary_to_authority_currentness
    direct_first_crossing_boundary_to_coupling_creation
    direct_first_crossing_boundary_to_third_candidate_route
    direct_first_crossing_boundary_to_third_model_route
    direct_first_crossing_boundary_to_presence
    direct_first_crossing_boundary_to_identity
    direct_first_crossing_boundary_to_standing_descendant
    direct_first_crossing_boundary_to_descendant_standing
    direct_first_crossing_boundary_to_output_action
    direct_first_crossing_boundary_to_follow_on_work
    """.split()
)

EXPECTED_CONSTITUTIONAL_EVENT_KEY = {
    "target": {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "boundary_contract_reference": BOUNDARY_CONTRACT_REFERENCE,
        "boundary_contract_sha256": BOUNDARY_CONTRACT_SHA256,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    },
    "current_creation_result": {
        "result_reference": CURRENT_SOURCE_RESULT_REFERENCE,
        "result_sha256": CURRENT_SOURCE_RESULT_SHA256,
        "result_version": CURRENT_SOURCE_RESULT_VERSION,
        "resolver_module": CURRENT_SOURCE_RESOLVER_MODULE,
        "blocked": False,
        "block_code": None,
        "block_issue_path": None,
        "requires_boundary_allowance": False,
    },
    "operation": {
        "operation_family": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_id": CREATION_OPERATION_ID,
        "operation_type": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_version": "0.1.0",
        "operation_scope": (
            "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
        ),
    },
    "operation_event": {
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
    "operation_contract": {
        "operation_contract_family": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_contract_operation_id": CREATION_OPERATION_ID,
        "operation_contract_type": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_contract_version": "0.1.0",
        "operation_contract_scope": (
            "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
        ),
        "operation_contract_reference": (
            "spec/DESCENDANT_BODY_CREATION_OPERATION_V0_MIN_SPEC.md"
        ),
        "operation_contract_sha256": (
            "82cf281c103c53742dc963435df1a0efdb62037f591db926f9ea7a63dc33f6f4"
        ),
        "operation_contract_future_route": (
            "DESCENDANT_BODY_CREATION_OPERATION_THEN_FIRST_CROSSING_BOUNDARY_ONLY"
        ),
    },
    "descendant_body_a": {
        "descendant_body_id": DESCENDANT_BODY_A_ID,
        "candidate_standing_source_id": "descendant_body_basis_candidate_a_001",
        "candidate_role": "CANDIDATE_A",
        "candidate_standing_label": "CANDIDATE_A_STANDING",
        "candidate_basis_id": (
            "descendant_body_basis_candidate_a_001__"
            "motion_side_admissible_variation_basis"
        ),
        "candidate_basis_label": (
            "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
        ),
        "candidate_basis_scope": "Motion-side admissible variation",
    },
    "descendant_body_b": {
        "descendant_body_id": DESCENDANT_BODY_B_ID,
        "candidate_standing_source_id": "descendant_body_basis_candidate_b_001",
        "candidate_role": "CANDIDATE_B",
        "candidate_standing_label": "CANDIDATE_B_STANDING",
        "candidate_basis_id": (
            "descendant_body_basis_candidate_b_001__"
            "regulation_side_admissibility_bounds_basis"
        ),
        "candidate_basis_label": (
            "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
        ),
        "candidate_basis_scope": "Regulation-side admissibility bounds",
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
        "historical_operation_result_is_current_request": False,
        "historical_operation_result_is_current_occurrence": False,
        "historical_operation_occurrence_reused": False,
        "historical_operation_material_reused": False,
        "historical_operation_result_replayed": False,
        "historical_success_treated_as_fresh_permission": False,
    },
    "historical_first_crossing": {
        "result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_"
            "first_crossing_boundary_v0_min/first_crossing_boundary_001__"
            "first_crossing_boundary_v0_min_result.json"
        ),
        "result_sha256": (
            "cf9c7fe38465ea6d6e27ac7728004f5bf73851352f333c56284debf8b89d93f6"
        ),
        "outcome": OUTCOME_ALLOWED,
        "boundary_result": BOUNDARY_RESULT_ALLOWED,
        "result_is_current_permission": False,
        "result_is_current_source": False,
        "result_is_current_event": False,
        "result_replayed": False,
        "success_treated_as_fresh_permission": False,
    },
    "non_claim_attribution": {
        "source_operation": {"owner": "DESCENDANT_BODY_CREATION_OPERATION"},
        "source_family": {
            "owner": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
        },
        "target_local": {"owner": BOUNDARY_TYPE},
    },
}

EXPECTED_ORDINARY_DESCENDANT_BODY_CREATION_BASIS = {
    "source_outcome": "DESCENDANT_BODY_CREATION_OPERATION_CREATED",
    "source_operation_result": "DESCENDANT_BODY_CREATION_SUPPORTED",
    "descendant_body_creation_supported": True,
    "descendant_body_creation_authorized": True,
    "descendant_body_creation_performed": True,
    "descendant_body_a_created": True,
    "descendant_body_b_created": True,
    "descendant_body_created": True,
}

EXPECTED_REQUIRED_NON_CLAIMS = {
    "source_operation": {key: False for key in SOURCE_OPERATION_NON_CLAIM_KEYS},
    "target_local": {key: False for key in TARGET_LOCAL_NON_CLAIM_KEYS},
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


CONTROL_PATHS = frozenset({"$::mapping_cardinality", "intent", "boundary_question"})
CONSTITUTIONAL_EVENT_KEY_PATHS = frozenset(
    _leaf_paths(EXPECTED_CONSTITUTIONAL_EVENT_KEY, "constitutional_event_key")
)
ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS = frozenset(
    f"ordinary_descendant_body_creation_basis.{key}"
    for key in EXPECTED_ORDINARY_DESCENDANT_BODY_CREATION_BASIS
)
SOURCE_OPERATION_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_operation.{key}"
    for key in SOURCE_OPERATION_NON_CLAIM_KEYS
)
TARGET_LOCAL_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.target_local.{key}"
    for key in TARGET_LOCAL_NON_CLAIM_KEYS
)
REQUIRED_NON_CLAIM_PATHS = (
    SOURCE_OPERATION_NON_CLAIM_PATHS | TARGET_LOCAL_NON_CLAIM_PATHS
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_DESCENDANT_BODY_CREATION_BASIS": (
        ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS
    ),
    "REQUIRED_NON_CLAIM": REQUIRED_NON_CLAIM_PATHS,
}
ALL_REQUIRED_PATHS = frozenset().union(*CLASS_PATHS.values())
EXECUTABLE_ROOT_KEYS = frozenset(
    {
        "intent",
        "boundary_question",
        "constitutional_event_key",
        "ordinary_descendant_body_creation_basis",
        "required_non_claims",
    }
)

assert len(CONTROL_PATHS) == 3
assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 102
assert len(ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS) == 8
assert len(SOURCE_OPERATION_NON_CLAIM_PATHS) == 10
assert len(TARGET_LOCAL_NON_CLAIM_PATHS) == 66
assert len(REQUIRED_NON_CLAIM_PATHS) == 76
assert len(ALL_REQUIRED_PATHS) == 189
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & _other_paths
        for _other_name, _other_paths in CLASS_PATHS.items()
        if _other_name != _class_name
    )


def build_declared_first_crossing_boundary_v0_min_v2_request() -> dict[str, Any]:
    """Return the exact in-memory envelope without creating an event or artifact."""

    return {
        "intent": INTENT_RECORD,
        "boundary_question": BOUNDARY_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_descendant_body_creation_basis": deepcopy(
            EXPECTED_ORDINARY_DESCENDANT_BODY_CREATION_BASIS
        ),
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


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
        envelope["boundary_question"], BOUNDARY_QUESTION
    )
    checks.append(
        _check(
            "control_boundary_question_exact",
            "CONTROL",
            "boundary_question",
            question_valid,
            "CONTROL_INVALID",
        )
    )
    if not question_valid:
        return False, checks, "boundary_question", "CONTROL_INVALID"
    return True, checks, None, None


def _ordinary_review(
    ordinary: Any,
) -> tuple[str, list[dict[str, Any]], tuple[str, ...], str | None]:
    checks: list[dict[str, Any]] = []
    prefix = "ordinary_descendant_body_creation_basis"
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_basis_mapping",
                "ORDINARY_DESCENDANT_BODY_CREATION_BASIS",
                prefix,
                False,
                "ORDINARY_DESCENDANT_BODY_CREATION_BASIS_INVALID",
            )
        )
        return "blocked", checks, (), prefix

    actual_keys = set(ordinary)
    expected_keys = set(EXPECTED_ORDINARY_DESCENDANT_BODY_CREATION_BASIS)
    extras = sorted(actual_keys - expected_keys)
    missing_keys = sorted(expected_keys - actual_keys)
    if extras:
        path = f"{prefix}.{extras[0]}"
        checks.append(
            _check(
                "ordinary_basis_no_unsupported_fields",
                "ORDINARY_DESCENDANT_BODY_CREATION_BASIS",
                path,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return "blocked", checks, (), path

    missing_paths = tuple(f"{prefix}.{key}" for key in missing_keys)
    checks.append(
        _check(
            "ordinary_basis_complete",
            "ORDINARY_DESCENDANT_BODY_CREATION_BASIS",
            prefix,
            not missing_paths,
        )
    )

    issue_path: str | None = None
    contradictory = False
    for key in sorted(actual_keys & expected_keys):
        path = f"{prefix}.{key}"
        exact = _same_exact_value(
            ordinary[key], EXPECTED_ORDINARY_DESCENDANT_BODY_CREATION_BASIS[key]
        )
        checks.append(
            _check(
                f"ordinary_basis_{key}",
                "ORDINARY_DESCENDANT_BODY_CREATION_BASIS",
                path,
                exact,
                "ORDINARY_DESCENDANT_BODY_CREATION_BASIS_INVALID",
            )
        )
        contradictory = contradictory or not exact
        if issue_path is None and not exact:
            issue_path = path

    if contradictory:
        return "blocked", checks, missing_paths, issue_path
    if missing_paths:
        return "requires", checks, missing_paths, missing_paths[0]
    return "allowed", checks, (), None


def _event_projection(event_valid: bool, key: str) -> Any:
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[key]) if event_valid else None


def _build_result(
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    event_valid: bool,
    block_code: str | None = None,
    issue_path: str | None = None,
    missing_ordinary_paths: tuple[str, ...] = (),
) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    requires = outcome == OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION
    boundary = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "first_crossing_boundary_result": (
            BOUNDARY_RESULT_ALLOWED
            if allowed
            else BOUNDARY_RESULT_REQUIRES
            if requires
            else BOUNDARY_RESULT_NOT_EVALUATED
        ),
        **{field: allowed for field in POSITIVE_BOUNDARY_BOOLEAN_FIELDS},
        **{field: False for field in TARGET_LOCAL_NON_CLAIM_KEYS},
    }
    failed_check_count = sum(check["passed"] is False for check in checks)
    passed_check_count = len(checks) - failed_check_count

    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "boundary_question": BOUNDARY_QUESTION,
        "current_boundary_event": {
            "persistent_boundary_id": BOUNDARY_ID,
            "persistent_creation_operation_id": CREATION_OPERATION_ID,
            "fresh_operation_request_id": CREATION_OPERATION_REQUEST_ID,
            "source_result_reference": CURRENT_SOURCE_RESULT_REFERENCE,
            "source_result_sha256": CURRENT_SOURCE_RESULT_SHA256,
            "descendant_body_a_id": DESCENDANT_BODY_A_ID,
            "descendant_body_b_id": DESCENDANT_BODY_B_ID,
            "same_identity_same_binding_is_deterministic_rerender": True,
            "resolver_call_count_is_event_count": False,
            "sibling_event_identity_allocated": False,
        },
        "current_creation_result_binding": _event_projection(
            event_valid, "current_creation_result"
        ),
        "persistent_boundary_contract": _event_projection(event_valid, "target"),
        "persistent_creation_operation": _event_projection(event_valid, "operation"),
        "fresh_operation_request": _event_projection(event_valid, "operation_event"),
        "operation_contract": _event_projection(event_valid, "operation_contract"),
        "descendant_body_subject": (
            {
                "descendant_body_a": _event_projection(
                    event_valid, "descendant_body_a"
                ),
                "descendant_body_b": _event_projection(
                    event_valid, "descendant_body_b"
                ),
                "pair": _event_projection(event_valid, "pair"),
                "one_pair_preserved_boundary_condition": event_valid,
                "bodies_merged": False,
                "per_body_boundary_decisions_created": False,
                "bodies_ranked": False,
                "coupling_created": False,
            }
            if event_valid
            else None
        ),
        "source_binding": (
            {
                "source": _event_projection(event_valid, "source"),
                "source_applicability": _event_projection(
                    event_valid, "source_applicability"
                ),
            }
            if event_valid
            else None
        ),
        "freshness_and_history": (
            {
                "freshness": _event_projection(event_valid, "freshness"),
                "historical_first_crossing": _event_projection(
                    event_valid, "historical_first_crossing"
                ),
            }
            if event_valid
            else None
        ),
        "non_claim_attribution": _event_projection(
            event_valid, "non_claim_attribution"
        ),
        "ordinary_descendant_body_creation_basis_review": {
            "complete": allowed,
            "missing_paths": list(missing_ordinary_paths),
            "issue_path": (
                issue_path
                if issue_path
                and issue_path.startswith("ordinary_descendant_body_creation_basis")
                else None
            ),
            "requires_descendant_body_creation_creates_retry_permission": False,
            "requires_descendant_body_creation_creates_successor_permission": False,
        },
        "first_crossing_boundary": boundary,
        "source_operation_non_claims": {
            key: False for key in SOURCE_OPERATION_NON_CLAIM_KEYS
        },
        "target_local_non_claims": {
            key: False for key in TARGET_LOCAL_NON_CLAIM_KEYS
        },
        "first_crossing_boundary_checks": checks,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requires_descendant_body_creation": requires,
        },
        "downstream_stopping_point": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "next_separately_bounded_rank": "FIRST_CROSSING_OPERATION",
            "first_crossing_operation_invoked": False,
            "first_crossing_operation_authorized": False,
            "first_crossing_operation_performed": False,
            "relation_boundary_invoked": False,
            "standing_descendant_created": False,
            "standing_created": False,
            "relation_created": False,
            "currentness_created": False,
            "authority_created": False,
            "presence_established": False,
            "identity_created": False,
            "coupling_created": False,
            "runtime_created": False,
            "api_created": False,
            "output_authorized": False,
            "action_authorized": False,
            "automatic_successor_created": False,
        },
    }


def resolve_first_crossing_boundary_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Resolve one exact current boundary event without I/O or persistence."""

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
        supplied_envelope["ordinary_descendant_body_creation_basis"]
    )
    checks.extend(ordinary_checks)
    if ordinary_state == "blocked":
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code=(
                "UNSUPPORTED_INPUT"
                if ordinary_issue
                and ordinary_issue.rsplit(".", 1)[-1]
                not in EXPECTED_ORDINARY_DESCENDANT_BODY_CREATION_BASIS
                else "ORDINARY_DESCENDANT_BODY_CREATION_BASIS_INVALID"
            ),
            issue_path=ordinary_issue,
            missing_ordinary_paths=missing_paths,
        )
    if ordinary_state == "requires":
        return _build_result(
            OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
            checks,
            event_valid=True,
            missing_ordinary_paths=missing_paths,
        )
    return _build_result(OUTCOME_ALLOWED, checks, event_valid=True)
