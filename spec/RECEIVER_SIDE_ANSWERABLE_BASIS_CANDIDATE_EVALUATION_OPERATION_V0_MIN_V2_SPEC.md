# Receiver-Side Answerable Basis Candidate Evaluation Operation V0 Minimum V2 Specification

## 1. Purpose

This is one standalone V2 successor specification for the same constitutional one-candidate, eight-dimension evaluation operation first externalized by `spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_V0_MIN_SPEC.md`. It clarifies the immediate downstream route, deterministic result precedence, atomic eight-dimension basis preflight, separation of supplied basis from resolver-derived results, and exhaustion after one complete evaluation. It does not evaluate the selected candidate, admit live evaluation basis, record a dimension result, decide candidate sufficiency, or authorize downstream work.

## 2. Scope

The operation is limited to one already supplied, received, recorded, and preserved selected candidate; one selected reception operation; one completed evaluation boundary; one bounded evaluation request; and eight independent dimensions. It creates no second candidate, reception, evaluation boundary, live evaluation, candidate sufficiency, candidate insufficiency, candidate-level indeterminacy, receiver attestation, receiver answerable receipt, presence re-evaluation, identity, relation, coupling, FIELD machinery, runtime, API, public intake, authority, standing, output, action, synchronization, or follow-on authorization.

## 3. Successor Relation

The predecessor specification remains preserved lineage and remains unchanged. It first externalized this operation family. V2 preserves its constitutional operation identity and does not retroactively repair, invalidate, overwrite, or silently correct it. V2 clarifies downstream route, aggregate-result precedence, atomic basis admission, result derivation, and exhaustion only; it records no live evaluation.

## 4. Operation Question

Given the exact selected candidate, the completed evaluation boundary that allowed consideration only, and eight upstream dimensions that remain `NOT_EVALUATED`, may one future bounded operation preflight complete admissible basis for all eight dimensions, evaluate all eight exactly once, derive dimension-specific results without semantic collapse, and stop before candidate sufficiency, attestation, receipt, presence re-evaluation, or downstream authorization?

## 5. Required Answer

Yes, but only as one separately bounded operation with complete admitted basis across all eight dimensions. A bounded incomplete request may record `REQUIRES_EVALUATION_BASIS` without evaluating any dimension. A completed operation may record only a completed evaluation result or the more specific indeterminate evaluation result. Candidate sufficiency is the immediate separate downstream question; this specification authorizes no sufficiency boundary or later route.

## 6. Operation Identifiers

- `receiver_side_answerable_basis_candidate_evaluation_operation_id = receiver_side_answerable_basis_candidate_evaluation_operation_001`
- `receiver_side_answerable_basis_candidate_evaluation_operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION`
- `receiver_side_answerable_basis_candidate_evaluation_operation_version = 0.1.0`
- `receiver_side_answerable_basis_candidate_evaluation_operation_scope = EVALUATE_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ACROSS_EIGHT_SEPARATE_DIMENSIONS_ONLY`
- `admissible_future_route = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_THEN_CANDIDATE_SUFFICIENCY_BOUNDARY_ONLY`

The required upstream boundary type is `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY`; its required outcome is `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_ALLOWED`; its required result is `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED`. The boundary is required to be recorded, result-recorded, and consideration-allowed. The selected reception result and selected candidate material are required to be referenced. Prior candidate evaluation, sufficiency, insufficiency, candidate-level indeterminacy, attestation, receiver answerable receipt, custody distinction, refusability, withholding posture, presence, second-candidate, repeated-evaluation, reusable-route, and follow-on postures are required false.

Completed candidate evaluation does not directly authorize receiver-attestation consideration, receiver-answerable-receipt consideration, or presence re-evaluation. Only after a separately bounded candidate-sufficiency result may later attestation, receipt, or presence questions be considered. This specification authorizes none of those later boundaries.

## 7. Selected Candidate Identity

- `receiver_side_answerable_basis_candidate_id = receiver_side_answerable_basis_candidate_001`
- `receiver_side_answerable_basis_candidate_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE`
- `receiver_side_answerable_basis_candidate_scope = ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`
- `selected_candidate_reception_operation_id = receiver_side_answerable_basis_reception_operation_001`
- `selected_candidate_evaluation_boundary_id = receiver_side_answerable_basis_candidate_evaluation_boundary_001`

These identifiers bind one exact selected candidate only. They establish no evaluation result, sufficiency, attestation, receipt, or presence support.

## 8. Evaluation Dimensions

The operation defines exactly these separate dimensions:

