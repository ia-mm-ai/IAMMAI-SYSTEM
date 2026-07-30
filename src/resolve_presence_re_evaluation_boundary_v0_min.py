"""Resolve one bounded presence re-evaluation consideration boundary.

The resolver reads only the governing specification and the two exact
completed upstream artifacts.  It preserves their separate standing and may
record only whether a later, separately bounded re-evaluation operation may
be considered.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESOLVER_MODULE = "resolve_presence_re_evaluation_boundary_v0_min"
RESULT_VERSION = "0.1.0"

BOUNDARY_ID = "presence_re_evaluation_boundary_001"
BOUNDARY_TYPE = "PRESENCE_RE_EVALUATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_PRESENCE_RE_EVALUATION_AFTER_RECORDED_"
    "RECEIVER_ANSWERABLE_RECEIPT_ONLY"
)

PRIOR_PRESENCE_OPERATION_ID = "presence_operation_001"
PRIOR_PRESENCE_OPERATION_TYPE = "PRESENCE_OPERATION"
PRIOR_PRESENCE_OPERATION_VERSION = "0.1.0"
PRIOR_PRESENCE_OPERATION_SCOPE = (
    "EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_"
    "RECEIVER_ATTESTATION_REQUIREMENT_ONLY"
)
PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED = (
    "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"
)
PRIOR_PRESENCE_RESULT_REQUIRED = "REQUIRES_RECEIVER_ATTESTATION"
PRIOR_PRESENCE_RESOLVER_MODULE = "resolve_presence_operation_v0_min"
PRIOR_PRESENCE_PASSED_CHECK_COUNT = 446

RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation_001"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION = "0.1.0"
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE = (
    "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
    "RECEIVER_ATTESTATION_RESULT_ONLY"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)
RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min"
)
RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT = 357
RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE = (
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_THEN_SEPARATE_"
    "PRESENCE_RE_EVALUATION_BOUNDARY_ONLY_IF_"
    "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)

ADMISSIBLE_FUTURE_ROUTE = (
    "PRESENCE_RE_EVALUATION_BOUNDARY_THEN_SEPARATE_"
    "PRESENCE_RE_EVALUATION_OPERATION_ONLY"
)

OUTCOME_ALLOWED = "PRESENCE_RE_EVALUATION_BOUNDARY_ALLOWED"
OUTCOME_NOT_ALLOWED = "PRESENCE_RE_EVALUATION_BOUNDARY_NOT_ALLOWED"
OUTCOME_BLOCKED = "PRESENCE_RE_EVALUATION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED, OUTCOME_BLOCKED)

RESULT_ALLOWED = "PRESENCE_RE_EVALUATION_OPERATION_CONSIDERATION_ALLOWED"
RESULT_NOT_ALLOWED = (
    "PRESENCE_RE_EVALUATION_OPERATION_CONSIDERATION_NOT_ALLOWED"
)
RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_FAMILY = (RESULT_ALLOWED, RESULT_NOT_ALLOWED, RESULT_NOT_EVALUATED)
BOUNDARY_RESULT_FAMILY = RESULT_FAMILY

DECISION_CODE_ALLOWED = "PRESENCE_RE_EVALUATION_CONSIDERATION_ALLOWED"
DECISION_REASON_ALLOWED = (
    "prior lawful waiting presence result and later recorded "
    "receiver-answerable receipt admitted for one separate presence "
    "re-evaluation operation consideration only"
)
DECISION_CODE_NOT_ALLOWED = (
    "PRESENCE_RE_EVALUATION_CONSIDERATION_NOT_ALLOWED"
)
DECISION_REASON_NOT_ALLOWED = (
    "presence re-evaluation operation consideration not selected"
)

INTENT_RECORD = "RECORD_PRESENCE_RE_EVALUATION_BOUNDARY"
INTENT_BLOCK = "BLOCK_PRESENCE_RE_EVALUATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/PRESENCE_RE_EVALUATION_BOUNDARY_V0_MIN_SPEC.md"
)
PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min/"
    "presence_operation_001__presence_operation_v0_min_result.json"
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation_"
    "v0_min/receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min_result.json"
)
GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SPECIFICATION_PATH
PRIOR_PRESENCE_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT / PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT / RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
)
CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "presence_re_evaluation_boundary_v0_min"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "presence_re_evaluation_boundary_001__"
    "presence_re_evaluation_boundary_v0_min_result.json"
)

SPEC_REQUIRED_MARKERS = (
    ("title", "# Presence Re-Evaluation Boundary V0 Minimum Specification"),
    (
        "boundary_id",
        "presence_re_evaluation_boundary_id = " + BOUNDARY_ID,
    ),
    (
        "boundary_type",
        "presence_re_evaluation_boundary_type = " + BOUNDARY_TYPE,
    ),
    (
        "boundary_version",
        "presence_re_evaluation_boundary_version = " + BOUNDARY_VERSION,
    ),
    (
        "boundary_scope",
        "presence_re_evaluation_boundary_scope = " + BOUNDARY_SCOPE,
    ),
    ("future_route", ADMISSIBLE_FUTURE_ROUTE),
    (
        "prior_artifact_path",
        str(PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH),
    ),
    (
        "receipt_artifact_path",
        str(RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH),
    ),
    (
        "prior_operation_id",
        "prior_presence_operation_id = " + PRIOR_PRESENCE_OPERATION_ID,
    ),
    (
        "prior_operation_type",
        "prior_presence_operation_type = " + PRIOR_PRESENCE_OPERATION_TYPE,
    ),
    (
        "prior_operation_version",
        "prior_presence_operation_version = "
        + PRIOR_PRESENCE_OPERATION_VERSION,
    ),
    (
        "prior_operation_scope",
        "prior_presence_operation_scope = " + PRIOR_PRESENCE_OPERATION_SCOPE,
    ),
    (
        "prior_outcome",
        "prior_presence_operation_outcome_required = "
        + PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
    ),
    (
        "prior_result",
        "prior_presence_result_required = " + PRIOR_PRESENCE_RESULT_REQUIRED,
    ),
    (
        "receipt_operation_id",
        "receiver_answerable_receipt_operation_id = "
        + RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
    ),
    (
        "receipt_operation_type",
        "receiver_answerable_receipt_operation_type = "
        + RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
    ),
    (
        "receipt_operation_version",
        "receiver_answerable_receipt_operation_version = "
        + RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
    ),
    (
        "receipt_operation_scope",
        "receiver_answerable_receipt_operation_scope = "
        + RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
    ),
    (
        "receipt_outcome",
        "receiver_answerable_receipt_operation_outcome_required = "
        + RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED,
    ),
    (
        "receipt_result",
        "receiver_answerable_receipt_operation_result_required = "
        + RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED,
    ),
    (
        "separate_standing",
        "The two artifacts are separate standing. Neither may replace the "
        "other.",
    ),
    (
        "no_overwrite",
        "Changed standing permits reconsideration only through this new "
        "additive boundary",
    ),
    (
        "prior_receipt_absent",
        "prior `receiver_answerable_receipt_present = false`",
    ),
    (
        "later_receipt_present",
        "later `receiver_answerable_receipt_present = true`",
    ),
    ("changed_condition_limit", "## 8. Changed-Condition Limit"),
    ("outcome_allowed", OUTCOME_ALLOWED),
    ("outcome_not_allowed", OUTCOME_NOT_ALLOWED),
    ("outcome_blocked", OUTCOME_BLOCKED),
    ("result_allowed", RESULT_ALLOWED),
    ("result_not_allowed", RESULT_NOT_ALLOWED),
    ("result_not_evaluated", RESULT_NOT_EVALUATED),
    ("allowed_rule", "Consideration may be `ALLOWED` only when:"),
    (
        "not_allowed_rule",
        "Consideration may be `NOT_ALLOWED` only when",
    ),
    (
        "blocked_rule",
        "The boundary must record `BLOCKED` when",
    ),
    (
        "branch_default",
        "Default and `BLOCKED` posture is:",
    ),
    ("branch_allowed", "An `ALLOWED` result records:"),
    ("branch_not_allowed", "A `NOT_ALLOWED` result records:"),
    (
        "branch_exhaustion",
        "Boundary exhaustion is not re-evaluation completion and is not "
        "presence.",
    ),
    (
        "prior_waiting_not_error",
        "Prior lawful waiting result is not error.",
    ),
    (
        "receipt_not_presence",
        "Receipt is not presence.",
    ),
    (
        "receipt_not_complete_basis",
        "Receipt presence is not complete receiver-answerable basis "
        "satisfaction.",
    ),
    (
        "consideration_not_re_evaluation",
        "Re-evaluation consideration is not re-evaluation.",
    ),
    (
        "boundary_not_operation",
        "Re-evaluation boundary is not re-evaluation operation.",
    ),
    (
        "support_not_authorization",
        "Presence support is not presence authorization.",
    ),
    (
        "authorization_not_establishment",
        "Presence authorization is not presence establishment.",
    ),
    (
        "establishment_not_recording",
        "Presence establishment is not presence recording.",
    ),
    (
        "perishability",
        "Presence, if ever supported, is perishable.",
    ),
    (
        "perishability_not_lapse",
        "Perishability is not immediate lapse.",
    ),
    ("lapse_consideration_not_lapse", "Lapse consideration is not lapse."),
    (
        "no_supported_presence",
        "No supported presence currently stands.",
    ),
    (
        "contaminated_lineage",
        "All contaminated lineage remains unchanged.",
    ),
    ("open_not_next", "Open does not mean next."),
)
SPEC_MARKERS = tuple(marker for _, marker in SPEC_REQUIRED_MARKERS)

PRIOR_TRUE_POSTURES = (
    "presence_operation_recorded",
    "presence_evaluation_performed",
    "presence_result_recorded",
    "presence_operation_requires_receiver_attestation",
    "receiver_attestation_required",
    "receiver_answerable_basis_required",
)
PRIOR_FALSE_POSTURES = (
    "receiver_attested",
    "receiver_answerable_receipt_present",
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
)
RECEIPT_TRUE_POSTURES = (
    "operation_basis_supplied",
    "operation_basis_admitted",
    "receiver_answerable_receipt_operation_recorded",
    "receiver_answerable_receipt_operation_result_recorded",
    "receiver_answerable_receipt_operation_exhausted",
    "receiver_answerable_receipt_decided",
    "receiver_answerable_receipt_recorded",
    "receiver_answerable_receipt_present",
)
RECEIPT_FALSE_POSTURES = (
    "receiver_answerable_receipt_not_recorded",
    "receiver_answerable_receipt_indeterminate",
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
)

REQUIRED_FALSE_NON_CLAIMS = (
    "presence_re_evaluation_boundary_created",
    "presence_re_evaluation_operation_created",
    "presence_re_evaluation_operation_executed",
    "presence_re_evaluation_result_recorded",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "durable_presence_created",
    "permanent_presence_created",
    "irrevocable_presence_created",
    "self_renewing_presence_created",
    "presence_lapse_boundary_created",
    "presence_lapse_operation_created",
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
    "repeated_presence_re_evaluation_boundary_permission_created",
    "reusable_presence_re_evaluation_route_created",
    "same_presence_re_evaluation_boundary_rerun_authorized",
    "automatic_presence_re_evaluation_boundary_retry_created",
    "presence_re_evaluation_boundary_debt_created",
    "presence_re_evaluation_boundary_obligation_created",
    "prior_presence_operation_overwritten",
    "prior_presence_operation_invalidated",
    "prior_presence_operation_superseded",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
)

OMISSION_POSTURE_FIELDS = (
    "complete_prior_presence_artifact_omitted",
    "complete_changed_condition_receipt_artifact_omitted",
    "complete_candidate_sufficiency_material_omitted",
    "bounded_capture_source_bodies_omitted",
    "archive_bytes_omitted",
    "hash_record_body_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
    "alternative_presence_artifacts_omitted",
    "alternative_receipt_artifacts_omitted",
)

LINEAGE_POSTURE_FIELDS = (
    "prior_presence_result_preserved",
    "prior_presence_artifact_remains_truthful",
    "later_receipt_result_preserved",
    "changed_standing_recorded_without_overwrite",
    "prior_and_later_artifacts_remain_separate_standing",
    "earlier_waiting_result_and_later_receipt_presence_coexist",
    "successor_presence_result_not_selected",
    "no_prior_artifact_repaired_invalidated_superseded_or_replaced",
    "contaminated_lineage_unchanged",
)

PERISHABILITY_POSTURE_FIELDS = (
    "presence_if_ever_supported_remains_perishable",
    "future_supported_presence_requires_separately_bounded_lapse_handling",
    "re_evaluation_does_not_create_durable_presence",
    "perishability_is_not_immediate_lapse",
    "lapse_consideration_is_not_lapse",
    "no_supported_presence_currently_stands",
)

NON_MEANING_FIELDS = (
    "prior_lawful_waiting_result_is_not_error",
    "changed_standing_is_not_silent_overwrite",
    "receipt_is_not_presence",
    "receipt_presence_is_not_complete_receiver_answerable_basis_satisfaction",
    "re_evaluation_consideration_is_not_re_evaluation",
    "boundary_is_not_operation",
    "operation_consideration_is_not_presence_support",
    "support_is_not_authorization",
    "authorization_is_not_establishment",
    "establishment_is_not_recording",
    "recording_is_not_identity_custody_proof_provenance_proof_"
    "physical_validity_proof_authority_truth_or_standing",
    "presence_if_ever_supported_is_perishable",
    "perishability_is_not_immediate_lapse",
    "lapse_consideration_is_not_lapse",
    "boundary_exhaustion_is_not_revised_presence_result",
    "open_does_not_mean_next",
    "not_allowed_is_not_prior_result_wrong",
    "not_allowed_is_not_receipt_false_or_rejected",
    "not_allowed_is_not_presence_impossible_or_denied",
    "not_allowed_is_not_lapse",
    "not_allowed_is_not_debt_or_obligation",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_caller_selected_outcome": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
    "request_caller_selected_boundary_result": (
        "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
    ),
    "request_caller_selected_completed_consideration_posture": (
        "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
    ),
    "request_revised_presence_result_preclaimed": (
        "PROHIBITED_REVISED_PRESENCE_RESULT_REQUESTED"
    ),
    "request_presence_re_evaluation_operation_created": (
        "PROHIBITED_RE_EVALUATION_OPERATION_REQUESTED"
    ),
    "request_presence_re_evaluation_operation_executed": (
        "PROHIBITED_RE_EVALUATION_OPERATION_REQUESTED"
    ),
    "request_presence_re_evaluation_result_recorded": (
        "PROHIBITED_REVISED_PRESENCE_RESULT_REQUESTED"
    ),
    "request_presence_supported": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_authorized": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_established": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_recorded": "PROHIBITED_PRESENCE_REQUESTED",
    "request_receiver_answerable_basis_custody_distinct": (
        "PROHIBITED_RECEIVER_BASIS_PRECLAIM_REQUESTED"
    ),
    "request_receiver_answerable_basis_refusable": (
        "PROHIBITED_RECEIVER_BASIS_PRECLAIM_REQUESTED"
    ),
    "request_receiver_answerable_basis_could_have_been_withheld": (
        "PROHIBITED_RECEIVER_BASIS_PRECLAIM_REQUESTED"
    ),
    "request_durable_presence_created": "PROHIBITED_DURABLE_PRESENCE_REQUESTED",
    "request_permanent_presence_created": (
        "PROHIBITED_DURABLE_PRESENCE_REQUESTED"
    ),
    "request_irrevocable_presence_created": (
        "PROHIBITED_DURABLE_PRESENCE_REQUESTED"
    ),
    "request_self_renewing_presence_created": (
        "PROHIBITED_DURABLE_PRESENCE_REQUESTED"
    ),
    "request_presence_lapse_boundary_created": (
        "PROHIBITED_LAPSE_REQUESTED"
    ),
    "request_presence_lapse_operation_created": (
        "PROHIBITED_LAPSE_REQUESTED"
    ),
    "request_presence_lapse_result_recorded": "PROHIBITED_LAPSE_REQUESTED",
    "request_presence_lapsed": "PROHIBITED_LAPSE_REQUESTED",
    "request_presence_expired": "PROHIBITED_LAPSE_REQUESTED",
    "request_identity_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_custody_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_custody_proven": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_provenance_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_provenance_proven": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_physical_validity_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_physical_validity_proven": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_authority_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_truth_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_standing_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_relation_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_coupling_assigned": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_coupling_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_field_machinery_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_runtime_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_api_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_public_interface_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_public_intake_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
    "request_output_authorized": "PROHIBITED_AUTHORIZATION_REQUESTED",
    "request_action_authorized": "PROHIBITED_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorized": (
        "PROHIBITED_AUTHORIZATION_REQUESTED"
    ),
    "request_synchronization_authorized": (
        "PROHIBITED_AUTHORIZATION_REQUESTED"
    ),
    "request_follow_on_authorized": "PROHIBITED_AUTHORIZATION_REQUESTED",
    "request_follow_on_work_authorized": (
        "PROHIBITED_AUTHORIZATION_REQUESTED"
    ),
    "request_prior_presence_operation_overwrite": (
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED"
    ),
    "request_prior_presence_operation_invalidation": (
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED"
    ),
    "request_prior_presence_operation_supersession": (
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED"
    ),
    "request_prior_presence_operation_repair": (
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED"
    ),
    "request_prior_presence_operation_replacement": (
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED"
    ),
    "request_prior_presence_operation_normalization": (
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED"
    ),
    "request_complete_prior_presence_artifact_embedding": (
        "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
    ),
    "request_complete_receipt_operation_artifact_embedding": (
        "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
    ),
    "request_complete_candidate_sufficiency_material_embedding": (
        "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
    ),
    "request_bounded_capture_source_body_read": (
        "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
    ),
    "request_archive_bytes_read": "PROHIBITED_CAPTURE_BODY_READ_REQUESTED",
    "request_hash_record_body_read": (
        "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
    ),
    "request_text_component_bodies_read": (
        "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
    ),
    "request_recorded_signal_body_read": (
        "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
    ),
    "request_repository_scan": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_file_discovery": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_glob": "PROHIBITED_ALTERNATIVE_ARTIFACT_SEARCH_REQUESTED",
    "request_rglob": "PROHIBITED_ALTERNATIVE_ARTIFACT_SEARCH_REQUESTED",
    "request_sibling_discovery": (
        "PROHIBITED_ALTERNATIVE_ARTIFACT_SEARCH_REQUESTED"
    ),
    "request_alternative_artifact_search": (
        "PROHIBITED_ALTERNATIVE_ARTIFACT_SEARCH_REQUESTED"
    ),
    "request_replacement_result_inference": (
        "PROHIBITED_ALTERNATIVE_ARTIFACT_SEARCH_REQUESTED"
    ),
    "request_contaminated_lineage_validation": (
        "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED"
    ),
    "request_repeated_boundary_permission_created": (
        "PROHIBITED_REPEATED_USE_REQUESTED"
    ),
    "request_reusable_route_created": "PROHIBITED_REPEATED_USE_REQUESTED",
    "request_same_boundary_rerun_authorized": (
        "PROHIBITED_REPEATED_USE_REQUESTED"
    ),
    "request_automatic_boundary_retry_created": (
        "PROHIBITED_REPEATED_USE_REQUESTED"
    ),
    "request_boundary_debt_created": "PROHIBITED_REPEATED_USE_REQUESTED",
    "request_boundary_obligation_created": (
        "PROHIBITED_REPEATED_USE_REQUESTED"
    ),
    "request_scheduled_presence_re_evaluation": (
        "PROHIBITED_REPEATED_USE_REQUESTED"
    ),
    "request_scheduled_presence_lapse": (
        "PROHIBITED_REPEATED_USE_REQUESTED"
    ),
    "request_automatic_next_step": "PROHIBITED_REPEATED_USE_REQUESTED",
}

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
        "PRIOR_PRESENCE_TRUE_POSTURE_NOT_TRUE",
        "PRIOR_PRESENCE_FALSE_POSTURE_NOT_FALSE",
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
        "RECEIPT_RESULT_CARDINALITY_MISMATCH",
        "RECEIPT_TRUE_POSTURE_NOT_TRUE",
        "RECEIPT_FALSE_POSTURE_NOT_FALSE",
        "RECEIPT_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "RECEIPT_FUTURE_ROUTE_MISMATCH",
        "CHANGED_CONDITION_MISMATCH",
        "SEPARATE_STANDING_NOT_PRESERVED",
        "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "PROHIBITED_REVISED_PRESENCE_RESULT_REQUESTED",
        "PROHIBITED_RE_EVALUATION_OPERATION_REQUESTED",
        "PROHIBITED_PRESENCE_REQUESTED",
        "PROHIBITED_RECEIVER_BASIS_PRECLAIM_REQUESTED",
        "PROHIBITED_DURABLE_PRESENCE_REQUESTED",
        "PROHIBITED_LAPSE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_REQUESTED",
        "PROHIBITED_AUTHORIZATION_REQUESTED",
        "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED",
        "PROHIBITED_COMPLETE_MATERIAL_REQUESTED",
        "PROHIBITED_CAPTURE_BODY_READ_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "PROHIBITED_ALTERNATIVE_ARTIFACT_SEARCH_REQUESTED",
        "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED",
        "PROHIBITED_REPEATED_USE_REQUESTED",
        "WRITE_REFUSED",
    }
)

BLOCKED_ROUTES = (
    "prior_waiting_result_to_revised_presence_result",
    "receipt_to_presence",
    "receipt_presence_to_custody_distinctness",
    "receipt_presence_to_refusability",
    "receipt_presence_to_could_have_been_withheld_proof",
    "receipt_to_identity_custody_proof_provenance_proof_"
    "physical_validity_proof_authority_truth_or_standing",
    "re_evaluation_boundary_to_re_evaluation_completion",
    "re_evaluation_consideration_to_presence_support",
    "presence_support_to_immortal_irrevocable_permanent_"
    "self_renewing_or_durable_presence",
    "perishability_to_immediate_lapse",
    "future_lapse_route_to_lapse_without_separate_boundary_and_operation",
    "boundary_result_to_relation_coupling_field_runtime_api_public_surface_"
    "output_action_derivative_reception_synchronization_or_follow_on",
    "boundary_result_to_repeat_reusable_rerun_retry_debt_obligation_"
    "scheduled_work_or_automatic_next",
    "presence_re_evaluation_boundary_to_repair_normalization_redemption_"
    "or_contaminated_lineage_validation",
)

WHAT_REMAINS_OPEN = (
    "presence re-evaluation boundary tests",
    "presence re-evaluation boundary live result",
    "presence re-evaluation boundary terminal summary",
    "presence re-evaluation operation specification",
    "presence re-evaluation operation resolver",
    "presence re-evaluation operation tests",
    "presence re-evaluation operation request",
    "presence re-evaluation operation live result",
    "custody-distinctness evaluation",
    "refusability evaluation",
    "could-have-been-withheld evaluation",
    "revised presence result",
    "presence support",
    "presence authorization",
    "presence establishment",
    "presence recording",
    "presence-lapse boundary only after any future supported presence",
    "presence-lapse operation only after any future supported presence "
    "and separate boundary",
    "identity",
    "custody",
    "provenance",
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

RESULT_SECTIONS = frozenset(
    {
        "presence_re_evaluation_boundary_metadata",
        "declared_presence_re_evaluation_boundary_request",
        "specification_validation",
        "prior_presence_artifact_validation",
        "receipt_operation_artifact_validation",
        "correspondence_and_changed_condition_validation",
        "compact_upstream_standing",
        "lineage_preservation_posture",
        "perishability_posture",
        "boundary_decision",
        "block",
        "boundary_posture",
        "presence_re_evaluation_boundary",
        "presence_re_evaluation_boundary_checks",
        "presence_re_evaluation_boundary_statement",
        "presence_re_evaluation_boundary_non_meaning",
        "omission_posture",
        "blocked_routes",
        "admissible_future_route",
        "what_remains_open",
        "non_claims",
        "result_level_non_claims_canonical_false",
        "outcome",
        "boundary_result",
        "completed_consideration_posture_count",
        "failed_check_count",
        "passed_check_count",
        "resolver_module",
        "result_version",
        "presence_re_evaluation_boundary_summary",
    }
)


class PresenceReEvaluationBoundaryV0MinError(Exception):
    """Raised for invalid request paths and refused result writes."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {field: True for field in OMISSION_POSTURE_FIELDS}


