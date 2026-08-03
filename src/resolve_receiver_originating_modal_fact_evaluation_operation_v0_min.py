"""Resolve one bounded receiver-originating modal-fact evaluation operation.

The resolver reads only the governing specification, one exact completed
source-admissibility boundary, one exact declaration surface, three exact
carriage artifacts, and an explicitly supplied request path. It evaluates
source support for two receiver-allocated conditions without establishing
body-native fact, truth, authority, standing, identity, or presence.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESOLVER_MODULE = "resolve_receiver_originating_modal_fact_evaluation_operation_v0_min"
RESULT_VERSION = "0.1.0"

OPERATION_ID = "receiver_originating_modal_fact_evaluation_operation_001"
OPERATION_TYPE = "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "EVALUATE_ONE_EXACT_RECEIVER_ORIGINATING_DECLARATION_FOR_"
    "TWO_RECEIVER_ALLOCATED_MODAL_FACTS_ONLY"
)

INTENT_RECORD = "RECORD_RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD,)

OUTCOME_SUPPORTED = "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED"
OUTCOME_REQUIRES_BASIS = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_REQUIRES_BASIS"
)
OUTCOME_INDETERMINATE = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_INDETERMINATE"
)
OUTCOME_BLOCKED = "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_SUPPORTED,
    OUTCOME_REQUIRES_BASIS,
    OUTCOME_INDETERMINATE,
    OUTCOME_BLOCKED,
)

OPERATION_RESULT_SUPPORTED = "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_SUPPORTED"
OPERATION_RESULT_REQUIRES_BASIS = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_REQUIRES_BASIS"
)
OPERATION_RESULT_INDETERMINATE = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_INDETERMINATE"
)
OPERATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
OPERATION_RESULT_FAMILY = (
    OPERATION_RESULT_SUPPORTED,
    OPERATION_RESULT_REQUIRES_BASIS,
    OPERATION_RESULT_INDETERMINATE,
    OPERATION_RESULT_NOT_EVALUATED,
)
RESULT_FAMILY = OPERATION_RESULT_FAMILY

TARGET_EVALUATION_SUPPORTED = "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
TARGET_EVALUATION_REQUIRES_BASIS = "REQUIRES_BASIS"
TARGET_EVALUATION_INDETERMINATE = "INDETERMINATE"
TARGET_EVALUATION_NOT_EVALUATED = "NOT_EVALUATED"
TARGET_CONDITION_EVALUATION_FAMILY = (
    TARGET_EVALUATION_SUPPORTED,
    TARGET_EVALUATION_REQUIRES_BASIS,
    TARGET_EVALUATION_INDETERMINATE,
    TARGET_EVALUATION_NOT_EVALUATED,
)
CONDITION_EVALUATION_FAMILY = TARGET_CONDITION_EVALUATION_FAMILY

TARGET_CONDITIONS = (
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
)
REQUIRED_MATTER_TUPLE = TARGET_CONDITIONS
MATTER_TUPLE = REQUIRED_MATTER_TUPLE
TARGET_DECLARATION_RECORDS = {
    "receiver_answerable_basis_refusable": "could_have_been_refused",
    "receiver_answerable_basis_could_have_been_withheld": (
        "could_have_been_withheld"
    ),
}

EXCLUDED_CONDITIONS = (
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_controlled_by_declaring_side",
    "repo_local_execution_only",
    "operator_only_attestation",
    "derivative_rendering_attestation",
    "same_custody_countersignature",
    "automatic_acknowledgement",
    "generated_affirmation",
    "forged_receiver_attestation",
    "inadmissible_receiver_basis",
)

SELECTED_SOURCE_CLASS = "RECEIVER_ORIGINATING_DECLARATION_SOURCE"
SELECTED_RELATION_CLASS = "RECEIVER_ALLOCATED_MODAL_FACT_EVALUATION_RELATION"
SELECTED_MATTER_CLASS = (
    "RECEIVER_ANSWERABLE_BASIS_REFUSABILITY_AND_WITHHOLDABILITY_ONLY"
)
SELECTED_SOURCE_ORIGIN = "RECEIVER_ORIGINATING"
SELECTED_SOURCE_PROVENANCE_POSTURE = "DECLARED_RECEIVER_CUSTODY_REFERENCE_ONLY"
SELECTED_SOURCE_ARRIVAL_POSTURE = "CARRIED_ARRIVAL"

REPO_ROOT = Path(__file__).resolve().parents[1]

GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_V0_MIN_SPEC.md"
)
BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_originating_modal_fact_source_admissibility_boundary_v0_min/"
    "receiver_originating_modal_fact_source_admissibility_boundary_001__"
    "receiver_originating_modal_fact_source_admissibility_boundary_"
    "v0_min_result.json"
)
DECLARATION_SURFACE_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001/extracted/receiver_attestation_001/"
    "freely_given_statement.txt"
)
CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_"
    "v0_min_result_001.json"
)
RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_receiver_attestation_operation_"
    "v0_min_result_001.json"
)
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation_"
    "v0_min/receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001__receiver_side_answerable_"
    "basis_receiver_answerable_receipt_operation_v0_min_result.json"
)
DECLARATION_ARCHIVE_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001/original_zip/receiver_attestation_001.zip"
)
DECLARATION_ARCHIVE_MEMBER = "receiver_attestation_001/freely_given_statement.txt"

GOVERNING_SPECIFICATION_PATH = REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SPECIFICATION_PATH
BOUNDARY_ARTIFACT_PATH = REPO_ROOT / BOUNDARY_ARTIFACT_RELATIVE_PATH
DECLARATION_SURFACE_PATH = REPO_ROOT / DECLARATION_SURFACE_RELATIVE_PATH
CANDIDATE_SUFFICIENCY_ARTIFACT_PATH = (
    REPO_ROOT / CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ATTESTATION_ARTIFACT_PATH = (
    REPO_ROOT / RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH = (
    REPO_ROOT / RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
)
DECLARATION_ARCHIVE_PATH = REPO_ROOT / DECLARATION_ARCHIVE_RELATIVE_PATH

OUTPUT_ROOT_NAME = (
    "integrity_host_v0_min_coexistence_"
    "receiver_originating_modal_fact_evaluation_operation_v0_min"
)
CANONICAL_OUTPUT_ROOT = REPO_ROOT / "artifacts" / OUTPUT_ROOT_NAME
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "receiver_originating_modal_fact_evaluation_operation_001__"
    "receiver_originating_modal_fact_evaluation_operation_v0_min_result.json"
)

RESULT_SECTIONS = frozenset(
    {
        "admissible_future_route",
        "atomic_operation_basis_posture",
        "block",
        "blocked_conversions",
        "boundary_artifact_validation",
        "candidate_sufficiency_artifact_validation",
        "completed_modal_fact_evaluation_result_posture_count",
        "declared_receiver_originating_modal_fact_evaluation_operation_request",
        "excluded_condition_posture",
        "failed_check_count",
        "lineage_preservation_posture",
        "non_claims",
        "omission_posture",
        "operation_decision",
        "operation_posture",
        "operation_result",
        "outcome",
        "passed_check_count",
        "prior_presence_preservation_posture",
        "receiver_answerable_receipt_artifact_validation",
        "receiver_attestation_artifact_validation",
        "receiver_originating_declaration_validation",
        "receiver_originating_modal_fact_evaluation_operation",
        "receiver_originating_modal_fact_evaluation_operation_checks",
        "receiver_originating_modal_fact_evaluation_operation_metadata",
        "receiver_originating_modal_fact_evaluation_operation_non_meaning",
        "receiver_originating_modal_fact_evaluation_operation_result",
        "receiver_originating_modal_fact_evaluation_operation_statement",
        "receiver_originating_modal_fact_evaluation_operation_summary",
        "resolver_module",
        "result_level_non_claims_canonical_false",
        "result_version",
        "source_selection_and_carriage_lineage",
        "specification_validation",
        "target_condition_evaluations",
        "target_support_posture",
        "what_remains_open",
    }
)

BOUNDARY_SHA256 = "f24795566eb369ad935e2212aba83ef68bfd1661363cc94da2f53498cc2935ac"
DECLARATION_SHA256 = "9c1aeb888cd182fdbce789e1bb191f5778712f82483d7eca1334800dac4dd3eb"
DECLARATION_ARCHIVE_SHA256 = (
    "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c"
)
CANDIDATE_SUFFICIENCY_SHA256 = (
    "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4"
)
RECEIVER_ATTESTATION_SHA256 = (
    "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9"
)
RECEIVER_ANSWERABLE_RECEIPT_SHA256 = (
    "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb"
)

DECLARATION_BYTE_COUNT = 207
DECLARATION_CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
DECLARATION_PROVENANCE_REFERENCE = (
    "declared://receiver-custody/IAMMAI-RECEIVER/receiver_attestation_001"
)
DECLARATION_RECEIPT_BUNDLE = "receiver_attestation_001"
DECLARATION_RECEIVER_LABEL = "Mario"
REQUIRED_DECLARATION_RECORDS = {
    "freely_given": "true",
    "could_have_been_refused": "true",
    "could_have_been_withheld": "true",
    "prescribed_by_declaring_side": "false",
    "attestation_words_authored_by_receiver_only": "true",
    "confirmed_by_receiver_at": "2026-07-28T06:37:56Z",
}

BOUNDARY_RESOLVER_MODULE = (
    "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min"
)
BOUNDARY_ID = "receiver_originating_modal_fact_source_admissibility_boundary_001"
BOUNDARY_TYPE = "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_EXACT_RECEIVER_ORIGINATING_DECLARATION_AS_SOURCE_FOR_"
    "TWO_RECEIVER_ALLOCATED_MODAL_FACTS_ONLY"
)
BOUNDARY_OUTCOME_REQUIRED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED"
)
BOUNDARY_RESULT_REQUIRED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_ALLOWED"
)
BOUNDARY_PASSED_CHECK_COUNT = 308
BOUNDARY_FUTURE_ROUTE_REQUIRED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_THEN_"
    "SEPARATE_RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_ONLY"
)

CANDIDATE_SUFFICIENCY_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min"
)
CANDIDATE_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
CANDIDATE_SUFFICIENCY_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
)
CANDIDATE_SUFFICIENCY_OPERATION_SCOPE = (
    "DECIDE_SUFFICIENCY_POSTURE_OF_ONE_SELECTED_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_RECORDED"
)
CANDIDATE_SUFFICIENCY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
)
CANDIDATE_SUFFICIENCY_PASSED_CHECK_COUNT = 140
REQUIRED_SUFFICIENCY_DIMENSIONS = (
    "receiver_answerability_fit",
    "selected_purpose_adequacy",
    "bounded_material_completeness",
    "unresolved_contradiction_posture",
    "unsupported_assumption_dependency",
    "scope_constrained_usability",
    "refusal_withholding_compatibility",
    "provenance_capture_limitation_posture",
)

RECEIVER_ATTESTATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min"
)
RECEIVER_ATTESTATION_OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_001"
)
RECEIVER_ATTESTATION_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION"
)
RECEIVER_ATTESTATION_OPERATION_SCOPE = (
    "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_FOR_"
    "ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
)
RECEIVER_ATTESTATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_RECORDED"
)
RECEIVER_ATTESTATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
)
RECEIVER_ATTESTATION_PASSED_CHECK_COUNT = 160

RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation_001"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE = (
    "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
    "RECEIVER_ATTESTATION_RESULT_ONLY"
)
RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT = 357

PRIOR_PRESENCE_OUTCOME = (
    "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS"
)
PRIOR_PRESENCE_RESULT = "REQUIRES_RECEIVER_ANSWERABLE_BASIS"
PRIOR_SATISFIED_CONDITIONS = (
    "receiver_attested",
    "receiver_answerable_receipt_present",
)
PRIOR_REQUIRES_BASIS_CONDITIONS = (
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_controlled_by_declaring_side",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "repo_local_execution_only",
    "operator_only_attestation",
    "derivative_rendering_attestation",
    "same_custody_countersignature",
    "automatic_acknowledgement",
    "generated_affirmation",
    "forged_receiver_attestation",
    "inadmissible_receiver_basis",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "receiver_answerable_basis_refusable_established",
    "receiver_answerable_basis_could_have_been_withheld_established",
    "receiver_actual_refusal_established",
    "receiver_actual_withholding_established",
    "receiver_freedom_established",
    "receiver_originating_declaration_truth_created",
    "receiver_originating_declaration_authority_created",
    "receiver_originating_declaration_native_standing_created",
    "source_authority_created",
    "canon_admission_created",
    "governance_force_created",
    "truth_created",
    "standing_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "identity_created",
    "custody_created",
    "custody_proven",
    "provenance_created",
    "provenance_proven",
    "physical_validity_created",
    "physical_validity_proven",
    "relation_created",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    (
        "repeated_receiver_originating_modal_fact_"
        "evaluation_operation_permission_created"
    ),
    (
        "reusable_receiver_originating_modal_fact_"
        "evaluation_operation_route_created"
    ),
    (
        "same_receiver_originating_modal_fact_"
        "evaluation_operation_rerun_authorized"
    ),
    (
        "automatic_receiver_originating_modal_fact_"
        "evaluation_operation_retry_created"
    ),
    "receiver_originating_modal_fact_evaluation_operation_debt_created",
    "receiver_originating_modal_fact_evaluation_operation_obligation_created",
    "scheduled_receiver_originating_modal_fact_evaluation_created",
    "scheduled_presence_re_evaluation_created",
    "automatic_next_step_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
)

LINEAGE_PRESERVATION_FIELDS = (
    "selected_source_remains_receiver_originating",
    "source_relation_remains_legible",
    "declared_provenance_reference_remains_legible",
    "carried_arrival_remains_non_native",
    "source_not_naturalized",
    "native_standing_not_created",
    "jurisdiction_not_collapsed",
    "custody_and_jurisdiction_distinction_preserved_without_custody_proof",
    "prior_intake_and_admission_chronology_preserved",
    "prior_candidate_sufficiency_remains_limited_to_original_matter",
    "prior_receiver_attestation_result_preserved",
    "prior_receiver_answerable_receipt_result_preserved",
    "prior_presence_requires_basis_result_preserved",
    "source_admissibility_boundary_result_preserved",
    (
        "no_prior_artifact_repaired_invalidated_superseded_"
        "normalized_replaced_or_overwritten"
    ),
    "contaminated_lineage_unchanged",
)

BOUNDARY_LINEAGE_PRESERVATION_FIELDS = tuple(
    field
    for field in LINEAGE_PRESERVATION_FIELDS
    if field != "source_admissibility_boundary_result_preserved"
)

OMISSION_POSTURE_FIELDS = (
    "complete_upstream_artifacts_omitted",
    "complete_declaration_body_omitted_beyond_compact_identity_and_two_records",
    "complete_candidate_sufficiency_material_omitted",
    "complete_bounded_capture_signal_bodies_omitted",
    "archive_bytes_omitted",
    "alternative_declarations_omitted",
    "alternative_artifacts_omitted",
    "unrelated_receiver_side_material_omitted",
    "excluded_condition_evidence_bodies_omitted",
)

NON_MEANING_FIELDS = (
    "prior_lawful_requires_basis_result_is_not_failure",
    "boundary_allowance_is_not_source_use",
    "source_admissibility_is_not_supported_evaluation",
    "declaration_record_is_not_evaluated_support",
    "evaluated_support_is_not_actual_refusal",
    "evaluated_support_is_not_actual_withholding",
    "receiver_originating_statement_is_not_universal_freedom",
    "candidate_sufficiency_is_not_target_evaluation",
    "receipt_is_not_target_evaluation",
    "supported_evaluation_is_not_declaration_truth",
    "supported_evaluation_is_not_source_authority",
    "supported_evaluation_is_not_native_standing",
    "supported_evaluation_is_not_general_truth",
    "supported_evaluation_is_not_standing",
    "supported_evaluation_is_not_presence",
    "operation_exhaustion_is_not_establishment",
    "operation_exhaustion_is_not_complete_receiver_answerable_basis",
    "operation_exhaustion_is_not_presence",
    "open_does_not_mean_next",
)

BLOCKED_CONVERSIONS = (
    "boundary_allowance_to_supported_evaluation_without_operation",
    "source_admissibility_to_source_supported_evaluation",
    "declaration_record_to_body_native_modal_fact",
    "declaration_to_actual_refusal",
    "declaration_to_actual_withholding",
    "declaration_to_receiver_freedom",
    "candidate_evaluation_to_target_support",
    "candidate_sufficiency_to_target_support",
    "attestation_to_target_support",
    "receipt_to_target_support",
    "source_supported_evaluation_to_declaration_truth",
    "source_supported_evaluation_to_source_authority",
    "source_supported_evaluation_to_native_standing",
    "source_supported_evaluation_to_general_truth_or_standing",
    "source_supported_evaluation_to_presence",
    "two_supported_targets_to_complete_receiver_answerable_basis",
    "two_supported_targets_to_presence_re_evaluation",
    "carried_arrival_to_body_native_fact",
    (
        "operation_exhaustion_to_repeat_reusable_rerun_retry_debt_"
        "obligation_scheduled_work_or_automatic_next"
    ),
    "operation_to_repair_scan_discovery_or_validation_enforcement",
    "operation_to_contaminated_lineage_validation",
)

SPEC_REQUIRED_MARKERS = (
    (
        "title",
        "# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum Specification",
    ),
    ("operation_identity", "## 2. Operation Identity"),
    ("operation_id", "receiver_originating_modal_fact_evaluation_operation_001"),
    ("operation_type", OPERATION_TYPE),
    ("operation_scope", OPERATION_SCOPE),
    ("reference_law", "## 3. Governing Reference Law"),
    ("boundary_basis", "## 4. Exact Completed Boundary Basis"),
    ("boundary_path", str(BOUNDARY_ARTIFACT_RELATIVE_PATH)),
    ("boundary_digest", BOUNDARY_SHA256),
    ("selected_source", "## 5. Exact Selected Source"),
    ("declaration_path", str(DECLARATION_SURFACE_RELATIVE_PATH)),
    ("declaration_digest", DECLARATION_SHA256),
    ("candidate_lineage", str(CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH)),
    ("attestation_lineage", str(RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH)),
    ("receipt_lineage", str(RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH)),
    ("atomic_basis", "## 7. Atomic Operation Basis"),
    ("operation_question", "## 8. Operation Question and Matter Limit"),
    ("evaluation_family", "## 9. Condition Evaluation Family and Support Standard"),
    ("supported_value", TARGET_EVALUATION_SUPPORTED),
    ("outcome_family", "## 10. Outcome, Result, and Precedence"),
    ("outcome_supported", OUTCOME_SUPPORTED),
    ("outcome_requires_basis", OUTCOME_REQUIRES_BASIS),
    ("outcome_indeterminate", OUTCOME_INDETERMINATE),
    ("outcome_blocked", OUTCOME_BLOCKED),
    ("branch_posture", "## 11. Branch Posture"),
    ("completed_branches", "## 12. Completed Result Branches"),
    ("excluded_conditions", "## 13. Excluded Conditions"),
    ("prior_presence", "## 14. Prior Presence Re-Evaluation Standing"),
    ("lineage", "## 15. Source-Origin, Jurisdiction, and Lineage Preservation"),
    ("request", "## 16. Canonical Request"),
    ("read_omission", "## 17. Read and Omission Posture"),
    ("blocked_conversions", "## 18. Blocked Conversions"),
    ("non_claims", "## 19. Preserved Non-Claims"),
    ("future_route", "## 20. Exhaustion and Future Route"),
    ("null_route", "admissible_future_route = null"),
    ("open", "## 21. What Remains Open"),
    ("closing_lock", "## 22. Closing Lock"),
    ("open_not_next", "Open does not mean next."),
)
SPEC_MARKERS = tuple(marker for _, marker in SPEC_REQUIRED_MARKERS)

PROHIBITED_DIRECT_REQUEST_FIELDS = frozenset(
    {
        "outcome",
        "operation_result",
        "receiver_originating_modal_fact_evaluation_operation_result",
        "receiver_answerable_basis_refusable",
        "receiver_answerable_basis_could_have_been_withheld",
        "receiver_answerable_basis_refusable_supported",
        "receiver_answerable_basis_could_have_been_withheld_supported",
        "receiver_answerable_basis_refusable_established",
        "receiver_answerable_basis_could_have_been_withheld_established",
        "missing_or_insufficient_modal_fact_basis",
        "indeterminate_modal_fact_conditions",
        "excluded_condition_posture",
        "declaration_body",
        "declaration_content",
        "semantic_payload",
        "truth",
        "authority",
        "standing",
        "presence",
        "downstream_result",
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "REQUEST_BOOLEAN_REQUIRED",
        "REQUEST_MATTER_MISMATCH",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "REQUEST_PATH_INVALID",
        "REQUEST_PATH_MISSING",
        "REQUEST_PATH_UNREADABLE",
        "REQUEST_PATH_DUPLICATE_KEYED",
        "REQUEST_PATH_NOT_PARSEABLE",
        "REQUEST_PATH_NOT_MAPPING",
        "SPECIFICATION_REFERENCE_MISSING",
        "SPECIFICATION_UTF8_INVALID",
        "SPECIFICATION_MARKER_MISSING",
        "BOUNDARY_ARTIFACT_MISSING",
        "BOUNDARY_ARTIFACT_UNREADABLE",
        "BOUNDARY_ARTIFACT_DIGEST_MISMATCH",
        "BOUNDARY_ARTIFACT_DUPLICATE_KEYED",
        "BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        "BOUNDARY_ARTIFACT_NOT_MAPPING",
        "BOUNDARY_ARTIFACT_SECTION_MISSING",
        "BOUNDARY_METADATA_MISMATCH",
        "BOUNDARY_FAILED_CHECKS_PRESENT",
        "BOUNDARY_BLOCKED",
        "BOUNDARY_IDENTITY_MISMATCH",
        "BOUNDARY_RESULT_MISMATCH",
        "BOUNDARY_POSTURE_MISMATCH",
        "BOUNDARY_CARDINALITY_MISMATCH",
        "BOUNDARY_SOURCE_IDENTITY_MISMATCH",
        "BOUNDARY_FALSE_LOCK_MISMATCH",
        "DECLARATION_SURFACE_MISSING",
        "DECLARATION_SURFACE_UNREADABLE",
        "DECLARATION_BYTE_COUNT_MISMATCH",
        "DECLARATION_DIGEST_MISMATCH",
        "DECLARATION_BOM_PRESENT",
        "DECLARATION_UTF8_INVALID",
        "DECLARATION_RECORD_MALFORMED",
        "DECLARATION_RECORD_DUPLICATE",
        "DECLARATION_RECORD_SET_MISMATCH",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_MISSING",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_UNREADABLE",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_DUPLICATE_KEYED",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_NOT_PARSEABLE",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_NOT_MAPPING",
        "CANDIDATE_SUFFICIENCY_ARTIFACT_SECTION_MISSING",
        "CANDIDATE_SUFFICIENCY_METADATA_MISMATCH",
        "CANDIDATE_SUFFICIENCY_FAILED_CHECKS_PRESENT",
        "CANDIDATE_SUFFICIENCY_BLOCKED",
        "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH",
        "CANDIDATE_SUFFICIENCY_RESULT_MISMATCH",
        "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH",
        "CANDIDATE_SUFFICIENCY_CARDINALITY_MISMATCH",
        "RECEIVER_ATTESTATION_ARTIFACT_MISSING",
        "RECEIVER_ATTESTATION_ARTIFACT_UNREADABLE",
        "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH",
        "RECEIVER_ATTESTATION_ARTIFACT_DUPLICATE_KEYED",
        "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
        "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
        "RECEIVER_ATTESTATION_ARTIFACT_SECTION_MISSING",
        "RECEIVER_ATTESTATION_METADATA_MISMATCH",
        "RECEIVER_ATTESTATION_FAILED_CHECKS_PRESENT",
        "RECEIVER_ATTESTATION_BLOCKED",
        "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        "RECEIVER_ATTESTATION_RESULT_MISMATCH",
        "RECEIVER_ATTESTATION_POSTURE_MISMATCH",
        "RECEIVER_ATTESTATION_CARDINALITY_MISMATCH",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_MISSING",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_UNREADABLE",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DUPLICATE_KEYED",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_NOT_PARSEABLE",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_NOT_MAPPING",
        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_SECTION_MISSING",
        "RECEIVER_ANSWERABLE_RECEIPT_METADATA_MISMATCH",
        "RECEIVER_ANSWERABLE_RECEIPT_FAILED_CHECKS_PRESENT",
        "RECEIVER_ANSWERABLE_RECEIPT_BLOCKED",
        "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH",
        "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH",
        "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH",
        "RECEIVER_ANSWERABLE_RECEIPT_CARDINALITY_MISMATCH",
        "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "ATOMIC_BASIS_NOT_ADMITTED",
        "TARGET_EVALUATION_INVALID",
        "WRITE_REFUSED",
    }
)


class ReceiverOriginatingModalFactEvaluationOperationV0MinError(Exception):
    """Raised only when a canonical result cannot be summarized or written."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when strict JSON repeats an object member."""


