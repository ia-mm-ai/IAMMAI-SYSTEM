# Relation Operation V0 Minimum Specification

## 1. Purpose

This specification defines one future relation-operation shape downstream of the completed relation boundary. It asks only whether First Crossing A and First Crossing B may later be evaluated for relation without converting that evaluation into FIELD machinery, runtime, currentness, authority, coupling, presence, identity, standing, or follow-on work.

It does not authorize relation, create relation, perform relation operation, create FIELD machinery, runtime, API, currentness, authority, standing descendants, or descendant-standing checks; assign or create coupling; admit a third candidate or model; establish presence or identity; authorize output, action, derivative reception, synchronization, follow-on authorization, or follow-on work; scan or discover files; repair the affected file; validate prior unsupported claims; or override or bypass an upstream completed line.

## 2. Scope

This is operation-spec-only. It records no operation result, relation record, relation authorization, relation creation, or relation performance. First crossing remains prior basis only until a separately bounded future operation evaluates relation.

```text
relation_operation_recorded = false
relation_evaluation_performed = false
relation_result_recorded = false
relation_result = NOT_EVALUATED
relation_supported = false
relation_authorized = false
relation_created = false
relation_operation_performed = false
relation_recorded = false
first_crossing_a_used_as_relation_basis = false
first_crossing_b_used_as_relation_basis = false
first_crossing_pair_used_as_relation_basis = false
```

All conversion and downstream posture remains false under section 16.

## 3. Operation Question

Given that the relation boundary recorded `RELATION_OPERATION_CONSIDERATION_ALLOWED` after first-crossing support, while preserving that relation boundary permission is not relation creation, relation operation consideration is not relation, relation was not authorized, relation was not created, relation operation was not performed, coupling was not assigned or created, presence was not established, identity was not created, and follow-on was not authorized, may the system define one future relation operation that evaluates whether First Crossing A and First Crossing B may record relation without creating FIELD machinery, runtime, currentness, authority, coupling, presence, identity, or follow-on work?

## 4. Required Answer

Yes, but only as a relation operation specification. No relation is authorized, created, or performed here. No coupling is assigned, no presence is established, and no identity is created.

## 5. Operation Identifiers

```text
relation_operation_id = relation_operation_001
relation_operation_type = RELATION_OPERATION
relation_operation_version = 0.1.0
relation_operation_scope = EVALUATE_RELATION_AFTER_BOUNDARY_ALLOWANCE_ONLY
prior_relation_boundary_type = RELATION_BOUNDARY
prior_relation_boundary_outcome_required = RELATION_BOUNDARY_ALLOWED
prior_relation_boundary_result_required = RELATION_OPERATION_CONSIDERATION_ALLOWED
prior_relation_operation_consideration_allowed_required = true
prior_first_crossing_operation_referenced_required = true
prior_first_crossing_a_referenced_required = true
prior_first_crossing_b_referenced_required = true
prior_first_crossing_pair_referenced_required = true
prior_relation_authorized_required = false
prior_relation_created_required = false
prior_relation_operation_performed_required = false
prior_coupling_created_required = false
prior_presence_established_required = false
prior_identity_created_required = false
prior_follow_on_authorized_required = false
prior_follow_on_work_authorized_required = false
admissible_future_route = RELATION_OPERATION_THEN_PRESENCE_BOUNDARY_ONLY

first_crossing_a_id = first_crossing_a_001
first_crossing_b_id = first_crossing_b_001
first_crossing_pair_scope = SEPARATE_FIRST_CROSSING_RECORDS_ONLY
descendant_body_a_id = descendant_body_a_001
descendant_body_b_id = descendant_body_b_001
descendant_body_pair_scope = SEPARATE_DESCENDANT_BODY_RECORDS_ONLY
candidate_a_standing_source_id = descendant_body_basis_candidate_a_001
candidate_b_standing_source_id = descendant_body_basis_candidate_b_001
candidate_a_role = CANDIDATE_A
candidate_b_role = CANDIDATE_B
candidate_a_standing_label = CANDIDATE_A_STANDING
candidate_b_standing_label = CANDIDATE_B_STANDING

relation_id = relation_001
relation_pair_scope = RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY
```

## 6. Future Operation Admissibility

A future relation operation may evaluate relation only when all required inputs are supplied:

- The completed relation boundary terminal summary records `RELATION_BOUNDARY_ALLOWED`, `RELATION_OPERATION_CONSIDERATION_ALLOWED`, `relation_operation_consideration_allowed = true`, `first_crossing_operation_referenced = true`, `first_crossing_a_referenced = true`, `first_crossing_b_referenced = true`, and `first_crossing_pair_referenced = true`.
- That boundary preserves `relation_authorized = false`, `relation_created = false`, `relation_operation_performed = false`, `coupling_created = false`, `presence_established = false`, `identity_created = false`, `follow_on_authorized = false`, and `follow_on_work_authorized = false`.
- The completed first-crossing operation v2 terminal summary records `FIRST_CROSSING_SUPPORTED`, `first_crossing_supported = true`, `first_crossing_authorized = true`, `crossing_authorized = true`, `first_crossing_performed = true`, `crossing_performed = true`, `first_crossing_a_recorded = true`, and `first_crossing_b_recorded = true`.
- That operation preserves that first crossing is not relation, coupling, presence, or identity; crossing authorization and performance are not relation creation.
- The request does not ask to create FIELD machinery, runtime, API, currentness, authority, standing, coupling assignment or creation, a third candidate or model, presence, identity, output, action, derivative reception, synchronization, standing descendant, descendant standing, follow-on authorization, or follow-on work.
- All downstream non-claims remain false.

## 7. Relation Support Criteria

A future relation operation may support relation only if relation boundary allowance is present; First Crossing A and First Crossing B are present as separate first-crossing records and prior basis only; first crossing is not relation before that operation; crossing authorization and performance are not relation creation; first crossing is not coupling, presence, or identity; and all non-conversion locks hold.

Those locks include sibling and non-hierarchy preservation for First Crossing A/B, Descendant Body A/B, and Candidate A/B; Regulation not sovereign over Motion; Motion not erasing Regulation; coupling unassigned and uncreated; no third candidate or model; no presence; no identity; and all downstream non-claims false.

## 8. Relation Material Object Shape

A future result may include `relation_operation_material` with exactly `relation_evaluation`, `relation_basis_evaluation`, and `relation_pair_evaluation`.

```text
relation_evaluation:
  relation_id = relation_001
  relation_pair_scope = RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY
  relation_supported = true
  relation_authorized = true
  relation_created = true
  relation_operation_performed = true
  relation_recorded = true
  field_machinery_created = false
  runtime_created = false
  api_created = false
  currentness_created = false
  authority_created = false
  coupling_created = false
  presence_established = false
  identity_created = false
  follow_on_authorized = false
  follow_on_work_authorized = false

relation_basis_evaluation:
  first_crossing_a_id = first_crossing_a_001
  first_crossing_b_id = first_crossing_b_001
  first_crossing_pair_scope = SEPARATE_FIRST_CROSSING_RECORDS_ONLY
  first_crossing_a_used_as_relation_basis = true
  first_crossing_b_used_as_relation_basis = true
  first_crossing_pair_used_as_relation_basis = true
  first_crossing_a_is_relation = false
  first_crossing_b_is_relation = false
  first_crossing_pair_is_relation = false
  crossing_authorization_is_relation_creation = false
  crossing_performance_is_relation_creation = false
  first_crossing_is_coupling = false
  first_crossing_is_presence = false
  first_crossing_is_identity = false

relation_pair_evaluation:
  relation_supported = true
  relation_created = true
  first_crossing_pair_used_as_relation_basis = true
  relation_pair_scope = RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY
  first_crossings_remain_sibling = true
  first_crossing_non_hierarchy_preserved = true
  descendant_body_non_hierarchy_preserved = true
  candidate_standing_non_hierarchy_preserved = true
  regulation_not_sovereign_over_motion = true
  motion_does_not_erase_regulation = true
  coupling_assigned = false
  coupling_created = false
  third_candidate_created = false
  third_model_admitted = false
  presence_established = false
  identity_created = false
  standing_descendant_created = false
  descendant_standing_check_performed = false
  follow_on_authorized = false
  follow_on_work_authorized = false
```

## 9. Permitted Future Operation Result

A future relation operation may return exactly one of `RELATION_OPERATION_RECORDED`, `RELATION_OPERATION_NOT_RECORDED`, `RELATION_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE`, or `RELATION_OPERATION_BLOCKED`.

If all admissibility requirements and relation support criteria hold, it may record only `relation_operation_recorded = true`, `relation_evaluation_performed = true`, `relation_result_recorded = true`, `relation_result = RELATION_SUPPORTED`, `relation_supported = true`, `relation_authorized = true`, `relation_created = true`, `relation_operation_performed = true`, `relation_recorded = true`, and the three first-crossing relation-basis fields true.

If boundary allowance is missing or insufficient while the request remains bounded, it may record `relation_result = REQUIRES_BOUNDARY_ALLOWANCE` while preserving relation authorization, creation, and performance false. If relation support is evaluated but insufficient, it may record `relation_result = RELATION_NOT_SUPPORTED` with those fields false. Converted requests must record `RELATION_OPERATION_BLOCKED`.

