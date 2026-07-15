"""Executable boundary tests for source-body reception identity preservation only.

These tests prove that the resolver preserves one selected source-body surface
identity for one declared reception request without recognizing or authorizing
reception, receiving source, defining final source-body identity, inflating the
selected surface into whole-body identity, replacing source, validating or
invalidating source, creating adoption, authority, currentness, standing,
vessel or derivative relation, operation permission, public readiness, final
completion, continuation, publication flow, or follow-on work.
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

import resolve_source_body_reception_identity_preservation_boundary as resolver  # noqa: E402


PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
NOT_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_NOT_PRESERVED"
REQUIRES_ADDITIONAL_BASIS = "SOURCE_BODY_RECEPTION_IDENTITY_REQUIRES_ADDITIONAL_BASIS"
BLOCKED = "SOURCE_BODY_RECEPTION_IDENTITY_REVIEW_BLOCKED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {
    PRESERVED,
    NOT_PRESERVED,
    REQUIRES_ADDITIONAL_BASIS,
    BLOCKED,
}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_identity_metadata",
    "declared_identity_preservation_question",
    "selected_reception_request_declaration",
    "selected_source_body_surface",
    "receiving_context",
    "identity_preservation_basis",
    "identity_preservation_scope",
    "identity_preservation_checks",
    "identity_preservation_statement",
    "identity_preservation_non_meaning",
    "additional_basis_required",
    "not_preserved_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_identity_summary",
}

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_IDENTITY_PRESERVATION_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)


def false_identity_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def false_declaration_non_claims() -> dict[str, bool]:
    return {
        "reception_recognized": False,
        "reception_authorized": False,
        "source_received": False,
        "adoption_created": False,
        "authority_created": False,
        "currentness_created": False,
        "standing_created": False,
        "standing_propagated": False,
        "vessel_relation_created": False,
        "derivative_relation_created": False,
        "operation_permission_created": False,
        "source_replaced": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "receiving_context_became_source": False,
        "receiving_context_became_authority": False,
        "receiving_context_became_current": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }


def distributed_operation_closure_context() -> dict[str, object]:
    return {
        "context_id": "distributed-operation-closure-context-001",
        "context_path": (
            "artifacts/integrity_host_v0_min_coexistence_distributed_operation_"
            "closure_boundary/distributed_operation_closure_boundary_for_"
            "boundary_chain_001__distributed_operation_closure_result.json"
        ),
        "outcome": "DISTRIBUTED_OPERATION_CLOSURE_BOUNDARY_RECORDED",
        "context_only": True,
        "evidence_only": True,
        "not_selected_source_body_surface_by_default": True,
        "did_not_authorize_reception": True,
        "did_not_authorize_follow_on_work": True,
        "reception_authorized": False,
        "follow_on_work_authorized": False,
    }


def terminal_summary_context() -> dict[str, object]:
    return {
        "context_id": "distributed-operation-boundary-chain-terminal-summary-v0",
        "context_path": "spec/DISTRIBUTED_OPERATION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md",
        "context_only": True,
        "evidence_only": True,
        "not_selected_source_body_surface_by_default": True,
        "did_not_open_or_authorize_source_body_reception": True,
        "source_body_reception_authorized": False,
        "publication_flow_opened": False,
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
        "distributed_operation_closure_context": distributed_operation_closure_context(),
        "terminal_summary_context": terminal_summary_context(),
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "source_received": False,
        "adoption_created": False,
        "source_replaced": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "final_source_body_identity_defined": False,
        "whole_body_identity_defined": False,
        "currentness_created": False,
        "authority_created": False,
    }


def receiving_context() -> dict[str, object]:
    return {
        "receiving_context_id": "receiving-context-001",
        "receiving_context_name": "bounded receiving context",
        "receiving_context_reference": "IAMMAI-SYSTEM present execution line",
        "receiving_context_type": "PRESENT_EXECUTION_CONTEXT",
        "receiving_context_declared": True,
        "receiving_context_remains_context_only": True,
        "receiving_context_became_source": False,
        "receiving_context_became_authority": False,
        "receiving_context_became_current": False,
        "source_validated_by_receiving_context": False,
        "source_invalidated_by_receiving_context": False,
        "adoption_created": False,
        "operation_permission_created": False,
        "publication_flow_opened": False,
    }


def reception_purpose() -> dict[str, object]:
    return {
        "purpose_id": "identity-preservation-before-reception-review",
        "purpose_statement": "Preserve selected source-body surface identity for later review.",
        "purpose_is_permission": False,
    }


def reception_limits() -> dict[str, object]:
    return {
        "limits_id": "source-body-reception-identity-preservation-limits-001",
        "identity_preservation_only": True,
        "no_reception_recognition": True,
        "no_reception_authorization": True,
        "no_source_receipt": True,
        "no_final_source_body_identity": True,
        "no_whole_body_identity_inflation": True,
        "no_source_replacement": True,
        "no_source_validation": True,
        "no_source_invalidation": True,
        "no_adoption": True,
        "no_authority": True,
        "no_currentness": True,
        "no_operation_permission": True,
        "no_public_readiness": True,
        "no_final_completion": True,
        "no_follow_on_work": True,
    }


def selected_reception_request_declaration(
    **overrides: object,
) -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    purpose = reception_purpose()
    limits = reception_limits()
    statement = {
        "source_body_reception_request_declared": True,
        "selected_source_body_surface_preserved": True,
        "selected_source_body_surface_remains_source": True,
        "receiving_context_declared": True,
        "receiving_context_remains_context_only": True,
        "reception_class_declared": True,
        "reception_class_supported": True,
        "reception_purpose_declared": True,
        "reception_limits_declared": True,
        "distributed_operation_closure_context_only": True,
        "terminal_summary_context_only": True,
    }
    statement.update(false_declaration_non_claims())
    result: dict[str, object] = {
        "source_body_reception_request_metadata": {
            "source_body_reception_request_result_id": (
                "source_body_reception_request_declaration__request-001"
            ),
            "source_body_reception_request_result_type": (
                "source_body_reception_request_declaration_result"
            ),
            "source_body_reception_request_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_request_declaration",
        },
        "declared_reception_question": {
            "reception_request_id": "source-body-reception-request-001",
            "reception_question": "What source-body reception request has been declared for later review?",
        },
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "reception_class": {
            "selected_reception_class": "REFERENCE_RECEPTION",
            "reception_class_supported": True,
        },
        "reception_purpose": {"reception_purpose": purpose},
        "reception_limits": {"reception_limits": limits},
        "declaration_checks": [],
        "declaration_statement": statement,
        "non_claims": false_declaration_non_claims(),
        "outcome": REQUEST_DECLARED,
        "source_body_reception_request_summary": {
            "outcome": REQUEST_DECLARED,
            "reception_request_id": "source-body-reception-request-001",
            "failed_check_count": 0,
            "passed_check_count": 36,
            "selected_source_body_surface_preserved": True,
            "selected_source_body_surface_remains_source": True,
            "receiving_context_declared": True,
            "receiving_context_remains_context_only": True,
            "reception_class": "REFERENCE_RECEPTION",
            "reception_purpose": purpose,
        },
    }
    result.update(overrides)
    return result


def identity_preservation_basis() -> dict[str, object]:
    return {
        "basis_id": "source-body-reception-identity-preservation-basis-001",
        "selected_reception_request_declaration_preserved": True,
        "selected_source_body_surface_remains_source_posture": True,
        "receiving_context_remains_non_source_posture": True,
        "closure_context_is_context_only": True,
        "terminal_summary_context_is_context_only": True,
        "request_declaration_is_context_only": True,
        "no_replacement_posture": True,
        "no_validation_posture": True,
        "no_invalidation_posture": True,
        "latest_artifact_not_source": True,
        "carrier_possession_not_source": True,
        "registry_reference_not_source_replacement": True,
        "identity_preservation_is_not_reception": True,
        "identity_preservation_is_not_authorization": True,
        "identity_preservation_does_not_define_final_identity": True,
        "identity_preservation_does_not_inflate_selected_surface_to_whole_body": True,
    }


def declared_identity_preservation_request(
    selected_declaration: dict[str, object] | None = None,
    **overrides: object,
) -> dict[str, object]:
    selected = selected_declaration or selected_reception_request_declaration()
    summary = selected.get("source_body_reception_request_summary", {})
    request_id = None
    if isinstance(summary, dict):
        request_id = summary.get("reception_request_id")
    request: dict[str, object] = {
        "identity_preservation_request_id": "source-body-reception-identity-preservation-001",
        "identity_preservation_question": (
            "How is the selected source-body surface identity preserved for this declared reception request?"
        ),
        "identity_preservation_intent": "RECORD_SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION",
        "selected_reception_request_declaration": selected,
        "selected_reception_request_declaration_id": request_id,
        "selected_reception_request_declaration_outcome": selected.get("outcome"),
        "identity_preservation_basis": identity_preservation_basis(),
        "identity_preservation_scope": list(SUPPORTED_SCOPE),
        "request_declaration_context": {
            "request_declaration_context_id": "request-declaration-context-001",
            "context_only": True,
            "evidence_only": True,
            "request_declaration_does_not_replace_source": True,
        },
        "requested_identity_preservation_outcome": PRESERVED,
        "additional_basis_context": {},
        "not_preserved_basis": None,
        "declared_non_claims": false_identity_non_claims(),
    }
    request.update(overrides)
    return request


def resolve(request: object | None) -> dict[str, object]:
    return resolver.resolve_source_body_reception_identity_preservation_boundary(
        declared_identity_preservation_request=request
    )


class IdentityPreservationAssertions:
    def assert_outcome_family(self, result: dict[str, object]) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_block(self, request: object, code: str) -> dict[str, object]:
        result = resolve(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        self.assertFalse(result["non_claims"]["source_body_reception_identity_preserved"])
        self.assert_outcome_family(result)
        return result

    def assert_required_non_claims_false(self, result: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
            self.assertIs(result["non_claims"][key], False, key)

    def assert_no_identity_collapse(self, section: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, section, key)
            self.assertIs(section[key], False, key)


class TestSourceBodyReceptionIdentityPreserved(
    IdentityPreservationAssertions, unittest.TestCase
):
    def setUp(self) -> None:
        self.request = declared_identity_preservation_request()
        self.request_before = copy.deepcopy(self.request)
        self.result = resolve(self.request)

    def test_successful_identity_preserved_result_shape_and_statement(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(self.result))
        self.assertEqual(PRESERVED, self.result["outcome"])
        self.assertIsNone(self.result["block"]["block_code"])
        self.assertIsNone(self.result["block"]["block_reason"])
        self.assertEqual(0, self.result["source_body_reception_identity_summary"]["failed_check_count"])
        self.assertGreater(self.result["source_body_reception_identity_summary"]["passed_check_count"], 0)

        statement = self.result["identity_preservation_statement"]
        self.assertIs(statement["source_body_reception_identity_preserved"], True)
        self.assertIs(statement["selected_reception_request_declaration_preserved"], True)
        self.assertIs(statement["selected_reception_request_declaration_recorded"], True)
        self.assertIs(statement["selected_reception_request_declaration_failed_check_count_zero"], True)
        self.assertIs(statement["selected_source_body_surface_preserved"], True)
        self.assertIs(statement["selected_source_body_surface_remains_source"], True)
        self.assertIs(statement["selected_surface_is_not_whole_body_by_default"], True)
        self.assertIs(statement["receiving_context_preserved"], True)
        self.assertIs(statement["receiving_context_remains_context_only"], True)
        self.assertIs(statement["receiving_context_is_not_source"], True)
        self.assertIs(statement["receiving_context_is_not_authority"], True)
        self.assertIs(statement["receiving_context_is_not_current"], True)
        self.assertIs(statement["reception_class_preserved"], True)
        self.assertIs(statement["reception_purpose_preserved"], True)
        self.assertIs(statement["reception_limits_preserved"], True)
        self.assertIs(statement["closure_context_is_context_only"], True)
        self.assertIs(statement["terminal_summary_context_is_context_only"], True)
        self.assertIs(statement["request_declaration_is_context_only"], True)
        self.assert_no_identity_collapse(statement)
        self.assert_required_non_claims_false(self.result)
        self.assertIs(self.result["non_claims"]["source_body_reception_identity_preserved"], True)
        self.assertEqual(self.request_before, self.request)

    def test_metadata_and_declared_question_are_bounded(self) -> None:
        metadata = self.result["source_body_reception_identity_metadata"]
        for key in (
            "source_body_reception_identity_result_id",
            "source_body_reception_identity_result_type",
            "source_body_reception_identity_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["source_body_reception_identity_result_version"])
        self.assertEqual(
            "resolve_source_body_reception_identity_preservation_boundary",
            metadata["resolver_module"],
        )

        question = self.result["declared_identity_preservation_question"]
        self.assertEqual(
            self.request["identity_preservation_request_id"],
            question["identity_preservation_request_id"],
        )
        self.assertEqual(
            self.request["identity_preservation_question"],
            question["identity_preservation_question"],
        )
        self.assertEqual(
            "RECORD_SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION",
            question["identity_preservation_intent"],
        )
        self.assertEqual(REQUEST_DECLARED, question["selected_reception_request_declaration_outcome"])
        self.assertIs(question["identity_preservation_is_not_reception"], True)
        self.assertIs(question["identity_preservation_is_not_authorization"], True)
        self.assertIs(question["identity_preservation_is_not_final_source_body_identity"], True)
        self.assertIs(question["identity_preservation_is_not_whole_body_identity"], True)

    def test_selected_request_declaration_is_preserved_not_upgraded(self) -> None:
        declaration = self.result["selected_reception_request_declaration"]
        self.assertEqual("source-body-reception-request-001", declaration["selected_reception_request_declaration_id"])
        self.assertEqual(REQUEST_DECLARED, declaration["selected_reception_request_declaration_outcome"])
        self.assertIs(declaration["selected_reception_request_declaration_recorded"], True)
        self.assertIs(declaration["selected_reception_request_declaration_failed_check_count_zero"], True)
        self.assertIs(declaration["request_declaration_did_not_recognize_reception"], True)
        self.assertIs(declaration["request_declaration_did_not_authorize_reception"], True)
        self.assertIs(declaration["request_declaration_did_not_receive_source"], True)
        self.assertIs(declaration["request_declaration_remains_context_evidence_only"], True)
        self.assertIs(declaration["request_declaration_did_not_mutate_replay_or_merge"], True)
        self.assertIs(declaration["selected_source_body_surface_preserved_by_request_declaration"], True)
        self.assertIs(declaration["selected_source_body_surface_remains_source_by_request_declaration"], True)
        self.assertIs(declaration["receiving_context_declared_by_request_declaration"], True)
        self.assertIs(declaration["receiving_context_remains_context_only_by_request_declaration"], True)

    def test_selected_surface_receiving_context_and_basis_are_preserved(self) -> None:
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
        self.assertIs(surface["final_source_body_identity_defined"], False)
        self.assertIs(surface["whole_body_identity_defined"], False)
        self.assertIs(surface["currentness_created"], False)
        self.assertIs(surface["authority_created"], False)

        context = self.result["receiving_context"]
        self.assertEqual("receiving-context-001", context["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", context["receiving_context_type"])
        self.assertIs(context["receiving_context_preserved"], True)
        self.assertIs(context["receiving_context_remains_context_only"], True)
        self.assertIs(context["receiving_context_is_not_source"], True)
        self.assertIs(context["receiving_context_is_not_authority"], True)
        self.assertIs(context["receiving_context_is_not_current"], True)
        self.assertIs(context["receiving_context_did_not_validate_source"], True)
        self.assertIs(context["receiving_context_did_not_invalidate_source"], True)
        self.assertIs(context["receiving_context_did_not_create_adoption"], True)
        self.assertIs(context["receiving_context_did_not_create_operation_permission"], True)
        self.assertIs(context["receiving_context_did_not_open_publication_flow"], True)

        basis = self.result["identity_preservation_basis"]
        self.assertTrue(basis["selected_reception_request_declaration"])
        self.assertTrue(basis["selected_source_body_surface"])
        self.assertTrue(basis["source_body_identity_basis"])
        self.assertTrue(basis["source_body_lineage_basis"])
        self.assertEqual("REFERENCE_RECEPTION", basis["reception_class"])
        self.assertTrue(basis["reception_purpose"])
        self.assertTrue(basis["reception_limits"])
        self.assertTrue(basis["distributed_operation_closure_context"])
        self.assertTrue(basis["terminal_summary_context"])
        self.assertTrue(basis["request_declaration_context"])
        self.assertIs(basis["closure_context_is_context_only"], True)
        self.assertIs(basis["terminal_summary_context_is_context_only"], True)
        self.assertIs(basis["request_declaration_is_context_only"], True)
        self.assertIs(basis["selected_source_body_surface_remains_source"], True)
        self.assertIs(basis["receiving_context_remains_non_source"], True)
        self.assertIs(basis["no_source_replacement"], True)
        self.assertIs(basis["no_source_validation_by_receiving_context"], True)
        self.assertIs(basis["no_source_invalidation_by_receiving_context"], True)
        self.assertIs(basis["latest_artifact_not_source"], True)
        self.assertIs(basis["carrier_possession_not_source"], True)
        self.assertIs(basis["registry_reference_not_source_replacement"], True)
        self.assertIs(basis["identity_preservation_is_not_reception"], True)
        self.assertIs(basis["identity_preservation_is_not_authorization"], True)
        self.assertIs(basis["identity_preservation_does_not_define_final_identity"], True)
        self.assertIs(basis["identity_preservation_does_not_inflate_selected_surface_to_whole_body"], True)

    def test_supported_scope_values_and_checks_are_recorded(self) -> None:
        for value in SUPPORTED_SCOPE:
            result = resolve(declared_identity_preservation_request(identity_preservation_scope=[value]))
            self.assertEqual(PRESERVED, result["outcome"], value)
            scope = result["identity_preservation_scope"]
            self.assertEqual([value], scope["selected_identity_preservation_scope_values"])
            self.assertIs(scope["all_selected_scope_values_supported"], True)

        unsupported = resolve(declared_identity_preservation_request(identity_preservation_scope=["UNSUPPORTED_SCOPE"]))
        self.assertEqual(BLOCKED, unsupported["outcome"])
        self.assertEqual("UNSUPPORTED_IDENTITY_PRESERVATION_SCOPE", unsupported["block"]["block_code"])

        checks = self.result["identity_preservation_checks"]
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
            "identity preservation question declared",
            "identity preservation intent supported",
            "selected reception request declaration result present",
            "selected reception request declaration outcome declared",
            "selected reception request declaration outcome declared request",
            "selected reception request declaration failed check count zero",
            "selected source-body surface identifier preserved",
            "selected source-body surface type preserved",
            "selected source-body surface path/reference preserved",
            "source-body identity basis preserved",
            "source-body lineage basis preserved",
            "selected source-body surface remains source",
            "selected source-body surface is not whole body by default",
            "receiving context preserved",
            "receiving context remains context only",
            "receiving context is not source",
            "receiving context is not authority",
            "receiving context is not current",
            "reception class preserved",
            "reception purpose preserved",
            "reception limits preserved",
            "distributed-operation closure context remains context/evidence only where supplied",
            "terminal summary context remains context/evidence only where supplied",
            "request declaration remains context/evidence only",
            "no source replacement",
            "no source validation by receiving context",
            "no source invalidation by receiving context",
            "declaration still does not recognize reception",
            "declaration still does not authorize reception",
            "latest artifact not source",
            "carrier possession not source",
            "registry/reference not source replacement",
            "no mutation/replay/merge",
            "non-claims remain false",
        ):
            self.assertIn(expected, names)

    def test_non_meaning_remaining_open_non_claims_and_summary(self) -> None:
        non_meaning = self.result["identity_preservation_non_meaning"]
        for key in (
            "reception_recognized",
            "reception_authorized",
            "source_received",
            "final_source_body_identity_defined",
            "whole_body_identity_defined",
            "selected_source_body_surface_became_whole_body",
            "source_adopted",
            "source_validated",
            "source_invalidated",
            "source_replaced",
            "receiving_context_became_source",
            "receiving_context_became_authority",
            "receiving_context_became_current",
            "closure_artifact_became_source",
            "terminal_summary_became_source",
            "request_declaration_artifact_became_source",
            "latest_artifact_became_source",
            "carrier_possession_became_source",
            "registry_reference_replaced_source",
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
            "source_body_reception_identity_preservation_test",
            "source_body_reception_identity_preservation_live_artifact",
            "receiving_context_role_boundary",
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
            "public_readiness",
            "final_completion",
            "follow_on_work",
            "open_means_not_scheduled",
            "open_means_not_authorized",
            "open_means_not_executed",
        ):
            self.assertIs(remains_open[key], True, key)

        summary = self.result["source_body_reception_identity_summary"]
        self.assertEqual(PRESERVED, summary["outcome"])
        self.assertIs(summary["identity_preserved"], True)
        self.assertIs(summary["not_preserved"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertEqual("source-body-surface-001", summary["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", summary["selected_source_body_surface_type"])
        self.assertEqual("receiving-context-001", summary["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", summary["receiving_context_type"])
        self.assertIs(summary["selected_request_declaration_recorded"], True)
        self.assertIs(summary["selected_source_body_surface_remains_source"], True)
        self.assertIs(summary["selected_surface_is_not_whole_body_by_default"], True)
        self.assertIs(summary["receiving_context_remains_context_only"], True)
        self.assertIs(summary["receiving_context_is_not_source"], True)
        self.assertIs(summary["receiving_context_is_not_authority"], True)
        self.assertIs(summary["receiving_context_is_not_current"], True)
        self.assertIs(summary["request_declaration_context_only"], True)
        self.assertIs(summary["no_reception_recognized"], True)
        self.assertIs(summary["no_reception_authorized"], True)
        self.assertIs(summary["no_source_received"], True)
        self.assertIs(summary["no_final_source_body_identity_defined"], True)
        self.assertIs(summary["no_whole_body_identity_inflation"], True)
        self.assertIs(summary["no_adoption"], True)
        self.assertIs(summary["no_authority"], True)
        self.assertIs(summary["no_currentness"], True)
        self.assertIs(summary["no_standing"], True)
        self.assertIs(summary["no_vessel_relation"], True)
        self.assertIs(summary["no_derivative_relation"], True)
        self.assertIs(summary["no_operation_permission"], True)
        self.assertIs(summary["no_public_readiness"], True)
        self.assertIs(summary["no_final_completion"], True)
        self.assertIs(summary["no_follow_on_work"], True)
        self.assertEqual(
            {key: False for key in REQUIRED_NON_CLAIMS},
            summary["key_non_claims"],
        )


class TestIdentityPreservationAlternateOutcomes(
    IdentityPreservationAssertions, unittest.TestCase
):
    def test_requires_additional_basis_preserves_missing_basis_as_unexecuted(self) -> None:
        context = {
            "reason": "selected source-body surface identifier too generic",
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
        request = declared_identity_preservation_request(
            requested_identity_preservation_outcome=REQUIRES_ADDITIONAL_BASIS,
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
        self.assertFalse(result["non_claims"]["source_body_reception_identity_preserved"])
        self.assert_required_non_claims_false(result)
        self.assertEqual(before, request)

    def test_not_preserved_preserves_readable_basis_without_repair(self) -> None:
        not_preserved = {
            "reason": "source replacement risk remains unresolved",
            "repair_authorized": False,
        }
        request = declared_identity_preservation_request(
            requested_identity_preservation_outcome=NOT_PRESERVED,
            not_preserved_basis=not_preserved,
        )
        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(NOT_PRESERVED, result["outcome"])
        self.assertEqual(not_preserved, result["not_preserved_basis"]["not_preserved_basis"])
        self.assertIs(result["not_preserved_basis"]["identity_not_preserved"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_mutate"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_repair"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_authorize"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_receive_source"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_replace_source"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_validate_source"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_invalidate_source"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_create_currentness"], True)
        self.assertIs(result["not_preserved_basis"]["not_preserved_does_not_recognize_reception"], True)
        self.assertFalse(result["non_claims"]["source_body_reception_identity_preserved"])
        self.assert_required_non_claims_false(result)
        self.assertEqual(before, request)


class TestIdentityPreservationHelpersAndPaths(
    IdentityPreservationAssertions, unittest.TestCase
):
    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        selected = selected_reception_request_declaration()
        request = resolver.build_declared_source_body_reception_identity_preservation_request(
            "identity-preservation-builder-001",
            "How is the selected source-body surface identity preserved for this declared reception request?",
            selected,
            identity_preservation_basis(),
            list(SUPPORTED_SCOPE),
            selected_reception_request_declaration_id="source-body-reception-request-001",
            selected_reception_request_declaration_outcome=REQUEST_DECLARED,
            additional_basis_context={"reason": "none"},
            not_preserved_basis={"reason": "none"},
        )
        self.assertEqual("identity-preservation-builder-001", request["identity_preservation_request_id"])
        self.assertEqual(selected, request["selected_reception_request_declaration"])
        self.assertEqual(list(SUPPORTED_SCOPE), request["identity_preservation_scope"])
        self.assertEqual({"reason": "none"}, request["additional_basis_context"])
        self.assertEqual({"reason": "none"}, request["not_preserved_basis"])
        self.assertEqual(false_identity_non_claims(), request["declared_non_claims"])
        result = resolve(request)
        self.assertEqual(PRESERVED, result["outcome"])

    def test_path_based_selected_request_declaration_result_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            declaration_path = Path(temp_dir) / "selected_declaration.json"
            declaration_path.write_text(
                json.dumps(selected_reception_request_declaration(), indent=2),
                encoding="utf-8",
            )
            request = declared_identity_preservation_request()
            request.pop("selected_reception_request_declaration")
            request["selected_reception_request_declaration_path"] = str(declaration_path)
            result = resolve(request)
            self.assertEqual(PRESERVED, result["outcome"])
            selected = result["selected_reception_request_declaration"]
            self.assertEqual(str(declaration_path), selected["selected_reception_request_declaration_path"])
            self.assertEqual("source-body-reception-request-001", selected["selected_reception_request_declaration_id"])
            self.assertEqual(REQUEST_DECLARED, selected["selected_reception_request_declaration_outcome"])

    def test_path_based_identity_preservation_request_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request_path = Path(temp_dir) / "identity_request.json"
            request_path.write_text(
                json.dumps(declared_identity_preservation_request(), indent=2),
                encoding="utf-8",
            )
            path_result = resolver.resolve_source_body_reception_identity_preservation_boundary_from_path(
                request_path
            )
            mapping_result = resolve(declared_identity_preservation_request())
            self.assertEqual(PRESERVED, path_result["outcome"])
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                str(request_path),
                path_result["declared_identity_preservation_question"][
                    "declared_identity_preservation_request_path"
                ],
            )

    def test_write_behavior_uses_additive_temp_paths_and_suffixes(self) -> None:
        result = resolve(declared_identity_preservation_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "identity_result.json"
            written = resolver.write_source_body_reception_identity_preservation_result(
                result, explicit_path
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))

            default_root = Path(temp_dir) / "identity-root"
            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION_ROOT",
                default_root,
            ):
                first = resolver.write_source_body_reception_identity_preservation_result(result)
                second = resolver.write_source_body_reception_identity_preservation_result(result)
            self.assertEqual(default_root, first.parent)
            self.assertEqual(default_root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertIn("__source_body_reception_identity_preservation_result", first.name)
            self.assertNotIn("source_body_reception_request_declaration", str(first))
            self.assertNotIn("source_body_reception_boundary", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_identity_preservation_request()
        request_before = copy.deepcopy(request)
        selected_before = copy.deepcopy(request["selected_reception_request_declaration"])
        surface_before = copy.deepcopy(
            request["selected_reception_request_declaration"]["selected_source_body_surface"]
        )
        context_before = copy.deepcopy(
            request["selected_reception_request_declaration"]["receiving_context"]
        )
        basis_before = copy.deepcopy(request["identity_preservation_basis"])
        scope_before = copy.deepcopy(request["identity_preservation_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(PRESERVED, first["outcome"])
        self.assertEqual(PRESERVED, second["outcome"])
        self.assertEqual(request_before, request)
        self.assertEqual(selected_before, request["selected_reception_request_declaration"])
        self.assertEqual(surface_before, request["selected_reception_request_declaration"]["selected_source_body_surface"])
        self.assertEqual(context_before, request["selected_reception_request_declaration"]["receiving_context"])
        self.assertEqual(basis_before, request["identity_preservation_basis"])
        self.assertEqual(scope_before, request["identity_preservation_scope"])


class TestIdentityPreservationBlocking(
    IdentityPreservationAssertions, unittest.TestCase
):
    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        self.assert_block(
            declared_identity_preservation_request(
                identity_preservation_intent=(
                    "BLOCK_SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION_REVIEW"
                )
            ),
            "IDENTITY_PRESERVATION_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assert_block(None, "IDENTITY_PRESERVATION_QUESTION_UNDECLARED")
        self.assert_block("not a mapping", "DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED")

    def test_request_path_unreadable_and_malformed_cases_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing.json"
            result = resolver.resolve_source_body_reception_identity_preservation_boundary_from_path(
                missing
            )
            self.assertEqual(BLOCKED, result["outcome"])
            self.assertEqual("DECLARED_IDENTITY_PRESERVATION_REQUEST_UNREADABLE", result["block"]["block_code"])

            malformed = Path(temp_dir) / "malformed.json"
            malformed.write_text("{not-json", encoding="utf-8")
            result = resolver.resolve_source_body_reception_identity_preservation_boundary_from_path(
                malformed
            )
            self.assertEqual("DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED", result["block"]["block_code"])

            array_payload = Path(temp_dir) / "array.json"
            array_payload.write_text("[]", encoding="utf-8")
            result = resolver.resolve_source_body_reception_identity_preservation_boundary_from_path(
                array_payload
            )
            self.assertEqual("DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED", result["block"]["block_code"])

    def test_selected_request_declaration_path_unreadable_and_malformed_cases_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing-selected.json"
            request = declared_identity_preservation_request(
                selected_reception_request_declaration_path=str(missing)
            )
            request.pop("selected_reception_request_declaration")
            self.assert_block(request, "RECEPTION_REQUEST_DECLARATION_RESULT_UNREADABLE")

            malformed = Path(temp_dir) / "malformed-selected.json"
            malformed.write_text("{not-json", encoding="utf-8")
            request = declared_identity_preservation_request(
                selected_reception_request_declaration_path=str(malformed)
            )
            request.pop("selected_reception_request_declaration")
            self.assert_block(request, "RECEPTION_REQUEST_DECLARATION_RESULT_MALFORMED")

            array_payload = Path(temp_dir) / "array-selected.json"
            array_payload.write_text("[]", encoding="utf-8")
            request = declared_identity_preservation_request(
                selected_reception_request_declaration_path=str(array_payload)
            )
            request.pop("selected_reception_request_declaration")
            self.assert_block(request, "RECEPTION_REQUEST_DECLARATION_RESULT_MALFORMED")

    def test_selected_request_declaration_result_issues_block(self) -> None:
        missing_outcome = selected_reception_request_declaration()
        missing_outcome.pop("outcome")
        missing_outcome["source_body_reception_request_summary"].pop("outcome")
        self.assert_block(
            declared_identity_preservation_request(selected_declaration=missing_outcome),
            "RECEPTION_REQUEST_DECLARATION_RESULT_OUTCOME_MISSING",
        )

        wrong_outcome = selected_reception_request_declaration(outcome="SOURCE_BODY_RECEPTION_REQUEST_BLOCKED")
        wrong_outcome["source_body_reception_request_summary"]["outcome"] = "SOURCE_BODY_RECEPTION_REQUEST_BLOCKED"
        self.assert_block(
            declared_identity_preservation_request(selected_declaration=wrong_outcome),
            "RECEPTION_REQUEST_DECLARATION_RESULT_NOT_DECLARED",
        )

        failed_checks = selected_reception_request_declaration()
        failed_checks["source_body_reception_request_summary"]["failed_check_count"] = 1
        self.assert_block(
            declared_identity_preservation_request(selected_declaration=failed_checks),
            "RECEPTION_REQUEST_DECLARATION_RESULT_HAS_FAILED_CHECKS",
        )

    def test_missing_required_selected_basis_blocks(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []

        declaration = selected_reception_request_declaration()
        declaration.pop("selected_source_body_surface")
        cases.append(("SELECTED_SOURCE_BODY_SURFACE_MISSING", declaration))

        for key, code in (
            ("selected_source_body_surface_identifier", "SELECTED_SOURCE_BODY_SURFACE_IDENTIFIER_MISSING"),
            ("selected_source_body_surface_type", "SELECTED_SOURCE_BODY_SURFACE_TYPE_MISSING"),
            ("selected_source_body_surface_path", "SELECTED_SOURCE_BODY_SURFACE_REFERENCE_MISSING"),
            ("source_body_identity_basis", "SOURCE_BODY_IDENTITY_BASIS_MISSING"),
            ("source_body_lineage_basis", "SOURCE_BODY_LINEAGE_BASIS_MISSING"),
        ):
            declaration = selected_reception_request_declaration()
            declaration["selected_source_body_surface"].pop(key)
            if key == "selected_source_body_surface_path":
                declaration["selected_source_body_surface"].pop("selected_source_body_surface_reference")
            cases.append((code, declaration))

        declaration = selected_reception_request_declaration()
        declaration.pop("receiving_context")
        cases.append(("RECEIVING_CONTEXT_MISSING", declaration))

        declaration = selected_reception_request_declaration()
        declaration["receiving_context"].pop("receiving_context_type")
        cases.append(("RECEIVING_CONTEXT_TYPE_MISSING", declaration))

        declaration = selected_reception_request_declaration()
        declaration.pop("reception_class")
        declaration["source_body_reception_request_summary"].pop("reception_class")
        cases.append(("RECEPTION_CLASS_MISSING", declaration))

        declaration = selected_reception_request_declaration()
        declaration.pop("reception_purpose")
        declaration["source_body_reception_request_summary"].pop("reception_purpose")
        cases.append(("RECEPTION_PURPOSE_MISSING", declaration))

        declaration = selected_reception_request_declaration()
        declaration.pop("reception_limits")
        cases.append(("RECEPTION_LIMITS_MISSING", declaration))

        for code, declaration in cases:
            with self.subTest(code=code):
                self.assert_block(
                    declared_identity_preservation_request(selected_declaration=declaration),
                    code,
                )

    def test_malformed_surface_context_and_unsupported_scope_block(self) -> None:
        self.assert_block(
            declared_identity_preservation_request(selected_source_body_surface=["bad"]),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        )
        self.assert_block(
            declared_identity_preservation_request(receiving_context=["bad"]),
            "RECEIVING_CONTEXT_MALFORMED",
        )
        self.assert_block(
            declared_identity_preservation_request(identity_preservation_scope=["UNSUPPORTED"]),
            "UNSUPPORTED_IDENTITY_PRESERVATION_SCOPE",
        )

    def test_identity_preservation_collapse_flags_block(self) -> None:
        cases = {
            "reception_recognized": "IDENTITY_PRESERVATION_RECOGNIZES_RECEPTION",
            "reception_authorized": "IDENTITY_PRESERVATION_AUTHORIZES_RECEPTION",
            "source_received": "IDENTITY_PRESERVATION_RECEIVES_SOURCE",
            "final_source_body_identity_defined": "IDENTITY_PRESERVATION_DEFINES_FINAL_SOURCE_BODY_IDENTITY",
            "selected_surface_inflated_to_whole_body": "IDENTITY_PRESERVATION_INFLATES_SELECTED_SURFACE_TO_WHOLE_BODY",
            "source_replaced": "IDENTITY_PRESERVATION_REPLACES_SOURCE",
            "source_validated_by_receiving_context": "IDENTITY_PRESERVATION_VALIDATES_SOURCE",
            "source_invalidated_by_receiving_context": "IDENTITY_PRESERVATION_INVALIDATES_SOURCE",
            "receiving_context_became_source": "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE",
            "receiving_context_became_authority": "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_AUTHORITY",
            "receiving_context_became_current": "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_CURRENT",
            "closure_artifact_became_source": "IDENTITY_PRESERVATION_TREATS_CLOSURE_ARTIFACT_AS_SOURCE",
            "terminal_summary_became_source": "IDENTITY_PRESERVATION_TREATS_TERMINAL_SUMMARY_AS_SOURCE",
            "request_declaration_became_source": "IDENTITY_PRESERVATION_TREATS_REQUEST_DECLARATION_AS_SOURCE",
            "latest_artifact_became_source": "IDENTITY_PRESERVATION_TREATS_LATEST_ARTIFACT_AS_SOURCE",
            "carrier_possession_became_source": "IDENTITY_PRESERVATION_TREATS_CARRIER_POSSESSION_AS_SOURCE",
            "registry_reference_replaced_source": "IDENTITY_PRESERVATION_TREATS_REGISTRY_REFERENCE_AS_SOURCE_REPLACEMENT",
            "adoption_created": "IDENTITY_PRESERVATION_CREATES_ADOPTION",
            "authority_created": "IDENTITY_PRESERVATION_CREATES_AUTHORITY",
            "currentness_created": "IDENTITY_PRESERVATION_CREATES_CURRENTNESS",
            "standing_created": "IDENTITY_PRESERVATION_CREATES_STANDING",
            "standing_propagated": "IDENTITY_PRESERVATION_CREATES_STANDING_PROPAGATION",
            "vessel_relation_created": "IDENTITY_PRESERVATION_CREATES_VESSEL_RELATION",
            "derivative_relation_created": "IDENTITY_PRESERVATION_CREATES_DERIVATIVE_RELATION",
            "operation_permission_created": "IDENTITY_PRESERVATION_CREATES_OPERATION_PERMISSION",
            "public_launch_readiness_created": "IDENTITY_PRESERVATION_CREATES_PUBLIC_READINESS",
            "final_completion_claimed": "IDENTITY_PRESERVATION_CLAIMS_FINAL_COMPLETION",
            "follow_on_work_authorized": "IDENTITY_PRESERVATION_AUTHORIZES_FOLLOW_ON_WORK",
            "continuation_authorized": "IDENTITY_PRESERVATION_AUTHORIZES_CONTINUATION",
            "publication_flow_opened": "IDENTITY_PRESERVATION_OPENS_PUBLICATION_FLOW",
        }
        for field, code in cases.items():
            with self.subTest(field=field):
                self.assert_block(declared_identity_preservation_request(**{field: True}), code)

    def test_mutation_replay_merge_and_non_claim_failures_block(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                self.assert_block(
                    declared_identity_preservation_request(**{field: True}),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing_non_claims = false_identity_non_claims()
        missing_non_claims.pop("merge_performed")
        self.assert_block(
            declared_identity_preservation_request(declared_non_claims=missing_non_claims),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

        flipped_non_claims = false_identity_non_claims()
        flipped_non_claims["merge_performed"] = True
        self.assert_block(
            declared_identity_preservation_request(declared_non_claims=flipped_non_claims),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )


if __name__ == "__main__":
    unittest.main()
