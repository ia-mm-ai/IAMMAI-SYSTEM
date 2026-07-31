"""Resolve one receiver-originating modal-fact source-admissibility boundary.

The resolver reads only the governing specification, four exact completed
JSON artifacts, one exact declaration surface, and an explicitly supplied
request path.  It may record only whether that declaration is admissible as
source for one later bounded two-condition evaluation consideration.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESOLVER_MODULE = (
    "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min"
)
RESULT_VERSION = "0.1.0"

BOUNDARY_ID = (
    "receiver_originating_modal_fact_source_admissibility_boundary_001"
)
BOUNDARY_TYPE = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY"
)
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_EXACT_RECEIVER_ORIGINATING_DECLARATION_AS_SOURCE_FOR_"
    "TWO_RECEIVER_ALLOCATED_MODAL_FACTS_ONLY"
)

SELECTED_SOURCE_CLASS = "RECEIVER_ORIGINATING_DECLARATION_SOURCE"
SELECTED_RELATION_CLASS = "RECEIVER_ALLOCATED_MODAL_FACT_EVALUATION_RELATION"
SELECTED_MATTER_CLASS = (
    "RECEIVER_ANSWERABLE_BASIS_REFUSABILITY_AND_WITHHOLDABILITY_ONLY"
)
SELECTED_SOURCE_ORIGIN = "RECEIVER_ORIGINATING"
SELECTED_SOURCE_PROVENANCE_POSTURE = (
    "DECLARED_RECEIVER_CUSTODY_REFERENCE_ONLY"
)
SELECTED_SOURCE_ARRIVAL_POSTURE = "CARRIED_ARRIVAL"
REQUIRED_MATTER_TUPLE = (
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
)
MATTER_TUPLE = REQUIRED_MATTER_TUPLE

OUTCOME_ALLOWED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED"
)
OUTCOME_NOT_ALLOWED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_NOT_ALLOWED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED, OUTCOME_BLOCKED)

RESULT_ALLOWED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_ALLOWED"
)
RESULT_NOT_ALLOWED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_NOT_ALLOWED"
)
RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_FAMILY = (RESULT_ALLOWED, RESULT_NOT_ALLOWED, RESULT_NOT_EVALUATED)
BOUNDARY_RESULT_FAMILY = RESULT_FAMILY

ADMISSIBILITY_PASSED = "PASSED"
ADMISSIBILITY_NOT_PASSED = "NOT_PASSED"
ADMISSIBILITY_NOT_EVALUATED = "NOT_EVALUATED"
ADMISSIBILITY_EVALUATION_FAMILY = (
    ADMISSIBILITY_PASSED,
    ADMISSIBILITY_NOT_PASSED,
    ADMISSIBILITY_NOT_EVALUATED,
)

ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_THEN_"
    "SEPARATE_RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_ONLY"
)

DECISION_CODE_ALLOWED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_ALLOWED"
)
DECISION_REASON_ALLOWED = (
    "exact receiver-originating declaration admitted as source for one "
    "bounded two-condition modal-fact evaluation consideration only"
)
DECISION_CODE_NOT_ALLOWED = (
    "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_NOT_ALLOWED"
)
DECISION_REASON_NOT_ALLOWED = (
    "receiver-originating modal-fact evaluation consideration not selected"
)

REPO_ROOT = Path(__file__).resolve().parents[1]

GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_"
    "BOUNDARY_V0_MIN_SPEC.md"
)
PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "presence_re_evaluation_operation_v0_min/"
    "presence_re_evaluation_operation_001__"
    "presence_re_evaluation_operation_v0_min_result.json"
)
DECLARATION_SURFACE_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001/extracted/"
    "receiver_attestation_001/freely_given_statement.txt"
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
    "receiver_answerable_receipt_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min_result.json"
)
DECLARATION_ARCHIVE_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001/original_zip/"
    "receiver_attestation_001.zip"
)
DECLARATION_ARCHIVE_MEMBER = (
    "receiver_attestation_001/freely_given_statement.txt"
)

GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SPECIFICATION_PATH
PRIOR_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT / PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
)
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

CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_originating_modal_fact_source_admissibility_boundary_v0_min"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "receiver_originating_modal_fact_source_admissibility_boundary_001__"
    "receiver_originating_modal_fact_source_admissibility_boundary_"
    "v0_min_result.json"
)

DECLARATION_BYTE_COUNT = 207
DECLARATION_SHA256 = (
    "9c1aeb888cd182fdbce789e1bb191f5778712f82483d7eca1334800dac4dd3eb"
)
DECLARATION_ARCHIVE_SHA256 = (
    "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c"
)
DECLARATION_CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
DECLARATION_PROVENANCE_REFERENCE = (
    "declared://receiver-custody/IAMMAI-RECEIVER/"
    "receiver_attestation_001"
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

PRIOR_OPERATION_SHA256 = (
    "fa3f05965de18382b48a37d54abeb04ed4e3d4383b8e75c11ccaa1ca07c15776"
)
PRIOR_OPERATION_RESOLVER_MODULE = (
    "resolve_presence_re_evaluation_operation_v0_min"
)
PRIOR_OPERATION_OUTCOME_REQUIRED = (
    "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS"
)
PRIOR_OPERATION_RESULT_REQUIRED = "REQUIRES_RECEIVER_ANSWERABLE_BASIS"
PRIOR_OPERATION_PASSED_CHECK_COUNT = 409

CANDIDATE_SUFFICIENCY_SHA256 = (
    "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4"
)
CANDIDATE_SUFFICIENCY_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "candidate_sufficiency_operation_v0_min"
)
CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "CANDIDATE_SUFFICIENCY_OPERATION_RECORDED"
)
CANDIDATE_SUFFICIENCY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
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

RECEIVER_ATTESTATION_SHA256 = (
    "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9"
)
RECEIVER_ATTESTATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)
RECEIVER_ATTESTATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_RECORDED"
)
RECEIVER_ATTESTATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
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
RECEIVER_ATTESTATION_PASSED_CHECK_COUNT = 160

RECEIVER_ANSWERABLE_RECEIPT_SHA256 = (
    "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb"
)
RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min"
)
RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE = (
    "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
    "RECEIVER_ATTESTATION_RESULT_ONLY"
)
RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT = 357

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
    "truth_created",
    "standing_created",
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
        "source_admissibility_boundary_permission_created"
    ),
    (
        "reusable_receiver_originating_modal_fact_"
        "source_admissibility_route_created"
    ),
    (
        "same_receiver_originating_modal_fact_"
        "source_admissibility_boundary_rerun_authorized"
    ),
    (
        "automatic_receiver_originating_modal_fact_"
        "source_admissibility_boundary_retry_created"
    ),
    (
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_debt_created"
    ),
    (
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_obligation_created"
    ),
    "scheduled_receiver_originating_modal_fact_evaluation_created",
    "automatic_next_step_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
)

OMISSION_POSTURE_FIELDS = (
    "complete_prior_operation_artifact_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_material_omitted",
    "complete_receiver_attestation_artifact_omitted",
    "complete_receiver_answerable_receipt_artifact_omitted",
    "complete_bounded_capture_signal_bodies_omitted",
    "complete_declaration_body_omitted",
    "archive_bytes_omitted",
    "alternative_declarations_omitted",
    "alternative_artifacts_omitted",
    "unrelated_receiver_side_material_omitted",
)

LINEAGE_PRESERVATION_FIELDS = (
    "selected_source_remains_receiver_originating",
    "source_relation_remains_legible",
    "declared_provenance_reference_remains_legible",
    "carried_arrival_remains_non_native",
    "custody_and_jurisdiction_distinction_preserved_without_custody_proof",
    "prior_intake_and_admission_chronology_preserved",
    "prior_candidate_sufficiency_remains_limited_to_original_matter",
    "prior_receiver_attestation_result_preserved",
    "prior_receiver_answerable_receipt_result_preserved",
    "prior_presence_requires_basis_result_preserved",
    (
        "no_prior_artifact_repaired_invalidated_superseded_"
        "normalized_replaced_or_overwritten"
    ),
    "source_not_naturalized",
    "native_standing_not_created",
    "jurisdiction_not_collapsed",
    "contaminated_lineage_unchanged",
)

NON_MEANING_FIELDS = (
    "prior_lawful_requires_basis_result_is_not_failure",
    "candidate_sufficiency_is_not_modal_fact_establishment",
    "receipt_is_not_source_authority",
    "admissible_declaration_is_not_true_declaration",
    "admissible_declaration_is_not_authoritative_declaration",
    "source_admissibility_consideration_is_not_source_use",
    "source_use_is_not_modal_fact_evaluation",
    "modal_fact_evaluation_is_not_modal_fact_establishment",
    "modal_fact_establishment_is_not_presence",
    "refusability_is_not_actual_refusal",
    "could_have_been_withheld_is_not_actual_withholding",
    "declared_freedom_posture_is_not_universal_or_metaphysical_freedom",
    "boundary_exhaustion_is_not_standing",
    "open_does_not_mean_next",
    "not_allowed_is_not_declaration_false",
    "not_allowed_is_not_receiver_lacked_freedom",
    "not_allowed_is_not_refusal_or_withholding_impossible",
    "not_allowed_is_not_source_inadmissible_for_every_relation",
    "not_allowed_is_not_presence_denied",
    "not_allowed_is_not_debt_or_obligation",
)

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

BLOCKED_CONVERSIONS = (
    "contact_to_jurisdictional_belonging",
    "receipt_or_preservation_to_source_admissibility",
    "prior_admission_to_new_matter_fit",
    "candidate_sufficiency_to_modal_fact_truth",
    "declaration_to_established_refusability_or_withholdability",
    "declaration_to_receiver_freedom",
    "admissible_source_to_authoritative_source",
    "carried_arrival_to_native_standing",
    "source_use_to_standing_or_presence",
    (
        "boundary_result_to_repeat_reusable_route_rerun_retry_debt_"
        "obligation_scheduled_work_or_automatic_next"
    ),
    (
        "source_admissibility_boundary_to_repair_or_"
        "contaminated_lineage_validation"
    ),
)

WHAT_REMAINS_OPEN = (
    "receiver-originating modal-fact source-admissibility boundary tests",
    "receiver-originating modal-fact source-admissibility boundary request",
    "receiver-originating modal-fact source-admissibility boundary live result",
    (
        "receiver-originating modal-fact source-admissibility boundary "
        "terminal summary"
    ),
    "receiver-originating modal-fact evaluation operation specification",
    "receiver-originating modal-fact evaluation operation resolver",
    "receiver-originating modal-fact evaluation operation tests",
    "receiver-originating modal-fact evaluation operation request",
    "receiver-originating modal-fact evaluation operation live result",
    "receiver-originating modal-fact evaluation operation terminal summary",
    "actual evaluation of receiver_answerable_basis_refusable",
    (
        "actual evaluation of "
        "receiver_answerable_basis_could_have_been_withheld"
    ),
    "source-body-verifiable integrity conditions",
    "receiver-answerable-basis successor operation",
    "later presence re-evaluation",
    "presence support, authorization, establishment, and recording",
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
)

SPEC_REQUIRED_MARKERS = (
    (
        "title",
        "# Receiver-Originating Modal Fact Source Admissibility "
        "Boundary V0 Minimum Specification",
    ),
    ("identity_section", "## 2. Boundary Identity, Classes, and Matter"),
    (
        "boundary_id",
        "receiver_originating_modal_fact_source_admissibility_boundary_id = "
        + BOUNDARY_ID,
    ),
    ("boundary_type", BOUNDARY_TYPE),
    ("boundary_scope", BOUNDARY_SCOPE),
    ("source_class", SELECTED_SOURCE_CLASS),
    ("relation_class", SELECTED_RELATION_CLASS),
    ("matter_class", SELECTED_MATTER_CLASS),
    ("governing_law", "## 3. Governing Law and Non-Collapse"),
    ("prior_standing", "## 4. Exact Prior Requires-Basis Standing"),
    ("prior_artifact", str(PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH)),
    ("declaration_section", "## 5. Exact Receiver-Originating Declaration Source"),
    ("declaration_path", str(DECLARATION_SURFACE_RELATIVE_PATH)),
    ("declaration_digest", DECLARATION_SHA256),
    ("declaration_refusable", "could_have_been_refused=true"),
    ("declaration_withholdable", "could_have_been_withheld=true"),
    ("carriage_lineage", "## 6. Exact Completed Carriage Lineage"),
    ("candidate_artifact", str(CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH)),
    ("attestation_artifact", str(RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH)),
    (
        "receipt_artifact",
        str(RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH),
    ),
    ("question", "## 7. Boundary Question and Answer"),
    ("three_parts", "## 8. Three-Part Admissibility Evaluation"),
    ("source_admissibility", "### 8.1 Source admissibility"),
    ("scope_admissibility", "### 8.2 Scope and matter admissibility"),
    ("transition_admissibility", "### 8.3 Transition admissibility"),
    ("outcome_family", "## 9. Outcome and Consideration Families"),
    ("outcome_allowed", OUTCOME_ALLOWED),
    ("outcome_not_allowed", OUTCOME_NOT_ALLOWED),
    ("outcome_blocked", OUTCOME_BLOCKED),
    ("result_allowed", RESULT_ALLOWED),
    ("result_not_allowed", RESULT_NOT_ALLOWED),
    ("decision_rules", "## 10. Canonical Request and Decision Rules"),
    ("branch_posture", "## 11. Boundary Recording, Exhaustion, and Future Route"),
    ("future_route", ADMISSIBLE_FUTURE_ROUTE),
    ("distinctions", "## 12. Constitutional Distinctions"),
    ("read_posture", "## 13. Read and Omission Posture"),
    ("non_claims", "## 14. Required False Non-Claims"),
    ("blocked_conversions", "## 15. Blocked Conversions and Separate Conditions"),
    ("lineage", "## 16. Lineage Preservation and What Remains Open"),
    ("open_not_next", "Open does not mean next."),
    ("closing_lock", "## 17. Closing Lock"),
)
SPEC_MARKERS = tuple(marker for _, marker in SPEC_REQUIRED_MARKERS)

PROHIBITED_DIRECT_REQUEST_FIELDS = frozenset(
    {
        "outcome",
        "boundary_result",
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result"
        ),
        "decision_code",
        "decision_reason",
        "source_admissibility_evaluation",
        "scope_and_matter_admissibility_evaluation",
        "transition_admissibility_evaluation",
        "receiver_answerable_basis_refusable",
        "receiver_answerable_basis_could_have_been_withheld",
        "receiver_answerable_basis_refusable_established",
        (
            "receiver_answerable_basis_"
            "could_have_been_withheld_established"
        ),
        "modal_fact_evaluation_result",
        "presence_result",
        "downstream_operation_result",
        "declaration_content",
        "declaration_body",
        "semantic_payload",
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
        "SPECIFICATION_REFERENCE_MISSING",
        "SPECIFICATION_MARKER_MISSING",
        "PRIOR_OPERATION_ARTIFACT_MISSING",
        "PRIOR_OPERATION_ARTIFACT_UNREADABLE",
        "PRIOR_OPERATION_ARTIFACT_DIGEST_MISMATCH",
        "PRIOR_OPERATION_ARTIFACT_DUPLICATE_KEYED",
        "PRIOR_OPERATION_ARTIFACT_NOT_PARSEABLE",
        "PRIOR_OPERATION_ARTIFACT_NOT_MAPPING",
        "PRIOR_OPERATION_ARTIFACT_SECTION_MISSING",
        "PRIOR_OPERATION_METADATA_MISMATCH",
        "PRIOR_OPERATION_FAILED_CHECKS_PRESENT",
        "PRIOR_OPERATION_BLOCKED",
        "PRIOR_OPERATION_RESULT_MISMATCH",
        "PRIOR_OPERATION_POSTURE_MISMATCH",
        "DECLARATION_SURFACE_MISSING",
        "DECLARATION_SURFACE_UNREADABLE",
        "DECLARATION_BYTE_COUNT_MISMATCH",
        "DECLARATION_DIGEST_MISMATCH",
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
        "CARRIAGE_LINEAGE_MISMATCH",
        "SOURCE_ADMISSIBILITY_NOT_PASSED",
        "SCOPE_AND_MATTER_ADMISSIBILITY_NOT_PASSED",
        "TRANSITION_ADMISSIBILITY_NOT_PASSED",
        "WRITE_REFUSED",
    }
)

RESULT_SECTIONS = frozenset(
    {
        "receiver_originating_modal_fact_source_admissibility_boundary_metadata",
        "declared_receiver_originating_modal_fact_source_admissibility_boundary_request",
        "specification_validation",
        "prior_operation_artifact_validation",
        "receiver_originating_declaration_validation",
        "candidate_sufficiency_artifact_validation",
        "receiver_attestation_artifact_validation",
        "receiver_answerable_receipt_artifact_validation",
        "source_selection_and_carriage_lineage",
        "admissibility_evaluations",
        "lineage_preservation_posture",
        "excluded_condition_posture",
        "boundary_decision",
        "block",
        "boundary_posture",
        "receiver_originating_modal_fact_source_admissibility_boundary",
        "receiver_originating_modal_fact_source_admissibility_boundary_checks",
        "receiver_originating_modal_fact_source_admissibility_boundary_statement",
        "receiver_originating_modal_fact_source_admissibility_boundary_non_meaning",
        "omission_posture",
        "blocked_conversions",
        "admissible_future_route",
        "what_remains_open",
        "non_claims",
        "result_level_non_claims_canonical_false",
        "outcome",
        "boundary_result",
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result"
        ),
        "completed_consideration_posture_count",
        "failed_check_count",
        "passed_check_count",
        "resolver_module",
        "result_version",
        "receiver_originating_modal_fact_source_admissibility_boundary_summary",
    }
)


class ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
    Exception
):
    """Raised for invalid request paths and refused result writes."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when strict JSON contains a repeated object member."""


