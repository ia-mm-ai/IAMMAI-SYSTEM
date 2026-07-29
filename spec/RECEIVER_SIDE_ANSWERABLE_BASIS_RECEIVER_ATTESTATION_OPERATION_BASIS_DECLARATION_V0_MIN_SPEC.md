# Receiver-Side Answerable Basis Receiver Attestation Operation Basis Declaration V0 Minimum Specification

## 1. Purpose

This specification defines one minimum bounded declaration act for declaring one exact prepared receiver-attestation-operation basis declaration candidate.

The declaration may consume only the exact written `PREPARED` preparation artifact named in Section 3. It may determine only whether the exact 21-field candidate contained in that artifact may be recorded as one declared receiver-attestation-operation basis.

This is declaration-specification-only work. It does not perform declaration, repeat preparation, recompute archive correspondence, reread bounded capture files, reconstruct or alter the candidate, supply or admit basis, execute or exhaust the receiver-attestation operation, select or record an operation result, record receiver attestation, create receiver-answerable receipt, or establish presence, identity, custody, provenance, physical validity, authority, truth, or standing.

## 2. Declaration Identity and Selected Line

The declaration identity is exactly:

- `declaration_id = receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_001`
- `declaration_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION`
- `declaration_version = 0.1.0`
- `declaration_scope = DECLARE_ONE_EXACT_PREPARED_RECEIVER_ATTESTATION_OPERATION_BASIS_CANDIDATE_ONLY`
- `governing_declaration_specification_path = spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_V0_MIN_SPEC.md`

The selected preparation identity is exactly:

- `selected_preparation_id = receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_001`
- `selected_preparation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION`
- `selected_preparation_version = 0.1.0`
- `selected_preparation_scope = PREPARE_ONE_SOURCE_BODY_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_ONLY`

The selected preparation-request identity carried by that preparation is exactly:

- `selected_preparation_request_id = receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_001`
- `selected_preparation_request_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_REQUEST`
- `selected_preparation_request_version = 0.1.0`
- `selected_preparation_request_scope = REQUEST_PREPARATION_OF_ONE_SOURCE_BODY_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_ONLY`

The selected operation identity is exactly:

- `selected_receiver_attestation_operation_id = receiver_side_answerable_basis_receiver_attestation_operation_001`
- `selected_receiver_attestation_operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION`
- `selected_receiver_attestation_operation_version = 0.1.0`
- `selected_receiver_attestation_operation_scope = ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY`

The selected candidate identity is exactly:

- `receiver_side_answerable_basis_candidate_id = receiver_side_answerable_basis_candidate_001`
- `receiver_side_answerable_basis_candidate_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE`
- `receiver_side_answerable_basis_candidate_scope = ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`

These values select one declaration decision only. Alternate identities or scopes are inadmissible.

## 3. Exact Selected Preparation Artifact

The declaration may consume only:

`artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min/receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_001__receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result.json`

The artifact must parse as one mapping and validate exactly:

- `resolver_module = resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min`
- `result_version = 0.1.0`
- `failed_check_count = 0`
- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_PREPARATION_PREPARED`
- `preparation_result = RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_PREPARED`
- `decision_code = CANDIDATE_PREPARED`
- `block.blocked = false`
- `preparation_recorded = true`
- `preparation_result_recorded = true`
- `preparation_exhausted = true`
- `basis_declaration_preparation_started = true`
- `basis_declaration_preparation_completed = true`
- `receiver_attestation_operation_basis_declaration_candidate_prepared = true`
- `receiver_attestation_operation_basis_prepared = true`
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
- `result_level_non_claims_canonical_false = true`
- `complete_material_omitted = true`

The preparation result and preparation postures may be carried in the artifact's selected preparation object. Validation must follow the artifact's exact wrapper and selected-object structure without broad recursive key search.

The selected preparation request, operation, and candidate identities carried by the preparation artifact must match Section 2 and the exact recorded preparation-request identity. The declaration must not reopen, rerun, replace, reinterpret, mutate, or re-exhaust the completed preparation.

## 4. Declaration Question and Standing Distinctions

The declaration question is:

May the exact prepared 21-field receiver-attestation-operation basis declaration candidate be recorded as one declared basis?

This is declaration only.

The following distinctions are mandatory:

- prepared candidate is not declared basis;
- declaration records repository standing for the exact prepared candidate only;
- declaration does not alter the candidate;
- declaration does not independently verify the receiver-originating occurrence;
- declaration does not establish receiver identity, custody, provenance, physical validity, current presence, authority, truth, or standing;
- declared basis is not supplied basis;
- supplied basis is not admitted basis;
- admitted basis is not operation execution;
- operation execution is not operation result;
- operation result is not receiver-answerable receipt;
- open does not mean next.

The declaration must not convert preparation completion, candidate shape, path correspondence, archive correspondence, or clean posture maps into any downstream result or standing.

## 5. Declaration Request Contract

A later resolver request must identify exactly the declaration, selected preparation, selected operation, selected candidate, governing specification, and selected preparation-artifact path defined by Sections 2 and 3.

The request must use one exact Boolean selection field:

- `basis_declaration_selected`

Its canonical default is exactly `true`.

- exact `true` selects the `DECLARED` branch after all validation passes;
- exact `false` selects the lawful `NOT_DECLARED` branch after all validation passes;
- null, integers including `0` and `1`, strings, sequences, mappings, or any other non-Boolean value block.

The request must carry canonical declared non-claims, each exactly Boolean `false`. It must not carry:

- a replacement or caller-supplied candidate;
- caller-selected posture maps;
- a declaration outcome or declaration result;
- an operation outcome or operation result;
- prior declaration, supply, admission, execution, or downstream standing;
- complete source bodies;
- a repository scan, glob, discovery, fallback, sibling search, or alternate-source instruction;
- a prohibited conversion, repeat permission, reusable route, rerun, retry, debt, obligation, scheduled supply, or automatic next step.

Unknown request fields, missing required fields, wrong types, or non-canonical values block.

## 6. Exact Prepared-Candidate Contract

The declaration may accept only the exact `prepared_declaration_candidate` mapping in the selected preparation artifact. It must contain exactly these 21 fields:

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

No field may be missing, added, altered, normalized, reconstructed, reordered into a different semantic object, or caller-substituted. The declaration specification does not duplicate the full live candidate values because the exact selected preparation-artifact reference and exact schema are sufficient.

The first 14 reference values must be exactly equal to the corresponding values in the selected prepared candidate. `evaluator_reference` must be exactly equal to the preparation evaluator reference. The declaration must not independently resolve, normalize, rediscover, or validate those paths against source files.

## 7. Exact Candidate Validation

Candidate validation is structural and equality-based only. It must establish:

- the candidate has exactly 21 fields;
- every candidate field is deeply equal to the corresponding prepared-candidate field;
- the candidate is preparation output from the exact selected preparation artifact;
- all four posture maps have exact key families and exact Boolean values;
- the non-conversion statement is exact;
- `basis_non_claims` has the exact governing operation key family and every value is exactly Boolean `false`;
- `receiver_attestation_recorded` is absent from `basis_non_claims`;
- no complete archive, complete text-component body, or complete recorded-signal body is embedded.

The exact live `trace_integrity_postures` are:

- `exact_boundary_reference_preserved = true`
- `exact_capture_directory_reference_preserved = true`
- `exact_component_references_preserved = true`
- `archive_correspondence_claimed = true`
- `required_text_components_declared_complete = true`
- `recorded_signal_artifact_declared_present = true`
- `complete_archive_not_embedded = true`
- `complete_signal_body_not_embedded = true`

The exact live `ambiguity_postures` are:

- `material_trace_ambiguity_present = false`
- `timestamp_interpretation_ambiguous = false`
- `component_correspondence_ambiguous = false`

The exact live `contradiction_postures` are:

- `material_trace_contradiction_present = false`
- `archive_correspondence_contradicted = false`
- `component_correspondence_contradicted = false`

The exact live `unresolved_postures` are:

- `trace_integrity_materially_unresolved = false`
- `archive_correspondence_materially_unresolved = false`
- `component_correspondence_materially_unresolved = false`

False ambiguity, contradiction, or unresolved posture does not create identity, provenance, truth, authority, presence, or standing.

The exact non-conversion statement is:

`bounded trace admission and recording do not establish occurrence creation, identity, independent custody, verified provenance, physical validity, current presence, receiver-answerable receipt, truth, authority, or standing.`

The exact `basis_non_claims` key family is:

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

Every value in this map must be exactly Boolean `false`. No declaration-only or additional key is permitted. The declaration must not independently recompute any candidate finding.

## 8. Outcome, Result, and Precedence

The declaration outcome family is exactly:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_DECLARED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_NOT_DECLARED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_BLOCKED`

