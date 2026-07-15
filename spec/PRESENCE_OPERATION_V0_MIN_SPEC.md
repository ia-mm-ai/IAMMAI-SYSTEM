# Presence Operation V0 Minimum Specification

## 1. Purpose

This specification defines only the shape of one future presence operation downstream of the completed presence boundary.

It permits a future presence operation to be specified and evaluated. It does not execute the operation, record an operation result, establish presence, support presence, authorize presence, or record presence.

The operation question is whether presence may be supported after boundary allowance. The required answer is that repo-local execution alone is insufficient and admissible receiver-side answerable basis is required.

## 2. Scope

This specification is additive, repo-local, operation-spec-only, and subordinate to constitutional and reference authority surfaces, current executable source, existing tests, emitted artifacts, and completed terminal summaries.

This specification does not:

- create or authorize identity;
- assign or create coupling;
- create FIELD machinery, runtime, API, currentness, authority, or standing;
- authorize output, action, derivative reception, synchronization, follow-on authorization, or follow-on work;
- dissolve, reverse, terminate, erase, mutate, or invalidate relation;
- punish relation lapse or create teardown logic or living relation state;
- preserve historical receipt;
- admit a third candidate or third model;
- create standing descendants or perform descendant-standing checks;
- scan the repository, discover files, repair the affected file, or validate prior unsupported claims;
- override or bypass any upstream completed line; or
- authorize any downstream route by itself.

## 3. Operation Question

Given that the completed presence boundary recorded `PRESENCE_BOUNDARY_ALLOWED` and `PRESENCE_OPERATION_CONSIDERATION_ALLOWED`, while preserving that presence boundary is not presence operation, boundary permission is not presence, and presence operation consideration is not presence, identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work, may a future presence operation record `PRESENCE_SUPPORTED` by repo-local execution alone?

## 4. Required Answer

No.

Presence operation may be specified and evaluated. Presence support may not be recorded from repo-local execution alone, operator-only attestation, derivative rendering, or same-custody countersignature.

Presence support requires receiver-side answerable basis that is custody-distinct from the declaring side, not controlled by the declaring side, refusable, and capable of being withheld. An answerable basis that could not have been withheld is not an answer.

A future resolver may record `PRESENCE_SUPPORTED` only if admissible receiver-side answerable basis is supplied. Until then, it must record `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION`, not `PRESENCE_SUPPORTED`, unless the request is otherwise prohibited and must be blocked.

`PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION` is not failure and is not blocked. It is the lawful waiting state for missing receiver-side answerable basis.

Presence is receiver-allocated. It cannot be emitted as self-proof, inherited from `relation_001`, inherited from relation lapse, or derived from historical relation record. Presence must be recorded, if ever supported, as a fresh answerable event.

## 5. Operation Identifiers

Required operation identifiers:

- `presence_operation_id = presence_operation_001`
- `presence_operation_type = PRESENCE_OPERATION`
- `presence_operation_version = 0.1.0`
- `presence_operation_scope = EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_RECEIVER_ATTESTATION_REQUIREMENT_ONLY`
- `prior_presence_boundary_type = PRESENCE_BOUNDARY`
- `prior_presence_boundary_outcome_required = PRESENCE_BOUNDARY_ALLOWED`
- `prior_presence_boundary_result_required = PRESENCE_OPERATION_CONSIDERATION_ALLOWED`
- `prior_presence_operation_consideration_allowed_required = true`
- `prior_relation_lapse_operation_referenced_required = true`
- `prior_relation_record_referenced_required = true`
- `prior_relation_basis_referenced_required = true`
- `prior_presence_supported_required = false`
- `prior_presence_authorized_required = false`
- `prior_presence_established_required = false`
- `prior_presence_recorded_required = false`
- `prior_identity_created_required = false`
- `prior_identity_authorized_required = false`
- `prior_coupling_created_required = false`
- `prior_field_machinery_created_required = false`
- `prior_runtime_created_required = false`
- `prior_api_created_required = false`
- `prior_currentness_created_required = false`
- `prior_authority_created_required = false`
- `prior_standing_created_required = false`
- `prior_output_authorized_required = false`
- `prior_action_authorized_required = false`
- `prior_derivative_reception_authorized_required = false`
- `prior_synchronization_authorized_required = false`
- `prior_follow_on_authorized_required = false`
- `prior_follow_on_work_authorized_required = false`
- `prior_relation_dissolution_authorized_required = false`
- `prior_relation_dissolution_performed_required = false`
- `prior_relation_reversed_required = false`
- `prior_relation_terminated_required = false`
- `prior_relation_erased_required = false`
- `prior_relation_mutated_required = false`
- `prior_relation_invalidated_required = false`
- `prior_relation_punished_required = false`
- `prior_relation_teardown_created_required = false`
- `prior_living_relation_state_created_required = false`
- `prior_living_relation_state_lapsed_required = false`
- `prior_living_relation_state_dissolved_required = false`
- `prior_historical_receipt_preservation_authorized_required = false`
- `prior_historical_receipt_preserved_required = false`
- `prior_third_candidate_created_required = false`
- `prior_third_model_admitted_required = false`
- `prior_standing_descendant_created_required = false`
- `prior_descendant_standing_check_performed_required = false`
- `admissible_future_route = PRESENCE_OPERATION_WITH_RECEIVER_ATTESTATION_THEN_IDENTITY_OR_COUPLING_BOUNDARY_CONSIDERATION_ONLY`

