"""Adversarial tests for the bounded occurrence-evidence allocation resolver.

The suite supplies one closed M/C/P/B(C,P)/A/I/O/R/T/E/ER envelope. It tests
allocation to exact O only, while preserving E as semantic owner and refusing
occurrence establishment, evidence-adequacy determination, proposition support,
adoption, integration, reuse, continuation, and successor authority.
"""

from __future__ import annotations

import builtins
import copy
import inspect
import sys
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_matter_bound_candidate_occurrence_evidence_allocation_v0_min as resolver


EXPECTED_NON_CLAIMS = {
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
}


def _declared_non_claims() -> dict[str, bool]:
    return {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS}


def _request(result_posture: str = "EXPECTED") -> dict[str, object]:
    object_ids = [
        "matter-001",
        "candidate-001",
        "proposition-001",
        "binding-001",
        "authorization-001",
        "invocation-001",
        "occurrence-001",
        "result-001",
        "trace-001",
        "contract-001",
        "posture-001",
        "evidence-001",
    ]
    return {
        "matter": {
            "matter_id": "matter-001",
            "matter_purpose": "Allocate evidence for one occurrence claim only.",
            "matter_scope": "candidate-001 occurrence-001 only",
            "allocation_question": (
                "May evidence-001 be allocated to occurrence-001 only?"
            ),
            "outside_boundary": (
                "No occurrence establishment or proposition evaluation."
            ),
        },
        "candidate_configuration": {
            "candidate_id": "candidate-001",
            "candidate_type": "BOUNDED_CANDIDATE_CONFIGURATION",
            "candidate_version": "0.1.0",
            "candidate_reference": "supplied/candidate-001.json",
            "candidate_content_identity": "sha256:candidate-001",
        },
        "represented_proposition": {
            "represented_proposition_id": "proposition-001",
            "represented_proposition_type": "BOUNDED_REPRESENTED_PROPOSITION",
            "represented_proposition_statement": (
                "The represented condition has the declared bounded posture."
            ),
            "represented_proposition_reference": "supplied/proposition-001.json",
            "represented_proposition_semantic_owner": "proposition-owner-001",
            "represented_proposition_matter_scope": (
                "matter-001 proposition meaning only"
            ),
        },
        "candidate_proposition_binding": {
            "candidate_proposition_binding_id": "binding-001",
            "candidate_proposition_binding_type": (
                "EXACT_CANDIDATE_TO_REPRESENTED_PROPOSITION_BINDING"
            ),
            "candidate_proposition_binding_direction": (
                "CANDIDATE_REPRESENTS_PROPOSITION"
            ),
            "candidate_proposition_binding_scope": "matter-001 only",
            "candidate_id": "candidate-001",
            "represented_proposition_id": "proposition-001",
        },
        "bounded_enactment_authorization": {
            "authorization_id": "authorization-001",
            "authorization_type": "SEPARATELY_ADMITTED_BOUNDED_AUTHORIZATION",
            "authorization_version": "0.1.0",
            "authorization_reference": "supplied/authorization-001.json",
            "admitted_scope": (
                "matter-001 candidate-001 invocation-001 input-001 "
                "condition-001 once only"
            ),
            "enactment_mode": "BOUNDED_SINGLE_INVOCATION",
            "candidate_id": "candidate-001",
            "matter_id": "matter-001",
            "invocation_id": "invocation-001",
            "input_ids": ["input-001"],
            "condition_ids": ["condition-001"],
            "permitted_invocation_count": 1,
            "non_reuse_posture": True,
        },
        "bounded_enactment_invocation": {
            "invocation_id": "invocation-001",
            "authorization_id": "authorization-001",
            "candidate_id": "candidate-001",
            "matter_id": "matter-001",
            "enactment_mode": "BOUNDED_SINGLE_INVOCATION",
            "input_ids": ["input-001"],
            "condition_ids": ["condition-001"],
            "result_id": "result-001",
            "trace_id": "trace-001",
        },
        "occurrence_claim": {
            "occurrence_claim_id": "occurrence-001",
            "occurrence_claim_type": "BOUNDED_CANDIDATE_ENACTMENT_OCCURRENCE",
            "occurrence_claim_wording": (
                "Candidate candidate-001 was enacted under invocation "
                "invocation-001 and authorization authorization-001; result "
                "result-001 and trace trace-001 were emitted."
            ),
            "occurrence_claim_scope": (
                "exact invocation, inputs, conditions, result, and trace only"
            ),
            "matter_id": "matter-001",
            "candidate_id": "candidate-001",
            "candidate_proposition_binding_id": "binding-001",
            "authorization_id": "authorization-001",
            "invocation_id": "invocation-001",
            "result_id": "result-001",
            "trace_id": "trace-001",
        },
        "result": {
            "result_id": "result-001",
            "result_reference": "supplied/result-001.json",
            "result_type": "BOUNDED_ENACTMENT_RESULT",
            "bounded_result_posture": result_posture,
        },
        "trace": {
            "trace_id": "trace-001",
            "trace_reference": "supplied/trace-001.json",
            "trace_type": "BOUNDED_ENACTMENT_TRACE",
            "trace_posture": "EXACT_INVOCATION_TRACE",
            "audit_or_occurrence_evidence_only": True,
        },
        "occurrence_evidence_contract": {
            "occurrence_evidence_contract_id": "contract-001",
            "occurrence_evidence_contract_type": (
                "BOUNDED_OCCURRENCE_EVIDENCE_CONTRACT"
            ),
            "occurrence_evidence_contract_version": "0.1.0",
            "occurrence_evidence_contract_reference": "supplied/contract-001.json",
            "occurrence_evidence_contract_semantic_owner": "contract-owner-001",
            "applicability_scope": (
                "occurrence-001 exact evidence class and claim shape only"
            ),
            "evidence_effect_location": "occurrence-001",
            "governed_evidence_class": "BOUNDED_INVOCATION_TRACE_EVIDENCE",
            "governed_occurrence_claim_type": (
                "BOUNDED_CANDIDATE_ENACTMENT_OCCURRENCE"
            ),
            "governed_occurrence_claim_scope": (
                "exact invocation, inputs, conditions, result, and trace only"
            ),
        },
        "contract_owned_allocability_rule_or_occurrence_support_posture": {
            "posture_id": "posture-001",
            "posture_type": "CONTRACT_OWNED_OCCURRENCE_ALLOCABILITY_POSTURE",
            "posture_reference": "supplied/contract-001.json#posture-001",
            "occurrence_evidence_contract_id": "contract-001",
            "semantic_owner": "contract-owner-001",
            "applicability_scope": (
                "occurrence-001 exact evidence class and claim shape only"
            ),
            "evidence_class": "BOUNDED_INVOCATION_TRACE_EVIDENCE",
            "occurrence_claim_id": "occurrence-001",
            "allocation_target_id": "occurrence-001",
            "allocation_target_type": "BOUNDED_CANDIDATE_ENACTMENT_OCCURRENCE",
            "allocation_to_exact_occurrence_claim_permitted": True,
            "allocation_to_represented_proposition_permitted": False,
        },
        "occurrence_evidence_references": [
            {
                "occurrence_evidence_reference_id": "evidence-001",
                "occurrence_evidence_reference": "supplied/trace-001.json#event-001",
                "evidence_class": "BOUNDED_INVOCATION_TRACE_EVIDENCE",
                "occurrence_evidence_contract_id": "contract-001",
                "contract_owned_posture_id": "posture-001",
                "occurrence_claim_id": "occurrence-001",
            }
        ],
        "evidence_allocation_statement": {
            "allocation_statement_id": "allocation-statement-001",
            "occurrence_claim_id": "occurrence-001",
            "sole_allocation_target_id": "occurrence-001",
            "represented_proposition_id": "proposition-001",
            "occurrence_evidence_reference_ids": ["evidence-001"],
            "allocated_to_occurrence_claim_only": True,
            "allocation_to_represented_proposition_refused": True,
        },
        "lineage_and_custody": {
            "object_references": [
                {
                    "object_id": object_id,
                    "lineage_reference": f"lineage/{object_id}",
                    "custody_reference": f"custody/{object_id}",
                }
                for object_id in object_ids
            ]
        },
        "bounded_allocation_decision_posture": {
            "allocation_decision_id": "allocation-decision-001",
            "allocation_decision_scope": "occurrence-001 allocation only",
            "occurrence_claim_id": "occurrence-001",
            "represented_proposition_id": "proposition-001",
            "one_allocation_decision_only": True,
            "occurrence_is_not_established": True,
            "evidence_adequacy_is_not_determined": True,
            "evidentiary_migration_is_blocked": True,
        },
        "declared_non_claims": _declared_non_claims(),
    }