def _canonical_lineage_posture() -> dict[str, bool]:
    return {field: True for field in LINEAGE_POSTURE_FIELDS}


def _canonical_perishability_posture() -> dict[str, bool]:
    return {field: True for field in PERISHABILITY_POSTURE_FIELDS}


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _identity_request_values() -> dict[str, Any]:
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "governing_presence_re_evaluation_boundary_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "prior_presence_operation_artifact_path": str(
            PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_answerable_receipt_operation_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "prior_presence_operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "prior_presence_operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "prior_presence_operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
        "prior_presence_operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
        "prior_presence_operation_outcome_required": (
            PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED
        ),
        "prior_presence_result_required": PRIOR_PRESENCE_RESULT_REQUIRED,
        "receiver_answerable_receipt_operation_id": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID
        ),
        "receiver_answerable_receipt_operation_type": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE
        ),
        "receiver_answerable_receipt_operation_version": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION
        ),
        "receiver_answerable_receipt_operation_scope": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE
        ),
        "receiver_answerable_receipt_operation_outcome_required": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED
        ),
        "receiver_answerable_receipt_operation_result_required": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _new_canonical_request() -> dict[str, Any]:
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_identity_request_values(),
        "presence_re_evaluation_operation_consideration_selected": True,
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    return request


