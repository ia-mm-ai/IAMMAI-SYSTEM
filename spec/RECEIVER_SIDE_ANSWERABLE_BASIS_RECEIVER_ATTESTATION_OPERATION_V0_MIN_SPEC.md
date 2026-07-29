# Receiver-Side Answerable Basis Receiver Attestation Operation V0 Minimum Specification

## 1. Purpose

This specification defines one minimum operation downstream of the exact completed v2 receiver-attestation consideration boundary. The operation determines whether one bounded receiver-originating attestation trace may be admitted and recorded for the exact selected receiver-side answerable-basis candidate.

The operation does not create the receiver-originating occurrence. It does not treat the preserved capture package as the occurrence itself. It does not independently verify receiver identity, provenance, custody, physical validity, current presence, truth, authority, or standing. It does not create receiver-answerable receipt or presence.

This is operation-spec-only work. It creates no resolver, test, request, supplied basis, artifact, declaration, operation execution, result, receipt boundary, presence route, identity, relation, coupling, FIELD machinery, runtime, API, output, action, synchronization, or follow-on authorization.

## 2. Operation Identity and Scope

- `operation_id = receiver_side_answerable_basis_receiver_attestation_operation_001`
- `operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION`
- `operation_version = 0.1.0`
- `operation_scope = ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY`
- `receiver_side_answerable_basis_receiver_attestation_operation_id = receiver_side_answerable_basis_receiver_attestation_operation_001`
- `receiver_side_answerable_basis_receiver_attestation_operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION`
- `receiver_side_answerable_basis_receiver_attestation_operation_version = 0.1.0`
- `receiver_side_answerable_basis_receiver_attestation_operation_scope = ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY`

These identifiers define one operation contract only. They do not execute the operation or preselect an outcome or result.

## 3. Selected Candidate

- `receiver_side_answerable_basis_candidate_id = receiver_side_answerable_basis_candidate_001`
- `receiver_side_answerable_basis_candidate_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE`
- `receiver_side_answerable_basis_candidate_scope = ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`
- `selected_candidate_sufficiency_operation_id = receiver_side_answerable_basis_candidate_sufficiency_operation_001`
- `selected_candidate_sufficiency_operation_result_required = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT`

The operation is bound to this exact candidate and no other candidate.

## 4. Required Upstream Boundary

The operation consumes only this exact written v2 boundary artifact:

`artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2/receiver_side_answerable_basis_receiver_attestation_boundary_001__receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result.json`

The artifact must parse and record exactly:

- `resolver_module = resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2`
- `result_version = 0.2.0`
- `failed_check_count = 0`
- `boundary_id = receiver_side_answerable_basis_receiver_attestation_boundary_001`
- `boundary_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY`
- `boundary_version = 0.1.0`
- `boundary_scope = CONSIDER_RECEIVER_ATTESTATION_FOR_ONE_SUFFICIENT_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`
- `selected_candidate_id = receiver_side_answerable_basis_candidate_001`
- `selected_sufficiency_operation_id = receiver_side_answerable_basis_candidate_sufficiency_operation_001`
- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_ALLOWED`
- `boundary_result = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_CONSIDERATION_ALLOWED`
- `receiver_attestation_boundary_recorded = true`
- `receiver_attestation_boundary_result_recorded = true`
- `receiver_attestation_consideration_allowed = true`
- `receiver_attestation_consideration_not_allowed = false`
- `receiver_attestation_boundary_exhausted = true`
- `bounded_material_selected_for_consideration = true`
- `specification_markers_validated = true`
- `selected_operation_validated = true`
- `eight_dimensions_validated = true`
- `upstream_false_locks_validated = true`
- `result_level_non_claims_canonical_false = true`
- `complete_operation_artifact_omitted = true`
- `complete_sufficiency_basis_omitted = true`
- `complete_capture_signal_data_omitted = true`

The operation must not reopen, rerun, reinterpret, repair, or extend the completed boundary or candidate-sufficiency operation.

## 5. Bounded Attestation-Trace Source

The only permitted trace source is:

`artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/`

The exact bounded component references are:

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

The operation may read only these exact bounded references. It must not discover alternate files. It must not embed the complete archive or complete recorded-signal body in a request, basis record, check, result, summary, or artifact.

Package existence alone is not sufficient for an attestation result. Filenames, paths, hashes, labels, timestamps, device metadata, signal samples, and capture wording do not independently establish receiver identity, independent custody, verified provenance, physical validity, current presence, truth, authority, standing, or receiver-answerable receipt.

## 6. Required Separation

The operation preserves these stages as distinct:

1. a receiver-originating occurrence outside the source body;
2. a trace produced or preserved from that occurrence;
3. submission or availability of the trace;
4. source-body reception of candidate material;
5. candidate evaluation and candidate sufficiency;
6. receiver-attestation consideration boundary standing;
7. this bounded attestation operation;
8. the operation's recorded result;
9. any later receiver-answerable receipt;
10. any later presence or standing consequence.

Occurrence is not artifact. Artifact does not create the occurrence. Preserved trace is not independent verification. Candidate sufficient is not receiver attestation. Consideration allowed is not receiver attestation. Operation authorization is not operation result. Receiver attestation recorded is not receiver-answerable receipt. Receiver attestation recorded is not presence. Receiver attestation recorded is not identity, authority, truth, or standing.

## 7. Operation Question

Does the exact bounded receiver-attestation trace satisfy the minimum admission-and-recording contract for one receiver attestation associated with the exact selected sufficient candidate?

The operation evaluates only trace admission and recording. It does not evaluate broader physical truth or downstream constitutional consequence.

## 8. Separately Supplied Operation Basis

The operation requires one separately supplied bounded basis. The basis is not the complete capture package, is not the full candidate-sufficiency basis, and must not preselect an operation result.

The basis must contain exactly:

- `selected_receiver_attestation_boundary_artifact_path`
- `bounded_capture_directory_path`
- `preserved_archive_path`
- `archive_hash_record_path`
- `expected_archive_sha256`
- `attestation_statement_path`
- `attestation_timestamp_path`
- `capture_method_path`
- `capture_only_statement_path`
- `freely_given_statement_path`
- `knock_reference_path`
- `receiver_label_path`
- `receiver_working_directory_path`
- `recorded_signal_path`
- `evaluator_reference`
- `trace_integrity_postures`
- `ambiguity_postures`
- `contradiction_postures`
- `unresolved_postures`
- `non_conversion_statement`
- `basis_non_claims`

Every path and hash value must match Section 4 or Section 5 exactly. `evaluator_reference` must be a non-empty bounded reference; it creates no evaluator identity, authority, standing, or truth.

`trace_integrity_postures` must contain exact Boolean values for:

- `exact_boundary_reference_preserved`
- `exact_capture_directory_reference_preserved`
- `exact_component_references_preserved`
- `archive_correspondence_claimed`
- `required_text_components_declared_complete`
- `recorded_signal_artifact_declared_present`
- `complete_archive_not_embedded`
- `complete_signal_body_not_embedded`

`ambiguity_postures` must contain exact Boolean values for:

- `material_trace_ambiguity_present`
- `timestamp_interpretation_ambiguous`
- `component_correspondence_ambiguous`

`contradiction_postures` must contain exact Boolean values for:

- `material_trace_contradiction_present`
- `archive_correspondence_contradicted`
- `component_correspondence_contradicted`

`unresolved_postures` must contain exact Boolean values for:

- `trace_integrity_materially_unresolved`
- `archive_correspondence_materially_unresolved`
- `component_correspondence_materially_unresolved`

The `non_conversion_statement` must state that bounded trace admission and recording do not establish occurrence creation, identity, independent custody, verified provenance, physical validity, current presence, receiver-answerable receipt, truth, authority, or standing.

`basis_non_claims` must contain the exact false set in Section 14. `receiver_attestation_recorded` is not a basis non-claim and must not be supplied by the caller.

## 9. Request and Atomic Admission Gate

Blocked-route validation occurs before basis admission. A request must identify the exact operation, candidate, upstream boundary artifact, governing specification, and bounded capture directory. It must contain canonical false non-claims and prohibited-request flags. It must not contain an outcome, operation result, branch posture, complete archive, complete signal body, or downstream result preclaim.

For an otherwise valid request:

- absent separately supplied operation basis produces the waiting outcome;
- non-mapping, malformed, unknown-field, alternate-identity, alternate-path, result-preclaiming, conversion-seeking, or non-claim-flipping basis blocks;
- caller-supplied operation or dimension results block;
- a false trace-integrity claim where exact positive correspondence is required blocks basis admission;
- missing or non-Boolean posture values block basis admission;
- a hash mismatch under `archive_correspondence_claimed = true` blocks;
- no partial basis admission or partial operation result may stand.

The operation must not automatically reuse the complete candidate-sufficiency basis as attestation-operation basis.

## 10. Required Bounded Checks

After request, specification, upstream, and basis admission, the operation checks only:

- exact upstream boundary standing is valid;
- exact selected candidate identity is preserved;
- all bounded trace paths equal the Section 5 paths;
- the preserved archive exists at the exact path;
- the archive-hash record exists and records the exact expected archive hash;
- computed archive SHA-256 equals the exact expected archive hash;
- all required bounded textual components exist and are readable;
- attestation-statement text is non-empty;
- attestation-timestamp text is non-empty and parses as `attested_at=<RFC3339 UTC timestamp>`;
- capture-method text is non-empty;
- capture-only-statement text is non-empty;
- freely-given-statement text is non-empty;
- knock-reference text is non-empty;
- receiver-label text is non-empty;
- receiver-working-directory declaration text is non-empty;
- the recorded-signal artifact exists at the exact path;
- the complete recorded-signal sample body is neither embedded nor interpreted;
- trace-integrity postures are complete;
- ambiguity, contradiction, and unresolved postures are complete;
- no material contradiction is predeclared as resolved while unresolved;
- no caller-selected result is supplied;
- all required non-conversion postures remain false.

Reading these exact declared paths is bounded validation, not filesystem discovery.

Hash matching confirms artifact correspondence only. It does not prove who produced the artifact, statement truth, physical presence, current presence, independent custody, provenance beyond the recorded package, receiver identity, authority, or standing.

## 11. Outcome and Result Families

The outcome family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_NOT_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_INDETERMINATE`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_REQUIRES_OPERATION_BASIS`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BLOCKED`

