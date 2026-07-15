"""Bounded relevance reception resolver V0 minimum.

This module records one bounded relevance reception posture only. It is
downstream of post-runtime-loop bounded relevance reception selection and the
runtime-layer closure review. Runtime loop remains one bounded runtime-loop
posture, the bounded runtime-loop envelope remains closed basis only, and
carrier-aware / distributed anatomy remains upstream basis only.

The resolver does not create relevance receipt, source transfer, source receipt,
reception authorization, source, authority, currentness, truth, action,
synchronization, inhabitance, runtime permission, public API,
participant-facing interface, distributed network behavior, deployment, public
release, operation permission, broader reusable permission, derivative
reception, vessel relation, adoption, receiving-context governance,
publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class BoundedRelevanceReceptionV0MinError(Exception):
    """Raised when bounded relevance reception resolver IO cannot proceed."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_bounded_relevance_reception_v0_min"

OUTCOME_RECORDED = "BOUNDED_RELEVANCE_RECEPTION_RECORDED"
OUTCOME_NOT_RECORDED = "BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = "BOUNDED_RELEVANCE_RECEPTION_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "BOUNDED_RELEVANCE_RECEPTION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_BOUNDED_RELEVANCE_RECEPTION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_BOUNDED_RELEVANCE_RECEPTION"
INTENT_BLOCK = "BLOCK_BOUNDED_RELEVANCE_RECEPTION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min")

CORE_QUESTION = (
    "Can the selected post-runtime-loop bounded relevance reception basis be used "
    "to record one bounded relevance reception posture, where one bounded relevance "
    "signal may be received into existing carrier-aware / distributed anatomy, "
    "without creating relevance receipt, source transfer, source receipt, reception "
    "authorization, source, authority, currentness, truth, action, synchronization, "
    "inhabitance, runtime permission, public API, participant-facing interface, "
    "distributed network behavior, deployment, public release, operation permission, "
    "broader reusable permission, derivative reception, vessel relation, adoption, "
    "receiving-context governance, publication flow, or follow-on work?"
)