def build_presence_re_evaluation_boundary_v0_min_request() -> dict[str, Any]:
    """Return one fresh canonical presence re-evaluation boundary request."""
    return _new_canonical_request()


def build_declared_presence_re_evaluation_boundary_v0_min_request(
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
        "presence_re_evaluation_operation_consideration_selected",
        "declared_non_claims",
        *PROHIBITED_REQUEST_FLAGS,
    }


def _direct_preclaim_fields() -> set[str]:
    return {
        "outcome",
        "boundary_result",
        "decision_code",
        "decision_reason",
        "presence_re_evaluation_boundary_recorded",
        "presence_re_evaluation_boundary_result_recorded",
        "presence_re_evaluation_operation_consideration_allowed",
        "presence_re_evaluation_operation_consideration_not_allowed",
        "presence_re_evaluation_boundary_exhausted",
        *REQUIRED_FALSE_NON_CLAIMS,
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
        payload = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_json_keys,
        )
    except _DuplicateJsonKeyError:
        return None, "duplicate_key"
    except (TypeError, ValueError, json.JSONDecodeError):
        return None, "not_parseable"
    return payload, None


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


def _exact_bool(value: Any, expected: bool) -> bool:
    return type(value) is bool and value is expected


def _exact_int(value: Any, expected: int) -> bool:
    return type(value) is int and value == expected


