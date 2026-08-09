"""Pure current-line resolver for one bounded RELATION_OPERATION event."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_relation_operation_v0_min_v3"
RESULT_VERSION = "0.3.0"

OPERATION_ID = "relation_operation_001"
OPERATION_TYPE = "RELATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_RELATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
OPERATION_CONTRACT_REFERENCE = "spec/RELATION_OPERATION_V0_MIN_SPEC.md"
OPERATION_CONTRACT_SHA256 = (
    "75afd2d64b22654c1132c0c44901ad7375723d2a64e476feb59b8e561ea6d8f4"
)
ADMISSIBLE_FUTURE_ROUTE = (
    "RELATION_OPERATION_THEN_RELATION_REVERSIBILITY_BOUNDARY_ONLY"
)

RELATION_ID = "relation_001"
RELATION_PAIR_SCOPE = "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
RELATION_OBJECT_CARDINALITY = 1
FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
FIRST_CROSSING_PAIR_SCOPE = "SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"
TOPOLOGY = "PAIR_SCOPED_NON_DIRECTIONAL"

CURRENT_BOUNDARY_RESULT_REFERENCE = (
    "artifacts/relation_boundary_v0_min_v2/"
    "relation_boundary_001__relation_boundary_v0_min_v2_result.json"
)
CURRENT_BOUNDARY_RESULT_SHA256 = (
    "7a33a06296bcded16bec1d7d408395039072d3754fc194f87c16355b7e3df77e"
)

INTENT_RECORD = "RECORD_RELATION_OPERATION"
OPERATION_QUESTION = (
    "Given the exact current RELATION_BOUNDARY result permitting separately "
    "bounded RELATION_OPERATION consideration over the exact pair-preserved "
    "first_crossing_a_001 / first_crossing_b_001 subject and persistent relation "
    "identity relation_001, may mature RELATION_OPERATION evaluate the relation "
    "basis and, only if supported, authorize, perform, create, and record one "
    "relation occurrence without creating coupling, standing, currentness, "
    "authority, presence, identity, runtime, or downstream authorization?"
)

OUTCOME_BLOCKED = "RELATION_OPERATION_BLOCKED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = (
    "RELATION_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
)
OUTCOME_NOT_RECORDED = "RELATION_OPERATION_NOT_RECORDED"
OUTCOME_RECORDED = "RELATION_OPERATION_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_NOT_RECORDED,
    OUTCOME_RECORDED,
)

RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_REQUIRES_BOUNDARY_ALLOWANCE = "REQUIRES_BOUNDARY_ALLOWANCE"
RESULT_NOT_SUPPORTED = "RELATION_NOT_SUPPORTED"
RESULT_SUPPORTED = "RELATION_SUPPORTED"

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
    relation_operation_recorded
    relation_evaluation_performed
    relation_result_recorded
    relation_supported
    relation_authorized
    relation_created
    relation_operation_performed
    relation_recorded
    first_crossing_a_used_as_relation_basis
    first_crossing_b_used_as_relation_basis
    first_crossing_pair_used_as_relation_basis
    """.split()
)

SOURCE_BOUNDARY_NON_CLAIM_KEYS = tuple(
    """
    relation_authorized
    relation_created
    relation_operation_performed
    coupling_created
    presence_established
    identity_created
    follow_on_authorized
    follow_on_work_authorized
    """.split()
)

OPERATION_LOCAL_NON_CLAIM_KEYS = tuple(
    """
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
    coupling_assigned_to_relation
    coupling_assigned_to_first_crossing_a
    coupling_assigned_to_first_crossing_b
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
    relation_boundary_overridden
    relation_boundary_bypassed
    first_crossing_operation_v1_repaired
    first_crossing_operation_v1_overwritten
    first_crossing_operation_v1_converted_to_standing
    first_crossing_operation_v2_overridden
    first_crossing_operation_v2_bypassed
    scan_performed
    repository_scan_performed
    file_discovery_performed
    repair_performed
    validation_enforced
    hidden_repair_performed
    silent_overwrite_performed
    direct_relation_operation_spec_to_relation_operation_completion
    direct_relation_boundary_allowance_to_relation_without_operation
    direct_first_crossing_to_relation_without_relation_boundary_and_operation
    direct_relation_to_field_machinery
    direct_relation_to_runtime
    direct_relation_to_authority_currentness
    direct_relation_to_coupling_assignment
    direct_relation_to_coupling_creation
    direct_relation_to_third_candidate_route
    direct_relation_to_third_model_route
    direct_relation_to_presence
    direct_relation_to_identity
    direct_relation_to_standing_descendant
    direct_relation_to_descendant_standing
    direct_relation_to_output_action
    direct_relation_to_follow_on_work
    """.split()
)

