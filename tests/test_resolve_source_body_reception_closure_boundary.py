"""Executable boundary tests for source-body reception closure.

These tests prove that the resolver records bounded reception-chain closure
only. Closure is not source receipt, not source received, not reception
authorization, not adoption, not authority, not currentness, not operation
permission, not public readiness, not final completion, not continuation,
not reusable permission, and not follow-on authorization.
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

import resolve_source_body_reception_closure_boundary as resolver  # noqa: E402


RECORDED = "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED"
NOT_RECORDED = "SOURCE_BODY_RECEPTION_CLOSURE_NOT_RECORDED"
REQUIRES_ADDITIONAL_BASIS = "SOURCE_BODY_RECEPTION_CLOSURE_REQUIRES_ADDITIONAL_BASIS"
BLOCKED = "SOURCE_BODY_RECEPTION_CLOSURE_REVIEW_BLOCKED"
CONFORMANCE_PASSED = "SOURCE_BODY_RECEPTION_CONFORMANCE_PASSED"

OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_closure_metadata",
    "declared_closure_question",
    "selected_conformance_result",
    "selected_source_body_surface",
    "receiving_context",
    "closure_basis",
    "closure_limits",
    "closure_scope",
    "closure_checks",
    "closure_statement",
    "closure_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_closure_summary",
}

SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_CLOSURE_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)


def false_closure_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def selected_source_body_surface() -> dict[str, object]:
    return {
        "selected_source_body_surface_identifier": "source-body-surface-closure-001",
        "selected_source_body_surface_type": "REFERENCE_SOURCE_BODY_SURFACE",
        "selected_source_body_surface_path": "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
        "selected_source_body_surface_reference": "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
        "source_body_identity_basis": {
            "identity_basis_id": "source-body-identity-basis-closure-001",
            "identity_basis_declared": True,
        },
        "source_body_lineage_basis": {
            "lineage_basis_id": "source-body-lineage-basis-closure-001",
            "lineage_basis_declared": True,
        },
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "selected_source_body_surface_is_not_whole_body_by_default": True,
        "source_received": False,
        "source_receipt_recorded": False,
        "source_receipt_created": False,
        "adoption_created": False,
        "source_replaced": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
    }


def receiving_context() -> dict[str, object]:
    return {
        "receiving_context_id": "receiving-context-closure-001",
        "receiving_context_name": "bounded receiving context",
        "receiving_context_reference": "IAMMAI-SYSTEM present execution line",
        "receiving_context_type": "PRESENT_EXECUTION_CONTEXT",
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


def selected_receipt_exhaustion_result() -> dict[str, object]:
    return {
        "source_body_reception_receipt_exhaustion_metadata": {
            "source_body_reception_receipt_exhaustion_result_id": (
                "source_body_reception_receipt_exhaustion__closure-001"
            ),
            "source_body_reception_receipt_exhaustion_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_receipt_exhaustion_boundary",
        },
        "outcome": "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_RECORDED",
        "failed_check_count": 0,
        "receipt_exhaustion_statement": {
            "source_body_reception_receipt_exhaustion_recorded": True,
            "receipt_exhaustion_of_recognition_record_accounting_only": True,
            "reception_authorized": False,
            "source_received": False,
            "source_receipt_recorded": False,
            "source_receipt_created": False,
            "source_body_reception_conformance_recorded": False,
            "reception_closure_passed": False,
        },
    }


def selected_recognition_result() -> dict[str, object]:
    return {
        "source_body_reception_recognition_metadata": {
            "source_body_reception_recognition_result_id": (
                "source_body_reception_recognition__closure-001"
            ),
            "source_body_reception_recognition_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_recognition_boundary",
        },
        "outcome": "SOURCE_BODY_RECEPTION_RECOGNITION_RECORDED",
        "failed_check_count": 0,
        "recognition_statement": {
            "source_body_reception_recognition_recorded": True,
            "recognition_remained_bounded_accounting_recognition_only": True,
        },
    }


def selected_non_capture_result() -> dict[str, object]:
    return {
        "source_body_reception_non_capture_metadata": {
            "source_body_reception_non_capture_result_id": (
                "source_body_reception_non_capture__closure-001"
            ),
            "source_body_reception_non_capture_result_version": "0.1.0",
            "resolver_module": (
                "resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary"
            ),
        },
        "outcome": "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED",
        "failed_check_count": 0,
        "non_capture_statement": {
            "non_capture_remained_refusal_check_outcome_only": True,
            "adoption_created": False,
            "currentness_created": False,
        },
    }


def selected_eligibility_result() -> dict[str, object]:
    return {
        "source_body_reception_eligibility_metadata": {
            "source_body_reception_eligibility_result_id": (
                "source_body_reception_eligibility__closure-001"
            ),
            "source_body_reception_eligibility_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_eligibility_admissibility_boundary",
        },
        "outcome": "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW",
        "failed_check_count": 0,
        "eligibility_statement": {
            "eligibility_admissibility_remained_review_readiness_only": True,
        },
    }


def selected_receiving_context_role_result() -> dict[str, object]:
    return {
        "source_body_reception_receiving_context_role_metadata": {
            "source_body_reception_receiving_context_role_result_id": (
                "source_body_reception_receiving_context_role__closure-001"
            ),
            "source_body_reception_receiving_context_role_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_receiving_context_role_boundary",
        },
        "outcome": "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED",
        "failed_check_count": 0,
        "receiving_context_role_statement": {
            "receiving_context_role_remained_context_role_only": True,
        },
    }


def selected_identity_preservation_result() -> dict[str, object]:
    return {
        "source_body_reception_identity_metadata": {
            "source_body_reception_identity_result_id": (
                "source_body_reception_identity_preservation__closure-001"
            ),
            "source_body_reception_identity_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_identity_preservation_boundary",
        },
        "outcome": "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED",
        "failed_check_count": 0,
        "identity_preservation_statement": {
            "identity_preservation_preserved_source_identity_only": True,
        },
    }


def selected_request_declaration_result() -> dict[str, object]:
    return {
        "source_body_reception_request_metadata": {
            "source_body_reception_request_result_id": (
                "source_body_reception_request_declaration__closure-001"
            ),
            "source_body_reception_request_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_request_declaration",
        },
        "outcome": "SOURCE_BODY_RECEPTION_REQUEST_DECLARED",
        "failed_check_count": 0,
        "request_declaration_statement": {
            "request_declaration_remained_declaration_only": True,
        },
    }


def conformance_basis() -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    return {
        "selected_receipt_exhaustion_result": selected_receipt_exhaustion_result(),
        "selected_recognition_result": selected_recognition_result(),
        "selected_non_capture_result": selected_non_capture_result(),
        "selected_eligibility_result": selected_eligibility_result(),
        "selected_receiving_context_role_result": selected_receiving_context_role_result(),
        "selected_identity_preservation_result": selected_identity_preservation_result(),
        "selected_reception_request_declaration_result": selected_request_declaration_result(),
        "selected_source_body_surface": surface,
        "source_body_identity_basis": surface["source_body_identity_basis"],
        "source_body_lineage_basis": surface["source_body_lineage_basis"],
        "receiving_context": context,
        "receiving_context_type": context["receiving_context_type"],
        "reception_class": "SOURCE_BODY_RECEPTION_REVIEW",
        "reception_purpose": "close conformed reception-family boundary chain",
        "reception_limits": {
            "bounded_to_source_body_reception_family": True,
            "not_reception_authorization": True,
            "not_source_receipt": True,
        },
        "selected_receiving_context_role": "bounded reference review context",
        "receiving_context_role_class": "REFERENCE_REVIEW_CONTEXT",
        "receiving_context_role_limits": {
            "role_remains_context_only": True,
            "role_is_not_authority": True,
        },
        "conformance_basis_declared": True,
        "reception_chain_conformance_only": True,
        "request_declaration_remained_declaration_only": True,
        "identity_preservation_preserved_source_identity_only": True,
        "receiving_context_role_remained_context_role_only": True,
        "eligibility_admissibility_remained_review_readiness_only": True,
        "non_capture_remained_refusal_check_outcome_only": True,
        "recognition_remained_bounded_accounting_recognition_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "source_receipt_remains_uncreated": True,
        "conformance_is_not_authorization": True,
        "conformance_is_not_source_receipt": True,
        "conformance_is_not_closure": True,
        "closure_requires_separate_boundary": True,
    }


def conformance_limits() -> dict[str, object]:
    return {
        "conformance_limits_declared": True,
        "reception_chain_conformance_only": True,
        "conformance_is_not_authorization": True,
        "conformance_is_not_source_receipt": True,
        "conformance_does_not_receive_source": True,
        "conformance_does_not_create_source_receipt": True,
        "conformance_is_not_closure": True,
        "closure_requires_separate_boundary": True,
    }


def selected_conformance_result() -> dict[str, object]:
    basis = conformance_basis()
    return {
        "source_body_reception_conformance_metadata": {
            "source_body_reception_conformance_result_id": (
                "source_body_reception_conformance__closure-001"
            ),
            "source_body_reception_conformance_result_type": (
                "source_body_reception_conformance_boundary_result"
            ),
            "source_body_reception_conformance_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_conformance_boundary",
        },
        "outcome": CONFORMANCE_PASSED,
        "failed_check_count": 0,
        "conformance_basis": basis,
        "conformance_limits": conformance_limits(),
        "selected_receipt_exhaustion_result": basis["selected_receipt_exhaustion_result"],
        "selected_source_body_surface": basis["selected_source_body_surface"],
        "receiving_context": basis["receiving_context"],
        "conformance_statement": {
            "source_body_reception_conformance_recorded": True,
            "source_body_reception_conformance_passed": True,
            "reception_boundary_chain_conformance_passed": True,
            "reception_family_conformance_passed": True,
            "selected_receipt_exhaustion_result_preserved": True,
            "selected_recognition_result_preserved": True,
            "selected_non_capture_result_preserved": True,
            "selected_eligibility_result_preserved": True,
            "selected_receiving_context_role_result_preserved": True,
            "selected_identity_preservation_result_preserved": True,
            "selected_reception_request_declaration_result_preserved": True,
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "selected_surface_is_not_whole_body_by_default": True,
            "receiving_context_preserved": True,
            "receiving_context_remains_context_only": True,
            "receiving_context_is_not_source": True,
            "receiving_context_is_not_authority": True,
            "receiving_context_is_not_current": True,
            "reception_chain_conformance_only": True,
            "conformance_remained_reception_chain_conformance_only": True,
            "reception_authorized": False,
            "source_received": False,
            "source_receipt_recorded": False,
            "source_receipt_created": False,
            "receiving_context_governance_created": False,
            "adoption_created": False,
            "authority_created": False,
            "currentness_created": False,
            "standing_created": False,
            "vessel_relation_created": False,
            "derivative_relation_created": False,
            "operation_permission_created": False,
            "publication_flow_opened": False,
            "public_launch_readiness_created": False,
            "final_completion_claimed": False,
            "follow_on_work_authorized": False,
            "continuation_authorized": False,
            "reusable_permission_created": False,
            "another_reception_request_authorized": False,
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
        },
        "non_claims": {
            **false_closure_non_claims(),
            "reception_closure_passed": False,
        },
        "source_body_reception_conformance_summary": {
            "outcome": CONFORMANCE_PASSED,
            "failed_check_count": 0,
            "selected_receipt_exhaustion_result_preserved": True,
            "selected_recognition_result_preserved": True,
            "selected_non_capture_result_preserved": True,
            "selected_eligibility_result_preserved": True,
            "selected_receiving_context_role_result_preserved": True,
            "selected_identity_preservation_result_preserved": True,
            "selected_request_declaration_result_preserved": True,
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "selected_surface_is_not_whole_body_by_default": True,
            "receiving_context_preserved": True,
            "receiving_context_remains_context_only": True,
            "receiving_context_is_not_source": True,
            "receiving_context_is_not_authority": True,
            "receiving_context_is_not_current": True,
        },
    }


def closure_basis() -> dict[str, object]:
    return {
        "closure_basis_declared": True,
        "reception_chain_closure_only": True,
        "request_declaration_remained_declaration_only": True,
        "identity_preservation_preserved_source_identity_only": True,
        "receiving_context_role_remained_context_role_only": True,
        "eligibility_admissibility_remained_review_readiness_only": True,
        "non_capture_remained_refusal_check_outcome_only": True,
        "recognition_remained_bounded_accounting_recognition_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "conformance_remained_reception_chain_conformance_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "source_receipt_remains_uncreated": True,
        "closure_is_not_authorization": True,
        "closure_is_not_source_receipt": True,
        "closure_is_not_final_completion": True,
        "closure_does_not_authorize_continuation": True,
        "closure_does_not_authorize_follow_on_work": True,
        "closure_does_not_create_reusable_permission": True,
        "closure_does_not_authorize_another_reception_request": True,
    }


def closure_limits() -> dict[str, object]:
    return {
        "closure_limits_declared": True,
        "reception_chain_closure_only": True,
        "closure_is_not_authorization": True,
        "closure_is_not_source_receipt": True,
        "closure_does_not_receive_source": True,
        "closure_does_not_create_source_receipt": True,
        "closure_is_not_adoption": True,
        "closure_is_not_authority": True,
        "closure_is_not_currentness": True,
        "closure_is_not_validation": True,
        "closure_is_not_invalidation": True,
        "closure_is_not_operation_permission": True,
        "closure_is_not_publication_flow": True,
        "closure_is_not_final_completion": True,
        "closure_does_not_authorize_continuation": True,
        "closure_does_not_authorize_follow_on_work": True,
        "closure_does_not_create_reusable_permission": True,
    }


def declared_closure_request(**overrides: object) -> dict[str, object]:
    request = {
        "closure_request_id": "source-body-reception-closure-request-001",
        "closure_question": "Can this conformed source-body reception boundary chain be closed?",
        "closure_intent": "RECORD_SOURCE_BODY_RECEPTION_CLOSURE",
        "selected_conformance_result": selected_conformance_result(),
        "selected_conformance_result_id": "source_body_reception_conformance__closure-001",
        "selected_conformance_result_outcome": CONFORMANCE_PASSED,
        "closure_basis": closure_basis(),
        "closure_limits": closure_limits(),
        "closure_scope": list(SUPPORTED_SCOPE),
        "requested_closure_outcome": RECORDED,
        "declared_non_claims": false_closure_non_claims(),
    }
    request.update(overrides)
    return request


def resolve(request: dict[str, object]) -> dict[str, object]:
    return resolver.resolve_source_body_reception_closure_boundary(
        declared_closure_request=request
    )


def block_code(result: dict[str, object]) -> str | None:
    return result["block"]["block_code"]


class SourceBodyReceptionClosureBoundaryTests(unittest.TestCase):
    def assertFalseNonClaims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assertNoClosureCollapse(self, result: dict[str, object]) -> None:
        statement = result["closure_statement"]
        non_claims = result["non_claims"]
        for key in (
            "reception_authorized",
            "source_received",
            "source_receipt_recorded",
            "source_receipt_created",
            "receiving_context_governance_created",
            "source_validated_by_receiving_context",
            "source_invalidated_by_receiving_context",
            "source_replaced",
            "adoption_created",
            "authority_created",
            "currentness_created",
            "standing_created",
            "standing_propagated",
            "vessel_relation_created",
            "derivative_relation_created",
            "operation_permission_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
            "reusable_permission_created",
            "another_reception_request_authorized",
        ):
            self.assertIs(statement[key], False, key)
            self.assertIs(non_claims[key], False, key)

    def test_successful_closure_recorded_result(self) -> None:
        request = declared_closure_request()
        original = copy.deepcopy(request)

        result = resolve(request)

        self.assertEqual(set(result), TOP_LEVEL_SECTIONS)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["source_body_reception_closure_summary"]["failed_check_count"], 0)
        self.assertEqual(request, original)

        statement = result["closure_statement"]
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(statement[key], True, key)
            self.assertIs(result["non_claims"][key], True, key)
        for key in (
            "selected_conformance_result_preserved",
            "selected_conformance_result_recorded",
            "selected_conformance_result_failed_check_count_zero",
            "selected_receipt_exhaustion_result_preserved",
            "selected_recognition_result_preserved",
            "selected_non_capture_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_receiving_context_role_result_preserved",
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
            "reception_chain_closure_only",
            "request_declaration_remained_declaration_only",
            "identity_preservation_preserved_source_identity_only",
            "receiving_context_role_remained_context_role_only",
            "eligibility_admissibility_remained_review_readiness_only",
            "non_capture_remained_refusal_check_outcome_only",
            "recognition_remained_bounded_accounting_recognition_only",
            "receipt_exhaustion_remained_recognition_record_accounting_only",
            "conformance_remained_reception_chain_conformance_only",
            "closure_is_not_authorization",
            "closure_is_not_source_receipt",
            "closure_does_not_receive_source",
            "closure_does_not_create_source_receipt",
            "closure_is_not_final_completion",
            "closure_does_not_authorize_continuation",
            "closure_does_not_authorize_follow_on_work",
            "closure_does_not_create_reusable_permission",
            "closure_does_not_authorize_another_reception_request",
        ):
            self.assertIs(statement[key], True, key)
        self.assertFalseNonClaims(result)
        self.assertNoClosureCollapse(result)

    def test_metadata_declared_selected_surface_context_basis_limits_and_scope(self) -> None:
        result = resolve(declared_closure_request())
        metadata = result["source_body_reception_closure_metadata"]
        for key in (
            "source_body_reception_closure_result_id",
            "source_body_reception_closure_result_type",
            "source_body_reception_closure_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(metadata["source_body_reception_closure_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_source_body_reception_closure_boundary")

        declared = result["declared_closure_question"]
        self.assertEqual(declared["closure_request_id"], "source-body-reception-closure-request-001")
        self.assertEqual(declared["closure_intent"], "RECORD_SOURCE_BODY_RECEPTION_CLOSURE")
        self.assertEqual(declared["selected_conformance_result_outcome"], CONFORMANCE_PASSED)
        self.assertEqual(declared["selected_source_body_surface_identifier"], "source-body-surface-closure-001")
        self.assertEqual(declared["receiving_context_type"], "PRESENT_EXECUTION_CONTEXT")
        self.assertEqual(declared["reception_class"], "SOURCE_BODY_RECEPTION_REVIEW")
        self.assertIs(declared["closure_is_not_authorization"], True)
        self.assertIs(declared["closure_is_not_source_receipt"], True)
        self.assertIs(declared["closure_does_not_authorize_continuation"], True)
        self.assertIs(declared["closure_does_not_authorize_follow_on_work"], True)
        self.assertIs(declared["closure_does_not_create_reusable_permission"], True)
        self.assertIs(declared["closure_does_not_authorize_another_reception_request"], True)

        selected = result["selected_conformance_result"]
        self.assertEqual(selected["selected_conformance_result_outcome"], CONFORMANCE_PASSED)
        self.assertIs(selected["selected_conformance_outcome_is_passed"], True)
        self.assertIs(selected["selected_conformance_result_failed_check_count_zero"], True)
        self.assertIs(selected["selected_conformance_result_preserved"], True)
        self.assertIs(selected["selected_conformance_result_recorded"], True)
        self.assertIs(selected["selected_conformance_result_passed"], True)
        self.assertIs(selected["conformance_remained_reception_chain_conformance_only"], True)
        self.assertIs(selected["conformance_did_not_authorize_reception"], True)
        self.assertIs(selected["conformance_did_not_receive_source"], True)
        self.assertIs(selected["conformance_did_not_record_source_receipt"], True)
        self.assertIs(selected["conformance_did_not_create_source_receipt"], True)
        self.assertIs(selected["conformance_did_not_claim_closure"], True)
        self.assertIs(selected["conformance_did_not_claim_final_completion"], True)
        self.assertIs(selected["conformance_did_not_authorize_continuation"], True)
        self.assertIs(selected["conformance_did_not_authorize_follow_on_work"], True)

        surface = result["selected_source_body_surface"]
        self.assertEqual(surface["selected_source_body_surface_identifier"], "source-body-surface-closure-001")
        self.assertEqual(surface["selected_source_body_surface_type"], "REFERENCE_SOURCE_BODY_SURFACE")
        self.assertEqual(
            surface["selected_source_body_surface_reference"],
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
        )
        self.assertTrue(surface["source_body_identity_basis"])
        self.assertTrue(surface["source_body_lineage_basis"])
        for key in (
            "selected_source_body_surface_remains_source",
            "selected_source_body_surface_is_not_whole_body_by_default",
            "selected_source_body_surface_is_not_received",
            "selected_source_body_surface_is_not_adopted",
            "selected_source_body_surface_is_not_replaced",
            "selected_source_body_surface_is_not_validated_by_receiving_context",
            "selected_source_body_surface_is_not_invalidated_by_receiving_context",
        ):
            self.assertIs(surface[key], True, key)

        context = result["receiving_context"]
        self.assertEqual(context["receiving_context_id"], "receiving-context-closure-001")
        self.assertEqual(context["receiving_context_type"], "PRESENT_EXECUTION_CONTEXT")
        for key in (
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
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

        basis = result["closure_basis"]
        for key in (
            "selected_conformance_result",
            "selected_receipt_exhaustion_result",
            "selected_recognition_result",
            "selected_non_capture_result",
            "selected_eligibility_result",
            "selected_receiving_context_role_result",
            "selected_identity_preservation_result",
            "selected_reception_request_declaration_result",
            "selected_source_body_surface",
            "source_body_identity_basis",
            "source_body_lineage_basis",
            "receiving_context",
            "receiving_context_type",
            "reception_class",
            "reception_purpose",
            "reception_limits",
            "selected_receiving_context_role",
            "receiving_context_role_class",
            "receiving_context_role_limits",
            "conformance_basis",
            "conformance_limits",
            "closure_basis_as_supplied",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "reception_chain_closure_only",
            "request_declaration_remained_declaration_only",
            "identity_preservation_preserved_source_identity_only",
            "receiving_context_role_remained_context_role_only",
            "eligibility_admissibility_remained_review_readiness_only",
            "non_capture_remained_refusal_check_outcome_only",
            "recognition_remained_bounded_accounting_recognition_only",
            "receipt_exhaustion_remained_recognition_record_accounting_only",
            "conformance_remained_reception_chain_conformance_only",
            "source_remains_unreceived",
            "source_receipt_remains_unrecorded",
            "source_receipt_remains_uncreated",
            "closure_is_not_authorization",
            "closure_is_not_source_receipt",
            "closure_is_not_final_completion",
            "closure_does_not_authorize_continuation",
            "closure_does_not_authorize_follow_on_work",
            "closure_does_not_create_reusable_permission",
            "closure_does_not_authorize_another_reception_request",
        ):
            self.assertIs(basis[key], True, key)

        limits = result["closure_limits"]
        self.assertEqual(limits["closure_limits_as_supplied"], closure_limits())
        for key in (
            "reception_chain_closure_only",
            "closure_is_not_authorization",
            "closure_is_not_source_receipt",
            "closure_does_not_receive_source",
            "closure_does_not_create_source_receipt",
            "closure_is_not_adoption",
            "closure_is_not_authority",
            "closure_is_not_currentness",
            "closure_is_not_validation",
            "closure_is_not_invalidation",
            "closure_is_not_operation_permission",
            "closure_is_not_publication_flow",
            "closure_is_not_final_completion",
            "closure_does_not_authorize_continuation",
            "closure_does_not_authorize_follow_on_work",
            "closure_does_not_create_reusable_permission",
        ):
            self.assertIs(limits[key], True, key)

        scope = result["closure_scope"]
        self.assertEqual(set(scope["selected_closure_scope_values"]), set(SUPPORTED_SCOPE))
        self.assertEqual(scope["unsupported_closure_scope_values"], [])
        self.assertIs(scope["all_selected_scope_values_supported"], True)

    def test_supported_scope_values_and_unsupported_scope_block(self) -> None:
        for value in SUPPORTED_SCOPE:
            with self.subTest(scope=value):
                result = resolve(declared_closure_request(closure_scope=[value]))
                self.assertEqual(result["outcome"], RECORDED)
                self.assertEqual(result["closure_scope"]["selected_closure_scope_values"], [value])
        result = resolve(declared_closure_request(closure_scope=["UNSUPPORTED_CLOSURE_SCOPE_VALUE"]))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_CLOSURE_SCOPE")

    def test_closure_checks_are_explicit_and_pass_for_recorded_result(self) -> None:
        result = resolve(declared_closure_request())
        checks = result["closure_checks"]
        self.assertGreater(len(checks), 40)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertIs(check["passed"], True, check["check_name"])
        self.assertEqual(result["source_body_reception_closure_summary"]["failed_check_count"], 0)

        check_names = {check["check_name"] for check in checks}
        expected = {
            "closure_question_declared",
            "closure_intent_supported",
            "selected_conformance_result_present",
            "selected_conformance_outcome_declared",
            "selected_conformance_outcome_passed",
            "selected_conformance_failed_check_count_zero",
            "selected_receipt_exhaustion_result_preserved",
            "selected_recognition_result_preserved",
            "selected_non_capture_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_receiving_context_role_result_preserved",
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
            "conformance_was_recorded",
            "conformance_passed",
            "conformance_reception_chain_only",
            "source_unreceived",
            "source_receipt_unrecorded",
            "source_receipt_uncreated",
            "closure_basis_declared",
            "closure_limits_declared",
            "closure_scope_supported",
            "closure_is_not_authorization",
            "closure_is_not_source_receipt",
            "closure_does_not_receive_source",
            "closure_does_not_create_source_receipt",
            "closure_does_not_create_adoption",
            "closure_does_not_create_authority",
            "closure_does_not_create_currentness",
            "closure_does_not_validate_source",
            "closure_does_not_invalidate_source",
            "closure_does_not_replace_source",
            "closure_does_not_create_operation_permission",
            "closure_does_not_create_governance",
            "closure_does_not_open_publication_flow",
            "closure_does_not_create_public_readiness",
            "closure_does_not_claim_final_completion",
            "closure_does_not_authorize_continuation",
            "closure_does_not_authorize_follow_on_work",
            "closure_does_not_create_reusable_permission",
            "closure_does_not_authorize_another_reception_request",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected.issubset(check_names))

    def test_closure_statement_non_meaning_open_items_non_claims_and_summary(self) -> None:
        result = resolve(declared_closure_request())
        non_meaning = result["closure_non_meaning"]
        for key in (
            "closure_does_not_mean_reception_authorized",
            "closure_does_not_mean_source_received",
            "closure_does_not_mean_source_receipt_recorded",
            "closure_does_not_mean_source_receipt_created",
            "closure_does_not_mean_source_adopted",
            "closure_does_not_mean_source_validated",
            "closure_does_not_mean_source_invalidated",
            "closure_does_not_mean_source_replaced",
            "closure_does_not_mean_receiving_context_became_source",
            "closure_does_not_mean_receiving_context_became_authority",
            "closure_does_not_mean_receiving_context_became_current",
            "closure_does_not_mean_receiving_context_became_receiver",
            "closure_does_not_mean_receiving_context_became_adopter",
            "closure_does_not_mean_receiving_context_became_validator",
            "closure_does_not_mean_receiving_context_became_invalidator",
            "closure_does_not_mean_receiving_context_became_operator",
            "closure_does_not_mean_receiving_context_governance_created",
            "closure_does_not_mean_standing_created",
            "closure_does_not_mean_standing_propagated",
            "closure_does_not_mean_vessel_relation_created",
            "closure_does_not_mean_derivative_relation_created",
            "closure_does_not_mean_operation_permission_created",
            "closure_does_not_mean_public_readiness_created",
            "closure_does_not_mean_final_completion_claimed",
            "closure_does_not_mean_follow_on_work_authorized",
            "closure_does_not_mean_continuation_authorized",
            "closure_does_not_mean_publication_flow_opened",
            "closure_does_not_mean_reusable_permission_created",
            "closure_does_not_mean_successor_reception_authorized",
            "closure_does_not_mean_another_reception_request_authorized",
        ):
            self.assertIs(non_meaning[key], True, key)

        open_section = result["what_remains_open"]
        for item in (
            "source-body reception closure test",
            "source-body reception closure live artifact",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "standing creation",
            "operation permission",
            "receiving-context governance",
            "public readiness",
            "final completion",
            "follow-on work",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
        ):
            self.assertIn(item, open_section["open_items"])
        self.assertIs(open_section["open_means_not_scheduled"], True)
        self.assertIs(open_section["open_means_not_authorized"], True)
        self.assertIs(open_section["open_means_not_executed"], True)

        summary = resolver.build_source_body_reception_closure_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertEqual(summary["closure_request_id"], "source-body-reception-closure-request-001")
        self.assertTrue(summary["closure_recorded"])
        self.assertTrue(summary["boundary_chain_closed"])
        self.assertTrue(summary["reception_closure_passed"])
        self.assertTrue(summary["reception_family_closure_recorded"])
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertTrue(summary["selected_conformance_result_preserved"])
        self.assertTrue(summary["selected_conformance_result_recorded"])
        self.assertTrue(summary["selected_conformance_result_failed_check_count_zero"])
        self.assertTrue(summary["selected_receipt_exhaustion_result_preserved"])
        self.assertTrue(summary["selected_recognition_result_preserved"])
        self.assertTrue(summary["selected_non_capture_result_preserved"])
        self.assertTrue(summary["selected_eligibility_result_preserved"])
        self.assertTrue(summary["selected_receiving_context_role_result_preserved"])
        self.assertTrue(summary["selected_identity_preservation_result_preserved"])
        self.assertTrue(summary["selected_request_declaration_result_preserved"])
        self.assertTrue(summary["selected_source_body_surface_preserved"])
        self.assertTrue(summary["selected_source_body_surface_remains_source"])
        self.assertTrue(summary["selected_surface_is_not_whole_body_by_default"])
        self.assertTrue(summary["receiving_context_preserved"])
        self.assertTrue(summary["receiving_context_remains_context_only"])
        self.assertTrue(summary["receiving_context_is_not_source"])
        self.assertTrue(summary["receiving_context_is_not_authority"])
        self.assertTrue(summary["receiving_context_is_not_current"])
        self.assertTrue(summary["reception_chain_closure_only"])
        self.assertTrue(summary["conformance_reception_chain_only"])
        self.assertTrue(summary["closure_not_authorization"])
        self.assertTrue(summary["closure_not_source_receipt"])
        self.assertTrue(summary["closure_not_final_completion"])
        self.assertTrue(summary["closure_not_continuation"])
        self.assertTrue(summary["closure_not_reusable_permission"])
        self.assertTrue(summary["no_source_received"])
        self.assertTrue(summary["no_source_receipt_recorded"])
        self.assertTrue(summary["no_source_receipt_created"])
        self.assertTrue(summary["no_adoption_authority_currentness_standing"])
        self.assertTrue(summary["no_vessel_derivative_relation"])
        self.assertTrue(summary["no_operation_permission_governance_publication_flow"])
        self.assertTrue(summary["no_public_readiness_final_completion_follow_on_work"])
        self.assertTrue(summary["no_reusable_permission"])
        self.assertTrue(summary["no_another_reception_request_authorized"])
        self.assertFalseNonClaims(result)

    def test_requires_additional_basis_and_not_recorded_are_bounded(self) -> None:
        additional_context = {
            "closure_basis_too_generic": True,
            "closure_limits_unclear": True,
            "closure_reusable_permission_distinction_unclear": True,
        }
        result = resolve(
            declared_closure_request(
                requested_closure_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        self.assertEqual(
            result["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertIs(result["additional_basis_required"]["missing_basis_not_scheduled"], True)
        self.assertIs(result["additional_basis_required"]["missing_basis_not_authorized"], True)
        self.assertIs(result["additional_basis_required"]["missing_basis_not_executed"], True)
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(result["closure_statement"][key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        self.assertNoClosureCollapse(result)

        not_recorded_basis = {
            "closure_basis_cannot_be_bounded": True,
            "closure_overread_as_reusable_permission": True,
            "closure_overread_as_permission_for_another_reception_request": True,
        }
        result = resolve(
            declared_closure_request(
                requested_closure_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(result["outcome"], NOT_RECORDED)
        self.assertIs(result["not_recorded_basis"]["not_recorded"], True)
        self.assertEqual(result["not_recorded_basis"]["not_recorded_basis"], not_recorded_basis)
        for key in (
            "not_recorded_does_not_mutate",
            "not_recorded_does_not_repair",
            "not_recorded_does_not_authorize",
            "not_recorded_does_not_receive",
            "not_recorded_does_not_record_source_receipt",
            "not_recorded_does_not_create_source_receipt",
            "not_recorded_does_not_replace",
            "not_recorded_does_not_validate",
            "not_recorded_does_not_invalidate",
            "not_recorded_does_not_create_currentness",
            "not_recorded_does_not_claim_final_completion",
            "not_recorded_does_not_authorize_follow_on_work",
            "not_recorded_does_not_create_reusable_permission",
            "not_recorded_does_not_authorize_another_reception_request",
        ):
            self.assertIs(result["not_recorded_basis"][key], True, key)
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(result["closure_statement"][key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        self.assertNoClosureCollapse(result)

    def test_request_builder_helper_preserves_bounded_request(self) -> None:
        selected = selected_conformance_result()
        request = resolver.build_declared_source_body_reception_closure_request(
            "closure-request-builder-001",
            "Can this conformed source-body reception boundary chain be closed?",
            selected,
            closure_basis(),
            closure_limits(),
            list(SUPPORTED_SCOPE),
            selected_conformance_result_id="source_body_reception_conformance__closure-001",
            selected_conformance_result_outcome=CONFORMANCE_PASSED,
            additional_basis_context={"closure_limits_unclear": True},
            not_recorded_basis={"closure_overread_as_final_completion": True},
        )
        self.assertEqual(request["closure_request_id"], "closure-request-builder-001")
        self.assertEqual(request["closure_question"], "Can this conformed source-body reception boundary chain be closed?")
        self.assertEqual(request["selected_conformance_result"], selected)
        self.assertEqual(request["closure_basis"], closure_basis())
        self.assertEqual(request["closure_limits"], closure_limits())
        self.assertEqual(request["closure_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_conformance_result_outcome"], CONFORMANCE_PASSED)
        self.assertEqual(request["requested_closure_outcome"], RECORDED)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)
        for key in (
            "reception_authorized",
            "source_received",
            "source_receipt_recorded",
            "source_receipt_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "another_reception_request_authorized",
        ):
            self.assertIs(request[key], False, key)

        result = resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])

    def test_path_based_selected_conformance_request_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            selected_path = tmp / "selected_conformance_result.json"
            selected_path.write_text(
                json.dumps(selected_conformance_result(), indent=2, sort_keys=True),
                encoding="utf-8",
            )
            request = declared_closure_request(
                selected_conformance_result_path=str(selected_path),
                selected_conformance_result=selected_conformance_result(),
            )
            request.pop("selected_conformance_result")

            result = resolve(request)
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(
                result["selected_conformance_result"]["selected_conformance_result_path"],
                str(selected_path),
            )

            request_path = tmp / "declared_closure_request.json"
            request_path.write_text(
                json.dumps(request, indent=2, sort_keys=True),
                encoding="utf-8",
            )
            path_result = resolver.resolve_source_body_reception_closure_boundary_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), TOP_LEVEL_SECTIONS)
            self.assertEqual(
                path_result["declared_closure_question"]["declared_closure_request_path"],
                str(request_path),
            )

            output_path = tmp / "nested" / "closure_result.json"
            written_path = resolver.write_source_body_reception_closure_result(
                result, output_path
            )
            self.assertTrue(written_path.exists())
            written = json.loads(written_path.read_text(encoding="utf-8"))
            self.assertEqual(set(written), TOP_LEVEL_SECTIONS)

            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_CLOSURE_BOUNDARY_ROOT",
                tmp / "default-closure-root",
            ):
                first = resolver.write_source_body_reception_closure_result(result)
                second = resolver.write_source_body_reception_closure_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("default-closure-root", str(first))
            self.assertNotIn("source_body_reception_conformance_boundary", str(first))
            self.assertNotIn("derivative", str(first))
            self.assertNotIn("successor", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_closure_request()
        selected = request["selected_conformance_result"]
        nested_items = [
            selected,
            selected["conformance_basis"]["selected_receipt_exhaustion_result"],
            selected["conformance_basis"]["selected_recognition_result"],
            selected["conformance_basis"]["selected_non_capture_result"],
            selected["conformance_basis"]["selected_eligibility_result"],
            selected["conformance_basis"]["selected_receiving_context_role_result"],
            selected["conformance_basis"]["selected_identity_preservation_result"],
            selected["conformance_basis"]["selected_reception_request_declaration_result"],
            selected["conformance_basis"]["selected_source_body_surface"],
            selected["conformance_basis"]["receiving_context"],
            request["closure_basis"],
            request["closure_limits"],
            request["closure_scope"],
        ]
        before_request = copy.deepcopy(request)
        before_nested = [copy.deepcopy(item) for item in nested_items]

        first = resolve(request)
        second = resolve(request)

        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        self.assertEqual(request, before_request)
        for item, before in zip(nested_items, before_nested):
            self.assertEqual(item, before)

    def test_explicit_missing_and_malformed_request_blocks(self) -> None:
        result = resolve(declared_closure_request(closure_intent="BLOCK_SOURCE_BODY_RECEPTION_CLOSURE_REVIEW"))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CLOSURE_REVIEW_REQUEST_EXPLICITLY_BLOCKED")
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(result["closure_statement"][key], False, key)

        result = resolver.resolve_source_body_reception_closure_boundary()
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CLOSURE_QUESTION_UNDECLARED")

        result = resolver.resolve_source_body_reception_closure_boundary(
            declared_closure_request="not a mapping"
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "DECLARED_CLOSURE_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            missing = tmp / "missing.json"
            result = resolver.resolve_source_body_reception_closure_boundary_from_path(missing)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "DECLARED_CLOSURE_REQUEST_UNREADABLE")

            malformed = tmp / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            result = resolver.resolve_source_body_reception_closure_boundary_from_path(malformed)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "DECLARED_CLOSURE_REQUEST_MALFORMED")

            array_path = tmp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            result = resolver.resolve_source_body_reception_closure_boundary_from_path(array_path)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "DECLARED_CLOSURE_REQUEST_MALFORMED")

    def test_selected_conformance_path_and_result_issue_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            missing = tmp / "missing-conformance.json"
            result = resolve(
                declared_closure_request(
                    selected_conformance_result_path=str(missing),
                    selected_conformance_result=selected_conformance_result(),
                )
            )
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "CONFORMANCE_RESULT_UNREADABLE")

            malformed = tmp / "malformed-conformance.json"
            malformed.write_text("{", encoding="utf-8")
            result = resolve(
                declared_closure_request(
                    selected_conformance_result_path=str(malformed),
                    selected_conformance_result=selected_conformance_result(),
                )
            )
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "CONFORMANCE_RESULT_MALFORMED")

            array_path = tmp / "array-conformance.json"
            array_path.write_text("[]", encoding="utf-8")
            result = resolve(
                declared_closure_request(
                    selected_conformance_result_path=str(array_path),
                    selected_conformance_result=selected_conformance_result(),
                )
            )
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "CONFORMANCE_RESULT_MALFORMED")

        selected = selected_conformance_result()
        selected.pop("outcome")
        selected["source_body_reception_conformance_summary"].pop("outcome")
        request = declared_closure_request(selected_conformance_result=selected)
        request.pop("selected_conformance_result_outcome")
        result = resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CONFORMANCE_RESULT_OUTCOME_MISSING")

        selected = selected_conformance_result()
        selected["outcome"] = "SOURCE_BODY_RECEPTION_CONFORMANCE_NOT_PASSED"
        request = declared_closure_request(selected_conformance_result=selected)
        request.pop("selected_conformance_result_outcome")
        result = resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CONFORMANCE_RESULT_NOT_PASSED")

        selected = selected_conformance_result()
        selected["failed_check_count"] = 1
        result = resolve(declared_closure_request(selected_conformance_result=selected))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CONFORMANCE_RESULT_HAS_FAILED_CHECKS")

    def test_missing_required_selected_basis_blocks(self) -> None:
        cases = (
            ("selected_receipt_exhaustion_result", "RECEIPT_EXHAUSTION_RESULT_MISSING"),
            ("selected_recognition_result", "RECOGNITION_RESULT_MISSING"),
            ("selected_non_capture_result", "NON_CAPTURE_RESULT_MISSING"),
            ("selected_eligibility_result", "ELIGIBILITY_RESULT_MISSING"),
            ("selected_receiving_context_role_result", "RECEIVING_CONTEXT_ROLE_RESULT_MISSING"),
            ("selected_identity_preservation_result", "IDENTITY_PRESERVATION_RESULT_MISSING"),
            (
                "selected_reception_request_declaration_result",
                "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
            ),
            ("selected_source_body_surface", "SELECTED_SOURCE_BODY_SURFACE_MISSING"),
            ("receiving_context", "RECEIVING_CONTEXT_MISSING"),
        )
        for key, expected in cases:
            with self.subTest(key=key):
                selected = selected_conformance_result()
                selected["conformance_basis"].pop(key)
                if key in selected:
                    selected.pop(key)
                result = resolve(declared_closure_request(selected_conformance_result=selected))
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), expected)

        basis_cases = (
            ("receiving_context_type", "RECEIVING_CONTEXT_TYPE_MISSING"),
            ("reception_class", "RECEPTION_CLASS_MISSING"),
            ("reception_purpose", "RECEPTION_PURPOSE_MISSING"),
            ("reception_limits", "RECEPTION_LIMITS_MISSING"),
        )
        for key, expected in basis_cases:
            with self.subTest(key=key):
                selected = selected_conformance_result()
                if key == "receiving_context_type":
                    selected["conformance_basis"]["receiving_context"].pop("receiving_context_type")
                selected["conformance_basis"].pop(key, None)
                result = resolve(declared_closure_request(selected_conformance_result=selected))
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), expected)

        result = resolve(declared_closure_request(closure_basis={}))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CLOSURE_BASIS_MISSING")

        result = resolve(declared_closure_request(closure_limits={}))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "CLOSURE_LIMITS_MISSING")

    def test_malformed_surface_and_context_block_with_bounded_codes(self) -> None:
        selected = selected_conformance_result()
        selected["conformance_basis"]["selected_source_body_surface"] = "malformed"
        selected.pop("selected_source_body_surface")
        result = resolve(declared_closure_request(selected_conformance_result=selected))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            block_code(result),
            {"SELECTED_SOURCE_BODY_SURFACE_MALFORMED", "SELECTED_SOURCE_BODY_SURFACE_MISSING"},
        )

        selected = selected_conformance_result()
        selected["conformance_basis"]["receiving_context"] = "malformed"
        selected.pop("receiving_context")
        result = resolve(declared_closure_request(selected_conformance_result=selected))
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            block_code(result),
            {"RECEIVING_CONTEXT_MALFORMED", "RECEIVING_CONTEXT_MISSING"},
        )

    def test_closure_collapse_overreach_flags_block(self) -> None:
        cases = (
            ("reception_authorized", "CLOSURE_AUTHORIZES_RECEPTION"),
            ("source_received", "CLOSURE_RECEIVES_SOURCE"),
            ("source_receipt_recorded", "CLOSURE_RECORDS_SOURCE_RECEIPT"),
            ("source_receipt_created", "CLOSURE_CREATES_SOURCE_RECEIPT"),
            ("receiving_context_governance_created", "CLOSURE_CREATES_GOVERNANCE"),
            ("receiving_context_became_source", "CLOSURE_TREATS_CONTEXT_AS_SOURCE"),
            ("receiving_context_became_authority", "CLOSURE_TREATS_CONTEXT_AS_AUTHORITY"),
            ("receiving_context_became_current", "CLOSURE_TREATS_CONTEXT_AS_CURRENT"),
            ("receiving_context_became_receiver", "CLOSURE_TREATS_CONTEXT_AS_RECEIVER"),
            ("receiving_context_became_adopter", "CLOSURE_TREATS_CONTEXT_AS_ADOPTER"),
            ("receiving_context_became_validator", "CLOSURE_TREATS_CONTEXT_AS_VALIDATOR"),
            ("receiving_context_became_invalidator", "CLOSURE_TREATS_CONTEXT_AS_INVALIDATOR"),
            ("receiving_context_became_operator", "CLOSURE_TREATS_CONTEXT_AS_OPERATOR"),
            ("source_validated_by_receiving_context", "CLOSURE_VALIDATES_SOURCE"),
            ("source_invalidated_by_receiving_context", "CLOSURE_INVALIDATES_SOURCE"),
            ("source_replaced", "CLOSURE_REPLACES_SOURCE"),
            ("adoption_created", "CLOSURE_CREATES_ADOPTION"),
            ("authority_created", "CLOSURE_CREATES_AUTHORITY"),
            ("currentness_created", "CLOSURE_CREATES_CURRENTNESS"),
            ("standing_created", "CLOSURE_CREATES_STANDING"),
            ("standing_propagated", "CLOSURE_CREATES_STANDING_PROPAGATION"),
            ("vessel_relation_created", "CLOSURE_CREATES_VESSEL_RELATION"),
            ("derivative_relation_created", "CLOSURE_CREATES_DERIVATIVE_RELATION"),
            ("operation_permission_created", "CLOSURE_CREATES_OPERATION_PERMISSION"),
            ("public_launch_readiness_created", "CLOSURE_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "CLOSURE_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "CLOSURE_AUTHORIZES_FOLLOW_ON_WORK"),
            ("continuation_authorized", "CLOSURE_AUTHORIZES_CONTINUATION"),
            ("publication_flow_opened", "CLOSURE_OPENS_PUBLICATION_FLOW"),
            ("reusable_permission_created", "CLOSURE_CREATES_REUSABLE_PERMISSION"),
            ("another_reception_request_authorized", "CLOSURE_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
        )
        for flag, expected in cases:
            with self.subTest(flag=flag):
                request = declared_closure_request(**{flag: True})
                result = resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), expected)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                result = resolve(declared_closure_request(**{flag: True}))
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        request = declared_closure_request()
        request["declared_non_claims"].pop("reception_authorized")
        result = resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

        request = declared_closure_request()
        request["declared_non_claims"]["source_received"] = True
        result = resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            block_code(result),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "CLOSURE_RECEIVES_SOURCE"},
        )

    def test_outcome_family_is_closed(self) -> None:
        for requested, expected in (
            (RECORDED, RECORDED),
            (NOT_RECORDED, NOT_RECORDED),
            (REQUIRES_ADDITIONAL_BASIS, REQUIRES_ADDITIONAL_BASIS),
        ):
            with self.subTest(requested=requested):
                result = resolve(declared_closure_request(requested_closure_outcome=requested))
                self.assertIn(result["outcome"], OUTCOME_FAMILY)
                self.assertEqual(result["outcome"], expected)

        result = resolve(declared_closure_request(closure_scope=["not supported"]))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(result["outcome"], BLOCKED)


if __name__ == "__main__":
    unittest.main()
