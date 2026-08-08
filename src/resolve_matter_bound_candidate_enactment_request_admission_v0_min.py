"""Pure matter-bound candidate-enactment request-admission resolver.

The resolver consumes one closed in-memory M/C/EC/CA/P/B(C,P)/Q/X/S/I/K/L
envelope. Candidate applicability arrives as one exact, attributable,
family-owned emission. This module checks that emission structurally; it does
not interpret contract prose or candidate-result vocabulary, authorize or
perform enactment, evaluate the represented proposition, access the
filesystem, or persist state.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


RESOLVER_MODULE = (
    "resolve_matter_bound_candidate_enactment_request_admission_v0_min"
)
RESULT_VERSION = "0.1.0"

REQUEST_ADMISSION_TYPE = "MATTER_BOUND_CANDIDATE_ENACTMENT_REQUEST_ADMISSION"
REQUEST_ADMISSION_VERSION = "0.1.0"
REQUEST_ADMISSION_SCOPE = (
    "ONE_EXACT_MATTER_ONE_EXACT_CANDIDATE_ONE_EXACT_REPRESENTED_PROPOSITION_"
    "ONE_EXACT_SINGLE_ENACTMENT_REQUEST_ONLY"
)

OUTCOME_ADMITTED = "CANDIDATE_ENACTMENT_REQUEST_ADMITTED"
OUTCOME_NOT_ADMITTED = "CANDIDATE_ENACTMENT_REQUEST_NOT_ADMITTED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "CANDIDATE_ENACTMENT_REQUEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_REVIEW_BLOCKED = "CANDIDATE_ENACTMENT_REQUEST_REVIEW_BLOCKED"
OUTCOMES = (
    OUTCOME_ADMITTED,
    OUTCOME_NOT_ADMITTED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_REVIEW_BLOCKED,
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_readmitted",
    "candidate_standing_created",
    "candidate_currentness_created",
    "candidate_authority_created",
    "enactment_authorization_created",
    "invocation_authorization_created",
    "invocation_permission_created",
    "execution_permission_created",
    "candidate_enacted",
    "execution_performed",
    "enactment_occurrence_established",
    "output_created",
    "result_created",
    "trace_created",
    "success_established",
    "evidence_allocation_recorded",
    "evidence_adequacy_determined",
    "represented_proposition_evidenced",
    "represented_proposition_true",
    "represented_proposition_false",
    "represented_proposition_current",
    "represented_proposition_standing",
    "represented_proposition_authoritative",
    "governing_authority_created",
    "candidate_adopted",
    "candidate_integrated",
    "deployment_created",
    "runtime_hosting_created",
    "repeat_permission_created",
    "reusable_permission_created",
    "continuation_permission_created",
    "follow_on_permission_created",
    "successor_force_created",
    "candidate_registry_created",
    "global_candidate_ontology_created",
    "cross_family_semantic_allowlist_created",
    "source_family_semantics_overridden",
    "semantic_ownership_transferred",
    "standing_invocation_lane_created",
    "automatic_successor_created",
    "follow_on_work_authorized",
)
CANONICAL_NON_CLAIMS = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}

REQUEST_KEYS = frozenset(
    {
        "matter",
        "candidate_configuration",
        "family_owned_candidate_contract",
        "family_owned_candidate_basis",
        "family_owned_applicability_emission",
        "represented_proposition",
        "candidate_proposition_binding",
        "candidate_enactment_request",
        "requested_enactment",
        "requested_enactment_scope",
        "proposed_inputs",
        "proposed_conditions",
        "requested_locality_or_destination",
        "single_invocation_posture",
        "declared_non_claims",
    }
)

MATTER_FIELDS = (
    "matter_id",
    "matter_type",
    "matter_purpose",
    "matter_scope",
    "request_admission_question",
    "outside_boundary",
)
CANDIDATE_FIELDS = (
    "candidate_id",
    "candidate_type",
    "source_family",
    "custody_reference",
    "lineage_reference",
    "candidate_version",
    "candidate_immutable_reference",
    "candidate_content_identity",
    "candidate_standing",
    "candidate_current",
)
CONTRACT_FIELDS = (
    "candidate_contract_id",
    "candidate_contract_type",
    "candidate_contract_version",
    "candidate_contract_immutable_reference",
    "candidate_contract_semantic_owner",
    "source_family",
    "applicable_scope",
    "candidate_effect_location",
    "declared_use_applicability_rule_reference",
    "candidate_id",
    "candidate_basis_id",
    "declared_request_admission_use",
)
CANDIDATE_BASIS_FIELDS = (
    "candidate_basis_id",
    "candidate_basis_type",
    "candidate_basis_version",
    "candidate_basis_immutable_reference",
    "recorded_contract_owned_posture",
    "supporting_basis_references",
    "lineage_reference",
    "custody_reference",
    "candidate_basis_scope",
    "limitations",
    "candidate_basis_non_claims",
    "candidate_contract_id",
    "candidate_contract_semantic_owner",
    "source_family",
    "candidate_id",
    "declared_request_admission_use",
)
APPLICABILITY_EMISSION_FIELDS = (
    "applicability_emission_id",
    "applicability_emission_type",
    "applicability_emission_immutable_reference",
    "candidate_contract_id",
    "candidate_contract_immutable_reference",
    "candidate_contract_semantic_owner",
    "source_family",
    "candidate_basis_id",
    "candidate_id",
    "candidate_effect_location",
    "declared_request_admission_use",
    "applicable_scope",
    "lineage_reference",
    "custody_reference",
    "applicability_result",
    "applicability_basis_reference",
)
PROPOSITION_FIELDS = (
    "represented_proposition_id",
    "represented_proposition_type",
    "represented_proposition_statement",
    "represented_proposition_immutable_reference",
    "represented_proposition_semantic_owner",
    "matter_id",
    "matter_scope",
    "outside_boundary",
)
BINDING_FIELDS = (
    "candidate_proposition_binding_id",
    "candidate_proposition_binding_type",
    "candidate_proposition_binding_direction",
    "candidate_proposition_binding_scope",
    "matter_id",
    "candidate_id",
    "represented_proposition_id",
    "candidate_enactment_request_id",
)
ENACTMENT_REQUEST_FIELDS = (
    "candidate_enactment_request_id",
    "candidate_enactment_request_type",
    "candidate_enactment_request_version",
    "candidate_enactment_request_immutable_reference",
    "matter_id",
    "candidate_id",
    "represented_proposition_id",
    "candidate_proposition_binding_id",
    "requested_enactment_id",
    "requested_enactment_scope_id",
    "proposed_input_set_id",
    "proposed_condition_set_id",
    "requested_locality_or_destination_id",
    "declared_request_admission_use",
    "request_purpose",
    "request_scope",
    "outside_boundary",
    "request_admission_only_statement",
    "request_admission_does_not_authorize_or_perform_statement",
)
REQUESTED_ENACTMENT_FIELDS = (
    "requested_enactment_id",
    "requested_enactment_type",
    "matter_id",
    "candidate_id",
    "represented_proposition_id",
    "candidate_proposition_binding_id",
    "candidate_enactment_request_id",
    "requested_enactment_scope_id",
)
REQUESTED_SCOPE_FIELDS = (
    "requested_enactment_scope_id",
    "matter_id",
    "candidate_id",
    "represented_proposition_id",
    "candidate_proposition_binding_id",
    "candidate_enactment_request_id",
    "requested_enactment_id",
    "proposed_input_set_id",
    "proposed_condition_set_id",
    "requested_locality_or_destination_id",
    "requested_invocation_count",
    "maximum_requested_effect",
    "outside_boundary",
    "locality_or_destination_required",
)
PROPOSED_INPUT_FIELDS = (
    "proposed_input_set_id",
    "matter_id",
    "candidate_enactment_request_id",
    "requested_enactment_id",
    "input_references",
)
PROPOSED_CONDITION_FIELDS = (
    "proposed_condition_set_id",
    "matter_id",
    "candidate_enactment_request_id",
    "requested_enactment_id",
    "condition_references",
)
LOCALITY_FIELDS = (
    "requested_locality_or_destination_id",
    "requested_locality_or_destination_type",
    "requested_locality_or_destination_reference",
    "matter_id",
    "candidate_enactment_request_id",
    "requested_enactment_id",
    "requested_enactment_scope_id",
)
SINGLE_INVOCATION_FIELDS = (
    "requested_invocation_count",
    "no_repeat_posture",
    "no_reuse_posture",
    "no_standing_invocation_lane_posture",
    "no_automatic_successor_posture",
)

REQUEST_ADMISSION_ONLY_STATEMENT = (
    "REQUEST_ADMISSION_ONLY_FOR_POSSIBLE_LATER_SEPARATELY_BOUNDED_"
    "ENACTMENT_AUTHORIZATION_REVIEW"
)
REQUEST_DOES_NOT_AUTHORIZE_OR_PERFORM_STATEMENT = (
    "REQUEST_ADMISSION_DOES_NOT_AUTHORIZE_OR_PERFORM_REQUESTED_ENACTMENT"
)
REQUIRED_BINDING_DIRECTION = "CANDIDATE_TO_REPRESENTED_PROPOSITION"

STOP_REASONS = {
    "REQUEST_NOT_MAPPING": "The request must be one in-memory mapping.",
    "REQUEST_KEYS_INVALID": "The request contains an unknown or non-canonical top-level field.",
    "REQUEST_FIELDS_INCOMPLETE": "The closed request envelope is missing a required top-level field.",
    "MATTER_ADDITIONAL_BASIS_REQUIRED": "One exact matter and all bounded matter fields are required.",
    "MATTER_MALFORMED": "The exact matter structure is malformed.",
    "CANDIDATE_ADDITIONAL_BASIS_REQUIRED": "One exact candidate configuration is required.",
    "CANDIDATE_MALFORMED": "The candidate configuration is malformed.",
    "CONTRACT_ADDITIONAL_BASIS_REQUIRED": "One exact family-owned candidate contract is required.",
    "CONTRACT_MALFORMED": "The family-owned candidate contract is malformed.",
    "CANDIDATE_BASIS_ADDITIONAL_BASIS_REQUIRED": "One exact family-owned candidate basis is required.",
    "CANDIDATE_BASIS_MALFORMED": "The family-owned candidate basis is malformed.",
    "APPLICABILITY_EMISSION_ADDITIONAL_BASIS_REQUIRED": "One exact attributable EC-owned and CA-carried applicability emission is required.",
    "APPLICABILITY_EMISSION_MALFORMED": "The family-owned applicability emission is malformed or semantically unexplained.",
    "PROPOSITION_ADDITIONAL_BASIS_REQUIRED": "One exact represented proposition is required.",
    "PROPOSITION_MALFORMED": "The represented proposition is malformed.",
    "BINDING_ADDITIONAL_BASIS_REQUIRED": "One exact directional candidate-proposition binding is required.",
    "BINDING_MALFORMED": "The candidate-proposition binding is malformed.",
    "ENACTMENT_REQUEST_ADDITIONAL_BASIS_REQUIRED": "One exact candidate-enactment request is required.",
    "ENACTMENT_REQUEST_MALFORMED": "The candidate-enactment request is malformed.",
    "REQUESTED_ENACTMENT_ADDITIONAL_BASIS_REQUIRED": "One exact requested enactment identity is required.",
    "REQUESTED_ENACTMENT_MALFORMED": "The requested enactment identity is malformed.",
    "REQUESTED_SCOPE_ADDITIONAL_BASIS_REQUIRED": "One exact requested enactment scope is required.",
    "REQUESTED_SCOPE_MALFORMED": "The requested enactment scope is malformed.",
    "PROPOSED_INPUTS_ADDITIONAL_BASIS_REQUIRED": "One exact nonempty proposed input set is required.",
    "PROPOSED_INPUTS_MALFORMED": "The proposed input set is malformed.",
    "PROPOSED_CONDITIONS_ADDITIONAL_BASIS_REQUIRED": "One exact nonempty proposed condition set is required.",
    "PROPOSED_CONDITIONS_MALFORMED": "The proposed condition set is malformed.",
    "LOCALITY_ADDITIONAL_BASIS_REQUIRED": "One exact locality or destination is required by the requested scope.",
    "LOCALITY_MALFORMED": "The locality or destination is malformed.",
    "SINGLE_INVOCATION_ADDITIONAL_BASIS_REQUIRED": "Exact one-shot invocation guardrails are required.",
    "SINGLE_INVOCATION_MALFORMED": "The single-invocation posture is malformed.",
    "NON_CLAIM_ADDITIONAL_BASIS_REQUIRED": "The complete canonical non-claim set is required.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "Every mandatory non-claim must be present and exactly false.",
    "CANDIDATE_VERSION_OR_REFERENCE_REQUIRED": "Candidate version or immutable reference is incomplete.",
    "CANDIDATE_POSTURE_OVERREACH": "The candidate is not explicitly non-standing and non-current.",
    "CONTRACT_BINDING_MISMATCH": "EC does not bind exact C, CA, source family, scope, and declared use.",
    "CANDIDATE_BASIS_BINDING_MISMATCH": "CA is not exactly attributable to EC, its semantic owner, source family, C, and declared use.",
    "APPLICABILITY_EMISSION_BINDING_MISMATCH": "The applicability emission is not exactly attributable and bound to EC, CA, C, ownership, effect, scope, lineage, custody, and basis.",
    "APPLICABILITY_EMISSION_NOT_APPLICABLE": "The exact family-owned applicability result does not support this declared request-admission use.",
    "PROPOSITION_BINDING_MISMATCH": "P does not remain bound to exact M and its matter scope.",
    "BINDING_IDENTITY_MISMATCH": "B(C,P) does not directionally bind exact C, P, Q, and M.",
    "ENACTMENT_REQUEST_BINDING_MISMATCH": "Q does not bind exact M, C, P, B(C,P), X, S, I, K, L, and declared use.",
    "ENACTMENT_REQUEST_LANGUAGE_OVERREACH": "Q claims authorization, invocation, execution, occurrence, proposition judgment, standing, adoption, integration, or selection authority.",
    "REQUESTED_ENACTMENT_BINDING_MISMATCH": "X is not the exact request target bound by Q.",
    "REQUESTED_SCOPE_BINDING_MISMATCH": "S does not bind exact M, C, P, B(C,P), Q, X, I, K, L, and one-invocation scope.",
    "PROPOSED_INPUTS_BINDING_MISMATCH": "I does not bind exact M, Q, and X.",
    "PROPOSED_CONDITIONS_BINDING_MISMATCH": "K does not bind exact M, Q, and X.",
    "LOCALITY_BINDING_MISMATCH": "L does not bind exact M, Q, X, and S.",
    "LOCALITY_CONTRADICTS_SCOPE": "L is present when S excludes it or absent identifiers contradict S.",
    "SINGLE_INVOCATION_POSTURE_OVERREACH": "The request is not exactly one-shot or creates repeat, reuse, standing-lane, or automatic-successor posture.",
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
        "CANDIDATE_POSTURE_OVERREACH",
        "CONTRACT_BINDING_MISMATCH",
        "CANDIDATE_BASIS_BINDING_MISMATCH",
        "APPLICABILITY_EMISSION_BINDING_MISMATCH",
        "PROPOSITION_BINDING_MISMATCH",
        "BINDING_IDENTITY_MISMATCH",
        "ENACTMENT_REQUEST_BINDING_MISMATCH",
        "ENACTMENT_REQUEST_LANGUAGE_OVERREACH",
        "REQUESTED_ENACTMENT_BINDING_MISMATCH",
        "REQUESTED_SCOPE_BINDING_MISMATCH",
        "PROPOSED_INPUTS_BINDING_MISMATCH",
        "PROPOSED_CONDITIONS_BINDING_MISMATCH",
        "LOCALITY_BINDING_MISMATCH",
        "LOCALITY_CONTRADICTS_SCOPE",
        "SINGLE_INVOCATION_POSTURE_OVERREACH",
    }
)

NON_MEANING = (
    "candidate_enactment_request_admission_is_not_candidate_readmission",
    "request_admission_is_not_enactment_authorization",
    "enactment_authorization_is_not_invocation_permission",
    "invocation_permission_is_not_execution",
    "execution_is_not_occurrence_establishment",
    "candidate_is_not_represented_proposition",
    "candidate_proposition_binding_is_not_proposition_truth",
    "family_owned_applicability_is_not_candidate_standing",
    "request_completeness_is_not_candidate_merit",
    "admitted_request_is_not_scope_approval_or_enactment_authorization",
    "admitted_request_is_not_automatic_authorization_review",
)
OPEN_ITEMS = (
    "candidate_specific_enactment_authorization",
    "invocation_authorization_or_permission",
    "candidate_enactment_or_execution",
    "occurrence_establishment_or_evidence_allocation",
    "represented_proposition_evaluation",
    "candidate_adoption_or_integration",
    "runtime_sandbox_locality_or_deployment",
    "artifact_receipt_or_terminal_summary",
    "later_successor_work",
)

_FORBIDDEN_REQUEST_LANGUAGE = (
    "enactment is authorized",
    "enactment authorized",
    "authorizes enactment",
    "invocation is permitted",
    "invocation permitted",
    "execution occurred",
    "execution performed",
    "occurrence was established",
    "occurrence established",
    "output was created",
    "result was created",
    "trace was created",
    "success was established",
    "evidence adequacy was determined",
    "represented proposition is true",
    "represented proposition is false",
    "represented proposition stands",
    "represented proposition is standing",
    "candidate stands",
    "candidate is standing",
    "candidate is adopted",
    "candidate was adopted",
    "candidate is integrated",
    "candidate was integrated",
    "requested scope is approved",
    "latest candidate",
    "newest candidate",
    "most recent candidate",
    "repository presence selects",
    "directory order selects",
    "timestamp selects",
    "sequence number selects",
    "test success selects",
)


def resolve_matter_bound_candidate_enactment_request_admission_v0_min(
    request: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Resolve one exact candidate-enactment request-admission envelope."""

    checks: list[dict[str, Any]] = []
    normalized: dict[str, Any] = {
        key: None for key in REQUEST_KEYS if key != "declared_non_claims"
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

    section_definitions = (
        ("matter", MATTER_FIELDS, "MATTER", (), ()),
        (
            "candidate_configuration",
            CANDIDATE_FIELDS,
            "CANDIDATE",
            ("candidate_standing", "candidate_current"),
            ("candidate_version", "candidate_immutable_reference"),
        ),
        (
            "family_owned_candidate_contract",
            CONTRACT_FIELDS,
            "CONTRACT",
            (),
            ("candidate_contract_version",),
        ),
        (
            "family_owned_candidate_basis",
            CANDIDATE_BASIS_FIELDS,
            "CANDIDATE_BASIS",
            (
                "supporting_basis_references",
                "limitations",
                "candidate_basis_non_claims",
            ),
            ("candidate_basis_version",),
        ),
        (
            "family_owned_applicability_emission",
            APPLICABILITY_EMISSION_FIELDS,
            "APPLICABILITY_EMISSION",
            ("applicability_result",),
            (),
        ),
        (
            "represented_proposition",
            PROPOSITION_FIELDS,
            "PROPOSITION",
            (),
            (
                "represented_proposition_statement",
                "represented_proposition_immutable_reference",
            ),
        ),
        ("candidate_proposition_binding", BINDING_FIELDS, "BINDING", (), ()),
        (
            "candidate_enactment_request",
            ENACTMENT_REQUEST_FIELDS,
            "ENACTMENT_REQUEST",
            (),
            (
                "candidate_enactment_request_version",
                "requested_locality_or_destination_id",
            ),
        ),
        (
            "requested_enactment",
            REQUESTED_ENACTMENT_FIELDS,
            "REQUESTED_ENACTMENT",
            (),
            (),
        ),
        (
            "requested_enactment_scope",
            REQUESTED_SCOPE_FIELDS,
            "REQUESTED_SCOPE",
            ("requested_invocation_count", "locality_or_destination_required"),
            ("requested_locality_or_destination_id",),
        ),
        (
            "proposed_inputs",
            PROPOSED_INPUT_FIELDS,
            "PROPOSED_INPUTS",
            ("input_references",),
            (),
        ),
        (
            "proposed_conditions",
            PROPOSED_CONDITION_FIELDS,
            "PROPOSED_CONDITIONS",
            ("condition_references",),
            (),
        ),
        (
            "single_invocation_posture",
            SINGLE_INVOCATION_FIELDS,
            "SINGLE_INVOCATION",
            SINGLE_INVOCATION_FIELDS,
            (),
        ),
    )
    for section_name, fields, prefix, non_text, nullable in section_definitions:
        value, state = _normalize_fixed_mapping(
            request.get(section_name),
            fields,
            non_text_fields=frozenset(non_text),
            nullable_text_fields=frozenset(nullable),
        )
        if state == "missing":
            return stopped(
                f"{section_name}_is_complete",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                f"{prefix}_ADDITIONAL_BASIS_REQUIRED",
            )
        if state == "invalid":
            return stopped(
                f"{section_name}_is_exact",
                OUTCOME_REVIEW_BLOCKED,
                f"{prefix}_MALFORMED",
            )
        normalized[section_name] = value
        passed(f"{section_name}_is_exact")

    candidate = normalized["candidate_configuration"]
    candidate_basis = normalized["family_owned_candidate_basis"]
    applicability = normalized["family_owned_applicability_emission"]
    proposition = normalized["represented_proposition"]
    enactment_request = normalized["candidate_enactment_request"]
    requested_scope = normalized["requested_enactment_scope"]
    proposed_inputs = normalized["proposed_inputs"]
    proposed_conditions = normalized["proposed_conditions"]
    invocation_posture = normalized["single_invocation_posture"]

    for field, owner, prefix in (
        ("supporting_basis_references", candidate_basis, "CANDIDATE_BASIS"),
        ("limitations", candidate_basis, "CANDIDATE_BASIS"),
        ("input_references", proposed_inputs, "PROPOSED_INPUTS"),
        ("condition_references", proposed_conditions, "PROPOSED_CONDITIONS"),
    ):
        items, state = _normalize_text_list(owner[field])
        if state == "missing":
            return stopped(
                f"{field}_is_present",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                f"{prefix}_ADDITIONAL_BASIS_REQUIRED",
            )
        if state == "invalid":
            return stopped(
                f"{field}_is_exact", OUTCOME_REVIEW_BLOCKED, f"{prefix}_MALFORMED"
            )
        owner[field] = items

    basis_non_claims, state = _normalize_family_non_claims(
        candidate_basis["candidate_basis_non_claims"]
    )
    if state == "missing":
        return stopped(
            "candidate_basis_non_claims_are_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "CANDIDATE_BASIS_ADDITIONAL_BASIS_REQUIRED",
        )
    if state == "invalid":
        return stopped(
            "candidate_basis_non_claims_are_exact_false",
            OUTCOME_REVIEW_BLOCKED,
            "CANDIDATE_BASIS_MALFORMED",
        )
    candidate_basis["candidate_basis_non_claims"] = basis_non_claims

    if (
        type(candidate["candidate_standing"]) is not bool
        or type(candidate["candidate_current"]) is not bool
        or type(applicability["applicability_result"]) is not bool
        or not _exact_int(requested_scope["requested_invocation_count"])
        or type(requested_scope["locality_or_destination_required"]) is not bool
        or not _exact_int(invocation_posture["requested_invocation_count"])
        or any(
            type(invocation_posture[key]) is not bool
            for key in SINGLE_INVOCATION_FIELDS
            if key != "requested_invocation_count"
        )
    ):
        return stopped(
            "specialized_scalar_types_are_exact",
            OUTCOME_REVIEW_BLOCKED,
            "SINGLE_INVOCATION_MALFORMED",
        )
    passed("specialized_scalar_types_are_exact")

    locality_required = requested_scope["locality_or_destination_required"]
    locality_value = request.get("requested_locality_or_destination")
    if locality_value is None:
        if locality_required:
            return stopped(
                "required_locality_is_present",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "LOCALITY_ADDITIONAL_BASIS_REQUIRED",
            )
        if (
            enactment_request["requested_locality_or_destination_id"] is not None
            or requested_scope["requested_locality_or_destination_id"] is not None
        ):
            return stopped(
                "absent_locality_identifiers_are_coherent",
                OUTCOME_REVIEW_BLOCKED,
                "LOCALITY_CONTRADICTS_SCOPE",
            )
        normalized["requested_locality_or_destination"] = None
        passed("locality_is_exactly_absent_where_not_required")
    else:
        locality, state = _normalize_fixed_mapping(locality_value, LOCALITY_FIELDS)
        if state == "missing":
            return stopped(
                "requested_locality_or_destination_is_complete",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "LOCALITY_ADDITIONAL_BASIS_REQUIRED",
            )
        if state == "invalid":
            return stopped(
                "requested_locality_or_destination_is_exact",
                OUTCOME_REVIEW_BLOCKED,
                "LOCALITY_MALFORMED",
            )
        if not locality_required:
            return stopped(
                "locality_presence_matches_requested_scope",
                OUTCOME_REVIEW_BLOCKED,
                "LOCALITY_CONTRADICTS_SCOPE",
            )
        normalized["requested_locality_or_destination"] = locality
        passed("requested_locality_or_destination_is_exact")

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
    contract = normalized["family_owned_candidate_contract"]
    binding = normalized["candidate_proposition_binding"]
    requested_enactment = normalized["requested_enactment"]
    locality = normalized["requested_locality_or_destination"]

    if not (
        _has_text(candidate["candidate_version"])
        or _has_text(candidate["candidate_immutable_reference"])
    ):
        return stopped(
            "candidate_version_or_reference_is_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "CANDIDATE_VERSION_OR_REFERENCE_REQUIRED",
        )
    if candidate["candidate_standing"] is not False or candidate["candidate_current"] is not False:
        return stopped(
            "candidate_remains_non_standing_and_non_current",
            OUTCOME_REVIEW_BLOCKED,
            "CANDIDATE_POSTURE_OVERREACH",
        )
    passed("candidate_remains_exact_non_standing_and_non_current")

    declared_use = enactment_request["declared_request_admission_use"]
    if (
        contract["source_family"] != candidate["source_family"]
        or contract["candidate_id"] != candidate["candidate_id"]
        or contract["candidate_basis_id"] != candidate_basis["candidate_basis_id"]
        or contract["declared_request_admission_use"] != declared_use
    ):
        return stopped(
            "contract_binds_exact_candidate_basis_family_and_use",
            OUTCOME_REVIEW_BLOCKED,
            "CONTRACT_BINDING_MISMATCH",
        )
    passed("contract_binds_exact_candidate_basis_family_and_use")

    if (
        candidate_basis["candidate_contract_id"] != contract["candidate_contract_id"]
        or candidate_basis["candidate_contract_semantic_owner"]
        != contract["candidate_contract_semantic_owner"]
        or candidate_basis["source_family"] != candidate["source_family"]
        or candidate_basis["candidate_id"] != candidate["candidate_id"]
        or candidate_basis["declared_request_admission_use"] != declared_use
        or candidate_basis["candidate_basis_scope"] != contract["applicable_scope"]
    ):
        return stopped(
            "candidate_basis_is_exactly_attributable_and_bound",
            OUTCOME_REVIEW_BLOCKED,
            "CANDIDATE_BASIS_BINDING_MISMATCH",
        )
    passed("candidate_basis_is_exactly_attributable_and_bound")

    applicability_bindings = {
        "candidate_contract_id": contract["candidate_contract_id"],
        "candidate_contract_immutable_reference": contract[
            "candidate_contract_immutable_reference"
        ],
        "candidate_contract_semantic_owner": contract[
            "candidate_contract_semantic_owner"
        ],
        "source_family": candidate["source_family"],
        "candidate_basis_id": candidate_basis["candidate_basis_id"],
        "candidate_id": candidate["candidate_id"],
        "candidate_effect_location": contract["candidate_effect_location"],
        "declared_request_admission_use": declared_use,
        "applicable_scope": contract["applicable_scope"],
        "lineage_reference": candidate_basis["lineage_reference"],
        "custody_reference": candidate_basis["custody_reference"],
    }
    if (
        any(applicability[key] != value for key, value in applicability_bindings.items())
        or applicability["applicability_basis_reference"]
        not in candidate_basis["supporting_basis_references"]
    ):
        return stopped(
            "family_owned_applicability_emission_is_exactly_attributable_and_bound",
            OUTCOME_REVIEW_BLOCKED,
            "APPLICABILITY_EMISSION_BINDING_MISMATCH",
        )
    passed("family_owned_applicability_emission_is_exactly_attributable_and_bound")

    if (
        proposition["matter_id"] != matter["matter_id"]
        or proposition["matter_scope"] != matter["matter_scope"]
        or not (
            _has_text(proposition["represented_proposition_statement"])
            or _has_text(proposition["represented_proposition_immutable_reference"])
        )
    ):
        return stopped(
            "represented_proposition_binds_exact_matter",
            OUTCOME_REVIEW_BLOCKED,
            "PROPOSITION_BINDING_MISMATCH",
        )
    passed("represented_proposition_binds_exact_matter")

    if (
        binding["candidate_proposition_binding_direction"]
        != REQUIRED_BINDING_DIRECTION
        or binding["matter_id"] != matter["matter_id"]
        or binding["candidate_id"] != candidate["candidate_id"]
        or binding["represented_proposition_id"]
        != proposition["represented_proposition_id"]
        or binding["candidate_enactment_request_id"]
        != enactment_request["candidate_enactment_request_id"]
    ):
        return stopped(
            "binding_names_exact_candidate_proposition_request_and_matter",
            OUTCOME_REVIEW_BLOCKED,
            "BINDING_IDENTITY_MISMATCH",
        )
    passed("binding_names_exact_candidate_proposition_request_and_matter")

    expected_request_bindings = {
        "matter_id": matter["matter_id"],
        "candidate_id": candidate["candidate_id"],
        "represented_proposition_id": proposition["represented_proposition_id"],
        "candidate_proposition_binding_id": binding[
            "candidate_proposition_binding_id"
        ],
        "requested_enactment_id": requested_enactment["requested_enactment_id"],
        "requested_enactment_scope_id": requested_scope[
            "requested_enactment_scope_id"
        ],
        "proposed_input_set_id": proposed_inputs["proposed_input_set_id"],
        "proposed_condition_set_id": proposed_conditions[
            "proposed_condition_set_id"
        ],
    }
    locality_id = (
        None if locality is None else locality["requested_locality_or_destination_id"]
    )
    if (
        any(enactment_request[key] != value for key, value in expected_request_bindings.items())
        or enactment_request["requested_locality_or_destination_id"] != locality_id
        or enactment_request["candidate_enactment_request_type"]
        != "CANDIDATE_ENACTMENT_REQUEST"
        or enactment_request["request_admission_only_statement"]
        != REQUEST_ADMISSION_ONLY_STATEMENT
        or enactment_request[
            "request_admission_does_not_authorize_or_perform_statement"
        ]
        != REQUEST_DOES_NOT_AUTHORIZE_OR_PERFORM_STATEMENT
    ):
        return stopped(
            "candidate_enactment_request_binds_exact_envelope_and_remains_request_only",
            OUTCOME_REVIEW_BLOCKED,
            "ENACTMENT_REQUEST_BINDING_MISMATCH",
        )
    request_language = " ".join(
        str(enactment_request[key]).casefold()
        for key in ("request_purpose", "request_scope", "outside_boundary")
    )
    if any(fragment in request_language for fragment in _FORBIDDEN_REQUEST_LANGUAGE):
        return stopped(
            "candidate_enactment_request_contains_no_overreach_claim",
            OUTCOME_REVIEW_BLOCKED,
            "ENACTMENT_REQUEST_LANGUAGE_OVERREACH",
        )
    passed("candidate_enactment_request_binds_exact_envelope_and_remains_request_only")

    expected_enactment_bindings = {
        "matter_id": matter["matter_id"],
        "candidate_id": candidate["candidate_id"],
        "represented_proposition_id": proposition["represented_proposition_id"],
        "candidate_proposition_binding_id": binding[
            "candidate_proposition_binding_id"
        ],
        "candidate_enactment_request_id": enactment_request[
            "candidate_enactment_request_id"
        ],
        "requested_enactment_scope_id": requested_scope[
            "requested_enactment_scope_id"
        ],
    }
    if any(
        requested_enactment[key] != value
        for key, value in expected_enactment_bindings.items()
    ):
        return stopped(
            "requested_enactment_is_exact_request_target",
            OUTCOME_REVIEW_BLOCKED,
            "REQUESTED_ENACTMENT_BINDING_MISMATCH",
        )
    passed("requested_enactment_is_exact_request_target_only")

    expected_scope_bindings = {
        "matter_id": matter["matter_id"],
        "candidate_id": candidate["candidate_id"],
        "represented_proposition_id": proposition["represented_proposition_id"],
        "candidate_proposition_binding_id": binding[
            "candidate_proposition_binding_id"
        ],
        "candidate_enactment_request_id": enactment_request[
            "candidate_enactment_request_id"
        ],
        "requested_enactment_id": requested_enactment["requested_enactment_id"],
        "proposed_input_set_id": proposed_inputs["proposed_input_set_id"],
        "proposed_condition_set_id": proposed_conditions[
            "proposed_condition_set_id"
        ],
        "requested_locality_or_destination_id": locality_id,
    }
    if any(requested_scope[key] != value for key, value in expected_scope_bindings.items()):
        return stopped(
            "requested_scope_binds_exact_envelope",
            OUTCOME_REVIEW_BLOCKED,
            "REQUESTED_SCOPE_BINDING_MISMATCH",
        )
    passed("requested_scope_binds_exact_envelope")

    for section, id_key, expected_id, code in (
        (
            proposed_inputs,
            "proposed_input_set_id",
            enactment_request["proposed_input_set_id"],
            "PROPOSED_INPUTS_BINDING_MISMATCH",
        ),
        (
            proposed_conditions,
            "proposed_condition_set_id",
            enactment_request["proposed_condition_set_id"],
            "PROPOSED_CONDITIONS_BINDING_MISMATCH",
        ),
    ):
        if (
            section[id_key] != expected_id
            or section["matter_id"] != matter["matter_id"]
            or section["candidate_enactment_request_id"]
            != enactment_request["candidate_enactment_request_id"]
            or section["requested_enactment_id"]
            != requested_enactment["requested_enactment_id"]
        ):
            return stopped(
                f"{id_key}_binds_exact_request_and_enactment",
                OUTCOME_REVIEW_BLOCKED,
                code,
            )
    passed("proposed_inputs_and_conditions_bind_exact_request_and_enactment")

    if locality is not None and (
        locality["matter_id"] != matter["matter_id"]
        or locality["candidate_enactment_request_id"]
        != enactment_request["candidate_enactment_request_id"]
        or locality["requested_enactment_id"]
        != requested_enactment["requested_enactment_id"]
        or locality["requested_enactment_scope_id"]
        != requested_scope["requested_enactment_scope_id"]
    ):
        return stopped(
            "locality_binds_exact_request_enactment_and_scope",
            OUTCOME_REVIEW_BLOCKED,
            "LOCALITY_BINDING_MISMATCH",
        )
    passed("locality_posture_is_coherent_and_creates_no_runtime_or_deployment")

    if (
        requested_scope["requested_invocation_count"] != 1
        or invocation_posture["requested_invocation_count"] != 1
        or invocation_posture["no_repeat_posture"] is not True
        or invocation_posture["no_reuse_posture"] is not True
        or invocation_posture["no_standing_invocation_lane_posture"] is not True
        or invocation_posture["no_automatic_successor_posture"] is not True
    ):
        return stopped(
            "request_is_exactly_one_shot_without_successor_force",
            OUTCOME_REVIEW_BLOCKED,
            "SINGLE_INVOCATION_POSTURE_OVERREACH",
        )
    passed("request_is_exactly_one_shot_without_repeat_reuse_lane_or_successor")
    passed("family_owned_applicability_consumed_without_raw_contract_interpretation")

    if applicability["applicability_result"] is False:
        return stopped(
            "family_owned_applicability_supports_exact_declared_use",
            OUTCOME_NOT_ADMITTED,
            "APPLICABILITY_EMISSION_NOT_APPLICABLE",
        )
    passed("family_owned_applicability_supports_exact_declared_use")

    return _build_result(
        outcome=OUTCOME_ADMITTED,
        normalized=normalized,
        checks=checks,
        stopping_code=None,
    )


def _normalize_fixed_mapping(
    value: Any,
    fields: tuple[str, ...],
    *,
    non_text_fields: frozenset[str] = frozenset(),
    nullable_text_fields: frozenset[str] = frozenset(),
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
    for field in fields:
        item = value[field]
        if field in non_text_fields:
            normalized[field] = item
        elif field in nullable_text_fields and item is None:
            normalized[field] = None
        elif item is None or item == "":
            return None, "missing"
        elif not _has_text(item):
            return None, "invalid"
        else:
            normalized[field] = str(item)
    return normalized, None


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


def _normalize_family_non_claims(
    value: Any,
) -> tuple[dict[str, bool] | None, str | None]:
    if value is None or value == {}:
        return None, "missing"
    if not isinstance(value, Mapping):
        return None, "invalid"
    if any(not _has_text(key) or item is not False for key, item in value.items()):
        return None, "invalid"
    return {str(key): False for key in sorted(value)}, None


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
    request = normalized.get("candidate_enactment_request")
    candidate = normalized.get("candidate_configuration")
    admitted = outcome == OUTCOME_ADMITTED
    request_id = (
        request.get("candidate_enactment_request_id")
        if isinstance(request, Mapping)
        else None
    )
    candidate_id = (
        candidate.get("candidate_id") if isinstance(candidate, Mapping) else None
    )

    return {
        "metadata": {
            "matter_bound_candidate_enactment_request_admission_type": REQUEST_ADMISSION_TYPE,
            "matter_bound_candidate_enactment_request_admission_version": REQUEST_ADMISSION_VERSION,
            "matter_bound_candidate_enactment_request_admission_scope": REQUEST_ADMISSION_SCOPE,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
        },
        **{
            key: _copy_normalized(value)
            for key, value in normalized.items()
            if key != "declared_non_claims"
        },
        "request_admission_decision": {
            "decision_outcome": outcome,
            "candidate_enactment_request_admitted": admitted,
            "admitted_object_type": "CANDIDATE_ENACTMENT_REQUEST" if admitted else None,
            "admitted_object_id": request_id if admitted else None,
            "candidate_enactment_request_id": request_id,
            "candidate_id": candidate_id,
            "candidate_admitted_or_readmitted": False,
            "candidate_standing_created": False,
            "candidate_currentness_created": False,
            "requested_scope_approved": False,
            "requested_enactment_authorized": False,
            "represented_proposition_evaluated": False,
            "request_envelope_singular": admitted,
            "request_scope_bounded": admitted,
            "requested_invocation_count_is_one": admitted,
            "family_owned_candidate_basis_preserved": admitted,
            "candidate_proposition_binding_preserved": admitted,
            "separate_enactment_authorization_review_required": admitted,
            "result_level_non_claims_canonical_false": True,
        },
        "checks": [dict(check) for check in checks],
        "result": {
            "outcome": outcome,
            "completion_posture": outcome,
            "lawful_terminal_outcome_recorded": True,
            "candidate_enactment_request_admitted": admitted,
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
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "OUTCOMES",
    "OUTCOME_ADMITTED",
    "OUTCOME_NOT_ADMITTED",
    "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
    "OUTCOME_REVIEW_BLOCKED",
    "REQUEST_ADMISSION_ONLY_STATEMENT",
    "REQUEST_ADMISSION_SCOPE",
    "REQUEST_ADMISSION_TYPE",
    "REQUEST_ADMISSION_VERSION",
    "REQUEST_DOES_NOT_AUTHORIZE_OR_PERFORM_STATEMENT",
    "REQUIRED_BINDING_DIRECTION",
    "REQUIRED_FALSE_NON_CLAIMS",
    "RESOLVER_MODULE",
    "RESULT_VERSION",
    "STOP_CODES",
    "resolve_matter_bound_candidate_enactment_request_admission_v0_min",
]
