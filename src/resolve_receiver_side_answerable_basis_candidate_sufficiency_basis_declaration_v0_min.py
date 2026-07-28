"""Validate one bounded candidate-sufficiency basis declaration.

The resolver validates declaration structure and readiness for later separate
supply only. It does not supply or admit basis, execute the waiting operation,
derive dimension or candidate results, or create downstream standing.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "declaration_v0_min"
)

DECLARATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_001"
)
DECLARATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION"
)
DECLARATION_VERSION = "0.1.0"
DECLARATION_SCOPE = (
    "DECLARE_ONE_BOUNDED_EIGHT_DIMENSION_CANDIDATE_SUFFICIENCY_BASIS_ONLY"
)

SELECTED_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
SELECTED_SUFFICIENCY_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
)
SELECTED_SUFFICIENCY_OPERATION_VERSION = "0.1.0"
SELECTED_SUFFICIENCY_OPERATION_SCOPE = (
    "DECIDE_SUFFICIENCY_POSTURE_OF_ONE_SELECTED_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED = "REQUIRES_SUFFICIENCY_BASIS"
SELECTED_SUFFICIENCY_OPERATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_"
    "REQUIRES_SUFFICIENCY_BASIS"
)
SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = (
    "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_SUFFICIENCY_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001"
)
SELECTED_SUFFICIENCY_BOUNDARY_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY"
)
SELECTED_RECEPTION_OPERATION_ID = (
    "receiver_side_answerable_basis_reception_operation_001"
)
SELECTED_EVALUATION_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
)
SELECTED_EVALUATION_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_evaluation_operation_001"
)

SUFFICIENCY_DECLARATION_DIMENSION_IDS = (
    "receiver_answerability_fit",
    "selected_purpose_adequacy",
    "bounded_material_completeness",
    "unresolved_contradiction_posture",
    "unsupported_assumption_dependency",
    "scope_constrained_usability",
    "refusal_withholding_compatibility",
    "provenance_capture_limitation_posture",
)

DIMENSION_LABELS = MappingProxyType(
    {
        "receiver_answerability_fit": "receiver-answerability fit",
        "selected_purpose_adequacy": "selected-purpose adequacy",
        "bounded_material_completeness": "bounded material completeness",
        "unresolved_contradiction_posture": "unresolved contradiction posture",
        "unsupported_assumption_dependency": "unsupported assumption dependency",
        "scope_constrained_usability": "scope-constrained usability",
        "refusal_withholding_compatibility": (
            "refusal and withholding compatibility"
        ),
        "provenance_capture_limitation_posture": (
            "provenance and capture limitation posture"
        ),
    }
)

DIMENSION_RULE_KEYS = MappingProxyType(
    {
        "receiver_answerability_fit": MappingProxyType(
            {
                "support": "bounded_receiver_answerability_fit_supported",
                "contradiction": (
                    "bounded_receiver_answerability_fit_contradicted"
                ),
                "unresolved": "bounded_receiver_answerability_fit_unresolved",
            }
        ),
        "selected_purpose_adequacy": MappingProxyType(
            {
                "support": "selected_purpose_adequacy_supported",
                "contradiction": "selected_purpose_adequacy_contradicted",
                "unresolved": "selected_purpose_adequacy_unresolved",
            }
        ),
        "bounded_material_completeness": MappingProxyType(
            {
                "support": "bounded_material_complete_for_selected_purpose",
                "contradiction": (
                    "bounded_material_incomplete_for_selected_purpose"
                ),
                "unresolved": "bounded_material_completeness_unresolved",
            }
        ),
        "unresolved_contradiction_posture": MappingProxyType(
            {
                "support": (
                    "no_unresolved_material_contradiction_for_selected_purpose"
                ),
                "contradiction": (
                    "material_contradiction_present_for_selected_purpose"
                ),
                "unresolved": "material_contradiction_posture_unresolved",
            }
        ),
        "unsupported_assumption_dependency": MappingProxyType(
            {
                "support": "no_required_unsupported_assumption_dependency",
                "contradiction": (
                    "required_unsupported_assumption_dependency_present"
                ),
                "unresolved": "unsupported_assumption_dependency_unresolved",
            }
        ),
        "scope_constrained_usability": MappingProxyType(
            {
                "support": "usable_within_selected_scope",
                "contradiction": "not_usable_within_selected_scope",
                "unresolved": "scope_constrained_usability_unresolved",
            }
        ),
        "refusal_withholding_compatibility": MappingProxyType(
            {
                "support": (
                    "compatible_with_recorded_refusal_and_withholding_postures"
                ),
                "contradiction": (
                    "incompatible_with_recorded_refusal_or_withholding_posture"
                ),
                "unresolved": "refusal_withholding_compatibility_unresolved",
            }
        ),
        "provenance_capture_limitation_posture": MappingProxyType(
            {
                "support": (
                    "provenance_and_capture_limitations_bounded_and_preserved"
                ),
                "contradiction": (
                    "provenance_or_capture_limitation_materially_contradicts_"
                    "selected_use"
                ),
                "unresolved": (
                    "provenance_capture_limitation_posture_unresolved"
                ),
            }
        ),
    }
)

DIMENSION_NON_CONVERSION_STATEMENTS = MappingProxyType(
    {
        "receiver_answerability_fit": (
            "receiver-answerability fit is not attestation, receipt, or presence."
        ),
        "selected_purpose_adequacy": (
            "selected-purpose adequacy is bounded-purpose posture only, not "
            "truth or standing."
        ),
        "bounded_material_completeness": (
            "bounded completeness is not unrestricted completeness or candidate "
            "truth."
        ),
        "unresolved_contradiction_posture": (
            "no unresolved material contradiction is not verified truth."
        ),
        "unsupported_assumption_dependency": (
            "absence of a required unsupported assumption dependency is not "
            "authority or standing."
        ),
        "scope_constrained_usability": (
            "scoped usability is not general usability, output authorization, "
            "or action authorization."
        ),
        "refusal_withholding_compatibility": (
            "refusal and withholding compatibility is not consent, attestation, "
            "or receipt."
        ),
        "provenance_capture_limitation_posture": (
            "bounded provenance and capture limitations are not verified "
            "provenance, physical validity, or presence."
        ),
    }
)

OUTCOME_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION_"
    "RECORDED"
)
OUTCOME_REQUIRES_COMPLETE_DECLARATION = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION_"
    "REQUIRES_COMPLETE_DECLARATION"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION_"
    "BLOCKED"
)
OUTCOME_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION_"
    "NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_COMPLETE_DECLARATION,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

DECLARATION_RESULT_READY_FOR_SUPPLY = (
    "CANDIDATE_SUFFICIENCY_BASIS_DECLARATION_READY_FOR_SUPPLY"
)
DECLARATION_RESULT_REQUIRES_COMPLETE = (
    "REQUIRES_COMPLETE_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION"
)
DECLARATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
DECLARATION_RESULT_FAMILY = (
    DECLARATION_RESULT_READY_FOR_SUPPLY,
    DECLARATION_RESULT_REQUIRES_COMPLETE,
    DECLARATION_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "DECLARATION"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
    "BASIS_DECLARATION"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "DECLARATION"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

ADMISSIBLE_FUTURE_ROUTE = (
    "CANDIDATE_SUFFICIENCY_BASIS_DECLARATION_THEN_SEPARATE_OPERATION_REQUEST_"
    "SUPPLY_ONLY"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "DECLARATION_V0_MIN_SPEC.md"
)
SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_"
    "v0_min_result.json"
)
GOVERNING_DECLARATION_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH
)
SELECTED_WAITING_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
)
OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "declaration_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "declaration_001__receiver_side_answerable_basis_candidate_sufficiency_"
    "basis_declaration_v0_min_result.json"
)

MAX_SEQUENCE_ITEMS = 32
MAX_MAPPING_ITEMS = 192
MAX_TEXT_LENGTH = 2_048
MAX_KEY_LENGTH = 160
MAX_BOUNDED_DEPTH = 6
MAX_SERIALIZED_RECORD_SIZE = 32_768
MAX_SERIALIZED_DECLARATION_SIZE = 262_144
MAX_SERIALIZED_REQUEST_SIZE = 393_216
MAX_SERIALIZED_RESULT_SIZE = 524_288
MAX_RESULT_SEQUENCE_ITEMS = 256
MAX_RESULT_MAPPING_ITEMS = 256
MAX_RESULT_DEPTH = 8


class ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError(
    Exception
):
    """Raised when a declaration result cannot be written lawfully."""


REQUIRED_BASIS_NON_CLAIMS = (
    "caller_supplied_dimension_result",
    "caller_supplied_candidate_result",
    "evaluator_reference_to_authority",
    "evaluator_reference_to_identity",
    "evaluator_reference_to_standing",
    "evaluator_reference_to_truth",
    "declarant_reference_to_authority",
    "declarant_reference_to_identity",
    "declarant_reference_to_standing",
    "declarant_reference_to_truth",
    "basis_items_to_established_truth",
    "basis_references_to_verified_provenance",
    "source_body_authorship_to_independent_custody",
    "declaration_readiness_to_operation_authorization",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "caller_supplied_dimension_result",
    "caller_supplied_candidate_result",
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "candidate_sufficiency_decided",
    "candidate_sufficiency_established",
    "candidate_insufficiency_established",
    "candidate_indeterminacy_established",
    "candidate_sufficiency_basis_separately_supplied",
    "candidate_sufficiency_basis_admitted_by_operation",
    "candidate_sufficiency_operation_created",
    "candidate_sufficiency_operation_authorized",
    "candidate_sufficiency_operation_recorded",
    "candidate_sufficiency_operation_result_recorded",
    "candidate_sufficiency_operation_executed",
    "candidate_sufficiency_operation_exhausted",
    "partial_dimension_evaluation_recorded",
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_attestation_boundary_created",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "continuity_memory_written",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "evaluator_reference_to_authority",
    "evaluator_reference_to_identity",
    "evaluator_reference_to_standing",
    "evaluator_reference_to_truth",
    "declarant_reference_to_authority",
    "declarant_reference_to_identity",
    "declarant_reference_to_standing",
    "declarant_reference_to_truth",
    "basis_items_to_established_truth",
    "basis_references_to_verified_provenance",
    "source_body_authorship_to_independent_custody",
    "declaration_readiness_to_operation_authorization",
    "repeated_declaration_permission_created",
    "reusable_declaration_route_created",
    "silent_declaration_replacement_authorized",
    "automatic_redeclaration_created",
    "declaration_debt_created",
    "declaration_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_declaration_result_preclaim": "DECLARATION_RESULT_PRECLAIMED",
        "request_declaration_ready_for_supply_preclaim": (
            "DECLARATION_RESULT_PRECLAIMED"
        ),
        "request_basis_separate_supply": (
            "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
        ),
        "request_basis_operation_admission": (
            "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
        ),
        "request_operation_execution": (
            "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
        ),
        "request_operation_exhaustion": (
            "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
        ),
        "request_dimension_result": (
            "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
        ),
        "request_candidate_sufficient": (
            "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
        ),
        "request_candidate_insufficient": (
            "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
        ),
        "request_candidate_indeterminate": (
            "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
        ),
        "request_receiver_attestation_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_attestation_support": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_answerable_receipt_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_support": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_authorization": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_establishment": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_recording": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_identity_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_relation_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_coupling_assignment": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_coupling_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_field_machinery_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_runtime_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_api_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_authority_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_standing_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_truth_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_output_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_action_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_synchronization_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_follow_on_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_follow_on_work_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_repeated_declaration_permission_creation": (
            "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
            "OBLIGATION_REQUESTED"
        ),
        "request_reusable_declaration_route_creation": (
            "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
            "OBLIGATION_REQUESTED"
        ),
        "request_silent_declaration_replacement": (
            "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
            "OBLIGATION_REQUESTED"
        ),
        "request_automatic_redeclaration": (
            "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
            "OBLIGATION_REQUESTED"
        ),
        "request_declaration_debt_creation": (
            "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
            "OBLIGATION_REQUESTED"
        ),
        "request_declaration_obligation_creation": (
            "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
            "OBLIGATION_REQUESTED"
        ),
        "request_repository_scan": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_file_discovery": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_affected_file_repair": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_affected_file_mutation": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_prior_unsupported_claim_validation": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_validation_enforcement": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INTENT",
        "DECLARATION_SPEC_REFERENCE_MISSING",
        "DECLARATION_SPEC_MARKER_MISSING",
        "SELECTED_WAITING_OPERATION_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_MAPPING",
        "REQUEST_VALUE_MISMATCH",
        "SELECTED_DECLARATION_IDENTITY_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
        "UPSTREAM_OPERATION_NOT_WAITING_FOR_BASIS",
        "UPSTREAM_OPERATION_RESULT_MISMATCH",
        "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
        "UPSTREAM_BOUNDARY_NOT_VALIDATED",
        "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_COMPLETE",
        "UPSTREAM_ATOMIC_GATE_ALREADY_PASSED",
        "UPSTREAM_OPERATION_ALREADY_RECORDED",
        "UPSTREAM_OPERATION_RESULT_ALREADY_RECORDED",
        "UPSTREAM_OPERATION_ALREADY_EXHAUSTED",
        "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
        "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
        "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "DECLARATION_RECORDS_NOT_MAPPING",
        "DECLARATION_DIMENSION_SET_MISMATCH",
        "DECLARATION_RECORD_NOT_MAPPING",
        "DECLARATION_RECORD_IDENTITY_MISMATCH",
        "DECLARATION_BASIS_ITEMS_INVALID",
        "DECLARATION_BASIS_REFERENCES_INVALID",
        "DECLARANT_REFERENCE_INVALID",
        "EVALUATOR_REFERENCE_INVALID",
        "DECLARATION_RULE_INPUTS_INVALID",
        "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
        "DECLARATION_NON_CONVERSION_STATEMENT_MISMATCH",
        "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
        "FALSE_INDEPENDENT_PREPARER_CLAIM",
        "FALSE_SEPARATE_CUSTODY_CLAIM",
        "DECLARATION_RESULT_PRECLAIMED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED",
        "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED",
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "PROHIBITED_REPEATED_REUSABLE_REPLACEMENT_REDECLARATION_DEBT_OR_"
        "OBLIGATION_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "EXPLICIT_BLOCK_REQUESTED",
        "WRITE_REFUSED",
    }
)

DECLARATION_SPEC_MARKER_CLASSES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Candidate Sufficiency Basis "
            "Declaration V0 Minimum Specification",
        ),
        "declaration_identity": (
            DECLARATION_ID,
            DECLARATION_TYPE,
            DECLARATION_SCOPE,
        ),
        "selected_operation_identity": (
            SELECTED_SUFFICIENCY_OPERATION_ID,
            SELECTED_SUFFICIENCY_OPERATION_TYPE,
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
        ),
        "dimension_set": SUFFICIENCY_DECLARATION_DIMENSION_IDS,
        "result_family": (
            DECLARATION_RESULT_READY_FOR_SUPPLY,
            DECLARATION_RESULT_REQUIRES_COMPLETE,
            DECLARATION_RESULT_NOT_EVALUATED,
        ),
        "outcome_family": OUTCOME_FAMILY,
        "authorship_posture": (
            "source_body_authored",
            "independent_preparer_claimed",
            "separate_custody_claimed_by_preparer",
        ),
        "non_conversion": (
            "Support posture declared is not",
            "Contradiction posture declared is not",
            "Unresolved posture declared is not",
            "Declaration is not operation supply.",
            "Preparation is not admission.",
        ),
    }
)

WAITING_WHAT_REMAINS_OPEN = (
    "separately supplied eight-dimension candidate-sufficiency basis",
    "actual candidate-sufficiency evaluation",
    "candidate-sufficiency result",
    "receiver-attestation boundary, only after candidate sufficient",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)

INCOMPLETE_WHAT_REMAINS_OPEN = (
    "complete eight-record candidate-sufficiency basis declaration",
    "candidate-sufficiency basis declaration live standing",
    "preparation-request declaration, if separately selected",
    "source-body preparation of the eight declaration records, if separately selected",
    "separate operation-request supply of the prepared basis",
    "actual candidate-sufficiency evaluation",
    "candidate-sufficiency result",
    "receiver-attestation boundary, only after candidate sufficient",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)

READY_WHAT_REMAINS_OPEN = (
    "preparation-request declaration, if separately selected",
    "source-body preparation record provenance, if separately recorded",
    "separate operation-request supply of the prepared basis",
    "actual candidate-sufficiency evaluation",
    "candidate-sufficiency result",
    "receiver-attestation boundary, only after candidate sufficient",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)

BLOCKED_ROUTES = (
    "declaration_to_operation_supply_or_admission",
    "declaration_to_dimension_or_candidate_result",
    "declaration_to_operation_execution_or_exhaustion",
    "declarant_or_evaluator_reference_to_authority_identity_standing_or_truth",
    "source_body_authorship_to_independent_custody",
    "declaration_to_receiver_attestation_receipt_or_presence",
    "declaration_to_downstream_standing",
    "declaration_to_repeated_reusable_replacement_or_automatic_redeclaration",
    "declaration_to_repository_repair_scan_discovery_or_validation",
    "declaration_to_contaminated_lineage_validation",
)

RESULT_SECTIONS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_metadata",
        "declared_receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_basis",
        "upstream_basis",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_records",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_checks",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_statement",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_non_meaning",
        "declaration_result_detail",
        "permitted_future_route",
        "blocked_routes",
        "what_remains_open",
        "non_claims",
        "outcome",
        "block",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_summary",
        "resolver_module",
        "result_version",
        "failed_check_count",
        "passed_check_count",
    }
)

DECLARATION_RECORD_FIELDS = frozenset(
    {
        "dimension_id",
        "receiver_side_answerable_basis_candidate_id",
        "selected_candidate_sufficiency_boundary_id",
        "selected_candidate_sufficiency_operation_id",
        "basis_items",
        "basis_references",
        "declarant_reference",
        "evaluator_reference",
        "support_postures",
        "contradiction_postures",
        "unresolved_postures",
        "basis_non_claims",
        "non_conversion_statement",
        "source_body_authored",
        "independent_preparer_claimed",
        "separate_custody_claimed_by_preparer",
    }
)

DECLARATION_RESULT_PRECLAIM_FIELDS = frozenset(
    {
        "candidate_sufficiency_basis_declaration_recorded",
        "candidate_sufficiency_basis_declaration_result_recorded",
        "candidate_sufficiency_basis_declaration_ready_for_supply",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_recorded",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_result_recorded",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_result",
        "declaration_result",
        "declaration_complete",
        "declaration_ready_for_supply",
        "outcome",
    }
)

SUPPLY_EXECUTION_PRECLAIM_FIELDS = frozenset(
    {
        "candidate_sufficiency_basis_separately_supplied",
        "candidate_sufficiency_basis_admitted_by_operation",
        "candidate_sufficiency_operation_executed",
        "candidate_sufficiency_operation_exhausted",
        "basis_separately_supplied",
        "basis_admitted",
        "operation_executed",
        "operation_exhausted",
        "operation_result",
    }
)

DIMENSION_CANDIDATE_PRECLAIM_FIELDS = frozenset(
    {
        "dimension_result",
        "dimension_results",
        "requested_dimension_result",
        "candidate_result",
        "requested_candidate_result",
        "receiver_side_answerable_basis_candidate_sufficient",
        "receiver_side_answerable_basis_candidate_insufficient",
        "receiver_side_answerable_basis_candidate_indeterminate",
        "candidate_sufficiency_decided",
        "candidate_sufficiency_established",
        "candidate_insufficiency_established",
        "candidate_indeterminacy_established",
    }
)

RECEIVER_PRESENCE_PRECLAIM_FIELDS = frozenset(
    {
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_answerable_receipt_present",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
    }
)

DOWNSTREAM_PRECLAIM_FIELDS = frozenset(
    set(REQUIRED_FALSE_NON_CLAIMS)
    - set(DIMENSION_CANDIDATE_PRECLAIM_FIELDS)
    - set(RECEIVER_PRESENCE_PRECLAIM_FIELDS)
    - set(SUPPLY_EXECUTION_PRECLAIM_FIELDS)
)

UPSTREAM_CANDIDATE_FALSE_POSTURES = (
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "candidate_sufficiency_decided",
    "candidate_sufficiency_established",
    "candidate_insufficiency_established",
    "candidate_indeterminacy_established",
)

UPSTREAM_RECEIVER_FALSE_POSTURES = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_attestation_boundary_created",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
)

UPSTREAM_REPEAT_AND_DOWNSTREAM_FALSE_POSTURES = (
    "repeated_candidate_sufficiency_operation_permission_created",
    "reusable_candidate_sufficiency_operation_route_created",
    "same_candidate_sufficiency_operation_rerun_authorized",
    "automatic_candidate_sufficiency_operation_retry_created",
    "candidate_sufficiency_operation_debt_created",
    "candidate_sufficiency_operation_obligation_created",
    "identity_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "continuity_memory_written",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)


def _exact_bool(value: Any) -> bool:
    return value is True or value is False


def _mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _as_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _display_path(value: Path | str) -> str:
    path = _as_path(value)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError):
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, "not_parseable"


def _serialized_size(value: Any) -> int | None:
    try:
        return len(
            json.dumps(
                value,
                ensure_ascii=True,
                sort_keys=True,
                allow_nan=False,
            ).encode("utf-8")
        )
    except (TypeError, ValueError):
        return None


def _bounded_value(value: Any, depth: int = 0) -> bool:
    if depth > MAX_BOUNDED_DEPTH:
        return False
    if value is None or isinstance(value, bool):
        return True
    if isinstance(value, int) and not isinstance(value, bool):
        return abs(value) <= 1_000_000_000_000
    if isinstance(value, float):
        return (
            value == value
            and abs(value) != float("inf")
            and abs(value) <= 1_000_000_000_000
        )
    if isinstance(value, str):
        return len(value) <= MAX_TEXT_LENGTH
    if isinstance(value, Mapping):
        return len(value) <= MAX_MAPPING_ITEMS and all(
            isinstance(key, str)
            and 0 < len(key) <= MAX_KEY_LENGTH
            and _bounded_value(nested, depth + 1)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return len(value) <= MAX_SEQUENCE_ITEMS and all(
            _bounded_value(item, depth + 1) for item in value
        )
    return False


def _bounded_result_value(value: Any, depth: int = 0) -> bool:
    if depth > MAX_RESULT_DEPTH:
        return False
    if value is None or isinstance(value, bool):
        return True
    if isinstance(value, int) and not isinstance(value, bool):
        return abs(value) <= 1_000_000_000_000
    if isinstance(value, float):
        return (
            value == value
            and abs(value) != float("inf")
            and abs(value) <= 1_000_000_000_000
        )
    if isinstance(value, str):
        return len(value) <= MAX_TEXT_LENGTH
    if isinstance(value, Mapping):
        return len(value) <= MAX_RESULT_MAPPING_ITEMS and all(
            isinstance(key, str)
            and 0 < len(key) <= MAX_KEY_LENGTH
            and _bounded_result_value(nested, depth + 1)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return len(value) <= MAX_RESULT_SEQUENCE_ITEMS and all(
            _bounded_result_value(item, depth + 1) for item in value
        )
    return False


def _bounded_non_empty_mapping(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value) and _bounded_value(value)


def _bounded_mapping_sequence(value: Any) -> bool:
    return (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes, bytearray))
        and 0 < len(value) <= MAX_SEQUENCE_ITEMS
        and all(_bounded_non_empty_mapping(item) for item in value)
    )


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "passed": passed}
    if not passed and code is not None:
        item["block_code"] = code
        item["failure_code"] = code
    return item


def _failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> None:
    checks.append(_check(name, False, code))


def _require(
    checks: list[dict[str, Any]],
    name: str,
    condition: bool,
    code: str,
    reason: str,
) -> tuple[str | None, str | None]:
    checks.append(_check(name, condition, code if not condition else None))
    if condition:
        return None, None
    return code, reason


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_basis_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_BASIS_NON_CLAIMS}


def _all_false_mapping(
    value: Any,
    required: Sequence[str],
    *,
    exact: bool = True,
) -> bool:
    if not isinstance(value, Mapping):
        return False
    if exact and set(value) != set(required):
        return False
    return all(value.get(key) is False for key in required)


def _marker_status(
    text: str,
    marker_classes: Mapping[str, Sequence[str]],
) -> dict[str, bool]:
    return {
        name: all(marker in text for marker in markers)
        for name, markers in marker_classes.items()
    }


def _expected_request_values() -> dict[str, str]:
    return {
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_id": DECLARATION_ID,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_type": DECLARATION_TYPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_version": DECLARATION_VERSION,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_scope": DECLARATION_SCOPE,
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_candidate_sufficiency_operation_type": (
            SELECTED_SUFFICIENCY_OPERATION_TYPE
        ),
        "selected_candidate_sufficiency_operation_version": (
            SELECTED_SUFFICIENCY_OPERATION_VERSION
        ),
        "selected_candidate_sufficiency_operation_scope": (
            SELECTED_SUFFICIENCY_OPERATION_SCOPE
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "selected_candidate_sufficiency_boundary_type": (
            SELECTED_SUFFICIENCY_BOUNDARY_TYPE
        ),
        "selected_candidate_reception_operation_id": (
            SELECTED_RECEPTION_OPERATION_ID
        ),
        "selected_candidate_evaluation_boundary_id": (
            SELECTED_EVALUATION_BOUNDARY_ID
        ),
        "selected_candidate_evaluation_operation_id": (
            SELECTED_EVALUATION_OPERATION_ID
        ),
    }


def _expected_request_paths() -> dict[str, str]:
    return {
        "governing_declaration_specification_path": str(
            GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_waiting_operation_artifact_path": str(
            SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            "intent",
            "declaration_records_supplied",
            "declaration_records",
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(_expected_request_paths()),
            *tuple(PROHIBITED_REQUEST_FLAGS),
        }
    )


def _find_mapping_key(value: Any, keys: set[str], depth: int = 0) -> str | None:
    if depth > MAX_BOUNDED_DEPTH:
        return None
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if key in keys:
                return str(key)
            if key in {"basis_non_claims", "declared_non_claims"}:
                continue
            found = _find_mapping_key(nested, keys, depth + 1)
            if found is not None:
                return found
    elif isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        for nested in value:
            found = _find_mapping_key(nested, keys, depth + 1)
            if found is not None:
                return found
    return None


def _preclaim_code(
    value: Mapping[str, Any],
    *,
    recursive: bool = True,
) -> tuple[str | None, str | None]:
    categories = (
        (
            DECLARATION_RESULT_PRECLAIM_FIELDS,
            "DECLARATION_RESULT_PRECLAIMED",
        ),
        (
            SUPPLY_EXECUTION_PRECLAIM_FIELDS,
            "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED",
        ),
        (
            DIMENSION_CANDIDATE_PRECLAIM_FIELDS,
            "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED",
        ),
        (
            RECEIVER_PRESENCE_PRECLAIM_FIELDS,
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
        ),
        (
            DOWNSTREAM_PRECLAIM_FIELDS,
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        ),
    )
    for keys, code in categories:
        found = (
            _find_mapping_key(value, set(keys))
            if recursive
            else next((str(key) for key in value if key in keys), None)
        )
        if found is not None:
            return code, found
    return None, None


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    size = _serialized_size(request)
    if (
        size is None
        or size > MAX_SERIALIZED_REQUEST_SIZE
        or not _bounded_value(request)
    ):
        _failure(checks, "request_is_bounded", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "request is not bounded JSON material"

    preclaim_code, preclaim_field = _preclaim_code(request, recursive=False)
    if preclaim_code is not None:
        _failure(checks, "request_contains_no_result_preclaim", preclaim_code)
        return preclaim_code, f"{preclaim_field} is a prohibited preclaim"

    unknown = set(request) - _request_allowed_keys()
    if unknown:
        _failure(checks, "request_has_only_supported_fields", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "request contains unsupported fields"

    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        _failure(checks, "intent_supported", "UNSUPPORTED_INTENT")
        return "UNSUPPORTED_INTENT", "intent is unsupported"
    if intent == INTENT_BLOCK:
        _failure(checks, "intent_not_explicit_block", "EXPLICIT_BLOCK_REQUESTED")
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent"

    declaration_keys = {
        key
        for key in _expected_request_values()
        if "sufficiency_basis_declaration_" in key
    }
    operation_keys = {
        key
        for key in _expected_request_values()
        if key.startswith("selected_candidate_sufficiency_operation_")
    }
    candidate_keys = {
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "selected_candidate_reception_operation_id",
        "selected_candidate_evaluation_boundary_id",
        "selected_candidate_evaluation_operation_id",
    }
    boundary_keys = {
        "selected_candidate_sufficiency_boundary_id",
        "selected_candidate_sufficiency_boundary_type",
    }
    for key, expected in _expected_request_values().items():
        if request.get(key) == expected:
            continue
        if key in declaration_keys:
            code = "SELECTED_DECLARATION_IDENTITY_MISMATCH"
        elif key in operation_keys:
            code = "SELECTED_OPERATION_IDENTITY_MISMATCH"
        elif key in boundary_keys:
            code = "SELECTED_BOUNDARY_IDENTITY_MISMATCH"
        elif key in candidate_keys:
            code = "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
        else:
            code = "REQUEST_VALUE_MISMATCH"
        _failure(checks, f"request_{key}_matches", code)
        return code, f"{key} does not match the selected declaration line"

    for key, expected in _expected_request_paths().items():
        if request.get(key) != expected:
            _failure(checks, f"request_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return (
                "REQUEST_VALUE_MISMATCH",
                f"{key} must reference the exact selected repo-local path",
            )

    supplied = request.get("declaration_records_supplied")
    if not _exact_bool(supplied):
        _failure(
            checks,
            "declaration_records_supplied_is_boolean",
            "REQUEST_VALUE_MISMATCH",
        )
        return (
            "REQUEST_VALUE_MISMATCH",
            "declaration_records_supplied must be boolean",
        )

    if not _all_false_mapping(
        request.get("declared_non_claims"),
        REQUIRED_FALSE_NON_CLAIMS,
    ):
        _failure(
            checks,
            "declared_non_claims_are_canonical_false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims are missing, additional, malformed, or flipped",
        )

    for key, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(key)
        if value is True:
            _failure(checks, f"{key}_not_requested", code)
            return code, f"{key} is prohibited"
        if value is not False:
            _failure(checks, f"{key}_is_false", "REQUEST_VALUE_MISMATCH")
            return "REQUEST_VALUE_MISMATCH", f"{key} must be false"

    records = request.get("declaration_records")
    if supplied is False and records is not None:
        _failure(
            checks,
            "declaration_records_match_supplied_posture",
            "REQUEST_VALUE_MISMATCH",
        )
        return (
            "REQUEST_VALUE_MISMATCH",
            "declaration records are present while supplied posture is false",
        )
    if supplied is True and records is None:
        _failure(
            checks,
            "declaration_records_match_supplied_posture",
            "DECLARATION_RECORDS_NOT_MAPPING",
        )
        return (
            "DECLARATION_RECORDS_NOT_MAPPING",
            "supplied declaration records are absent",
        )

    checks.append(_check("request_is_bounded", True))
    return None, None


def _validate_upstream(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    upstream: dict[str, Any] = {
        "governing_paths": {
            "governing_declaration_specification_path": _display_path(
                GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH
            ),
            "selected_waiting_operation_artifact_path": _display_path(
                SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
        },
        "marker_validation": {},
        "complete_waiting_operation_artifact_omitted": True,
        "complete_upstream_checks_omitted": True,
    }

    spec_text, error = _read_text(
        GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH
    )
    if error is not None or spec_text is None:
        _failure(
            checks,
            "declaration_specification_exists",
            "DECLARATION_SPEC_REFERENCE_MISSING",
        )
        return (
            upstream,
            "DECLARATION_SPEC_REFERENCE_MISSING",
            "governing declaration specification is unavailable",
        )
    markers = _marker_status(spec_text, DECLARATION_SPEC_MARKER_CLASSES)
    upstream["marker_validation"]["governing_declaration_specification"] = (
        markers
    )
    if not all(markers.values()):
        _failure(
            checks,
            "declaration_specification_markers_present",
            "DECLARATION_SPEC_MARKER_MISSING",
        )
        return (
            upstream,
            "DECLARATION_SPEC_MARKER_MISSING",
            "governing declaration specification markers are incomplete",
        )
    checks.append(_check("declaration_specification_markers_present", True))

    artifact, error = _read_json(
        SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
    )
    if error in {"not_a_file", "unreadable"}:
        _failure(
            checks,
            "selected_waiting_operation_artifact_exists",
            "SELECTED_WAITING_OPERATION_ARTIFACT_REFERENCE_MISSING",
        )
        return (
            upstream,
            "SELECTED_WAITING_OPERATION_ARTIFACT_REFERENCE_MISSING",
            "selected waiting-operation artifact is unavailable",
        )
    if error is not None:
        _failure(
            checks,
            "selected_waiting_operation_artifact_parseable",
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_PARSEABLE",
        )
        return (
            upstream,
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_PARSEABLE",
            "selected waiting-operation artifact is not parseable",
        )
    if not isinstance(artifact, Mapping):
        _failure(
            checks,
            "selected_waiting_operation_artifact_mapping",
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_MAPPING",
        )
        return (
            upstream,
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_MAPPING",
            "selected waiting-operation artifact is not a mapping",
        )

    operation = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation"
    )
    dimensions = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_"
        "operation_dimensions"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_summary"
    )
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, dimensions, summary, non_claims)
    ):
        _failure(
            checks,
            "selected_waiting_operation_artifact_shape",
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_MAPPING",
        )
        return (
            upstream,
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_MAPPING",
            "selected waiting-operation artifact shape is incomplete",
        )

    root_requirements = (
        (
            "resolver_module",
            artifact.get("resolver_module")
            == SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE,
            "SELECTED_OPERATION_IDENTITY_MISMATCH",
            "waiting-operation resolver module does not match",
        ),
        (
            "result_version",
            artifact.get("result_version") == RESULT_VERSION,
            "SELECTED_OPERATION_IDENTITY_MISMATCH",
            "waiting-operation result version does not match",
        ),
        (
            "outcome",
            artifact.get("outcome")
            == SELECTED_SUFFICIENCY_OPERATION_OUTCOME_REQUIRED,
            "UPSTREAM_OPERATION_NOT_WAITING_FOR_BASIS",
            "upstream operation is not waiting for sufficiency basis",
        ),
        (
            "failed_check_count",
            artifact.get("failed_check_count") == 0,
            "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
            "upstream operation has failed checks",
        ),
    )
    for name, condition, code, reason in root_requirements:
        failure_code, failure_reason = _require(
            checks,
            f"upstream_{name}",
            condition,
            code,
            reason,
        )
        if failure_code is not None:
            return upstream, failure_code, failure_reason

    operation_identity = {
        "operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "operation_type": SELECTED_SUFFICIENCY_OPERATION_TYPE,
        "operation_version": SELECTED_SUFFICIENCY_OPERATION_VERSION,
        "operation_scope": SELECTED_SUFFICIENCY_OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_type": (
            SELECTED_SUFFICIENCY_OPERATION_TYPE
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_version": (
            SELECTED_SUFFICIENCY_OPERATION_VERSION
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_scope": (
            SELECTED_SUFFICIENCY_OPERATION_SCOPE
        ),
    }
    for field, expected in operation_identity.items():
        code, reason = _require(
            checks,
            f"upstream_operation_{field}",
            operation.get(field) == expected,
            "SELECTED_OPERATION_IDENTITY_MISMATCH",
            f"upstream operation identity does not match {field}",
        )
        if code is not None:
            return upstream, code, reason

    candidate_identity = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": (
            SELECTED_RECEPTION_OPERATION_ID
        ),
        "selected_candidate_evaluation_boundary_id": (
            SELECTED_EVALUATION_BOUNDARY_ID
        ),
        "selected_candidate_evaluation_operation_id": (
            SELECTED_EVALUATION_OPERATION_ID
        ),
    }
    for field, expected in candidate_identity.items():
        code, reason = _require(
            checks,
            f"upstream_candidate_{field}",
            operation.get(field) == expected,
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            f"upstream selected candidate identity does not match {field}",
        )
        if code is not None:
            return upstream, code, reason

    boundary_identity = {
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "selected_candidate_sufficiency_boundary_type": (
            SELECTED_SUFFICIENCY_BOUNDARY_TYPE
        ),
    }
    for field, expected in boundary_identity.items():
        code, reason = _require(
            checks,
            f"upstream_boundary_{field}",
            operation.get(field) == expected,
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            f"upstream selected boundary identity does not match {field}",
        )
        if code is not None:
            return upstream, code, reason

    operation_results = (
        operation.get("operation_result"),
        operation.get("candidate_sufficiency_operation_result"),
        operation.get(
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_result"
        ),
    )
    code, reason = _require(
        checks,
        "upstream_operation_result",
        all(
            value == SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
            for value in operation_results
        ),
        "UPSTREAM_OPERATION_RESULT_MISMATCH",
        "upstream operation result does not require sufficiency basis",
    )
    if code is not None:
        return upstream, code, reason

    code, reason = _require(
        checks,
        "upstream_boundary_validated",
        summary.get("upstream_boundary_validated") is True,
        "UPSTREAM_BOUNDARY_NOT_VALIDATED",
        "upstream operation did not validate its selected boundary",
    )
    if code is not None:
        return upstream, code, reason

    code, reason = _require(
        checks,
        "upstream_basis_not_supplied_or_complete",
        operation.get("sufficiency_basis_supplied") is False
        and operation.get("sufficiency_basis_complete") is False
        and summary.get("sufficiency_basis_supplied") is False
        and summary.get("sufficiency_basis_complete") is False,
        "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_COMPLETE",
        "upstream basis is already supplied or complete",
    )
    if code is not None:
        return upstream, code, reason

    code, reason = _require(
        checks,
        "upstream_atomic_gate_not_passed",
        operation.get("atomic_sufficiency_basis_gate_passed") is False
        and summary.get("atomic_sufficiency_basis_gate_passed") is False,
        "UPSTREAM_ATOMIC_GATE_ALREADY_PASSED",
        "upstream atomic sufficiency-basis gate already passed",
    )
    if code is not None:
        return upstream, code, reason

    operation_postures = (
        (
            "candidate_sufficiency_operation_recorded",
            "UPSTREAM_OPERATION_ALREADY_RECORDED",
        ),
        (
            "candidate_sufficiency_operation_result_recorded",
            "UPSTREAM_OPERATION_RESULT_ALREADY_RECORDED",
        ),
        (
            "candidate_sufficiency_operation_exhausted",
            "UPSTREAM_OPERATION_ALREADY_EXHAUSTED",
        ),
    )
    for field, failure_code in operation_postures:
        code, reason = _require(
            checks,
            f"upstream_{field}_false",
            operation.get(field) is False,
            failure_code,
            f"upstream {field} is already true",
        )
        if code is not None:
            return upstream, code, reason

    for field in UPSTREAM_CANDIDATE_FALSE_POSTURES:
        code, reason = _require(
            checks,
            f"upstream_candidate_{field}_false",
            operation.get(field) is False,
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            f"upstream candidate result posture is present: {field}",
        )
        if code is not None:
            return upstream, code, reason

    if set(dimensions) != set(SUFFICIENCY_DECLARATION_DIMENSION_IDS):
        _failure(
            checks,
            "upstream_dimension_set_exact",
            "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
        )
        return (
            upstream,
            "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
            "upstream dimension set does not match the exact waiting set",
        )
    for dimension_id in SUFFICIENCY_DECLARATION_DIMENSION_IDS:
        dimension = dimensions.get(dimension_id)
        waiting = (
            isinstance(dimension, Mapping)
            and dimension.get("dimension_id") == dimension_id
            and dimension.get("dimension_result") == "NOT_EVALUATED"
            and dimension.get("dimension_evaluated") is False
            and dimension.get("dimension_established") is False
        )
        code, reason = _require(
            checks,
            f"upstream_dimension_{dimension_id}_not_evaluated",
            waiting,
            "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
            f"upstream dimension is not in exact waiting posture: {dimension_id}",
        )
        if code is not None:
            return upstream, code, reason

    for field in UPSTREAM_RECEIVER_FALSE_POSTURES:
        code, reason = _require(
            checks,
            f"upstream_receiver_{field}_false",
            operation.get(field) is False,
            "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            f"upstream receiver, receipt, or presence posture is present: {field}",
        )
        if code is not None:
            return upstream, code, reason

    for field in UPSTREAM_REPEAT_AND_DOWNSTREAM_FALSE_POSTURES:
        exact_false = operation.get(field) is False and non_claims.get(field) is False
        code, reason = _require(
            checks,
            f"upstream_downstream_{field}_false",
            exact_false,
            "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            f"upstream rerun, retry, debt, obligation, or downstream posture "
            f"is present: {field}",
        )
        if code is not None:
            return upstream, code, reason

    open_state = artifact.get("what_remains_open")
    stale_markers = (
        "candidate-sufficiency operation specification",
        "candidate-sufficiency operation resolver",
        "candidate-sufficiency operation test",
        "waiting artifact",
    )
    open_valid = (
        isinstance(open_state, list)
        and tuple(open_state) == WAITING_WHAT_REMAINS_OPEN
        and bool(open_state)
        and open_state[0]
        == "separately supplied eight-dimension candidate-sufficiency basis"
        and not any(
            marker in str(item).lower()
            for marker in stale_markers
            for item in open_state
        )
    )
    code, reason = _require(
        checks,
        "upstream_what_remains_open_exact",
        open_valid,
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "upstream waiting open state is stale or mismatched",
    )
    if code is not None:
        return upstream, code, reason

    upstream.update(
        {
            "selected_waiting_operation_metadata": {
                "resolver_module": artifact.get("resolver_module"),
                "result_version": artifact.get("result_version"),
                "outcome": artifact.get("outcome"),
                "failed_check_count": artifact.get("failed_check_count"),
                "passed_check_count": artifact.get("passed_check_count"),
            },
            "selected_waiting_operation_identity": {
                "operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
                "operation_type": SELECTED_SUFFICIENCY_OPERATION_TYPE,
                "operation_version": SELECTED_SUFFICIENCY_OPERATION_VERSION,
                "operation_scope": SELECTED_SUFFICIENCY_OPERATION_SCOPE,
                "operation_result": (
                    SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
                ),
                "candidate_id": CANDIDATE_ID,
                "candidate_type": CANDIDATE_TYPE,
                "candidate_scope": CANDIDATE_SCOPE,
                "sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
                "reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
                "evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
                "evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
            },
            "waiting_posture_validation": {
                "upstream_boundary_validated": True,
                "sufficiency_basis_supplied": False,
                "sufficiency_basis_complete": False,
                "atomic_sufficiency_basis_gate_passed": False,
                "candidate_sufficiency_operation_recorded": False,
                "candidate_sufficiency_operation_result_recorded": False,
                "candidate_sufficiency_operation_exhausted": False,
                "candidate_results_false": True,
                "all_eight_dimensions_not_evaluated": True,
                "receiver_receipt_presence_false": True,
                "rerun_retry_debt_obligation_and_downstream_false": True,
                "what_remains_open_exact": True,
            },
        }
    )
    checks.append(_check("selected_waiting_operation_posture_valid", True))
    return upstream, None, None


def _posture_mapping_valid(value: Any, expected_key: str) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == {expected_key}
        and _exact_bool(value.get(expected_key))
    )


def _validate_declaration_record(
    dimension_id: str,
    record: Any,
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    if not isinstance(record, Mapping):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_mapping",
            "DECLARATION_RECORD_NOT_MAPPING",
        )
        return (
            "DECLARATION_RECORD_NOT_MAPPING",
            f"{dimension_id} declaration record is not a mapping",
        )

    size = _serialized_size(record)
    if (
        size is None
        or size > MAX_SERIALIZED_RECORD_SIZE
        or not _bounded_value(record)
    ):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_bounded",
            "DECLARATION_RECORD_NOT_MAPPING",
        )
        return (
            "DECLARATION_RECORD_NOT_MAPPING",
            f"{dimension_id} declaration record is not bounded JSON material",
        )

    preclaim_code, preclaim_field = _preclaim_code(record)
    if preclaim_code is not None:
        if preclaim_code == "DECLARATION_RESULT_PRECLAIMED":
            code = "DECLARATION_RESULT_PRECLAIMED"
        elif preclaim_code in {
            "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED",
            "PROHIBITED_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED",
        }:
            code = "RESULT_POSTURE_PRECLAIMED"
        else:
            code = preclaim_code
        _failure(
            checks,
            f"declaration_record_{dimension_id}_no_preclaim",
            code,
        )
        return code, f"{dimension_id} contains prohibited {preclaim_field}"

    if set(record) != set(DECLARATION_RECORD_FIELDS):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_exact_fields",
            "DECLARATION_RECORD_NOT_MAPPING",
        )
        return (
            "DECLARATION_RECORD_NOT_MAPPING",
            f"{dimension_id} declaration record fields do not match",
        )

    identity = {
        "dimension_id": dimension_id,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
    }
    if any(record.get(key) != expected for key, expected in identity.items()):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_identity",
            "DECLARATION_RECORD_IDENTITY_MISMATCH",
        )
        return (
            "DECLARATION_RECORD_IDENTITY_MISMATCH",
            f"{dimension_id} declaration record identity does not match",
        )

    if not _bounded_mapping_sequence(record.get("basis_items")):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_basis_items",
            "DECLARATION_BASIS_ITEMS_INVALID",
        )
        return (
            "DECLARATION_BASIS_ITEMS_INVALID",
            f"{dimension_id} basis items are not bounded non-empty mappings",
        )
    if not _bounded_mapping_sequence(record.get("basis_references")):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_basis_references",
            "DECLARATION_BASIS_REFERENCES_INVALID",
        )
        return (
            "DECLARATION_BASIS_REFERENCES_INVALID",
            f"{dimension_id} basis references are not bounded non-empty mappings",
        )
    if not _bounded_non_empty_mapping(record.get("declarant_reference")):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_declarant_reference",
            "DECLARANT_REFERENCE_INVALID",
        )
        return (
            "DECLARANT_REFERENCE_INVALID",
            f"{dimension_id} declarant reference is invalid",
        )
    if not _bounded_non_empty_mapping(record.get("evaluator_reference")):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_evaluator_reference",
            "EVALUATOR_REFERENCE_INVALID",
        )
        return (
            "EVALUATOR_REFERENCE_INVALID",
            f"{dimension_id} evaluator reference is invalid",
        )

    rule_keys = DIMENSION_RULE_KEYS[dimension_id]
    for field, rule_name in (
        ("support_postures", "support"),
        ("contradiction_postures", "contradiction"),
        ("unresolved_postures", "unresolved"),
    ):
        if not _posture_mapping_valid(
            record.get(field),
            rule_keys[rule_name],
        ):
            _failure(
                checks,
                f"declaration_record_{dimension_id}_{field}",
                "DECLARATION_RULE_INPUTS_INVALID",
            )
            return (
                "DECLARATION_RULE_INPUTS_INVALID",
                f"{dimension_id} {field} does not contain the exact boolean rule input",
            )

    if not _all_false_mapping(
        record.get("basis_non_claims"),
        REQUIRED_BASIS_NON_CLAIMS,
    ):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_basis_non_claims",
            "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return (
            "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            f"{dimension_id} basis non-claims are missing or flipped",
        )

    if (
        record.get("non_conversion_statement")
        != DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
    ):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_non_conversion",
            "DECLARATION_NON_CONVERSION_STATEMENT_MISMATCH",
        )
        return (
            "DECLARATION_NON_CONVERSION_STATEMENT_MISMATCH",
            f"{dimension_id} non-conversion statement does not match",
        )

    authorship_fields = (
        "source_body_authored",
        "independent_preparer_claimed",
        "separate_custody_claimed_by_preparer",
    )
    if not all(_exact_bool(record.get(field)) for field in authorship_fields):
        _failure(
            checks,
            f"declaration_record_{dimension_id}_authorship_boolean",
            "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
        )
        return (
            "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
            f"{dimension_id} authorship posture is not explicitly boolean",
        )
    if record.get("independent_preparer_claimed") is True:
        _failure(
            checks,
            f"declaration_record_{dimension_id}_no_independent_preparer_claim",
            "FALSE_INDEPENDENT_PREPARER_CLAIM",
        )
        return (
            "FALSE_INDEPENDENT_PREPARER_CLAIM",
            f"{dimension_id} falsely claims an independent preparer",
        )
    if record.get("separate_custody_claimed_by_preparer") is True:
        _failure(
            checks,
            f"declaration_record_{dimension_id}_no_separate_custody_claim",
            "FALSE_SEPARATE_CUSTODY_CLAIM",
        )
        return (
            "FALSE_SEPARATE_CUSTODY_CLAIM",
            f"{dimension_id} falsely claims separate custody",
        )

    checks.append(
        _check(f"declaration_record_{dimension_id}_structurally_valid", True)
    )
    return None, None


def _validate_declaration_records(
    records: Any,
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, bool, list[str]]:
    missing: list[str] = []
    if not isinstance(records, Mapping):
        _failure(
            checks,
            "declaration_records_mapping",
            "DECLARATION_RECORDS_NOT_MAPPING",
        )
        return (
            "DECLARATION_RECORDS_NOT_MAPPING",
            "declaration records are not a mapping",
            False,
            missing,
        )

    size = _serialized_size(records)
    if (
        size is None
        or size > MAX_SERIALIZED_DECLARATION_SIZE
        or not _bounded_value(records)
    ):
        _failure(
            checks,
            "declaration_records_bounded",
            "DECLARATION_RECORDS_NOT_MAPPING",
        )
        return (
            "DECLARATION_RECORDS_NOT_MAPPING",
            "declaration records exceed bounded structure",
            False,
            missing,
        )

    unknown = set(records) - set(SUFFICIENCY_DECLARATION_DIMENSION_IDS)
    if unknown:
        _failure(
            checks,
            "declaration_dimension_set_known",
            "DECLARATION_DIMENSION_SET_MISMATCH",
        )
        return (
            "DECLARATION_DIMENSION_SET_MISMATCH",
            "declaration contains unsupported dimension records",
            False,
            missing,
        )

    for dimension_id in SUFFICIENCY_DECLARATION_DIMENSION_IDS:
        if dimension_id not in records:
            missing.append(dimension_id)
            continue
        code, reason = _validate_declaration_record(
            dimension_id,
            records.get(dimension_id),
            checks,
        )
        if code is not None:
            return code, reason, False, missing

    complete = not missing and set(records) == set(
        SUFFICIENCY_DECLARATION_DIMENSION_IDS
    )
    if complete:
        checks.append(
            _check("declaration_exact_eight_record_set_complete", True)
        )
    else:
        checks.append(
            _check("declaration_partial_material_lawfully_incomplete", True)
        )
    return None, None, complete, missing


def _record_summaries(records: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(records, Mapping):
        return {}
    summaries: dict[str, dict[str, Any]] = {}
    for dimension_id in SUFFICIENCY_DECLARATION_DIMENSION_IDS:
        record = records.get(dimension_id)
        if not isinstance(record, Mapping):
            continue
        items = record.get("basis_items")
        references = record.get("basis_references")
        support = record.get("support_postures")
        contradiction = record.get("contradiction_postures")
        unresolved = record.get("unresolved_postures")
        rule_keys = DIMENSION_RULE_KEYS[dimension_id]
        summaries[dimension_id] = {
            "dimension_id": dimension_id,
            "basis_item_count": (
                len(items)
                if isinstance(items, Sequence)
                and not isinstance(items, (str, bytes, bytearray))
                else None
            ),
            "basis_reference_count": (
                len(references)
                if isinstance(references, Sequence)
                and not isinstance(references, (str, bytes, bytearray))
                else None
            ),
            "declarant_reference_supplied": _bounded_non_empty_mapping(
                record.get("declarant_reference")
            ),
            "evaluator_reference_supplied": _bounded_non_empty_mapping(
                record.get("evaluator_reference")
            ),
            "support_key_names": (
                [rule_keys["support"]]
                if isinstance(support, Mapping)
                else []
            ),
            "contradiction_key_names": (
                [rule_keys["contradiction"]]
                if isinstance(contradiction, Mapping)
                else []
            ),
            "unresolved_key_names": (
                [rule_keys["unresolved"]]
                if isinstance(unresolved, Mapping)
                else []
            ),
            "basis_non_claims_validated": _all_false_mapping(
                record.get("basis_non_claims"),
                REQUIRED_BASIS_NON_CLAIMS,
            ),
            "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
            "selected_candidate_sufficiency_boundary_id": (
                SELECTED_SUFFICIENCY_BOUNDARY_ID
            ),
            "selected_candidate_sufficiency_operation_id": (
                SELECTED_SUFFICIENCY_OPERATION_ID
            ),
            "source_body_authored": (
                record.get("source_body_authored")
                if _exact_bool(record.get("source_body_authored"))
                else None
            ),
            "independent_preparer_claimed": (
                record.get("independent_preparer_claimed")
                if _exact_bool(record.get("independent_preparer_claimed"))
                else None
            ),
            "separate_custody_claimed_by_preparer": (
                record.get("separate_custody_claimed_by_preparer")
                if _exact_bool(
                    record.get("separate_custody_claimed_by_preparer")
                )
                else None
            ),
            "complete_declaration_record_omitted": True,
        }
    return summaries


def _declaration_state(
    outcome: str,
    declaration_result: str,
    *,
    records_supplied: bool,
    complete: bool,
    record_count: int,
) -> dict[str, Any]:
    ready = outcome == OUTCOME_RECORDED and complete
    state: dict[str, Any] = {
        "declaration_id": DECLARATION_ID,
        "declaration_type": DECLARATION_TYPE,
        "declaration_version": DECLARATION_VERSION,
        "declaration_scope": DECLARATION_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_id": DECLARATION_ID,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_type": DECLARATION_TYPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_version": DECLARATION_VERSION,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_scope": DECLARATION_SCOPE,
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_candidate_sufficiency_operation_type": (
            SELECTED_SUFFICIENCY_OPERATION_TYPE
        ),
        "selected_candidate_sufficiency_operation_version": (
            SELECTED_SUFFICIENCY_OPERATION_VERSION
        ),
        "selected_candidate_sufficiency_operation_scope": (
            SELECTED_SUFFICIENCY_OPERATION_SCOPE
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "selected_candidate_sufficiency_boundary_type": (
            SELECTED_SUFFICIENCY_BOUNDARY_TYPE
        ),
        "selected_candidate_reception_operation_id": (
            SELECTED_RECEPTION_OPERATION_ID
        ),
        "selected_candidate_evaluation_boundary_id": (
            SELECTED_EVALUATION_BOUNDARY_ID
        ),
        "selected_candidate_evaluation_operation_id": (
            SELECTED_EVALUATION_OPERATION_ID
        ),
        "declaration_result": declaration_result,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_result": declaration_result,
        "declaration_records_supplied": records_supplied,
        "declaration_record_count": record_count,
        "declaration_dimension_ids": list(
            SUFFICIENCY_DECLARATION_DIMENSION_IDS
        ),
        "declaration_complete": ready,
        "candidate_sufficiency_basis_declaration_recorded": ready,
        "candidate_sufficiency_basis_declaration_result_recorded": ready,
        "candidate_sufficiency_basis_declaration_ready_for_supply": ready,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_recorded": ready,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_result_recorded": ready,
        "candidate_sufficiency_basis_separately_supplied": False,
        "candidate_sufficiency_basis_admitted_by_operation": False,
        "candidate_sufficiency_operation_executed": False,
        "candidate_sufficiency_operation_exhausted": False,
        "dimension_results_derived": False,
        "candidate_result_derived": False,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }
    state.update(_canonical_non_claims())
    return state


def _what_remains_open(outcome: str) -> list[str]:
    if outcome == OUTCOME_RECORDED:
        return list(READY_WHAT_REMAINS_OPEN)
    return list(INCOMPLETE_WHAT_REMAINS_OPEN)


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    declaration = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration"
    )
    records = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_records"
    )
    upstream = result.get("upstream_basis")
    declaration = declaration if isinstance(declaration, Mapping) else {}
    records = records if isinstance(records, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    summaries = records.get("record_summaries")
    summaries = summaries if isinstance(summaries, Mapping) else {}
    source_body_count = sum(
        record.get("source_body_authored") is True
        for record in summaries.values()
        if isinstance(record, Mapping)
    )
    non_source_body_count = sum(
        record.get("source_body_authored") is False
        for record in summaries.values()
        if isinstance(record, Mapping)
    )
    return {
        "outcome": result.get("outcome"),
        "declaration_result": declaration.get("declaration_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "declaration_identity": {
            "declaration_id": declaration.get("declaration_id"),
            "declaration_type": declaration.get("declaration_type"),
            "declaration_version": declaration.get("declaration_version"),
            "declaration_scope": declaration.get("declaration_scope"),
        },
        "selected_identity": {
            "candidate_id": declaration.get(
                "receiver_side_answerable_basis_candidate_id"
            ),
            "sufficiency_boundary_id": declaration.get(
                "selected_candidate_sufficiency_boundary_id"
            ),
            "sufficiency_operation_id": declaration.get(
                "selected_candidate_sufficiency_operation_id"
            ),
        },
        "upstream_waiting_operation_validated": (
            upstream.get("waiting_posture_validation", {}).get(
                "what_remains_open_exact"
            )
            is True
            if isinstance(
                upstream.get("waiting_posture_validation"), Mapping
            )
            else False
        ),
        "declaration_records_supplied": declaration.get(
            "declaration_records_supplied"
        ),
        "declaration_complete": declaration.get("declaration_complete"),
        "declaration_record_count": declaration.get(
            "declaration_record_count"
        ),
        "declaration_dimension_ids": copy.deepcopy(
            declaration.get("declaration_dimension_ids", [])
        ),
        "declaration_ready_for_supply": declaration.get(
            "candidate_sufficiency_basis_declaration_ready_for_supply"
        ),
        "supply_admission_execution_exhaustion_postures": {
            key: declaration.get(key)
            for key in (
                "candidate_sufficiency_basis_separately_supplied",
                "candidate_sufficiency_basis_admitted_by_operation",
                "candidate_sufficiency_operation_executed",
                "candidate_sufficiency_operation_exhausted",
            )
        },
        "authorship_posture_counts": {
            "source_body_authored": source_body_count,
            "non_source_body_authored": non_source_body_count,
            "independent_preparer_claimed": 0,
            "separate_custody_claimed_by_preparer": 0,
        },
        "candidate_receiver_receipt_presence_route_and_downstream_locks_false": (
            all(
                declaration.get(key) is False
                for key in REQUIRED_FALSE_NON_CLAIMS
            )
        ),
        "complete_declaration_content_omitted": records.get(
            "complete_declaration_content_omitted"
        ),
        "governing_paths": copy.deepcopy(
            upstream.get("governing_paths", {})
        ),
        "marker_validation": copy.deepcopy(
            upstream.get("marker_validation", {})
        ),
        "non_claims_canonical_false": (
            _all_false_mapping(
                result.get("non_claims"),
                REQUIRED_FALSE_NON_CLAIMS,
            )
        ),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    declaration_result: str,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    records: Mapping[str, Any] | None = None,
    complete: bool = False,
    missing: Sequence[str] = (),
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    records_supplied = request.get("declaration_records_supplied") is True
    summaries = _record_summaries(records)
    ready_complete = outcome == OUTCOME_RECORDED and complete
    state = _declaration_state(
        outcome,
        declaration_result,
        records_supplied=records_supplied,
        complete=ready_complete,
        record_count=len(summaries),
    )
    declared = {
        "intent": (
            request.get("intent")
            if request.get("intent") in SUPPORTED_INTENTS
            else None
        ),
        "declaration_records_supplied": (
            request.get("declaration_records_supplied")
            if _exact_bool(request.get("declaration_records_supplied"))
            else None
        ),
        **_expected_request_values(),
        **_expected_request_paths(),
        "request_identity_values_validated": all(
            request.get(key) == expected
            for key, expected in {
                **_expected_request_values(),
                **_expected_request_paths(),
            }.items()
        ),
    }
    declared["complete_declaration_records_omitted"] = True
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_metadata": {
            "declaration_id": DECLARATION_ID,
            "declaration_type": DECLARATION_TYPE,
            "declaration_version": DECLARATION_VERSION,
            "declaration_scope": DECLARATION_SCOPE,
        },
        "declared_receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_basis": declared,
        "upstream_basis": copy.deepcopy(dict(upstream or {})),
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration": state,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_records": {
            "declaration_records_supplied": records_supplied,
            "declaration_complete": ready_complete,
            "declaration_record_count": len(summaries),
            "declaration_record_ids": [
                dimension_id
                for dimension_id in SUFFICIENCY_DECLARATION_DIMENSION_IDS
                if dimension_id in summaries
            ],
            "missing_declaration_record_ids": list(missing),
            "record_summaries": summaries,
            "complete_declaration_content_omitted": True,
            "complete_basis_items_omitted": True,
            "complete_basis_references_omitted": True,
            "declarant_reference_content_omitted": True,
            "evaluator_reference_content_omitted": True,
            "raw_candidate_material_omitted": True,
            "capture_material_omitted": True,
        },
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_checks": copy.deepcopy(checks),
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_statement": {
            "one_selected_waiting_operation_consumed_as_upstream_standing": True,
            "waiting_operation_not_reopened": True,
            "waiting_operation_not_rerun": True,
            "declaration_is_not_operation_supply": True,
            "preparation_is_not_admission": True,
            "basis_record_is_not_dimension_result": True,
            "declaration_readiness_is_not_operation_authorization": True,
            "no_dimension_result_accepted": True,
            "no_candidate_result_accepted": True,
            "source_body_authorship_not_independent_custody": True,
            "declaration_ready_for_later_separate_supply_only": True,
            "result_level_non_claims_canonical_false": True,
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
        },
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_non_meaning": {
            "support_posture_declared_is_not_satisfied": True,
            "contradiction_posture_declared_is_not_not_satisfied": True,
            "unresolved_posture_declared_is_not_indeterminate": True,
            "complete_eight_record_declaration_is_not_candidate_sufficient": True,
            "declarant_reference_is_not_authority_identity_standing_or_truth": True,
            "evaluator_reference_is_not_authority_identity_standing_or_truth": True,
            "basis_items_are_not_established_truth": True,
            "basis_references_are_not_verified_provenance": True,
            "source_body_authorship_is_not_independent_custody": True,
            "declaration_readiness_is_not_basis_admission": True,
            "declaration_readiness_is_not_operation_execution": True,
            "declaration_readiness_is_not_operation_exhaustion": True,
        },
        "declaration_result_detail": {
            "declaration_result": declaration_result,
            "declaration_records_supplied": records_supplied,
            "declaration_complete": ready_complete,
            "declaration_ready_for_supply": outcome == OUTCOME_RECORDED,
            "candidate_sufficiency_basis_separately_supplied": False,
            "candidate_sufficiency_basis_admitted_by_operation": False,
            "candidate_sufficiency_operation_executed": False,
            "candidate_sufficiency_operation_exhausted": False,
            "dimension_result_exists": False,
            "candidate_result_exists": False,
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": _what_remains_open(outcome),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
    }
    result["failed_check_count"] = sum(
        check.get("passed") is False for check in checks
    )
    result["passed_check_count"] = sum(
        check.get("passed") is True for check in checks
    )
    result[
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_summary"
    ] = _summary_from_result(result)
    return result


def build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request(
    *,
    intent: str = INTENT_RECORD,
    declaration_records_supplied: bool | None = None,
    declaration_records: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    governing_declaration_specification_path: Path | str | None = None,
    selected_waiting_operation_artifact_path: Path | str | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical request without fabricating declaration records."""
    supplied = (
        declaration_records is not None
        if declaration_records_supplied is None
        else declaration_records_supplied
    )
    governing_path = (
        str(GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH)
        if governing_declaration_specification_path is None
        else str(governing_declaration_specification_path)
    )
    waiting_path = (
        str(SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH)
        if selected_waiting_operation_artifact_path is None
        else str(selected_waiting_operation_artifact_path)
    )
    request: dict[str, Any] = {
        "intent": intent,
        **_expected_request_values(),
        "governing_declaration_specification_path": governing_path,
        "selected_waiting_operation_artifact_path": waiting_path,
        "declaration_records_supplied": supplied,
        "declaration_records": copy.deepcopy(declaration_records),
        "declared_non_claims": copy.deepcopy(
            declared_non_claims
            if declared_non_claims is not None
            else _canonical_non_claims()
        ),
        **{key: False for key in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request(
    declaration_records: Mapping[str, Any],
    **kwargs: Any,
) -> dict[str, Any]:
    """Build one request carrying caller-prepared declaration records."""
    return (
        build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request(
            declaration_records=declaration_records,
            declaration_records_supplied=True,
            **kwargs,
        )
    )


def resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate one declaration and return waiting, ready, blocked, or no-record."""
    if request is None:
        bounded_request: Mapping[str, Any] = (
            build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {},
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="request is not a mapping",
        )
    else:
        bounded_request = copy.deepcopy(dict(request))

    checks: list[dict[str, Any]] = []
    code, reason = _validate_request(bounded_request, checks)
    if code is not None:
        return _result(
            bounded_request,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            code=code,
            reason=reason,
        )

    if bounded_request.get("intent") == INTENT_DO_NOT_RECORD:
        checks.append(_check("do_not_record_intent_honored", True))
        return _result(
            bounded_request,
            OUTCOME_NOT_RECORDED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
        )

    upstream, code, reason = _validate_upstream(checks)
    if code is not None:
        return _result(
            bounded_request,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            upstream=upstream,
            code=code,
            reason=reason,
        )

    if bounded_request.get("declaration_records_supplied") is False:
        checks.append(_check("absent_declaration_is_lawful_waiting", True))
        return _result(
            bounded_request,
            OUTCOME_REQUIRES_COMPLETE_DECLARATION,
            DECLARATION_RESULT_REQUIRES_COMPLETE,
            checks,
            upstream=upstream,
            missing=list(SUFFICIENCY_DECLARATION_DIMENSION_IDS),
        )

    records = bounded_request.get("declaration_records")
    code, reason, complete, missing = _validate_declaration_records(
        records,
        checks,
    )
    if code is not None:
        return _result(
            bounded_request,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            upstream=upstream,
            records=records if isinstance(records, Mapping) else None,
            missing=missing,
            code=code,
            reason=reason,
        )
    if not complete:
        checks.append(
            _check("partial_non_deceptive_declaration_remains_incomplete", True)
        )
        return _result(
            bounded_request,
            OUTCOME_REQUIRES_COMPLETE_DECLARATION,
            DECLARATION_RESULT_REQUIRES_COMPLETE,
            checks,
            upstream=upstream,
            records=records if isinstance(records, Mapping) else None,
            missing=missing,
        )

    checks.append(
        _check(
            "complete_declaration_ready_for_later_separate_supply_only",
            True,
        )
    )
    return _result(
        bounded_request,
        OUTCOME_RECORDED,
        DECLARATION_RESULT_READY_FOR_SUPPLY,
        checks,
        upstream=upstream,
        records=records if isinstance(records, Mapping) else None,
        complete=True,
    )


def resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one JSON request path without filesystem discovery."""
    value, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        checks = [
            _check(
                "request_path_is_mapping_json",
                False,
                "REQUEST_NOT_MAPPING",
            )
        ]
        return _result(
            {},
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="request path is missing, malformed, or not a mapping",
        )
    return (
        resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min(
            value
        )
    )


def build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return bounded summary metadata without declaration content."""
    if not isinstance(result, Mapping):
        raise (
            ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError(
                "result must be a mapping"
            )
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    index = 1
    while True:
        candidate = path.with_name(f"{stem}_{index:03d}{suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def _contains_forbidden_material(value: Any) -> bool:
    forbidden_keys = {
        "basis_items",
        "basis_references",
        "declarant_reference",
        "evaluator_reference",
        "candidate_material",
        "candidate_packet",
        "raw_candidate_material",
        "capture_material",
        "raw_samples",
        "zip_bytes",
        "selected_waiting_operation_artifact",
        "waiting_operation_artifact_content",
        "upstream_checks",
        "receiver_side_answerable_basis_candidate_sufficiency_operation",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_checks",
    }
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in forbidden_keys:
                return True
            if _contains_forbidden_material(nested):
                return True
    elif isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return any(_contains_forbidden_material(item) for item in value)
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    if parts & {
        "spec",
        "tests",
        "reference",
        "presence",
        "relation",
        "identity",
        "field",
        "runtime",
        "api",
        "public-intake",
        "descendant",
        "receiver-capture",
        "candidate-reception",
    }:
        return True
    forbidden_artifact_prefixes = (
        "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
        "candidate_reception_",
        "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
        "candidate_evaluation_",
        "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
        "candidate_sufficiency_boundary_",
        "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
        "candidate_sufficiency_operation_",
    )
    forbidden_artifact_tokens = (
        "_presence_",
        "_relation_",
        "_identity_",
        "_field_",
        "_runtime_",
        "_api_",
        "_public_intake_",
        "_descendant_",
        "_receiver_capture_",
    )
    return any(
        part.startswith(forbidden_artifact_prefixes)
        or (
            part.startswith("integrity_host_")
            and any(token in part for token in forbidden_artifact_tokens)
        )
        for part in parts
    )


def _validate_result_for_write(result: Mapping[str, Any]) -> None:
    error_type = (
        ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError
    )
    if set(result) != set(RESULT_SECTIONS):
        raise error_type("result sections do not match resolver contract")
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise error_type("result identity does not match resolver")
    outcome = result.get("outcome")
    if outcome not in OUTCOME_FAMILY:
        raise error_type("result outcome is unsupported")
    size = _serialized_size(result)
    if (
        size is None
        or size > MAX_SERIALIZED_RESULT_SIZE
        or not _bounded_result_value(result)
    ):
        raise error_type("result is not bounded JSON material")
    if not _all_false_mapping(
        result.get("non_claims"),
        REQUIRED_FALSE_NON_CLAIMS,
    ):
        raise error_type("result non-claims are not canonical false")
    if _contains_forbidden_material(result):
        raise error_type("result contains complete or copied declaration material")

    declaration = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration"
    )
    records = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_records"
    )
    detail = result.get("declaration_result_detail")
    block = result.get("block")
    checks = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_checks"
    )
    if not all(
        isinstance(value, Mapping)
        for value in (declaration, records, detail, block)
    ) or not isinstance(checks, list):
        raise error_type("result shape is malformed")

    wrapper_fields = {
        "outcome",
        "block",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_checks",
        "non_claims",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_summary",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "declaration_metadata",
    }
    if set(declaration) & wrapper_fields:
        raise error_type("declaration object contains wrapper fields")

    expected_result = {
        OUTCOME_RECORDED: DECLARATION_RESULT_READY_FOR_SUPPLY,
        OUTCOME_REQUIRES_COMPLETE_DECLARATION: (
            DECLARATION_RESULT_REQUIRES_COMPLETE
        ),
        OUTCOME_BLOCKED: DECLARATION_RESULT_NOT_EVALUATED,
        OUTCOME_NOT_RECORDED: DECLARATION_RESULT_NOT_EVALUATED,
    }[outcome]
    if (
        declaration.get("declaration_result") != expected_result
        or detail.get("declaration_result") != expected_result
    ):
        raise error_type("result branch and declaration result do not match")

    ready = outcome == OUTCOME_RECORDED
    readiness_fields = (
        "declaration_complete",
        "candidate_sufficiency_basis_declaration_recorded",
        "candidate_sufficiency_basis_declaration_result_recorded",
        "candidate_sufficiency_basis_declaration_ready_for_supply",
    )
    if any(declaration.get(field) is not ready for field in readiness_fields):
        raise error_type("declaration readiness posture does not match branch")
    if detail.get("declaration_complete") is not ready:
        raise error_type("declaration detail completeness does not match branch")
    if detail.get("declaration_ready_for_supply") is not ready:
        raise error_type("declaration detail readiness does not match branch")

    locked_false = (
        "candidate_sufficiency_basis_separately_supplied",
        "candidate_sufficiency_basis_admitted_by_operation",
        "candidate_sufficiency_operation_executed",
        "candidate_sufficiency_operation_exhausted",
    )
    for field in locked_false:
        if declaration.get(field) is not False or detail.get(field) is not False:
            raise error_type(f"{field} must remain false")

    record_summaries = records.get("record_summaries")
    if not isinstance(record_summaries, Mapping):
        raise error_type("record summaries are malformed")
    if ready and (
        set(record_summaries) != set(SUFFICIENCY_DECLARATION_DIMENSION_IDS)
        or records.get("declaration_record_count")
        != len(SUFFICIENCY_DECLARATION_DIMENSION_IDS)
        or records.get("declaration_complete") is not True
    ):
        raise error_type("ready result does not contain eight bounded summaries")
    if not ready and records.get("declaration_complete") is not False:
        raise error_type("non-ready result claims complete declaration")

    expected_open = (
        READY_WHAT_REMAINS_OPEN if ready else INCOMPLETE_WHAT_REMAINS_OPEN
    )
    if tuple(result.get("what_remains_open", ())) != expected_open:
        raise error_type("result open state does not match branch")

    actual_failed = sum(
        isinstance(check, Mapping) and check.get("passed") is False
        for check in checks
    )
    actual_passed = sum(
        isinstance(check, Mapping) and check.get("passed") is True
        for check in checks
    )
    if (
        result.get("failed_check_count") != actual_failed
        or result.get("passed_check_count") != actual_passed
    ):
        raise error_type("result check counts are inconsistent")
    for check in checks:
        if not isinstance(check, Mapping):
            raise error_type("result contains malformed check record")
        for key in ("block_code", "failure_code"):
            if key in check and check.get(key) not in BLOCK_CODES:
                raise error_type("result contains non-public failure code")

    blocked = outcome == OUTCOME_BLOCKED
    if block.get("blocked") is not blocked:
        raise error_type("result block posture does not match outcome")
    if blocked:
        if (
            block.get("code") not in BLOCK_CODES
            or block.get("block_code") != block.get("code")
            or not isinstance(block.get("reason"), str)
            or not block.get("reason")
            or actual_failed == 0
        ):
            raise error_type("blocked result does not contain a public block")
    elif any(
        block.get(key) is not None for key in ("code", "block_code", "reason")
    ):
        raise error_type("clean result contains block detail")


def write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one validated declaration result with deterministic suffixing."""
    if not isinstance(result, Mapping):
        raise (
            ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError(
                "result must be a mapping"
            )
        )
    _validate_result_for_write(result)
    target = (
        Path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise (
            ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError(
                "output path is forbidden"
            )
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_output_path(target)
    try:
        target.write_text(
            json.dumps(
                result,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            + "\n",
            encoding="utf-8",
        )
    except OSError as error:
        raise (
            ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError(
                "result write refused"
            )
        ) from error
    return target
