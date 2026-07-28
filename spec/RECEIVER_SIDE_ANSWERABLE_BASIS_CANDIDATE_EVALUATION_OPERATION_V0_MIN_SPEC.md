# Receiver-Side Answerable Basis Candidate Evaluation Operation V0 Minimum Specification

## 1. Purpose

This specification defines one future bounded operation for evaluating exactly one already received and recorded receiver-side answerable-basis candidate across eight separate dimensions. It is downstream of `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED`. It does not itself evaluate the candidate, assert a dimension result, decide candidate sufficiency, insufficiency, or indeterminacy, create receiver attestation or receiver answerable receipt, re-run presence, or authorize downstream work.

## 2. Scope

The operation is limited to one selected candidate, one selected reception operation, one completed evaluation boundary, one evaluation request, and eight independent dimensions. It creates no additional candidate, reception, evaluation boundary, live result, identity, relation, coupling, FIELD machinery, runtime, API, public intake, authority, standing, truth, continuity memory, output, action, synchronization, or follow-on authorization.

## 3. Operation Question

Given one exact candidate already supplied, received, recorded, and preserved; a completed evaluation boundary allowing consideration; and eight upstream dimensions still `NOT_EVALUATED`, may one future bounded operation evaluate that candidate across those dimensions separately, record dimension-specific results without semantic collapse, derive at most one bounded candidate-evaluation result, and stop before attestation, receipt, presence re-evaluation, or downstream authorization?

## 4. Required Answer

Yes, but only as one separately bounded candidate evaluation operation. It may evaluate exactly one selected candidate and each dimension independently. It must not collapse declarations into established facts, dimension results into receiver attestation or receiver answerable receipt, or all dimensions into presence.

## 5. Operation Identifiers

- `receiver_side_answerable_basis_candidate_evaluation_operation_id = receiver_side_answerable_basis_candidate_evaluation_operation_001`
- `receiver_side_answerable_basis_candidate_evaluation_operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION`
- `receiver_side_answerable_basis_candidate_evaluation_operation_version = 0.1.0`
- `receiver_side_answerable_basis_candidate_evaluation_operation_scope = EVALUATE_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ACROSS_EIGHT_SEPARATE_DIMENSIONS_ONLY`
- `prior_candidate_evaluation_boundary_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY`
- `prior_candidate_evaluation_boundary_outcome_required = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_ALLOWED`
- `prior_candidate_evaluation_boundary_result_required = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED`
- `prior_candidate_evaluation_boundary_recorded_required = true`; `prior_candidate_evaluation_boundary_result_recorded_required = true`; `prior_candidate_evaluation_consideration_allowed_required = true`
- `selected_candidate_reception_result_referenced_required = true`; `selected_candidate_material_referenced_required = true`
- `prior_candidate_evaluated_required = false`; `prior_candidate_sufficient_required = false`; `prior_candidate_insufficient_required = false`; `prior_candidate_indeterminate_required = false`
- `prior_receiver_attestation_created_required = false`; `prior_receiver_attestation_supported_required = false`; `prior_receiver_answerable_receipt_present_required = false`
- `prior_custody_distinct_required = false`; `prior_refusable_required = false`; `prior_could_have_been_withheld_required = false`
- `prior_presence_supported_required = false`; `prior_presence_authorized_required = false`; `prior_presence_established_required = false`; `prior_presence_recorded_required = false`
- `prior_second_candidate_received_required = false`; `prior_second_candidate_evaluated_required = false`; `prior_repeated_evaluation_permission_created_required = false`; `prior_reusable_route_created_required = false`
- `prior_follow_on_authorized_required = false`; `prior_follow_on_work_authorized_required = false`
- `admissible_future_route = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_THEN_SEPARATE_RECEIVER_ATTESTATION_OR_RECEIPT_BOUNDARY_CONSIDERATION_ONLY`

## 6. Selected Candidate Identity

- `receiver_side_answerable_basis_candidate_id = receiver_side_answerable_basis_candidate_001`
- `receiver_side_answerable_basis_candidate_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE`
- `receiver_side_answerable_basis_candidate_scope = ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`
- `selected_candidate_reception_operation_id = receiver_side_answerable_basis_reception_operation_001`
- `selected_candidate_evaluation_boundary_id = receiver_side_answerable_basis_candidate_evaluation_boundary_001`

These identifiers bind the operation to the one already received candidate only. They establish no evaluation result.

