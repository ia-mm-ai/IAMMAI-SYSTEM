# Receiver-Side Answerable Basis Receiver Attestation Operation Basis Declaration Preparation Request V0 Minimum Specification

## 1. Purpose

This specification defines one minimum preparation request for one separately prepared source-body declaration candidate containing the exact receiver-attestation-operation basis family required by `spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_V0_MIN_SPEC.md`.

It answers only:

May one bounded source-body preparer be asked to prepare one declaration candidate for the separately supplied receiver-attestation-operation basis required by the selected waiting operation?

Yes, but only as one bounded request to prepare a declaration candidate. This specification does not create a request artifact, perform preparation, complete basis authorship, declare or admit basis, supply basis to the operation, execute or exhaust the operation, preselect an operation result, create receiver attestation or receiver-answerable receipt, or establish presence, identity, authority, truth, or standing.

## 2. Preparation-Request Identity and Scope

- `preparation_request_id = receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_001`
- `preparation_request_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST`
- `preparation_request_version = 0.1.0`
- `preparation_request_scope = REQUEST_PREPARATION_OF_ONE_SOURCE_BODY_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_ONLY`

These identifiers define one preparation-request contract only. They do not record an actual request or establish that preparation has begun.

## 3. Selected Operation and Candidate

The request is bound to exactly:

- `selected_receiver_attestation_operation_id = receiver_side_answerable_basis_receiver_attestation_operation_001`
- `selected_receiver_attestation_operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION`
- `selected_receiver_attestation_operation_version = 0.1.0`
- `selected_receiver_attestation_operation_scope = ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY`
- `receiver_side_answerable_basis_candidate_id = receiver_side_answerable_basis_candidate_001`
- `receiver_side_answerable_basis_candidate_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE`
- `receiver_side_answerable_basis_candidate_scope = ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`

Alternate operation or candidate identities are inadmissible.

## 4. Required Waiting Standing

The request may reference only this exact written waiting artifact:

`artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_attestation_operation_v0_min/receiver_side_answerable_basis_receiver_attestation_operation_001__receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result.json`

The artifact must parse and preserve:

- `resolver_module = resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min`
- `result_version = 0.1.0`
- `failed_check_count = 0`
- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_REQUIRES_OPERATION_BASIS`
- `operation_result = null`
- `basis_supplied = false`
- `basis_admitted = false`
- `block.blocked = false`
- `upstream_boundary_validated = true`
- `receiver_attestation_operation_recorded = false`
- `receiver_attestation_operation_result_recorded = false`
- `receiver_attestation_operation_exhausted = false`
- `receiver_attestation_decided = false`
- `receiver_attestation_recorded = false`
- `receiver_attestation_not_recorded = false`
- `receiver_attestation_indeterminate = false`
- `result_level_non_claims_canonical_false = true`
- `complete_upstream_boundary_artifact_omitted = true`
- `complete_candidate_sufficiency_artifact_omitted = true`
- `complete_candidate_sufficiency_basis_omitted = true`
- `complete_operation_basis_omitted = true`
- `archive_bytes_omitted = true`
- `text_component_bodies_omitted = true`
- `recorded_signal_body_omitted = true`

The waiting artifact is upstream standing only. This preparation request must not reopen, rerun, reinterpret, replace, mutate, or exhaust the waiting operation.

## 5. Request and Source-Body Distinctions

This is a request to prepare a declaration candidate only:

- request is not preparation completion;
- preparation is not basis-authorship completion;
- preparation is not declaration;
- declaration is not operation supply;
- operation supply is not basis admission;
- basis admission is not operation execution;
- operation execution is not operation result;
- operation result is not receiver-answerable receipt or presence.

The receiver-originating occurrence is outside the source body. The preserved capture package is a trace of that occurrence, not the occurrence itself. The source body may later prepare an accountable evaluation basis concerning the trace. Source-body preparation does not make the trace receiver-originating and does not independently verify the occurrence.

Source-body preparation does not establish receiver identity, custody, provenance, physical validity, current presence, truth, authority, or standing.

## 6. Requested Declaration-Candidate Schema

The request may ask for one later declaration candidate containing exactly these 21 operation-basis fields:

1. `selected_receiver_attestation_boundary_artifact_path`
2. `bounded_capture_directory_path`
3. `preserved_archive_path`
4. `archive_hash_record_path`
5. `expected_archive_sha256`
6. `attestation_statement_path`
7. `attestation_timestamp_path`
8. `capture_method_path`
9. `capture_only_statement_path`
10. `freely_given_statement_path`
11. `knock_reference_path`
12. `receiver_label_path`
13. `receiver_working_directory_path`
14. `recorded_signal_path`
15. `evaluator_reference`
16. `trace_integrity_postures`
17. `ambiguity_postures`
18. `contradiction_postures`
19. `unresolved_postures`
20. `non_conversion_statement`
21. `basis_non_claims`

The preparation request may identify this schema, its exact governing references, and its required posture-key families. It must not populate these fields as completed basis values, represent the basis as prepared or declared, or select an operation result.

The declaration candidate must not embed archive bytes, complete textual component bodies, complete recorded-signal data, complete upstream artifacts, or the complete candidate-sufficiency basis.

## 7. Exact Bounded Source References

A later declaration candidate may refer only to this exact bounded source family:

- selected v2 boundary artifact: `artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2/receiver_side_answerable_basis_receiver_attestation_boundary_001__receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result.json`
- bounded capture directory: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001`
- preserved archive: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/original_zip/receiver_attestation_001.zip`
- archive-hash record: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/hashes/receiver_attestation_001.sha256`
- expected archive SHA-256: `a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c`
- attestation statement: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/attestation_statement.txt`
- attestation timestamp: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/attested_at.txt`
- capture method: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/capture_method.txt`
- capture-only statement: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/capture_only_statement.txt`
- freely-given statement: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/freely_given_statement.txt`
- knock reference: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/knock_reference.txt`
- receiver label: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/receiver_label.txt`
- receiver working-directory declaration: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/receiver_working_directory.txt`
- recorded-signal artifact: `artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/knock_20260727_215052.json`

Listing a path or hash is not file validation, basis preparation, basis declaration, provenance verification, identity establishment, truth establishment, presence establishment, authority, or standing.

## 8. Required Posture-Key Families

A later declaration candidate must use exact Boolean maps with these keys.

`trace_integrity_postures`:

- `exact_boundary_reference_preserved`
- `exact_capture_directory_reference_preserved`
- `exact_component_references_preserved`
- `archive_correspondence_claimed`
- `required_text_components_declared_complete`
- `recorded_signal_artifact_declared_present`
- `complete_archive_not_embedded`
- `complete_signal_body_not_embedded`

`ambiguity_postures`:

- `material_trace_ambiguity_present`
- `timestamp_interpretation_ambiguous`
- `component_correspondence_ambiguous`

`contradiction_postures`:

- `material_trace_contradiction_present`
- `archive_correspondence_contradicted`
- `component_correspondence_contradicted`

`unresolved_postures`:

- `trace_integrity_materially_unresolved`
- `archive_correspondence_materially_unresolved`
- `component_correspondence_materially_unresolved`

The preparation request does not assign values to these maps. Ambiguity, contradiction, and unresolved posture must remain available for truthful later declaration without forced closure.

The canonical later-basis non-conversion statement is exactly:

`bounded trace admission and recording do not establish occurrence creation, identity, independent custody, verified provenance, physical validity, current presence, receiver-answerable receipt, truth, authority, or standing.`

The later `basis_non_claims` map must contain exactly the false basis non-claims required by Section 14 of the governing operation specification. `receiver_attestation_recorded` is not a basis non-claim and must not be supplied by a preparer.

## 9. Requirements for Later Preparation

A later separately selected source-body preparation act must:

- read only the exact declared bounded paths;
- perform no repository-wide scan or alternate-file discovery;
- compute or verify bounded correspondence only as permitted by the operation contract;
- preserve the exact Boolean posture maps;
- preserve ambiguity, contradiction, and unresolved posture without forced closure;
- provide one non-empty bounded evaluator reference;
- preserve the canonical non-conversion statement;
- preserve the exact false basis non-claims;
- omit complete archive, text-component, recorded-signal, upstream-artifact, and candidate-sufficiency-basis bodies;
- avoid caller-selected operation outcomes and results.

This specification performs none of those preparation acts.

## 10. Outcome and Result Families

The preparation-request outcome family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_NOT_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_BLOCKED`

The preparation-request result family is exactly:

- `RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_RECORDED`
- `RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_NOT_RECORDED`
- `NOT_EVALUATED`

`RECORDED`, `NOT_RECORDED`, and `INDETERMINATE` receiver-attestation operation results are not preparation-request results.

A recorded preparation request means only that one later bounded preparation act may be considered. It does not mean a preparer accepted the request, preparation began or completed, a basis or declaration exists, basis may be supplied, or the operation may execute.

## 11. Recording and Branch Postures

A preparation request may be recorded only when:

- the preparation-request, operation, and candidate identities are exact;
- the exact waiting artifact is referenced and its standing is clean;
- the requested declaration-candidate schema is exact;
- the bounded source-reference family is exact;
- the requested posture-key families and non-conversion sentence are exact;
- no completed basis value, source body, operation result, or downstream result is supplied or preclaimed;
- all required request non-claims are exactly Boolean false.

A completed recorded request may set only:

- `preparation_request_recorded = true`
- `preparation_request_result_recorded = true`
- `preparation_request_exhausted = true`
- `basis_declaration_preparation_requested = true`

It must keep:

- `basis_declaration_preparation_started = false`
- `basis_declaration_preparation_completed = false`
- `receiver_attestation_operation_basis_prepared = false`
- `receiver_attestation_operation_basis_declared = false`
- `receiver_attestation_operation_basis_supplied = false`
- `receiver_attestation_operation_basis_admitted = false`
- `receiver_attestation_operation_recorded = false`
- `receiver_attestation_operation_result_recorded = false`
- `receiver_attestation_operation_exhausted = false`
- `receiver_attestation_decided = false`
- `receiver_attestation_recorded = false`
- `receiver_attestation_not_recorded = false`
- `receiver_attestation_indeterminate = false`

A completed not-recorded request must set:

- `preparation_request_recorded = false`
- `preparation_request_result_recorded = true`
- `preparation_request_exhausted = true`
- `basis_declaration_preparation_requested = false`

It records no preparation permission and remains false for every completed-operation posture. A blocked request remains unrecorded, result-unrecorded, unexhausted, and false for `basis_declaration_preparation_requested`.

## 12. Required False Non-Claims

Every preparation-request result must preserve exactly Boolean false for at least:

- `receiver_attestation_created`
- `receiver_attestation_supported`
- `receiver_attestation_recorded`
- `receiver_attestation_not_recorded`
- `receiver_attestation_indeterminate`
- `receiver_answerable_receipt_present`
- `receiver_answerable_receipt_boundary_created`
- `presence_supported`
- `presence_authorized`
- `presence_established`
- `presence_recorded`
- `presence_re_evaluation_boundary_created`
- `identity_created`
- `authority_created`
- `standing_created`
- `truth_created`
- `relation_created`
- `coupling_assigned`
- `coupling_created`
- `field_machinery_created`
- `runtime_created`
- `api_created`
- `public_interface_created`
- `public_intake_created`
- `output_authorized`
- `action_authorized`
- `synchronization_authorized`
- `follow_on_authorized`
- `follow_on_work_authorized`
- `repeated_receiver_attestation_operation_basis_declaration_preparation_request_permission_created`
- `reusable_receiver_attestation_operation_basis_declaration_preparation_route_created`
- `same_receiver_attestation_operation_basis_declaration_preparation_request_rerun_authorized`
- `automatic_receiver_attestation_operation_basis_declaration_preparation_request_retry_created`
- `receiver_attestation_operation_basis_declaration_preparation_request_debt_created`
- `receiver_attestation_operation_basis_declaration_preparation_request_obligation_created`
- `prior_unsupported_candidate_a_claim_validated`
- `prior_unsupported_candidate_b_claim_validated`
- `prior_unsupported_derivation_event_claim_validated`
- `affected_file_repaired`
- `repository_scan_performed`
- `file_discovery_performed`
- `validation_enforced`

No false non-claim may be listed as true.

## 13. Blocking Rules

Invalid waiting standing or an invalid preparation-request contract must produce:

- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_BLOCKED`
- `request_result = NOT_EVALUATED`
- `preparation_request_recorded = false`
- `preparation_request_result_recorded = false`
- `preparation_request_exhausted = false`
- `basis_declaration_preparation_requested = false`