The declaration result family is exactly:

- `RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED`
- `RECEIVER_ATTESTATION_OPERATION_BASIS_NOT_DECLARED`
- `NOT_EVALUATED`

Deterministic precedence is:

1. structural or constitutional invalidity produces `BLOCKED` and `NOT_EVALUATED`;
2. otherwise, exact valid declaration input with `basis_declaration_selected = false` produces `NOT_DECLARED`;
3. otherwise, exact valid declaration input with `basis_declaration_selected = true` produces `DECLARED`.

No caller-selected declaration result is admissible. A declaration result is derived only after exact upstream and candidate validation.

## 9. Declared Branch

`DECLARED` may stand only when:

- declaration identity and scope are exact;
- selected preparation, operation, and candidate identities are exact;
- the exact preparation artifact is valid and `PREPARED`;
- the exact 21-field candidate is present and unchanged;
- all candidate maps, the statement, and basis non-claims are exact;
- no prior declaration, supply, admission, operation execution, operation result, or downstream standing is present;
- `basis_declaration_selected` is exactly `true`;
- no prohibited conversion is requested.

A declared result records:

- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_DECLARED`
- `declaration_result = RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED`
- `block.blocked = false`
- `declaration_recorded = true`
- `declaration_result_recorded = true`
- `declaration_exhausted = true`
- `receiver_attestation_operation_basis_declaration_recorded = true`
- `receiver_attestation_operation_basis_declared = true`

It keeps exactly false:

- `receiver_attestation_operation_basis_supplied`
- `receiver_attestation_operation_basis_admitted`
- `receiver_attestation_operation_recorded`
- `receiver_attestation_operation_result_recorded`
- `receiver_attestation_operation_exhausted`
- `receiver_attestation_decided`
- `receiver_attestation_recorded`
- `receiver_attestation_not_recorded`
- `receiver_attestation_indeterminate`

A declared result may include one exact immutable candidate reference or one `declared_receiver_attestation_operation_basis` mapping deeply equal to the prepared candidate. It must not include a transformed, normalized, reconstructed, or expanded candidate.

Declared means only that the exact prepared candidate has declaration standing in this declaration artifact. It does not mean basis supplied, basis admitted, operation authorized, operation executed, receiver attestation recorded, receiver-answerable receipt present, or presence or standing established.

## 10. Not-Declared Branch

`NOT_DECLARED` may stand only when all declaration structure, upstream preparation standing, and candidate validation are exact; `basis_declaration_selected` is exactly `false`; and no blocking condition or prohibited conversion exists.

A not-declared result records:

- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_NOT_DECLARED`
- `declaration_result = RECEIVER_ATTESTATION_OPERATION_BASIS_NOT_DECLARED`
- `block.blocked = false`
- `declaration_recorded = true`
- `declaration_result_recorded = true`
- `declaration_exhausted = true`
- `receiver_attestation_operation_basis_declaration_recorded = false`
- `receiver_attestation_operation_basis_declared = false`