class _NonFiniteJsonNumberError(ValueError):
    """Raised when JSON uses NaN or infinity extensions."""


_MISSING = object()


def _reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _reject_non_finite_json_number(value: str) -> Any:
    raise _NonFiniteJsonNumberError(value)


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_bytes(value: Path | str) -> tuple[bytes | None, str | None]:
    try:
        path = _as_repo_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_bytes(), None
    except (OSError, TypeError, ValueError):
        return None, "unreadable"


def _parse_json_bytes(payload: bytes) -> tuple[Any | None, str | None]:
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return None, "invalid_utf8"
    try:
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_json_keys,
            parse_constant=_reject_non_finite_json_number,
        )
    except _DuplicateJsonKeyError:
        return None, "duplicate_key"
    except (
        _NonFiniteJsonNumberError,
        TypeError,
        ValueError,
        json.JSONDecodeError,
    ):
        return None, "not_parseable"
    return value, None


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    payload, error = _read_bytes(value)
    if error is not None or payload is None:
        return None, error
    return _parse_json_bytes(payload)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _exact(value: Any, expected: Any) -> bool:
    if type(expected) is bool:
        return type(value) is bool and value is expected
    if type(expected) is int:
        return type(value) is int and value == expected
    return value == expected


def _canonical_false_mapping(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and bool(value)
        and all(type(item) is bool and item is False for item in value.values())
    )


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _canonical_lineage_posture(completed: bool) -> dict[str, bool]:
    return {field: completed for field in LINEAGE_PRESERVATION_FIELDS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {
        **{field: True for field in OMISSION_POSTURE_FIELDS},
        "complete_material_omission_posture": True,
    }


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _canonical_excluded_condition_posture() -> dict[str, Any]:
    return {
        "excluded_condition_evaluation_performed": False,
        "excluded_conditions_not_evaluated": True,
        "condition_evaluations": {
            field: TARGET_EVALUATION_NOT_EVALUATED
            for field in EXCLUDED_CONDITIONS
        },
    }


def _identity_request_values() -> dict[str, Any]:
    return {
        "intent": INTENT_RECORD,
        "receiver_originating_modal_fact_evaluation_operation_id": OPERATION_ID,
        "receiver_originating_modal_fact_evaluation_operation_type": OPERATION_TYPE,
        "receiver_originating_modal_fact_evaluation_operation_version": OPERATION_VERSION,
        "receiver_originating_modal_fact_evaluation_operation_scope": OPERATION_SCOPE,
        (
            "governing_receiver_originating_modal_fact_evaluation_"
            "operation_specification_path"
        ): str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        (
            "receiver_originating_modal_fact_source_admissibility_"
            "boundary_artifact_path"
        ): str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
        "selected_receiver_originating_declaration_surface_path": str(
            DECLARATION_SURFACE_RELATIVE_PATH
        ),
        "selected_candidate_sufficiency_operation_artifact_path": str(
            CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
        ),
        "selected_receiver_attestation_operation_artifact_path": str(
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
        ),
        "selected_receiver_answerable_receipt_operation_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
        ),
        "selected_receiver_originating_declaration_archive_path": str(
            DECLARATION_ARCHIVE_RELATIVE_PATH
        ),
        "selected_receiver_originating_declaration_archive_member": (
            DECLARATION_ARCHIVE_MEMBER
        ),
        "selected_receiver_originating_declaration_byte_count": (
            DECLARATION_BYTE_COUNT
        ),
        "selected_receiver_originating_declaration_sha256": DECLARATION_SHA256,
        "selected_receiver_originating_declaration_archive_sha256": (
            DECLARATION_ARCHIVE_SHA256
        ),
        "selected_receiver_originating_declaration_candidate_id": (
            DECLARATION_CANDIDATE_ID
        ),
        (
            "selected_receiver_originating_declaration_"
            "source_provenance_reference"
        ): DECLARATION_PROVENANCE_REFERENCE,
        "selected_receiver_originating_declaration_receipt_bundle": (
            DECLARATION_RECEIPT_BUNDLE
        ),
        "selected_receiver_originating_declaration_receiver_label": (
            DECLARATION_RECEIVER_LABEL
        ),
        "selected_source_class": SELECTED_SOURCE_CLASS,
        "selected_relation_class": SELECTED_RELATION_CLASS,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "selected_matter": list(TARGET_CONDITIONS),
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_provenance_posture": SELECTED_SOURCE_PROVENANCE_POSTURE,
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "receiver_originating_modal_fact_evaluation_execution_selected": True,
    }


def _new_canonical_request() -> dict[str, Any]:
    return {
        **_identity_request_values(),
        "declared_non_claims": _canonical_non_claims(),
    }


def build_receiver_originating_modal_fact_evaluation_operation_v0_min_request(
) -> dict[str, Any]:
    """Return one fresh canonical operation request."""
    return copy.deepcopy(_new_canonical_request())