The non-null completed operation-result family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_NOT_RECORDED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_INDETERMINATE`

Waiting and blocked outcomes record no operation result. No outcome or result is selected by this specification.

## 12. Decision Rules and Precedence

After the atomic gate passes, result precedence is exactly:

1. If any required ambiguity or unresolved posture is true, record `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_INDETERMINATE`.
2. Otherwise, if any material contradiction posture is true, or any minimum admission check has a completed negative result, record `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_NOT_RECORDED`.
3. Otherwise, if every minimum admission check passes, record `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED`.

`INDETERMINATE` takes precedence over `NOT_RECORDED`; `NOT_RECORDED` takes precedence over `RECORDED`. Exactly one completed result posture may be true. Structural invalidity, path mismatch, result preclaim, or claimed-match hash mismatch blocks before this precedence is applied.

## 13. Branch Postures

Default, waiting, and blocked posture is:

- `receiver_attestation_operation_recorded = false`
- `receiver_attestation_operation_result_recorded = false`
- `receiver_attestation_operation_result = null`
- `receiver_attestation_operation_exhausted = false`
- `receiver_attestation_decided = false`
- `receiver_attestation_recorded = false`
- `receiver_attestation_not_recorded = false`
- `receiver_attestation_indeterminate = false`

For a completed `RECORDED` result:

- `receiver_attestation_operation_recorded = true`
- `receiver_attestation_operation_result_recorded = true`
- `receiver_attestation_operation_exhausted = true`
- `receiver_attestation_decided = true`
- `receiver_attestation_recorded = true`
- `receiver_attestation_not_recorded = false`
- `receiver_attestation_indeterminate = false`
- `receiver_attestation_created = false`

The receiver-originating occurrence was not created by the source body.

For a completed `NOT_RECORDED` result:

- `receiver_attestation_operation_recorded = true`
- `receiver_attestation_operation_result_recorded = true`
- `receiver_attestation_operation_exhausted = true`
- `receiver_attestation_decided = true`
- `receiver_attestation_recorded = false`
- `receiver_attestation_not_recorded = true`
- `receiver_attestation_indeterminate = false`

`NOT_RECORDED` does not mean the external occurrence did not happen, the receiver lied, the candidate is insufficient, the capture package must be deleted, the trace is erased, contaminated lineage is repaired, the receiver is absent, or presence is disproved.

For a completed `INDETERMINATE` result:

- `receiver_attestation_operation_recorded = true`
- `receiver_attestation_operation_result_recorded = true`
- `receiver_attestation_operation_exhausted = true`
- `receiver_attestation_decided = true`
- `receiver_attestation_recorded = false`
- `receiver_attestation_not_recorded = false`
- `receiver_attestation_indeterminate = true`

`INDETERMINATE` means the bounded trace does not support a truthful recorded or not-recorded result under the admitted basis. It is not `NOT_RECORDED`.

## 14. Required False Non-Claims

Every result preserves these fields as exactly false:

- `receiver_attestation_created`
- `receiver_attestation_supported`
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
- `repeated_receiver_attestation_operation_permission_created`
- `reusable_receiver_attestation_operation_route_created`
- `same_receiver_attestation_operation_rerun_authorized`
- `automatic_receiver_attestation_operation_retry_created`
- `receiver_attestation_operation_debt_created`
- `receiver_attestation_operation_obligation_created`
- `prior_unsupported_candidate_a_claim_validated`
- `prior_unsupported_candidate_b_claim_validated`
- `prior_unsupported_derivation_event_claim_validated`
- `affected_file_repaired`
- `repository_scan_performed`
- `file_discovery_performed`
- `validation_enforced`

No false non-claim may be listed as true. `receiver_attestation_recorded` is a branch-specific operation result posture. It defaults to false and may become true only in the completed `RECORDED` branch; it is not a general false non-claim.

## 15. Waiting, Blocking, Exhaustion, and Single Use

If the separately supplied operation basis is absent, the operation outcome is `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_REQUIRES_OPERATION_BASIS`. The operation remains unrecorded, has no result, is not exhausted, and creates no downstream authorization.

Invalid request shape, result preclaim, invalid specification markers, invalid upstream boundary, malformed supplied basis, path mismatch, claimed-match hash mismatch, prohibited conversion, repeated-use request, repair request, scan request, discovery request, or contaminated-lineage validation request produces `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BLOCKED`. A blocked result remains unrecorded, result-unrecorded, unexhausted, and false for all three completed result postures.

The operation becomes exhausted only after exactly one complete `RECORDED`, `NOT_RECORDED`, or `INDETERMINATE` result is recorded. Waiting and blocked postures are not exhausted.

Exhaustion does not authorize receiver-answerable receipt, presence re-evaluation, identity, authority, standing, relation, coupling, output, action, synchronization, or follow-on work.

A completed operation creates no repeated receiver-attestation-operation permission, reusable receiver-attestation route, silent rerun, automatic retry, debt, obligation, or scheduled next step. Changed files or newly noticed evidence do not authorize automatic rerun.

## 16. Blocked Conversions

The operation blocks:

- candidate sufficiency directly to attestation recording;
- consideration allowed directly to attestation recording;
- capture-package existence directly to attestation recording;
- hash match directly to receiver identity, truth, physical presence, current presence, authority, or standing;
- attestation recording directly to receiver-answerable receipt or presence;
- attestation recording directly to identity, authority, truth, standing, relation, or coupling;
- completed operation directly to repeated permission, reusable route, silent rerun, retry, debt, obligation, or automatic next step;
- this operation directly to repair or validation of contaminated lineage.

Contaminated lineage remains preserved. This operation performs no repository scan, file discovery, affected-file repair, replacement, normalization, redemption, or validation enforcement.

## 17. Permitted Future Route and Closing Lock

Only if a later separately executed resolver records `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED` may a receiver-answerable-receipt boundary be considered later.

This specification does not create, authorize, select, schedule, or execute that boundary. A recorded attestation does not itself constitute receiver-answerable receipt. Open does not mean next.

This specification defines only one bounded receiver-attestation operation contract for the exact selected sufficient candidate, exact completed allowed v2 boundary, separately supplied operation basis, and exact bounded trace package. It does not record receiver attestation, create the receiver-originating occurrence, verify identity or provenance, establish presence, truth, authority, or standing, create receipt, authorize repeat use, repair contaminated lineage, or execute follow-on work. Any operation execution, result artifact, receiver-answerable-receipt boundary, presence consequence, or downstream work requires a separate bounded step.