class _NonFiniteJsonNumberError(ValueError):
    """Raised when JSON uses NaN or infinity extensions."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _reject_non_finite_json_number(value: str) -> Any:
    raise _NonFiniteJsonNumberError(value)


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {field: True for field in OMISSION_POSTURE_FIELDS}


def _canonical_lineage_posture() -> dict[str, bool]:
    return {field: True for field in LINEAGE_PRESERVATION_FIELDS}


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _canonical_excluded_condition_posture() -> dict[str, Any]:
    return {
        "excluded_condition_evaluation_performed": False,
        "excluded_conditions_not_evaluated": True,
        "condition_evaluations": {
            field: ADMISSIBILITY_NOT_EVALUATED
            for field in EXCLUDED_CONDITIONS
        },
    }


def _identity_request_values() -> dict[str, Any]:
    return {
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_id"
        ): BOUNDARY_ID,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_type"
        ): BOUNDARY_TYPE,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_version"
        ): BOUNDARY_VERSION,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_scope"
        ): BOUNDARY_SCOPE,
        (
            "governing_receiver_originating_modal_fact_"
            "source_admissibility_boundary_specification_path"
        ): str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "prior_presence_re_evaluation_operation_artifact_path": str(
            PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
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
        "selected_receiver_originating_declaration_sha256": (
            DECLARATION_SHA256
        ),
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
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_provenance_posture": (
            SELECTED_SOURCE_PROVENANCE_POSTURE
        ),
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "selected_matter": list(REQUIRED_MATTER_TUPLE),
    }


def _new_canonical_request() -> dict[str, Any]:
    return {
        **_identity_request_values(),
        "receiver_originating_modal_fact_evaluation_consideration_selected": (
            True
        ),
        "declared_non_claims": _canonical_non_claims(),
    }


def build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request(
) -> dict[str, Any]:
    """Return one fresh canonical source-admissibility boundary request."""
    return copy.deepcopy(_new_canonical_request())


def build_declared_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return a fresh canonical request with every override kept visible."""
    request = _new_canonical_request()
    request.update(copy.deepcopy(overrides))
    return request


def _canonical_request_keys() -> set[str]:
    return {
        *_identity_request_values(),
        "receiver_originating_modal_fact_evaluation_consideration_selected",
        "declared_non_claims",
    }


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


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    payload, error = _read_bytes(value)
    if error is not None or payload is None:
        return None, error
    try:
        return payload.decode("utf-8", errors="strict"), None
    except UnicodeDecodeError:
        return None, "invalid_utf8"


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


def _exact_bool(value: Any, expected: bool) -> bool:
    return type(value) is bool and value is expected


def _exact_int(value: Any, expected: int) -> bool:
    return type(value) is int and value == expected


def _canonical_false_mapping(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and bool(value)
        and all(type(item) is bool and item is False for item in value.values())
    )


def _non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _exact_true_mapping(value: Any, fields: tuple[str, ...]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(fields)
        and all(value.get(field) is True for field in fields)
    )


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
    *,
    expected: Any = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "passed": passed}
    if expected is not None:
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
    expected: Any = None,
) -> tuple[str | None, str | None]:
    checks.append(_check(name, condition, code, expected=expected))
    return (None, None) if condition else (code, reason)


def _add_failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> None:
    checks.append(_check(name, False, code))


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    direct = set(request).intersection(PROHIBITED_DIRECT_REQUEST_FIELDS)
    if direct:
        _add_failure(
            checks,
            "request.direct_result_or_semantic_preclaim",
            "RESULT_POSTURE_PRECLAIMED",
        )
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "request contains a result, semantic payload, or downstream preclaim",
        )

    canonical_keys = _canonical_request_keys()
    if canonical_keys.difference(request):
        _add_failure(checks, "request.schema", "REQUEST_FIELD_MISSING")
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    if set(request).difference(canonical_keys):
        _add_failure(checks, "request.schema", "REQUEST_UNKNOWN_FIELD")
        return "REQUEST_UNKNOWN_FIELD", "request contains unknown fields"
    checks.append(_check("request.schema", True))

    for field, expected in _identity_request_values().items():
        actual = request.get(field)
        if field == "selected_matter":
            valid = (
                isinstance(actual, Sequence)
                and not isinstance(actual, (str, bytes, bytearray))
                and list(actual) == list(REQUIRED_MATTER_TUPLE)
                and len(actual) == len(REQUIRED_MATTER_TUPLE)
            )
            code = "REQUEST_MATTER_MISMATCH"
        elif type(expected) is bool:
            valid = _exact_bool(actual, expected)
            code = "REQUEST_VALUE_MISMATCH"
        elif type(expected) is int:
            valid = _exact_int(actual, expected)
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

    selected = request.get(
        "receiver_originating_modal_fact_evaluation_consideration_selected"
    )
    code, reason = _require(
        checks,
        (
            "request.receiver_originating_modal_fact_"
            "evaluation_consideration_selected"
        ),
        type(selected) is bool,
        "REQUEST_BOOLEAN_REQUIRED",
        "evaluation consideration selection must be an exact Boolean",
        expected="boolean",
    )
    if code is not None:
        return code, reason

    if not _non_claims_valid(request.get("declared_non_claims")):
        _add_failure(
            checks,
            "request.declared_non_claims",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims must be the exact canonical false set",
        )
    checks.append(_check("request.declared_non_claims", True))
    return None, None