## 7. Evaluation Dimensions

The operation defines exactly these independent dimensions:

1. `candidate_structural_correspondence`
2. `declared_provenance_posture`
3. `receiver_authorship_posture`
4. `separate_custody_posture`
5. `refusability_posture`
6. `could_have_been_withheld_posture`
7. `prior_knock_correspondence_posture`
8. `capture_record_posture`

Candidate structural correspondence may evaluate only candidate id, type, scope, selected reception-operation id, selected evaluation-boundary id, one prior presence-operation knock-reference posture, and structural correspondence between selected records. It does not establish semantic sufficiency.

Declared provenance posture may evaluate only whether required declared provenance and custody references are present, internally addressable, and structurally corresponding. It does not establish verified provenance, source identity, authority, standing, or custody distinction.

Receiver-authorship posture may evaluate a bounded receiver-authorship declaration and its structural attribution to the selected packet. It does not establish receiver identity or metaphysical authorship certainty.

Separate-custody posture may evaluate bounded evidence supporting distinct receiver-controlled custody from the source repository at relevant occurrence and preservation stages. Filename, directory, working path, or declaration alone does not establish custody distinction.

Refusability posture may evaluate bounded support that submission could have been refused before source-body reception. Declaration alone does not establish refusability.

Could-have-been-withheld posture may evaluate bounded support that the trace could have remained outside source-body custody. It remains distinct from separate custody and refusability.

Prior-knock correspondence posture may evaluate whether the selected trace corresponds to exactly one bounded prior presence-operation knock reference. It does not establish attestation, receipt, or presence support.

Capture-record posture may evaluate whether bounded capture records, hashes, timestamps, and physical-signal files are present, internally consistent, and addressable. It does not establish physical-signal validity, bodily presence, human identity, receiver attestation, or truth.

## 8. Dimension Result Family

Each dimension may return exactly one of:

- `SATISFIED`
- `NOT_SATISFIED`
- `INDETERMINATE`
- `NOT_EVALUATED`

`SATISFIED` means that dimension's bounded evidence requirements were met. `NOT_SATISFIED` means they were affirmatively not met. `INDETERMINATE` means the available bounded basis does not permit a truthful satisfied or not-satisfied result. `NOT_EVALUATED` means no lawful evaluation occurred. `INDETERMINATE` is not failure; `NOT_SATISFIED` is not rejection of the candidate as a whole; `SATISFIED` is not attestation, receipt, or presence support.

## 9. Dimension Evaluation Posture

For each dimension, a future operation records only:

- `dimension_id`
- `dimension_label`
- `dimension_result`
- `dimension_evaluated`
- `dimension_established`
- `basis_referenced`
- `missing_or_inconsistent_dimension_basis`
- a compact non-conversion statement

`dimension_evaluated = true` only when that dimension was actually evaluated. `dimension_established = true` only when `dimension_result = SATISFIED`; it remains false for `NOT_SATISFIED`, `INDETERMINATE`, and `NOT_EVALUATED`. No dimension silently satisfies another.

## 10. Candidate Aggregate Posture

The operation defines:

- `receiver_side_answerable_basis_candidate_evaluated`
- `receiver_side_answerable_basis_candidate_all_dimensions_satisfied`
- `receiver_side_answerable_basis_candidate_any_dimension_not_satisfied`
- `receiver_side_answerable_basis_candidate_any_dimension_indeterminate`
- `receiver_side_answerable_basis_candidate_sufficient`
- `receiver_side_answerable_basis_candidate_insufficient`
- `receiver_side_answerable_basis_candidate_indeterminate`

Candidate evaluated may become true only when all eight dimensions were evaluated. All-dimensions-satisfied may become true only when all eight results are `SATISFIED`; any-dimension-not-satisfied or any-dimension-indeterminate may become true only for the corresponding explicit dimension result. None automatically derives candidate sufficiency, insufficiency, or indeterminacy. Dimension completion is not candidate sufficiency.

## 11. Operation Admissibility

A future operation may evaluate only if the completed boundary terminal summary exists and records the allowed boundary outcome and consideration result; the selected boundary artifact exists and parses; the selected candidate basis is exact; candidate evaluation remains false upstream; all eight dimensions remain `NOT_EVALUATED` upstream; no attestation, receipt, presence, second-candidate, repeated-evaluation-permission, reusable-route, or follow-on posture is true upstream; exactly one candidate and one evaluation request are supplied; no result is pre-claimed; and all required non-claims remain false.