Relation and presence basis identifiers:

- `relation_id = relation_001`
- `relation_pair_scope = RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY`
- `relation_lapse_id = relation_lapse_001`
- `relation_lapse_scope = RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY`
- `first_crossing_a_id = first_crossing_a_001`
- `first_crossing_b_id = first_crossing_b_001`
- `first_crossing_pair_scope = SEPARATE_FIRST_CROSSING_RECORDS_ONLY`
- `descendant_body_a_id = descendant_body_a_001`
- `descendant_body_b_id = descendant_body_b_001`
- `descendant_body_pair_scope = SEPARATE_DESCENDANT_BODY_RECORDS_ONLY`
- `candidate_a_standing_source_id = descendant_body_basis_candidate_a_001`
- `candidate_b_standing_source_id = descendant_body_basis_candidate_b_001`
- `candidate_a_role = CANDIDATE_A`
- `candidate_b_role = CANDIDATE_B`
- `candidate_a_standing_label = CANDIDATE_A_STANDING`
- `candidate_b_standing_label = CANDIDATE_B_STANDING`
- `presence_id = presence_001`
- `presence_scope = PRESENCE_AFTER_RELATION_LAPSE_WITH_RECEIVER_ATTESTATION_ONLY`
- supported result identifier: `presence_result = PRESENCE_SUPPORTED`

## 6. Receiver-Side Answerable Basis Requirement

Receiver-side answerable basis identifiers and initial posture:

- `receiver_answerable_basis_id = receiver_answerable_basis_001`
- `receiver_answerable_basis_type = RECEIVER_SIDE_ANSWERABLE_BASIS`
- `receiver_answerable_basis_scope = CUSTODY_DISTINCT_REFUSABLE_RECEIVER_ATTESTATION_OR_EXTERNAL_ANSWERABLE_RECEIPT_ONLY`
- `receiver_attested = false`
- `receiver_answerable_receipt_present = false`
- `receiver_answerable_basis_custody_distinct = false`
- `receiver_answerable_basis_controlled_by_declaring_side = false`
- `receiver_answerable_basis_refusable = false`
- `receiver_answerable_basis_could_have_been_withheld = false`
- `operator_only_attestation = false`
- `derivative_rendering_attestation = false`
- `same_custody_countersignature = false`
- `automatic_acknowledgement = false`
- `generated_affirmation = false`
- `repo_local_execution_only = true`
- `receiver_attestation_required = true`

Receiver-side answerable basis must be custody-distinct from the declaring side, must not be controlled by the declaring side, must have refusability, and must have been capable of being withheld.

The following are not receiver-side answerable basis:

- automatic acknowledgement;
- generated affirmation;
- same-hand signature;
- same-custody signature or countersignature;
- derivative rendering of reception;
- repo-local artifact;
- operator-only attestation; or
- any answer controlled by the declaring side or incapable of being withheld.

## 7. Future Operation Admissibility

A future presence operation may evaluate only if all required boundary allowance inputs are supplied:

