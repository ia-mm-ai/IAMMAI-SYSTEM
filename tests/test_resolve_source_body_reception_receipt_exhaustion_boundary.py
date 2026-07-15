"""Executable boundary tests for source-body reception receipt / exhaustion.

These tests prove that the resolver records receipt / exhaustion only as
recognition-record accounting. Receipt / exhaustion is not source receipt, not
reception authorization, not source received, not adoption, not authority, not
currentness, and not conformance or closure.
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

import resolve_source_body_reception_receipt_exhaustion_boundary as resolver  # noqa: E402


RECORDED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_RECORDED"
NOT_RECORDED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_NOT_RECORDED"
REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_REVIEW_BLOCKED"
RECOGNITION_RECORDED = "SOURCE_BODY_RECEPTION_RECOGNITION_RECORDED"
NON_CAPTURE_PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED"
ELIGIBLE = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"
ROLE_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
IDENTITY_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
REQUEST_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "source_body_reception_receipt_exhaustion_metadata",
    "declared_receipt_exhaustion_question",
    "selected_recognition_result",
    "selected_source_body_surface",
    "receiving_context",
    "receipt_exhaustion_basis",
    "recognition_record_receipt_basis",
    "recognition_record_exhaustion_basis",
    "receipt_exhaustion_scope",
    "receipt_exhaustion_checks",
    "receipt_exhaustion_statement",
    "receipt_exhaustion_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_reception_receipt_exhaustion_summary",
}

SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_RECEIPT_EXHAUSTION_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)

RECOGNITION_SCOPE = (
    "RECOGNITION_REVIEW_ONLY",
    "RECOGNITION_IS_NOT_AUTHORIZATION",
    "RECOGNITION_IS_NOT_SOURCE_RECEIPT",
    "RECOGNITION_IS_NOT_ADOPTION",
    "RECOGNITION_IS_NOT_AUTHORITY",
    "RECOGNITION_IS_NOT_CURRENTNESS",
    "RECOGNITION_IS_NOT_VALIDATION",
    "RECOGNITION_IS_NOT_INVALIDATION",
    "RECOGNITION_IS_NOT_OPERATION_PERMISSION",
    "RECOGNITION_IS_NOT_PUBLICATION_FLOW",
    "RECEIPT_EXHAUSTION_REQUIRES_SEPARATE_BOUNDARY",
    "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY",
    "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
)


def false_receipt_exhaustion_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def false_recognition_non_claims() -> dict[str, bool]:
    non_claims = false_receipt_exhaustion_non_claims()
    non_claims["receipt_exhaustion_passed"] = False
    return non_claims


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
            "receiving_context_type": context["receiving_context_type"],
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
            "selected_identity_preservation_result": role_result[
                "selected_identity_preservation_result"
            ],
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
            "purpose_id": "receipt-exhaustion-input",
            "purpose_statement": "Bounded receipt / exhaustion input only.",
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
        "non_capture_basis": {"non_capture_basis_declared": True},
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
            "adoption_created": False,
            "authority_created": False,
            "currentness_created": False,
            "standing_created": False,
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
        },
        "non_capture_checks": [
            {"check_name": "synthetic non-capture check", "passed": True}
        ],
        "non_claims": false_recognition_non_claims(),
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


def selected_recognition_result() -> dict[str, object]:
    non_capture = selected_non_capture_result()
    eligibility = non_capture["non_capture_basis"]["selected_eligibility_result"]
    role_result = non_capture["non_capture_basis"][
        "selected_receiving_context_role_result"
    ]
    identity = non_capture["non_capture_basis"]["selected_identity_preservation_result"]
    request_declaration = non_capture["non_capture_basis"][
        "selected_reception_request_declaration_result"
    ]
    surface = non_capture["non_capture_basis"]["selected_source_body_surface"]
    context = non_capture["non_capture_basis"]["receiving_context"]
    role = non_capture["non_capture_basis"]["selected_receiving_context_role"]
    basis = {
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
        "reception_class": "REFERENCE_RECEPTION",
        "reception_purpose": {
            "purpose_id": "recognized-reception-accounting",
            "purpose_statement": "Bounded recognized reception accounting only.",
        },
        "reception_limits": {
            "reception_limits_id": "recognition-limits-001",
            "no_authorization": True,
            "no_source_receipt": True,
        },
        "selected_receiving_context_role": role,
        "receiving_context_role_class": role["receiving_context_role_class"],
        "receiving_context_role_limits": role["receiving_context_role_limits"],
        "eligibility_basis": non_capture["non_capture_basis"]["eligibility_basis"],
        "admissibility_basis": non_capture["non_capture_basis"]["admissibility_basis"],
        "review_readiness_limits": non_capture["non_capture_basis"][
            "review_readiness_limits"
        ],
        "non_capture_basis": non_capture["non_capture_basis"]["non_capture_basis"],
        "recognition_basis": recognition_basis(),
        "bounded_recognition_only": True,
        "recognized_for_later_reception_family_accounting_only": True,
    }
    statement = {
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
        "receipt_exhaustion_passed": False,
        **false_receipt_exhaustion_non_claims(),
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
            "source_body_reception_recognition_result_id": (
                "source_body_reception_recognition__recognition-001"
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
            "reception_purpose": basis["reception_purpose"],
            "source_body_reception_recognition_recorded": True,
            "reception_recognized": True,
            "bounded_recognition_for_accounting_only": True,
        },
        "declared_recognition_question": {
            "recognition_request_id": "source-body-reception-recognition-request-001",
            "recognition_question": (
                "Can this non-capture-passed source-body reception request be "
                "boundedly recognized?"
            ),
            "recognition_intent": "RECORD_SOURCE_BODY_RECEPTION_RECOGNITION",
        },
        "selected_non_capture_result": {
            "raw_selected_non_capture_result": non_capture,
            "selected_non_capture_result_preserved": True,
        },
        "selected_source_body_surface": surface,
        "receiving_context": context,
        "recognition_basis": basis,
        "recognition_limits": {"recognition_limits": recognition_limits()},
        "recognition_scope": list(RECOGNITION_SCOPE),
        "recognition_statement": statement,
        "recognition_checks": [
            {"check_name": "synthetic recognition check", "passed": True}
        ],
        "non_claims": {
            **false_receipt_exhaustion_non_claims(),
            "receipt_exhaustion_passed": False,
        },
    }


def receipt_exhaustion_basis() -> dict[str, object]:
    return {
        "receipt_exhaustion_basis_declared": True,
        "receipt_exhaustion_of_recognition_accounting_only": True,
        "recognition_record_receipt_only": True,
        "recognition_record_exhaustion_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
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


def declared_receipt_exhaustion_request(**overrides: object) -> dict[str, object]:
    selected = selected_recognition_result()
    request = {
        "receipt_exhaustion_request_id": (
            "source-body-reception-receipt-exhaustion-request-001"
        ),
        "receipt_exhaustion_question": (
            "Can this bounded source-body reception recognition record be "
            "receipted and exhausted for reception-family accounting?"
        ),
        "receipt_exhaustion_intent": (
            "RECORD_SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION"
        ),
        "selected_recognition_result": selected,
        "selected_recognition_result_id": (
            "source_body_reception_recognition__recognition-001"
        ),
        "selected_recognition_result_outcome": RECOGNITION_RECORDED,
        "receipt_exhaustion_basis": receipt_exhaustion_basis(),
        "recognition_record_receipt_basis": recognition_record_receipt_basis(),
        "recognition_record_exhaustion_basis": recognition_record_exhaustion_basis(),
        "receipt_exhaustion_scope": list(SUPPORTED_SCOPE),
        "requested_receipt_exhaustion_outcome": RECORDED,
        "declared_non_claims": false_receipt_exhaustion_non_claims(),
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


class SourceBodyReceptionReceiptExhaustionBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict[str, object] | None = None) -> dict[str, object]:
        return resolver.resolve_source_body_reception_receipt_exhaustion_boundary(
            declared_receipt_exhaustion_request=request
        )

    def assert_block(self, result: dict[str, object], code: str) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], code)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_no_downstream_claims(
        self, result: dict[str, object], *, recorded: bool = False
    ) -> None:
        non_claims = result["non_claims"]
        statement = result["receipt_exhaustion_statement"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
            self.assertIs(statement[key], False, key)
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(non_claims[key], recorded, key)
            self.assertIs(statement[key], recorded, key)

    def test_successful_receipt_exhaustion_recorded_result(self) -> None:
        request = declared_receipt_exhaustion_request()
        original = copy.deepcopy(request)

        result = self.resolve(request)

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertEqual(set(result), TOP_LEVEL_SECTIONS)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["source_body_reception_receipt_exhaustion_summary"][
                "failed_check_count"
            ],
            0,
        )
        self.assertEqual(request, original)

        metadata = result["source_body_reception_receipt_exhaustion_metadata"]
        self.assertTrue(metadata["source_body_reception_receipt_exhaustion_result_id"])
        self.assertTrue(metadata["source_body_reception_receipt_exhaustion_result_type"])
        self.assertEqual(
            metadata["source_body_reception_receipt_exhaustion_result_version"],
            "0.1.0",
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_source_body_reception_receipt_exhaustion_boundary",
        )

        declared = result["declared_receipt_exhaustion_question"]
        self.assertEqual(
            declared["receipt_exhaustion_request_id"],
            "source-body-reception-receipt-exhaustion-request-001",
        )
        self.assertEqual(declared["selected_recognition_result_outcome"], RECOGNITION_RECORDED)
        self.assertEqual(declared["reception_class"], "REFERENCE_RECEPTION")
        self.assertTrue(declared["receipt_exhaustion_is_not_source_receipt"])
        self.assertTrue(declared["receipt_exhaustion_is_not_authorization"])
        self.assertTrue(declared["receipt_exhaustion_does_not_decide_conformance"])
        self.assertTrue(declared["receipt_exhaustion_does_not_decide_closure"])

        selected = result["selected_recognition_result"]
        self.assertEqual(selected["selected_recognition_result_outcome"], RECOGNITION_RECORDED)
        self.assertTrue(selected["selected_recognition_outcome_is_recorded"])
        self.assertTrue(selected["selected_recognition_result_failed_check_count_zero"])
        self.assertTrue(selected["selected_recognition_result_preserved"])
        self.assertTrue(selected["selected_recognition_result_recorded"])
        self.assertTrue(selected["selected_non_capture_result_preserved"])
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
        self.assertTrue(selected["source_body_reception_recognition_recorded"])
        self.assertTrue(selected["reception_recognized"])
        self.assertTrue(selected["recognition_bounded_for_accounting_only"])
        self.assertTrue(selected["recognition_is_not_authorization"])
        self.assertTrue(selected["recognition_is_not_source_receipt"])
        self.assertTrue(selected["source_remains_unreceived"])
        self.assertTrue(selected["source_receipt_remains_unrecorded"])

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

        basis = result["receipt_exhaustion_basis"]
        for key in (
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
            "recognition_scope",
            "receipt_exhaustion_basis",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "receipt_exhaustion_of_recognition_accounting_only",
            "recognition_record_receipt_only",
            "recognition_record_exhaustion_only",
            "source_remains_unreceived",
            "source_receipt_remains_unrecorded",
            "receipt_exhaustion_is_not_authorization",
            "receipt_exhaustion_is_not_source_receipt",
            "receipt_exhaustion_is_not_conformance",
            "receipt_exhaustion_is_not_closure",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(basis[key], key)

        receipt_basis = result["recognition_record_receipt_basis"]
        self.assertEqual(
            receipt_basis["recognition_record_receipt_basis"],
            recognition_record_receipt_basis(),
        )
        self.assertTrue(receipt_basis["recognition_record_receipted_for_accounting_only"])
        self.assertTrue(receipt_basis["recognized_reception_accounting_receipt_recorded_only"])
        self.assertTrue(receipt_basis["source_receipt_not_recorded"])
        self.assertFalse(receipt_basis["source_received"])
        self.assertFalse(receipt_basis["reception_authorization"])
        self.assertTrue(receipt_basis["receipt_is_not_source_receipt"])
        self.assertTrue(receipt_basis["receipt_is_not_authorization"])
        self.assertTrue(receipt_basis["receipt_is_not_adoption"])
        self.assertTrue(receipt_basis["receipt_is_not_conformance"])
        self.assertTrue(receipt_basis["receipt_is_not_closure"])

        exhaustion_basis = result["recognition_record_exhaustion_basis"]
        self.assertEqual(
            exhaustion_basis["recognition_record_exhaustion_basis"],
            recognition_record_exhaustion_basis(),
        )
        self.assertTrue(
            exhaustion_basis["recognition_record_exhaustion_recorded_for_this_layer_only"]
        )
        self.assertTrue(exhaustion_basis["recognized_reception_accounting_exhausted_only"])
        self.assertTrue(exhaustion_basis["exhaustion_is_not_closure"])
        self.assertTrue(exhaustion_basis["exhaustion_is_not_final_completion"])
        self.assertTrue(exhaustion_basis["exhaustion_is_not_conformance"])
        self.assertTrue(exhaustion_basis["exhaustion_does_not_authorize_continuation"])
        self.assertTrue(exhaustion_basis["exhaustion_does_not_authorize_follow_on_work"])

        scope = result["receipt_exhaustion_scope"]
        self.assertEqual(set(scope["selected_receipt_exhaustion_scope_values"]), set(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_scope_values_supported"])
        self.assertEqual(scope["unsupported_receipt_exhaustion_scope_values"], [])
        for key in (
            "recognition_record_receipt_only",
            "recognition_record_exhaustion_only",
            "receipt_exhaustion_is_not_source_receipt",
            "receipt_exhaustion_is_not_authorization",
            "receipt_exhaustion_does_not_receive_source",
            "receipt_exhaustion_does_not_create_source_receipt",
            "receipt_exhaustion_is_not_adoption",
            "receipt_exhaustion_is_not_authority",
            "receipt_exhaustion_is_not_currentness",
            "receipt_exhaustion_is_not_validation",
            "receipt_exhaustion_is_not_invalidation",
            "receipt_exhaustion_is_not_operation_permission",
            "receipt_exhaustion_is_not_publication_flow",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(scope[key], key)

        statement = result["receipt_exhaustion_statement"]
        for key in (
            "source_body_reception_receipt_exhaustion_recorded",
            "reception_recognition_receipt_recorded",
            "reception_recognition_exhaustion_recorded",
            "recognized_reception_accounting_receipt_recorded",
            "recognized_reception_accounting_exhausted",
            "selected_recognition_result_preserved",
            "selected_recognition_result_recorded",
            "selected_recognition_result_failed_check_count_zero",
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
            "reception_recognized",
            "recognition_bounded_for_accounting_only",
            "receipt_exhaustion_of_recognition_accounting_only",
            "recognition_record_receipt_only",
            "recognition_record_exhaustion_only",
            "receipt_exhaustion_is_not_source_receipt",
            "receipt_exhaustion_is_not_authorization",
            "receipt_exhaustion_does_not_receive_source",
            "receipt_exhaustion_does_not_create_source_receipt",
            "receipt_exhaustion_is_not_conformance",
            "receipt_exhaustion_is_not_closure",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(statement[key], key)
        self.assert_no_downstream_claims(result, recorded=True)

    def test_checks_non_meaning_and_open_sections(self) -> None:
        result = self.resolve(declared_receipt_exhaustion_request())

        checks = result["receipt_exhaustion_checks"]
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
            "receipt_exhaustion_question_declared",
            "receipt_exhaustion_intent_supported",
            "selected_recognition_result_present",
            "selected_recognition_outcome_declared",
            "selected_recognition_outcome_recorded",
            "selected_recognition_failed_check_count_zero",
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
            "reception_recognized_true",
            "recognition_bounded_for_accounting_only",
            "recognition_not_authorization",
            "recognition_not_source_receipt",
            "source_unreceived",
            "source_receipt_unrecorded",
            "receipt_exhaustion_basis_declared",
            "recognition_record_receipt_basis_declared",
            "recognition_record_exhaustion_basis_declared",
            "receipt_exhaustion_scope_supported",
            "receipt_exhaustion_is_not_source_receipt",
            "receipt_exhaustion_does_not_receive_source",
            "receipt_exhaustion_does_not_authorize_reception",
            "receipt_exhaustion_does_not_create_source_receipt",
            "receipt_exhaustion_does_not_create_adoption",
            "receipt_exhaustion_does_not_create_authority",
            "receipt_exhaustion_does_not_create_currentness",
            "receipt_exhaustion_does_not_validate_source",
            "receipt_exhaustion_does_not_invalidate_source",
            "receipt_exhaustion_does_not_replace_source",
            "receipt_exhaustion_does_not_create_operation_permission",
            "receipt_exhaustion_does_not_create_governance",
            "receipt_exhaustion_does_not_open_publication_flow",
            "receipt_exhaustion_does_not_create_public_readiness",
            "receipt_exhaustion_does_not_claim_final_completion",
            "receipt_exhaustion_does_not_authorize_continuation",
            "receipt_exhaustion_does_not_authorize_follow_on_work",
            "conformance_remains_future_work",
            "closure_remains_future_work",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_checks.issubset(check_names))

        non_meaning = result["receipt_exhaustion_non_meaning"]
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
            "conformance_passed",
            "closure_recorded",
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "continuation_authorized",
            "publication_flow_opened",
        ):
            self.assertTrue(non_meaning[f"does_not_mean_{meaning}"], meaning)
        self.assertTrue(non_meaning["receipt_exhaustion_is_not_source_receipt"])
        self.assertTrue(non_meaning["receipt_exhaustion_is_not_authorization"])
        self.assertTrue(non_meaning["receipt_exhaustion_is_not_source_received"])
        self.assertTrue(non_meaning["receipt_exhaustion_is_not_conformance"])
        self.assertTrue(non_meaning["receipt_exhaustion_is_not_closure"])

        additional = result["additional_basis_required"]
        self.assertFalse(additional["additional_basis_required"])
        self.assertTrue(additional["missing_basis_is_not_scheduled"])
        self.assertTrue(additional["missing_basis_is_not_authorized"])
        self.assertTrue(additional["missing_basis_is_not_executed"])

        open_section = result["what_remains_open"]
        for item in (
            "source-body reception receipt / exhaustion test",
            "source-body reception receipt / exhaustion live artifact",
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
                result = self.resolve(
                    declared_receipt_exhaustion_request(receipt_exhaustion_scope=[value])
                )
                self.assertEqual(result["outcome"], RECORDED)
                self.assertIn(
                    value,
                    result["receipt_exhaustion_scope"][
                        "selected_receipt_exhaustion_scope_values"
                    ],
                )
        result = self.resolve(
            declared_receipt_exhaustion_request(
                receipt_exhaustion_scope=list(SUPPORTED_SCOPE)
                + ["UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE"]
            )
        )
        self.assert_block(result, "UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE")

    def test_requires_additional_basis_and_not_recorded_results(self) -> None:
        additional_context = {
            "receipt_exhaustion_basis_too_generic": True,
            "recognition_record_receipt_basis_unclear": True,
            "exhaustion_closure_distinction_unclear": True,
            "missing_basis_is_not_scheduled": True,
        }
        requires = self.resolve(
            declared_receipt_exhaustion_request(
                requested_receipt_exhaustion_outcome=REQUIRES_ADDITIONAL_BASIS,
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
        self.assertTrue(
            requires["additional_basis_required"]["missing_basis_is_not_executed"]
        )
        self.assert_no_downstream_claims(requires, recorded=False)

        not_recorded_basis = {
            "receipt_exhaustion_basis_cannot_be_bounded": True,
            "receipt_overread_as_source_receipt": True,
            "receipt_exhaustion_cannot_be_separated_from_closure": True,
        }
        not_recorded = self.resolve(
            declared_receipt_exhaustion_request(
                requested_receipt_exhaustion_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertEqual(
            not_recorded["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_basis,
        )
        self.assertTrue(
            not_recorded["not_recorded_basis"]["not_recorded_does_not_mutate"]
        )
        self.assertTrue(
            not_recorded["not_recorded_basis"][
                "not_recorded_does_not_record_source_receipt"
            ]
        )
        self.assertTrue(
            not_recorded["not_recorded_basis"]["not_recorded_does_not_claim_closure"]
        )
        self.assert_no_downstream_claims(not_recorded, recorded=False)

    def test_summary_helper_and_request_builder(self) -> None:
        selected = selected_recognition_result()
        additional_context = {"receipt_source_receipt_distinction_unclear": True}
        not_recorded_basis = {"receipt_overread_as_authorization": True}
        request = resolver.build_declared_source_body_reception_receipt_exhaustion_request(
            "receipt-exhaustion-builder-request-001",
            "Can this recognition record be receipted and exhausted for accounting?",
            selected,
            receipt_exhaustion_basis(),
            recognition_record_receipt_basis(),
            recognition_record_exhaustion_basis(),
            list(SUPPORTED_SCOPE),
            selected_recognition_result_id="selected-recognition-builder-001",
            selected_recognition_result_outcome=RECOGNITION_RECORDED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )
        self.assertEqual(
            request["receipt_exhaustion_request_id"],
            "receipt-exhaustion-builder-request-001",
        )
        self.assertEqual(
            request["receipt_exhaustion_question"],
            "Can this recognition record be receipted and exhausted for accounting?",
        )
        self.assertEqual(request["selected_recognition_result"], selected)
        self.assertEqual(request["receipt_exhaustion_basis"], receipt_exhaustion_basis())
        self.assertEqual(
            request["recognition_record_receipt_basis"],
            recognition_record_receipt_basis(),
        )
        self.assertEqual(
            request["recognition_record_exhaustion_basis"],
            recognition_record_exhaustion_basis(),
        )
        self.assertEqual(request["receipt_exhaustion_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_recognition_result_id"], "selected-recognition-builder-001")
        self.assertEqual(request["selected_recognition_result_outcome"], RECOGNITION_RECORDED)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertFalse(contains_true_key(request, key), key)
        for key in (
            "source_receipt_recorded",
            "source_receipt_created",
            "source_received",
            "reception_authorized",
            "reception_conformance_passed",
            "reception_closure_passed",
        ):
            self.assertFalse(contains_true_key(request, key), key)

        result = self.resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        summary = resolver.build_source_body_reception_receipt_exhaustion_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(
            summary["receipt_exhaustion_request_id"],
            "receipt-exhaustion-builder-request-001",
        )
        self.assertEqual(summary["selected_recognition_result_outcome"], RECOGNITION_RECORDED)
        self.assertEqual(summary["passed_check_count"], len(result["receipt_exhaustion_checks"]))
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "receipt_exhaustion_recorded",
            "recognition_record_receipt_recorded",
            "recognition_record_exhaustion_recorded",
            "recognized_reception_accounting_receipt_recorded",
            "recognized_reception_accounting_exhausted",
            "selected_recognition_result_preserved",
            "selected_recognition_result_recorded",
            "selected_recognition_result_failed_check_count_zero",
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
            "reception_recognized",
            "recognition_bounded_for_accounting_only",
            "receipt_exhaustion_of_recognition_accounting_only",
            "recognition_record_receipt_only",
            "recognition_record_exhaustion_only",
            "receipt_exhaustion_not_source_receipt",
            "receipt_exhaustion_not_authorization",
            "no_source_received",
            "no_source_receipt_recorded",
            "no_source_receipt_created",
            "conformance_future",
            "closure_future",
            "no_adoption_authority_currentness_standing",
            "no_vessel_derivative_relation",
            "no_operation_permission_governance_publication_flow",
            "no_public_readiness_final_completion_follow_on_work",
        ):
            self.assertTrue(summary[key], key)

    def test_path_based_selected_recognition_request_and_write_helpers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selected_path = root / "selected_recognition.json"
            selected_payload = selected_recognition_result()
            selected_path.write_text(json.dumps(selected_payload), encoding="utf-8")
            request = declared_receipt_exhaustion_request(
                selected_recognition_result_path=str(selected_path)
            )
            request.pop("selected_recognition_result")
            result = self.resolve(request)
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(
                result["selected_recognition_result"]["selected_recognition_result_path"],
                str(selected_path),
            )
            self.assertEqual(
                result["selected_recognition_result"][
                    "selected_recognition_result_outcome"
                ],
                RECOGNITION_RECORDED,
            )

            request_path = root / "declared_receipt_exhaustion_request.json"
            request_path.write_text(
                json.dumps(declared_receipt_exhaustion_request()),
                encoding="utf-8",
            )
            path_result = (
                resolver.resolve_source_body_reception_receipt_exhaustion_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), TOP_LEVEL_SECTIONS)
            self.assertEqual(
                path_result["declared_receipt_exhaustion_question"][
                    "declared_receipt_exhaustion_request_path"
                ],
                str(request_path),
            )

            output = root / "nested" / "receipt_exhaustion_result.json"
            written = resolver.write_source_body_reception_receipt_exhaustion_result(
                path_result, output
            )
            self.assertEqual(written, output)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["outcome"], RECORDED)

    def test_default_write_uses_bounded_root_and_does_not_overwrite(self) -> None:
        result = self.resolve(declared_receipt_exhaustion_request())
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp) / "receipt-exhaustion-root"
            original_root = str(
                resolver.SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT
            )
            self.assertIn("source_body_reception_receipt_exhaustion_boundary", original_root)
            self.assertNotIn("source_body_reception_recognition_boundary", original_root)
            self.assertNotIn("source_body_reception_conformance", original_root)
            with patch.object(
                resolver,
                "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT",
                temp_root,
            ):
                first = resolver.write_source_body_reception_receipt_exhaustion_result(
                    result
                )
                second = resolver.write_source_body_reception_receipt_exhaustion_result(
                    result
                )
            self.assertEqual(first.parent, temp_root)
            self.assertEqual(second.parent, temp_root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = declared_receipt_exhaustion_request()
        original_request = copy.deepcopy(request)
        selected_original = copy.deepcopy(request["selected_recognition_result"])
        nested_non_capture_original = copy.deepcopy(
            request["selected_recognition_result"]["recognition_basis"][
                "selected_non_capture_result"
            ]
        )
        surface_original = copy.deepcopy(
            request["selected_recognition_result"]["recognition_basis"][
                "selected_source_body_surface"
            ]
        )
        context_original = copy.deepcopy(
            request["selected_recognition_result"]["recognition_basis"][
                "receiving_context"
            ]
        )
        basis_original = copy.deepcopy(request["receipt_exhaustion_basis"])
        receipt_basis_original = copy.deepcopy(request["recognition_record_receipt_basis"])
        exhaustion_basis_original = copy.deepcopy(
            request["recognition_record_exhaustion_basis"]
        )
        scope_original = copy.deepcopy(request["receipt_exhaustion_scope"])

        first = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_recognition_result"], selected_original)
        self.assertEqual(
            request["selected_recognition_result"]["recognition_basis"][
                "selected_non_capture_result"
            ],
            nested_non_capture_original,
        )
        self.assertEqual(
            request["selected_recognition_result"]["recognition_basis"][
                "selected_source_body_surface"
            ],
            surface_original,
        )
        self.assertEqual(
            request["selected_recognition_result"]["recognition_basis"][
                "receiving_context"
            ],
            context_original,
        )
        self.assertEqual(request["receipt_exhaustion_basis"], basis_original)
        self.assertEqual(
            request["recognition_record_receipt_basis"], receipt_basis_original
        )
        self.assertEqual(
            request["recognition_record_exhaustion_basis"], exhaustion_basis_original
        )
        self.assertEqual(request["receipt_exhaustion_scope"], scope_original)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selected_path = root / "selected_recognition.json"
            selected_path.write_text(json.dumps(selected_original, sort_keys=True), encoding="utf-8")
            before = selected_path.read_text(encoding="utf-8")
            path_request = declared_receipt_exhaustion_request(
                selected_recognition_result_path=str(selected_path)
            )
            path_request.pop("selected_recognition_result")
            result = self.resolve(path_request)
            resolver.write_source_body_reception_receipt_exhaustion_result(
                result, root / "additive" / "receipt_exhaustion.json"
            )
            self.assertEqual(selected_path.read_text(encoding="utf-8"), before)

    def test_blocking_request_shape_and_paths(self) -> None:
        self.assert_block(self.resolve(None), "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED")
        malformed = resolver.resolve_source_body_reception_receipt_exhaustion_boundary(
            declared_receipt_exhaustion_request=["not", "a", "mapping"]
        )
        self.assert_block(
            malformed, "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED"
        )
        block_request = declared_receipt_exhaustion_request(
            receipt_exhaustion_intent=(
                "BLOCK_SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_REVIEW"
            )
        )
        self.assert_block(
            self.resolve(block_request),
            "RECEIPT_EXHAUSTION_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            missing = (
                resolver.resolve_source_body_reception_receipt_exhaustion_boundary_from_path(
                    root / "missing.json"
                )
            )
            self.assert_block(missing, "DECLARED_RECEIPT_EXHAUSTION_REQUEST_UNREADABLE")
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self.assert_block(
                resolver.resolve_source_body_reception_receipt_exhaustion_boundary_from_path(
                    malformed_path
                ),
                "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED",
            )
            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_block(
                resolver.resolve_source_body_reception_receipt_exhaustion_boundary_from_path(
                    array_path
                ),
                "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED",
            )

    def test_blocking_selected_recognition_paths_and_result_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request = declared_receipt_exhaustion_request(
                selected_recognition_result_path=str(root / "missing.json")
            )
            request.pop("selected_recognition_result")
            self.assert_block(self.resolve(request), "RECOGNITION_RESULT_UNREADABLE")

            malformed_path = root / "selected-malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            request = declared_receipt_exhaustion_request(
                selected_recognition_result_path=str(malformed_path)
            )
            request.pop("selected_recognition_result")
            self.assert_block(self.resolve(request), "RECOGNITION_RESULT_MALFORMED")

            array_path = root / "selected-array.json"
            array_path.write_text("[]", encoding="utf-8")
            request = declared_receipt_exhaustion_request(
                selected_recognition_result_path=str(array_path)
            )
            request.pop("selected_recognition_result")
            self.assert_block(self.resolve(request), "RECOGNITION_RESULT_MALFORMED")

        missing_outcome = declared_receipt_exhaustion_request()
        missing_outcome.pop("selected_recognition_result_outcome")
        missing_outcome["selected_recognition_result"].pop("outcome")
        missing_outcome["selected_recognition_result"][
            "source_body_reception_recognition_summary"
        ].pop("outcome")
        self.assert_block(
            self.resolve(missing_outcome),
            "RECOGNITION_RESULT_OUTCOME_MISSING",
        )

        wrong_outcome = declared_receipt_exhaustion_request(
            selected_recognition_result_outcome=(
                "SOURCE_BODY_RECEPTION_RECOGNITION_NOT_RECORDED"
            )
        )
        wrong_outcome["selected_recognition_result"]["outcome"] = (
            "SOURCE_BODY_RECEPTION_RECOGNITION_NOT_RECORDED"
        )
        self.assert_block(self.resolve(wrong_outcome), "RECOGNITION_RESULT_NOT_RECORDED")

        failed_checks = declared_receipt_exhaustion_request()
        failed_checks["selected_recognition_result"][
            "source_body_reception_recognition_summary"
        ]["failed_check_count"] = 1
        self.assert_block(
            self.resolve(failed_checks), "RECOGNITION_RESULT_HAS_FAILED_CHECKS"
        )

    def test_blocking_missing_required_basis(self) -> None:
        cases = (
            ("selected_non_capture_result", "NON_CAPTURE_RESULT_MISSING"),
            ("selected_eligibility_result", "ELIGIBILITY_RESULT_MISSING"),
            (
                "selected_receiving_context_role_result",
                "RECEIVING_CONTEXT_ROLE_RESULT_MISSING",
            ),
            (
                "selected_identity_preservation_result",
                "IDENTITY_PRESERVATION_RESULT_MISSING",
            ),
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
                request = declared_receipt_exhaustion_request()
                remove_key_recursive(request["selected_recognition_result"], key)
                self.assert_block(self.resolve(request), code)

        request = declared_receipt_exhaustion_request()
        request.pop("receipt_exhaustion_basis")
        self.assert_block(self.resolve(request), "RECEIPT_EXHAUSTION_BASIS_MISSING")

        request = declared_receipt_exhaustion_request()
        request.pop("recognition_record_receipt_basis")
        self.assert_block(
            self.resolve(request), "RECOGNITION_RECORD_RECEIPT_BASIS_MISSING"
        )

        request = declared_receipt_exhaustion_request()
        request.pop("recognition_record_exhaustion_basis")
        self.assert_block(
            self.resolve(request), "RECOGNITION_RECORD_EXHAUSTION_BASIS_MISSING"
        )

    def test_blocking_malformed_surface_and_context(self) -> None:
        request = declared_receipt_exhaustion_request(
            selected_source_body_surface="not-a-mapping"
        )
        self.assert_block(self.resolve(request), "SELECTED_SOURCE_BODY_SURFACE_MALFORMED")

        request = declared_receipt_exhaustion_request(
            receiving_context="not-a-mapping",
            receiving_context_type="PRESENT_EXECUTION_CONTEXT",
        )
        self.assert_block(self.resolve(request), "RECEIVING_CONTEXT_MALFORMED")

    def test_blocking_receipt_exhaustion_overreach_flags(self) -> None:
        cases = (
            ("reception_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_RECEPTION"),
            ("source_received", "RECEIPT_EXHAUSTION_RECEIVES_SOURCE"),
            ("source_receipt_recorded", "RECEIPT_EXHAUSTION_RECORDS_SOURCE_RECEIPT"),
            ("source_receipt_created", "RECEIPT_EXHAUSTION_CREATES_SOURCE_RECEIPT"),
            (
                "receiving_context_governance_created",
                "RECEIPT_EXHAUSTION_CREATES_GOVERNANCE",
            ),
            (
                "receiving_context_became_source",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_SOURCE",
            ),
            (
                "receiving_context_became_authority",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_AUTHORITY",
            ),
            (
                "receiving_context_became_current",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_CURRENT",
            ),
            (
                "receiving_context_became_receiver",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_RECEIVER",
            ),
            (
                "receiving_context_became_adopter",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_ADOPTER",
            ),
            (
                "receiving_context_became_validator",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_VALIDATOR",
            ),
            (
                "receiving_context_became_invalidator",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_INVALIDATOR",
            ),
            (
                "receiving_context_became_operator",
                "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_OPERATOR",
            ),
            (
                "source_validated_by_receiving_context",
                "RECEIPT_EXHAUSTION_VALIDATES_SOURCE",
            ),
            (
                "source_invalidated_by_receiving_context",
                "RECEIPT_EXHAUSTION_INVALIDATES_SOURCE",
            ),
            ("source_replaced", "RECEIPT_EXHAUSTION_REPLACES_SOURCE"),
            ("adoption_created", "RECEIPT_EXHAUSTION_CREATES_ADOPTION"),
            ("authority_created", "RECEIPT_EXHAUSTION_CREATES_AUTHORITY"),
            ("currentness_created", "RECEIPT_EXHAUSTION_CREATES_CURRENTNESS"),
            ("standing_created", "RECEIPT_EXHAUSTION_CREATES_STANDING"),
            ("standing_propagated", "RECEIPT_EXHAUSTION_CREATES_STANDING_PROPAGATION"),
            ("vessel_relation_created", "RECEIPT_EXHAUSTION_CREATES_VESSEL_RELATION"),
            (
                "derivative_relation_created",
                "RECEIPT_EXHAUSTION_CREATES_DERIVATIVE_RELATION",
            ),
            (
                "operation_permission_created",
                "RECEIPT_EXHAUSTION_CREATES_OPERATION_PERMISSION",
            ),
            (
                "public_launch_readiness_created",
                "RECEIPT_EXHAUSTION_CREATES_PUBLIC_READINESS",
            ),
            ("final_completion_claimed", "RECEIPT_EXHAUSTION_CLAIMS_FINAL_COMPLETION"),
            (
                "follow_on_work_authorized",
                "RECEIPT_EXHAUSTION_AUTHORIZES_FOLLOW_ON_WORK",
            ),
            ("continuation_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_CONTINUATION"),
            ("publication_flow_opened", "RECEIPT_EXHAUSTION_OPENS_PUBLICATION_FLOW"),
            (
                "reception_conformance_passed",
                "RECEIPT_EXHAUSTION_CLAIMS_CONFORMANCE_PASSED",
            ),
            ("reception_closure_passed", "RECEIPT_EXHAUSTION_CLAIMS_CLOSURE_PASSED"),
        )
        for key, code in cases:
            with self.subTest(key=key):
                request = declared_receipt_exhaustion_request()
                request[key] = True
                self.assert_block(self.resolve(request), code)

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        for key in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(key=key):
                request = declared_receipt_exhaustion_request()
                request[key] = True
                self.assert_block(
                    self.resolve(request), "MUTATION_REPLAY_OR_MERGE_DETECTED"
                )

        missing = declared_receipt_exhaustion_request()
        missing["declared_non_claims"].pop("source_received")
        self.assert_block(self.resolve(missing), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = declared_receipt_exhaustion_request()
        flipped["declared_non_claims"]["source_received"] = True
        self.assert_block(self.resolve(flipped), "RECEIPT_EXHAUSTION_RECEIVES_SOURCE")


if __name__ == "__main__":
    unittest.main()