def build_declared_receiver_originating_modal_fact_evaluation_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return a canonical request while keeping every override visible."""
    request = _new_canonical_request()
    request.update(copy.deepcopy(overrides))
    return request


def _canonical_request_keys() -> set[str]:
    return {*_identity_request_values(), "declared_non_claims"}


def _operation_basis_supplied(request: Any) -> bool:
    if not isinstance(request, Mapping):
        return False
    fields = (
        "governing_receiver_originating_modal_fact_evaluation_operation_specification_path",
        "receiver_originating_modal_fact_source_admissibility_boundary_artifact_path",
        "selected_receiver_originating_declaration_surface_path",
        "selected_candidate_sufficiency_operation_artifact_path",
        "selected_receiver_attestation_operation_artifact_path",
        "selected_receiver_answerable_receipt_operation_artifact_path",
    )
    return all(
        isinstance(request.get(field), str) and bool(request.get(field))
        for field in fields
    )


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
    *,
    expected: Any = _MISSING,
) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "passed": passed}
    if expected is not _MISSING:
        item["expected"] = copy.deepcopy(expected)
    if not passed and code is not None:
        item["failure_code"] = code
        item["block_code"] = code
    return item


def _require(
    checks: list[dict[str, Any]],
    name: str,
    condition: bool,
    code: str,
    reason: str,
    *,
    expected: Any = _MISSING,
) -> tuple[str | None, str | None]:
    checks.append(_check(name, condition, code, expected=expected))
    return (None, None) if condition else (code, reason)


def _expect_many(
    checks: list[dict[str, Any]],
    prefix: str,
    expectations: Sequence[tuple[str, Any, Any, str]],
) -> tuple[str | None, str | None]:
    for name, actual, expected, code in expectations:
        failure, reason = _require(
            checks,
            prefix + "." + name,
            _exact(actual, expected),
            code,
            prefix.replace("_", "-") + " standing mismatch: " + name,
            expected=expected,
        )
        if failure is not None:
            return failure, reason
    return None, None


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    direct = set(request).intersection(PROHIBITED_DIRECT_REQUEST_FIELDS)
    if direct:
        return _require(
            checks,
            "request.result_or_semantic_preclaim",
            False,
            "RESULT_POSTURE_PRECLAIMED",
            "request contains a result, semantic payload, or downstream preclaim",
        )

    canonical_keys = _canonical_request_keys()
    if canonical_keys.difference(request):
        return _require(
            checks,
            "request.schema",
            False,
            "REQUEST_FIELD_MISSING",
            "canonical request fields are missing",
        )
    if set(request).difference(canonical_keys):
        return _require(
            checks,
            "request.schema",
            False,
            "REQUEST_UNKNOWN_FIELD",
            "request contains unknown fields",
        )
    checks.append(_check("request.schema", True, expected="exact canonical keys"))

    for field, expected in _identity_request_values().items():
        actual = request.get(field)
        if field == "selected_matter":
            valid = (
                isinstance(actual, Sequence)
                and not isinstance(actual, (str, bytes, bytearray))
                and list(actual) == list(TARGET_CONDITIONS)
                and len(actual) == len(TARGET_CONDITIONS)
            )
            code = "REQUEST_MATTER_MISMATCH"
        elif type(expected) is bool:
            valid = type(actual) is bool and actual is expected
            code = "REQUEST_BOOLEAN_REQUIRED" if type(actual) is not bool else "REQUEST_VALUE_MISMATCH"
        elif type(expected) is int:
            valid = type(actual) is int and actual == expected
            code = "REQUEST_VALUE_MISMATCH"
        else:
            valid = actual == expected
            code = "REQUEST_VALUE_MISMATCH"
        failure, reason = _require(
            checks,
            "request." + field,
            valid,
            code,
            field + " does not match the canonical request",
            expected=expected,
        )
        if failure is not None:
            return failure, reason

    if not _non_claims_valid(request.get("declared_non_claims")):
        return _require(
            checks,
            "request.declared_non_claims",
            False,
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims must be the exact canonical false set",
        )
    checks.append(_check("request.declared_non_claims", True, expected=False))
    return None, None


def _empty_specification_validation() -> dict[str, Any]:
    return {
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "marker_validation": {name: False for name, _ in SPEC_REQUIRED_MARKERS},
        "specification_validated": False,
    }


def _validate_specification(
    checks: list[dict[str, Any]],
    read_path: Path | str,
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_specification_validation()
    payload, error = _read_bytes(read_path)
    if error is not None or payload is None:
        code = "SPECIFICATION_REFERENCE_MISSING"
        _require(
            checks,
            "specification.reference",
            False,
            code,
            "governing operation specification is unavailable",
        )
        return code, "governing operation specification is unavailable", validation
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        code = "SPECIFICATION_UTF8_INVALID"
        _require(
            checks,
            "specification.utf8",
            False,
            code,
            "governing operation specification is not strict UTF-8",
        )
        return code, "governing operation specification is not strict UTF-8", validation
    checks.append(_check("specification.reference", True))
    for name, marker in SPEC_REQUIRED_MARKERS:
        valid = marker in text
        validation["marker_validation"][name] = valid
        code, reason = _require(
            checks,
            "specification." + name,
            valid,
            "SPECIFICATION_MARKER_MISSING",
            "governing specification marker is missing: " + name,
            expected=marker,
        )
        if code is not None:
            return code, reason, validation
    validation["specification_validated"] = True
    return None, None, validation


def _empty_json_artifact_validation(
    path: Path,
    expected_sha256: str,
) -> dict[str, Any]:
    return {
        "artifact_path": str(path),
        "expected_sha256": expected_sha256,
        "observed_sha256": None,
        "strict_json_validated": False,
        "artifact_validated": False,
        "identity_validated": False,
        "result_validated": False,
        "completion_and_cardinality_validated": False,
        "false_locks_validated": False,
        "standing": {},
    }


def _load_exact_json_artifact(
    *,
    read_path: Path | str,
    canonical_path: Path,
    expected_sha256: str,
    prefix: str,
    code_prefix: str,
    checks: list[dict[str, Any]],
    validation: dict[str, Any],
) -> tuple[str | None, str | None, Mapping[str, Any] | None]:
    payload, error = _read_bytes(read_path)
    if error == "not_a_file":
        code = code_prefix + "_ARTIFACT_MISSING"
        _require(
            checks,
            prefix + ".reference",
            False,
            code,
            prefix + " artifact is unavailable",
        )
        return code, prefix + " artifact is unavailable", None
    if error is not None or payload is None:
        code = code_prefix + "_ARTIFACT_UNREADABLE"
        _require(
            checks,
            prefix + ".reference",
            False,
            code,
            prefix + " artifact is unreadable",
        )
        return code, prefix + " artifact is unreadable", None

    validation["artifact_path"] = str(canonical_path)
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    code, reason = _require(
        checks,
        prefix + ".sha256",
        observed == expected_sha256,
        code_prefix + "_ARTIFACT_DIGEST_MISMATCH",
        prefix + " artifact digest does not match exact standing",
        expected=expected_sha256,
    )
    if code is not None:
        return code, reason, None

    artifact, parse_error = _parse_json_bytes(payload)
    if parse_error == "duplicate_key":
        code = code_prefix + "_ARTIFACT_DUPLICATE_KEYED"
        _require(
            checks,
            prefix + ".strict_json",
            False,
            code,
            prefix + " artifact contains duplicate JSON keys",
        )
        return code, prefix + " artifact contains duplicate JSON keys", None
    if parse_error is not None:
        code = code_prefix + "_ARTIFACT_NOT_PARSEABLE"
        _require(
            checks,
            prefix + ".strict_json",
            False,
            code,
            prefix + " artifact is not strict UTF-8 JSON",
        )
        return code, prefix + " artifact is not strict UTF-8 JSON", None
    if not isinstance(artifact, Mapping):
        code = code_prefix + "_ARTIFACT_NOT_MAPPING"
        _require(
            checks,
            prefix + ".mapping",
            False,
            code,
            prefix + " artifact is not a mapping",
        )
        return code, prefix + " artifact is not a mapping", None
    validation["strict_json_validated"] = True
    checks.append(_check(prefix + ".strict_json_mapping", True))
    return None, None, artifact


BOUNDARY_FALSE_LOCKS = (
    "receiver_answerable_basis_refusable_established",
    "receiver_answerable_basis_could_have_been_withheld_established",
    "receiver_actual_refusal_established",
    "receiver_actual_withholding_established",
    "receiver_freedom_established",
    "receiver_originating_declaration_truth_created",
    "receiver_originating_declaration_authority_created",
    "receiver_originating_declaration_native_standing_created",
    "source_authority_created",
    "truth_created",
    "standing_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
)


def _empty_boundary_validation() -> dict[str, Any]:
    return _empty_json_artifact_validation(
        BOUNDARY_ARTIFACT_RELATIVE_PATH,
        BOUNDARY_SHA256,
    )


def _validate_boundary_artifact(
    checks: list[dict[str, Any]],
    read_path: Path | str,
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_boundary_validation()
    code, reason, artifact = _load_exact_json_artifact(
        read_path=read_path,
        canonical_path=BOUNDARY_ARTIFACT_RELATIVE_PATH,
        expected_sha256=BOUNDARY_SHA256,
        prefix="boundary",
        code_prefix="BOUNDARY",
        checks=checks,
        validation=validation,
    )
    if code is not None or artifact is None:
        return code, reason, validation

    boundary = artifact.get(
        "receiver_originating_modal_fact_source_admissibility_boundary"
    )
    summary = artifact.get(
        "receiver_originating_modal_fact_source_admissibility_boundary_summary"
    )
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    prior = artifact.get("prior_operation_artifact_validation")
    lineage = artifact.get("lineage_preservation_posture")
    source = artifact.get("source_selection_and_carriage_lineage")
    if not all(
        isinstance(value, Mapping)
        for value in (boundary, summary, block, non_claims, prior, lineage, source)
    ):
        code = "BOUNDARY_ARTIFACT_SECTION_MISSING"
        _require(
            checks,
            "boundary.sections",
            False,
            code,
            "boundary artifact lacks required compact sections",
        )
        return code, "boundary artifact lacks required compact sections", validation
    checks.append(_check("boundary.sections", True))

    expectations: list[tuple[str, Any, Any, str]] = [
        ("resolver_module", artifact.get("resolver_module"), BOUNDARY_RESOLVER_MODULE, "BOUNDARY_METADATA_MISMATCH"),
        ("result_version", artifact.get("result_version"), RESULT_VERSION, "BOUNDARY_METADATA_MISMATCH"),
        ("outcome", artifact.get("outcome"), BOUNDARY_OUTCOME_REQUIRED, "BOUNDARY_RESULT_MISMATCH"),
        ("boundary_result", artifact.get("boundary_result"), BOUNDARY_RESULT_REQUIRED, "BOUNDARY_RESULT_MISMATCH"),
        ("failed_check_count", artifact.get("failed_check_count"), 0, "BOUNDARY_FAILED_CHECKS_PRESENT"),
        ("passed_check_count", artifact.get("passed_check_count"), BOUNDARY_PASSED_CHECK_COUNT, "BOUNDARY_METADATA_MISMATCH"),
        ("blocked", block.get("blocked"), False, "BOUNDARY_BLOCKED"),
        ("selection", summary.get("selection"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("boundary_id", boundary.get("boundary_id"), BOUNDARY_ID, "BOUNDARY_IDENTITY_MISMATCH"),
        ("boundary_type", boundary.get("boundary_type"), BOUNDARY_TYPE, "BOUNDARY_IDENTITY_MISMATCH"),
        ("boundary_version", boundary.get("boundary_version"), RESULT_VERSION, "BOUNDARY_IDENTITY_MISMATCH"),
        ("boundary_scope", boundary.get("boundary_scope"), BOUNDARY_SCOPE, "BOUNDARY_IDENTITY_MISMATCH"),
        ("source_admissibility_evaluation", boundary.get("source_admissibility_evaluation"), "PASSED", "BOUNDARY_POSTURE_MISMATCH"),
        ("scope_and_matter_admissibility_evaluation", boundary.get("scope_and_matter_admissibility_evaluation"), "PASSED", "BOUNDARY_POSTURE_MISMATCH"),
        ("transition_admissibility_evaluation", boundary.get("transition_admissibility_evaluation"), "PASSED", "BOUNDARY_POSTURE_MISMATCH"),
        ("boundary_recorded", boundary.get("receiver_originating_modal_fact_source_admissibility_boundary_recorded"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("boundary_result_recorded", boundary.get("receiver_originating_modal_fact_source_admissibility_boundary_result_recorded"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("boundary_exhausted", boundary.get("receiver_originating_modal_fact_source_admissibility_boundary_exhausted"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("consideration_allowed", boundary.get("receiver_originating_modal_fact_evaluation_consideration_allowed"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("consideration_not_allowed", boundary.get("receiver_originating_modal_fact_evaluation_consideration_not_allowed"), False, "BOUNDARY_POSTURE_MISMATCH"),
        ("source_selection_recorded", boundary.get("source_selection_recorded"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("completed_count", boundary.get("completed_consideration_posture_count"), 1, "BOUNDARY_CARDINALITY_MISMATCH"),
        ("source_class", boundary.get("selected_source_class"), SELECTED_SOURCE_CLASS, "BOUNDARY_IDENTITY_MISMATCH"),
        ("relation_class", boundary.get("selected_relation_class"), SELECTED_RELATION_CLASS, "BOUNDARY_IDENTITY_MISMATCH"),
        ("matter_class", boundary.get("selected_matter_class"), SELECTED_MATTER_CLASS, "BOUNDARY_IDENTITY_MISMATCH"),
        ("source_origin", boundary.get("selected_source_origin"), SELECTED_SOURCE_ORIGIN, "BOUNDARY_IDENTITY_MISMATCH"),
        ("provenance_posture", boundary.get("selected_source_provenance_posture"), SELECTED_SOURCE_PROVENANCE_POSTURE, "BOUNDARY_IDENTITY_MISMATCH"),
        ("arrival_posture", boundary.get("selected_source_arrival_posture"), SELECTED_SOURCE_ARRIVAL_POSTURE, "BOUNDARY_IDENTITY_MISMATCH"),
        ("native_standing", boundary.get("selected_source_native_standing"), False, "BOUNDARY_POSTURE_MISMATCH"),
        ("receiver_origin_preserved", summary.get("receiver_origin_preserved"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("source_relation_preserved", summary.get("source_relation_preserved"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("jurisdiction", boundary.get("jurisdiction_distinction_preserved"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("jurisdiction_preserved", summary.get("jurisdiction_preserved"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("source_not_naturalized", summary.get("source_not_naturalized"), True, "BOUNDARY_POSTURE_MISMATCH"),
        ("future_route", boundary.get("admissible_future_route"), BOUNDARY_FUTURE_ROUTE_REQUIRED, "BOUNDARY_POSTURE_MISMATCH"),
    ]
    code, reason = _expect_many(checks, "boundary", expectations)
    if code is not None:
        return code, reason, validation

    selected_matter = boundary.get("selected_matter")
    code, reason = _require(
        checks,
        "boundary.selected_matter",
        isinstance(selected_matter, list)
        and selected_matter == list(TARGET_CONDITIONS),
        "BOUNDARY_IDENTITY_MISMATCH",
        "boundary selected matter is not the exact ordered pair",
        expected=list(TARGET_CONDITIONS),
    )
    if code is not None:
        return code, reason, validation

    declaration_identity = boundary.get("selected_receiver_originating_declaration")
    expected_identity = {
        "archive_path": str(DECLARATION_ARCHIVE_RELATIVE_PATH),
        "archive_member": DECLARATION_ARCHIVE_MEMBER,
        "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
        "byte_count": DECLARATION_BYTE_COUNT,
        "declaration_sha256": DECLARATION_SHA256,
        "archive_sha256": DECLARATION_ARCHIVE_SHA256,
        "candidate_id": DECLARATION_CANDIDATE_ID,
        "source_provenance_reference": DECLARATION_PROVENANCE_REFERENCE,
        "receipt_bundle": DECLARATION_RECEIPT_BUNDLE,
        "receiver_label": DECLARATION_RECEIVER_LABEL,
    }
    code, reason = _require(
        checks,
        "boundary.source_identity",
        isinstance(declaration_identity, Mapping)
        and dict(declaration_identity) == expected_identity,
        "BOUNDARY_SOURCE_IDENTITY_MISMATCH",
        "boundary source identity does not match exact declaration",
        expected="exact compact declaration identity",
    )
    if code is not None:
        return code, reason, validation

    matter_records = boundary.get("matter_relevant_declaration_records")
    code, reason = _require(
        checks,
        "boundary.matter_relevant_records",
        isinstance(matter_records, Mapping)
        and dict(matter_records)
        == {
            "could_have_been_refused": True,
            "could_have_been_withheld": True,
        },
        "BOUNDARY_SOURCE_IDENTITY_MISMATCH",
        "boundary matter-relevant records do not match exact source",
        expected="exact two matter-relevant records",
    )
    if code is not None:
        return code, reason, validation

    for field in BOUNDARY_FALSE_LOCKS:
        code, reason = _require(
            checks,
            "boundary.false_lock." + field,
            boundary.get(field) is False and non_claims.get(field) is False,
            "BOUNDARY_FALSE_LOCK_MISMATCH",
            "boundary false lock is not canonical false: " + field,
            expected=False,
        )
        if code is not None:
            return code, reason, validation
    if not _canonical_false_mapping(non_claims):
        code = "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE"
        _require(
            checks,
            "boundary.non_claims",
            False,
            code,
            "boundary non-claims are not canonical false",
        )
        return code, "boundary non-claims are not canonical false", validation
    checks.append(_check("boundary.non_claims", True, expected=False))

    prior_standing = prior.get("standing")
    prior_valid = (
        prior.get("artifact_validated") is True
        and prior.get("completion_and_cardinality_validated") is True
        and prior.get("false_locks_validated") is True
        and isinstance(prior_standing, Mapping)
        and prior_standing.get("outcome") == PRIOR_PRESENCE_OUTCOME
        and prior_standing.get("operation_result") == PRIOR_PRESENCE_RESULT
        and prior_standing.get("presence_re_evaluation_operation_exhausted") is True
        and prior_standing.get("admissible_future_route") is None
        and prior_standing.get("receiver_attested") == "SATISFIED"
        and prior_standing.get("receiver_answerable_receipt_present") == "SATISFIED"
        and prior_standing.get("receiver_answerable_basis_refusable") == "REQUIRES_BASIS"
        and prior_standing.get("receiver_answerable_basis_could_have_been_withheld")
        == "REQUIRES_BASIS"
        and all(
            prior_standing.get(field) is False
            for field in (
                "presence_supported",
                "presence_authorized",
                "presence_established",
                "presence_recorded",
            )
        )
    )
    code, reason = _require(
        checks,
        "boundary.prior_presence_standing",
        prior_valid,
        "BOUNDARY_POSTURE_MISMATCH",
        "boundary does not preserve the exact compact prior presence standing",
        expected=PRIOR_PRESENCE_RESULT,
    )
    if code is not None:
        return code, reason, validation

    required_true_groups = (
        (lineage, BOUNDARY_LINEAGE_PRESERVATION_FIELDS),
        (
            source,
            (
                "source_selection_recorded",
                "exact_source_identity_validated",
                "source_class_validated",
                "receiver_origin_validated",
                "declared_provenance_posture_validated",
                "candidate_correspondence_validated",
                "candidate_sufficiency_lineage_validated",
                "receiver_attestation_lineage_validated",
                "receiver_answerable_receipt_lineage_validated",
                "prior_requires_basis_lineage_validated",
                "carriage_lineage_validated",
            ),
        ),
    )
    for mapping, fields in required_true_groups:
        for field in fields:
            code, reason = _require(
                checks,
                "boundary.lineage." + field,
                mapping.get(field) is True,
                "BOUNDARY_POSTURE_MISMATCH",
                "boundary lineage field is not exact true: " + field,
                expected=True,
            )
            if code is not None:
                return code, reason, validation

    validation.update(
        {
            "artifact_validated": True,
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "standing": {
                "boundary_id": BOUNDARY_ID,
                "outcome": BOUNDARY_OUTCOME_REQUIRED,
                "boundary_result": BOUNDARY_RESULT_REQUIRED,
                "failed_check_count": 0,
                "passed_check_count": BOUNDARY_PASSED_CHECK_COUNT,
                "boundary_exhausted": True,
                "completed_consideration_posture_count": 1,
                "selected_source_class": SELECTED_SOURCE_CLASS,
                "selected_relation_class": SELECTED_RELATION_CLASS,
                "selected_matter_class": SELECTED_MATTER_CLASS,
                "selected_source_origin": SELECTED_SOURCE_ORIGIN,
                "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
                "selected_source_native_standing": False,
                "jurisdiction_distinction_preserved": True,
                "source_not_naturalized": True,
                "prior_presence_outcome": PRIOR_PRESENCE_OUTCOME,
                "prior_presence_result": PRIOR_PRESENCE_RESULT,
                "admissible_future_route": BOUNDARY_FUTURE_ROUTE_REQUIRED,
            },
        }
    )
    return None, None, validation


def _empty_declaration_validation() -> dict[str, Any]:
    return {
        "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
        "declaration_archive_path": str(DECLARATION_ARCHIVE_RELATIVE_PATH),
        "declaration_archive_member": DECLARATION_ARCHIVE_MEMBER,
        "expected_byte_count": DECLARATION_BYTE_COUNT,
        "observed_byte_count": None,
        "expected_sha256": DECLARATION_SHA256,
        "observed_sha256": None,
        "archive_sha256_identity": DECLARATION_ARCHIVE_SHA256,
        "candidate_id": DECLARATION_CANDIDATE_ID,
        "source_provenance_reference": DECLARATION_PROVENANCE_REFERENCE,
        "receipt_bundle": DECLARATION_RECEIPT_BUNDLE,
        "receiver_label": DECLARATION_RECEIVER_LABEL,
        "strict_utf8_validated": False,
        "bom_absent": False,
        "exact_six_unique_records_validated": False,
        "source_context_records_validated": False,
        "matter_relevant_records": {},
        "complete_declaration_body_omitted": True,
        "declaration_validated": False,
    }


def _validate_declaration_surface(
    checks: list[dict[str, Any]],
    read_path: Path | str,
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_declaration_validation()
    payload, error = _read_bytes(read_path)
    if error == "not_a_file":
        code = "DECLARATION_SURFACE_MISSING"
        _require(
            checks,
            "declaration.reference",
            False,
            code,
            "exact declaration surface is unavailable",
        )
        return code, "exact declaration surface is unavailable", validation
    if error is not None or payload is None:
        code = "DECLARATION_SURFACE_UNREADABLE"
        _require(
            checks,
            "declaration.reference",
            False,
            code,
            "exact declaration surface is unreadable",
        )
        return code, "exact declaration surface is unreadable", validation

    validation["observed_byte_count"] = len(payload)
    code, reason = _require(
        checks,
        "declaration.byte_count",
        len(payload) == DECLARATION_BYTE_COUNT,
        "DECLARATION_BYTE_COUNT_MISMATCH",
        "declaration byte count does not match exact identity",
        expected=DECLARATION_BYTE_COUNT,
    )
    if code is not None:
        return code, reason, validation

    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    code, reason = _require(
        checks,
        "declaration.sha256",
        observed == DECLARATION_SHA256,
        "DECLARATION_DIGEST_MISMATCH",
        "declaration digest does not match exact identity",
        expected=DECLARATION_SHA256,
    )
    if code is not None:
        return code, reason, validation

    bom_absent = not payload.startswith(b"\xef\xbb\xbf")
    validation["bom_absent"] = bom_absent
    code, reason = _require(
        checks,
        "declaration.bom_absent",
        bom_absent,
        "DECLARATION_BOM_PRESENT",
        "declaration surface contains an unpermitted UTF-8 BOM",
        expected=True,
    )
    if code is not None:
        return code, reason, validation

    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        code = "DECLARATION_UTF8_INVALID"
        _require(
            checks,
            "declaration.utf8",
            False,
            code,
            "declaration surface is not strict UTF-8",
        )
        return code, "declaration surface is not strict UTF-8", validation
    validation["strict_utf8_validated"] = True
    checks.append(_check("declaration.utf8", True))

    lines = text.splitlines()
    if len(lines) != len(REQUIRED_DECLARATION_RECORDS) or any(not line for line in lines):
        code = "DECLARATION_RECORD_SET_MISMATCH"
        _require(
            checks,
            "declaration.record_count",
            False,
            code,
            "declaration must contain exactly six non-empty records",
            expected=6,
        )
        return code, "declaration must contain exactly six non-empty records", validation

    records: dict[str, str] = {}
    for index, line in enumerate(lines):
        if line.count("=") != 1:
            code = "DECLARATION_RECORD_MALFORMED"
            _require(
                checks,
                "declaration.record." + str(index),
                False,
                code,
                "declaration record is not one key=value pair",
            )
            return code, "declaration record is not one key=value pair", validation
        key, value = line.split("=", 1)
        if not key or not value:
            code = "DECLARATION_RECORD_MALFORMED"
            _require(
                checks,
                "declaration.record." + str(index),
                False,
                code,
                "declaration record has an empty key or value",
            )
            return code, "declaration record has an empty key or value", validation
        if key in records:
            code = "DECLARATION_RECORD_DUPLICATE"
            _require(
                checks,
                "declaration.record." + key,
                False,
                code,
                "declaration surface contains a duplicate key",
            )
            return code, "declaration surface contains a duplicate key", validation
        records[key] = value

    code, reason = _require(
        checks,
        "declaration.record_set",
        records == REQUIRED_DECLARATION_RECORDS,
        "DECLARATION_RECORD_SET_MISMATCH",
        "declaration keys or values do not match exact standing",
        expected="exact six declaration records",
    )
    if code is not None:
        return code, reason, validation

    for key, expected in REQUIRED_DECLARATION_RECORDS.items():
        checks.append(
            _check("declaration.record." + key, records[key] == expected, expected=expected)
        )
    validation.update(
        {
            "exact_six_unique_records_validated": True,
            "source_context_records_validated": True,
            "matter_relevant_records": {
                "could_have_been_refused": True,
                "could_have_been_withheld": True,
            },
            "declaration_validated": True,
        }
    )
    return None, None, validation


def _empty_candidate_validation() -> dict[str, Any]:
    return _empty_json_artifact_validation(
        CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
        CANDIDATE_SUFFICIENCY_SHA256,
    )


def _validate_candidate_sufficiency_artifact(
    checks: list[dict[str, Any]],
    read_path: Path | str,
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_candidate_validation()
    code, reason, artifact = _load_exact_json_artifact(
        read_path=read_path,
        canonical_path=CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
        expected_sha256=CANDIDATE_SUFFICIENCY_SHA256,
        prefix="candidate_sufficiency",
        code_prefix="CANDIDATE_SUFFICIENCY",
        checks=checks,
        validation=validation,
    )
    if code is not None or artifact is None:
        return code, reason, validation
    operation = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_summary"
    )
    detail = artifact.get("operation_result_detail")
    dimensions = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
    )
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, detail, dimensions, block, non_claims)
    ):
        code = "CANDIDATE_SUFFICIENCY_ARTIFACT_SECTION_MISSING"
        _require(
            checks,
            "candidate_sufficiency.sections",
            False,
            code,
            "candidate-sufficiency artifact lacks compact sections",
        )
        return code, "candidate-sufficiency artifact lacks compact sections", validation
    checks.append(_check("candidate_sufficiency.sections", True))

    expectations = [
        ("resolver_module", artifact.get("resolver_module"), CANDIDATE_SUFFICIENCY_RESOLVER_MODULE, "CANDIDATE_SUFFICIENCY_METADATA_MISMATCH"),
        ("result_version", artifact.get("result_version"), RESULT_VERSION, "CANDIDATE_SUFFICIENCY_METADATA_MISMATCH"),
        ("outcome", artifact.get("outcome"), CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED, "CANDIDATE_SUFFICIENCY_RESULT_MISMATCH"),
        ("failed_check_count", artifact.get("failed_check_count"), 0, "CANDIDATE_SUFFICIENCY_FAILED_CHECKS_PRESENT"),
        ("passed_check_count", artifact.get("passed_check_count"), CANDIDATE_SUFFICIENCY_PASSED_CHECK_COUNT, "CANDIDATE_SUFFICIENCY_METADATA_MISMATCH"),
        ("blocked", block.get("blocked"), False, "CANDIDATE_SUFFICIENCY_BLOCKED"),
        ("operation_id", operation.get("operation_id"), CANDIDATE_SUFFICIENCY_OPERATION_ID, "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH"),
        ("operation_type", operation.get("operation_type"), CANDIDATE_SUFFICIENCY_OPERATION_TYPE, "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH"),
        ("operation_version", operation.get("operation_version"), RESULT_VERSION, "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH"),
        ("operation_scope", operation.get("operation_scope"), CANDIDATE_SUFFICIENCY_OPERATION_SCOPE, "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH"),
        ("candidate_id", operation.get("receiver_side_answerable_basis_candidate_id"), DECLARATION_CANDIDATE_ID, "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH"),
        ("operation_result", operation.get("operation_result"), CANDIDATE_SUFFICIENCY_RESULT_REQUIRED, "CANDIDATE_SUFFICIENCY_RESULT_MISMATCH"),
        ("summary_result", summary.get("operation_result"), CANDIDATE_SUFFICIENCY_RESULT_REQUIRED, "CANDIDATE_SUFFICIENCY_RESULT_MISMATCH"),
        ("detail_result", detail.get("operation_result"), CANDIDATE_SUFFICIENCY_RESULT_REQUIRED, "CANDIDATE_SUFFICIENCY_RESULT_MISMATCH"),
        ("basis_supplied", operation.get("sufficiency_basis_supplied"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("basis_complete", operation.get("sufficiency_basis_complete"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("atomic_gate", operation.get("atomic_sufficiency_basis_gate_passed"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("candidate_sufficient", operation.get("receiver_side_answerable_basis_candidate_sufficient"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("operation_recorded", operation.get("candidate_sufficiency_operation_recorded"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("result_recorded", operation.get("candidate_sufficiency_operation_result_recorded"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("operation_exhausted", operation.get("candidate_sufficiency_operation_exhausted"), True, "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH"),
        ("candidate_count", detail.get("candidate_result_posture_count"), 1, "CANDIDATE_SUFFICIENCY_CARDINALITY_MISMATCH"),
        ("dimension_count", detail.get("evaluated_dimension_count"), 8, "CANDIDATE_SUFFICIENCY_CARDINALITY_MISMATCH"),
    ]
    code, reason = _expect_many(checks, "candidate_sufficiency", expectations)
    if code is not None:
        return code, reason, validation

    code, reason = _require(
        checks,
        "candidate_sufficiency.dimensions",
        set(dimensions) == set(REQUIRED_SUFFICIENCY_DIMENSIONS)
        and len(dimensions) == 8,
        "CANDIDATE_SUFFICIENCY_CARDINALITY_MISMATCH",
        "candidate-sufficiency dimension family is not exact",
        expected=list(REQUIRED_SUFFICIENCY_DIMENSIONS),
    )
    if code is not None:
        return code, reason, validation
    for dimension in REQUIRED_SUFFICIENCY_DIMENSIONS:
        item = dimensions.get(dimension)
        valid = (
            isinstance(item, Mapping)
            and item.get("dimension_id") == dimension
            and item.get("dimension_result") == "SATISFIED"
            and item.get("dimension_evaluated") is True
            and item.get("dimension_established") is True
        )
        code, reason = _require(
            checks,
            "candidate_sufficiency.dimension." + dimension,
            valid,
            "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH",
            "candidate-sufficiency dimension mismatch: " + dimension,
            expected="SATISFIED",
        )
        if code is not None:
            return code, reason, validation

    if not _canonical_false_mapping(non_claims):
        code = "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE"
        _require(
            checks,
            "candidate_sufficiency.non_claims",
            False,
            code,
            "candidate-sufficiency non-claims are not canonical false",
        )
        return code, "candidate-sufficiency non-claims are not canonical false", validation
    checks.append(_check("candidate_sufficiency.non_claims", True, expected=False))

    validation.update(
        {
            "artifact_validated": True,
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "standing": {
                "operation_id": CANDIDATE_SUFFICIENCY_OPERATION_ID,
                "outcome": CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED,
                "operation_result": CANDIDATE_SUFFICIENCY_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "refusal_withholding_compatibility": "SATISFIED",
                "operation_basis_complete_and_admitted": True,
                "operation_exhausted": True,
                "candidate_result_posture_count": 1,
                "evaluated_dimension_count": 8,
            },
        }
    )
    return None, None, validation


def _empty_attestation_validation() -> dict[str, Any]:
    return _empty_json_artifact_validation(
        RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
        RECEIVER_ATTESTATION_SHA256,
    )


def _validate_receiver_attestation_artifact(
    checks: list[dict[str, Any]],
    read_path: Path | str,
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_attestation_validation()
    code, reason, artifact = _load_exact_json_artifact(
        read_path=read_path,
        canonical_path=RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
        expected_sha256=RECEIVER_ATTESTATION_SHA256,
        prefix="receiver_attestation",
        code_prefix="RECEIVER_ATTESTATION",
        checks=checks,
        validation=validation,
    )
    if code is not None or artifact is None:
        return code, reason, validation
    operation = artifact.get(
        "receiver_side_answerable_basis_receiver_attestation_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_receiver_attestation_operation_summary"
    )
    identity = artifact.get("selected_operation_and_candidate_identity")
    posture = artifact.get("operation_posture")
    detail = artifact.get("operation_result_detail")
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, identity, posture, detail, block, non_claims)
    ):
        code = "RECEIVER_ATTESTATION_ARTIFACT_SECTION_MISSING"
        _require(
            checks,
            "receiver_attestation.sections",
            False,
            code,
            "receiver-attestation artifact lacks compact sections",
        )
        return code, "receiver-attestation artifact lacks compact sections", validation
    checks.append(_check("receiver_attestation.sections", True))

    expectations = [
        ("resolver_module", artifact.get("resolver_module"), RECEIVER_ATTESTATION_RESOLVER_MODULE, "RECEIVER_ATTESTATION_METADATA_MISMATCH"),
        ("result_version", artifact.get("result_version"), RESULT_VERSION, "RECEIVER_ATTESTATION_METADATA_MISMATCH"),
        ("outcome", artifact.get("outcome"), RECEIVER_ATTESTATION_OUTCOME_REQUIRED, "RECEIVER_ATTESTATION_RESULT_MISMATCH"),
        ("failed_check_count", artifact.get("failed_check_count"), 0, "RECEIVER_ATTESTATION_FAILED_CHECKS_PRESENT"),
        ("passed_check_count", artifact.get("passed_check_count"), RECEIVER_ATTESTATION_PASSED_CHECK_COUNT, "RECEIVER_ATTESTATION_METADATA_MISMATCH"),
        ("blocked", block.get("blocked"), False, "RECEIVER_ATTESTATION_BLOCKED"),
        ("operation_id", operation.get("operation_id"), RECEIVER_ATTESTATION_OPERATION_ID, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("operation_type", operation.get("operation_type"), RECEIVER_ATTESTATION_OPERATION_TYPE, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("operation_version", operation.get("operation_version"), RESULT_VERSION, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("operation_scope", operation.get("operation_scope"), RECEIVER_ATTESTATION_OPERATION_SCOPE, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("candidate_id", operation.get("receiver_side_answerable_basis_candidate_id"), DECLARATION_CANDIDATE_ID, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("selected_sufficiency_id", operation.get("selected_candidate_sufficiency_operation_id"), CANDIDATE_SUFFICIENCY_OPERATION_ID, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("selected_sufficiency_result", operation.get("selected_candidate_sufficiency_operation_result_required"), CANDIDATE_SUFFICIENCY_RESULT_REQUIRED, "RECEIVER_ATTESTATION_IDENTITY_MISMATCH"),
        ("operation_result", operation.get("receiver_attestation_operation_result"), RECEIVER_ATTESTATION_RESULT_REQUIRED, "RECEIVER_ATTESTATION_RESULT_MISMATCH"),
        ("summary_result", summary.get("operation_result"), RECEIVER_ATTESTATION_RESULT_REQUIRED, "RECEIVER_ATTESTATION_RESULT_MISMATCH"),
        ("detail_result", detail.get("operation_result"), RECEIVER_ATTESTATION_RESULT_REQUIRED, "RECEIVER_ATTESTATION_RESULT_MISMATCH"),
        ("basis_supplied", operation.get("operation_basis_supplied"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("basis_admitted", operation.get("operation_basis_admitted"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("attestation_decided", operation.get("receiver_attestation_decided"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("attestation_recorded", operation.get("receiver_attestation_recorded"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("operation_recorded", operation.get("receiver_attestation_operation_recorded"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("result_recorded", operation.get("receiver_attestation_operation_result_recorded"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("operation_exhausted", operation.get("receiver_attestation_operation_exhausted"), True, "RECEIVER_ATTESTATION_POSTURE_MISMATCH"),
        ("completed_count", detail.get("completed_result_posture_count"), 1, "RECEIVER_ATTESTATION_CARDINALITY_MISMATCH"),
    ]
    code, reason = _expect_many(checks, "receiver_attestation", expectations)
    if code is not None:
        return code, reason, validation

    correspondence_valid = (
        identity.get("operation_id") == RECEIVER_ATTESTATION_OPERATION_ID
        and identity.get("selected_candidate_id") == DECLARATION_CANDIDATE_ID
        and identity.get("selected_sufficiency_operation_id")
        == CANDIDATE_SUFFICIENCY_OPERATION_ID
        and identity.get("selected_sufficiency_operation_result_required")
        == CANDIDATE_SUFFICIENCY_RESULT_REQUIRED
        and posture.get("operation_recorded") is True
        and posture.get("operation_result_recorded") is True
        and posture.get("operation_exhausted") is True
    )
    code, reason = _require(
        checks,
        "receiver_attestation.correspondence",
        correspondence_valid,
        "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        "receiver-attestation correspondence is not exact",
        expected=DECLARATION_CANDIDATE_ID,
    )
    if code is not None:
        return code, reason, validation
    if not _canonical_false_mapping(non_claims):
        code = "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE"
        _require(
            checks,
            "receiver_attestation.non_claims",
            False,
            code,
            "receiver-attestation non-claims are not canonical false",
        )
        return code, "receiver-attestation non-claims are not canonical false", validation
    checks.append(_check("receiver_attestation.non_claims", True, expected=False))

    validation.update(
        {
            "artifact_validated": True,
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "standing": {
                "operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
                "outcome": RECEIVER_ATTESTATION_OUTCOME_REQUIRED,
                "operation_result": RECEIVER_ATTESTATION_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "operation_basis_supplied": True,
                "operation_basis_admitted": True,
                "receiver_attestation_recorded": True,
                "operation_exhausted": True,
                "completed_result_posture_count": 1,
            },
        }
    )
    return None, None, validation


def _empty_receipt_validation() -> dict[str, Any]:
    return _empty_json_artifact_validation(
        RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
        RECEIVER_ANSWERABLE_RECEIPT_SHA256,
    )


def _validate_receiver_answerable_receipt_artifact(
    checks: list[dict[str, Any]],
    read_path: Path | str,
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_receipt_validation()
    code, reason, artifact = _load_exact_json_artifact(
        read_path=read_path,
        canonical_path=RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
        expected_sha256=RECEIVER_ANSWERABLE_RECEIPT_SHA256,
        prefix="receiver_answerable_receipt",
        code_prefix="RECEIVER_ANSWERABLE_RECEIPT",
        checks=checks,
        validation=validation,
    )
    if code is not None or artifact is None:
        return code, reason, validation
    operation = artifact.get(
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_summary"
    )
    identity = artifact.get("selected_operation_and_candidate_identity")
    posture = artifact.get("operation_posture")
    detail = artifact.get("operation_result_detail")
    correspondence = artifact.get("upstream_correspondence_validation")
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (
            operation,
            summary,
            identity,
            posture,
            detail,
            correspondence,
            block,
            non_claims,
        )
    ):
        code = "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_SECTION_MISSING"
        _require(
            checks,
            "receiver_answerable_receipt.sections",
            False,
            code,
            "receiver-answerable-receipt artifact lacks compact sections",
        )
        return code, "receiver-answerable-receipt artifact lacks compact sections", validation
    checks.append(_check("receiver_answerable_receipt.sections", True))

    expectations = [
        ("resolver_module", artifact.get("resolver_module"), RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE, "RECEIVER_ANSWERABLE_RECEIPT_METADATA_MISMATCH"),
        ("result_version", artifact.get("result_version"), RESULT_VERSION, "RECEIVER_ANSWERABLE_RECEIPT_METADATA_MISMATCH"),
        ("outcome", artifact.get("outcome"), RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED, "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH"),
        ("failed_check_count", artifact.get("failed_check_count"), 0, "RECEIVER_ANSWERABLE_RECEIPT_FAILED_CHECKS_PRESENT"),
        ("passed_check_count", artifact.get("passed_check_count"), RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT, "RECEIVER_ANSWERABLE_RECEIPT_METADATA_MISMATCH"),
        ("blocked", block.get("blocked"), False, "RECEIVER_ANSWERABLE_RECEIPT_BLOCKED"),
        ("operation_id", operation.get("operation_id"), RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("operation_type", operation.get("operation_type"), RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("operation_version", operation.get("operation_version"), RESULT_VERSION, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("operation_scope", operation.get("operation_scope"), RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("candidate_id", operation.get("receiver_side_answerable_basis_candidate_id"), DECLARATION_CANDIDATE_ID, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("selected_attestation_id", operation.get("selected_receiver_attestation_operation_id"), RECEIVER_ATTESTATION_OPERATION_ID, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("selected_attestation_result", operation.get("selected_receiver_attestation_operation_result_required"), RECEIVER_ATTESTATION_RESULT_REQUIRED, "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH"),
        ("operation_result", operation.get("receiver_answerable_receipt_operation_result"), RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED, "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH"),
        ("top_result", artifact.get("operation_result"), RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED, "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH"),
        ("summary_result", summary.get("operation_result"), RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED, "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH"),
        ("detail_result", detail.get("operation_result"), RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED, "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH"),
        ("basis_supplied", operation.get("operation_basis_supplied"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("basis_admitted", operation.get("operation_basis_admitted"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("receipt_decided", operation.get("receiver_answerable_receipt_decided"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("receipt_recorded", operation.get("receiver_answerable_receipt_recorded"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("receipt_present", operation.get("receiver_answerable_receipt_present"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("operation_recorded", operation.get("receiver_answerable_receipt_operation_recorded"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("result_recorded", operation.get("receiver_answerable_receipt_operation_result_recorded"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("operation_exhausted", operation.get("receiver_answerable_receipt_operation_exhausted"), True, "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH"),
        ("completed_count", operation.get("completed_result_posture_count"), 1, "RECEIVER_ANSWERABLE_RECEIPT_CARDINALITY_MISMATCH"),
    ]
    code, reason = _expect_many(checks, "receiver_answerable_receipt", expectations)
    if code is not None:
        return code, reason, validation

    correspondence_valid = (
        identity.get("operation_id") == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID
        and identity.get("selected_candidate_id") == DECLARATION_CANDIDATE_ID
        and identity.get("selected_attestation_operation_id")
        == RECEIVER_ATTESTATION_OPERATION_ID
        and identity.get("selected_attestation_operation_result_required")
        == RECEIVER_ATTESTATION_RESULT_REQUIRED
        and correspondence.get("upstream_correspondence_validated") is True
        and correspondence.get("selected_attestation_operation_identity_corresponds")
        is True
        and correspondence.get("selected_candidate_identity_corresponds") is True
        and posture.get("completed_result_posture_count") == 1
    )
    code, reason = _require(
        checks,
        "receiver_answerable_receipt.correspondence",
        correspondence_valid,
        "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH",
        "receiver-answerable-receipt correspondence is not exact",
        expected=RECEIVER_ATTESTATION_OPERATION_ID,
    )
    if code is not None:
        return code, reason, validation
    if not _canonical_false_mapping(non_claims):
        code = "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE"
        _require(
            checks,
            "receiver_answerable_receipt.non_claims",
            False,
            code,
            "receiver-answerable-receipt non-claims are not canonical false",
        )
        return code, "receiver-answerable-receipt non-claims are not canonical false", validation
    checks.append(_check("receiver_answerable_receipt.non_claims", True, expected=False))

    validation.update(
        {
            "artifact_validated": True,
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "standing": {
                "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
                "outcome": RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED,
                "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "selected_attestation_operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
                "operation_basis_supplied": True,
                "operation_basis_admitted": True,
                "receiver_answerable_receipt_present": True,
                "receiver_answerable_receipt_recorded": True,
                "operation_exhausted": True,
                "completed_result_posture_count": 1,
            },
        }
    )
    return None, None, validation


def _empty_atomic_basis(request: Any) -> dict[str, Any]:
    return {
        "operation_basis_supplied": _operation_basis_supplied(request),
        "specification_validated": False,
        "boundary_artifact_validated": False,
        "declaration_validated": False,
        "candidate_sufficiency_artifact_validated": False,
        "receiver_attestation_artifact_validated": False,
        "receiver_answerable_receipt_artifact_validated": False,
        "all_six_governed_files_validated": False,
        "canonical_request_validated": False,
        "operation_basis_admitted": False,
        "partial_basis_cannot_produce_completed_result": True,
    }


def _derive_target_evaluations(
    *,
    atomic_basis_admitted: bool,
    declaration: Mapping[str, Any],
) -> dict[str, str]:
    if not atomic_basis_admitted:
        return {
            field: TARGET_EVALUATION_NOT_EVALUATED for field in TARGET_CONDITIONS
        }
    records = declaration.get("matter_relevant_records")
    if not isinstance(records, Mapping):
        return {
            field: TARGET_EVALUATION_INDETERMINATE for field in TARGET_CONDITIONS
        }
    evaluations: dict[str, str] = {}
    for condition, record in TARGET_DECLARATION_RECORDS.items():
        value = records.get(record)
        if value is True:
            evaluations[condition] = TARGET_EVALUATION_SUPPORTED
        elif value is False:
            evaluations[condition] = TARGET_EVALUATION_REQUIRES_BASIS
        else:
            evaluations[condition] = TARGET_EVALUATION_INDETERMINATE
    return evaluations


def _outcome_from_evaluations(evaluations: Mapping[str, str]) -> str:
    values = [evaluations.get(field) for field in TARGET_CONDITIONS]
    if any(value == TARGET_EVALUATION_INDETERMINATE for value in values):
        return OUTCOME_INDETERMINATE
    if any(value == TARGET_EVALUATION_REQUIRES_BASIS for value in values):
        return OUTCOME_REQUIRES_BASIS
    if all(value == TARGET_EVALUATION_SUPPORTED for value in values):
        return OUTCOME_SUPPORTED
    return OUTCOME_BLOCKED


def _operation_result_for_outcome(outcome: str | None) -> str:
    if outcome == OUTCOME_SUPPORTED:
        return OPERATION_RESULT_SUPPORTED
    if outcome == OUTCOME_REQUIRES_BASIS:
        return OPERATION_RESULT_REQUIRES_BASIS
    if outcome == OUTCOME_INDETERMINATE:
        return OPERATION_RESULT_INDETERMINATE
    return OPERATION_RESULT_NOT_EVALUATED


def _completed_outcome(outcome: str | None) -> bool:
    return outcome in {
        OUTCOME_SUPPORTED,
        OUTCOME_REQUIRES_BASIS,
        OUTCOME_INDETERMINATE,
    }


def _branch_posture(
    outcome: str | None,
    *,
    basis_supplied: bool,
) -> dict[str, Any]:
    completed = _completed_outcome(outcome)
    return {
        "operation_basis_supplied": basis_supplied,
        "operation_basis_admitted": completed,
        "receiver_originating_modal_fact_evaluation_performed": completed,
        "receiver_originating_modal_fact_evaluation_result_decided": completed,
        "receiver_originating_modal_fact_evaluation_result_recorded": completed,
        "receiver_originating_modal_fact_evaluation_operation_recorded": completed,
        "receiver_originating_modal_fact_evaluation_operation_result_recorded": completed,
        "receiver_originating_modal_fact_evaluation_operation_exhausted": completed,
        "completed_modal_fact_evaluation_result_posture_count": int(completed),
    }


def _decision_for_outcome(
    outcome: str | None,
    *,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    if outcome == OUTCOME_SUPPORTED:
        decision_code = OPERATION_RESULT_SUPPORTED
        decision_reason = (
            "both exact target conditions are supported by the admitted "
            "receiver-originating source under the bounded source relation"
        )
    elif outcome == OUTCOME_REQUIRES_BASIS:
        decision_code = OPERATION_RESULT_REQUIRES_BASIS
        decision_reason = (
            "one or more target conditions require additional bounded basis"
        )
    elif outcome == OUTCOME_INDETERMINATE:
        decision_code = OPERATION_RESULT_INDETERMINATE
        decision_reason = (
            "one or more target conditions remain indeterminate under the "
            "admitted bounded basis"
        )
    elif outcome == OUTCOME_BLOCKED:
        decision_code = code
        decision_reason = reason
    else:
        decision_code = None
        decision_reason = None
    return {
        "decision_code": decision_code,
        "decision_reason": decision_reason,
        "decision_evaluated": _completed_outcome(outcome),
        "result_precedence": [
            OUTCOME_BLOCKED,
            OUTCOME_INDETERMINATE,
            OUTCOME_REQUIRES_BASIS,
            OUTCOME_SUPPORTED,
        ],
    }


def _prior_presence_posture(completed: bool) -> dict[str, Any]:
    evaluations = {
        **{field: "SATISFIED" for field in PRIOR_SATISFIED_CONDITIONS},
        **{
            field: "REQUIRES_BASIS"
            for field in PRIOR_REQUIRES_BASIS_CONDITIONS
        },
    }
    return {
        "compact_prior_presence_standing_validated": completed,
        "prior_presence_result_preserved": completed,
        "prior_outcome": PRIOR_PRESENCE_OUTCOME,
        "prior_operation_result": PRIOR_PRESENCE_RESULT,
        "prior_operation_exhausted": completed,
        "prior_admissible_future_route": None,
        "condition_evaluations": evaluations,
        "all_twelve_prior_requires_basis_conditions_historically_legible": completed,
        "presence_supported": False,
        "presence_authorized": False,
        "presence_established": False,
        "presence_recorded": False,
    }


def _source_selection_posture(completed: bool) -> dict[str, Any]:
    return {
        "source_selection_validated": completed,
        "exact_source_identity_validated": completed,
        "exact_source_class_validated": completed,
        "exact_relation_class_validated": completed,
        "exact_matter_class_validated": completed,
        "receiver_origin_validated": completed,
        "declared_provenance_posture_validated": completed,
        "carried_arrival_validated": completed,
        "non_native_standing_validated": completed,
        "jurisdiction_distinction_validated": completed,
        "candidate_correspondence_validated": completed,
        "receiver_attestation_correspondence_validated": completed,
        "receiver_answerable_receipt_correspondence_validated": completed,
        "only_two_matter_relevant_records_used": completed,
        "adjacent_declaration_records_not_imported": True,
    }


def _what_remains_open(outcome: str | None) -> list[str]:
    items = [
        "receiver-originating modal-fact evaluation operation tests",
        "receiver-originating modal-fact evaluation operation request",
        "receiver-originating modal-fact evaluation operation live result",
        "receiver-originating modal-fact evaluation operation terminal summary",
    ]
    if not _completed_outcome(outcome):
        items.append("actual execution of the two modal-fact evaluations")
    items.extend(
        [
            "separately bounded modal-fact establishment question",
            "excluded source-body-verifiable integrity conditions",
            "later receiver-answerable-basis successor",
            "later presence re-evaluation",
            "presence support, authorization, establishment, and recording",
            "threshold",
            "truth settlement",
            "identity",
            "custody proof",
            "provenance proof",
            "physical validity",
            "authority",
            "truth",
            "standing",
            "relation",
            "coupling",
            "FIELD machinery",
            "runtime",
            "API",
            "public interface",
            "public intake",
            "output",
            "action",
            "derivative reception",
            "synchronization",
            "repair",
            "validation",
            "follow-on work",
        ]
    )
    return items


def _declared_request_posture(
    request: Any,
    *,
    validated: bool,
) -> dict[str, bool]:
    mapping = request if isinstance(request, Mapping) else {}
    return {
        "canonical_schema_validated": validated
        and set(mapping) == _canonical_request_keys(),
        "intent_validated": validated and mapping.get("intent") == INTENT_RECORD,
        "canonical_identity_and_paths_validated": validated
        and all(
            mapping.get(field) == expected
            for field, expected in _identity_request_values().items()
        ),
        "execution_selected": validated
        and mapping.get(
            "receiver_originating_modal_fact_evaluation_execution_selected"
        )
        is True,
        "declared_non_claims_validated": validated
        and _non_claims_valid(mapping.get("declared_non_claims")),
        "unknown_request_fields_absent": isinstance(request, Mapping)
        and not bool(set(mapping).difference(_canonical_request_keys())),
        "result_and_semantic_preclaims_absent": isinstance(request, Mapping)
        and not bool(set(mapping).intersection(PROHIBITED_DIRECT_REQUEST_FIELDS)),
    }


def _target_evaluation_section(
    evaluations: Mapping[str, str],
) -> dict[str, dict[str, Any]]:
    return {
        condition: {
            "condition_id": condition,
            "evaluation": evaluations.get(
                condition,
                TARGET_EVALUATION_NOT_EVALUATED,
            ),
            "matter_relevant_declaration_record": TARGET_DECLARATION_RECORDS[
                condition
            ],
            "matter_relevant_declaration_value": (
                True
                if evaluations.get(condition) == TARGET_EVALUATION_SUPPORTED
                else None
            ),
            "source_support_only": True,
            "modal_fact_established": False,
        }
        for condition in TARGET_CONDITIONS
    }


def _statement(outcome: str | None) -> dict[str, bool]:
    completed = _completed_outcome(outcome)
    return {
        "one_exact_receiver_originating_source_evaluated": completed,
        "exactly_two_target_conditions_only": True,
        "source_support_evaluation_only": True,
        "source_admissibility_not_repeated": True,
        "receiver_origin_preserved": True,
        "source_relation_preserved": True,
        "declared_provenance_posture_preserved": True,
        "carried_arrival_remains_non_native": True,
        "jurisdiction_distinction_preserved": True,
        "declaration_not_naturalized": True,
        "target_modal_facts_not_established": True,
        "actual_refusal_or_withholding_not_established": True,
        "universal_or_metaphysical_freedom_not_established": True,
        "truth_authority_standing_identity_and_presence_not_created": True,
        "excluded_source_body_conditions_not_evaluated": True,
        "prior_presence_result_not_revised": True,
        "no_scan_discovery_repair_or_latest_file_selection": True,
        "no_automatic_future_route": True,
        "result_level_non_claims_canonical_false": True,
        "open_does_not_mean_next": True,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("receiver_originating_modal_fact_evaluation_operation")
    operation = operation if isinstance(operation, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    decision = result.get("operation_decision")
    decision = decision if isinstance(decision, Mapping) else {}
    spec = result.get("specification_validation")
    spec = spec if isinstance(spec, Mapping) else {}
    boundary = result.get("boundary_artifact_validation")
    boundary = boundary if isinstance(boundary, Mapping) else {}
    declaration = result.get("receiver_originating_declaration_validation")
    declaration = declaration if isinstance(declaration, Mapping) else {}
    candidate = result.get("candidate_sufficiency_artifact_validation")
    candidate = candidate if isinstance(candidate, Mapping) else {}
    attestation = result.get("receiver_attestation_artifact_validation")
    attestation = attestation if isinstance(attestation, Mapping) else {}
    receipt = result.get("receiver_answerable_receipt_artifact_validation")
    receipt = receipt if isinstance(receipt, Mapping) else {}
    atomic = result.get("atomic_operation_basis_posture")
    atomic = atomic if isinstance(atomic, Mapping) else {}
    evaluations = result.get("target_condition_evaluations")
    evaluations = evaluations if isinstance(evaluations, Mapping) else {}
    prior = result.get("prior_presence_preservation_posture")
    prior = prior if isinstance(prior, Mapping) else {}
    omission = result.get("omission_posture")
    omission = omission if isinstance(omission, Mapping) else {}
    lineage = result.get("lineage_preservation_posture")
    lineage = lineage if isinstance(lineage, Mapping) else {}
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "boundary_artifact_path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
        "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
        "candidate_sufficiency_artifact_path": str(
            CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_attestation_artifact_path": str(
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_answerable_receipt_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
        ),
        "selected_source_class": SELECTED_SOURCE_CLASS,
        "selected_relation_class": SELECTED_RELATION_CLASS,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "selected_matter": list(TARGET_CONDITIONS),
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_provenance_posture": SELECTED_SOURCE_PROVENANCE_POSTURE,
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "outcome": result.get("outcome"),
        "operation_result": result.get("operation_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("decision_code"),
        "decision_reason": decision.get("decision_reason"),
        "specification_validated": spec.get("specification_validated"),
        "boundary_artifact_validated": boundary.get("artifact_validated"),
        "declaration_validated": declaration.get("declaration_validated"),
        "candidate_sufficiency_artifact_validated": candidate.get(
            "artifact_validated"
        ),
        "receiver_attestation_artifact_validated": attestation.get(
            "artifact_validated"
        ),
        "receiver_answerable_receipt_artifact_validated": receipt.get(
            "artifact_validated"
        ),
        "operation_basis_supplied": atomic.get("operation_basis_supplied"),
        "operation_basis_admitted": atomic.get("operation_basis_admitted"),
        "target_condition_evaluations": {
            field: (
                evaluations.get(field, {}).get("evaluation")
                if isinstance(evaluations.get(field), Mapping)
                else None
            )
            for field in TARGET_CONDITIONS
        },
        "receiver_answerable_basis_refusable_supported": operation.get(
            "receiver_answerable_basis_refusable_supported"
        ),
        "receiver_answerable_basis_could_have_been_withheld_supported": (
            operation.get(
                "receiver_answerable_basis_could_have_been_withheld_supported"
            )
        ),
        "completed_modal_fact_evaluation_result_posture_count": result.get(
            "completed_modal_fact_evaluation_result_posture_count"
        ),
        "operation_exhausted": operation.get(
            "receiver_originating_modal_fact_evaluation_operation_exhausted"
        ),
        "excluded_conditions_not_evaluated": result.get(
            "excluded_condition_posture", {}
        ).get("excluded_conditions_not_evaluated"),
        "prior_presence_result_preserved": prior.get(
            "prior_presence_result_preserved"
        ),
        "source_origin_and_jurisdiction_preserved": bool(lineage)
        and all(value is True for value in lineage.values()),
        "result_level_non_claims_canonical_false": result.get(
            "result_level_non_claims_canonical_false"
        ),
        "complete_material_omission_posture": omission.get(
            "complete_material_omission_posture"
        ),
        "admissible_future_route": result.get("admissible_future_route"),
    }


def _build_result(
    request: Any,
    outcome: str | None,
    checks: list[dict[str, Any]],
    *,
    request_validated: bool = False,
    specification_validation: Mapping[str, Any] | None = None,
    boundary_validation: Mapping[str, Any] | None = None,
    declaration_validation: Mapping[str, Any] | None = None,
    candidate_validation: Mapping[str, Any] | None = None,
    attestation_validation: Mapping[str, Any] | None = None,
    receipt_validation: Mapping[str, Any] | None = None,
    atomic_basis: Mapping[str, Any] | None = None,
    evaluations: Mapping[str, str] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    basis_supplied = _operation_basis_supplied(request)
    completed = _completed_outcome(outcome)
    operation_result = _operation_result_for_outcome(outcome)
    evals = (
        dict(evaluations)
        if isinstance(evaluations, Mapping)
        else {
            field: TARGET_EVALUATION_NOT_EVALUATED
            for field in TARGET_CONDITIONS
        }
    )
    if not completed:
        evals = {
            field: TARGET_EVALUATION_NOT_EVALUATED
            for field in TARGET_CONDITIONS
        }
    support = {
        field: evals.get(field) == TARGET_EVALUATION_SUPPORTED
        for field in TARGET_CONDITIONS
    }
    missing = [
        field
        for field in TARGET_CONDITIONS
        if evals.get(field) == TARGET_EVALUATION_REQUIRES_BASIS
    ]
    indeterminate = [
        field
        for field in TARGET_CONDITIONS
        if evals.get(field) == TARGET_EVALUATION_INDETERMINATE
    ]
    branch = _branch_posture(outcome, basis_supplied=basis_supplied)
    atomic = (
        copy.deepcopy(dict(atomic_basis))
        if isinstance(atomic_basis, Mapping)
        else _empty_atomic_basis(request)
    )
    atomic["operation_basis_supplied"] = basis_supplied
    atomic["operation_basis_admitted"] = completed
    lineage = _canonical_lineage_posture(completed)
    operation = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_originating_modal_fact_evaluation_operation_id": OPERATION_ID,
        "receiver_originating_modal_fact_evaluation_operation_type": OPERATION_TYPE,
        "receiver_originating_modal_fact_evaluation_operation_version": OPERATION_VERSION,
        "receiver_originating_modal_fact_evaluation_operation_scope": OPERATION_SCOPE,
        "selected_source_class": SELECTED_SOURCE_CLASS,
        "selected_relation_class": SELECTED_RELATION_CLASS,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "selected_matter": list(TARGET_CONDITIONS),
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_provenance_posture": SELECTED_SOURCE_PROVENANCE_POSTURE,
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "receiver_originating_modal_fact_evaluation_operation_result": operation_result,
        "receiver_answerable_basis_refusable_evaluation": evals[
            "receiver_answerable_basis_refusable"
        ],
        "receiver_answerable_basis_could_have_been_withheld_evaluation": evals[
            "receiver_answerable_basis_could_have_been_withheld"
        ],
        "receiver_answerable_basis_refusable_supported": support[
            "receiver_answerable_basis_refusable"
        ],
        "receiver_answerable_basis_could_have_been_withheld_supported": support[
            "receiver_answerable_basis_could_have_been_withheld"
        ],
        "missing_or_insufficient_modal_fact_basis": missing,
        "indeterminate_modal_fact_conditions": indeterminate,
        "excluded_condition_evaluation_performed": False,
        "excluded_conditions_not_evaluated": True,
        "admissible_future_route": None,
        **branch,
        **_canonical_non_claims(),
    }
    result: dict[str, Any] = {
        "receiver_originating_modal_fact_evaluation_operation_metadata": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "boundary_artifact_path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
            "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
            "candidate_sufficiency_artifact_path": str(
                CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
            ),
            "receiver_attestation_artifact_path": str(
                RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
            ),
            "receiver_answerable_receipt_artifact_path": str(
                RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
            ),
        },
        "declared_receiver_originating_modal_fact_evaluation_operation_request": (
            _declared_request_posture(request, validated=request_validated)
        ),
        "specification_validation": (
            copy.deepcopy(dict(specification_validation))
            if isinstance(specification_validation, Mapping)
            else _empty_specification_validation()
        ),
        "boundary_artifact_validation": (
            copy.deepcopy(dict(boundary_validation))
            if isinstance(boundary_validation, Mapping)
            else _empty_boundary_validation()
        ),
        "receiver_originating_declaration_validation": (
            copy.deepcopy(dict(declaration_validation))
            if isinstance(declaration_validation, Mapping)
            else _empty_declaration_validation()
        ),
        "candidate_sufficiency_artifact_validation": (
            copy.deepcopy(dict(candidate_validation))
            if isinstance(candidate_validation, Mapping)
            else _empty_candidate_validation()
        ),
        "receiver_attestation_artifact_validation": (
            copy.deepcopy(dict(attestation_validation))
            if isinstance(attestation_validation, Mapping)
            else _empty_attestation_validation()
        ),
        "receiver_answerable_receipt_artifact_validation": (
            copy.deepcopy(dict(receipt_validation))
            if isinstance(receipt_validation, Mapping)
            else _empty_receipt_validation()
        ),
        "atomic_operation_basis_posture": atomic,
        "source_selection_and_carriage_lineage": _source_selection_posture(
            completed
        ),
        "target_condition_evaluations": _target_evaluation_section(evals),
        "target_support_posture": {
            "receiver_answerable_basis_refusable_supported": support[
                "receiver_answerable_basis_refusable"
            ],
            "receiver_answerable_basis_could_have_been_withheld_supported": support[
                "receiver_answerable_basis_could_have_been_withheld"
            ],
            "support_is_matter_bound": True,
            "support_is_source_relation_bound": True,
            "support_is_not_reality_wide_establishment": True,
        },
        "excluded_condition_posture": _canonical_excluded_condition_posture(),
        "prior_presence_preservation_posture": _prior_presence_posture(completed),
        "operation_posture": {
            **branch,
            "single_use_only": True,
            "source_admissibility_not_repeated": True,
            "operation_exhaustion_is_not_modal_fact_establishment": True,
            "operation_exhaustion_is_not_complete_receiver_answerable_basis": True,
            "operation_exhaustion_is_not_presence": True,
        },
        "lineage_preservation_posture": lineage,
        "omission_posture": _canonical_omission_posture(),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        "receiver_originating_modal_fact_evaluation_operation_non_meaning": (
            _canonical_non_meaning()
        ),
        "blocked_conversions": list(BLOCKED_CONVERSIONS),
        "operation_decision": _decision_for_outcome(
            outcome,
            code=code,
            reason=reason,
        ),
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "receiver_originating_modal_fact_evaluation_operation": operation,
        "receiver_originating_modal_fact_evaluation_operation_statement": (
            _statement(outcome)
        ),
        "receiver_originating_modal_fact_evaluation_operation_checks": (
            copy.deepcopy(checks)
        ),
        "admissible_future_route": None,
        "what_remains_open": _what_remains_open(outcome),
        "outcome": outcome,
        "operation_result": operation_result,
        "receiver_originating_modal_fact_evaluation_operation_result": (
            operation_result
        ),
        "completed_modal_fact_evaluation_result_posture_count": branch[
            "completed_modal_fact_evaluation_result_posture_count"
        ],
        "failed_check_count": sum(
            check.get("passed") is False for check in checks
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in checks
        ),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
    }
    result["receiver_originating_modal_fact_evaluation_operation_summary"] = (
        _summary_from_result(result)
    )
    return result


def build_receiver_originating_modal_fact_evaluation_operation_v0_min_default_result(
) -> dict[str, Any]:
    """Return the pure pre-execution default posture without filesystem reads."""
    return _build_result(
        {},
        None,
        [],
        request_validated=False,
    )


def build_receiver_originating_modal_fact_evaluation_operation_v0_min_result(
) -> dict[str, Any]:
    """Return the pure pre-execution default result posture."""
    return build_receiver_originating_modal_fact_evaluation_operation_v0_min_default_result()


def _append_completed_checks(
    checks: list[dict[str, Any]],
    outcome: str,
    evaluations: Mapping[str, str],
) -> None:
    for field in TARGET_CONDITIONS:
        checks.append(
            _check(
                "target_evaluation." + field,
                evaluations.get(field) in TARGET_CONDITION_EVALUATION_FAMILY,
                expected=evaluations.get(field),
            )
        )
    for field in EXCLUDED_CONDITIONS:
        checks.append(
            _check(
                "excluded_condition." + field,
                True,
                expected=TARGET_EVALUATION_NOT_EVALUATED,
            )
        )
    for field in LINEAGE_PRESERVATION_FIELDS:
        checks.append(_check("lineage." + field, True, expected=True))
    for field in REQUIRED_FALSE_NON_CLAIMS:
        checks.append(_check("non_claims." + field, True, expected=False))
    for field in OMISSION_POSTURE_FIELDS:
        checks.append(_check("omission." + field, True, expected=True))
    for field in NON_MEANING_FIELDS:
        checks.append(_check("non_meaning." + field, True, expected=True))
    checks.extend(
        [
            _check("atomic_basis.operation_basis_admitted", True, expected=True),
            _check("evaluation.excluded_conditions_not_evaluated", True, expected=True),
            _check("evaluation.prior_presence_preserved", True, expected=True),
            _check("evaluation.admissible_future_route", True, expected=None),
            _check("evaluation.no_scan_discovery_repair", True, expected=True),
            _check("branch.outcome", outcome in OUTCOME_FAMILY, expected=outcome),
        ]
    )


def _blocked_result(
    request: Any,
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    **validations: Any,
) -> dict[str, Any]:
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        code=code,
        reason=reason,
        **validations,
    )


def resolve_receiver_originating_modal_fact_evaluation_operation_v0_min(
    request: Mapping[str, Any] | None = None,
    *,
    governing_specification_path: Path | str | None = None,
    boundary_artifact_path: Path | str | None = None,
    declaration_surface_path: Path | str | None = None,
    candidate_sufficiency_artifact_path: Path | str | None = None,
    receiver_attestation_artifact_path: Path | str | None = None,
    receiver_answerable_receipt_artifact_path: Path | str | None = None,
) -> dict[str, Any]:
    """Resolve one exact two-condition source-support operation."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request: Any = _new_canonical_request()
    elif not isinstance(request, Mapping):
        declared_request = copy.deepcopy(request)
        code = "REQUEST_NOT_MAPPING"
        _require(
            checks,
            "request.mapping",
            False,
            code,
            "declared request is not a mapping",
        )
        return _blocked_result(
            declared_request,
            checks,
            code,
            "declared request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        return _blocked_result(declared_request, checks, code, str(reason))
    request_validated = True

    specification_read_path = (
        governing_specification_path
        if governing_specification_path is not None
        else GOVERNING_SPECIFICATION_RELATIVE_PATH
    )
    boundary_read_path = (
        boundary_artifact_path
        if boundary_artifact_path is not None
        else BOUNDARY_ARTIFACT_RELATIVE_PATH
    )
    declaration_read_path = (
        declaration_surface_path
        if declaration_surface_path is not None
        else DECLARATION_SURFACE_RELATIVE_PATH
    )
    candidate_read_path = (
        candidate_sufficiency_artifact_path
        if candidate_sufficiency_artifact_path is not None
        else CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
    )
    attestation_read_path = (
        receiver_attestation_artifact_path
        if receiver_attestation_artifact_path is not None
        else RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
    )
    receipt_read_path = (
        receiver_answerable_receipt_artifact_path
        if receiver_answerable_receipt_artifact_path is not None
        else RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
    )

    code, reason, specification = _validate_specification(
        checks,
        specification_read_path,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
        )

    code, reason, boundary = _validate_boundary_artifact(
        checks,
        boundary_read_path,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
        )

    code, reason, declaration = _validate_declaration_surface(
        checks,
        declaration_read_path,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
            declaration_validation=declaration,
        )

    code, reason, candidate = _validate_candidate_sufficiency_artifact(
        checks,
        candidate_read_path,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
            declaration_validation=declaration,
            candidate_validation=candidate,
        )

    code, reason, attestation = _validate_receiver_attestation_artifact(
        checks,
        attestation_read_path,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
        )

    code, reason, receipt = _validate_receiver_answerable_receipt_artifact(
        checks,
        receipt_read_path,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
            receipt_validation=receipt,
        )

    atomic = _empty_atomic_basis(declared_request)
    atomic.update(
        {
            "specification_validated": specification.get(
                "specification_validated"
            )
            is True,
            "boundary_artifact_validated": boundary.get("artifact_validated")
            is True,
            "declaration_validated": declaration.get("declaration_validated")
            is True,
            "candidate_sufficiency_artifact_validated": candidate.get(
                "artifact_validated"
            )
            is True,
            "receiver_attestation_artifact_validated": attestation.get(
                "artifact_validated"
            )
            is True,
            "receiver_answerable_receipt_artifact_validated": receipt.get(
                "artifact_validated"
            )
            is True,
            "canonical_request_validated": request_validated,
        }
    )
    all_files = all(
        atomic.get(field) is True
        for field in (
            "specification_validated",
            "boundary_artifact_validated",
            "declaration_validated",
            "candidate_sufficiency_artifact_validated",
            "receiver_attestation_artifact_validated",
            "receiver_answerable_receipt_artifact_validated",
        )
    )
    atomic["all_six_governed_files_validated"] = all_files
    atomic["operation_basis_admitted"] = (
        all_files
        and request_validated
        and atomic.get("operation_basis_supplied") is True
    )
    code, reason = _require(
        checks,
        "atomic_basis.operation_basis_admitted",
        atomic["operation_basis_admitted"] is True,
        "ATOMIC_BASIS_NOT_ADMITTED",
        "the exact atomic operation basis was not admitted",
        expected=True,
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            str(reason),
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
            receipt_validation=receipt,
            atomic_basis=atomic,
        )

    evaluations = _derive_target_evaluations(
        atomic_basis_admitted=True,
        declaration=declaration,
    )
    outcome = _outcome_from_evaluations(evaluations)
    if outcome == OUTCOME_BLOCKED:
        code = "TARGET_EVALUATION_INVALID"
        _require(
            checks,
            "target_evaluation.complete_family",
            False,
            code,
            "target evaluations do not produce one lawful operation result",
        )
        return _blocked_result(
            declared_request,
            checks,
            code,
            "target evaluations do not produce one lawful operation result",
            request_validated=request_validated,
            specification_validation=specification,
            boundary_validation=boundary,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
            receipt_validation=receipt,
            atomic_basis=atomic,
        )

    _append_completed_checks(checks, outcome, evaluations)
    return _build_result(
        declared_request,
        outcome,
        checks,
        request_validated=request_validated,
        specification_validation=specification,
        boundary_validation=boundary,
        declaration_validation=declaration,
        candidate_validation=candidate,
        attestation_validation=attestation,
        receipt_validation=receipt,
        atomic_basis=atomic,
        evaluations=evaluations,
    )


def _request_path_blocked_result(
    code: str,
    reason: str,
) -> dict[str, Any]:
    checks = [_check("request_path.strict_json_mapping", False, code)]
    return _blocked_result(
        {},
        checks,
        code,
        reason,
    )


def resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(
    request_path: Path | str,
    **resolver_paths: Any,
) -> dict[str, Any]:
    """Strictly read one explicit request path and resolve without discovery."""
    try:
        path = Path(request_path)
    except (TypeError, ValueError):
        return _request_path_blocked_result(
            "REQUEST_PATH_INVALID",
            "request path is invalid",
        )
    payload, error = _read_bytes(path)
    if error == "not_a_file":
        return _request_path_blocked_result(
            "REQUEST_PATH_MISSING",
            "request JSON path is unavailable",
        )
    if error is not None or payload is None:
        return _request_path_blocked_result(
            "REQUEST_PATH_UNREADABLE",
            "request JSON path is unreadable",
        )
    parsed, parse_error = _parse_json_bytes(payload)
    if parse_error == "duplicate_key":
        return _request_path_blocked_result(
            "REQUEST_PATH_DUPLICATE_KEYED",
            "request JSON contains duplicate keys",
        )
    if parse_error is not None:
        return _request_path_blocked_result(
            "REQUEST_PATH_NOT_PARSEABLE",
            "request JSON is not strict parseable UTF-8 JSON",
        )
    if not isinstance(parsed, Mapping):
        return _request_path_blocked_result(
            "REQUEST_PATH_NOT_MAPPING",
            "request JSON top-level value is not a mapping",
        )
    return resolve_receiver_originating_modal_fact_evaluation_operation_v0_min(
        parsed,
        **resolver_paths,
    )


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "complete_boundary_artifact",
        "complete_candidate_sufficiency_artifact",
        "complete_receiver_attestation_artifact",
        "complete_receiver_answerable_receipt_artifact",
        "complete_declaration_body",
        "declaration_body",
        "declaration_content",
        "semantic_payload",
        "sufficiency_basis_records",
        "basis_items",
        "basis_references",
        "bounded_capture_signal_bodies",
        "capture_signal_data",
        "signal_samples",
        "raw_signal_data",
        "archive_bytes",
        "archive_body",
        "alternative_declarations",
        "alternative_artifacts",
        "unrelated_receiver_side_material",
        "excluded_condition_evidence_bodies",
    }
    if isinstance(value, Mapping):
        return any(
            key in forbidden_keys or _contains_prohibited_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return any(_contains_prohibited_complete_material(item) for item in value)
    return False


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get("receiver_originating_modal_fact_evaluation_operation_checks")
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping)
        and set(check).issubset(
            {"name", "passed", "expected", "failure_code", "block_code"}
        )
        and isinstance(check.get("name"), str)
        and bool(check.get("name"))
        and type(check.get("passed")) is bool
        for check in checks
    ):
        return False
    failed = sum(check.get("passed") is False for check in checks)
    passed = sum(check.get("passed") is True for check in checks)
    if result.get("failed_check_count") != failed or result.get("passed_check_count") != passed:
        return False
    for check in checks:
        if check.get("passed") is True and (
            "failure_code" in check or "block_code" in check
        ):
            return False
        if check.get("passed") is False and (
            check.get("failure_code") != check.get("block_code")
            or check.get("failure_code") not in BLOCK_CODES
        ):
            return False
        for field in ("failure_code", "block_code"):
            if field in check and check[field] not in BLOCK_CODES:
                return False
    if result.get("outcome") == OUTCOME_BLOCKED:
        block = result.get("block")
        return (
            failed == 1
            and isinstance(block, Mapping)
            and any(
                check.get("passed") is False
                and check.get("block_code") == block.get("code")
                for check in checks
            )
        )
    return result.get("outcome") in OUTCOME_FAMILY and failed == 0