The following conversions must block:

- waiting operation directly to prepared basis;
- waiting operation directly to basis declaration;
- preparation request directly to preparation completion;
- preparation request directly to basis standing;
- preparation request directly to operation supply, admission, execution, exhaustion, or result;
- capture-package existence directly to prepared or declared basis;
- hash or path reference directly to verified provenance, identity, truth, presence, authority, or standing;
- preparation request directly to receiver attestation, receiver-answerable receipt, or presence;
- completed request directly to repeat permission, reusable route, silent rerun, automatic retry, debt, obligation, scheduled preparation, or automatic next step;
- this request directly to repair or validation of contaminated lineage.

Malformed identity, alternate path, unknown field, completed-basis preclaim, operation-result preclaim, source-body embedding, non-claim flip, repository scan request, file-discovery request, or contaminated-lineage conversion must block.

## 14. Exhaustion and Single Use

The preparation request becomes exhausted only after one complete request result is recorded. Request exhaustion means only that this one request decision is complete.

Request exhaustion does not mean preparation has begun or completed, a declaration or basis exists, basis may be supplied or admitted, the operation may execute, or another step is authorized.

A completed request creates no repeated preparation-request permission, reusable preparation route, same-request silent rerun, automatic retry, debt, obligation, scheduled preparation, or automatic next step. Changed files or newly noticed evidence do not authorize repetition.

## 15. Permitted Future Route

Only after a later separately implemented resolver records the preparation request as `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST_RECORDED` may one separate source-body preparation artifact be considered.

That later preparation remains separately bounded and optional. It does not follow automatically from this specification or from artifact availability. This specification does not create, authorize, select, schedule, or perform that preparation. Open does not mean next.

## 16. Relation to Existing Lineage

The receiver-attestation consideration boundary v2, the receiver-attestation-operation contract, the 18-test operation suite, the clean waiting artifact, the waiting terminal summary, the candidate-sufficiency lineage, the bounded capture lineage, and all contaminated lineage remain unchanged.

This specification does not repair, reinterpret, validate, replace, or normalize any earlier request, preparation, declaration, basis, operation, artifact, result, test, resolver, specification, or terminal summary. It does not convert preserved unsupported candidate or derivation claims into valid standing.

## 17. What Remains Open

Open and unexecuted:

- preparation-request resolver;
- preparation-request test;
- preparation-request live artifact;
- source-body basis preparation;
- basis declaration;
- basis submission;
- receiver-attestation operation execution with separately supplied basis;
- `RECORDED`, `NOT_RECORDED`, or `INDETERMINATE` receiver-attestation operation result;
- receiver-answerable receipt;
- presence re-evaluation;
- identity;
- authority;
- truth;
- standing;
- relation;
- coupling;
- FIELD machinery;
- runtime;
- API;
- output;
- action;
- synchronization;
- follow-on work.

Open means not selected, not scheduled, not authorized, and not executed.

## 18. Closing Lock

This specification defines one source-body receiver-attestation-operation basis-declaration preparation-request contract only. It asks only whether one bounded declaration candidate may later be prepared for the exact selected waiting operation from the exact bounded source-reference family.

It creates no live request, preparation act, prepared basis, declaration, basis supply, basis admission, operation execution, operation result, receiver attestation, receiver-answerable receipt, presence, identity, authority, truth, standing, reusable route, retry, debt, obligation, repair, validation, or follow-on standing.
