"""Resolve one bounded receiver-side candidate-sufficiency operation.

The resolver consumes one exact allowed and exhausted sufficiency boundary.
Absent separately supplied sufficiency basis is a lawful waiting posture.  A
completed result is derived only from one atomically admitted eight-record
basis and stops before attestation, receipt, presence, or downstream standing.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min"

OPERATION_ID = "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
OPERATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "DECIDE_SUFFICIENCY_POSTURE_OF_ONE_SELECTED_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)

SELECTED_SUFFICIENCY_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001"
)
SELECTED_SUFFICIENCY_BOUNDARY_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY"
)
SELECTED_SUFFICIENCY_BOUNDARY_VERSION = "0.1.0"
SELECTED_SUFFICIENCY_BOUNDARY_SCOPE = (
    "CONSIDER_SUFFICIENCY_OF_ONE_COMPLETEDLY_EVALUATED_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_CONSIDERATION_ALLOWED"
)
SELECTED_SUFFICIENCY_BOUNDARY_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY_ALLOWED"
)
SELECTED_SUFFICIENCY_BOUNDARY_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min"
)
SELECTED_SUFFICIENCY_BOUNDARY_ADMISSIBLE_FUTURE_ROUTE = (
    "CANDIDATE_SUFFICIENCY_BOUNDARY_THEN_CANDIDATE_SUFFICIENCY_OPERATION_ONLY"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
SELECTED_RECEPTION_OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"
SELECTED_EVALUATION_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
)
SELECTED_EVALUATION_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_evaluation_operation_001"
)

ADMISSIBLE_FUTURE_ROUTE = (
    "CANDIDATE_SUFFICIENCY_OPERATION_THEN_RECEIVER_ATTESTATION_BOUNDARY_"
    "ONLY_IF_CANDIDATE_SUFFICIENT"
)
REQUIRED_FUTURE_ROUTE = ADMISSIBLE_FUTURE_ROUTE

SUFFICIENCY_DIMENSION_IDS = (
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
        "refusal_withholding_compatibility": "refusal and withholding compatibility",
        "provenance_capture_limitation_posture": "provenance and capture limitation posture",
    }
)

DIMENSION_RULE_KEYS = MappingProxyType(
    {
        "receiver_answerability_fit": MappingProxyType(
            {
                "support": "bounded_receiver_answerability_fit_supported",
                "contradiction": "bounded_receiver_answerability_fit_contradicted",
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
                "contradiction": "bounded_material_incomplete_for_selected_purpose",
                "unresolved": "bounded_material_completeness_unresolved",
            }
        ),
        "unresolved_contradiction_posture": MappingProxyType(
            {
                "support": "no_unresolved_material_contradiction_for_selected_purpose",
                "contradiction": "material_contradiction_present_for_selected_purpose",
                "unresolved": "material_contradiction_posture_unresolved",
            }
        ),
        "unsupported_assumption_dependency": MappingProxyType(
            {
                "support": "no_required_unsupported_assumption_dependency",
                "contradiction": "required_unsupported_assumption_dependency_present",
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
                "support": "compatible_with_recorded_refusal_and_withholding_postures",
                "contradiction": "incompatible_with_recorded_refusal_or_withholding_posture",
                "unresolved": "refusal_withholding_compatibility_unresolved",
            }
        ),
        "provenance_capture_limitation_posture": MappingProxyType(
            {
                "support": "provenance_and_capture_limitations_bounded_and_preserved",
                "contradiction": (
                    "provenance_or_capture_limitation_materially_contradicts_selected_use"
                ),
                "unresolved": "provenance_capture_limitation_posture_unresolved",
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
            "selected-purpose adequacy is bounded-purpose posture only, not truth or standing."
        ),
        "bounded_material_completeness": (
            "bounded completeness is not unrestricted completeness or candidate truth."
        ),
        "unresolved_contradiction_posture": (
            "no unresolved material contradiction is not verified truth."
        ),
        "unsupported_assumption_dependency": (
            "absence of a required unsupported assumption dependency is not authority or standing."
        ),
        "scope_constrained_usability": (
            "scoped usability is not general usability, output authorization, or action authorization."
        ),
        "refusal_withholding_compatibility": (
            "refusal and withholding compatibility is not consent, attestation, or receipt."
        ),
        "provenance_capture_limitation_posture": (
            "bounded provenance and capture limitations are not verified provenance, "
            "physical validity, or presence."
        ),
    }
)

OUTCOME_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_RECORDED"
)
OUTCOME_REQUIRES_BASIS = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_"
    "REQUIRES_SUFFICIENCY_BASIS"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_BLOCKED"
)
OUTCOME_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_BASIS,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

OPERATION_RESULT_SUFFICIENT = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
OPERATION_RESULT_INSUFFICIENT = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_INSUFFICIENT"
OPERATION_RESULT_INDETERMINATE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_INDETERMINATE"
)
OPERATION_RESULT_REQUIRES_BASIS = "REQUIRES_SUFFICIENCY_BASIS"
OPERATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
OPERATION_RESULT_FAMILY = (
    OPERATION_RESULT_SUFFICIENT,
    OPERATION_RESULT_INSUFFICIENT,
    OPERATION_RESULT_INDETERMINATE,
    OPERATION_RESULT_REQUIRES_BASIS,
    OPERATION_RESULT_NOT_EVALUATED,
)

DIMENSION_RESULT_SATISFIED = "SATISFIED"
DIMENSION_RESULT_NOT_SATISFIED = "NOT_SATISFIED"
DIMENSION_RESULT_INDETERMINATE = "INDETERMINATE"
DIMENSION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
DIMENSION_RESULT_FAMILY = (
    DIMENSION_RESULT_SATISFIED,
    DIMENSION_RESULT_NOT_SATISFIED,
    DIMENSION_RESULT_INDETERMINATE,
    DIMENSION_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
)
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_V0_MIN_SPEC.md"
)
SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result.json"
)
GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH
)
SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_PATH
OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result.json"
)

SPEC_MARKERS = (
    "# Receiver-Side Answerable Basis Candidate Sufficiency Operation V0 Minimum Specification",
    OPERATION_ID,
    OPERATION_TYPE,
    OPERATION_SCOPE,
    SELECTED_SUFFICIENCY_BOUNDARY_ID,
    SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED,
    ADMISSIBLE_FUTURE_ROUTE,
    *SUFFICIENCY_DIMENSION_IDS,
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_BASIS,
    OPERATION_RESULT_SUFFICIENT,
    OPERATION_RESULT_INSUFFICIENT,
    OPERATION_RESULT_INDETERMINATE,
)

REQUIRED_UPSTREAM_BOUNDARY_DECLARATIONS = MappingProxyType(
    {
        "resolver_module": SELECTED_SUFFICIENCY_BOUNDARY_RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": SELECTED_SUFFICIENCY_BOUNDARY_OUTCOME_REQUIRED,
        "boundary_result": SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED,
        "failed_check_count": 0,
        "candidate_sufficiency_boundary_recorded": True,
        "candidate_sufficiency_boundary_result_recorded": True,
        "candidate_sufficiency_consideration_allowed": True,
        "candidate_sufficiency_boundary_exhausted": True,
        "atomic_gate_validated": True,
        "eight_dimensions_validated": True,
        "candidate_aggregate_validated": True,
        "exhaustion_validated": True,
        "current_false_posture_validated": True,
        "candidate_results_false": True,
        "receiver_receipt_presence_downstream_false": True,
        "repeated_reusable_rerun_false": True,
    }
)

REQUIRED_UPSTREAM_CANDIDATE_FALSE_POSTURES = (
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "candidate_sufficiency_decided",
    "candidate_sufficiency_established",
    "candidate_insufficiency_established",
    "candidate_indeterminacy_established",
)
REQUIRED_UPSTREAM_OPERATION_FALSE_POSTURES = (
    "candidate_sufficiency_operation_created",
    "candidate_sufficiency_operation_authorized",
    "candidate_sufficiency_operation_executed",
)
REQUIRED_UPSTREAM_RECEIVER_FALSE_POSTURES = (
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
REQUIRED_UPSTREAM_REPEAT_FALSE_POSTURES = (
    "repeated_candidate_sufficiency_boundary_permission_created",
    "reusable_candidate_sufficiency_route_created",
    "same_candidate_sufficiency_boundary_rerun_authorized",
    "automatic_candidate_sufficiency_boundary_retry_created",
    "candidate_sufficiency_boundary_debt_created",
    "candidate_sufficiency_boundary_obligation_created",
    "follow_on_authorized",
    "follow_on_work_authorized",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "repeated_candidate_sufficiency_operation_permission_created",
    "reusable_candidate_sufficiency_operation_route_created",
    "same_candidate_sufficiency_operation_rerun_authorized",
    "automatic_candidate_sufficiency_operation_retry_created",
    "candidate_sufficiency_operation_debt_created",
    "candidate_sufficiency_operation_obligation_created",
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
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

REQUIRED_BASIS_NON_CLAIMS = (
    "caller_supplied_dimension_result",
    "caller_supplied_candidate_result",
    "evaluator_reference_to_authority",
    "evaluator_reference_to_identity",
    "evaluator_reference_to_standing",
    "evaluator_reference_to_truth",
    "basis_items_to_established_truth",
    "basis_references_to_verified_provenance",
    "candidate_sufficiency_to_receiver_attestation",
    "candidate_sufficiency_to_receiver_answerable_receipt",
    "candidate_sufficiency_to_presence_support",
    "candidate_sufficiency_to_downstream_authorization",
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_caller_selected_dimension_result": "PROHIBITED_RESULT_SELECTION_REQUESTED",
        "request_caller_selected_candidate_result": "PROHIBITED_RESULT_SELECTION_REQUESTED",
        "request_partial_evaluation": "PROHIBITED_PARTIAL_EVALUATION_REQUESTED",
        "request_candidate_sufficiency_preclaim": "PROHIBITED_RESULT_SELECTION_REQUESTED",
        "request_candidate_insufficiency_preclaim": "PROHIBITED_RESULT_SELECTION_REQUESTED",
        "request_candidate_indeterminacy_preclaim": "PROHIBITED_RESULT_SELECTION_REQUESTED",
        "request_receiver_attestation_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_attestation_support": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_attestation_boundary_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_answerable_receipt_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_answerable_receipt_boundary_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_support": "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_authorization": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_establishment": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_recording": "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_re_evaluation_boundary_creation": (
            "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_identity_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_relation_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_coupling_assignment": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_coupling_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_field_machinery_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_runtime_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_api_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_public_interface_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_public_intake_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_authority_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_standing_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_truth_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_continuity_memory_write": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_output_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_action_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_synchronization_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_repeated_operation_permission_creation": (
            "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED"
        ),
        "request_reusable_operation_route_creation": (
            "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED"
        ),
        "request_same_candidate_operation_rerun": (
            "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED"
        ),
        "request_automatic_operation_retry_creation": (
            "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED"
        ),
        "request_operation_debt_creation": (
            "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED"
        ),
        "request_operation_obligation_creation": (
            "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED"
        ),
        "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_follow_on_work_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_candidate_rejection": (
            "PROHIBITED_CANDIDATE_REJECTION_DELETION_ERASURE_INVALIDATION_OR_REPAIR_REQUESTED"
        ),
        "request_candidate_deletion": (
            "PROHIBITED_CANDIDATE_REJECTION_DELETION_ERASURE_INVALIDATION_OR_REPAIR_REQUESTED"
        ),
        "request_candidate_erasure": (
            "PROHIBITED_CANDIDATE_REJECTION_DELETION_ERASURE_INVALIDATION_OR_REPAIR_REQUESTED"
        ),
        "request_candidate_invalidation": (
            "PROHIBITED_CANDIDATE_REJECTION_DELETION_ERASURE_INVALIDATION_OR_REPAIR_REQUESTED"
        ),
        "request_candidate_repair": (
            "PROHIBITED_CANDIDATE_REJECTION_DELETION_ERASURE_INVALIDATION_OR_REPAIR_REQUESTED"
        ),
        "request_repository_scan": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "request_file_discovery": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
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
        "SUFFICIENCY_OPERATION_SPEC_REFERENCE_MISSING",
        "SUFFICIENCY_OPERATION_SPEC_MARKER_MISSING",
        "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_MAPPING",
        "REQUEST_VALUE_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
        "UPSTREAM_BOUNDARY_NOT_ALLOWED",
        "UPSTREAM_BOUNDARY_RESULT_MISMATCH",
        "UPSTREAM_BOUNDARY_FAILED_CHECKS_PRESENT",
        "UPSTREAM_BOUNDARY_NOT_RECORDED",
        "UPSTREAM_BOUNDARY_RESULT_NOT_RECORDED",
        "UPSTREAM_CONSIDERATION_NOT_ALLOWED",
        "UPSTREAM_BOUNDARY_NOT_EXHAUSTED",
        "UPSTREAM_BOUNDARY_VALIDATION_INCOMPLETE",
        "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        "UPSTREAM_OPERATION_POSTURE_ALREADY_PRESENT",
        "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
        "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT",
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "SUFFICIENCY_BASIS_NOT_MAPPING",
        "SUFFICIENCY_BASIS_DIMENSION_SET_MISMATCH",
        "SUFFICIENCY_BASIS_RECORD_NOT_MAPPING",
        "SUFFICIENCY_BASIS_RECORD_IDENTITY_MISMATCH",
        "SUFFICIENCY_BASIS_ITEMS_INVALID",
        "SUFFICIENCY_BASIS_REFERENCES_INVALID",
        "SUFFICIENCY_BASIS_EVALUATOR_REFERENCE_INVALID",
        "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID",
        "SUFFICIENCY_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
        "SUFFICIENCY_BASIS_NON_CONVERSION_STATEMENT_MISMATCH",
        "SUFFICIENCY_BASIS_RESULT_PRECLAIMED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_RESULT_SELECTION_REQUESTED",
        "PROHIBITED_PARTIAL_EVALUATION_REQUESTED",
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
        "PROHIBITED_CANDIDATE_REJECTION_DELETION_ERASURE_INVALIDATION_OR_REPAIR_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "EXPLICIT_BLOCK_REQUESTED",
        "WRITE_REFUSED",
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
SUFFICIENT_WHAT_REMAINS_OPEN = (
    "receiver-attestation boundary, if separately selected",
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
NON_SUFFICIENT_WHAT_REMAINS_OPEN = (
    "separately lawful new basis route, if later selected",
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
INCOMPLETE_BRANCH_WHAT_REMAINS_OPEN = (
    "candidate-sufficiency operation request, if separately selected",
)
EXPECTED_UPSTREAM_WHAT_REMAINS_OPEN = (
    "candidate-sufficiency operation specification, if separately selected",
    "candidate-sufficiency operation resolver and test, if separately selected",
    "candidate-sufficiency decision",
    "receiver-attestation boundary, only after lawful candidate-sufficiency standing",
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
    "evaluation_result_to_candidate_sufficiency",
    "evaluation_dimensions_to_candidate_sufficiency",
    "boundary_result_to_candidate_sufficiency",
    "caller_basis_to_caller_selected_result",
    "evaluator_reference_to_authority_identity_standing_or_truth",
    "candidate_sufficient_to_receiver_attestation_receipt_or_presence",
    "candidate_insufficient_to_rejection_deletion_erasure_repair_or_invalidation",
    "candidate_indeterminate_to_candidate_insufficiency",
    "candidate_result_to_downstream_conversion",
    "completed_operation_to_repeated_permission_reusable_route_or_silent_rerun",
    "changed_files_or_new_evidence_to_automatic_rerun",
    "completed_operation_to_contaminated_lineage_validation",
)

RESULT_SECTIONS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_sufficiency_operation_metadata",
        "declared_receiver_side_answerable_basis_candidate_sufficiency_operation_basis",
        "upstream_basis",
        "receiver_side_answerable_basis_candidate_sufficiency_operation",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_basis",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_checks",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_statement",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_non_meaning",
        "operation_result_detail",
        "permitted_future_route",
        "blocked_routes",
        "what_remains_open",
        "non_claims",
        "outcome",
        "block",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_summary",
        "resolver_module",
        "result_version",
        "failed_check_count",
        "passed_check_count",
    }
)

MAX_SEQUENCE_ITEMS = 32
MAX_MAPPING_ITEMS = 48
MAX_TEXT_LENGTH = 2048
MAX_BOUNDED_DEPTH = 6

_BASIS_RECORD_FIELDS = frozenset(
    {
        "dimension_id",
        "receiver_side_answerable_basis_candidate_id",
        "selected_candidate_sufficiency_boundary_id",
        "basis_items",
        "basis_references",
        "evaluator_reference",
        "support_postures",
        "contradiction_postures",
        "unresolved_postures",
        "basis_non_claims",
        "non_conversion_statement",
    }
)
_BASIS_PRECLAIM_FIELDS = frozenset(
    {
        "dimension_result",
        "requested_dimension_result",
        "candidate_result",
        "requested_candidate_result",
        "operation_result",
        "requested_operation_result",
        "outcome",
        "receiver_side_answerable_basis_candidate_sufficient",
        "receiver_side_answerable_basis_candidate_insufficient",
        "receiver_side_answerable_basis_candidate_indeterminate",
        "candidate_sufficiency_decided",
        "candidate_sufficiency_established",
        "candidate_insufficiency_established",
        "candidate_indeterminacy_established",
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_answerable_receipt_present",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "identity_created",
        "authority_created",
        "standing_created",
        "truth_created",
        "output_authorized",
        "action_authorized",
        "synchronization_authorized",
        "follow_on_authorized",
        "follow_on_work_authorized",
    }
)


class ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(Exception):
    """Raised when a bounded candidate-sufficiency result cannot be written."""


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_basis_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_BASIS_NON_CLAIMS}


def _check(name: str, passed: bool, code: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"name": name, "passed": passed}
    if not passed and code is not None:
        result["failure_code"] = code
        result["block_code"] = code
    return result


def _add_failure(checks: list[dict[str, Any]], name: str, code: str) -> None:
    checks.append(_check(name, False, code))


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_repo_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except OSError:
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except (TypeError, ValueError, json.JSONDecodeError):
        return None, "not_parseable"


def _declared_non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _basis_non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_BASIS_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_BASIS_NON_CLAIMS)
    )


def _expected_request_values() -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "selected_candidate_sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "selected_candidate_sufficiency_boundary_type": SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
        "selected_candidate_sufficiency_boundary_result_required": (
            SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED
        ),
        "governing_sufficiency_operation_specification_path": str(
            GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_sufficiency_boundary_artifact_path": str(
            SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "required_upstream_boundary_declarations": dict(
            REQUIRED_UPSTREAM_BOUNDARY_DECLARATIONS
        ),
    }


def build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request(
    sufficiency_basis_records: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical bounded operation request."""
    supplied = sufficiency_basis_records is not None
    if isinstance(sufficiency_basis_records, Mapping):
        records: Any = copy.deepcopy(dict(sufficiency_basis_records))
    elif sufficiency_basis_records is None:
        records = {}
    else:
        records = copy.deepcopy(sufficiency_basis_records)
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_expected_request_values(),
        "sufficiency_basis_supplied": supplied,
        "sufficiency_basis_records": records,
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request(
    sufficiency_basis_records: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build the declared request using the same canonical request shape."""
    return build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request(
        sufficiency_basis_records=sufficiency_basis_records,
        **overrides,
    )


def _request_preclaim_fields() -> set[str]:
    return {
        "outcome",
        "operation_result",
        "candidate_sufficiency_operation_result",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_result",
        "candidate_sufficiency_operation_recorded",
        "candidate_sufficiency_operation_result_recorded",
        "candidate_sufficiency_operation_exhausted",
        "receiver_side_answerable_basis_candidate_sufficient",
        "receiver_side_answerable_basis_candidate_insufficient",
        "receiver_side_answerable_basis_candidate_indeterminate",
        "candidate_sufficiency_decided",
        "candidate_sufficiency_established",
        "candidate_insufficiency_established",
        "candidate_indeterminacy_established",
        "dimension_results",
        "selected_boundary_artifact",
        "complete_boundary_artifact",
        "receiver_side_answerable_basis_candidate_sufficiency_boundary",
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_checks",
    }


def _request_mismatch_code(field: str) -> str:
    if field.startswith("operation_"):
        return "SELECTED_OPERATION_IDENTITY_MISMATCH"
    if field in {
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "selected_candidate_reception_operation_id",
        "selected_candidate_evaluation_boundary_id",
        "selected_candidate_evaluation_operation_id",
    }:
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if field.startswith("selected_candidate_sufficiency_boundary_"):
        return "SELECTED_BOUNDARY_IDENTITY_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _validate_request(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None]:
    intent = request.get("intent")
    if intent == INTENT_BLOCK:
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if intent not in SUPPORTED_INTENTS:
        return "UNSUPPORTED_INTENT", "intent is not supported"

    for field, expected in _expected_request_values().items():
        valid = request.get(field) == expected
        code = _request_mismatch_code(field)
        checks.append(_check("request." + field, valid, code))
        if not valid:
            return code, field + " does not match the canonical operation request"

    if not _declared_non_claims_valid(request.get("declared_non_claims")):
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared_non_claims must contain exact canonical false postures",
        )

    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        valid = field in request and request.get(field) is False
        checks.append(
            _check(
                "request." + field,
                valid,
                code if field in request else "REQUEST_VALUE_MISMATCH",
            )
        )
        if not valid:
            return (
                code if field in request else "REQUEST_VALUE_MISMATCH",
                field + " must be present and false",
            )

    for field in _request_preclaim_fields():
        if field in request:
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be caller-supplied"

    if not isinstance(request.get("sufficiency_basis_supplied"), bool):
        return "REQUEST_VALUE_MISMATCH", "sufficiency_basis_supplied must be boolean"

    allowed = {
        "intent",
        "sufficiency_basis_supplied",
        "sufficiency_basis_records",
        "declared_non_claims",
        *tuple(_expected_request_values()),
        *tuple(PROHIBITED_REQUEST_FLAGS),
    }
    unknown = set(request).difference(allowed)
    if unknown:
        return "REQUEST_VALUE_MISMATCH", "declared request contains unknown fields"

    if (
        request.get("sufficiency_basis_supplied") is False
        and request.get("sufficiency_basis_records") != {}
    ):
        return (
            "REQUEST_VALUE_MISMATCH",
            "basis records must be empty when sufficiency basis is not supplied",
        )
    return None, None


def _empty_upstream_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    expected = _expected_request_values()
    return {
        "governing_paths": {
            "governing_sufficiency_operation_specification_path": (
                expected["governing_sufficiency_operation_specification_path"]
                if request.get("governing_sufficiency_operation_specification_path")
                == expected["governing_sufficiency_operation_specification_path"]
                else None
            ),
            "selected_sufficiency_boundary_artifact_path": (
                expected["selected_sufficiency_boundary_artifact_path"]
                if request.get("selected_sufficiency_boundary_artifact_path")
                == expected["selected_sufficiency_boundary_artifact_path"]
                else None
            ),
        },
        "marker_validation": {
            "governing_sufficiency_operation_specification": False,
        },
        "selected_boundary_metadata": {},
        "selected_boundary_identity": {},
        "selected_candidate_identity": {},
        "upstream_boundary_validation": {},
        "current_false_posture_validation": {},
        "corrected_open_state_validation": False,
        "complete_boundary_artifact_omitted": True,
        "complete_upstream_checks_omitted": True,
    }


def _require(
    checks: list[dict[str, Any]],
    name: str,
    condition: bool,
    code: str,
    reason: str,
) -> tuple[str | None, str | None]:
    checks.append(_check(name, condition, code))
    return (None, None) if condition else (code, reason)


def _validate_upstream_boundary(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    upstream = _empty_upstream_basis(request)

    spec_text, spec_error = _read_text(
        request["governing_sufficiency_operation_specification_path"]
    )
    if spec_error is not None or spec_text is None:
        return (
            "SUFFICIENCY_OPERATION_SPEC_REFERENCE_MISSING",
            "governing sufficiency-operation specification is unavailable",
            upstream,
        )
    markers_valid = all(marker in spec_text for marker in SPEC_MARKERS)
    upstream["marker_validation"][
        "governing_sufficiency_operation_specification"
    ] = markers_valid
    code, reason = _require(
        checks,
        "governing_sufficiency_operation_specification_markers",
        markers_valid,
        "SUFFICIENCY_OPERATION_SPEC_MARKER_MISSING",
        "governing sufficiency-operation specification markers are incomplete",
    )
    if code is not None:
        return code, reason, upstream

    artifact, artifact_error = _read_json(
        request["selected_sufficiency_boundary_artifact_path"]
    )
    if artifact_error in {"not_a_file", "unreadable"}:
        return (
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            "selected sufficiency-boundary artifact is unavailable",
            upstream,
        )
    if artifact_error == "not_parseable":
        return (
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            "selected sufficiency-boundary artifact is not parseable JSON",
            upstream,
        )
    if not isinstance(artifact, Mapping):
        return (
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "selected sufficiency-boundary artifact is not a mapping",
            upstream,
        )

    boundary = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_boundary"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_summary"
    )
    if not isinstance(boundary, Mapping) or not isinstance(summary, Mapping):
        return (
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "selected artifact lacks required bounded boundary sections",
            upstream,
        )

    upstream["selected_boundary_metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "outcome": artifact.get("outcome"),
        "failed_check_count": artifact.get("failed_check_count"),
        "passed_check_count": artifact.get("passed_check_count"),
    }
    upstream["selected_boundary_identity"] = {
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "boundary_result": boundary.get("candidate_sufficiency_boundary_result"),
    }
    upstream["selected_candidate_identity"] = {
        "candidate_id": boundary.get("receiver_side_answerable_basis_candidate_id"),
        "candidate_type": boundary.get("receiver_side_answerable_basis_candidate_type"),
        "candidate_scope": boundary.get("receiver_side_answerable_basis_candidate_scope"),
        "reception_operation_id": boundary.get(
            "selected_candidate_reception_operation_id"
        ),
        "evaluation_boundary_id": boundary.get(
            "selected_candidate_evaluation_boundary_id"
        ),
        "evaluation_operation_id": boundary.get(
            "selected_candidate_evaluation_operation_id"
        ),
    }

    for field, expected in (
        ("resolver_module", SELECTED_SUFFICIENCY_BOUNDARY_RESOLVER_MODULE),
        ("result_version", RESULT_VERSION),
    ):
        code, reason = _require(
            checks,
            "upstream." + field,
            artifact.get(field) == expected,
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            "selected boundary " + field + " does not match",
        )
        if code is not None:
            return code, reason, upstream

    code, reason = _require(
        checks,
        "upstream.outcome",
        artifact.get("outcome") == SELECTED_SUFFICIENCY_BOUNDARY_OUTCOME_REQUIRED,
        "UPSTREAM_BOUNDARY_NOT_ALLOWED",
        "selected boundary outcome is not allowed",
    )
    if code is not None:
        return code, reason, upstream
    code, reason = _require(
        checks,
        "upstream.failed_check_count",
        artifact.get("failed_check_count") == 0,
        "UPSTREAM_BOUNDARY_FAILED_CHECKS_PRESENT",
        "selected boundary has failed checks",
    )
    if code is not None:
        return code, reason, upstream

    identity_requirements = {
        "boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "boundary_type": SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
        "boundary_version": SELECTED_SUFFICIENCY_BOUNDARY_VERSION,
        "boundary_scope": SELECTED_SUFFICIENCY_BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_type": (
            SELECTED_SUFFICIENCY_BOUNDARY_TYPE
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_version": (
            SELECTED_SUFFICIENCY_BOUNDARY_VERSION
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_scope": (
            SELECTED_SUFFICIENCY_BOUNDARY_SCOPE
        ),
        "admissible_future_route": (
            SELECTED_SUFFICIENCY_BOUNDARY_ADMISSIBLE_FUTURE_ROUTE
        ),
    }
    for field, expected in identity_requirements.items():
        code, reason = _require(
            checks,
            "upstream." + field,
            boundary.get(field) == expected,
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            "selected boundary identity does not match " + field,
        )
        if code is not None:
            return code, reason, upstream

    candidate_requirements = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
    }
    for field, expected in candidate_requirements.items():
        code, reason = _require(
            checks,
            "upstream." + field,
            boundary.get(field) == expected,
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            "selected candidate identity does not match " + field,
        )
        if code is not None:
            return code, reason, upstream

    boundary_result = boundary.get("candidate_sufficiency_boundary_result")
    code, reason = _require(
        checks,
        "upstream.boundary_result",
        boundary_result == SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED,
        "UPSTREAM_BOUNDARY_RESULT_MISMATCH",
        "selected boundary result does not allow consideration",
    )
    if code is not None:
        return code, reason, upstream
    code, reason = _require(
        checks,
        "upstream.boundary_result_alias",
        boundary.get(
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_result"
        )
        == SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED,
        "UPSTREAM_BOUNDARY_RESULT_MISMATCH",
        "selected boundary result alias does not allow consideration",
    )
    if code is not None:
        return code, reason, upstream

    posture_requirements = (
        (
            "candidate_sufficiency_boundary_recorded",
            "UPSTREAM_BOUNDARY_NOT_RECORDED",
        ),
        (
            "candidate_sufficiency_boundary_result_recorded",
            "UPSTREAM_BOUNDARY_RESULT_NOT_RECORDED",
        ),
        (
            "candidate_sufficiency_consideration_allowed",
            "UPSTREAM_CONSIDERATION_NOT_ALLOWED",
        ),
        (
            "candidate_sufficiency_boundary_exhausted",
            "UPSTREAM_BOUNDARY_NOT_EXHAUSTED",
        ),
        (
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded",
            "UPSTREAM_BOUNDARY_NOT_RECORDED",
        ),
        (
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded",
            "UPSTREAM_BOUNDARY_RESULT_NOT_RECORDED",
        ),
    )
    boundary_validation: dict[str, bool] = {}
    for field, failure_code in posture_requirements:
        valid = boundary.get(field) is True
        boundary_validation[field] = valid
        code, reason = _require(
            checks,
            "upstream." + field,
            valid,
            failure_code,
            "selected boundary posture is not true: " + field,
        )
        if code is not None:
            upstream["upstream_boundary_validation"] = boundary_validation
            return code, reason, upstream

    summary_fields = (
        "atomic_gate_validated",
        "eight_dimensions_validated",
        "candidate_aggregate_validated",
        "exhaustion_validated",
        "current_false_posture_validated",
        "candidate_results_false",
        "receiver_receipt_presence_downstream_false",
        "repeated_reusable_rerun_false",
    )
    for field in summary_fields:
        valid = summary.get(field) is True
        boundary_validation[field] = valid
        code, reason = _require(
            checks,
            "upstream.summary." + field,
            valid,
            "UPSTREAM_BOUNDARY_VALIDATION_INCOMPLETE",
            "selected boundary validation is incomplete: " + field,
        )
        if code is not None:
            upstream["upstream_boundary_validation"] = boundary_validation
            return code, reason, upstream
    upstream["upstream_boundary_validation"] = boundary_validation

    false_groups = (
        (
            REQUIRED_UPSTREAM_CANDIDATE_FALSE_POSTURES,
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        ),
        (
            REQUIRED_UPSTREAM_OPERATION_FALSE_POSTURES,
            "UPSTREAM_OPERATION_POSTURE_ALREADY_PRESENT",
        ),
        (
            REQUIRED_UPSTREAM_RECEIVER_FALSE_POSTURES,
            "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
        ),
        (
            REQUIRED_UPSTREAM_REPEAT_FALSE_POSTURES,
            "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT",
        ),
    )
    current_false: dict[str, bool] = {}
    for fields, failure_code in false_groups:
        for field in fields:
            valid = boundary.get(field) is False
            current_false[field] = valid
            code, reason = _require(
                checks,
                "upstream.false." + field,
                valid,
                failure_code,
                "selected boundary contains prohibited prior posture: " + field,
            )
            if code is not None:
                upstream["current_false_posture_validation"] = current_false
                return code, reason, upstream
    upstream["current_false_posture_validation"] = current_false

    open_state = artifact.get("what_remains_open")
    corrected_open = (
        isinstance(open_state, list)
        and tuple(open_state) == EXPECTED_UPSTREAM_WHAT_REMAINS_OPEN
        and bool(open_state)
        and open_state[0]
        == "candidate-sufficiency operation specification, if separately selected"
    )
    upstream["corrected_open_state_validation"] = corrected_open
    code, reason = _require(
        checks,
        "upstream.corrected_what_remains_open",
        corrected_open,
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "selected boundary open state is stale or mismatched",
    )
    if code is not None:
        return code, reason, upstream
    return None, None, upstream


def _empty_basis_state() -> dict[str, Any]:
    return {
        "sufficiency_basis_supplied": False,
        "sufficiency_basis_complete": False,
        "all_dimension_basis_records_present": False,
        "all_dimension_basis_records_bounded": False,
        "all_dimension_basis_records_reference_selected_candidate": False,
        "all_dimension_basis_records_reference_selected_boundary": False,
        "all_dimension_basis_records_contain_evaluator_reference": False,
        "all_dimension_basis_records_contain_rule_input_maps": False,
        "all_dimension_basis_records_non_result_preclaiming": False,
        "all_dimension_basis_records_preserve_non_claims": False,
        "all_dimension_basis_records_non_conversion_validated": False,
        "no_caller_supplied_operation_result": True,
        "atomic_sufficiency_basis_gate_passed": False,
        "dimension_basis_metadata": {},
        "complete_supplied_basis_omitted": True,
    }


def _bounded_value(value: Any, depth: int = 0) -> bool:
    if depth > MAX_BOUNDED_DEPTH:
        return False
    if value is None or isinstance(value, bool):
        return True
    if isinstance(value, int) and not isinstance(value, bool):
        return abs(value) <= 1_000_000_000_000
    if isinstance(value, float):
        return value == value and abs(value) != float("inf") and abs(value) <= 1_000_000_000_000
    if isinstance(value, str):
        return len(value) <= MAX_TEXT_LENGTH
    if isinstance(value, Mapping):
        return (
            len(value) <= MAX_MAPPING_ITEMS
            and all(
                isinstance(key, str)
                and 0 < len(key) <= 160
                and _bounded_value(nested, depth + 1)
                for key, nested in value.items()
            )
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return len(value) <= MAX_SEQUENCE_ITEMS and all(
            _bounded_value(item, depth + 1) for item in value
        )
    return False


def _bounded_mapping_sequence(value: Any) -> bool:
    return (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes, bytearray))
        and 0 < len(value) <= MAX_SEQUENCE_ITEMS
        and all(isinstance(item, Mapping) and _bounded_value(item) for item in value)
    )


def _contains_basis_preclaim(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(
        set(value).intersection(_BASIS_PRECLAIM_FIELDS)
    )


def _single_boolean_map(value: Any, required_key: str) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == {required_key}
        and isinstance(value.get(required_key), bool)
    )


def _basis_record_metadata(
    dimension_id: str,
    record: Mapping[str, Any],
) -> dict[str, Any]:
    keys = DIMENSION_RULE_KEYS[dimension_id]
    items = record.get("basis_items")
    references = record.get("basis_references")
    return {
        "dimension_id": dimension_id,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "selected_candidate_sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "basis_items_count": len(items) if isinstance(items, Sequence) else 0,
        "basis_references_count": (
            len(references) if isinstance(references, Sequence) else 0
        ),
        "evaluator_reference_supplied": isinstance(
            record.get("evaluator_reference"), Mapping
        )
        and bool(record.get("evaluator_reference")),
        "support_key": keys["support"],
        "contradiction_key": keys["contradiction"],
        "unresolved_key": keys["unresolved"],
        "basis_non_claims_validated": _basis_non_claims_valid(
            record.get("basis_non_claims")
        ),
        "non_conversion_statement_validated": (
            record.get("non_conversion_statement")
            == DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
        ),
        "complete_supplied_basis_omitted": True,
    }


def _derive_dimension_result(
    dimension_id: str, record: Mapping[str, Any]
) -> str:
    keys = DIMENSION_RULE_KEYS[dimension_id]
    support = record["support_postures"][keys["support"]]
    contradiction = record["contradiction_postures"][keys["contradiction"]]
    unresolved = record["unresolved_postures"][keys["unresolved"]]
    if unresolved is True:
        return DIMENSION_RESULT_INDETERMINATE
    if contradiction is True:
        return DIMENSION_RESULT_NOT_SATISFIED
    if support is False:
        return DIMENSION_RESULT_NOT_SATISFIED
    return DIMENSION_RESULT_SATISFIED


def _validate_basis_records(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[
    str | None,
    str | None,
    dict[str, Any],
    dict[str, str],
    bool,
]:
    state = _empty_basis_state()
    not_evaluated = {
        dimension_id: DIMENSION_RESULT_NOT_EVALUATED
        for dimension_id in SUFFICIENCY_DIMENSION_IDS
    }
    supplied = request.get("sufficiency_basis_supplied")
    records = request.get("sufficiency_basis_records")
    state["sufficiency_basis_supplied"] = supplied is True

    if supplied is False:
        checks.append(_check("sufficiency_basis_absent_waiting_posture", True))
        return None, None, state, not_evaluated, False
    if not isinstance(records, Mapping):
        return (
            "SUFFICIENCY_BASIS_NOT_MAPPING",
            "supplied sufficiency basis must be a mapping",
            state,
            not_evaluated,
            False,
        )
    if set(records) != set(SUFFICIENCY_DIMENSION_IDS):
        return (
            "SUFFICIENCY_BASIS_DIMENSION_SET_MISMATCH",
            "supplied sufficiency basis must contain exactly eight dimension records",
            state,
            not_evaluated,
            False,
        )
    state["all_dimension_basis_records_present"] = True

    derived: dict[str, str] = {}
    metadata: dict[str, dict[str, Any]] = {}
    for dimension_id in SUFFICIENCY_DIMENSION_IDS:
        record = records.get(dimension_id)
        if not isinstance(record, Mapping):
            return (
                "SUFFICIENCY_BASIS_RECORD_NOT_MAPPING",
                dimension_id + " basis record is not a mapping",
                state,
                not_evaluated,
                False,
            )
        if set(record) != _BASIS_RECORD_FIELDS:
            if _contains_basis_preclaim(
                {key: value for key, value in record.items() if key != "basis_non_claims"}
            ):
                code = "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"
                reason = dimension_id + " basis record contains a result preclaim"
            else:
                code = "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"
                reason = dimension_id + " basis record fields are not exact"
            return code, reason, state, not_evaluated, False

        if _contains_basis_preclaim(
            {key: value for key, value in record.items() if key != "basis_non_claims"}
        ):
            return (
                "SUFFICIENCY_BASIS_RESULT_PRECLAIMED",
                dimension_id + " basis record contains a result preclaim",
                state,
                not_evaluated,
                False,
            )

        identity_valid = (
            record.get("dimension_id") == dimension_id
            and record.get("receiver_side_answerable_basis_candidate_id")
            == CANDIDATE_ID
            and record.get("selected_candidate_sufficiency_boundary_id")
            == SELECTED_SUFFICIENCY_BOUNDARY_ID
        )
        if not identity_valid:
            return (
                "SUFFICIENCY_BASIS_RECORD_IDENTITY_MISMATCH",
                dimension_id + " basis record identity does not match",
                state,
                not_evaluated,
                False,
            )
        if not _bounded_mapping_sequence(record.get("basis_items")):
            return (
                "SUFFICIENCY_BASIS_ITEMS_INVALID",
                dimension_id + " basis_items are absent, unbounded, or malformed",
                state,
                not_evaluated,
                False,
            )
        if not _bounded_mapping_sequence(record.get("basis_references")):
            return (
                "SUFFICIENCY_BASIS_REFERENCES_INVALID",
                dimension_id + " basis_references are absent, unbounded, or malformed",
                state,
                not_evaluated,
                False,
            )
        evaluator_reference = record.get("evaluator_reference")
        if (
            not isinstance(evaluator_reference, Mapping)
            or not evaluator_reference
            or not _bounded_value(evaluator_reference)
        ):
            return (
                "SUFFICIENCY_BASIS_EVALUATOR_REFERENCE_INVALID",
                dimension_id + " evaluator_reference is absent, unbounded, or malformed",
                state,
                not_evaluated,
                False,
            )

        keys = DIMENSION_RULE_KEYS[dimension_id]
        if not (
            _single_boolean_map(record.get("support_postures"), keys["support"])
            and _single_boolean_map(
                record.get("contradiction_postures"), keys["contradiction"]
            )
            and _single_boolean_map(
                record.get("unresolved_postures"), keys["unresolved"]
            )
        ):
            return (
                "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID",
                dimension_id + " rule-input posture maps are invalid",
                state,
                not_evaluated,
                False,
            )
        if not _basis_non_claims_valid(record.get("basis_non_claims")):
            return (
                "SUFFICIENCY_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
                dimension_id + " basis non-claims are missing or flipped",
                state,
                not_evaluated,
                False,
            )
        if (
            record.get("non_conversion_statement")
            != DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
        ):
            return (
                "SUFFICIENCY_BASIS_NON_CONVERSION_STATEMENT_MISMATCH",
                dimension_id + " non-conversion statement does not match",
                state,
                not_evaluated,
                False,
            )
        metadata[dimension_id] = _basis_record_metadata(dimension_id, record)
        derived[dimension_id] = _derive_dimension_result(dimension_id, record)
        checks.append(_check("sufficiency_basis." + dimension_id, True))

    state.update(
        {
            "sufficiency_basis_complete": True,
            "all_dimension_basis_records_bounded": True,
            "all_dimension_basis_records_reference_selected_candidate": True,
            "all_dimension_basis_records_reference_selected_boundary": True,
            "all_dimension_basis_records_contain_evaluator_reference": True,
            "all_dimension_basis_records_contain_rule_input_maps": True,
            "all_dimension_basis_records_non_result_preclaiming": True,
            "all_dimension_basis_records_preserve_non_claims": True,
            "all_dimension_basis_records_non_conversion_validated": True,
            "atomic_sufficiency_basis_gate_passed": True,
            "dimension_basis_metadata": metadata,
        }
    )
    return None, None, state, derived, True


def _candidate_result_from_dimensions(dimension_results: Mapping[str, str]) -> str:
    values = tuple(dimension_results.get(key) for key in SUFFICIENCY_DIMENSION_IDS)
    if DIMENSION_RESULT_NOT_EVALUATED in values:
        return OPERATION_RESULT_REQUIRES_BASIS
    if DIMENSION_RESULT_INDETERMINATE in values:
        return OPERATION_RESULT_INDETERMINATE
    if DIMENSION_RESULT_NOT_SATISFIED in values:
        return OPERATION_RESULT_INSUFFICIENT
    if values and all(value == DIMENSION_RESULT_SATISFIED for value in values):
        return OPERATION_RESULT_SUFFICIENT
    return OPERATION_RESULT_REQUIRES_BASIS


def _dimension_objects(
    dimension_results: Mapping[str, str], basis_state: Mapping[str, Any]
) -> dict[str, dict[str, Any]]:
    metadata = basis_state.get("dimension_basis_metadata")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    gate_passed = basis_state.get("atomic_sufficiency_basis_gate_passed") is True
    dimensions: dict[str, dict[str, Any]] = {}
    for dimension_id in SUFFICIENCY_DIMENSION_IDS:
        result = dimension_results.get(
            dimension_id, DIMENSION_RESULT_NOT_EVALUATED
        )
        basis_metadata = metadata.get(dimension_id)
        basis_metadata = basis_metadata if isinstance(basis_metadata, Mapping) else {}
        keys = DIMENSION_RULE_KEYS[dimension_id]
        dimensions[dimension_id] = {
            "dimension_id": dimension_id,
            "dimension_label": DIMENSION_LABELS[dimension_id],
            "dimension_result": result,
            "dimension_evaluated": gate_passed
            and result != DIMENSION_RESULT_NOT_EVALUATED,
            "dimension_established": gate_passed
            and result != DIMENSION_RESULT_NOT_EVALUATED,
            "basis_referenced": gate_passed,
            "result_derived_from_rule_inputs": gate_passed,
            "support_key": keys["support"],
            "contradiction_key": keys["contradiction"],
            "unresolved_key": keys["unresolved"],
            "basis_items_count": basis_metadata.get("basis_items_count", 0),
            "basis_references_count": basis_metadata.get("basis_references_count", 0),
            "evaluator_reference_supplied": basis_metadata.get(
                "evaluator_reference_supplied", False
            ),
            "basis_non_claims_validated": basis_metadata.get(
                "basis_non_claims_validated", False
            ),
            "non_conversion_statement_validated": basis_metadata.get(
                "non_conversion_statement_validated", False
            ),
            "complete_supplied_basis_omitted": True,
        }
    return dimensions


def _candidate_postures(operation_result: str) -> dict[str, bool]:
    sufficient = operation_result == OPERATION_RESULT_SUFFICIENT
    insufficient = operation_result == OPERATION_RESULT_INSUFFICIENT
    indeterminate = operation_result == OPERATION_RESULT_INDETERMINATE
    completed = sufficient or insufficient or indeterminate
    return {
        "receiver_side_answerable_basis_candidate_sufficient": sufficient,
        "receiver_side_answerable_basis_candidate_insufficient": insufficient,
        "receiver_side_answerable_basis_candidate_indeterminate": indeterminate,
        "candidate_sufficiency_decided": completed,
        "candidate_sufficiency_established": sufficient,
        "candidate_insufficiency_established": insufficient,
        "candidate_indeterminacy_established": indeterminate,
    }


def _operation_object(
    operation_result: str,
    basis_state: Mapping[str, Any],
) -> dict[str, Any]:
    postures = _candidate_postures(operation_result)
    completed = operation_result in {
        OPERATION_RESULT_SUFFICIENT,
        OPERATION_RESULT_INSUFFICIENT,
        OPERATION_RESULT_INDETERMINATE,
    }
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_operation_id": (
            OPERATION_ID
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_type": (
            OPERATION_TYPE
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_version": (
            OPERATION_VERSION
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_scope": (
            OPERATION_SCOPE
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "selected_candidate_sufficiency_boundary_type": (
            SELECTED_SUFFICIENCY_BOUNDARY_TYPE
        ),
        "selected_candidate_sufficiency_boundary_result_required": (
            SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_result": operation_result,
        "candidate_sufficiency_operation_result": operation_result,
        "receiver_side_answerable_basis_candidate_sufficiency_operation_result": (
            operation_result
        ),
        "sufficiency_basis_supplied": basis_state.get(
            "sufficiency_basis_supplied"
        )
        is True,
        "sufficiency_basis_complete": basis_state.get(
            "sufficiency_basis_complete"
        )
        is True,
        "atomic_sufficiency_basis_gate_passed": basis_state.get(
            "atomic_sufficiency_basis_gate_passed"
        )
        is True,
        "candidate_sufficiency_operation_recorded": completed,
        "candidate_sufficiency_operation_result_recorded": completed,
        "candidate_sufficiency_operation_exhausted": completed,
        "partial_evaluation_recorded": False,
        **postures,
        **_canonical_non_claims(),
    }


def _declared_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    records = request.get("sufficiency_basis_records")
    record_keys = (
        [
            dimension_id
            for dimension_id in SUFFICIENCY_DIMENSION_IDS
            if dimension_id in records
        ]
        if isinstance(records, Mapping)
        else []
    )
    expected = _expected_request_values()

    def canonical(field: str) -> Any:
        return expected[field] if request.get(field) == expected[field] else None

    return {
        "intent": (
            request.get("intent")
            if request.get("intent") in SUPPORTED_INTENTS
            else None
        ),
        "operation_id": canonical("operation_id"),
        "operation_type": canonical("operation_type"),
        "operation_version": canonical("operation_version"),
        "operation_scope": canonical("operation_scope"),
        "receiver_side_answerable_basis_candidate_id": canonical(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "receiver_side_answerable_basis_candidate_type": canonical(
            "receiver_side_answerable_basis_candidate_type"
        ),
        "receiver_side_answerable_basis_candidate_scope": canonical(
            "receiver_side_answerable_basis_candidate_scope"
        ),
        "selected_candidate_reception_operation_id": canonical(
            "selected_candidate_reception_operation_id"
        ),
        "selected_candidate_evaluation_boundary_id": canonical(
            "selected_candidate_evaluation_boundary_id"
        ),
        "selected_candidate_evaluation_operation_id": canonical(
            "selected_candidate_evaluation_operation_id"
        ),
        "selected_candidate_sufficiency_boundary_id": canonical(
            "selected_candidate_sufficiency_boundary_id"
        ),
        "selected_candidate_sufficiency_boundary_type": canonical(
            "selected_candidate_sufficiency_boundary_type"
        ),
        "governing_sufficiency_operation_specification_path": canonical(
            "governing_sufficiency_operation_specification_path"
        ),
        "selected_sufficiency_boundary_artifact_path": canonical(
            "selected_sufficiency_boundary_artifact_path"
        ),
        "admissible_future_route": canonical("admissible_future_route"),
        "sufficiency_basis_supplied": (
            request.get("sufficiency_basis_supplied")
            if isinstance(request.get("sufficiency_basis_supplied"), bool)
            else False
        ),
        "sufficiency_basis_record_count": (
            len(records)
            if isinstance(records, Mapping) and len(records) <= MAX_MAPPING_ITEMS
            else len(record_keys)
        ),
        "sufficiency_basis_dimension_ids": record_keys,
        "complete_supplied_basis_omitted": True,
        "declared_non_claims_validated": _declared_non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
    }


def _operation_statement(
    upstream_validated: bool,
    operation_result: str,
) -> dict[str, bool]:
    completed = operation_result in {
        OPERATION_RESULT_SUFFICIENT,
        OPERATION_RESULT_INSUFFICIENT,
        OPERATION_RESULT_INDETERMINATE,
    }
    return {
        "one_selected_allowed_boundary_consumed_as_upstream_standing": (
            upstream_validated
        ),
        "boundary_not_reopened": True,
        "boundary_not_rerun": True,
        "separate_sufficiency_basis_required": True,
        "evaluation_basis_not_reused_as_sufficiency_basis": True,
        "no_caller_selected_dimension_result_accepted": True,
        "no_caller_selected_candidate_result_accepted": True,
        "partial_evaluation_does_not_stand": True,
        "operation_single_use_when_completed": True,
        "operation_exhausted_only_after_completed_candidate_result": True,
        "completed_candidate_result_recorded": completed,
        "result_level_non_claims_canonical_false": True,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
        "open_does_not_mean_next_unless_separately_selected": True,
    }


def _operation_non_meaning() -> dict[str, bool]:
    return {
        "candidate_evaluation_is_not_candidate_sufficiency": True,
        "all_evaluation_dimensions_satisfied_is_not_candidate_sufficiency": True,
        "consideration_allowed_is_not_candidate_sufficiency_decided": True,
        "sufficiency_basis_is_not_sufficiency_result": True,
        "candidate_sufficient_is_not_receiver_attestation": True,
        "candidate_sufficient_is_not_receiver_answerable_receipt": True,
        "candidate_sufficient_is_not_presence_support": True,
        "candidate_insufficient_is_not_candidate_existence_rejection": True,
        "candidate_indeterminate_is_not_candidate_insufficiency": True,
        "operation_exhaustion_is_not_downstream_authorization": True,
        "evaluator_reference_is_not_authority_identity_standing_or_truth": True,
        "basis_items_are_not_established_truth": True,
        "basis_references_are_not_verified_provenance": True,
    }


def _what_remains_open(outcome: str, operation_result: str) -> list[str]:
    if outcome == OUTCOME_REQUIRES_BASIS:
        return list(WAITING_WHAT_REMAINS_OPEN)
    if outcome == OUTCOME_RECORDED and operation_result == OPERATION_RESULT_SUFFICIENT:
        return list(SUFFICIENT_WHAT_REMAINS_OPEN)
    if outcome == OUTCOME_RECORDED and operation_result in {
        OPERATION_RESULT_INSUFFICIENT,
        OPERATION_RESULT_INDETERMINATE,
    }:
        return list(NON_SUFFICIENT_WHAT_REMAINS_OPEN)
    return list(INCOMPLETE_BRANCH_WHAT_REMAINS_OPEN)


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation"
    )
    basis = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_basis"
    )
    dimensions = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
    )
    upstream = result.get("upstream_basis")
    operation = operation if isinstance(operation, Mapping) else {}
    basis = basis if isinstance(basis, Mapping) else {}
    dimensions = dimensions if isinstance(dimensions, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "operation_result": operation.get("operation_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "operation_id": operation.get("operation_id"),
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "selected_candidate_id": operation.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "selected_boundary_id": operation.get(
            "selected_candidate_sufficiency_boundary_id"
        ),
        "selected_boundary_result_required": operation.get(
            "selected_candidate_sufficiency_boundary_result_required"
        ),
        "upstream_boundary_validated": all(
            upstream.get("upstream_boundary_validation", {}).values()
        )
        if isinstance(upstream.get("upstream_boundary_validation"), Mapping)
        and upstream.get("upstream_boundary_validation")
        else False,
        "atomic_sufficiency_basis_gate_passed": basis.get(
            "atomic_sufficiency_basis_gate_passed"
        )
        is True,
        "sufficiency_basis_supplied": basis.get("sufficiency_basis_supplied")
        is True,
        "sufficiency_basis_complete": basis.get("sufficiency_basis_complete")
        is True,
        "dimension_results": {
            dimension_id: entry.get("dimension_result")
            for dimension_id, entry in dimensions.items()
            if isinstance(entry, Mapping)
        },
        "candidate_result_postures": {
            field: operation.get(field)
            for field in (
                "receiver_side_answerable_basis_candidate_sufficient",
                "receiver_side_answerable_basis_candidate_insufficient",
                "receiver_side_answerable_basis_candidate_indeterminate",
                "candidate_sufficiency_decided",
                "candidate_sufficiency_established",
                "candidate_insufficiency_established",
                "candidate_indeterminacy_established",
            )
        },
        "candidate_sufficiency_operation_exhausted": operation.get(
            "candidate_sufficiency_operation_exhausted"
        ),
        "repeated_reusable_rerun_retry_debt_obligation_locks_false": all(
            operation.get(field) is False
            for field in REQUIRED_FALSE_NON_CLAIMS[:6]
        ),
        "receiver_receipt_presence_downstream_locks_false": all(
            operation.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS
        ),
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
        "marker_validation": copy.deepcopy(upstream.get("marker_validation", {})),
        "complete_supplied_basis_omitted": basis.get(
            "complete_supplied_basis_omitted"
        )
        is True,
        "complete_boundary_artifact_omitted": upstream.get(
            "complete_boundary_artifact_omitted"
        )
        is True,
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    operation_result: str,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    basis_state: Mapping[str, Any] | None = None,
    dimension_results: Mapping[str, str] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    bounded_upstream = (
        copy.deepcopy(dict(upstream))
        if isinstance(upstream, Mapping)
        else _empty_upstream_basis(request)
    )
    bounded_basis = (
        copy.deepcopy(dict(basis_state))
        if isinstance(basis_state, Mapping)
        else _empty_basis_state()
    )
    bounded_dimension_results = (
        dict(dimension_results)
        if isinstance(dimension_results, Mapping)
        else {
            dimension_id: DIMENSION_RESULT_NOT_EVALUATED
            for dimension_id in SUFFICIENCY_DIMENSION_IDS
        }
    )
    operation = _operation_object(operation_result, bounded_basis)
    dimensions = _dimension_objects(bounded_dimension_results, bounded_basis)
    upstream_validated = (
        bool(bounded_upstream.get("upstream_boundary_validation"))
        and all(bounded_upstream["upstream_boundary_validation"].values())
        and bounded_upstream.get("corrected_open_state_validation") is True
    )
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_sufficiency_operation_metadata": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "selected_sufficiency_boundary_artifact_path": (
                str(SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH)
                if request.get("selected_sufficiency_boundary_artifact_path")
                == str(SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH)
                else None
            ),
        },
        "declared_receiver_side_answerable_basis_candidate_sufficiency_operation_basis": (
            _declared_basis(request)
        ),
        "upstream_basis": bounded_upstream,
        "receiver_side_answerable_basis_candidate_sufficiency_operation": operation,
        "receiver_side_answerable_basis_candidate_sufficiency_operation_basis": (
            bounded_basis
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions": (
            dimensions
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_checks": (
            copy.deepcopy(checks)
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_statement": (
            _operation_statement(upstream_validated, operation_result)
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_non_meaning": (
            _operation_non_meaning()
        ),
        "operation_result_detail": {
            "operation_result": operation_result,
            "atomic_sufficiency_basis_gate_passed": bounded_basis.get(
                "atomic_sufficiency_basis_gate_passed"
            )
            is True,
            "evaluated_dimension_count": sum(
                entry.get("dimension_evaluated") is True
                for entry in dimensions.values()
            ),
            "candidate_result_posture_count": sum(
                operation.get(field) is True
                for field in (
                    "receiver_side_answerable_basis_candidate_sufficient",
                    "receiver_side_answerable_basis_candidate_insufficient",
                    "receiver_side_answerable_basis_candidate_indeterminate",
                )
            ),
            "candidate_result_precedence": (
                "INDETERMINATE_THEN_INSUFFICIENT_THEN_SUFFICIENT"
            ),
            "complete_supplied_basis_omitted": True,
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": _what_remains_open(outcome, operation_result),
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
        "failed_check_count": sum(check.get("passed") is False for check in checks),
        "passed_check_count": sum(check.get("passed") is True for check in checks),
    }
    result[
        "receiver_side_answerable_basis_candidate_sufficiency_operation_summary"
    ] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one selected candidate-sufficiency operation."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = (
            build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        declared_request = (
            build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request()
        )
        _add_failure(checks, "declared_request_mapping", "REQUEST_NOT_MAPPING")
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared operation request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        _add_failure(checks, "declared_request", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            code=code,
            reason=reason,
        )
    if declared_request["intent"] == INTENT_DO_NOT_RECORD:
        return _result(
            declared_request,
            OUTCOME_NOT_RECORDED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
        )

    code, reason, upstream = _validate_upstream_boundary(declared_request, checks)
    if code is not None:
        _add_failure(checks, "upstream_boundary", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            upstream=upstream,
            code=code,
            reason=reason,
        )

    code, reason, basis_state, dimension_results, gate_passed = (
        _validate_basis_records(declared_request, checks)
    )
    if code is not None:
        _add_failure(checks, "sufficiency_basis", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            upstream=upstream,
            basis_state=basis_state,
            code=code,
            reason=reason,
        )
    if not gate_passed:
        return _result(
            declared_request,
            OUTCOME_REQUIRES_BASIS,
            OPERATION_RESULT_REQUIRES_BASIS,
            checks,
            upstream=upstream,
            basis_state=basis_state,
            dimension_results=dimension_results,
        )

    operation_result = _candidate_result_from_dimensions(dimension_results)
    if operation_result == OPERATION_RESULT_REQUIRES_BASIS:
        return _result(
            declared_request,
            OUTCOME_REQUIRES_BASIS,
            operation_result,
            checks,
            upstream=upstream,
            basis_state=basis_state,
            dimension_results=dimension_results,
        )
    return _result(
        declared_request,
        OUTCOME_RECORDED,
        operation_result,
        checks,
        upstream=upstream,
        basis_state=basis_state,
        dimension_results=dimension_results,
    )


def resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Read one request path without discovery and resolve it."""
    payload, error = _read_json(request_path)
    if error is not None or not isinstance(payload, Mapping):
        request = (
            build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request()
        )
        checks = [_check("declared_request_path", False, "REQUEST_NOT_MAPPING")]
        return _result(
            request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="request path is unavailable, not parseable, or not a mapping",
        )
    return resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min(
        payload
    )


def build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact material-omitting operation summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            path.stem + "_" + f"{index:03d}" + path.suffix
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def _contains_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "basis_items",
        "basis_references",
        "evaluator_reference",
        "candidate_material",
        "raw_candidate_material",
        "candidate_packet",
        "capture_material",
        "complete_capture_data",
        "raw_samples",
        "zip_bytes",
        "complete_boundary_artifact",
        "selected_boundary_artifact",
        "complete_upstream_checks",
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_checks",
        "receiver_side_answerable_basis_candidate_evaluation_operation_checks",
        "receiver_side_answerable_basis_candidate_evaluation_operation_basis",
    }
    if isinstance(value, Mapping):
        return any(
            key in forbidden_keys or _contains_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_complete_material(item) for item in value)
    return False


