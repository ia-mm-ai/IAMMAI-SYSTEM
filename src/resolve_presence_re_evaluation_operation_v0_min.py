"""Resolve one bounded presence re-evaluation operation.

The resolver admits one exact completed re-evaluation boundary, one exact
historical waiting presence result, one exact later receiver-attestation
result, and one exact later receiver-answerable-receipt result.  It preserves
those artifacts as separate standing and derives at most one additive,
time- and scope-bounded successor presence result.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESOLVER_MODULE = "resolve_presence_re_evaluation_operation_v0_min"
RESULT_VERSION = "0.1.0"

OPERATION_ID = "presence_re_evaluation_operation_001"
OPERATION_TYPE = "PRESENCE_RE_EVALUATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "RE_EVALUATE_ONE_PRIOR_PRESENCE_RESULT_AFTER_ONE_RECORDED_"
    "RECEIVER_ANSWERABLE_RECEIPT_ONLY"
)

BOUNDARY_ID = "presence_re_evaluation_boundary_001"
BOUNDARY_TYPE = "PRESENCE_RE_EVALUATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_PRESENCE_RE_EVALUATION_AFTER_RECORDED_"
    "RECEIVER_ANSWERABLE_RECEIPT_ONLY"
)
BOUNDARY_RESOLVER_MODULE = "resolve_presence_re_evaluation_boundary_v0_min"
BOUNDARY_RESULT_VERSION = "0.1.0"
BOUNDARY_OUTCOME_REQUIRED = "PRESENCE_RE_EVALUATION_BOUNDARY_ALLOWED"
BOUNDARY_RESULT_REQUIRED = (
    "PRESENCE_RE_EVALUATION_OPERATION_CONSIDERATION_ALLOWED"
)
BOUNDARY_PASSED_CHECK_COUNT = 371
BOUNDARY_COMPLETED_CONSIDERATION_POSTURE_COUNT = 1

PRIOR_PRESENCE_OPERATION_ID = "presence_operation_001"
PRIOR_PRESENCE_OPERATION_TYPE = "PRESENCE_OPERATION"
PRIOR_PRESENCE_OPERATION_VERSION = "0.1.0"
PRIOR_PRESENCE_OPERATION_SCOPE = (
    "EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_"
    "RECEIVER_ATTESTATION_REQUIREMENT_ONLY"
)
PRIOR_PRESENCE_RESOLVER_MODULE = "resolve_presence_operation_v0_min"
PRIOR_PRESENCE_RESULT_VERSION = "0.1.0"
PRIOR_PRESENCE_OUTCOME_REQUIRED = (
    "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"
)
PRIOR_PRESENCE_RESULT_REQUIRED = "REQUIRES_RECEIVER_ATTESTATION"
PRIOR_PRESENCE_PASSED_CHECK_COUNT = 446

RECEIVER_ATTESTATION_OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_001"
)
RECEIVER_ATTESTATION_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION"
)
RECEIVER_ATTESTATION_OPERATION_VERSION = "0.1.0"
RECEIVER_ATTESTATION_OPERATION_SCOPE = (
    "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
    "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
)
RECEIVER_ATTESTATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)
RECEIVER_ATTESTATION_RESULT_VERSION = "0.1.0"
RECEIVER_ATTESTATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_RECORDED"
)
RECEIVER_ATTESTATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
)
RECEIVER_ATTESTATION_PASSED_CHECK_COUNT = 160
RECEIVER_ATTESTATION_COMPLETED_RESULT_POSTURE_COUNT = 1
RECEIVER_ATTESTATION_SELECTED_CANDIDATE_ID = (
    "receiver_side_answerable_basis_candidate_001"
)
RECEIVER_ATTESTATION_SELECTED_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
RECEIVER_ATTESTATION_SELECTED_SUFFICIENCY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
)

RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION = "0.1.0"
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE = (
    "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
    "RECEIVER_ATTESTATION_RESULT_ONLY"
)
RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min"
)
RECEIVER_ANSWERABLE_RECEIPT_RESULT_VERSION = "0.1.0"
RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT = 357
RECEIVER_ANSWERABLE_RECEIPT_COMPLETED_RESULT_POSTURE_COUNT = 1

OUTCOME_SUPPORTED = "PRESENCE_RE_EVALUATION_OPERATION_SUPPORTED"
OUTCOME_REQUIRES_BASIS = (
    "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS"
)
OUTCOME_INDETERMINATE = "PRESENCE_RE_EVALUATION_OPERATION_INDETERMINATE"
OUTCOME_BLOCKED = "PRESENCE_RE_EVALUATION_OPERATION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_SUPPORTED,
    OUTCOME_REQUIRES_BASIS,
    OUTCOME_INDETERMINATE,
    OUTCOME_BLOCKED,
)

RESULT_SUPPORTED = "PRESENCE_SUPPORTED"
RESULT_REQUIRES_BASIS = "REQUIRES_RECEIVER_ANSWERABLE_BASIS"
RESULT_INDETERMINATE = "PRESENCE_INDETERMINATE"
RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_FAMILY = (
    RESULT_SUPPORTED,
    RESULT_REQUIRES_BASIS,
    RESULT_INDETERMINATE,
    RESULT_NOT_EVALUATED,
)
OPERATION_RESULT_FAMILY = RESULT_FAMILY

EVALUATION_SATISFIED = "SATISFIED"
EVALUATION_REQUIRES_BASIS = "REQUIRES_BASIS"
EVALUATION_INDETERMINATE = "INDETERMINATE"
EVALUATION_NOT_EVALUATED = "NOT_EVALUATED"
EVALUATION_FAMILY = (
    EVALUATION_SATISFIED,
    EVALUATION_REQUIRES_BASIS,
    EVALUATION_INDETERMINATE,
    EVALUATION_NOT_EVALUATED,
)

INTENT_RECORD = "RECORD_PRESENCE_RE_EVALUATION_OPERATION"
INTENT_BLOCK = "BLOCK_PRESENCE_RE_EVALUATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

DECISION_CODE_SUPPORTED = "PRESENCE_RE_EVALUATION_SUPPORTED"
DECISION_CODE_REQUIRES_BASIS = (
    "PRESENCE_RE_EVALUATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS"
)
DECISION_CODE_INDETERMINATE = "PRESENCE_RE_EVALUATION_INDETERMINATE"
DECISION_REASON_SUPPORTED = (
    "every required presence condition was satisfied by the exact "
    "admitted four-artifact basis"
)
DECISION_REASON_REQUIRES_BASIS = (
    "one or more required receiver-answerable-basis conditions are not "
    "established by the admitted compact basis"
)
DECISION_REASON_INDETERMINATE = (
    "the admitted basis could not lawfully classify one or more required "
    "presence conditions"
)

SUPPORTED_FUTURE_ROUTE = (
    "PRESENCE_RE_EVALUATION_OPERATION_SUPPORTED_THEN_SEPARATE_"
    "PRESENCE_LAPSE_BOUNDARY_CONSIDERATION_ONLY"
)
SUPPORTED_PRESENCE_ENDING_POSTURE = (
    "REQUIRES_SEPARATELY_BOUNDED_PRESENCE_LAPSE_HANDLING"
)
CHANGED_CONDITION = (
    "RECEIVER_ATTESTATION_AND_RECEIVER_ANSWERABLE_RECEIPT_RECORDED_"
    "AFTER_PRIOR_WAITING_PRESENCE_RESULT"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/PRESENCE_RE_EVALUATION_OPERATION_V0_MIN_SPEC.md"
)
BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "presence_re_evaluation_boundary_v0_min/"
    "presence_re_evaluation_boundary_001__"
    "presence_re_evaluation_boundary_v0_min_result.json"
)
PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min/"
    "presence_operation_001__presence_operation_v0_min_result.json"
)
RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result_001.json"
)
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min/"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min_result.json"
)

GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
BOUNDARY_ARTIFACT_PATH = REPO_ROOT / BOUNDARY_ARTIFACT_RELATIVE_PATH
PRIOR_PRESENCE_ARTIFACT_PATH = (
    REPO_ROOT / PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ATTESTATION_ARTIFACT_PATH = (
    REPO_ROOT / RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH = (
    REPO_ROOT / RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SPECIFICATION_PATH

CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "presence_re_evaluation_operation_v0_min"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "presence_re_evaluation_operation_001__"
    "presence_re_evaluation_operation_v0_min_result.json"
)
DETERMINISTIC_FILENAME = OUTPUT_FILENAME

CONDITION_REQUIREMENTS = MappingProxyType(
    {
        "receiver_attested": True,
        "receiver_answerable_receipt_present": True,
        "receiver_answerable_basis_custody_distinct": True,
        "receiver_answerable_basis_controlled_by_declaring_side": False,
        "receiver_answerable_basis_refusable": True,
        "receiver_answerable_basis_could_have_been_withheld": True,
        "repo_local_execution_only": False,
        "operator_only_attestation": False,
        "derivative_rendering_attestation": False,
        "same_custody_countersignature": False,
        "automatic_acknowledgement": False,
        "generated_affirmation": False,
        "forged_receiver_attestation": False,
        "inadmissible_receiver_basis": False,
    }
)
CONDITION_KEYS = tuple(CONDITION_REQUIREMENTS)

REQUIRED_FALSE_NON_CLAIMS = (
    "durable_presence_created",
    "permanent_presence_created",
    "irrevocable_presence_created",
    "immortal_presence_created",
    "self_renewing_presence_created",
    "presence_lapse_boundary_created",
    "presence_lapse_operation_created",
    "presence_lapse_result_recorded",
    "presence_lapsed",
    "presence_expired",
    "identity_created",
    "custody_created",
    "custody_proven",
    "provenance_created",
    "provenance_proven",
    "physical_validity_created",
    "physical_validity_proven",
    "authority_created",
    "truth_created",
    "standing_created",
    "relation_created",
    "coupling_assigned",
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
    "repeated_presence_re_evaluation_operation_permission_created",
    "reusable_presence_re_evaluation_operation_route_created",
    "same_presence_re_evaluation_operation_rerun_authorized",
    "automatic_presence_re_evaluation_operation_retry_created",
    "presence_re_evaluation_operation_debt_created",
    "presence_re_evaluation_operation_obligation_created",
    "scheduled_presence_re_evaluation_created",
    "scheduled_presence_lapse_created",
    "automatic_next_step_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "prior_presence_operation_overwritten",
    "prior_presence_operation_invalidated",
    "prior_presence_operation_superseded",
    "successor_presence_is_retroactive_presence",
)

OMISSION_POSTURE_FIELDS = (
    "complete_presence_re_evaluation_boundary_artifact_omitted",
    "complete_prior_presence_artifact_omitted",
    "complete_receiver_attestation_artifact_omitted",
    "complete_receiver_answerable_receipt_artifact_omitted",
    "complete_candidate_sufficiency_material_omitted",
    "bounded_capture_source_bodies_omitted",
    "archive_bytes_omitted",
    "hash_record_body_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
    "alternative_artifacts_omitted",
)

ATTESTATION_REQUIRED_FALSE_POSTURES = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_receiver_attestation_operation_permission_created",
    "reusable_receiver_attestation_operation_route_created",
    "same_receiver_attestation_operation_rerun_authorized",
    "automatic_receiver_attestation_operation_retry_created",
    "receiver_attestation_operation_debt_created",
    "receiver_attestation_operation_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

RECEIPT_REQUIRED_FALSE_POSTURES = (
    "receiver_answerable_receipt_created",
    "receiver_answerable_receipt_supported",
    "presence_re_evaluation_boundary_created",
    "presence_re_evaluation_operation_created",
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
    "authority_created",
    "truth_created",
    "standing_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_receiver_answerable_receipt_operation_permission_created",
    "reusable_receiver_answerable_receipt_operation_route_created",
    "same_receiver_answerable_receipt_operation_rerun_authorized",
    "automatic_receiver_answerable_receipt_operation_retry_created",
    "receiver_answerable_receipt_operation_debt_created",
    "receiver_answerable_receipt_operation_obligation_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
)

SPEC_REQUIRED_MARKERS = (
    ("title", "# Presence Re-Evaluation Operation V0 Minimum Specification"),
    ("operation_id", "presence_re_evaluation_operation_id = " + OPERATION_ID),
    (
        "operation_type",
        "presence_re_evaluation_operation_type = " + OPERATION_TYPE,
    ),
    (
        "operation_version",
        "presence_re_evaluation_operation_version = " + OPERATION_VERSION,
    ),
    (
        "operation_scope",
        "presence_re_evaluation_operation_scope = " + OPERATION_SCOPE,
    ),
    ("boundary_artifact_path", str(BOUNDARY_ARTIFACT_RELATIVE_PATH)),
    (
        "prior_presence_artifact_path",
        str(PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH),
    ),
    (
        "receiver_attestation_artifact_path",
        str(RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH),
    ),
    (
        "receiver_answerable_receipt_artifact_path",
        str(RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH),
    ),
    ("atomic_basis", "The basis must be admitted atomically."),
    ("boundary_outcome", BOUNDARY_OUTCOME_REQUIRED),
    ("boundary_result", BOUNDARY_RESULT_REQUIRED),
    ("prior_presence_outcome", PRIOR_PRESENCE_OUTCOME_REQUIRED),
    ("prior_presence_result", PRIOR_PRESENCE_RESULT_REQUIRED),
    ("attestation_outcome", RECEIVER_ATTESTATION_OUTCOME_REQUIRED),
    ("attestation_result", RECEIVER_ATTESTATION_RESULT_REQUIRED),
    ("receipt_outcome", RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED),
    ("receipt_result", RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED),
    (
        "historical_later_successor_separation",
        "The result must preserve three separate layers:",
    ),
    ("receiver_attested_condition", "receiver_attested = true"),
    (
        "receiver_answerable_receipt_condition",
        "receiver_answerable_receipt_present = true",
    ),
    (
        "custody_distinct_condition",
        "receiver_answerable_basis_custody_distinct = true",
    ),
    (
        "controlled_by_declaring_side_condition",
        "receiver_answerable_basis_controlled_by_declaring_side = false",
    ),
    ("refusable_condition", "receiver_answerable_basis_refusable = true"),
    (
        "could_have_been_withheld_condition",
        "receiver_answerable_basis_could_have_been_withheld = true",
    ),
    ("evaluation_satisfied", EVALUATION_SATISFIED),
    ("evaluation_requires_basis", EVALUATION_REQUIRES_BASIS),
    ("evaluation_indeterminate", EVALUATION_INDETERMINATE),
    ("evaluation_not_evaluated", EVALUATION_NOT_EVALUATED),
    (
        "receipt_non_conversion",
        "Receipt presence alone establishes none of custody-distinctness, "
        "refusability, or could-have-been-withheld.",
    ),
    ("outcome_supported", OUTCOME_SUPPORTED),
    ("outcome_requires_basis", OUTCOME_REQUIRES_BASIS),
    ("outcome_indeterminate", OUTCOME_INDETERMINATE),
    ("outcome_blocked", OUTCOME_BLOCKED),
    ("precedence", "Selection order is:"),
    ("supported_branch", "### 11.3 Supported branch"),
    ("requires_basis_branch", "### 11.4 Requires-basis branch"),
    ("indeterminate_branch", "### 11.5 Indeterminate branch"),
    (
        "perishability",
        "presence_if_ever_supported_remains_perishable = true",
    ),
    ("lapse_separation", "lapse_consideration_is_not_lapse = true"),
    ("canonical_request", "## 13. Canonical Request"),
    ("read_and_omission", "## 14. Read and Omission Posture"),
    ("blocked_conversions", "## 15. Blocked Conversions"),
    (
        "constitutional_distinctions",
        "## 16. Required Constitutional Distinctions",
    ),
    ("preserved_non_claims", "## 17. Preserved Non-Claims"),
    ("contaminated_lineage", "Contaminated lineage remains unchanged."),
    ("branch_specific_future_route", "## 19. Branch-Specific Future Route"),
    ("open_not_next", "Open does not mean next."),
)
SPEC_MARKERS = tuple(marker for _, marker in SPEC_REQUIRED_MARKERS)

PROHIBITED_PRECLAIM_FIELDS = frozenset(
    {
        "outcome",
        "presence_re_evaluation_operation_result",
        "successor_presence_result",
        "condition_evaluations",
        "missing_or_insufficient_receiver_answerable_basis",
        "indeterminate_receiver_answerable_basis_conditions",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "presence_re_evaluation_operation_requires_receiver_answerable_basis",
        "receiver_answerable_basis_required",
        "presence_re_evaluation_indeterminate",
        "presence_re_evaluation_performed",
        "successor_presence_result_decided",
        "successor_presence_result_recorded",
        "presence_re_evaluation_operation_recorded",
        "presence_re_evaluation_operation_result_recorded",
        "presence_re_evaluation_operation_exhausted",
        "completed_successor_result_posture_count",
        "semantic_payload",
        *CONDITION_KEYS,
        *REQUIRED_FALSE_NON_CLAIMS,
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "REQUEST_BOOLEAN_REQUIRED",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "SPECIFICATION_REFERENCE_MISSING",
        "SPECIFICATION_MARKER_MISSING",
        "BOUNDARY_ARTIFACT_MISSING",
        "BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        "BOUNDARY_ARTIFACT_DUPLICATE_KEYED",
        "BOUNDARY_ARTIFACT_NOT_MAPPING",
        "BOUNDARY_ARTIFACT_SECTION_MISSING",
        "BOUNDARY_METADATA_MISMATCH",
        "BOUNDARY_FAILED_CHECKS_PRESENT",
        "BOUNDARY_BLOCKED",
        "BOUNDARY_IDENTITY_MISMATCH",
        "BOUNDARY_RESULT_MISMATCH",
        "BOUNDARY_COMPLETION_MISMATCH",
        "BOUNDARY_CARDINALITY_MISMATCH",
        "PRIOR_PRESENCE_ARTIFACT_MISSING",
        "PRIOR_PRESENCE_ARTIFACT_NOT_PARSEABLE",
        "PRIOR_PRESENCE_ARTIFACT_DUPLICATE_KEYED",
        "PRIOR_PRESENCE_ARTIFACT_NOT_MAPPING",
        "PRIOR_PRESENCE_ARTIFACT_SECTION_MISSING",
        "PRIOR_PRESENCE_METADATA_MISMATCH",
        "PRIOR_PRESENCE_FAILED_CHECKS_PRESENT",
        "PRIOR_PRESENCE_BLOCKED",
        "PRIOR_PRESENCE_IDENTITY_MISMATCH",
        "PRIOR_PRESENCE_RESULT_MISMATCH",
        "PRIOR_PRESENCE_POSTURE_MISMATCH",
        "RECEIVER_ATTESTATION_ARTIFACT_MISSING",
        "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
        "RECEIVER_ATTESTATION_ARTIFACT_DUPLICATE_KEYED",
        "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
        "RECEIVER_ATTESTATION_ARTIFACT_SECTION_MISSING",
        "RECEIVER_ATTESTATION_METADATA_MISMATCH",
        "RECEIVER_ATTESTATION_FAILED_CHECKS_PRESENT",
        "RECEIVER_ATTESTATION_BLOCKED",
        "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        "RECEIVER_ATTESTATION_RESULT_MISMATCH",
        "RECEIVER_ATTESTATION_COMPLETION_MISMATCH",
        "RECEIVER_ATTESTATION_CARDINALITY_MISMATCH",
        "RECEIVER_ATTESTATION_FALSE_LOCK_MISMATCH",
        "RECEIPT_ARTIFACT_MISSING",
        "RECEIPT_ARTIFACT_NOT_PARSEABLE",
        "RECEIPT_ARTIFACT_DUPLICATE_KEYED",
        "RECEIPT_ARTIFACT_NOT_MAPPING",
        "RECEIPT_ARTIFACT_SECTION_MISSING",
        "RECEIPT_METADATA_MISMATCH",
        "RECEIPT_FAILED_CHECKS_PRESENT",
        "RECEIPT_BLOCKED",
        "RECEIPT_IDENTITY_MISMATCH",
        "RECEIPT_RESULT_MISMATCH",
        "RECEIPT_COMPLETION_MISMATCH",
        "RECEIPT_CARDINALITY_MISMATCH",
        "RECEIPT_FALSE_LOCK_MISMATCH",
        "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        "WRITE_REFUSED",
    }
)

BLOCKED_ROUTES = (
    "boundary_allowance_to_supported_presence",
    "receipt_to_supported_presence",
    "receiver_attestation_to_supported_presence",
    "prior_waiting_result_to_successor_result_without_re_evaluation",
    "historical_false_posture_to_silent_successor_overwrite",
    "receipt_presence_to_custody_distinctness",
    "receipt_presence_to_refusability",
    "receipt_presence_to_could_have_been_withheld",
    "candidate_sufficiency_to_presence_support",
    "supported_presence_to_durable_presence",
    "supported_presence_to_identity_proof_authority_truth_or_standing",
    "perishability_to_immediate_lapse",
    "operation_exhaustion_to_lapse",
    "operation_result_to_repeat_retry_debt_obligation_or_automatic_next",
    "presence_re_evaluation_to_repair_scan_discovery_or_validation",
)

NON_MEANING_FIELDS = (
    "prior_lawful_waiting_result_is_not_error",
    "changed_standing_is_not_silent_overwrite",
    "boundary_is_not_re_evaluation_operation",
    "basis_admission_is_not_successor_result_selection",
    "receipt_is_not_presence",
    "receipt_presence_is_not_complete_basis_satisfaction",
    "receiver_attestation_is_not_presence",
    "custody_distinctness_is_not_custody_proof",
    "refusability_is_not_refusal",
    "could_have_been_withheld_is_not_actual_withholding",
    "authorization_is_not_establishment",
    "establishment_is_not_recording",
    "recording_is_not_identity_provenance_physical_validity_authority_truth_or_standing",
    "successor_presence_is_not_retroactive_presence",
    "supported_presence_is_perishable",
    "perishability_is_not_immediate_lapse",
    "lapse_consideration_is_not_lapse",
    "operation_exhaustion_is_not_durable_presence",
    "open_does_not_mean_next",
)

RESULT_SECTIONS = frozenset(
    {
        "presence_re_evaluation_operation_metadata",
        "declared_presence_re_evaluation_operation_request",
        "specification_validation",
        "presence_re_evaluation_boundary_artifact_validation",
        "prior_presence_artifact_validation",
        "receiver_attestation_artifact_validation",
        "receiver_answerable_receipt_artifact_validation",
        "atomic_operation_basis_posture",
        "prior_presence_posture",
        "later_receiver_side_posture",
        "successor_presence_evaluation_posture",
        "condition_evaluations",
        "missing_or_insufficient_receiver_answerable_basis",
        "indeterminate_receiver_answerable_basis_conditions",
        "lineage_preservation_posture",
        "perishability_posture",
        "operation_decision",
        "block",
        "operation_posture",
        "presence_re_evaluation_operation",
        "presence_re_evaluation_operation_checks",
        "presence_re_evaluation_operation_statement",
        "presence_re_evaluation_operation_non_meaning",
        "omission_posture",
        "blocked_routes",
        "admissible_future_route",
        "what_remains_open",
        "non_claims",
        "result_level_non_claims_canonical_false",
        "outcome",
        "presence_re_evaluation_operation_result",
        "successor_presence_result",
        "completed_successor_result_posture_count",
        "failed_check_count",
        "passed_check_count",
        "resolver_module",
        "result_version",
        "presence_re_evaluation_operation_summary",
    }
)


class PresenceReEvaluationOperationV0MinError(Exception):
    """Raised for invalid request paths and refused result writes."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateJsonKeyError(key)
        value[key] = item
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {field: True for field in OMISSION_POSTURE_FIELDS}


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _canonical_lineage_posture() -> dict[str, Any]:
    return {
        "prior_presence_result_preserved": True,
        "prior_presence_operation_overwritten": False,
        "prior_presence_operation_invalidated": False,
        "prior_presence_operation_superseded": False,
        "presence_re_evaluation_boundary_preserved": True,
        "receiver_attestation_result_preserved": True,
        "receiver_answerable_receipt_result_preserved": True,
        "changed_condition": CHANGED_CONDITION,
        "successor_presence_result_additive": True,
        "successor_presence_result_time_scope_bounded": True,
        "successor_presence_is_retroactive_presence": False,
        "contaminated_lineage_unchanged": True,
    }