def _target_evaluation_values_for_write(
    result: Mapping[str, Any],
) -> dict[str, str] | None:
    section = result.get("target_condition_evaluations")
    if not isinstance(section, Mapping) or set(section) != set(TARGET_CONDITIONS):
        return None
    evaluations: dict[str, str] = {}
    for condition in TARGET_CONDITIONS:
        item = section.get(condition)
        if not isinstance(item, Mapping):
            return None
        evaluation = item.get("evaluation")
        if (
            set(item)
            != {
                "condition_id",
                "evaluation",
                "matter_relevant_declaration_record",
                "matter_relevant_declaration_value",
                "source_support_only",
                "modal_fact_established",
            }
            or item.get("condition_id") != condition
            or evaluation not in TARGET_CONDITION_EVALUATION_FAMILY
            or item.get("matter_relevant_declaration_record")
            != TARGET_DECLARATION_RECORDS[condition]
            or item.get("matter_relevant_declaration_value")
            != (True if evaluation == TARGET_EVALUATION_SUPPORTED else None)
            or item.get("source_support_only") is not True
            or item.get("modal_fact_established") is not False
        ):
            return None
        evaluations[condition] = str(evaluation)
    return evaluations


def _expected_operation_object(
    outcome: str,
    evaluations: Mapping[str, str],
    *,
    basis_supplied: bool,
) -> dict[str, Any]:
    support = {
        field: evaluations.get(field) == TARGET_EVALUATION_SUPPORTED
        for field in TARGET_CONDITIONS
    }
    branch = _branch_posture(outcome, basis_supplied=basis_supplied)
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_originating_modal_fact_evaluation_operation_id": OPERATION_ID,
        "receiver_originating_modal_fact_evaluation_operation_type": OPERATION_TYPE,
        "receiver_originating_modal_fact_evaluation_operation_version": OPERATION_VERSION,
        "receiver_originating_modal_fact_evaluation_operation_scope": OPERATION_SCOPE,
        "selected_source_class": SELECTED_SOURCE_CLASS,
        "selected_relation_class": SELECTED_RELATION_CLASS,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "selected_matter": list(TARGET_CONDITIONS),
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_provenance_posture": SELECTED_SOURCE_PROVENANCE_POSTURE,
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "receiver_originating_modal_fact_evaluation_operation_result": (
            _operation_result_for_outcome(outcome)
        ),
        "receiver_answerable_basis_refusable_evaluation": evaluations.get(
            "receiver_answerable_basis_refusable"
        ),
        "receiver_answerable_basis_could_have_been_withheld_evaluation": (
            evaluations.get(
                "receiver_answerable_basis_could_have_been_withheld"
            )
        ),
        "receiver_answerable_basis_refusable_supported": support[
            "receiver_answerable_basis_refusable"
        ],
        "receiver_answerable_basis_could_have_been_withheld_supported": (
            support["receiver_answerable_basis_could_have_been_withheld"]
        ),
        "missing_or_insufficient_modal_fact_basis": [
            field
            for field in TARGET_CONDITIONS
            if evaluations.get(field) == TARGET_EVALUATION_REQUIRES_BASIS
        ],
        "indeterminate_modal_fact_conditions": [
            field
            for field in TARGET_CONDITIONS
            if evaluations.get(field) == TARGET_EVALUATION_INDETERMINATE
        ],
        "excluded_condition_evaluation_performed": False,
        "excluded_conditions_not_evaluated": True,
        "admissible_future_route": None,
        **branch,
        **_canonical_non_claims(),
    }