def _empty_specification_validation() -> dict[str, Any]:
    return {
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "marker_validation": {
            name: False for name, _ in SPEC_REQUIRED_MARKERS
        },
        "specification_validated": False,
    }


def _validate_specification(
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_specification_validation()
    text, error = _read_text(GOVERNING_SPECIFICATION_RELATIVE_PATH)
    if error is not None or text is None:
        _add_failure(
            checks,
            "specification.reference",
            "SPECIFICATION_REFERENCE_MISSING",
        )
        return (
            "SPECIFICATION_REFERENCE_MISSING",
            "governing source-admissibility specification is unavailable",
            validation,
        )
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
    path: Path,
    expected_sha256: str,
    prefix: str,
    code_prefix: str,
    checks: list[dict[str, Any]],
    validation: dict[str, Any],
) -> tuple[
    str | None,
    str | None,
    Mapping[str, Any] | None,
]:
    payload, error = _read_bytes(path)
    if error == "not_a_file":
        code = code_prefix + "_ARTIFACT_MISSING"
        _add_failure(checks, prefix + ".reference", code)
        return code, prefix + " artifact is unavailable", None
    if error is not None or payload is None:
        code = code_prefix + "_ARTIFACT_UNREADABLE"
        _add_failure(checks, prefix + ".reference", code)
        return code, prefix + " artifact is unreadable", None

    observed_sha256 = _sha256(payload)
    validation["observed_sha256"] = observed_sha256
    code, reason = _require(
        checks,
        prefix + ".sha256",
        observed_sha256 == expected_sha256,
        code_prefix + "_ARTIFACT_DIGEST_MISMATCH",
        prefix + " artifact digest does not match exact standing",
        expected=expected_sha256,
    )
    if code is not None:
        return code, reason, None

    artifact, parse_error = _parse_json_bytes(payload)
    if parse_error == "duplicate_key":
        code = code_prefix + "_ARTIFACT_DUPLICATE_KEYED"
        _add_failure(checks, prefix + ".strict_json", code)
        return code, prefix + " artifact contains duplicate JSON keys", None
    if parse_error is not None:
        code = code_prefix + "_ARTIFACT_NOT_PARSEABLE"
        _add_failure(checks, prefix + ".strict_json", code)
        return code, prefix + " artifact is not strict UTF-8 JSON", None
    if not isinstance(artifact, Mapping):
        code = code_prefix + "_ARTIFACT_NOT_MAPPING"
        _add_failure(checks, prefix + ".mapping", code)
        return code, prefix + " artifact is not a mapping", None
    checks.append(_check(prefix + ".strict_json_mapping", True))
    validation["strict_json_validated"] = True
    return None, None, artifact


def _empty_prior_validation() -> dict[str, Any]:
    return _empty_json_artifact_validation(
        PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH,
        PRIOR_OPERATION_SHA256,
    )


def _validate_prior_operation_artifact(
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_prior_validation()
    code, reason, artifact = _load_exact_json_artifact(
        path=PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH,
        expected_sha256=PRIOR_OPERATION_SHA256,
        prefix="prior_operation",
        code_prefix="PRIOR_OPERATION",
        checks=checks,
        validation=validation,
    )
    if code is not None or artifact is None:
        return code, reason, validation

    operation = artifact.get("presence_re_evaluation_operation")
    summary = artifact.get("presence_re_evaluation_operation_summary")
    condition_evaluations = artifact.get("condition_evaluations")
    block = artifact.get("block")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, condition_evaluations, block)
    ):
        code = "PRIOR_OPERATION_ARTIFACT_SECTION_MISSING"
        _add_failure(checks, "prior_operation.sections", code)
        return (
            code,
            "prior operation artifact lacks canonical compact sections",
            validation,
        )
    checks.append(_check("prior_operation.sections", True))

    metadata_expectations = (
        ("resolver_module", artifact.get("resolver_module"), PRIOR_OPERATION_RESOLVER_MODULE),
        ("result_version", artifact.get("result_version"), RESULT_VERSION),
        ("outcome", artifact.get("outcome"), PRIOR_OPERATION_OUTCOME_REQUIRED),
        (
            "operation_result",
            artifact.get("presence_re_evaluation_operation_result"),
            PRIOR_OPERATION_RESULT_REQUIRED,
        ),
        (
            "successor_presence_result",
            artifact.get("successor_presence_result"),
            PRIOR_OPERATION_RESULT_REQUIRED,
        ),
        ("failed_check_count", artifact.get("failed_check_count"), 0),
        (
            "passed_check_count",
            artifact.get("passed_check_count"),
            PRIOR_OPERATION_PASSED_CHECK_COUNT,
        ),
    )
    for name, actual, expected in metadata_expectations:
        if type(expected) is int:
            valid = _exact_int(actual, expected)
            failure = (
                "PRIOR_OPERATION_FAILED_CHECKS_PRESENT"
                if name == "failed_check_count"
                else "PRIOR_OPERATION_METADATA_MISMATCH"
            )
        else:
            valid = actual == expected
            failure = (
                "PRIOR_OPERATION_RESULT_MISMATCH"
                if "result" in name
                else "PRIOR_OPERATION_METADATA_MISMATCH"
            )
        code, reason = _require(
            checks,
            "prior_operation." + name,
            valid,
            failure,
            "prior operation standing mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "prior_operation.blocked",
        _exact_bool(block.get("blocked"), False),
        "PRIOR_OPERATION_BLOCKED",
        "prior operation artifact is blocked or lacks exact false posture",
        expected=False,
    )
    if code is not None:
        return code, reason, validation

    true_postures = (
        "operation_basis_admitted",
        "presence_re_evaluation_performed",
        "presence_re_evaluation_operation_recorded",
        "presence_re_evaluation_operation_result_recorded",
        "presence_re_evaluation_operation_exhausted",
    )
    for field in true_postures:
        code, reason = _require(
            checks,
            "prior_operation.true_posture." + field,
            _exact_bool(operation.get(field), True),
            "PRIOR_OPERATION_POSTURE_MISMATCH",
            "required prior operation posture is not exact true: " + field,
            expected=True,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "prior_operation.completed_successor_result_posture_count",
        _exact_int(
            operation.get("completed_successor_result_posture_count"),
            1,
        )
        and _exact_int(
            artifact.get("completed_successor_result_posture_count"),
            1,
        ),
        "PRIOR_OPERATION_POSTURE_MISMATCH",
        "prior operation must preserve one completed successor posture",
        expected=1,
    )
    if code is not None:
        return code, reason, validation

    for field in (
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
    ):
        code, reason = _require(
            checks,
            "prior_operation.false_posture." + field,
            _exact_bool(operation.get(field), False),
            "PRIOR_OPERATION_POSTURE_MISMATCH",
            "prior operation presence posture must remain false: " + field,
            expected=False,
        )
        if code is not None:
            return code, reason, validation

    if artifact.get("admissible_future_route") is not None:
        _add_failure(
            checks,
            "prior_operation.admissible_future_route",
            "PRIOR_OPERATION_POSTURE_MISMATCH",
        )
        return (
            "PRIOR_OPERATION_POSTURE_MISMATCH",
            "prior operation future route must remain null",
            validation,
        )
    checks.append(
        _check(
            "prior_operation.admissible_future_route",
            True,
            expected="null",
        )
    )

    evaluations = {
        "receiver_attested": "SATISFIED",
        "receiver_answerable_receipt_present": "SATISFIED",
        "receiver_answerable_basis_refusable": "REQUIRES_BASIS",
        (
            "receiver_answerable_basis_could_have_been_withheld"
        ): "REQUIRES_BASIS",
    }
    for field, expected in evaluations.items():
        item = condition_evaluations.get(field)
        valid = (
            isinstance(item, Mapping)
            and item.get("evaluation") == expected
        )
        code, reason = _require(
            checks,
            "prior_operation.condition." + field,
            valid,
            "PRIOR_OPERATION_POSTURE_MISMATCH",
            "prior operation condition mismatch: " + field,
            expected=expected,
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
                "outcome": PRIOR_OPERATION_OUTCOME_REQUIRED,
                "operation_result": PRIOR_OPERATION_RESULT_REQUIRED,
                "failed_check_count": 0,
                "passed_check_count": PRIOR_OPERATION_PASSED_CHECK_COUNT,
                "operation_basis_admitted": True,
                "presence_re_evaluation_performed": True,
                "presence_re_evaluation_operation_exhausted": True,
                "completed_successor_result_posture_count": 1,
                "admissible_future_route": None,
                "presence_supported": False,
                "presence_authorized": False,
                "presence_established": False,
                "presence_recorded": False,
                "receiver_attested": "SATISFIED",
                "receiver_answerable_receipt_present": "SATISFIED",
                "receiver_answerable_basis_refusable": "REQUIRES_BASIS",
                (
                    "receiver_answerable_basis_"
                    "could_have_been_withheld"
                ): "REQUIRES_BASIS",
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
        "exact_six_unique_records_validated": False,
        "matter_relevant_records": {},
        "complete_declaration_body_omitted": True,
        "declaration_validated": False,
    }