def _canonical_perishability_posture(outcome: str) -> dict[str, Any]:
    supported = outcome == OUTCOME_SUPPORTED
    return {
        "presence_if_ever_supported_remains_perishable": True,
        "future_supported_presence_requires_separately_bounded_lapse_handling": (
            True
        ),
        "re_evaluation_does_not_create_durable_presence": True,
        "perishability_is_not_immediate_lapse": True,
        "lapse_consideration_is_not_lapse": True,
        "supported_presence_is_perishable": supported,
        "supported_presence_ending_posture": (
            SUPPORTED_PRESENCE_ENDING_POSTURE if supported else None
        ),
        "supported_presence_silently_persists_beyond_admitted_basis": False,
        "durable_presence_created": False,
        "permanent_presence_created": False,
        "irrevocable_presence_created": False,
        "immortal_presence_created": False,
        "self_renewing_presence_created": False,
        "presence_lapse_boundary_created": False,
        "presence_lapse_operation_created": False,
        "presence_lapse_result_recorded": False,
        "presence_lapsed": False,
        "presence_expired": False,
        "presence_lapse_route_absent": not supported,
    }


def _identity_request_values() -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "governing_presence_re_evaluation_operation_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "presence_re_evaluation_boundary_artifact_path": str(
            BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "prior_presence_operation_artifact_path": str(
            PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_attestation_operation_artifact_path": str(
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_answerable_receipt_operation_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
        ),
    }


