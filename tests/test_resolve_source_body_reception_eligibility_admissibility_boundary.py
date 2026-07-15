"""Executable boundary tests for source-body reception eligibility only.

These tests prove that the resolver records review-readiness for one declared
source-body reception request after receiving-context role recording. Eligibility
is not reception. Admissibility is not authorization. Source remains unreceived,
receiving context remains context only, and non-capture and recognition remain
future work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_source_body_reception_eligibility_admissibility_boundary as resolver  # noqa: E402


ELIGIBLE = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"
NOT_ELIGIBLE = "SOURCE_BODY_RECEPTION_NOT_ELIGIBLE_OR_ADMISSIBLE"
REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_ELIGIBILITY_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "SOURCE_BODY_RECEPTION_ELIGIBILITY_REVIEW_BLOCKED"
ROLE_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
IDENTITY_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {
    ELIGIBLE,
    NOT_ELIGIBLE,
    REQUIRES_ADDITIONAL_BASIS,
    BLOCKED,
}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_eligibility_metadata",
    "declared_eligibility_question",
    "selected_receiving_context_role_result",
    "selected_source_body_surface",
    "receiving_context",
    "eligibility_basis",
    "admissibility_basis",
    "eligibility_scope",
    "eligibility_checks",
    "eligibility_statement",
    "eligibility_non_meaning",
    "additional_basis_required",
    "not_eligible_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_eligibility_summary",
}

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_RECEPTION_ELIGIBILITY_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)


def false_eligibility_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def false_role_non_claims() -> dict[str, bool]:
    return {
        "reception_recognized": False,
        "reception_authorized": False,
        "source_received": False,
        "receiving_context_governance_created": False,
        "receiving_context_became_source": False,
        "receiving_context_became_authority": False,
        "receiving_context_became_current": False,
        "receiving_context_became_receiver": False,
        "receiving_context_became_adopter": False,
        "receiving_context_became_validator": False,
        "receiving_context_became_invalidator": False,
        "receiving_context_became_operator": False,
        "receiving_context_became_vessel": False,
        "receiving_context_became_derivative": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "source_replaced": False,
        "adoption_created": False,
        "authority_created": False,
        "currentness_created": False,
        "standing_created": False,
        "standing_propagated": False,
        "vessel_relation_created": False,
        "derivative_relation_created": False,
        "operation_permission_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }


def selected_reception_request_declaration_result() -> dict[str, object]:
    return {
        "source_body_reception_request_metadata": {
            "source_body_reception_request_result_id": (
                "source_body_reception_request_declaration__request-001"
            ),
            "source_body_reception_request_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_request_declaration",
        },
        "declared_reception_question": {
            "reception_request_id": "source-body-reception-request-001",
            "reception_question": "What source-body reception request has been declared?",
        },
        "outcome": REQUEST_DECLARED,
        "source_body_reception_request_summary": {
            "outcome": REQUEST_DECLARED,
            "failed_check_count": 0,
            "reception_request_id": "source-body-reception-request-001",
        },
    }


def selected_source_body_surface() -> dict[str, object]:
    return {
        "selected_source_body_surface_identifier": "source-body-surface-001",
        "selected_source_body_surface_type": "REFERENCE_SOURCE_BODY_SURFACE",
        "selected_source_body_surface_path": "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
        "selected_source_body_surface_reference": "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
        "source_body_identity_basis": {
            "identity_basis_id": "source-body-identity-basis-001",
            "identity_basis_declared": True,
        },
        "source_body_lineage_basis": {
            "lineage_basis_id": "source-body-lineage-basis-001",
            "lineage_basis_declared": True,
        },
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "source_received": False,
        "adoption_created": False,
        "source_replaced": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
    }


def receiving_context() -> dict[str, object]:
    return {
        "receiving_context_id": "receiving-context-001",
        "receiving_context_name": "bounded receiving context",
        "receiving_context_reference": "IAMMAI-SYSTEM present execution line",
        "receiving_context_type": "PRESENT_EXECUTION_CONTEXT",
        "context_only": True,
        "evidence_only": True,
        "receiving_context_preserved": True,
        "receiving_context_remains_context_only": True,
        "receiving_context_became_source": False,
        "receiving_context_became_authority": False,
        "receiving_context_became_current": False,
        "receiving_context_became_receiver": False,
        "receiving_context_became_adopter": False,
        "receiving_context_became_validator": False,
        "receiving_context_became_invalidator": False,
        "receiving_context_became_operator": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "receiving_context_governance_created": False,
        "operation_permission_created": False,
        "publication_flow_opened": False,
    }


def reception_purpose() -> dict[str, object]:
    return {
        "purpose_id": "eligibility-before-reception-recognition",
        "purpose_statement": "Screen declared request for later reception-family review only.",
        "purpose_is_permission": False,
    }


def reception_limits() -> dict[str, object]:
    return {
        "limits_id": "source-body-reception-eligibility-limits-001",
        "eligibility_boundary_only": True,
        "no_reception_recognition": True,
        "no_reception_authorization": True,
        "no_source_receipt": True,
        "no_non_capture_claim": True,
        "no_recognition_claim": True,
        "no_operation_permission": True,
        "no_publication_flow": True,
    }


def selected_identity_preservation_result() -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    return {
        "source_body_reception_identity_metadata": {
            "source_body_reception_identity_result_id": (
                "source_body_reception_identity_preservation__identity-001"
            ),
            "source_body_reception_identity_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_identity_preservation_boundary",
        },
        "selected_reception_request_declaration_result": (
            selected_reception_request_declaration_result()
        ),
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "outcome": IDENTITY_PRESERVED,
        "source_body_reception_identity_summary": {
            "outcome": IDENTITY_PRESERVED,
            "failed_check_count": 0,
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "selected_surface_is_not_whole_body_by_default": True,
            "receiving_context_preserved": True,
            "receiving_context_remains_context_only": True,
            "receiving_context_is_not_source": True,
            "receiving_context_is_not_authority": True,
            "receiving_context_is_not_current": True,
            "reception_class_preserved": True,
            "reception_purpose_preserved": True,
            "reception_limits_preserved": True,
        },
    }


def declared_receiving_context_role() -> dict[str, object]:
    return {
        "declared_receiving_context_role_id": "reference-review-context-role-001",
        "declared_receiving_context_role_statement": (
            "Receiving context is bounded reference review context only."
        ),
        "role_is_bounded_review_posture_only": True,
    }


def receiving_context_role_limits() -> dict[str, bool]:
    return {
        "role_boundary_only": True,
        "role_is_not_reception": True,
        "role_is_not_authorization": True,
        "role_is_not_source_receipt": True,
        "role_is_not_source_authority": True,
        "role_is_not_currentness": True,
        "role_is_not_adoption": True,
        "role_is_not_validation": True,
        "role_is_not_invalidation": True,
        "role_is_not_operation_permission": True,
        "role_is_not_vessel_relation": True,
        "role_is_not_derivative_relation": True,
        "role_is_not_publication_flow": True,
    }


def receiving_context_role_basis() -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    return {
        "basis_id": "source-body-reception-receiving-context-role-basis-001",
        "selected_identity_preservation_result": selected_identity_preservation_result(),
        "selected_reception_request_declaration_result": (
            selected_reception_request_declaration_result()
        ),
        "selected_source_body_surface": surface,
        "source_body_identity_basis": surface["source_body_identity_basis"],
        "source_body_lineage_basis": surface["source_body_lineage_basis"],
        "receiving_context": context,
        "receiving_context_type": context["receiving_context_type"],
        "reception_class": "REFERENCE_RECEPTION",
        "reception_purpose": reception_purpose(),
        "reception_limits": reception_limits(),
        "declared_receiving_context_role": declared_receiving_context_role(),
        "receiving_context_role_class": "REFERENCE_REVIEW_CONTEXT",
        "receiving_context_role_limits": receiving_context_role_limits(),
        "role_non_reception_distinction": True,
        "role_non_authorization_distinction": True,
        "role_non_authority_distinction": True,
        "role_non_currentness_distinction": True,
        "role_non_adoption_distinction": True,
        "role_non_validation_distinction": True,
        "role_non_operation_permission_distinction": True,
        "role_non_publication_flow_distinction": True,
        "source_body_surface_remains_source": True,
        "receiving_context_remains_context_only": True,
    }


def selected_receiving_context_role_result(**overrides: object) -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    basis = receiving_context_role_basis()
    statement = {
        "source_body_reception_receiving_context_role_recorded": True,
        "selected_identity_preservation_result_preserved": True,
        "selected_identity_preservation_result_recorded": True,
        "selected_identity_preservation_result_failed_check_count_zero": True,
        "selected_reception_request_declaration_result_preserved": True,
        "selected_source_body_surface_preserved": True,
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "receiving_context_preserved": True,
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "receiving_context_role_declared": True,
        "role_is_not_permission": True,
        "role_is_not_reception": True,
        "role_is_not_authorization": True,
        "role_is_not_source_receipt": True,
        "role_is_not_source_authority": True,
        "role_is_not_currentness": True,
        "role_is_not_adoption": True,
        "role_is_not_validation": True,
        "role_is_not_invalidation": True,
        "role_is_not_operation_permission": True,
        "role_is_not_vessel_relation": True,
        "role_is_not_derivative_relation": True,
        "role_is_not_publication_flow": True,
        "reception_class_preserved": True,
        "reception_purpose_preserved": True,
        "reception_limits_preserved": True,
        "identity_preservation_basis_preserved": True,
    }
    statement.update(false_role_non_claims())
    result: dict[str, object] = {
        "source_body_reception_receiving_context_role_metadata": {
            "source_body_reception_receiving_context_role_result_id": (
                "source_body_reception_receiving_context_role__role-001"
            ),
            "source_body_reception_receiving_context_role_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_receiving_context_role_boundary",
        },
        "declared_receiving_context_role_question": {
            "receiving_context_role_request_id": (
                "source-body-reception-receiving-context-role-001"
            ),
            "receiving_context_role_question": (
                "What bounded receiving-context role may be recorded?"
            ),
        },
        "selected_identity_preservation_result": selected_identity_preservation_result(),
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "receiving_context_role": {
            "declared_receiving_context_role": basis["declared_receiving_context_role"],
            "receiving_context_role_class": "REFERENCE_REVIEW_CONTEXT",
            "receiving_context_role_limits": basis["receiving_context_role_limits"],
        },
        "receiving_context_role_basis": basis,
        "receiving_context_role_checks": [
            {
                "check_name": "receiving-context role is not reception",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
                "failure_code": None,
            }
        ],
        "receiving_context_role_statement": statement,
        "non_claims": false_role_non_claims(),
        "outcome": ROLE_RECORDED,
        "source_body_reception_receiving_context_role_summary": {
            "outcome": ROLE_RECORDED,
            "source_body_reception_receiving_context_role_result_id": (
                "source_body_reception_receiving_context_role__role-001"
            ),
            "failed_check_count": 0,
            "passed_check_count": 50,
            "selected_identity_preservation_result_preserved": True,
            "selected_identity_preservation_result_recorded": True,
            "selected_identity_preservation_result_failed_check_count_zero": True,
            "selected_reception_request_declaration_result_preserved": True,
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "selected_surface_is_not_whole_body_by_default": True,
            "receiving_context_preserved": True,
            "receiving_context_remains_context_only": True,
            "receiving_context_is_not_source": True,
            "receiving_context_is_not_authority": True,
            "receiving_context_is_not_current": True,
            "receiving_context_role_declared": True,
            "receiving_context_role_class": "REFERENCE_REVIEW_CONTEXT",
            "role_is_not_permission": True,
            "role_is_not_reception": True,
            "role_is_not_authorization": True,
            "role_is_not_source_receipt": True,
            "role_is_not_source_authority": True,
            "role_is_not_currentness": True,
            "role_is_not_adoption": True,
            "role_is_not_validation": True,
            "role_is_not_invalidation": True,
            "role_is_not_operation_permission": True,
            "role_is_not_publication_flow": True,
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": reception_purpose(),
            "reception_class_preserved": True,
            "reception_purpose_preserved": True,
            "reception_limits_preserved": True,
        },
    }
    result.update(overrides)
    return result


def eligibility_basis() -> dict[str, object]:
    return {
        "eligibility_basis_id": "source-body-reception-eligibility-basis-001",
        "eligibility_basis_declared": True,
        "eligible_for_later_reception_review_only": True,
        "eligibility_is_not_reception": True,
        "eligibility_is_not_recognition": True,
        "eligibility_is_not_source_receipt": True,
        "eligibility_does_not_decide_non_capture": True,
        "eligibility_does_not_decide_recognition": True,
        "source_body_surface_remains_source": True,
        "receiving_context_remains_context_only": True,
    }


def admissibility_basis() -> dict[str, object]:
    return {
        "admissibility_basis_id": "source-body-reception-admissibility-basis-001",
        "admissibility_basis_declared": True,
        "admissible_for_later_reception_review_only": True,
        "admissibility_is_not_authorization": True,
        "admissibility_does_not_authorize_reception": True,
        "admissibility_does_not_receive_source": True,
        "admissibility_does_not_create_adoption": True,
        "admissibility_does_not_create_authority": True,
        "admissibility_does_not_create_currentness": True,
        "admissibility_does_not_create_validation": True,
        "admissibility_does_not_create_invalidation": True,
        "admissibility_does_not_create_operation_permission": True,
        "admissibility_does_not_create_governance": True,
        "admissibility_does_not_create_publication_flow": True,
        "admissibility_does_not_create_public_readiness": True,
        "admissibility_does_not_claim_final_completion": True,
        "admissibility_does_not_authorize_continuation": True,
        "admissibility_does_not_authorize_follow_on_work": True,
        "non_capture_requires_separate_boundary": True,
        "recognition_requires_separate_boundary": True,
    }


def review_readiness_limits() -> dict[str, object]:
    return {
        "review_readiness_limits_id": "review-readiness-limits-001",
        "review_readiness_limits_declared": True,
        "eligible_for_reception_review_only": True,
        "admissible_for_reception_review_only": True,
        "non_capture_requires_separate_boundary": True,
        "recognition_requires_separate_boundary": True,
    }


def declared_eligibility_request(
    selected_role: dict[str, object] | None = None,
    *,
    eligibility_scope: object | None = None,
    **overrides: object,
) -> dict[str, object]:
    role_result = (
        selected_receiving_context_role_result()
        if selected_role is None
        else selected_role
    )
    metadata = role_result.get("source_body_reception_receiving_context_role_metadata", {})
    role_id = None
    if isinstance(metadata, dict):
        role_id = metadata.get("source_body_reception_receiving_context_role_result_id")
    request: dict[str, object] = {
        "eligibility_request_id": "source-body-reception-eligibility-001",
        "eligibility_question": (
            "Is this declared source-body reception request eligible and admissible for later reception-family review?"
        ),
        "eligibility_intent": "RECORD_SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY",
        "selected_receiving_context_role_result": role_result,
        "selected_receiving_context_role_result_id": role_id,
        "selected_receiving_context_role_result_outcome": role_result.get("outcome"),
        "eligibility_basis": eligibility_basis(),
        "admissibility_basis": admissibility_basis(),
        "eligibility_scope": list(SUPPORTED_SCOPE)
        if eligibility_scope is None
        else eligibility_scope,
        "review_readiness_limits": review_readiness_limits(),
        "requested_eligibility_outcome": ELIGIBLE,
        "additional_basis_context": {},
        "not_eligible_basis": None,
        "declared_non_claims": false_eligibility_non_claims(),
    }
    request.update(overrides)
    return request


def resolve(request: object | None) -> dict[str, object]:
    return resolver.resolve_source_body_reception_eligibility_admissibility_boundary(
        declared_eligibility_request=request
    )


class EligibilityAssertions:
    def assert_outcome_family(self, result: dict[str, object]) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_block(self, request: object, code: str) -> dict[str, object]:
        result = resolve(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        self.assertFalse(
            result["non_claims"]["source_body_reception_eligible_admissible_for_review"]
        )
        self.assert_outcome_family(result)
        return result

    def assert_required_non_claims_false(self, result: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
            self.assertIs(result["non_claims"][key], False, key)

    def assert_no_eligibility_collapse(self, section: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, section, key)
            self.assertIs(section[key], False, key)


class TestSourceBodyReceptionEligibilityAdmissible(
    EligibilityAssertions, unittest.TestCase
):
    def setUp(self) -> None:
        self.request = declared_eligibility_request()
        self.request_before = copy.deepcopy(self.request)
        self.result = resolve(self.request)

    def test_successful_eligibility_result_shape_and_statement(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(self.result))
        self.assertEqual(ELIGIBLE, self.result["outcome"])
        self.assertIsNone(self.result["block"]["block_code"])
        self.assertIsNone(self.result["block"]["block_reason"])
        self.assertEqual(
            0,
            self.result["source_body_reception_eligibility_summary"][
                "failed_check_count"
            ],
        )

        statement = self.result["eligibility_statement"]
        for key in (
            "source_body_reception_eligible_admissible_for_review",
            "selected_receiving_context_role_result_preserved",
            "selected_receiving_context_role_result_recorded",
            "selected_receiving_context_role_result_failed_check_count_zero",
            "selected_identity_preservation_result_preserved",
            "selected_reception_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "selected_source_body_surface_remains_source",
            "selected_surface_is_not_whole_body_by_default",
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "receiving_context_role_preserved",
            "receiving_context_role_remains_bounded",
            "role_is_not_reception",
            "role_is_not_authorization",
            "role_is_not_source_receipt",
            "role_is_not_authority_currentness_adoption_validation_invalidation",
            "reception_class_preserved",
            "reception_purpose_preserved",
            "reception_limits_preserved",
            "eligibility_basis_declared",
            "admissibility_basis_declared",
            "review_readiness_limits_declared",
            "eligible_for_reception_review_only",
            "admissible_for_reception_review_only",
            "eligibility_is_not_reception",
            "admissibility_is_not_authorization",
            "eligibility_does_not_receive_source",
            "non_capture_requires_separate_boundary",
            "recognition_requires_separate_boundary",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_no_eligibility_collapse(statement)
        self.assert_required_non_claims_false(self.result)
        self.assertIs(
            self.result["non_claims"][
                "source_body_reception_eligible_admissible_for_review"
            ],
            True,
        )
        self.assertEqual(self.request_before, self.request)

    def test_metadata_and_declared_question_are_bounded(self) -> None:
        metadata = self.result["source_body_reception_eligibility_metadata"]
        for key in (
            "source_body_reception_eligibility_result_id",
            "source_body_reception_eligibility_result_type",
            "source_body_reception_eligibility_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["source_body_reception_eligibility_result_version"])
        self.assertEqual(
            "resolve_source_body_reception_eligibility_admissibility_boundary",
            metadata["resolver_module"],
        )

        question = self.result["declared_eligibility_question"]
        self.assertEqual(self.request["eligibility_request_id"], question["eligibility_request_id"])
        self.assertEqual(self.request["eligibility_question"], question["eligibility_question"])
        self.assertEqual(
            "RECORD_SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY",
            question["eligibility_intent"],
        )
        self.assertEqual(ROLE_RECORDED, question["selected_receiving_context_role_result_outcome"])
        self.assertEqual("source-body-surface-001", question["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", question["selected_source_body_surface_type"])
        self.assertEqual("receiving-context-001", question["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", question["receiving_context_type"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", question["receiving_context_role_class"])
        self.assertEqual("REFERENCE_RECEPTION", question["reception_class"])
        self.assertTrue(question["reception_purpose"])
        self.assertIs(question["eligibility_is_not_reception"], True)
        self.assertIs(question["admissibility_is_not_authorization"], True)
        self.assertIs(question["non_capture_requires_separate_boundary"], True)
        self.assertIs(question["recognition_requires_separate_boundary"], True)

    def test_selected_receiving_context_role_result_is_preserved_not_upgraded(self) -> None:
        selected = self.result["selected_receiving_context_role_result"]
        self.assertEqual(
            "source_body_reception_receiving_context_role__role-001",
            selected["selected_receiving_context_role_result_id"],
        )
        self.assertEqual(ROLE_RECORDED, selected["selected_receiving_context_role_result_outcome"])
        self.assertIs(selected["selected_receiving_context_role_result_recorded"], True)
        self.assertIs(
            selected["selected_receiving_context_role_result_failed_check_count_zero"],
            True,
        )
        self.assertIs(selected["selected_identity_preservation_result_preserved"], True)
        self.assertIs(selected["selected_reception_request_declaration_result_preserved"], True)
        self.assertIs(selected["selected_source_body_surface_preserved_by_role"], True)
        self.assertIs(selected["selected_source_body_surface_remains_source_by_role"], True)
        self.assertIs(selected["selected_surface_is_not_whole_body_by_default_by_role"], True)
        self.assertIs(selected["receiving_context_preserved_by_role"], True)
        self.assertIs(selected["receiving_context_remains_context_only_by_role"], True)
        self.assertIs(selected["receiving_context_is_not_source_by_role"], True)
        self.assertIs(selected["receiving_context_is_not_authority_by_role"], True)
        self.assertIs(selected["receiving_context_is_not_current_by_role"], True)
        self.assertIs(selected["receiving_context_role_preserved_by_role"], True)
        self.assertIs(selected["receiving_context_role_remains_bounded_by_role"], True)
        for key in (
            "receiving_context_role_is_not_reception_by_role",
            "receiving_context_role_is_not_authorization_by_role",
            "receiving_context_role_is_not_source_receipt_by_role",
            "receiving_context_role_is_not_source_authority_by_role",
            "receiving_context_role_is_not_currentness_by_role",
            "receiving_context_role_is_not_adoption_by_role",
            "receiving_context_role_is_not_validation_by_role",
            "receiving_context_role_is_not_invalidation_by_role",
            "receiving_context_role_is_not_operation_permission_by_role",
            "receiving_context_role_is_not_publication_flow_by_role",
            "role_result_did_not_recognize_reception",
            "role_result_did_not_authorize_reception",
            "role_result_did_not_receive_source",
            "role_result_did_not_mutate_replay_or_merge",
        ):
            self.assertIs(selected[key], True, key)
        for key, value in selected["selected_receiving_context_role_result"]["non_claims"].items():
            self.assertIs(value, False, key)

    def test_selected_surface_receiving_context_and_bases_are_preserved(self) -> None:
        surface = self.result["selected_source_body_surface"]
        self.assertEqual("source-body-surface-001", surface["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", surface["selected_source_body_surface_type"])
        self.assertEqual("reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md", surface["selected_source_body_surface_path"])
        self.assertEqual("reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md", surface["selected_source_body_surface_reference"])
        self.assertTrue(surface["source_body_identity_basis"])
        self.assertTrue(surface["source_body_lineage_basis"])
        self.assertIs(surface["selected_source_body_surface_remains_source"], True)
        self.assertIs(surface["selected_surface_is_not_whole_body_by_default"], True)
        self.assertIs(surface["selected_source_body_surface_not_received"], True)
        self.assertIs(surface["selected_source_body_surface_not_adopted"], True)
        self.assertIs(surface["selected_source_body_surface_not_replaced"], True)
        self.assertIs(surface["selected_source_body_surface_not_validated_by_receiving_context"], True)
        self.assertIs(surface["selected_source_body_surface_not_invalidated_by_receiving_context"], True)

        context = self.result["receiving_context"]
        self.assertEqual("receiving-context-001", context["receiving_context_id"])
        self.assertEqual("bounded receiving context", context["receiving_context_name"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", context["receiving_context_type"])
        self.assertIs(context["receiving_context_preserved"], True)
        self.assertIs(context["receiving_context_remains_context_only"], True)
        for key in (
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "receiving_context_is_not_receiver",
            "receiving_context_is_not_adopter",
            "receiving_context_is_not_validator",
            "receiving_context_is_not_invalidator",
            "receiving_context_is_not_operator",
            "receiving_context_did_not_validate_source",
            "receiving_context_did_not_invalidate_source",
            "receiving_context_did_not_create_governance",
            "receiving_context_did_not_create_operation_permission",
            "receiving_context_did_not_open_publication_flow",
        ):
            self.assertIs(context[key], True, key)

        eligibility = self.result["eligibility_basis"]
        self.assertTrue(eligibility["selected_receiving_context_role_result"])
        self.assertTrue(eligibility["selected_identity_preservation_result"])
        self.assertTrue(eligibility["selected_request_declaration_result"])
        self.assertTrue(eligibility["selected_source_body_surface"])
        self.assertTrue(eligibility["source_body_identity_basis"])
        self.assertTrue(eligibility["source_body_lineage_basis"])
        self.assertTrue(eligibility["receiving_context"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", eligibility["receiving_context_type"])
        self.assertEqual("REFERENCE_RECEPTION", eligibility["reception_class"])
        self.assertTrue(eligibility["reception_purpose"])
        self.assertTrue(eligibility["reception_limits"])
        self.assertTrue(eligibility["selected_receiving_context_role"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", eligibility["receiving_context_role_class"])
        self.assertTrue(eligibility["receiving_context_role_limits"])
        self.assertEqual(self.request["eligibility_basis"], eligibility["declared_eligibility_basis"])
        for key in (
            "eligible_for_later_reception_review_only",
            "eligibility_is_not_reception",
            "eligibility_is_not_recognition",
            "eligibility_is_not_source_receipt",
            "eligibility_does_not_decide_non_capture",
            "eligibility_does_not_decide_recognition",
            "source_body_surface_remains_source",
            "receiving_context_remains_context_only",
        ):
            self.assertIs(eligibility[key], True, key)

        admissibility = self.result["admissibility_basis"]
        self.assertEqual(self.request["admissibility_basis"], admissibility["declared_admissibility_basis"])
        for key in (
            "admissible_for_later_reception_review_only",
            "admissibility_is_not_authorization",
            "admissibility_does_not_authorize_reception",
            "admissibility_does_not_receive_source",
            "admissibility_does_not_create_adoption",
            "admissibility_does_not_create_authority",
            "admissibility_does_not_create_currentness",
            "admissibility_does_not_create_validation",
            "admissibility_does_not_create_invalidation",
            "admissibility_does_not_create_operation_permission",
            "admissibility_does_not_create_governance",
            "admissibility_does_not_create_publication_flow",
            "admissibility_does_not_create_public_readiness",
            "admissibility_does_not_claim_final_completion",
            "admissibility_does_not_authorize_continuation",
            "admissibility_does_not_authorize_follow_on_work",
            "non_capture_requires_separate_boundary",
            "recognition_requires_separate_boundary",
        ):
            self.assertIs(admissibility[key], True, key)

    def test_supported_scope_values_and_checks_are_recorded(self) -> None:
        for value in SUPPORTED_SCOPE:
            with self.subTest(scope=value):
                result = resolve(declared_eligibility_request(eligibility_scope=[value]))
                self.assertEqual(ELIGIBLE, result["outcome"])
                scope = result["eligibility_scope"]
                self.assertEqual([value], scope["selected_eligibility_scope_values"])
                self.assertIs(scope["all_selected_scope_values_supported"], True)

        checks = self.result["eligibility_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertIs(check["passed"], True, check["check_name"])
        names = {check["check_name"] for check in checks}
        for expected in (
            "eligibility / admissibility question declared",
            "eligibility / admissibility intent supported",
            "selected receiving-context role result present",
            "selected receiving-context role outcome declared",
            "selected receiving-context role outcome recorded",
            "selected receiving-context role failed check count zero",
            "selected identity preservation result preserved",
            "selected request declaration result preserved",
            "selected source-body surface preserved",
            "selected source-body surface remains source",
            "selected surface is not whole body by default",
            "receiving context preserved",
            "receiving context remains context only",
            "receiving context is not source",
            "receiving context is not authority",
            "receiving context is not current",
            "receiving-context role preserved",
            "receiving-context role remains bounded",
            "receiving-context role is not reception",
            "receiving-context role is not authorization",
            "receiving-context role is not source receipt",
            "receiving-context role is not authority/currentness/adoption/validation/invalidation",
            "reception class preserved",
            "reception purpose preserved",
            "reception limits preserved",
            "eligibility basis declared",
            "admissibility basis declared",
            "review-readiness limits declared",
            "eligibility is not reception",
            "admissibility is not authorization",
            "eligibility does not receive source",
            "eligibility does not create adoption",
            "eligibility does not create authority",
            "eligibility does not create currentness",
            "eligibility does not create validation",
            "eligibility does not create invalidation",
            "eligibility does not create operation permission",
            "eligibility does not create governance",
            "eligibility does not create publication flow",
            "eligibility does not create public readiness",
            "eligibility does not claim final completion",
            "eligibility does not authorize continuation",
            "eligibility does not authorize follow-on work",
            "non-capture remains future work",
            "recognition remains future work",
            "no mutation/replay/merge",
            "non-claims remain false",
        ):
            self.assertIn(expected, names)

    def test_non_meaning_remaining_open_non_claims_and_summary(self) -> None:
        non_meaning = self.result["eligibility_non_meaning"]
        for key in (
            "reception_recognized",
            "reception_authorized",
            "source_received",
            "source_adopted",
            "source_validated",
            "source_invalidated",
            "source_replaced",
            "receiving_context_became_source",
            "receiving_context_became_authority",
            "receiving_context_became_current",
            "receiving_context_became_receiver",
            "receiving_context_became_adopter",
            "receiving_context_became_validator",
            "receiving_context_became_invalidator",
            "receiving_context_became_operator",
            "receiving_context_governance_created",
            "standing_created",
            "standing_propagated",
            "vessel_relation_created",
            "derivative_relation_created",
            "operation_permission_created",
            "non_capture_passed",
            "reception_recognition_passed",
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
        ):
            self.assertIs(non_meaning[key], True, key)

        remains_open = self.result["what_remains_open"]
        for key in (
            "source_body_reception_eligibility_admissibility_test",
            "source_body_reception_eligibility_admissibility_live_artifact",
            "non_capture_non_adoption_non_currentness_boundary",
            "source_body_reception_recognition_boundary",
            "source_body_reception_receipt_exhaustion_boundary",
            "source_body_reception_conformance_boundary",
            "source_body_reception_closure_boundary",
            "derivative_reception",
            "vessel_relation",
            "adoption",
            "authority_creation",
            "currentness_creation",
            "standing_creation",
            "operation_permission",
            "receiving_context_governance",
            "public_readiness",
            "final_completion",
            "follow_on_work",
            "open_means_not_scheduled",
            "open_means_not_authorized",
            "open_means_not_executed",
        ):
            self.assertIs(remains_open[key], True, key)

        summary = self.result["source_body_reception_eligibility_summary"]
        helper_summary = resolver.build_source_body_reception_eligibility_admissibility_summary(
            self.result
        )
        self.assertEqual(summary, helper_summary)
        self.assertEqual(ELIGIBLE, summary["outcome"])
        self.assertIs(summary["eligible_admissible"], True)
        self.assertIs(summary["not_eligible_or_admissible"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertEqual("source-body-surface-001", summary["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", summary["selected_source_body_surface_type"])
        self.assertEqual("receiving-context-001", summary["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", summary["receiving_context_type"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", summary["receiving_context_role_class"])
        self.assertEqual("REFERENCE_RECEPTION", summary["reception_class"])
        self.assertTrue(summary["reception_purpose"])
        for key in (
            "selected_receiving_context_role_result_preserved",
            "selected_receiving_context_role_result_recorded",
            "selected_receiving_context_role_result_failed_check_count_zero",
            "selected_identity_preservation_result_preserved",
            "selected_reception_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "selected_source_body_surface_remains_source",
            "selected_surface_is_not_whole_body_by_default",
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "receiving_context_role_preserved",
            "receiving_context_role_remains_bounded",
            "role_is_not_reception",
            "role_is_not_authorization",
            "role_is_not_source_receipt",
            "role_is_not_source_authority",
            "role_is_not_currentness",
            "role_is_not_adoption",
            "role_is_not_validation",
            "role_is_not_invalidation",
            "role_is_not_authority_currentness_adoption_validation_invalidation",
            "reception_class_preserved",
            "reception_purpose_preserved",
            "reception_limits_preserved",
            "eligibility_basis_declared",
            "admissibility_basis_declared",
            "review_readiness_limits_declared",
            "eligible_for_review_only",
            "admissible_for_review_only",
            "eligibility_is_not_reception",
            "admissibility_is_not_authorization",
            "no_source_received",
            "non_capture_future",
            "recognition_future",
            "no_reception_recognized",
            "no_reception_authorized",
            "no_source_validation",
            "no_source_invalidation",
            "no_source_replacement",
            "no_adoption",
            "no_authority",
            "no_currentness",
            "no_standing",
            "no_vessel_relation",
            "no_derivative_relation",
            "no_operation_permission",
            "no_governance",
            "no_publication_flow",
            "no_public_readiness",
            "no_final_completion",
            "no_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        expected_non_claims = false_eligibility_non_claims()
        expected_non_claims["source_body_reception_eligible_admissible_for_review"] = True
        self.assertEqual(expected_non_claims, summary["key_non_claims"])


class TestEligibilityAlternateOutcomes(EligibilityAssertions, unittest.TestCase):
    def test_requires_additional_basis_preserves_missing_basis_as_unexecuted(self) -> None:
        context = {
            "reason": "eligibility basis too generic",
            "review_readiness_limits_unclear": True,
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
        request = declared_eligibility_request(
            requested_eligibility_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context=context,
        )
        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, result["outcome"])
        self.assertEqual(context, result["additional_basis_required"]["additional_basis_context"])
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        self.assertIs(result["additional_basis_required"]["additional_basis_scheduled"], False)
        self.assertIs(result["additional_basis_required"]["additional_basis_authorized"], False)
        self.assertIs(result["additional_basis_required"]["additional_basis_executed"], False)
        self.assertIs(result["additional_basis_required"]["missing_basis_does_not_create_governance"], True)
        self.assertIs(result["additional_basis_required"]["missing_basis_does_not_decide_non_capture"], True)
        self.assertIs(result["additional_basis_required"]["missing_basis_does_not_decide_recognition"], True)
        self.assert_required_non_claims_false(result)
        self.assertFalse(result["non_claims"]["source_body_reception_eligible_admissible_for_review"])
        self.assertEqual(before, request)

    def test_not_eligible_preserves_readable_basis_without_repair(self) -> None:
        not_eligible = {
            "reason": "recognition cannot be kept separate from admissibility",
            "repair_authorized": False,
        }
        request = declared_eligibility_request(
            requested_eligibility_outcome=NOT_ELIGIBLE,
            not_eligible_basis=not_eligible,
        )
        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(NOT_ELIGIBLE, result["outcome"])
        self.assertEqual(not_eligible, result["not_eligible_basis"]["not_eligible_basis"])
        self.assertIs(result["not_eligible_basis"]["source_body_reception_not_eligible_or_admissible"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_mutate"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_repair"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_authorize"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_receive_source"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_replace_source"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_validate_source"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_invalidate_source"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_create_currentness"], True)
        self.assertIs(result["not_eligible_basis"]["not_eligible_does_not_recognize_reception"], True)
        self.assert_required_non_claims_false(result)
        self.assertFalse(result["non_claims"]["source_body_reception_eligible_admissible_for_review"])
        self.assertEqual(before, request)


class TestEligibilityHelpersAndPaths(EligibilityAssertions, unittest.TestCase):
    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        role_result = selected_receiving_context_role_result()
        eligible_basis = eligibility_basis()
        admissible_basis = admissibility_basis()
        limits = review_readiness_limits()
        request = resolver.build_declared_source_body_reception_eligibility_admissibility_request(
            "eligibility-builder-001",
            "Is this declared request eligible and admissible for later review?",
            role_result,
            eligible_basis,
            admissible_basis,
            list(SUPPORTED_SCOPE),
            selected_receiving_context_role_result_id=(
                "source_body_reception_receiving_context_role__role-001"
            ),
            selected_receiving_context_role_result_outcome=ROLE_RECORDED,
            review_readiness_limits=limits,
            additional_basis_context={"reason": "none"},
            not_eligible_basis={"reason": "none"},
        )
        self.assertEqual("eligibility-builder-001", request["eligibility_request_id"])
        self.assertEqual(role_result, request["selected_receiving_context_role_result"])
        self.assertEqual(eligible_basis, request["eligibility_basis"])
        self.assertEqual(admissible_basis, request["admissibility_basis"])
        self.assertEqual(list(SUPPORTED_SCOPE), request["eligibility_scope"])
        self.assertEqual(limits, request["review_readiness_limits"])
        self.assertEqual({"reason": "none"}, request["additional_basis_context"])
        self.assertEqual({"reason": "none"}, request["not_eligible_basis"])
        self.assertEqual(false_eligibility_non_claims(), request["declared_non_claims"])
        result = resolve(request)
        self.assertEqual(ELIGIBLE, result["outcome"])

    def test_path_based_selected_receiving_context_role_result_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            role_path = Path(temp_dir) / "selected_role.json"
            role_payload = json.dumps(selected_receiving_context_role_result(), indent=2)
            role_path.write_text(role_payload, encoding="utf-8")
            request = declared_eligibility_request(selected_role={})
            request.pop("selected_receiving_context_role_result")
            request["selected_receiving_context_role_result_path"] = str(role_path)
            result = resolve(request)
            self.assertEqual(ELIGIBLE, result["outcome"])
            selected = result["selected_receiving_context_role_result"]
            self.assertEqual(str(role_path), selected["selected_receiving_context_role_result_path"])
            self.assertEqual(
                "source_body_reception_receiving_context_role__role-001",
                selected["selected_receiving_context_role_result_id"],
            )
            self.assertEqual(ROLE_RECORDED, selected["selected_receiving_context_role_result_outcome"])
            self.assertEqual(role_payload, role_path.read_text(encoding="utf-8"))

    def test_path_based_eligibility_request_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request_path = Path(temp_dir) / "eligibility_request.json"
            request_path.write_text(
                json.dumps(declared_eligibility_request(), indent=2),
                encoding="utf-8",
            )
            path_result = resolver.resolve_source_body_reception_eligibility_admissibility_boundary_from_path(
                request_path
            )
            mapping_result = resolve(declared_eligibility_request())
            self.assertEqual(ELIGIBLE, path_result["outcome"])
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                str(request_path),
                path_result["declared_eligibility_question"][
                    "declared_eligibility_request_path"
                ],
            )

    def test_write_behavior_uses_additive_temp_paths_and_suffixes(self) -> None:
        result = resolve(declared_eligibility_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "eligibility_result.json"
            written = resolver.write_source_body_reception_eligibility_admissibility_result(
                result, explicit_path
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))

            default_root = Path(temp_dir) / "eligibility-root"
            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY_BOUNDARY_ROOT",
                default_root,
            ):
                first = resolver.write_source_body_reception_eligibility_admissibility_result(result)
                second = resolver.write_source_body_reception_eligibility_admissibility_result(result)
            self.assertEqual(default_root, first.parent)
            self.assertEqual(default_root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertIn("__source_body_reception_eligibility_admissibility_result", first.name)
            self.assertNotIn("source_body_reception_receiving_context_role", str(first))
            self.assertNotIn("source_body_reception_recognition", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_eligibility_request()
        request_before = copy.deepcopy(request)
        role_before = copy.deepcopy(request["selected_receiving_context_role_result"])
        identity_before = copy.deepcopy(
            request["selected_receiving_context_role_result"][
                "selected_identity_preservation_result"
            ]
        )
        declaration_before = copy.deepcopy(
            request["selected_receiving_context_role_result"][
                "receiving_context_role_basis"
            ]["selected_reception_request_declaration_result"]
        )
        surface_before = copy.deepcopy(
            request["selected_receiving_context_role_result"]["selected_source_body_surface"]
        )
        context_before = copy.deepcopy(
            request["selected_receiving_context_role_result"]["receiving_context"]
        )
        eligibility_before = copy.deepcopy(request["eligibility_basis"])
        admissibility_before = copy.deepcopy(request["admissibility_basis"])
        scope_before = copy.deepcopy(request["eligibility_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(ELIGIBLE, first["outcome"])
        self.assertEqual(ELIGIBLE, second["outcome"])
        self.assertEqual(request_before, request)
        self.assertEqual(role_before, request["selected_receiving_context_role_result"])
        self.assertEqual(
            identity_before,
            request["selected_receiving_context_role_result"][
                "selected_identity_preservation_result"
            ],
        )
        self.assertEqual(
            declaration_before,
            request["selected_receiving_context_role_result"][
                "receiving_context_role_basis"
            ]["selected_reception_request_declaration_result"],
        )
        self.assertEqual(
            surface_before,
            request["selected_receiving_context_role_result"]["selected_source_body_surface"],
        )
        self.assertEqual(
            context_before,
            request["selected_receiving_context_role_result"]["receiving_context"],
        )
        self.assertEqual(eligibility_before, request["eligibility_basis"])
        self.assertEqual(admissibility_before, request["admissibility_basis"])
        self.assertEqual(scope_before, request["eligibility_scope"])

        with tempfile.TemporaryDirectory() as temp_dir:
            role_path = Path(temp_dir) / "selected_role.json"
            role_payload = json.dumps(selected_receiving_context_role_result(), indent=2)
            role_path.write_text(role_payload, encoding="utf-8")
            path_request = declared_eligibility_request(selected_role={})
            path_request.pop("selected_receiving_context_role_result")
            path_request["selected_receiving_context_role_result_path"] = str(role_path)
            path_result = resolve(path_request)
            self.assertEqual(ELIGIBLE, path_result["outcome"])
            self.assertEqual(role_payload, role_path.read_text(encoding="utf-8"))


class TestEligibilityBlocking(EligibilityAssertions, unittest.TestCase):
    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        self.assert_block(
            declared_eligibility_request(
                eligibility_intent="BLOCK_SOURCE_BODY_RECEPTION_ELIGIBILITY_REVIEW"
            ),
            "RECEPTION_ELIGIBILITY_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assert_block(None, "RECEPTION_ELIGIBILITY_QUESTION_UNDECLARED")
        self.assert_block("not a mapping", "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_MALFORMED")

    def test_request_path_unreadable_and_malformed_cases_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing.json"
            result = resolver.resolve_source_body_reception_eligibility_admissibility_boundary_from_path(
                missing
            )
            self.assertEqual(BLOCKED, result["outcome"])
            self.assertEqual(
                "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_UNREADABLE",
                result["block"]["block_code"],
            )

            malformed = Path(temp_dir) / "malformed.json"
            malformed.write_text("{not-json", encoding="utf-8")
            result = resolver.resolve_source_body_reception_eligibility_admissibility_boundary_from_path(
                malformed
            )
            self.assertEqual(
                "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_MALFORMED",
                result["block"]["block_code"],
            )

            array_payload = Path(temp_dir) / "array.json"
            array_payload.write_text("[]", encoding="utf-8")
            result = resolver.resolve_source_body_reception_eligibility_admissibility_boundary_from_path(
                array_payload
            )
            self.assertEqual(
                "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_MALFORMED",
                result["block"]["block_code"],
            )

    def test_selected_receiving_context_role_path_unreadable_and_malformed_cases_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing-selected.json"
            request = declared_eligibility_request(selected_role={})
            request.pop("selected_receiving_context_role_result")
            request["selected_receiving_context_role_result_path"] = str(missing)
            self.assert_block(request, "RECEIVING_CONTEXT_ROLE_RESULT_UNREADABLE")

            malformed = Path(temp_dir) / "malformed-selected.json"
            malformed.write_text("{not-json", encoding="utf-8")
            request = declared_eligibility_request(selected_role={})
            request.pop("selected_receiving_context_role_result")
            request["selected_receiving_context_role_result_path"] = str(malformed)
            self.assert_block(request, "RECEIVING_CONTEXT_ROLE_RESULT_MALFORMED")

            array_payload = Path(temp_dir) / "array-selected.json"
            array_payload.write_text("[]", encoding="utf-8")
            request = declared_eligibility_request(selected_role={})
            request.pop("selected_receiving_context_role_result")
            request["selected_receiving_context_role_result_path"] = str(array_payload)
            self.assert_block(request, "RECEIVING_CONTEXT_ROLE_RESULT_MALFORMED")

    def test_selected_receiving_context_role_result_issues_block(self) -> None:
        missing_outcome = selected_receiving_context_role_result()
        missing_outcome.pop("outcome")
        missing_outcome["source_body_reception_receiving_context_role_summary"].pop("outcome")
        self.assert_block(
            declared_eligibility_request(selected_role=missing_outcome),
            "RECEIVING_CONTEXT_ROLE_RESULT_OUTCOME_MISSING",
        )

        wrong_outcome = selected_receiving_context_role_result(
            outcome="SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_NOT_RECORDED"
        )
        wrong_outcome["source_body_reception_receiving_context_role_summary"][
            "outcome"
        ] = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_NOT_RECORDED"
        self.assert_block(
            declared_eligibility_request(selected_role=wrong_outcome),
            "RECEIVING_CONTEXT_ROLE_RESULT_NOT_RECORDED",
        )

        failed_checks = selected_receiving_context_role_result()
        failed_checks["source_body_reception_receiving_context_role_summary"][
            "failed_check_count"
        ] = 1
        self.assert_block(
            declared_eligibility_request(selected_role=failed_checks),
            "RECEIVING_CONTEXT_ROLE_RESULT_HAS_FAILED_CHECKS",
        )

    def test_missing_required_selected_basis_blocks(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []

        role_result = selected_receiving_context_role_result()
        role_result.pop("selected_identity_preservation_result")
        role_result["receiving_context_role_basis"].pop("selected_identity_preservation_result")
        cases.append(("IDENTITY_PRESERVATION_RESULT_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result["receiving_context_role_basis"].pop(
            "selected_reception_request_declaration_result"
        )
        role_result["selected_identity_preservation_result"].pop(
            "selected_reception_request_declaration_result"
        )
        cases.append(("RECEPTION_REQUEST_DECLARATION_RESULT_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result.pop("selected_source_body_surface")
        role_result["receiving_context_role_basis"].pop("selected_source_body_surface")
        cases.append(("SELECTED_SOURCE_BODY_SURFACE_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result.pop("receiving_context")
        role_result["receiving_context_role_basis"].pop("receiving_context")
        role_result["receiving_context_role_basis"].pop("receiving_context_type")
        cases.append(("RECEIVING_CONTEXT_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result["receiving_context"].pop("receiving_context_type")
        role_result["receiving_context_role_basis"].pop("receiving_context_type")
        role_result["receiving_context_role_basis"]["receiving_context"].pop(
            "receiving_context_type"
        )
        cases.append(("RECEIVING_CONTEXT_TYPE_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result.pop("receiving_context_role")
        role_result["receiving_context_role_basis"].pop("declared_receiving_context_role")
        cases.append(("RECEIVING_CONTEXT_ROLE_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result["receiving_context_role"].pop("receiving_context_role_class")
        role_result["receiving_context_role_basis"].pop("receiving_context_role_class")
        role_result["source_body_reception_receiving_context_role_summary"].pop(
            "receiving_context_role_class"
        )
        cases.append(("RECEIVING_CONTEXT_ROLE_CLASS_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result["receiving_context_role_basis"].pop("reception_class")
        role_result["source_body_reception_receiving_context_role_summary"].pop(
            "reception_class"
        )
        cases.append(("RECEPTION_CLASS_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result["receiving_context_role_basis"].pop("reception_purpose")
        role_result["source_body_reception_receiving_context_role_summary"].pop(
            "reception_purpose"
        )
        cases.append(("RECEPTION_PURPOSE_MISSING", role_result))

        role_result = selected_receiving_context_role_result()
        role_result["receiving_context_role_basis"].pop("reception_limits")
        cases.append(("RECEPTION_LIMITS_MISSING", role_result))

        for code, role_result in cases:
            with self.subTest(code=code):
                self.assert_block(declared_eligibility_request(selected_role=role_result), code)

        request = declared_eligibility_request()
        request.pop("eligibility_basis")
        self.assert_block(request, "ELIGIBILITY_BASIS_MISSING")

        request = declared_eligibility_request()
        request.pop("admissibility_basis")
        self.assert_block(request, "ADMISSIBILITY_BASIS_MISSING")

        request = declared_eligibility_request()
        request.pop("review_readiness_limits")
        self.assert_block(request, "REVIEW_READINESS_LIMITS_MISSING")

    def test_malformed_surface_context_and_unsupported_scope_block(self) -> None:
        self.assert_block(
            declared_eligibility_request(selected_source_body_surface=["bad"]),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        )
        self.assert_block(
            declared_eligibility_request(receiving_context=["bad"]),
            "RECEIVING_CONTEXT_MALFORMED",
        )
        self.assert_block(
            declared_eligibility_request(eligibility_scope=["UNSUPPORTED_SCOPE"]),
            "UNSUPPORTED_RECEPTION_ELIGIBILITY_SCOPE",
        )

    def test_eligibility_collapse_flags_block(self) -> None:
        cases = {
            "reception_recognized": "RECEPTION_ELIGIBILITY_RECOGNIZES_RECEPTION",
            "reception_authorized": "RECEPTION_ELIGIBILITY_AUTHORIZES_RECEPTION",
            "source_received": "RECEPTION_ELIGIBILITY_RECEIVES_SOURCE",
            "receiving_context_governance_created": "RECEPTION_ELIGIBILITY_CREATES_GOVERNANCE",
            "receiving_context_became_source": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_SOURCE",
            "receiving_context_became_authority": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_AUTHORITY",
            "receiving_context_became_current": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_CURRENT",
            "receiving_context_became_receiver": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_RECEIVER",
            "receiving_context_became_adopter": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_ADOPTER",
            "receiving_context_became_validator": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_VALIDATOR",
            "receiving_context_became_invalidator": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_INVALIDATOR",
            "receiving_context_became_operator": "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_OPERATOR",
            "source_validated_by_receiving_context": "RECEPTION_ELIGIBILITY_VALIDATES_SOURCE",
            "source_invalidated_by_receiving_context": "RECEPTION_ELIGIBILITY_INVALIDATES_SOURCE",
            "source_replaced": "RECEPTION_ELIGIBILITY_REPLACES_SOURCE",
            "adoption_created": "RECEPTION_ELIGIBILITY_CREATES_ADOPTION",
            "authority_created": "RECEPTION_ELIGIBILITY_CREATES_AUTHORITY",
            "currentness_created": "RECEPTION_ELIGIBILITY_CREATES_CURRENTNESS",
            "standing_created": "RECEPTION_ELIGIBILITY_CREATES_STANDING",
            "standing_propagated": "RECEPTION_ELIGIBILITY_CREATES_STANDING_PROPAGATION",
            "vessel_relation_created": "RECEPTION_ELIGIBILITY_CREATES_VESSEL_RELATION",
            "derivative_relation_created": "RECEPTION_ELIGIBILITY_CREATES_DERIVATIVE_RELATION",
            "operation_permission_created": "RECEPTION_ELIGIBILITY_CREATES_OPERATION_PERMISSION",
            "public_launch_readiness_created": "RECEPTION_ELIGIBILITY_CREATES_PUBLIC_READINESS",
            "final_completion_claimed": "RECEPTION_ELIGIBILITY_CLAIMS_FINAL_COMPLETION",
            "follow_on_work_authorized": "RECEPTION_ELIGIBILITY_AUTHORIZES_FOLLOW_ON_WORK",
            "continuation_authorized": "RECEPTION_ELIGIBILITY_AUTHORIZES_CONTINUATION",
            "publication_flow_opened": "RECEPTION_ELIGIBILITY_OPENS_PUBLICATION_FLOW",
            "non_capture_passed": "RECEPTION_ELIGIBILITY_CLAIMS_NON_CAPTURE_PASSED",
            "reception_recognition_passed": "RECEPTION_ELIGIBILITY_CLAIMS_RECOGNITION_PASSED",
        }
        for field, code in cases.items():
            with self.subTest(field=field):
                request = declared_eligibility_request()
                request["eligibility_basis"][field] = True
                self.assert_block(request, code)

    def test_mutation_replay_merge_and_non_claim_issues_block(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = declared_eligibility_request()
                request["eligibility_basis"][field] = True
                self.assert_block(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

        request = declared_eligibility_request()
        request["declared_non_claims"].pop("reception_recognized")
        self.assert_block(request, "NON_CLAIM_MISSING_OR_FLIPPED")

        request = declared_eligibility_request()
        request["declared_non_claims"]["reception_recognized"] = True
        self.assert_block(request, "RECEPTION_ELIGIBILITY_RECOGNIZES_RECEPTION")


if __name__ == "__main__":
    unittest.main()
