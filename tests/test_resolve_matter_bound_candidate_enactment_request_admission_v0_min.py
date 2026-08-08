"""Adversarial tests for bounded candidate-enactment request admission.

The suite supplies one closed M/C/EC/CA/P/B(C,P)/Q/X/S/I/K/L envelope.
Applicability is carried only by one exact attributable family-owned emission;
raw contract prose, CA labels, naked booleans, paths, recency, and test success
cannot substitute for that emission. Q is the only admitted object.
"""

from __future__ import annotations

import builtins
import copy
import inspect
import json
import sys
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_matter_bound_candidate_enactment_request_admission_v0_min as resolver


EXPECTED_NON_CLAIMS = {
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
}


def _declared_non_claims() -> dict[str, bool]:
    return {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS}


def _request(*, applicable: bool = True) -> dict[str, object]:
    matter_scope = "matter-001 candidate-enactment request admission only"
    application_scope = "matter-001 candidate-001 request-admission-use-001 only"
    return {
        "matter": {
            "matter_id": "matter-001",
            "matter_type": "BOUNDED_CANDIDATE_ENACTMENT_REQUEST_MATTER",
            "matter_purpose": "Review one exact candidate-enactment request.",
            "matter_scope": matter_scope,
            "request_admission_question": (
                "May request-001 become a candidate for a later separate review?"
            ),
            "outside_boundary": "No effect beyond request admission review.",
        },
        "candidate_configuration": {
            "candidate_id": "candidate-001",
            "candidate_type": "BOUNDED_CANDIDATE_CONFIGURATION",
            "source_family": "candidate-family-001",
            "custody_reference": "custody/candidate-001",
            "lineage_reference": "lineage/candidate-001",
            "candidate_version": "0.1.0",
            "candidate_immutable_reference": "supplied/candidate-001.json",
            "candidate_content_identity": "sha256:candidate-001",
            "candidate_standing": False,
            "candidate_current": False,
        },
        "family_owned_candidate_contract": {
            "candidate_contract_id": "contract-001",
            "candidate_contract_type": "FAMILY_OWNED_CANDIDATE_CONTRACT",
            "candidate_contract_version": "0.1.0",
            "candidate_contract_immutable_reference": "supplied/contract-001.json",
            "candidate_contract_semantic_owner": "candidate-family-owner-001",
            "source_family": "candidate-family-001",
            "applicable_scope": application_scope,
            "candidate_effect_location": "contract-001#candidate-effect-001",
            "declared_use_applicability_rule_reference": (
                "contract-001#request-admission-use-rule-001"
            ),
            "candidate_id": "candidate-001",
            "candidate_basis_id": "candidate-basis-001",
            "declared_request_admission_use": "request-admission-use-001",
        },
        "family_owned_candidate_basis": {
            "candidate_basis_id": "candidate-basis-001",
            "candidate_basis_type": "FAMILY_OWNED_CANDIDATE_BASIS",
            "candidate_basis_version": "0.1.0",
            "candidate_basis_immutable_reference": (
                "supplied/candidate-basis-001.json"
            ),
            "recorded_contract_owned_posture": "FAMILY_LOCAL_RECORDED_POSTURE",
            "supporting_basis_references": [
                "supplied/candidate-basis-001.json#basis-001"
            ],
            "lineage_reference": "lineage/candidate-basis-001",
            "custody_reference": "custody/candidate-basis-001",
            "candidate_basis_scope": application_scope,
            "limitations": ["Exact declared request-admission use only."],
            "candidate_basis_non_claims": {
                "candidate_standing_created": False,
                "enactment_authorization_created": False,
            },
            "candidate_contract_id": "contract-001",
            "candidate_contract_semantic_owner": "candidate-family-owner-001",
            "source_family": "candidate-family-001",
            "candidate_id": "candidate-001",
            "declared_request_admission_use": "request-admission-use-001",
        },
        "family_owned_applicability_emission": {
            "applicability_emission_id": "applicability-emission-001",
            "applicability_emission_type": (
                "EC_OWNED_CA_CARRIED_REQUEST_ADMISSION_APPLICABILITY"
            ),
            "applicability_emission_immutable_reference": (
                "supplied/candidate-basis-001.json#applicability-emission-001"
            ),
            "candidate_contract_id": "contract-001",
            "candidate_contract_immutable_reference": "supplied/contract-001.json",
            "candidate_contract_semantic_owner": "candidate-family-owner-001",
            "source_family": "candidate-family-001",
            "candidate_basis_id": "candidate-basis-001",
            "candidate_id": "candidate-001",
            "candidate_effect_location": "contract-001#candidate-effect-001",
            "declared_request_admission_use": "request-admission-use-001",
            "applicable_scope": application_scope,
            "lineage_reference": "lineage/candidate-basis-001",
            "custody_reference": "custody/candidate-basis-001",
            "applicability_result": applicable,
            "applicability_basis_reference": (
                "supplied/candidate-basis-001.json#basis-001"
            ),
        },
        "represented_proposition": {
            "represented_proposition_id": "proposition-001",
            "represented_proposition_type": "BOUNDED_REPRESENTED_PROPOSITION",
            "represented_proposition_statement": (
                "The exact represented condition has the declared posture."
            ),
            "represented_proposition_immutable_reference": (
                "supplied/proposition-001.json"
            ),
            "represented_proposition_semantic_owner": "proposition-owner-001",
            "matter_id": "matter-001",
            "matter_scope": matter_scope,
            "outside_boundary": "No proposition evaluation in this boundary.",
        },
        "candidate_proposition_binding": {
            "candidate_proposition_binding_id": "binding-001",
            "candidate_proposition_binding_type": (
                "EXACT_CANDIDATE_TO_REPRESENTED_PROPOSITION_BINDING"
            ),
            "candidate_proposition_binding_direction": (
                resolver.REQUIRED_BINDING_DIRECTION
            ),
            "candidate_proposition_binding_scope": (
                "matter-001 request-001 representation only"
            ),
            "matter_id": "matter-001",
            "candidate_id": "candidate-001",
            "represented_proposition_id": "proposition-001",
            "candidate_enactment_request_id": "request-001",
        },
        "candidate_enactment_request": {
            "candidate_enactment_request_id": "request-001",
            "candidate_enactment_request_type": "CANDIDATE_ENACTMENT_REQUEST",
            "candidate_enactment_request_version": "0.1.0",
            "candidate_enactment_request_immutable_reference": (
                "supplied/request-001.json"
            ),
            "matter_id": "matter-001",
            "candidate_id": "candidate-001",
            "represented_proposition_id": "proposition-001",
            "candidate_proposition_binding_id": "binding-001",
            "requested_enactment_id": "enactment-001",
            "requested_enactment_scope_id": "scope-001",
            "proposed_input_set_id": "inputs-001",
            "proposed_condition_set_id": "conditions-001",
            "requested_locality_or_destination_id": "locality-001",
            "declared_request_admission_use": "request-admission-use-001",
            "request_purpose": "Review one exact request envelope.",
            "request_scope": "request-001 and enactment-001 proposal only.",
            "outside_boundary": "No effect beyond this bounded review.",
            "request_admission_only_statement": (
                resolver.REQUEST_ADMISSION_ONLY_STATEMENT
            ),
            "request_admission_does_not_authorize_or_perform_statement": (
                resolver.REQUEST_DOES_NOT_AUTHORIZE_OR_PERFORM_STATEMENT
            ),
        },
        "requested_enactment": {
            "requested_enactment_id": "enactment-001",
            "requested_enactment_type": "BOUNDED_CANDIDATE_ENACTMENT",
            "matter_id": "matter-001",
            "candidate_id": "candidate-001",
            "represented_proposition_id": "proposition-001",
            "candidate_proposition_binding_id": "binding-001",
            "candidate_enactment_request_id": "request-001",
            "requested_enactment_scope_id": "scope-001",
        },
        "requested_enactment_scope": {
            "requested_enactment_scope_id": "scope-001",
            "matter_id": "matter-001",
            "candidate_id": "candidate-001",
            "represented_proposition_id": "proposition-001",
            "candidate_proposition_binding_id": "binding-001",
            "candidate_enactment_request_id": "request-001",
            "requested_enactment_id": "enactment-001",
            "proposed_input_set_id": "inputs-001",
            "proposed_condition_set_id": "conditions-001",
            "requested_locality_or_destination_id": "locality-001",
            "requested_invocation_count": 1,
            "maximum_requested_effect": "One bounded proposed enactment only.",
            "outside_boundary": "No effect outside scope-001.",
            "locality_or_destination_required": True,
        },
        "proposed_inputs": {
            "proposed_input_set_id": "inputs-001",
            "matter_id": "matter-001",
            "candidate_enactment_request_id": "request-001",
            "requested_enactment_id": "enactment-001",
            "input_references": ["supplied/input-001.json"],
        },
        "proposed_conditions": {
            "proposed_condition_set_id": "conditions-001",
            "matter_id": "matter-001",
            "candidate_enactment_request_id": "request-001",
            "requested_enactment_id": "enactment-001",
            "condition_references": ["supplied/condition-001.json"],
        },
        "requested_locality_or_destination": {
            "requested_locality_or_destination_id": "locality-001",
            "requested_locality_or_destination_type": "BOUNDED_LOCALITY_REFERENCE",
            "requested_locality_or_destination_reference": (
                "supplied/locality-001.json"
            ),
            "matter_id": "matter-001",
            "candidate_enactment_request_id": "request-001",
            "requested_enactment_id": "enactment-001",
            "requested_enactment_scope_id": "scope-001",
        },
        "single_invocation_posture": {
            "requested_invocation_count": 1,
            "no_repeat_posture": True,
            "no_reuse_posture": True,
            "no_standing_invocation_lane_posture": True,
            "no_automatic_successor_posture": True,
        },
        "declared_non_claims": _declared_non_claims(),
    }