def _new_canonical_request() -> dict[str, Any]:
    return {
        "intent": INTENT_RECORD,
        **_identity_request_values(),
        "presence_re_evaluation_execution_selected": True,
        "declared_non_claims": _canonical_non_claims(),
    }


def build_presence_re_evaluation_operation_v0_min_request() -> dict[str, Any]:
    """Return one fresh canonical operation-execution request."""
    return _new_canonical_request()


def build_declared_presence_re_evaluation_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return one fresh request with every deep-copied override visible."""
    request = _new_canonical_request()
    request.update(copy.deepcopy(overrides))
    return request


def _canonical_request_keys() -> set[str]:
    return {
        "intent",
        *_identity_request_values(),
        "presence_re_evaluation_execution_selected",
        "declared_non_claims",
    }


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_repo_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, TypeError, UnicodeError, ValueError):
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return (
            json.loads(text, object_pairs_hook=_reject_duplicate_json_keys),
            None,
        )
    except _DuplicateJsonKeyError:
        return None, "duplicate_key"
    except (TypeError, ValueError, json.JSONDecodeError):
        return None, "not_parseable"


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


def _add_failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> None:
    checks.append(_check(name, False, code))


def _matches_exact(value: Any, expected: Any) -> bool:
    if type(expected) is bool:
        return type(value) is bool and value is expected
    if type(expected) is int:
        return type(value) is int and value == expected
    return value == expected


def _expect_fields(
    checks: list[dict[str, Any]],
    prefix: str,
    value: Mapping[str, Any],
    expectations: Mapping[str, Any],
    code: str,
) -> bool:
    valid = True
    for field, expected in expectations.items():
        passed = _matches_exact(value.get(field), expected)
        checks.append(
            _check(
                prefix + "." + field,
                passed,
                code,
                expected=expected,
            )
        )
        valid = valid and passed
    return valid


def _first_failure(
    checks: Sequence[Mapping[str, Any]],
    start: int = 0,
) -> str | None:
    for item in checks[start:]:
        if item.get("passed") is False:
            code = item.get("block_code")
            if isinstance(code, str):
                return code
    return None


def _canonical_false_mapping_valid(
    value: Any,
    required_fields: Sequence[str] | None = None,
    *,
    exact_keys: bool = False,
) -> bool:
    if not isinstance(value, Mapping) or not value:
        return False
    if any(type(item) is not bool or item is not False for item in value.values()):
        return False
    if required_fields is None:
        return True
    required = set(required_fields)
    return set(value) == required if exact_keys else required.issubset(value)


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    if request.get("intent") == INTENT_BLOCK:
        _add_failure(checks, "request.intent", "EXPLICIT_BLOCK_REQUESTED")
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if request.get("intent") not in SUPPORTED_INTENTS:
        _add_failure(checks, "request.intent", "UNSUPPORTED_INTENT")
        return "UNSUPPORTED_INTENT", "request intent is unsupported"
    checks.append(_check("request.intent", True, expected=INTENT_RECORD))

    direct_preclaims = set(request).intersection(PROHIBITED_PRECLAIM_FIELDS)
    if direct_preclaims:
        _add_failure(
            checks,
            "request.direct_result_preclaim",
            "RESULT_POSTURE_PRECLAIMED",
        )
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "caller supplied a result, condition, or prohibited semantic posture",
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
        passed = request.get(field) == expected
        checks.append(
            _check(
                "request." + field,
                passed,
                "REQUEST_VALUE_MISMATCH",
                expected=expected,
            )
        )
        if not passed:
            return (
                "REQUEST_VALUE_MISMATCH",
                field + " does not match the canonical request",
            )

    selection = request.get("presence_re_evaluation_execution_selected")
    if type(selection) is not bool:
        _add_failure(
            checks,
            "request.presence_re_evaluation_execution_selected",
            "REQUEST_BOOLEAN_REQUIRED",
        )
        return (
            "REQUEST_BOOLEAN_REQUIRED",
            "presence re-evaluation selection must be an exact Boolean",
        )
    if selection is not True:
        _add_failure(
            checks,
            "request.presence_re_evaluation_execution_selected",
            "REQUEST_VALUE_MISMATCH",
        )
        return (
            "REQUEST_VALUE_MISMATCH",
            "presence re-evaluation execution was not selected",
        )
    checks.append(
        _check(
            "request.presence_re_evaluation_execution_selected",
            True,
            expected=True,
        )
    )

    if not _canonical_false_mapping_valid(
        request.get("declared_non_claims"),
        REQUIRED_FALSE_NON_CLAIMS,
        exact_keys=True,
    ):
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
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_specification_validation()
    text, error = _read_text(
        request[
            "governing_presence_re_evaluation_operation_specification_path"
        ]
    )
    if error is not None or text is None:
        _add_failure(
            checks,
            "specification.reference",
            "SPECIFICATION_REFERENCE_MISSING",
        )
        return (
            "SPECIFICATION_REFERENCE_MISSING",
            "governing presence re-evaluation operation specification is unavailable",
            state,
        )
    checks.append(_check("specification.reference", True))
    for name, marker in SPEC_REQUIRED_MARKERS:
        valid = marker in text
        state["marker_validation"][name] = valid
        checks.append(
            _check(
                "specification." + name,
                valid,
                "SPECIFICATION_MARKER_MISSING",
                expected=marker,
            )
        )
        if not valid:
            return (
                "SPECIFICATION_MARKER_MISSING",
                "governing specification marker is missing: " + name,
                state,
            )
    state["specification_validated"] = True
    return None, None, state


def _empty_artifact_validation(path: Path) -> dict[str, Any]:
    return {
        "artifact_path": str(path),
        "artifact_validated": False,
        "metadata_validated": False,
        "identity_validated": False,
        "result_validated": False,
        "completion_validated": False,
        "cardinality_validated": False,
        "false_locks_validated": False,
        "standing": {},
        "condition_postures": {},
    }


def _artifact_read_failure(
    checks: list[dict[str, Any]],
    prefix: str,
    error: str | None,
    missing_code: str,
    parse_code: str,
    duplicate_code: str,
) -> tuple[str, str]:
    if error == "duplicate_key":
        code = duplicate_code
        reason = prefix + " artifact contains duplicate JSON keys"
    elif error == "not_parseable":
        code = parse_code
        reason = prefix + " artifact is not parseable JSON"
    else:
        code = missing_code
        reason = prefix + " artifact is unavailable"
    _add_failure(checks, prefix + ".strict_json", code)
    return code, reason


def _validate_boundary_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_artifact_validation(BOUNDARY_ARTIFACT_RELATIVE_PATH)
    artifact, error = _read_json(
        request["presence_re_evaluation_boundary_artifact_path"]
    )
    if error is not None:
        code, reason = _artifact_read_failure(
            checks,
            "boundary",
            error,
            "BOUNDARY_ARTIFACT_MISSING",
            "BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            "BOUNDARY_ARTIFACT_DUPLICATE_KEYED",
        )
        return code, reason, state
    if not isinstance(artifact, Mapping):
        _add_failure(
            checks, "boundary.mapping", "BOUNDARY_ARTIFACT_NOT_MAPPING"
        )
        return (
            "BOUNDARY_ARTIFACT_NOT_MAPPING",
            "boundary artifact is not a mapping",
            state,
        )
    boundary = artifact.get("presence_re_evaluation_boundary")
    summary = artifact.get("presence_re_evaluation_boundary_summary")
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (boundary, summary, block, non_claims)
    ):
        _add_failure(
            checks,
            "boundary.sections",
            "BOUNDARY_ARTIFACT_SECTION_MISSING",
        )
        return (
            "BOUNDARY_ARTIFACT_SECTION_MISSING",
            "boundary artifact lacks canonical bounded sections",
            state,
        )
    checks.append(_check("boundary.strict_json_mapping", True))
    start = len(checks)
    metadata_valid = _expect_fields(
        checks,
        "boundary.wrapper",
        artifact,
        {
            "resolver_module": BOUNDARY_RESOLVER_MODULE,
            "result_version": BOUNDARY_RESULT_VERSION,
            "outcome": BOUNDARY_OUTCOME_REQUIRED,
            "boundary_result": BOUNDARY_RESULT_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": BOUNDARY_PASSED_CHECK_COUNT,
            "completed_consideration_posture_count": (
                BOUNDARY_COMPLETED_CONSIDERATION_POSTURE_COUNT
            ),
            "result_level_non_claims_canonical_false": True,
        },
        "BOUNDARY_METADATA_MISMATCH",
    )
    identity_valid = _expect_fields(
        checks,
        "boundary.object",
        boundary,
        {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "presence_re_evaluation_boundary_id": BOUNDARY_ID,
            "presence_re_evaluation_boundary_type": BOUNDARY_TYPE,
            "presence_re_evaluation_boundary_version": BOUNDARY_VERSION,
            "presence_re_evaluation_boundary_scope": BOUNDARY_SCOPE,
        },
        "BOUNDARY_IDENTITY_MISMATCH",
    )
    result_valid = _expect_fields(
        checks,
        "boundary.result",
        boundary,
        {
            "presence_re_evaluation_boundary_result": (
                BOUNDARY_RESULT_REQUIRED
            ),
            "presence_re_evaluation_boundary_recorded": True,
            "presence_re_evaluation_boundary_result_recorded": True,
            "presence_re_evaluation_boundary_exhausted": True,
            "presence_re_evaluation_operation_consideration_allowed": True,
            "presence_re_evaluation_operation_consideration_not_allowed": False,
            "completed_consideration_posture_count": (
                BOUNDARY_COMPLETED_CONSIDERATION_POSTURE_COUNT
            ),
        },
        "BOUNDARY_COMPLETION_MISMATCH",
    )
    block_valid = _matches_exact(block.get("blocked"), False)
    checks.append(
        _check(
            "boundary.blocked",
            block_valid,
            "BOUNDARY_BLOCKED",
            expected=False,
        )
    )
    non_claims_valid = _canonical_false_mapping_valid(non_claims)
    checks.append(
        _check(
            "boundary.non_claims",
            non_claims_valid,
            "BOUNDARY_COMPLETION_MISMATCH",
        )
    )
    failure = _first_failure(checks, start)
    if failure is not None:
        if failure == "BOUNDARY_METADATA_MISMATCH" and not _matches_exact(
            artifact.get("failed_check_count"), 0
        ):
            failure = "BOUNDARY_FAILED_CHECKS_PRESENT"
        return failure, "boundary artifact standing is not exact", state
    state.update(
        {
            "artifact_validated": True,
            "metadata_validated": metadata_valid,
            "identity_validated": identity_valid,
            "result_validated": result_valid,
            "completion_validated": result_valid,
            "cardinality_validated": True,
            "false_locks_validated": non_claims_valid,
            "standing": {
                "boundary_id": BOUNDARY_ID,
                "boundary_type": BOUNDARY_TYPE,
                "boundary_version": BOUNDARY_VERSION,
                "boundary_scope": BOUNDARY_SCOPE,
                "outcome": BOUNDARY_OUTCOME_REQUIRED,
                "boundary_result": BOUNDARY_RESULT_REQUIRED,
                "boundary_recorded": True,
                "boundary_exhausted": True,
                "consideration_allowed": True,
                "completed_consideration_posture_count": 1,
            },
        }
    )
    return None, None, state


def _validate_prior_presence_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_artifact_validation(PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH)
    artifact, error = _read_json(
        request["prior_presence_operation_artifact_path"]
    )
    if error is not None:
        code, reason = _artifact_read_failure(
            checks,
            "prior_presence",
            error,
            "PRIOR_PRESENCE_ARTIFACT_MISSING",
            "PRIOR_PRESENCE_ARTIFACT_NOT_PARSEABLE",
            "PRIOR_PRESENCE_ARTIFACT_DUPLICATE_KEYED",
        )
        return code, reason, state
    if not isinstance(artifact, Mapping):
        _add_failure(
            checks,
            "prior_presence.mapping",
            "PRIOR_PRESENCE_ARTIFACT_NOT_MAPPING",
        )
        return (
            "PRIOR_PRESENCE_ARTIFACT_NOT_MAPPING",
            "prior presence artifact is not a mapping",
            state,
        )
    operation = artifact.get("presence_operation")
    summary = artifact.get("presence_operation_summary")
    block = artifact.get("block")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, block)
    ):
        _add_failure(
            checks,
            "prior_presence.sections",
            "PRIOR_PRESENCE_ARTIFACT_SECTION_MISSING",
        )
        return (
            "PRIOR_PRESENCE_ARTIFACT_SECTION_MISSING",
            "prior presence artifact lacks canonical bounded sections",
            state,
        )
    checks.append(_check("prior_presence.strict_json_mapping", True))
    start = len(checks)
    metadata_valid = _expect_fields(
        checks,
        "prior_presence.wrapper",
        artifact,
        {
            "resolver_module": PRIOR_PRESENCE_RESOLVER_MODULE,
            "result_version": PRIOR_PRESENCE_RESULT_VERSION,
            "outcome": PRIOR_PRESENCE_OUTCOME_REQUIRED,
        },
        "PRIOR_PRESENCE_METADATA_MISMATCH",
    ) and _expect_fields(
        checks,
        "prior_presence.summary",
        summary,
        {
            "outcome": PRIOR_PRESENCE_OUTCOME_REQUIRED,
            "presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": PRIOR_PRESENCE_PASSED_CHECK_COUNT,
        },
        "PRIOR_PRESENCE_METADATA_MISMATCH",
    )
    identity_valid = _expect_fields(
        checks,
        "prior_presence.operation_identity",
        operation,
        {
            "operation_id": PRIOR_PRESENCE_OPERATION_ID,
            "operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
            "operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
            "operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
            "presence_operation_id": PRIOR_PRESENCE_OPERATION_ID,
            "presence_operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
            "presence_operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
            "presence_operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
        },
        "PRIOR_PRESENCE_IDENTITY_MISMATCH",
    )
    result_valid = _expect_fields(
        checks,
        "prior_presence.operation_result",
        operation,
        {
            "presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
            "presence_operation_recorded": True,
            "presence_evaluation_performed": True,
            "presence_result_recorded": True,
            "receiver_attested": False,
            "receiver_answerable_receipt_present": False,
            "receiver_answerable_basis_custody_distinct": False,
            "receiver_answerable_basis_refusable": False,
            "receiver_answerable_basis_could_have_been_withheld": False,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "presence_recorded": False,
        },
        "PRIOR_PRESENCE_POSTURE_MISMATCH",
    )
    block_valid = _matches_exact(block.get("blocked"), False)
    checks.append(
        _check(
            "prior_presence.blocked",
            block_valid,
            "PRIOR_PRESENCE_BLOCKED",
            expected=False,
        )
    )
    failure = _first_failure(checks, start)
    if failure is not None:
        if failure == "PRIOR_PRESENCE_METADATA_MISMATCH" and not _matches_exact(
            summary.get("failed_check_count"), 0
        ):
            failure = "PRIOR_PRESENCE_FAILED_CHECKS_PRESENT"
        return failure, "prior presence artifact standing is not exact", state
    condition_postures = {
        field: (
            operation.get(field)
            if type(operation.get(field)) is bool
            else None
        )
        for field in CONDITION_KEYS
    }
    standing = {
        "operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
        "operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
        "outcome": PRIOR_PRESENCE_OUTCOME_REQUIRED,
        "presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
        "presence_operation_recorded": True,
        "presence_evaluation_performed": True,
        "presence_result_recorded": True,
        "presence_supported": False,
        "presence_authorized": False,
        "presence_established": False,
        "presence_recorded": False,
    }
    state.update(
        {
            "artifact_validated": True,
            "metadata_validated": metadata_valid,
            "identity_validated": identity_valid,
            "result_validated": result_valid,
            "completion_validated": result_valid,
            "cardinality_validated": True,
            "false_locks_validated": result_valid,
            "standing": standing,
            "condition_postures": condition_postures,
        }
    )
    return None, None, state


def _validate_receiver_attestation_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_artifact_validation(
        RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
    )
    artifact, error = _read_json(
        request["receiver_attestation_operation_artifact_path"]
    )
    if error is not None:
        code, reason = _artifact_read_failure(
            checks,
            "receiver_attestation",
            error,
            "RECEIVER_ATTESTATION_ARTIFACT_MISSING",
            "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
            "RECEIVER_ATTESTATION_ARTIFACT_DUPLICATE_KEYED",
        )
        return code, reason, state
    if not isinstance(artifact, Mapping):
        _add_failure(
            checks,
            "receiver_attestation.mapping",
            "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
        )
        return (
            "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
            "receiver-attestation artifact is not a mapping",
            state,
        )
    operation = artifact.get(
        "receiver_side_answerable_basis_receiver_attestation_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_receiver_attestation_operation_summary"
    )
    detail = artifact.get("operation_result_detail")
    components = artifact.get("bounded_component_validation")
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (
            operation,
            summary,
            detail,
            components,
            block,
            non_claims,
        )
    ):
        _add_failure(
            checks,
            "receiver_attestation.sections",
            "RECEIVER_ATTESTATION_ARTIFACT_SECTION_MISSING",
        )
        return (
            "RECEIVER_ATTESTATION_ARTIFACT_SECTION_MISSING",
            "receiver-attestation artifact lacks canonical bounded sections",
            state,
        )
    checks.append(_check("receiver_attestation.strict_json_mapping", True))
    start = len(checks)
    metadata_valid = _expect_fields(
        checks,
        "receiver_attestation.wrapper",
        artifact,
        {
            "resolver_module": RECEIVER_ATTESTATION_RESOLVER_MODULE,
            "result_version": RECEIVER_ATTESTATION_RESULT_VERSION,
            "outcome": RECEIVER_ATTESTATION_OUTCOME_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": RECEIVER_ATTESTATION_PASSED_CHECK_COUNT,
        },
        "RECEIVER_ATTESTATION_METADATA_MISMATCH",
    )
    identity_valid = _expect_fields(
        checks,
        "receiver_attestation.identity",
        operation,
        {
            "operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
            "operation_type": RECEIVER_ATTESTATION_OPERATION_TYPE,
            "operation_version": RECEIVER_ATTESTATION_OPERATION_VERSION,
            "operation_scope": RECEIVER_ATTESTATION_OPERATION_SCOPE,
            "receiver_side_answerable_basis_candidate_id": (
                RECEIVER_ATTESTATION_SELECTED_CANDIDATE_ID
            ),
            "selected_candidate_sufficiency_operation_id": (
                RECEIVER_ATTESTATION_SELECTED_SUFFICIENCY_OPERATION_ID
            ),
            "selected_candidate_sufficiency_operation_result_required": (
                RECEIVER_ATTESTATION_SELECTED_SUFFICIENCY_RESULT_REQUIRED
            ),
        },
        "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
    )
    result_valid = _expect_fields(
        checks,
        "receiver_attestation.result",
        operation,
        {
            "receiver_attestation_operation_result": (
                RECEIVER_ATTESTATION_RESULT_REQUIRED
            ),
            "operation_basis_supplied": True,
            "operation_basis_admitted": True,
            "receiver_attestation_decided": True,
            "receiver_attestation_recorded": True,
            "receiver_attestation_operation_recorded": True,
            "receiver_attestation_operation_result_recorded": True,
            "receiver_attestation_operation_exhausted": True,
            "receiver_attestation_not_recorded": False,
            "receiver_attestation_indeterminate": False,
        },
        "RECEIVER_ATTESTATION_COMPLETION_MISMATCH",
    )
    cardinality_valid = _expect_fields(
        checks,
        "receiver_attestation.detail",
        detail,
        {
            "operation_result": RECEIVER_ATTESTATION_RESULT_REQUIRED,
            "completed_result_posture_count": (
                RECEIVER_ATTESTATION_COMPLETED_RESULT_POSTURE_COUNT
            ),
        },
        "RECEIVER_ATTESTATION_CARDINALITY_MISMATCH",
    )
    compact_valid = _expect_fields(
        checks,
        "receiver_attestation.summary",
        summary,
        {
            "operation_result": RECEIVER_ATTESTATION_RESULT_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": RECEIVER_ATTESTATION_PASSED_CHECK_COUNT,
            "blocked": False,
            "basis_supplied": True,
            "basis_admitted": True,
            "receiver_attestation_recorded": True,
            "receiver_attestation_operation_recorded": True,
            "receiver_attestation_operation_exhausted": True,
            "result_level_non_claims_canonical_false": True,
        },
        "RECEIVER_ATTESTATION_RESULT_MISMATCH",
    ) and _expect_fields(
        checks,
        "receiver_attestation.components",
        components,
        {
            "minimum_admission_checks_passed": True,
            "archive_bytes_omitted": True,
            "hash_record_body_omitted": True,
            "text_component_bodies_omitted": True,
            "recorded_signal_body_omitted": True,
            "text_components_validated": True,
            "timestamp_validated": True,
            "trace_paths_validated": True,
            "recorded_signal_artifact_existence_validated": True,
        },
        "RECEIVER_ATTESTATION_RESULT_MISMATCH",
    )
    block_valid = _matches_exact(block.get("blocked"), False)
    checks.append(
        _check(
            "receiver_attestation.blocked",
            block_valid,
            "RECEIVER_ATTESTATION_BLOCKED",
            expected=False,
        )
    )
    false_locks_valid = _expect_fields(
        checks,
        "receiver_attestation.false_lock",
        operation,
        {field: False for field in ATTESTATION_REQUIRED_FALSE_POSTURES},
        "RECEIVER_ATTESTATION_FALSE_LOCK_MISMATCH",
    ) and _canonical_false_mapping_valid(
        non_claims, ATTESTATION_REQUIRED_FALSE_POSTURES
    )
    checks.append(
        _check(
            "receiver_attestation.non_claims",
            _canonical_false_mapping_valid(
                non_claims, ATTESTATION_REQUIRED_FALSE_POSTURES
            ),
            "RECEIVER_ATTESTATION_FALSE_LOCK_MISMATCH",
        )
    )
    failure = _first_failure(checks, start)
    if failure is not None:
        if (
            failure == "RECEIVER_ATTESTATION_METADATA_MISMATCH"
            and not _matches_exact(artifact.get("failed_check_count"), 0)
        ):
            failure = "RECEIVER_ATTESTATION_FAILED_CHECKS_PRESENT"
        return (
            failure,
            "receiver-attestation artifact standing is not exact",
            state,
        )
    condition_postures = {
        field: (
            operation.get(field)
            if field in operation and type(operation.get(field)) is bool
            else None
        )
        for field in CONDITION_KEYS
    }
    standing = {
        "operation_id": RECEIVER_ATTESTATION_OPERATION_ID,
        "operation_type": RECEIVER_ATTESTATION_OPERATION_TYPE,
        "operation_version": RECEIVER_ATTESTATION_OPERATION_VERSION,
        "operation_scope": RECEIVER_ATTESTATION_OPERATION_SCOPE,
        "outcome": RECEIVER_ATTESTATION_OUTCOME_REQUIRED,
        "operation_result": RECEIVER_ATTESTATION_RESULT_REQUIRED,
        "operation_basis_supplied": True,
        "operation_basis_admitted": True,
        "receiver_attestation_recorded": True,
        "operation_recorded": True,
        "operation_result_recorded": True,
        "operation_exhausted": True,
        "completed_result_posture_count": 1,
        "selected_candidate_id": RECEIVER_ATTESTATION_SELECTED_CANDIDATE_ID,
        "selected_sufficiency_operation_id": (
            RECEIVER_ATTESTATION_SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_sufficiency_result_required": (
            RECEIVER_ATTESTATION_SELECTED_SUFFICIENCY_RESULT_REQUIRED
        ),
        "downstream_false_locks_preserved": True,
    }
    state.update(
        {
            "artifact_validated": True,
            "metadata_validated": metadata_valid,
            "identity_validated": identity_valid,
            "result_validated": result_valid and compact_valid,
            "completion_validated": result_valid,
            "cardinality_validated": cardinality_valid,
            "false_locks_validated": false_locks_valid,
            "standing": standing,
            "condition_postures": condition_postures,
        }
    )
    return None, None, state


def _validate_receiver_answerable_receipt_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_artifact_validation(
        RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
    )
    artifact, error = _read_json(
        request["receiver_answerable_receipt_operation_artifact_path"]
    )
    if error is not None:
        code, reason = _artifact_read_failure(
            checks,
            "receipt",
            error,
            "RECEIPT_ARTIFACT_MISSING",
            "RECEIPT_ARTIFACT_NOT_PARSEABLE",
            "RECEIPT_ARTIFACT_DUPLICATE_KEYED",
        )
        return code, reason, state
    if not isinstance(artifact, Mapping):
        _add_failure(checks, "receipt.mapping", "RECEIPT_ARTIFACT_NOT_MAPPING")
        return (
            "RECEIPT_ARTIFACT_NOT_MAPPING",
            "receiver-answerable-receipt artifact is not a mapping",
            state,
        )
    operation = artifact.get(
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_summary"
    )
    detail = artifact.get("operation_result_detail")
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, detail, block, non_claims)
    ):
        _add_failure(
            checks, "receipt.sections", "RECEIPT_ARTIFACT_SECTION_MISSING"
        )
        return (
            "RECEIPT_ARTIFACT_SECTION_MISSING",
            "receipt artifact lacks canonical bounded sections",
            state,
        )
    checks.append(_check("receipt.strict_json_mapping", True))
    start = len(checks)
    metadata_valid = _expect_fields(
        checks,
        "receipt.wrapper",
        artifact,
        {
            "resolver_module": RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE,
            "result_version": RECEIVER_ANSWERABLE_RECEIPT_RESULT_VERSION,
            "outcome": RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED,
            "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT,
            "result_level_non_claims_canonical_false": True,
        },
        "RECEIPT_METADATA_MISMATCH",
    )
    identity_valid = _expect_fields(
        checks,
        "receipt.identity",
        operation,
        {
            "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
            "operation_type": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
            "operation_version": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
            "operation_scope": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
            "selected_receiver_attestation_operation_id": (
                RECEIVER_ATTESTATION_OPERATION_ID
            ),
            "selected_receiver_attestation_operation_type": (
                RECEIVER_ATTESTATION_OPERATION_TYPE
            ),
            "selected_receiver_attestation_operation_version": (
                RECEIVER_ATTESTATION_OPERATION_VERSION
            ),
            "selected_receiver_attestation_operation_scope": (
                RECEIVER_ATTESTATION_OPERATION_SCOPE
            ),
            "selected_receiver_attestation_operation_result_required": (
                RECEIVER_ATTESTATION_RESULT_REQUIRED
            ),
            "receiver_side_answerable_basis_candidate_id": (
                RECEIVER_ATTESTATION_SELECTED_CANDIDATE_ID
            ),
        },
        "RECEIPT_IDENTITY_MISMATCH",
    )
    result_valid = _expect_fields(
        checks,
        "receipt.result",
        operation,
        {
            "receiver_answerable_receipt_operation_result": (
                RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED
            ),
            "operation_basis_supplied": True,
            "operation_basis_admitted": True,
            "receiver_answerable_receipt_decided": True,
            "receiver_answerable_receipt_recorded": True,
            "receiver_answerable_receipt_present": True,
            "receiver_answerable_receipt_operation_recorded": True,
            "receiver_answerable_receipt_operation_result_recorded": True,
            "receiver_answerable_receipt_operation_exhausted": True,
            "receiver_answerable_receipt_not_recorded": False,
            "receiver_answerable_receipt_indeterminate": False,
        },
        "RECEIPT_COMPLETION_MISMATCH",
    )
    cardinality_valid = _expect_fields(
        checks,
        "receipt.detail",
        detail,
        {
            "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
            "completed_result_posture_count": (
                RECEIVER_ANSWERABLE_RECEIPT_COMPLETED_RESULT_POSTURE_COUNT
            ),
        },
        "RECEIPT_CARDINALITY_MISMATCH",
    )
    summary_valid = _expect_fields(
        checks,
        "receipt.summary",
        summary,
        {
            "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT,
            "blocked": False,
            "operation_basis_supplied": True,
            "operation_basis_admitted": True,
            "receiver_answerable_receipt_recorded": True,
            "receiver_answerable_receipt_present": True,
            "receiver_answerable_receipt_operation_recorded": True,
            "receiver_answerable_receipt_operation_result_recorded": True,
            "receiver_answerable_receipt_operation_exhausted": True,
            "result_level_non_claims_canonical_false": True,
        },
        "RECEIPT_RESULT_MISMATCH",
    )
    block_valid = _matches_exact(block.get("blocked"), False)
    checks.append(
        _check(
            "receipt.blocked",
            block_valid,
            "RECEIPT_BLOCKED",
            expected=False,
        )
    )
    false_locks_valid = _expect_fields(
        checks,
        "receipt.false_lock",
        operation,
        {field: False for field in RECEIPT_REQUIRED_FALSE_POSTURES},
        "RECEIPT_FALSE_LOCK_MISMATCH",
    ) and _canonical_false_mapping_valid(
        non_claims, RECEIPT_REQUIRED_FALSE_POSTURES
    )
    checks.append(
        _check(
            "receipt.non_claims",
            _canonical_false_mapping_valid(
                non_claims, RECEIPT_REQUIRED_FALSE_POSTURES
            ),
            "RECEIPT_FALSE_LOCK_MISMATCH",
        )
    )
    failure = _first_failure(checks, start)
    if failure is not None:
        if failure == "RECEIPT_METADATA_MISMATCH" and not _matches_exact(
            artifact.get("failed_check_count"), 0
        ):
            failure = "RECEIPT_FAILED_CHECKS_PRESENT"
        return failure, "receipt artifact standing is not exact", state
    condition_postures = {
        field: (
            operation.get(field)
            if field in operation and type(operation.get(field)) is bool
            else None
        )
        for field in CONDITION_KEYS
    }
    standing = {
        "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
        "operation_type": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
        "operation_version": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
        "operation_scope": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
        "outcome": RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED,
        "operation_result": RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED,
        "operation_basis_supplied": True,
        "operation_basis_admitted": True,
        "receiver_answerable_receipt_decided": True,
        "receiver_answerable_receipt_recorded": True,
        "receiver_answerable_receipt_present": True,
        "operation_recorded": True,
        "operation_result_recorded": True,
        "operation_exhausted": True,
        "completed_result_posture_count": 1,
        "selected_receiver_attestation_operation_id": (
            RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_candidate_id": RECEIVER_ATTESTATION_SELECTED_CANDIDATE_ID,
        "downstream_false_locks_preserved": True,
    }
    state.update(
        {
            "artifact_validated": True,
            "metadata_validated": metadata_valid,
            "identity_validated": identity_valid,
            "result_validated": result_valid and summary_valid,
            "completion_validated": result_valid,
            "cardinality_validated": cardinality_valid,
            "false_locks_validated": false_locks_valid,
            "standing": standing,
            "condition_postures": condition_postures,
        }
    )
    return None, None, state


def _default_condition_evaluations() -> dict[str, dict[str, Any]]:
    return {
        field: {
            "historical_prior_value": None,
            "later_compact_standing": {
                "receiver_attestation_value": None,
                "receiver_answerable_receipt_value": None,
            },
            "required_successor_value": required,
            "evaluation": EVALUATION_NOT_EVALUATED,
            "successor_value": False,
            "compact_evidence_code": "OPERATION_BASIS_NOT_ADMITTED",
            "reason": "condition was not evaluated because operation basis was not admitted",
        }
        for field, required in CONDITION_REQUIREMENTS.items()
    }


def _evaluate_conditions(
    prior: Mapping[str, Any],
    attestation: Mapping[str, Any],
    receipt: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    prior_conditions = prior.get("condition_postures")
    attestation_conditions = attestation.get("condition_postures")
    receipt_conditions = receipt.get("condition_postures")
    prior_conditions = (
        prior_conditions if isinstance(prior_conditions, Mapping) else {}
    )
    attestation_conditions = (
        attestation_conditions
        if isinstance(attestation_conditions, Mapping)
        else {}
    )
    receipt_conditions = (
        receipt_conditions if isinstance(receipt_conditions, Mapping) else {}
    )
    attestation_standing = attestation.get("standing")
    receipt_standing = receipt.get("standing")
    attestation_standing = (
        attestation_standing
        if isinstance(attestation_standing, Mapping)
        else {}
    )
    receipt_standing = (
        receipt_standing if isinstance(receipt_standing, Mapping) else {}
    )
    evaluations: dict[str, dict[str, Any]] = {}
    for field, required in CONDITION_REQUIREMENTS.items():
        historical = prior_conditions.get(field)
        later_attestation = attestation_conditions.get(field)
        later_receipt = receipt_conditions.get(field)
        if field == "receiver_attested":
            evaluation = (
                EVALUATION_SATISFIED
                if attestation_standing.get("receiver_attestation_recorded")
                is True
                else EVALUATION_REQUIRES_BASIS
            )
            evidence_code = (
                "EXACT_RECORDED_RECEIVER_ATTESTATION"
                if evaluation == EVALUATION_SATISFIED
                else "RECEIVER_ATTESTATION_NOT_ESTABLISHED"
            )
            reason = (
                "exact recorded receiver-attestation result establishes "
                "receiver_attested"
                if evaluation == EVALUATION_SATISFIED
                else "exact compact basis does not establish receiver attestation"
            )
        elif field == "receiver_answerable_receipt_present":
            evaluation = (
                EVALUATION_SATISFIED
                if receipt_standing.get("receiver_answerable_receipt_present")
                is True
                else EVALUATION_REQUIRES_BASIS
            )
            evidence_code = (
                "EXACT_RECORDED_RECEIVER_ANSWERABLE_RECEIPT"
                if evaluation == EVALUATION_SATISFIED
                else "RECEIVER_ANSWERABLE_RECEIPT_NOT_ESTABLISHED"
            )
            reason = (
                "exact recorded receiver-answerable-receipt result establishes "
                "receipt presence"
                if evaluation == EVALUATION_SATISFIED
                else "exact compact basis does not establish receipt presence"
            )
        else:
            exact_values = [
                value
                for value in (later_attestation, later_receipt)
                if type(value) is bool
            ]
            if (
                len(exact_values) == 2
                and exact_values[0] is not exact_values[1]
            ):
                evaluation = EVALUATION_INDETERMINATE
                evidence_code = "COMPACT_LATER_STANDING_CONFLICTS"
                reason = (
                    "exact admitted later compact standing conflicts for "
                    + field
                )
            elif (
                len(exact_values) == 2
                and all(value is required for value in exact_values)
            ):
                evaluation = EVALUATION_SATISFIED
                evidence_code = "EXACT_LATER_FALSE_OR_TRUE_LOCK_PRESERVED"
                reason = (
                    "both exact later compact results preserve the required "
                    "successor value"
                )
            else:
                evaluation = EVALUATION_REQUIRES_BASIS
                evidence_code = "EXACT_SUCCESSOR_CONDITION_NOT_ESTABLISHED"
                reason = (
                    "admitted compact basis does not establish the required "
                    "successor value; receipt and attestation are not converted "
                    "into this condition"
                )
        successor_value = (
            required if evaluation == EVALUATION_SATISFIED else False
        )
        evaluations[field] = {
            "historical_prior_value": (
                historical if type(historical) is bool else None
            ),
            "later_compact_standing": {
                "receiver_attestation_value": (
                    later_attestation
                    if type(later_attestation) is bool
                    else None
                ),
                "receiver_answerable_receipt_value": (
                    later_receipt if type(later_receipt) is bool else None
                ),
            },
            "required_successor_value": required,
            "evaluation": evaluation,
            "successor_value": successor_value,
            "compact_evidence_code": evidence_code,
            "reason": reason,
        }
    return evaluations


def _outcome_from_evaluations(
    evaluations: Mapping[str, Mapping[str, Any]],
) -> str:
    values = [evaluations[field].get("evaluation") for field in CONDITION_KEYS]
    if any(value == EVALUATION_INDETERMINATE for value in values):
        return OUTCOME_INDETERMINATE
    if any(value == EVALUATION_REQUIRES_BASIS for value in values):
        return OUTCOME_REQUIRES_BASIS
    if all(value == EVALUATION_SATISFIED for value in values):
        return OUTCOME_SUPPORTED
    return OUTCOME_BLOCKED


def _result_for_outcome(outcome: str) -> str:
    if outcome == OUTCOME_SUPPORTED:
        return RESULT_SUPPORTED
    if outcome == OUTCOME_REQUIRES_BASIS:
        return RESULT_REQUIRES_BASIS
    if outcome == OUTCOME_INDETERMINATE:
        return RESULT_INDETERMINATE
    return RESULT_NOT_EVALUATED


def _decision_for_outcome(
    outcome: str,
    *,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    if outcome == OUTCOME_SUPPORTED:
        decision_code = DECISION_CODE_SUPPORTED
        decision_reason = DECISION_REASON_SUPPORTED
    elif outcome == OUTCOME_REQUIRES_BASIS:
        decision_code = DECISION_CODE_REQUIRES_BASIS
        decision_reason = DECISION_REASON_REQUIRES_BASIS
    elif outcome == OUTCOME_INDETERMINATE:
        decision_code = DECISION_CODE_INDETERMINATE
        decision_reason = DECISION_REASON_INDETERMINATE
    else:
        decision_code = code
        decision_reason = reason
    return {
        "decision_code": decision_code,
        "decision_reason": decision_reason,
        "decision_evaluated": outcome != OUTCOME_BLOCKED,
        "result_precedence": [
            OUTCOME_BLOCKED,
            OUTCOME_INDETERMINATE,
            OUTCOME_REQUIRES_BASIS,
            OUTCOME_SUPPORTED,
        ],
    }


def _branch_posture(outcome: str) -> dict[str, Any]:
    completed = outcome in {
        OUTCOME_SUPPORTED,
        OUTCOME_REQUIRES_BASIS,
        OUTCOME_INDETERMINATE,
    }
    return {
        "presence_re_evaluation_performed": completed,
        "successor_presence_result_decided": completed,
        "successor_presence_result_recorded": completed,
        "presence_re_evaluation_operation_recorded": completed,
        "presence_re_evaluation_operation_result_recorded": completed,
        "presence_re_evaluation_operation_exhausted": completed,
        "completed_successor_result_posture_count": int(completed),
    }


def _operation_basis_supplied(request: Mapping[str, Any]) -> bool:
    fields = (
        "presence_re_evaluation_boundary_artifact_path",
        "prior_presence_operation_artifact_path",
        "receiver_attestation_operation_artifact_path",
        "receiver_answerable_receipt_operation_artifact_path",
    )
    return all(
        isinstance(request.get(field), str) and bool(request.get(field))
        for field in fields
    )


def _empty_atomic_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "operation_basis_supplied": _operation_basis_supplied(request),
        "boundary_artifact_validated": False,
        "prior_presence_artifact_validated": False,
        "receiver_attestation_artifact_validated": False,
        "receiver_answerable_receipt_artifact_validated": False,
        "all_four_exact_artifacts_validated": False,
        "operation_basis_admitted": False,
        "partial_basis_cannot_produce_successor_result": True,
    }


def _declared_request_posture(
    request: Mapping[str, Any],
) -> dict[str, bool]:
    return {
        "intent_validated": request.get("intent") == INTENT_RECORD,
        "canonical_identity_and_paths_validated": all(
            request.get(field) == expected
            for field, expected in _identity_request_values().items()
        ),
        "presence_re_evaluation_execution_selected": (
            type(request.get("presence_re_evaluation_execution_selected"))
            is bool
            and request.get("presence_re_evaluation_execution_selected")
            is True
        ),
        "declared_non_claims_validated": _canonical_false_mapping_valid(
            request.get("declared_non_claims"),
            REQUIRED_FALSE_NON_CLAIMS,
            exact_keys=True,
        ),
        "unknown_request_fields_absent": not bool(
            set(request).difference(_canonical_request_keys())
        ),
        "result_and_condition_preclaims_absent": not bool(
            set(request).intersection(PROHIBITED_PRECLAIM_FIELDS)
        ),
    }


def _what_remains_open(
    outcome: str,
    missing: Sequence[str],
    indeterminate: Sequence[str],
) -> list[str]:
    open_items: list[str] = []
    if outcome == OUTCOME_REQUIRES_BASIS:
        open_items.extend(
            "receiver-side basis for " + field for field in missing
        )
    elif outcome == OUTCOME_INDETERMINATE:
        open_items.extend(
            "lawful classification of " + field for field in indeterminate
        )
    if outcome != OUTCOME_SUPPORTED:
        open_items.extend(
            [
                "successor presence support",
                "successor presence authorization",
                "successor presence establishment",
                "successor presence recording",
            ]
        )
    open_items.extend(
        [
            "separately bounded presence-lapse handling after any supported presence",
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
    return open_items


def _operation_object(
    request: Mapping[str, Any],
    outcome: str,
    operation_result: str,
    atomic_basis: Mapping[str, Any],
    evaluations: Mapping[str, Mapping[str, Any]],
    missing: Sequence[str],
    indeterminate: Sequence[str],
) -> dict[str, Any]:
    branch = _branch_posture(outcome)
    supported = outcome == OUTCOME_SUPPORTED
    requires_basis = outcome == OUTCOME_REQUIRES_BASIS
    is_indeterminate = outcome == OUTCOME_INDETERMINATE
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "presence_re_evaluation_operation_id": OPERATION_ID,
        "presence_re_evaluation_operation_type": OPERATION_TYPE,
        "presence_re_evaluation_operation_version": OPERATION_VERSION,
        "presence_re_evaluation_operation_scope": OPERATION_SCOPE,
        "presence_re_evaluation_execution_selected": (
            request.get("presence_re_evaluation_execution_selected") is True
        ),
        "operation_basis_supplied": atomic_basis.get(
            "operation_basis_supplied"
        )
        is True,
        "operation_basis_admitted": atomic_basis.get(
            "operation_basis_admitted"
        )
        is True,
        **branch,
        "presence_re_evaluation_operation_result": operation_result,
        "successor_presence_result": operation_result,
        "presence_supported": supported,
        "presence_authorized": supported,
        "presence_established": supported,
        "presence_recorded": supported,
        "presence_re_evaluation_operation_requires_receiver_answerable_basis": (
            requires_basis
        ),
        "receiver_answerable_basis_required": requires_basis,
        "presence_re_evaluation_indeterminate": is_indeterminate,
        "missing_or_insufficient_receiver_answerable_basis": list(missing),
        "indeterminate_receiver_answerable_basis_conditions": list(
            indeterminate
        ),
        **{
            field: (
                evaluations.get(field, {}).get("successor_value") is True
            )
            for field in CONDITION_KEYS
        },
        **_canonical_lineage_posture(),
        **_canonical_perishability_posture(outcome),
        **_canonical_non_claims(),
    }
    return operation


def _successor_posture(operation: Mapping[str, Any]) -> dict[str, Any]:
    fields = (
        "successor_presence_result",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "presence_re_evaluation_operation_requires_receiver_answerable_basis",
        "receiver_answerable_basis_required",
        "presence_re_evaluation_indeterminate",
        "presence_re_evaluation_performed",
        "successor_presence_result_decided",
        "successor_presence_result_recorded",
        "successor_presence_result_additive",
        "successor_presence_result_time_scope_bounded",
        "successor_presence_is_retroactive_presence",
        "completed_successor_result_posture_count",
    )
    return {
        **{field: copy.deepcopy(operation.get(field)) for field in fields},
        "condition_values": {
            field: operation.get(field) for field in CONDITION_KEYS
        },
    }


def _append_completed_checks(
    checks: list[dict[str, Any]],
    outcome: str,
    evaluations: Mapping[str, Mapping[str, Any]],
    missing: Sequence[str],
    indeterminate: Sequence[str],
    route: str | None,
) -> None:
    for field in CONDITION_KEYS:
        evaluation = evaluations[field].get("evaluation")
        checks.append(
            _check(
                "condition." + field + ".classified",
                evaluation
                in {
                    EVALUATION_SATISFIED,
                    EVALUATION_REQUIRES_BASIS,
                    EVALUATION_INDETERMINATE,
                },
                "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
            )
        )
    checks.append(
        _check(
            "condition.precedence",
            _outcome_from_evaluations(evaluations) == outcome,
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    checks.append(
        _check(
            "condition.missing_basis_list",
            list(missing)
            == [
                field
                for field in CONDITION_KEYS
                if evaluations[field].get("evaluation")
                == EVALUATION_REQUIRES_BASIS
            ],
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    checks.append(
        _check(
            "condition.indeterminate_list",
            list(indeterminate)
            == [
                field
                for field in CONDITION_KEYS
                if evaluations[field].get("evaluation")
                == EVALUATION_INDETERMINATE
            ],
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    for field, value in _canonical_lineage_posture().items():
        checks.append(
            _check(
                "lineage." + field,
                True,
                expected=value,
            )
        )
    for field, value in _canonical_perishability_posture(outcome).items():
        checks.append(
            _check(
                "perishability." + field,
                True,
                expected=value,
            )
        )
    for field in REQUIRED_FALSE_NON_CLAIMS:
        checks.append(
            _check("non_claims." + field, True, expected=False)
        )
    for field in OMISSION_POSTURE_FIELDS:
        checks.append(_check("omission." + field, True, expected=True))
    checks.append(
        _check(
            "future_route.branch_correct",
            route == (
                SUPPORTED_FUTURE_ROUTE
                if outcome == OUTCOME_SUPPORTED
                else None
            ),
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )


def _append_blocked_safety_checks(
    checks: list[dict[str, Any]],
) -> None:
    for field in CONDITION_KEYS:
        checks.append(
            _check(
                "condition." + field + ".not_evaluated",
                True,
                expected=EVALUATION_NOT_EVALUATED,
            )
        )
    for field in REQUIRED_FALSE_NON_CLAIMS:
        checks.append(
            _check("non_claims." + field, True, expected=False)
        )
    for field in OMISSION_POSTURE_FIELDS:
        checks.append(_check("omission." + field, True, expected=True))


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("presence_re_evaluation_operation")
    operation = operation if isinstance(operation, Mapping) else {}
    metadata = result.get("presence_re_evaluation_operation_metadata")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    specification = result.get("specification_validation")
    specification = specification if isinstance(specification, Mapping) else {}
    boundary = result.get(
        "presence_re_evaluation_boundary_artifact_validation"
    )
    boundary = boundary if isinstance(boundary, Mapping) else {}
    prior = result.get("prior_presence_artifact_validation")
    prior = prior if isinstance(prior, Mapping) else {}
    attestation = result.get("receiver_attestation_artifact_validation")
    attestation = attestation if isinstance(attestation, Mapping) else {}
    receipt = result.get(
        "receiver_answerable_receipt_artifact_validation"
    )
    receipt = receipt if isinstance(receipt, Mapping) else {}
    atomic = result.get("atomic_operation_basis_posture")
    atomic = atomic if isinstance(atomic, Mapping) else {}
    lineage = result.get("lineage_preservation_posture")
    lineage = lineage if isinstance(lineage, Mapping) else {}
    perishability = result.get("perishability_posture")
    perishability = perishability if isinstance(perishability, Mapping) else {}
    decision = result.get("operation_decision")
    decision = decision if isinstance(decision, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    evaluations = result.get("condition_evaluations")
    evaluations = evaluations if isinstance(evaluations, Mapping) else {}
    evaluation_counts = {
        evaluation: sum(
            isinstance(evaluations.get(field), Mapping)
            and evaluations[field].get("evaluation") == evaluation
            for field in CONDITION_KEYS
        )
        for evaluation in EVALUATION_FAMILY
    }
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "operation_id": operation.get("operation_id"),
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "specification_path": metadata.get("specification_path"),
        "boundary_artifact_path": metadata.get("boundary_artifact_path"),
        "prior_presence_artifact_path": metadata.get(
            "prior_presence_artifact_path"
        ),
        "receiver_attestation_artifact_path": metadata.get(
            "receiver_attestation_artifact_path"
        ),
        "receiver_answerable_receipt_artifact_path": metadata.get(
            "receiver_answerable_receipt_artifact_path"
        ),
        "outcome": result.get("outcome"),
        "operation_result": result.get(
            "presence_re_evaluation_operation_result"
        ),
        "successor_presence_result": result.get("successor_presence_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("decision_code"),
        "decision_reason": decision.get("decision_reason"),
        "execution_selected": operation.get(
            "presence_re_evaluation_execution_selected"
        ),
        "specification_validated": specification.get(
            "specification_validated"
        ),
        "boundary_artifact_validated": boundary.get("artifact_validated"),
        "prior_presence_artifact_validated": prior.get("artifact_validated"),
        "receiver_attestation_artifact_validated": attestation.get(
            "artifact_validated"
        ),
        "receiver_answerable_receipt_artifact_validated": receipt.get(
            "artifact_validated"
        ),
        "operation_basis_supplied": atomic.get("operation_basis_supplied"),
        "operation_basis_admitted": atomic.get("operation_basis_admitted"),
        "presence_re_evaluation_performed": operation.get(
            "presence_re_evaluation_performed"
        ),
        "successor_presence_result_decided": operation.get(
            "successor_presence_result_decided"
        ),
        "successor_presence_result_recorded": operation.get(
            "successor_presence_result_recorded"
        ),
        "presence_re_evaluation_operation_recorded": operation.get(
            "presence_re_evaluation_operation_recorded"
        ),
        "presence_re_evaluation_operation_result_recorded": operation.get(
            "presence_re_evaluation_operation_result_recorded"
        ),
        "presence_re_evaluation_operation_exhausted": operation.get(
            "presence_re_evaluation_operation_exhausted"
        ),
        "completed_successor_result_posture_count": result.get(
            "completed_successor_result_posture_count"
        ),
        "prior_presence_result_preserved": lineage.get(
            "prior_presence_result_preserved"
        ),
        "presence_re_evaluation_boundary_preserved": lineage.get(
            "presence_re_evaluation_boundary_preserved"
        ),
        "receiver_attestation_result_preserved": lineage.get(
            "receiver_attestation_result_preserved"
        ),
        "receiver_answerable_receipt_result_preserved": lineage.get(
            "receiver_answerable_receipt_result_preserved"
        ),
        "changed_condition": lineage.get("changed_condition"),
        "no_overwrite": lineage.get(
            "prior_presence_operation_overwritten"
        )
        is False,
        "successor_additive": lineage.get(
            "successor_presence_result_additive"
        ),
        "successor_time_scope_bounded": lineage.get(
            "successor_presence_result_time_scope_bounded"
        ),
        "no_retroactive_presence": lineage.get(
            "successor_presence_is_retroactive_presence"
        )
        is False,
        "condition_evaluation_counts": evaluation_counts,
        "missing_or_insufficient_receiver_answerable_basis": copy.deepcopy(
            result.get(
                "missing_or_insufficient_receiver_answerable_basis", []
            )
        ),
        "indeterminate_receiver_answerable_basis_conditions": copy.deepcopy(
            result.get(
                "indeterminate_receiver_answerable_basis_conditions", []
            )
        ),
        "presence_supported": operation.get("presence_supported"),
        "presence_authorized": operation.get("presence_authorized"),
        "presence_established": operation.get("presence_established"),
        "presence_recorded": operation.get("presence_recorded"),
        "requires_receiver_answerable_basis": operation.get(
            "presence_re_evaluation_operation_requires_receiver_answerable_basis"
        ),
        "receiver_answerable_basis_required": operation.get(
            "receiver_answerable_basis_required"
        ),
        "presence_re_evaluation_indeterminate": operation.get(
            "presence_re_evaluation_indeterminate"
        ),
        "perishability_preserved": all(
            perishability.get(field) is True
            for field in (
                "presence_if_ever_supported_remains_perishable",
                "future_supported_presence_requires_separately_bounded_lapse_handling",
                "re_evaluation_does_not_create_durable_presence",
                "perishability_is_not_immediate_lapse",
                "lapse_consideration_is_not_lapse",
            )
        ),
        "durable_presence_absent": all(
            perishability.get(field) is False
            for field in (
                "durable_presence_created",
                "permanent_presence_created",
                "irrevocable_presence_created",
                "immortal_presence_created",
                "self_renewing_presence_created",
            )
        ),
        "lapse_route_absent": result.get("admissible_future_route") is None,
        "result_level_non_claims_canonical_false": result.get(
            "result_level_non_claims_canonical_false"
        ),
        "complete_material_omission_posture": all(
            result.get("omission_posture", {}).get(field) is True
            for field in OMISSION_POSTURE_FIELDS
        )
        if isinstance(result.get("omission_posture"), Mapping)
        else False,
        "admissible_future_route": result.get("admissible_future_route"),
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    specification: Mapping[str, Any] | None = None,
    boundary: Mapping[str, Any] | None = None,
    prior: Mapping[str, Any] | None = None,
    attestation: Mapping[str, Any] | None = None,
    receipt: Mapping[str, Any] | None = None,
    atomic_basis: Mapping[str, Any] | None = None,
    evaluations: Mapping[str, Mapping[str, Any]] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    bounded_specification = (
        copy.deepcopy(dict(specification))
        if isinstance(specification, Mapping)
        else _empty_specification_validation()
    )
    bounded_boundary = (
        copy.deepcopy(dict(boundary))
        if isinstance(boundary, Mapping)
        else _empty_artifact_validation(BOUNDARY_ARTIFACT_RELATIVE_PATH)
    )
    bounded_prior = (
        copy.deepcopy(dict(prior))
        if isinstance(prior, Mapping)
        else _empty_artifact_validation(PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH)
    )
    bounded_attestation = (
        copy.deepcopy(dict(attestation))
        if isinstance(attestation, Mapping)
        else _empty_artifact_validation(
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
        )
    )
    bounded_receipt = (
        copy.deepcopy(dict(receipt))
        if isinstance(receipt, Mapping)
        else _empty_artifact_validation(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
        )
    )
    bounded_atomic = (
        copy.deepcopy(dict(atomic_basis))
        if isinstance(atomic_basis, Mapping)
        else _empty_atomic_basis(request)
    )
    bounded_evaluations = (
        copy.deepcopy(
            {
                key: dict(value)
                for key, value in evaluations.items()
                if isinstance(value, Mapping)
            }
        )
        if isinstance(evaluations, Mapping)
        else _default_condition_evaluations()
    )
    operation_result = _result_for_outcome(outcome)
    missing = [
        field
        for field in CONDITION_KEYS
        if bounded_evaluations[field].get("evaluation")
        == EVALUATION_REQUIRES_BASIS
    ]
    indeterminate = [
        field
        for field in CONDITION_KEYS
        if bounded_evaluations[field].get("evaluation")
        == EVALUATION_INDETERMINATE
    ]
    route = SUPPORTED_FUTURE_ROUTE if outcome == OUTCOME_SUPPORTED else None
    bounded_checks = copy.deepcopy(checks)
    if outcome == OUTCOME_BLOCKED:
        _append_blocked_safety_checks(bounded_checks)
    else:
        _append_completed_checks(
            bounded_checks,
            outcome,
            bounded_evaluations,
            missing,
            indeterminate,
            route,
        )
    operation = _operation_object(
        request,
        outcome,
        operation_result,
        bounded_atomic,
        bounded_evaluations,
        missing,
        indeterminate,
    )
    branch = _branch_posture(outcome)
    decision = _decision_for_outcome(
        outcome,
        code=code,
        reason=reason,
    )
    result: dict[str, Any] = {
        "presence_re_evaluation_operation_metadata": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "specification_path": str(
                GOVERNING_SPECIFICATION_RELATIVE_PATH
            ),
            "boundary_artifact_path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
            "prior_presence_artifact_path": str(
                PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
            ),
            "receiver_attestation_artifact_path": str(
                RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
            ),
            "receiver_answerable_receipt_artifact_path": str(
                RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
            ),
        },
        "declared_presence_re_evaluation_operation_request": (
            _declared_request_posture(request)
        ),
        "specification_validation": bounded_specification,
        "presence_re_evaluation_boundary_artifact_validation": (
            bounded_boundary
        ),
        "prior_presence_artifact_validation": bounded_prior,
        "receiver_attestation_artifact_validation": bounded_attestation,
        "receiver_answerable_receipt_artifact_validation": bounded_receipt,
        "atomic_operation_basis_posture": bounded_atomic,
        "prior_presence_posture": copy.deepcopy(
            bounded_prior.get("standing", {})
        ),
        "later_receiver_side_posture": {
            "receiver_attestation": copy.deepcopy(
                bounded_attestation.get("standing", {})
            ),
            "receiver_answerable_receipt": copy.deepcopy(
                bounded_receipt.get("standing", {})
            ),
        },
        "successor_presence_evaluation_posture": _successor_posture(
            operation
        ),
        "condition_evaluations": bounded_evaluations,
        "missing_or_insufficient_receiver_answerable_basis": missing,
        "indeterminate_receiver_answerable_basis_conditions": indeterminate,
        "lineage_preservation_posture": _canonical_lineage_posture(),
        "perishability_posture": _canonical_perishability_posture(outcome),
        "operation_decision": decision,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "operation_posture": {
            "operation_basis_supplied": bounded_atomic.get(
                "operation_basis_supplied"
            )
            is True,
            "operation_basis_admitted": bounded_atomic.get(
                "operation_basis_admitted"
            )
            is True,
            **branch,
            "single_use_only": True,
            "no_overwrite": True,
            "successor_additive": True,
            "successor_time_scope_bounded": True,
            "no_retroactive_presence": True,
        },
        "presence_re_evaluation_operation": operation,
        "presence_re_evaluation_operation_checks": bounded_checks,
        "presence_re_evaluation_operation_statement": {
            "one_exact_four_artifact_basis_evaluated": (
                bounded_atomic.get("operation_basis_admitted") is True
            ),
            "one_successor_presence_result_selected": outcome
            != OUTCOME_BLOCKED,
            "historical_prior_result_preserved": True,
            "later_receiver_side_standing_preserved": True,
            "successor_result_additive_not_retroactive": True,
            "receipt_not_converted_to_custody_distinctness_refusability_or_withholding": (
                True
            ),
            "result_level_non_claims_canonical_false": True,
        },
        "presence_re_evaluation_operation_non_meaning": (
            _canonical_non_meaning()
        ),
        "omission_posture": _canonical_omission_posture(),
        "blocked_routes": list(BLOCKED_ROUTES),
        "admissible_future_route": route,
        "what_remains_open": _what_remains_open(
            outcome, missing, indeterminate
        ),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        "outcome": outcome,
        "presence_re_evaluation_operation_result": operation_result,
        "successor_presence_result": operation_result,
        "completed_successor_result_posture_count": branch[
            "completed_successor_result_posture_count"
        ],
        "failed_check_count": sum(
            item.get("passed") is False for item in bounded_checks
        ),
        "passed_check_count": sum(
            item.get("passed") is True for item in bounded_checks
        ),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
    }
    result["presence_re_evaluation_operation_summary"] = (
        _summary_from_result(result)
    )
    return result


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    **sections: Any,
) -> dict[str, Any]:
    if not any(item.get("passed") is False for item in checks):
        _add_failure(checks, "blocked.result", code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        code=code,
        reason=reason,
        **sections,
    )


def resolve_presence_re_evaluation_operation_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact four-artifact presence re-evaluation operation."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = _new_canonical_request()
        checks.append(_check("request.mapping", True))
    elif not isinstance(request, Mapping):
        declared_request = _new_canonical_request()
        _add_failure(checks, "request.mapping", "REQUEST_NOT_MAPPING")
        return _blocked_result(
            declared_request,
            checks,
            "REQUEST_NOT_MAPPING",
            "declared presence re-evaluation request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))
        checks.append(_check("request.mapping", True))

    atomic = _empty_atomic_basis(declared_request)
    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "request validation failed",
            atomic_basis=atomic,
        )

    code, reason, specification = _validate_specification(
        declared_request, checks
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "specification validation failed",
            specification=specification,
            atomic_basis=atomic,
        )

    code, reason, boundary = _validate_boundary_artifact(
        declared_request, checks
    )
    atomic["boundary_artifact_validated"] = boundary.get(
        "artifact_validated"
    ) is True
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "boundary validation failed",
            specification=specification,
            boundary=boundary,
            atomic_basis=atomic,
        )

    code, reason, prior = _validate_prior_presence_artifact(
        declared_request, checks
    )
    atomic["prior_presence_artifact_validated"] = prior.get(
        "artifact_validated"
    ) is True
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "prior presence validation failed",
            specification=specification,
            boundary=boundary,
            prior=prior,
            atomic_basis=atomic,
        )

    code, reason, attestation = _validate_receiver_attestation_artifact(
        declared_request, checks
    )
    atomic["receiver_attestation_artifact_validated"] = attestation.get(
        "artifact_validated"
    ) is True
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "receiver-attestation validation failed",
            specification=specification,
            boundary=boundary,
            prior=prior,
            attestation=attestation,
            atomic_basis=atomic,
        )

    code, reason, receipt = _validate_receiver_answerable_receipt_artifact(
        declared_request, checks
    )
    atomic["receiver_answerable_receipt_artifact_validated"] = receipt.get(
        "artifact_validated"
    ) is True
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "receiver-answerable-receipt validation failed",
            specification=specification,
            boundary=boundary,
            prior=prior,
            attestation=attestation,
            receipt=receipt,
            atomic_basis=atomic,
        )

    all_valid = all(
        atomic[field] is True
        for field in (
            "boundary_artifact_validated",
            "prior_presence_artifact_validated",
            "receiver_attestation_artifact_validated",
            "receiver_answerable_receipt_artifact_validated",
        )
    )
    atomic["all_four_exact_artifacts_validated"] = all_valid
    atomic["operation_basis_admitted"] = all_valid
    checks.append(
        _check(
            "atomic_basis.all_four_exact_artifacts_validated",
            all_valid,
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    checks.append(
        _check(
            "atomic_basis.operation_basis_admitted",
            all_valid,
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    if not all_valid:
        return _blocked_result(
            declared_request,
            checks,
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
            "all four exact basis artifacts must validate atomically",
            specification=specification,
            boundary=boundary,
            prior=prior,
            attestation=attestation,
            receipt=receipt,
            atomic_basis=atomic,
        )

    evaluations = _evaluate_conditions(prior, attestation, receipt)
    outcome = _outcome_from_evaluations(evaluations)
    if outcome == OUTCOME_BLOCKED:
        return _blocked_result(
            declared_request,
            checks,
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
            "condition matrix did not produce a lawful completed branch",
            specification=specification,
            boundary=boundary,
            prior=prior,
            attestation=attestation,
            receipt=receipt,
            atomic_basis=atomic,
        )
    return _build_result(
        declared_request,
        outcome,
        checks,
        specification=specification,
        boundary=boundary,
        prior=prior,
        attestation=attestation,
        receipt=receipt,
        atomic_basis=atomic,
        evaluations=evaluations,
    )


def resolve_presence_re_evaluation_operation_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Strictly load one explicit request path and resolve it."""
    try:
        path = Path(request_path)
    except (TypeError, ValueError) as exc:
        raise PresenceReEvaluationOperationV0MinError(
            "REQUEST_PATH_INVALID: request path is invalid"
        ) from exc
    payload, error = _read_json(path)
    if error is not None:
        raise PresenceReEvaluationOperationV0MinError(
            "REQUEST_PATH_INVALID: request JSON is unavailable, malformed, "
            "or duplicate-keyed"
        )
    if not isinstance(payload, Mapping):
        raise PresenceReEvaluationOperationV0MinError(
            "REQUEST_PATH_INVALID: request JSON must contain one object"
        )
    return resolve_presence_re_evaluation_operation_v0_min(payload)


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "complete_presence_re_evaluation_boundary_artifact",
        "presence_re_evaluation_boundary_artifact",
        "complete_prior_presence_artifact",
        "prior_presence_artifact",
        "complete_receiver_attestation_artifact",
        "receiver_attestation_artifact",
        "complete_receiver_answerable_receipt_artifact",
        "receiver_answerable_receipt_artifact",
        "complete_candidate_sufficiency_material",
        "candidate_sufficiency_basis",
        "sufficiency_basis_records",
        "bounded_capture_source_body",
        "archive_bytes",
        "archive_body",
        "hash_record_body",
        "text_component_bodies",
        "recorded_signal_body",
        "signal_samples",
        "raw_signal_data",
    }
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).casefold() in forbidden_keys:
                return True
            if _contains_prohibited_complete_material(item):
                return True
        return False
    if isinstance(value, (list, tuple)):
        return any(_contains_prohibited_complete_material(item) for item in value)
    return isinstance(value, (bytes, bytearray, memoryview))


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get("presence_re_evaluation_operation_checks")
    if not isinstance(checks, list) or not checks:
        return False
    if any(not isinstance(item, Mapping) for item in checks):
        return False
    failed = sum(item.get("passed") is False for item in checks)
    passed = sum(item.get("passed") is True for item in checks)
    if (
        type(result.get("failed_check_count")) is not int
        or type(result.get("passed_check_count")) is not int
        or result.get("failed_check_count") != failed
        or result.get("passed_check_count") != passed
    ):
        return False
    for item in checks:
        if type(item.get("passed")) is not bool:
            return False
        for field in ("failure_code", "block_code"):
            if field in item and item[field] not in BLOCK_CODES:
                return False
    return (
        failed > 0
        if result.get("outcome") == OUTCOME_BLOCKED
        else failed == 0
    )