def _candidate_postures_valid(
    operation: Mapping[str, Any], operation_result: str
) -> bool:
    expected = _candidate_postures(operation_result)
    return all(operation.get(field) is value for field, value in expected.items())


def _dimension_results_from_result(result: Mapping[str, Any]) -> dict[str, str] | None:
    dimensions = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
    )
    if not isinstance(dimensions, Mapping) or set(dimensions) != set(
        SUFFICIENCY_DIMENSION_IDS
    ):
        return None
    values: dict[str, str] = {}
    for dimension_id in SUFFICIENCY_DIMENSION_IDS:
        entry = dimensions.get(dimension_id)
        if (
            not isinstance(entry, Mapping)
            or entry.get("dimension_id") != dimension_id
            or entry.get("dimension_result") not in DIMENSION_RESULT_FAMILY
        ):
            return None
        evaluated = entry.get("dimension_result") != DIMENSION_RESULT_NOT_EVALUATED
        if (
            entry.get("dimension_evaluated") is not evaluated
            or entry.get("dimension_established") is not evaluated
            or entry.get("basis_referenced") is not evaluated
            or entry.get("result_derived_from_rule_inputs") is not evaluated
        ):
            return None
        values[dimension_id] = entry["dimension_result"]
    return values


def _result_branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    operation = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation"
    )
    if not isinstance(operation, Mapping):
        return False
    operation_result = operation.get("operation_result")
    if operation_result not in OPERATION_RESULT_FAMILY:
        return False
    if (
        operation.get("candidate_sufficiency_operation_result") != operation_result
        or operation.get(
            "receiver_side_answerable_basis_candidate_sufficiency_operation_result"
        )
        != operation_result
    ):
        return False
    if not _candidate_postures_valid(operation, operation_result):
        return False
    dimensions = _dimension_results_from_result(result)
    if dimensions is None:
        return False

    completed = operation_result in {
        OPERATION_RESULT_SUFFICIENT,
        OPERATION_RESULT_INSUFFICIENT,
        OPERATION_RESULT_INDETERMINATE,
    }
    operation_fields_valid = (
        operation.get("candidate_sufficiency_operation_recorded") is completed
        and operation.get("candidate_sufficiency_operation_result_recorded")
        is completed
        and operation.get("candidate_sufficiency_operation_exhausted") is completed
    )
    if not operation_fields_valid:
        return False

    if outcome == OUTCOME_RECORDED:
        return (
            completed
            and operation.get("sufficiency_basis_supplied") is True
            and operation.get("sufficiency_basis_complete") is True
            and operation.get("atomic_sufficiency_basis_gate_passed") is True
            and _candidate_result_from_dimensions(dimensions) == operation_result
            and all(
                value != DIMENSION_RESULT_NOT_EVALUATED
                for value in dimensions.values()
            )
        )
    if outcome == OUTCOME_REQUIRES_BASIS:
        return (
            operation_result == OPERATION_RESULT_REQUIRES_BASIS
            and operation.get("sufficiency_basis_complete") is False
            and operation.get("atomic_sufficiency_basis_gate_passed") is False
            and all(
                value == DIMENSION_RESULT_NOT_EVALUATED
                for value in dimensions.values()
            )
        )
    if outcome in {OUTCOME_BLOCKED, OUTCOME_NOT_RECORDED}:
        return (
            operation_result == OPERATION_RESULT_NOT_EVALUATED
            and all(
                value == DIMENSION_RESULT_NOT_EVALUATED
                for value in dimensions.values()
            )
        )
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    normalized = "/" + "/".join(part.lower() for part in path.resolve().parts) + "/"
    forbidden_fragments = (
        "/spec/",
        "/tests/",
        "/reference/",
        "candidate_reception",
        "candidate-reception",
        "evaluation_boundary",
        "evaluation-boundary",
        "/evaluation/",
        "evaluation_basis",
        "evaluation-basis",
        "evaluation_operation",
        "evaluation-operation",
        "sufficiency_boundary",
        "sufficiency-boundary",
        "presence",
        "relation",
        "identity",
        "field",
        "runtime",
        "/api/",
        "_api",
        "public_api",
        "public-api",
        "public_intake",
        "public-intake",
        "descendant",
        "receiver_capture",
        "receiver-capture",
    )
    return any(fragment in normalized for fragment in forbidden_fragments)