- completed presence boundary terminal summary records `PRESENCE_BOUNDARY_ALLOWED`;
- completed presence boundary terminal summary records `PRESENCE_OPERATION_CONSIDERATION_ALLOWED`;
- completed presence boundary terminal summary records `presence_operation_consideration_allowed = true`;
- completed presence boundary terminal summary records `relation_lapse_operation_referenced = true`;
- completed presence boundary terminal summary records `relation_record_referenced = true`;
- completed presence boundary terminal summary records `relation_basis_referenced = true`;
- completed presence boundary terminal summary records presence boundary is not presence operation;
- completed presence boundary terminal summary records presence boundary permission is not presence;
- completed presence boundary terminal summary records presence operation consideration is not presence;
- completed presence boundary terminal summary records presence operation consideration is not identity;
- completed presence boundary terminal summary records presence operation consideration is not coupling;
- completed presence boundary terminal summary records presence operation consideration is not FIELD machinery;
- completed presence boundary terminal summary records presence operation consideration is not runtime;
- completed presence boundary terminal summary records presence operation consideration is not API;
- completed presence boundary terminal summary records presence operation consideration is not currentness;
- completed presence boundary terminal summary records presence operation consideration is not authority;
- completed presence boundary terminal summary records presence operation consideration is not standing;
- completed presence boundary terminal summary records presence operation consideration is not output authorization;
- completed presence boundary terminal summary records presence operation consideration is not action authorization;
- completed presence boundary terminal summary records presence operation consideration is not derivative reception;
- completed presence boundary terminal summary records presence operation consideration is not synchronization;
- completed presence boundary terminal summary records presence operation consideration is not follow-on authorization;
- completed presence boundary terminal summary records presence operation consideration is not follow-on work;
- completed presence boundary terminal summary records presence was not supported;
- completed presence boundary terminal summary records presence was not authorized;
- completed presence boundary terminal summary records presence was not established;
- completed presence boundary terminal summary records presence was not recorded;
- completed presence boundary terminal summary records identity was not created;
- completed presence boundary terminal summary records identity was not authorized;
- completed presence boundary terminal summary records coupling remains unassigned;
- completed presence boundary terminal summary records coupling was not created;
- completed presence boundary terminal summary records relation record was confirmed historical-only;
- completed presence boundary terminal summary records historical relation record is not living relation state;
- completed presence boundary terminal summary records historical relation record is not presence;
- completed presence boundary terminal summary records historical relation record is not identity;
- completed presence boundary terminal summary records historical relation record is not coupling;
- completed presence boundary terminal summary records `relation_001` does not become landlord of the between;
- completed presence boundary terminal summary records `relation_001` does not outrank First Crossing A;
- completed presence boundary terminal summary records `relation_001` does not outrank First Crossing B;
- completed presence boundary terminal summary records `relation_001` does not outrank the related first-crossing pair; and
- completed presence boundary terminal summary records follow-on work is not authorized.

If boundary allowance is present but receiver-side answerable basis is missing or insufficient, a future operation may record `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION`.

A future operation may record `PRESENCE_SUPPORTED` only when all of these inputs are supplied:

- `receiver_attested = true`
- `receiver_answerable_receipt_present = true`
- `receiver_answerable_basis_custody_distinct = true`
- `receiver_answerable_basis_controlled_by_declaring_side = false`
- `receiver_answerable_basis_refusable = true`
- `receiver_answerable_basis_could_have_been_withheld = true`
- `repo_local_execution_only = false`
- `operator_only_attestation = false`
- `derivative_rendering_attestation = false`
- `same_custody_countersignature = false`
- `automatic_acknowledgement = false`
- `generated_affirmation = false`
- `forged_receiver_attestation = false`
- `inadmissible_receiver_basis = false`

If any receiver-side answerable basis requirement is missing or insufficient, the future operation must return `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION`, not `PRESENCE_SUPPORTED`, unless the request is otherwise prohibited and must return `PRESENCE_OPERATION_BLOCKED`.

A request must be blocked if it converts the operation into presence as identity, coupling assignment, coupling creation, FIELD machinery, runtime, API, currentness, authority, standing, output, action, derivative reception, synchronization, follow-on authorization, follow-on work, relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punitive interpretation, teardown logic, living relation state creation, historical receipt preservation, third candidate, third model, standing descendant creation, descendant standing, repair, scan, discovery, validation enforcement, or any downstream route.