def _expected_artifact_standings() -> tuple[tuple[str, Path, str, dict[str, Any]], ...]:
    return (
        (
            "boundary_artifact_validation",
            BOUNDARY_ARTIFACT_RELATIVE_PATH,
            BOUNDARY_SHA256,
            {
                "boundary_id": BOUNDARY_ID,
                "outcome": BOUNDARY_OUTCOME_REQUIRED,
                "boundary_result": BOUNDARY_RESULT_REQUIRED,
                "failed_check_count": 0,
                "passed_check_count": BOUNDARY_PASSED_CHECK_COUNT,
                "boundary_exhausted": True,
                "completed_consideration_posture_count": 1,
                "selected_source_class": SELECTED_SOURCE_CLASS,
                "selected_relation_class": SELECTED_RELATION_CLASS,
                "selected_matter_class": SELECTED_MATTER_CLASS,
                "selected_source_origin": SELECTED_SOURCE_ORIGIN,
                "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
                "selected_source_native_standing": False,
                "jurisdiction_distinction_preserved": True,
                "source_not_naturalized": True,
                "prior_presence_outcome": PRIOR_PRESENCE_OUTCOME,
                "prior_presence_result": PRIOR_PRESENCE_RESULT,
                "admissible_future_route": BOUNDARY_FUTURE_ROUTE_REQUIRED,
            },
        ),
        (
            "candidate_sufficiency_artifact_validation",
            CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
            CANDIDATE_SUFFICIENCY_SHA256,
            {
                "operation_id": CANDIDATE_SUFFICIENCY_OPERATION_ID,
                "outcome": CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED,
                "operation_result": CANDIDATE_SUFFICIENCY_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "refusal_withholding_compatibility": "SATISFIED",
                "operation_basis_complete_and_admitted": True,
                "operation_exhausted": True,
                "candidate_result_posture_count": 1,
                "evaluated_dimension_count": 8,
            },
        ),
        (
            "receiver_attestation_artifact_validation",
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
            RECEIVER_ATTESTATION_SHA256,
            {
                "operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
                "outcome": RECEIVER_ATTESTATION_OUTCOME_REQUIRED,
                "operation_result": RECEIVER_ATTESTATION_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "operation_basis_supplied": True,
                "operation_basis_admitted": True,
                "receiver_attestation_recorded": True,
                "operation_exhausted": True,
                "completed_result_posture_count": 1,
            },
        ),
        (
            "receiver_answerable_receipt_artifact_validation",
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
            RECEIVER_ANSWERABLE_RECEIPT_SHA256,
            {
                "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
                "outcome": RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED,
                "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "selected_attestation_operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
                "operation_basis_supplied": True,
                "operation_basis_admitted": True,
                "receiver_answerable_receipt_present": True,
                "receiver_answerable_receipt_recorded": True,
                "operation_exhausted": True,
                "completed_result_posture_count": 1,
            },
        ),
    )


