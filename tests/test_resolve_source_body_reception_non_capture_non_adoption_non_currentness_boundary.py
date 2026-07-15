"""Executable boundary tests for source-body reception non-capture only.

These tests prove that the resolver records non-capture, non-adoption, and
non-currentness only as refusal/check outcomes. Non-capture passed is not
reception recognition, not reception authorization, and not source receipt.
Reception remains unrecognized and unauthorized, source remains unreceived,
and recognition remains future work.
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

import resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary as resolver  # noqa: E402


PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED"
NOT_PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_NOT_PASSED"
REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_NON_CAPTURE_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_REVIEW_BLOCKED"
ELIGIBLE = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"
ROLE_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
IDENTITY_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {PASSED, NOT_PASSED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_non_capture_metadata",
    "declared_non_capture_question",
    "selected_eligibility_result",
    "selected_source_body_surface",
    "receiving_context",
    "non_capture_basis",
    "non_adoption_basis",
    "non_currentness_basis",
    "non_capture_scope",
    "non_capture_checks",
    "non_capture_statement",
    "non_capture_non_meaning",
    "additional_basis_required",
    "not_passed_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_non_capture_summary",
}

SUPPORTED_SCOPE = (
    "NON_CAPTURE_REVIEW_ONLY",
    "NON_ADOPTION_REVIEW_ONLY",
    "NON_CURRENTNESS_REVIEW_ONLY",
    "NON_CAPTURE_IS_NOT_RECEPTION",
    "NON_CAPTURE_IS_NOT_AUTHORIZATION",
    "NON_CAPTURE_IS_NOT_SOURCE_RECEIPT",
    "NON_CAPTURE_IS_NOT_RECOGNITION",
    "NON_CAPTURE_DOES_NOT_VALIDATE_SOURCE",
    "NON_CAPTURE_DOES_NOT_INVALIDATE_SOURCE",
    "NO_SOURCE_REPLACEMENT",
    "NO_RECEIVING_CONTEXT_AUTHORITY",
    "NO_RECEIVING_CONTEXT_CURRENTNESS",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "RECOGNITION_REQUIRES_SEPARATE_BOUNDARY",
)

REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)
ALLOWED_PASSED_TRUE_FIELDS = tuple(resolver.ALLOWED_PASSED_TRUE_FIELDS)


def false_non_capture_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


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
        "selected_source_body_surface_is_not_whole_body_by_default": True,
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
        "purpose_id": "non-capture-before-reception-recognition",
        "purpose_statement": "Check capture, adoption, and currentness risks only.",
        "purpose_is_permission": False,
    }


def reception_limits() -> dict[str, object]:
    return {
        "limits_id": "source-body-reception-non-capture-limits-001",
        "non_capture_boundary_only": True,
        "no_reception_recognition": True,
        "no_reception_authorization": True,
        "no_source_receipt": True,
        "recognition_requires_separate_boundary": True,
        "no_operation_permission": True,
        "no_publication_flow": True,
    }


def selected_identity_preservation_result(
    surface: dict[str, object] | None = None,
    context: dict[str, object] | None = None,
    request_declaration: dict[str, object] | None = None,
) -> dict[str, object]:
    surface = copy.deepcopy(surface or selected_source_body_surface())
    context = copy.deepcopy(context or receiving_context())
    request_declaration = copy.deepcopy(
        request_declaration or selected_reception_request_declaration_result()
    )
    return {
        "source_body_reception_identity_metadata": {
            "source_body_reception_identity_result_id": (
                "source_body_reception_identity_preservation__identity-001"
            ),
            "source_body_reception_identity_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_identity_preservation_boundary",
        },
        "outcome": IDENTITY_PRESERVED,
        "source_body_reception_identity_summary": {
            "outcome": IDENTITY_PRESERVED,
            "failed_check_count": 0,
            "selected_source_body_surface_identifier": (
                surface["selected_source_body_surface_identifier"]
            ),
        },
        "selected_reception_request_declaration_result": request_declaration,
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "identity_preservation_statement": {
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "selected_surface_is_not_whole_body_by_default": True,
            "receiving_context_preserved": True,
            "receiving_context_remains_context_only": True,
            "receiving_context_is_not_source": True,
            "receiving_context_is_not_authority": True,
            "receiving_context_is_not_current": True,
            "reception_recognized": False,
            "reception_authorized": False,
            "source_received": False,
            "source_replaced": False,
            "source_validated_by_receiving_context": False,
            "source_invalidated_by_receiving_context": False,
        },
    }


def selected_receiving_context_role_result(
    identity: dict[str, object] | None = None,
    surface: dict[str, object] | None = None,
    context: dict[str, object] | None = None,
    request_declaration: dict[str, object] | None = None,
) -> dict[str, object]:
    surface = copy.deepcopy(surface or selected_source_body_surface())
    context = copy.deepcopy(context or receiving_context())
    request_declaration = copy.deepcopy(
        request_declaration or selected_reception_request_declaration_result()
    )
    identity = copy.deepcopy(
        identity
        or selected_identity_preservation_result(surface, context, request_declaration)
    )
    role = {
        "receiving_context_role_id": "receiving-context-role-001",
        "receiving_context_role": "bounded reference review context",
        "receiving_context_role_class": "REFERENCE_REVIEW_CONTEXT",
        "receiving_context_role_limits": {
            "role_limits_id": "receiving-context-role-limits-001",
            "role_is_not_reception": True,
            "role_is_not_authorization": True,
            "role_is_not_source_receipt": True,
            "role_remains_bounded": True,
        },
    }
    statement = {
        "receiving_context_role_declared": True,
        "receiving_context_role_class_supported": True,
        "receiving_context_role_limits_present": True,
        "receiving_context_role_preserved": True,
        "receiving_context_role_remains_bounded": True,
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
        "reception_recognized": False,
        "reception_authorized": False,
        "source_received": False,
        "receiving_context_governance_created": False,
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
    return {
        "source_body_reception_receiving_context_role_metadata": {
            "source_body_reception_receiving_context_role_result_id": (
                "source_body_reception_receiving_context_role__role-001"
            ),
            "source_body_reception_receiving_context_role_result_version": "0.1.0",
            "resolver_module": (
                "resolve_source_body_reception_receiving_context_role_boundary"
            ),
        },
        "outcome": ROLE_RECORDED,
        "source_body_reception_receiving_context_role_summary": {
            "outcome": ROLE_RECORDED,
            "failed_check_count": 0,
            "selected_receiving_context_role_result_id": (
                "source_body_reception_receiving_context_role__role-001"
            ),
        },
        "selected_identity_preservation_result": identity,
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "receiving_context_role": role,
        "receiving_context_role_basis": {
            "selected_identity_preservation_result": identity,
            "selected_reception_request_declaration_result": request_declaration,
            "selected_source_body_surface": surface,
            "receiving_context": context,
            "receiving_context_role_class": role["receiving_context_role_class"],
            "receiving_context_role_limits": role["receiving_context_role_limits"],
        },
        "receiving_context_role_statement": statement,
        "non_claims": {
            key: False
            for key in (
                "reception_recognized",
                "reception_authorized",
                "source_received",
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
                "mutation_performed",
                "replay_performed",
                "merge_performed",
            )
        },
    }


def selected_eligibility_result() -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    request_declaration = selected_reception_request_declaration_result()
    identity = selected_identity_preservation_result(surface, context, request_declaration)
    role_result = selected_receiving_context_role_result(
        identity, surface, context, request_declaration
    )
    role = role_result["receiving_context_role"]
    statement = {
        "source_body_reception_eligible_admissible_for_review": True,
        "selected_receiving_context_role_result_preserved": True,
        "selected_receiving_context_role_result_recorded": True,
        "selected_receiving_context_role_result_failed_check_count_zero": True,
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
        "receiving_context_role_preserved": True,
        "receiving_context_role_remains_bounded": True,
        "eligibility_admissibility_is_review_readiness_only": True,
        "eligible_for_reception_review_only": True,
        "admissible_for_reception_review_only": True,
        "eligibility_is_not_reception": True,
        "admissibility_is_not_authorization": True,
        "eligibility_does_not_receive_source": True,
        "reception_class_preserved": True,
        "reception_purpose_preserved": True,
        "reception_limits_preserved": True,
        "reception_recognized": False,
        "reception_authorized": False,
        "source_received": False,
        "non_capture_passed": False,
        "reception_recognition_passed": False,
        "adoption_created": False,
        "authority_created": False,
        "currentness_created": False,
        "standing_created": False,
        "standing_propagated": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "source_replaced": False,
        "operation_permission_created": False,
        "receiving_context_governance_created": False,
        "publication_flow_opened": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "continuation_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }
    eligibility_basis = {
        "selected_receiving_context_role_result": role_result,
        "selected_identity_preservation_result": identity,
        "selected_reception_request_declaration_result": request_declaration,
        "selected_source_body_surface": surface,
        "source_body_identity_basis": surface["source_body_identity_basis"],
        "source_body_lineage_basis": surface["source_body_lineage_basis"],
        "receiving_context": context,
        "receiving_context_type": context["receiving_context_type"],
        "reception_class": "REFERENCE_RECEPTION",
        "reception_purpose": reception_purpose(),
        "reception_limits": reception_limits(),
        "selected_receiving_context_role": role,
        "receiving_context_role_class": role["receiving_context_role_class"],
        "receiving_context_role_limits": role["receiving_context_role_limits"],
        "eligibility_basis": {
            "eligibility_basis_declared": True,
            "eligible_for_later_reception_review_only": True,
        },
        "admissibility_basis": {
            "admissibility_basis_declared": True,
            "admissible_for_later_reception_review_only": True,
        },
        "review_readiness_limits": {
            "review_readiness_limits_declared": True,
            "recognition_requires_separate_boundary": True,
        },
    }
    return {
        "source_body_reception_eligibility_metadata": {
            "source_body_reception_eligibility_result_id": (
                "source_body_reception_eligibility__eligibility-001"
            ),
            "source_body_reception_eligibility_result_version": "0.1.0",
            "resolver_module": (
                "resolve_source_body_reception_eligibility_admissibility_boundary"
            ),
        },
        "outcome": ELIGIBLE,
        "source_body_reception_eligibility_summary": {
            "outcome": ELIGIBLE,
            "failed_check_count": 0,
            "selected_eligibility_result_failed_check_count": 0,
            "selected_eligibility_result_id": (
                "source_body_reception_eligibility__eligibility-001"
            ),
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
            "eligible_for_review_only": True,
            "reception_recognized": False,
            "reception_authorized": False,
            "source_received": False,
            "selected_source_body_surface_identifier": (
                surface["selected_source_body_surface_identifier"]
            ),
            "selected_source_body_surface_type": (
                surface["selected_source_body_surface_type"]
            ),
            "selected_source_body_surface_reference": (
                surface["selected_source_body_surface_reference"]
            ),
            "receiving_context_id": context["receiving_context_id"],
            "receiving_context_type": context["receiving_context_type"],
            "receiving_context_role_class": role["receiving_context_role_class"],
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": reception_purpose(),
        },
        "selected_receiving_context_role_result": role_result,
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "eligibility_basis": eligibility_basis,
        "admissibility_basis": eligibility_basis["admissibility_basis"],
        "review_readiness_limits": eligibility_basis["review_readiness_limits"],
        "eligibility_statement": statement,
        "eligibility_checks": [{"check_name": "synthetic eligibility", "passed": True}],
        "non_claims": {
            key: False
            for key in (
                "reception_recognized",
                "reception_authorized",
                "source_received",
                "non_capture_passed",
                "reception_recognition_passed",
                "adoption_created",
                "authority_created",
                "currentness_created",
                "standing_created",
                "standing_propagated",
                "source_validated_by_receiving_context",
                "source_invalidated_by_receiving_context",
                "source_replaced",
                "operation_permission_created",
                "receiving_context_governance_created",
                "publication_flow_opened",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
                "continuation_authorized",
                "mutation_performed",
                "replay_performed",
                "merge_performed",
            )
        },
    }


def non_capture_basis() -> dict[str, object]:
    return {
        "non_capture_basis_declared": True,
        "non_capture_review_only": True,
        "selected_source_body_surface_remains_uncaptured": True,
        "receiving_context_remains_context_only": True,
        "authority_capture_checked_and_refused": True,
        "validation_capture_checked_and_refused": True,
        "invalidation_capture_checked_and_refused": True,
        "source_replacement_capture_checked_and_refused": True,
        "operation_permission_capture_checked_and_refused": True,
        "governance_capture_checked_and_refused": True,
        "publication_flow_capture_checked_and_refused": True,
    }


def non_adoption_basis() -> dict[str, object]:
    return {
        "non_adoption_basis_declared": True,
        "adoption_risk_checked_and_refused": True,
        "adoption_remains_false": True,
        "no_review_posture_adopted_selected_source_body_surface": True,
        "non_adoption_is_not_adoption": True,
        "non_adoption_does_not_authorize_reception": True,
        "non_adoption_does_not_receive_source": True,
    }


def non_currentness_basis() -> dict[str, object]:
    return {
        "non_currentness_basis_declared": True,
        "currentness_risk_checked_and_refused": True,
        "currentness_remains_false": True,
        "selected_source_body_surface_was_not_made_current": True,
        "receiving_context_was_not_made_current": True,
        "latest_artifact_or_carrier_context_did_not_create_currentness": True,
        "non_currentness_is_not_currentness": True,
        "non_currentness_does_not_authorize_reception": True,
        "non_currentness_does_not_receive_source": True,
    }


def recognition_dependency() -> dict[str, object]:
    return {
        "recognition_dependency_declared": True,
        "recognition_requires_separate_boundary": True,
        "recognition_remains_future_work": True,
        "reception_recognition_passed": False,
        "reception_recognized": False,
        "reception_authorized": False,
        "source_received": False,
    }


def declared_non_capture_request(**overrides: object) -> dict[str, object]:
    selected = selected_eligibility_result()
    request = {
        "non_capture_request_id": "source-body-reception-non-capture-request-001",
        "non_capture_question": (
            "Did this eligible source-body reception request pass non-capture, "
            "non-adoption, and non-currentness review?"
        ),
        "non_capture_intent": "RECORD_SOURCE_BODY_RECEPTION_NON_CAPTURE",
        "selected_eligibility_result": selected,
        "selected_eligibility_result_id": (
            "source_body_reception_eligibility__eligibility-001"
        ),
        "selected_eligibility_result_outcome": ELIGIBLE,
        "non_capture_basis": non_capture_basis(),
        "non_adoption_basis": non_adoption_basis(),
        "non_currentness_basis": non_currentness_basis(),
        "non_capture_scope": list(SUPPORTED_SCOPE),
        "requested_non_capture_outcome": PASSED,
        "recognition_dependency": recognition_dependency(),
        "declared_non_claims": false_non_capture_non_claims(),
    }
    request.update(overrides)
    return request


def remove_key_recursive(value: object, key_to_remove: str) -> None:
    if isinstance(value, dict):
        value.pop(key_to_remove, None)
        for nested in value.values():
            remove_key_recursive(nested, key_to_remove)
    elif isinstance(value, list):
        for nested in value:
            remove_key_recursive(nested, key_to_remove)


def block_code(result: dict[str, object]) -> object:
    return result["block"]["code"]


class SourceBodyReceptionNonCaptureBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict[str, object]) -> dict[str, object]:
        return resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary(
            declared_non_capture_request=request
        )

    def assert_boundary_result(self, result: dict[str, object]) -> None:
        self.assertIsInstance(result, dict)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))

    def assert_no_forbidden_claims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        statement = result["non_capture_statement"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertFalse(non_claims[key], key)
            self.assertFalse(statement[key], key)
        if result["outcome"] == PASSED:
            for key in ALLOWED_PASSED_TRUE_FIELDS:
                self.assertTrue(non_claims[key], key)
        else:
            for key in ALLOWED_PASSED_TRUE_FIELDS:
                self.assertFalse(non_claims[key], key)

    def assert_blocked(self, result: dict[str, object], code: str) -> None:
        self.assert_boundary_result(result)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(code, block_code(result))
        self.assertFalse(result["non_capture_statement"]["non_capture_passed"])
        self.assert_no_forbidden_claims(result)

    def test_successful_non_capture_passed_result(self) -> None:
        request = declared_non_capture_request()
        request_before = copy.deepcopy(request)
        result = self.resolve(request)

        self.assertEqual(request_before, request)
        self.assert_boundary_result(result)
        self.assertEqual(PASSED, result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(0, result["source_body_reception_non_capture_summary"]["failed_check_count"])

        statement = result["non_capture_statement"]
        for key in (
            "source_body_reception_non_capture_passed",
            "non_capture_boundary_recorded",
            "non_capture_passed",
            "non_adoption_passed",
            "non_currentness_passed",
            "selected_eligibility_result_preserved",
            "selected_eligibility_result_recorded",
            "selected_eligibility_result_failed_check_count_zero",
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
            "receiving_context_role_preserved",
            "receiving_context_role_remains_bounded",
            "eligibility_admissibility_is_review_readiness_only",
            "adoption_risk_checked_and_refused",
            "currentness_risk_checked_and_refused",
            "authority_capture_checked_and_refused",
            "validation_capture_checked_and_refused",
            "invalidation_capture_checked_and_refused",
            "source_replacement_capture_checked_and_refused",
            "operation_permission_capture_checked_and_refused",
            "governance_capture_checked_and_refused",
            "publication_flow_capture_checked_and_refused",
            "recognition_dependency_preserved",
            "recognition_requires_separate_boundary",
        ):
            self.assertTrue(statement[key], key)
        self.assert_no_forbidden_claims(result)

    def test_metadata_and_declared_non_capture_question(self) -> None:
        result = self.resolve(declared_non_capture_request())
        metadata = result["source_body_reception_non_capture_metadata"]
        for key in (
            "source_body_reception_non_capture_result_id",
            "source_body_reception_non_capture_result_type",
            "source_body_reception_non_capture_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["source_body_reception_non_capture_result_version"])
        self.assertEqual(
            "resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary",
            metadata["resolver_module"],
        )

        declared = result["declared_non_capture_question"]
        self.assertEqual("source-body-reception-non-capture-request-001", declared["non_capture_request_id"])
        self.assertEqual("RECORD_SOURCE_BODY_RECEPTION_NON_CAPTURE", declared["non_capture_intent"])
        self.assertEqual(ELIGIBLE, declared["selected_eligibility_result_outcome"])
        self.assertEqual("source-body-surface-001", declared["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", declared["selected_source_body_surface_type"])
        self.assertEqual("receiving-context-001", declared["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", declared["receiving_context_type"])
        self.assertEqual("REFERENCE_RECEPTION", declared["reception_class"])
        self.assertTrue(declared["non_capture_is_not_reception"])
        self.assertTrue(declared["non_capture_is_not_authorization"])
        self.assertTrue(declared["non_capture_is_not_source_receipt"])
        self.assertTrue(declared["non_capture_is_not_recognition"])

    def test_selected_eligibility_surface_context_and_bases_preserved(self) -> None:
        request = declared_non_capture_request()
        selected_before = copy.deepcopy(request["selected_eligibility_result"])
        result = self.resolve(request)

        selected = result["selected_eligibility_result"]
        self.assertEqual("source_body_reception_eligibility__eligibility-001", selected["selected_eligibility_result_id"])
        self.assertEqual(ELIGIBLE, selected["selected_eligibility_result_outcome"])
        self.assertTrue(selected["selected_eligibility_outcome_is_eligible_admissible"])
        self.assertTrue(selected["selected_eligibility_result_failed_check_count_zero"])
        self.assertTrue(selected["selected_receiving_context_role_result_preserved"])
        self.assertTrue(selected["selected_identity_preservation_result_preserved"])
        self.assertTrue(selected["selected_reception_request_declaration_result_preserved"])
        self.assertTrue(selected["selected_source_body_surface_preserved"])
        self.assertTrue(selected["selected_source_body_surface_remains_source"])
        self.assertTrue(selected["selected_surface_is_not_whole_body_by_default"])
        self.assertTrue(selected["receiving_context_remains_context_only"])
        self.assertTrue(selected["eligibility_admissibility_is_review_readiness_only"])
        self.assertTrue(selected["eligibility_did_not_recognize_reception"])
        self.assertTrue(selected["eligibility_did_not_authorize_reception"])
        self.assertTrue(selected["eligibility_did_not_receive_source"])
        self.assertTrue(selected["eligibility_did_not_claim_non_capture_passed"])
        self.assertTrue(selected["eligibility_did_not_claim_recognition_passed"])
        self.assertEqual(selected_before, request["selected_eligibility_result"])

        surface = result["selected_source_body_surface"]
        self.assertEqual("source-body-surface-001", surface["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", surface["selected_source_body_surface_type"])
        self.assertEqual(
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            surface["selected_source_body_surface_reference"],
        )
        self.assertTrue(surface["selected_source_body_surface_remains_source"])
        self.assertTrue(surface["selected_source_body_surface_is_not_whole_body_by_default"])
        self.assertTrue(surface["selected_source_body_surface_is_not_received"])
        self.assertTrue(surface["selected_source_body_surface_is_not_adopted"])
        self.assertTrue(surface["selected_source_body_surface_is_not_replaced"])
        self.assertTrue(surface["selected_source_body_surface_is_not_validated_by_receiving_context"])
        self.assertTrue(surface["selected_source_body_surface_is_not_invalidated_by_receiving_context"])

        context = result["receiving_context"]
        self.assertEqual("receiving-context-001", context["receiving_context_id"])
        self.assertEqual("bounded receiving context", context["receiving_context_name"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", context["receiving_context_type"])
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
            self.assertTrue(context[key], key)

        basis = result["non_capture_basis"]
        for key in (
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
            "eligibility_basis",
            "admissibility_basis",
            "review_readiness_limits",
            "non_capture_basis",
        ):
            self.assertIn(key, basis)
        for key in (
            "non_capture_review_only",
            "selected_source_body_surface_remains_uncaptured",
            "receiving_context_remains_context_only",
            "authority_capture_checked_and_refused",
            "validation_capture_checked_and_refused",
            "invalidation_capture_checked_and_refused",
            "source_replacement_capture_checked_and_refused",
            "operation_permission_capture_checked_and_refused",
            "governance_capture_checked_and_refused",
            "publication_flow_capture_checked_and_refused",
            "recognition_dependency_preserved",
        ):
            self.assertTrue(basis[key], key)

        adoption = result["non_adoption_basis"]
        self.assertTrue(adoption["adoption_risk_checked_and_refused"])
        self.assertTrue(adoption["adoption_remains_false"])
        self.assertTrue(adoption["non_adoption_is_not_adoption"])
        self.assertTrue(adoption["non_adoption_does_not_authorize_reception"])
        self.assertTrue(adoption["non_adoption_does_not_receive_source"])

        currentness = result["non_currentness_basis"]
        self.assertTrue(currentness["currentness_risk_checked_and_refused"])
        self.assertTrue(currentness["currentness_remains_false"])
        self.assertTrue(currentness["selected_source_body_surface_was_not_made_current_by_this_boundary"])
        self.assertTrue(currentness["receiving_context_was_not_made_current_by_this_boundary"])
        self.assertTrue(currentness["non_currentness_is_not_currentness"])
        self.assertTrue(currentness["non_currentness_does_not_authorize_reception"])
        self.assertTrue(currentness["non_currentness_does_not_receive_source"])

    def test_supported_scope_values_and_checks(self) -> None:
        for scope_value in SUPPORTED_SCOPE:
            with self.subTest(scope_value=scope_value):
                result = self.resolve(declared_non_capture_request(non_capture_scope=[scope_value]))
                self.assertEqual(PASSED, result["outcome"])
                self.assertIn(scope_value, result["non_capture_scope"]["selected_non_capture_scope_values"])

        result = self.resolve(declared_non_capture_request())
        self.assertTrue(result["non_capture_scope"]["all_selected_scope_values_supported"])
        for check in result["non_capture_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertTrue(check["passed"], check["check_name"])
        check_names = {check["check_name"] for check in result["non_capture_checks"]}
        for expected in (
            "non_capture_question_declared",
            "non_capture_intent_supported",
            "selected_eligibility_result_present",
            "selected_eligibility_outcome_declared",
            "selected_eligibility_outcome_eligible_admissible",
            "selected_eligibility_failed_check_count_zero",
            "selected_receiving_context_role_result_preserved",
            "selected_identity_preservation_result_preserved",
            "selected_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "receiving_context_remains_context_only",
            "eligibility_admissibility_review_readiness_only",
            "reception_unrecognized",
            "reception_unauthorized",
            "source_unreceived",
            "non_capture_basis_declared",
            "non_adoption_basis_declared",
            "non_currentness_basis_declared",
            "recognition_dependency_declared",
            "adoption_remains_false",
            "authority_remains_false",
            "currentness_remains_false",
            "standing_remains_false",
            "source_validation_false",
            "source_invalidation_false",
            "source_replacement_false",
            "operation_permission_false",
            "receiving_context_governance_false",
            "publication_flow_false",
            "public_readiness_false",
            "final_completion_false",
            "follow_on_work_false",
            "continuation_false",
            "recognition_future",
            "recognition_passed_false",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        ):
            self.assertIn(expected, check_names)

    def test_non_meaning_remaining_open_and_summary(self) -> None:
        result = self.resolve(declared_non_capture_request())
        non_meaning = result["non_capture_non_meaning"]
        for key in (
            "does_not_mean_reception_recognized",
            "does_not_mean_reception_authorized",
            "does_not_mean_source_received",
            "does_not_mean_source_adopted",
            "does_not_mean_source_validated",
            "does_not_mean_source_invalidated",
            "does_not_mean_source_replaced",
            "does_not_mean_receiving_context_became_source",
            "does_not_mean_receiving_context_became_authority",
            "does_not_mean_receiving_context_became_current",
            "does_not_mean_receiving_context_became_receiver",
            "does_not_mean_receiving_context_became_adopter",
            "does_not_mean_receiving_context_became_validator",
            "does_not_mean_receiving_context_became_invalidator",
            "does_not_mean_receiving_context_became_operator",
            "does_not_mean_receiving_context_governance_created",
            "does_not_mean_standing_created",
            "does_not_mean_standing_propagated",
            "does_not_mean_vessel_relation_created",
            "does_not_mean_derivative_relation_created",
            "does_not_mean_operation_permission_created",
            "does_not_mean_reception_recognition_passed",
            "does_not_mean_public_readiness_created",
            "does_not_mean_final_completion_claimed",
            "does_not_mean_follow_on_work_authorized",
            "does_not_mean_continuation_authorized",
            "does_not_mean_publication_flow_opened",
        ):
            self.assertTrue(non_meaning[key], key)

        remains_open = result["what_remains_open"]
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])
        for item in (
            "source-body reception recognition boundary",
            "source-body reception receipt / exhaustion boundary",
            "source-body reception conformance boundary",
            "source-body reception closure boundary",
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
        ):
            self.assertIn(item, remains_open["open_items"])

        summary = resolver.build_source_body_reception_non_capture_summary(result)
        self.assertEqual(PASSED, summary["outcome"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertTrue(summary["non_capture_passed"])
        self.assertTrue(summary["non_adoption_passed"])
        self.assertTrue(summary["non_currentness_passed"])
        self.assertFalse(summary["not_passed"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertTrue(summary["selected_eligibility_result_preserved"])
        self.assertTrue(summary["selected_eligibility_result_recorded"])
        self.assertTrue(summary["selected_eligibility_result_failed_check_count_zero"])
        self.assertTrue(summary["selected_receiving_context_role_result_preserved"])
        self.assertTrue(summary["selected_identity_preservation_result_preserved"])
        self.assertTrue(summary["selected_request_declaration_result_preserved"])
        self.assertTrue(summary["selected_source_body_surface_preserved"])
        self.assertTrue(summary["selected_source_body_surface_remains_source"])
        self.assertTrue(summary["receiving_context_remains_context_only"])
        self.assertTrue(summary["eligibility_admissibility_review_readiness_only"])
        self.assertTrue(summary["adoption_risk_checked_refused"])
        self.assertTrue(summary["currentness_risk_checked_refused"])
        self.assertTrue(summary["authority_capture_checked_refused"])
        self.assertTrue(summary["validation_capture_checked_refused"])
        self.assertTrue(summary["invalidation_capture_checked_refused"])
        self.assertTrue(summary["source_replacement_capture_checked_refused"])
        self.assertTrue(summary["operation_permission_capture_checked_refused"])
        self.assertTrue(summary["governance_capture_checked_refused"])
        self.assertTrue(summary["publication_flow_capture_checked_refused"])
        self.assertTrue(summary["recognition_dependency_preserved"])
        self.assertTrue(summary["recognition_requires_separate_boundary"])
        self.assertTrue(summary["no_reception_recognized"])
        self.assertTrue(summary["no_reception_authorized"])
        self.assertTrue(summary["no_source_received"])
        self.assertTrue(summary["no_recognition_passed"])
        self.assertTrue(summary["no_source_validation"])
        self.assertTrue(summary["no_source_invalidation"])
        self.assertTrue(summary["no_source_replacement"])
        self.assertTrue(summary["no_adoption"])
        self.assertTrue(summary["no_authority"])
        self.assertTrue(summary["no_currentness"])
        self.assertTrue(summary["no_standing"])
        self.assertTrue(summary["no_vessel_relation"])
        self.assertTrue(summary["no_derivative_relation"])
        self.assertTrue(summary["no_operation_permission"])
        self.assertTrue(summary["no_governance"])
        self.assertTrue(summary["no_publication_flow"])
        self.assertTrue(summary["no_public_readiness"])
        self.assertTrue(summary["no_final_completion"])
        self.assertTrue(summary["no_follow_on_work"])

    def test_additional_basis_and_not_passed_results(self) -> None:
        additional_context = {
            "missing_basis": [
                "non-capture basis too generic",
                "recognition dependency unclear",
            ],
            "additional_basis_not_scheduled": True,
        }
        additional = self.resolve(
            declared_non_capture_request(
                requested_non_capture_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, additional["outcome"])
        self.assertEqual(additional_context, additional["additional_basis_required"]["additional_basis_context"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        self.assert_no_forbidden_claims(additional)

        not_passed_basis_value = {
            "not_passed_reason": "capture risk cannot be bounded",
            "does_not_authorize_repair": True,
        }
        not_passed = self.resolve(
            declared_non_capture_request(
                requested_non_capture_outcome=NOT_PASSED,
                not_passed_basis=not_passed_basis_value,
            )
        )
        self.assertEqual(NOT_PASSED, not_passed["outcome"])
        self.assertEqual(not_passed_basis_value, not_passed["not_passed_basis"]["not_passed_basis"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_mutate"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_repair"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_authorize"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_receive"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_replace"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_validate"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_invalidate"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_create_currentness"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_claim_recognition_passed"])
        self.assertTrue(not_passed["not_passed_basis"]["does_not_recognize_reception"])
        self.assert_no_forbidden_claims(not_passed)

    def test_builder_helper_and_path_based_selected_eligibility(self) -> None:
        selected = selected_eligibility_result()
        request = resolver.build_declared_source_body_reception_non_capture_request(
            "source-body-reception-non-capture-request-001",
            "Did the request pass non-capture review?",
            selected,
            non_capture_basis(),
            non_adoption_basis(),
            non_currentness_basis(),
            list(SUPPORTED_SCOPE),
            selected_eligibility_result_id="source_body_reception_eligibility__eligibility-001",
            selected_eligibility_result_outcome=ELIGIBLE,
            recognition_dependency=recognition_dependency(),
            additional_basis_context={"basis": "not scheduled"},
            not_passed_basis={"reason": "not used"},
        )
        self.assertEqual("source-body-reception-non-capture-request-001", request["non_capture_request_id"])
        self.assertEqual(selected, request["selected_eligibility_result"])
        self.assertEqual(non_capture_basis(), request["non_capture_basis"])
        self.assertEqual(non_adoption_basis(), request["non_adoption_basis"])
        self.assertEqual(non_currentness_basis(), request["non_currentness_basis"])
        self.assertEqual(list(SUPPORTED_SCOPE), request["non_capture_scope"])
        for value in request["declared_non_claims"].values():
            self.assertFalse(value)
        result = self.resolve(request)
        self.assertEqual(PASSED, result["outcome"])

        with tempfile.TemporaryDirectory() as tmp:
            selected_path = Path(tmp) / "selected_eligibility.json"
            selected_path.write_text(json.dumps(selected), encoding="utf-8")
            path_request = declared_non_capture_request(
                selected_eligibility_result_path=str(selected_path),
                selected_eligibility_result={},
            )
            path_result = self.resolve(path_request)
            self.assertEqual(PASSED, path_result["outcome"])
            self.assertEqual(str(selected_path), path_result["selected_eligibility_result"]["selected_eligibility_result_path"])
            self.assertEqual(ELIGIBLE, path_result["selected_eligibility_result"]["selected_eligibility_result_outcome"])

    def test_path_based_request_and_write_behavior(self) -> None:
        request = declared_non_capture_request()
        with tempfile.TemporaryDirectory() as tmp:
            request_path = Path(tmp) / "declared_non_capture_request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary_from_path(
                request_path
            )
            mapping_result = self.resolve(request)
            self.assertEqual(PASSED, path_result["outcome"])
            self.assertEqual(set(mapping_result.keys()), set(path_result.keys()))
            self.assertEqual(
                str(request_path),
                path_result["declared_non_capture_question"]["declared_non_capture_request_path"],
            )

            output_path = Path(tmp) / "nested" / "non_capture_result.json"
            written = resolver.write_source_body_reception_non_capture_result(
                path_result, output_path
            )
            self.assertEqual(output_path, written)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed.keys()))

            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_NON_CAPTURE_BOUNDARY_ROOT",
                Path(tmp) / "default-root",
            ):
                first = resolver.write_source_body_reception_non_capture_result(path_result)
                second = resolver.write_source_body_reception_non_capture_result(path_result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn(
                "source_body_reception_non_capture_non_adoption_non_currentness_boundary",
                str(resolver.SOURCE_BODY_RECEPTION_NON_CAPTURE_BOUNDARY_ROOT),
            )
            self.assertNotIn(
                "source_body_reception_eligibility_admissibility_boundary",
                str(resolver.SOURCE_BODY_RECEPTION_NON_CAPTURE_BOUNDARY_ROOT),
            )
            self.assertNotIn(
                "source_body_reception_recognition",
                str(resolver.SOURCE_BODY_RECEPTION_NON_CAPTURE_BOUNDARY_ROOT),
            )

    def test_non_mutation_posture(self) -> None:
        request = declared_non_capture_request()
        selected_before = copy.deepcopy(request["selected_eligibility_result"])
        role_before = copy.deepcopy(
            request["selected_eligibility_result"]["selected_receiving_context_role_result"]
        )
        identity_before = copy.deepcopy(
            request["selected_eligibility_result"]["eligibility_basis"]["selected_identity_preservation_result"]
        )
        declaration_before = copy.deepcopy(
            request["selected_eligibility_result"]["eligibility_basis"]["selected_reception_request_declaration_result"]
        )
        surface_before = copy.deepcopy(request["selected_eligibility_result"]["selected_source_body_surface"])
        context_before = copy.deepcopy(request["selected_eligibility_result"]["receiving_context"])
        non_capture_basis_before = copy.deepcopy(request["non_capture_basis"])
        non_adoption_basis_before = copy.deepcopy(request["non_adoption_basis"])
        non_currentness_basis_before = copy.deepcopy(request["non_currentness_basis"])
        scope_before = copy.deepcopy(request["non_capture_scope"])
        request_before = copy.deepcopy(request)

        first = self.resolve(request)
        second = self.resolve(request)
        self.assertEqual(PASSED, first["outcome"])
        self.assertEqual(PASSED, second["outcome"])
        self.assertEqual(request_before, request)
        self.assertEqual(selected_before, request["selected_eligibility_result"])
        self.assertEqual(role_before, request["selected_eligibility_result"]["selected_receiving_context_role_result"])
        self.assertEqual(identity_before, request["selected_eligibility_result"]["eligibility_basis"]["selected_identity_preservation_result"])
        self.assertEqual(declaration_before, request["selected_eligibility_result"]["eligibility_basis"]["selected_reception_request_declaration_result"])
        self.assertEqual(surface_before, request["selected_eligibility_result"]["selected_source_body_surface"])
        self.assertEqual(context_before, request["selected_eligibility_result"]["receiving_context"])
        self.assertEqual(non_capture_basis_before, request["non_capture_basis"])
        self.assertEqual(non_adoption_basis_before, request["non_adoption_basis"])
        self.assertEqual(non_currentness_basis_before, request["non_currentness_basis"])
        self.assertEqual(scope_before, request["non_capture_scope"])

        with tempfile.TemporaryDirectory() as tmp:
            selected_path = Path(tmp) / "selected_eligibility.json"
            selected_path.write_text(json.dumps(selected_before), encoding="utf-8")
            before_text = selected_path.read_text(encoding="utf-8")
            path_request = declared_non_capture_request(
                selected_eligibility_result_path=str(selected_path),
                selected_eligibility_result={},
            )
            result = self.resolve(path_request)
            output = resolver.write_source_body_reception_non_capture_result(
                result, Path(tmp) / "new" / "result.json"
            )
            self.assertTrue(output.exists())
            self.assertEqual(before_text, selected_path.read_text(encoding="utf-8"))

    def test_explicit_missing_malformed_and_path_blocks(self) -> None:
        explicit = self.resolve(
            declared_non_capture_request(
                non_capture_intent="BLOCK_SOURCE_BODY_RECEPTION_NON_CAPTURE_REVIEW"
            )
        )
        self.assertEqual(BLOCKED, explicit["outcome"])
        self.assertIn(
            block_code(explicit),
            {"NON_CAPTURE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"},
        )
        self.assertFalse(explicit["non_capture_statement"]["non_capture_passed"])

        self.assert_blocked(
            resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary(),
            "NON_CAPTURE_QUESTION_UNDECLARED",
        )
        self.assert_blocked(
            resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary(
                declared_non_capture_request=["not", "a", "mapping"]
            ),
            "DECLARED_NON_CAPTURE_REQUEST_MALFORMED",
        )

        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            self.assert_blocked(
                resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary_from_path(
                    missing
                ),
                "DECLARED_NON_CAPTURE_REQUEST_UNREADABLE",
            )
            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            self.assertEqual(
                "DECLARED_NON_CAPTURE_REQUEST_UNREADABLE",
                block_code(
                    resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary_from_path(
                        malformed
                    )
                ),
            )
            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_blocked(
                resolver.resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary_from_path(
                    array_path
                ),
                "DECLARED_NON_CAPTURE_REQUEST_MALFORMED",
            )

    def test_selected_eligibility_path_and_result_issue_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing-selected.json"
            self.assert_blocked(
                self.resolve(declared_non_capture_request(selected_eligibility_result_path=str(missing))),
                "ELIGIBILITY_RESULT_UNREADABLE",
            )
            malformed = Path(tmp) / "malformed-selected.json"
            malformed.write_text("{not json", encoding="utf-8")
            self.assert_blocked(
                self.resolve(declared_non_capture_request(selected_eligibility_result_path=str(malformed))),
                "ELIGIBILITY_RESULT_UNREADABLE",
            )
            array_path = Path(tmp) / "array-selected.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_blocked(
                self.resolve(declared_non_capture_request(selected_eligibility_result_path=str(array_path))),
                "ELIGIBILITY_RESULT_MALFORMED",
            )

        missing_outcome = selected_eligibility_result()
        missing_outcome.pop("outcome")
        missing_outcome["source_body_reception_eligibility_summary"].pop("outcome")
        request = declared_non_capture_request(
            selected_eligibility_result=missing_outcome,
            selected_eligibility_result_outcome=None,
        )
        self.assert_blocked(self.resolve(request), "ELIGIBILITY_RESULT_OUTCOME_MISSING")

        not_eligible = selected_eligibility_result()
        not_eligible["outcome"] = "SOURCE_BODY_RECEPTION_NOT_ELIGIBLE_OR_ADMISSIBLE"
        not_eligible["source_body_reception_eligibility_summary"]["outcome"] = (
            "SOURCE_BODY_RECEPTION_NOT_ELIGIBLE_OR_ADMISSIBLE"
        )
        request = declared_non_capture_request(
            selected_eligibility_result=not_eligible,
            selected_eligibility_result_outcome=None,
        )
        self.assert_blocked(self.resolve(request), "ELIGIBILITY_RESULT_NOT_ELIGIBLE_ADMISSIBLE")

        failed = selected_eligibility_result()
        failed["source_body_reception_eligibility_summary"]["failed_check_count"] = 1
        request = declared_non_capture_request(selected_eligibility_result=failed)
        self.assert_blocked(self.resolve(request), "ELIGIBILITY_RESULT_HAS_FAILED_CHECKS")

    def test_missing_required_basis_blocks(self) -> None:
        selected_missing_cases = {
            "selected_receiving_context_role_result": "RECEIVING_CONTEXT_ROLE_RESULT_MISSING",
            "selected_identity_preservation_result": "IDENTITY_PRESERVATION_RESULT_MISSING",
            "selected_reception_request_declaration_result": "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
            "selected_source_body_surface": "SELECTED_SOURCE_BODY_SURFACE_MISSING",
            "receiving_context": "RECEIVING_CONTEXT_MISSING",
            "receiving_context_type": "RECEIVING_CONTEXT_TYPE_MISSING",
            "selected_receiving_context_role": "RECEIVING_CONTEXT_ROLE_MISSING",
            "receiving_context_role_class": "RECEIVING_CONTEXT_ROLE_CLASS_MISSING",
            "reception_class": "RECEPTION_CLASS_MISSING",
            "reception_purpose": "RECEPTION_PURPOSE_MISSING",
            "reception_limits": "RECEPTION_LIMITS_MISSING",
        }
        for missing_key, expected_code in selected_missing_cases.items():
            with self.subTest(missing_key=missing_key):
                selected = selected_eligibility_result()
                remove_key_recursive(selected, missing_key)
                if missing_key == "selected_receiving_context_role":
                    remove_key_recursive(selected, "receiving_context_role")
                request = declared_non_capture_request(selected_eligibility_result=selected)
                self.assert_blocked(self.resolve(request), expected_code)

        request_missing_cases = {
            "non_capture_basis": "NON_CAPTURE_BASIS_MISSING",
            "non_adoption_basis": "NON_ADOPTION_BASIS_MISSING",
            "non_currentness_basis": "NON_CURRENTNESS_BASIS_MISSING",
            "recognition_dependency": "RECOGNITION_DEPENDENCY_MISSING",
        }
        for missing_key, expected_code in request_missing_cases.items():
            with self.subTest(missing_key=missing_key):
                request = declared_non_capture_request()
                request.pop(missing_key)
                self.assert_blocked(self.resolve(request), expected_code)

    def test_malformed_surface_context_and_unsupported_scope_blocks(self) -> None:
        selected = selected_eligibility_result()
        selected["selected_source_body_surface"] = "not a mapping"
        self.assert_blocked(
            self.resolve(declared_non_capture_request(selected_eligibility_result=selected)),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        )

        selected = selected_eligibility_result()
        selected["receiving_context"] = "not a mapping"
        self.assert_blocked(
            self.resolve(declared_non_capture_request(selected_eligibility_result=selected)),
            "RECEIVING_CONTEXT_MALFORMED",
        )

        self.assert_blocked(
            self.resolve(declared_non_capture_request(non_capture_scope=["UNSUPPORTED_SCOPE"])),
            "UNSUPPORTED_NON_CAPTURE_SCOPE",
        )

    def test_collapse_flag_blocks(self) -> None:
        collapse_cases = {
            "reception_recognized": "NON_CAPTURE_RECOGNIZES_RECEPTION",
            "reception_authorized": "NON_CAPTURE_AUTHORIZES_RECEPTION",
            "source_received": "NON_CAPTURE_RECEIVES_SOURCE",
            "reception_recognition_passed": "NON_CAPTURE_CLAIMS_RECOGNITION_PASSED",
            "receiving_context_governance_created": "NON_CAPTURE_CREATES_GOVERNANCE",
            "receiving_context_became_source": "NON_CAPTURE_TREATS_CONTEXT_AS_SOURCE",
            "receiving_context_became_authority": "NON_CAPTURE_TREATS_CONTEXT_AS_AUTHORITY",
            "receiving_context_became_current": "NON_CAPTURE_TREATS_CONTEXT_AS_CURRENT",
            "receiving_context_became_receiver": "NON_CAPTURE_TREATS_CONTEXT_AS_RECEIVER",
            "receiving_context_became_adopter": "NON_CAPTURE_TREATS_CONTEXT_AS_ADOPTER",
            "receiving_context_became_validator": "NON_CAPTURE_TREATS_CONTEXT_AS_VALIDATOR",
            "receiving_context_became_invalidator": "NON_CAPTURE_TREATS_CONTEXT_AS_INVALIDATOR",
            "receiving_context_became_operator": "NON_CAPTURE_TREATS_CONTEXT_AS_OPERATOR",
            "source_validated_by_receiving_context": "NON_CAPTURE_VALIDATES_SOURCE",
            "source_invalidated_by_receiving_context": "NON_CAPTURE_INVALIDATES_SOURCE",
            "source_replaced": "NON_CAPTURE_REPLACES_SOURCE",
            "adoption_created": "NON_CAPTURE_CREATES_ADOPTION",
            "authority_created": "NON_CAPTURE_CREATES_AUTHORITY",
            "currentness_created": "NON_CAPTURE_CREATES_CURRENTNESS",
            "standing_created": "NON_CAPTURE_CREATES_STANDING",
            "standing_propagated": "NON_CAPTURE_CREATES_STANDING_PROPAGATION",
            "vessel_relation_created": "NON_CAPTURE_CREATES_VESSEL_RELATION",
            "derivative_relation_created": "NON_CAPTURE_CREATES_DERIVATIVE_RELATION",
            "operation_permission_created": "NON_CAPTURE_CREATES_OPERATION_PERMISSION",
            "public_launch_readiness_created": "NON_CAPTURE_CREATES_PUBLIC_READINESS",
            "final_completion_claimed": "NON_CAPTURE_CLAIMS_FINAL_COMPLETION",
            "follow_on_work_authorized": "NON_CAPTURE_AUTHORIZES_FOLLOW_ON_WORK",
            "continuation_authorized": "NON_CAPTURE_AUTHORIZES_CONTINUATION",
            "publication_flow_opened": "NON_CAPTURE_OPENS_PUBLICATION_FLOW",
        }
        for field, expected_code in collapse_cases.items():
            with self.subTest(field=field):
                request = declared_non_capture_request(**{field: True})
                self.assert_blocked(self.resolve(request), expected_code)

    def test_mutation_replay_merge_and_required_non_claim_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = declared_non_capture_request(**{field: True})
                self.assert_blocked(self.resolve(request), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = declared_non_capture_request()
        missing_non_claim["declared_non_claims"].pop("source_received")
        self.assert_blocked(self.resolve(missing_non_claim), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = declared_non_capture_request()
        flipped_non_claim["declared_non_claims"]["source_received"] = True
        flipped = self.resolve(flipped_non_claim)
        self.assertEqual(BLOCKED, flipped["outcome"])
        self.assertIn(
            block_code(flipped),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "NON_CAPTURE_RECEIVES_SOURCE"},
        )


if __name__ == "__main__":
    unittest.main()