Even a supported future relation operation preserves FIELD machinery, runtime, API, currentness, authority, standing, output, action, derivative reception, synchronization, every coupling field, third candidate, third model, presence, identity, standing descendant, descendant-standing check, follow-on authorization, and follow-on work false.

## 10. Required Invariants

- Relation operation spec is not relation operation result. Relation operation permission is not relation creation.
- Relation creation, if later supported, is not FIELD machinery, runtime, API, currentness, authority, coupling, presence, identity, follow-on authorization, follow-on work authorization, standing descendant, descendant standing, presence-bearing, or identity-bearing.
- Relation does not assign or create coupling, admit a third candidate or model, establish presence, or create identity.
- First crossing remains prior basis and is not erased by relation. Crossing authorization and performance are not relation creation.
- First Crossing A/B, Descendant Body A/B, and Candidate A/B remain sibling and non-hierarchical. Regulation may not become sovereign over Motion; Motion may not erase Regulation; coupling remains unassigned.
- Coupling is not a third candidate or third model and is not created by relation operation. No third candidate or model is admitted.
- V1 failed attempt remains lineage only; V2 successor does not erase V1. No orphaned state, silent reset, or overwrite is authorized. Contaminated lineage remains preserved. No downstream route is authorized by this operation spec.

## 11. Relation to Completed Relation Boundary

`spec/RELATION_BOUNDARY_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the relation boundary line. It recorded:

```text
outcome = RELATION_BOUNDARY_ALLOWED
failed_check_count = 0
passed_check_count = 250
result_version = 0.1.0
relation_boundary_result = RELATION_OPERATION_CONSIDERATION_ALLOWED
relation_operation_consideration_allowed = true
first_crossing_operation_referenced = true
first_crossing_a_referenced = true
first_crossing_b_referenced = true
first_crossing_pair_referenced = true
relation_authorized = false
relation_created = false
relation_operation_performed = false
coupling_created = false
presence_established = false
identity_created = false
standing_descendant_created = false
descendant_standing_check_performed = false
follow_on_authorized = false
follow_on_work_authorized = false
```

This operation spec is downstream of that completed boundary. It does not authorize or create relation.

## 12. Relation to Completed First-Crossing Operation V2

`spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the first-crossing operation v2 line. It recorded `FIRST_CROSSING_SUPPORTED` and recorded First Crossing A and First Crossing B as first-crossing records only, while preserving relation, presence, identity, coupling, standing descendant, descendant-standing checks, and follow-on false. This operation spec does not reopen or change first-crossing operation v2.

## 13. Relation to Completed First-Crossing Boundary