def _hex_sha256_or_none(value: Any) -> bool:
    return value is None or (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _artifact_validation_valid(
    validation: Any,
    path: Path,
    digest: str,
    standing: Mapping[str, Any],
    *,
    completed_result: bool,
) -> bool:
    if not isinstance(validation, Mapping):
        return False
    expected_keys = set(_empty_json_artifact_validation(path, digest))
    status_fields = (
        "strict_json_validated",
        "artifact_validated",
        "identity_validated",
        "result_validated",
        "completion_and_cardinality_validated",
        "false_locks_validated",
    )
    if (
        set(validation) != expected_keys
        or validation.get("artifact_path") != str(path)
        or validation.get("expected_sha256") != digest
        or not _hex_sha256_or_none(validation.get("observed_sha256"))
        or any(type(validation.get(field)) is not bool for field in status_fields)
        or not isinstance(validation.get("standing"), Mapping)
    ):
        return False
    artifact_validated = validation.get("artifact_validated") is True
    if artifact_validated:
        if (
            validation.get("observed_sha256") != digest
            or any(validation.get(field) is not True for field in status_fields)
            or dict(validation.get("standing", {})) != dict(standing)
        ):
            return False
    elif (
        any(
            validation.get(field) is not False
            for field in status_fields
            if field != "strict_json_validated"
        )
        or dict(validation.get("standing", {}))
    ):
        return False
    return not completed_result or artifact_validated


def _validation_sections_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    completed = _completed_outcome(str(outcome))
    operation = result.get("receiver_originating_modal_fact_evaluation_operation")
    declared = result.get(
        "declared_receiver_originating_modal_fact_evaluation_operation_request"
    )
    specification = result.get("specification_validation")
    declaration = result.get("receiver_originating_declaration_validation")
    atomic = result.get("atomic_operation_basis_posture")
    source = result.get("source_selection_and_carriage_lineage")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, declared, specification, declaration, atomic, source)
    ):
        return False

    expected_metadata = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "boundary_artifact_path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
        "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
        "candidate_sufficiency_artifact_path": str(
            CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_attestation_artifact_path": str(
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_answerable_receipt_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
        ),
    }
    if result.get(
        "receiver_originating_modal_fact_evaluation_operation_metadata"
    ) != expected_metadata:
        return False

    declared_keys = set(_declared_request_posture({}, validated=False))
    if (
        set(declared) != declared_keys
        or any(type(value) is not bool for value in declared.values())
        or (
            completed
            and not all(value is True for value in declared.values())
        )
    ):
        return False

    if (
        set(specification) != set(_empty_specification_validation())
        or specification.get("specification_path")
        != str(GOVERNING_SPECIFICATION_RELATIVE_PATH)
        or not isinstance(specification.get("marker_validation"), Mapping)
        or set(specification.get("marker_validation", {}))
        != {name for name, _ in SPEC_REQUIRED_MARKERS}
        or any(
            type(value) is not bool
            for value in specification.get("marker_validation", {}).values()
        )
        or type(specification.get("specification_validated")) is not bool
        or (
            specification.get("specification_validated") is True
            and not all(
                value is True
                for value in specification.get("marker_validation", {}).values()
            )
        )
        or (completed and specification.get("specification_validated") is not True)
    ):
        return False

    if any(
        not _artifact_validation_valid(
            result.get(key),
            path,
            digest,
            standing,
            completed_result=completed,
        )
        for key, path, digest, standing in _expected_artifact_standings()
    ):
        return False

    expected_declaration_keys = set(_empty_declaration_validation())
    declaration_bool_fields = (
        "strict_utf8_validated",
        "bom_absent",
        "exact_six_unique_records_validated",
        "source_context_records_validated",
        "complete_declaration_body_omitted",
        "declaration_validated",
    )
    fixed_declaration_values = {
        "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
        "declaration_archive_path": str(DECLARATION_ARCHIVE_RELATIVE_PATH),
        "declaration_archive_member": DECLARATION_ARCHIVE_MEMBER,
        "expected_byte_count": DECLARATION_BYTE_COUNT,
        "expected_sha256": DECLARATION_SHA256,
        "archive_sha256_identity": DECLARATION_ARCHIVE_SHA256,
        "candidate_id": DECLARATION_CANDIDATE_ID,
        "source_provenance_reference": DECLARATION_PROVENANCE_REFERENCE,
        "receipt_bundle": DECLARATION_RECEIPT_BUNDLE,
        "receiver_label": DECLARATION_RECEIVER_LABEL,
    }
    if (
        set(declaration) != expected_declaration_keys
        or any(
            declaration.get(field) != expected
            for field, expected in fixed_declaration_values.items()
        )
        or any(
            type(declaration.get(field)) is not bool
            for field in declaration_bool_fields
        )
        or declaration.get("complete_declaration_body_omitted") is not True
        or not _hex_sha256_or_none(declaration.get("observed_sha256"))
        or (
            declaration.get("observed_byte_count") is not None
            and type(declaration.get("observed_byte_count")) is not int
        )
        or not isinstance(declaration.get("matter_relevant_records"), Mapping)
    ):
        return False
    if declaration.get("declaration_validated") is True:
        if (
            declaration.get("observed_byte_count") != DECLARATION_BYTE_COUNT
            or declaration.get("observed_sha256") != DECLARATION_SHA256
            or any(
                declaration.get(field) is not True
                for field in declaration_bool_fields
            )
            or dict(declaration.get("matter_relevant_records", {}))
            != {
                "could_have_been_refused": True,
                "could_have_been_withheld": True,
            }
        ):
            return False
    elif (
        declaration.get("exact_six_unique_records_validated") is not False
        or declaration.get("source_context_records_validated") is not False
        or dict(declaration.get("matter_relevant_records", {}))
    ):
        return False
    if completed and declaration.get("declaration_validated") is not True:
        return False

    atomic_keys = set(_empty_atomic_basis({}))
    atomic_bool_fields = tuple(atomic_keys)
    governed_validation_fields = (
        "specification_validated",
        "boundary_artifact_validated",
        "declaration_validated",
        "candidate_sufficiency_artifact_validated",
        "receiver_attestation_artifact_validated",
        "receiver_answerable_receipt_artifact_validated",
    )
    if (
        set(atomic) != atomic_keys
        or any(type(atomic.get(field)) is not bool for field in atomic_bool_fields)
        or atomic.get("partial_basis_cannot_produce_completed_result") is not True
        or atomic.get("operation_basis_supplied")
        is not operation.get("operation_basis_supplied")
        or atomic.get("operation_basis_admitted") is not completed
        or atomic.get("all_six_governed_files_validated")
        is not all(atomic.get(field) is True for field in governed_validation_fields)
        or (completed and not all(atomic.get(field) is True for field in atomic_keys))
    ):
        return False

    return (
        dict(source) == _source_selection_posture(completed)
        and result.get("prior_presence_preservation_posture")
        == _prior_presence_posture(completed)
        and result.get("lineage_preservation_posture")
        == _canonical_lineage_posture(completed)
        and result.get("omission_posture") == _canonical_omission_posture()
        and result.get(
            "receiver_originating_modal_fact_evaluation_operation_non_meaning"
        )
        == _canonical_non_meaning()
        and result.get("blocked_conversions") == list(BLOCKED_CONVERSIONS)
        and result.get("excluded_condition_posture")
        == _canonical_excluded_condition_posture()
        and result.get(
            "receiver_originating_modal_fact_evaluation_operation_statement"
        )
        == _statement(str(outcome))
        and result.get("what_remains_open") == _what_remains_open(str(outcome))
    )


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    operation = result.get("receiver_originating_modal_fact_evaluation_operation")
    block = result.get("block")
    decision = result.get("operation_decision")
    evaluations = _target_evaluation_values_for_write(result)
    if (
        outcome not in OUTCOME_FAMILY
        or not isinstance(operation, Mapping)
        or not isinstance(block, Mapping)
        or not isinstance(decision, Mapping)
        or evaluations is None
        or type(operation.get("operation_basis_supplied")) is not bool
    ):
        return False
    completed = _completed_outcome(str(outcome))
    if completed:
        if (
            TARGET_EVALUATION_NOT_EVALUATED in evaluations.values()
            or _outcome_from_evaluations(evaluations) != outcome
        ):
            return False
    elif any(
        evaluation != TARGET_EVALUATION_NOT_EVALUATED
        for evaluation in evaluations.values()
    ):
        return False

    expected_result = _operation_result_for_outcome(str(outcome))
    expected_operation = _expected_operation_object(
        str(outcome),
        evaluations,
        basis_supplied=operation.get("operation_basis_supplied") is True,
    )
    expected_support = {
        "receiver_answerable_basis_refusable_supported": (
            evaluations["receiver_answerable_basis_refusable"]
            == TARGET_EVALUATION_SUPPORTED
        ),
        "receiver_answerable_basis_could_have_been_withheld_supported": (
            evaluations["receiver_answerable_basis_could_have_been_withheld"]
            == TARGET_EVALUATION_SUPPORTED
        ),
        "support_is_matter_bound": True,
        "support_is_source_relation_bound": True,
        "support_is_not_reality_wide_establishment": True,
    }
    expected_operation_posture = {
        **_branch_posture(
            str(outcome),
            basis_supplied=operation.get("operation_basis_supplied") is True,
        ),
        "single_use_only": True,
        "source_admissibility_not_repeated": True,
        "operation_exhaustion_is_not_modal_fact_establishment": True,
        "operation_exhaustion_is_not_complete_receiver_answerable_basis": True,
        "operation_exhaustion_is_not_presence": True,
    }
    if outcome == OUTCOME_BLOCKED:
        expected_block = {
            "blocked": True,
            "code": block.get("code"),
            "block_code": block.get("code"),
            "reason": block.get("reason"),
        }
        if (
            block.get("code") not in BLOCK_CODES
            or not isinstance(block.get("reason"), str)
            or not block.get("reason")
        ):
            return False
    else:
        expected_block = {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }
    return (
        dict(operation) == expected_operation
        and result.get("target_condition_evaluations")
        == _target_evaluation_section(evaluations)
        and result.get("target_support_posture") == expected_support
        and result.get("operation_posture") == expected_operation_posture
        and dict(block) == expected_block
        and dict(decision)
        == _decision_for_outcome(
            str(outcome),
            code=expected_block.get("code"),
            reason=expected_block.get("reason"),
        )
        and result.get("operation_result") == expected_result
        and result.get(
            "receiver_originating_modal_fact_evaluation_operation_result"
        )
        == expected_result
        and result.get("completed_modal_fact_evaluation_result_posture_count")
        == int(completed)
        and result.get("admissible_future_route") is None
    )