def _validate_declaration_surface(
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_declaration_validation()
    payload, error = _read_bytes(DECLARATION_SURFACE_RELATIVE_PATH)
    if error == "not_a_file":
        _add_failure(
            checks,
            "declaration.reference",
            "DECLARATION_SURFACE_MISSING",
        )
        return (
            "DECLARATION_SURFACE_MISSING",
            "exact receiver-originating declaration surface is unavailable",
            validation,
        )
    if error is not None or payload is None:
        _add_failure(
            checks,
            "declaration.reference",
            "DECLARATION_SURFACE_UNREADABLE",
        )
        return (
            "DECLARATION_SURFACE_UNREADABLE",
            "exact receiver-originating declaration surface is unreadable",
            validation,
        )

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

    observed_sha256 = _sha256(payload)
    validation["observed_sha256"] = observed_sha256
    code, reason = _require(
        checks,
        "declaration.sha256",
        observed_sha256 == DECLARATION_SHA256,
        "DECLARATION_DIGEST_MISMATCH",
        "declaration digest does not match exact identity",
        expected=DECLARATION_SHA256,
    )
    if code is not None:
        return code, reason, validation

    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        _add_failure(
            checks,
            "declaration.utf8",
            "DECLARATION_UTF8_INVALID",
        )
        return (
            "DECLARATION_UTF8_INVALID",
            "declaration surface is not strict UTF-8",
            validation,
        )
    validation["strict_utf8_validated"] = True
    checks.append(_check("declaration.utf8", True))

    records: dict[str, str] = {}
    lines = text.splitlines()
    if len(lines) != len(REQUIRED_DECLARATION_RECORDS):
        _add_failure(
            checks,
            "declaration.record_count",
            "DECLARATION_RECORD_SET_MISMATCH",
        )
        return (
            "DECLARATION_RECORD_SET_MISMATCH",
            "declaration must contain exactly six records",
            validation,
        )
    for index, line in enumerate(lines):
        if line.count("=") != 1:
            _add_failure(
                checks,
                "declaration.record." + str(index),
                "DECLARATION_RECORD_MALFORMED",
            )
            return (
                "DECLARATION_RECORD_MALFORMED",
                "declaration record is not one key=value pair",
                validation,
            )
        key, value = line.split("=", 1)
        if not key or not value:
            _add_failure(
                checks,
                "declaration.record." + str(index),
                "DECLARATION_RECORD_MALFORMED",
            )
            return (
                "DECLARATION_RECORD_MALFORMED",
                "declaration record has an empty key or value",
                validation,
            )
        if key in records:
            _add_failure(
                checks,
                "declaration.record." + key,
                "DECLARATION_RECORD_DUPLICATE",
            )
            return (
                "DECLARATION_RECORD_DUPLICATE",
                "declaration surface contains a duplicate key",
                validation,
            )
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

    validation.update(
        {
            "exact_six_unique_records_validated": True,
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
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_candidate_validation()
    code, reason, artifact = _load_exact_json_artifact(
        path=CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
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
        "receiver_side_answerable_basis_"
        "candidate_sufficiency_operation_summary"
    )
    detail = artifact.get("operation_result_detail")
    dimensions = artifact.get(
        "receiver_side_answerable_basis_"
        "candidate_sufficiency_operation_dimensions"
    )
    block = artifact.get("block")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, detail, dimensions, block)
    ):
        code = "CANDIDATE_SUFFICIENCY_ARTIFACT_SECTION_MISSING"
        _add_failure(checks, "candidate_sufficiency.sections", code)
        return (
            code,
            "candidate sufficiency artifact lacks canonical compact sections",
            validation,
        )
    checks.append(_check("candidate_sufficiency.sections", True))

    metadata_expectations = (
        (
            "resolver_module",
            artifact.get("resolver_module"),
            CANDIDATE_SUFFICIENCY_RESOLVER_MODULE,
        ),
        ("result_version", artifact.get("result_version"), RESULT_VERSION),
        (
            "outcome",
            artifact.get("outcome"),
            CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED,
        ),
        ("failed_check_count", artifact.get("failed_check_count"), 0),
        (
            "passed_check_count",
            artifact.get("passed_check_count"),
            CANDIDATE_SUFFICIENCY_PASSED_CHECK_COUNT,
        ),
    )
    for name, actual, expected in metadata_expectations:
        valid = (
            _exact_int(actual, expected)
            if type(expected) is int
            else actual == expected
        )
        failure = (
            "CANDIDATE_SUFFICIENCY_FAILED_CHECKS_PRESENT"
            if name == "failed_check_count"
            else "CANDIDATE_SUFFICIENCY_METADATA_MISMATCH"
        )
        code, reason = _require(
            checks,
            "candidate_sufficiency." + name,
            valid,
            failure,
            "candidate sufficiency metadata mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "candidate_sufficiency.blocked",
        _exact_bool(block.get("blocked"), False),
        "CANDIDATE_SUFFICIENCY_BLOCKED",
        "candidate sufficiency artifact is blocked",
        expected=False,
    )
    if code is not None:
        return code, reason, validation

    identity_expectations = (
        ("operation_id", CANDIDATE_SUFFICIENCY_OPERATION_ID),
        ("operation_type", CANDIDATE_SUFFICIENCY_OPERATION_TYPE),
        ("operation_version", RESULT_VERSION),
        ("operation_scope", CANDIDATE_SUFFICIENCY_OPERATION_SCOPE),
        ("receiver_side_answerable_basis_candidate_id", DECLARATION_CANDIDATE_ID),
    )
    for field, expected in identity_expectations:
        code, reason = _require(
            checks,
            "candidate_sufficiency.identity." + field,
            operation.get(field) == expected,
            "CANDIDATE_SUFFICIENCY_IDENTITY_MISMATCH",
            "candidate sufficiency identity mismatch: " + field,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    result_locations = (
        operation.get("operation_result"),
        operation.get("candidate_sufficiency_operation_result"),
        operation.get(
            "receiver_side_answerable_basis_"
            "candidate_sufficiency_operation_result"
        ),
        summary.get("operation_result"),
        detail.get("operation_result"),
    )
    code, reason = _require(
        checks,
        "candidate_sufficiency.operation_result",
        all(
            value == CANDIDATE_SUFFICIENCY_RESULT_REQUIRED
            for value in result_locations
        ),
        "CANDIDATE_SUFFICIENCY_RESULT_MISMATCH",
        "candidate sufficiency result does not match exact sufficient result",
        expected=CANDIDATE_SUFFICIENCY_RESULT_REQUIRED,
    )
    if code is not None:
        return code, reason, validation

    true_postures = (
        "sufficiency_basis_supplied",
        "sufficiency_basis_complete",
        "atomic_sufficiency_basis_gate_passed",
        "candidate_sufficiency_decided",
        "candidate_sufficiency_established",
        "receiver_side_answerable_basis_candidate_sufficient",
        "candidate_sufficiency_operation_recorded",
        "candidate_sufficiency_operation_result_recorded",
        "candidate_sufficiency_operation_exhausted",
    )
    for field in true_postures:
        code, reason = _require(
            checks,
            "candidate_sufficiency.true_posture." + field,
            _exact_bool(operation.get(field), True),
            "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH",
            "candidate sufficiency posture is not exact true: " + field,
            expected=True,
        )
        if code is not None:
            return code, reason, validation
    for field in (
        "candidate_indeterminacy_established",
        "candidate_insufficiency_established",
        "receiver_side_answerable_basis_candidate_indeterminate",
        "receiver_side_answerable_basis_candidate_insufficient",
        "partial_evaluation_recorded",
    ):
        code, reason = _require(
            checks,
            "candidate_sufficiency.false_posture." + field,
            _exact_bool(operation.get(field), False),
            "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH",
            "candidate sufficiency false lock is not exact false: " + field,
            expected=False,
        )
        if code is not None:
            return code, reason, validation

    dimensions_valid = (
        set(dimensions) == set(REQUIRED_SUFFICIENCY_DIMENSIONS)
        and all(
            isinstance(dimensions.get(field), Mapping)
            and dimensions[field].get("dimension_result") == "SATISFIED"
            and dimensions[field].get("dimension_evaluated") is True
            and dimensions[field].get("dimension_established") is True
            for field in REQUIRED_SUFFICIENCY_DIMENSIONS
        )
        and summary.get("dimension_results", {}).get(
            "refusal_withholding_compatibility"
        )
        == "SATISFIED"
    )
    code, reason = _require(
        checks,
        "candidate_sufficiency.dimensions",
        dimensions_valid,
        "CANDIDATE_SUFFICIENCY_POSTURE_MISMATCH",
        "candidate sufficiency dimensions do not preserve exact standing",
        expected="eight SATISFIED dimensions",
    )
    if code is not None:
        return code, reason, validation

    cardinality_valid = (
        _exact_int(detail.get("candidate_result_posture_count"), 1)
        and _exact_int(detail.get("evaluated_dimension_count"), 8)
        and summary.get("selected_candidate_id") == DECLARATION_CANDIDATE_ID
        and summary.get("candidate_sufficiency_operation_exhausted") is True
    )
    code, reason = _require(
        checks,
        "candidate_sufficiency.cardinality",
        cardinality_valid,
        "CANDIDATE_SUFFICIENCY_CARDINALITY_MISMATCH",
        "candidate sufficiency completion or cardinality mismatch",
        expected="one result posture and eight evaluated dimensions",
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
                "operation_id": CANDIDATE_SUFFICIENCY_OPERATION_ID,
                "operation_type": CANDIDATE_SUFFICIENCY_OPERATION_TYPE,
                "operation_version": RESULT_VERSION,
                "operation_scope": CANDIDATE_SUFFICIENCY_OPERATION_SCOPE,
                "outcome": CANDIDATE_SUFFICIENCY_OUTCOME_REQUIRED,
                "operation_result": CANDIDATE_SUFFICIENCY_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "refusal_withholding_compatibility": "SATISFIED",
                "candidate_sufficiency_operation_exhausted": True,
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
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_attestation_validation()
    code, reason, artifact = _load_exact_json_artifact(
        path=RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
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
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_summary"
    )
    identity = artifact.get("selected_operation_and_candidate_identity")
    posture = artifact.get("operation_posture")
    detail = artifact.get("operation_result_detail")
    non_claims = artifact.get("non_claims")
    block = artifact.get("block")
    if not all(
        isinstance(value, Mapping)
        for value in (
            operation,
            summary,
            identity,
            posture,
            detail,
            non_claims,
            block,
        )
    ):
        code = "RECEIVER_ATTESTATION_ARTIFACT_SECTION_MISSING"
        _add_failure(checks, "receiver_attestation.sections", code)
        return (
            code,
            "receiver-attestation artifact lacks canonical compact sections",
            validation,
        )
    checks.append(_check("receiver_attestation.sections", True))

    metadata_expectations = (
        (
            "resolver_module",
            artifact.get("resolver_module"),
            RECEIVER_ATTESTATION_RESOLVER_MODULE,
        ),
        ("result_version", artifact.get("result_version"), RESULT_VERSION),
        (
            "outcome",
            artifact.get("outcome"),
            RECEIVER_ATTESTATION_OUTCOME_REQUIRED,
        ),
        ("failed_check_count", artifact.get("failed_check_count"), 0),
        (
            "passed_check_count",
            artifact.get("passed_check_count"),
            RECEIVER_ATTESTATION_PASSED_CHECK_COUNT,
        ),
    )
    for name, actual, expected in metadata_expectations:
        valid = (
            _exact_int(actual, expected)
            if type(expected) is int
            else actual == expected
        )
        failure = (
            "RECEIVER_ATTESTATION_FAILED_CHECKS_PRESENT"
            if name == "failed_check_count"
            else "RECEIVER_ATTESTATION_METADATA_MISMATCH"
        )
        code, reason = _require(
            checks,
            "receiver_attestation." + name,
            valid,
            failure,
            "receiver-attestation metadata mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "receiver_attestation.blocked",
        _exact_bool(block.get("blocked"), False)
        and _exact_bool(summary.get("blocked"), False),
        "RECEIVER_ATTESTATION_BLOCKED",
        "receiver-attestation artifact is blocked",
        expected=False,
    )
    if code is not None:
        return code, reason, validation

    identity_expectations = (
        ("operation_id", RECEIVER_ATTESTATION_OPERATION_ID),
        ("operation_type", RECEIVER_ATTESTATION_OPERATION_TYPE),
        ("operation_version", RESULT_VERSION),
        ("operation_scope", RECEIVER_ATTESTATION_OPERATION_SCOPE),
        ("receiver_side_answerable_basis_candidate_id", DECLARATION_CANDIDATE_ID),
    )
    for field, expected in identity_expectations:
        code, reason = _require(
            checks,
            "receiver_attestation.identity." + field,
            operation.get(field) == expected,
            "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            "receiver-attestation identity mismatch: " + field,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    correspondence_valid = (
        identity.get("operation_id") == RECEIVER_ATTESTATION_OPERATION_ID
        and identity.get("selected_candidate_id") == DECLARATION_CANDIDATE_ID
        and identity.get("selected_sufficiency_operation_id")
        == CANDIDATE_SUFFICIENCY_OPERATION_ID
        and identity.get("selected_sufficiency_operation_result_required")
        == CANDIDATE_SUFFICIENCY_RESULT_REQUIRED
        and operation.get("selected_candidate_sufficiency_operation_id")
        == CANDIDATE_SUFFICIENCY_OPERATION_ID
        and operation.get(
            "selected_candidate_sufficiency_operation_result_required"
        )
        == CANDIDATE_SUFFICIENCY_RESULT_REQUIRED
    )
    code, reason = _require(
        checks,
        "receiver_attestation.correspondence",
        correspondence_valid,
        "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        "receiver-attestation candidate correspondence mismatch",
        expected=DECLARATION_CANDIDATE_ID,
    )
    if code is not None:
        return code, reason, validation

    result_locations = (
        operation.get("receiver_attestation_operation_result"),
        summary.get("operation_result"),
        detail.get("operation_result"),
    )
    code, reason = _require(
        checks,
        "receiver_attestation.operation_result",
        all(
            value == RECEIVER_ATTESTATION_RESULT_REQUIRED
            for value in result_locations
        ),
        "RECEIVER_ATTESTATION_RESULT_MISMATCH",
        "receiver-attestation result does not match exact recorded result",
        expected=RECEIVER_ATTESTATION_RESULT_REQUIRED,
    )
    if code is not None:
        return code, reason, validation

    for field in (
        "operation_basis_supplied",
        "operation_basis_admitted",
        "receiver_attestation_decided",
        "receiver_attestation_recorded",
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_result_recorded",
        "receiver_attestation_operation_exhausted",
    ):
        code, reason = _require(
            checks,
            "receiver_attestation.true_posture." + field,
            _exact_bool(operation.get(field), True),
            "RECEIVER_ATTESTATION_POSTURE_MISMATCH",
            "receiver-attestation posture is not exact true: " + field,
            expected=True,
        )
        if code is not None:
            return code, reason, validation

    cardinality_valid = (
        _exact_int(detail.get("completed_result_posture_count"), 1)
        and posture.get("operation_exhausted") is True
        and posture.get("operation_recorded") is True
        and posture.get("operation_result_recorded") is True
    )
    code, reason = _require(
        checks,
        "receiver_attestation.cardinality",
        cardinality_valid,
        "RECEIVER_ATTESTATION_CARDINALITY_MISMATCH",
        "receiver-attestation completion or cardinality mismatch",
        expected=1,
    )
    if code is not None:
        return code, reason, validation

    code, reason = _require(
        checks,
        "receiver_attestation.non_claims",
        _canonical_false_mapping(non_claims),
        "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "receiver-attestation non-claims are not canonical false",
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
                "operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
                "operation_type": RECEIVER_ATTESTATION_OPERATION_TYPE,
                "operation_version": RESULT_VERSION,
                "operation_scope": RECEIVER_ATTESTATION_OPERATION_SCOPE,
                "outcome": RECEIVER_ATTESTATION_OUTCOME_REQUIRED,
                "operation_result": RECEIVER_ATTESTATION_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
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
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_receipt_validation()
    code, reason, artifact = _load_exact_json_artifact(
        path=RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
        expected_sha256=RECEIVER_ANSWERABLE_RECEIPT_SHA256,
        prefix="receiver_answerable_receipt",
        code_prefix="RECEIVER_ANSWERABLE_RECEIPT",
        checks=checks,
        validation=validation,
    )
    if code is not None or artifact is None:
        return code, reason, validation

    operation = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_summary"
    )
    identity = artifact.get("selected_operation_and_candidate_identity")
    posture = artifact.get("operation_posture")
    detail = artifact.get("operation_result_detail")
    correspondence = artifact.get("upstream_correspondence_validation")
    non_claims = artifact.get("non_claims")
    block = artifact.get("block")
    if not all(
        isinstance(value, Mapping)
        for value in (
            operation,
            summary,
            identity,
            posture,
            detail,
            correspondence,
            non_claims,
            block,
        )
    ):
        code = "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_SECTION_MISSING"
        _add_failure(checks, "receiver_answerable_receipt.sections", code)
        return (
            code,
            "receiver-answerable-receipt artifact lacks compact sections",
            validation,
        )
    checks.append(_check("receiver_answerable_receipt.sections", True))

    metadata_expectations = (
        (
            "resolver_module",
            artifact.get("resolver_module"),
            RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE,
        ),
        ("result_version", artifact.get("result_version"), RESULT_VERSION),
        (
            "outcome",
            artifact.get("outcome"),
            RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED,
        ),
        ("failed_check_count", artifact.get("failed_check_count"), 0),
        (
            "passed_check_count",
            artifact.get("passed_check_count"),
            RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT,
        ),
    )
    for name, actual, expected in metadata_expectations:
        valid = (
            _exact_int(actual, expected)
            if type(expected) is int
            else actual == expected
        )
        failure = (
            "RECEIVER_ANSWERABLE_RECEIPT_FAILED_CHECKS_PRESENT"
            if name == "failed_check_count"
            else "RECEIVER_ANSWERABLE_RECEIPT_METADATA_MISMATCH"
        )
        code, reason = _require(
            checks,
            "receiver_answerable_receipt." + name,
            valid,
            failure,
            "receiver-answerable-receipt metadata mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "receiver_answerable_receipt.blocked",
        _exact_bool(block.get("blocked"), False)
        and _exact_bool(summary.get("blocked"), False),
        "RECEIVER_ANSWERABLE_RECEIPT_BLOCKED",
        "receiver-answerable-receipt artifact is blocked",
        expected=False,
    )
    if code is not None:
        return code, reason, validation

    identity_expectations = (
        ("operation_id", RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID),
        ("operation_type", RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE),
        ("operation_version", RESULT_VERSION),
        ("operation_scope", RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE),
        ("receiver_side_answerable_basis_candidate_id", DECLARATION_CANDIDATE_ID),
    )
    for field, expected in identity_expectations:
        code, reason = _require(
            checks,
            "receiver_answerable_receipt.identity." + field,
            operation.get(field) == expected,
            "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH",
            "receiver-answerable-receipt identity mismatch: " + field,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    correspondence_valid = (
        identity.get("operation_id") == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID
        and identity.get("selected_candidate_id") == DECLARATION_CANDIDATE_ID
        and identity.get("selected_attestation_operation_id")
        == RECEIVER_ATTESTATION_OPERATION_ID
        and identity.get("selected_attestation_operation_result_required")
        == RECEIVER_ATTESTATION_RESULT_REQUIRED
        and operation.get("selected_receiver_attestation_operation_id")
        == RECEIVER_ATTESTATION_OPERATION_ID
        and operation.get(
            "selected_receiver_attestation_operation_result_required"
        )
        == RECEIVER_ATTESTATION_RESULT_REQUIRED
        and correspondence.get("upstream_correspondence_validated") is True
        and correspondence.get(
            "selected_attestation_operation_identity_corresponds"
        )
        is True
        and correspondence.get("selected_candidate_identity_corresponds")
        is True
    )
    code, reason = _require(
        checks,
        "receiver_answerable_receipt.correspondence",
        correspondence_valid,
        "RECEIVER_ANSWERABLE_RECEIPT_IDENTITY_MISMATCH",
        "receiver-answerable-receipt correspondence mismatch",
        expected=RECEIVER_ATTESTATION_OPERATION_ID,
    )
    if code is not None:
        return code, reason, validation

    result_locations = (
        artifact.get("operation_result"),
        operation.get("receiver_answerable_receipt_operation_result"),
        summary.get("operation_result"),
        detail.get("operation_result"),
    )
    code, reason = _require(
        checks,
        "receiver_answerable_receipt.operation_result",
        all(
            value == RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED
            for value in result_locations
        ),
        "RECEIVER_ANSWERABLE_RECEIPT_RESULT_MISMATCH",
        "receipt result does not match exact recorded result",
        expected=RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
    )
    if code is not None:
        return code, reason, validation

    for field in (
        "operation_basis_supplied",
        "operation_basis_admitted",
        "receiver_answerable_receipt_decided",
        "receiver_answerable_receipt_recorded",
        "receiver_answerable_receipt_present",
        "receiver_answerable_receipt_operation_recorded",
        "receiver_answerable_receipt_operation_result_recorded",
        "receiver_answerable_receipt_operation_exhausted",
    ):
        code, reason = _require(
            checks,
            "receiver_answerable_receipt.true_posture." + field,
            _exact_bool(operation.get(field), True),
            "RECEIVER_ANSWERABLE_RECEIPT_POSTURE_MISMATCH",
            "receipt posture is not exact true: " + field,
            expected=True,
        )
        if code is not None:
            return code, reason, validation

    cardinality_valid = (
        _exact_int(operation.get("completed_result_posture_count"), 1)
        and _exact_int(posture.get("completed_result_posture_count"), 1)
        and _exact_int(detail.get("completed_result_posture_count"), 1)
        and summary.get("receiver_answerable_receipt_operation_exhausted")
        is True
    )
    code, reason = _require(
        checks,
        "receiver_answerable_receipt.cardinality",
        cardinality_valid,
        "RECEIVER_ANSWERABLE_RECEIPT_CARDINALITY_MISMATCH",
        "receipt completion or cardinality mismatch",
        expected=1,
    )
    if code is not None:
        return code, reason, validation

    code, reason = _require(
        checks,
        "receiver_answerable_receipt.non_claims",
        _canonical_false_mapping(non_claims)
        and artifact.get("result_level_non_claims_canonical_false") is True,
        "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "receipt non-claims are not canonical false",
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
                "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
                "operation_type": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
                "operation_version": RESULT_VERSION,
                "operation_scope": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
                "outcome": RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED,
                "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
                "candidate_id": DECLARATION_CANDIDATE_ID,
                "selected_attestation_operation_id": (
                    RECEIVER_ATTESTATION_OPERATION_ID
                ),
                "operation_basis_admitted": True,
                "receiver_answerable_receipt_recorded": True,
                "receiver_answerable_receipt_present": True,
                "operation_exhausted": True,
                "completed_result_posture_count": 1,
            },
        }
    )
    return None, None, validation


def _empty_source_lineage() -> dict[str, Any]:
    return {
        "source_selection_recorded": False,
        "exact_source_identity_validated": False,
        "source_class_validated": False,
        "receiver_origin_validated": False,
        "declared_provenance_posture_validated": False,
        "candidate_correspondence_validated": False,
        "candidate_sufficiency_lineage_validated": False,
        "receiver_attestation_lineage_validated": False,
        "receiver_answerable_receipt_lineage_validated": False,
        "prior_requires_basis_lineage_validated": False,
        "carriage_lineage_validated": False,
    }


def _validate_three_part_admissibility(
    request: Mapping[str, Any],
    *,
    prior: Mapping[str, Any],
    declaration: Mapping[str, Any],
    candidate: Mapping[str, Any],
    attestation: Mapping[str, Any],
    receipt: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[
    str | None,
    str | None,
    dict[str, Any],
]:
    source_lineage = _empty_source_lineage()
    candidate_standing = candidate.get("standing")
    attestation_standing = attestation.get("standing")
    receipt_standing = receipt.get("standing")
    prior_standing = prior.get("standing")
    standing_available = all(
        isinstance(value, Mapping)
        for value in (
            candidate_standing,
            attestation_standing,
            receipt_standing,
            prior_standing,
        )
    )
    source_valid = (
        declaration.get("declaration_validated") is True
        and request.get("selected_source_class") == SELECTED_SOURCE_CLASS
        and request.get("selected_source_origin") == SELECTED_SOURCE_ORIGIN
        and request.get("selected_source_provenance_posture")
        == SELECTED_SOURCE_PROVENANCE_POSTURE
        and request.get(
            "selected_receiver_originating_declaration_"
            "source_provenance_reference"
        )
        == DECLARATION_PROVENANCE_REFERENCE
        and request.get(
            "selected_receiver_originating_declaration_candidate_id"
        )
        == DECLARATION_CANDIDATE_ID
        and standing_available
        and candidate_standing.get("candidate_id") == DECLARATION_CANDIDATE_ID
        and attestation_standing.get("candidate_id") == DECLARATION_CANDIDATE_ID
        and receipt_standing.get("candidate_id") == DECLARATION_CANDIDATE_ID
        and receipt_standing.get("selected_attestation_operation_id")
        == RECEIVER_ATTESTATION_OPERATION_ID
        and prior_standing.get("operation_result")
        == PRIOR_OPERATION_RESULT_REQUIRED
    )
    code, reason = _require(
        checks,
        "admissibility.source",
        source_valid,
        "SOURCE_ADMISSIBILITY_NOT_PASSED",
        "exact source identity, class, origin, provenance, or carriage failed",
        expected=ADMISSIBILITY_PASSED,
    )
    if code is not None:
        return code, reason, source_lineage

    source_lineage.update(
        {
            "source_selection_recorded": True,
            "exact_source_identity_validated": True,
            "source_class_validated": True,
            "receiver_origin_validated": True,
            "declared_provenance_posture_validated": True,
            "candidate_correspondence_validated": True,
            "candidate_sufficiency_lineage_validated": True,
            "receiver_attestation_lineage_validated": True,
            "receiver_answerable_receipt_lineage_validated": True,
            "prior_requires_basis_lineage_validated": True,
            "carriage_lineage_validated": True,
        }
    )

    relevant = declaration.get("matter_relevant_records")
    scope_valid = (
        request.get("selected_relation_class") == SELECTED_RELATION_CLASS
        and request.get("selected_matter_class") == SELECTED_MATTER_CLASS
        and request.get("selected_matter") == list(REQUIRED_MATTER_TUPLE)
        and isinstance(relevant, Mapping)
        and relevant
        == {
            "could_have_been_refused": True,
            "could_have_been_withheld": True,
        }
        and candidate_standing.get("refusal_withholding_compatibility")
        == "SATISFIED"
        and _non_claims_valid(request.get("declared_non_claims"))
        and request["declared_non_claims"].get(
            "receiver_answerable_basis_refusable_established"
        )
        is False
        and request["declared_non_claims"].get(
            "receiver_answerable_basis_could_have_been_withheld_established"
        )
        is False
    )
    code, reason = _require(
        checks,
        "admissibility.scope_and_matter",
        scope_valid,
        "SCOPE_AND_MATTER_ADMISSIBILITY_NOT_PASSED",
        "relation class, matter class, exact tuple, or non-conversion failed",
        expected=ADMISSIBILITY_PASSED,
    )
    if code is not None:
        return code, reason, _empty_source_lineage()

    transition_valid = (
        request.get("selected_source_origin") == SELECTED_SOURCE_ORIGIN
        and request.get("selected_source_provenance_posture")
        == SELECTED_SOURCE_PROVENANCE_POSTURE
        and request.get("selected_source_arrival_posture")
        == SELECTED_SOURCE_ARRIVAL_POSTURE
        and request.get("selected_source_native_standing") is False
        and request.get("jurisdiction_distinction_preserved") is True
        and all(
            request["declared_non_claims"].get(field) is False
            for field in (
                "receiver_originating_declaration_native_standing_created",
                "receiver_originating_declaration_authority_created",
                "source_authority_created",
                "canon_admission_created",
                "governance_force_created",
                "truth_created",
                "standing_created",
            )
        )
    )
    code, reason = _require(
        checks,
        "admissibility.transition",
        transition_valid,
        "TRANSITION_ADMISSIBILITY_NOT_PASSED",
        "origin, provenance, carried arrival, jurisdiction, or non-native lock failed",
        expected=ADMISSIBILITY_PASSED,
    )
    if code is not None:
        return code, reason, _empty_source_lineage()
    return None, None, source_lineage


def _branch_values(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    not_allowed = outcome == OUTCOME_NOT_ALLOWED
    completed = allowed or not_allowed
    return {
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_recorded"
        ): completed,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result_recorded"
        ): completed,
        "receiver_originating_modal_fact_evaluation_consideration_allowed": (
            allowed
        ),
        (
            "receiver_originating_modal_fact_"
            "evaluation_consideration_not_allowed"
        ): not_allowed,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_exhausted"
        ): completed,
        "source_selection_recorded": completed,
        "completed_consideration_posture_count": int(allowed)
        + int(not_allowed),
    }


def _boundary_result_for_outcome(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return RESULT_ALLOWED
    if outcome == OUTCOME_NOT_ALLOWED:
        return RESULT_NOT_ALLOWED
    return RESULT_NOT_EVALUATED


def _route_for_outcome(outcome: str) -> str | None:
    return ADMISSIBLE_FUTURE_ROUTE if outcome == OUTCOME_ALLOWED else None


def _admissibility_evaluations_for_outcome(
    outcome: str,
) -> dict[str, str]:
    value = (
        ADMISSIBILITY_PASSED
        if outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
        else ADMISSIBILITY_NOT_EVALUATED
    )
    return {
        "source_admissibility_evaluation": value,
        "scope_and_matter_admissibility_evaluation": value,
        "transition_admissibility_evaluation": value,
    }


def _decision_for_outcome(
    outcome: str,
    *,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    if outcome == OUTCOME_ALLOWED:
        return {
            "decision_code": DECISION_CODE_ALLOWED,
            "decision_reason": DECISION_REASON_ALLOWED,
        }
    if outcome == OUTCOME_NOT_ALLOWED:
        return {
            "decision_code": DECISION_CODE_NOT_ALLOWED,
            "decision_reason": DECISION_REASON_NOT_ALLOWED,
        }
    return {"decision_code": code, "decision_reason": reason}


def _compact_declaration_identity() -> dict[str, Any]:
    return {
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


def _boundary_object(
    outcome: str,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    selected = request.get(
        "receiver_originating_modal_fact_evaluation_consideration_selected"
    )
    branch = _branch_values(outcome)
    evaluations = _admissibility_evaluations_for_outcome(outcome)
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_id"
        ): BOUNDARY_ID,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_type"
        ): BOUNDARY_TYPE,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_version"
        ): BOUNDARY_VERSION,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_scope"
        ): BOUNDARY_SCOPE,
        "selected_source_class": SELECTED_SOURCE_CLASS,
        "selected_relation_class": SELECTED_RELATION_CLASS,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_provenance_posture": (
            SELECTED_SOURCE_PROVENANCE_POSTURE
        ),
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "selected_matter": list(REQUIRED_MATTER_TUPLE),
        "selected_receiver_originating_declaration": (
            _compact_declaration_identity()
        ),
        "matter_relevant_declaration_records": {
            "could_have_been_refused": True,
            "could_have_been_withheld": True,
        },
        (
            "receiver_originating_modal_fact_"
            "evaluation_consideration_selected"
        ): selected if completed and type(selected) is bool else False,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result"
        ): _boundary_result_for_outcome(outcome),
        **evaluations,
        **branch,
        "admissible_future_route": _route_for_outcome(outcome),
        **_canonical_non_claims(),
    }


