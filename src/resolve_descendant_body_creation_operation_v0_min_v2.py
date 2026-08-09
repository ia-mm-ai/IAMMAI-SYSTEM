"""Pure current-line resolver for one descendant-body-creation operation event."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any

from resolve_descendant_body_creation_operation_request_v0_min import (
    EXPECTED_CONSTITUTIONAL_EVENT_KEY as _REQUEST_CONSTITUTIONAL_EVENT_BINDING,
    REQUEST_QUESTION as _RECORDED_OPERATION_REQUEST_QUESTION,
)


RESOLVER_MODULE = "resolve_descendant_body_creation_operation_v0_min_v2"
RESULT_VERSION = "0.2.0"

OPERATION_FAMILY = "DESCENDANT_BODY_CREATION_OPERATION"
OPERATION_ID = "descendant_body_creation_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CREATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
OPERATION_REQUEST_ID = "descendant_body_creation_operation_request_001"

OPERATION_CONTRACT_REFERENCE = "spec/DESCENDANT_BODY_CREATION_OPERATION_V0_MIN_SPEC.md"
OPERATION_CONTRACT_SHA256 = (
    "82cf281c103c53742dc963435df1a0efdb62037f591db926f9ea7a63dc33f6f4"
)
CURRENT_SOURCE_RESULT_REFERENCE = (
    "artifacts/descendant_body_creation_operation_request_v0_min/"
    "descendant_body_creation_operation_request_001__"
    "descendant_body_creation_operation_request_v0_min_result.json"
)
CURRENT_SOURCE_RESULT_SHA256 = (
    "dd95b114773c8ff1b1f0a271530f282c2360b3aa58c07231886f111808d6e744"
)
ADMISSIBLE_FUTURE_ROUTE = (
    "DESCENDANT_BODY_CREATION_OPERATION_THEN_FIRST_CROSSING_BOUNDARY_ONLY"
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CREATION_OPERATION"
OPERATION_QUESTION = (
    "Given exact recorded current operation request "
    "descendant_body_creation_operation_request_001, persistent operation "
    "descendant_body_creation_operation_001, the exact current V3 boundary allowance, "
    "consumed and exhausted current lineage, complete Candidate A/B pair, source "
    "semantic ownership and applicability, exact operation contract, freshness and "
    "historical non-replay, and all required non-claims, may "
    "DESCENDANT_BODY_CREATION_OPERATION evaluate whether Candidate A standing and "
    "Candidate B standing may receive their separate descendant-body records under its "
    "mature law?"
)

OUTCOME_BLOCKED = "DESCENDANT_BODY_CREATION_OPERATION_BLOCKED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = (
    "DESCENDANT_BODY_CREATION_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
)
OUTCOME_NOT_CREATED = "DESCENDANT_BODY_CREATION_OPERATION_NOT_CREATED"
OUTCOME_CREATED = "DESCENDANT_BODY_CREATION_OPERATION_CREATED"
OUTCOME_FAMILY = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_NOT_CREATED,
    OUTCOME_CREATED,
)

RESULT_SUPPORTED = "DESCENDANT_BODY_CREATION_SUPPORTED"
RESULT_NOT_SUPPORTED = "DESCENDANT_BODY_CREATION_NOT_SUPPORTED"

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INPUT",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
    }
)

POSITIVE_OPERATION_FIELDS = (
    "descendant_body_creation_operation_recorded",
    "descendant_body_creation_evaluation_performed",
    "descendant_body_creation_result_recorded",
    "descendant_body_a_creation_evaluated",
    "descendant_body_b_creation_evaluated",
    "descendant_body_a_creation_supported",
    "descendant_body_b_creation_supported",
    "descendant_body_creation_supported",
    "descendant_body_creation_authorized",
    "descendant_body_creation_performed",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
)

OPERATION_LOCAL_NON_CLAIM_KEYS = tuple(
    """
    standing_descendant_created
    descendant_body_a_is_standing_descendant
    descendant_body_b_is_standing_descendant
    descendant_standing_check_performed
    crossing_authorized
    first_crossing_authorized
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
    coupling_assigned_to_candidate_a
    coupling_assigned_to_candidate_b
    coupling_created
    third_candidate_created
    third_model_admitted
    presence_established
    identity_created
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
    descendant_body_creation_boundary_overridden
    descendant_body_creation_boundary_bypassed
    candidate_standing_operation_overridden
    candidate_standing_operation_bypassed
    scan_performed
    repository_scan_performed
    file_discovery_performed
    repair_performed
    validation_enforced
    hidden_repair_performed
    silent_overwrite_performed
    direct_descendant_body_creation_operation_spec_to_descendant_body_creation_operation_completion
    direct_boundary_allowance_to_descendant_body_creation_without_operation
    direct_candidate_standing_to_descendant_body_creation_without_boundary_and_operation
    direct_descendant_body_creation_to_standing_descendant
    direct_descendant_body_creation_to_descendant_standing
    direct_descendant_body_creation_to_crossing
    direct_descendant_body_creation_to_relation
    direct_descendant_body_creation_to_runtime
    direct_descendant_body_creation_to_authority_currentness
    direct_descendant_body_creation_to_coupling_creation
    direct_descendant_body_creation_to_third_candidate_route
    direct_descendant_body_creation_to_third_model_route
    direct_descendant_body_creation_to_presence
    direct_descendant_body_creation_to_identity
    direct_descendant_body_creation_to_output_action
    direct_descendant_body_creation_to_follow_on_work
    """.split()
)

EXPECTED_OPERATION_REQUEST_POSTURE = {
    "operation_request_id": OPERATION_REQUEST_ID,
    "operation_request_type": "DESCENDANT_BODY_CREATION_OPERATION_REQUEST",
    "operation_request_version": "0.1.0",
    "operation_request_scope": (
        "ONE_FRESH_DESCENDANT_BODY_CREATION_OPERATION_REQUEST_ONE_CURRENT_V3_"
        "BOUNDARY_RESULT_ONLY"
    ),
    "descendant_body_creation_operation_request_recorded": True,
    "exact_operation_request_identity_preserved": True,
    "persistent_operation_target_preserved": True,
    "current_v3_boundary_result_preserved": True,
    "current_lineage_binding_preserved": True,
    "selected_surface_complete_pair_preserved": True,
    "source_family_semantic_ownership_preserved": True,
    "source_applicability_preserved": True,
    "operation_contract_preserved": True,
    "declared_matter_use_preserved": True,
    "freshness_and_non_replay_preserved": True,
    "result_level_non_claims_canonical_false": True,
}

EXPECTED_OPERATION_REQUEST_RESULT = {
    "result_reference": CURRENT_SOURCE_RESULT_REFERENCE,
    "result_sha256": CURRENT_SOURCE_RESULT_SHA256,
    "resolver_module": "resolve_descendant_body_creation_operation_request_v0_min",
    "result_version": "0.1.0",
    "outcome": "DESCENDANT_BODY_CREATION_OPERATION_REQUEST_RECORDED",
    "passed_check_count": 240,
    "failed_check_count": 0,
    "request_question": _RECORDED_OPERATION_REQUEST_QUESTION,
    "block": {
        "blocked": False,
        "code": None,
        "issue_path": None,
        "requirement_code": None,
    },
    "ordinary_request_basis_review": {
        "complete": True,
        "missing_paths": [],
        "additional_basis_creates_no_retry_or_successor_permission": True,
    },
    "descendant_body_creation_operation_request": EXPECTED_OPERATION_REQUEST_POSTURE,
    "constitutional_event_binding": _REQUEST_CONSTITUTIONAL_EVENT_BINDING,
}
EXPECTED_CONSTITUTIONAL_EVENT_KEY = {
    "operation_request_result": EXPECTED_OPERATION_REQUEST_RESULT
}
EXPECTED_ORDINARY_OPERATION_BASIS = {
    "descendant_body_creation_support_evidence_present": True
}
EXPECTED_REQUIRED_NON_CLAIMS = {
    "operation_local": {key: False for key in OPERATION_LOCAL_NON_CLAIM_KEYS}
}

DESCENDANT_BODY_A_RECORD = {
    "descendant_body_id": "descendant_body_a_001",
    "candidate_standing_source_id": "descendant_body_basis_candidate_a_001",
    "candidate_role": "CANDIDATE_A",
    "candidate_standing_label": "CANDIDATE_A_STANDING",
    "candidate_basis_id": (
        "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
    ),
    "candidate_basis_label": "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS",
    "candidate_basis_scope": "Motion-side admissible variation",
    "candidate_standing_created": True,
    "candidate_standing_is_descendant_body": False,
    "descendant_body_creation_supported": True,
    "descendant_body_creation_authorized": True,
    "descendant_body_created": True,
    "standing_descendant_created": False,
    "descendant_body_is_standing_descendant": False,
    "crossing_authorized": False,
    "relation_created": False,
    "presence_established": False,
    "identity_created": False,
}
DESCENDANT_BODY_B_RECORD = {
    "descendant_body_id": "descendant_body_b_001",
    "candidate_standing_source_id": "descendant_body_basis_candidate_b_001",
    "candidate_role": "CANDIDATE_B",
    "candidate_standing_label": "CANDIDATE_B_STANDING",
    "candidate_basis_id": (
        "descendant_body_basis_candidate_b_001__regulation_side_"
        "admissibility_bounds_basis"
    ),
    "candidate_basis_label": (
        "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
    ),
    "candidate_basis_scope": "Regulation-side admissibility bounds",
    "candidate_standing_created": True,
    "candidate_standing_is_descendant_body": False,
    "descendant_body_creation_supported": True,
    "descendant_body_creation_authorized": True,
    "descendant_body_created": True,
    "standing_descendant_created": False,
    "descendant_body_is_standing_descendant": False,
    "crossing_authorized": False,
    "relation_created": False,
    "presence_established": False,
    "identity_created": False,
}
DESCENDANT_BODY_PAIR_RESULT = {
    "both_descendant_body_creations_supported": True,
    "both_descendant_body_creations_authorized": True,
    "both_descendant_bodies_created": True,
    "descendant_body_a_created": True,
    "descendant_body_b_created": True,
    "descendant_body_created": True,
    "descendant_bodies_remain_sibling": True,
    "descendant_body_non_hierarchy_preserved": True,
    "candidate_standing_non_hierarchy_preserved": True,
    "candidate_basis_non_hierarchy_preserved": True,
    "regulation_not_sovereign_over_motion": True,
    "motion_does_not_erase_regulation": True,
    "standing_descendant_created": False,
    "descendant_standing_check_performed": False,
    "crossing_authorized": False,
    "first_crossing_authorized": False,
    "coupling_assigned": False,
    "coupling_created": False,
    "third_candidate_created": False,
    "third_model_admitted": False,
    "relation_created": False,
    "presence_established": False,
    "identity_created": False,
    "follow_on_authorized": False,
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
ORDINARY_OPERATION_BASIS_PATHS = frozenset(
    {"ordinary_operation_basis.descendant_body_creation_support_evidence_present"}
)
REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.operation_local.{key}"
    for key in OPERATION_LOCAL_NON_CLAIM_KEYS
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_OPERATION_BASIS": ORDINARY_OPERATION_BASIS_PATHS,
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
assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 179
assert len(ORDINARY_OPERATION_BASIS_PATHS) == 1
assert len(REQUIRED_NON_CLAIM_PATHS) == 65
assert len(ALL_REQUIRED_PATHS) == 248
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & _other_paths
        for _other_name, _other_paths in CLASS_PATHS.items()
        if _other_name != _class_name
    )


def build_declared_descendant_body_creation_operation_v0_min_v2_request(
    *, descendant_body_creation_support_evidence_present: Any = True
) -> dict[str, Any]:
    """Return the canonical supplied envelope without creating an event or artifact."""

    return {
        "intent": INTENT_RECORD,
        "operation_question": OPERATION_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_operation_basis": {
            "descendant_body_creation_support_evidence_present": (
                descendant_body_creation_support_evidence_present
            )
        },
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
    checks.append(
        _check(
            "control_root_mapping_cardinality",
            "CONTROL",
            "$::mapping_cardinality",
            root_valid,
            "UNSUPPORTED_INPUT" if extras else "CONTROL_INVALID",
        )
    )
    if not root_valid:
        issue = extras[0] if extras else missing[0]
        return (
            False,
            checks,
            issue,
            "UNSUPPORTED_INPUT" if extras else "CONTROL_INVALID",
        )

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
) -> tuple[str, list[dict[str, Any]], str | None]:
    path = "ordinary_operation_basis.descendant_body_creation_support_evidence_present"
    checks: list[dict[str, Any]] = []
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_operation_basis_mapping",
                "ORDINARY_OPERATION_BASIS",
                "ordinary_operation_basis",
                False,
            )
        )
        return "not_created", checks, "ordinary_operation_basis"

    extras = sorted(
        set(ordinary) - {"descendant_body_creation_support_evidence_present"}
    )
    if extras:
        checks.append(
            _check(
                "ordinary_operation_basis_no_unsupported_fields",
                "ORDINARY_OPERATION_BASIS",
                f"ordinary_operation_basis.{extras[0]}",
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return "blocked", checks, f"ordinary_operation_basis.{extras[0]}"

    support = ordinary.get("descendant_body_creation_support_evidence_present")
    exact_true = _same_exact_value(support, True)
    checks.append(
        _check(
            "ordinary_descendant_body_creation_support_evidence_present",
            "ORDINARY_OPERATION_BASIS",
            path,
            exact_true,
        )
    )
    return ("created" if exact_true else "not_created"), checks, (
        None if exact_true else path
    )


def _event_projection(event_valid: bool, *path: str) -> Any:
    if not event_valid:
        return None
    current: Any = EXPECTED_CONSTITUTIONAL_EVENT_KEY
    for key in path:
        current = current[key]
    return deepcopy(current)


def _build_result(
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    event_valid: bool,
    block_code: str | None = None,
    issue_path: str | None = None,
    ordinary_issue_path: str | None = None,
) -> dict[str, Any]:
    created = outcome == OUTCOME_CREATED
    operation_posture = {field: created for field in POSITIVE_OPERATION_FIELDS}
    operation_posture.update(
        {
            "operation_family": OPERATION_FAMILY,
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "descendant_body_creation_result": (
                RESULT_SUPPORTED
                if created
                else RESULT_NOT_SUPPORTED
                if outcome == OUTCOME_NOT_CREATED
                else None
            ),
        }
    )
    failed_check_count = sum(not check["passed"] for check in checks)
    passed_check_count = len(checks) - failed_check_count

    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "operation_question": OPERATION_QUESTION,
        "current_operation_event": {
            "persistent_operation_id": OPERATION_ID,
            "fresh_operation_request_id": OPERATION_REQUEST_ID,
            "source_result_reference": CURRENT_SOURCE_RESULT_REFERENCE,
            "source_result_sha256": CURRENT_SOURCE_RESULT_SHA256,
            "same_identity_same_binding_is_deterministic_rerender": True,
            "resolver_call_count_is_event_count": False,
        },
        "operation_request_result_binding": _event_projection(
            event_valid, "operation_request_result"
        ),
        "current_lineage": (
            {
                "current_request": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "current_request",
                ),
                "current_request_admission": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "current_request_admission",
                ),
                "actual_consumption": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "actual_consumption",
                ),
                "current_boundary": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "current_boundary",
                ),
            }
            if event_valid
            else None
        ),
        "persistent_operation_contract": _event_projection(
            event_valid,
            "operation_request_result",
            "constitutional_event_binding",
            "operation_contract",
        ),
        "selected_candidate_source": _event_projection(
            event_valid,
            "operation_request_result",
            "constitutional_event_binding",
            "selected_surface",
        ),
        "source_applicability_and_use": (
            {
                "source_applicability": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "source_applicability",
                ),
                "declared_use": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "declared_use",
                ),
            }
            if event_valid
            else None
        ),
        "freshness_and_history": (
            {
                "freshness": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "freshness",
                ),
                "historical_operation_evidence_only": _event_projection(
                    event_valid,
                    "operation_request_result",
                    "constitutional_event_binding",
                    "historical_operation",
                ),
            }
            if event_valid
            else None
        ),
        "ordinary_operation_basis_review": {
            "support_evidence_exact_boolean_true": created,
            "issue_path": ordinary_issue_path,
            "not_created_creates_retry_or_successor_permission": False,
        },
        "descendant_body_creation_operation": operation_posture,
        "descendant_body_creation_material": (
            {
                "descendant_body_a": deepcopy(DESCENDANT_BODY_A_RECORD),
                "descendant_body_b": deepcopy(DESCENDANT_BODY_B_RECORD),
                "pair_result": deepcopy(DESCENDANT_BODY_PAIR_RESULT),
            }
            if created
            else {}
        ),
        "operation_local_non_claims": {
            key: False for key in OPERATION_LOCAL_NON_CLAIM_KEYS
        },
        "descendant_body_creation_operation_checks": checks,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requires_boundary_allowance": (
                outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
            ),
        },
        "downstream_stopping_point": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "next_separately_bounded_rank": "FIRST_CROSSING_BOUNDARY",
            "first_crossing_boundary_invoked": False,
            "first_crossing_boundary_authorized": False,
            "standing_descendant_created": False,
            "crossing_authorized": False,
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
            "derivative_reception_authorized": False,
            "synchronization_authorized": False,
            "follow_on_work_authorized": False,
            "automatic_successor_created": False,
        },
    }


def resolve_descendant_body_creation_operation_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Resolve one closed current-event envelope without I/O or persistence."""

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

    ordinary_state, ordinary_checks, ordinary_issue = _ordinary_review(
        supplied_envelope["ordinary_operation_basis"]
    )
    checks.extend(ordinary_checks)
    if ordinary_state == "blocked":
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code="UNSUPPORTED_INPUT",
            issue_path=ordinary_issue,
        )
    if ordinary_state == "not_created":
        return _build_result(
            OUTCOME_NOT_CREATED,
            checks,
            event_valid=True,
            ordinary_issue_path=ordinary_issue,
        )
    return _build_result(OUTCOME_CREATED, checks, event_valid=True)

