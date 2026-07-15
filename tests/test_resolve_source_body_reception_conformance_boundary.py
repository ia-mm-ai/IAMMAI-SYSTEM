"""Executable boundary tests for source-body reception conformance.

These tests prove that the resolver records reception-chain conformance only.
Conformance is not source receipt, not source received, not reception
authorization, not adoption, not authority, not currentness, not final
completion, and not closure.
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

import resolve_source_body_reception_conformance_boundary as resolver  # noqa: E402


PASSED = "SOURCE_BODY_RECEPTION_CONFORMANCE_PASSED"
NOT_PASSED = "SOURCE_BODY_RECEPTION_CONFORMANCE_NOT_PASSED"
REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_CONFORMANCE_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "SOURCE_BODY_RECEPTION_CONFORMANCE_REVIEW_BLOCKED"
RECEIPT_EXHAUSTION_RECORDED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_RECORDED"
RECOGNITION_RECORDED = "SOURCE_BODY_RECEPTION_RECOGNITION_RECORDED"
NON_CAPTURE_PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED"
ELIGIBLE = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"
ROLE_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
IDENTITY_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {PASSED, NOT_PASSED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_conformance_metadata",
    "declared_conformance_question",
    "selected_receipt_exhaustion_result",
    "selected_source_body_surface",
    "receiving_context",
    "conformance_basis",
    "conformance_limits",
    "conformance_scope",
    "conformance_checks",
    "conformance_statement",
    "conformance_non_meaning",
    "additional_basis_required",
    "not_passed_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_conformance_summary",
}

SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_CONFORMANCE_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
ALLOWED_PASSED_TRUE_FIELDS = tuple(resolver.ALLOWED_PASSED_TRUE_FIELDS)


def false_conformance_non_claims() -> dict[str, bool]:
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
        "source_receipt_recorded": False,
        "source_receipt_created": False,
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
    surface: dict[str, object],
    context: dict[str, object],
    request_declaration: dict[str, object],
) -> dict[str, object]:
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
            "reception_authorized": False,
            "source_received": False,
            "source_receipt_recorded": False,
        },
    }


def selected_receiving_context_role_result(
    identity: dict[str, object],
    surface: dict[str, object],
    context: dict[str, object],
    request_declaration: dict[str, object],
) -> dict[str, object]:
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
            "receiving_context_type": context["receiving_context_type"],
            "selected_receiving_context_role": role["receiving_context_role"],
            "receiving_context_role_class": role["receiving_context_role_class"],
            "receiving_context_role_limits": role["receiving_context_role_limits"],
        },
        "receiving_context_role_statement": {
            "receiving_context_role_preserved": True,
            "receiving_context_role_remains_bounded": True,
            "role_is_not_reception": True,
            "role_is_not_authorization": True,
            "role_is_not_source_receipt": True,
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
        },
        "selected_receiving_context_role_result": role_result,
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "eligibility_basis": {
            "selected_receiving_context_role_result": role_result,
            "selected_identity_preservation_result": identity,
            "selected_reception_request_declaration_result": request_declaration,
            "selected_source_body_surface": surface,
            "receiving_context": context,
            "receiving_context_type": context["receiving_context_type"],
            "selected_receiving_context_role": role["receiving_context_role"],
            "receiving_context_role_class": role["receiving_context_role_class"],
            "receiving_context_role_limits": role["receiving_context_role_limits"],
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
            "reception_authorized": False,
            "source_received": False,
        },
    }


def selected_non_capture_result() -> dict[str, object]:
    eligibility = selected_eligibility_result()
    role_result = eligibility["selected_receiving_context_role_result"]
    identity = role_result["selected_identity_preservation_result"]
    request_declaration = identity["selected_reception_request_declaration_result"]
    surface = eligibility["selected_source_body_surface"]
    context = eligibility["receiving_context"]
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
        },
        "selected_eligibility_result": {
            "raw_selected_eligibility_result": eligibility,
        },
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "non_capture_basis": {
            "selected_eligibility_result": eligibility,
            "selected_receiving_context_role_result": role_result,
            "selected_identity_preservation_result": identity,
            "selected_reception_request_declaration_result": request_declaration,
            "selected_source_body_surface": surface,
            "receiving_context": context,
        },
        "non_capture_statement": {
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
            "non_capture_passed_as_refusal_check_outcome_only": True,
            "non_adoption_passed_as_refusal_check_outcome_only": True,
            "non_currentness_passed_as_refusal_check_outcome_only": True,
            "reception_authorized": False,
            "source_received": False,
            "source_receipt_recorded": False,
            "source_receipt_created": False,
            "adoption_created": False,
            "authority_created": False,
            "currentness_created": False,
        },
    }


def selected_recognition_result() -> dict[str, object]:
    non_capture = selected_non_capture_result()
    eligibility = non_capture["non_capture_basis"]["selected_eligibility_result"]
    role_result = non_capture["non_capture_basis"]["selected_receiving_context_role_result"]
    identity = non_capture["non_capture_basis"]["selected_identity_preservation_result"]
    request_declaration = non_capture["non_capture_basis"][
        "selected_reception_request_declaration_result"
    ]
    surface = non_capture["selected_source_body_surface"]
    context = non_capture["receiving_context"]
    role = role_result["receiving_context_role"]
    recognition_basis = {
        "selected_non_capture_result": non_capture,
        "selected_eligibility_result": eligibility,
        "selected_receiving_context_role_result": role_result,
        "selected_identity_preservation_result": identity,
        "selected_reception_request_declaration_result": request_declaration,
        "selected_source_body_surface": surface,
        "source_body_identity_basis": surface["source_body_identity_basis"],
        "source_body_lineage_basis": surface["source_body_lineage_basis"],
        "receiving_context": context,
        "receiving_context_type": context["receiving_context_type"],
        "reception_class": "SOURCE_BODY_RECEPTION_REVIEW",
        "reception_purpose": "bounded reception-family accounting",
        "reception_limits": {"review_only": True},
        "selected_receiving_context_role": role["receiving_context_role"],
        "receiving_context_role_class": role["receiving_context_role_class"],
        "receiving_context_role_limits": role["receiving_context_role_limits"],
        "recognition_basis": {"recognition_basis_declared": True},
        "recognition_limits": {"recognition_limits_declared": True},
        "recognition_scope": [
            "RECOGNITION_REVIEW_ONLY",
            "RECOGNITION_IS_NOT_AUTHORIZATION",
            "RECOGNITION_IS_NOT_SOURCE_RECEIPT",
            "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY",
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
        ],
        "bounded_recognition_only": True,
        "recognized_for_later_reception_family_accounting_only": True,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_currentness": True,
    }
    return {
        "source_body_reception_recognition_metadata": {
            "source_body_reception_recognition_result_id": (
                "source_body_reception_recognition__recognition-001"
            ),
            "source_body_reception_recognition_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_reception_recognition_boundary",
        },
        "outcome": RECOGNITION_RECORDED,
        "source_body_reception_recognition_summary": {
            "outcome": RECOGNITION_RECORDED,
            "failed_check_count": 0,
        },
        "selected_non_capture_result": {
            "raw_selected_non_capture_result": non_capture,
        },
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "recognition_basis": recognition_basis,
        "recognition_limits": {
            "recognition_limits": {"recognition_limits_declared": True},
            "recognition_is_not_authorization": True,
            "recognition_is_not_source_receipt": True,
            "conformance_requires_separate_boundary": True,
            "closure_requires_separate_boundary": True,
        },
        "recognition_statement": {
            "source_body_reception_recognition_recorded": True,
            "reception_recognized": True,
            "selected_non_capture_result_preserved": True,
            "selected_non_capture_result_recorded": True,
            "selected_non_capture_result_failed_check_count_zero": True,
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
            "bounded_recognition_for_accounting_only": True,
            "recognition_is_not_authorization": True,
            "recognition_is_not_source_receipt": True,
            "reception_authorized": False,
            "source_received": False,
            "source_receipt_recorded": False,
            "source_receipt_created": False,
            "reception_closure_passed": False,
        },
        "non_claims": {
            **false_conformance_non_claims(),
            "receipt_exhaustion_passed": False,
            "reception_conformance_passed": False,
        },
    }


def receipt_exhaustion_basis() -> dict[str, object]:
    recognition = selected_recognition_result()
    basis = recognition["recognition_basis"]
    return {
        "selected_recognition_result": recognition,
        "selected_non_capture_result": basis["selected_non_capture_result"],
        "selected_eligibility_result": basis["selected_eligibility_result"],
        "selected_receiving_context_role_result": basis[
            "selected_receiving_context_role_result"
        ],
        "selected_identity_preservation_result": basis[
            "selected_identity_preservation_result"
        ],
        "selected_reception_request_declaration_result": basis[
            "selected_reception_request_declaration_result"
        ],
        "selected_source_body_surface": basis["selected_source_body_surface"],
        "source_body_identity_basis": basis["source_body_identity_basis"],
        "source_body_lineage_basis": basis["source_body_lineage_basis"],
        "receiving_context": basis["receiving_context"],
        "receiving_context_type": basis["receiving_context_type"],
        "reception_class": basis["reception_class"],
        "reception_purpose": basis["reception_purpose"],
        "reception_limits": basis["reception_limits"],
        "selected_receiving_context_role": basis["selected_receiving_context_role"],
        "receiving_context_role_class": basis["receiving_context_role_class"],
        "receiving_context_role_limits": basis["receiving_context_role_limits"],
        "recognition_basis": basis["recognition_basis"],
        "recognition_limits": recognition["recognition_limits"],
        "receipt_exhaustion_basis": {"receipt_exhaustion_basis_declared": True},
        "recognition_record_receipt_basis": {
            "recognition_record_receipt_basis_declared": True,
        },
        "recognition_record_exhaustion_basis": {
            "recognition_record_exhaustion_basis_declared": True,
        },
        "receipt_exhaustion_of_recognition_accounting_only": True,
        "recognition_record_receipt_only": True,
        "recognition_record_exhaustion_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "source_receipt_remains_uncreated": True,
        "receipt_exhaustion_is_not_authorization": True,
        "receipt_exhaustion_is_not_source_receipt": True,
        "receipt_exhaustion_is_not_conformance": True,
        "receipt_exhaustion_is_not_closure": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
    }


def recognition_record_receipt_basis() -> dict[str, object]:
    return {
        "recognition_record_receipt_basis_declared": True,
        "recognition_record_receipted_for_accounting_only": True,
        "recognized_reception_accounting_receipt_recorded_only": True,
        "source_receipt_not_recorded": True,
        "source_received": False,
        "reception_authorization": False,
        "receipt_is_not_source_receipt": True,
        "receipt_is_not_authorization": True,
        "receipt_is_not_adoption": True,
        "receipt_is_not_conformance": True,
        "receipt_is_not_closure": True,
    }


def recognition_record_exhaustion_basis() -> dict[str, object]:
    return {
        "recognition_record_exhaustion_basis_declared": True,
        "recognition_record_exhaustion_recorded_for_this_layer_only": True,
        "recognized_reception_accounting_exhausted_only": True,
        "exhaustion_is_not_closure": True,
        "exhaustion_is_not_final_completion": True,
        "exhaustion_is_not_conformance": True,
        "exhaustion_does_not_authorize_continuation": True,
        "exhaustion_does_not_authorize_follow_on_work": True,
    }


def selected_receipt_exhaustion_result() -> dict[str, object]:
    basis = receipt_exhaustion_basis()
    surface = basis["selected_source_body_surface"]
    context = basis["receiving_context"]
    return {
        "source_body_reception_receipt_exhaustion_metadata": {
            "source_body_reception_receipt_exhaustion_result_id": (
                "source_body_reception_receipt_exhaustion__receipt-001"
            ),
            "source_body_reception_receipt_exhaustion_result_version": "0.1.0",
            "resolver_module": (
                "resolve_source_body_reception_receipt_exhaustion_boundary"
            ),
        },
        "outcome": RECEIPT_EXHAUSTION_RECORDED,
        "source_body_reception_receipt_exhaustion_summary": {
            "outcome": RECEIPT_EXHAUSTION_RECORDED,
            "failed_check_count": 0,
        },
        "selected_recognition_result": {
            "raw_selected_recognition_result": basis["selected_recognition_result"],
        },
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "receipt_exhaustion_basis": basis,
        "recognition_record_receipt_basis": {
            "recognition_record_receipt_basis": recognition_record_receipt_basis(),
        },
        "recognition_record_exhaustion_basis": {
            "recognition_record_exhaustion_basis": recognition_record_exhaustion_basis(),
        },
        "receipt_exhaustion_statement": {
            "source_body_reception_receipt_exhaustion_recorded": True,
            "reception_recognition_receipt_recorded": True,
            "reception_recognition_exhaustion_recorded": True,
            "recognized_reception_accounting_receipt_recorded": True,
            "recognized_reception_accounting_exhausted": True,
            "source_body_reception_recognition_recorded": True,
            "reception_recognized": True,
            "selected_recognition_result_preserved": True,
            "selected_recognition_result_recorded": True,
            "selected_recognition_result_failed_check_count_zero": True,
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
            "recognition_bounded_for_accounting_only": True,
            "receipt_exhaustion_of_recognition_accounting_only": True,
            "recognition_record_receipt_only": True,
            "recognition_record_exhaustion_only": True,
            "receipt_exhaustion_is_not_source_receipt": True,
            "receipt_exhaustion_is_not_authorization": True,
            "receipt_exhaustion_does_not_receive_source": True,
            "receipt_exhaustion_does_not_create_source_receipt": True,
            "receipt_exhaustion_is_not_conformance": True,
            "receipt_exhaustion_is_not_closure": True,
            "conformance_requires_separate_boundary": True,
            "closure_requires_separate_boundary": True,
            **false_conformance_non_claims(),
        },
        "non_claims": false_conformance_non_claims(),
    }


def conformance_basis() -> dict[str, object]:
    receipt = selected_receipt_exhaustion_result()
    basis = receipt["receipt_exhaustion_basis"]
    return {
        "selected_receipt_exhaustion_result": receipt,
        "selected_recognition_result": basis["selected_recognition_result"],
        "selected_non_capture_result": basis["selected_non_capture_result"],
        "selected_eligibility_result": basis["selected_eligibility_result"],
        "selected_receiving_context_role_result": basis[
            "selected_receiving_context_role_result"
        ],
        "selected_identity_preservation_result": basis[
            "selected_identity_preservation_result"
        ],
        "selected_reception_request_declaration_result": basis[
            "selected_reception_request_declaration_result"
        ],
        "selected_source_body_surface": basis["selected_source_body_surface"],
        "source_body_identity_basis": basis["source_body_identity_basis"],
        "source_body_lineage_basis": basis["source_body_lineage_basis"],
        "receiving_context": basis["receiving_context"],
        "receiving_context_type": basis["receiving_context_type"],
        "reception_class": basis["reception_class"],
        "reception_purpose": basis["reception_purpose"],
        "reception_limits": basis["reception_limits"],
        "selected_receiving_context_role": basis["selected_receiving_context_role"],
        "receiving_context_role_class": basis["receiving_context_role_class"],
        "receiving_context_role_limits": basis["receiving_context_role_limits"],
        "recognition_basis": basis["recognition_basis"],
        "recognition_limits": basis["recognition_limits"],
        "receipt_exhaustion_basis": basis["receipt_exhaustion_basis"],
        "recognition_record_receipt_basis": recognition_record_receipt_basis(),
        "recognition_record_exhaustion_basis": recognition_record_exhaustion_basis(),
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
        "conformance_is_not_adoption": True,
        "conformance_is_not_authority": True,
        "conformance_is_not_currentness": True,
        "conformance_is_not_validation": True,
        "conformance_is_not_invalidation": True,
        "conformance_is_not_operation_permission": True,
        "conformance_is_not_publication_flow": True,
        "conformance_is_not_closure": True,
        "closure_requires_separate_boundary": True,
    }


def declared_conformance_request(**overrides: object) -> dict[str, object]:
    receipt = overrides.pop(
        "selected_receipt_exhaustion_result",
        selected_receipt_exhaustion_result(),
    )
    request = {
        "conformance_request_id": "conformance-request-001",
        "conformance_question": (
            "Did the recorded source-body reception boundary chain conform to "
            "its own prior constraints?"
        ),
        "conformance_intent": "RECORD_SOURCE_BODY_RECEPTION_CONFORMANCE",
        "selected_receipt_exhaustion_result": receipt,
        "selected_receipt_exhaustion_result_id": (
            "source_body_reception_receipt_exhaustion__receipt-001"
        ),
        "selected_receipt_exhaustion_result_outcome": RECEIPT_EXHAUSTION_RECORDED,
        "conformance_basis": conformance_basis(),
        "conformance_limits": conformance_limits(),
        "conformance_scope": list(SUPPORTED_SCOPE),
        "requested_conformance_outcome": PASSED,
        "declared_non_claims": false_conformance_non_claims(),
    }
    request.update(overrides)
    return request


def remove_key_recursively(value: object, key_to_remove: str) -> object:
    if isinstance(value, dict):
        return {
            key: remove_key_recursively(child, key_to_remove)
            for key, child in value.items()
            if key != key_to_remove
        }
    if isinstance(value, list):
        return [remove_key_recursively(child, key_to_remove) for child in value]
    return value


def resolved(request: dict[str, object] | None = None) -> dict[str, object]:
    return resolver.resolve_source_body_reception_conformance_boundary(
        declared_conformance_request=request or declared_conformance_request()
    )


class SourceBodyReceptionConformanceBoundaryTests(unittest.TestCase):
    def assert_block_code(self, result: dict[str, object], code: str) -> None:
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        self.assertFalse(
            result["conformance_statement"]["source_body_reception_conformance_passed"]
        )

    def assert_false_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def test_successful_conformance_passed_result(self) -> None:
        request = declared_conformance_request()
        result = resolved(request)

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertEqual(PASSED, result["outcome"])
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["source_body_reception_conformance_summary"]["failed_check_count"])

        statement = result["conformance_statement"]
        for key in ALLOWED_PASSED_TRUE_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in (
            "selected_receipt_exhaustion_result_preserved",
            "selected_receipt_exhaustion_result_recorded",
            "selected_receipt_exhaustion_result_failed_check_count_zero",
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
            "reception_chain_conformance_only",
            "request_declaration_remained_declaration_only",
            "identity_preservation_preserved_source_identity_only",
            "receiving_context_role_remained_context_role_only",
            "eligibility_admissibility_remained_review_readiness_only",
            "non_capture_remained_refusal_check_outcome_only",
            "recognition_remained_bounded_accounting_recognition_only",
            "receipt_exhaustion_remained_recognition_record_accounting_only",
            "conformance_is_not_authorization",
            "conformance_is_not_source_receipt",
            "conformance_does_not_receive_source",
            "conformance_does_not_create_source_receipt",
            "conformance_is_not_closure",
            "closure_requires_separate_boundary",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_false_non_claims(result)

    def test_metadata_declared_question_selected_receipt_surface_and_context(self) -> None:
        result = resolved()
        metadata = result["source_body_reception_conformance_metadata"]
        for key in (
            "source_body_reception_conformance_result_id",
            "source_body_reception_conformance_result_type",
            "source_body_reception_conformance_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["source_body_reception_conformance_result_version"])
        self.assertEqual(
            "resolve_source_body_reception_conformance_boundary",
            metadata["resolver_module"],
        )

        question = result["declared_conformance_question"]
        self.assertEqual("conformance-request-001", question["conformance_request_id"])
        self.assertIn("conform", question["conformance_question"])
        self.assertEqual("RECORD_SOURCE_BODY_RECEPTION_CONFORMANCE", question["conformance_intent"])
        self.assertEqual(RECEIPT_EXHAUSTION_RECORDED, question["selected_receipt_exhaustion_result_outcome"])
        self.assertEqual("source-body-surface-001", question["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", question["selected_source_body_surface_type"])
        self.assertEqual("receiving-context-001", question["receiving_context_id"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", question["receiving_context_type"])
        self.assertEqual("SOURCE_BODY_RECEPTION_REVIEW", question["reception_class"])
        self.assertEqual("bounded reception-family accounting", question["reception_purpose"])
        self.assertIs(question["conformance_is_not_authorization"], True)
        self.assertIs(question["conformance_is_not_source_receipt"], True)
        self.assertIs(question["conformance_does_not_decide_closure"], True)
        self.assertIs(result["conformance_statement"]["closure_requires_separate_boundary"], True)

        selected = result["selected_receipt_exhaustion_result"]
        self.assertEqual(RECEIPT_EXHAUSTION_RECORDED, selected["selected_receipt_exhaustion_result_outcome"])
        self.assertIsNone(selected["selected_receipt_exhaustion_result_path"])
        for key in (
            "selected_receipt_exhaustion_outcome_is_recorded",
            "selected_receipt_exhaustion_result_failed_check_count_zero",
            "selected_receipt_exhaustion_result_preserved",
            "selected_receipt_exhaustion_result_recorded",
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
            "source_body_reception_recognition_recorded",
            "source_body_reception_receipt_exhaustion_recorded",
            "receipt_exhaustion_recorded",
            "receipt_exhaustion_remained_recognition_accounting_only",
            "receipt_exhaustion_did_not_authorize_reception",
            "receipt_exhaustion_did_not_receive_source",
            "receipt_exhaustion_did_not_record_source_receipt",
            "receipt_exhaustion_did_not_create_source_receipt",
            "receipt_exhaustion_did_not_claim_conformance",
            "receipt_exhaustion_did_not_claim_closure",
        ):
            self.assertIs(selected[key], True, key)

        surface = result["selected_source_body_surface"]
        self.assertEqual("source-body-surface-001", surface["selected_source_body_surface_identifier"])
        self.assertEqual("REFERENCE_SOURCE_BODY_SURFACE", surface["selected_source_body_surface_type"])
        self.assertEqual(
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            surface["selected_source_body_surface_path"],
        )
        for key in (
            "source_body_identity_basis",
            "source_body_lineage_basis",
        ):
            self.assertTrue(surface[key], key)
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
        self.assertEqual("receiving-context-001", context["receiving_context_id"])
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
            self.assertIs(context[key], True, key)

    def test_conformance_basis_limits_and_scope(self) -> None:
        result = resolved()
        basis = result["conformance_basis"]
        for key in (
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
            "recognition_basis",
            "recognition_limits",
            "receipt_exhaustion_basis",
            "recognition_record_receipt_basis",
            "recognition_record_exhaustion_basis",
            "conformance_basis",
        ):
            self.assertTrue(basis[key], key)
        for key in (
            "reception_chain_conformance_only",
            "request_declaration_remained_declaration_only",
            "identity_preservation_preserved_source_identity_only",
            "receiving_context_role_remained_context_role_only",
            "eligibility_admissibility_remained_review_readiness_only",
            "non_capture_remained_refusal_check_outcome_only",
            "recognition_remained_bounded_accounting_recognition_only",
            "receipt_exhaustion_remained_recognition_record_accounting_only",
            "source_remains_unreceived",
            "source_receipt_remains_unrecorded",
            "source_receipt_remains_uncreated",
            "conformance_is_not_authorization",
            "conformance_is_not_source_receipt",
            "conformance_is_not_closure",
            "closure_requires_separate_boundary",
        ):
            self.assertIs(basis[key], True, key)

        limits = result["conformance_limits"]
        self.assertTrue(limits["conformance_limits"]["conformance_limits_declared"])
        for key in (
            "reception_chain_conformance_only",
            "conformance_is_not_authorization",
            "conformance_is_not_source_receipt",
            "conformance_does_not_receive_source",
            "conformance_does_not_create_source_receipt",
            "conformance_is_not_adoption",
            "conformance_is_not_authority",
            "conformance_is_not_currentness",
            "conformance_is_not_validation",
            "conformance_is_not_invalidation",
            "conformance_is_not_operation_permission",
            "conformance_is_not_publication_flow",
            "conformance_is_not_closure",
            "closure_requires_separate_boundary",
        ):
            self.assertIs(limits[key], True, key)

        scope = result["conformance_scope"]
        self.assertEqual(set(SUPPORTED_SCOPE), set(scope["selected_conformance_scope_values"]))
        self.assertTrue(scope["all_selected_scope_values_supported"])
        self.assertEqual([], scope["unsupported_conformance_scope_values"])
        for key in (
            "reception_chain_conformance_only",
            "conformance_is_not_authorization",
            "conformance_is_not_source_receipt",
            "conformance_does_not_receive_source",
            "conformance_does_not_create_source_receipt",
            "conformance_is_not_adoption",
            "conformance_is_not_authority",
            "conformance_is_not_currentness",
            "conformance_is_not_validation",
            "conformance_is_not_invalidation",
            "conformance_is_not_operation_permission",
            "conformance_is_not_publication_flow",
            "conformance_is_not_closure",
            "closure_requires_separate_boundary",
        ):
            self.assertIs(scope[key], True, key)

    def test_supported_scope_values_and_unsupported_scope_blocks(self) -> None:
        for scope_value in SUPPORTED_SCOPE:
            with self.subTest(scope_value=scope_value):
                request = declared_conformance_request(conformance_scope=[scope_value])
                self.assertEqual(PASSED, resolved(request)["outcome"])

        result = resolved(
            declared_conformance_request(conformance_scope=["UNSUPPORTED_SCOPE"])
        )
        self.assert_block_code(result, "UNSUPPORTED_CONFORMANCE_SCOPE")

    def test_conformance_checks_records(self) -> None:
        result = resolved()
        checks = result["conformance_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue(
                "block_code" in check or "failure_code" in check,
                check,
            )
            self.assertIs(check["passed"], True, check["check_name"])
        self.assertEqual(0, result["source_body_reception_conformance_summary"]["failed_check_count"])

        check_names = {check["check_name"] for check in checks}
        expected_names = {
            "conformance_question_declared",
            "conformance_intent_supported",
            "selected_receipt_exhaustion_result_present",
            "selected_receipt_exhaustion_outcome_declared",
            "selected_receipt_exhaustion_outcome_recorded",
            "selected_receipt_exhaustion_failed_check_count_zero",
            "selected_recognition_result_preserved",
            "selected_non_capture_result_preserved",
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
            "recognition_was_recorded",
            "receipt_exhaustion_was_recorded",
            "receipt_exhaustion_recognition_accounting_only",
            "source_unreceived",
            "source_receipt_unrecorded",
            "source_receipt_uncreated",
            "conformance_basis_declared",
            "conformance_limits_declared",
            "conformance_scope_supported",
            "conformance_is_not_authorization",
            "conformance_is_not_source_receipt",
            "conformance_does_not_receive_source",
            "conformance_does_not_create_source_receipt",
            "conformance_does_not_create_adoption",
            "conformance_does_not_create_authority",
            "conformance_does_not_create_currentness",
            "conformance_does_not_validate_source",
            "conformance_does_not_invalidate_source",
            "conformance_does_not_replace_source",
            "conformance_does_not_create_operation_permission",
            "conformance_does_not_create_governance",
            "conformance_does_not_open_publication_flow",
            "conformance_does_not_create_public_readiness",
            "conformance_does_not_claim_final_completion",
            "conformance_does_not_authorize_continuation",
            "conformance_does_not_authorize_follow_on_work",
            "conformance_does_not_claim_closure",
            "closure_remains_future_work",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_names.issubset(check_names))

    def test_non_meaning_additional_basis_not_passed_and_open_items(self) -> None:
        result = resolved()
        non_meaning = result["conformance_non_meaning"]
        for meaning in (
            "reception_authorized",
            "source_received",
            "source_receipt_recorded",
            "source_receipt_created",
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
            "closure_recorded",
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
        ):
            self.assertIs(non_meaning[f"does_not_mean_{meaning}"], True, meaning)
        self.assertFalse(result["additional_basis_required"]["additional_basis_required"])
        self.assertTrue(result["additional_basis_required"]["missing_basis_is_not_scheduled"])
        self.assertTrue(result["additional_basis_required"]["missing_basis_is_not_authorized"])
        self.assertTrue(result["additional_basis_required"]["missing_basis_is_not_executed"])
        self.assertFalse(result["not_passed_basis"]["not_passed"])

        open_section = result["what_remains_open"]
        for item in (
            "source-body reception conformance test",
            "source-body reception conformance live artifact",
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

        additional_context = {
            "reason": "conformance basis too generic",
            "missing_basis": ["conformance/closure distinction unclear"],
        }
        additional_result = resolved(
            declared_conformance_request(
                requested_conformance_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, additional_result["outcome"])
        self.assertEqual(
            additional_context,
            additional_result["additional_basis_required"]["additional_basis_context"],
        )
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_is_not_scheduled"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_is_not_authorized"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_is_not_executed"])
        for key in ALLOWED_PASSED_TRUE_FIELDS:
            self.assertIs(additional_result["conformance_statement"][key], False)
        self.assert_false_non_claims(additional_result)

        not_passed_basis = {
            "reason": "conformance basis cannot be bounded",
            "not_passed_does_not_authorize_repair": True,
        }
        not_passed_result = resolved(
            declared_conformance_request(
                requested_conformance_outcome=NOT_PASSED,
                not_passed_basis=not_passed_basis,
            )
        )
        self.assertEqual(NOT_PASSED, not_passed_result["outcome"])
        self.assertEqual(
            not_passed_basis,
            not_passed_result["not_passed_basis"]["not_passed_basis"],
        )
        for key in (
            "not_passed_does_not_mutate",
            "not_passed_does_not_repair",
            "not_passed_does_not_authorize",
            "not_passed_does_not_receive",
            "not_passed_does_not_record_source_receipt",
            "not_passed_does_not_create_source_receipt",
            "not_passed_does_not_replace",
            "not_passed_does_not_validate",
            "not_passed_does_not_invalidate",
            "not_passed_does_not_create_currentness",
            "not_passed_does_not_claim_closure",
        ):
            self.assertIs(not_passed_result["not_passed_basis"][key], True, key)
        for key in ALLOWED_PASSED_TRUE_FIELDS:
            self.assertIs(not_passed_result["conformance_statement"][key], False)
        self.assert_false_non_claims(not_passed_result)

    def test_summary_helper_and_request_builder(self) -> None:
        receipt = selected_receipt_exhaustion_result()
        request = resolver.build_declared_source_body_reception_conformance_request(
            "builder-conformance-request-001",
            "Did the chain conform?",
            receipt,
            {"conformance_basis_declared": True},
            {"conformance_limits_declared": True},
            list(SUPPORTED_SCOPE),
            selected_receipt_exhaustion_result_id="receipt-id-from-builder",
            selected_receipt_exhaustion_result_outcome=RECEIPT_EXHAUSTION_RECORDED,
            additional_basis_context={"reason": "closure dependency unclear"},
            not_passed_basis={"reason": "recorded chain cannot be shown"},
        )
        self.assertEqual("builder-conformance-request-001", request["conformance_request_id"])
        self.assertEqual("Did the chain conform?", request["conformance_question"])
        self.assertEqual(receipt, request["selected_receipt_exhaustion_result"])
        self.assertEqual({"conformance_basis_declared": True}, request["conformance_basis"])
        self.assertEqual({"conformance_limits_declared": True}, request["conformance_limits"])
        self.assertEqual(list(SUPPORTED_SCOPE), request["conformance_scope"])
        self.assertEqual("receipt-id-from-builder", request["selected_receipt_exhaustion_result_id"])
        self.assertEqual(RECEIPT_EXHAUSTION_RECORDED, request["selected_receipt_exhaustion_result_outcome"])
        self.assertEqual(PASSED, request["requested_conformance_outcome"])
        self.assertNotIn("source_body_reception_conformance_recorded", request)
        self.assertNotIn("source_body_reception_conformance_passed", request)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolved(request)
        self.assertEqual(PASSED, result["outcome"])
        summary = resolver.build_source_body_reception_conformance_summary(result)
        self.assertEqual(PASSED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual("builder-conformance-request-001", summary["conformance_request_id"])
        self.assertEqual("Did the chain conform?", summary["conformance_question"])
        self.assertEqual("RECORD_SOURCE_BODY_RECEPTION_CONFORMANCE", summary["conformance_intent"])
        self.assertEqual("receipt-id-from-builder", summary["selected_receipt_exhaustion_result_id"])
        self.assertEqual(RECEIPT_EXHAUSTION_RECORDED, summary["selected_receipt_exhaustion_result_outcome"])
        self.assertEqual("source-body-surface-001", summary["selected_source_body_surface_identifier"])
        self.assertEqual("PRESENT_EXECUTION_CONTEXT", summary["receiving_context_type"])
        self.assertEqual(0, summary["failed_check_count"])
        for key in (
            "conformance_recorded",
            "conformance_passed",
            "reception_boundary_chain_conformance_passed",
            "reception_family_conformance_passed",
            "selected_receipt_exhaustion_result_preserved",
            "selected_receipt_exhaustion_result_recorded",
            "selected_receipt_exhaustion_result_failed_check_count_zero",
            "selected_recognition_result_preserved",
            "selected_non_capture_result_preserved",
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
            "reception_chain_conformance_only",
            "request_declaration_remained_declaration_only",
            "identity_preservation_preserved_source_identity_only",
            "receiving_context_role_remained_context_role_only",
            "eligibility_admissibility_review_readiness_only",
            "non_capture_refusal_check_only",
            "recognition_bounded_accounting_only",
            "receipt_exhaustion_recognition_record_accounting_only",
            "conformance_not_authorization",
            "conformance_not_source_receipt",
            "conformance_not_closure",
            "no_source_received",
            "no_source_receipt_recorded",
            "no_source_receipt_created",
            "closure_future",
            "no_adoption_authority_currentness_standing",
            "no_vessel_derivative_relation",
            "no_operation_permission_governance_publication_flow",
            "no_public_readiness_final_completion_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        self.assertEqual(result["non_claims"], summary["key_non_claims"])

    def test_path_based_resolution_and_write_helpers(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            receipt_path = temp / "selected_receipt_exhaustion.json"
            receipt_payload = selected_receipt_exhaustion_result()
            receipt_path.write_text(json.dumps(receipt_payload), encoding="utf-8")

            request = declared_conformance_request(
                selected_receipt_exhaustion_result_path=str(receipt_path)
            )
            request.pop("selected_receipt_exhaustion_result")
            result = resolved(request)
            self.assertEqual(PASSED, result["outcome"])
            self.assertEqual(
                str(receipt_path),
                result["selected_receipt_exhaustion_result"][
                    "selected_receipt_exhaustion_result_path"
                ],
            )
            self.assertEqual(
                RECEIPT_EXHAUSTION_RECORDED,
                result["selected_receipt_exhaustion_result"][
                    "selected_receipt_exhaustion_result_outcome"
                ],
            )

            request_path = temp / "declared_conformance_request.json"
            request_path.write_text(json.dumps(declared_conformance_request()), encoding="utf-8")
            path_result = resolver.resolve_source_body_reception_conformance_boundary_from_path(
                request_path
            )
            self.assertEqual(PASSED, path_result["outcome"])
            self.assertEqual(TOP_LEVEL_SECTIONS, set(path_result))
            self.assertEqual(
                str(request_path),
                path_result["declared_conformance_question"][
                    "declared_conformance_request_path"
                ],
            )

            output_path = temp / "nested" / "conformance_result.json"
            written = resolver.write_source_body_reception_conformance_result(
                result, output_path
            )
            self.assertEqual(output_path, written)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_CONFORMANCE_BOUNDARY_ROOT",
                temp / "conformance_root",
            ):
                first = resolver.write_source_body_reception_conformance_result(result)
                second = resolver.write_source_body_reception_conformance_result(result)
            self.assertTrue(str(first).startswith(str(temp / "conformance_root")))
            self.assertNotEqual(first, second)
            self.assertIn("__source_body_reception_conformance_result", first.name)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertNotIn("receipt_exhaustion_boundary", str(first))
            self.assertNotIn("closure_boundary", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_conformance_request()
        original_request = copy.deepcopy(request)
        original_receipt = copy.deepcopy(request["selected_receipt_exhaustion_result"])
        original_basis = copy.deepcopy(request["conformance_basis"])
        original_limits = copy.deepcopy(request["conformance_limits"])
        original_scope = copy.deepcopy(request["conformance_scope"])

        first = resolved(request)
        second = resolved(request)

        self.assertEqual(original_request, request)
        self.assertEqual(original_receipt, request["selected_receipt_exhaustion_result"])
        self.assertEqual(original_basis, request["conformance_basis"])
        self.assertEqual(original_limits, request["conformance_limits"])
        self.assertEqual(original_scope, request["conformance_scope"])
        self.assertEqual(PASSED, first["outcome"])
        self.assertEqual(PASSED, second["outcome"])

        receipt = request["selected_receipt_exhaustion_result"]
        receipt_basis = receipt["receipt_exhaustion_basis"]
        for key in (
            "selected_recognition_result",
            "selected_non_capture_result",
            "selected_eligibility_result",
            "selected_receiving_context_role_result",
            "selected_identity_preservation_result",
            "selected_reception_request_declaration_result",
            "selected_source_body_surface",
            "receiving_context",
        ):
            self.assertEqual(original_receipt["receipt_exhaustion_basis"][key], receipt_basis[key])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            receipt_path = temp / "upstream_receipt.json"
            receipt_path.write_text(json.dumps(original_receipt), encoding="utf-8")
            before = receipt_path.read_text(encoding="utf-8")
            request_from_path = declared_conformance_request(
                selected_receipt_exhaustion_result_path=str(receipt_path)
            )
            request_from_path.pop("selected_receipt_exhaustion_result")
            result = resolved(request_from_path)
            resolver.write_source_body_reception_conformance_result(
                result, temp / "conformance.json"
            )
            self.assertEqual(before, receipt_path.read_text(encoding="utf-8"))

    def test_explicit_missing_and_malformed_request_blocks(self) -> None:
        explicit = resolved(
            declared_conformance_request(
                conformance_intent="BLOCK_SOURCE_BODY_RECEPTION_CONFORMANCE_REVIEW"
            )
        )
        self.assert_block_code(explicit, "CONFORMANCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED")

        missing = resolver.resolve_source_body_reception_conformance_boundary()
        self.assert_block_code(missing, "CONFORMANCE_QUESTION_UNDECLARED")

        malformed = resolver.resolve_source_body_reception_conformance_boundary(
            declared_conformance_request=["not", "a", "mapping"]
        )
        self.assert_block_code(malformed, "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

    def test_request_and_selected_path_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            missing_request = temp / "missing.json"
            result = resolver.resolve_source_body_reception_conformance_boundary_from_path(
                missing_request
            )
            self.assert_block_code(result, "DECLARED_CONFORMANCE_REQUEST_UNREADABLE")

            malformed_request = temp / "malformed_request.json"
            malformed_request.write_text("{not json", encoding="utf-8")
            result = resolver.resolve_source_body_reception_conformance_boundary_from_path(
                malformed_request
            )
            self.assert_block_code(result, "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

            array_request = temp / "array_request.json"
            array_request.write_text("[]", encoding="utf-8")
            result = resolver.resolve_source_body_reception_conformance_boundary_from_path(
                array_request
            )
            self.assert_block_code(result, "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

            request = declared_conformance_request(
                selected_receipt_exhaustion_result_path=str(temp / "missing_receipt.json")
            )
            request.pop("selected_receipt_exhaustion_result")
            self.assert_block_code(resolved(request), "RECEIPT_EXHAUSTION_RESULT_UNREADABLE")

            malformed_receipt = temp / "malformed_receipt.json"
            malformed_receipt.write_text("{not json", encoding="utf-8")
            request["selected_receipt_exhaustion_result_path"] = str(malformed_receipt)
            self.assert_block_code(resolved(request), "RECEIPT_EXHAUSTION_RESULT_MALFORMED")

            array_receipt = temp / "array_receipt.json"
            array_receipt.write_text("[]", encoding="utf-8")
            request["selected_receipt_exhaustion_result_path"] = str(array_receipt)
            self.assert_block_code(resolved(request), "RECEIPT_EXHAUSTION_RESULT_MALFORMED")

    def test_selected_receipt_exhaustion_result_issue_blocks(self) -> None:
        receipt = selected_receipt_exhaustion_result()
        receipt.pop("outcome")
        receipt["source_body_reception_receipt_exhaustion_summary"].pop("outcome")
        request = declared_conformance_request(
            selected_receipt_exhaustion_result=receipt,
            selected_receipt_exhaustion_result_outcome=None,
            expected_selected_receipt_exhaustion_outcome=None,
        )
        request.pop("selected_receipt_exhaustion_result_outcome")
        self.assert_block_code(resolved(request), "RECEIPT_EXHAUSTION_RESULT_OUTCOME_MISSING")

        receipt = selected_receipt_exhaustion_result()
        receipt["outcome"] = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_NOT_RECORDED"
        receipt["source_body_reception_receipt_exhaustion_summary"]["outcome"] = (
            "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_NOT_RECORDED"
        )
        request = declared_conformance_request(selected_receipt_exhaustion_result=receipt)
        request.pop("selected_receipt_exhaustion_result_outcome")
        self.assert_block_code(resolved(request), "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED")

        receipt = selected_receipt_exhaustion_result()
        receipt["source_body_reception_receipt_exhaustion_summary"]["failed_check_count"] = 1
        self.assert_block_code(
            resolved(declared_conformance_request(selected_receipt_exhaustion_result=receipt)),
            "RECEIPT_EXHAUSTION_RESULT_HAS_FAILED_CHECKS",
        )

    def test_missing_required_selected_basis_blocks(self) -> None:
        cases = (
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
            ("receiving_context_type", "RECEIVING_CONTEXT_TYPE_MISSING"),
            ("reception_class", "RECEPTION_CLASS_MISSING"),
            ("reception_purpose", "RECEPTION_PURPOSE_MISSING"),
            ("reception_limits", "RECEPTION_LIMITS_MISSING"),
        )
        for missing_key, block_code in cases:
            with self.subTest(missing_key=missing_key):
                receipt = remove_key_recursively(
                    selected_receipt_exhaustion_result(),
                    missing_key,
                )
                request = declared_conformance_request(
                    selected_receipt_exhaustion_result=receipt
                )
                if missing_key in {
                    "receiving_context_type",
                    "reception_class",
                    "reception_purpose",
                    "reception_limits",
                }:
                    request = remove_key_recursively(request, missing_key)
                self.assert_block_code(resolved(request), block_code)

        request = declared_conformance_request()
        request.pop("conformance_basis")
        self.assert_block_code(resolved(request), "CONFORMANCE_BASIS_MISSING")

        request = declared_conformance_request()
        request.pop("conformance_limits")
        self.assert_block_code(resolved(request), "CONFORMANCE_LIMITS_MISSING")

    def test_malformed_surface_and_context_blocks(self) -> None:
        receipt = selected_receipt_exhaustion_result()
        receipt["receipt_exhaustion_basis"]["selected_source_body_surface"] = "malformed"
        receipt["selected_source_body_surface"] = "malformed"
        request = declared_conformance_request(selected_receipt_exhaustion_result=receipt)
        self.assert_block_code(resolved(request), "SELECTED_SOURCE_BODY_SURFACE_MALFORMED")

        receipt = selected_receipt_exhaustion_result()
        receipt["receipt_exhaustion_basis"]["receiving_context"] = "malformed"
        receipt["receiving_context"] = "malformed"
        request = declared_conformance_request(selected_receipt_exhaustion_result=receipt)
        self.assert_block_code(resolved(request), "RECEIVING_CONTEXT_MALFORMED")

    def test_conformance_overreach_blocks(self) -> None:
        cases = (
            ("reception_authorized", "CONFORMANCE_AUTHORIZES_RECEPTION"),
            ("source_received", "CONFORMANCE_RECEIVES_SOURCE"),
            ("source_receipt_recorded", "CONFORMANCE_RECORDS_SOURCE_RECEIPT"),
            ("source_receipt_created", "CONFORMANCE_CREATES_SOURCE_RECEIPT"),
            ("receiving_context_governance_created", "CONFORMANCE_CREATES_GOVERNANCE"),
            ("receiving_context_became_source", "CONFORMANCE_TREATS_CONTEXT_AS_SOURCE"),
            ("receiving_context_became_authority", "CONFORMANCE_TREATS_CONTEXT_AS_AUTHORITY"),
            ("receiving_context_became_current", "CONFORMANCE_TREATS_CONTEXT_AS_CURRENT"),
            ("receiving_context_became_receiver", "CONFORMANCE_TREATS_CONTEXT_AS_RECEIVER"),
            ("receiving_context_became_adopter", "CONFORMANCE_TREATS_CONTEXT_AS_ADOPTER"),
            ("receiving_context_became_validator", "CONFORMANCE_TREATS_CONTEXT_AS_VALIDATOR"),
            ("receiving_context_became_invalidator", "CONFORMANCE_TREATS_CONTEXT_AS_INVALIDATOR"),
            ("receiving_context_became_operator", "CONFORMANCE_TREATS_CONTEXT_AS_OPERATOR"),
            ("source_validated_by_receiving_context", "CONFORMANCE_VALIDATES_SOURCE"),
            ("source_invalidated_by_receiving_context", "CONFORMANCE_INVALIDATES_SOURCE"),
            ("source_replaced", "CONFORMANCE_REPLACES_SOURCE"),
            ("adoption_created", "CONFORMANCE_CREATES_ADOPTION"),
            ("authority_created", "CONFORMANCE_CREATES_AUTHORITY"),
            ("currentness_created", "CONFORMANCE_CREATES_CURRENTNESS"),
            ("standing_created", "CONFORMANCE_CREATES_STANDING"),
            ("standing_propagated", "CONFORMANCE_CREATES_STANDING_PROPAGATION"),
            ("vessel_relation_created", "CONFORMANCE_CREATES_VESSEL_RELATION"),
            ("derivative_relation_created", "CONFORMANCE_CREATES_DERIVATIVE_RELATION"),
            ("operation_permission_created", "CONFORMANCE_CREATES_OPERATION_PERMISSION"),
            ("public_launch_readiness_created", "CONFORMANCE_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "CONFORMANCE_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "CONFORMANCE_AUTHORIZES_FOLLOW_ON_WORK"),
            ("continuation_authorized", "CONFORMANCE_AUTHORIZES_CONTINUATION"),
            ("publication_flow_opened", "CONFORMANCE_OPENS_PUBLICATION_FLOW"),
            ("reception_closure_passed", "CONFORMANCE_CLAIMS_CLOSURE_PASSED"),
        )
        for field, block_code in cases:
            with self.subTest(field=field):
                self.assert_block_code(
                    resolved(declared_conformance_request(**{field: True})),
                    block_code,
                )

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                self.assert_block_code(
                    resolved(declared_conformance_request(**{field: True})),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        request = declared_conformance_request()
        request["declared_non_claims"].pop("source_received")
        self.assert_block_code(resolved(request), "NON_CLAIM_MISSING_OR_FLIPPED")

        request = declared_conformance_request()
        request["declared_non_claims"]["source_received"] = True
        result = resolved(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertIn(
            result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "CONFORMANCE_RECEIVES_SOURCE"},
        )


if __name__ == "__main__":
    unittest.main()