def _declared_request_posture(
    request: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    selected = request.get(
        "receiver_originating_modal_fact_evaluation_consideration_selected"
    )
    return {
        "canonical_schema_validated": set(request) == _canonical_request_keys(),
        "canonical_identity_and_paths_validated": all(
            request.get(field) == expected
            for field, expected in _identity_request_values().items()
        ),
        (
            "receiver_originating_modal_fact_"
            "evaluation_consideration_selected"
        ): selected if completed and type(selected) is bool else False,
        "declared_non_claims_validated": _non_claims_valid(
            request.get("declared_non_claims")
        ),
        "result_and_semantic_preclaims_absent": not bool(
            set(request).intersection(PROHIBITED_DIRECT_REQUEST_FIELDS)
        ),
        "unknown_request_fields_absent": not bool(
            set(request).difference(_canonical_request_keys())
        ),
    }


def _statement(outcome: str) -> dict[str, bool]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    return {
        "one_exact_receiver_originating_declaration_considered": completed,
        "source_admissibility_only": True,
        "two_condition_matter_only": True,
        "receiver_origin_preserved": True,
        "declared_provenance_preserved": True,
        "carried_arrival_remains_non_native": True,
        "jurisdiction_distinction_preserved": True,
        "declaration_not_naturalized": True,
        "modal_fact_evaluation_not_performed": True,
        "modal_fact_not_established": True,
        "actual_refusal_or_withholding_not_established": True,
        "receiver_freedom_not_established": True,
        "truth_authority_standing_and_presence_not_created": True,
        "later_modal_fact_evaluation_operation_not_created_or_executed": True,
        "excluded_source_body_conditions_not_evaluated": True,
        "no_scan_discovery_repair_replacement_or_normalization": True,
        "result_level_non_claims_canonical_false": True,
        "open_does_not_mean_next": True,
    }


def _append_generated_checks(
    checks: list[dict[str, Any]],
    outcome: str,
) -> None:
    for field in REQUIRED_FALSE_NON_CLAIMS:
        checks.append(_check("non_claims." + field, True, expected=False))
    checks.append(
        _check(
            "non_claims.result_level_non_claims_canonical_false",
            True,
            expected=True,
        )
    )
    for field in OMISSION_POSTURE_FIELDS:
        checks.append(_check("omission." + field, True, expected=True))
    for field in LINEAGE_PRESERVATION_FIELDS:
        checks.append(_check("lineage." + field, True, expected=True))
    for field in NON_MEANING_FIELDS:
        checks.append(_check("non_meaning." + field, True, expected=True))
    for field in EXCLUDED_CONDITIONS:
        checks.append(
            _check(
                "excluded_condition." + field,
                True,
                expected=ADMISSIBILITY_NOT_EVALUATED,
            )
        )
    for field, expected in _branch_values(outcome).items():
        checks.append(_check("branch." + field, True, expected=expected))
    for field, expected in _admissibility_evaluations_for_outcome(
        outcome
    ).items():
        checks.append(_check("branch." + field, True, expected=expected))


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get(
        "receiver_originating_modal_fact_source_admissibility_boundary"
    )
    boundary = boundary if isinstance(boundary, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    decision = result.get("boundary_decision")
    decision = decision if isinstance(decision, Mapping) else {}
    specification = result.get("specification_validation")
    specification = (
        specification if isinstance(specification, Mapping) else {}
    )
    prior = result.get("prior_operation_artifact_validation")
    prior = prior if isinstance(prior, Mapping) else {}
    declaration = result.get("receiver_originating_declaration_validation")
    declaration = declaration if isinstance(declaration, Mapping) else {}
    candidate = result.get("candidate_sufficiency_artifact_validation")
    candidate = candidate if isinstance(candidate, Mapping) else {}
    attestation = result.get("receiver_attestation_artifact_validation")
    attestation = attestation if isinstance(attestation, Mapping) else {}
    receipt = result.get("receiver_answerable_receipt_artifact_validation")
    receipt = receipt if isinstance(receipt, Mapping) else {}
    evaluations = result.get("admissibility_evaluations")
    evaluations = evaluations if isinstance(evaluations, Mapping) else {}
    lineage = result.get("lineage_preservation_posture")
    lineage = lineage if isinstance(lineage, Mapping) else {}
    omission = result.get("omission_posture")
    omission = omission if isinstance(omission, Mapping) else {}
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "prior_operation_artifact_path": str(
            PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "declaration_surface_path": str(DECLARATION_SURFACE_RELATIVE_PATH),
        "declaration_sha256": DECLARATION_SHA256,
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
        "selected_matter": list(REQUIRED_MATTER_TUPLE),
        "selected_source_origin": SELECTED_SOURCE_ORIGIN,
        "selected_source_arrival_posture": SELECTED_SOURCE_ARRIVAL_POSTURE,
        "selected_source_native_standing": False,
        "jurisdiction_distinction_preserved": True,
        "outcome": result.get("outcome"),
        "boundary_result": result.get("boundary_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("decision_code"),
        "decision_reason": decision.get("decision_reason"),
        "selection": boundary.get(
            "receiver_originating_modal_fact_"
            "evaluation_consideration_selected"
        ),
        "specification_validated": specification.get(
            "specification_validated"
        ),
        "prior_operation_artifact_validated": prior.get(
            "artifact_validated"
        ),
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
        "source_admissibility_evaluation": evaluations.get(
            "source_admissibility_evaluation"
        ),
        "scope_and_matter_admissibility_evaluation": evaluations.get(
            "scope_and_matter_admissibility_evaluation"
        ),
        "transition_admissibility_evaluation": evaluations.get(
            "transition_admissibility_evaluation"
        ),
        "boundary_recorded": boundary.get(
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_recorded"
        ),
        "boundary_result_recorded": boundary.get(
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result_recorded"
        ),
        "boundary_exhausted": boundary.get(
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_exhausted"
        ),
        "source_selection_recorded": boundary.get(
            "source_selection_recorded"
        ),
        "consideration_allowed": boundary.get(
            "receiver_originating_modal_fact_"
            "evaluation_consideration_allowed"
        ),
        "consideration_not_allowed": boundary.get(
            "receiver_originating_modal_fact_"
            "evaluation_consideration_not_allowed"
        ),
        "completed_consideration_posture_count": result.get(
            "completed_consideration_posture_count"
        ),
        "receiver_origin_preserved": lineage.get(
            "selected_source_remains_receiver_originating"
        ),
        "source_relation_preserved": lineage.get(
            "source_relation_remains_legible"
        ),
        "jurisdiction_preserved": lineage.get(
            "jurisdiction_not_collapsed"
        ),
        "source_not_naturalized": lineage.get("source_not_naturalized"),
        "modal_fact_truth_authority_standing_presence_absent": all(
            boundary.get(field) is False
            for field in (
                "receiver_answerable_basis_refusable_established",
                (
                    "receiver_answerable_basis_"
                    "could_have_been_withheld_established"
                ),
                "source_authority_created",
                "truth_created",
                "standing_created",
                "presence_supported",
                "presence_authorized",
                "presence_established",
                "presence_recorded",
            )
        ),
        "downstream_non_claims_canonical_false": _non_claims_valid(
            result.get("non_claims")
        ),
        "result_level_non_claims_canonical_false": result.get(
            "result_level_non_claims_canonical_false"
        ),
        "complete_material_omission_posture": (
            bool(omission)
            and all(value is True for value in omission.values())
        ),
        "admissible_future_route": result.get("admissible_future_route"),
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    prior_validation: Mapping[str, Any] | None = None,
    declaration_validation: Mapping[str, Any] | None = None,
    candidate_validation: Mapping[str, Any] | None = None,
    attestation_validation: Mapping[str, Any] | None = None,
    receipt_validation: Mapping[str, Any] | None = None,
    source_lineage: Mapping[str, Any] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    specification = (
        copy.deepcopy(dict(specification_validation))
        if isinstance(specification_validation, Mapping)
        else _empty_specification_validation()
    )
    prior = (
        copy.deepcopy(dict(prior_validation))
        if isinstance(prior_validation, Mapping)
        else _empty_prior_validation()
    )
    declaration = (
        copy.deepcopy(dict(declaration_validation))
        if isinstance(declaration_validation, Mapping)
        else _empty_declaration_validation()
    )
    candidate = (
        copy.deepcopy(dict(candidate_validation))
        if isinstance(candidate_validation, Mapping)
        else _empty_candidate_validation()
    )
    attestation = (
        copy.deepcopy(dict(attestation_validation))
        if isinstance(attestation_validation, Mapping)
        else _empty_attestation_validation()
    )
    receipt = (
        copy.deepcopy(dict(receipt_validation))
        if isinstance(receipt_validation, Mapping)
        else _empty_receipt_validation()
    )
    source = (
        copy.deepcopy(dict(source_lineage))
        if isinstance(source_lineage, Mapping)
        else _empty_source_lineage()
    )
    branch = _branch_values(outcome)
    evaluations = _admissibility_evaluations_for_outcome(outcome)
    boundary_result = _boundary_result_for_outcome(outcome)
    route = _route_for_outcome(outcome)
    decision = _decision_for_outcome(outcome, code=code, reason=reason)
    result: dict[str, Any] = {
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_metadata"
        ): {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "prior_operation_artifact_path": str(
                PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
            "declaration_surface_path": str(
                DECLARATION_SURFACE_RELATIVE_PATH
            ),
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
        (
            "declared_receiver_originating_modal_fact_"
            "source_admissibility_boundary_request"
        ): _declared_request_posture(request, outcome),
        "specification_validation": specification,
        "prior_operation_artifact_validation": prior,
        "receiver_originating_declaration_validation": declaration,
        "candidate_sufficiency_artifact_validation": candidate,
        "receiver_attestation_artifact_validation": attestation,
        "receiver_answerable_receipt_artifact_validation": receipt,
        "source_selection_and_carriage_lineage": source,
        "admissibility_evaluations": evaluations,
        "lineage_preservation_posture": _canonical_lineage_posture(),
        "excluded_condition_posture": (
            _canonical_excluded_condition_posture()
        ),
        "boundary_decision": {
            **decision,
            "selection": (
                request.get(
                    "receiver_originating_modal_fact_"
                    "evaluation_consideration_selected"
                )
                if outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
                else False
            ),
        },
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "boundary_posture": {
            **branch,
            **evaluations,
            "single_use_only": True,
            "boundary_exhaustion_is_not_source_use": True,
            "boundary_exhaustion_is_not_modal_fact_evaluation": True,
            "boundary_exhaustion_is_not_modal_fact_establishment": True,
            "boundary_exhaustion_is_not_standing_or_presence": True,
        },
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary"
        ): _boundary_object(outcome, request),
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_checks"
        ): copy.deepcopy(checks),
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_statement"
        ): _statement(outcome),
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_non_meaning"
        ): _canonical_non_meaning(),
        "omission_posture": _canonical_omission_posture(),
        "blocked_conversions": list(BLOCKED_CONVERSIONS),
        "admissible_future_route": route,
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        "outcome": outcome,
        "boundary_result": boundary_result,
        (
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result"
        ): boundary_result,
        "completed_consideration_posture_count": branch[
            "completed_consideration_posture_count"
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
    result[
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_summary"
    ] = _summary_from_result(result)
    return result


def resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact source-admissibility boundary without side effects."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = _new_canonical_request()
    elif not isinstance(request, Mapping):
        declared_request = _new_canonical_request()
        _add_failure(checks, "request.mapping", "REQUEST_NOT_MAPPING")
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            code=code,
            reason=reason,
        )

    code, reason, specification = _validate_specification(checks)
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            code=code,
            reason=reason,
        )

    code, reason, prior = _validate_prior_operation_artifact(checks)
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            code=code,
            reason=reason,
        )

    code, reason, declaration = _validate_declaration_surface(checks)
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            declaration_validation=declaration,
            code=code,
            reason=reason,
        )

    code, reason, candidate = _validate_candidate_sufficiency_artifact(
        checks
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            declaration_validation=declaration,
            candidate_validation=candidate,
            code=code,
            reason=reason,
        )

    code, reason, attestation = _validate_receiver_attestation_artifact(
        checks
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
            code=code,
            reason=reason,
        )

    code, reason, receipt = (
        _validate_receiver_answerable_receipt_artifact(checks)
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
            receipt_validation=receipt,
            code=code,
            reason=reason,
        )

    code, reason, source_lineage = _validate_three_part_admissibility(
        declared_request,
        prior=prior,
        declaration=declaration,
        candidate=candidate,
        attestation=attestation,
        receipt=receipt,
        checks=checks,
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            declaration_validation=declaration,
            candidate_validation=candidate,
            attestation_validation=attestation,
            receipt_validation=receipt,
            code=code,
            reason=reason,
        )

    selected = declared_request[
        "receiver_originating_modal_fact_evaluation_consideration_selected"
    ]
    checks.append(
        _check(
            (
                "decision.receiver_originating_modal_fact_"
                "evaluation_consideration_selected"
            ),
            True,
            expected=selected,
        )
    )
    outcome = OUTCOME_ALLOWED if selected else OUTCOME_NOT_ALLOWED
    _append_generated_checks(checks, outcome)
    return _build_result(
        declared_request,
        outcome,
        checks,
        specification_validation=specification,
        prior_validation=prior,
        declaration_validation=declaration,
        candidate_validation=candidate,
        attestation_validation=attestation,
        receipt_validation=receipt,
        source_lineage=source_lineage,
    )


def resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Strictly load one explicit request path and resolve without discovery."""
    payload, error = _read_json(request_path)
    if error is not None:
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "invalid request path JSON: " + error
        )
    if not isinstance(payload, Mapping):
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "invalid request path JSON: top-level value must be a mapping"
        )
    return (
        resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min(
            payload
        )
    )


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "complete_prior_operation_artifact",
        "complete_candidate_sufficiency_artifact",
        "complete_candidate_sufficiency_material",
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
    }
    if isinstance(value, Mapping):
        return any(
            key in forbidden_keys
            or _contains_prohibited_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return any(
            _contains_prohibited_complete_material(item) for item in value
        )
    return False


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get(
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_checks"
    )
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping)
        and set(check).issubset(
            {
                "name",
                "passed",
                "expected",
                "failure_code",
                "block_code",
            }
        )
        and isinstance(check.get("name"), str)
        and bool(check.get("name"))
        and type(check.get("passed")) is bool
        for check in checks
    ):
        return False
    failed = sum(check.get("passed") is False for check in checks)
    passed = sum(check.get("passed") is True for check in checks)
    if (
        not _exact_int(result.get("failed_check_count"), failed)
        or not _exact_int(result.get("passed_check_count"), passed)
    ):
        return False
    for check in checks:
        for field in ("failure_code", "block_code"):
            if field in check and check[field] not in BLOCK_CODES:
                return False
    if result.get("outcome") in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}:
        return failed == 0
    return failed > 0


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    boundary = result.get(
        "receiver_originating_modal_fact_source_admissibility_boundary"
    )
    posture = result.get("boundary_posture")
    evaluations = result.get("admissibility_evaluations")
    block = result.get("block")
    decision = result.get("boundary_decision")
    if (
        outcome not in OUTCOME_FAMILY
        or not isinstance(boundary, Mapping)
        or not isinstance(posture, Mapping)
        or not isinstance(evaluations, Mapping)
        or not isinstance(block, Mapping)
        or not isinstance(decision, Mapping)
    ):
        return False

    expected_request = _new_canonical_request()
    expected_request[
        "receiver_originating_modal_fact_evaluation_consideration_selected"
    ] = outcome == OUTCOME_ALLOWED
    if dict(boundary) != _boundary_object(str(outcome), expected_request):
        return False

    expected_branch = _branch_values(str(outcome))
    expected_evaluations = _admissibility_evaluations_for_outcome(
        str(outcome)
    )
    expected_posture = {
        **expected_branch,
        **expected_evaluations,
        "single_use_only": True,
        "boundary_exhaustion_is_not_source_use": True,
        "boundary_exhaustion_is_not_modal_fact_evaluation": True,
        "boundary_exhaustion_is_not_modal_fact_establishment": True,
        "boundary_exhaustion_is_not_standing_or_presence": True,
    }
    if (
        dict(posture) != expected_posture
        or dict(evaluations) != expected_evaluations
        or result.get("boundary_result")
        != _boundary_result_for_outcome(str(outcome))
        or result.get(
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_result"
        )
        != _boundary_result_for_outcome(str(outcome))
        or result.get("admissible_future_route")
        != _route_for_outcome(str(outcome))
        or not _exact_int(
            result.get("completed_consideration_posture_count"),
            expected_branch["completed_consideration_posture_count"],
        )
    ):
        return False

    if outcome == OUTCOME_ALLOWED:
        return (
            block
            == {
                "blocked": False,
                "code": None,
                "block_code": None,
                "reason": None,
            }
            and decision.get("decision_code") == DECISION_CODE_ALLOWED
            and decision.get("decision_reason") == DECISION_REASON_ALLOWED
            and decision.get("selection") is True
        )
    if outcome == OUTCOME_NOT_ALLOWED:
        return (
            block
            == {
                "blocked": False,
                "code": None,
                "block_code": None,
                "reason": None,
            }
            and decision.get("decision_code") == DECISION_CODE_NOT_ALLOWED
            and decision.get("decision_reason") == DECISION_REASON_NOT_ALLOWED
            and decision.get("selection") is False
        )
    return (
        block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
        and decision.get("decision_code") == block.get("code")
        and decision.get("decision_reason") == block.get("reason")
        and decision.get("selection") is False
    )


def _validation_sections_valid(result: Mapping[str, Any]) -> bool:
    metadata = result.get(
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_metadata"
    )
    declared = result.get(
        "declared_receiver_originating_modal_fact_"
        "source_admissibility_boundary_request"
    )
    specification = result.get("specification_validation")
    prior = result.get("prior_operation_artifact_validation")
    declaration = result.get("receiver_originating_declaration_validation")
    candidate = result.get("candidate_sufficiency_artifact_validation")
    attestation = result.get("receiver_attestation_artifact_validation")
    receipt = result.get("receiver_answerable_receipt_artifact_validation")
    source = result.get("source_selection_and_carriage_lineage")
    lineage = result.get("lineage_preservation_posture")
    excluded = result.get("excluded_condition_posture")
    non_meaning = result.get(
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_non_meaning"
    )
    omission = result.get("omission_posture")
    if not all(
        isinstance(value, Mapping)
        for value in (
            metadata,
            declared,
            specification,
            prior,
            declaration,
            candidate,
            attestation,
            receipt,
            source,
            lineage,
            excluded,
            non_meaning,
            omission,
        )
    ):
        return False

    expected_metadata = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "prior_operation_artifact_path": str(
            PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
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
    if (
        dict(metadata) != expected_metadata
        or not _exact_true_mapping(lineage, LINEAGE_PRESERVATION_FIELDS)
        or not _exact_true_mapping(non_meaning, NON_MEANING_FIELDS)
        or not _exact_true_mapping(omission, OMISSION_POSTURE_FIELDS)
        or dict(excluded) != _canonical_excluded_condition_posture()
        or result.get("blocked_conversions") != list(BLOCKED_CONVERSIONS)
        or result.get("what_remains_open") != list(WHAT_REMAINS_OPEN)
        or result.get(
            "receiver_originating_modal_fact_"
            "source_admissibility_boundary_statement"
        )
        != _statement(str(result.get("outcome")))
    ):
        return False

    expected_json_validations = (
        (
            prior,
            PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH,
            PRIOR_OPERATION_SHA256,
        ),
        (
            candidate,
            CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
            CANDIDATE_SUFFICIENCY_SHA256,
        ),
        (
            attestation,
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
            RECEIVER_ATTESTATION_SHA256,
        ),
        (
            receipt,
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
            RECEIVER_ANSWERABLE_RECEIPT_SHA256,
        ),
    )
    for validation, path, digest in expected_json_validations:
        if (
            set(validation)
            != set(_empty_json_artifact_validation(path, digest))
            or validation.get("artifact_path") != str(path)
            or validation.get("expected_sha256") != digest
            or validation.get("observed_sha256") not in {None, digest}
            or not isinstance(validation.get("standing"), Mapping)
            or any(
                type(validation.get(field)) is not bool
                for field in (
                    "strict_json_validated",
                    "artifact_validated",
                    "identity_validated",
                    "result_validated",
                    "completion_and_cardinality_validated",
                    "false_locks_validated",
                )
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
        or set(declaration) != set(_empty_declaration_validation())
        or declaration.get("declaration_surface_path")
        != str(DECLARATION_SURFACE_RELATIVE_PATH)
        or declaration.get("expected_sha256") != DECLARATION_SHA256
        or declaration.get("observed_sha256") not in {None, DECLARATION_SHA256}
        or declaration.get("observed_byte_count")
        not in {None, DECLARATION_BYTE_COUNT}
        or set(source) != set(_empty_source_lineage())
        or any(type(value) is not bool for value in source.values())
        or any(type(value) is not bool for value in declared.values())
    ):
        return False

    if result.get("outcome") == OUTCOME_BLOCKED:
        return True
    return (
        declared.get("canonical_schema_validated") is True
        and declared.get("canonical_identity_and_paths_validated") is True
        and declared.get("declared_non_claims_validated") is True
        and declared.get("result_and_semantic_preclaims_absent") is True
        and declared.get("unknown_request_fields_absent") is True
        and specification.get("specification_validated") is True
        and all(
            value is True
            for value in specification.get("marker_validation", {}).values()
        )
        and all(
            validation.get("artifact_validated") is True
            and validation.get("identity_validated") is True
            and validation.get("result_validated") is True
            and validation.get("completion_and_cardinality_validated") is True
            and validation.get("false_locks_validated") is True
            and validation.get("observed_sha256")
            == validation.get("expected_sha256")
            and bool(validation.get("standing"))
            for validation, _, _ in expected_json_validations
        )
        and declaration.get("declaration_validated") is True
        and declaration.get("strict_utf8_validated") is True
        and declaration.get("exact_six_unique_records_validated") is True
        and declaration.get("observed_byte_count") == DECLARATION_BYTE_COUNT
        and declaration.get("observed_sha256") == DECLARATION_SHA256
        and declaration.get("matter_relevant_records")
        == {
            "could_have_been_refused": True,
            "could_have_been_withheld": True,
        }
        and all(value is True for value in source.values())
    )


def _result_valid_for_write(result: Mapping[str, Any]) -> bool:
    summary_key = (
        "receiver_originating_modal_fact_"
        "source_admissibility_boundary_summary"
    )
    return (
        result.get("resolver_module") == RESOLVER_MODULE
        and result.get("result_version") == RESULT_VERSION
        and set(result) == RESULT_SECTIONS
        and _branch_valid(result)
        and _checks_valid(result)
        and _validation_sections_valid(result)
        and _non_claims_valid(result.get("non_claims"))
        and result.get("result_level_non_claims_canonical_false") is True
        and not _contains_prohibited_complete_material(result)
        and result.get(summary_key) == _summary_from_result(result)
    )


def build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic summary without complete material."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "summary requires a compatible resolver result"
        )
    return _summary_from_result(result)


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_allowed(path: Path) -> bool:
    try:
        resolved = path.resolve()
        output_root = OUTPUT_ROOT.resolve()
        protected_roots = (
            (REPO_ROOT / "reference").resolve(),
            (REPO_ROOT / "spec").resolve(),
            (REPO_ROOT / "src").resolve(),
            (REPO_ROOT / "tests").resolve(),
            DECLARATION_SURFACE_PATH.parent.parent.parent.resolve(),
            PRIOR_OPERATION_ARTIFACT_PATH.parent.resolve(),
            CANDIDATE_SUFFICIENCY_ARTIFACT_PATH.parent.resolve(),
            RECEIVER_ATTESTATION_ARTIFACT_PATH.parent.resolve(),
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH.parent.resolve(),
            (REPO_ROOT / "artifacts/contaminated_lineage").resolve(),
        )
        return (
            OUTPUT_ROOT.name == CANONICAL_OUTPUT_ROOT.name
            and _path_within(resolved, output_root)
            and not any(
                _path_within(resolved, protected) for protected in protected_roots
            )
        )
    except (OSError, RuntimeError, TypeError, ValueError):
        return False


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            path.stem + "_" + f"{index:03d}" + path.suffix
        )
        if not candidate.exists():
            return candidate
    raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid result in the exact output family without overwrite."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "WRITE_REFUSED: malformed or inconsistent boundary result"
        )
    explicit = output_path is not None
    try:
        target = (
            _as_repo_path(output_path)
            if explicit
            else OUTPUT_ROOT / OUTPUT_FILENAME
        )
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "WRITE_REFUSED: output path is protected or outside the exact "
            "source-admissibility-boundary output family"
        )
    if target.is_dir():
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "WRITE_REFUSED: output path is a directory"
        )
    if explicit and target.exists():
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "WRITE_REFUSED: explicit output path already exists"
        )
    if not explicit:
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
        raise ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError(
            "WRITE_REFUSED: unable to write boundary result"
        ) from exc
    return target
