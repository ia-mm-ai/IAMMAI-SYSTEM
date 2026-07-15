# Descendant Body Differentiation Operation V0 Minimum Specification

## 1. Purpose

This file defines one future descendant-body differentiation operation.

This file does not implement the operation.

This file does not perform the operation.

This file does not create operation result, candidate records, descendant bodies, derivation, standing, relation, crossing, FIELD machinery, runtime, currentness, authority, output, action, derivative reception, synchronization, repair, scan, validation enforcement, or follow-on work.

This operation spec is downstream of the completed descendant-body differentiation operation boundary line.

## 2. Status and Rank

This spec is additive.

This spec is repo-local to `IAMMAI-SYSTEM`.

This spec ranks below constitutional and reference authority surfaces.

This spec ranks below current executable source, existing tests, emitted artifacts, and standing terminal summaries.

This spec is downstream of:

- `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md`
- `spec/SEAM_CASE_LAW__CO_AGENCY_AUTHORIZATION_UNSUPPORTED_EXISTENCE_CLAIM_V0.md`
- `spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md`
- `spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_V0_MIN_SPEC.md`
- `spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md`

This spec preserves `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` unchanged as contaminated lineage.

This spec does not replace, repair, edit, delete, overwrite, rename, move, patch, normalize, invalidate, or silently correct any upstream file.

This spec does not authorize follow-on work.

## 3. Upstream Basis

`spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` is preserved contaminated lineage.

The affected file contains unsupported existence claims:

- `descendant_body_basis_candidate_a_created = true`
- `descendant_body_basis_candidate_b_created = true`
- `descendant_body_basis_derivation_event_recorded = true`

The existence-claim evidence check mechanically recorded those claims as `UNSUPPORTED`.

The descendant-body differentiation operation boundary recorded:

- `boundary_type = DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY`
- `future_operation_type = DESCENDANT_BODY_DIFFERENTIATION_OPERATION`
- `future_operation_scope = ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY`
- `future_candidate_record_policy = EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS`
- `future_failure_visibility_policy = BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL`
- `future_operation_not_created = true`
- `candidate_records_not_created = true`
- `descendant_bodies_not_created = true`

This spec is downstream of that boundary result and does not override it.

## 4. Operation Question

Given one declared standing body-proof basis reference, one preserved contaminated descendant derivation event file, one completed existence-claim evidence check line, and one completed descendant-body differentiation operation boundary line, may a separately implemented descendant-body differentiation operation attempt to record one operation result that either emits exactly two non-standing descendant-body-basis candidate records with operation evidence, or blocks visibly without creating candidate records, while preserving that the operation does not create standing descendants, authorize crossing, create relation, create FIELD machinery, create runtime, create currentness, create authority, authorize output, authorize action, authorize derivative reception, authorize synchronization, repair the affected file, validate prior unsupported claims, or authorize follow-on work?

## 5. Definitions

`descendant-body differentiation operation` means a future bounded operation, not performed here, that may attempt to produce two non-standing descendant-body-basis candidate records from one declared standing body-proof basis reference.

`standing body-proof basis reference` means the declared upstream reference used as the basis for the operation, without recreating or restating the upstream body-proof basis here.

`operation result` means a future emitted result object from a separately implemented resolver.

`candidate record` means a future result-contained record emitted by the operation only if all operation requirements pass.

`non-standing descendant-body-basis candidate` means a candidate record emitted by the operation that is explicitly not a standing descendant body and does not authorize standing, crossing, relation, FIELD machinery, runtime, currentness, authority, output, action, derivative reception, synchronization, or follow-on work.

`operation evidence` means the emitted operation result fields, candidate record fields, evidence references, and checks sufficient to support the prospective claim that candidate records were created by this operation.

`visible block` means an operation result that refuses candidate-record creation and records why no candidate records were produced.

`contaminated lineage` means `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` preserved unchanged for the unsupported existence-claim class.

`operation spec` means this file as operation specification only, not operation execution.

## 6. Operation Input Shape

Future operation input must include at minimum:

- `operation_id`
- `operation_type`
- `operation_version`
- `operation_scope`
- `operation_intent`
- `source_body_proof_basis_reference`
- `contaminated_lineage_reference`
- `evidence_requirement_boundary_reference`
- `evidence_check_terminal_summary_reference`
- `evidence_check_artifact_reference`
- `differentiation_operation_boundary_reference`
- `differentiation_operation_boundary_artifact_reference`
- `candidate_record_count_requested`
- `candidate_record_policy`
- `failure_visibility_policy`
- `differentiation_method`
- `scan_allowed`
- `repair_allowed`
- `validation_enforcement_allowed`
- `standing_authorized`
- `crossing_authorized`
- `relation_authorized`
- `field_machinery_authorized`
- `runtime_authorized`
- `currentness_authorized`
- `authority_authorized`
- `output_authorized`
- `action_authorized`
- `derivative_reception_authorized`
- `synchronization_authorized`
- `follow_on_authorized`
- `declared_non_claims`

Required future operation constants and postures:

