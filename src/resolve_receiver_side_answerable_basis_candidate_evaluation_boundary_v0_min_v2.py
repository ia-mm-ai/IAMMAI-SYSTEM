"""Resolve one bounded receiver-side candidate-evaluation boundary result.

This standalone v2 successor preserves the v1 boundary behavior while keeping
prior reception-operation locks distinct from current evaluation-boundary
locks. It reads only the governing specification and one declared reception
artifact; candidate material is never opened or copied into the result.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2"

BOUNDARY_ID = "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
BOUNDARY_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_EVALUATION_OF_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"

PRIOR_RECEPTION_OPERATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION"
PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED"
PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED"
PRIOR_RECEPTION_OPERATION_RECORDED_REQUIRED = True
PRIOR_RECEPTION_OPERATION_RESULT_RECORDED_REQUIRED = True
PRIOR_CANDIDATE_MATERIAL_SUPPLIED_REQUIRED = True
PRIOR_CANDIDATE_MATERIAL_RECEIVED_REQUIRED = True
PRIOR_CANDIDATE_MATERIAL_RECORDED_REQUIRED = True
PRIOR_CANDIDATE_MATERIAL_PRESERVED_REQUIRED = True
PRIOR_CANDIDATE_SOURCE_PROVENANCE_REFERENCE_SUPPLIED_REQUIRED = True
PRIOR_CANDIDATE_RECEIVED_REQUIRED = True
PRIOR_CANDIDATE_RECORDED_REQUIRED = True
PRIOR_CANDIDATE_EVALUATED_REQUIRED = False
PRIOR_RECEPTION_BOUNDARY_REFERENCED_REQUIRED = True
PRIOR_SECOND_CANDIDATE_RECEIVED_REQUIRED = False
PRIOR_REPEATED_RECEPTION_PERMISSION_CREATED_REQUIRED = False
PRIOR_REUSABLE_ROUTE_CREATED_REQUIRED = False
PRIOR_RECEIVER_ATTESTATION_CREATED_REQUIRED = False
PRIOR_RECEIVER_ATTESTATION_SUPPORTED_REQUIRED = False
PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED = False
PRIOR_CUSTODY_DISTINCT_REQUIRED = False
PRIOR_REFUSABLE_REQUIRED = False
PRIOR_COULD_HAVE_BEEN_WITHHELD_REQUIRED = False
PRIOR_PRESENCE_SUPPORTED_REQUIRED = False
PRIOR_PRESENCE_AUTHORIZED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_PRESENCE_RECORDED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
PRIOR_FAILED_CHECK_COUNT_REQUIRED = 0
ADMISSIBLE_FUTURE_ROUTE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_THEN_CANDIDATE_EVALUATION_OPERATION_ONLY"

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
SELECTED_RECEPTION_OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"

OUTCOME_ALLOWED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_REQUIRES_RECORDED_CANDIDATE_BASIS"
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

BOUNDARY_RESULT_ALLOWED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED"
BOUNDARY_RESULT_REQUIRES = "REQUIRES_RECORDED_CANDIDATE_BASIS"
BOUNDARY_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
BOUNDARY_RESULT_FAMILY = (
    BOUNDARY_RESULT_ALLOWED,
    BOUNDARY_RESULT_REQUIRES,
    BOUNDARY_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_BOUNDARY_SPEC_RELATIVE_PATH = Path("spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_V0_MIN_SPEC.md")
SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_operation_v0_min/"
    "receiver_side_answerable_basis_reception_operation_001__receiver_side_answerable_basis_reception_operation_v0_min_result_001.json"
)
GOVERNING_BOUNDARY_SPEC_PATH = REPO_ROOT / GOVERNING_BOUNDARY_SPEC_RELATIVE_PATH
SELECTED_CANDIDATE_RECEPTION_RESULT_PATH = REPO_ROOT / SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH
OUTPUT_ROOT = REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2"
OUTPUT_FILENAME = "receiver_side_answerable_basis_candidate_evaluation_boundary_001__receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result.json"


class ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error(Exception):
    """Raised when a v2 result cannot be written within the boundary."""


DEFAULT_FALSE_FIELDS = (
    "receiver_side_answerable_basis_candidate_evaluated",
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_present",
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "receiver_side_answerable_basis_refusable",
    "receiver_side_answerable_basis_could_have_been_withheld",
    "candidate_answers_prior_presence_knock",
    "candidate_receiver_authorship_established",
    "candidate_receiver_identity_established",
    "candidate_source_identity_established",
    "candidate_declared_provenance_verified",
    "candidate_separate_custody_established",
    "candidate_voluntary_supply_established",
    "candidate_physical_signal_validated",
    "candidate_human_presence_inferred",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "identity_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "mailbox_created",
    "listener_created",
    "queue_created",
    "endpoint_created",
    "shared_intake_lane_created",
    "reusable_route_created",
    "repeated_evaluation_permission_created",
    "second_candidate_received",
    "second_candidate_evaluated",
    "currentness_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "continuity_memory_written",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
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

CONVERSION_FALSE_FIELDS = (
    "candidate_reception_to_candidate_evaluation_completion",
    "candidate_reception_to_candidate_sufficiency",
    "candidate_reception_to_candidate_insufficiency",
    "candidate_reception_to_receiver_attestation",
    "candidate_reception_to_receiver_answerable_receipt",
    "candidate_reception_to_custody_distinctness",
    "candidate_reception_to_refusability",
    "candidate_reception_to_could_have_been_withheld",
    "candidate_reception_to_presence_support",
    "evaluation_boundary_permission_to_evaluation_completion",
    "evaluation_boundary_permission_to_evaluation_result",
    "packet_filename_to_constitutional_classification",
    "directory_name_to_constitutional_classification",
    "attestation_word_to_receiver_attestation",
    "receiver_label_to_receiver_identity",
    "candidate_kind_to_answerable_basis_sufficiency",
    "declared_attestation_form_to_established_attestation",
    "declared_source_provenance_reference_to_verified_provenance",
    "source_reference_to_source_identity",
    "source_reference_to_authority",
    "source_reference_to_standing",
    "receiver_working_directory_to_custody_distinction",
    "custody_declaration_to_established_custody_distinction",
    "freely_given_declaration_to_established_voluntary_supply",
    "refusal_declaration_to_established_refusability",
    "withholding_declaration_to_established_could_have_been_withheld",
    "receiver_authorship_declaration_to_established_receiver_authorship",
    "hash_correspondence_to_semantic_sufficiency",
    "hash_correspondence_to_receiver_identity",
    "timestamp_to_currentness",
    "timestamp_to_authority",
    "device_metadata_to_human_identity",
    "physical_signal_to_bodily_presence",
    "accelerometer_data_to_validated_knock",
    "capture_metadata_to_receiver_attestation",
    "capture_metadata_to_receiver_answerable_receipt",
    "prior_knock_reference_to_established_answerability",
    "candidate_evaluation_to_receiver_attestation",
    "candidate_evaluation_to_receiver_answerable_receipt",
    "candidate_evaluation_to_presence_support",
    "candidate_evaluation_to_presence_authorization",
    "candidate_evaluation_to_presence_establishment",
    "candidate_evaluation_to_presence_recording",
    "candidate_evaluation_to_identity",
    "candidate_evaluation_to_relation",
    "candidate_evaluation_to_coupling",
    "candidate_evaluation_to_field_machinery",
    "candidate_evaluation_to_runtime",
    "candidate_evaluation_to_api",
    "candidate_evaluation_to_public_interface",
    "candidate_evaluation_to_public_intake",
    "candidate_evaluation_to_mailbox",
    "candidate_evaluation_to_listener",
    "candidate_evaluation_to_queue",
    "candidate_evaluation_to_endpoint",
    "candidate_evaluation_to_shared_intake_lane",
    "candidate_evaluation_to_reusable_route",
    "candidate_evaluation_to_repeated_evaluation_permission",
    "candidate_evaluation_to_second_candidate",
    "candidate_evaluation_to_second_candidate_reception",
    "candidate_evaluation_to_second_candidate_evaluation",
    "candidate_evaluation_to_currentness",
    "candidate_evaluation_to_authority",
    "candidate_evaluation_to_standing",
    "candidate_evaluation_to_truth_creation",
    "candidate_evaluation_to_continuity_memory",
    "candidate_evaluation_to_output_authorization",
    "candidate_evaluation_to_action_authorization",
    "candidate_evaluation_to_derivative_reception",
    "candidate_evaluation_to_synchronization",
    "candidate_evaluation_to_follow_on_authorization",
    "candidate_evaluation_to_follow_on_work",
    "selected_candidate_to_retroactive_contaminated_lineage_validation",
)
REQUIRED_FALSE_NON_CLAIMS = tuple(dict.fromkeys(DEFAULT_FALSE_FIELDS + CONVERSION_FALSE_FIELDS))
ALLOWED_TRUE_RECORDED_FIELDS = (
    "receiver_side_answerable_basis_candidate_evaluation_boundary_recorded",
    "receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded",
    "receiver_side_answerable_basis_candidate_evaluation_consideration_allowed",
    "selected_candidate_reception_result_referenced",
    "selected_candidate_material_referenced",
)

BLOCK_CODES = frozenset({
    "REQUEST_NOT_MAPPING", "REQUEST_PATH_UNREADABLE", "REQUEST_JSON_INVALID", "UNSUPPORTED_INTENT",
    "BOUNDARY_SPEC_REFERENCE_MISSING", "BOUNDARY_SPEC_MARKER_MISSING",
    "SELECTED_CANDIDATE_RECEPTION_RESULT_REFERENCE_MISSING",
    "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE", "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_MAPPING",
    "REQUEST_VALUE_MISMATCH", "RECORDED_CANDIDATE_BASIS_MISSING_OR_INCONSISTENT",
    "SELECTED_CANDIDATE_IDENTITY_MISMATCH", "SELECTED_RECEPTION_OPERATION_MISMATCH",
    "PRIOR_RECEPTION_OUTCOME_MISMATCH", "PRIOR_RECEPTION_RESULT_MISMATCH",
    "PRIOR_RECEPTION_OPERATION_NOT_RECORDED", "PRIOR_RECEPTION_OPERATION_RESULT_NOT_RECORDED",
    "PRIOR_CANDIDATE_MATERIAL_NOT_SUPPLIED", "PRIOR_CANDIDATE_MATERIAL_NOT_RECEIVED",
    "PRIOR_CANDIDATE_MATERIAL_NOT_RECORDED", "PRIOR_CANDIDATE_MATERIAL_NOT_PRESERVED",
    "PRIOR_CANDIDATE_PROVENANCE_REFERENCE_NOT_SUPPLIED", "PRIOR_CANDIDATE_NOT_RECEIVED",
    "PRIOR_CANDIDATE_NOT_RECORDED", "PRIOR_CANDIDATE_ALREADY_EVALUATED",
    "PRIOR_RECEPTION_BOUNDARY_NOT_REFERENCED", "PRIOR_RECEPTION_RESULT_HAS_FAILED_CHECKS",
    "PRIOR_SECOND_CANDIDATE_POSTURE_TRUE", "PRIOR_REUSABLE_OR_REPEATED_RECEPTION_POSTURE_TRUE",
    "PRIOR_RECEIVER_ATTESTATION_POSTURE_TRUE", "PRIOR_RECEIVER_ANSWERABLE_RECEIPT_POSTURE_TRUE",
    "PRIOR_CUSTODY_REFUSABILITY_OR_WITHHOLDING_POSTURE_TRUE", "PRIOR_PRESENCE_POSTURE_TRUE",
    "PRIOR_FOLLOW_ON_POSTURE_TRUE", "NON_CLAIM_MISSING_OR_FLIPPED", "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED", "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED", "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "PROHIBITED_CUSTODY_REFUSABILITY_OR_WITHHOLDING_REQUESTED",
    "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "PROHIBITED_PHYSICAL_SIGNAL_OR_HUMAN_PRESENCE_VALIDATION_REQUESTED", "PROHIBITED_PRESENCE_REQUESTED",
    "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED", "PROHIBITED_COUPLING_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED", "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_ROUTE_REQUESTED",
    "PROHIBITED_SECOND_CANDIDATE_OR_EVALUATION_REQUESTED",
    "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED", "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
})

PROHIBITED_REQUEST_FLAGS = {
    "request_candidate_evaluation": "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
    "request_candidate_sufficiency": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_insufficiency": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_indeterminacy": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "request_custody_distinctness_decision": "PROHIBITED_CUSTODY_REFUSABILITY_OR_WITHHOLDING_REQUESTED",
    "request_refusability_decision": "PROHIBITED_CUSTODY_REFUSABILITY_OR_WITHHOLDING_REQUESTED",
    "request_could_have_been_withheld_decision": "PROHIBITED_CUSTODY_REFUSABILITY_OR_WITHHOLDING_REQUESTED",
    "request_receiver_authorship_establishment": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_receiver_identity_establishment": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_source_identity_establishment": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_declared_provenance_verification": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_separate_custody_establishment": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_voluntary_supply_establishment": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_prior_knock_answerability_establishment": "PROHIBITED_AUTHORSHIP_IDENTITY_OR_PROVENANCE_ESTABLISHMENT_REQUESTED",
    "request_physical_signal_validation": "PROHIBITED_PHYSICAL_SIGNAL_OR_HUMAN_PRESENCE_VALIDATION_REQUESTED",
    "request_bodily_presence_inference": "PROHIBITED_PHYSICAL_SIGNAL_OR_HUMAN_PRESENCE_VALIDATION_REQUESTED",
    "request_human_presence_inference": "PROHIBITED_PHYSICAL_SIGNAL_OR_HUMAN_PRESENCE_VALIDATION_REQUESTED",
    "request_presence_support": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_authorization": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_recording": "PROHIBITED_PRESENCE_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "request_coupling_assignment": "PROHIBITED_COUPLING_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_public_interface_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_public_intake_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_mailbox_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_listener_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_queue_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_endpoint_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_shared_intake_lane_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_reusable_route_creation": "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_ROUTE_REQUESTED",
    "request_repeated_evaluation_permission_creation": "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_ROUTE_REQUESTED",
    "request_second_candidate_reception": "PROHIBITED_SECOND_CANDIDATE_OR_EVALUATION_REQUESTED",
    "request_second_candidate_evaluation": "PROHIBITED_SECOND_CANDIDATE_OR_EVALUATION_REQUESTED",
    "request_currentness_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_truth_creation": "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED",
    "request_continuity_memory_write": "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_follow_on_work_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

EXPECTED_REQUEST_VALUES = {
    "boundary_id": BOUNDARY_ID,
    "boundary_type": BOUNDARY_TYPE,
    "boundary_version": BOUNDARY_VERSION,
    "boundary_scope": BOUNDARY_SCOPE,
    "prior_reception_operation_type": PRIOR_RECEPTION_OPERATION_TYPE,
    "prior_reception_operation_outcome_required": PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED,
    "prior_reception_operation_result_required": PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED,
    "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
    "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
    "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
    "selected_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
}

BOUNDARY_SPEC_MARKER_CLASSES = (
    ("boundary_identity", ("Receiver-Side Answerable Basis Candidate Evaluation Boundary V0 Minimum Specification", BOUNDARY_TYPE, BOUNDARY_ID, BOUNDARY_SCOPE)),
    ("selected_successful_reception_basis", (PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED, PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED, "candidate_material_supplied = true", "candidate_material_received = true", "candidate_material_recorded = true", "candidate_material_preserved = true", "candidate_source_provenance_reference_supplied = true", "receiver_side_answerable_basis_candidate_evaluated = false", "failed_check_count = 0")),
    ("candidate_identity", (CANDIDATE_ID, CANDIDATE_TYPE, CANDIDATE_SCOPE, SELECTED_RECEPTION_OPERATION_ID, str(SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH))),
    ("evaluation_consideration_only", ("evaluation consideration only", "Candidate evaluation boundary is not candidate evaluation operation.", "Evaluation consideration is not evaluation.", "does not perform candidate evaluation", "prescribe the evaluation result")),
    ("evaluation_dimension_separation", ("Candidate structural correspondence", "Declared provenance posture", "Receiver-authorship posture", "Separate-custody posture", "Refusability posture", "Could-have-been-withheld posture", "Prior-knock correspondence posture", "Capture-record posture", "No single declaration", "must not silently collapse into one omnibus boolean")),
    ("declaration_locks", ("Candidate declaration is not established fact.", "Declared provenance reference is not verified provenance.", "Receiver label is not receiver identity.", "Filesystem path is not custody distinction.", "Declared custody is not established custody distinction.", "Declared receiver authorship is not established receiver authorship.", "Declared refusability is not established refusability.", "Declared withholding posture is not established could-have-been-withheld posture.", "Hash correspondence is not semantic sufficiency", "Timestamp is not currentness or authority.", "Device metadata is not human identity.", "Recorded physical signal is not automatically bodily presence.", "The word `attestation` is not receiver attestation.", "Receiver attestation is distinct from receiver answerable receipt.")),
    ("boundary_outcomes", (OUTCOME_ALLOWED, OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS, OUTCOME_BLOCKED, BOUNDARY_RESULT_ALLOWED, BOUNDARY_RESULT_REQUIRES)),
    ("permitted_route", (ADMISSIBLE_FUTURE_ROUTE, "A future receiver-side answerable-basis candidate evaluation boundary resolver may evaluate the selected successful candidate-reception artifact", "future boundary artifact may record", "one separately bounded candidate evaluation operation", "No receiver attestation, receiver answerable receipt, presence re-evaluation, second candidate, reusable evaluation route, or later operation is authorized")),
    ("stale_list_posture", ("static `what_remains_open` list", "do not override the same artifact's decisive structured reception result", "does not edit, repair, normalize, or replace that artifact", "must not reproduce actual candidate material or actual candidate reception as still open")),
    ("contaminated_lineage", ("DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage", "prior unsupported claims remain unsupported", "does not repair, edit, delete, overwrite, replace, validate, redeem, clean, or reinterpret that file", "must not be used to retroactively validate unrelated contaminated existence claims")),
)
TARGET_SPEC_MARKER_CLASSES = BOUNDARY_SPEC_MARKER_CLASSES

EVALUATION_DIMENSIONS = (
    ("candidate_structural_correspondence", "Candidate structural correspondence", "Structural correspondence is not candidate sufficiency."),
    ("declared_provenance_posture", "Declared provenance posture", "Declared provenance posture is not verified provenance."),
    ("receiver_authorship_posture", "Receiver-authorship posture", "Receiver-authorship posture is not established receiver authorship."),
    ("separate_custody_posture", "Separate-custody posture", "Separate-custody posture is not established custody distinction."),
    ("refusability_posture", "Refusability posture", "Refusability posture is not established refusability."),
    ("could_have_been_withheld_posture", "Could-have-been-withheld posture", "Withholding posture is not an established withholding result."),
    ("prior_knock_correspondence_posture", "Prior-knock correspondence posture", "Prior-knock correspondence is not established answerability."),
    ("capture_record_posture", "Capture-record posture", "Capture-record posture is not validation of signal, presence, identity, or truth."),
)

WHAT_REMAINS_OPEN = (
    "candidate evaluation boundary test", "candidate evaluation boundary live artifact", "actual candidate evaluation boundary execution",
    "candidate evaluation operation specification, if separately selected", "candidate evaluation operation resolver, if separately bounded",
    "candidate evaluation operation test, if separately bounded", "candidate evaluation operation live artifact, if separately bounded",
    "candidate structural-correspondence evaluation", "declared-provenance-posture evaluation", "receiver-authorship-posture evaluation",
    "separate-custody-posture evaluation", "refusability-posture evaluation", "could-have-been-withheld-posture evaluation",
    "prior-knock-correspondence evaluation", "capture-record-posture evaluation", "answerable-basis sufficiency result",
    "receiver attestation", "receiver answerable receipt", "custody distinctness", "refusability", "could-have-been-withheld posture",
    "presence re-evaluation, if separately bounded", "presence support", "presence authorization", "presence establishment", "presence recording",
    "identity boundary", "relation boundary", "coupling boundary", "FIELD machinery", "runtime", "API", "public interface", "public intake",
    "currentness", "authority", "standing", "output authorization", "action authorization", "derivative reception", "synchronization",
    "externalization boundary", "follow-on work",
)


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _as_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _check(name: str, passed: bool, block_code: str | None = None) -> dict[str, Any]:
    check: dict[str, Any] = {"name": name, "passed": passed}
    if block_code is not None:
        check["block_code"] = block_code
    return check


def _read_text(path_value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_path(path_value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError):
        return None, "unreadable"


def _read_json(path_value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(path_value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, "not_parseable"


def _marker_status(specification: str) -> dict[str, bool]:
    return {name: all(marker in specification for marker in markers) for name, markers in BOUNDARY_SPEC_MARKER_CLASSES}


def _dimensions() -> dict[str, dict[str, Any]]:
    return {
        identifier: {
            "dimension_id": identifier,
            "dimension_label": label,
            "evaluation_status": BOUNDARY_RESULT_NOT_EVALUATED,
            "established": False,
            "non_conversion_statement": statement,
        }
        for identifier, label, statement in EVALUATION_DIMENSIONS
    }


def _boundary_state(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    requires = outcome == OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS
    recorded = allowed or requires
    state: dict[str, Any] = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_id": BOUNDARY_ID,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_type": BOUNDARY_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_version": BOUNDARY_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_scope": BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_recorded": recorded,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded": recorded,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_result": (
            BOUNDARY_RESULT_ALLOWED if allowed else BOUNDARY_RESULT_REQUIRES if requires else BOUNDARY_RESULT_NOT_EVALUATED
        ),
        "receiver_side_answerable_basis_candidate_evaluation_consideration_allowed": allowed,
        "selected_candidate_reception_result_referenced": allowed,
        "selected_candidate_material_referenced": allowed,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }
    state.update(_canonical_non_claims())
    return state


def _selected_basis(
    path: Path | str | None,
    artifact: Mapping[str, Any] | None,
    parseable: bool,
    stale_exception: bool,
) -> dict[str, Any]:
    operation = artifact.get("receiver_side_answerable_basis_reception_operation", {}) if artifact else {}
    material = artifact.get("receiver_side_answerable_basis_reception_operation_material", {}) if artifact else {}
    record = material.get("supplied_candidate_material_record", {}) if isinstance(material, Mapping) else {}
    operation = operation if isinstance(operation, Mapping) else {}
    record = record if isinstance(record, Mapping) else {}
    return {
        "selected_candidate_reception_artifact_path": str(path) if path is not None else None,
        "selected_artifact_parseable": parseable,
        "selected_operation_id": operation.get("receiver_side_answerable_basis_reception_operation_id"),
        "selected_operation_type": operation.get("receiver_side_answerable_basis_reception_operation_type"),
        "selected_operation_result": operation.get("receiver_side_answerable_basis_reception_operation_result"),
        "candidate_id": operation.get("receiver_side_answerable_basis_candidate_id"),
        "candidate_type": operation.get("receiver_side_answerable_basis_candidate_type"),
        "candidate_scope": operation.get("receiver_side_answerable_basis_candidate_scope"),
        "candidate_material_present": "candidate_material" in record and record.get("candidate_material") is not None,
        "candidate_material_supplied": operation.get("candidate_material_supplied"),
        "candidate_material_received": operation.get("candidate_material_received"),
        "candidate_material_recorded": operation.get("candidate_material_recorded"),
        "candidate_material_preserved": operation.get("candidate_material_preserved"),
        "candidate_source_provenance_reference_supplied": operation.get("candidate_source_provenance_reference_supplied"),
        "candidate_received": operation.get("receiver_side_answerable_basis_candidate_received"),
        "candidate_recorded": operation.get("receiver_side_answerable_basis_candidate_recorded"),
        "candidate_evaluated": operation.get("receiver_side_answerable_basis_candidate_evaluated"),
        "prior_reception_boundary_referenced": operation.get("prior_receiver_side_answerable_basis_reception_boundary_referenced"),
        "prior_second_candidate_received": operation.get("second_candidate_received"),
        "prior_repeated_reception_permission_created": operation.get("repeated_reception_permission_created"),
        "prior_reusable_route_created": operation.get("reusable_route_created"),
        "failed_check_count": artifact.get("failed_check_count") if artifact else None,
        "stale_open_list_exception_recognized": stale_exception,
        "complete_candidate_material_omitted_from_boundary_result": True,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("receiver_side_answerable_basis_candidate_evaluation_boundary", {})
    basis = result.get("selected_receiver_side_answerable_basis_candidate_basis", {})
    upstream = result.get("upstream_basis", {})
    dimensions = result.get("receiver_side_answerable_basis_candidate_evaluation_dimensions", {})
    boundary = boundary if isinstance(boundary, Mapping) else {}
    basis = basis if isinstance(basis, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    statuses: dict[str, Any] = {}
    if isinstance(dimensions, Mapping):
        statuses = {
            key: value.get("evaluation_status")
            for key, value in dimensions.items()
            if isinstance(value, Mapping)
        }
    return {
        "outcome": result.get("outcome"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "result_version": result.get("result_version"),
        "resolver_module": result.get("resolver_module"),
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "boundary_result": boundary.get("receiver_side_answerable_basis_candidate_evaluation_boundary_result"),
        "evaluation_consideration_allowed": boundary.get("receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"),
        "governing_boundary_specification_path": upstream.get("governing_boundary_specification_path"),
        "selected_candidate_reception_artifact_path": basis.get("selected_candidate_reception_artifact_path"),
        "selected_operation_id": basis.get("selected_operation_id"),
        "selected_operation_type": basis.get("selected_operation_type"),
        "selected_operation_outcome": upstream.get("selected_operation_outcome"),
        "selected_operation_result": basis.get("selected_operation_result"),
        "candidate_id": basis.get("candidate_id"),
        "candidate_type": basis.get("candidate_type"),
        "candidate_scope": basis.get("candidate_scope"),
        "candidate_material_supplied": basis.get("candidate_material_supplied"),
        "candidate_material_received": basis.get("candidate_material_received"),
        "candidate_material_recorded": basis.get("candidate_material_recorded"),
        "candidate_material_preserved": basis.get("candidate_material_preserved"),
        "candidate_source_provenance_reference_supplied": basis.get("candidate_source_provenance_reference_supplied"),
        "candidate_received": basis.get("candidate_received"),
        "candidate_recorded": basis.get("candidate_recorded"),
        "candidate_evaluated": basis.get("candidate_evaluated"),
        "prior_reception_boundary_referenced": basis.get("prior_reception_boundary_referenced"),
        "failed_upstream_check_count": basis.get("failed_check_count"),
        "prior_second_candidate_received": basis.get("prior_second_candidate_received"),
        "prior_repeated_reception_permission_created": basis.get("prior_repeated_reception_permission_created"),
        "prior_reusable_route_created": basis.get("prior_reusable_route_created"),
        "second_candidate_received": boundary.get("second_candidate_received"),
        "repeated_evaluation_permission_created": boundary.get("repeated_evaluation_permission_created"),
        "reusable_route_created": boundary.get("reusable_route_created"),
        "receiver_attestation_created": boundary.get("receiver_attestation_created"),
        "receiver_attestation_supported": boundary.get("receiver_attestation_supported"),
        "receiver_answerable_receipt_present": boundary.get("receiver_answerable_receipt_present"),
        "receiver_answerable_basis_custody_distinct": boundary.get("receiver_answerable_basis_custody_distinct"),
        "receiver_answerable_basis_refusable": boundary.get("receiver_answerable_basis_refusable"),
        "receiver_answerable_basis_could_have_been_withheld": boundary.get("receiver_answerable_basis_could_have_been_withheld"),
        "presence_postures": {key: boundary.get(key) for key in ("presence_supported", "presence_authorized", "presence_established", "presence_recorded")},
        "stale_open_list_exception_recognized": basis.get("stale_open_list_exception_recognized"),
        "selected_candidate_basis_referenced": boundary.get("selected_candidate_reception_result_referenced"),
        "selected_candidate_material_referenced": boundary.get("selected_candidate_material_referenced"),
        "evaluation_dimensions": statuses,
        "missing_or_inconsistent_recorded_candidate_basis": copy.deepcopy(result.get("missing_or_inconsistent_recorded_candidate_basis", [])),
        "marker_classes": copy.deepcopy(upstream.get("governing_boundary_specification_marker_classes", {})),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any] | None = None,
    missing: list[str] | None = None,
    code: str | None = None,
    reason: str | None = None,
    artifact: Mapping[str, Any] | None = None,
    artifact_path: Path | str | None = None,
    parseable: bool = False,
    stale_exception: bool = False,
) -> dict[str, Any]:
    boundary = _boundary_state(outcome)
    basis = _selected_basis(artifact_path, artifact, parseable, stale_exception)
    material_preserved = all(basis.get(key) is True for key in ("candidate_material_supplied", "candidate_material_received", "candidate_material_recorded", "candidate_material_preserved"))
    candidate_recorded = basis.get("candidate_received") is True and basis.get("candidate_recorded") is True
    declared_fields = (
        "intent", "boundary_id", "boundary_type", "boundary_version", "boundary_scope",
        "governing_boundary_specification_path", "selected_successful_candidate_reception_artifact_path",
        "prior_reception_operation_type", "prior_reception_operation_outcome_required", "prior_reception_operation_result_required",
        "receiver_side_answerable_basis_candidate_id", "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope", "selected_reception_operation_id", "admissible_future_route",
    )
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_evaluation_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
        },
        "declared_receiver_side_answerable_basis_candidate_evaluation_boundary_basis": {
            key: copy.deepcopy(request[key]) for key in declared_fields if key in request
        },
        "upstream_basis": copy.deepcopy(dict(upstream_basis or {})),
        "receiver_side_answerable_basis_candidate_evaluation_boundary": boundary,
        "selected_receiver_side_answerable_basis_candidate_basis": basis,
        "receiver_side_answerable_basis_candidate_evaluation_dimensions": _dimensions(),
        "receiver_side_answerable_basis_candidate_evaluation_boundary_checks": copy.deepcopy(checks),
        "receiver_side_answerable_basis_candidate_evaluation_boundary_statement": {
            "selected_candidate_material_already_supplied_received_recorded_and_preserved": material_preserved,
            "selected_candidate_already_received_and_recorded": candidate_recorded,
            "candidate_evaluation_remains_false": True,
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
            "result_level_non_claims_canonical_false": True,
        },
        "receiver_side_answerable_basis_candidate_evaluation_boundary_non_meaning": {
            "candidate_reception_is_not_candidate_evaluation": True,
            "candidate_preservation_is_not_candidate_validation": True,
            "candidate_content_is_not_established_meaning": True,
            "declaration_is_not_established_fact": True,
        },
        "boundary_result_detail": {
            "result": boundary["receiver_side_answerable_basis_candidate_evaluation_boundary_result"],
            "consideration_allowed": boundary["receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"],
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": list(CONVERSION_FALSE_FIELDS),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "missing_or_inconsistent_recorded_candidate_basis": list(missing or []),
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
    result["receiver_side_answerable_basis_candidate_evaluation_boundary_summary"] = _summary_from_result(result)
    return result


def _declared_non_claims_are_valid(value: Any) -> bool:
    return isinstance(value, Mapping) and all(value.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _validate_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    if request.get("intent") not in SUPPORTED_INTENTS:
        return "UNSUPPORTED_INTENT", "intent is not supported"
    for key, expected in EXPECTED_REQUEST_VALUES.items():
        passed = request.get(key) == expected
        checks.append(_check(key, passed, None if passed else "REQUEST_VALUE_MISMATCH"))
        if not passed:
            return "REQUEST_VALUE_MISMATCH", key + " does not match the bounded request"
    if not _declared_non_claims_are_valid(request.get("declared_non_claims")):
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared_non_claims must contain every required key as false"
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        passed = request.get(field, False) is False
        checks.append(_check(field, passed, None if passed else code))
        if not passed:
            return code, field + " requests a prohibited conversion"
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        if request.get(field, False) is not False:
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be pre-claimed"
    if request.get("receiver_side_answerable_basis_candidate_evaluation_boundary_result") not in (None, BOUNDARY_RESULT_NOT_EVALUATED):
        return "RESULT_POSTURE_PRECLAIMED", "boundary result may not be pre-claimed"
    for field in (
        "candidate_material", "candidate_source_provenance_reference", "second_candidate_material",
        "second_candidate_reception_artifact_path", "candidate_collection", "alternate_candidate",
        "alternate_reception_operation", "alternate_candidate_reception_artifact_path",
    ):
        if field in request:
            return "PROHIBITED_SECOND_CANDIDATE_OR_EVALUATION_REQUESTED", field + " is not an admissible boundary input"
    return None, None


def _artifact_requirements() -> tuple[tuple[str, Any, str], ...]:
    return (
        ("receiver_side_answerable_basis_reception_operation_type", PRIOR_RECEPTION_OPERATION_TYPE, "operation_type"),
        ("receiver_side_answerable_basis_reception_operation_id", SELECTED_RECEPTION_OPERATION_ID, "operation_id"),
        ("receiver_side_answerable_basis_reception_operation_result", PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED, "operation_result"),
        ("receiver_side_answerable_basis_reception_operation_recorded", True, "operation_recorded"),
        ("receiver_side_answerable_basis_reception_operation_result_recorded", True, "operation_result_recorded"),
        ("receiver_side_answerable_basis_candidate_id", CANDIDATE_ID, "candidate_id"),
        ("receiver_side_answerable_basis_candidate_type", CANDIDATE_TYPE, "candidate_type"),
        ("receiver_side_answerable_basis_candidate_scope", CANDIDATE_SCOPE, "candidate_scope"),
        ("candidate_material_supplied", True, "candidate_material_supplied"),
        ("candidate_material_received", True, "candidate_material_received"),
        ("candidate_material_recorded", True, "candidate_material_recorded"),
        ("candidate_material_preserved", True, "candidate_material_preserved"),
        ("candidate_source_provenance_reference_supplied", True, "candidate_source_provenance_reference_supplied"),
        ("receiver_side_answerable_basis_candidate_received", True, "candidate_received"),
        ("receiver_side_answerable_basis_candidate_recorded", True, "candidate_recorded"),
        ("receiver_side_answerable_basis_candidate_evaluated", False, "candidate_evaluated"),
        ("prior_receiver_side_answerable_basis_reception_boundary_referenced", True, "prior_reception_boundary_referenced"),
        ("second_candidate_received", False, "second_candidate_received"),
        ("repeated_reception_permission_created", False, "repeated_reception_permission_created"),
        ("reusable_route_created", False, "reusable_route_created"),
        ("receiver_attestation_created", False, "receiver_attestation_created"),
        ("receiver_attestation_supported", False, "receiver_attestation_supported"),
        ("receiver_answerable_receipt_present", False, "receiver_answerable_receipt_present"),
        ("receiver_answerable_basis_custody_distinct", False, "receiver_answerable_basis_custody_distinct"),
        ("receiver_answerable_basis_refusable", False, "receiver_answerable_basis_refusable"),
        ("receiver_answerable_basis_could_have_been_withheld", False, "receiver_answerable_basis_could_have_been_withheld"),
        ("presence_supported", False, "presence_supported"),
        ("presence_authorized", False, "presence_authorized"),
        ("presence_established", False, "presence_established"),
        ("presence_recorded", False, "presence_recorded"),
        ("follow_on_authorized", False, "follow_on_authorized"),
        ("follow_on_work_authorized", False, "follow_on_work_authorized"),
    )


def _evaluate_sources(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[dict[str, Any], list[str], str | None, str | None, Mapping[str, Any] | None, Path | None, bool, bool]:
    upstream: dict[str, Any] = {}
    specification_path = request.get("governing_boundary_specification_path")
    if not isinstance(specification_path, (str, Path)):
        return upstream, [], "BOUNDARY_SPEC_REFERENCE_MISSING", "governing boundary specification path is missing", None, None, False, False
    specification, specification_error = _read_text(specification_path)
    upstream["governing_boundary_specification_path"] = str(_as_path(specification_path))
    if specification_error is not None or specification is None:
        checks.append(_check("governing_boundary_specification_reference", False, "BOUNDARY_SPEC_REFERENCE_MISSING"))
        return upstream, [], "BOUNDARY_SPEC_REFERENCE_MISSING", "governing boundary specification is unavailable", None, None, False, False
    markers = _marker_status(specification)
    upstream["governing_boundary_specification_marker_classes"] = markers
    for name, passed in markers.items():
        checks.append(_check("governing_boundary_specification_" + name, passed, None if passed else "BOUNDARY_SPEC_MARKER_MISSING"))
    if not all(markers.values()):
        return upstream, [], "BOUNDARY_SPEC_MARKER_MISSING", "governing boundary specification lacks required posture markers", None, None, False, False

    artifact_value = request.get("selected_successful_candidate_reception_artifact_path")
    if not isinstance(artifact_value, (str, Path)):
        return upstream, ["selected_candidate_reception_artifact"], None, None, None, None, False, False
    artifact_path = _as_path(artifact_value)
    upstream["selected_candidate_reception_artifact_path"] = str(artifact_path)
    artifact, artifact_error = _read_json(artifact_path)
    if artifact_error in ("not_a_file", "unreadable"):
        return upstream, ["selected_candidate_reception_artifact"], None, None, None, artifact_path, False, False
    if artifact_error == "not_parseable":
        checks.append(_check("selected_candidate_reception_artifact_json", False, "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE"))
        return upstream, [], "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE", "selected candidate reception artifact is not parseable JSON", None, artifact_path, False, False
    if not isinstance(artifact, Mapping):
        checks.append(_check("selected_candidate_reception_artifact_mapping", False, "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_MAPPING"))
        return upstream, [], "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_MAPPING", "selected candidate reception artifact is not a mapping", None, artifact_path, True, False

    operation = artifact.get("receiver_side_answerable_basis_reception_operation")
    material = artifact.get("receiver_side_answerable_basis_reception_operation_material")
    record = material.get("supplied_candidate_material_record") if isinstance(material, Mapping) else None
    if not isinstance(operation, Mapping) or not isinstance(record, Mapping):
        return upstream, ["selected_candidate_reception_operation"], None, None, artifact, artifact_path, True, False

    missing: list[str] = []
    if artifact.get("outcome") != PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED:
        missing.append("outcome")
    else:
        checks.append(_check("selected_operation_outcome", True))
    for field, expected, name in _artifact_requirements():
        if operation.get(field) != expected:
            missing.append(name)
        else:
            checks.append(_check("selected_" + name, True))
    if artifact.get("failed_check_count") != PRIOR_FAILED_CHECK_COUNT_REQUIRED:
        missing.append("failed_check_count")
    else:
        checks.append(_check("selected_failed_check_count", True))
    for field in ("candidate_material_supplied", "candidate_material_received", "candidate_material_recorded", "candidate_material_preserved"):
        if record.get(field) is not True:
            missing.append("supplied_candidate_material_record." + field)
    if "candidate_material" not in record or record.get("candidate_material") is None:
        missing.append("candidate_material")
    non_claims = artifact.get("non_claims")
    if not isinstance(non_claims, Mapping) or any(value is not False for value in non_claims.values()):
        missing.append("upstream_non_claims")
    stale_entries = artifact.get("what_remains_open")
    stale_exception = isinstance(stale_entries, list) and {
        "actual receiver-side answerable-basis candidate material", "actual candidate reception"
    }.issubset(set(stale_entries))
    upstream.update({
        "selected_operation_outcome": artifact.get("outcome"),
        "selected_artifact_parseable": True,
        "selected_artifact_stale_open_list_exception_recognized": stale_exception,
    })
    return upstream, list(dict.fromkeys(missing)), None, None, artifact, artifact_path, True, stale_exception


def build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request(
    *,
    intent: str = INTENT_RECORD,
    boundary_id: str = BOUNDARY_ID,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_version: str = BOUNDARY_VERSION,
    boundary_scope: str = BOUNDARY_SCOPE,
    governing_boundary_specification_path: Path | str | None = None,
    selected_successful_candidate_reception_artifact_path: Path | str | None = None,
    prior_reception_operation_type: str = PRIOR_RECEPTION_OPERATION_TYPE,
    prior_reception_operation_outcome_required: str = PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED,
    prior_reception_operation_result_required: str = PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED,
    receiver_side_answerable_basis_candidate_id: str = CANDIDATE_ID,
    receiver_side_answerable_basis_candidate_type: str = CANDIDATE_TYPE,
    receiver_side_answerable_basis_candidate_scope: str = CANDIDATE_SCOPE,
    selected_reception_operation_id: str = SELECTED_RECEPTION_OPERATION_ID,
    admissible_future_route: str = ADMISSIBLE_FUTURE_ROUTE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one bounded v2 request without accepting candidate material."""
    request: dict[str, Any] = {
        "intent": intent,
        "boundary_id": boundary_id,
        "boundary_type": boundary_type,
        "boundary_version": boundary_version,
        "boundary_scope": boundary_scope,
        "governing_boundary_specification_path": str(GOVERNING_BOUNDARY_SPEC_PATH if governing_boundary_specification_path is None else governing_boundary_specification_path),
        "selected_successful_candidate_reception_artifact_path": str(SELECTED_CANDIDATE_RECEPTION_RESULT_PATH if selected_successful_candidate_reception_artifact_path is None else selected_successful_candidate_reception_artifact_path),
        "prior_reception_operation_type": prior_reception_operation_type,
        "prior_reception_operation_outcome_required": prior_reception_operation_outcome_required,
        "prior_reception_operation_result_required": prior_reception_operation_result_required,
        "receiver_side_answerable_basis_candidate_id": receiver_side_answerable_basis_candidate_id,
        "receiver_side_answerable_basis_candidate_type": receiver_side_answerable_basis_candidate_type,
        "receiver_side_answerable_basis_candidate_scope": receiver_side_answerable_basis_candidate_scope,
        "selected_reception_operation_id": selected_reception_operation_id,
        "admissible_future_route": admissible_future_route,
        "declared_non_claims": _canonical_non_claims() if declared_non_claims is None else copy.deepcopy(declared_non_claims),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request(**kwargs: Any) -> dict[str, Any]:
    """Compatibility spelling for the bounded v2 declared-request builder."""
    return build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request(**kwargs)


def resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(
    declared_receiver_side_answerable_basis_candidate_evaluation_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one v2 boundary consideration result without candidate evaluation."""
    if declared_receiver_side_answerable_basis_candidate_evaluation_boundary is None:
        request: Mapping[str, Any] = build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request()
    elif not isinstance(declared_receiver_side_answerable_basis_candidate_evaluation_boundary, Mapping):
        return _result({}, OUTCOME_BLOCKED, [_check("request_mapping", False, "REQUEST_NOT_MAPPING")], code="REQUEST_NOT_MAPPING", reason="declared boundary request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_receiver_side_answerable_basis_candidate_evaluation_boundary))

    checks: list[dict[str, Any]] = [_check("request_mapping", True)]
    code, reason = _validate_request(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, checks, code=code, reason=reason)
    if request.get("intent") == INTENT_BLOCK:
        checks.append(_check("explicit_block", False, "EXPLICIT_BLOCK_REQUESTED"))
        return _result(request, OUTCOME_BLOCKED, checks, code="EXPLICIT_BLOCK_REQUESTED", reason="explicit block requested")
    if request.get("intent") == INTENT_DO_NOT_RECORD:
        return _result(request, OUTCOME_NOT_RECORDED, checks)

    upstream, missing, code, reason, artifact, artifact_path, parseable, stale_exception = _evaluate_sources(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, checks, upstream, [], code, reason, artifact, artifact_path, parseable, stale_exception)
    if missing:
        return _result(request, OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS, checks, upstream, missing, None, None, artifact, artifact_path, parseable, stale_exception)
    return _result(request, OUTCOME_ALLOWED, checks, upstream, [], None, None, artifact, artifact_path, parseable, stale_exception)


def resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_from_path(
    declared_receiver_side_answerable_basis_candidate_evaluation_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read one declared v2 request JSON path without discovery."""
    path = _as_path(declared_receiver_side_answerable_basis_candidate_evaluation_boundary_path)
    try:
        if not path.is_file():
            raise OSError("request path is not a file")
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        return _result({}, OUTCOME_BLOCKED, [_check("declared_request_path", False, "REQUEST_PATH_UNREADABLE")], code="REQUEST_PATH_UNREADABLE", reason="declared request path is unavailable")
    except (UnicodeDecodeError, json.JSONDecodeError):
        return _result({}, OUTCOME_BLOCKED, [_check("declared_request_json", False, "REQUEST_JSON_INVALID")], code="REQUEST_JSON_INVALID", reason="declared request JSON is invalid")
    return resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(payload)


def build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return the compact v2 summary without candidate material."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: result is not a mapping")
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def _contains_candidate_material(value: Any) -> bool:
    if isinstance(value, Mapping):
        return "candidate_material" in value or any(_contains_candidate_material(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_candidate_material(item) for item in value)
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    forbidden = {"spec", "tests", "reference", "presence", "relation", "identity", "field", "runtime", "api", "public-intake", "descendant", "receiver-capture"}
    return any(part.lower() in forbidden or "receiver_attestation_capture" in part.lower() for part in path.parts)


def write_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None,
) -> Path:
    """Write only a structurally valid, candidate-material-free v2 result."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: result is not a mapping")
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: resolver identity is invalid")
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: outcome is invalid")
    if not _declared_non_claims_are_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: non-claims are invalid")
    if _contains_candidate_material(result):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: candidate material is not writable here")
    requested = OUTPUT_ROOT / OUTPUT_FILENAME if output_path is None else Path(output_path)
    if _output_path_is_forbidden(requested):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: output root is forbidden")
    target = _next_available_output_path(requested)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error("WRITE_REFUSED: unable to write result") from exc
    return target