SUPPORTED_SCOPE_VALUES = (
    "BOUNDED_RELEVANCE_RECEPTION_SPEC_ONLY",
    "ONE_BOUNDED_RELEVANCE_RECEPTION_POSTURE_RECORDED",
    "BOUNDED_RELEVANCE_SIGNAL_DECLARED",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_DECLARED",
    "RUNTIME_LAYER_CLOSURE_BASIS_PRESERVED",
    "RUNTIME_LOOP_BASIS_PRESERVED",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_PRESERVED",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_PRESERVED",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SOURCE_TRANSFER",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SOURCE_RECEIPT",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_RECEPTION_AUTHORIZATION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SOURCE",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_AUTHORITY",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_CURRENTNESS",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_TRUTH",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_ACTION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SYNCHRONIZATION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_INHABITANCE",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_RUNTIME_PERMISSION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_PUBLIC_API",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "NO_SOURCE_TRANSFER",
    "NO_SOURCE_RECEIPT",
    "NO_RECEPTION_AUTHORIZATION",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_TRUTH_CREATED",
    "NO_ACTION_CREATED",
    "NO_SYNCHRONIZATION_CREATED",
    "NO_INHABITANCE_CREATED",
    "NO_RUNTIME_PERMISSION_CREATED",
    "NO_PUBLIC_API_CREATED",
    "NO_PARTICIPANT_FACING_INTERFACE_CREATED",
    "NO_DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "NO_DEPLOYMENT_CREATED",
    "NO_PUBLIC_RELEASE_CREATED",
    "NO_OPERATION_PERMISSION_CREATED",
    "NO_BROADER_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ADOPTION",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "NO_PUBLICATION_FLOW",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_TRUTH_INFERENCE",
    "NO_ACTION_INFERENCE",
    "NO_SYNCHRONIZATION_INFERENCE",
    "NO_INHABITANCE_INFERENCE",
    "NO_RUNTIME_PERMISSION_INFERENCE",
    "NO_PUBLIC_API_INFERENCE",
    "NO_PARTICIPANT_INTERFACE_INFERENCE",
    "NO_DISTRIBUTED_NETWORK_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)
SUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "relevance_receipt_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "action_created",
    "synchronization_created",
    "inhabitance_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "bounded_relevance_reception_treated_as_source_transfer",
    "bounded_relevance_reception_treated_as_source_receipt",
    "bounded_relevance_reception_treated_as_reception_authorization",
    "bounded_relevance_reception_treated_as_source",
    "bounded_relevance_reception_treated_as_authority",
    "bounded_relevance_reception_treated_as_currentness",
    "bounded_relevance_reception_treated_as_truth",
    "bounded_relevance_reception_treated_as_action",
    "bounded_relevance_reception_treated_as_synchronization",
    "bounded_relevance_reception_treated_as_inhabitance",
    "bounded_relevance_reception_treated_as_runtime_permission",
    "bounded_relevance_reception_treated_as_public_api",
    "bounded_relevance_reception_treated_as_participant_facing_interface",
    "bounded_relevance_reception_treated_as_distributed_network_behavior",
    "bounded_relevance_signal_treated_as_source",
    "bounded_relevance_signal_treated_as_authority",
    "bounded_relevance_signal_treated_as_currentness",
    "bounded_relevance_signal_treated_as_truth",
    "bounded_relevance_signal_treated_as_action",
    "bounded_relevance_signal_treated_as_synchronization",
    "bounded_relevance_signal_treated_as_inhabitance",
    "bounded_relevance_signal_treated_as_runtime_permission",
    "bounded_relevance_signal_treated_as_public_api",
    "bounded_relevance_signal_treated_as_participant_facing_interface",
    "bounded_relevance_signal_treated_as_distributed_network_behavior",
    "carrier_context_treated_as_authority",
    "carrier_context_treated_as_currentness",
    "carrier_context_treated_as_action",
    "carrier_context_treated_as_synchronization",
    "carrier_context_treated_as_runtime_permission",
    "carrier_context_treated_as_public_api",
    "carrier_context_treated_as_participant_facing_interface",
    "carrier_context_treated_as_distributed_network_behavior",
    "runtime_loop_treated_as_public_api",
    "runtime_loop_treated_as_participant_facing_interface",
    "runtime_loop_treated_as_distributed_network_behavior",
    "bounded_runtime_loop_envelope_treated_as_bounded_relevance_reception_authority",
    "artifact_existence_treated_as_bounded_relevance_reception_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_bounded_relevance_reception_authority",
    "repo_local_availability_treated_as_bounded_relevance_reception_authority",
    "hidden_repo_state_used_as_bounded_relevance_reception_content",
    "hidden_repo_state_used_as_bounded_relevance_reception_authority",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "runtime_daemon_boundary_v1_failure_hidden",
    "runtime_daemon_boundary_v1_failure_repaired",
    "runtime_daemon_boundary_v1_failure_claimed_passed",
    "runtime_hosting_boundary_v1_failure_hidden",
    "runtime_hosting_boundary_v1_failure_repaired",
    "runtime_hosting_boundary_v1_failure_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "bounded_relevance_reception_recorded",
    "bounded_relevance_reception_posture_recorded",
    "bounded_relevance_signal_declared",
    "bounded_relevance_reception_envelope_declared",
    "runtime_layer_closure_basis_preserved",
    "runtime_loop_basis_preserved",
    "bounded_runtime_loop_envelope_preserved",
    "carrier_aware_distributed_anatomy_basis_preserved",
    "bounded_relevance_reception_not_source_transfer",
    "bounded_relevance_reception_not_source_receipt",
    "bounded_relevance_reception_not_reception_authorization",
    "bounded_relevance_reception_not_source",
    "bounded_relevance_reception_not_authority",
    "bounded_relevance_reception_not_currentness",
    "bounded_relevance_reception_not_truth",
    "bounded_relevance_reception_not_action",
    "bounded_relevance_reception_not_synchronization",
    "bounded_relevance_reception_not_inhabitance",
    "bounded_relevance_reception_not_runtime_permission",
    "bounded_relevance_reception_not_public_api",
    "bounded_relevance_reception_not_participant_facing_interface",
    "bounded_relevance_reception_not_distributed_network_behavior",
    "source_transfer_not_created",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "truth_not_created",
    "action_not_created",
    "synchronization_not_created",
    "inhabitance_not_created",
    "runtime_permission_not_created",
    "public_api_not_created",
    "participant_facing_interface_not_created",
    "distributed_network_behavior_not_created",
    "deployment_not_created",
    "public_release_not_created",
    "operation_permission_not_created",
    "broader_reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_bounded_relevance_reception_authority",
    "repo_local_availability_not_bounded_relevance_reception_authority",
    "artifact_existence_not_bounded_relevance_reception_authority",
    "latest_file_posture_not_bounded_relevance_reception_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "BOUNDED_RELEVANCE_RECEPTION_QUESTION_UNDECLARED",
    "BOUNDED_RELEVANCE_RECEPTION_INTENT_UNSUPPORTED",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_BASIS_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_ALREADY_CREATED_RECEPTION",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_AUTHORIZED_MECHANISM",
    "RUNTIME_LAYER_CLOSURE_BASIS_MISSING",
    "RUNTIME_LAYER_CLOSURE_NOT_RECORDED",
    "RUNTIME_LAYER_CLOSURE_DID_NOT_CLOSE_INTERNAL_RUNTIME_STACK",
    "RUNTIME_LAYER_CLOSURE_SELECTED_PUBLIC_API",
    "RUNTIME_LAYER_CLOSURE_SELECTED_PARTICIPANT_INTERFACE",
    "RUNTIME_LAYER_CLOSURE_SELECTED_DISTRIBUTED_NETWORK",
    "RUNTIME_LAYER_CLOSURE_SELECTED_SOURCE_AUTHORITY_CURRENTNESS",
    "RUNTIME_LAYER_CLOSURE_SELECTED_DEPLOYMENT_OPERATION",
    "RUNTIME_LAYER_CLOSURE_AUTHORIZED_FOLLOW_ON_WORK",
    "RUNTIME_LOOP_BASIS_MISSING",
    "RUNTIME_LOOP_NOT_RECORDED",
    "RUNTIME_LOOP_FAILED_CHECKS_PRESENT",
    "RUNTIME_LOOP_VERSION_NOT_0_1_0",
    "RUNTIME_LOOP_DID_NOT_RECORD_BOUNDED_RUNTIME_LOOP_POSTURE",
    "RUNTIME_LOOP_DID_NOT_RECORD_BOUNDED_RUNTIME_LOOP_ENVELOPE",
    "RUNTIME_LOOP_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_LOOP_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_ALREADY_CREATED_SOURCE",
    "RUNTIME_LOOP_ALREADY_CREATED_AUTHORITY",
    "RUNTIME_LOOP_ALREADY_CREATED_CURRENTNESS",
    "RUNTIME_LOOP_ALREADY_CREATED_DEPLOYMENT",
    "RUNTIME_LOOP_ALREADY_CREATED_PUBLIC_RELEASE",
    "RUNTIME_LOOP_ALREADY_CREATED_OPERATION_PERMISSION",
    "RUNTIME_LOOP_AUTHORIZED_FOLLOW_ON_WORK",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_TREATED_AS_RECEPTION_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_ACTION_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_SYNCHRONIZATION_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_RUNTIME_PERMISSION",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_PUBLIC_API",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_PARTICIPANT_INTERFACE",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_DISTRIBUTED_NETWORK",
    "BOUNDED_RELEVANCE_SIGNAL_MISSING",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_SOURCE",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_AUTHORITY",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_CURRENTNESS",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_TRUTH",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_ACTION",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_SYNCHRONIZATION",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_INHABITANCE",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_RUNTIME_PERMISSION",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_PUBLIC_API",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RELEVANCE_BASIS_MISSING",
    "RELEVANCE_BASIS_TREATED_AS_TRUTH",
    "RELEVANCE_BASIS_TREATED_AS_AUTHORITY",
    "RELEVANCE_SCOPE_MISSING",
    "RELEVANCE_SCOPE_UNBOUNDED",
    "BOUNDED_RELEVANCE_RECEPTION_RECORDED_BEFORE_REVIEW",
    "RELEVANCE_RECEIPT_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "INHABITANCE_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_BOUNDED_RELEVANCE_RECEPTION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE",
    "DECLARED_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
    "DECLARED_BOUNDED_RELEVANCE_RECEPTION_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_SIGNAL_BODY_MUST_NOT_RETURN",
    "RAW_RELEVANCE_BODY_MUST_NOT_RETURN",
    "RAW_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_INHABITANCE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_bounded_relevance_reception_body",
    "raw_bounded_relevance_signal_body",
    "raw_relevance_body",
    "raw_relevance_receipt_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_inhabitance_body",
    "raw_runtime_permission_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "bounded_relevance_reception_body",
    "bounded_relevance_signal_body",
    "relevance_body",
    "relevance_receipt_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
    "synchronization_body",
    "inhabitance_body",
    "runtime_permission_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

OFFICIAL_STRINGS = set(SUPPORTED_SCOPE_VALUES) | set(OUTCOME_FAMILY) | set(BLOCK_CODES) | set(
    REQUIRED_FALSE_NON_CLAIMS
) | set(ALLOWED_TRUE_RECORDED_FIELDS)

TOP_LEVEL_SECTIONS = (
    "bounded_relevance_reception_metadata",
    "declared_bounded_relevance_reception_question",
    "selected_bounded_relevance_reception_selection_basis",
    "selected_runtime_layer_closure_basis",
    "selected_runtime_loop_basis",
    "selected_runtime_loop_terminal_summary_basis",
    "selected_runtime_loop_boundary_basis",
    "selected_runtime_daemon_basis",
    "selected_runtime_daemon_boundary_basis",
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
    "selected_carrier_aware_distributed_anatomy_basis",
    "selected_carrier_role_emission_basis",
    "selected_carrier_lifecycle_basis",
    "selected_registry_persistence_basis",
    "selected_cross_carrier_receipt_refusal_return_basis",
    "selected_divergence_basis",
    "selected_cross_carrier_currentness_caution_basis",
    "selected_standing_propagation_basis",
    "selected_distributed_standing_distinction_basis",
    "selected_synchronization_non_synchronization_basis",
    "selected_operation_admission_basis",
    "selected_execution_emission_boundary_basis",
    "selected_action_consequence_refusal_basis",
    "selected_distributed_chain_closure_basis",
    "bounded_relevance_reception_spec_only_posture",
    "one_bounded_relevance_reception_posture",
    "bounded_relevance_signal",
    "relevance_basis",
    "relevance_scope",
    "relevance_signal_carrier_context",
    "bounded_relevance_reception_envelope",
    "runtime_layer_closure_basis_preserved_posture",
    "runtime_loop_basis_preserved_posture",
    "bounded_runtime_loop_envelope_preserved_posture",
    "carrier_aware_distributed_anatomy_basis_preserved_posture",
    "bounded_relevance_reception_not_source_transfer_posture",
    "bounded_relevance_reception_not_source_receipt_posture",
    "bounded_relevance_reception_not_reception_authorization_posture",
    "bounded_relevance_reception_not_source_posture",
    "bounded_relevance_reception_not_authority_posture",
    "bounded_relevance_reception_not_currentness_posture",
    "bounded_relevance_reception_not_truth_posture",
    "bounded_relevance_reception_not_action_posture",
    "bounded_relevance_reception_not_synchronization_posture",
    "bounded_relevance_reception_not_inhabitance_posture",
    "bounded_relevance_reception_not_runtime_permission_posture",
    "bounded_relevance_reception_not_public_api_posture",
    "bounded_relevance_reception_not_participant_facing_interface_posture",
    "bounded_relevance_reception_not_distributed_network_behavior_posture",
    "source_transfer_not_created_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "truth_not_created_posture",
    "action_not_created_posture",
    "synchronization_not_created_posture",
    "inhabitance_not_created_posture",
    "runtime_permission_not_created_posture",
    "public_api_not_created_posture",
    "participant_facing_interface_not_created_posture",
    "distributed_network_behavior_not_created_posture",
    "deployment_not_created_posture",
    "public_release_not_created_posture",
    "operation_permission_not_created_posture",
    "broader_reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_bounded_relevance_reception_authority_posture",
    "artifact_existence_not_bounded_relevance_reception_authority_posture",
    "latest_file_posture_not_bounded_relevance_reception_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "bounded_relevance_reception_scope",
    "bounded_relevance_reception_checks",
    "bounded_relevance_reception_statement",
    "bounded_relevance_reception_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "bounded_relevance_reception_summary",
)

OPEN_ITEMS = (
    "bounded relevance reception resolver",
    "bounded relevance reception test",
    "bounded relevance reception live artifact",
    "bounded relevance reception terminal summary, if needed",
    "relevance receipt shape",
    "public API",
    "participant-facing interface",
    "distributed network behavior",
    "source transfer",
    "source receipt",
    "reception authorization",
    "derivative reception",
    "vessel relation",
    "adoption",
    "authority creation",
    "currentness creation",
    "truth creation",
    "action",
    "synchronization",
    "inhabitance",
    "runtime permission",
    "operation permission",
    "receiving-context governance",
    "deployment",
    "public release",
    "publication flow",
    "broader reusable permission",
    "successor reception request",
    "follow-on work",
)

REFERENCE_BASIS_DEFAULTS = {
    "selected_bounded_relevance_reception_selection_basis": {
        "path": "spec/POST_RUNTIME_LOOP_BOUNDED_RELEVANCE_RECEPTION_SELECTION_V0.md",
        "basis_role": "selected_next_layer_pressure_basis_only",
    },
    "selected_runtime_layer_closure_basis": {
        "path": "spec/POST_RUNTIME_LOOP_INTERNAL_RUNTIME_LAYER_CLOSURE_REVIEW_V0.md",
        "basis_role": "controlling_internal_runtime_closure_basis",
    },
    "selected_runtime_loop_basis": {
        "path": "artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop",
        "basis_role": "runtime_loop_live_artifact_basis",
    },
    "selected_runtime_loop_terminal_summary_basis": {
        "path": "spec/POST_RUNTIME_DAEMON_RUNTIME_LOOP_TERMINAL_SUMMARY_V0.md",
        "basis_role": "runtime_loop_terminal_summary_basis",
    },
    "selected_runtime_loop_boundary_basis": {
        "path": "spec/POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        "basis_role": "runtime_loop_boundary_basis",
    },
    "selected_runtime_daemon_basis": {
        "path": "spec/POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_TERMINAL_SUMMARY_V0.md",
        "basis_role": "runtime_daemon_basis",
    },
    "selected_runtime_daemon_boundary_basis": {
        "path": "spec/POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        "basis_role": "runtime_daemon_boundary_basis",
    },
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis": {
        "path": "tests/test_resolve_post_self_recursive_growth_runtime_daemon_boundary.py",
        "basis_role": "preserved_over_strict_failed_test_evidence_only",
    },
    "selected_carrier_aware_distributed_anatomy_basis": {
        "basis_role": "upstream_basis_only",
        "authority_created": False,
    },
    "selected_carrier_role_emission_basis": {"basis_role": "upstream_basis_only"},
    "selected_carrier_lifecycle_basis": {"basis_role": "upstream_basis_only"},
    "selected_registry_persistence_basis": {"basis_role": "upstream_basis_only"},
    "selected_cross_carrier_receipt_refusal_return_basis": {"basis_role": "upstream_basis_only"},
    "selected_divergence_basis": {"basis_role": "upstream_basis_only"},
    "selected_cross_carrier_currentness_caution_basis": {"basis_role": "caution_only"},
    "selected_standing_propagation_basis": {"basis_role": "upstream_basis_only"},
    "selected_distributed_standing_distinction_basis": {"basis_role": "upstream_basis_only"},
    "selected_synchronization_non_synchronization_basis": {"basis_role": "upstream_basis_only"},
    "selected_operation_admission_basis": {"basis_role": "upstream_basis_only"},
    "selected_execution_emission_boundary_basis": {"basis_role": "upstream_basis_only"},
    "selected_action_consequence_refusal_basis": {"basis_role": "upstream_basis_only"},
    "selected_distributed_chain_closure_basis": {"basis_role": "upstream_basis_only"},
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _deepcopy_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def _sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _contains_raw_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in RAW_SENTINELS)


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _sensitive_key(key):
        if value in (None, "", [], {}):
            return value
        if isinstance(value, str) and value in OFFICIAL_STRINGS:
            return value
        if isinstance(value, (list, tuple)) and all(isinstance(item, str) and item in OFFICIAL_STRINGS for item in value):
            return list(value)
        return "[REDACTED_BOUNDED_RELEVANCE_RECEPTION_RAW_BODY]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if _contains_raw_sentinel(value):
            return "[REDACTED_BOUNDED_RELEVANCE_RECEPTION_RAW_BODY]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    return value