def _result_valid_for_write(result: Mapping[str, Any]) -> bool:
    summary = result.get("receiver_originating_modal_fact_evaluation_operation_summary")
    return (
        result.get("resolver_module") == RESOLVER_MODULE
        and result.get("result_version") == RESULT_VERSION
        and set(result) == RESULT_SECTIONS
        and result.get("outcome") in OUTCOME_FAMILY
        and _checks_valid(result)
        and _branch_valid(result)
        and _validation_sections_valid(result)
        and _non_claims_valid(result.get("non_claims"))
        and result.get("result_level_non_claims_canonical_false") is True
        and not _contains_prohibited_complete_material(result)
        and summary == _summary_from_result(result)
    )


def build_receiver_originating_modal_fact_evaluation_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic summary for a compatible result."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "summary requires a compatible resolver result"
        )
    return _summary_from_result(result)


def write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid result to the exact canonical path without overwrite."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "WRITE_REFUSED: malformed or inconsistent operation result"
        )
    canonical_target = OUTPUT_ROOT / OUTPUT_FILENAME
    try:
        target = canonical_target if output_path is None else _as_repo_path(output_path)
        if target.resolve() != canonical_target.resolve():
            raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
                "WRITE_REFUSED: output path is not the exact canonical result path"
            )
    except ReceiverOriginatingModalFactEvaluationOperationV0MinError:
        raise
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if OUTPUT_ROOT.name != OUTPUT_ROOT_NAME:
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "WRITE_REFUSED: output root identity mismatch"
        )
    if target.exists():
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "WRITE_REFUSED: canonical result already exists"
        )
    if target.parent.exists() and not target.parent.is_dir():
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "WRITE_REFUSED: canonical output root is not a directory"
        )
    try:
        target.parent.mkdir(exist_ok=True)
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
        raise ReceiverOriginatingModalFactEvaluationOperationV0MinError(
            "WRITE_REFUSED: unable to write canonical operation result"
        ) from exc
    return target