1. `candidate_structural_correspondence`
2. `declared_provenance_posture`
3. `receiver_authorship_posture`
4. `separate_custody_posture`
5. `refusability_posture`
6. `could_have_been_withheld_posture`
7. `prior_knock_correspondence_posture`
8. `capture_record_posture`

Every dimension remains `NOT_EVALUATED` in this specification itself. No dimension silently satisfies another.

## 9. Dimension Result Family

Each lawfully evaluated dimension has exactly one result: `SATISFIED`, `NOT_SATISFIED`, or `INDETERMINATE`. `NOT_EVALUATED` means no lawful evaluation occurred.

- `SATISFIED` means the admitted basis met the bounded requirements declared for that dimension.
- `NOT_SATISFIED` means the admitted basis affirmatively shows that one or more required dimension conditions were not met.
- `INDETERMINATE` means the admitted basis was sufficient to perform the evaluation but insufficient to truthfully choose either other result.

`SATISFIED` is dimension-bounded, not unrestricted truth. `NOT_SATISFIED` is not rejection of the candidate as a whole. `INDETERMINATE` is not failure. `NOT_EVALUATED` is not a negative result. Supplied evaluation basis is not a dimension result; a requested dimension result is not admissible evaluation basis; only the resolver may derive a dimension result under the governing rules.

## 10. Atomic Evaluation-Basis Gate

Before evaluating any dimension, a future resolver must preflight all eight separately supplied basis records and derive these gate postures:

- `evaluation_basis_supplied`
- `evaluation_basis_complete`
- `all_dimension_basis_records_present`
- `all_dimension_basis_records_bounded`
- `all_dimension_basis_records_reference_selected_candidate`
- `all_dimension_basis_records_reference_selected_boundary`
- `all_dimension_basis_records_non_result_preclaiming`
- `all_dimension_basis_records_admissible`

If any record is absent, malformed, references another candidate or boundary, pre-claims a result, or requests prohibited conversion, no dimension may be evaluated. All eight results remain `NOT_EVALUATED`; every `dimension_evaluated` and `dimension_established` remains false; and `receiver_side_answerable_basis_candidate_evaluated` remains false. A request that is otherwise bounded may record `REQUIRES_EVALUATION_BASIS`; malformed, deceptive, pre-claiming, alternate-candidate, conversion-seeking, or otherwise prohibited requests must block.

Partial evaluation may not stand. The operation may not record some evaluated dimensions while leaving others `NOT_EVALUATED`, and it may not create a route for later completion of the same candidate evaluation.

## 11. Dimension-Basis Record Shape

One separately supplied bounded record is required for each dimension. Each record may contain only:

- `dimension_id`
- `selected_candidate_id`
- `selected_candidate_reception_operation_id`
- `selected_candidate_evaluation_boundary_id`
- `basis_supplied`
- `basis_items`
- `basis_references`
- `explicit_support_postures`
- `explicit_contradiction_postures`
- `unresolved_postures`
- `evaluator_reference`
- `basis_non_claims`

`basis_items` and `basis_references` are bounded inputs only. `evaluator_reference` is a declared reference, not evaluator authority, identity, standing, or truth. Explicit support is not automatically `SATISFIED`; explicit contradiction is not automatically `NOT_SATISFIED` unless recognized by the governing dimension rule; unresolved posture is not automatically `INDETERMINATE` unless admitted basis permits lawful evaluation. The record contains no requested or pre-claimed result and no candidate sufficiency, attestation, receipt, presence, authority, standing, or downstream-result preclaim. The future resolver preserves supplied basis without silently rewriting it.

## 12. Dimension-Result Derivation

Only after the atomic gate passes, the future resolver derives exactly one result per dimension in this order:

1. Record `SATISFIED` when admitted basis affirmatively satisfies every required bounded condition and contains no governing contradiction.
2. Otherwise record `NOT_SATISFIED` when admitted basis affirmatively establishes that one or more required bounded conditions were not met.
3. Otherwise record `INDETERMINATE`.

`NOT_EVALUATED` is used only when the operation does not lawfully enter evaluation. Absence of contradiction is not `SATISFIED`; absence of support is not `NOT_SATISFIED`; and caller labels do not control derivation.

## 13. Operation-Result Precedence

The outcome family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_REQUIRES_EVALUATION_BASIS`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_BLOCKED`