def _condition_matrix_valid(result: Mapping[str, Any]) -> bool:
    evaluations = result.get("condition_evaluations")
    if not isinstance(evaluations, Mapping) or set(evaluations) != set(
        CONDITION_KEYS
    ):
        return False
    outcome = result.get("outcome")
    for field, required in CONDITION_REQUIREMENTS.items():
        item = evaluations.get(field)
        if not isinstance(item, Mapping) or set(item) != {
            "historical_prior_value",
            "later_compact_standing",
            "required_successor_value",
            "evaluation",
            "successor_value",
            "compact_evidence_code",
            "reason",
        }:
            return False
        later = item.get("later_compact_standing")
        if not isinstance(later, Mapping) or set(later) != {
            "receiver_attestation_value",
            "receiver_answerable_receipt_value",
        }:
            return False
        if item.get("historical_prior_value") is not None and type(
            item.get("historical_prior_value")
        ) is not bool:
            return False
        if any(
            value is not None and type(value) is not bool
            for value in later.values()
        ):
            return False
        if not _matches_exact(item.get("required_successor_value"), required):
            return False
        if item.get("evaluation") not in EVALUATION_FAMILY:
            return False
        if type(item.get("successor_value")) is not bool:
            return False
        if not isinstance(item.get("compact_evidence_code"), str) or not item.get(
            "compact_evidence_code"
        ):
            return False
        if not isinstance(item.get("reason"), str) or not item.get("reason"):
            return False
        if outcome == OUTCOME_BLOCKED:
            if item.get("evaluation") != EVALUATION_NOT_EVALUATED:
                return False
        elif item.get("evaluation") == EVALUATION_NOT_EVALUATED:
            return False
    if outcome == OUTCOME_BLOCKED:
        expected_outcome = OUTCOME_BLOCKED
    else:
        expected_outcome = _outcome_from_evaluations(evaluations)
    if expected_outcome != outcome:
        return False
    expected_missing = [
        field
        for field in CONDITION_KEYS
        if evaluations[field].get("evaluation")
        == EVALUATION_REQUIRES_BASIS
    ]
    expected_indeterminate = [
        field
        for field in CONDITION_KEYS
        if evaluations[field].get("evaluation")
        == EVALUATION_INDETERMINATE
    ]
    return (
        result.get("missing_or_insufficient_receiver_answerable_basis")
        == expected_missing
        and result.get(
            "indeterminate_receiver_answerable_basis_conditions"
        )
        == expected_indeterminate
    )


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    operation_result = result.get(
        "presence_re_evaluation_operation_result"
    )
    operation = result.get("presence_re_evaluation_operation")
    posture = result.get("operation_posture")
    atomic = result.get("atomic_operation_basis_posture")
    block = result.get("block")
    decision = result.get("operation_decision")
    if (
        outcome not in OUTCOME_FAMILY
        or operation_result != _result_for_outcome(str(outcome))
        or result.get("successor_presence_result") != operation_result
        or not all(
            isinstance(value, Mapping)
            for value in (operation, posture, atomic, block, decision)
        )
    ):
        return False
    expected_branch = _branch_posture(str(outcome))
    if any(
        not _matches_exact(operation.get(field), expected)
        or not _matches_exact(posture.get(field), expected)
        for field, expected in expected_branch.items()
    ):
        return False
    if not _matches_exact(
        result.get("completed_successor_result_posture_count"),
        expected_branch["completed_successor_result_posture_count"],
    ):
        return False
    completed = outcome != OUTCOME_BLOCKED
    if (atomic.get("operation_basis_admitted") is True) is not completed:
        return False
    if operation.get("operation_basis_admitted") is not completed:
        return False
    supported = outcome == OUTCOME_SUPPORTED
    requires_basis = outcome == OUTCOME_REQUIRES_BASIS
    indeterminate = outcome == OUTCOME_INDETERMINATE
    if any(
        operation.get(field) is not supported
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        )
    ):
        return False
    if (
        operation.get(
            "presence_re_evaluation_operation_requires_receiver_answerable_basis"
        )
        is not requires_basis
        or operation.get("receiver_answerable_basis_required")
        is not requires_basis
        or operation.get("presence_re_evaluation_indeterminate")
        is not indeterminate
    ):
        return False
    if any(operation.get(field) is not False for field in REQUIRED_FALSE_NON_CLAIMS):
        return False
    if outcome == OUTCOME_BLOCKED:
        return (
            block.get("blocked") is True
            and block.get("code") in BLOCK_CODES
            and block.get("block_code") == block.get("code")
            and isinstance(block.get("reason"), str)
            and bool(block.get("reason"))
            and decision.get("decision_code") == block.get("code")
            and decision.get("decision_reason") == block.get("reason")
            and result.get("admissible_future_route") is None
        )
    expected_decision = {
        OUTCOME_SUPPORTED: (
            DECISION_CODE_SUPPORTED,
            DECISION_REASON_SUPPORTED,
        ),
        OUTCOME_REQUIRES_BASIS: (
            DECISION_CODE_REQUIRES_BASIS,
            DECISION_REASON_REQUIRES_BASIS,
        ),
        OUTCOME_INDETERMINATE: (
            DECISION_CODE_INDETERMINATE,
            DECISION_REASON_INDETERMINATE,
        ),
    }[outcome]
    return (
        block
        == {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }
        and decision.get("decision_code") == expected_decision[0]
        and decision.get("decision_reason") == expected_decision[1]
        and result.get("admissible_future_route")
        == (SUPPORTED_FUTURE_ROUTE if supported else None)
    )