## 8. Permitted Future Operation Result

A future presence operation may return exactly one of three outcomes:

- `PRESENCE_OPERATION_SUPPORTED`
- `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION`
- `PRESENCE_OPERATION_BLOCKED`

If all boundary admissibility and receiver-side answerable basis requirements are satisfied, `PRESENCE_OPERATION_SUPPORTED` may record:

- `presence_operation_recorded = true`
- `presence_evaluation_performed = true`
- `presence_result_recorded = true`
- `presence_result = PRESENCE_SUPPORTED`
- `presence_supported = true`
- `presence_authorized = true`
- `presence_established = true`
- `presence_recorded = true`
- `receiver_attested = true`
- `receiver_answerable_receipt_present = true`
- `receiver_answerable_basis_custody_distinct = true`
- `receiver_answerable_basis_controlled_by_declaring_side = false`
- `receiver_answerable_basis_refusable = true`
- `receiver_answerable_basis_could_have_been_withheld = true`
- `repo_local_execution_only = false`
- `operator_only_attestation = false`
- `derivative_rendering_attestation = false`
- `same_custody_countersignature = false`
- `automatic_acknowledgement = false`
- `generated_affirmation = false`
- `forged_receiver_attestation = false`
- `inadmissible_receiver_basis = false`

Even when `PRESENCE_SUPPORTED` is recorded, every presence-is-not, identity, coupling, downstream authorization, relation, historical-receipt, third-candidate, third-model, standing-descendant, and descendant-standing posture enumerated as false in Section 18 must remain false. Presence support is still not identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work.

If boundary allowance is present but receiver-side answerable basis is missing or insufficient, `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION` may record:

- `presence_result = REQUIRES_RECEIVER_ATTESTATION`
- `presence_supported = false`
- `presence_authorized = false`
- `presence_established = false`
- `presence_recorded = false`
- `presence_operation_requires_receiver_attestation = true`
- `receiver_attestation_required = true`
- `missing_or_insufficient_receiver_answerable_basis = non-empty`

This waiting outcome is not failure, not blocked, and not support.

`PRESENCE_OPERATION_BLOCKED` is required for any prohibited conversion or route in Sections 7 and 17. The word `BLOCKED` in the permitted route means the `PRESENCE_OPERATION_BLOCKED` outcome; it is not a fourth outcome.

## 9. Required Invariants

- Presence operation is not self-satisfying.
- Presence support cannot be recorded from repo-local execution alone.
- Presence support cannot be recorded from operator-only attestation.
- Presence support cannot be recorded from derivative rendering.
- Presence support cannot be recorded from same-custody countersignature.
- Presence support cannot be recorded from automatic acknowledgement.
- Presence support cannot be recorded from generated affirmation.
- Presence support requires receiver-side answerable basis.
- Receiver-side answerable basis must be custody-distinct from the declaring side.
- Receiver-side answerable basis must not be controlled by the declaring side.
- Receiver-side answerable basis must have refusability.
- Receiver-side answerable basis must have been capable of being withheld.
- An answerable basis that could not have been withheld is not an answer.
- Presence is receiver-allocated.
- Presence cannot be emitted as self-proof.
- Presence cannot be inherited from `relation_001`.
- Presence cannot be inherited from relation lapse.
- Presence cannot be derived from historical relation record.
- Presence must be recorded, if ever supported, as a fresh answerable event.
- Presence is not identity.
- Presence is not coupling.
- Presence is not FIELD machinery.
- Presence is not runtime.
- Presence is not API.
- Presence is not currentness.
- Presence is not authority.
- Presence is not standing.
- Presence is not output authorization.
- Presence is not action authorization.
- Presence is not derivative reception.
- Presence is not synchronization.
- Presence is not follow-on authorization.
- Presence is not follow-on work.
- Historical relation record is not presence.
- Historical relation record is not identity.
- Historical relation record is not coupling.
- `relation_001` must not become landlord of the between.
- `relation_001` must not outrank First Crossing A.
- `relation_001` must not outrank First Crossing B.
- `relation_001` must not outrank the related first-crossing pair.
- Coupling remains unassigned unless separately bounded.
- Coupling must not be treated as third candidate.
- Coupling must not be treated as third model.
- No third candidate is admitted.
- No third model is admitted.
- Identity requires a separately bounded operation.
- Coupling requires a separately bounded operation.
- FIELD machinery requires a separately bounded operation.
- Runtime requires a separately bounded operation.
- API requires a separately bounded operation.
- Currentness requires a separately bounded operation.
- Authority requires a separately bounded operation.
- Standing requires a separately bounded operation.
- No orphaned state is authorized.
- No silent reset is authorized.
- No overwrite is authorized.
- Contaminated lineage remains preserved.