## 12. Permitted Operation Results

The operation outcome family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_REQUIRES_EVALUATION_BASIS`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_BLOCKED`

The operation result family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE`
- `REQUIRES_EVALUATION_BASIS`

`RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED` is permitted only when all eight dimensions were actually evaluated and have explicit allowed results. It means evaluation completed, not all dimensions satisfied and not candidate sufficiency. `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE` is permitted when one or more dimensions are indeterminate without an operation block. `REQUIRES_EVALUATION_BASIS` is permitted when bounded basis is absent or incomplete before evaluation begins.

## 13. Required Evidence Posture

A future resolver may use only explicitly supplied bounded evaluation basis and exact selected repository references. It must not browse externally, search the repository, discover alternate files, infer or generate evidence, treat absence of contradiction as satisfaction, treat declaration alone as proof where independent support is required, evaluate another candidate, re-run reception, alter candidate material, or alter upstream artifacts.

## 14. Required Invariants

- Candidate evaluation operation is not candidate evaluation boundary. Evaluation permission is not evaluation execution.
- Dimension evaluation is not candidate sufficiency. Dimension satisfaction is not receiver attestation, receiver answerable receipt, or presence support. All dimensions satisfied is not candidate sufficiency. Evaluation completed is not candidate sufficiency.
- Candidate evaluation indeterminate is not candidate insufficiency. `INDETERMINATE` is not failure. `NOT_SATISFIED` is not candidate rejection. `NOT_EVALUATED` is not negative evaluation.
- Declaration is not established fact. Structural correspondence is not semantic sufficiency. Declared provenance is not verified provenance. Receiver-authorship posture is not receiver identity.
- Separate custody is distinct from refusability; refusability is distinct from could-have-been-withheld posture. Prior-knock correspondence is not receiver answerable receipt. Capture-record posture is not physical-signal validity; physical-signal validity is not bodily presence; bodily presence is not receiver attestation.
- Receiver attestation is distinct from receiver answerable receipt. Receiver answerable receipt is distinct from candidate evaluation. One candidate evaluation is not permission for a second evaluation or reusable evaluation permission.
- Candidate evaluation is not presence support, identity, relation, coupling, FIELD machinery, runtime, API, authority, standing, truth, continuity memory, output, action, synchronization, or follow-on work. Open means not scheduled, not authorized, and not executed.

## 15. Relation to Completed Evaluation Boundary

`spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the evaluation-boundary line. It recorded boundary allowed and evaluation consideration allowed while all eight dimensions remained `NOT_EVALUATED`; candidate evaluation, attestation, receipt, custody, refusability, withholding, and presence remained false. This operation specification is downstream of that completed result and does not reopen or alter the boundary.

## 16. Relation to Selected Candidate Reception

The selected candidate has already been supplied, received, recorded, and preserved. This specification does not receive, alter, normalize, reinterpret, or replace candidate material.

## 17. Relation to Completed Presence Operation

The completed presence operation remains unchanged. Even a completed candidate evaluation does not automatically satisfy the presence operation, create receiver attestation, create receiver answerable receipt, or support presence.

## 18. Permitted Future Route

Exactly one route is defined:

1. A future evaluation-operation resolver may inspect the completed evaluation boundary, selected boundary artifact, selected reception artifact, and explicitly supplied bounded evaluation basis.
2. It may evaluate exactly eight separate dimensions and record one result for each.
3. It may record evaluation completion or evaluation indeterminacy.
4. It must preserve candidate sufficiency, attestation, receipt, and presence as false.
5. Any sufficiency, attestation, receipt, or presence consideration requires a later separately bounded boundary.
6. The operation terminates after one evaluation of the selected candidate.

## 19. Blocked Routes

The following conversions are blocked: boundary permission directly to completed evaluation; candidate reception directly to evaluation result; one dimension result to omnibus candidate sufficiency; all dimensions satisfied directly to receiver attestation, receiver answerable receipt, or presence support; any dimension satisfied directly to another dimension satisfied; declaration directly to established fact; filename or directory name directly to custody distinction; receiver label directly to receiver identity; hash match directly to semantic sufficiency; timestamp directly to currentness or authority; device metadata directly to human identity; physical signal directly to bodily presence; capture record directly to receiver attestation; prior-knock correspondence directly to receiver answerable receipt; evaluation completion directly to candidate sufficiency or insufficiency; evaluation indeterminacy directly to candidate insufficiency; candidate evaluation directly to presence support, presence authorization, presence establishment, presence recording, identity, relation, coupling, FIELD machinery, runtime, API, public intake, authority, standing, truth, continuity memory, output, action, synchronization, or follow-on work; first evaluation to second-candidate evaluation, repeated-evaluation permission, or reusable route; selected candidate to retroactive validation of contaminated lineage; repository scan, file discovery, affected-file repair, and validation-enforcement routes.