def _supporting_sections_valid(result: Mapping[str, Any]) -> bool:
    metadata = result.get("presence_re_evaluation_operation_metadata")
    declared = result.get("declared_presence_re_evaluation_operation_request")
    specification = result.get("specification_validation")
    lineage = result.get("lineage_preservation_posture")
    perishability = result.get("perishability_posture")
    omission = result.get("omission_posture")
    non_meaning = result.get("presence_re_evaluation_operation_non_meaning")
    if not all(
        isinstance(value, Mapping)
        for value in (
            metadata,
            declared,
            specification,
            lineage,
            perishability,
            omission,
            non_meaning,
        )
    ):
        return False
    expected_metadata = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "boundary_artifact_path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
        "prior_presence_artifact_path": str(
            PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_attestation_artifact_path": str(
            RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_answerable_receipt_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
        ),
    }
    return (
        dict(metadata) == expected_metadata
        and all(type(value) is bool for value in declared.values())
        and dict(lineage) == _canonical_lineage_posture()
        and dict(perishability)
        == _canonical_perishability_posture(str(result.get("outcome")))
        and dict(omission) == _canonical_omission_posture()
        and dict(non_meaning) == _canonical_non_meaning()
        and result.get("blocked_routes") == list(BLOCKED_ROUTES)
        and isinstance(result.get("what_remains_open"), list)
        and all(
            isinstance(item, str) and bool(item)
            for item in result.get("what_remains_open", [])
        )
        and isinstance(specification.get("marker_validation"), Mapping)
        and set(specification.get("marker_validation", {}))
        == {name for name, _ in SPEC_REQUIRED_MARKERS}
        and all(
            type(value) is bool
            for value in specification.get("marker_validation", {}).values()
        )
    )


