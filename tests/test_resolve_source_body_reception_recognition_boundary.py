"""Executable boundary tests for source-body reception recognition only.

These tests prove that the resolver records bounded source-body reception
recognition for one non-capture-passed request / relation candidate. Recognition
is not authorization, not source receipt, not adoption, not authority, not
currentness, and not receipt / exhaustion, conformance, or closure.
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

import resolve_source_body_reception_recognition_boundary as resolver  # noqa: E402


RECORDED = "SOURCE_BODY_RECEPTION_RECOGNITION_RECORDED"
NOT_RECORDED = "SOURCE_BODY_RECEPTION_RECOGNITION_NOT_RECORDED"
REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_RECOGNITION_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "SOURCE_BODY_RECEPTION_RECOGNITION_REVIEW_BLOCKED"
NON_CAPTURE_PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED"
ELIGIBLE = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"
ROLE_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
IDENTITY_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_recognition_metadata",
    "declared_recognition_question",
    "selected_non_capture_result",
    "selected_source_body_surface",
    "receiving_context",
    "recognition_basis",
    "recognition_limits",
    "recognition_scope",
    "recognition_checks",
    "recognition_statement",
    "recognition_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_recognition_summary",
}

SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_RECOGNITION_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)


def false_recognition_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


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
        },
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
            "role_remains_bounded": True,
            "role_is_not_reception": True,
            "role_is_not_authorization": True,
            "role_is_not_source_receipt": True,
        },
    }
    return {
        "source_body_reception_receiving_context_role_metadata": {
            "source_body_reception_receiving_context_role_result_id": (
                "source_body_reception_receiving_context_role__role-001"
            ),
            "source_body_reception_receiving_context_role_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_receiving_context_role_boundary",
        },
        "outcome": ROLE_RECORDED,
        "source_body_reception_receiving_context_role_summary": {
            "outcome": ROLE_RECORDED,
            "failed_check_count": 0,
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
        "receiving_context_role_statement": {
            "receiving_context_role_preserved": True,
            "receiving_context_role_remains_bounded": True,
            "role_is_not_reception": True,
            "role_is_not_authorization": True,
            "role_is_not_source_receipt": True,
            "reception_recognized": False,
            "reception_authorized": False,
            "source_received": False,
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
        },
        "selected_receiving_context_role_result": role_result,
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "eligibility_basis": {
            "selected_receiving_context_role_result": role_result,
            "selected_identity_preservation_result": identity,
            "selected_reception_request_declaration_result": request_declaration,
            "selected_source_body_surface": surface,
            "source_body_identity_basis": surface["source_body_identity_basis"],
            "source_body_lineage_basis": surface["source_body_lineage_basis"],
            "receiving_context": context,
            "receiving_context_type": context["receiving_context_type"],
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": {
                "purpose_id": "bounded-reception-review",
                "purpose_statement": "Bounded reception-family review only.",
            },
            "reception_limits": {
                "reception_limits_id": "reception-limits-001",
                "no_authorization": True,
                "no_source_receipt": True,
            },
            "selected_receiving_context_role": role,
            "receiving_context_role_class": role["receiving_context_role_class"],
            "receiving_context_role_limits": role["receiving_context_role_limits"],
            "eligibility_basis": {"eligibility_basis_declared": True},
            "admissibility_basis": {"admissibility_basis_declared": True},
            "review_readiness_limits": {
                "review_readiness_limits_declared": True,
                "non_capture_requires_separate_boundary": True,
            },
        },
        "eligibility_statement": {
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
            "eligibility_admissibility_is_review_readiness_only": True,
            "eligibility_is_not_reception": True,
            "admissibility_is_not_authorization": True,
            "reception_recognized": False,
            "reception_authorized": False,
            "source_received": False,
            "non_capture_passed": False,
            "reception_recognition_passed": False,
        },
    }


def recognition_basis() -> dict[str, object]:
    return {
        "recognition_basis_declared": True,
        "bounded_recognition_only": True,
        "recognized_for_later_reception_family_accounting_only": True,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_currentness": True,
        "recognition_does_not_validate_source": True,
        "recognition_does_not_invalidate_source": True,
        "recognition_does_not_create_operation_permission": True,
        "receipt_exhaustion_requires_separate_boundary": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
    }


def recognition_limits() -> dict[str, object]:
    return {
        "recognition_limits_declared": True,
        "recognition_review_only": True,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_authority": True,
        "recognition_is_not_currentness": True,
        "recognition_is_not_validation": True,
        "recognition_is_not_invalidation": True,
        "recognition_is_not_operation_permission": True,
        "recognition_is_not_publication_flow": True,
        "receipt_exhaustion_requires_separate_boundary": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
    }


def selected_non_capture_result() -> dict[str, object]:
    eligibility = selected_eligibility_result()
    role_result = eligibility["selected_receiving_context_role_result"]
    identity = role_result["selected_identity_preservation_result"]
    request_declaration = identity["selected_reception_request_declaration_result"]
    surface = eligibility["selected_source_body_surface"]
    context = eligibility["receiving_context"]
    role = role_result["receiving_context_role"]
    non_capture_basis = {
        "selected_eligibility_result": eligibility,
        "selected_receiving_context_role_result": role_result,
        "selected_identity_preservation_result": identity,
        "selected_reception_request_declaration_result": request_declaration,
        "selected_source_body_surface": surface,
        "source_body_identity_basis": surface["source_body_identity_basis"],
        "source_body_lineage_basis": surface["source_body_lineage_basis"],
        "receiving_context": context,
        "receiving_context_type": context["receiving_context_type"],
        "reception_class": "REFERENCE_RECEPTION",
        "reception_purpose": {
            "purpose_id": "recognition-after-non-capture",
            "purpose_statement": "Bounded recognition review only.",
        },
        "reception_limits": {
            "reception_limits_id": "recognition-input-limits-001",
            "no_authorization": True,
            "no_source_receipt": True,
        },
        "selected_receiving_context_role": role,
        "receiving_context_role_class": role["receiving_context_role_class"],
        "receiving_context_role_limits": role["receiving_context_role_limits"],
        "eligibility_basis": eligibility["eligibility_basis"]["eligibility_basis"],
        "admissibility_basis": eligibility["eligibility_basis"]["admissibility_basis"],
        "review_readiness_limits": eligibility["eligibility_basis"][
            "review_readiness_limits"
        ],
        "non_capture_basis": {
            "non_capture_basis_declared": True,
            "authority_capture_checked_and_refused": True,
            "validation_capture_checked_and_refused": True,
            "invalidation_capture_checked_and_refused": True,
            "source_replacement_capture_checked_and_refused": True,
            "operation_permission_capture_checked_and_refused": True,
            "governance_capture_checked_and_refused": True,
            "publication_flow_capture_checked_and_refused": True,
        },
    }
    statement = {
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
        "eligibility_admissibility_is_review_readiness_only": True,
        "non_capture_passed": True,
        "non_adoption_passed": True,
        "non_currentness_passed": True,
        "non_capture_passed_as_refusal_check_outcome_only": True,
        "non_adoption_passed_as_refusal_check_outcome_only": True,
        "non_currentness_passed_as_refusal_check_outcome_only": True,
        "reception_authorized": False,
        "source_received": False,
        "reception_recognition_passed": False,
        "receiving_context_governance_created": False,
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
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "follow_on_work_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }
    return {
        "source_body_reception_non_capture_metadata": {
            "source_body_reception_non_capture_result_id": (
                "source_body_reception_non_capture__non-capture-001"
            ),
            "source_body_reception_non_capture_result_version": "0.1.0",
            "resolver_module": (
                "resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary"
            ),
        },
        "outcome": NON_CAPTURE_PASSED,
        "source_body_reception_non_capture_summary": {
            "outcome": NON_CAPTURE_PASSED,
            "failed_check_count": 0,
            "source_body_reception_non_capture_result_id": (
                "source_body_reception_non_capture__non-capture-001"
            ),
            "selected_source_body_surface_identifier": (
                surface["selected_source_body_surface_identifier"]
            ),
            "selected_source_body_surface_type": surface["selected_source_body_surface_type"],
            "selected_source_body_surface_reference": (
                surface["selected_source_body_surface_reference"]
            ),
            "receiving_context_id": context["receiving_context_id"],
            "receiving_context_type": context["receiving_context_type"],
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": non_capture_basis["reception_purpose"],
        },
        "selected_eligibility_result": {
            "raw_selected_eligibility_result": eligibility,
            "selected_eligibility_result_preserved": True,
        },
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "non_capture_basis": non_capture_basis,
        "non_adoption_basis": {
            "non_adoption_basis_declared": True,
            "adoption_risk_checked_and_refused": True,
            "adoption_remains_false": True,
        },
        "non_currentness_basis": {
            "non_currentness_basis_declared": True,
            "currentness_risk_checked_and_refused": True,
            "currentness_remains_false": True,
        },
        "non_capture_statement": statement,
        "non_capture_checks": [
            {"check_name": "synthetic non-capture check", "passed": True}
        ],
        "non_claims": {
            key: False
            for key in (
                "reception_recognized",
                "reception_authorized",
                "source_received",
                "reception_recognition_passed",
                "receiving_context_governance_created",
                "receiving_context_became_source",
                "receiving_context_became_authority",
                "receiving_context_became_current",
                "receiving_context_became_receiver",
                "receiving_context_became_adopter",
                "receiving_context_became_validator",
                "receiving_context_became_invalidator",
                "receiving_context_became_operator",
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


def declared_recognition_request(**overrides: object) -> dict[str, object]:
    selected = selected_non_capture_result()
    request = {
        "recognition_request_id": "source-body-reception-recognition-request-001",
        "recognition_question": (
            "Can this non-capture-passed source-body reception request be "
            "boundedly recognized?"
        ),
        "recognition_intent": "RECORD_SOURCE_BODY_RECEPTION_RECOGNITION",
        "selected_non_capture_result": selected,
        "selected_non_capture_result_id": (
            "source_body_reception_non_capture__non-capture-001"
        ),
        "selected_non_capture_result_outcome": NON_CAPTURE_PASSED,
        "recognition_basis": recognition_basis(),
        "recognition_limits": recognition_limits(),
        "recognition_scope": list(SUPPORTED_SCOPE),
        "requested_recognition_outcome": RECORDED,
        "declared_non_claims": false_recognition_non_claims(),
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


def contains_true_key(value: object, key: str) -> bool:
    if isinstance(value, dict):
        for nested_key, nested_value in value.items():
            if nested_key == key and nested_value is True:
                return True
            if contains_true_key(nested_value, key):
                return True
    elif isinstance(value, list):
        return any(contains_true_key(nested, key) for nested in value)
    return False


class SourceBodyReceptionRecognitionBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict[str, object] | None = None) -> dict[str, object]:
        return resolver.resolve_source_body_reception_recognition_boundary(
            declared_recognition_request=request
        )

    def assert_block(self, result: dict[str, object], code: str) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], code)

    def assert_no_downstream_claims(
        self, result: dict[str, object], *, recorded: bool = False
    ) -> None:
        non_claims = result["non_claims"]
        statement = result["recognition_statement"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
            self.assertIs(statement[key], False, key)
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(non_claims[key], recorded, key)
            self.assertIs(statement[key], recorded, key)

    def test_successful_recognition_recorded_result(self) -> None:
        request = declared_recognition_request()
        original = copy.deepcopy(request)

        result = self.resolve(request)

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["source_body_reception_recognition_summary"]["failed_check_count"],
            0,
        )
        self.assertEqual(request, original)

        metadata = result["source_body_reception_recognition_metadata"]
        self.assertTrue(metadata["source_body_reception_recognition_result_id"])
        self.assertTrue(metadata["source_body_reception_recognition_result_type"])
        self.assertEqual(
            metadata["source_body_reception_recognition_result_version"], "0.1.0"
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_source_body_reception_recognition_boundary",
        )

        declared = result["declared_recognition_question"]
        self.assertEqual(
            declared["recognition_request_id"],
            "source-body-reception-recognition-request-001",
        )
        self.assertEqual(
            declared["selected_non_capture_result_outcome"], NON_CAPTURE_PASSED
        )
        self.assertEqual(declared["reception_class"], "REFERENCE_RECEPTION")
        self.assertTrue(declared["recognition_is_not_authorization"])
        self.assertTrue(declared["recognition_is_not_source_receipt"])
        self.assertTrue(declared["recognition_is_not_adoption"])
        self.assertTrue(declared["recognition_is_not_currentness"])

        selected = result["selected_non_capture_result"]
        self.assertEqual(selected["selected_non_capture_result_outcome"], NON_CAPTURE_PASSED)
        self.assertTrue(selected["selected_non_capture_outcome_is_passed"])
        self.assertTrue(selected["selected_non_capture_result_failed_check_count_zero"])
        self.assertTrue(selected["selected_non_capture_result_preserved"])
        self.assertTrue(selected["selected_non_capture_result_recorded"])
        self.assertTrue(selected["selected_eligibility_result_preserved"])
        self.assertTrue(selected["selected_receiving_context_role_result_preserved"])
        self.assertTrue(selected["selected_identity_preservation_result_preserved"])
        self.assertTrue(
            selected["selected_reception_request_declaration_result_preserved"]
        )
        self.assertTrue(selected["selected_source_body_surface_preserved"])
        self.assertTrue(selected["selected_source_body_surface_remains_source"])
        self.assertTrue(selected["selected_surface_is_not_whole_body_by_default"])
        self.assertTrue(selected["receiving_context_preserved"])
        self.assertTrue(selected["receiving_context_remains_context_only"])
        self.assertTrue(selected["receiving_context_is_not_source"])
        self.assertTrue(selected["receiving_context_is_not_authority"])
        self.assertTrue(selected["receiving_context_is_not_current"])
        self.assertTrue(selected["non_capture_passed_as_refusal_check_outcome_only"])
        self.assertTrue(selected["non_adoption_passed_as_refusal_check_outcome_only"])
        self.assertTrue(selected["non_currentness_passed_as_refusal_check_outcome_only"])
        self.assertTrue(selected["non_capture_did_not_authorize_reception"])
        self.assertTrue(selected["non_capture_did_not_receive_source"])
        self.assertTrue(selected["non_capture_did_not_claim_recognition_passed"])

        surface = result["selected_source_body_surface"]
        self.assertEqual(
            surface["selected_source_body_surface_identifier"],
            "source-body-surface-001",
        )
        self.assertEqual(
            surface["selected_source_body_surface_type"],
            "REFERENCE_SOURCE_BODY_SURFACE",
        )
        self.assertTrue(surface["selected_source_body_surface_reference"])
        self.assertTrue(surface["source_body_identity_basis"])
        self.assertTrue(surface["source_body_lineage_basis"])
        self.assertTrue(surface["selected_source_body_surface_remains_source"])
        self.assertTrue(surface["selected_source_body_surface_is_not_whole_body_by_default"])
        self.assertTrue(surface["selected_source_body_surface_is_not_received"])
        self.assertTrue(surface["selected_source_body_surface_is_not_adopted"])
        self.assertTrue(surface["selected_source_body_surface_is_not_replaced"])
        self.assertTrue(
            surface[
                "selected_source_body_surface_is_not_validated_by_receiving_context"
            ]
        )
        self.assertTrue(
            surface[
                "selected_source_body_surface_is_not_invalidated_by_receiving_context"
            ]
        )

        context = result["receiving_context"]
        self.assertEqual(context["receiving_context_id"], "receiving-context-001")
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
            self.assertTrue(context[key], key)

        basis = result["recognition_basis"]
        for key in (
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
            "eligibility_basis",
            "admissibility_basis",
            "review_readiness_limits",
            "non_capture_basis",
            "non_adoption_basis",
            "non_currentness_basis",
            "recognition_basis",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "bounded_recognition_only",
            "recognized_for_later_reception_family_accounting_only",
            "recognition_is_not_authorization",
            "recognition_is_not_source_receipt",
            "recognition_is_not_adoption",
            "recognition_is_not_currentness",
            "recognition_does_not_validate_source",
            "recognition_does_not_invalidate_source",
            "recognition_does_not_create_operation_permission",
            "receipt_exhaustion_requires_separate_boundary",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(basis[key], key)

        limits = result["recognition_limits"]
        self.assertEqual(limits["recognition_limits"], recognition_limits())
        for key in (
            "recognition_review_only",
            "recognition_is_not_authorization",
            "recognition_is_not_source_receipt",
            "recognition_is_not_adoption",
            "recognition_is_not_authority",
            "recognition_is_not_currentness",
            "recognition_is_not_validation",
            "recognition_is_not_invalidation",
            "recognition_is_not_operation_permission",
            "recognition_is_not_publication_flow",
            "receipt_exhaustion_requires_separate_boundary",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(limits[key], key)

        scope = result["recognition_scope"]
        self.assertEqual(set(scope["selected_recognition_scope_values"]), set(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_scope_values_supported"])
        self.assertEqual(scope["unsupported_recognition_scope_values"], [])

        checks = result["recognition_checks"]
        self.assertTrue(checks)
        self.assertTrue(all(check["passed"] for check in checks))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
        check_names = {check["check_name"] for check in checks}
        expected_checks = {
            "recognition_question_declared",
            "recognition_intent_supported",
            "selected_non_capture_result_present",
            "selected_non_capture_outcome_declared",
            "selected_non_capture_outcome_passed",
            "selected_non_capture_failed_check_count_zero",
            "selected_eligibility_result_preserved",
            "selected_receiving_context_role_result_preserved",
            "selected_identity_preservation_result_preserved",
            "selected_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "selected_source_body_surface_remains_source",
            "selected_surface_is_not_whole_body_by_default",
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "eligibility_admissibility_review_readiness_only",
            "non_capture_passed_refusal_check_only",
            "non_adoption_passed_refusal_check_only",
            "non_currentness_passed_refusal_check_only",
            "recognition_basis_declared",
            "recognition_limits_declared",
            "recognition_scope_supported",
            "recognition_is_not_authorization",
            "recognition_does_not_receive_source",
            "recognition_does_not_create_source_receipt",
            "recognition_does_not_create_adoption",
            "recognition_does_not_create_authority",
            "recognition_does_not_create_currentness",
            "recognition_does_not_validate_source",
            "recognition_does_not_invalidate_source",
            "recognition_does_not_replace_source",
            "recognition_does_not_create_operation_permission",
            "recognition_does_not_create_governance",
            "recognition_does_not_open_publication_flow",
            "recognition_does_not_create_public_readiness",
            "recognition_does_not_claim_final_completion",
            "recognition_does_not_authorize_continuation",
            "recognition_does_not_authorize_follow_on_work",
            "receipt_exhaustion_remains_future_work",
            "conformance_remains_future_work",
            "closure_remains_future_work",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_checks.issubset(check_names))

        statement = result["recognition_statement"]
        for key in (
            "source_body_reception_recognition_recorded",
            "reception_recognized",
            "selected_non_capture_result_preserved",
            "selected_non_capture_result_recorded",
            "selected_non_capture_result_failed_check_count_zero",
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
            "eligibility_admissibility_is_review_readiness_only",
            "non_capture_passed_as_refusal_check_outcome_only",
            "non_adoption_passed_as_refusal_check_outcome_only",
            "non_currentness_passed_as_refusal_check_outcome_only",
            "bounded_recognition_for_accounting_only",
            "recognition_is_not_authorization",
            "recognition_is_not_source_receipt",
            "recognition_is_not_adoption",
            "recognition_is_not_authority",
            "recognition_is_not_currentness",
            "recognition_is_not_validation",
            "recognition_is_not_invalidation",
            "recognition_is_not_operation_permission",
            "recognition_is_not_publication_flow",
            "receipt_exhaustion_requires_separate_boundary",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(statement[key], key)
        self.assert_no_downstream_claims(result, recorded=True)

        non_meaning = result["recognition_non_meaning"]
        for meaning in (
            "reception_authorized",
            "source_received",
            "source_receipt_recorded",
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
            "receipt_exhaustion_completed",
            "conformance_passed",
            "closure_recorded",
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
        ):
            self.assertTrue(non_meaning[f"does_not_mean_{meaning}"], meaning)

        additional = result["additional_basis_required"]
        self.assertFalse(additional["additional_basis_required"])
        self.assertTrue(additional["missing_basis_is_not_scheduled"])
        self.assertTrue(additional["missing_basis_is_not_authorized"])
        self.assertTrue(additional["missing_basis_is_not_executed"])

        open_section = result["what_remains_open"]
        for item in (
            "source-body reception recognition test",
            "source-body reception recognition live artifact",
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
            self.assertIn(item, open_section["open_items"])
        self.assertTrue(open_section["open_means_not_scheduled"])
        self.assertTrue(open_section["open_means_not_authorized"])
        self.assertTrue(open_section["open_means_not_executed"])

    def test_supported_scope_values_and_unsupported_scope(self) -> None:
        for value in SUPPORTED_SCOPE:
            with self.subTest(value=value):
                result = self.resolve(declared_recognition_request(recognition_scope=[value]))
                self.assertEqual(result["outcome"], RECORDED)
                self.assertIn(value, result["recognition_scope"]["selected_recognition_scope_values"])
        result = self.resolve(
            declared_recognition_request(
                recognition_scope=list(SUPPORTED_SCOPE) + ["UNSUPPORTED_RECOGNITION_SCOPE"]
            )
        )
        self.assert_block(result, "UNSUPPORTED_RECOGNITION_SCOPE")

    def test_requires_additional_basis_and_not_recorded_results(self) -> None:
        additional_context = {
            "recognition_basis_too_generic": True,
            "receipt_exhaustion_dependency_unclear": True,
            "missing_basis_is_not_scheduled": True,
        }
        requires = self.resolve(
            declared_recognition_request(
                requested_recognition_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(requires["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(
            requires["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertTrue(
            requires["additional_basis_required"]["missing_basis_is_not_authorized"]
        )
        self.assert_no_downstream_claims(requires, recorded=False)

        not_recorded_basis = {
            "recognition_basis_cannot_be_bounded": True,
            "recognition_overread_as_source_receipt": True,
            "recognition_cannot_be_separated_from_closure": True,
        }
        not_recorded = self.resolve(
            declared_recognition_request(
                requested_recognition_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertEqual(
            not_recorded["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_basis,
        )
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_mutate"])
        self.assertTrue(
            not_recorded["not_recorded_basis"][
                "not_recorded_does_not_claim_conformance_or_closure"
            ]
        )
        self.assert_no_downstream_claims(not_recorded, recorded=False)

    def test_summary_helper_and_request_builder(self) -> None:
        selected = selected_non_capture_result()
        additional_context = {"recognition_limits_unclear": True}
        not_recorded_basis = {"recognition_overread_as_authorization": True}
        request = resolver.build_declared_source_body_reception_recognition_request(
            "recognition-builder-request-001",
            "Can this request be recognized for accounting only?",
            selected,
            recognition_basis(),
            recognition_limits(),
            list(SUPPORTED_SCOPE),
            selected_non_capture_result_id="selected-non-capture-builder-001",
            selected_non_capture_result_outcome=NON_CAPTURE_PASSED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )
        self.assertEqual(request["recognition_request_id"], "recognition-builder-request-001")
        self.assertEqual(request["recognition_question"], "Can this request be recognized for accounting only?")
        self.assertEqual(request["selected_non_capture_result"], selected)
        self.assertEqual(request["recognition_basis"], recognition_basis())
        self.assertEqual(request["recognition_limits"], recognition_limits())
        self.assertEqual(request["recognition_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_non_capture_result_id"], "selected-non-capture-builder-001")
        self.assertEqual(request["selected_non_capture_result_outcome"], NON_CAPTURE_PASSED)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertFalse(contains_true_key(request, key), key)

        result = self.resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        summary = resolver.build_source_body_reception_recognition_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["recognition_request_id"], "recognition-builder-request-001")
        self.assertEqual(summary["selected_non_capture_result_outcome"], NON_CAPTURE_PASSED)
        self.assertEqual(summary["passed_check_count"], len(result["recognition_checks"]))
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["recognition_recorded"])
        self.assertTrue(summary["reception_recognized"])
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        for key in (
            "selected_non_capture_result_preserved",
            "selected_non_capture_result_recorded",
            "selected_non_capture_result_failed_check_count_zero",
            "selected_eligibility_result_preserved",
            "selected_receiving_context_role_result_preserved",
            "selected_identity_preservation_result_preserved",
            "selected_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "selected_source_body_surface_remains_source",
            "selected_surface_is_not_whole_body_by_default",
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "eligibility_admissibility_review_readiness_only",
            "non_capture_passed_as_refusal_check_outcome_only",
            "non_adoption_passed_as_refusal_check_outcome_only",
            "non_currentness_passed_as_refusal_check_outcome_only",
            "bounded_recognition_for_accounting_only",
            "recognition_is_not_authorization",
            "recognition_is_not_source_receipt",
            "recognition_is_not_adoption",
            "recognition_is_not_currentness",
            "recognition_is_not_validation",
            "recognition_is_not_invalidation",
            "recognition_is_not_operation_permission",
            "recognition_is_not_publication_flow",
            "receipt_exhaustion_future",
            "conformance_future",
            "closure_future",
            "no_reception_authorization",
            "no_source_received",
            "no_source_receipt",
            "no_source_replacement",
            "no_adoption_authority_currentness_standing",
            "no_vessel_derivative_relation",
            "no_operation_permission_governance_publication_flow",
            "no_public_readiness_final_completion_follow_on_work",
        ):
            self.assertTrue(summary[key], key)

    def test_path_based_selected_non_capture_request_and_write_helpers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selected_path = root / "selected_non_capture.json"
            selected_payload = selected_non_capture_result()
            selected_path.write_text(json.dumps(selected_payload), encoding="utf-8")
            request = declared_recognition_request(
                selected_non_capture_result_path=str(selected_path)
            )
            request.pop("selected_non_capture_result")
            result = self.resolve(request)
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(
                result["selected_non_capture_result"]["selected_non_capture_result_path"],
                str(selected_path),
            )
            self.assertEqual(
                result["selected_non_capture_result"]["selected_non_capture_result_outcome"],
                NON_CAPTURE_PASSED,
            )

            request_path = root / "declared_recognition_request.json"
            request_path.write_text(json.dumps(declared_recognition_request()), encoding="utf-8")
            path_result = resolver.resolve_source_body_reception_recognition_boundary_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), TOP_LEVEL_SECTIONS)
            self.assertEqual(
                path_result["declared_recognition_question"][
                    "declared_recognition_request_path"
                ],
                str(request_path),
            )

            output = root / "nested" / "recognition_result.json"
            written = resolver.write_source_body_reception_recognition_result(
                path_result, output
            )
            self.assertEqual(written, output)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["outcome"], RECORDED)

    def test_default_write_uses_bounded_root_and_does_not_overwrite(self) -> None:
        result = self.resolve(declared_recognition_request())
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp) / "recognition-root"
            original_root = str(resolver.SOURCE_BODY_RECEPTION_RECOGNITION_BOUNDARY_ROOT)
            self.assertIn("source_body_reception_recognition_boundary", original_root)
            self.assertNotIn("non_capture_non_adoption_non_currentness", original_root)
            self.assertNotIn("receipt_exhaustion", original_root)
            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_RECOGNITION_BOUNDARY_ROOT",
                temp_root,
            ):
                first = resolver.write_source_body_reception_recognition_result(result)
                second = resolver.write_source_body_reception_recognition_result(result)
            self.assertEqual(first.parent, temp_root)
            self.assertEqual(second.parent, temp_root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = declared_recognition_request()
        original_request = copy.deepcopy(request)
        selected_original = copy.deepcopy(request["selected_non_capture_result"])
        surface_original = copy.deepcopy(
            request["selected_non_capture_result"]["non_capture_basis"][
                "selected_source_body_surface"
            ]
        )
        context_original = copy.deepcopy(
            request["selected_non_capture_result"]["non_capture_basis"][
                "receiving_context"
            ]
        )
        basis_original = copy.deepcopy(request["recognition_basis"])
        limits_original = copy.deepcopy(request["recognition_limits"])
        scope_original = copy.deepcopy(request["recognition_scope"])

        first = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_non_capture_result"], selected_original)
        self.assertEqual(
            request["selected_non_capture_result"]["non_capture_basis"][
                "selected_source_body_surface"
            ],
            surface_original,
        )
        self.assertEqual(
            request["selected_non_capture_result"]["non_capture_basis"][
                "receiving_context"
            ],
            context_original,
        )
        self.assertEqual(request["recognition_basis"], basis_original)
        self.assertEqual(request["recognition_limits"], limits_original)
        self.assertEqual(request["recognition_scope"], scope_original)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selected_path = root / "selected_non_capture.json"
            selected_path.write_text(json.dumps(selected_original, sort_keys=True), encoding="utf-8")
            before = selected_path.read_text(encoding="utf-8")
            path_request = declared_recognition_request(
                selected_non_capture_result_path=str(selected_path)
            )
            path_request.pop("selected_non_capture_result")
            result = self.resolve(path_request)
            resolver.write_source_body_reception_recognition_result(
                result, root / "additive" / "recognition.json"
            )
            self.assertEqual(selected_path.read_text(encoding="utf-8"), before)

    def test_blocking_request_shape_and_paths(self) -> None:
        self.assert_block(self.resolve(None), "RECOGNITION_QUESTION_UNDECLARED")
        malformed = resolver.resolve_source_body_reception_recognition_boundary(
            declared_recognition_request=["not", "a", "mapping"]
        )
        self.assert_block(malformed, "DECLARED_RECOGNITION_REQUEST_MALFORMED")
        block_request = declared_recognition_request(
            recognition_intent="BLOCK_SOURCE_BODY_RECEPTION_RECOGNITION_REVIEW"
        )
        self.assert_block(
            self.resolve(block_request),
            "RECOGNITION_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            missing = resolver.resolve_source_body_reception_recognition_boundary_from_path(
                root / "missing.json"
            )
            self.assert_block(missing, "DECLARED_RECOGNITION_REQUEST_UNREADABLE")
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self.assert_block(
                resolver.resolve_source_body_reception_recognition_boundary_from_path(
                    malformed_path
                ),
                "DECLARED_RECOGNITION_REQUEST_MALFORMED",
            )
            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_block(
                resolver.resolve_source_body_reception_recognition_boundary_from_path(
                    array_path
                ),
                "DECLARED_RECOGNITION_REQUEST_MALFORMED",
            )

    def test_blocking_selected_non_capture_paths_and_result_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request = declared_recognition_request(
                selected_non_capture_result_path=str(root / "missing.json")
            )
            request.pop("selected_non_capture_result")
            self.assert_block(self.resolve(request), "NON_CAPTURE_RESULT_UNREADABLE")

            malformed_path = root / "selected-malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            request = declared_recognition_request(
                selected_non_capture_result_path=str(malformed_path)
            )
            request.pop("selected_non_capture_result")
            self.assert_block(self.resolve(request), "NON_CAPTURE_RESULT_MALFORMED")

            array_path = root / "selected-array.json"
            array_path.write_text("[]", encoding="utf-8")
            request = declared_recognition_request(
                selected_non_capture_result_path=str(array_path)
            )
            request.pop("selected_non_capture_result")
            self.assert_block(self.resolve(request), "NON_CAPTURE_RESULT_MALFORMED")

        missing_outcome = declared_recognition_request()
        missing_outcome.pop("selected_non_capture_result_outcome")
        missing_outcome["selected_non_capture_result"].pop("outcome")
        missing_outcome["selected_non_capture_result"][
            "source_body_reception_non_capture_summary"
        ].pop("outcome")
        self.assert_block(
            self.resolve(missing_outcome),
            "NON_CAPTURE_RESULT_OUTCOME_MISSING",
        )

        wrong_outcome = declared_recognition_request(
            selected_non_capture_result_outcome="SOURCE_BODY_RECEPTION_NON_CAPTURE_NOT_PASSED"
        )
        wrong_outcome["selected_non_capture_result"]["outcome"] = (
            "SOURCE_BODY_RECEPTION_NON_CAPTURE_NOT_PASSED"
        )
        self.assert_block(self.resolve(wrong_outcome), "NON_CAPTURE_RESULT_NOT_PASSED")

        failed_checks = declared_recognition_request()
        failed_checks["selected_non_capture_result"][
            "source_body_reception_non_capture_summary"
        ]["failed_check_count"] = 1
        self.assert_block(self.resolve(failed_checks), "NON_CAPTURE_RESULT_HAS_FAILED_CHECKS")

    def test_blocking_missing_required_basis(self) -> None:
        cases = (
            ("selected_eligibility_result", "ELIGIBILITY_RESULT_MISSING"),
            ("selected_receiving_context_role_result", "RECEIVING_CONTEXT_ROLE_RESULT_MISSING"),
            ("selected_identity_preservation_result", "IDENTITY_PRESERVATION_RESULT_MISSING"),
            (
                "selected_reception_request_declaration_result",
                "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
            ),
            ("selected_source_body_surface", "SELECTED_SOURCE_BODY_SURFACE_MISSING"),
            ("receiving_context", "RECEIVING_CONTEXT_MISSING"),
            ("receiving_context_type", "RECEIVING_CONTEXT_TYPE_MISSING"),
            ("reception_class", "RECEPTION_CLASS_MISSING"),
            ("reception_purpose", "RECEPTION_PURPOSE_MISSING"),
            ("reception_limits", "RECEPTION_LIMITS_MISSING"),
        )
        for key, code in cases:
            with self.subTest(key=key):
                request = declared_recognition_request()
                remove_key_recursive(request["selected_non_capture_result"], key)
                self.assert_block(self.resolve(request), code)

        request = declared_recognition_request()
        request.pop("recognition_basis")
        self.assert_block(self.resolve(request), "RECOGNITION_BASIS_MISSING")

        request = declared_recognition_request()
        request.pop("recognition_limits")
        self.assert_block(self.resolve(request), "RECOGNITION_LIMITS_MISSING")

    def test_blocking_malformed_surface_and_context(self) -> None:
        request = declared_recognition_request(
            selected_source_body_surface="not-a-mapping"
        )
        self.assert_block(self.resolve(request), "SELECTED_SOURCE_BODY_SURFACE_MALFORMED")

        request = declared_recognition_request(
            receiving_context="not-a-mapping",
            receiving_context_type="PRESENT_EXECUTION_CONTEXT",
        )
        self.assert_block(self.resolve(request), "RECEIVING_CONTEXT_MALFORMED")

    def test_blocking_recognition_overreach_flags(self) -> None:
        cases = (
            ("reception_authorized", "RECOGNITION_AUTHORIZES_RECEPTION"),
            ("source_received", "RECOGNITION_RECEIVES_SOURCE"),
            ("source_receipt_recorded", "RECOGNITION_CREATES_SOURCE_RECEIPT"),
            ("receiving_context_governance_created", "RECOGNITION_CREATES_GOVERNANCE"),
            ("receiving_context_became_source", "RECOGNITION_TREATS_CONTEXT_AS_SOURCE"),
            (
                "receiving_context_became_authority",
                "RECOGNITION_TREATS_CONTEXT_AS_AUTHORITY",
            ),
            ("receiving_context_became_current", "RECOGNITION_TREATS_CONTEXT_AS_CURRENT"),
            ("receiving_context_became_receiver", "RECOGNITION_TREATS_CONTEXT_AS_RECEIVER"),
            ("receiving_context_became_adopter", "RECOGNITION_TREATS_CONTEXT_AS_ADOPTER"),
            ("receiving_context_became_validator", "RECOGNITION_TREATS_CONTEXT_AS_VALIDATOR"),
            (
                "receiving_context_became_invalidator",
                "RECOGNITION_TREATS_CONTEXT_AS_INVALIDATOR",
            ),
            ("receiving_context_became_operator", "RECOGNITION_TREATS_CONTEXT_AS_OPERATOR"),
            ("source_validated_by_receiving_context", "RECOGNITION_VALIDATES_SOURCE"),
            ("source_invalidated_by_receiving_context", "RECOGNITION_INVALIDATES_SOURCE"),
            ("source_replaced", "RECOGNITION_REPLACES_SOURCE"),
            ("adoption_created", "RECOGNITION_CREATES_ADOPTION"),
            ("authority_created", "RECOGNITION_CREATES_AUTHORITY"),
            ("currentness_created", "RECOGNITION_CREATES_CURRENTNESS"),
            ("standing_created", "RECOGNITION_CREATES_STANDING"),
            ("standing_propagated", "RECOGNITION_CREATES_STANDING_PROPAGATION"),
            ("vessel_relation_created", "RECOGNITION_CREATES_VESSEL_RELATION"),
            ("derivative_relation_created", "RECOGNITION_CREATES_DERIVATIVE_RELATION"),
            ("operation_permission_created", "RECOGNITION_CREATES_OPERATION_PERMISSION"),
            ("public_launch_readiness_created", "RECOGNITION_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "RECOGNITION_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "RECOGNITION_AUTHORIZES_FOLLOW_ON_WORK"),
            ("continuation_authorized", "RECOGNITION_AUTHORIZES_CONTINUATION"),
            ("publication_flow_opened", "RECOGNITION_OPENS_PUBLICATION_FLOW"),
            (
                "receipt_exhaustion_passed",
                "RECOGNITION_CLAIMS_RECEIPT_EXHAUSTION_PASSED",
            ),
            ("reception_conformance_passed", "RECOGNITION_CLAIMS_CONFORMANCE_PASSED"),
            ("reception_closure_passed", "RECOGNITION_CLAIMS_CLOSURE_PASSED"),
        )
        for key, code in cases:
            with self.subTest(key=key):
                request = declared_recognition_request()
                request[key] = True
                self.assert_block(self.resolve(request), code)

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        for key in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(key=key):
                request = declared_recognition_request()
                request[key] = True
                self.assert_block(self.resolve(request), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing = declared_recognition_request()
        missing["declared_non_claims"].pop("source_received")
        self.assert_block(self.resolve(missing), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = declared_recognition_request()
        flipped["declared_non_claims"]["source_received"] = True
        self.assert_block(self.resolve(flipped), "RECOGNITION_RECEIVES_SOURCE")


if __name__ == "__main__":
    unittest.main()