def _declared(value: Any) -> bool:
    if value is None:
        return False
    if value is False:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def _flag(request: Mapping[str, Any], key: str, default: bool = False) -> bool:
    value = request.get(key, default)
    return bool(value)


def _truthy_or_declared(request: Mapping[str, Any], key: str) -> bool:
    value = request.get(key)
    if isinstance(value, Mapping) and "declared" in value:
        return bool(value["declared"])
    return _declared(value)


def _basis_declared(request: Mapping[str, Any], basis_key: str, path_key: str | None = None) -> bool:
    if _declared(request.get(basis_key)):
        return True
    return path_key is not None and _declared(request.get(path_key))


def _scope_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return [str(value)]


def _unsupported_scope_values(request: Mapping[str, Any]) -> list[str]:
    values = _scope_values(request.get("bounded_relevance_reception_scope"))
    return [value for value in values if value not in SUPPORTED_SCOPE_VALUES]


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str,
    *,
    blocking: bool = True,
) -> dict[str, Any]:
    check: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": _sanitize(actual_posture),
    }
    if passed:
        check["block_code"] = None
        check["failure_code"] = None
    elif blocking:
        check["block_code"] = code
        check["failure_code"] = None
    else:
        check["block_code"] = None
        check["failure_code"] = code
    return check


def _posture_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    request_key: str,
    check_name: str,
    code: str = "NON_CLAIM_MISSING_OR_FLIPPED",
) -> None:
    checks.append(
        _make_check(
            check_name,
            _truthy_or_declared(request, request_key),
            "declared bounded posture",
            request.get(request_key),
            code,
        )
    )


def _not_flag_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    check_name: str,
    code: str,
) -> None:
    checks.append(
        _make_check(
            check_name,
            not _flag(request, key),
            "false",
            request.get(key, False),
            code,
        )
    )


def _envelope_disallows(
    envelope: Any,
    *keys: str,
) -> bool:
    if not isinstance(envelope, Mapping):
        return False
    for key in keys:
        if bool(envelope.get(key)):
            return False
    disallowed = envelope.get("disallowed_authorizations")
    if isinstance(disallowed, (list, tuple, set)):
        lowered = {str(item).lower() for item in disallowed}
        if any(key.lower() not in lowered for key in keys):
            return False
    return True


