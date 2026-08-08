"""Additive v2 result-envelope correction for standing-effect applicability.

The governing boundary and v1 decision semantics remain unchanged. This
successor preserves exact source-owned structures already accepted by the v1
validator so the emitted result satisfies the governing Section 12 contract.
It performs no filesystem access, hashing, persistence, operation invocation,
standing derivation, or semantic interpretation.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min as _v1


RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_standing_effect_applicability_"
    "boundary_v0_min_v2"
)
RESULT_VERSION = "0.2.0"

BOUNDARY_ID = _v1.BOUNDARY_ID
BOUNDARY_TYPE = _v1.BOUNDARY_TYPE
BOUNDARY_VERSION = _v1.BOUNDARY_VERSION
BOUNDARY_SCOPE = _v1.BOUNDARY_SCOPE

OUTCOME_RECORDED = _v1.OUTCOME_RECORDED
OUTCOME_NOT_APPLICABLE = _v1.OUTCOME_NOT_APPLICABLE
OUTCOME_REQUIRES_ADDITIONAL_BASIS = _v1.OUTCOME_REQUIRES_ADDITIONAL_BASIS
OUTCOME_REVIEW_BLOCKED = _v1.OUTCOME_REVIEW_BLOCKED
OUTCOMES = _v1.OUTCOMES

SOURCE_FAMILY = _v1.SOURCE_FAMILY
SOURCE_SEMANTIC_OWNER = _v1.SOURCE_SEMANTIC_OWNER
SOURCE_CONTRACT_VERSION = _v1.SOURCE_CONTRACT_VERSION
SOURCE_CONTRACT_REFERENCE = _v1.SOURCE_CONTRACT_REFERENCE
SOURCE_CONTRACT_CONTENT_IDENTITY = _v1.SOURCE_CONTRACT_CONTENT_IDENTITY
SOURCE_ARTIFACT_REFERENCE = _v1.SOURCE_ARTIFACT_REFERENCE
SOURCE_ARTIFACT_CONTENT_IDENTITY = _v1.SOURCE_ARTIFACT_CONTENT_IDENTITY
SOURCE_OUTCOME = _v1.SOURCE_OUTCOME
SOURCE_FAILED_CHECK_COUNT = _v1.SOURCE_FAILED_CHECK_COUNT
SOURCE_PASSED_CHECK_COUNT = _v1.SOURCE_PASSED_CHECK_COUNT

SOURCE_OPERATION_ID = _v1.SOURCE_OPERATION_ID
SOURCE_OPERATION_TYPE = _v1.SOURCE_OPERATION_TYPE
SOURCE_OPERATION_VERSION = _v1.SOURCE_OPERATION_VERSION
SOURCE_OPERATION_SCOPE = _v1.SOURCE_OPERATION_SCOPE
SOURCE_CANDIDATE_STANDING_RESULT = _v1.SOURCE_CANDIDATE_STANDING_RESULT
BASIS_PAIR_SCOPE = _v1.BASIS_PAIR_SCOPE
ADMISSIBLE_FUTURE_ROUTE = _v1.ADMISSIBLE_FUTURE_ROUTE

CANDIDATE_A_RECORD_ID = _v1.CANDIDATE_A_RECORD_ID
CANDIDATE_A_ROLE = _v1.CANDIDATE_A_ROLE
CANDIDATE_A_BASIS_ID = _v1.CANDIDATE_A_BASIS_ID
CANDIDATE_A_BASIS_LABEL = _v1.CANDIDATE_A_BASIS_LABEL
CANDIDATE_B_RECORD_ID = _v1.CANDIDATE_B_RECORD_ID
CANDIDATE_B_ROLE = _v1.CANDIDATE_B_ROLE
CANDIDATE_B_BASIS_ID = _v1.CANDIDATE_B_BASIS_ID
CANDIDATE_B_BASIS_LABEL = _v1.CANDIDATE_B_BASIS_LABEL

STANDING_EFFECT_LOCATIONS = _v1.STANDING_EFFECT_LOCATIONS
SOURCE_LINEAGE_REFERENCES = _v1.SOURCE_LINEAGE_REFERENCES
SOURCE_REQUIRED_FALSE_NON_CLAIMS = _v1.SOURCE_REQUIRED_FALSE_NON_CLAIMS
REQUIRED_FALSE_NON_CLAIMS = _v1.REQUIRED_FALSE_NON_CLAIMS
NO_STANDING_CHANGE_FIELDS = _v1.NO_STANDING_CHANGE_FIELDS
STOP_CODES = _v1.STOP_CODES
BLOCK_CODES = _v1.BLOCK_CODES
OPEN_ITEMS = _v1.OPEN_ITEMS


def _copy_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _copy_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_copy_value(item) for item in value]
    if isinstance(value, tuple):
        return [_copy_value(item) for item in value]
    return value


def _check_passed(result: Mapping[str, Any], check_id: str) -> bool:
    checks = result.get("checks")
    if not isinstance(checks, list):
        return False
    return any(
        isinstance(check, Mapping)
        and check.get("check_id") == check_id
        and check.get("passed") is True
        for check in checks
    )


def _request_mapping(request: object, key: str) -> Mapping[str, Any] | None:
    if not isinstance(request, Mapping):
        return None
    value = request.get(key)
    return value if isinstance(value, Mapping) else None


def _preserve_section_12_result_material(
    result: dict[str, Any], request: object
) -> None:
    if not isinstance(request, Mapping):
        return

    source_binding = result.get("source_binding")
    if not isinstance(source_binding, dict):
        return

    if _check_passed(result, "source_contract_matches"):
        contract = _request_mapping(request, "source_standing_contract")
        if contract is not None:
            source_binding["source_standing_contract_version"] = _copy_value(
                contract["source_standing_contract_version"]
            )
            source_binding["source_standing_contract_content_identity"] = _copy_value(
                contract["source_standing_contract_content_identity"]
            )

    if _check_passed(result, "effect_locations_match_source"):
        result["standing_effect_locations"] = _copy_value(
            request["standing_effect_locations"]
        )

    if _check_passed(result, "source_artifact_matches"):
        artifact = _request_mapping(request, "source_artifact")
        if artifact is not None:
            for key in (
                "source_outcome",
                "source_failed_check_count",
                "source_passed_check_count",
            ):
                source_binding[key] = _copy_value(artifact[key])

    if _check_passed(result, "source_operation_matches"):
        operation = _request_mapping(request, "source_operation")
        if operation is not None:
            result["source_operation"] = _copy_value(operation)
            for key in (
                "candidate_standing_operation_type",
                "candidate_standing_operation_version",
                "candidate_standing_operation_scope",
                "candidate_standing_supported",
                "candidate_standing_authorized",
                "candidate_standing_created",
                "candidate_a_standing_created",
                "candidate_b_standing_created",
                "basis_pair_scope",
            ):
                source_binding[key] = _copy_value(operation[key])
            if source_binding.get("source_standing_created") is True:
                source_binding["source_standing_created"] = (
                    operation["candidate_standing_created"] is True
                )

    if _check_passed(result, "candidate_pair_matches_complete_sibling_pair"):
        pair = _request_mapping(request, "candidate_pair")
        if pair is not None:
            result["candidate_pair"] = _copy_value(pair)
            candidate_a = pair["candidate_a"]
            candidate_b = pair["candidate_b"]
            source_binding.update(
                {
                    "candidate_a_role": _copy_value(candidate_a["candidate_role"]),
                    "candidate_a_basis_label": _copy_value(
                        candidate_a["candidate_basis_label"]
                    ),
                    "candidate_b_role": _copy_value(candidate_b["candidate_role"]),
                    "candidate_b_basis_label": _copy_value(
                        candidate_b["candidate_basis_label"]
                    ),
                }
            )

    if _check_passed(result, "source_material_preserves_complete_pair"):
        material = _request_mapping(request, "candidate_standing_operation_material")
        if material is not None:
            result["candidate_standing_operation_material"] = _copy_value(material)
            result["standing_pair_evaluation"] = _copy_value(
                material["standing_pair_evaluation"]
            )

    if _check_passed(result, "source_lineage_matches"):
        result["source_lineage"] = _copy_value(request["source_lineage"])

    for check_id, key in (
        ("source_custody_matches", "source_custody"),
        ("source_rank_matches", "source_rank"),
        ("source_scope_matches", "source_scope"),
    ):
        if _check_passed(result, check_id):
            result[key] = _copy_value(request[key])

    if _check_passed(result, "cross_object_binding_matches"):
        result["cross_object_binding"] = _copy_value(
            request["cross_object_binding"]
        )


def build_declared_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2_request(
    declared_downstream_matter_use: str = ADMISSIBLE_FUTURE_ROUTE,
    **overrides: Any,
) -> dict[str, Any]:
    """Build the unchanged canonical closed request envelope for v2."""

    return _v1.build_declared_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_request(
        declared_downstream_matter_use,
        **overrides,
    )


def resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2(
    request: object,
) -> dict[str, Any]:
    """Resolve with v1 decisions and preserve the validated Section 12 envelope."""

    result = _copy_value(
        _v1.resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min(
            request
        )
    )
    result["result_version"] = RESULT_VERSION
    result["resolver_module"] = RESOLVER_MODULE
    _preserve_section_12_result_material(result, request)
    return result