## 10. Relation to Completed Presence Boundary

`spec/PRESENCE_BOUNDARY_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the presence boundary line and is treated as standing because it is present and clean.

The completed presence boundary recorded:

- `outcome = PRESENCE_BOUNDARY_ALLOWED`
- `failed_check_count = 0`
- `passed_check_count = 381`
- `result_version = 0.1.0`
- `presence_boundary_result = PRESENCE_OPERATION_CONSIDERATION_ALLOWED`
- `presence_operation_consideration_allowed = true`
- `relation_lapse_operation_referenced = true`
- `relation_record_referenced = true`
- `relation_basis_referenced = true`
- `presence_supported = false`
- `presence_authorized = false`
- `presence_established = false`
- `presence_recorded = false`
- `identity_created = false`
- `identity_authorized = false`
- `coupling_created = false`
- `field_machinery_created = false`
- `runtime_created = false`
- `api_created = false`
- `currentness_created = false`
- `authority_created = false`
- `standing_created = false`
- `output_authorized = false`
- `action_authorized = false`
- `derivative_reception_authorized = false`
- `synchronization_authorized = false`
- `follow_on_authorized = false`
- `follow_on_work_authorized = false`

This operation specification is downstream of that completed boundary. It does not reopen, change, repair, patch, invalidate, erase, or mutate the presence boundary result.

## 11. Relation to Completed Relation Lapse Operation

`spec/RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the relation lapse operation line.

The completed relation lapse operation recorded `RELATION_LAPSE_OPERATION_RECORDED`, `RELATION_LAPSE_SUPPORTED`, and `relation_001` as historical relation record only.

This operation specification does not reopen, change, repair, patch, invalidate, erase, or mutate the relation lapse operation result.

## 12. Relation to Completed Relation Lapse Boundary

`spec/RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the relation lapse boundary line.

The completed relation lapse boundary recorded `RELATION_LAPSE_BOUNDARY_ALLOWED` and `RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED`.

This operation specification does not reopen, change, repair, patch, invalidate, erase, or mutate the relation lapse boundary result.

## 13. Relation to Completed Relation Reversibility Operation

`spec/RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the relation reversibility operation line.

The completed relation reversibility operation recorded `RELATION_REVERSIBILITY_OPERATION_RECORDED`, `RELATION_REVERSIBILITY_SUPPORTED`, and `relation_001` as historical relation record only.

This operation specification does not reopen, change, repair, patch, invalidate, erase, or mutate the relation reversibility operation result.

## 14. Relation to Completed Relation Operation

`spec/RELATION_OPERATION_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the relation operation line.

The completed relation operation recorded `RELATION_OPERATION_RECORDED`, `RELATION_SUPPORTED`, and relation as one relation record between separate first-crossing records only.

This operation specification does not reopen, change, repair, patch, invalidate, erase, or mutate the relation operation result.

## 15. Relation to Completed First-Crossing Operation V2

`spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the first-crossing operation v2 line.

The completed first-crossing operation v2 recorded `FIRST_CROSSING_SUPPORTED` and First Crossing A and First Crossing B as first-crossing records only.

This operation specification does not reopen or change first-crossing operation v2.

## 16. Permitted Future Route

Exactly one future route is permitted:

1. A future presence operation resolver may evaluate the completed presence boundary terminal summary.
2. A future operation artifact may record `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION` if boundary allowance is present but admissible receiver-side answerable basis is missing or insufficient.
3. A future operation artifact may record `PRESENCE_SUPPORTED` only if admissible receiver-side answerable basis is supplied and all custody, control, refusability, and could-have-been-withheld checks pass.
4. A future operation artifact must record `BLOCKED` if operation is converted into identity creation, coupling assignment, coupling creation, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punitive interpretation, teardown logic, living relation state creation, historical receipt preservation, third candidate, third model, standing descendant creation, descendant standing, follow-on authorization, follow-on work, repair, scan, discovery, validation enforcement, or forged receiver attestation acceptance.
5. Only after a future presence operation records `PRESENCE_SUPPORTED` with admissible receiver-side answerable basis may a separately bounded identity boundary, coupling boundary, or later boundary be considered.
6. No identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output, action, derivative reception, synchronization, or later operation is authorized by this operation specification alone.

## 17. Blocked Routes

The future operation must explicitly block:

- direct presence operation spec to `PRESENCE_SUPPORTED`;
- repo-local execution to `PRESENCE_SUPPORTED`;
- operator-only attestation to `PRESENCE_SUPPORTED`;
- derivative rendering attestation to `PRESENCE_SUPPORTED`;
- same-custody countersignature to `PRESENCE_SUPPORTED`;
- automatic acknowledgement to `PRESENCE_SUPPORTED`;
- generated affirmation to `PRESENCE_SUPPORTED`;
- forged receiver attestation to `PRESENCE_SUPPORTED`;
- non-refusable answer to `PRESENCE_SUPPORTED`;
- answer that could not have been withheld to `PRESENCE_SUPPORTED`;
- declaring-side-controlled receiver basis to `PRESENCE_SUPPORTED`;
- direct presence boundary to presence support;
- direct relation lapse operation to presence support;
- direct historical relation record to presence support;
- direct `relation_001` to presence support;
- direct presence operation to identity;
- direct presence operation to coupling assignment;
- direct presence operation to coupling creation;
- direct presence operation to FIELD machinery;
- direct presence operation to runtime;
- direct presence operation to API;
- direct presence operation to authority/currentness;
- direct presence operation to standing;
- direct presence operation to output authorization;
- direct presence operation to action authorization;
- direct presence operation to derivative reception;
- direct presence operation to synchronization;
- direct presence operation to follow-on work;
- direct presence operation to relation dissolution;
- direct presence operation to relation reversal;
- direct presence operation to relation termination;
- direct presence operation to relation erasure;
- direct presence operation to relation mutation;
- direct presence operation to relation invalidation;
- direct presence operation to punitive interpretation;
- direct presence operation to teardown logic;
- direct presence operation to living relation state;
- direct presence operation to historical receipt preservation;
- repository scan route;
- file discovery route;
- affected-file repair route; and
- prior unsupported-claim validation route.

## 18. Preserved Non-Claims

Default operation posture before future evaluation:

- `presence_operation_recorded = false`
- `presence_evaluation_performed = false`
- `presence_result_recorded = false`
- `presence_result = NOT_EVALUATED`
- `presence_operation_requires_receiver_attestation = true`
- `receiver_attestation_required = true`
- `repo_local_execution_only = true`

The following remain false in this specification:

- `presence_supported = false`
- `presence_authorized = false`
- `presence_established = false`
- `presence_recorded = false`
- `receiver_attested = false`
- `receiver_answerable_receipt_present = false`
- `receiver_answerable_basis_custody_distinct = false`
- `receiver_answerable_basis_controlled_by_declaring_side = false`
- `receiver_answerable_basis_refusable = false`
- `receiver_answerable_basis_could_have_been_withheld = false`
- `operator_only_attestation = false`
- `derivative_rendering_attestation = false`
- `same_custody_countersignature = false`
- `automatic_acknowledgement = false`
- `generated_affirmation = false`
- `forged_receiver_attestation = false`
- `inadmissible_receiver_basis = false`
- `presence_is_identity = false`
- `presence_is_coupling = false`
- `presence_is_field_machinery = false`
- `presence_is_runtime = false`
- `presence_is_api = false`
- `presence_is_currentness = false`
- `presence_is_authority = false`
- `presence_is_standing = false`
- `presence_is_output_authorization = false`
- `presence_is_action_authorization = false`
- `presence_is_derivative_reception = false`
- `presence_is_synchronization = false`
- `presence_is_follow_on_authorization = false`
- `presence_is_follow_on_work = false`
- `identity_created = false`
- `identity_authorized = false`
- `coupling_assigned_to_relation = false`
- `coupling_assigned_to_first_crossing_a = false`
- `coupling_assigned_to_first_crossing_b = false`
- `coupling_assigned_to_descendant_body_a = false`
- `coupling_assigned_to_descendant_body_b = false`
- `coupling_assigned_to_candidate_a = false`
- `coupling_assigned_to_candidate_b = false`
- `coupling_created = false`
- `field_machinery_created = false`
- `runtime_created = false`
- `api_created = false`
- `currentness_created = false`
- `authority_created = false`
- `standing_created = false`
- `output_authorized = false`
- `action_authorized = false`
- `derivative_reception_authorized = false`
- `synchronization_authorized = false`
- `follow_on_authorized = false`
- `follow_on_work_authorized = false`
- `relation_dissolution_authorized = false`
- `relation_dissolution_performed = false`
- `relation_reversed = false`
- `relation_terminated = false`
- `relation_erased = false`
- `relation_mutated = false`
- `relation_invalidated = false`
- `relation_punished = false`
- `relation_teardown_created = false`
- `living_relation_state_created = false`
- `living_relation_state_lapsed = false`
- `living_relation_state_dissolved = false`
- `historical_receipt_preservation_authorized = false`
- `historical_receipt_preserved = false`
- `third_candidate_created = false`
- `third_model_admitted = false`
- `standing_descendant_created = false`
- `descendant_standing_check_performed = false`
- `prior_unsupported_candidate_a_claim_validated = false`
- `prior_unsupported_candidate_b_claim_validated = false`
- `prior_unsupported_derivation_event_claim_validated = false`
- `valid_derivation_event_recorded = false`
- `affected_file_repaired = false`
- `affected_file_edited = false`
- `affected_file_deleted = false`
- `affected_file_overwritten = false`
- `affected_file_replaced = false`
- `affected_file_redeemed = false`
- `affected_file_treated_as_clean_basis = false`
- `contaminated_lineage_treated_as_clean_basis = false`
- `presence_boundary_overridden = false`
- `presence_boundary_bypassed = false`
- `presence_boundary_invalidated = false`
- `relation_lapse_operation_overridden = false`
- `relation_lapse_operation_bypassed = false`
- `relation_lapse_operation_invalidated = false`
- `relation_operation_overridden = false`
- `relation_operation_bypassed = false`
- `relation_operation_invalidated = false`
- `relation_record_erased = false`
- `relation_record_mutated = false`
- `scan_performed = false`
- `repository_scan_performed = false`
- `file_discovery_performed = false`
- `repair_performed = false`
- `validation_enforced = false`
- `hidden_repair_performed = false`
- `silent_overwrite_performed = false`
- `direct_presence_operation_spec_to_presence_supported = false`
- `repo_local_execution_to_presence_supported = false`
- `operator_only_attestation_to_presence_supported = false`
- `derivative_rendering_attestation_to_presence_supported = false`
- `same_custody_countersignature_to_presence_supported = false`
- `automatic_acknowledgement_to_presence_supported = false`
- `generated_affirmation_to_presence_supported = false`
- `forged_receiver_attestation_to_presence_supported = false`
- `non_refusable_answer_to_presence_supported = false`
- `answer_that_could_not_have_been_withheld_to_presence_supported = false`
- `declaring_side_controlled_receiver_basis_to_presence_supported = false`
- `direct_presence_boundary_to_presence_support = false`
- `direct_relation_lapse_operation_to_presence_support = false`
- `direct_historical_relation_record_to_presence_support = false`
- `direct_relation_001_to_presence_support = false`
- `direct_presence_operation_to_identity = false`
- `direct_presence_operation_to_coupling_assignment = false`
- `direct_presence_operation_to_coupling_creation = false`
- `direct_presence_operation_to_field_machinery = false`
- `direct_presence_operation_to_runtime = false`
- `direct_presence_operation_to_api = false`
- `direct_presence_operation_to_authority_currentness = false`
- `direct_presence_operation_to_standing = false`
- `direct_presence_operation_to_output_authorization = false`
- `direct_presence_operation_to_action_authorization = false`
- `direct_presence_operation_to_derivative_reception = false`
- `direct_presence_operation_to_synchronization = false`
- `direct_presence_operation_to_follow_on_work = false`
- `direct_presence_operation_to_relation_dissolution = false`
- `direct_presence_operation_to_relation_reversal = false`
- `direct_presence_operation_to_relation_termination = false`
- `direct_presence_operation_to_relation_erasure = false`
- `direct_presence_operation_to_relation_mutation = false`
- `direct_presence_operation_to_relation_invalidation = false`
- `direct_presence_operation_to_punitive_interpretation = false`
- `direct_presence_operation_to_teardown_logic = false`
- `direct_presence_operation_to_living_relation_state = false`
- `direct_presence_operation_to_historical_receipt_preservation = false`

