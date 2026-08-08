"""Pure matter-bound candidate occurrence-evidence allocation resolver.

The resolver consumes one closed in-memory request envelope and structurally
checks whether exact supplied evidence references may be allocated to one exact
occurrence claim. The occurrence-evidence contract remains the semantic owner:
this module verifies an exact supplied contract-owned posture and its bindings,
but does not read contract prose, determine evidence adequacy, establish the
occurrence, evaluate the represented proposition, enact anything, or persist
state.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


RESOLVER_MODULE = (
    "resolve_matter_bound_candidate_occurrence_evidence_allocation_v0_min"
)
RESULT_VERSION = "0.1.0"

ALLOCATION_TYPE = "MATTER_BOUND_CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION"
ALLOCATION_VERSION = "0.1.0"
ALLOCATION_SCOPE = (
    "ONE_EXACT_MATTER_ONE_EXACT_CANDIDATE_ONE_EXACT_REPRESENTED_PROPOSITION_"
    "ONE_SEPARATELY_AUTHORIZED_BOUNDED_ENACTMENT_ONE_EXACT_OCCURRENCE_CLAIM_ONLY"
)

OUTCOME_RECORDED = "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_NOT_RECORDED"
OUTCOME_REVIEW_BLOCKED = (
    "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_REVIEW_BLOCKED"
)
OUTCOMES = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REVIEW_BLOCKED,
)

REQUIRED_FALSE_NON_CLAIMS = (
    "enactment_authorization_created",
    "enactment_occurrence_established",
    "occurrence_claim_established",
    "occurrence_truth_generalized",
    "represented_proposition_evidenced",
    "represented_proposition_true",
    "represented_proposition_current",
    "represented_proposition_standing",
    "represented_proposition_authoritative",
    "candidate_standing_created",
    "candidate_authority_created",
    "candidate_adopted",
    "candidate_integrated",
    "reuse_permission_created",
    "continuation_permission_created",
    "successor_authority_created",
    "runtime_created",
    "sandbox_created",
    "local_field_created",
    "prior_standing_revoked",
    "registry_created",
    "ontology_created",
    "catalogue_created",
    "coverage_authority_created",
    "interpreter_authority_created",
    "semantic_ownership_transferred",
    "globality_created",
    "public_readiness_created",
    "deployment_permission_created",
    "follow_on_work_authorized",
    "evidence_adequacy_determined_by_allocation_boundary",
    "occurrence_evidence_invented",
    "evidence_migrated_to_represented_proposition",
    "result_treated_as_success",
    "result_standing_created",
    "trace_treated_as_success",
    "trace_execution_authority_persisted",
    "success_treated_as_proposition_support",
    "repetition_treated_as_adoption_force",
    "repetition_treated_as_integration_force",
    "standing_invocation_lane_created",
    "repeat_enactment_permission_created",
    "authorization_scope_widened",
    "source_family_overridden",
    "proposition_semantics_reinterpreted",
    "candidate_preference_selected",
    "prior_standing_granted_by_allocation",
    "currentness_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "adoption_force_created",
    "integration_force_created",
    "mutation_performed",
    "automatic_next_step_created",
)
CANONICAL_NON_CLAIMS = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}

REQUEST_KEYS = frozenset(
    {
        "matter",
        "candidate_configuration",
        "represented_proposition",
        "candidate_proposition_binding",
        "bounded_enactment_authorization",
        "bounded_enactment_invocation",
        "occurrence_claim",
        "result",
        "trace",
        "occurrence_evidence_contract",
        "contract_owned_allocability_rule_or_occurrence_support_posture",
        "occurrence_evidence_references",
        "evidence_allocation_statement",
        "lineage_and_custody",
        "bounded_allocation_decision_posture",
        "declared_non_claims",
    }
)

MATTER_FIELDS = (
    "matter_id",
    "matter_purpose",
    "matter_scope",
    "allocation_question",
    "outside_boundary",
)
CANDIDATE_FIELDS = (
    "candidate_id",
    "candidate_type",
    "candidate_version",
    "candidate_reference",
    "candidate_content_identity",
)
PROPOSITION_FIELDS = (
    "represented_proposition_id",
    "represented_proposition_type",
    "represented_proposition_statement",
    "represented_proposition_reference",
    "represented_proposition_semantic_owner",
    "represented_proposition_matter_scope",
)
BINDING_FIELDS = (
    "candidate_proposition_binding_id",
    "candidate_proposition_binding_type",
    "candidate_proposition_binding_direction",
    "candidate_proposition_binding_scope",
    "candidate_id",
    "represented_proposition_id",
)
AUTHORIZATION_FIELDS = (
    "authorization_id",
    "authorization_type",
    "authorization_version",
    "authorization_reference",
    "admitted_scope",
    "enactment_mode",
    "candidate_id",
    "matter_id",
    "invocation_id",
    "input_ids",
    "condition_ids",
    "permitted_invocation_count",
    "non_reuse_posture",
)
INVOCATION_FIELDS = (
    "invocation_id",
    "authorization_id",
    "candidate_id",
    "matter_id",
    "enactment_mode",
    "input_ids",
    "condition_ids",
    "result_id",
    "trace_id",
)
OCCURRENCE_CLAIM_FIELDS = (
    "occurrence_claim_id",
    "occurrence_claim_type",
    "occurrence_claim_wording",
    "occurrence_claim_scope",
    "matter_id",
    "candidate_id",
    "candidate_proposition_binding_id",
    "authorization_id",
    "invocation_id",
    "result_id",
    "trace_id",
)
RESULT_FIELDS = (
    "result_id",
    "result_reference",
    "result_type",
    "bounded_result_posture",
)
TRACE_FIELDS = (
    "trace_id",
    "trace_reference",
    "trace_type",
    "trace_posture",
    "audit_or_occurrence_evidence_only",
)
CONTRACT_FIELDS = (
    "occurrence_evidence_contract_id",
    "occurrence_evidence_contract_type",
    "occurrence_evidence_contract_version",
    "occurrence_evidence_contract_reference",
    "occurrence_evidence_contract_semantic_owner",
    "applicability_scope",
    "evidence_effect_location",
    "governed_evidence_class",
    "governed_occurrence_claim_type",
    "governed_occurrence_claim_scope",
)
CONTRACT_POSTURE_FIELDS = (
    "posture_id",
    "posture_type",
    "posture_reference",
    "occurrence_evidence_contract_id",
    "semantic_owner",
    "applicability_scope",
    "evidence_class",
    "occurrence_claim_id",
    "allocation_target_id",
    "allocation_target_type",
    "allocation_to_exact_occurrence_claim_permitted",
    "allocation_to_represented_proposition_permitted",
)
EVIDENCE_REFERENCE_FIELDS = (
    "occurrence_evidence_reference_id",
    "occurrence_evidence_reference",
    "evidence_class",
    "occurrence_evidence_contract_id",
    "contract_owned_posture_id",
    "occurrence_claim_id",
)
ALLOCATION_STATEMENT_FIELDS = (
    "allocation_statement_id",
    "occurrence_claim_id",
    "sole_allocation_target_id",
    "represented_proposition_id",
    "occurrence_evidence_reference_ids",
    "allocated_to_occurrence_claim_only",
    "allocation_to_represented_proposition_refused",
)
LINEAGE_AND_CUSTODY_FIELDS = ("object_references",)
OBJECT_REFERENCE_FIELDS = (
    "object_id",
    "lineage_reference",
    "custody_reference",
)
DECISION_POSTURE_FIELDS = (
    "allocation_decision_id",
    "allocation_decision_scope",
    "occurrence_claim_id",
    "represented_proposition_id",
    "one_allocation_decision_only",
    "occurrence_is_not_established",
    "evidence_adequacy_is_not_determined",
    "evidentiary_migration_is_blocked",
)

STOP_REASONS = {
    "REQUEST_NOT_MAPPING": "The request must be one in-memory mapping.",
    "REQUEST_FIELDS_INCOMPLETE": "The closed request envelope is missing a required top-level field.",
    "REQUEST_KEYS_INVALID": "The request contains an unknown or non-canonical top-level field.",
    "MATTER_ADDITIONAL_BASIS_REQUIRED": "One exact matter and all of its bounded fields are required.",
    "MATTER_MALFORMED": "The matter structure is malformed.",
    "CANDIDATE_ADDITIONAL_BASIS_REQUIRED": "One exact candidate configuration is required.",
    "CANDIDATE_MALFORMED": "The candidate configuration is malformed.",
    "PROPOSITION_ADDITIONAL_BASIS_REQUIRED": "One exact represented proposition is required.",
    "PROPOSITION_MALFORMED": "The represented proposition is malformed.",
    "BINDING_ADDITIONAL_BASIS_REQUIRED": "One exact directional candidate-proposition binding is required.",
    "BINDING_MALFORMED": "The candidate-proposition binding is malformed.",
    "AUTHORIZATION_ADDITIONAL_BASIS_REQUIRED": "One separately admitted bounded authorization is required.",
    "AUTHORIZATION_MALFORMED": "The authorization structure is malformed.",
    "INVOCATION_ADDITIONAL_BASIS_REQUIRED": "One exact bounded invocation, inputs, and conditions are required.",
    "INVOCATION_MALFORMED": "The invocation structure is malformed.",
    "OCCURRENCE_CLAIM_ADDITIONAL_BASIS_REQUIRED": "One exact occurrence claim and wording are required.",
    "OCCURRENCE_CLAIM_MALFORMED": "The occurrence claim is malformed.",
    "RESULT_ADDITIONAL_BASIS_REQUIRED": "One exact bounded result reference is required.",
    "RESULT_MALFORMED": "The result structure is malformed.",
    "TRACE_ADDITIONAL_BASIS_REQUIRED": "One exact bounded trace reference is required.",
    "TRACE_MALFORMED": "The trace structure is malformed.",
    "CONTRACT_ADDITIONAL_BASIS_REQUIRED": "One exact occurrence-evidence contract is required.",
    "CONTRACT_MALFORMED": "The occurrence-evidence contract is malformed.",
    "CONTRACT_POSTURE_ADDITIONAL_BASIS_REQUIRED": "One exact attributable contract-owned allocability rule or support posture is required.",
    "CONTRACT_POSTURE_MALFORMED": "The contract-owned allocability rule or support posture is malformed.",
    "EVIDENCE_REFERENCES_ADDITIONAL_BASIS_REQUIRED": "Exact occurrence-evidence references are required.",
    "EVIDENCE_REFERENCES_MALFORMED": "Occurrence-evidence references are malformed.",
    "ALLOCATION_STATEMENT_ADDITIONAL_BASIS_REQUIRED": "One exact O-only allocation statement is required.",
    "ALLOCATION_STATEMENT_MALFORMED": "The allocation statement is malformed.",
    "LINEAGE_CUSTODY_ADDITIONAL_BASIS_REQUIRED": "Exact lineage and custody bindings are required.",
    "LINEAGE_CUSTODY_MALFORMED": "Lineage or custody bindings are malformed.",
    "DECISION_POSTURE_ADDITIONAL_BASIS_REQUIRED": "One bounded allocation-decision posture is required.",
    "DECISION_POSTURE_MALFORMED": "The allocation-decision posture is malformed.",
    "NON_CLAIM_ADDITIONAL_BASIS_REQUIRED": "The complete canonical non-claim set is required.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "Every mandatory non-claim must be present and exactly false.",
    "BINDING_IDENTITY_MISMATCH": "The candidate-proposition binding does not bind exact C and P.",
    "AUTHORIZATION_BINDING_MISMATCH": "Authorization does not bind exact M, C, I, inputs, and conditions.",
    "AUTHORIZATION_SCOPE_NOT_APPLICABLE": "Authorization scope, count, or non-reuse posture does not cover the claimed enactment.",
    "INVOCATION_BINDING_MISMATCH": "Invocation does not bind exact A, C, M, inputs, conditions, R, and T.",
    "OCCURRENCE_CLAIM_BINDING_MISMATCH": "Occurrence claim does not bind exact M, C, B(C,P), A, I, R, and T.",
    "OCCURRENCE_CLAIM_OVERREACH": "Occurrence wording contains a proposition truth, standing, authority, adoption, or integration claim.",
    "TRACE_POSTURE_OVERREACH": "Trace is not limited to audit or occurrence-evidence posture.",
    "CONTRACT_BINDING_MISMATCH": "Contract does not structurally govern the supplied evidence class and exact O claim shape.",
    "CONTRACT_POSTURE_BINDING_MISMATCH": "The supplied contract-owned posture is not exactly attributable and bound to E and O.",
    "CONTRACT_POSTURE_NOT_APPLICABLE": "The supplied contract-owned posture does not permit allocation to exact O only.",
    "EVIDENCE_REFERENCE_BINDING_MISMATCH": "Every evidence reference must bind exact E, contract-owned posture, and O.",
    "EVIDENCE_REFERENCE_ID_DUPLICATED": "Evidence-reference identities and references must be unique.",
    "ALLOCATION_TARGET_NOT_EXACT_OCCURRENCE": "The allocation statement does not name exact O as its sole target.",
    "ALLOCATION_TO_PROPOSITION_NOT_REFUSED": "The allocation statement does not refuse allocation to P.",
    "LINEAGE_CUSTODY_BINDING_MISMATCH": "Lineage and custody do not cover exactly the selected envelope objects.",
    "DECISION_POSTURE_OVERREACH": "The declared decision posture would establish occurrence, determine adequacy, migrate evidence, or widen decisions.",
}
STOP_CODES = frozenset(STOP_REASONS)
BLOCK_CODES = frozenset(
    code
    for code in STOP_CODES
    if code.endswith("MALFORMED")
    or code
    in {
        "REQUEST_NOT_MAPPING",
        "REQUEST_KEYS_INVALID",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "BINDING_IDENTITY_MISMATCH",
        "AUTHORIZATION_BINDING_MISMATCH",
        "INVOCATION_BINDING_MISMATCH",
        "OCCURRENCE_CLAIM_BINDING_MISMATCH",
        "OCCURRENCE_CLAIM_OVERREACH",
        "TRACE_POSTURE_OVERREACH",
        "CONTRACT_BINDING_MISMATCH",
        "CONTRACT_POSTURE_BINDING_MISMATCH",
        "EVIDENCE_REFERENCE_BINDING_MISMATCH",
        "EVIDENCE_REFERENCE_ID_DUPLICATED",
        "LINEAGE_CUSTODY_BINDING_MISMATCH",
        "DECISION_POSTURE_OVERREACH",
    }
)

NON_MEANING = (
    "allocation_is_not_occurrence_establishment",
    "allocation_is_not_evidence_adequacy_determination",
    "occurrence_evidence_is_not_represented_proposition_evidence",
    "occurrence_is_not_represented_proposition_truth",
    "result_is_not_success_or_standing",
    "trace_is_not_execution_authority_or_standing",
    "success_is_not_proposition_support_adoption_or_integration",
    "repetition_is_not_currentness_reuse_or_successor_authority",
)
OPEN_ITEMS = (
    "live_candidate_enactment",
    "occurrence_evidence_establishment_or_verification",
    "proposition_evaluation",
    "candidate_comparison_adoption_or_integration",
    "runtime_hosting",
    "correspondence_or_standing_basis_integration",
    "artifact_receipt_or_terminal_summary",
    "later_successor_work",
)

_FORBIDDEN_OCCURRENCE_WORDING = (
    "represented proposition is true",
    "represented proposition stands",
    "represented proposition is standing",
    "represented proposition is authoritative",
    "proposition truth established",
    "proposition standing established",
    "proposition authority established",
    "candidate is adopted",
    "candidate was adopted",
    "candidate is integrated",
    "candidate was integrated",
)


def resolve_matter_bound_candidate_occurrence_evidence_allocation_v0_min(
    request: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Resolve one exact occurrence-evidence allocation envelope."""

    checks: list[dict[str, Any]] = []
    normalized: dict[str, Any] = {
        key: [] if key == "occurrence_evidence_references" else None
        for key in REQUEST_KEYS
        if key != "declared_non_claims"
    }

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
            normalized=normalized,
            checks=checks,
            stopping_code=code,
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

    sections = (
        ("matter", MATTER_FIELDS, "MATTER"),
        ("candidate_configuration", CANDIDATE_FIELDS, "CANDIDATE"),
        ("represented_proposition", PROPOSITION_FIELDS, "PROPOSITION"),
        ("candidate_proposition_binding", BINDING_FIELDS, "BINDING"),
        ("bounded_enactment_authorization", AUTHORIZATION_FIELDS, "AUTHORIZATION"),
        ("bounded_enactment_invocation", INVOCATION_FIELDS, "INVOCATION"),
        ("occurrence_claim", OCCURRENCE_CLAIM_FIELDS, "OCCURRENCE_CLAIM"),
        ("result", RESULT_FIELDS, "RESULT"),
        ("trace", TRACE_FIELDS, "TRACE"),
        ("occurrence_evidence_contract", CONTRACT_FIELDS, "CONTRACT"),
        (
            "contract_owned_allocability_rule_or_occurrence_support_posture",
            CONTRACT_POSTURE_FIELDS,
            "CONTRACT_POSTURE",
        ),
        (
            "evidence_allocation_statement",
            ALLOCATION_STATEMENT_FIELDS,
            "ALLOCATION_STATEMENT",
        ),
        (
            "bounded_allocation_decision_posture",
            DECISION_POSTURE_FIELDS,
            "DECISION_POSTURE",
        ),
    )
    for section_name, fields, code_prefix in sections:
        value, state = _normalize_fixed_mapping(request.get(section_name), fields)
        if state == "missing":
            return stopped(
                f"{section_name}_is_complete",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                f"{code_prefix}_ADDITIONAL_BASIS_REQUIRED",
            )
        if state == "invalid":
            return stopped(
                f"{section_name}_is_exact",
                OUTCOME_REVIEW_BLOCKED,
                f"{code_prefix}_MALFORMED",
            )
        normalized[section_name] = value
        passed(f"{section_name}_is_exact")

    authorization = normalized["bounded_enactment_authorization"]
    invocation = normalized["bounded_enactment_invocation"]
    allocation_statement = normalized["evidence_allocation_statement"]
    decision_posture = normalized["bounded_allocation_decision_posture"]

    for section, list_fields, code_prefix in (
        (authorization, ("input_ids", "condition_ids"), "AUTHORIZATION"),
        (invocation, ("input_ids", "condition_ids"), "INVOCATION"),
        (
            allocation_statement,
            ("occurrence_evidence_reference_ids",),
            "ALLOCATION_STATEMENT",
        ),
    ):
        for field in list_fields:
            items, state = _normalize_text_list(section.get(field))
            if state == "missing":
                return stopped(
                    f"{field}_is_present",
                    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    f"{code_prefix}_ADDITIONAL_BASIS_REQUIRED",
                )
            if state == "invalid":
                return stopped(
                    f"{field}_is_exact",
                    OUTCOME_REVIEW_BLOCKED,
                    f"{code_prefix}_MALFORMED",
                )
            section[field] = items

    if (
        not _exact_int(authorization["permitted_invocation_count"])
        or type(authorization["non_reuse_posture"]) is not bool
    ):
        return stopped(
            "authorization_scope_types_are_exact",
            OUTCOME_REVIEW_BLOCKED,
            "AUTHORIZATION_MALFORMED",
        )
    if type(normalized["trace"]["audit_or_occurrence_evidence_only"]) is not bool:
        return stopped(
            "trace_posture_type_is_exact", OUTCOME_REVIEW_BLOCKED, "TRACE_MALFORMED"
        )
    for key in (
        "allocation_to_exact_occurrence_claim_permitted",
        "allocation_to_represented_proposition_permitted",
    ):
        if type(normalized[
            "contract_owned_allocability_rule_or_occurrence_support_posture"
        ][key]) is not bool:
            return stopped(
                "contract_owned_posture_types_are_exact",
                OUTCOME_REVIEW_BLOCKED,
                "CONTRACT_POSTURE_MALFORMED",
            )
    for key in (
        "allocated_to_occurrence_claim_only",
        "allocation_to_represented_proposition_refused",
    ):
        if type(allocation_statement[key]) is not bool:
            return stopped(
                "allocation_statement_types_are_exact",
                OUTCOME_REVIEW_BLOCKED,
                "ALLOCATION_STATEMENT_MALFORMED",
            )
    for key in (
        "one_allocation_decision_only",
        "occurrence_is_not_established",
        "evidence_adequacy_is_not_determined",
        "evidentiary_migration_is_blocked",
    ):
        if type(decision_posture[key]) is not bool:
            return stopped(
                "decision_posture_types_are_exact",
                OUTCOME_REVIEW_BLOCKED,
                "DECISION_POSTURE_MALFORMED",
            )
    passed("specialized_scalar_types_are_exact")

    evidence, state = _normalize_evidence_references(
        request.get("occurrence_evidence_references")
    )
    if state == "missing":
        return stopped(
            "occurrence_evidence_references_are_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "EVIDENCE_REFERENCES_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid":
        return stopped(
            "occurrence_evidence_references_are_exact",
            OUTCOME_REVIEW_BLOCKED,
            "EVIDENCE_REFERENCES_MALFORMED",
        )
    normalized["occurrence_evidence_references"] = evidence
    passed("occurrence_evidence_references_are_exact")

    lineage, state = _normalize_lineage_and_custody(request.get("lineage_and_custody"))
    if state == "missing":
        return stopped(
            "lineage_and_custody_are_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "LINEAGE_CUSTODY_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid":
        return stopped(
            "lineage_and_custody_are_exact",
            OUTCOME_REVIEW_BLOCKED,
            "LINEAGE_CUSTODY_MALFORMED",
        )
    normalized["lineage_and_custody"] = lineage
    passed("lineage_and_custody_are_exact")

    non_claim_state = _validate_non_claims(request.get("declared_non_claims"))
    if non_claim_state == "missing":
        return stopped(
            "mandatory_non_claims_are_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "NON_CLAIM_ADDITIONAL_BASIS_REQUIRED",
        )
    if non_claim_state == "invalid":
        return stopped(
            "mandatory_non_claims_remain_false",
            OUTCOME_REVIEW_BLOCKED,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    passed("mandatory_non_claims_remain_false")

    matter = normalized["matter"]
    candidate = normalized["candidate_configuration"]
    proposition = normalized["represented_proposition"]
    binding = normalized["candidate_proposition_binding"]
    occurrence = normalized["occurrence_claim"]
    result = normalized["result"]
    trace = normalized["trace"]
    contract = normalized["occurrence_evidence_contract"]
    contract_posture = normalized[
        "contract_owned_allocability_rule_or_occurrence_support_posture"
    ]

    if (
        binding["candidate_id"] != candidate["candidate_id"]
        or binding["represented_proposition_id"]
        != proposition["represented_proposition_id"]
    ):
        return stopped(
            "binding_names_exact_candidate_and_proposition",
            OUTCOME_REVIEW_BLOCKED,
            "BINDING_IDENTITY_MISMATCH",
        )
    passed("binding_names_exact_candidate_and_proposition")

    if (
        authorization["candidate_id"] != candidate["candidate_id"]
        or authorization["matter_id"] != matter["matter_id"]
        or authorization["invocation_id"] != invocation["invocation_id"]
        or authorization["enactment_mode"] != invocation["enactment_mode"]
        or authorization["input_ids"] != invocation["input_ids"]
        or authorization["condition_ids"] != invocation["condition_ids"]
    ):
        return stopped(
            "authorization_binds_exact_enactment",
            OUTCOME_REVIEW_BLOCKED,
            "AUTHORIZATION_BINDING_MISMATCH",
        )
    if (
        authorization["permitted_invocation_count"] != 1
        or authorization["non_reuse_posture"] is not True
    ):
        return stopped(
            "authorization_scope_covers_one_non_reusable_invocation",
            OUTCOME_NOT_RECORDED,
            "AUTHORIZATION_SCOPE_NOT_APPLICABLE",
        )
    passed("authorization_scope_covers_one_non_reusable_invocation")

    if (
        invocation["authorization_id"] != authorization["authorization_id"]
        or invocation["candidate_id"] != candidate["candidate_id"]
        or invocation["matter_id"] != matter["matter_id"]
        or invocation["result_id"] != result["result_id"]
        or invocation["trace_id"] != trace["trace_id"]
    ):
        return stopped(
            "invocation_binds_exact_envelope",
            OUTCOME_REVIEW_BLOCKED,
            "INVOCATION_BINDING_MISMATCH",
        )
    passed("invocation_binds_exact_envelope")

    occurrence_bindings = {
        "matter_id": matter["matter_id"],
        "candidate_id": candidate["candidate_id"],
        "candidate_proposition_binding_id": binding[
            "candidate_proposition_binding_id"
        ],
        "authorization_id": authorization["authorization_id"],
        "invocation_id": invocation["invocation_id"],
        "result_id": result["result_id"],
        "trace_id": trace["trace_id"],
    }
    if any(occurrence[key] != value for key, value in occurrence_bindings.items()):
        return stopped(
            "occurrence_claim_binds_exact_envelope",
            OUTCOME_REVIEW_BLOCKED,
            "OCCURRENCE_CLAIM_BINDING_MISMATCH",
        )
    wording = occurrence["occurrence_claim_wording"].casefold()
    if any(fragment in wording for fragment in _FORBIDDEN_OCCURRENCE_WORDING):
        return stopped(
            "occurrence_claim_remains_occurrence_only",
            OUTCOME_REVIEW_BLOCKED,
            "OCCURRENCE_CLAIM_OVERREACH",
        )
    passed("occurrence_claim_binds_exact_envelope_and_remains_occurrence_only")

    if trace["audit_or_occurrence_evidence_only"] is not True:
        return stopped(
            "trace_remains_audit_or_occurrence_evidence_only",
            OUTCOME_REVIEW_BLOCKED,
            "TRACE_POSTURE_OVERREACH",
        )
    passed("result_and_trace_remain_bounded_non_authoritative_posture")

    evidence_classes = {item["evidence_class"] for item in evidence}
    if (
        len(evidence_classes) != 1
        or contract["governed_evidence_class"] not in evidence_classes
        or contract["evidence_effect_location"]
        != occurrence["occurrence_claim_id"]
        or contract["governed_occurrence_claim_type"]
        != occurrence["occurrence_claim_type"]
        or contract["governed_occurrence_claim_scope"]
        != occurrence["occurrence_claim_scope"]
    ):
        return stopped(
            "contract_structurally_governs_evidence_and_occurrence_shape",
            OUTCOME_REVIEW_BLOCKED,
            "CONTRACT_BINDING_MISMATCH",
        )
    passed("contract_structurally_governs_evidence_and_occurrence_shape")

    if (
        contract_posture["occurrence_evidence_contract_id"]
        != contract["occurrence_evidence_contract_id"]
        or contract_posture["semantic_owner"]
        != contract["occurrence_evidence_contract_semantic_owner"]
        or contract_posture["applicability_scope"] != contract["applicability_scope"]
        or contract_posture["evidence_class"]
        != contract["governed_evidence_class"]
        or contract_posture["occurrence_claim_id"]
        != occurrence["occurrence_claim_id"]
        or contract_posture["allocation_target_id"]
        != occurrence["occurrence_claim_id"]
        or contract_posture["allocation_target_type"]
        != occurrence["occurrence_claim_type"]
    ):
        return stopped(
            "contract_owned_posture_is_attributable_and_exactly_bound",
            OUTCOME_REVIEW_BLOCKED,
            "CONTRACT_POSTURE_BINDING_MISMATCH",
        )
    if (
        contract_posture["allocation_to_exact_occurrence_claim_permitted"]
        is not True
        or contract_posture["allocation_to_represented_proposition_permitted"]
        is not False
    ):
        return stopped(
            "contract_owned_posture_applies_to_exact_occurrence_only",
            OUTCOME_NOT_RECORDED,
            "CONTRACT_POSTURE_NOT_APPLICABLE",
        )
    passed("contract_owned_posture_applies_to_exact_occurrence_only")

    for item in evidence:
        if (
            item["occurrence_evidence_contract_id"]
            != contract["occurrence_evidence_contract_id"]
            or item["contract_owned_posture_id"] != contract_posture["posture_id"]
            or item["evidence_class"] != contract["governed_evidence_class"]
            or item["occurrence_claim_id"] != occurrence["occurrence_claim_id"]
        ):
            return stopped(
                "evidence_references_bind_exact_contract_posture_and_occurrence",
                OUTCOME_REVIEW_BLOCKED,
                "EVIDENCE_REFERENCE_BINDING_MISMATCH",
            )
    passed("evidence_references_bind_exact_contract_posture_and_occurrence")

    evidence_ids = [item["occurrence_evidence_reference_id"] for item in evidence]
    if (
        allocation_statement["occurrence_claim_id"]
        != occurrence["occurrence_claim_id"]
        or allocation_statement["sole_allocation_target_id"]
        != occurrence["occurrence_claim_id"]
        or allocation_statement["allocated_to_occurrence_claim_only"] is not True
        or allocation_statement["occurrence_evidence_reference_ids"] != evidence_ids
    ):
        return stopped(
            "allocation_statement_names_exact_occurrence_as_sole_target",
            OUTCOME_NOT_RECORDED,
            "ALLOCATION_TARGET_NOT_EXACT_OCCURRENCE",
        )
    if (
        allocation_statement["represented_proposition_id"]
        != proposition["represented_proposition_id"]
        or allocation_statement["allocation_to_represented_proposition_refused"]
        is not True
    ):
        return stopped(
            "allocation_statement_refuses_allocation_to_proposition",
            OUTCOME_NOT_RECORDED,
            "ALLOCATION_TO_PROPOSITION_NOT_REFUSED",
        )
    passed("allocation_statement_preserves_occurrence_only_non_migration")

    expected_object_ids = [
        matter["matter_id"],
        candidate["candidate_id"],
        proposition["represented_proposition_id"],
        binding["candidate_proposition_binding_id"],
        authorization["authorization_id"],
        invocation["invocation_id"],
        occurrence["occurrence_claim_id"],
        result["result_id"],
        trace["trace_id"],
        contract["occurrence_evidence_contract_id"],
        contract_posture["posture_id"],
        *evidence_ids,
    ]
    actual_object_ids = [
        item["object_id"] for item in lineage["object_references"]
    ]
    if actual_object_ids != expected_object_ids:
        return stopped(
            "lineage_and_custody_bind_every_selected_object",
            OUTCOME_REVIEW_BLOCKED,
            "LINEAGE_CUSTODY_BINDING_MISMATCH",
        )
    passed("lineage_and_custody_bind_every_selected_object")

    if (
        decision_posture["occurrence_claim_id"]
        != occurrence["occurrence_claim_id"]
        or decision_posture["represented_proposition_id"]
        != proposition["represented_proposition_id"]
        or decision_posture["one_allocation_decision_only"] is not True
        or decision_posture["occurrence_is_not_established"] is not True
        or decision_posture["evidence_adequacy_is_not_determined"] is not True
        or decision_posture["evidentiary_migration_is_blocked"] is not True
    ):
        return stopped(
            "decision_posture_preserves_boundary_limits",
            OUTCOME_REVIEW_BLOCKED,
            "DECISION_POSTURE_OVERREACH",
        )
    passed("decision_posture_preserves_boundary_limits")
    passed("exact_e_owned_posture_verified_without_contract_prose_interpretation")

    return _build_result(
        outcome=OUTCOME_RECORDED,
        normalized=normalized,
        checks=checks,
        stopping_code=None,
    )


def _normalize_fixed_mapping(
    value: Any, fields: tuple[str, ...]
) -> tuple[dict[str, Any] | None, str | None]:
    if value is None:
        return None, "missing"
    if not isinstance(value, Mapping):
        return None, "invalid"
    expected = frozenset(fields)
    actual = frozenset(value)
    if actual - expected:
        return None, "invalid"
    if expected - actual:
        return None, "missing"

    normalized: dict[str, Any] = {}
    non_text = {
        "input_ids",
        "condition_ids",
        "permitted_invocation_count",
        "non_reuse_posture",
        "audit_or_occurrence_evidence_only",
        "allocation_to_exact_occurrence_claim_permitted",
        "allocation_to_represented_proposition_permitted",
        "occurrence_evidence_reference_ids",
        "allocated_to_occurrence_claim_only",
        "allocation_to_represented_proposition_refused",
        "one_allocation_decision_only",
        "occurrence_is_not_established",
        "evidence_adequacy_is_not_determined",
        "evidentiary_migration_is_blocked",
    }
    for field in fields:
        item = value[field]
        if field in non_text:
            normalized[field] = item
        elif item is None or item == "":
            return None, "missing"
        elif not _has_text(item):
            return None, "invalid"
        else:
            normalized[field] = str(item)
    return normalized, None


def _normalize_evidence_references(
    value: Any,
) -> tuple[list[dict[str, str]], str | None]:
    if value is None or value == []:
        return [], "missing"
    if not isinstance(value, list):
        return [], "invalid"
    normalized: list[dict[str, str]] = []
    for item in value:
        entry, state = _normalize_fixed_mapping(item, EVIDENCE_REFERENCE_FIELDS)
        if state is not None:
            return [], state
        normalized.append(entry)  # type: ignore[arg-type]
    ids = [item["occurrence_evidence_reference_id"] for item in normalized]
    refs = [item["occurrence_evidence_reference"] for item in normalized]
    if len(set(ids)) != len(ids) or len(set(refs)) != len(refs):
        return [], "invalid"
    return normalized, None


def _normalize_lineage_and_custody(
    value: Any,
) -> tuple[dict[str, list[dict[str, str]]] | None, str | None]:
    if value is None:
        return None, "missing"
    if not isinstance(value, Mapping):
        return None, "invalid"
    expected = frozenset(LINEAGE_AND_CUSTODY_FIELDS)
    actual = frozenset(value)
    if actual - expected:
        return None, "invalid"
    if expected - actual:
        return None, "missing"
    items = value.get("object_references")
    if items is None or items == []:
        return None, "missing"
    if not isinstance(items, list):
        return None, "invalid"
    normalized: list[dict[str, str]] = []
    for item in items:
        entry, state = _normalize_fixed_mapping(item, OBJECT_REFERENCE_FIELDS)
        if state is not None:
            return None, state
        normalized.append(entry)  # type: ignore[arg-type]
    ids = [item["object_id"] for item in normalized]
    if len(set(ids)) != len(ids):
        return None, "invalid"
    return {"object_references": normalized}, None


def _normalize_text_list(value: Any) -> tuple[list[str] | None, str | None]:
    if value is None or value == []:
        return None, "missing"
    if not isinstance(value, list):
        return None, "invalid"
    if not all(_has_text(item) for item in value):
        return None, "invalid"
    normalized = [str(item) for item in value]
    if len(set(normalized)) != len(normalized):
        return None, "invalid"
    return normalized, None


def _validate_non_claims(value: Any) -> str | None:
    if value is None:
        return "missing"
    if not isinstance(value, Mapping):
        return "invalid"
    expected = frozenset(REQUIRED_FALSE_NON_CLAIMS)
    actual = frozenset(value)
    if actual - expected:
        return "invalid"
    if expected - actual:
        return "missing"
    if any(value.get(key) is not False for key in REQUIRED_FALSE_NON_CLAIMS):
        return "invalid"
    return None


def _build_result(
    *,
    outcome: str,
    normalized: Mapping[str, Any],
    checks: list[dict[str, Any]],
    stopping_code: str | None,
) -> dict[str, Any]:
    occurrence = normalized.get("occurrence_claim")
    proposition = normalized.get("represented_proposition")
    evidence = normalized.get("occurrence_evidence_references") or []
    recorded = outcome == OUTCOME_RECORDED
    occurrence_id = (
        occurrence.get("occurrence_claim_id")
        if isinstance(occurrence, Mapping)
        else None
    )
    proposition_id = (
        proposition.get("represented_proposition_id")
        if isinstance(proposition, Mapping)
        else None
    )
    evidence_ids = [
        item["occurrence_evidence_reference_id"]
        for item in evidence
        if isinstance(item, Mapping) and "occurrence_evidence_reference_id" in item
    ]

    copied = {
        ("bounded_result" if key == "result" else key): _copy_normalized(value)
        for key, value in normalized.items()
        if key != "declared_non_claims"
    }
    return {
        "metadata": {
            "matter_bound_candidate_occurrence_evidence_allocation_type": ALLOCATION_TYPE,
            "matter_bound_candidate_occurrence_evidence_allocation_version": ALLOCATION_VERSION,
            "matter_bound_candidate_occurrence_evidence_allocation_scope": ALLOCATION_SCOPE,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
        },
        **copied,
        "allocation_decision": {
            "decision_outcome": outcome,
            "allocation_recorded": recorded,
            "occurrence_claim_id": occurrence_id,
            "sole_allocation_target_id": occurrence_id if recorded else None,
            "represented_proposition_id": proposition_id,
            "allocated_occurrence_evidence_reference_ids": (
                evidence_ids if recorded else []
            ),
            "evidence_references_remain_bound_to_exact_occurrence_claim": recorded,
            "evidence_migration_to_represented_proposition_blocked": True,
            "exact_supplied_envelope_preserved": recorded,
            "occurrence_established": False,
            "evidence_adequacy_determined": False,
        },
        "checks": [dict(check) for check in checks],
        "result": {
            "outcome": outcome,
            "completion_posture": outcome,
            "lawful_terminal_outcome_recorded": True,
            "allocation_recorded": recorded,
            "stopping_code": stopping_code,
        },
        "non_meaning": list(NON_MEANING),
        "what_remains_open": {
            "open_items": list(OPEN_ITEMS),
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next": True,
        },
        "non_claims": dict(CANONICAL_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": stopping_code if outcome == OUTCOME_REVIEW_BLOCKED else None,
            "reason": (
                STOP_REASONS[stopping_code]
                if outcome == OUTCOME_REVIEW_BLOCKED and stopping_code is not None
                else None
            ),
        },
    }


def _copy_normalized(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _copy_normalized(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_copy_normalized(item) for item in value]
    return value


def _exact_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


__all__ = [
    "ALLOCATION_SCOPE",
    "ALLOCATION_TYPE",
    "ALLOCATION_VERSION",
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "OUTCOMES",
    "OUTCOME_NOT_RECORDED",
    "OUTCOME_RECORDED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "OUTCOME_REVIEW_BLOCKED",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_VERSION",
    "STOP_CODES",
    "resolve_matter_bound_candidate_occurrence_evidence_allocation_v0_min",
]