def _resolve(request: object) -> dict[str, object]:
    return resolver.resolve_matter_bound_candidate_occurrence_evidence_allocation_v0_min(
        request  # type: ignore[arg-type]
    )


class MatterBoundCandidateOccurrenceEvidenceAllocationTests(unittest.TestCase):
    def assertCanonicalNonClaims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(EXPECTED_NON_CLAIMS, set(non_claims))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims[key], False)

    def assertLawfulStop(self, result: dict[str, object]) -> None:
        self.assertIn(result["outcome"], resolver.OUTCOMES)
        self.assertNotEqual(resolver.OUTCOME_RECORDED, result["outcome"])
        resolution = result["result"]
        self.assertIs(resolution["lawful_terminal_outcome_recorded"], True)
        self.assertCanonicalNonClaims(result)

    def assertRecorded(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.OUTCOME_RECORDED, result["outcome"])
        self.assertIs(result["allocation_decision"]["allocation_recorded"], True)
        self.assertIsNone(result["block"]["code"])
        self.assertCanonicalNonClaims(result)

    def test_public_contract_and_complete_mandatory_non_claim_set(self) -> None:
        self.assertEqual("0.1.0", resolver.RESULT_VERSION)
        self.assertEqual(
            "resolve_matter_bound_candidate_occurrence_evidence_allocation_v0_min",
            resolver.RESOLVER_MODULE,
        )
        self.assertEqual(
            "MATTER_BOUND_CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION",
            resolver.ALLOCATION_TYPE,
        )
        self.assertEqual("0.1.0", resolver.ALLOCATION_VERSION)
        self.assertEqual(
            "ONE_EXACT_MATTER_ONE_EXACT_CANDIDATE_ONE_EXACT_REPRESENTED_"
            "PROPOSITION_ONE_SEPARATELY_AUTHORIZED_BOUNDED_ENACTMENT_ONE_EXACT_"
            "OCCURRENCE_CLAIM_ONLY",
            resolver.ALLOCATION_SCOPE,
        )
        self.assertEqual(EXPECTED_NON_CLAIMS, set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertEqual(
            {
                "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_RECORDED",
                "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_REQUIRES_ADDITIONAL_BASIS",
                "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_NOT_RECORDED",
                "CANDIDATE_OCCURRENCE_EVIDENCE_ALLOCATION_REVIEW_BLOCKED",
            },
            set(resolver.OUTCOMES),
        )
        self.assertFalse(any(name.startswith("write_") for name in resolver.__all__))
        self.assertFalse(any(name.endswith("_from_path") for name in resolver.__all__))

    def test_exact_singular_envelope_records_o_only(self) -> None:
        result = _resolve(_request())
        self.assertRecorded(result)
        metadata = result["metadata"]
        self.assertEqual(resolver.ALLOCATION_TYPE, metadata[
            "matter_bound_candidate_occurrence_evidence_allocation_type"
        ])
        self.assertEqual("occurrence-001", result["allocation_decision"][
            "sole_allocation_target_id"
        ])
        self.assertEqual(
            ["evidence-001"],
            result["allocation_decision"][
                "allocated_occurrence_evidence_reference_ids"
            ],
        )
        self.assertIs(
            result["allocation_decision"][
                "evidence_migration_to_represented_proposition_blocked"
            ],
            True,
        )
        self.assertIs(result["allocation_decision"]["occurrence_established"], False)
        self.assertIs(
            result["allocation_decision"]["evidence_adequacy_determined"], False
        )
        self.assertEqual("result-001", result["bounded_result"]["result_id"])
        self.assertEqual(resolver.OUTCOME_RECORDED, result["result"]["outcome"])

    def test_p_other_or_second_allocation_target_fails_closed(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        direct_p = _request()
        direct_p["evidence_allocation_statement"]["sole_allocation_target_id"] = (
            "proposition-001"
        )
        cases.append(("direct_p", direct_p))
        other = _request()
        other["evidence_allocation_statement"]["sole_allocation_target_id"] = "other"
        cases.append(("other", other))
        second = _request()
        second["evidence_allocation_statement"]["second_allocation_target_id"] = (
            "proposition-001"
        )
        cases.append(("second", second))
        posture_to_p = _request()
        posture_to_p[
            "contract_owned_allocability_rule_or_occurrence_support_posture"
        ]["allocation_target_id"] = "proposition-001"
        cases.append(("contract_posture_to_p", posture_to_p))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_missing_or_mismatched_m_c_p_and_binding_fail_closed(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for section in (
            "matter",
            "candidate_configuration",
            "represented_proposition",
            "candidate_proposition_binding",
        ):
            request = _request()
            del request[section]
            cases.append((f"missing_{section}", request))

        mutations = (
            ("matter_id", "matter", "matter_id", "other-matter"),
            ("candidate_in_binding", "candidate_proposition_binding", "candidate_id", "other-candidate"),
            ("proposition_in_binding", "candidate_proposition_binding", "represented_proposition_id", "other-proposition"),
            ("candidate_in_occurrence", "occurrence_claim", "candidate_id", "other-candidate"),
            ("matter_in_occurrence", "occurrence_claim", "matter_id", "other-matter"),
            ("binding_in_occurrence", "occurrence_claim", "candidate_proposition_binding_id", "other-binding"),
            ("proposition_in_allocation", "evidence_allocation_statement", "represented_proposition_id", "other-proposition"),
        )
        for label, section, key, value in mutations:
            request = _request()
            request[section][key] = value
            cases.append((label, request))

        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_authorization_must_cover_exact_single_non_reusable_invocation(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        missing = _request()
        del missing["bounded_enactment_authorization"]
        cases.append(("missing_authorization", missing))
        missing_scope = _request()
        del missing_scope["bounded_enactment_authorization"]["admitted_scope"]
        cases.append(("missing_scope", missing_scope))
        for key, value in (
            ("candidate_id", "other-candidate"),
            ("matter_id", "other-matter"),
            ("invocation_id", "other-invocation"),
            ("enactment_mode", "other-mode"),
            ("input_ids", ["other-input"]),
            ("condition_ids", ["other-condition"]),
            ("permitted_invocation_count", 2),
            ("non_reuse_posture", False),
        ):
            request = _request()
            request["bounded_enactment_authorization"][key] = value
            cases.append((key, request))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_invocation_and_occurrence_bind_exact_envelope(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for section in ("bounded_enactment_invocation", "occurrence_claim"):
            request = _request()
            del request[section]
            cases.append((f"missing_{section}", request))
        for section, key, value in (
            ("bounded_enactment_invocation", "authorization_id", "other-authorization"),
            ("bounded_enactment_invocation", "candidate_id", "other-candidate"),
            ("bounded_enactment_invocation", "matter_id", "other-matter"),
            ("bounded_enactment_invocation", "result_id", "other-result"),
            ("bounded_enactment_invocation", "trace_id", "other-trace"),
            ("occurrence_claim", "authorization_id", "other-authorization"),
            ("occurrence_claim", "invocation_id", "other-invocation"),
            ("occurrence_claim", "result_id", "other-result"),
            ("occurrence_claim", "trace_id", "other-trace"),
        ):
            request = _request()
            request[section][key] = value
            cases.append((f"{section}_{key}", request))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_occurrence_wording_cannot_claim_p_or_candidate_adoption(self) -> None:
        forbidden = (
            "Represented proposition is true.",
            "Represented proposition stands.",
            "Represented proposition is authoritative.",
            "Proposition truth established.",
            "Proposition standing established.",
            "Proposition authority established.",
            "Candidate is adopted.",
            "Candidate was integrated.",
        )
        for wording in forbidden:
            with self.subTest(wording=wording):
                request = _request()
                request["occurrence_claim"]["occurrence_claim_wording"] = wording
                result = _resolve(request)
                self.assertEqual(resolver.OUTCOME_REVIEW_BLOCKED, result["outcome"])
                self.assertEqual("OCCURRENCE_CLAIM_OVERREACH", result["block"]["code"])
                self.assertCanonicalNonClaims(result)

    def test_result_and_trace_are_exact_and_trace_remains_non_authoritative(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for section in ("result", "trace"):
            request = _request()
            del request[section]
            cases.append((f"missing_{section}", request))
        for section, key in (("result", "result_reference"), ("trace", "trace_reference")):
            request = _request()
            del request[section][key]
            cases.append((f"missing_{section}_{key}", request))
        substituted_result = _request()
        substituted_result["result"]["result_id"] = "latest-result"
        cases.append(("substituted_result", substituted_result))
        substituted_trace = _request()
        substituted_trace["trace"]["trace_id"] = "latest-trace"
        cases.append(("substituted_trace", substituted_trace))
        trace_overreach = _request()
        trace_overreach["trace"]["audit_or_occurrence_evidence_only"] = False
        cases.append(("trace_overreach", trace_overreach))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_e_and_exact_e_owned_posture_are_required_and_attributable(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        missing_contract = _request()
        del missing_contract["occurrence_evidence_contract"]
        cases.append(("missing_contract", missing_contract))
        missing_posture = _request()
        del missing_posture[
            "contract_owned_allocability_rule_or_occurrence_support_posture"
        ]
        cases.append(("missing_posture", missing_posture))
        for section, key in (
            ("occurrence_evidence_contract", "occurrence_evidence_contract_semantic_owner"),
            ("occurrence_evidence_contract", "applicability_scope"),
            ("occurrence_evidence_contract", "evidence_effect_location"),
            ("contract_owned_allocability_rule_or_occurrence_support_posture", "posture_reference"),
        ):
            request = _request()
            del request[section][key]
            cases.append((f"missing_{key}", request))
        for key, value in (
            ("occurrence_evidence_contract_id", "other-contract"),
            ("semantic_owner", "caller-owned"),
            ("applicability_scope", "other-scope"),
            ("evidence_class", "other-evidence-class"),
            ("occurrence_claim_id", "other-occurrence"),
        ):
            request = _request()
            request[
                "contract_owned_allocability_rule_or_occurrence_support_posture"
            ][key] = value
            cases.append((f"posture_{key}", request))
        wrong_effect_location = _request()
        wrong_effect_location["occurrence_evidence_contract"][
            "evidence_effect_location"
        ] = "proposition-001"
        cases.append(("wrong_effect_location", wrong_effect_location))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_negative_e_owned_applicability_is_lawful_not_recorded(self) -> None:
        for key, value in (
            ("allocation_to_exact_occurrence_claim_permitted", False),
            ("allocation_to_represented_proposition_permitted", True),
        ):
            with self.subTest(key=key):
                request = _request()
                request[
                    "contract_owned_allocability_rule_or_occurrence_support_posture"
                ][key] = value
                result = _resolve(request)
                self.assertEqual(resolver.OUTCOME_NOT_RECORDED, result["outcome"])
                self.assertIs(result["result"]["lawful_terminal_outcome_recorded"], True)
                self.assertCanonicalNonClaims(result)

    def test_naked_boolean_outcome_or_repository_existence_cannot_replace_e_posture(self) -> None:
        substitutes = (
            ("supports_occurrence", True),
            ("contract_outcome", "SUPPORTS_OCCURRENCE"),
            ("contract_file_exists", True),
            ("receipt_exists", True),
            ("latest_contract_selected", True),
        )
        for key, value in substitutes:
            with self.subTest(substitute=key):
                request = _request()
                del request[
                    "contract_owned_allocability_rule_or_occurrence_support_posture"
                ]
                request[key] = value
                result = _resolve(request)
                self.assertEqual(resolver.OUTCOME_REVIEW_BLOCKED, result["outcome"])
                self.assertEqual("REQUEST_KEYS_INVALID", result["block"]["code"])
                self.assertCanonicalNonClaims(result)

    def test_evidence_references_are_exact_unique_and_bound_to_o(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        missing = _request()
        missing["occurrence_evidence_references"] = []
        cases.append(("missing", missing))
        other_o = _request()
        other_o["occurrence_evidence_references"][0]["occurrence_claim_id"] = (
            "other-occurrence"
        )
        cases.append(("other_occurrence", other_o))
        other_contract = _request()
        other_contract["occurrence_evidence_references"][0][
            "occurrence_evidence_contract_id"
        ] = "other-contract"
        cases.append(("other_contract", other_contract))
        duplicate = _request()
        duplicate["occurrence_evidence_references"].append(
            copy.deepcopy(duplicate["occurrence_evidence_references"][0])
        )
        cases.append(("duplicate", duplicate))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_allocation_statement_and_decision_posture_preserve_boundary(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for section in (
            "evidence_allocation_statement",
            "bounded_allocation_decision_posture",
        ):
            request = _request()
            del request[section]
            cases.append((f"missing_{section}", request))
        for key, value in (
            ("sole_allocation_target_id", "other-occurrence"),
            ("allocated_to_occurrence_claim_only", False),
            ("allocation_to_represented_proposition_refused", False),
        ):
            request = _request()
            request["evidence_allocation_statement"][key] = value
            cases.append((key, request))
        for key, value in (
            ("one_allocation_decision_only", False),
            ("occurrence_is_not_established", False),
            ("evidence_adequacy_is_not_determined", False),
            ("evidentiary_migration_is_blocked", False),
        ):
            request = _request()
            request["bounded_allocation_decision_posture"][key] = value
            cases.append((key, request))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_lineage_and_custody_cover_exact_selected_objects(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        missing = _request()
        del missing["lineage_and_custody"]
        cases.append(("missing", missing))
        missing_entry = _request()
        missing_entry["lineage_and_custody"]["object_references"].pop()
        cases.append(("missing_entry", missing_entry))
        substituted = _request()
        substituted["lineage_and_custody"]["object_references"][0][
            "object_id"
        ] = "other-matter"
        cases.append(("substituted", substituted))
        missing_custody = _request()
        del missing_custody["lineage_and_custody"]["object_references"][0][
            "custody_reference"
        ]
        cases.append(("missing_custody", missing_custody))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertLawfulStop(_resolve(request))

    def test_every_result_polarity_remains_o_only_and_never_supports_p(self) -> None:
        for posture in (
            "EXPECTED",
            "FAILED",
            "SURPRISING",
            "REFUSED",
            "INCOMPLETE",
            "SUCCESSFUL",
        ):
            with self.subTest(posture=posture):
                result = _resolve(_request(posture))
                self.assertRecorded(result)
                self.assertEqual(posture, result["bounded_result"][
                    "bounded_result_posture"
                ])
                self.assertIs(result["non_claims"]["represented_proposition_evidenced"], False)
                self.assertIs(result["non_claims"]["result_treated_as_success"], False)
                self.assertIs(result["non_claims"]["result_standing_created"], False)

    def test_repeated_success_creates_no_currentness_reuse_or_successor_force(self) -> None:
        request = _request("SUCCESSFUL")
        results = [_resolve(copy.deepcopy(request)) for _ in range(3)]
        self.assertEqual(results[0], results[1])
        self.assertEqual(results[1], results[2])
        for result in results:
            self.assertRecorded(result)
            for key in (
                "represented_proposition_current",
                "candidate_adopted",
                "candidate_integrated",
                "reuse_permission_created",
                "continuation_permission_created",
                "successor_authority_created",
                "repetition_treated_as_adoption_force",
                "repetition_treated_as_integration_force",
                "repeat_enactment_permission_created",
                "currentness_created",
                "adoption_force_created",
                "integration_force_created",
            ):
                self.assertIs(result["non_claims"][key], False)

    def test_recorded_neither_establishes_o_nor_determines_adequacy_or_merit(self) -> None:
        request = _request()
        request["candidate_configuration"]["candidate_content_identity"] = (
            "sha256:polished-complete-candidate"
        )
        result = _resolve(request)
        self.assertRecorded(result)
        self.assertIs(result["allocation_decision"]["occurrence_established"], False)
        self.assertIs(
            result["allocation_decision"]["evidence_adequacy_determined"], False
        )
        for key in (
            "enactment_occurrence_established",
            "occurrence_claim_established",
            "evidence_adequacy_determined_by_allocation_boundary",
            "candidate_standing_created",
            "candidate_authority_created",
            "candidate_preference_selected",
            "truth_created",
            "standing_created",
            "authority_created",
        ):
            self.assertIs(result["non_claims"][key], False)

    def test_every_non_claim_is_required_false_and_output_canonicalizes_false(self) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(key=key, posture="flipped"):
                request = _request()
                request["declared_non_claims"][key] = True
                result = _resolve(request)
                self.assertEqual(resolver.OUTCOME_REVIEW_BLOCKED, result["outcome"])
                self.assertEqual("NON_CLAIM_MISSING_OR_FLIPPED", result["block"]["code"])
                self.assertCanonicalNonClaims(result)
            with self.subTest(key=key, posture="missing"):
                request = _request()
                del request["declared_non_claims"][key]
                result = _resolve(request)
                self.assertEqual(
                    resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    result["outcome"],
                )
                self.assertCanonicalNonClaims(result)

    def test_unknown_or_ambiguous_structure_is_rejected_at_every_shape(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        top = _request()
        top["alternative_candidates"] = ["candidate-002"]
        cases.append(("top", top))
        nested_sections = (
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
            "evidence_allocation_statement",
            "bounded_allocation_decision_posture",
        )
        for section in nested_sections:
            request = _request()
            request[section]["unknown_field"] = "not admitted"
            cases.append((section, request))
        evidence = _request()
        evidence["occurrence_evidence_references"][0]["unknown_field"] = True
        cases.append(("evidence", evidence))
        lineage = _request()
        lineage["lineage_and_custody"]["object_references"][0][
            "unknown_field"
        ] = True
        cases.append(("lineage", lineage))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertEqual(
                    resolver.OUTCOME_REVIEW_BLOCKED, _resolve(request)["outcome"]
                )

    def test_all_four_outcomes_are_lawful_and_codes_are_public(self) -> None:
        recorded = _resolve(_request())
        additional_request = _request()
        del additional_request[
            "contract_owned_allocability_rule_or_occurrence_support_posture"
        ]
        additional = _resolve(additional_request)
        not_recorded_request = _request()
        not_recorded_request[
            "contract_owned_allocability_rule_or_occurrence_support_posture"
        ]["allocation_to_exact_occurrence_claim_permitted"] = False
        not_recorded = _resolve(not_recorded_request)
        blocked = _resolve(None)
        results = (recorded, additional, not_recorded, blocked)
        self.assertEqual(set(resolver.OUTCOMES), {item["outcome"] for item in results})
        for result in results:
            self.assertIs(result["result"]["lawful_terminal_outcome_recorded"], True)
            self.assertCanonicalNonClaims(result)
            for check in result["checks"]:
                if check["failure_code"] is not None:
                    self.assertIn(check["failure_code"], resolver.STOP_CODES)
                if check["block_code"] is not None:
                    self.assertIn(check["block_code"], resolver.BLOCK_CODES)

    def test_input_is_not_mutated_and_output_is_independent(self) -> None:
        request = _request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        self.assertEqual(before, request)
        first["candidate_configuration"]["candidate_id"] = "changed-output"
        first["non_claims"]["truth_created"] = True
        self.assertEqual(before, request)
        second = _resolve(request)
        self.assertEqual("candidate-001", second["candidate_configuration"]["candidate_id"])
        self.assertIs(second["non_claims"]["truth_created"], False)

    def test_resolver_is_pure_and_introduces_no_machinery(self) -> None:
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
            "GLOBAL_EVIDENCE_VOCABULARY",
            "GLOBAL_OUTCOME_ALLOWLIST",
            "CANDIDATE_REGISTRY",
            "CANDIDATE_CATALOGUE",
            "RANKING",
        ):
            self.assertFalse(hasattr(resolver, forbidden_name))

        request = _request()
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
            result = _resolve(request)
        self.assertRecorded(result)


if __name__ == "__main__":
    unittest.main()
