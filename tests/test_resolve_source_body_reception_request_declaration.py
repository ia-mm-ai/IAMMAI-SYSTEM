"""Executable boundary tests for source-body reception request declaration only.

These tests prove that the resolver declares one bounded reception request for
later review without recognizing reception, authorizing reception, adopting or
replacing source, creating currentness, standing, public readiness, final
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

import resolve_source_body_reception_request_declaration as resolver  # noqa: E402


DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"
NOT_SUFFICIENT = "SOURCE_BODY_RECEPTION_REQUEST_NOT_SUFFICIENT"
REQUIRES_ADDITIONAL_BASIS = "SOURCE_BODY_RECEPTION_REQUEST_REQUIRES_ADDITIONAL_BASIS"
BLOCKED = "SOURCE_BODY_RECEPTION_REQUEST_BLOCKED"

OUTCOME_FAMILY = {
    DECLARED,
    NOT_SUFFICIENT,
    REQUIRES_ADDITIONAL_BASIS,
    BLOCKED,
}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_request_metadata",
    "declared_reception_question",
    "selected_source_body_surface",
    "receiving_context",
    "reception_class",
    "reception_purpose",
    "reception_limits",
    "declaration_checks",
    "declaration_statement",
    "declaration_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_request_summary",
}

REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)


def false_non_claims() -> dict[str, bool]:
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


def distributed_operation_closure_context() -> dict[str, object]:
    return {
        "context_id": "distributed-operation-closure-context-001",
        "context_path": (
            "artifacts/integrity_host_v0_min_coexistence_distributed_operation_"
            "closure_boundary/distributed_operation_closure_boundary_for_"
            "boundary_chain_001__distributed_operation_closure_result.json"
        ),
        "outcome": "DISTRIBUTED_OPERATION_CLOSURE_BOUNDARY_RECORDED",
        "context_evidence_only": True,
        "context_only": True,
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
        "context_evidence_only": True,
        "context_only": True,
        "not_selected_source_body_surface_by_default": True,
        "did_not_open_or_authorize_source_body_reception": True,
        "source_body_reception_authorized": False,
        "publication_flow_opened": False,
    }


def reception_purpose() -> dict[str, object]:
    return {
        "purpose_id": "inspect-source-body-surface-for-later-review",
        "purpose_statement": "Declare one bounded request for later source-body reception review.",
        "purpose_is_permission": False,
    }


def reception_limits() -> dict[str, object]:
    return {
        "limits_id": "source-body-reception-request-limits-001",
        "declaration_only": True,
        "no_reception_recognition": True,
        "no_reception_authorization": True,
        "no_adoption": True,
        "no_authority": True,
        "no_currentness": True,
        "no_standing": True,
        "no_vessel_or_derivative_relation": True,
        "no_operation_permission": True,
        "no_public_readiness": True,
        "no_final_completion": True,
        "no_follow_on_work": True,
    }


def declared_reception_request(**overrides: object) -> dict[str, object]:
    surface = selected_source_body_surface()
    context = receiving_context()
    request: dict[str, object] = {
        "reception_request_id": "source-body-reception-request-001",
        "reception_question": "What source-body reception request has been declared for later review?",
        "selected_source_body_surface": surface,
        "selected_source_body_surface_identifier": surface["selected_source_body_surface_identifier"],
        "selected_source_body_surface_type": surface["selected_source_body_surface_type"],
        "selected_source_body_surface_path": surface["selected_source_body_surface_path"],
        "selected_source_body_surface_reference": surface["selected_source_body_surface_reference"],
        "source_body_identity_basis": surface["source_body_identity_basis"],
        "source_body_lineage_basis": surface["source_body_lineage_basis"],
        "distributed_operation_closure_context": distributed_operation_closure_context(),
        "terminal_summary_context": terminal_summary_context(),
        "receiving_context": context,
        "receiving_context_id": context["receiving_context_id"],
        "receiving_context_type": context["receiving_context_type"],
        "reception_class": "REFERENCE_RECEPTION",
        "reception_purpose": reception_purpose(),
        "reception_limits": reception_limits(),
        "requested_reception_declaration_outcome": DECLARED,
        "additional_basis_context": {},
        "not_sufficient_reason": None,
        "declared_non_claims": false_non_claims(),
    }
    request.update(overrides)
    return request


def resolve(request: dict[str, object] | object | None) -> dict[str, object]:
    return resolver.resolve_source_body_reception_request_declaration(
        declared_reception_request=request
    )


class SourceBodyReceptionRequestDeclarationAssertions:
    def assert_outcome_family(self, result: dict[str, object]) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_block(self, request: object, code: str) -> dict[str, object]:
        result = resolve(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        self.assertFalse(result["non_claims"].get("source_body_reception_request_declared"))
        self.assert_outcome_family(result)
        return result

    def assert_required_non_claims_false(self, result: dict[str, object]) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
            self.assertIs(result["non_claims"][key], False, key)

    def assert_no_reception_or_capture(self, section: dict[str, object]) -> None:
        for key in (
            "reception_recognized",
            "reception_authorized",
            "source_received",
            "adoption_created",
            "authority_created",
            "currentness_created",
            "standing_created",
            "standing_propagated",
            "vessel_relation_created",
            "derivative_relation_created",
            "operation_permission_created",
            "source_replaced",
            "source_validated_by_receiving_context",
            "source_invalidated_by_receiving_context",
            "receiving_context_became_source",
            "receiving_context_became_authority",
            "receiving_context_became_current",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
        ):
            self.assertIn(key, section, key)
            self.assertIs(section[key], False, key)


class TestSourceBodyReceptionRequestDeclared(
    SourceBodyReceptionRequestDeclarationAssertions, unittest.TestCase
):
    def setUp(self) -> None:
        self.request = declared_reception_request()
        self.request_before = copy.deepcopy(self.request)
        self.result = resolve(self.request)

    def test_successful_declared_result_shape_and_statement(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(self.result))
        self.assertEqual(DECLARED, self.result["outcome"])
        self.assertIsNone(self.result["block"]["block_code"])
        self.assertIsNone(self.result["block"]["block_reason"])
        self.assertEqual(0, self.result["source_body_reception_request_summary"]["failed_check_count"])
        self.assertGreater(self.result["source_body_reception_request_summary"]["passed_check_count"], 0)

        statement = self.result["declaration_statement"]
        self.assertIs(statement["source_body_reception_request_declared"], True)
        self.assertIs(statement["selected_source_body_surface_preserved"], True)
        self.assertIs(statement["selected_source_body_surface_remains_source"], True)
        self.assertIs(statement["receiving_context_declared"], True)
        self.assertIs(statement["receiving_context_remains_context_only"], True)
        self.assertIs(statement["reception_class_declared"], True)
        self.assertIs(statement["reception_class_supported"], True)
        self.assertIs(statement["reception_purpose_declared"], True)
        self.assertIs(statement["reception_limits_declared"], True)
        self.assertIs(statement["distributed_operation_closure_context_only"], True)
        self.assertIs(statement["terminal_summary_context_only"], True)
        self.assert_no_reception_or_capture(statement)
        self.assert_required_non_claims_false(self.result)
        self.assertIs(self.result["non_claims"]["source_body_reception_request_declared"], True)
        self.assertEqual(self.request_before, self.request)

    def test_metadata_and_declared_reception_question_are_bounded(self) -> None:
        metadata = self.result["source_body_reception_request_metadata"]
        for key in (
            "source_body_reception_request_result_id",
            "source_body_reception_request_result_type",
            "source_body_reception_request_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["source_body_reception_request_result_version"])
        self.assertEqual(
            "resolve_source_body_reception_request_declaration",
            metadata["resolver_module"],
        )

        question = self.result["declared_reception_question"]
        self.assertEqual(self.request["reception_request_id"], question["reception_request_id"])
        self.assertEqual(self.request["reception_question"], question["reception_question"])
        self.assertIs(question["declaration_is_not_reception_recognition"], True)
        self.assertIs(question["declaration_is_not_reception_authorization"], True)
        self.assertIs(question["declaration_is_not_adoption"], True)
        self.assertIs(question["declaration_is_not_authority"], True)
        self.assertIs(question["declaration_is_not_currentness"], True)
        self.assertIs(question["declaration_is_not_source_replacement"], True)

    def test_selected_source_body_surface_and_context_are_preserved(self) -> None:
        surface = self.result["selected_source_body_surface"]
        self.assertEqual("source-body-surface-001", surface["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", surface["selected_source_body_surface_type"])
        self.assertEqual(
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            surface["selected_source_body_surface_path"],
        )
        self.assertEqual(
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            surface["selected_source_body_surface_reference"],
        )
        self.assertEqual(self.request["source_body_identity_basis"], surface["source_body_identity_basis"])
        self.assertEqual(self.request["source_body_lineage_basis"], surface["source_body_lineage_basis"])
        self.assertIs(surface["selected_source_body_surface_preserved"], True)
        self.assertIs(surface["selected_source_body_surface_remains_source"], True)
        self.assertIs(surface["selected_source_body_surface_not_received"], True)
        self.assertIs(surface["selected_source_body_surface_not_adopted"], True)
        self.assertIs(surface["selected_source_body_surface_not_replaced"], True)
        self.assertIs(surface["selected_source_body_surface_not_validated_by_receiving_context"], True)
        self.assertIs(surface["selected_source_body_surface_not_invalidated_by_receiving_context"], True)
        self.assertIs(surface["distributed_operation_closure_context_only"], True)
        self.assertIs(surface["terminal_summary_context_only"], True)
        self.assertIs(
            surface["distributed_operation_closure_artifact_is_not_selected_source_body_surface_by_default"],
            True,
        )
        self.assertIs(surface["terminal_summary_is_not_selected_source_body_surface_by_default"], True)

        context = self.result["receiving_context"]
        self.assertEqual("receiving-context-001", context["receiving_context_id"])
        self.assertEqual(
            "bounded receiving context",
            context["receiving_context"]["receiving_context_name"],
        )
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", context["receiving_context_type"])
        self.assertIs(context["receiving_context_declared"], True)
        self.assertIs(context["receiving_context_remains_context_only"], True)
        self.assertIs(context["receiving_context_did_not_become_source"], True)
        self.assertIs(context["receiving_context_did_not_become_authority"], True)
        self.assertIs(context["receiving_context_did_not_become_current"], True)
        self.assertIs(context["receiving_context_did_not_validate_source"], True)
        self.assertIs(context["receiving_context_did_not_invalidate_source"], True)
        self.assertIs(context["receiving_context_did_not_create_adoption"], True)
        self.assertIs(context["receiving_context_did_not_create_operation_permission"], True)
        self.assertIs(context["receiving_context_did_not_open_publication_flow"], True)

    def test_reception_class_purpose_limits_checks_and_non_meaning(self) -> None:
        reception_class = self.result["reception_class"]
        self.assertEqual("REFERENCE_RECEPTION", reception_class["selected_reception_class"])
        self.assertIs(reception_class["reception_class_declared"], True)
        self.assertIs(reception_class["reception_class_supported"], True)
        self.assertEqual(set(resolver.SUPPORTED_RECEPTION_CLASSES), set(reception_class["supported_reception_classes"]))
        self.assertIs(reception_class["class_is_declaration_class_only"], True)
        self.assertIs(reception_class["class_does_not_recognize_reception"], True)
        self.assertIs(reception_class["class_does_not_authorize_reception"], True)
        self.assertIs(reception_class["derivative_reception_supported"], False)

        purpose = self.result["reception_purpose"]
        self.assertEqual(self.request["reception_purpose"], purpose["reception_purpose"])
        self.assertIs(purpose["reception_purpose_declared"], True)
        self.assertIs(purpose["purpose_is_not_permission"], True)

        limits = self.result["reception_limits"]
        self.assertEqual(self.request["reception_limits"], limits["reception_limits"])
        self.assertIs(limits["reception_limits_declared"], True)
        self.assertIs(limits["limits_preserve_no_recognition"], True)
        self.assertIs(limits["limits_preserve_no_authorization"], True)

        checks = self.result["declaration_checks"]
        self.assertGreaterEqual(len(checks), 35)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertIs(check["passed"], True, check["check_name"])
        check_names = {check["check_name"] for check in checks}
        for expected_name in (
            "reception request id declared",
            "reception question declared",
            "selected source-body surface declared",
            "selected source-body surface identifier declared",
            "selected source-body surface type declared",
            "selected source-body surface path/reference declared",
            "source-body identity basis declared",
            "source-body lineage basis declared",
            "receiving context declared",
            "receiving context type declared",
            "reception class supported",
            "reception purpose declared",
            "reception limits declared",
            "receiving context remains context only",
            "selected source-body surface remains source",
            "distributed-operation closure context remains context/evidence only",
            "terminal summary context remains context/evidence only",
            "declaration does not recognize reception",
            "declaration does not authorize reception",
            "declaration does not create adoption",
            "declaration does not create authority",
            "declaration does not create currentness",
            "declaration does not create standing",
            "declaration does not create standing propagation",
            "declaration does not create vessel relation",
            "declaration does not create derivative relation",
            "declaration does not create operation permission",
            "declaration does not replace source",
            "declaration does not validate source",
            "declaration does not invalidate source",
            "declaration does not create public readiness",
            "declaration does not claim final completion",
            "declaration does not authorize follow-on work",
            "declaration does not authorize continuation",
            "declaration does not open publication flow",
            "no mutation/replay/merge",
            "non-claims remain false",
        ):
            self.assertIn(expected_name, check_names)

        non_meaning = self.result["declaration_non_meaning"]
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
            self.assertIn(key, non_meaning, key)
            self.assertIs(non_meaning[key], True, key)

    def test_additional_basis_empty_open_items_and_summary(self) -> None:
        additional = self.result["additional_basis_required"]
        self.assertIs(additional["additional_basis_required"], False)
        self.assertEqual({}, additional["additional_basis_context"])
        self.assertIs(additional["additional_basis_scheduled"], False)
        self.assertIs(additional["additional_basis_authorized"], False)
        self.assertIs(additional["additional_basis_executed"], False)

        open_items = self.result["what_remains_open"]
        for key in (
            "source_body_reception_request_declaration_test",
            "source_body_reception_request_declaration_live_artifact",
            "source_body_identity_preservation_boundary",
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
        ):
            self.assertIn(key, open_items, key)
            self.assertIs(open_items[key], True, key)
        self.assertIs(open_items["open_means_not_scheduled"], True)
        self.assertIs(open_items["open_means_not_authorized"], True)
        self.assertIs(open_items["open_means_not_executed"], True)

        summary = resolver.build_source_body_reception_request_declaration_summary(self.result)
        self.assertEqual(DECLARED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(self.request["reception_request_id"], summary["reception_request_id"])
        self.assertEqual(self.request["reception_question"], summary["reception_question"])
        self.assertEqual("source-body-surface-001", summary["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", summary["selected_source_body_surface_type"])
        self.assertEqual(
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            summary["selected_source_body_surface_reference"],
        )
        self.assertEqual("receiving-context-001", summary["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", summary["receiving_context_type"])
        self.assertEqual("REFERENCE_RECEPTION", summary["reception_class"])
        self.assertEqual(self.request["reception_purpose"], summary["reception_purpose"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["request_declared"], True)
        self.assertIs(summary["not_sufficient"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["selected_source_body_surface_preserved"], True)
        self.assertIs(summary["selected_source_body_surface_remains_source"], True)
        self.assertIs(summary["receiving_context_declared"], True)
        self.assertIs(summary["receiving_context_remains_context_only"], True)
        self.assertIs(summary["reception_class_supported"], True)
        self.assertIs(summary["reception_purpose_declared"], True)
        self.assertIs(summary["reception_limits_declared"], True)
        self.assertIs(summary["closure_context_only_where_supplied"], True)
        self.assertIs(summary["terminal_summary_context_only_where_supplied"], True)
        self.assertIs(summary["no_reception_recognized"], True)
        self.assertIs(summary["no_reception_authorized"], True)
        self.assertIs(summary["no_adoption"], True)
        self.assertIs(summary["no_authority"], True)
        self.assertIs(summary["no_currentness"], True)
        self.assertIs(summary["no_standing"], True)
        self.assertIs(summary["no_vessel_relation"], True)
        self.assertIs(summary["no_derivative_relation"], True)
        self.assertIs(summary["no_operation_permission"], True)
        self.assertIs(summary["no_source_replacement"], True)
        self.assertIs(summary["no_source_validation"], True)
        self.assertIs(summary["no_source_invalidation"], True)
        self.assertIs(summary["no_public_readiness"], True)
        self.assertIs(summary["no_final_completion"], True)
        self.assertIs(summary["no_follow_on_work"], True)
        self.assert_required_non_claims_false({"non_claims": summary["key_non_claims"]})


class TestSourceBodyReceptionRequestDeclarationVariants(
    SourceBodyReceptionRequestDeclarationAssertions, unittest.TestCase
):
    def test_supported_reception_classes_declare_and_unsupported_classes_block(self) -> None:
        for reception_class in resolver.SUPPORTED_RECEPTION_CLASSES:
            with self.subTest(reception_class=reception_class):
                result = resolve(declared_reception_request(reception_class=reception_class))
                self.assertEqual(DECLARED, result["outcome"])
                self.assertEqual(reception_class, result["reception_class"]["selected_reception_class"])
                self.assertIs(result["reception_class"]["reception_class_supported"], True)

        for reception_class in ("DERIVATIVE_RECEPTION", "UNBOUNDED_RECEPTION"):
            with self.subTest(reception_class=reception_class):
                result = self.assert_block(
                    declared_reception_request(reception_class=reception_class),
                    "UNSUPPORTED_RECEPTION_CLASS",
                )
                self.assertIs(result["non_claims"]["derivative_relation_created"], False)
                self.assertIs(result["non_claims"]["vessel_relation_created"], False)
                self.assertIs(result["non_claims"]["adoption_created"], False)
                self.assertIs(result["non_claims"]["authority_created"], False)
                self.assertIs(result["non_claims"]["currentness_created"], False)
                self.assertIs(result["non_claims"]["standing_created"], False)

    def test_requires_additional_basis_preserves_missing_basis_without_authorizing_it(self) -> None:
        context = {
            "selected_source_body_surface_identity_too_generic": True,
            "source_body_lineage_basis_unclear": True,
            "receiving_context_too_vague": True,
            "receiving_context_type_unclear": True,
            "reception_purpose_too_broad": True,
            "reception_limits_incomplete": True,
            "non_claims_incomplete_but_not_flipped": True,
            "distributed_operation_closure_context_not_bounded_as_context_only": True,
            "terminal_summary_context_not_bounded_as_context_only": True,
        }
        request = declared_reception_request(
            requested_reception_declaration_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context=context,
        )
        request_before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, result["outcome"])
        self.assertEqual(context, result["additional_basis_required"]["additional_basis_context"])
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        self.assertIs(result["additional_basis_required"]["additional_basis_scheduled"], False)
        self.assertIs(result["additional_basis_required"]["additional_basis_authorized"], False)
        self.assertIs(result["additional_basis_required"]["additional_basis_executed"], False)
        self.assert_no_reception_or_capture(result["declaration_statement"])
        self.assertEqual(request_before, request)

    def test_not_sufficient_preserves_readable_basis_without_repair_or_capture(self) -> None:
        reason = "request cannot yet support later reception review without capture risk"
        request = declared_reception_request(
            requested_reception_declaration_outcome=NOT_SUFFICIENT,
            not_sufficient_reason=reason,
        )
        request_before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(NOT_SUFFICIENT, result["outcome"])
        self.assertEqual(reason, result["declaration_statement"]["not_sufficient_reason"])
        self.assertIs(result["non_claims"]["source_body_reception_request_declared"], False)
        self.assert_no_reception_or_capture(result["declaration_statement"])
        self.assertEqual(request_before, request)

    def test_request_builder_helper_builds_resolvable_declaration_request(self) -> None:
        surface = selected_source_body_surface()
        context = receiving_context()
        additional_basis = {"receiving_context_too_vague": True}
        not_sufficient_reason = "selected source-body surface ambiguous"
        request = resolver.build_declared_source_body_reception_request(
            reception_request_id="source-body-reception-request-built-001",
            reception_question="What source-body reception request has been declared for later review?",
            selected_source_body_surface=surface,
            receiving_context=context,
            reception_class="INSPECTION_RECEPTION",
            reception_purpose=reception_purpose(),
            reception_limits=reception_limits(),
            source_body_identity_basis=surface["source_body_identity_basis"],
            source_body_lineage_basis=surface["source_body_lineage_basis"],
            distributed_operation_closure_context=distributed_operation_closure_context(),
            terminal_summary_context=terminal_summary_context(),
            requested_reception_declaration_outcome=DECLARED,
            additional_basis_context=additional_basis,
            not_sufficient_reason=not_sufficient_reason,
        )

        self.assertEqual("source-body-reception-request-built-001", request["reception_request_id"])
        self.assertEqual(surface, request["selected_source_body_surface"])
        self.assertEqual(context, request["receiving_context"])
        self.assertEqual("INSPECTION_RECEPTION", request["reception_class"])
        self.assertEqual(surface["source_body_identity_basis"], request["source_body_identity_basis"])
        self.assertEqual(surface["source_body_lineage_basis"], request["source_body_lineage_basis"])
        self.assertEqual(additional_basis, request["additional_basis_context"])
        self.assertEqual(not_sufficient_reason, request["not_sufficient_reason"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolve(request)
        self.assertEqual(DECLARED, result["outcome"])
        self.assertEqual("INSPECTION_RECEPTION", result["reception_class"]["selected_reception_class"])

    def test_path_based_request_resolution(self) -> None:
        request = declared_reception_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            request_path = Path(temp_dir) / "declared_request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_source_body_reception_request_declaration_from_path(request_path)

        mapping_result = resolve(request)
        self.assertEqual(DECLARED, result["outcome"])
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertEqual(TOP_LEVEL_SECTIONS, set(mapping_result))
        self.assertEqual(str(request_path), result["declared_reception_question"]["declared_reception_request_path"])

    def test_write_behavior_with_explicit_and_default_output_paths(self) -> None:
        result = resolve(declared_reception_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "request_result.json"
            written = resolver.write_source_body_reception_request_declaration_result(
                result, explicit_path
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "request_declaration_root"
            future_boundary_root = Path(temp_dir) / "source_body_reception_boundary"
            closure_root = Path(temp_dir) / "distributed_operation_closure_boundary"
            with patch.object(resolver, "SOURCE_BODY_RECEPTION_REQUEST_DECLARATION_ROOT", root):
                first = resolver.write_source_body_reception_request_declaration_result(result)
                second = resolver.write_source_body_reception_request_declaration_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__source_body_reception_request_declaration_result.json"))
            self.assertTrue(second.name.endswith("__source_body_reception_request_declaration_result_001.json"))
            self.assertNotEqual(closure_root, first.parent)
            self.assertNotEqual(future_boundary_root, first.parent)

    def test_non_mutation_posture_and_additive_write(self) -> None:
        request = declared_reception_request()
        request_before = copy.deepcopy(request)
        surface_before = copy.deepcopy(request["selected_source_body_surface"])
        context_before = copy.deepcopy(request["receiving_context"])
        purpose_before = copy.deepcopy(request["reception_purpose"])
        limits_before = copy.deepcopy(request["reception_limits"])
        closure_before = copy.deepcopy(request["distributed_operation_closure_context"])
        terminal_before = copy.deepcopy(request["terminal_summary_context"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(DECLARED, first["outcome"])
        self.assertEqual(DECLARED, second["outcome"])
        self.assertEqual(request_before, request)
        self.assertEqual(surface_before, request["selected_source_body_surface"])
        self.assertEqual(context_before, request["receiving_context"])
        self.assertEqual(purpose_before, request["reception_purpose"])
        self.assertEqual(limits_before, request["reception_limits"])
        self.assertEqual(closure_before, request["distributed_operation_closure_context"])
        self.assertEqual(terminal_before, request["terminal_summary_context"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            selected_surface_artifact = temp_root / "selected_source_body_surface.json"
            closure_artifact = temp_root / "closure_artifact.json"
            terminal_summary = temp_root / "terminal_summary.md"
            upstream_artifact = temp_root / "upstream.json"
            selected_surface_artifact.write_text("selected-source", encoding="utf-8")
            closure_artifact.write_text("closure", encoding="utf-8")
            terminal_summary.write_text("terminal", encoding="utf-8")
            upstream_artifact.write_text("upstream", encoding="utf-8")
            before_contents = {
                path: path.read_text(encoding="utf-8")
                for path in (
                    selected_surface_artifact,
                    closure_artifact,
                    terminal_summary,
                    upstream_artifact,
                )
            }

            out_path = temp_root / "out" / "request_declaration_result.json"
            resolver.write_source_body_reception_request_declaration_result(first, out_path)

            for path, before in before_contents.items():
                self.assertEqual(before, path.read_text(encoding="utf-8"), str(path))


class TestSourceBodyReceptionRequestDeclarationBlocking(
    SourceBodyReceptionRequestDeclarationAssertions, unittest.TestCase
):
    def test_missing_and_malformed_requests_block(self) -> None:
        self.assert_block(None, "RECEPTION_REQUEST_ID_MISSING")
        self.assert_block(["not", "a", "mapping"], "DECLARED_RECEPTION_REQUEST_MALFORMED")

    def test_request_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            missing = temp_root / "missing.json"
            result = resolver.resolve_source_body_reception_request_declaration_from_path(missing)
            self.assertEqual(BLOCKED, result["outcome"])
            self.assertEqual("DECLARED_RECEPTION_REQUEST_UNREADABLE", result["block"]["block_code"])

            malformed = temp_root / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            result = resolver.resolve_source_body_reception_request_declaration_from_path(malformed)
            self.assertEqual(BLOCKED, result["outcome"])
            self.assertEqual("DECLARED_RECEPTION_REQUEST_MALFORMED", result["block"]["block_code"])

            array_json = temp_root / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            result = resolver.resolve_source_body_reception_request_declaration_from_path(array_json)
            self.assertEqual(BLOCKED, result["outcome"])
            self.assertEqual("DECLARED_RECEPTION_REQUEST_MALFORMED", result["block"]["block_code"])

    def test_missing_required_selected_basis_blocks_with_specific_codes(self) -> None:
        cases = (
            ("reception_request_id", "RECEPTION_REQUEST_ID_MISSING", lambda r: r.pop("reception_request_id")),
            ("reception_question", "RECEPTION_QUESTION_MISSING", lambda r: r.pop("reception_question")),
            (
                "selected_source_body_surface",
                "SELECTED_SOURCE_BODY_SURFACE_MISSING",
                lambda r: r.pop("selected_source_body_surface"),
            ),
            (
                "selected_source_body_surface_identifier",
                "SELECTED_SOURCE_BODY_SURFACE_IDENTIFIER_MISSING",
                lambda r: (
                    r.pop("selected_source_body_surface_identifier"),
                    r["selected_source_body_surface"].pop("selected_source_body_surface_identifier"),
                ),
            ),
            (
                "selected_source_body_surface_type",
                "SELECTED_SOURCE_BODY_SURFACE_TYPE_MISSING",
                lambda r: (
                    r.pop("selected_source_body_surface_type"),
                    r["selected_source_body_surface"].pop("selected_source_body_surface_type"),
                ),
            ),
            (
                "selected_source_body_surface_reference",
                "SELECTED_SOURCE_BODY_SURFACE_REFERENCE_MISSING",
                lambda r: (
                    r.pop("selected_source_body_surface_path"),
                    r.pop("selected_source_body_surface_reference"),
                    r["selected_source_body_surface"].pop("selected_source_body_surface_path"),
                    r["selected_source_body_surface"].pop("selected_source_body_surface_reference"),
                ),
            ),
            (
                "source_body_identity_basis",
                "SOURCE_BODY_IDENTITY_BASIS_MISSING",
                lambda r: (
                    r.pop("source_body_identity_basis"),
                    r["selected_source_body_surface"].pop("source_body_identity_basis"),
                ),
            ),
            (
                "source_body_lineage_basis",
                "SOURCE_BODY_LINEAGE_BASIS_MISSING",
                lambda r: (
                    r.pop("source_body_lineage_basis"),
                    r["selected_source_body_surface"].pop("source_body_lineage_basis"),
                ),
            ),
            ("receiving_context", "RECEIVING_CONTEXT_MISSING", lambda r: r.pop("receiving_context")),
            (
                "receiving_context_type",
                "RECEIVING_CONTEXT_TYPE_MISSING",
                lambda r: (
                    r.pop("receiving_context_type"),
                    r["receiving_context"].pop("receiving_context_type"),
                ),
            ),
            ("reception_class", "RECEPTION_CLASS_MISSING", lambda r: r.pop("reception_class")),
            ("reception_purpose", "RECEPTION_PURPOSE_MISSING", lambda r: r.pop("reception_purpose")),
            ("reception_limits", "RECEPTION_LIMITS_MISSING", lambda r: r.pop("reception_limits")),
        )
        for name, code, mutate in cases:
            with self.subTest(name=name):
                request = declared_reception_request()
                mutate(request)
                self.assert_block(request, code)

    def test_malformed_surface_and_receiving_context_block(self) -> None:
        self.assert_block(
            declared_reception_request(selected_source_body_surface=7),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        )
        self.assert_block(
            declared_reception_request(receiving_context=7),
            "RECEIVING_CONTEXT_MALFORMED",
        )

    def test_collapse_and_capture_flags_block_with_representative_codes(self) -> None:
        cases = (
            ("reception_recognized", "RECEPTION_DECLARATION_RECOGNIZES_RECEPTION"),
            ("reception_authorized", "RECEPTION_DECLARATION_AUTHORIZES_RECEPTION"),
            ("adoption_created", "RECEPTION_DECLARATION_CREATES_ADOPTION"),
            ("authority_created", "RECEPTION_DECLARATION_CREATES_AUTHORITY"),
            ("currentness_created", "RECEPTION_DECLARATION_CREATES_CURRENTNESS"),
            ("standing_created", "RECEPTION_DECLARATION_CREATES_STANDING"),
            ("standing_propagated", "RECEPTION_DECLARATION_CREATES_STANDING_PROPAGATION"),
            ("vessel_relation_created", "RECEPTION_DECLARATION_CREATES_VESSEL_RELATION"),
            ("derivative_relation_created", "RECEPTION_DECLARATION_CREATES_DERIVATIVE_RELATION"),
            ("operation_permission_created", "RECEPTION_DECLARATION_CREATES_OPERATION_PERMISSION"),
            ("source_replaced", "RECEPTION_DECLARATION_REPLACES_SOURCE"),
            ("source_validated_by_receiving_context", "RECEPTION_DECLARATION_VALIDATES_SOURCE"),
            ("source_invalidated_by_receiving_context", "RECEPTION_DECLARATION_INVALIDATES_SOURCE"),
            ("receiving_context_became_source", "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE"),
            ("receiving_context_became_authority", "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_AUTHORITY"),
            ("receiving_context_became_current", "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_CURRENT"),
            ("public_launch_readiness_created", "RECEPTION_DECLARATION_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "RECEPTION_DECLARATION_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "RECEPTION_DECLARATION_AUTHORIZES_FOLLOW_ON_WORK"),
            ("continuation_authorized", "RECEPTION_DECLARATION_SCHEDULES_CONTINUATION"),
            ("publication_flow_opened", "RECEPTION_DECLARATION_OPENS_PUBLICATION_FLOW"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = declared_reception_request()
                request["declared_non_claims"][flag] = True
                self.assert_block(request, code)

    def test_mutation_replay_or_merge_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                request = declared_reception_request()
                request["declared_non_claims"][flag] = True
                self.assert_block(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        request = declared_reception_request()
        request["declared_non_claims"].pop("reception_recognized")
        self.assert_block(request, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = declared_reception_request()
        flipped["declared_non_claims"]["source_received"] = True
        result = resolve(flipped)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertIn(
            result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "RECEPTION_DECLARATION_RECOGNIZES_RECEPTION"},
        )


if __name__ == "__main__":
    unittest.main()