def _non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _true_mapping_valid(value: Any, fields: tuple[str, ...]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(fields)
        and all(value.get(field) is True for field in fields)
    )


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

    if set(request).intersection(_direct_preclaim_fields()):
        _add_failure(
            checks,
            "request.direct_result_preclaim",
            "RESULT_POSTURE_PRECLAIMED",
        )
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "caller supplied a direct result or downstream posture",
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
        code, reason = _require(
            checks,
            "request." + field,
            request.get(field) == expected,
            "REQUEST_VALUE_MISMATCH",
            field + " does not match the canonical request",
            expected=expected,
        )
        if code is not None:
            return code, reason

    selection = request.get(
        "presence_re_evaluation_operation_consideration_selected"
    )
    code, reason = _require(
        checks,
        "request.presence_re_evaluation_operation_consideration_selected",
        type(selection) is bool,
        "REQUEST_BOOLEAN_REQUIRED",
        "re-evaluation consideration selection must be an exact Boolean",
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

    for field, block_code in PROHIBITED_REQUEST_FLAGS.items():
        code, reason = _require(
            checks,
            "request." + field,
            _exact_bool(request.get(field), False),
            block_code,
            field + " must remain exact Boolean false",
            expected=False,
        )
        if code is not None:
            return code, reason
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
            "governing presence re-evaluation specification is unavailable",
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


def _empty_prior_validation() -> dict[str, Any]:
    return {
        "artifact_path": str(PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH),
        "artifact_validated": False,
        "identity_validated": False,
        "waiting_result_validated": False,
        "true_postures_validated": False,
        "false_postures_validated": False,
        "artifact_truthful_and_unblocked": False,
        "standing": {},
    }


def _validate_prior_presence_artifact(
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_prior_validation()
    artifact, error = _read_json(PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH)
    if error in {"not_a_file", "unreadable"}:
        _add_failure(checks, "prior.reference", "PRIOR_PRESENCE_ARTIFACT_MISSING")
        return (
            "PRIOR_PRESENCE_ARTIFACT_MISSING",
            "exact prior presence artifact is unavailable",
            validation,
        )
    if error == "duplicate_key":
        _add_failure(
            checks,
            "prior.strict_json",
            "PRIOR_PRESENCE_ARTIFACT_DUPLICATE_KEYED",
        )
        return (
            "PRIOR_PRESENCE_ARTIFACT_DUPLICATE_KEYED",
            "prior presence artifact contains duplicate JSON keys",
            validation,
        )
    if error == "not_parseable":
        _add_failure(
            checks,
            "prior.strict_json",
            "PRIOR_PRESENCE_ARTIFACT_NOT_PARSEABLE",
        )
        return (
            "PRIOR_PRESENCE_ARTIFACT_NOT_PARSEABLE",
            "prior presence artifact is not parseable JSON",
            validation,
        )
    if not isinstance(artifact, Mapping):
        _add_failure(
            checks,
            "prior.mapping",
            "PRIOR_PRESENCE_ARTIFACT_NOT_MAPPING",
        )
        return (
            "PRIOR_PRESENCE_ARTIFACT_NOT_MAPPING",
            "prior presence artifact is not a mapping",
            validation,
        )
    checks.append(_check("prior.strict_json_mapping", True))

    operation = artifact.get("presence_operation")
    summary = artifact.get("presence_operation_summary")
    block = artifact.get("block")
    if not all(isinstance(value, Mapping) for value in (operation, summary, block)):
        _add_failure(
            checks,
            "prior.required_sections",
            "PRIOR_PRESENCE_ARTIFACT_SECTION_MISSING",
        )
        return (
            "PRIOR_PRESENCE_ARTIFACT_SECTION_MISSING",
            "prior presence artifact lacks canonical bounded sections",
            validation,
        )
    checks.append(_check("prior.required_sections", True))

    metadata_expectations = (
        ("resolver_module", artifact.get("resolver_module"), PRIOR_PRESENCE_RESOLVER_MODULE),
        ("result_version", artifact.get("result_version"), RESULT_VERSION),
        ("outcome", artifact.get("outcome"), PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED),
        ("summary.outcome", summary.get("outcome"), PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED),
        ("summary.failed_check_count", summary.get("failed_check_count"), 0),
        (
            "summary.passed_check_count",
            summary.get("passed_check_count"),
            PRIOR_PRESENCE_PASSED_CHECK_COUNT,
        ),
    )
    for name, actual, expected in metadata_expectations:
        if isinstance(expected, int):
            valid = _exact_int(actual, expected)
            failure_code = (
                "PRIOR_PRESENCE_FAILED_CHECKS_PRESENT"
                if name.endswith("failed_check_count")
                else "PRIOR_PRESENCE_METADATA_MISMATCH"
            )
        else:
            valid = actual == expected
            failure_code = "PRIOR_PRESENCE_METADATA_MISMATCH"
        code, reason = _require(
            checks,
            "prior." + name,
            valid,
            failure_code,
            "prior presence metadata mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "prior.blocked",
        _exact_bool(block.get("blocked"), False),
        "PRIOR_PRESENCE_BLOCKED",
        "prior presence artifact is blocked or lacks exact false posture",
        expected=False,
    )
    if code is not None:
        return code, reason, validation

    identity_expectations = {
        "operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
        "operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
        "presence_operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "presence_operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "presence_operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
        "presence_operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
    }
    for field, expected in identity_expectations.items():
        code, reason = _require(
            checks,
            "prior.identity." + field,
            operation.get(field) == expected,
            "PRIOR_PRESENCE_IDENTITY_MISMATCH",
            "prior presence identity mismatch: " + field,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    for location, actual in (
        ("operation.presence_result", operation.get("presence_result")),
        ("summary.presence_result", summary.get("presence_result")),
    ):
        code, reason = _require(
            checks,
            "prior." + location,
            actual == PRIOR_PRESENCE_RESULT_REQUIRED,
            "PRIOR_PRESENCE_RESULT_MISMATCH",
            "prior presence result is not the exact waiting result",
            expected=PRIOR_PRESENCE_RESULT_REQUIRED,
        )
        if code is not None:
            return code, reason, validation

    for field in PRIOR_TRUE_POSTURES:
        code, reason = _require(
            checks,
            "prior.true_posture." + field,
            _exact_bool(operation.get(field), True),
            "PRIOR_PRESENCE_TRUE_POSTURE_NOT_TRUE",
            "required prior presence posture is not exact true: " + field,
            expected=True,
        )
        if code is not None:
            return code, reason, validation
    for field in PRIOR_FALSE_POSTURES:
        code, reason = _require(
            checks,
            "prior.false_posture." + field,
            _exact_bool(operation.get(field), False),
            "PRIOR_PRESENCE_FALSE_POSTURE_NOT_FALSE",
            "required prior presence posture is not exact false: " + field,
            expected=False,
        )
        if code is not None:
            return code, reason, validation

    validation.update(
        {
            "artifact_validated": True,
            "identity_validated": True,
            "waiting_result_validated": True,
            "true_postures_validated": True,
            "false_postures_validated": True,
            "artifact_truthful_and_unblocked": True,
            "standing": {
                "operation_id": PRIOR_PRESENCE_OPERATION_ID,
                "operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
                "operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
                "operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
                "outcome": PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
                "presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
                "receiver_answerable_receipt_present": False,
                "presence_supported": False,
                "presence_authorized": False,
                "presence_established": False,
                "presence_recorded": False,
            },
        }
    )
    return None, None, validation


def _empty_receipt_validation() -> dict[str, Any]:
    return {
        "artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "artifact_validated": False,
        "identity_validated": False,
        "recorded_result_validated": False,
        "completed_result_cardinality_validated": False,
        "operation_completed_and_exhausted": False,
        "receipt_recorded_and_present": False,
        "false_locks_validated": False,
        "result_level_non_claims_canonical_false": False,
        "future_route_validated": False,
        "standing": {},
    }


def _validate_receipt_operation_artifact(
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_receipt_validation()
    artifact, error = _read_json(
        RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
    )
    if error in {"not_a_file", "unreadable"}:
        _add_failure(checks, "receipt.reference", "RECEIPT_ARTIFACT_MISSING")
        return (
            "RECEIPT_ARTIFACT_MISSING",
            "exact changed-condition receipt artifact is unavailable",
            validation,
        )
    if error == "duplicate_key":
        _add_failure(
            checks,
            "receipt.strict_json",
            "RECEIPT_ARTIFACT_DUPLICATE_KEYED",
        )
        return (
            "RECEIPT_ARTIFACT_DUPLICATE_KEYED",
            "receipt artifact contains duplicate JSON keys",
            validation,
        )
    if error == "not_parseable":
        _add_failure(
            checks,
            "receipt.strict_json",
            "RECEIPT_ARTIFACT_NOT_PARSEABLE",
        )
        return (
            "RECEIPT_ARTIFACT_NOT_PARSEABLE",
            "receipt artifact is not parseable JSON",
            validation,
        )
    if not isinstance(artifact, Mapping):
        _add_failure(checks, "receipt.mapping", "RECEIPT_ARTIFACT_NOT_MAPPING")
        return (
            "RECEIPT_ARTIFACT_NOT_MAPPING",
            "receipt artifact is not a mapping",
            validation,
        )
    checks.append(_check("receipt.strict_json_mapping", True))

    operation = artifact.get(
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_summary"
    )
    block = artifact.get("block")
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (operation, summary, block, non_claims)
    ):
        _add_failure(
            checks,
            "receipt.required_sections",
            "RECEIPT_ARTIFACT_SECTION_MISSING",
        )
        return (
            "RECEIPT_ARTIFACT_SECTION_MISSING",
            "receipt artifact lacks canonical bounded sections",
            validation,
        )
    checks.append(_check("receipt.required_sections", True))

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
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED,
        ),
        ("failed_check_count", artifact.get("failed_check_count"), 0),
        (
            "passed_check_count",
            artifact.get("passed_check_count"),
            RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT,
        ),
    )
    for name, actual, expected in metadata_expectations:
        if isinstance(expected, int):
            valid = _exact_int(actual, expected)
            failure_code = (
                "RECEIPT_FAILED_CHECKS_PRESENT"
                if name == "failed_check_count"
                else "RECEIPT_METADATA_MISMATCH"
            )
        else:
            valid = actual == expected
            failure_code = "RECEIPT_METADATA_MISMATCH"
        code, reason = _require(
            checks,
            "receipt." + name,
            valid,
            failure_code,
            "receipt metadata mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    code, reason = _require(
        checks,
        "receipt.blocked",
        _exact_bool(block.get("blocked"), False)
        and _exact_bool(summary.get("blocked"), False),
        "RECEIPT_BLOCKED",
        "receipt artifact is blocked or lacks exact false posture",
        expected=False,
    )
    if code is not None:
        return code, reason, validation

    identity_expectations = {
        "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
        "operation_type": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
        "operation_version": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
        "operation_scope": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_id"
        ): RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_type"
        ): RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_version"
        ): RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_scope"
        ): RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
    }
    for field, expected in identity_expectations.items():
        code, reason = _require(
            checks,
            "receipt.identity." + field,
            operation.get(field) == expected,
            "RECEIPT_IDENTITY_MISMATCH",
            "receipt operation identity mismatch: " + field,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    for location, actual in (
        ("top.operation_result", artifact.get("operation_result")),
        (
            "operation.operation_result",
            operation.get("receiver_answerable_receipt_operation_result"),
        ),
        ("summary.operation_result", summary.get("operation_result")),
    ):
        code, reason = _require(
            checks,
            "receipt." + location,
            actual == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED,
            "RECEIPT_RESULT_MISMATCH",
            "receipt artifact does not record the exact required result",
            expected=RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED,
        )
        if code is not None:
            return code, reason, validation

    for field in RECEIPT_TRUE_POSTURES:
        code, reason = _require(
            checks,
            "receipt.true_posture." + field,
            _exact_bool(operation.get(field), True),
            "RECEIPT_TRUE_POSTURE_NOT_TRUE",
            "required receipt posture is not exact true: " + field,
            expected=True,
        )
        if code is not None:
            return code, reason, validation
    for field in RECEIPT_FALSE_POSTURES:
        code, reason = _require(
            checks,
            "receipt.false_posture." + field,
            _exact_bool(operation.get(field), False),
            "RECEIPT_FALSE_POSTURE_NOT_FALSE",
            "required receipt false lock is missing or not false: " + field,
            expected=False,
        )
        if code is not None:
            return code, reason, validation

    count = operation.get("completed_result_posture_count")
    code, reason = _require(
        checks,
        "receipt.completed_result_posture_count",
        _exact_int(count, 1)
        and _exact_int(summary.get("completed_result_posture_count"), 1),
        "RECEIPT_RESULT_CARDINALITY_MISMATCH",
        "exactly one completed receipt result posture must stand",
        expected=1,
    )
    if code is not None:
        return code, reason, validation

    canonical_non_claims = (
        bool(non_claims)
        and all(type(value) is bool and value is False for value in non_claims.values())
        and _exact_bool(
            artifact.get("result_level_non_claims_canonical_false"),
            True,
        )
        and _exact_bool(
            summary.get("result_level_non_claims_canonical_false"),
            True,
        )
    )
    code, reason = _require(
        checks,
        "receipt.result_level_non_claims",
        canonical_non_claims,
        "RECEIPT_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "receipt result-level non-claims are not canonical false",
    )
    if code is not None:
        return code, reason, validation

    route_valid = (
        artifact.get("admissible_future_route")
        == RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE
        and summary.get("admissible_future_route")
        == RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE
    )
    code, reason = _require(
        checks,
        "receipt.admissible_future_route",
        route_valid,
        "RECEIPT_FUTURE_ROUTE_MISMATCH",
        "receipt future route does not name this separate boundary",
        expected=RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE,
    )
    if code is not None:
        return code, reason, validation

    validation.update(
        {
            "artifact_validated": True,
            "identity_validated": True,
            "recorded_result_validated": True,
            "completed_result_cardinality_validated": True,
            "operation_completed_and_exhausted": True,
            "receipt_recorded_and_present": True,
            "false_locks_validated": True,
            "result_level_non_claims_canonical_false": True,
            "future_route_validated": True,
            "standing": {
                "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
                "operation_type": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
                "operation_version": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
                "operation_scope": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
                "outcome": (
                    RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED
                ),
                "operation_result": (
                    RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED
                ),
                "receiver_answerable_receipt_recorded": True,
                "receiver_answerable_receipt_present": True,
                "completed_result_posture_count": 1,
                "operation_completed_and_exhausted": True,
                "downstream_false_locks_preserved": True,
                "admissible_future_route": (
                    RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE
                ),
            },
        }
    )
    return None, None, validation


def _empty_correspondence_validation() -> dict[str, Any]:
    return {
        "prior_presence_result": None,
        "prior_receiver_answerable_receipt_present": None,
        "later_receiver_answerable_receipt_present": None,
        "later_receiver_answerable_receipt_recorded": None,
        "later_operation_completed_and_exhausted": False,
        "later_completed_result_posture_count": 0,
        "later_future_route": None,
        "later_downstream_false_locks_preserved": False,
        "artifacts_remain_separate_standing": False,
        "no_overwrite_invalidation_supersession_repair_or_replacement": False,
        "changed_condition_validated": False,
    }


def _validate_correspondence(
    request: Mapping[str, Any],
    prior: Mapping[str, Any],
    receipt: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_correspondence_validation()
    prior_standing = prior.get("standing")
    receipt_standing = receipt.get("standing")
    if not isinstance(prior_standing, Mapping) or not isinstance(
        receipt_standing,
        Mapping,
    ):
        _add_failure(
            checks,
            "correspondence.standing",
            "CHANGED_CONDITION_MISMATCH",
        )
        return (
            "CHANGED_CONDITION_MISMATCH",
            "validated compact upstream standing is unavailable",
            validation,
        )

    expectations = (
        (
            "prior_presence_result",
            prior_standing.get("presence_result"),
            PRIOR_PRESENCE_RESULT_REQUIRED,
        ),
        (
            "prior_receiver_answerable_receipt_present",
            prior_standing.get("receiver_answerable_receipt_present"),
            False,
        ),
        (
            "later_receiver_answerable_receipt_present",
            receipt_standing.get("receiver_answerable_receipt_present"),
            True,
        ),
        (
            "later_receiver_answerable_receipt_recorded",
            receipt_standing.get("receiver_answerable_receipt_recorded"),
            True,
        ),
        (
            "later_operation_completed_and_exhausted",
            receipt_standing.get("operation_completed_and_exhausted"),
            True,
        ),
        (
            "later_completed_result_posture_count",
            receipt_standing.get("completed_result_posture_count"),
            1,
        ),
        (
            "later_future_route",
            receipt_standing.get("admissible_future_route"),
            RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE,
        ),
        (
            "later_downstream_false_locks_preserved",
            receipt_standing.get("downstream_false_locks_preserved"),
            True,
        ),
    )
    for name, actual, expected in expectations:
        if type(expected) is bool:
            valid = _exact_bool(actual, expected)
        elif type(expected) is int:
            valid = _exact_int(actual, expected)
        else:
            valid = actual == expected
        validation[name] = copy.deepcopy(actual)
        code, reason = _require(
            checks,
            "correspondence." + name,
            valid,
            "CHANGED_CONDITION_MISMATCH",
            "changed-condition correspondence mismatch: " + name,
            expected=expected,
        )
        if code is not None:
            return code, reason, validation

    separate = (
        request.get("prior_presence_operation_artifact_path")
        != request.get("receiver_answerable_receipt_operation_artifact_path")
        and prior_standing.get("operation_id")
        != receipt_standing.get("operation_id")
    )
    code, reason = _require(
        checks,
        "correspondence.artifacts_remain_separate_standing",
        separate,
        "SEPARATE_STANDING_NOT_PRESERVED",
        "prior presence and later receipt artifacts must remain separate",
        expected=True,
    )
    if code is not None:
        return code, reason, validation

    mutation_flags = (
        "request_prior_presence_operation_overwrite",
        "request_prior_presence_operation_invalidation",
        "request_prior_presence_operation_supersession",
        "request_prior_presence_operation_repair",
        "request_prior_presence_operation_replacement",
        "request_prior_presence_operation_normalization",
    )
    no_mutation = all(request.get(field) is False for field in mutation_flags)
    code, reason = _require(
        checks,
        "correspondence.no_prior_mutation",
        no_mutation,
        "SEPARATE_STANDING_NOT_PRESERVED",
        "prior presence standing must not be overwritten or repaired",
        expected=True,
    )
    if code is not None:
        return code, reason, validation

    validation.update(
        {
            "artifacts_remain_separate_standing": True,
            "no_overwrite_invalidation_supersession_repair_or_replacement": (
                True
            ),
            "changed_condition_validated": True,
        }
    )
    return None, None, validation


def _append_generated_posture_checks(
    checks: list[dict[str, Any]],
) -> None:
    for field in LINEAGE_POSTURE_FIELDS:
        checks.append(_check("lineage." + field, True, expected=True))
    for field in PERISHABILITY_POSTURE_FIELDS:
        checks.append(_check("perishability." + field, True, expected=True))
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
    for field in NON_MEANING_FIELDS:
        checks.append(_check("non_meaning." + field, True, expected=True))


def _branch_values(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    not_allowed = outcome == OUTCOME_NOT_ALLOWED
    completed = allowed or not_allowed
    return {
        "presence_re_evaluation_boundary_recorded": completed,
        "presence_re_evaluation_boundary_result_recorded": completed,
        "presence_re_evaluation_operation_consideration_allowed": allowed,
        "presence_re_evaluation_operation_consideration_not_allowed": (
            not_allowed
        ),
        "presence_re_evaluation_boundary_exhausted": completed,
        "completed_consideration_posture_count": int(allowed)
        + int(not_allowed),
    }


def _append_branch_checks(
    checks: list[dict[str, Any]],
    outcome: str,
) -> None:
    for field, value in _branch_values(outcome).items():
        checks.append(_check("branch." + field, True, expected=value))


def _boundary_result_for_outcome(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return RESULT_ALLOWED
    if outcome == OUTCOME_NOT_ALLOWED:
        return RESULT_NOT_ALLOWED
    return RESULT_NOT_EVALUATED


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


def _declared_request_posture(
    request: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    selection = request.get(
        "presence_re_evaluation_operation_consideration_selected"
    )
    return {
        "intent_validated": request.get("intent") == INTENT_RECORD,
        "canonical_identity_and_paths_validated": all(
            request.get(field) == expected
            for field, expected in _identity_request_values().items()
        ),
        "presence_re_evaluation_operation_consideration_selected": (
            selection if completed and type(selection) is bool else False
        ),
        "declared_non_claims_validated": _non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
        "unknown_request_fields_absent": (
            set(request).difference(_canonical_request_keys()) == set()
        ),
    }


def _boundary_object(
    outcome: str,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    branch = _branch_values(outcome)
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    selection = request.get(
        "presence_re_evaluation_operation_consideration_selected"
    )
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "presence_re_evaluation_boundary_id": BOUNDARY_ID,
        "presence_re_evaluation_boundary_type": BOUNDARY_TYPE,
        "presence_re_evaluation_boundary_version": BOUNDARY_VERSION,
        "presence_re_evaluation_boundary_scope": BOUNDARY_SCOPE,
        "prior_presence_operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "prior_presence_operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "prior_presence_operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
        "prior_presence_operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
        "prior_presence_operation_outcome_required": (
            PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED
        ),
        "prior_presence_result_required": PRIOR_PRESENCE_RESULT_REQUIRED,
        "receiver_answerable_receipt_operation_id": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID
        ),
        "receiver_answerable_receipt_operation_type": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE
        ),
        "receiver_answerable_receipt_operation_version": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION
        ),
        "receiver_answerable_receipt_operation_scope": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE
        ),
        "receiver_answerable_receipt_operation_outcome_required": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED
        ),
        "receiver_answerable_receipt_operation_result_required": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED
        ),
        "presence_re_evaluation_operation_consideration_selected": (
            selection if completed and type(selection) is bool else False
        ),
        "presence_re_evaluation_boundary_result": (
            _boundary_result_for_outcome(outcome)
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **branch,
        **_canonical_non_claims(),
        "presence_lapse_result_recorded": False,
        "scheduled_presence_re_evaluation_created": False,
        "scheduled_presence_lapse_created": False,
        "automatic_next_step_created": False,
    }