## 20. Preserved Non-Claims

Default operation posture is:

- `receiver_side_answerable_basis_candidate_evaluation_operation_recorded = false`
- `receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded = false`
- `receiver_side_answerable_basis_candidate_evaluation_operation_result = NOT_EVALUATED`
- `receiver_side_answerable_basis_candidate_evaluated = false`
- `receiver_side_answerable_basis_candidate_all_dimensions_satisfied = false`
- `receiver_side_answerable_basis_candidate_any_dimension_not_satisfied = false`
- `receiver_side_answerable_basis_candidate_any_dimension_indeterminate = false`
- `receiver_side_answerable_basis_candidate_sufficient = false`; `receiver_side_answerable_basis_candidate_insufficient = false`; `receiver_side_answerable_basis_candidate_indeterminate = false`
- `receiver_attestation_created = false`; `receiver_attestation_supported = false`; `receiver_answerable_receipt_present = false`
- `presence_supported = false`; `presence_authorized = false`; `presence_established = false`; `presence_recorded = false`
- `second_candidate_received = false`; `second_candidate_evaluated = false`; `repeated_evaluation_permission_created = false`; `reusable_route_created = false`
- `follow_on_authorized = false`; `follow_on_work_authorized = false`

Every dimension defaults to `NOT_EVALUATED`. Candidate sufficiency, insufficiency, and indeterminacy remain false unless a later separately bounded sufficiency boundary is selected.

## 21. Relation to Contaminated Lineage

Contaminated lineage remains preserved. No evaluation result may retroactively validate unrelated unsupported claims. This specification does not repair contaminated lineage.

## 22. What Remains Open

- candidate evaluation operation resolver
- candidate evaluation operation test
- candidate evaluation operation live artifact
- actual candidate evaluation
- dimension-specific evaluation basis and dimension-specific results
- candidate sufficiency boundary, receiver attestation boundary, receiver answerable receipt boundary, and presence re-evaluation, if separately selected or bounded
- identity, relation, coupling, FIELD machinery, runtime, API, authority, standing, output, action, synchronization, and follow-on work

Open means not scheduled, not authorized, and not executed. Open does not mean next unless separately selected.

## 23. Closing Lock

This operation specification defines only one future evaluation operation for the one receiver-side answerable-basis candidate already supplied, received, recorded, and preserved. It is downstream of the completed candidate evaluation boundary result RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED. It does not itself evaluate the candidate; record any dimension as SATISFIED, NOT_SATISFIED, or INDETERMINATE; decide candidate sufficiency, insufficiency, or indeterminacy; create receiver attestation or receiver answerable receipt; establish custody distinctness, refusability, could-have-been-withheld posture, receiver identity, source identity, verified provenance, physical-signal validity, bodily presence, human presence, or presence support; create identity, relation, coupling, FIELD machinery, runtime, API, public intake, currentness, authority, standing, truth, continuity memory, output, action, synchronization, follow-on authorization, or follow-on work; repair contaminated lineage; scan repository; discover files; or enforce validation. A future operation may evaluate exactly eight separate dimensions for exactly one selected candidate. Each dimension may return SATISFIED, NOT_SATISFIED, INDETERMINATE, or NOT_EVALUATED. INDETERMINATE is not failure. NOT_SATISFIED is not candidate rejection. Dimension satisfaction is not candidate sufficiency, receiver attestation, receiver answerable receipt, or presence support. Even if all eight dimensions are satisfied, candidate sufficiency remains a separate later question. Evaluation completion is not receiver attestation. Receiver attestation remains distinct from receiver answerable receipt. One candidate evaluation is not permission for a second evaluation or reusable evaluation route. Only after one future evaluation operation records dimension-specific results may a separately bounded candidate-sufficiency, receiver-attestation, receiver-answerable-receipt, or presence-re-evaluation boundary be considered. Open means not scheduled, not authorized, and not executed.