def write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid bounded operation result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    if set(result) != RESULT_SECTIONS:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: result sections are incomplete or unexpected"
        )
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: incompatible result metadata"
        )
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: unsupported result outcome"
        )
    if (
        not isinstance(result.get("failed_check_count"), int)
        or isinstance(result.get("failed_check_count"), bool)
        or not isinstance(result.get("passed_check_count"), int)
        or isinstance(result.get("passed_check_count"), bool)
        or result.get("failed_check_count", -1) < 0
        or result.get("passed_check_count", -1) < 0
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: check counts are malformed"
        )
    if not _declared_non_claims_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: non-claims are not canonical false"
        )
    operation = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation"
    )
    if not isinstance(operation, Mapping) or not all(
        operation.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: repeated or downstream locks are not false"
        )
    if not _result_branch_valid(result):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: outcome, operation result, dimensions, or exhaustion mismatch"
        )
    result_detail = result.get("operation_result_detail")
    if (
        not isinstance(result_detail, Mapping)
        or result_detail.get("operation_result") != operation.get("operation_result")
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: operation result detail does not match"
        )
    checks = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_checks"
    )
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping) for check in checks
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: checks are malformed"
        )
    for check in checks:
        for field in ("failure_code", "block_code"):
            if field in check and check.get(field) not in BLOCK_CODES:
                raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
                    "WRITE_REFUSED: check contains a non-public failure code"
                )
    expected_failed = sum(check.get("passed") is False for check in checks)
    expected_passed = sum(check.get("passed") is True for check in checks)
    if (
        result.get("failed_check_count") != expected_failed
        or result.get("passed_check_count") != expected_passed
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: check counts do not match checks"
        )
    summary = result.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_summary"
    )
    if not isinstance(summary, Mapping) or dict(summary) != _summary_from_result(result):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: operation summary does not match result"
        )
    block = result.get("block")
    if not isinstance(block, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: block posture is malformed"
        )
    if result.get("outcome") == OUTCOME_BLOCKED:
        if (
            block.get("blocked") is not True
            or block.get("code") not in BLOCK_CODES
            or result.get("failed_check_count", 0) <= 0
        ):
            raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
                "WRITE_REFUSED: blocked outcome lacks public failure posture"
            )
    elif (
        block.get("blocked") is not False
        or block.get("code") is not None
        or block.get("block_code") is not None
        or block.get("reason") is not None
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: non-blocked outcome contains block posture"
        )
    if (
        result.get("outcome") != OUTCOME_BLOCKED
        and result.get("failed_check_count") != 0
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: non-blocked outcome contains failed checks"
        )
    if _contains_complete_material(result):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: complete basis, boundary, candidate, capture, or checks material"
        )

    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: output path is forbidden"
        )
    target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(
                dict(result),
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