No declared-basis object, basis supply, admission, operation execution, operation result, or downstream posture may become true.

`NOT_DECLARED` does not mean preparation failed, the candidate is fabricated, the receiver-originating occurrence did not happen, the receiver is false, candidate sufficiency is revoked, or the receiver-attestation operation produced `NOT_RECORDED` or `INDETERMINATE`.

## 11. Blocked Branch

Structural or constitutional invalidity produces:

- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_BLOCKED`
- `declaration_result = NOT_EVALUATED`
- `declaration_recorded = false`
- `declaration_result_recorded = false`
- `declaration_exhausted = false`
- `receiver_attestation_operation_basis_declaration_recorded = false`
- `receiver_attestation_operation_basis_declared = false`
- `block.blocked = true`

The declaration must block at least:

- malformed or non-mapping declaration input;
- incorrect declaration, preparation, preparation-request, operation, or candidate identity;
- incorrect governing specification path;
- incorrect preparation-artifact path;
- missing, unreadable, malformed, mismatched, blocked, failed, non-`PREPARED`, or unexhausted preparation artifact;
- preparation artifact without one exact 21-field candidate;
- altered, missing, additional, normalized, reconstructed, or caller-substituted candidate field;
- caller-supplied replacement candidate;
- caller-selected posture map, declaration outcome, declaration result, operation outcome, or operation result;
- altered evaluator reference or non-conversion statement;
- missing, added, wrong-type, or flipped basis non-claim;
- prior basis declaration, basis supply, basis admission, operation execution, or operation result;
- complete source-body embedding;
- repository scan, globbing, file discovery, fallback lookup, sibling search, or alternate-source substitution;
- receiver attestation, receipt, presence, identity, custody, provenance, physical validity, authority, truth, standing, relation, coupling, output, action, synchronization, repair, validation, or follow-on conversion;
- repeat permission, reusable route, rerun, retry, debt, obligation, scheduled supply, or automatic-next-step creation.

A blocked result records no partial declaration or declared-basis standing.

## 12. Omission and Result-Level Non-Claims

Every declaration result must omit:

- the complete preparation-request artifact;
- the complete waiting-operation artifact;
- the complete upstream boundary artifact;
- the complete candidate-sufficiency artifact;
- the complete candidate-sufficiency basis;
- archive bytes;
- complete text-component bodies;
- the complete recorded-signal body.

A result may include compact preparation-artifact validation metadata, exact declaration identity, declaration-result posture, canonical non-claims, omission posture, and the exact candidate or exact immutable candidate reference permitted by Section 9. It must record `complete_material_omitted = true`.

Every branch must record `result_level_non_claims_canonical_false = true` and keep these operation postures exactly false:

- `receiver_attestation_operation_basis_supplied`
- `receiver_attestation_operation_basis_admitted`
- `receiver_attestation_operation_recorded`
- `receiver_attestation_operation_result_recorded`
- `receiver_attestation_operation_exhausted`
- `receiver_attestation_decided`
- `receiver_attestation_recorded`
- `receiver_attestation_not_recorded`
- `receiver_attestation_indeterminate`

Every branch must preserve at least these result-level non-claims as exactly Boolean `false`:

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
- `repeated_receiver_attestation_operation_basis_declaration_permission_created`
- `reusable_receiver_attestation_operation_basis_declaration_route_created`
- `same_receiver_attestation_operation_basis_declaration_rerun_authorized`
- `automatic_receiver_attestation_operation_basis_declaration_retry_created`
- `receiver_attestation_operation_basis_declaration_debt_created`
- `receiver_attestation_operation_basis_declaration_obligation_created`
- `prior_unsupported_candidate_a_claim_validated`
- `prior_unsupported_candidate_b_claim_validated`
- `prior_unsupported_derivation_event_claim_validated`
- `affected_file_repaired`
- `repository_scan_performed`
- `file_discovery_performed`
- `validation_enforced`

No result-level false non-claim may be listed as true. Branch-specific declaration fields are not universal false non-claims.

## 13. Blocked Conversions

The declaration blocks:

- prepared candidate directly to supplied basis;
- prepared candidate directly to admitted basis;
- declaration directly to operation execution;
- declaration directly to operation result;
- declaration directly to receiver-attestation recording;
- candidate posture maps directly to identity, provenance, truth, authority, presence, or standing;
- archive correspondence directly to verified provenance or occurrence truth;
- declaration exhaustion directly to supply authorization;
- completed declaration directly to reusable route, retry, debt, obligation, scheduled supply, or automatic next step;
- declaration directly to repair or validation of contaminated lineage.

No route may bypass one later separate basis-supply act and the receiver-attestation operation's atomic admission gate.

## 14. Exhaustion, Single Use, and Future Route

A completed `DECLARED` or `NOT_DECLARED` result becomes exhausted only after one complete declaration result is recorded. Declaration exhaustion means only that this one declaration decision is complete.

Exhaustion does not authorize basis supply, basis admission, operation execution, another declaration, retry, rerun, or follow-on work.

A completed declaration creates no:

- repeated declaration permission;
- reusable declaration route;
- same-declaration silent rerun;
- automatic retry;
- debt;
- obligation;
- scheduled supply;
- automatic next step.

Only after one later resolver records `RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED` may one separate basis-supply act be considered. This specification does not create, authorize, select, schedule, or perform basis supply.

Open does not mean next.

## 15. Preserved Lineage and Open Work

All receiver-side answerable-basis reception, evaluation, candidate-sufficiency, candidate-sufficiency-basis, receiver-attestation consideration-boundary v1 and v2, waiting receiver-attestation operation, preparation-request, completed preparation, exact 21-field candidate, bounded capture, and contaminated lineage remain unchanged.

The completed v2 boundary artifact and terminal summary, waiting operation artifact and terminal summary, recorded preparation-request artifact and terminal summary, completed preparation artifact and terminal summary, their specifications, resolvers, and tests remain upstream standing only.

This specification does not repair, reinterpret, validate, replace, normalize, mutate, or overwrite any earlier specification, resolver, test, request, preparation, declaration, supplied basis, operation, artifact, result, terminal summary, evidence, proposition, limitation, reference, support posture, contradiction posture, unresolved posture, or contaminated claim.

Open and unexecuted:

- declaration resolver;
- declaration test;
- declaration live artifact;
- basis supply;
- supply resolver and test;
- basis admission;
- receiver-attestation-operation execution;
- `RECORDED`, `NOT_RECORDED`, or `INDETERMINATE` operation result;
- receiver attestation;
- receiver-answerable receipt;
- presence re-evaluation;
- identity;
- custody;
- provenance;
- physical validity;
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

## 16. Closing Lock

This specification defines one bounded declaration contract for one exact prepared receiver-attestation-operation basis declaration candidate. It consumes only the exact written `PREPARED` preparation artifact, validates the exact 21-field candidate by schema and deep equality, and may record only `DECLARED` or `NOT_DECLARED` after structural validation.

It does not repeat preparation, reread bounded capture files, recompute archive correspondence, alter the prepared candidate, supply or admit basis, execute or exhaust the receiver-attestation operation, select or record an operation result, record receiver attestation, create receiver-answerable receipt, establish presence, identity, custody, provenance, physical validity, authority, truth, or standing, create a reusable route, retry, debt, obligation, repair, validation, or follow-on authorization.

Declared basis remains separate from supplied basis. Supplied basis remains separate from admitted basis. Admitted basis remains separate from operation execution. Operation execution remains separate from operation result. Operation result remains separate from receiver-answerable receipt. Open does not mean next.