No false non-claim is listed as true.

## 19. Relation to Contaminated Lineage

`spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage for the unsupported existence-claim class.

Prior unsupported claims include:

- `descendant_body_basis_candidate_a_created = true`
- `descendant_body_basis_candidate_b_created = true`
- `descendant_body_basis_derivation_event_recorded = true`

The existence-claim evidence check mechanically recorded those claims as `UNSUPPORTED`.

This operation specification does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file.

This operation specification does not treat the affected file as evidence for candidate creation, candidate distinctness, candidate scope, scope division, candidate-specific content, seal material, lineage receipt material, digest material, standing, descendant-body creation, first crossing, relation, reversibility, lapse, presence, identity, coupling, FIELD machinery, or clean basis.

## 20. What Remains Open

- presence operation resolver
- presence operation test
- presence operation live artifact
- actual presence operation
- receiver-side answerable basis, if separately supplied
- receiver-side answerable basis custody check
- receiver-side answerable basis refusability check
- receiver-side answerable basis could-have-been-withheld check
- identity boundary, if separately bounded
- coupling boundary, if separately bounded
- relation dissolution boundary, if separately bounded
- relation dissolution operation, if separately bounded
- FIELD machinery
- runtime
- API
- currentness
- authority
- standing
- output authorization
- action authorization
- derivative reception
- synchronization
- externalization boundary
- follow-on work

Open means not scheduled, not authorized, and not executed.

## 21. Closing Lock

This operation spec defines only a future presence operation shape downstream of the completed presence boundary. It does not itself execute presence or record an operation result. Presence operation is not self-satisfying. Presence support cannot be recorded from repo-local execution alone, operator-only attestation, derivative rendering, same-custody countersignature, automatic acknowledgement, generated affirmation, or any answerable basis controlled by the declaring side. Presence support requires receiver-side answerable basis that is custody-distinct, not controlled by the declaring side, refusable, and capable of being withheld. An answerable basis that could not have been withheld is not an answer. Until admissible receiver-side answerable basis is supplied, a future presence operation must record PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION rather than PRESENCE_SUPPORTED, unless the request is otherwise prohibited and must be blocked. PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION is not failure, not blocked, and not support. It is the lawful waiting state for missing receiver-side answerable basis. Presence is receiver-allocated and cannot be emitted as self-proof, inherited from relation_001, inherited from relation lapse, or derived from historical relation record. Presence must be recorded, if ever supported, as a fresh answerable event. Even if PRESENCE_SUPPORTED is later recorded with admissible receiver-side answerable basis, presence is not identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work. This operation spec does not create identity, assign coupling, create coupling, create FIELD machinery, create runtime, create API, create currentness, create authority, create standing, authorize output, authorize action, authorize derivative reception, authorize synchronization, authorize follow-on work, dissolve relation, reverse relation, terminate relation, erase relation, mutate relation_001, invalidate relation, punish relation lapse, create teardown logic, create living relation state, preserve historical receipt, admit a third candidate, admit a third model, create standing descendants, perform descendant-standing checks, repair the affected file, validate prior unsupported claims, scan repository, discover files, enforce validation, or authorize follow-on work. Only after a future presence operation records PRESENCE_SUPPORTED with admissible receiver-side answerable basis may a separately bounded identity boundary, coupling boundary, or later boundary be considered. Open means not scheduled, not authorized, and not executed.