EXPECTED_CONSTITUTIONAL_EVENT_KEY: dict[str, Any] = {
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
        "result_version": "0.2.0",
        "resolver_module": "resolve_relation_boundary_v0_min_v2",
        "blocked": False,
        "block_code": None,
        "block_issue_path": None,
        "requires_first_crossing": False,
    },
    "boundary": {
        "boundary_id": "relation_boundary_001",
        "boundary_type": "RELATION_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": "CONSIDER_RELATION_AFTER_FIRST_CROSSING_ONLY",
        "boundary_contract_reference": "spec/RELATION_BOUNDARY_V0_MIN_SPEC.md",
        "boundary_contract_sha256": (
            "6c1d05b022cd48e83d404d2df86aa5aeeddff50e82d5b7d17f79a6402bd3ed6d"
        ),
        "admissible_future_route": "RELATION_BOUNDARY_THEN_RELATION_OPERATION_ONLY",
    },
    "operation_event": {
        "persistent_operation_id": OPERATION_ID,
        "persistent_boundary_id": "relation_boundary_001",
        "current_boundary_result_reference": CURRENT_BOUNDARY_RESULT_REFERENCE,
        "current_boundary_result_sha256": CURRENT_BOUNDARY_RESULT_SHA256,
        "relation_id": RELATION_ID,
        "first_crossing_a_id": FIRST_CROSSING_A_ID,
        "first_crossing_b_id": FIRST_CROSSING_B_ID,
        "descendant_body_a_id": DESCENDANT_BODY_A_ID,
        "descendant_body_b_id": DESCENDANT_BODY_B_ID,
        "persistent_creation_operation_id": "descendant_body_creation_operation_001",
        "fresh_creation_operation_request_id": (
            "descendant_body_creation_operation_request_001"
        ),
        "same_identity_same_binding_is_deterministic_rerender": True,
        "resolver_call_count_is_event_count": False,
        "sibling_event_identity_allocated": False,
    },
    "crossing_operation": {
        "operation_id": "first_crossing_operation_001",
        "operation_type": "FIRST_CROSSING_OPERATION",
        "operation_version": "0.1.0",
        "operation_scope": "EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY",
        "operation_contract_reference": "spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md",
        "operation_contract_sha256": (
            "047460dc058b8d6a8655d0fef03a422e2330fd832dd4b2045b45968517896549"
        ),
        "admissible_future_route": (
            "FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY"
        ),
    },
    "crossing_operation_event": {
        "persistent_operation_id": "first_crossing_operation_001",
        "persistent_boundary_id": "first_crossing_boundary_001",
        "current_boundary_result_reference": (
            "artifacts/first_crossing_boundary_v0_min_v2/"
            "first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json"
        ),
        "current_boundary_result_sha256": (
            "bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1"
        ),
        "persistent_creation_operation_id": "descendant_body_creation_operation_001",
        "fresh_creation_operation_request_id": (
            "descendant_body_creation_operation_request_001"
        ),
        "descendant_body_a_id": DESCENDANT_BODY_A_ID,
        "descendant_body_b_id": DESCENDANT_BODY_B_ID,
        "one_shared_operation_event": True,
        "separate_operation_occurrences_created": False,
        "same_identity_same_binding_is_deterministic_rerender": True,
        "resolver_call_count_is_event_count": False,
        "sibling_event_identity_allocated": False,
    },
    "creation_operation": {
        "operation_family": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_id": "descendant_body_creation_operation_001",
        "operation_type": "DESCENDANT_BODY_CREATION_OPERATION",
        "operation_version": "0.1.0",
        "operation_scope": (
            "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
        ),
    },
    "creation_operation_event": {
        "fresh_operation_request_id": "descendant_body_creation_operation_request_001",
        "persistent_operation_id": "descendant_body_creation_operation_001",
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
    "relation": {
        "relation_id": RELATION_ID,
        "relation_pair_scope": RELATION_PAIR_SCOPE,
    },
    "first_crossing_a": {
        "first_crossing_id": FIRST_CROSSING_A_ID,
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
    "first_crossing_b": {
        "first_crossing_id": FIRST_CROSSING_B_ID,
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
        "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
        "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
        "complete_pair_preserved": True,
        "descendant_bodies_remain_sibling": True,
        "descendant_body_non_hierarchy_preserved": True,
        "candidate_standing_non_hierarchy_preserved": True,
        "candidate_basis_non_hierarchy_preserved": True,
        "motion_does_not_erase_regulation": True,
        "regulation_not_sovereign_over_motion": True,
        "one_shared_crossing_operation_event": True,
        "separate_crossing_occurrences_created": False,
        "source_semantic_owner_transferred": False,
        "topology": TOPOLOGY,
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
    "source_stopping": {
        "automatic_successor_created": False,
        "relation_operation_authorized": False,
        "relation_operation_invoked": False,
    },
    "freshness": {
        "current_boundary_result_identity_declared": True,
        "current_boundary_result_identity_distinct_from_historical_operation_occurrence": True,
        "current_operation_event_identity_declared": True,
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
            "artifacts/integrity_host_v0_min_coexistence_relation_operation_v0_min/"
            "relation_operation_001__relation_operation_v0_min_result.json"
        ),
        "result_sha256": (
            "0e0b8d5ee6bbc01f77cd6e42463e62e4d10019475efa06359046c364acba9bae"
        ),
        "outcome": OUTCOME_RECORDED,
        "relation_result": RESULT_SUPPORTED,
        "relation_id": RELATION_ID,
        "result_is_current_permission": False,
        "result_is_current_source": False,
        "result_is_current_occurrence": False,
        "result_replayed": False,
        "success_treated_as_fresh_permission": False,
    },
    "reversibility_bridge": {
        "boundary_id": "relation_reversibility_boundary_001",
        "boundary_type": "RELATION_REVERSIBILITY_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": (
            "CONSIDER_RELATION_REVERSIBILITY_AFTER_RELATION_SUPPORT_BEFORE_PRESENCE_ONLY"
        ),
        "boundary_contract_reference": (
            "spec/RELATION_REVERSIBILITY_BOUNDARY_V0_MIN_SPEC.md"
        ),
        "boundary_contract_sha256": (
            "422a9ce767c9273a5c898d1d9d7da6d57a0ba7c5da4ac54ed3be9995ae2d8bd3"
        ),
        "admissible_future_route": (
            "RELATION_REVERSIBILITY_BOUNDARY_THEN_"
            "RELATION_REVERSIBILITY_OPERATION_ONLY"
        ),
        "direct_relation_operation_to_presence_boundary_without_"
        "reversibility_boundary_consideration": False,
    },
    "non_claim_attribution": {
        "source_boundary": {"owner": "RELATION_BOUNDARY"},
        "source_crossing_operation": {"owner": "FIRST_CROSSING_OPERATION"},
        "source_family": {"owner": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"},
        "target_local": {"owner": OPERATION_TYPE},
    },
}

EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE = {
    "source_outcome": "RELATION_BOUNDARY_ALLOWED",
    "source_boundary_result": "RELATION_OPERATION_CONSIDERATION_ALLOWED",
    "relation_operation_consideration_allowed": True,
    "first_crossing_operation_referenced": True,
    "first_crossing_a_referenced": True,
    "first_crossing_b_referenced": True,
    "first_crossing_pair_referenced": True,
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
ORDINARY_RELATION_SUPPORT_BASIS_PATHS = frozenset(
    {"ordinary_operation_basis.relation_support_found"}
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
    "ORDINARY_RELATION_SUPPORT_BASIS": ORDINARY_RELATION_SUPPORT_BASIS_PATHS,
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
assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 158
assert len(ORDINARY_BOUNDARY_ALLOWANCE_PATHS) == 7
assert len(ORDINARY_RELATION_SUPPORT_BASIS_PATHS) == 1
assert len(SOURCE_BOUNDARY_NON_CLAIM_PATHS) == 8
assert len(OPERATION_LOCAL_NON_CLAIM_PATHS) == 68
assert len(REQUIRED_NON_CLAIM_PATHS) == 76
assert len(ALL_REQUIRED_PATHS) == 245
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & _other_paths
        for _other_name, _other_paths in CLASS_PATHS.items()
        if _other_name != _class_name
    )
assert not set(POSITIVE_OPERATION_BOOLEAN_FIELDS) & set(
    OPERATION_LOCAL_NON_CLAIM_KEYS
)


def build_declared_relation_operation_v0_min_v3_request() -> dict[str, Any]:
    """Return the exact candidate envelope without creating a relation event."""

    return {
        "intent": INTENT_RECORD,
        "operation_question": OPERATION_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_operation_basis": {
            **deepcopy(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE),
            "relation_support_found": True,
        },
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


build_relation_operation_v0_min_v3_request = (
    build_declared_relation_operation_v0_min_v3_request
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
        return False, checks, extras[0] if extras else missing[0], root_code

    intent_valid = _same_exact_value(envelope["intent"], INTENT_RECORD)
    checks.append(
        _check("control_intent_exact", "CONTROL", "intent", intent_valid, "CONTROL_INVALID")
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


def _ordinary_allowance_review(
    ordinary: Any,
) -> tuple[str, list[dict[str, Any]], tuple[str, ...], str | None]:
    prefix = "ordinary_operation_basis"
    checks: list[dict[str, Any]] = []
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_boundary_allowance_mapping",
                "ORDINARY_BOUNDARY_ALLOWANCE",
                prefix,
                False,
                "ORDINARY_BOUNDARY_ALLOWANCE_INVALID",
            )
        )
        return "blocked", checks, (), prefix

    allowed_keys = set(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE) | {
        "relation_support_found"
    }
    extras = sorted(set(ordinary) - allowed_keys)
    if extras:
        path = f"{prefix}.{extras[0]}"
        checks.append(
            _check(
                "ordinary_basis_no_unsupported_fields",
                "ORDINARY_BOUNDARY_ALLOWANCE",
                path,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return "blocked", checks, (), path

    expected_keys = set(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE)
    present_keys = set(ordinary) & expected_keys
    missing_paths = tuple(
        f"{prefix}.{key}" for key in sorted(expected_keys - set(ordinary))
    )
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
    for key in sorted(present_keys):
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
    return "allowed", checks, (), None


def _event_projection(event_valid: bool, key: str) -> Any:
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[key]) if event_valid else None


def _relation_result(outcome: str) -> str:
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
        "relation_id": RELATION_ID,
        "relation_pair_scope": RELATION_PAIR_SCOPE,
        "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
        "relation_result": _relation_result(outcome),
        **{field: False for field in POSITIVE_OPERATION_BOOLEAN_FIELDS},
        **{field: False for field in OPERATION_LOCAL_NON_CLAIM_KEYS},
    }
    if recorded:
        operation.update(
            {field: True for field in POSITIVE_OPERATION_BOOLEAN_FIELDS}
        )
    return operation


def _operation_material(outcome: str, event_valid: bool) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "relation_evaluation": {
            "relation_id": RELATION_ID,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
            "relation_supported": recorded,
            "relation_authorized": recorded,
            "relation_created": recorded,
            "relation_operation_performed": recorded,
            "relation_recorded": recorded,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "standing_created": False,
            "currentness_created": False,
            "authority_created": False,
        },
        "relation_basis_evaluation": {
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "first_crossing_a_used_as_relation_basis": recorded,
            "first_crossing_b_used_as_relation_basis": recorded,
            "first_crossing_pair_used_as_relation_basis": recorded,
            "first_crossing_a_is_relation": False,
            "first_crossing_b_is_relation": False,
            "first_crossing_pair_is_relation": False,
            "crossing_authorization_is_relation_creation": False,
            "crossing_performance_is_relation_creation": False,
            "first_crossing_is_coupling": False,
            "first_crossing_is_presence": False,
            "first_crossing_is_identity": False,
        },
        "relation_pair_evaluation": {
            "relation_id": RELATION_ID,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "topology": TOPOLOGY,
            "complete_pair_preserved": event_valid,
            "first_crossings_remain_sibling": event_valid,
            "first_crossing_non_hierarchy_preserved": event_valid,
            "descendant_bodies_remain_sibling": event_valid,
            "descendant_body_non_hierarchy_preserved": event_valid,
            "candidate_standing_non_hierarchy_preserved": event_valid,
            "candidate_basis_non_hierarchy_preserved": event_valid,
            "motion_does_not_erase_regulation": event_valid,
            "regulation_not_sovereign_over_motion": event_valid,
            "source_semantic_owner_transferred": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
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
    allowance_complete: bool = False,
    support_posture: str = "NOT_EVALUATED",
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    operation = _operation_object(outcome)
    failed_check_count = sum(check["passed"] is False for check in checks)
    return {
        "executable_metadata": {
            "operation_id": OPERATION_ID,
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
        },
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "operation_question": OPERATION_QUESTION,
        "current_relation_operation_event": _event_projection(
            event_valid, "operation_event"
        ),
        "current_boundary_result_binding": _event_projection(
            event_valid, "current_boundary_result"
        ),
        "persistent_relation_operation_contract": _event_projection(
            event_valid, "target"
        ),
        "persistent_relation_boundary_identity": _event_projection(
            event_valid, "boundary"
        ),
        "persistent_crossing_operation_identity": _event_projection(
            event_valid, "crossing_operation"
        ),
        "crossing_operation_event": _event_projection(
            event_valid, "crossing_operation_event"
        ),
        "creation_operation_identity": _event_projection(
            event_valid, "creation_operation"
        ),
        "creation_operation_event": _event_projection(
            event_valid, "creation_operation_event"
        ),
        "persistent_relation_identity": (
            {
                **_event_projection(event_valid, "relation"),
                "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
                "identity_allocation_is_relation_existence": False,
            }
            if event_valid
            else None
        ),
        "relation_subject": (
            {
                "first_crossing_a": _event_projection(event_valid, "first_crossing_a"),
                "first_crossing_b": _event_projection(event_valid, "first_crossing_b"),
                "pair": _event_projection(event_valid, "pair"),
            }
            if event_valid
            else None
        ),
        "source_binding": _event_projection(event_valid, "source"),
        "source_applicability": _event_projection(event_valid, "source_applicability"),
        "source_stopping_posture": _event_projection(event_valid, "source_stopping"),
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
        "reversibility_bridge": _event_projection(
            event_valid, "reversibility_bridge"
        ),
        "non_claim_attribution": _event_projection(
            event_valid, "non_claim_attribution"
        ),
        "ordinary_boundary_allowance_review": {
            "complete": allowance_complete,
            "missing_paths": list(missing_allowance_paths),
            "requires_boundary_allowance_creates_retry_permission": False,
            "requires_boundary_allowance_creates_successor_permission": False,
        },
        "ordinary_relation_support_review": {
            "posture": support_posture,
            "relation_support_found": recorded,
            "not_recorded_creates_retry_permission": False,
            "not_recorded_creates_successor_permission": False,
        },
        "relation_operation": operation,
        "relation_operation_material": _operation_material(outcome, event_valid),
        "source_boundary_non_claims": {
            key: False for key in SOURCE_BOUNDARY_NON_CLAIM_KEYS
        },
        "operation_local_non_claims": {
            key: False for key in OPERATION_LOCAL_NON_CLAIM_KEYS
        },
        "relation_operation_checks": checks,
        "passed_check_count": len(checks) - failed_check_count,
        "failed_check_count": failed_check_count,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requires_boundary_allowance": (
                outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
            ),
            "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        },
        "downstream_stopping_point": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "next_separately_bounded_rank": "RELATION_REVERSIBILITY_BOUNDARY",
        },
    }


def resolve_relation_operation_v0_min_v3(supplied_envelope: Any) -> dict[str, Any]:
    """Resolve one exact current relation-operation event without I/O."""

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

    allowance_state, allowance_checks, missing_paths, allowance_issue = (
        _ordinary_allowance_review(supplied_envelope["ordinary_operation_basis"])
    )
    checks.extend(allowance_checks)
    if allowance_state == "blocked":
        key = allowance_issue.rsplit(".", 1)[-1] if allowance_issue else None
        code = (
            "UNSUPPORTED_INPUT"
            if key
            not in set(EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE)
            | {"relation_support_found"}
            else "ORDINARY_BOUNDARY_ALLOWANCE_INVALID"
        )
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code=code,
            issue_path=allowance_issue,
            missing_allowance_paths=missing_paths,
        )
    if allowance_state == "requires":
        return _build_result(
            OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            checks,
            event_valid=True,
            missing_allowance_paths=missing_paths,
            support_posture="NOT_EVALUATED",
        )

    ordinary = supplied_envelope["ordinary_operation_basis"]
    support = ordinary.get("relation_support_found")
    support_exact = _same_exact_value(support, True)
    checks.append(
        _check(
            "ordinary_relation_support_basis_exact",
            "ORDINARY_RELATION_SUPPORT_BASIS",
            "ordinary_operation_basis.relation_support_found",
            support_exact,
        )
    )
    if not support_exact:
        return _build_result(
            OUTCOME_NOT_RECORDED,
            checks,
            event_valid=True,
            allowance_complete=True,
            support_posture="NOT_SUPPORTED",
        )
    return _build_result(
        OUTCOME_RECORDED,
        checks,
        event_valid=True,
        allowance_complete=True,
        support_posture="SUPPORTED",
    )
