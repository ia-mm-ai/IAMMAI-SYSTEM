"""Executable boundary tests for source-body reception receiving-context role only.

These tests prove that the resolver records one bounded receiving-context role
for one declared source-body reception request after identity preservation. The
role is not reception, authorization, source receipt, source authority,
currentness, adoption, validation, invalidation, operation permission,
receiving-context governance, vessel relation, derivative relation, publication
flow, final completion, continuation, or follow-on work.
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

import resolve_source_body_reception_receiving_context_role_boundary as resolver  # noqa: E402


RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
NOT_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_NOT_RECORDED"
REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_REVIEW_BLOCKED"
IDENTITY_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {
    RECORDED,
    NOT_RECORDED,
    REQUIRES_ADDITIONAL_BASIS,
    BLOCKED,
}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_receiving_context_role_metadata",
    "declared_receiving_context_role_question",
    "selected_identity_preservation_result",
    "selected_source_body_surface",
    "receiving_context",
    "receiving_context_role",
    "receiving_context_role_basis",
    "receiving_context_role_scope",
    "receiving_context_role_checks",
    "receiving_context_role_statement",
    "receiving_context_role_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_receiving_context_role_summary",
}

SUPPORTED_ROLE_CLASSES = tuple(resolver.SUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES)
SUPPORTED_ROLE_SCOPE = tuple(resolver.SUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)


def false_role_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def false_identity_non_claims() -> dict[str, bool]:
    return {
        "reception_recognized": False,
        "reception_authorized": False,
        "source_received": False,
        "final_source_body_identity_defined": False,
        "selected_surface_inflated_to_whole_body": False,
        "source_replaced": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "receiving_context_became_source": False,
        "receiving_context_became_authority": False,
        "receiving_context_became_current": False,
        "closure_artifact_became_source": False,
        "terminal_summary_became_source": False,
        "latest_artifact_became_source": False,
        "carrier_possession_became_source": False,
        "registry_reference_replaced_source": False,
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
        "receiving_context_became_vessel": False,
        "receiving_context_became_derivative": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "receiving_context_governance_created": False,
        "operation_permission_created": False,
        "publication_flow_opened": False,
    }


def reception_purpose() -> dict[str, object]:
    return {
        "purpose_id": "receiving-context-role-before-reception-eligibility",
        "purpose_statement": "Record bounded receiving-context role for later review.",
        "purpose_is_permission": False,
    }


def reception_limits() -> dict[str, object]:
    return {
        "limits_id": "source-body-reception-receiving-context-role-limits-001",
        "role_boundary_only": True,
        "no_reception_recognition": True,
        "no_reception_authorization": True,
        "no_source_receipt": True,
        "no_receiving_context_governance": True,
        "no_source_authority": True,
        "no_currentness": True,
        "no_validation": True,
        "no_invalidation": True,
        "no_operation_permission": True,
        "no_publication_flow": True,
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


def identity_preservation_basis() -> dict[str, object]:
    return {
        "basis_id": "source-body-reception-identity-preservation-basis-001",
        "selected_reception_request_declaration_result": (
            selected_reception_request_declaration_result()
        ),
        "selected_source_body_surface": selected_source_body_surface(),
        "source_body_identity_basis": selected_source_body_surface()["source_body_identity_basis"],
        "source_body_lineage_basis": selected_source_body_surface()["source_body_lineage_basis"],
        "receiving_context": receiving_context(),
        "reception_class": "REFERENCE_RECEPTION",
        "reception_purpose": reception_purpose(),
        "reception_limits": reception_limits(),
        "source_body_surface_remains_source": True,
        "receiving_context_remains_context_only": True,
        "identity_preservation_is_not_reception": True,
        "identity_preservation_is_not_authorization": True,
    }


def selected_identity_preservation_result(**overrides: object) -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    purpose = reception_purpose()
    limits = reception_limits()
    statement = {
        "source_body_reception_identity_preserved": True,
        "selected_reception_request_declaration_preserved": True,
        "selected_reception_request_declaration_recorded": True,
        "selected_reception_request_declaration_failed_check_count_zero": True,
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
    }
    statement.update(false_identity_non_claims())
    result: dict[str, object] = {
        "source_body_reception_identity_metadata": {
            "source_body_reception_identity_result_id": (
                "source_body_reception_identity_preservation__identity-001"
            ),
            "source_body_reception_identity_result_type": (
                "source_body_reception_identity_preservation_result"
            ),
            "source_body_reception_identity_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_identity_preservation_boundary",
        },
        "declared_identity_preservation_question": {
            "identity_preservation_request_id": (
                "source-body-reception-identity-preservation-001"
            ),
            "identity_preservation_question": (
                "How is the selected source-body surface identity preserved?"
            ),
        },
        "selected_reception_request_declaration": (
            selected_reception_request_declaration_result()
        ),
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "identity_preservation_basis": {
            "selected_reception_request_declaration": (
                selected_reception_request_declaration_result()
            ),
            "selected_source_body_surface": surface,
            "source_body_identity_basis": surface["source_body_identity_basis"],
            "source_body_lineage_basis": surface["source_body_lineage_basis"],
            "receiving_context": context,
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": purpose,
            "reception_limits": limits,
        },
        "identity_preservation_checks": [
            {
                "check_name": "selected source-body surface remains source",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
                "failure_code": None,
            }
        ],
        "identity_preservation_statement": statement,
        "non_claims": false_identity_non_claims(),
        "outcome": IDENTITY_PRESERVED,
        "source_body_reception_identity_summary": {
            "outcome": IDENTITY_PRESERVED,
            "source_body_reception_identity_result_id": (
                "source_body_reception_identity_preservation__identity-001"
            ),
            "failed_check_count": 0,
            "passed_check_count": 44,
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "selected_surface_is_not_whole_body_by_default": True,
            "receiving_context_preserved": True,
            "receiving_context_remains_context_only": True,
            "receiving_context_is_not_source": True,
            "receiving_context_is_not_authority": True,
            "receiving_context_is_not_current": True,
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": purpose,
            "reception_class_preserved": True,
            "reception_purpose_preserved": True,
            "reception_limits_preserved": True,
        },
    }
    result.update(overrides)
    return result


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


def declared_receiving_context_role() -> dict[str, object]:
    return {
        "declared_receiving_context_role_id": "reference-review-context-role-001",
        "declared_receiving_context_role_statement": (
            "Receiving context is bounded reference review context only."
        ),
        "role_is_bounded_review_posture_only": True,
    }


def receiving_context_role_basis(role_class: str = "REFERENCE_REVIEW_CONTEXT") -> dict[str, object]:
    return {
        "basis_id": "source-body-reception-receiving-context-role-basis-001",
        "selected_identity_preservation_result_preserved": True,
        "declared_receiving_context_role": declared_receiving_context_role(),
        "receiving_context_role_class": role_class,
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


def declared_role_request(
    selected_identity: dict[str, object] | None = None,
    *,
    role_class: str = "REFERENCE_REVIEW_CONTEXT",
    role_scope: object | None = None,
    **overrides: object,
) -> dict[str, object]:
    identity = selected_identity or selected_identity_preservation_result()
    metadata = identity.get("source_body_reception_identity_metadata", {})
    identity_id = None
    if isinstance(metadata, dict):
        identity_id = metadata.get("source_body_reception_identity_result_id")
    basis = receiving_context_role_basis(role_class)
    request: dict[str, object] = {
        "receiving_context_role_request_id": (
            "source-body-reception-receiving-context-role-001"
        ),
        "receiving_context_role_question": (
            "What bounded receiving-context role may be recorded for this declared source-body reception request?"
        ),
        "receiving_context_role_intent": (
            "RECORD_SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE"
        ),
        "selected_identity_preservation_result": identity,
        "selected_identity_preservation_result_id": identity_id,
        "selected_identity_preservation_result_outcome": identity.get("outcome"),
        "receiving_context_role_basis": basis,
        "declared_receiving_context_role": basis["declared_receiving_context_role"],
        "receiving_context_role_class": role_class,
        "receiving_context_role_limits": basis["receiving_context_role_limits"],
        "receiving_context_role_scope": (
            list(SUPPORTED_ROLE_SCOPE) if role_scope is None else role_scope
        ),
        "requested_receiving_context_role_outcome": RECORDED,
        "additional_basis_context": {},
        "not_recorded_basis": None,
        "declared_non_claims": false_role_non_claims(),
    }
    request.update(overrides)
    return request


def resolve(request: object | None) -> dict[str, object]:
    return resolver.resolve_source_body_reception_receiving_context_role_boundary(
        declared_receiving_context_role_request=request
    )


class ReceivingContextRoleAssertions:
    def assert_outcome_family(self, result: dict[str, object]) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_block(self, request: object, code: str) -> dict[str, object]:
        result = resolve(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        self.assertFalse(
            result["non_claims"]["source_body_reception_receiving_context_role_recorded"]
        )
        self.assert_outcome_family(result)
        return result

    def assert_required_non_claims_false(self, result: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
            self.assertIs(result["non_claims"][key], False, key)

    def assert_no_role_collapse(self, section: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, section, key)
            self.assertIs(section[key], False, key)


class TestSourceBodyReceptionReceivingContextRoleRecorded(
    ReceivingContextRoleAssertions, unittest.TestCase
):
    def setUp(self) -> None:
        self.request = declared_role_request()
        self.request_before = copy.deepcopy(self.request)
        self.result = resolve(self.request)

    def test_successful_role_recorded_result_shape_and_statement(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(self.result))
        self.assertEqual(RECORDED, self.result["outcome"])
        self.assertIsNone(self.result["block"]["block_code"])
        self.assertIsNone(self.result["block"]["block_reason"])
        self.assertEqual(
            0,
            self.result["source_body_reception_receiving_context_role_summary"][
                "failed_check_count"
            ],
        )

        statement = self.result["receiving_context_role_statement"]
        for key in (
            "source_body_reception_receiving_context_role_recorded",
            "selected_identity_preservation_result_preserved",
            "selected_identity_preservation_result_recorded",
            "selected_identity_preservation_result_failed_check_count_zero",
            "selected_reception_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "selected_source_body_surface_remains_source",
            "selected_surface_is_not_whole_body_by_default",
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "reception_class_preserved",
            "reception_purpose_preserved",
            "reception_limits_preserved",
            "identity_preservation_basis_preserved",
            "receiving_context_role_declared",
            "receiving_context_role_class_supported",
            "receiving_context_role_limits_present",
            "role_is_not_reception",
            "role_is_not_authorization",
            "role_is_not_source_receipt",
            "role_is_not_source_authority",
            "role_is_not_currentness",
            "role_is_not_adoption",
            "role_is_not_validation",
            "role_is_not_invalidation",
            "role_is_not_operation_permission",
            "role_is_not_vessel_relation",
            "role_is_not_derivative_relation",
            "role_is_not_publication_flow",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_no_role_collapse(statement)
        self.assert_required_non_claims_false(self.result)
        self.assertIs(
            self.result["non_claims"]["source_body_reception_receiving_context_role_recorded"],
            True,
        )
        self.assertEqual(self.request_before, self.request)

    def test_metadata_and_declared_question_are_bounded(self) -> None:
        metadata = self.result["source_body_reception_receiving_context_role_metadata"]
        for key in (
            "source_body_reception_receiving_context_role_result_id",
            "source_body_reception_receiving_context_role_result_type",
            "source_body_reception_receiving_context_role_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(
            "0.1.0",
            metadata["source_body_reception_receiving_context_role_result_version"],
        )
        self.assertEqual(
            "resolve_source_body_reception_receiving_context_role_boundary",
            metadata["resolver_module"],
        )

        question = self.result["declared_receiving_context_role_question"]
        self.assertEqual(
            self.request["receiving_context_role_request_id"],
            question["receiving_context_role_request_id"],
        )
        self.assertEqual(
            self.request["receiving_context_role_question"],
            question["receiving_context_role_question"],
        )
        self.assertEqual(
            "RECORD_SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE",
            question["receiving_context_role_intent"],
        )
        self.assertEqual(
            IDENTITY_PRESERVED,
            question["selected_identity_preservation_result_outcome"],
        )
        self.assertEqual("source-body-surface-001", question["selected_source_body_surface_identifier"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", question["receiving_context_type"])
        self.assertEqual("REFERENCE_RECEPTION", question["reception_class"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", question["receiving_context_role_class"])
        self.assertIs(question["role_is_not_reception"], True)
        self.assertIs(question["role_is_not_authorization"], True)
        self.assertIs(question["role_does_not_create_source_authority"], True)
        self.assertIs(question["role_does_not_create_governance"], True)

    def test_selected_identity_preservation_result_is_preserved_not_upgraded(self) -> None:
        identity = self.result["selected_identity_preservation_result"]
        self.assertEqual(
            "source_body_reception_identity_preservation__identity-001",
            identity["selected_identity_preservation_result_id"],
        )
        self.assertEqual(
            IDENTITY_PRESERVED,
            identity["selected_identity_preservation_result_outcome"],
        )
        self.assertIs(identity["selected_identity_preservation_result_recorded"], True)
        self.assertIs(
            identity["selected_identity_preservation_result_failed_check_count_zero"],
            True,
        )
        self.assertIs(
            identity["selected_reception_request_declaration_result_preserved"], True
        )
        self.assertIs(identity["selected_source_body_surface_preserved_by_identity"], True)
        self.assertIs(
            identity["selected_source_body_surface_remains_source_by_identity"], True
        )
        self.assertIs(
            identity["selected_surface_is_not_whole_body_by_default_by_identity"], True
        )
        self.assertIs(identity["receiving_context_preserved_by_identity"], True)
        self.assertIs(identity["receiving_context_remains_context_only_by_identity"], True)
        self.assertIs(identity["receiving_context_is_not_source_by_identity"], True)
        self.assertIs(identity["receiving_context_is_not_authority_by_identity"], True)
        self.assertIs(identity["receiving_context_is_not_current_by_identity"], True)
        self.assertIs(identity["reception_class_preserved_by_identity"], True)
        self.assertIs(identity["reception_purpose_preserved_by_identity"], True)
        self.assertIs(identity["reception_limits_preserved_by_identity"], True)
        self.assertIs(identity["identity_preservation_did_not_recognize_reception"], True)
        self.assertIs(identity["identity_preservation_did_not_authorize_reception"], True)
        self.assertIs(identity["identity_preservation_did_not_receive_source"], True)
        self.assertIs(identity["identity_preservation_did_not_define_final_identity"], True)
        self.assertIs(identity["identity_preservation_did_not_mutate_replay_or_merge"], True)

    def test_selected_surface_receiving_context_role_and_basis_are_preserved(self) -> None:
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
            "receiving_context_is_not_vessel",
            "receiving_context_is_not_derivative",
            "receiving_context_did_not_validate_source",
            "receiving_context_did_not_invalidate_source",
            "receiving_context_did_not_create_governance",
            "receiving_context_did_not_create_operation_permission",
            "receiving_context_did_not_open_publication_flow",
        ):
            self.assertIs(context[key], True, key)

        role = self.result["receiving_context_role"]
        self.assertTrue(role["declared_receiving_context_role"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", role["receiving_context_role_class"])
        self.assertTrue(role["receiving_context_role_limits"])
        self.assertIs(role["receiving_context_role_class_supported"], True)
        self.assertIs(role["receiving_context_role_limits_present"], True)
        for key in (
            "role_is_bounded_review_posture_only",
            "role_is_not_permission",
            "role_is_not_reception",
            "role_is_not_authorization",
            "role_is_not_source_receipt",
            "role_is_not_source_authority",
            "role_is_not_currentness",
            "role_is_not_adoption",
            "role_is_not_validation",
            "role_is_not_invalidation",
            "role_is_not_operation_permission",
            "role_is_not_vessel_relation",
            "role_is_not_derivative_relation",
            "role_is_not_publication_flow",
        ):
            self.assertIs(role[key], True, key)

        basis = self.result["receiving_context_role_basis"]
        self.assertTrue(basis["selected_identity_preservation_result"])
        self.assertTrue(basis["selected_reception_request_declaration_result"])
        self.assertTrue(basis["selected_source_body_surface"])
        self.assertTrue(basis["source_body_identity_basis"])
        self.assertTrue(basis["source_body_lineage_basis"])
        self.assertTrue(basis["receiving_context"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", basis["receiving_context_type"])
        self.assertEqual("REFERENCE_RECEPTION", basis["reception_class"])
        self.assertTrue(basis["reception_purpose"])
        self.assertTrue(basis["reception_limits"])
        self.assertTrue(basis["identity_preservation_basis"])
        self.assertTrue(basis["declared_receiving_context_role"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", basis["receiving_context_role_class"])
        self.assertTrue(basis["receiving_context_role_limits"])
        for key in (
            "role_non_reception_distinction",
            "role_non_authorization_distinction",
            "role_non_authority_distinction",
            "role_non_currentness_distinction",
            "role_non_adoption_distinction",
            "role_non_validation_distinction",
            "role_non_operation_permission_distinction",
            "role_non_publication_flow_distinction",
            "source_body_surface_remains_source",
            "receiving_context_remains_context_only",
        ):
            self.assertIs(basis[key], True, key)

    def test_supported_role_classes_scope_values_and_checks_are_recorded(self) -> None:
        for role_class in SUPPORTED_ROLE_CLASSES:
            with self.subTest(role_class=role_class):
                result = resolve(declared_role_request(role_class=role_class))
                self.assertEqual(RECORDED, result["outcome"])
                self.assertEqual(
                    role_class,
                    result["receiving_context_role"]["receiving_context_role_class"],
                )

        for value in SUPPORTED_ROLE_SCOPE:
            with self.subTest(scope=value):
                result = resolve(declared_role_request(role_scope=[value]))
                self.assertEqual(RECORDED, result["outcome"])
                scope = result["receiving_context_role_scope"]
                self.assertEqual([value], scope["selected_receiving_context_role_scope_values"])
                self.assertIs(scope["all_selected_scope_values_supported"], True)

        checks = self.result["receiving_context_role_checks"]
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
            "receiving-context role question declared",
            "receiving-context role intent supported",
            "selected identity preservation result present",
            "selected identity preservation outcome declared",
            "selected identity preservation outcome preserved",
            "selected identity preservation failed check count zero",
            "selected reception request declaration result preserved",
            "selected source-body surface preserved",
            "selected source-body surface remains source",
            "selected surface is not whole body by default",
            "receiving context preserved",
            "receiving context remains context only",
            "receiving context is not source",
            "receiving context is not authority",
            "receiving context is not current",
            "reception class preserved",
            "reception purpose preserved",
            "reception limits preserved",
            "identity preservation basis preserved",
            "declared receiving-context role present",
            "receiving-context role class supported",
            "receiving-context role limits present",
            "role is not reception",
            "role is not authorization",
            "role is not source receipt",
            "role is not source authority",
            "role is not currentness",
            "role is not adoption",
            "role is not validation",
            "role is not invalidation",
            "role is not operation permission",
            "role is not vessel relation",
            "role is not derivative relation",
            "role is not publication flow",
            "source-body surface remains source",
            "no mutation/replay/merge",
            "non-claims remain false",
        ):
            self.assertIn(expected, names)

    def test_non_meaning_remaining_open_non_claims_and_summary(self) -> None:
        non_meaning = self.result["receiving_context_role_non_meaning"]
        for key in (
            "reception_recognized",
            "reception_authorized",
            "source_received",
            "receiving_context_governance_created",
            "receiving_context_became_source",
            "receiving_context_became_authority",
            "receiving_context_became_current",
            "receiving_context_became_receiver",
            "receiving_context_became_adopter",
            "receiving_context_became_validator",
            "receiving_context_became_invalidator",
            "receiving_context_became_operator",
            "receiving_context_became_vessel",
            "receiving_context_became_derivative",
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
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
        ):
            self.assertIs(non_meaning[key], True, key)

        remains_open = self.result["what_remains_open"]
        for key in (
            "source_body_reception_receiving_context_role_test",
            "source_body_reception_receiving_context_role_live_artifact",
            "reception_eligibility_admissibility_boundary",
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

        summary = self.result["source_body_reception_receiving_context_role_summary"]
        self.assertEqual(RECORDED, summary["outcome"])
        self.assertIs(summary["role_recorded"], True)
        self.assertIs(summary["not_recorded"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertEqual("source-body-surface-001", summary["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", summary["selected_source_body_surface_type"])
        self.assertEqual("receiving-context-001", summary["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", summary["receiving_context_type"])
        self.assertEqual("REFERENCE_REVIEW_CONTEXT", summary["receiving_context_role_class"])
        for key in (
            "selected_identity_preservation_result_preserved",
            "selected_identity_preservation_result_recorded",
            "selected_identity_preservation_result_failed_check_count_zero",
            "selected_reception_request_declaration_result_preserved",
            "selected_source_body_surface_preserved",
            "selected_source_body_surface_remains_source",
            "selected_surface_is_not_whole_body_by_default",
            "receiving_context_preserved",
            "receiving_context_remains_context_only",
            "receiving_context_is_not_source",
            "receiving_context_is_not_authority",
            "receiving_context_is_not_current",
            "reception_class_preserved",
            "reception_purpose_preserved",
            "reception_limits_preserved",
            "identity_preservation_basis_preserved",
            "receiving_context_role_declared",
            "receiving_context_role_class_supported",
            "receiving_context_role_limits_present",
            "role_is_not_reception",
            "role_is_not_authorization",
            "role_is_not_source_receipt",
            "role_is_not_source_authority",
            "role_is_not_currentness",
            "role_is_not_adoption",
            "role_is_not_validation",
            "role_is_not_invalidation",
            "role_is_not_operation_permission",
            "role_is_not_vessel_relation",
            "role_is_not_derivative_relation",
            "role_is_not_publication_flow",
            "no_reception_recognized",
            "no_reception_authorized",
            "no_source_received",
            "no_receiving_context_governance",
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
            "no_public_readiness",
            "no_final_completion",
            "no_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        self.assertEqual(
            {key: False for key in REQUIRED_NON_CLAIMS},
            summary["key_non_claims"],
        )


class TestReceivingContextRoleAlternateOutcomes(
    ReceivingContextRoleAssertions, unittest.TestCase
):
    def test_requires_additional_basis_preserves_missing_basis_as_unexecuted(self) -> None:
        context = {
            "reason": "receiving-context role class unclear",
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
        request = declared_role_request(
            requested_receiving_context_role_outcome=REQUIRES_ADDITIONAL_BASIS,
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
        self.assert_required_non_claims_false(result)
        self.assertFalse(
            result["non_claims"]["source_body_reception_receiving_context_role_recorded"]
        )
        self.assertEqual(before, request)

    def test_not_recorded_preserves_readable_basis_without_repair(self) -> None:
        not_recorded = {
            "reason": "role capture risk remains unresolved",
            "repair_authorized": False,
        }
        request = declared_role_request(
            requested_receiving_context_role_outcome=NOT_RECORDED,
            not_recorded_basis=not_recorded,
        )
        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(NOT_RECORDED, result["outcome"])
        self.assertEqual(not_recorded, result["not_recorded_basis"]["not_recorded_basis"])
        self.assertIs(result["not_recorded_basis"]["receiving_context_role_not_recorded"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_mutate"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_repair"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_authorize"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_receive_source"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_replace_source"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_validate_source"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_invalidate_source"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_create_currentness"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_recognize_reception"], True)
        self.assert_required_non_claims_false(result)
        self.assertFalse(
            result["non_claims"]["source_body_reception_receiving_context_role_recorded"]
        )
        self.assertEqual(before, request)


class TestReceivingContextRoleHelpersAndPaths(
    ReceivingContextRoleAssertions, unittest.TestCase
):
    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        identity = selected_identity_preservation_result()
        basis = receiving_context_role_basis("REQUEST_DECLARATION_CONTEXT")
        request = resolver.build_declared_source_body_reception_receiving_context_role_request(
            "receiving-context-role-builder-001",
            "What bounded receiving-context role may be recorded for this declared source-body reception request?",
            identity,
            basis,
            list(SUPPORTED_ROLE_SCOPE),
            selected_identity_preservation_result_id=(
                "source_body_reception_identity_preservation__identity-001"
            ),
            selected_identity_preservation_result_outcome=IDENTITY_PRESERVED,
            additional_basis_context={"reason": "none"},
            not_recorded_basis={"reason": "none"},
        )
        self.assertEqual(
            "receiving-context-role-builder-001",
            request["receiving_context_role_request_id"],
        )
        self.assertEqual(identity, request["selected_identity_preservation_result"])
        self.assertEqual(basis, request["receiving_context_role_basis"])
        self.assertEqual(list(SUPPORTED_ROLE_SCOPE), request["receiving_context_role_scope"])
        self.assertEqual({"reason": "none"}, request["additional_basis_context"])
        self.assertEqual({"reason": "none"}, request["not_recorded_basis"])
        self.assertEqual(false_role_non_claims(), request["declared_non_claims"])
        result = resolve(request)
        self.assertEqual(RECORDED, result["outcome"])

    def test_path_based_selected_identity_preservation_result_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            identity_path = Path(temp_dir) / "selected_identity.json"
            identity_path.write_text(
                json.dumps(selected_identity_preservation_result(), indent=2),
                encoding="utf-8",
            )
            request = declared_role_request(selected_identity={})
            request.pop("selected_identity_preservation_result")
            request["selected_identity_preservation_result_path"] = str(identity_path)
            result = resolve(request)
            self.assertEqual(RECORDED, result["outcome"])
            selected = result["selected_identity_preservation_result"]
            self.assertEqual(str(identity_path), selected["selected_identity_preservation_result_path"])
            self.assertEqual(
                "source_body_reception_identity_preservation__identity-001",
                selected["selected_identity_preservation_result_id"],
            )
            self.assertEqual(IDENTITY_PRESERVED, selected["selected_identity_preservation_result_outcome"])
            self.assertEqual(
                identity_path.read_text(encoding="utf-8"),
                json.dumps(selected_identity_preservation_result(), indent=2),
            )

    def test_path_based_receiving_context_role_request_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request_path = Path(temp_dir) / "role_request.json"
            request_path.write_text(
                json.dumps(declared_role_request(), indent=2),
                encoding="utf-8",
            )
            path_result = resolver.resolve_source_body_reception_receiving_context_role_boundary_from_path(
                request_path
            )
            mapping_result = resolve(declared_role_request())
            self.assertEqual(RECORDED, path_result["outcome"])
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                str(request_path),
                path_result["declared_receiving_context_role_question"][
                    "declared_receiving_context_role_request_path"
                ],
            )

    def test_write_behavior_uses_additive_temp_paths_and_suffixes(self) -> None:
        result = resolve(declared_role_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "role_result.json"
            written = resolver.write_source_body_reception_receiving_context_role_result(
                result, explicit_path
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))

            default_root = Path(temp_dir) / "receiving-context-role-root"
            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_BOUNDARY_ROOT",
                default_root,
            ):
                first = resolver.write_source_body_reception_receiving_context_role_result(result)
                second = resolver.write_source_body_reception_receiving_context_role_result(result)
            self.assertEqual(default_root, first.parent)
            self.assertEqual(default_root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertIn("__source_body_reception_receiving_context_role_result", first.name)
            self.assertNotIn("source_body_reception_identity_preservation", str(first))
            self.assertNotIn("source_body_reception_boundary", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_role_request()
        request_before = copy.deepcopy(request)
        identity_before = copy.deepcopy(request["selected_identity_preservation_result"])
        surface_before = copy.deepcopy(
            request["selected_identity_preservation_result"]["selected_source_body_surface"]
        )
        context_before = copy.deepcopy(
            request["selected_identity_preservation_result"]["receiving_context"]
        )
        basis_before = copy.deepcopy(request["receiving_context_role_basis"])
        scope_before = copy.deepcopy(request["receiving_context_role_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(RECORDED, first["outcome"])
        self.assertEqual(RECORDED, second["outcome"])
        self.assertEqual(request_before, request)
        self.assertEqual(identity_before, request["selected_identity_preservation_result"])
        self.assertEqual(
            surface_before,
            request["selected_identity_preservation_result"]["selected_source_body_surface"],
        )
        self.assertEqual(
            context_before,
            request["selected_identity_preservation_result"]["receiving_context"],
        )
        self.assertEqual(basis_before, request["receiving_context_role_basis"])
        self.assertEqual(scope_before, request["receiving_context_role_scope"])

        with tempfile.TemporaryDirectory() as temp_dir:
            identity_path = Path(temp_dir) / "selected_identity.json"
            identity_payload = json.dumps(selected_identity_preservation_result(), indent=2)
            identity_path.write_text(identity_payload, encoding="utf-8")
            path_request = declared_role_request(selected_identity={})
            path_request.pop("selected_identity_preservation_result")
            path_request["selected_identity_preservation_result_path"] = str(identity_path)
            path_result = resolve(path_request)
            self.assertEqual(RECORDED, path_result["outcome"])
            self.assertEqual(identity_payload, identity_path.read_text(encoding="utf-8"))


class TestReceivingContextRoleBlocking(
    ReceivingContextRoleAssertions, unittest.TestCase
):
    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        self.assert_block(
            declared_role_request(
                receiving_context_role_intent=(
                    "BLOCK_SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_REVIEW"
                )
            ),
            "RECEIVING_CONTEXT_ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assert_block(None, "RECEIVING_CONTEXT_ROLE_QUESTION_UNDECLARED")
        self.assert_block("not a mapping", "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED")

    def test_request_path_unreadable_and_malformed_cases_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing.json"
            result = resolver.resolve_source_body_reception_receiving_context_role_boundary_from_path(
                missing
            )
            self.assertEqual(BLOCKED, result["outcome"])
            self.assertEqual(
                "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_UNREADABLE",
                result["block"]["block_code"],
            )

            malformed = Path(temp_dir) / "malformed.json"
            malformed.write_text("{not-json", encoding="utf-8")
            result = resolver.resolve_source_body_reception_receiving_context_role_boundary_from_path(
                malformed
            )
            self.assertEqual(
                "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED",
                result["block"]["block_code"],
            )

            array_payload = Path(temp_dir) / "array.json"
            array_payload.write_text("[]", encoding="utf-8")
            result = resolver.resolve_source_body_reception_receiving_context_role_boundary_from_path(
                array_payload
            )
            self.assertEqual(
                "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED",
                result["block"]["block_code"],
            )

    def test_selected_identity_preservation_path_unreadable_and_malformed_cases_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing-selected.json"
            request = declared_role_request(selected_identity={})
            request.pop("selected_identity_preservation_result")
            request["selected_identity_preservation_result_path"] = str(missing)
            self.assert_block(request, "IDENTITY_PRESERVATION_RESULT_UNREADABLE")

            malformed = Path(temp_dir) / "malformed-selected.json"
            malformed.write_text("{not-json", encoding="utf-8")
            request = declared_role_request(selected_identity={})
            request.pop("selected_identity_preservation_result")
            request["selected_identity_preservation_result_path"] = str(malformed)
            self.assert_block(request, "IDENTITY_PRESERVATION_RESULT_MALFORMED")

            array_payload = Path(temp_dir) / "array-selected.json"
            array_payload.write_text("[]", encoding="utf-8")
            request = declared_role_request(selected_identity={})
            request.pop("selected_identity_preservation_result")
            request["selected_identity_preservation_result_path"] = str(array_payload)
            self.assert_block(request, "IDENTITY_PRESERVATION_RESULT_MALFORMED")

    def test_selected_identity_preservation_result_issues_block(self) -> None:
        missing_outcome = selected_identity_preservation_result()
        missing_outcome.pop("outcome")
        missing_outcome["source_body_reception_identity_summary"].pop("outcome")
        self.assert_block(
            declared_role_request(selected_identity=missing_outcome),
            "IDENTITY_PRESERVATION_RESULT_OUTCOME_MISSING",
        )

        wrong_outcome = selected_identity_preservation_result(
            outcome="SOURCE_BODY_RECEPTION_IDENTITY_NOT_PRESERVED"
        )
        wrong_outcome["source_body_reception_identity_summary"][
            "outcome"
        ] = "SOURCE_BODY_RECEPTION_IDENTITY_NOT_PRESERVED"
        self.assert_block(
            declared_role_request(selected_identity=wrong_outcome),
            "IDENTITY_PRESERVATION_RESULT_NOT_PRESERVED",
        )

        failed_checks = selected_identity_preservation_result()
        failed_checks["source_body_reception_identity_summary"]["failed_check_count"] = 1
        self.assert_block(
            declared_role_request(selected_identity=failed_checks),
            "IDENTITY_PRESERVATION_RESULT_HAS_FAILED_CHECKS",
        )

    def test_missing_required_selected_basis_blocks(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []

        identity = selected_identity_preservation_result()
        identity.pop("selected_reception_request_declaration")
        cases.append(("RECEPTION_REQUEST_DECLARATION_RESULT_MISSING", identity))

        identity = selected_identity_preservation_result()
        identity.pop("selected_source_body_surface")
        cases.append(("SELECTED_SOURCE_BODY_SURFACE_MISSING", identity))

        for key, code in (
            ("selected_source_body_surface_identifier", "SELECTED_SOURCE_BODY_SURFACE_IDENTIFIER_MISSING"),
            ("selected_source_body_surface_type", "SELECTED_SOURCE_BODY_SURFACE_TYPE_MISSING"),
            ("selected_source_body_surface_path", "SELECTED_SOURCE_BODY_SURFACE_REFERENCE_MISSING"),
            ("source_body_identity_basis", "SOURCE_BODY_IDENTITY_BASIS_MISSING"),
            ("source_body_lineage_basis", "SOURCE_BODY_LINEAGE_BASIS_MISSING"),
        ):
            identity = selected_identity_preservation_result()
            identity["selected_source_body_surface"].pop(key)
            if key == "selected_source_body_surface_path":
                identity["selected_source_body_surface"].pop("selected_source_body_surface_reference")
            cases.append((code, identity))

        identity = selected_identity_preservation_result()
        identity.pop("receiving_context")
        cases.append(("RECEIVING_CONTEXT_MISSING", identity))

        identity = selected_identity_preservation_result()
        identity["receiving_context"].pop("receiving_context_type")
        cases.append(("RECEIVING_CONTEXT_TYPE_MISSING", identity))

        for code, identity in cases:
            with self.subTest(code=code):
                self.assert_block(declared_role_request(selected_identity=identity), code)

        request = declared_role_request()
        request.pop("declared_receiving_context_role")
        request["receiving_context_role_basis"].pop("declared_receiving_context_role")
        self.assert_block(request, "RECEIVING_CONTEXT_ROLE_MISSING")

        request = declared_role_request()
        request.pop("receiving_context_role_class")
        request["receiving_context_role_basis"].pop("receiving_context_role_class")
        self.assert_block(request, "RECEIVING_CONTEXT_ROLE_CLASS_MISSING")

        request = declared_role_request()
        request.pop("receiving_context_role_limits")
        request["receiving_context_role_basis"].pop("receiving_context_role_limits")
        self.assert_block(request, "RECEIVING_CONTEXT_ROLE_LIMITS_MISSING")

    def test_malformed_surface_context_and_unsupported_scope_block(self) -> None:
        self.assert_block(
            declared_role_request(selected_source_body_surface=["bad"]),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        )
        self.assert_block(
            declared_role_request(receiving_context=["bad"]),
            "RECEIVING_CONTEXT_MALFORMED",
        )
        self.assert_block(
            declared_role_request(role_scope=["UNSUPPORTED_SCOPE"]),
            "UNSUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE",
        )

    def test_unsupported_role_classes_block_without_narrowing(self) -> None:
        unsupported_classes = (
            "SOURCE_RECEIVER",
            "SOURCE_ADOPTER",
            "SOURCE_VALIDATOR",
            "SOURCE_INVALIDATOR",
            "SOURCE_AUTHORITY",
            "CURRENT_CONTEXT",
            "OPERATION_OPERATOR",
            "VESSEL_CONTEXT",
            "DERIVATIVE_CONTEXT",
            "PUBLICATION_CONTEXT",
            "ARBITRARY_UNKNOWN_CONTEXT",
        )
        for role_class in unsupported_classes:
            with self.subTest(role_class=role_class):
                result = self.assert_block(
                    declared_role_request(role_class=role_class),
                    "UNSUPPORTED_RECEIVING_CONTEXT_ROLE_CLASS",
                )
                self.assertFalse(result["receiving_context_role"]["receiving_context_role_class_supported"])
                self.assertFalse(
                    result["non_claims"]["source_body_reception_receiving_context_role_recorded"]
                )

    def test_receiving_context_role_collapse_flags_block(self) -> None:
        cases = {
            "reception_recognized": "RECEIVING_CONTEXT_ROLE_RECOGNIZES_RECEPTION",
            "reception_authorized": "RECEIVING_CONTEXT_ROLE_AUTHORIZES_RECEPTION",
            "source_received": "RECEIVING_CONTEXT_ROLE_RECEIVES_SOURCE",
            "receiving_context_governance_created": "RECEIVING_CONTEXT_ROLE_CREATES_GOVERNANCE",
            "receiving_context_became_source": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_SOURCE",
            "receiving_context_became_authority": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_AUTHORITY",
            "receiving_context_became_current": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_CURRENT",
            "receiving_context_became_receiver": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_RECEIVER",
            "receiving_context_became_adopter": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_ADOPTER",
            "receiving_context_became_validator": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_VALIDATOR",
            "receiving_context_became_invalidator": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_INVALIDATOR",
            "receiving_context_became_operator": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_OPERATOR",
            "receiving_context_became_vessel": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_VESSEL",
            "receiving_context_became_derivative": "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_DERIVATIVE",
            "source_validated_by_receiving_context": "RECEIVING_CONTEXT_ROLE_VALIDATES_SOURCE",
            "source_invalidated_by_receiving_context": "RECEIVING_CONTEXT_ROLE_INVALIDATES_SOURCE",
            "source_replaced": "RECEIVING_CONTEXT_ROLE_REPLACES_SOURCE",
            "adoption_created": "RECEIVING_CONTEXT_ROLE_CREATES_ADOPTION",
            "authority_created": "RECEIVING_CONTEXT_ROLE_CREATES_AUTHORITY",
            "currentness_created": "RECEIVING_CONTEXT_ROLE_CREATES_CURRENTNESS",
            "standing_created": "RECEIVING_CONTEXT_ROLE_CREATES_STANDING",
            "standing_propagated": "RECEIVING_CONTEXT_ROLE_CREATES_STANDING_PROPAGATION",
            "vessel_relation_created": "RECEIVING_CONTEXT_ROLE_CREATES_VESSEL_RELATION",
            "derivative_relation_created": "RECEIVING_CONTEXT_ROLE_CREATES_DERIVATIVE_RELATION",
            "operation_permission_created": "RECEIVING_CONTEXT_ROLE_CREATES_OPERATION_PERMISSION",
            "public_launch_readiness_created": "RECEIVING_CONTEXT_ROLE_CREATES_PUBLIC_READINESS",
            "final_completion_claimed": "RECEIVING_CONTEXT_ROLE_CLAIMS_FINAL_COMPLETION",
            "follow_on_work_authorized": "RECEIVING_CONTEXT_ROLE_AUTHORIZES_FOLLOW_ON_WORK",
            "continuation_authorized": "RECEIVING_CONTEXT_ROLE_AUTHORIZES_CONTINUATION",
            "publication_flow_opened": "RECEIVING_CONTEXT_ROLE_OPENS_PUBLICATION_FLOW",
        }
        for field, code in cases.items():
            with self.subTest(field=field):
                self.assert_block(declared_role_request(**{field: True}), code)

    def test_mutation_replay_merge_and_non_claim_failures_block(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                self.assert_block(
                    declared_role_request(**{field: True}),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing_non_claims = false_role_non_claims()
        missing_non_claims.pop("merge_performed")
        self.assert_block(
            declared_role_request(declared_non_claims=missing_non_claims),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

        flipped_non_claims = false_role_non_claims()
        flipped_non_claims["merge_performed"] = True
        self.assert_block(
            declared_role_request(declared_non_claims=flipped_non_claims),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )


if __name__ == "__main__":
    unittest.main()