def _resolve(request: object) -> dict[str, object]:
    return resolver.resolve_matter_bound_candidate_enactment_request_admission_v0_min(
        request  # type: ignore[arg-type]
    )


class MatterBoundCandidateEnactmentRequestAdmissionTests(unittest.TestCase):
    def assertCanonicalNonClaims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(EXPECTED_NON_CLAIMS, set(non_claims))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims[key], False)

    def assertOutcome(self, result: dict[str, object], outcome: str) -> None:
        self.assertEqual(outcome, result["outcome"])
        self.assertIn(result["outcome"], resolver.OUTCOMES)
        self.assertIs(result["result"]["lawful_terminal_outcome_recorded"], True)
        self.assertCanonicalNonClaims(result)

    def assertStopped(self, result: dict[str, object]) -> None:
        self.assertNotEqual(resolver.OUTCOME_ADMITTED, result["outcome"])
        self.assertOutcome(result, result["outcome"])

    def test_public_contract_and_complete_mandatory_non_claim_set(self) -> None:
        self.assertEqual("0.1.0", resolver.RESULT_VERSION)
        self.assertEqual(
            "resolve_matter_bound_candidate_enactment_request_admission_v0_min",
            resolver.RESOLVER_MODULE,
        )
        self.assertEqual(
            "MATTER_BOUND_CANDIDATE_ENACTMENT_REQUEST_ADMISSION",
            resolver.REQUEST_ADMISSION_TYPE,
        )
        self.assertEqual("0.1.0", resolver.REQUEST_ADMISSION_VERSION)
        self.assertEqual(
            "ONE_EXACT_MATTER_ONE_EXACT_CANDIDATE_ONE_EXACT_REPRESENTED_"
            "PROPOSITION_ONE_EXACT_SINGLE_ENACTMENT_REQUEST_ONLY",
            resolver.REQUEST_ADMISSION_SCOPE,
        )
        self.assertEqual(EXPECTED_NON_CLAIMS, set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertEqual(
            {
                "CANDIDATE_ENACTMENT_REQUEST_ADMITTED",
                "CANDIDATE_ENACTMENT_REQUEST_NOT_ADMITTED",
                "CANDIDATE_ENACTMENT_REQUEST_REQUIRES_ADDITIONAL_BASIS",
                "CANDIDATE_ENACTMENT_REQUEST_REVIEW_BLOCKED",
            },
            set(resolver.OUTCOMES),
        )
        self.assertFalse(any(name.startswith("write_") for name in resolver.__all__))
        self.assertFalse(any(name.endswith("_from_path") for name in resolver.__all__))

    def test_complete_exact_positive_emission_admits_q_only(self) -> None:
        result = _resolve(_request())
        self.assertOutcome(result, resolver.OUTCOME_ADMITTED)
        decision = result["request_admission_decision"]
        self.assertEqual("CANDIDATE_ENACTMENT_REQUEST", decision["admitted_object_type"])
        self.assertEqual("request-001", decision["admitted_object_id"])
        self.assertIs(decision["candidate_enactment_request_admitted"], True)
        self.assertIs(decision["candidate_admitted_or_readmitted"], False)
        self.assertIs(decision["candidate_standing_created"], False)
        self.assertIs(decision["candidate_currentness_created"], False)
        self.assertIs(decision["requested_scope_approved"], False)
        self.assertIs(decision["requested_enactment_authorized"], False)
        self.assertIs(decision["represented_proposition_evaluated"], False)
        for key in (
            "request_envelope_singular",
            "request_scope_bounded",
            "requested_invocation_count_is_one",
            "family_owned_candidate_basis_preserved",
            "candidate_proposition_binding_preserved",
            "separate_enactment_authorization_review_required",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(decision[key], True)

    def test_admitted_creates_none_of_the_forbidden_downstream_postures(self) -> None:
        result = _resolve(_request())
        self.assertOutcome(result, resolver.OUTCOME_ADMITTED)
        for key in (
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
            "candidate_adopted",
            "candidate_integrated",
            "repeat_permission_created",
            "reusable_permission_created",
            "continuation_permission_created",
            "successor_force_created",
            "runtime_hosting_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(result["non_claims"][key], False)

    def test_every_required_topology_unit_is_singular_and_required(self) -> None:
        sections = (
            "matter",
            "candidate_configuration",
            "family_owned_candidate_contract",
            "family_owned_candidate_basis",
            "represented_proposition",
            "candidate_proposition_binding",
            "candidate_enactment_request",
            "requested_enactment",
            "requested_enactment_scope",
            "proposed_inputs",
            "proposed_conditions",
            "single_invocation_posture",
        )
        for section in sections:
            with self.subTest(missing=section):
                request = _request()
                del request[section]
                self.assertOutcome(
                    _resolve(request), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
                )
            with self.subTest(multiple=section):
                request = _request()
                request[section] = [request[section], copy.deepcopy(request[section])]
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_matter_candidate_and_source_family_bindings_fail_closed(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for section, key, value in (
            ("represented_proposition", "matter_id", "other-matter"),
            ("candidate_proposition_binding", "matter_id", "other-matter"),
            ("candidate_enactment_request", "matter_id", "other-matter"),
            ("requested_enactment", "matter_id", "other-matter"),
            ("family_owned_candidate_contract", "source_family", "other-family"),
            ("family_owned_candidate_contract", "candidate_id", "other-candidate"),
            ("family_owned_candidate_basis", "source_family", "other-family"),
            ("family_owned_candidate_basis", "candidate_id", "other-candidate"),
        ):
            request = _request()
            request[section][key] = value
            cases.append((f"{section}.{key}", request))
        for key in ("candidate_standing", "candidate_current"):
            request = _request()
            request["candidate_configuration"][key] = True
            cases.append((key, request))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_ec_and_ca_require_exact_owner_effect_rule_basis_lineage_custody_scope(self) -> None:
        missing_fields = (
            ("family_owned_candidate_contract", "candidate_contract_semantic_owner"),
            ("family_owned_candidate_contract", "source_family"),
            ("family_owned_candidate_contract", "candidate_effect_location"),
            (
                "family_owned_candidate_contract",
                "declared_use_applicability_rule_reference",
            ),
            ("family_owned_candidate_basis", "supporting_basis_references"),
            ("family_owned_candidate_basis", "lineage_reference"),
            ("family_owned_candidate_basis", "custody_reference"),
            ("family_owned_candidate_basis", "candidate_basis_scope"),
            ("family_owned_candidate_basis", "limitations"),
            ("family_owned_candidate_basis", "candidate_basis_non_claims"),
        )
        for section, key in missing_fields:
            with self.subTest(missing=f"{section}.{key}"):
                request = _request()
                del request[section][key]
                self.assertOutcome(
                    _resolve(request), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
                )

        for section, key, value in (
            ("family_owned_candidate_basis", "candidate_contract_id", "other"),
            (
                "family_owned_candidate_basis",
                "candidate_contract_semantic_owner",
                "caller-owner",
            ),
            ("family_owned_candidate_basis", "candidate_basis_scope", "other"),
            (
                "family_owned_candidate_basis",
                "declared_request_admission_use",
                "other-use",
            ),
        ):
            with self.subTest(mismatch=f"{section}.{key}"):
                request = _request()
                request[section][key] = value
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_materialized_family_owned_applicability_emission_is_decisive(self) -> None:
        missing = _request()
        del missing["family_owned_applicability_emission"]
        self.assertOutcome(
            _resolve(missing), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
        )

        incomplete = _request()
        del incomplete["family_owned_applicability_emission"][
            "applicability_basis_reference"
        ]
        self.assertOutcome(
            _resolve(incomplete), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
        )

        mismatches = (
            ("candidate_contract_id", "other-contract"),
            ("candidate_basis_id", "other-basis"),
            ("candidate_id", "other-candidate"),
            ("source_family", "other-family"),
            ("candidate_contract_semantic_owner", "other-owner"),
            ("candidate_effect_location", "other-effect"),
            ("declared_request_admission_use", "other-use"),
            ("applicable_scope", "outside-exact-scope"),
            ("lineage_reference", "other-lineage"),
            ("custody_reference", "other-custody"),
            ("applicability_basis_reference", "other-basis-reference"),
        )
        for key, value in mismatches:
            with self.subTest(mismatch=key):
                request = _request()
                request["family_owned_applicability_emission"][key] = value
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_exact_family_owned_negative_applicability_is_lawful_not_admitted(self) -> None:
        result = _resolve(_request(applicable=False))
        self.assertOutcome(result, resolver.OUTCOME_NOT_ADMITTED)
        self.assertEqual(
            "APPLICABILITY_EMISSION_NOT_APPLICABLE",
            result["result"]["stopping_code"],
        )
        self.assertIsNone(result["block"]["code"])
        self.assertEqual("candidate-001", result["candidate_configuration"]["candidate_id"])
        self.assertEqual("contract-001", result["family_owned_candidate_contract"][
            "candidate_contract_id"
        ])
        self.assertEqual("candidate-basis-001", result["family_owned_candidate_basis"][
            "candidate_basis_id"
        ])
        self.assertEqual("proposition-001", result["represented_proposition"][
            "represented_proposition_id"
        ])
        self.assertEqual("request-001", result["candidate_enactment_request"][
            "candidate_enactment_request_id"
        ])

    def test_no_naked_boolean_label_prose_or_repository_signal_can_substitute(self) -> None:
        substitutes = (
            ("supports_declared_use", True),
            ("candidate_outcome", "FAMILY_LOCAL_RECORDED_POSTURE"),
            ("raw_candidate_contract_prose", "This basis supports use."),
            ("candidate_file_exists", True),
            ("candidate_timestamp", "2099-01-01T00:00:00Z"),
            ("candidate_sequence", 9),
            ("candidate_test_success", True),
            ("latest_candidate_selected", True),
        )
        for key, value in substitutes:
            with self.subTest(substitute=key):
                request = _request()
                del request["family_owned_applicability_emission"]
                request[key] = value
                result = _resolve(request)
                self.assertOutcome(result, resolver.OUTCOME_REVIEW_BLOCKED)
                self.assertEqual("REQUEST_KEYS_INVALID", result["block"]["code"])

        raw_ca_only = _request()
        del raw_ca_only["family_owned_applicability_emission"]
        raw_ca_only["family_owned_candidate_basis"][
            "recorded_contract_owned_posture"
        ] = "UNEXPLAINED_FAMILY_OUTCOME"
        self.assertOutcome(
            _resolve(raw_ca_only), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
        )

    def test_proposition_and_directional_binding_must_be_exact(self) -> None:
        cases = (
            ("represented_proposition", "matter_scope", "other-scope"),
            ("candidate_proposition_binding", "candidate_id", "other-candidate"),
            (
                "candidate_proposition_binding",
                "represented_proposition_id",
                "other-proposition",
            ),
            (
                "candidate_proposition_binding",
                "candidate_enactment_request_id",
                "other-request",
            ),
            (
                "candidate_proposition_binding",
                "candidate_proposition_binding_direction",
                "REPRESENTED_PROPOSITION_TO_CANDIDATE",
            ),
        )
        for section, key, value in cases:
            with self.subTest(case=f"{section}.{key}"):
                request = _request()
                request[section][key] = value
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

        no_p_identity = _request()
        no_p_identity["represented_proposition"][
            "represented_proposition_statement"
        ] = None
        no_p_identity["represented_proposition"][
            "represented_proposition_immutable_reference"
        ] = None
        self.assertOutcome(_resolve(no_p_identity), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_q_language_cannot_claim_later_authority_or_semantic_result(self) -> None:
        forbidden_claims = (
            "Enactment is authorized.",
            "Invocation is permitted.",
            "Execution occurred.",
            "Occurrence was established.",
            "Output was created.",
            "Success was established.",
            "Evidence adequacy was determined.",
            "Represented proposition is true.",
            "Represented proposition is false.",
            "Candidate stands.",
            "Candidate is adopted.",
            "Candidate is integrated.",
            "Requested scope is approved.",
        )
        for claim in forbidden_claims:
            with self.subTest(claim=claim):
                request = _request()
                request["candidate_enactment_request"]["request_purpose"] = claim
                result = _resolve(request)
                self.assertOutcome(result, resolver.OUTCOME_REVIEW_BLOCKED)
                self.assertEqual(
                    "ENACTMENT_REQUEST_LANGUAGE_OVERREACH", result["block"]["code"]
                )

        wrong_statement = _request()
        wrong_statement["candidate_enactment_request"][
            "request_admission_only_statement"
        ] = "PLEASE AUTHORIZE THE REQUEST"
        self.assertOutcome(_resolve(wrong_statement), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_x_s_i_k_and_l_bind_exactly_without_approval_or_runtime(self) -> None:
        cases = (
            ("requested_enactment", "candidate_id", "other-candidate"),
            ("requested_enactment", "requested_enactment_scope_id", "other-scope"),
            ("requested_enactment_scope", "requested_enactment_id", "other"),
            ("requested_enactment_scope", "proposed_input_set_id", "other"),
            ("requested_enactment_scope", "proposed_condition_set_id", "other"),
            ("proposed_inputs", "matter_id", "other-matter"),
            ("proposed_inputs", "requested_enactment_id", "other-enactment"),
            ("proposed_conditions", "candidate_enactment_request_id", "other-request"),
            (
                "requested_locality_or_destination",
                "requested_enactment_scope_id",
                "other-scope",
            ),
        )
        for section, key, value in cases:
            with self.subTest(case=f"{section}.{key}"):
                request = _request()
                request[section][key] = value
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

        missing_required_locality = _request()
        missing_required_locality["requested_locality_or_destination"] = None
        self.assertOutcome(
            _resolve(missing_required_locality),
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        )

        locality_not_allowed = _request()
        locality_not_allowed["requested_enactment_scope"][
            "locality_or_destination_required"
        ] = False
        self.assertOutcome(_resolve(locality_not_allowed), resolver.OUTCOME_REVIEW_BLOCKED)

        no_locality = _request()
        no_locality["requested_enactment_scope"][
            "locality_or_destination_required"
        ] = False
        no_locality["requested_enactment_scope"][
            "requested_locality_or_destination_id"
        ] = None
        no_locality["candidate_enactment_request"][
            "requested_locality_or_destination_id"
        ] = None
        no_locality["requested_locality_or_destination"] = None
        self.assertOutcome(_resolve(no_locality), resolver.OUTCOME_ADMITTED)

    def test_one_shot_guardrails_and_closed_selection_posture_fail_closed(self) -> None:
        for section, key, value in (
            ("requested_enactment_scope", "requested_invocation_count", 2),
            ("single_invocation_posture", "requested_invocation_count", 2),
            ("single_invocation_posture", "no_repeat_posture", False),
            ("single_invocation_posture", "no_reuse_posture", False),
            (
                "single_invocation_posture",
                "no_standing_invocation_lane_posture",
                False,
            ),
            ("single_invocation_posture", "no_automatic_successor_posture", False),
        ):
            with self.subTest(case=f"{section}.{key}"):
                request = _request()
                request[section][key] = value
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

        selection_phrases = (
            "Select latest candidate.",
            "Select newest candidate.",
            "Select most recent candidate.",
            "Repository presence selects this candidate.",
            "Directory order selects this candidate.",
            "Timestamp selects this candidate.",
            "Sequence number selects this candidate.",
            "Test success selects this candidate.",
        )
        for phrase in selection_phrases:
            with self.subTest(selection=phrase):
                request = _request()
                request["candidate_enactment_request"]["request_purpose"] = phrase
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

        unknown_alternatives = (
            "alternative_candidate",
            "fallback_proposition",
            "second_request",
            "second_enactment_target",
        )
        for key in unknown_alternatives:
            with self.subTest(alternative=key):
                request = _request()
                request[key] = "not admitted"
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_request_polish_and_family_applicability_do_not_become_merit_or_standing(self) -> None:
        request = _request()
        request["candidate_enactment_request"]["request_purpose"] = (
            "A syntactically polished and complete request envelope."
        )
        result = _resolve(request)
        self.assertOutcome(result, resolver.OUTCOME_ADMITTED)
        self.assertIs(result["non_claims"]["candidate_standing_created"], False)
        self.assertIs(result["non_claims"]["candidate_currentness_created"], False)
        self.assertIs(result["non_claims"]["candidate_authority_created"], False)
        self.assertIs(result["non_claims"]["represented_proposition_evidenced"], False)
        for surface in (result, result["request_admission_decision"], result["result"]):
            self.assertNotIn("candidate_merit", surface)
            self.assertNotIn("candidate_rank", surface)
            self.assertNotIn("candidate_score", surface)

    def test_every_mandatory_non_claim_is_required_and_output_canonicalizes_false(self) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(key=key, posture="flipped"):
                request = _request()
                request["declared_non_claims"][key] = True
                result = _resolve(request)
                self.assertOutcome(result, resolver.OUTCOME_REVIEW_BLOCKED)
                self.assertEqual("NON_CLAIM_MISSING_OR_FLIPPED", result["block"]["code"])
                self.assertIs(result["non_claims"][key], False)
            with self.subTest(key=key, posture="missing"):
                request = _request()
                del request["declared_non_claims"][key]
                result = _resolve(request)
                self.assertOutcome(
                    result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
                )
                self.assertIs(result["non_claims"][key], False)

    def test_unknown_or_ambiguous_structure_is_rejected_at_every_shape(self) -> None:
        nested_sections = (
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
        )
        for section in nested_sections:
            with self.subTest(section=section):
                request = _request()
                request[section]["unknown_field"] = "not admitted"
                self.assertOutcome(_resolve(request), resolver.OUTCOME_REVIEW_BLOCKED)

        unknown_non_claim = _request()
        unknown_non_claim["declared_non_claims"]["general_permission_created"] = False
        self.assertOutcome(_resolve(unknown_non_claim), resolver.OUTCOME_REVIEW_BLOCKED)

    def test_all_four_outcomes_are_lawful_and_publicly_coded(self) -> None:
        admitted = _resolve(_request())
        not_admitted = _resolve(_request(applicable=False))
        additional_request = _request()
        del additional_request["family_owned_applicability_emission"]
        additional = _resolve(additional_request)
        blocked = _resolve(None)
        results = (admitted, not_admitted, additional, blocked)
        self.assertEqual(set(resolver.OUTCOMES), {item["outcome"] for item in results})
        for result in results:
            self.assertIs(result["result"]["lawful_terminal_outcome_recorded"], True)
            self.assertCanonicalNonClaims(result)
            for check in result["checks"]:
                if check["failure_code"] is not None:
                    self.assertIn(check["failure_code"], resolver.STOP_CODES)
                if check["block_code"] is not None:
                    self.assertIn(check["block_code"], resolver.BLOCK_CODES)

    def test_identical_calls_are_deterministic_without_mutation_or_retained_permission(self) -> None:
        request = _request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(before, request)
        self.assertEqual(first, second)
        self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))
        first["candidate_configuration"]["candidate_id"] = "changed-output"
        first["non_claims"]["reusable_permission_created"] = True
        third = _resolve(request)
        self.assertEqual("candidate-001", third["candidate_configuration"]["candidate_id"])
        self.assertIs(third["non_claims"]["reusable_permission_created"], False)

    def test_resolver_is_pure_filesystem_independent_and_semantically_non_owning(self) -> None:
        source = inspect.getsource(resolver)
        for forbidden_import in (
            "import os",
            "import pathlib",
            "from pathlib",
            "import subprocess",
            "import json",
            "import glob",
        ):
            self.assertNotIn(forbidden_import, source)
        for forbidden_name in (
            "write_result",
            "resolve_from_path",
            "GLOBAL_CANDIDATE_VOCABULARY",
            "GLOBAL_OUTCOME_ALLOWLIST",
            "CANDIDATE_REGISTRY",
            "CANDIDATE_CATALOGUE",
            "CANDIDATE_RANKING",
            "interpret_candidate_contract",
            "execute_candidate",
            "authorize_enactment",
        ):
            self.assertFalse(hasattr(resolver, forbidden_name))

        with mock.patch.object(
            builtins, "open", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "open", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "read_text", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "write_text", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "glob", side_effect=AssertionError("repository discovery")
        ), mock.patch.object(
            Path, "rglob", side_effect=AssertionError("repository discovery")
        ):
            result = _resolve(_request())
        self.assertOutcome(result, resolver.OUTCOME_ADMITTED)

        serialized_source = source.casefold()
        self.assertNotIn("eval(", serialized_source)
        self.assertNotIn("exec(", serialized_source)
        self.assertNotIn("candidate outcome allowlist", serialized_source)


if __name__ == "__main__":
    unittest.main()