- `operation_type = DESCENDANT_BODY_DIFFERENTIATION_OPERATION`
- `operation_version = 0.1.0`
- `operation_scope = ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY`
- `candidate_record_count_requested = 2`
- `candidate_record_policy = EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS`
- `failure_visibility_policy = BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL`
- `differentiation_method = DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION`
- `scan_allowed = false`
- `repair_allowed = false`
- `validation_enforcement_allowed = false`
- `standing_authorized = false`
- `crossing_authorized = false`
- `relation_authorized = false`
- `field_machinery_authorized = false`
- `runtime_authorized = false`
- `currentness_authorized = false`
- `authority_authorized = false`
- `output_authorized = false`
- `action_authorized = false`
- `derivative_reception_authorized = false`
- `synchronization_authorized = false`
- `follow_on_authorized = false`

Future operation outcomes may include:

- `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED`
- `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCKED`
- `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUIRES_ADDITIONAL_BASIS`
- `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_NOT_RECORDED`

Actual implementation requires a separately bounded resolver step.

## 7. Operation Behavior

A future implementation may record `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED` only if:

- operation input is declared and well-formed
- operation type is `DESCENDANT_BODY_DIFFERENTIATION_OPERATION`
- operation scope is `ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY`
- `candidate_record_count_requested = 2`
- `candidate_record_policy = EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS`
- `failure_visibility_policy = BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL`
- `differentiation_method = DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION`
- source body-proof basis reference is declared
- contaminated lineage reference is declared
- evidence check terminal summary reference is declared
- evidence check artifact reference is declared
- differentiation operation boundary reference is declared
- differentiation operation boundary artifact reference is declared
- completed boundary result markers are present
- completed evidence check result markers are present
- prior contaminated lineage markers are present
- `scan_allowed = false`
- `repair_allowed = false`
- `validation_enforcement_allowed = false`
- all standing, crossing, relation, FIELD, runtime, currentness, authority, output, action, derivative reception, synchronization, and follow-on authorization flags are false
- no request asks to repair the affected file
- no request asks to validate prior unsupported claims
- no request asks to treat contaminated lineage as clean basis
- no request asks to create standing descendants
- no request asks to authorize crossing, relation, FIELD machinery, runtime, currentness, authority, output, action, derivative reception, synchronization, or follow-on work
- exactly two candidate records are emitted
- each emitted candidate record includes operation evidence
- each emitted candidate record is explicitly non-standing
- each emitted candidate record has a distinct candidate role
- each emitted candidate record has a distinct candidate_record_id
- each emitted candidate record references the same source_body_proof_basis_reference
- each emitted candidate record references the operation_id
- each emitted candidate record does not inherit existence from the contaminated derivation event file
- each emitted candidate record records `candidate_record_created_by_operation = true`
- each emitted candidate record records `candidate_record_standing = false`
- each emitted candidate record records `descendant_body_created = false`
- each emitted candidate record records `crossing_authorized = false`
- each emitted candidate record records `relation_authorized = false`
- each emitted candidate record records `field_machinery_authorized = false`
- each emitted candidate record records `runtime_authorized = false`
- each emitted candidate record records `currentness_authorized = false`
- each emitted candidate record records `authority_authorized = false`
- each emitted candidate record records `output_authorized = false`
- each emitted candidate record records `action_authorized = false`
- each emitted candidate record records `derivative_reception_authorized = false`
- each emitted candidate record records `synchronization_authorized = false`
- each emitted candidate record records `follow_on_authorized = false`

A future implementation must record `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCKED` or `DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUIRES_ADDITIONAL_BASIS` when required basis, markers, input shape, candidate count, evidence policy, visibility policy, or non-claim posture fails.

No implementation exists in this spec.

## 8. Candidate Record Shape

Candidate records are future result-contained records only.

This spec does not create the candidate records.

If a future implementation records the operation successfully, it may emit exactly two candidate records.

Candidate A future shape:

- `candidate_record_id = descendant_body_basis_candidate_a_001`
- `candidate_record_type = NON_STANDING_DESCENDANT_BODY_BASIS_CANDIDATE`
- `candidate_role = CANDIDATE_A`
- `candidate_record_created_by_operation = true`
- `candidate_record_standing = false`
- `descendant_body_created = false`
- `source_body_proof_basis_reference = same declared operation basis`
- `operation_id = same operation id`
- `contaminated_lineage_reference = spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md`
- `inherited_from_contaminated_lineage = false`
- `prior_unsupported_claim_validated = false`
- `crossing_authorized = false`
- `relation_authorized = false`
- `field_machinery_authorized = false`
- `runtime_authorized = false`
- `currentness_authorized = false`
- `authority_authorized = false`
- `output_authorized = false`
- `action_authorized = false`
- `derivative_reception_authorized = false`
- `synchronization_authorized = false`
- `follow_on_authorized = false`

Candidate B future shape:

- `candidate_record_id = descendant_body_basis_candidate_b_001`
- `candidate_record_type = NON_STANDING_DESCENDANT_BODY_BASIS_CANDIDATE`
- `candidate_role = CANDIDATE_B`
- `candidate_record_created_by_operation = true`
- `candidate_record_standing = false`
- `descendant_body_created = false`
- `source_body_proof_basis_reference = same declared operation basis`
- `operation_id = same operation id`
- `contaminated_lineage_reference = spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md`
- `inherited_from_contaminated_lineage = false`
- `prior_unsupported_claim_validated = false`
- `crossing_authorized = false`
- `relation_authorized = false`
- `field_machinery_authorized = false`
- `runtime_authorized = false`
- `currentness_authorized = false`
- `authority_authorized = false`
- `output_authorized = false`
- `action_authorized = false`
- `derivative_reception_authorized = false`
- `synchronization_authorized = false`
- `follow_on_authorized = false`

## 9. Candidate Record Constraints

Candidate records, even if emitted by a future operation result, are non-standing.

Candidate records are not descendant bodies.

Candidate records do not authorize crossing.

Candidate records do not create relation.

Candidate records do not create FIELD machinery.

Candidate records do not create runtime.

Candidate records do not create API.

Candidate records do not create currentness.

Candidate records do not create authority.

Candidate records do not create standing.

Candidate records do not authorize output.

Candidate records do not authorize action.

Candidate records do not authorize derivative reception.

Candidate records do not authorize synchronization.

Candidate records do not authorize follow-on work.

Candidate records must not inherit existence from `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md`.

Candidate records must not retroactively validate prior unsupported claims.

Candidate records must not repair the affected file.

Candidate records must not make contaminated lineage clean basis.

## 10. Relation to Contaminated Lineage

`spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage.

Unsupported claims include:

- `descendant_body_basis_candidate_a_created = true`
- `descendant_body_basis_candidate_b_created = true`
- `descendant_body_basis_derivation_event_recorded = true`

The existence-claim evidence check mechanically recorded those claims as `UNSUPPORTED`.

This operation spec does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file.

This operation spec does not treat the affected file as evidence for candidate creation.

Any future operation implementation may only produce new evidence prospectively, not retroactively validate old unsupported claims.

Repo presence is not standing.

Codex execution is not truth.

Operator authorization is not sole authorship.

Derivative rendering is not standing evidence.

Later recognition is not proof of upstream validity.

Contaminated lineage is not clean basis.

## 11. Non-Claims

This spec preserves these non-claims as false:

- `operation_implemented = false`
- `operation_created = false`
- `operation_performed = false`
- `operation_recorded = false`
- `differentiation_performed = false`
- `operation_result_created = false`
- `candidate_records_created = false`
- `descendant_body_a_created = false`
- `descendant_body_b_created = false`
- `descendant_body_basis_candidate_a_created = false`
- `descendant_body_basis_candidate_b_created = false`
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
- `evidence_check_overridden = false`
- `evidence_check_bypassed = false`
- `boundary_overridden = false`
- `boundary_bypassed = false`
- `standing_descendant_created = false`
- `descendant_standing_check_performed = false`
- `first_crossing_authorized = false`
- `relation_created = false`
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
- `follow_on_work_authorized = false`
- `scan_performed = false`
- `repository_scan_performed = false`
- `repair_performed = false`
- `validation_enforced = false`
- `hidden_repair_performed = false`
- `silent_overwrite_performed = false`

Allowed future operation true postures, only if separately implemented and recorded by a future operation result, may include:

- `operation_result_created = true`
- `operation_recorded = true`
- `differentiation_performed = true`
- `candidate_records_created = true`
- `candidate_record_created_by_operation = true` for each emitted candidate record

This spec itself does not set any of those true.

No false non-claim is listed as true.

## 12. What Remains Open

Open and not executed:

- descendant-body differentiation operation resolver
- descendant-body differentiation operation test
- descendant-body differentiation operation artifact
- descendant-body differentiation operation terminal summary
- candidate-record evidence emission
- candidate-record standing checks
- repair or successor handling of the affected file, if ever separately bounded
- prose-shaped existence-claim handling, if ever separately bounded
- automated repository scan, if ever separately bounded
- contribution/provenance trace handling, if ever separately bounded
- first crossing
- relation
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
- follow-on work

Open means not scheduled.

Open means not authorized.

Open means not executed.

Open does not mean next unless separately selected.

## 13. Closing Lock

This operation spec defines only the conditions for a future descendant-body differentiation operation. It does not implement the operation, perform the operation, create operation result, create candidate records, create descendant bodies, validate prior unsupported claims, repair the affected file, create standing, authorize crossing, create relation, create FIELD machinery, create runtime, create currentness, create authority, authorize output, authorize action, authorize derivative reception, authorize synchronization, or authorize follow-on work. The affected descendant derivation event file remains preserved contaminated lineage for the unsupported existence-claim class. The completed existence-claim evidence check line remains standing as the mechanical classification that the three prior descendant existence claims are UNSUPPORTED. The completed descendant-body differentiation operation boundary line remains standing as the permission-to-define-operation boundary only. Any actual operation resolver, test, artifact, terminal summary, candidate-record evidence emission, candidate standing check, first crossing, relation, FIELD machinery, runtime, authority, currentness, output, action, derivative reception, synchronization, repair successor, automated scan, provenance trace, prose-shaped existence-claim handling, or follow-on work still requires a separately bounded step.