def _statement(outcome: str) -> dict[str, bool]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    return {
        "one_exact_prior_presence_artifact_read": completed,
        "one_exact_changed_condition_receipt_artifact_read": completed,
        "both_artifacts_preserved_as_separate_standing": completed,
        "changed_condition_validated_without_overwrite": completed,
        "presence_re_evaluation_consideration_only": completed,
        "presence_re_evaluation_operation_not_created_or_executed": True,
        "revised_presence_result_not_selected_or_recorded": True,
        "presence_not_supported_authorized_established_or_recorded": True,
        "receiver_answerable_basis_remaining_conditions_not_preclaimed": True,
        "no_lapse_route_or_result_created": True,
        "boundary_single_use_only": completed,
        "result_level_non_claims_canonical_false": True,
        "open_does_not_mean_next": True,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("presence_re_evaluation_boundary")
    boundary = boundary if isinstance(boundary, Mapping) else {}
    specification = result.get("specification_validation")
    specification = (
        specification if isinstance(specification, Mapping) else {}
    )
    prior = result.get("prior_presence_artifact_validation")
    prior = prior if isinstance(prior, Mapping) else {}
    receipt = result.get("receipt_operation_artifact_validation")
    receipt = receipt if isinstance(receipt, Mapping) else {}
    correspondence = result.get(
        "correspondence_and_changed_condition_validation"
    )
    correspondence = (
        correspondence if isinstance(correspondence, Mapping) else {}
    )
    lineage = result.get("lineage_preservation_posture")
    lineage = lineage if isinstance(lineage, Mapping) else {}
    perishability = result.get("perishability_posture")
    perishability = (
        perishability if isinstance(perishability, Mapping) else {}
    )
    decision = result.get("boundary_decision")
    decision = decision if isinstance(decision, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
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
        "prior_presence_artifact_path": str(
            PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "receipt_operation_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "prior_presence_operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "receipt_operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
        "prior_required_presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
        "required_receipt_result": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED
        ),
        "outcome": result.get("outcome"),
        "boundary_result": result.get("boundary_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("decision_code"),
        "decision_reason": decision.get("decision_reason"),
        "selection": boundary.get(
            "presence_re_evaluation_operation_consideration_selected"
        ),
        "specification_validated": specification.get(
            "specification_validated"
        ),
        "prior_presence_artifact_validated": prior.get(
            "artifact_validated"
        ),
        "receipt_operation_artifact_validated": receipt.get(
            "artifact_validated"
        ),
        "changed_condition_validated": correspondence.get(
            "changed_condition_validated"
        ),
        "prior_receipt_absence_validated": (
            correspondence.get("prior_receiver_answerable_receipt_present")
            is False
        ),
        "later_receipt_presence_validated": (
            correspondence.get("later_receiver_answerable_receipt_present")
            is True
        ),
        "prior_presence_result_preserved": lineage.get(
            "prior_presence_result_preserved"
        ),
        "later_receipt_result_preserved": lineage.get(
            "later_receipt_result_preserved"
        ),
        "no_overwrite_validated": lineage.get(
            "changed_standing_recorded_without_overwrite"
        ),
        "boundary_recorded": boundary.get(
            "presence_re_evaluation_boundary_recorded"
        ),
        "boundary_result_recorded": boundary.get(
            "presence_re_evaluation_boundary_result_recorded"
        ),
        "boundary_exhausted": boundary.get(
            "presence_re_evaluation_boundary_exhausted"
        ),
        "consideration_allowed": boundary.get(
            "presence_re_evaluation_operation_consideration_allowed"
        ),
        "consideration_not_allowed": boundary.get(
            "presence_re_evaluation_operation_consideration_not_allowed"
        ),
        "presence_re_evaluation_operation_absent": (
            boundary.get("presence_re_evaluation_operation_created") is False
            and boundary.get("presence_re_evaluation_operation_executed")
            is False
        ),
        "revised_presence_result_absent": (
            boundary.get("presence_re_evaluation_result_recorded") is False
        ),
        "presence_absent": all(
            boundary.get(field) is False
            for field in (
                "presence_supported",
                "presence_authorized",
                "presence_established",
                "presence_recorded",
            )
        ),
        "custody_distinctness_absent": (
            boundary.get("receiver_answerable_basis_custody_distinct")
            is False
        ),
        "refusability_absent": (
            boundary.get("receiver_answerable_basis_refusable") is False
        ),
        "could_have_been_withheld_absent": (
            boundary.get(
                "receiver_answerable_basis_could_have_been_withheld"
            )
            is False
        ),
        "durable_presence_absent": all(
            boundary.get(field) is False
            for field in (
                "durable_presence_created",
                "permanent_presence_created",
                "irrevocable_presence_created",
                "self_renewing_presence_created",
            )
        ),
        "lapse_route_absent": all(
            boundary.get(field) is False
            for field in (
                "presence_lapse_boundary_created",
                "presence_lapse_operation_created",
                "presence_lapse_result_recorded",
                "presence_lapsed",
                "presence_expired",
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
        "perishability_preserved": (
            bool(perishability)
            and all(value is True for value in perishability.values())
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    prior_validation: Mapping[str, Any] | None = None,
    receipt_validation: Mapping[str, Any] | None = None,
    correspondence_validation: Mapping[str, Any] | None = None,
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
    receipt = (
        copy.deepcopy(dict(receipt_validation))
        if isinstance(receipt_validation, Mapping)
        else _empty_receipt_validation()
    )
    correspondence = (
        copy.deepcopy(dict(correspondence_validation))
        if isinstance(correspondence_validation, Mapping)
        else _empty_correspondence_validation()
    )
    boundary = _boundary_object(outcome, request)
    branch = _branch_values(outcome)
    decision = _decision_for_outcome(outcome, code=code, reason=reason)
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    result: dict[str, Any] = {
        "presence_re_evaluation_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "prior_presence_artifact_path": str(
                PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
            "receipt_operation_artifact_path": str(
                RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
        },
        "declared_presence_re_evaluation_boundary_request": (
            _declared_request_posture(request, outcome)
        ),
        "specification_validation": specification,
        "prior_presence_artifact_validation": prior,
        "receipt_operation_artifact_validation": receipt,
        "correspondence_and_changed_condition_validation": correspondence,
        "compact_upstream_standing": {
            "prior_presence": copy.deepcopy(prior.get("standing", {})),
            "later_receipt": copy.deepcopy(receipt.get("standing", {})),
            "artifacts_remain_separate_standing": correspondence.get(
                "artifacts_remain_separate_standing"
            )
            is True,
            "complete_upstream_artifacts_not_embedded": True,
            "source_bodies_not_read": True,
        },
        "lineage_preservation_posture": _canonical_lineage_posture(),
        "perishability_posture": _canonical_perishability_posture(),
        "boundary_decision": {
            **decision,
            "selection": (
                request.get(
                    "presence_re_evaluation_operation_consideration_selected"
                )
                if completed
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
            "single_use_only": True,
            "boundary_exhaustion_is_not_re_evaluation_completion": True,
            "boundary_exhaustion_is_not_presence": True,
        },
        "presence_re_evaluation_boundary": boundary,
        "presence_re_evaluation_boundary_checks": copy.deepcopy(checks),
        "presence_re_evaluation_boundary_statement": _statement(outcome),
        "presence_re_evaluation_boundary_non_meaning": (
            _canonical_non_meaning()
        ),
        "omission_posture": _canonical_omission_posture(),
        "blocked_routes": list(BLOCKED_ROUTES),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        "outcome": outcome,
        "boundary_result": _boundary_result_for_outcome(outcome),
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
    result["presence_re_evaluation_boundary_summary"] = (
        _summary_from_result(result)
    )
    return result


def resolve_presence_re_evaluation_boundary_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact presence re-evaluation boundary without side effects."""
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

    code, reason, prior = _validate_prior_presence_artifact(checks)
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

    code, reason, receipt = _validate_receipt_operation_artifact(checks)
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            receipt_validation=receipt,
            code=code,
            reason=reason,
        )

    code, reason, correspondence = _validate_correspondence(
        declared_request,
        prior,
        receipt,
        checks,
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            prior_validation=prior,
            receipt_validation=receipt,
            correspondence_validation=correspondence,
            code=code,
            reason=reason,
        )

    _append_generated_posture_checks(checks)
    selected = declared_request[
        "presence_re_evaluation_operation_consideration_selected"
    ]
    checks.append(
        _check(
            "decision.presence_re_evaluation_operation_consideration_selected",
            True,
            expected=selected,
        )
    )
    outcome = OUTCOME_ALLOWED if selected else OUTCOME_NOT_ALLOWED
    _append_branch_checks(checks, outcome)
    return _build_result(
        declared_request,
        outcome,
        checks,
        specification_validation=specification,
        prior_validation=prior,
        receipt_validation=receipt,
        correspondence_validation=correspondence,
    )


def resolve_presence_re_evaluation_boundary_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Strictly load one request path and resolve it without discovery."""
    payload, error = _read_json(request_path)
    if error is not None:
        raise PresenceReEvaluationBoundaryV0MinError(
            "invalid request path JSON: " + error
        )
    if not isinstance(payload, Mapping):
        raise PresenceReEvaluationBoundaryV0MinError(
            "invalid request path JSON: top-level value must be a mapping"
        )
    return resolve_presence_re_evaluation_boundary_v0_min(payload)


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "complete_prior_presence_artifact",
        "complete_changed_condition_receipt_artifact",
        "prior_presence_artifact",
        "changed_condition_receipt_artifact",
        "complete_receipt_operation_artifact",
        "complete_candidate_sufficiency_material",
        "sufficiency_basis_records",
        "basis_items",
        "basis_references",
        "bounded_capture_source_bodies",
        "archive_bytes",
        "archive_body",
        "hash_record_body",
        "text_component_bodies",
        "recorded_signal_body",
        "capture_signal_data",
        "signal_samples",
        "raw_signal_data",
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
    checks = result.get("presence_re_evaluation_boundary_checks")
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
        and (
            "expected" not in check
            or isinstance(check.get("expected"), (str, int, bool))
        )
        for check in checks
    ):
        return False
    failed = sum(check.get("passed") is False for check in checks)
    passed = sum(check.get("passed") is True for check in checks)
    if (
        type(result.get("failed_check_count")) is not int
        or type(result.get("passed_check_count")) is not int
        or result.get("failed_check_count") != failed
        or result.get("passed_check_count") != passed
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
    boundary = result.get("presence_re_evaluation_boundary")
    posture = result.get("boundary_posture")
    block = result.get("block")
    decision = result.get("boundary_decision")
    if (
        outcome not in OUTCOME_FAMILY
        or not isinstance(boundary, Mapping)
        or not isinstance(posture, Mapping)
        or not isinstance(block, Mapping)
        or not isinstance(decision, Mapping)
    ):
        return False
    expected_request = _new_canonical_request()
    expected_request[
        "presence_re_evaluation_operation_consideration_selected"
    ] = outcome == OUTCOME_ALLOWED
    if dict(boundary) != _boundary_object(str(outcome), expected_request):
        return False
    expected_branch = _branch_values(str(outcome))
    expected_posture = {
        **expected_branch,
        "single_use_only": True,
        "boundary_exhaustion_is_not_re_evaluation_completion": True,
        "boundary_exhaustion_is_not_presence": True,
    }
    if dict(posture) != expected_posture:
        return False
    common = (
        boundary.get("boundary_id") == BOUNDARY_ID
        and boundary.get("boundary_type") == BOUNDARY_TYPE
        and boundary.get("boundary_version") == BOUNDARY_VERSION
        and boundary.get("boundary_scope") == BOUNDARY_SCOPE
        and boundary.get("admissible_future_route") == ADMISSIBLE_FUTURE_ROUTE
        and boundary.get("prior_presence_operation_id")
        == PRIOR_PRESENCE_OPERATION_ID
        and boundary.get("prior_presence_operation_type")
        == PRIOR_PRESENCE_OPERATION_TYPE
        and boundary.get("prior_presence_operation_version")
        == PRIOR_PRESENCE_OPERATION_VERSION
        and boundary.get("prior_presence_operation_scope")
        == PRIOR_PRESENCE_OPERATION_SCOPE
        and boundary.get("prior_presence_operation_outcome_required")
        == PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED
        and boundary.get("prior_presence_result_required")
        == PRIOR_PRESENCE_RESULT_REQUIRED
        and boundary.get("receiver_answerable_receipt_operation_id")
        == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID
        and boundary.get("receiver_answerable_receipt_operation_type")
        == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE
        and boundary.get("receiver_answerable_receipt_operation_version")
        == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION
        and boundary.get("receiver_answerable_receipt_operation_scope")
        == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE
        and boundary.get(
            "receiver_answerable_receipt_operation_outcome_required"
        )
        == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED
        and boundary.get(
            "receiver_answerable_receipt_operation_result_required"
        )
        == RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED
        and boundary.get("presence_lapse_result_recorded") is False
        and boundary.get("scheduled_presence_re_evaluation_created") is False
        and boundary.get("scheduled_presence_lapse_created") is False
        and boundary.get("automatic_next_step_created") is False
        and all(
            boundary.get(field) is False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
        and all(
            _exact_bool(boundary.get(field), expected)
            if type(expected) is bool
            else _exact_int(boundary.get(field), expected)
            for field, expected in expected_branch.items()
        )
        and all(
            _exact_bool(posture.get(field), expected)
            if type(expected) is bool
            else _exact_int(posture.get(field), expected)
            for field, expected in expected_branch.items()
        )
        and posture.get("single_use_only") is True
        and posture.get(
            "boundary_exhaustion_is_not_re_evaluation_completion"
        )
        is True
        and posture.get("boundary_exhaustion_is_not_presence") is True
        and _exact_int(
            result.get("completed_consideration_posture_count"),
            expected_branch["completed_consideration_posture_count"],
        )
    )
    if not common:
        return False
    boundary_result = _boundary_result_for_outcome(str(outcome))
    if (
        result.get("boundary_result") != boundary_result
        or boundary.get("presence_re_evaluation_boundary_result")
        != boundary_result
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


def _supporting_sections_valid(result: Mapping[str, Any]) -> bool:
    metadata = result.get("presence_re_evaluation_boundary_metadata")
    declared = result.get(
        "declared_presence_re_evaluation_boundary_request"
    )
    specification = result.get("specification_validation")
    prior = result.get("prior_presence_artifact_validation")
    receipt = result.get("receipt_operation_artifact_validation")
    correspondence = result.get(
        "correspondence_and_changed_condition_validation"
    )
    compact = result.get("compact_upstream_standing")
    lineage = result.get("lineage_preservation_posture")
    perishability = result.get("perishability_posture")
    non_meaning = result.get("presence_re_evaluation_boundary_non_meaning")
    omission = result.get("omission_posture")
    if not all(
        isinstance(value, Mapping)
        for value in (
            metadata,
            declared,
            specification,
            prior,
            receipt,
            correspondence,
            compact,
            lineage,
            perishability,
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
        "prior_presence_artifact_path": str(
            PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "receipt_operation_artifact_path": str(
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
    }
    declared_fields = {
        "intent_validated",
        "canonical_identity_and_paths_validated",
        "presence_re_evaluation_operation_consideration_selected",
        "declared_non_claims_validated",
        "prohibited_request_flags_validated",
        "unknown_request_fields_absent",
    }
    specification_fields = {
        "specification_path",
        "marker_validation",
        "specification_validated",
    }
    prior_fields = {
        "artifact_path",
        "artifact_validated",
        "identity_validated",
        "waiting_result_validated",
        "true_postures_validated",
        "false_postures_validated",
        "artifact_truthful_and_unblocked",
        "standing",
    }
    receipt_fields = {
        "artifact_path",
        "artifact_validated",
        "identity_validated",
        "recorded_result_validated",
        "completed_result_cardinality_validated",
        "operation_completed_and_exhausted",
        "receipt_recorded_and_present",
        "false_locks_validated",
        "result_level_non_claims_canonical_false",
        "future_route_validated",
        "standing",
    }
    correspondence_fields = set(_empty_correspondence_validation())
    compact_fields = {
        "prior_presence",
        "later_receipt",
        "artifacts_remain_separate_standing",
        "complete_upstream_artifacts_not_embedded",
        "source_bodies_not_read",
    }
    common = (
        dict(metadata) == expected_metadata
        and set(declared) == declared_fields
        and all(type(value) is bool for value in declared.values())
        and set(specification) == specification_fields
        and isinstance(specification.get("marker_validation"), Mapping)
        and set(specification.get("marker_validation", {}))
        == {name for name, _ in SPEC_REQUIRED_MARKERS}
        and all(
            type(value) is bool
            for value in specification.get("marker_validation", {}).values()
        )
        and type(specification.get("specification_validated")) is bool
        and set(prior) == prior_fields
        and all(
            type(prior.get(field)) is bool
            for field in prior_fields - {"artifact_path", "standing"}
        )
        and isinstance(prior.get("standing"), Mapping)
        and set(receipt) == receipt_fields
        and all(
            type(receipt.get(field)) is bool
            for field in receipt_fields - {"artifact_path", "standing"}
        )
        and isinstance(receipt.get("standing"), Mapping)
        and set(correspondence) == correspondence_fields
        and all(
            value is None or isinstance(value, (str, int, bool))
            for value in correspondence.values()
        )
        and set(compact) == compact_fields
        and isinstance(compact.get("prior_presence"), Mapping)
        and isinstance(compact.get("later_receipt"), Mapping)
        and type(compact.get("artifacts_remain_separate_standing")) is bool
        and _true_mapping_valid(lineage, LINEAGE_POSTURE_FIELDS)
        and _true_mapping_valid(perishability, PERISHABILITY_POSTURE_FIELDS)
        and _true_mapping_valid(non_meaning, NON_MEANING_FIELDS)
        and _true_mapping_valid(omission, OMISSION_POSTURE_FIELDS)
        and result.get("blocked_routes") == list(BLOCKED_ROUTES)
        and result.get("what_remains_open") == list(WHAT_REMAINS_OPEN)
        and result.get("admissible_future_route") == ADMISSIBLE_FUTURE_ROUTE
        and result.get("presence_re_evaluation_boundary_statement")
        == _statement(str(result.get("outcome")))
        and specification.get("specification_path")
        == str(GOVERNING_SPECIFICATION_RELATIVE_PATH)
        and prior.get("artifact_path")
        == str(PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH)
        and receipt.get("artifact_path")
        == str(
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
        )
        and compact.get("complete_upstream_artifacts_not_embedded") is True
        and compact.get("source_bodies_not_read") is True
    )
    if not common:
        return False

    markers = specification.get("marker_validation")
    expected_prior_standing = {
        "operation_id": PRIOR_PRESENCE_OPERATION_ID,
        "operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "operation_version": PRIOR_PRESENCE_OPERATION_VERSION,
        "operation_scope": PRIOR_PRESENCE_OPERATION_SCOPE,
        "outcome": PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
        "presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
        "receiver_answerable_receipt_present": False,
        "presence_supported": False,
        "presence_authorized": False,
        "presence_established": False,
        "presence_recorded": False,
    }
    expected_receipt_standing = {
        "operation_id": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
        "operation_type": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE,
        "operation_version": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION,
        "operation_scope": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE,
        "outcome": RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED,
        "operation_result": (
            RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED
        ),
        "receiver_answerable_receipt_recorded": True,
        "receiver_answerable_receipt_present": True,
        "completed_result_posture_count": 1,
        "operation_completed_and_exhausted": True,
        "downstream_false_locks_preserved": True,
        "admissible_future_route": RECEIVER_ANSWERABLE_RECEIPT_FUTURE_ROUTE,
    }
    if prior.get("standing") not in ({}, expected_prior_standing):
        return False
    if receipt.get("standing") not in ({}, expected_receipt_standing):
        return False
    if compact.get("prior_presence") not in ({}, expected_prior_standing):
        return False
    if compact.get("later_receipt") not in ({}, expected_receipt_standing):
        return False
    if result.get("outcome") == OUTCOME_BLOCKED:
        return True
    return (
        declared.get("intent_validated") is True
        and declared.get("canonical_identity_and_paths_validated") is True
        and declared.get("declared_non_claims_validated") is True
        and declared.get("prohibited_request_flags_validated") is True
        and declared.get("unknown_request_fields_absent") is True
        and declared.get(
            "presence_re_evaluation_operation_consideration_selected"
        )
        is (result.get("outcome") == OUTCOME_ALLOWED)
        and specification.get("specification_validated") is True
        and isinstance(markers, Mapping)
        and set(markers) == {name for name, _ in SPEC_REQUIRED_MARKERS}
        and all(value is True for value in markers.values())
        and prior.get("artifact_validated") is True
        and prior.get("identity_validated") is True
        and prior.get("waiting_result_validated") is True
        and prior.get("true_postures_validated") is True
        and prior.get("false_postures_validated") is True
        and prior.get("artifact_truthful_and_unblocked") is True
        and prior.get("standing") == expected_prior_standing
        and receipt.get("artifact_validated") is True
        and receipt.get("identity_validated") is True
        and receipt.get("recorded_result_validated") is True
        and receipt.get("completed_result_cardinality_validated") is True
        and receipt.get("operation_completed_and_exhausted") is True
        and receipt.get("receipt_recorded_and_present") is True
        and receipt.get("false_locks_validated") is True
        and receipt.get("result_level_non_claims_canonical_false") is True
        and receipt.get("future_route_validated") is True
        and receipt.get("standing") == expected_receipt_standing
        and correspondence.get("changed_condition_validated") is True
        and correspondence.get(
            "artifacts_remain_separate_standing"
        )
        is True
        and correspondence.get(
            "no_overwrite_invalidation_supersession_repair_or_replacement"
        )
        is True
        and compact.get("prior_presence") == expected_prior_standing
        and compact.get("later_receipt") == expected_receipt_standing
        and compact.get("artifacts_remain_separate_standing") is True
    )


def _result_valid_for_write(result: Mapping[str, Any]) -> bool:
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
        or set(result) != RESULT_SECTIONS
        or not _branch_valid(result)
        or not _checks_valid(result)
        or not _supporting_sections_valid(result)
        or not _non_claims_valid(result.get("non_claims"))
        or result.get("result_level_non_claims_canonical_false") is not True
        or _contains_prohibited_complete_material(result)
    ):
        return False
    return result.get(
        "presence_re_evaluation_boundary_summary"
    ) == _summary_from_result(result)


def build_presence_re_evaluation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic summary without upstream material."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise PresenceReEvaluationBoundaryV0MinError(
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
        return _path_within(
            path.resolve(),
            CANONICAL_OUTPUT_ROOT.resolve(),
        )
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
    raise PresenceReEvaluationBoundaryV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def write_presence_re_evaluation_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid result under the canonical family without overwriting."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise PresenceReEvaluationBoundaryV0MinError(
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
        raise PresenceReEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise PresenceReEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: output path is protected or outside the "
            "presence-re-evaluation-boundary output family"
        )
    if target.exists() and explicit:
        raise PresenceReEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: explicit output path already exists"
        )
    if target.is_dir():
        raise PresenceReEvaluationBoundaryV0MinError(
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
        raise PresenceReEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: unable to write boundary result"
        ) from exc
    return target