`spec/FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the first-crossing boundary line. It recorded `FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED`. This operation spec does not reopen or change first-crossing boundary.

## 14. Permitted Future Route

1. A future relation operation resolver may evaluate the completed relation boundary terminal summary and completed first-crossing operation v2 terminal summary.
2. A future relation operation artifact may record relation only if boundary allowance and first-crossing support are present, first crossing remains prior basis only, and all non-conversion locks hold.
3. It may record `REQUIRES_BOUNDARY_ALLOWANCE` if required boundary allowance is missing or insufficient.
4. It may record `NOT_RECORDED` if relation support is evaluated but insufficient.
5. It must record `BLOCKED` if relation is converted into FIELD machinery, runtime, currentness, authority, coupling assignment or creation, third candidate, third model, presence, identity, output, action, derivative reception, synchronization, standing descendant, descendant standing, follow-on authorization, or follow-on work.
6. Only after a future relation operation records `RELATION_SUPPORTED` may a separately bounded presence boundary be considered.
7. No later operation is authorized by this operation spec alone.

## 15. Blocked Routes

- direct relation operation spec to relation operation completion
- direct relation boundary allowance to relation without operation
- direct first crossing to relation without relation boundary and operation
- direct relation to FIELD machinery
- direct relation to runtime
- direct relation to authority/currentness
- direct relation to coupling assignment
- direct relation to coupling creation
- direct relation to third-candidate route
- direct relation to third-model route
- direct relation to presence
- direct relation to identity
- direct relation to standing descendant
- direct relation to descendant standing
- direct relation to output/action
- direct relation to follow-on work
- repository scan route
- file discovery route
- affected-file repair route
- prior unsupported-claim validation route

## 16. Preserved Non-Claims

```text
relation_operation_recorded = false
relation_evaluation_performed = false
relation_result_recorded = false
relation_supported = false
relation_authorized = false
relation_created = false
relation_operation_performed = false
relation_recorded = false
first_crossing_a_used_as_relation_basis = false
first_crossing_b_used_as_relation_basis = false
first_crossing_pair_used_as_relation_basis = false
field_machinery_created = false
runtime_created = false
api_created = false
currentness_created = false
authority_created = false
standing_created = false
output_authorized = false
action_authorized = false
derivative_reception_authorized = false
synchronization_authorized = false
coupling_assigned_to_relation = false
coupling_assigned_to_first_crossing_a = false
coupling_assigned_to_first_crossing_b = false
coupling_assigned_to_descendant_body_a = false
coupling_assigned_to_descendant_body_b = false
coupling_assigned_to_candidate_a = false
coupling_assigned_to_candidate_b = false
coupling_created = false
third_candidate_created = false
third_model_admitted = false
presence_established = false
identity_created = false
standing_descendant_created = false
descendant_standing_check_performed = false
follow_on_authorized = false
follow_on_work_authorized = false
prior_unsupported_candidate_a_claim_validated = false
prior_unsupported_candidate_b_claim_validated = false
prior_unsupported_derivation_event_claim_validated = false
valid_derivation_event_recorded = false
affected_file_repaired = false
affected_file_edited = false
affected_file_deleted = false
affected_file_overwritten = false
affected_file_replaced = false
affected_file_redeemed = false
affected_file_treated_as_clean_basis = false
contaminated_lineage_treated_as_clean_basis = false
relation_boundary_overridden = false
relation_boundary_bypassed = false
first_crossing_operation_v1_repaired = false
first_crossing_operation_v1_overwritten = false
first_crossing_operation_v1_converted_to_standing = false
first_crossing_operation_v2_overridden = false
first_crossing_operation_v2_bypassed = false
scan_performed = false
repository_scan_performed = false
file_discovery_performed = false
repair_performed = false
validation_enforced = false
hidden_repair_performed = false
silent_overwrite_performed = false
direct_relation_operation_spec_to_relation_operation_completion = false
direct_relation_boundary_allowance_to_relation_without_operation = false
direct_first_crossing_to_relation_without_relation_boundary_and_operation = false
direct_relation_to_field_machinery = false
direct_relation_to_runtime = false
direct_relation_to_authority_currentness = false
direct_relation_to_coupling_assignment = false
direct_relation_to_coupling_creation = false
direct_relation_to_third_candidate_route = false
direct_relation_to_third_model_route = false
direct_relation_to_presence = false
direct_relation_to_identity = false
direct_relation_to_standing_descendant = false
direct_relation_to_descendant_standing = false
direct_relation_to_output_action = false
direct_relation_to_follow_on_work = false
```

## 17. Relation to Contaminated Lineage

`spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage for the unsupported existence-claim class. Its prior unsupported claims include `descendant_body_basis_candidate_a_created = true`, `descendant_body_basis_candidate_b_created = true`, and `descendant_body_basis_derivation_event_recorded = true`; the existence-claim evidence check mechanically recorded them as `UNSUPPORTED`.

This operation spec does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file. It does not treat that file as evidence for candidate creation, candidate distinctness, candidate scope, scope division, candidate-specific content, seal material, lineage receipt material, digest material, standing, descendant-body creation, first crossing, relation, presence, identity, or clean basis.

## 18. What Remains Open

- relation operation resolver
- relation operation test
- relation operation live artifact
- actual relation evaluation
- presence boundary, if separately bounded after relation support
- presence
- FIELD machinery
- runtime
- API
- currentness
- authority
- standing
- identity boundary
- output authorization
- action authorization
- derivative reception
- synchronization
- externalization boundary
- follow-on work

Open means not scheduled, not authorized, and not executed.

## 19. Closing Lock

This operation spec defines only a future relation operation shape downstream of the completed relation boundary. It does not authorize relation, create relation, perform relation operation, create FIELD machinery, create runtime, create API, create currentness, create authority, assign coupling, create coupling, admit a third candidate, admit a third model, establish presence, create identity, create standing descendants, perform descendant-standing checks, authorize output, authorize action, authorize derivative reception, authorize synchronization, authorize follow-on work, repair the affected file, validate prior unsupported claims, scan repository, discover files, enforce validation, or authorize follow-on work. Relation operation spec is not relation operation result. Relation operation permission is not relation creation. Relation, if later supported, is not FIELD machinery. Relation is not coupling. Relation is not presence. Relation is not identity. Relation is not follow-on authorization. Relation is not follow-on work authorization. First crossing remains prior basis only. Only after a future relation operation records RELATION_SUPPORTED may a separately bounded presence boundary be considered. Open means not scheduled, not authorized, and not executed.