def _result_statement(outcome: str) -> dict[str, bool]:
    statement = {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    if outcome == OUTCOME_RECORDED:
        statement.update({key: True for key in ALLOWED_TRUE_RECORDED_FIELDS})
    statement.update(_canonical_non_claims())
    return statement


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    intent = request.get("bounded_relevance_reception_intent")
    scope_values = _scope_values(request.get("bounded_relevance_reception_scope"))
    unsupported_scope = _unsupported_scope_values(request)
    envelope = request.get("bounded_relevance_reception_envelope")
    declared_non_claims = request.get("declared_non_claims")

    checks.append(
        _make_check(
            "bounded relevance reception question declared",
            _declared(request.get("bounded_relevance_reception_question")),
            "declared bounded relevance reception question",
            request.get("bounded_relevance_reception_question"),
            "BOUNDED_RELEVANCE_RECEPTION_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _make_check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            f"one of {SUPPORTED_INTENTS}",
            intent,
            "BOUNDED_RELEVANCE_RECEPTION_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _make_check(
            "bounded relevance reception scope supported",
            bool(scope_values) and not unsupported_scope,
            "only supported bounded relevance reception scope values",
            scope_values,
            "UNSUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE",
        )
    )
    checks.append(
        _make_check(
            "bounded relevance reception selection basis declared",
            _basis_declared(
                request,
                "selected_bounded_relevance_reception_selection_basis",
                "selected_bounded_relevance_reception_selection_path",
            ),
            "declared selection basis",
            request.get("selected_bounded_relevance_reception_selection_basis")
            or request.get("selected_bounded_relevance_reception_selection_path"),
            "BOUNDED_RELEVANCE_RECEPTION_SELECTION_BASIS_MISSING",
        )
    )
    checks.append(
        _make_check(
            "bounded relevance reception selection states selected next-layer pressure",
            _flag(request, "selected_bounded_relevance_reception_selection_states_selected_next_layer_pressure"),
            "true",
            request.get("selected_bounded_relevance_reception_selection_states_selected_next_layer_pressure"),
            "BOUNDED_RELEVANCE_RECEPTION_SELECTION_NOT_RECORDED",
        )
    )
    _not_flag_check(
        request,
        checks,
        "selected_bounded_relevance_reception_selection_already_created_reception",
        "bounded relevance reception selection did not create bounded relevance reception",
        "BOUNDED_RELEVANCE_RECEPTION_SELECTION_ALREADY_CREATED_RECEPTION",
    )
    _not_flag_check(
        request,
        checks,
        "selected_bounded_relevance_reception_selection_authorized_mechanism",
        "bounded relevance reception selection did not authorize resolver/test/live artifact automatically",
        "BOUNDED_RELEVANCE_RECEPTION_SELECTION_AUTHORIZED_MECHANISM",
    )
    checks.append(
        _make_check(
            "runtime-layer closure basis declared",
            _basis_declared(request, "selected_runtime_layer_closure_basis", "selected_runtime_layer_closure_path"),
            "declared runtime-layer closure basis",
            request.get("selected_runtime_layer_closure_basis") or request.get("selected_runtime_layer_closure_path"),
            "RUNTIME_LAYER_CLOSURE_BASIS_MISSING",
        )
    )
    checks.append(
        _make_check(
            "runtime-layer closure recorded",
            _flag(request, "selected_runtime_layer_closure_recorded"),
            "true",
            request.get("selected_runtime_layer_closure_recorded"),
            "RUNTIME_LAYER_CLOSURE_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "runtime-layer closure closed internal runtime/autonomy stack through runtime loop",
            _flag(request, "selected_runtime_layer_closure_closed_internal_runtime_stack"),
            "true",
            request.get("selected_runtime_layer_closure_closed_internal_runtime_stack"),
            "RUNTIME_LAYER_CLOSURE_DID_NOT_CLOSE_INTERNAL_RUNTIME_STACK",
        )
    )
    checks.append(
        _make_check(
            "runtime-layer closure requires separate next-layer selection/admission",
            _flag(request, "selected_runtime_layer_closure_requires_next_layer_selection"),
            "true",
            request.get("selected_runtime_layer_closure_requires_next_layer_selection"),
            "RUNTIME_LAYER_CLOSURE_AUTHORIZED_FOLLOW_ON_WORK",
        )
    )
    _not_flag_check(
        request,
        checks,
        "selected_runtime_layer_closure_selected_public_api",
        "runtime-layer closure did not select public API",
        "RUNTIME_LAYER_CLOSURE_SELECTED_PUBLIC_API",
    )
    _not_flag_check(
        request,
        checks,
        "selected_runtime_layer_closure_selected_participant_facing_interface",
        "runtime-layer closure did not select participant-facing interface",
        "RUNTIME_LAYER_CLOSURE_SELECTED_PARTICIPANT_INTERFACE",
    )
    _not_flag_check(
        request,
        checks,
        "selected_runtime_layer_closure_selected_distributed_network_behavior",
        "runtime-layer closure did not select distributed network behavior",
        "RUNTIME_LAYER_CLOSURE_SELECTED_DISTRIBUTED_NETWORK",
    )
    _not_flag_check(
        request,
        checks,
        "selected_runtime_layer_closure_selected_source_authority_currentness",
        "runtime-layer closure did not select source/authority/currentness",
        "RUNTIME_LAYER_CLOSURE_SELECTED_SOURCE_AUTHORITY_CURRENTNESS",
    )
    _not_flag_check(
        request,
        checks,
        "selected_runtime_layer_closure_selected_deployment_operation",
        "runtime-layer closure did not select deployment/public-release/operation-permission",
        "RUNTIME_LAYER_CLOSURE_SELECTED_DEPLOYMENT_OPERATION",
    )
    _not_flag_check(
        request,
        checks,
        "selected_runtime_layer_closure_authorized_follow_on_work",
        "runtime-layer closure did not authorize follow-on work",
        "RUNTIME_LAYER_CLOSURE_AUTHORIZED_FOLLOW_ON_WORK",
    )
    checks.append(
        _make_check(
            "runtime-loop basis declared",
            _basis_declared(request, "selected_runtime_loop_basis", "selected_runtime_loop_result_path"),
            "declared runtime-loop basis",
            request.get("selected_runtime_loop_basis") or request.get("selected_runtime_loop_result_path"),
            "RUNTIME_LOOP_BASIS_MISSING",
        )
    )
    checks.append(
        _make_check(
            "runtime-loop outcome recorded",
            request.get("selected_runtime_loop_result_outcome") == "POST_RUNTIME_DAEMON_RUNTIME_LOOP_RECORDED",
            "POST_RUNTIME_DAEMON_RUNTIME_LOOP_RECORDED",
            request.get("selected_runtime_loop_result_outcome"),
            "RUNTIME_LOOP_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "runtime-loop version 0.1.0",
            request.get("selected_runtime_loop_result_version") == RESULT_VERSION,
            RESULT_VERSION,
            request.get("selected_runtime_loop_result_version"),
            "RUNTIME_LOOP_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _make_check(
            "runtime-loop failed checks zero",
            request.get("selected_runtime_loop_failed_check_count") == 0,
            "0",
            request.get("selected_runtime_loop_failed_check_count"),
            "RUNTIME_LOOP_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _make_check(
            "runtime-loop recorded bounded runtime-loop posture",
            _flag(request, "selected_runtime_loop_bounded_posture_recorded"),
            "true",
            request.get("selected_runtime_loop_bounded_posture_recorded"),
            "RUNTIME_LOOP_DID_NOT_RECORD_BOUNDED_RUNTIME_LOOP_POSTURE",
        )
    )
    checks.append(
        _make_check(
            "runtime-loop recorded bounded runtime-loop envelope",
            _flag(request, "selected_runtime_loop_bounded_runtime_loop_envelope_recorded"),
            "true",
            request.get("selected_runtime_loop_bounded_runtime_loop_envelope_recorded"),
            "RUNTIME_LOOP_DID_NOT_RECORD_BOUNDED_RUNTIME_LOOP_ENVELOPE",
        )
    )
    for key, name, code in (
        (
            "selected_runtime_loop_already_created_public_api",
            "runtime-loop did not create public API",
            "RUNTIME_LOOP_ALREADY_CREATED_PUBLIC_API",
        ),
        (
            "selected_runtime_loop_already_created_participant_facing_interface",
            "runtime-loop did not create participant-facing interface",
            "RUNTIME_LOOP_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_runtime_loop_already_created_distributed_network_behavior",
            "runtime-loop did not create distributed network behavior",
            "RUNTIME_LOOP_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        ("selected_runtime_loop_already_created_source", "runtime-loop did not create source", "RUNTIME_LOOP_ALREADY_CREATED_SOURCE"),
        (
            "selected_runtime_loop_already_created_authority",
            "runtime-loop did not create authority",
            "RUNTIME_LOOP_ALREADY_CREATED_AUTHORITY",
        ),
        (
            "selected_runtime_loop_already_created_currentness",
            "runtime-loop did not create currentness",
            "RUNTIME_LOOP_ALREADY_CREATED_CURRENTNESS",
        ),
        (
            "selected_runtime_loop_already_created_deployment",
            "runtime-loop did not create deployment",
            "RUNTIME_LOOP_ALREADY_CREATED_DEPLOYMENT",
        ),
        (
            "selected_runtime_loop_already_created_public_release",
            "runtime-loop did not create public release",
            "RUNTIME_LOOP_ALREADY_CREATED_PUBLIC_RELEASE",
        ),
        (
            "selected_runtime_loop_already_created_operation_permission",
            "runtime-loop did not create operation permission",
            "RUNTIME_LOOP_ALREADY_CREATED_OPERATION_PERMISSION",
        ),
        (
            "selected_runtime_loop_authorized_follow_on_work",
            "runtime-loop did not authorize follow-on work",
            "RUNTIME_LOOP_AUTHORIZED_FOLLOW_ON_WORK",
        ),
    ):
        _not_flag_check(request, checks, key, name, code)
    checks.append(
        _make_check(
            "runtime-loop canonicalized result-level non-claims",
            _flag(request, "selected_runtime_loop_non_claims_canonicalized"),
            "true",
            request.get("selected_runtime_loop_non_claims_canonicalized"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _make_check(
            "carrier-aware / distributed anatomy basis declared",
            _basis_declared(request, "selected_carrier_aware_distributed_anatomy_basis"),
            "declared carrier-aware / distributed anatomy basis",
            request.get("selected_carrier_aware_distributed_anatomy_basis"),
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_AUTHORITY",
        )
    )
    checks.append(
        _make_check(
            "carrier-aware / distributed anatomy basis remains basis only",
            _flag(request, "carrier_aware_distributed_anatomy_basis_preserved_posture"),
            "true basis-only posture",
            request.get("carrier_aware_distributed_anatomy_basis_preserved_posture"),
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_AUTHORITY",
        )
    )
    for key, name, code in (
        (
            "bounded_runtime_loop_envelope_treated_as_reception_authority",
            "bounded runtime-loop envelope not treated as bounded relevance reception authority",
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_TREATED_AS_RECEPTION_AUTHORITY",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_authority",
            "carrier-aware / distributed anatomy basis not authority",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_AUTHORITY",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_action_authority",
            "carrier-aware / distributed anatomy basis not action authority",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_ACTION_AUTHORITY",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_synchronization_authority",
            "carrier-aware / distributed anatomy basis not synchronization authority",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_SYNCHRONIZATION_AUTHORITY",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_runtime_permission",
            "carrier-aware / distributed anatomy basis not runtime permission",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_RUNTIME_PERMISSION",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_public_api",
            "carrier-aware / distributed anatomy basis not public API",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_PUBLIC_API",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_participant_interface",
            "carrier-aware / distributed anatomy basis not participant-facing interface",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_PARTICIPANT_INTERFACE",
        ),
        (
            "carrier_aware_distributed_anatomy_basis_treated_as_distributed_network",
            "carrier-aware / distributed anatomy basis not distributed network behavior",
            "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_DISTRIBUTED_NETWORK",
        ),
    ):
        _not_flag_check(request, checks, key, name, code)
    checks.append(
        _make_check(
            "bounded relevance signal declared",
            _declared(request.get("bounded_relevance_signal")) and not _flag(request, "bounded_relevance_signal_missing"),
            "one declared bounded relevance signal",
            request.get("bounded_relevance_signal"),
            "BOUNDED_RELEVANCE_SIGNAL_MISSING",
        )
    )
    for key, name, code in (
        ("bounded_relevance_signal_treated_as_source", "bounded relevance signal not source", "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_SOURCE"),
        (
            "bounded_relevance_signal_treated_as_authority",
            "bounded relevance signal not authority",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_AUTHORITY",
        ),
        (
            "bounded_relevance_signal_treated_as_currentness",
            "bounded relevance signal not currentness",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_CURRENTNESS",
        ),
        ("bounded_relevance_signal_treated_as_truth", "bounded relevance signal not truth", "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_TRUTH"),
        ("bounded_relevance_signal_treated_as_action", "bounded relevance signal not action", "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_ACTION"),
        (
            "bounded_relevance_signal_treated_as_synchronization",
            "bounded relevance signal not synchronization",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_SYNCHRONIZATION",
        ),
        (
            "bounded_relevance_signal_treated_as_inhabitance",
            "bounded relevance signal not inhabitance",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_INHABITANCE",
        ),
        (
            "bounded_relevance_signal_treated_as_runtime_permission",
            "bounded relevance signal not runtime permission",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_RUNTIME_PERMISSION",
        ),
        (
            "bounded_relevance_signal_treated_as_public_api",
            "bounded relevance signal not public API",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_PUBLIC_API",
        ),
        (
            "bounded_relevance_signal_treated_as_participant_facing_interface",
            "bounded relevance signal not participant-facing interface",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "bounded_relevance_signal_treated_as_distributed_network_behavior",
            "bounded relevance signal not distributed network behavior",
            "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
    ):
        _not_flag_check(request, checks, key, name, code)
    checks.append(
        _make_check(
            "relevance basis declared",
            _declared(request.get("relevance_basis")) and not _flag(request, "relevance_basis_missing"),
            "declared relevance basis",
            request.get("relevance_basis"),
            "RELEVANCE_BASIS_MISSING",
        )
    )
    _not_flag_check(request, checks, "relevance_basis_treated_as_truth", "relevance basis not truth", "RELEVANCE_BASIS_TREATED_AS_TRUTH")
    _not_flag_check(
        request,
        checks,
        "relevance_basis_treated_as_authority",
        "relevance basis not authority",
        "RELEVANCE_BASIS_TREATED_AS_AUTHORITY",
    )
    checks.append(
        _make_check(
            "relevance scope declared",
            _declared(request.get("relevance_scope")) and not _flag(request, "relevance_scope_missing"),
            "declared relevance scope",
            request.get("relevance_scope"),
            "RELEVANCE_SCOPE_MISSING",
        )
    )
    checks.append(
        _make_check(
            "relevance scope bounded",
            not _flag(request, "relevance_scope_unbounded"),
            "bounded relevance scope",
            request.get("relevance_scope_unbounded", False),
            "RELEVANCE_SCOPE_UNBOUNDED",
        )
    )
    checks.append(
        _make_check(
            "bounded relevance reception envelope declared",
            _declared(envelope),
            "declared bounded relevance reception envelope",
            envelope,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    for key, code, label in (
        ("authorize_arbitrary_reception", "NON_CLAIM_MISSING_OR_FLIPPED", "arbitrary reception"),
        ("authorize_repeated_reception", "NON_CLAIM_MISSING_OR_FLIPPED", "repeated reception"),
        ("authorize_source_receipt", "SOURCE_RECEIPT_OCCURRED", "source receipt"),
        ("authorize_reception_authorization", "RECEPTION_AUTHORIZATION_CREATED", "reception authorization"),
        ("authorize_action", "ACTION_CREATED", "action"),
        ("authorize_synchronization", "SYNCHRONIZATION_CREATED", "synchronization"),
        ("authorize_inhabitance", "INHABITANCE_CREATED", "inhabitance"),
        ("authorize_runtime_permission", "RUNTIME_PERMISSION_CREATED", "runtime permission"),
        ("authorize_follow_on_work", "FOLLOW_ON_WORK_AUTHORIZED", "follow-on work"),
    ):
        checks.append(
            _make_check(
                f"bounded relevance reception envelope does not authorize {label}",
                _envelope_disallows(envelope, key),
                f"{key}=false",
                envelope,
                code,
            )
        )
    checks.append(
        _make_check(
            "bounded relevance reception envelope does not authorize public API / participant-facing interface / distributed network behavior",
            _envelope_disallows(
                envelope,
                "authorize_public_api",
                "authorize_participant_facing_interface",
                "authorize_distributed_network_behavior",
            ),
            "public/interface/distributed authorizations false",
            envelope,
            "PUBLIC_API_CREATED",
        )
    )
    for key, name, code in (
        (
            "bounded_relevance_reception_recorded_before_review",
            "bounded relevance reception not recorded before this review",
            "BOUNDED_RELEVANCE_RECEPTION_RECORDED_BEFORE_REVIEW",
        ),
        ("relevance_receipt_created", "relevance receipt not created", "RELEVANCE_RECEIPT_CREATED"),
        ("source_transfer_occurred", "source transfer did not occur", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "source receipt did not occur", "SOURCE_RECEIPT_OCCURRED"),
        ("reception_authorization_created", "reception authorization not created", "RECEPTION_AUTHORIZATION_CREATED"),
        ("source_created", "source not created", "SOURCE_CREATED"),
        ("authority_created", "authority not created", "AUTHORITY_CREATED"),
        ("currentness_created", "currentness not created", "CURRENTNESS_CREATED"),
        ("truth_created", "truth not created", "TRUTH_CREATED"),
        ("action_created", "action not created", "ACTION_CREATED"),
        ("synchronization_created", "synchronization not created", "SYNCHRONIZATION_CREATED"),
        ("inhabitance_created", "inhabitance not created", "INHABITANCE_CREATED"),
        ("runtime_permission_created", "runtime permission not created", "RUNTIME_PERMISSION_CREATED"),
        ("public_api_created", "public API not created", "PUBLIC_API_CREATED"),
        (
            "participant_facing_interface_created",
            "participant-facing interface not created",
            "PARTICIPANT_FACING_INTERFACE_CREATED",
        ),
        (
            "distributed_network_behavior_created",
            "distributed network behavior not created",
            "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
        ),
        ("deployment_created", "deployment not created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "public release not created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "operation permission not created", "OPERATION_PERMISSION_CREATED"),
        ("broader_reusable_permission_created", "broader reusable permission not created", "BROADER_REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "derivative reception not authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "vessel relation not authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("adoption_created", "adoption not created", "ADOPTION_CREATED"),
        ("receiving_context_governance_created", "receiving-context governance not created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
        ("publication_flow_created", "publication flow not created", "PUBLICATION_FLOW_CREATED"),
        ("follow_on_work_authorized", "follow-on work not authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        (
            "artifact_existence_treated_as_bounded_relevance_reception_authority",
            "artifact existence not treated as bounded-relevance-reception authority",
            "ARTIFACT_EXISTENCE_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
        ),
        ("artifact_path_treated_as_currentness", "artifact path not treated as currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        (
            "latest_file_posture_treated_as_bounded_relevance_reception_authority",
            "latest file posture not treated as bounded-relevance-reception authority",
            "LATEST_FILE_POSTURE_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
        ),
        (
            "repo_local_availability_treated_as_bounded_relevance_reception_authority",
            "repo-local availability not treated as bounded-relevance-reception authority",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
        ),
        (
            "hidden_repo_state_used_as_bounded_relevance_reception_content",
            "hidden repo state not used as bounded-relevance-reception content",
            "HIDDEN_REPO_STATE_USED_AS_BOUNDED_RELEVANCE_RECEPTION_CONTENT",
        ),
        ("raw_full_prior_artifact_body_returned", "raw full prior artifact body not returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        ("runtime_daemon_boundary_v1_failure_hidden", "runtime-daemon-boundary v1 failure not hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("runtime_daemon_boundary_v1_failure_repaired", "runtime-daemon-boundary v1 failure not repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        (
            "runtime_daemon_boundary_v1_failure_claimed_passed",
            "runtime-daemon-boundary v1 failure not claimed passed",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        ("runtime_hosting_boundary_v1_failure_hidden", "runtime-hosting-boundary v1 failure not hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("runtime_hosting_boundary_v1_failure_repaired", "runtime-hosting-boundary v1 failure not repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        (
            "runtime_hosting_boundary_v1_failure_claimed_passed",
            "runtime-hosting-boundary v1 failure not claimed passed",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
    ):
        _not_flag_check(request, checks, key, name, code)
    checks.append(
        _make_check(
            "selected basis reference-shaped",
            _flag(request, "reference_shaped_input_posture"),
            "true",
            request.get("reference_shaped_input_posture"),
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        )
    )
    checks.append(
        _make_check(
            "predecessor failure evidence visible and unrepaired",
            not _flag(request, "predecessor_failure_repaired")
            and not _flag(request, "predecessor_failure_hidden")
            and not _flag(request, "predecessor_failure_claimed_passed"),
            "failure evidence preserved and not repaired/hidden/claimed passed",
            {
                "predecessor_failure_repaired": request.get("predecessor_failure_repaired", False),
                "predecessor_failure_hidden": request.get("predecessor_failure_hidden", False),
                "predecessor_failure_claimed_passed": request.get("predecessor_failure_claimed_passed", False),
            },
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )

    for request_key, check_name in (
        ("bounded_relevance_reception_spec_only_posture", "bounded-relevance-reception-spec-only posture declared"),
        ("one_bounded_relevance_reception_posture", "one-bounded-relevance-reception-posture declared"),
        ("bounded_relevance_signal", "bounded-relevance-signal-declared posture declared"),
        ("bounded_relevance_reception_envelope", "bounded-relevance-reception-envelope-declared posture declared"),
        ("runtime_layer_closure_basis_preserved_posture", "runtime-layer-closure-basis-preserved posture declared"),
        ("runtime_loop_basis_preserved_posture", "runtime-loop-basis-preserved posture declared"),
        ("bounded_runtime_loop_envelope_preserved_posture", "bounded-runtime-loop-envelope-preserved posture declared"),
        ("carrier_aware_distributed_anatomy_basis_preserved_posture", "carrier-aware-distributed-anatomy-basis-preserved posture declared"),
        ("bounded_relevance_reception_not_source_transfer_posture", "bounded-relevance-reception-not-source-transfer posture declared"),
        ("bounded_relevance_reception_not_source_receipt_posture", "bounded-relevance-reception-not-source-receipt posture declared"),
        (
            "bounded_relevance_reception_not_reception_authorization_posture",
            "bounded-relevance-reception-not-reception-authorization posture declared",
        ),
        ("bounded_relevance_reception_not_source_posture", "bounded-relevance-reception-not-source posture declared"),
        ("bounded_relevance_reception_not_authority_posture", "bounded-relevance-reception-not-authority posture declared"),
        ("bounded_relevance_reception_not_currentness_posture", "bounded-relevance-reception-not-currentness posture declared"),
        ("bounded_relevance_reception_not_truth_posture", "bounded-relevance-reception-not-truth posture declared"),
        ("bounded_relevance_reception_not_action_posture", "bounded-relevance-reception-not-action posture declared"),
        ("bounded_relevance_reception_not_synchronization_posture", "bounded-relevance-reception-not-synchronization posture declared"),
        ("bounded_relevance_reception_not_inhabitance_posture", "bounded-relevance-reception-not-inhabitance posture declared"),
        (
            "bounded_relevance_reception_not_runtime_permission_posture",
            "bounded-relevance-reception-not-runtime-permission posture declared",
        ),
        ("bounded_relevance_reception_not_public_api_posture", "bounded-relevance-reception-not-public-api posture declared"),
        (
            "bounded_relevance_reception_not_participant_facing_interface_posture",
            "bounded-relevance-reception-not-participant-facing-interface posture declared",
        ),
        (
            "bounded_relevance_reception_not_distributed_network_behavior_posture",
            "bounded-relevance-reception-not-distributed-network-behavior posture declared",
        ),
        (
            "source_transfer_not_created_posture",
            "source/authority/currentness/truth/action/synchronization/inhabitance/runtime-permission/public-api/participant-facing-interface/distributed-network-behavior/deployment/public-release/operation-permission/follow-on not-created posture declared",
        ),
        ("hidden_repo_state_excluded_posture", "hidden repo state excluded"),
        (
            "repo_local_availability_not_bounded_relevance_reception_authority_posture",
            "repo-local availability not bounded-relevance-reception authority",
        ),
        ("artifact_existence_not_bounded_relevance_reception_authority_posture", "artifact existence not bounded-relevance-reception authority"),
        ("latest_file_posture_not_bounded_relevance_reception_authority_posture", "latest file posture not bounded-relevance-reception authority"),
        ("selected_basis_reference_shape_posture", "selected basis reference-shaped"),
        ("raw_full_prior_artifact_body_not_returned_posture", "raw full prior artifact body not returned"),
        ("official_enum_scope_strings_not_redacted_posture", "official enum scope strings not redacted"),
        ("hostile_raw_body_content_contained_posture", "hostile raw body content contained"),
        ("result_level_non_claims_canonical_false_posture", "result-level required false non-claims canonical false"),
    ):
        _posture_check(request, checks, request_key, check_name)

    _posture_check(
        request,
        checks,
        "predecessor_failure_evidence_preserved_posture",
        "predecessor failure evidence preserved posture declared",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    checks.append(
        _make_check(
            "hidden repo state not used as bounded-relevance-reception authority",
            not _flag(request, "hidden_repo_state_used_as_bounded_relevance_reception_authority"),
            "false",
            request.get("hidden_repo_state_used_as_bounded_relevance_reception_authority", False),
            "HIDDEN_REPO_STATE_USED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
        )
    )
    checks.append(
        _make_check(
            "consumed token remains closed",
            not _flag(request, "consumed_request_reopened"),
            "false",
            request.get("consumed_request_reopened", False),
            "CONSUMED_REQUEST_REOPENED",
        )
    )
    checks.append(
        _make_check(
            "authorization token reuse blocked",
            not _flag(request, "authorization_token_reused"),
            "false",
            request.get("authorization_token_reused", False),
            "AUTHORIZATION_TOKEN_REUSED",
        )
    )
    checks.append(
        _make_check(
            "required non-claims false",
            isinstance(declared_non_claims, Mapping)
            and all(declared_non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
            "all required declared non-claims false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _basis_section(request: Mapping[str, Any], section: str) -> Any:
    value = request.get(section)
    if _declared(value):
        return _sanitize(value, section)
    if section in REFERENCE_BASIS_DEFAULTS:
        return _sanitize(REFERENCE_BASIS_DEFAULTS[section], section)
    return {"declared": False, "basis_role": "not_supplied"}


def _posture_section(request: Mapping[str, Any], section: str, default_name: str | None = None) -> Any:
    value = request.get(section)
    if _declared(value):
        return _sanitize(value, section)
    return {
        "declared": False,
        "posture": default_name or section,
    }


def _build_block(outcome: str, checks: list[dict[str, Any]], explicit_reason: Any = None) -> dict[str, Any]:
    failed_codes = [
        check.get("block_code")
        for check in checks
        if not check.get("passed") and check.get("block_code") in BLOCK_CODES
    ]
    code = failed_codes[0] if failed_codes else None
    return {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": code,
        "reason": _sanitize(explicit_reason) if explicit_reason else code,
        "failed_block_codes": failed_codes,
    }


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    intent = request.get("bounded_relevance_reception_intent")
    if any(not check.get("passed") and check.get("block_code") for check in checks):
        return OUTCOME_BLOCKED
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED
    if intent == INTENT_DO_NOT_RECORD or _declared(request.get("not_recorded_basis")):
        return OUTCOME_NOT_RECORDED
    if _declared(request.get("additional_basis_context")) or _declared(request.get("additional_basis_required")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return OUTCOME_RECORDED


def _safe_request_id(request: Mapping[str, Any]) -> str:
    value = str(request.get("bounded_relevance_reception_request_id") or "bounded_relevance_reception_v0_min_request")
    cleaned = "".join(character if character.isalnum() or character in ("-", "_") else "_" for character in value)
    return cleaned.strip("_") or "bounded_relevance_reception_v0_min_request"


def _base_result_from_request(request: Mapping[str, Any], checks: list[dict[str, Any]], outcome: str) -> dict[str, Any]:
    statement = _result_statement(outcome)
    passed_check_count = sum(1 for check in checks if check.get("passed"))
    failed_check_count = len(checks) - passed_check_count
    request_id = _safe_request_id(request)
    selected_scope = _scope_values(request.get("bounded_relevance_reception_scope"))
    result: dict[str, Any] = {
        "bounded_relevance_reception_metadata": {
            "bounded_relevance_reception_id": request_id,
            "bounded_relevance_reception_type": "bounded_relevance_reception_v0_min",
            "bounded_relevance_reception_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "intent": request.get("bounded_relevance_reception_intent"),
            "passed_check_count": passed_check_count,
            "failed_check_count": failed_check_count,
        },
        "declared_bounded_relevance_reception_question": {
            "question": _sanitize(request.get("bounded_relevance_reception_question")),
            "declared": _declared(request.get("bounded_relevance_reception_question")),
            "core_question": CORE_QUESTION,
        },
        "bounded_relevance_reception_spec_only_posture": _posture_section(request, "bounded_relevance_reception_spec_only_posture"),
        "one_bounded_relevance_reception_posture": _posture_section(request, "one_bounded_relevance_reception_posture"),
        "bounded_relevance_signal": _sanitize(request.get("bounded_relevance_signal"), "bounded_relevance_signal"),
        "relevance_basis": _sanitize(request.get("relevance_basis"), "relevance_basis"),
        "relevance_scope": _sanitize(request.get("relevance_scope"), "relevance_scope"),
        "relevance_signal_carrier_context": _sanitize(
            request.get("relevance_signal_carrier_context"), "relevance_signal_carrier_context"
        ),
        "bounded_relevance_reception_envelope": _sanitize(
            request.get("bounded_relevance_reception_envelope"), "bounded_relevance_reception_envelope"
        ),
        "bounded_relevance_reception_scope": {
            "selected_scope": selected_scope,
            "unsupported_scope_values": _unsupported_scope_values(request),
            "supported_scope_values": list(SUPPORTED_SCOPE_VALUES),
        },
        "bounded_relevance_reception_checks": checks,
        "bounded_relevance_reception_statement": statement,
        "bounded_relevance_reception_non_meaning": {
            "non_claims": _canonical_non_claims(),
            "statement": (
                "Bounded relevance reception is not relevance receipt, source transfer, "
                "source receipt, reception authorization, source, authority, currentness, "
                "truth, action, synchronization, inhabitance, runtime permission, public "
                "API, participant-facing interface, distributed network behavior, deployment, "
                "public release, operation permission, broader reusable permission, derivative "
                "reception, vessel relation, adoption, receiving-context governance, publication "
                "flow, or follow-on work."
            ),
        },
        "additional_basis_required": _sanitize(request.get("additional_basis_required") or request.get("additional_basis_context") or []),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis") or []),
        "what_remains_open": {
            "items": list(OPEN_ITEMS),
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
        },
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": _build_block(outcome, checks, request.get("block_reason")),
    }

    for section in (
        "selected_bounded_relevance_reception_selection_basis",
        "selected_runtime_layer_closure_basis",
        "selected_runtime_loop_basis",
        "selected_runtime_loop_terminal_summary_basis",
        "selected_runtime_loop_boundary_basis",
        "selected_runtime_daemon_basis",
        "selected_runtime_daemon_boundary_basis",
        "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
        "selected_carrier_aware_distributed_anatomy_basis",
        "selected_carrier_role_emission_basis",
        "selected_carrier_lifecycle_basis",
        "selected_registry_persistence_basis",
        "selected_cross_carrier_receipt_refusal_return_basis",
        "selected_divergence_basis",
        "selected_cross_carrier_currentness_caution_basis",
        "selected_standing_propagation_basis",
        "selected_distributed_standing_distinction_basis",
        "selected_synchronization_non_synchronization_basis",
        "selected_operation_admission_basis",
        "selected_execution_emission_boundary_basis",
        "selected_action_consequence_refusal_basis",
        "selected_distributed_chain_closure_basis",
    ):
        result[section] = _basis_section(request, section)

    for section in (
        "runtime_layer_closure_basis_preserved_posture",
        "runtime_loop_basis_preserved_posture",
        "bounded_runtime_loop_envelope_preserved_posture",
        "carrier_aware_distributed_anatomy_basis_preserved_posture",
        "bounded_relevance_reception_not_source_transfer_posture",
        "bounded_relevance_reception_not_source_receipt_posture",
        "bounded_relevance_reception_not_reception_authorization_posture",
        "bounded_relevance_reception_not_source_posture",
        "bounded_relevance_reception_not_authority_posture",
        "bounded_relevance_reception_not_currentness_posture",
        "bounded_relevance_reception_not_truth_posture",
        "bounded_relevance_reception_not_action_posture",
        "bounded_relevance_reception_not_synchronization_posture",
        "bounded_relevance_reception_not_inhabitance_posture",
        "bounded_relevance_reception_not_runtime_permission_posture",
        "bounded_relevance_reception_not_public_api_posture",
        "bounded_relevance_reception_not_participant_facing_interface_posture",
        "bounded_relevance_reception_not_distributed_network_behavior_posture",
        "source_transfer_not_created_posture",
        "source_receipt_not_created_posture",
        "reception_authorization_not_created_posture",
        "source_not_created_posture",
        "authority_not_created_posture",
        "currentness_not_created_posture",
        "truth_not_created_posture",
        "action_not_created_posture",
        "synchronization_not_created_posture",
        "inhabitance_not_created_posture",
        "runtime_permission_not_created_posture",
        "public_api_not_created_posture",
        "participant_facing_interface_not_created_posture",
        "distributed_network_behavior_not_created_posture",
        "deployment_not_created_posture",
        "public_release_not_created_posture",
        "operation_permission_not_created_posture",
        "broader_reusable_permission_not_created_posture",
        "follow_on_work_not_authorized_posture",
        "hidden_repo_state_excluded_posture",
        "repo_local_availability_not_bounded_relevance_reception_authority_posture",
        "artifact_existence_not_bounded_relevance_reception_authority_posture",
        "latest_file_posture_not_bounded_relevance_reception_authority_posture",
        "selected_basis_reference_shape_posture",
        "raw_full_prior_artifact_body_not_returned_posture",
        "official_enum_scope_strings_not_redacted_posture",
        "hostile_raw_body_content_contained_posture",
        "predecessor_failure_evidence_preserved_posture",
        "result_level_non_claims_canonical_false_posture",
    ):
        result[section] = _posture_section(request, section)

    ordered_result = {section: result.get(section) for section in TOP_LEVEL_SECTIONS if section != "bounded_relevance_reception_summary"}
    ordered_result["bounded_relevance_reception_summary"] = build_bounded_relevance_reception_v0_min_summary(ordered_result)
    return ordered_result


def _blocked_malformed_result(code: str, reason: str) -> dict[str, Any]:
    request = build_declared_bounded_relevance_reception_v0_min_request(
        bounded_relevance_reception_request_id="malformed_bounded_relevance_reception_v0_min_request",
        bounded_relevance_reception_intent=INTENT_BLOCK,
        block_reason=reason,
    )
    checks = [
        _make_check(
            "declared bounded relevance reception request readable and well-formed",
            False,
            "mapping JSON request",
            reason,
            code,
        )
    ]
    result = _base_result_from_request(request, checks, OUTCOME_BLOCKED)
    result["block"]["code"] = code
    result["block"]["reason"] = reason
    result["block"]["failed_block_codes"] = [code]
    result["bounded_relevance_reception_summary"] = build_bounded_relevance_reception_v0_min_summary(result)
    return result


def resolve_bounded_relevance_reception_v0_min(
    declared_bounded_relevance_reception_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded relevance reception posture from a declared request."""

    if declared_bounded_relevance_reception_request is None:
        request = build_declared_bounded_relevance_reception_v0_min_request()
    elif not isinstance(declared_bounded_relevance_reception_request, Mapping):
        return _blocked_malformed_result(
            "DECLARED_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
            "declared bounded relevance reception request is not a mapping",
        )
    else:
        request = _deepcopy_mapping(declared_bounded_relevance_reception_request)

    checks = _build_checks(request)
    outcome = _determine_outcome(request, checks)
    return _base_result_from_request(request, checks, outcome)


def resolve_bounded_relevance_reception_v0_min_from_path(
    declared_bounded_relevance_reception_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared request from JSON and resolve it."""

    path = Path(declared_bounded_relevance_reception_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
        loaded = json.loads(raw_text)
    except (OSError, json.JSONDecodeError) as exc:
        return _blocked_malformed_result(
            "DECLARED_BOUNDED_RELEVANCE_RECEPTION_REQUEST_UNREADABLE",
            f"declared bounded relevance reception request unreadable: {exc}",
        )
    return resolve_bounded_relevance_reception_v0_min(loaded)


def write_bounded_relevance_reception_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded relevance reception result artifact without overwriting."""

    if not isinstance(result, Mapping):
        raise BoundedRelevanceReceptionV0MinError("result must be a mapping")
    metadata = result.get("bounded_relevance_reception_metadata", {})
    if isinstance(metadata, Mapping):
        request_id = str(metadata.get("bounded_relevance_reception_id") or "bounded_relevance_reception_v0_min_request")
    else:
        request_id = "bounded_relevance_reception_v0_min_request"
    safe_request_id = "".join(character if character.isalnum() or character in ("-", "_") else "_" for character in request_id)
    filename = f"{safe_request_id}__bounded_relevance_reception_v0_min_result.json"
    candidate = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    candidate.parent.mkdir(parents=True, exist_ok=True)
    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        parent = candidate.parent
        index = 1
        while True:
            suffixed = parent / f"{stem}_{index:03d}{suffix}"
            if not suffixed.exists():
                candidate = suffixed
                break
            index += 1
    candidate.write_text(json.dumps(_sanitize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return candidate


def build_bounded_relevance_reception_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact summary from a bounded relevance reception result."""

    metadata = result.get("bounded_relevance_reception_metadata", {})
    question = result.get("declared_bounded_relevance_reception_question", {})
    statement = result.get("bounded_relevance_reception_statement", {})
    checks = result.get("bounded_relevance_reception_checks", [])
    block = result.get("block", {})
    selected_runtime_loop = result.get("selected_runtime_loop_basis", {})
    selected_runtime_layer_closure = result.get("selected_runtime_layer_closure_basis", {})
    selected_selection = result.get("selected_bounded_relevance_reception_selection_basis", {})

    if not isinstance(metadata, Mapping):
        metadata = {}
    if not isinstance(question, Mapping):
        question = {}
    if not isinstance(statement, Mapping):
        statement = {}
    if not isinstance(block, Mapping):
        block = {}
    if not isinstance(checks, list):
        checks = []

    passed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))

    runtime_loop_outcome = None
    runtime_loop_version = None
    runtime_loop_failed_check_count = None
    if isinstance(selected_runtime_loop, Mapping):
        runtime_loop_outcome = selected_runtime_loop.get("outcome") or "POST_RUNTIME_DAEMON_RUNTIME_LOOP_RECORDED"
        runtime_loop_version = selected_runtime_loop.get("version") or RESULT_VERSION
        runtime_loop_failed_check_count = selected_runtime_loop.get("failed_check_count", 0)

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("bounded_relevance_reception_id"),
        "question": question.get("question"),
        "intent": result.get("bounded_relevance_reception_metadata", {}).get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("bounded_relevance_reception_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "bounded_relevance_reception_recorded": bool(statement.get("bounded_relevance_reception_recorded")),
        "bounded_relevance_reception_posture_recorded": bool(statement.get("bounded_relevance_reception_posture_recorded")),
        "bounded_relevance_signal_declared": bool(statement.get("bounded_relevance_signal_declared")),
        "bounded_relevance_reception_envelope_declared": bool(statement.get("bounded_relevance_reception_envelope_declared")),
        "runtime_layer_closure_basis_preserved": bool(statement.get("runtime_layer_closure_basis_preserved")),
        "runtime_loop_basis_preserved": bool(statement.get("runtime_loop_basis_preserved")),
        "bounded_runtime_loop_envelope_preserved": bool(statement.get("bounded_runtime_loop_envelope_preserved")),
        "carrier_aware_distributed_anatomy_basis_preserved": bool(
            statement.get("carrier_aware_distributed_anatomy_basis_preserved")
        ),
        "bounded_relevance_reception_not_source_transfer": bool(statement.get("bounded_relevance_reception_not_source_transfer")),
        "bounded_relevance_reception_not_source_receipt": bool(statement.get("bounded_relevance_reception_not_source_receipt")),
        "bounded_relevance_reception_not_reception_authorization": bool(
            statement.get("bounded_relevance_reception_not_reception_authorization")
        ),
        "bounded_relevance_reception_not_authority": bool(statement.get("bounded_relevance_reception_not_authority")),
        "bounded_relevance_reception_not_currentness": bool(statement.get("bounded_relevance_reception_not_currentness")),
        "bounded_relevance_reception_not_truth": bool(statement.get("bounded_relevance_reception_not_truth")),
        "bounded_relevance_reception_not_action": bool(statement.get("bounded_relevance_reception_not_action")),
        "bounded_relevance_reception_not_synchronization": bool(statement.get("bounded_relevance_reception_not_synchronization")),
        "bounded_relevance_reception_not_inhabitance": bool(statement.get("bounded_relevance_reception_not_inhabitance")),
        "bounded_relevance_reception_not_runtime_permission": bool(
            statement.get("bounded_relevance_reception_not_runtime_permission")
        ),
        "bounded_relevance_reception_not_public_api": bool(statement.get("bounded_relevance_reception_not_public_api")),
        "bounded_relevance_reception_not_participant_facing_interface": bool(
            statement.get("bounded_relevance_reception_not_participant_facing_interface")
        ),
        "bounded_relevance_reception_not_distributed_network_behavior": bool(
            statement.get("bounded_relevance_reception_not_distributed_network_behavior")
        ),
        "source_transfer_not_created": bool(statement.get("source_transfer_not_created")),
        "source_receipt_not_created": bool(statement.get("source_receipt_not_created")),
        "reception_authorization_not_created": bool(statement.get("reception_authorization_not_created")),
        "source_not_created": bool(statement.get("source_not_created")),
        "authority_not_created": bool(statement.get("authority_not_created")),
        "currentness_not_created": bool(statement.get("currentness_not_created")),
        "truth_not_created": bool(statement.get("truth_not_created")),
        "action_not_created": bool(statement.get("action_not_created")),
        "synchronization_not_created": bool(statement.get("synchronization_not_created")),
        "inhabitance_not_created": bool(statement.get("inhabitance_not_created")),
        "runtime_permission_not_created": bool(statement.get("runtime_permission_not_created")),
        "public_api_not_created": bool(statement.get("public_api_not_created")),
        "participant_facing_interface_not_created": bool(statement.get("participant_facing_interface_not_created")),
        "distributed_network_behavior_not_created": bool(statement.get("distributed_network_behavior_not_created")),
        "deployment_not_created": bool(statement.get("deployment_not_created")),
        "public_release_not_created": bool(statement.get("public_release_not_created")),
        "operation_permission_not_created": bool(statement.get("operation_permission_not_created")),
        "follow_on_work_not_authorized": bool(statement.get("follow_on_work_not_authorized")),
        "hidden_repo_state_excluded": bool(statement.get("hidden_repo_state_excluded")),
        "hidden_repo_state_not_used_as_bounded_relevance_reception_authority": bool(
            statement.get("hidden_repo_state_not_used_as_bounded_relevance_reception_authority")
        ),
        "repo_local_availability_not_bounded_relevance_reception_authority": bool(
            statement.get("repo_local_availability_not_bounded_relevance_reception_authority")
        ),
        "artifact_existence_not_bounded_relevance_reception_authority": bool(
            statement.get("artifact_existence_not_bounded_relevance_reception_authority")
        ),
        "latest_file_posture_not_bounded_relevance_reception_authority": bool(
            statement.get("latest_file_posture_not_bounded_relevance_reception_authority")
        ),
        "selected_basis_reference_shape_preserved": bool(statement.get("selected_basis_reference_shape_preserved")),
        "raw_full_prior_artifact_body_not_returned": bool(statement.get("raw_full_prior_artifact_body_not_returned")),
        "official_enum_scope_strings_not_redacted": bool(statement.get("official_enum_scope_strings_not_redacted")),
        "hostile_raw_body_content_contained": bool(statement.get("hostile_raw_body_content_contained")),
        "result_level_non_claims_canonical_false": bool(statement.get("result_level_non_claims_canonical_false")),
        "selected_runtime_loop_outcome": runtime_loop_outcome,
        "selected_runtime_loop_version": runtime_loop_version,
        "selected_runtime_loop_failed_check_count": runtime_loop_failed_check_count,
        "selected_runtime_layer_closure_basis": _sanitize(selected_runtime_layer_closure),
        "selected_bounded_relevance_reception_selection_basis": _sanitize(selected_selection),
        "bounded_relevance_signal_summary": _sanitize(result.get("bounded_relevance_signal")),
        "relevance_basis_summary": _sanitize(result.get("relevance_basis")),
        "relevance_scope_summary": _sanitize(result.get("relevance_scope")),
        "carrier_context_summary": _sanitize(result.get("relevance_signal_carrier_context")),
        "bounded_relevance_reception_envelope_summary": _sanitize(result.get("bounded_relevance_reception_envelope")),
        "no_relevance_receipt_source_authority_currentness_truth_action_synchronization_inhabitance_runtime_permission_api_interface_distributed_network_deployment_public_release_follow_on": True,
        "key_non_claims": _canonical_non_claims(),
        "predecessor_failure_evidence_preserved": bool(statement.get("predecessor_failure_evidence_preserved")),
        "consumed_request_token_remains_closed": bool(statement.get("consumed_request_token_remains_closed")),
        "authorization_token_reuse_blocked": bool(statement.get("authorization_token_reuse_blocked")),
    }
    return summary


def build_declared_bounded_relevance_reception_v0_min_request(
    *,
    bounded_relevance_reception_request_id: str = "bounded_relevance_reception_v0_min_reference_review_001",
    bounded_relevance_reception_question: str = CORE_QUESTION,
    bounded_relevance_reception_intent: str = INTENT_RECORD,
    bounded_relevance_signal: Mapping[str, Any] | None = None,
    relevance_basis: Mapping[str, Any] | None = None,
    relevance_scope: Mapping[str, Any] | None = None,
    relevance_signal_carrier_context: Mapping[str, Any] | None = None,
    bounded_relevance_reception_envelope: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared request for one bounded relevance reception posture."""

    signal = dict(
        bounded_relevance_signal
        or {
            "signal_id": "bounded_relevance_signal_001",
            "signal_kind": "medium_facing_reception_material",
            "declared": True,
            "source_created": False,
            "authority_created": False,
            "currentness_created": False,
            "truth_created": False,
            "action_created": False,
            "synchronization_created": False,
            "inhabitance_created": False,
            "runtime_permission_created": False,
            "public_api_created": False,
            "participant_facing_interface_created": False,
            "distributed_network_behavior_created": False,
        }
    )
    basis = dict(
        relevance_basis
        or {
            "basis_id": "bounded_relevance_basis_001",
            "basis_role": "declared_relevance_basis_only",
            "truth_created": False,
            "source_created": False,
            "authority_created": False,
            "currentness_created": False,
            "action_created": False,
            "permission_created": False,
        }
    )
    scope = dict(
        relevance_scope
        or {
            "scope_id": "bounded_relevance_scope_001",
            "bounded": True,
            "one_signal_only": True,
            "arbitrary_reception_authorized": False,
            "repeated_reception_authorized": False,
        }
    )
    carrier_context = dict(
        relevance_signal_carrier_context
        or {
            "context_id": "bounded_relevance_signal_carrier_context_001",
            "basis_role": "context_only",
            "authority_created": False,
            "currentness_created": False,
            "action_created": False,
            "synchronization_created": False,
            "runtime_permission_created": False,
            "public_api_created": False,
            "participant_facing_interface_created": False,
            "distributed_network_behavior_created": False,
        }
    )
    envelope = dict(
        bounded_relevance_reception_envelope
        or {
            "envelope_id": "bounded_relevance_reception_envelope_001",
            "declared": True,
            "one_bounded_relevance_signal_only": True,
            "authorize_arbitrary_reception": False,
            "authorize_repeated_reception": False,
            "authorize_source_receipt": False,
            "authorize_reception_authorization": False,
            "authorize_source": False,
            "authorize_authority": False,
            "authorize_currentness": False,
            "authorize_truth": False,
            "authorize_action": False,
            "authorize_synchronization": False,
            "authorize_inhabitance": False,
            "authorize_runtime_permission": False,
            "authorize_public_api": False,
            "authorize_participant_facing_interface": False,
            "authorize_distributed_network_behavior": False,
            "authorize_deployment": False,
            "authorize_public_release": False,
            "authorize_operation_permission": False,
            "authorize_broader_reusable_permission": False,
            "authorize_follow_on_work": False,
            "fresh_admission_required_outside_envelope": True,
        }
    )

    request: dict[str, Any] = {
        "bounded_relevance_reception_request_id": bounded_relevance_reception_request_id,
        "bounded_relevance_reception_question": bounded_relevance_reception_question,
        "bounded_relevance_reception_intent": bounded_relevance_reception_intent,
        **copy.deepcopy(REFERENCE_BASIS_DEFAULTS),
        "bounded_relevance_reception_spec_only_posture": {"declared": True},
        "one_bounded_relevance_reception_posture": {"declared": True},
        "bounded_relevance_signal": signal,
        "relevance_basis": basis,
        "relevance_scope": scope,
        "relevance_signal_carrier_context": carrier_context,
        "bounded_relevance_reception_envelope": envelope,
        "runtime_layer_closure_basis_preserved_posture": {"declared": True},
        "runtime_loop_basis_preserved_posture": {"declared": True},
        "bounded_runtime_loop_envelope_preserved_posture": {"declared": True},
        "carrier_aware_distributed_anatomy_basis_preserved_posture": {"declared": True},
        "bounded_relevance_reception_not_source_transfer_posture": {"declared": True},
        "bounded_relevance_reception_not_source_receipt_posture": {"declared": True},
        "bounded_relevance_reception_not_reception_authorization_posture": {"declared": True},
        "bounded_relevance_reception_not_source_posture": {"declared": True},
        "bounded_relevance_reception_not_authority_posture": {"declared": True},
        "bounded_relevance_reception_not_currentness_posture": {"declared": True},
        "bounded_relevance_reception_not_truth_posture": {"declared": True},
        "bounded_relevance_reception_not_action_posture": {"declared": True},
        "bounded_relevance_reception_not_synchronization_posture": {"declared": True},
        "bounded_relevance_reception_not_inhabitance_posture": {"declared": True},
        "bounded_relevance_reception_not_runtime_permission_posture": {"declared": True},
        "bounded_relevance_reception_not_public_api_posture": {"declared": True},
        "bounded_relevance_reception_not_participant_facing_interface_posture": {"declared": True},
        "bounded_relevance_reception_not_distributed_network_behavior_posture": {"declared": True},
        "source_transfer_not_created_posture": {"declared": True},
        "source_receipt_not_created_posture": {"declared": True},
        "reception_authorization_not_created_posture": {"declared": True},
        "source_not_created_posture": {"declared": True},
        "authority_not_created_posture": {"declared": True},
        "currentness_not_created_posture": {"declared": True},
        "truth_not_created_posture": {"declared": True},
        "action_not_created_posture": {"declared": True},
        "synchronization_not_created_posture": {"declared": True},
        "inhabitance_not_created_posture": {"declared": True},
        "runtime_permission_not_created_posture": {"declared": True},
        "public_api_not_created_posture": {"declared": True},
        "participant_facing_interface_not_created_posture": {"declared": True},
        "distributed_network_behavior_not_created_posture": {"declared": True},
        "deployment_not_created_posture": {"declared": True},
        "public_release_not_created_posture": {"declared": True},
        "operation_permission_not_created_posture": {"declared": True},
        "broader_reusable_permission_not_created_posture": {"declared": True},
        "follow_on_work_not_authorized_posture": {"declared": True},
        "hidden_repo_state_excluded_posture": {"declared": True},
        "repo_local_availability_not_bounded_relevance_reception_authority_posture": {"declared": True},
        "artifact_existence_not_bounded_relevance_reception_authority_posture": {"declared": True},
        "latest_file_posture_not_bounded_relevance_reception_authority_posture": {"declared": True},
        "selected_basis_reference_shape_posture": {"declared": True},
        "raw_full_prior_artifact_body_not_returned_posture": {"declared": True},
        "official_enum_scope_strings_not_redacted_posture": {"declared": True},
        "hostile_raw_body_content_contained_posture": {"declared": True},
        "predecessor_failure_evidence_preserved_posture": {"declared": True},
        "result_level_non_claims_canonical_false_posture": {"declared": True},
        "bounded_relevance_reception_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _canonical_non_claims(),
        "selected_bounded_relevance_reception_selection_path": "spec/POST_RUNTIME_LOOP_BOUNDED_RELEVANCE_RECEPTION_SELECTION_V0.md",
        "selected_bounded_relevance_reception_selection_states_selected_next_layer_pressure": True,
        "selected_bounded_relevance_reception_selection_already_created_reception": False,
        "selected_bounded_relevance_reception_selection_authorized_mechanism": False,
        "selected_runtime_layer_closure_path": "spec/POST_RUNTIME_LOOP_INTERNAL_RUNTIME_LAYER_CLOSURE_REVIEW_V0.md",
        "selected_runtime_layer_closure_recorded": True,
        "selected_runtime_layer_closure_closed_internal_runtime_stack": True,
        "selected_runtime_layer_closure_requires_next_layer_selection": True,
        "selected_runtime_layer_closure_selected_public_api": False,
        "selected_runtime_layer_closure_selected_participant_facing_interface": False,
        "selected_runtime_layer_closure_selected_distributed_network_behavior": False,
        "selected_runtime_layer_closure_selected_source_authority_currentness": False,
        "selected_runtime_layer_closure_selected_deployment_operation": False,
        "selected_runtime_layer_closure_authorized_follow_on_work": False,
        "selected_runtime_loop_result_path": "artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop",
        "selected_runtime_loop_result_outcome": "POST_RUNTIME_DAEMON_RUNTIME_LOOP_RECORDED",
        "selected_runtime_loop_result_version": RESULT_VERSION,
        "selected_runtime_loop_failed_check_count": 0,
        "selected_runtime_loop_bounded_posture_recorded": True,
        "selected_runtime_loop_bounded_runtime_loop_envelope_recorded": True,
        "selected_runtime_loop_already_created_public_api": False,
        "selected_runtime_loop_already_created_participant_facing_interface": False,
        "selected_runtime_loop_already_created_distributed_network_behavior": False,
        "selected_runtime_loop_already_created_source": False,
        "selected_runtime_loop_already_created_authority": False,
        "selected_runtime_loop_already_created_currentness": False,
        "selected_runtime_loop_already_created_deployment": False,
        "selected_runtime_loop_already_created_public_release": False,
        "selected_runtime_loop_already_created_operation_permission": False,
        "selected_runtime_loop_authorized_follow_on_work": False,
        "selected_runtime_loop_non_claims_canonicalized": True,
        "bounded_runtime_loop_envelope_treated_as_reception_authority": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_authority": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_action_authority": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_synchronization_authority": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_runtime_permission": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_public_api": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_participant_interface": False,
        "carrier_aware_distributed_anatomy_basis_treated_as_distributed_network": False,
        "bounded_relevance_signal_missing": False,
        "bounded_relevance_signal_treated_as_source": False,
        "bounded_relevance_signal_treated_as_authority": False,
        "bounded_relevance_signal_treated_as_currentness": False,
        "bounded_relevance_signal_treated_as_truth": False,
        "bounded_relevance_signal_treated_as_action": False,
        "bounded_relevance_signal_treated_as_synchronization": False,
        "bounded_relevance_signal_treated_as_inhabitance": False,
        "bounded_relevance_signal_treated_as_runtime_permission": False,
        "bounded_relevance_signal_treated_as_public_api": False,
        "bounded_relevance_signal_treated_as_participant_facing_interface": False,
        "bounded_relevance_signal_treated_as_distributed_network_behavior": False,
        "relevance_basis_missing": False,
        "relevance_basis_treated_as_truth": False,
        "relevance_basis_treated_as_authority": False,
        "relevance_scope_missing": False,
        "relevance_scope_unbounded": False,
        "bounded_relevance_reception_recorded_before_review": False,
        "relevance_receipt_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "action_created": False,
        "synchronization_created": False,
        "inhabitance_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "deployment_created": False,
        "public_release_created": False,
        "operation_permission_created": False,
        "broader_reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "adoption_created": False,
        "receiving_context_governance_created": False,
        "publication_flow_created": False,
        "follow_on_work_authorized": False,
        "reference_shaped_input_posture": True,
        "hidden_repo_state_used_as_bounded_relevance_reception_authority": False,
        "hidden_repo_state_used_as_bounded_relevance_reception_content": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
    }
    request.update(overrides)
    return request