def _result_valid_for_write(result: Mapping[str, Any]) -> bool:
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
        or set(result) != RESULT_SECTIONS
        or not _checks_valid(result)
        or not _condition_matrix_valid(result)
        or not _branch_valid(result)
        or not _supporting_sections_valid(result)
        or not _canonical_false_mapping_valid(
            result.get("non_claims"),
            REQUIRED_FALSE_NON_CLAIMS,
            exact_keys=True,
        )
        or result.get("result_level_non_claims_canonical_false") is not True
        or _contains_prohibited_complete_material(result)
    ):
        return False
    summary = result.get("presence_re_evaluation_operation_summary")
    return isinstance(summary, Mapping) and dict(summary) == _summary_from_result(
        result
    )


def build_presence_re_evaluation_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic material-omitting summary."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise PresenceReEvaluationOperationV0MinError(
            "summary requires a compatible presence re-evaluation result"
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
        return _path_within(path.resolve(), OUTPUT_ROOT.resolve())
    except (OSError, RuntimeError, ValueError):
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
    raise PresenceReEvaluationOperationV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def write_presence_re_evaluation_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid result under the canonical family without overwrite."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise PresenceReEvaluationOperationV0MinError(
            "WRITE_REFUSED: malformed or inconsistent operation result"
        )
    explicit = output_path is not None
    try:
        target = (
            _as_repo_path(output_path)
            if explicit
            else OUTPUT_ROOT / OUTPUT_FILENAME
        )
    except (OSError, TypeError, ValueError) as exc:
        raise PresenceReEvaluationOperationV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise PresenceReEvaluationOperationV0MinError(
            "WRITE_REFUSED: output path is protected or outside the exact "
            "presence-re-evaluation-operation output family"
        )
    if target.exists() and explicit:
        raise PresenceReEvaluationOperationV0MinError(
            "WRITE_REFUSED: explicit output path already exists"
        )
    if target.is_dir():
        raise PresenceReEvaluationOperationV0MinError(
            "WRITE_REFUSED: output path is a directory"
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
        raise PresenceReEvaluationOperationV0MinError(
            "WRITE_REFUSED: unable to write operation result"
        ) from exc
    return target