The result family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE`
- `REQUIRES_EVALUATION_BASIS`

Apply this precedence:

1. `BLOCKED` takes precedence for malformed, prohibited, conversion-seeking, alternate-candidate, result-preclaiming, non-claim-flipping, or otherwise invalid requests.
2. `REQUIRES_EVALUATION_BASIS` applies only to a bounded request without complete admissible eight-dimension basis.
3. `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE` applies when all eight dimensions were lawfully evaluated and at least one is `INDETERMINATE`.
4. `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED` applies when all eight dimensions were lawfully evaluated and none is `INDETERMINATE`.

`EVALUATED` may include one or more `NOT_SATISFIED` dimensions and means only that the eight-dimension operation completed. `EVALUATION_INDETERMINATE` also means all eight dimensions were evaluated and is the more specific result when one or more dimensions are indeterminate. Neither establishes candidate sufficiency, insufficiency, or candidate-level indeterminacy.

## 14. Candidate Aggregate Posture

The operation preserves:

- `receiver_side_answerable_basis_candidate_evaluated`
- `receiver_side_answerable_basis_candidate_all_dimensions_satisfied`
- `receiver_side_answerable_basis_candidate_any_dimension_not_satisfied`
- `receiver_side_answerable_basis_candidate_any_dimension_indeterminate`
- `receiver_side_answerable_basis_candidate_sufficient`
- `receiver_side_answerable_basis_candidate_insufficient`
- `receiver_side_answerable_basis_candidate_indeterminate`

Candidate evaluated is true for either completed operation result because all eight dimensions were evaluated. All-dimensions-satisfied is true only when all eight are `SATISFIED`; any-dimension-not-satisfied is true only when one or more are `NOT_SATISFIED`; and any-dimension-indeterminate is true only when one or more are `INDETERMINATE`. Candidate sufficient, insufficient, and candidate-level indeterminate remain false. Dimension-level indeterminacy is not candidate-level indeterminacy; any dimension not satisfied is not candidate insufficiency; all dimensions satisfied is not candidate sufficiency.

## 15. Operation Exhaustion

After one complete eight-dimension evaluation:

- `candidate_evaluation_operation_exhausted = true`
- `second_candidate_received = false`
- `second_candidate_evaluated = false`
- `repeated_evaluation_permission_created = false`
- `reusable_route_created = false`
- `same_candidate_re_evaluation_authorized = false`
- `dimension_completion_route_created = false`
- `follow_on_authorized = false`
- `follow_on_work_authorized = false`

One complete operation cannot be resumed, extended with later dimension results, silently rerun, or inferred from changed files or newly noticed evidence. Correction requires a separately bounded correction or successor operation. For `REQUIRES_EVALUATION_BASIS`, exhaustion remains false, no evaluation has occurred, no debt or scheduled retry exists, and later basis supply is not automatically authorized; any later invocation remains subject to the same bounded request and exact candidate.

## 16. Dimension-Specific Rule Posture

Each future rule evaluates admitted bounded basis only:

1. Structural correspondence evaluates exact identifiers and selected-record correspondence, not semantic sufficiency.
2. Declared provenance evaluates declared references that are present, addressable, and structurally corresponding, not verified provenance, identity, authority, standing, or custody distinction.
3. Receiver authorship evaluates bounded declaration and structural attribution, not receiver identity or unrestricted authorship certainty.
4. Separate custody evaluates bounded support for distinct receiver-controlled custody at occurrence and preservation stages; declaration, filename, directory, or working path alone is insufficient.
5. Refusability evaluates bounded support that submission could have been refused before source-body reception; declaration alone is insufficient.
6. Could-have-been-withheld evaluates bounded support that the trace could have remained outside source-body custody; it is distinct from separate custody and refusability.
7. Prior-knock correspondence evaluates correspondence to exactly one selected bounded prior-knock reference, not attestation, receipt, or presence conversion.
8. Capture record evaluates bounded capture records, hashes, timestamps, and physical-signal records that are present, internally consistent, and addressable, not physical-signal validity, bodily presence, human identity, attestation, or truth.

## 17. Required Evidence Posture

A future resolver may use only the completed boundary, exact selected artifacts, and explicitly supplied bounded eight-dimension basis records. It may not browse externally, search or discover repository material, infer or generate evidence, silently rewrite supplied basis, alter candidate material, alter upstream artifacts, evaluate another candidate, or re-run reception. Declaration is not established fact; structural correspondence is not semantic sufficiency; declared provenance is not verified provenance; receiver-authorship posture is not receiver identity; and absence of contradiction or support has no result-converting force.

## 18. Required Invariants

Evaluation-boundary permission is not evaluation execution. Dimension evaluation is not candidate sufficiency, attestation, receiver answerable receipt, or presence support. Separate custody, refusability, and could-have-been-withheld posture remain distinct. Prior-knock correspondence is not receiver answerable receipt. Capture record is not physical-signal validity, bodily presence, human presence, or truth. One candidate evaluation is not a second evaluation or reusable evaluation permission. Candidate evaluation is not identity, relation, coupling, FIELD machinery, runtime, API, public intake, authority, standing, output, action, synchronization, or follow-on work.

## 19. Relation to Predecessor Specification

`spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_V0_MIN_SPEC.md` remains preserved predecessor lineage. It first externalized the eight-dimension operation family and remains unchanged. V2 preserves the same constitutional operation identity, clarifies the downstream route, aggregate-result precedence, atomic basis admission, result derivation, and exhaustion, does not retroactively change the predecessor, and does not record a live evaluation.

## 20. Relation to Completed Evaluation Boundary

`spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_TERMINAL_SUMMARY_V0.md` is governing upstream authority. The selected boundary artifact is required upstream basis. The completed boundary allowed evaluation consideration only; all dimensions remained `NOT_EVALUATED` and candidate evaluation remained false. This V2 operation specification is downstream of that result and does not reopen or alter the boundary.

## 21. Relation to Selected Candidate Reception

The selected candidate has already been supplied, received, recorded, and preserved in the selected successful reception artifact. V2 does not receive, alter, normalize, reinterpret, replace, or reproduce candidate material.

## 22. Relation to Completed Presence Operation

The completed presence operation remains unchanged. Completed evaluation does not satisfy presence. Candidate sufficiency must be separately considered before any later attestation, receipt, or presence route, and no such route is authorized here.

## 23. Permitted Future Route

1. A future V2-selected resolver may preflight the completed evaluation boundary, exact selected artifacts, and one separately supplied eight-dimension evaluation-basis request.
2. With complete basis absent but a bounded request, it may record `REQUIRES_EVALUATION_BASIS` without evaluating any dimension.
3. With complete admitted basis, it must evaluate all eight dimensions exactly once.
4. It must derive each dimension result under the governing dimension rule.
5. It must record `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE` when one or more dimensions are `INDETERMINATE`.
6. Otherwise it may record `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED` after all eight dimensions complete.
7. It must preserve candidate sufficiency, candidate insufficiency, candidate-level indeterminacy, attestation, receipt, and presence as false.
8. The operation exhausts after one complete eight-dimension evaluation.
9. The only immediate downstream family that may later be considered is one separately bounded candidate-sufficiency boundary.
10. No sufficiency boundary or later route is authorized by this specification alone.

## 24. Blocked Routes

Blocked routes include partial dimension evaluation; partial evaluation to later completion; missing basis to inferred result; caller-supplied, requested `SATISFIED`, requested `NOT_SATISFIED`, or requested `INDETERMINATE` result; evaluator reference to authority, identity, standing, or truth; support directly to `SATISFIED`; contradiction directly to `NOT_SATISFIED` without governing rule; unresolved posture directly to `INDETERMINATE` without lawful evaluation; all dimensions satisfied directly to candidate sufficiency; completed evaluation directly to attestation, receiver answerable receipt, presence re-evaluation, downstream authorization, or any later route; same-candidate silent rerun; complete evaluation to later dimension extension; changed files or newly noticed evidence to automatic re-evaluation.

The predecessor's blocked conversions remain blocked: evaluation-boundary permission directly to completed evaluation; candidate reception directly to evaluation result; one dimension result to omnibus candidate sufficiency; all dimensions satisfied directly to attestation, receiver answerable receipt, or presence support; any dimension result directly to another dimension result; declaration directly to established fact; filename or directory to custody distinction; receiver label to identity; hash match to semantic sufficiency; timestamp to authority or currentness; device metadata to human identity; physical signal to bodily presence; capture record to attestation; prior-knock correspondence to receipt; evaluation completion or indeterminacy directly to candidate sufficiency or insufficiency; first evaluation to second-candidate evaluation, repeated-evaluation permission, or reusable route; selected candidate to retroactive contaminated-lineage validation; repository scan, file discovery, affected-file repair, and validation-enforcement routes; and evaluation to presence support, presence authorization, presence establishment, presence recording, identity, relation, coupling, FIELD machinery, runtime, API, public intake, authority, standing, truth, continuity memory, output, action, synchronization, or follow-on work.

## 25. Preserved Non-Claims

Default operation posture preserves every predecessor non-claim:

- `receiver_side_answerable_basis_candidate_evaluation_operation_recorded = false`
- `receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded = false`
- `receiver_side_answerable_basis_candidate_evaluation_operation_result = NOT_EVALUATED`
- `receiver_side_answerable_basis_candidate_evaluated = false`
- `receiver_side_answerable_basis_candidate_all_dimensions_satisfied = false`
- `receiver_side_answerable_basis_candidate_any_dimension_not_satisfied = false`
- `receiver_side_answerable_basis_candidate_any_dimension_indeterminate = false`
- `receiver_side_answerable_basis_candidate_sufficient = false`
- `receiver_side_answerable_basis_candidate_insufficient = false`
- `receiver_side_answerable_basis_candidate_indeterminate = false`
- `receiver_attestation_created = false`
- `receiver_attestation_supported = false`
- `receiver_answerable_receipt_present = false`
- `presence_supported = false`
- `presence_authorized = false`
- `presence_established = false`
- `presence_recorded = false`
- `second_candidate_received = false`
- `second_candidate_evaluated = false`
- `repeated_evaluation_permission_created = false`
- `reusable_route_created = false`
- `follow_on_authorized = false`
- `follow_on_work_authorized = false`

It additionally preserves:

- `evaluation_basis_supplied = false`
- `evaluation_basis_complete = false`
- `all_dimension_basis_records_present = false`
- `all_dimension_basis_records_bounded = false`
- `all_dimension_basis_records_reference_selected_candidate = false`
- `all_dimension_basis_records_reference_selected_boundary = false`
- `all_dimension_basis_records_non_result_preclaiming = false`
- `all_dimension_basis_records_admissible = false`
- `candidate_evaluation_operation_exhausted = false`
- `same_candidate_re_evaluation_authorized = false`
- `dimension_completion_route_created = false`
- `partial_dimension_evaluation_recorded = false`
- `caller_supplied_dimension_result_accepted = false`
- `candidate_sufficiency_boundary_created = false`
- `receiver_attestation_boundary_created = false`
- `receiver_answerable_receipt_boundary_created = false`
- `presence_re_evaluation_boundary_created = false`

Every dimension remains `NOT_EVALUATED` in this specification itself. No false non-claim is listed as true.

## 26. Relation to Contaminated Lineage

Contaminated lineage remains unchanged. Unsupported claims remain unsupported. This specification does not repair, edit, delete, overwrite, replace, validate, redeem, clean, or reinterpret contaminated-lineage material.

## 27. What Remains Open

- V2 candidate evaluation operation resolver, test, and live artifact
- separately supplied eight-dimension evaluation basis
- actual candidate evaluation and dimension-specific derived results
- candidate-sufficiency boundary, if separately selected
- receiver-attestation boundary, receiver-answerable-receipt boundary, and presence re-evaluation, only after later lawful basis
- identity, relation, coupling, FIELD machinery, runtime, API, authority, standing, output, action, synchronization, and follow-on work

Open means not scheduled, not authorized, and not executed. Open does not mean next unless separately selected.

## 28. Closing Lock

This V2 specification preserves the same one-candidate, eight-dimension evaluation operation first externalized by spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_V0_MIN_SPEC.md while leaving that predecessor unchanged. It does not itself evaluate the selected candidate, admit live evaluation basis, derive a dimension result, record evaluation completion, decide candidate sufficiency, create receiver attestation or receiver answerable receipt, support or re-evaluate presence, or authorize downstream work. A future resolver must preflight the complete bounded basis for all eight dimensions before evaluating any dimension. Incomplete bounded basis may produce REQUIRES_EVALUATION_BASIS without evaluating any dimension. Partial evaluation may not stand. Once complete basis is admitted, all eight dimensions must be evaluated exactly once. Each dimension result must be derived by the resolver as SATISFIED, NOT_SATISFIED, or INDETERMINATE; caller-supplied result labels are not admissible results. If one or more dimensions are INDETERMINATE, the operation result must be RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE. Otherwise, after all eight dimensions are evaluated, the operation may record RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED, including when one or more dimensions are NOT_SATISFIED. Neither result establishes candidate sufficiency, candidate insufficiency, candidate-level indeterminacy, receiver attestation, receiver answerable receipt, or presence support. All dimensions satisfied is not candidate sufficiency. Any dimension not satisfied is not candidate insufficiency. Dimension-level indeterminacy is not candidate-level indeterminacy. The completed operation exhausts after one eight-dimension evaluation and creates no second-evaluation permission, reusable route, or later-completion route. The only immediate downstream family that may later be considered is one separately bounded candidate-sufficiency boundary. No sufficiency, attestation, receipt, presence, identity, relation, coupling, FIELD machinery, runtime, API, authority, standing, output, action, synchronization, or follow-on route is authorized by this specification. Open means not scheduled, not authorized, and not executed.
