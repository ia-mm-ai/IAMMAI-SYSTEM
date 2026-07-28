# Receiver-Side Answerable Basis Candidate Evaluation Boundary V0 Minimum Specification

## 1. Purpose

This specification defines one minimum boundary for deciding whether the one successfully received and recorded receiver-side answerable-basis candidate may become eligible for one separately bounded candidate evaluation operation.

It is downstream of the selected successful reception-operation result. It defines evaluation consideration only. It does not perform candidate evaluation, decide sufficiency, insufficiency, or indeterminacy, verify candidate semantics or declared provenance, establish receiver attestation or receiver answerable receipt, decide custody distinctness, refusability, or could-have-been-withheld posture, or re-run or satisfy the presence operation.

## 2. Scope

This is additive, repo-local, boundary-spec-only work. It is subordinate to constitutional and reference authority surfaces and to the governing reception operation, reception-boundary, and presence-operation surfaces.

The boundary concerns one already received candidate only. It does not create a new candidate, receive another candidate, reopen the completed reception operation, evaluate the physical knock signal, infer bodily presence from accelerometer data, or infer a human identity from a device identifier, filesystem path, receiver label, timestamp, hash, capture statement, packet label, directory name, filename, `candidate_kind` value, or the word `attestation`.

It creates no identity, relation, coupling, FIELD machinery, runtime, API, public interface, public intake, mailbox, listener, queue, endpoint, shared intake lane, reusable route, repeated evaluation permission, currentness, authority, standing, truth, continuity memory, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work.

## 3. Boundary Question

Given that one receiver-side answerable-basis candidate was separately supplied, received, recorded, and preserved as opaque candidate material by a completed bounded reception operation, while candidate evaluation, answerable-basis sufficiency, receiver attestation, receiver answerable receipt, custody distinctness, refusability, could-have-been-withheld posture, and all presence postures remain false, may one future bounded operation evaluate that one recorded candidate against explicitly declared answerable-basis conditions without treating candidate reception, candidate content, declared provenance, packet labels, hashes, timestamps, physical-signal data, or receiver-language as already established proof?

## 4. Required Answer

Yes, but only as one separately bounded receiver-side answerable-basis candidate evaluation operation downstream of this boundary.

This boundary allows evaluation consideration only. It does not perform evaluation, prescribe the evaluation result, establish candidate sufficiency, establish receiver attestation, establish receiver answerable receipt, or re-run or satisfy the presence operation.

## 5. Boundary Identifiers

- `receiver_side_answerable_basis_candidate_evaluation_boundary_id = receiver_side_answerable_basis_candidate_evaluation_boundary_001`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_version = 0.1.0`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_scope = CONSIDER_EVALUATION_OF_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`
- `prior_receiver_side_answerable_basis_reception_operation_type = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION`
- `prior_receiver_side_answerable_basis_reception_operation_outcome_required = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED`
- `prior_receiver_side_answerable_basis_reception_operation_result_required = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED`
- `prior_receiver_side_answerable_basis_reception_operation_recorded_required = true`
- `prior_receiver_side_answerable_basis_reception_operation_result_recorded_required = true`
- `prior_candidate_material_supplied_required = true`; `prior_candidate_material_received_required = true`; `prior_candidate_material_recorded_required = true`; `prior_candidate_material_preserved_required = true`
- `prior_candidate_source_provenance_reference_supplied_required = true`
- `prior_receiver_side_answerable_basis_candidate_received_required = true`; `prior_receiver_side_answerable_basis_candidate_recorded_required = true`; `prior_receiver_side_answerable_basis_candidate_evaluated_required = false`
- `prior_receiver_side_answerable_basis_reception_boundary_referenced_required = true`
- `prior_second_candidate_received_required = false`; `prior_repeated_reception_permission_created_required = false`; `prior_reusable_route_created_required = false`
- `prior_receiver_attestation_created_required = false`; `prior_receiver_attestation_supported_required = false`; `prior_receiver_answerable_receipt_present_required = false`
- `prior_receiver_answerable_basis_custody_distinct_required = false`; `prior_receiver_answerable_basis_refusable_required = false`; `prior_receiver_answerable_basis_could_have_been_withheld_required = false`
- `prior_presence_supported_required = false`; `prior_presence_authorized_required = false`; `prior_presence_established_required = false`; `prior_presence_recorded_required = false`
- `prior_follow_on_authorized_required = false`; `prior_follow_on_work_authorized_required = false`
- `admissible_future_route = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_THEN_CANDIDATE_EVALUATION_OPERATION_ONLY`

The default boundary posture is false:

- `receiver_side_answerable_basis_candidate_evaluation_boundary_recorded = false`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded = false`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_result = NOT_EVALUATED`
- `receiver_side_answerable_basis_candidate_evaluation_consideration_allowed = false`
- `selected_candidate_reception_result_referenced = false`; `selected_candidate_material_referenced = false`
- `receiver_side_answerable_basis_candidate_evaluated = false`; `receiver_side_answerable_basis_candidate_sufficient = false`; `receiver_side_answerable_basis_candidate_insufficient = false`; `receiver_side_answerable_basis_candidate_indeterminate = false`
- `receiver_attestation_created = false`; `receiver_attestation_supported = false`; `receiver_answerable_receipt_present = false`
- `receiver_answerable_basis_custody_distinct = false`; `receiver_answerable_basis_refusable = false`; `receiver_answerable_basis_could_have_been_withheld = false`
- `candidate_answers_prior_presence_knock = false`; `candidate_receiver_authorship_established = false`; `candidate_receiver_identity_established = false`; `candidate_source_identity_established = false`; `candidate_declared_provenance_verified = false`; `candidate_separate_custody_established = false`; `candidate_voluntary_supply_established = false`; `candidate_physical_signal_validated = false`; `candidate_human_presence_inferred = false`
- `presence_supported = false`; `presence_authorized = false`; `presence_established = false`; `presence_recorded = false`
- `identity_created = false`; `relation_created = false`; `coupling_assigned = false`; `coupling_created = false`; `field_machinery_created = false`; `runtime_created = false`; `api_created = false`
- `public_interface_created = false`; `public_intake_created = false`; `mailbox_created = false`; `listener_created = false`; `queue_created = false`; `endpoint_created = false`; `shared_intake_lane_created = false`
- `reusable_route_created = false`; `repeated_evaluation_permission_created = false`; `second_candidate_received = false`; `second_candidate_evaluated = false`
- `currentness_created = false`; `authority_created = false`; `standing_created = false`; `truth_created = false`; `continuity_memory_written = false`
- `output_authorized = false`; `action_authorized = false`; `derivative_reception_authorized = false`; `synchronization_authorized = false`; `follow_on_authorized = false`; `follow_on_work_authorized = false`

## 6. Selected Candidate Basis

The exact candidate identity is:

- `receiver_side_answerable_basis_candidate_id = receiver_side_answerable_basis_candidate_001`
- `receiver_side_answerable_basis_candidate_type = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE`
- `receiver_side_answerable_basis_candidate_scope = ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY`
- `selected_candidate_reception_operation_id = receiver_side_answerable_basis_reception_operation_001`
- `selected_candidate_reception_result_artifact = artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_operation_v0_min/receiver_side_answerable_basis_reception_operation_001__receiver_side_answerable_basis_reception_operation_v0_min_result_001.json`

These identifiers select the one already received candidate only. They do not establish candidate sufficiency, receiver identity, source identity, provenance validity, custody distinction, receiver attestation, receiver answerable receipt, or presence.

The selected successful reception artifact contains a static `what_remains_open` list inherited from the resolver implementation that still names actual candidate material and actual candidate reception. Those stale list entries do not override the same artifact's decisive structured reception result. This boundary does not edit, repair, normalize, or replace that artifact. It reads candidate material supplied, received, recorded, and preserved as true because the selected structured result records those postures true; it must not reproduce actual candidate material or actual candidate reception as still open. The stale open-list entries create no authority for broader interpretation.

## 7. Future Boundary Admissibility

A future candidate-evaluation boundary operation may allow evaluation consideration only if all of the following hold:

- the selected successful reception artifact exists and is parseable JSON;
- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED`;
- operation type is `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION` and operation result is `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED`;
- operation recorded and operation result recorded are true;
- candidate material supplied, received, recorded, and preserved are true;
- candidate source/provenance reference supplied is true;
- candidate received and candidate recorded are true, while candidate evaluated is false;
- candidate id, type, and scope match the exact required candidate identity;
- the prior reception boundary is referenced and `failed_check_count = 0`;
- second candidate received, repeated reception permission created, and reusable route created are false;
- receiver attestation, receiver answerable receipt, custody distinctness, refusability, could-have-been-withheld posture, and all presence postures remain false;
- all downstream non-claims remain false;
- the request does not pre-claim an evaluation outcome, ask this boundary to inspect, validate, classify, or interpret candidate semantics, or ask it to establish attestation, receipt, custody, refusability, withholding, identity, presence, authority, standing, relation, or follow-on work.

The boundary must treat the successful artifact's decisive structured result fields as governing.

## 8. Evaluation-Dimension Separation

A future evaluation operation may evaluate these distinct dimensions separately:

1. **Candidate structural correspondence:** whether the preserved candidate record corresponds to the required candidate id, type, scope, selected reception operation, and one prior presence-operation knock reference.
2. **Declared provenance posture:** whether a non-empty declared source/provenance reference and packet custody declaration are present as declarations. This is not verified provenance, source identity, custody distinction, authority, or standing.
3. **Receiver-authorship posture:** whether the candidate packet contains a declaration that its words were authored by the receiver. This is not established receiver authorship or receiver identity.
4. **Separate-custody posture:** whether the candidate packet contains a declaration that it originated in receiver-controlled custody separate from the source repository. This is not established custody distinctness.
5. **Refusability posture:** whether the candidate packet contains a declaration that supply could have been refused. This is not established refusability.
6. **Could-have-been-withheld posture:** whether the candidate packet contains a declaration that supply could have been withheld. This is not an established could-have-been-withheld result.
7. **Prior-knock correspondence posture:** whether the packet declares that it answers exactly the selected prior presence-operation knock and preserves a corresponding reference or digest. This is not established answerability, attestation, receipt, or presence support.
8. **Capture-record posture:** whether the packet preserves bounded capture metadata, hashes, timestamps, and a recorded physical-signal file. This is not validation of the physical signal, bodily presence, human identity, authorship, custody, or truth.

No single declaration, label, hash, timestamp, path, device record, capture file, or phrase may automatically satisfy another dimension. Evaluation dimensions must not silently collapse into one omnibus boolean.

## 9. Permitted Future Boundary Result

A future candidate-evaluation boundary operation may return exactly one of:

- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_ALLOWED`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_REQUIRES_RECORDED_CANDIDATE_BASIS`
- `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_BLOCKED`

If all admissibility requirements hold, it may record only:

- `receiver_side_answerable_basis_candidate_evaluation_boundary_recorded = true`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded = true`
- `receiver_side_answerable_basis_candidate_evaluation_boundary_result = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED`
- `receiver_side_answerable_basis_candidate_evaluation_consideration_allowed = true`
- `selected_candidate_reception_result_referenced = true`
- `selected_candidate_material_referenced = true`

Even when consideration is allowed, candidate evaluation, candidate sufficiency, candidate insufficiency, candidate indeterminacy, receiver attestation, receiver answerable receipt, custody distinctness, refusability, could-have-been-withheld posture, all listed establishment postures, all presence postures, and every downstream creation and authorization posture remain false.

If the selected candidate basis is missing, malformed, internally inconsistent on decisive structured result fields, or not the exact required candidate while the request remains bounded, the future boundary operation may record `receiver_side_answerable_basis_candidate_evaluation_boundary_result = REQUIRES_RECORDED_CANDIDATE_BASIS`, preserve `receiver_side_answerable_basis_candidate_evaluation_consideration_allowed = false`, and identify the missing or inconsistent recorded-candidate basis. Missing or insufficient boundary basis is not candidate rejection, candidate insufficiency, failed evaluation, receiver refusal, receiver attestation, receiver answerable receipt, presence failure, debt, or pending obligation.

Any request that performs candidate evaluation, chooses sufficiency, establishes attestation or receipt, establishes custody distinctness, refusability, withholding, authorship, identity, provenance, physical-signal validity, human presence, presence support, or any downstream creation must record `BLOCKED`.

## 10. Required Invariants

- Candidate evaluation boundary is not candidate evaluation operation. Evaluation consideration is not evaluation. Candidate reception is not candidate evaluation. Candidate preservation is not candidate validation.
- Candidate content is not established candidate meaning. Candidate declaration is not established fact. Candidate label is not candidate sufficiency. Packet filename and directory name are not constitutional classification. The word `attestation` is not receiver attestation. The value `candidate_kind` is not an evaluation result.
- Receiver label is not receiver identity. Filesystem path is not custody distinction. Declared custody is not established custody distinction. Declared receiver authorship is not established receiver authorship. Declared voluntary supply is not established voluntary supply. Declared refusability is not established refusability. Declared withholding posture is not established could-have-been-withheld posture.
- Declared provenance reference is not verified provenance. Source reference is not source identity, authority, or standing. Hash correspondence is not semantic sufficiency or receiver identity. Timestamp is not currentness or authority. Device metadata is not human identity.
- Accelerometer data is not automatically a valid knock. Recorded physical signal is not automatically bodily presence. Physical signal is not receiver attestation. Capture metadata is not receiver answerable receipt. Prior-knock reference is not proof that the candidate answers the knock.
- Candidate answerability is not receiver attestation or receiver answerable receipt. Candidate sufficiency is not receiver attestation or receiver answerable receipt. Receiver attestation is distinct from receiver answerable receipt. Receiver answerable receipt is distinct from candidate evaluation.
- Custody distinctness is distinct from refusability. Refusability is distinct from could-have-been-withheld posture. Could-have-been-withheld posture is distinct from separate custody.
- One successful candidate evaluation is not reusable evaluation permission. One candidate is not permission for a second candidate. One candidate evaluation is not permission for second evaluation.
- Candidate evaluation is not presence support, presence authorization, presence establishment, presence recording, identity, relation, coupling, FIELD machinery, runtime, API, public intake, currentness, authority, standing, truth creation, continuity memory, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work.
- No public surface, named receiver route, second candidate route, or downstream route is authorized by this boundary specification. Open means not scheduled, not authorized, and not executed.

## 11. Relation to Completed Reception Boundary

`spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_V0_MIN_SPEC.md` and `spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_TERMINAL_SUMMARY_V0.md` remain the governing completed reception-boundary surfaces. The selected v2 boundary line recorded `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_ALLOWED` and `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED` only, while candidate received, candidate recorded, candidate evaluated, receiver attestation, receiver answerable receipt, custody distinctness, refusability, could-have-been-withheld posture, and presence support remained false.

This specification is downstream of that completed boundary. It does not reopen, modify, replace, broaden, or convert boundary permission into evaluation completion.

## 12. Relation to Completed Reception Operation

`spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_TERMINAL_SUMMARY_V0.md` remains the first and only terminal summary for the receiver-side answerable-basis reception operation implementation line. It closed the original selected waiting execution: `RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_REQUIRES_CANDIDATE_MATERIAL`, `REQUIRES_CANDIDATE_MATERIAL`, no candidate supplied, no candidate received, no candidate recorded, and no candidate evaluated.

The later successful suffixed artifact was produced by the already bounded and completed operation machinery after separately supplied material arrived. That invocation does not reopen, replace, invalidate, or rewrite the terminal summary. Its successful invocation records candidate reception only.

## 13. Relation to Selected Successful Reception Artifact

The selected artifact is:

`artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_operation_v0_min/receiver_side_answerable_basis_reception_operation_001__receiver_side_answerable_basis_reception_operation_v0_min_result_001.json`

Its standing structured facts are:

- `outcome = RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED`
- `receiver_side_answerable_basis_reception_operation_result = RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED`
- `candidate_material_supplied = true`; `candidate_material_received = true`; `candidate_material_recorded = true`; `candidate_material_preserved = true`
- `candidate_source_provenance_reference_supplied = true`
- `receiver_side_answerable_basis_candidate_received = true`; `receiver_side_answerable_basis_candidate_recorded = true`; `receiver_side_answerable_basis_candidate_evaluated = false`
- `prior_receiver_side_answerable_basis_reception_boundary_referenced = true`
- `second_candidate_received = false`; `repeated_reception_permission_created = false`; `reusable_route_created = false`
- `receiver_attestation_created = false`; `receiver_attestation_supported = false`; `receiver_answerable_receipt_present = false`
- `receiver_answerable_basis_custody_distinct = false`; `receiver_answerable_basis_refusable = false`; `receiver_answerable_basis_could_have_been_withheld = false`
- `presence_supported = false`; `presence_authorized = false`; `presence_established = false`; `presence_recorded = false`
- `failed_check_count = 0`; `passed_check_count = 105`; `result_version = 0.1.0`; `resolver_module = resolve_receiver_side_answerable_basis_reception_operation_v0_min`

The selected candidate material was preserved as opaque material and includes references to one receipt bundle, one declared receiver label, one candidate kind, one declared attestation form, one prior knock-result digest, one receipt-zip path, and one receipt-zip digest. This specification does not reproduce, evaluate, or declare those contents true or false.

## 14. Relation to Completed Presence Operation

`spec/PRESENCE_OPERATION_TERMINAL_SUMMARY_V0.md` remains the completed terminal summary for the presence operation line. It recorded `PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION` and `REQUIRES_RECEIVER_ATTESTATION`: receiver attestation required, receiver-side answerable basis required, repo-local execution alone insufficient, and presence unsupported, unauthorized, unestablished, and unrecorded.

This candidate-evaluation boundary does not re-run, satisfy, or change the presence operation. Even a future successful candidate evaluation would not automatically create receiver attestation, receiver answerable receipt, or presence support.

## 15. Permitted Future Route

1. A future receiver-side answerable-basis candidate evaluation boundary resolver may evaluate the selected successful candidate-reception artifact and the governing upstream surfaces.
2. If the selected structured reception basis is exact and all non-conversion locks hold, a future boundary artifact may record `RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED`.
3. After that boundary is completed, one separately bounded candidate evaluation operation may evaluate the one selected candidate across explicitly separated dimensions.
4. That operation must preserve declaration-versus-established-fact distinctions.
5. That operation may not silently collapse structural correspondence, declared provenance, receiver authorship, separate custody, refusability, withholding, prior-knock correspondence, and capture-record posture into one undifferentiated success result.
6. No receiver attestation, receiver answerable receipt, presence re-evaluation, second candidate, reusable evaluation route, or later operation is authorized by this boundary alone.

## 16. Blocked Routes

The following conversions are explicitly blocked:

- candidate reception directly to candidate evaluation completion, candidate sufficiency, candidate insufficiency, receiver attestation, receiver answerable receipt, custody distinctness, refusability, could-have-been-withheld posture, or presence support;
- boundary permission directly to evaluation completion or evaluation result;
- packet filename or directory name to constitutional classification; the word `attestation` to receiver attestation; receiver label to receiver identity; `candidate_kind` value to answerable-basis sufficiency; declared attestation form to established attestation;
- declared source/provenance reference to verified provenance; source reference to source identity, authority, or standing; receiver working-directory path to custody distinction; custody declaration to established custody distinction; freely-given declaration to established voluntariness; could-have-been-refused declaration to established refusability; could-have-been-withheld declaration to established withholding posture; authored-by-receiver declaration to established receiver authorship;
- hash match to semantic sufficiency or receiver identity; timestamp to currentness or authority; device metadata to human identity; physical-signal file to bodily presence; accelerometer data to validated knock without bounded evaluation; capture metadata to receiver attestation or receiver answerable receipt; prior-knock reference to established answerability;
- candidate evaluation to receiver attestation, receiver answerable receipt, presence support, presence authorization, presence establishment, presence recording, identity, relation, coupling, FIELD machinery, runtime, API, public interface, public intake, mailbox, listener, queue, endpoint, shared intake lane, reusable route, repeated evaluation permission, second candidate reception, second candidate evaluation, currentness, authority, standing, truth creation, continuity memory, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work;
- selected candidate to retroactive validation of contaminated lineage; repository scan; file discovery; affected-file repair; or prior unsupported-claim validation.

## 17. Preserved Non-Claims

All default false postures and all blocked-route conversion postures remain false:

- `receiver_side_answerable_basis_candidate_evaluation_boundary_recorded = false`; `receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded = false`; `receiver_side_answerable_basis_candidate_evaluation_consideration_allowed = false`
- `selected_candidate_reception_result_referenced = false`; `selected_candidate_material_referenced = false`; `receiver_side_answerable_basis_candidate_evaluated = false`; `receiver_side_answerable_basis_candidate_sufficient = false`; `receiver_side_answerable_basis_candidate_insufficient = false`; `receiver_side_answerable_basis_candidate_indeterminate = false`
- `receiver_attestation_created = false`; `receiver_attestation_supported = false`; `receiver_answerable_receipt_present = false`; `receiver_answerable_basis_custody_distinct = false`; `receiver_answerable_basis_refusable = false`; `receiver_answerable_basis_could_have_been_withheld = false`
- `candidate_answers_prior_presence_knock = false`; `candidate_receiver_authorship_established = false`; `candidate_receiver_identity_established = false`; `candidate_source_identity_established = false`; `candidate_declared_provenance_verified = false`; `candidate_separate_custody_established = false`; `candidate_voluntary_supply_established = false`; `candidate_physical_signal_validated = false`; `candidate_human_presence_inferred = false`
- `presence_supported = false`; `presence_authorized = false`; `presence_established = false`; `presence_recorded = false`; `identity_created = false`; `relation_created = false`; `coupling_assigned = false`; `coupling_created = false`; `field_machinery_created = false`; `runtime_created = false`; `api_created = false`
- `public_interface_created = false`; `public_intake_created = false`; `mailbox_created = false`; `listener_created = false`; `queue_created = false`; `endpoint_created = false`; `shared_intake_lane_created = false`; `reusable_route_created = false`; `repeated_evaluation_permission_created = false`; `second_candidate_received = false`; `second_candidate_evaluated = false`
- `currentness_created = false`; `authority_created = false`; `standing_created = false`; `truth_created = false`; `continuity_memory_written = false`; `output_authorized = false`; `action_authorized = false`; `derivative_reception_authorized = false`; `synchronization_authorized = false`; `follow_on_authorized = false`; `follow_on_work_authorized = false`
- `prior_unsupported_candidate_a_claim_validated = false`; `prior_unsupported_candidate_b_claim_validated = false`; `prior_unsupported_derivation_event_claim_validated = false`; `affected_file_repaired = false`; `repository_scan_performed = false`; `file_discovery_performed = false`; `validation_enforced = false`
- `candidate_reception_to_candidate_evaluation_completion = false`; `candidate_reception_to_candidate_sufficiency = false`; `candidate_reception_to_candidate_insufficiency = false`; `candidate_reception_to_receiver_attestation = false`; `candidate_reception_to_receiver_answerable_receipt = false`; `candidate_reception_to_custody_distinctness = false`; `candidate_reception_to_refusability = false`; `candidate_reception_to_could_have_been_withheld = false`; `candidate_reception_to_presence_support = false`
- `evaluation_boundary_permission_to_evaluation_completion = false`; `evaluation_boundary_permission_to_evaluation_result = false`; `packet_filename_to_constitutional_classification = false`; `directory_name_to_constitutional_classification = false`; `attestation_word_to_receiver_attestation = false`; `receiver_label_to_receiver_identity = false`; `candidate_kind_to_answerable_basis_sufficiency = false`; `declared_attestation_form_to_established_attestation = false`
- `declared_source_provenance_reference_to_verified_provenance = false`; `source_reference_to_source_identity = false`; `source_reference_to_authority = false`; `source_reference_to_standing = false`; `receiver_working_directory_to_custody_distinction = false`; `custody_declaration_to_established_custody_distinction = false`; `freely_given_declaration_to_established_voluntary_supply = false`; `refusal_declaration_to_established_refusability = false`; `withholding_declaration_to_established_could_have_been_withheld = false`; `receiver_authorship_declaration_to_established_receiver_authorship = false`
- `hash_correspondence_to_semantic_sufficiency = false`; `hash_correspondence_to_receiver_identity = false`; `timestamp_to_currentness = false`; `timestamp_to_authority = false`; `device_metadata_to_human_identity = false`; `physical_signal_to_bodily_presence = false`; `accelerometer_data_to_validated_knock = false`; `capture_metadata_to_receiver_attestation = false`; `capture_metadata_to_receiver_answerable_receipt = false`; `prior_knock_reference_to_established_answerability = false`
- `candidate_evaluation_to_receiver_attestation = false`; `candidate_evaluation_to_receiver_answerable_receipt = false`; `candidate_evaluation_to_presence_support = false`; `candidate_evaluation_to_presence_authorization = false`; `candidate_evaluation_to_presence_establishment = false`; `candidate_evaluation_to_presence_recording = false`; `candidate_evaluation_to_identity = false`; `candidate_evaluation_to_relation = false`; `candidate_evaluation_to_coupling = false`; `candidate_evaluation_to_field_machinery = false`; `candidate_evaluation_to_runtime = false`; `candidate_evaluation_to_api = false`; `candidate_evaluation_to_public_intake = false`
- `candidate_evaluation_to_public_interface = false`; `candidate_evaluation_to_mailbox = false`; `candidate_evaluation_to_listener = false`; `candidate_evaluation_to_queue = false`; `candidate_evaluation_to_endpoint = false`; `candidate_evaluation_to_shared_intake_lane = false`; `candidate_evaluation_to_reusable_route = false`; `candidate_evaluation_to_repeated_evaluation_permission = false`
- `candidate_evaluation_to_second_candidate = false`; `candidate_evaluation_to_second_candidate_reception = false`; `candidate_evaluation_to_second_candidate_evaluation = false`; `candidate_evaluation_to_currentness = false`; `candidate_evaluation_to_authority = false`; `candidate_evaluation_to_standing = false`; `candidate_evaluation_to_truth_creation = false`; `candidate_evaluation_to_continuity_memory = false`; `candidate_evaluation_to_output_authorization = false`; `candidate_evaluation_to_action_authorization = false`; `candidate_evaluation_to_derivative_reception = false`; `candidate_evaluation_to_synchronization = false`; `candidate_evaluation_to_follow_on_authorization = false`; `candidate_evaluation_to_follow_on_work = false`
- `selected_candidate_to_retroactive_contaminated_lineage_validation = false`

No false non-claim is listed as true.

## 18. Relation to Contaminated Lineage

`spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage. Its prior unsupported claims remain unsupported. This boundary does not repair, edit, delete, overwrite, replace, validate, redeem, clean, or reinterpret that file. The selected receiver-side candidate must not be used to retroactively validate unrelated contaminated existence claims.

## 19. What This Does Not Create

This boundary creates no candidate evaluation, evaluation result, candidate sufficiency, candidate insufficiency, candidate indeterminacy, receiver attestation, receiver answerable receipt, custody-distinctness decision, refusability decision, could-have-been-withheld decision, receiver authorship establishment, receiver identity establishment, source identity establishment, verified provenance, voluntary-supply establishment, physical-signal validation, human-presence inference, presence support, presence authorization, presence establishment, presence recording, second candidate, second evaluation, reusable evaluation route, repeated evaluation permission, identity, relation, coupling, FIELD machinery, runtime, API, public interface, public intake, mailbox, listener, queue, endpoint, shared intake lane, currentness, authority, standing, truth, continuity memory, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, follow-on work, repository scan, file discovery, repair, or validation enforcement.

## 20. What Remains Open

Open and not executed:

- candidate evaluation boundary resolver; candidate evaluation boundary test; candidate evaluation boundary live artifact; actual candidate evaluation boundary execution
- candidate evaluation operation specification, resolver, test, and live artifact, each only if separately selected and bounded
- candidate structural-correspondence evaluation; declared-provenance-posture evaluation; receiver-authorship-posture evaluation; separate-custody-posture evaluation; refusability-posture evaluation; could-have-been-withheld-posture evaluation; prior-knock-correspondence evaluation; capture-record-posture evaluation
- answerable-basis sufficiency result; receiver attestation; receiver answerable receipt; custody distinctness; refusability; could-have-been-withheld posture
- presence re-evaluation, if separately bounded; presence support; presence authorization; presence establishment; presence recording
- identity boundary; relation boundary; coupling boundary; FIELD machinery; runtime; API; public interface; public intake; currentness; authority; standing; output authorization; action authorization; derivative reception; synchronization; externalization boundary; follow-on work

The selected candidate material has already been supplied, received, recorded, and preserved. The selected candidate has already been received and recorded. Candidate evaluation remains open. Open means not scheduled, not authorized, and not executed. Open does not mean next unless separately selected.

## 21. Closing Lock

This boundary specification defines only whether the one receiver-side answerable-basis candidate already supplied, received, recorded, and preserved by the selected successful reception-operation result may enter one separately bounded candidate evaluation operation. It does not perform candidate evaluation; decide candidate sufficiency, insufficiency, or indeterminacy; verify candidate semantics, declared provenance, receiver authorship, receiver identity, source identity, separate custody, voluntary supply, refusability, could-have-been-withheld posture, prior-knock answerability, physical-signal validity, bodily presence, or human presence; create receiver attestation or receiver answerable receipt; support, authorize, establish, or record presence; create identity, relation, coupling, FIELD machinery, runtime, API, public interface, public intake, mailbox, listener, queue, endpoint, shared intake lane, reusable route, repeated evaluation permission, second candidate, second evaluation, currentness, authority, standing, truth, or continuity memory; authorize output, action, derivative reception, synchronization, follow-on authorization, or follow-on work; repair the affected file; validate prior unsupported claims; scan repository; discover files; enforce validation; or authorize downstream work. Candidate reception is not candidate evaluation. Candidate preservation is not candidate validation. Candidate content is not established candidate meaning. Candidate declaration is not established fact. The word attestation is not receiver attestation. Receiver label is not receiver identity. Filesystem path is not custody distinction. Declared custody is not established custody distinction. Declared refusability is not established refusability. Declared withholding posture is not established could-have-been-withheld posture. Declared source/provenance reference is not verified provenance, source identity, authority, standing, or custody distinction. Hash correspondence is not semantic sufficiency or receiver identity. Timestamp is not currentness or authority. Device metadata is not human identity. Recorded physical signal is not automatically bodily presence, receiver attestation, or receiver answerable receipt. Receiver answerable receipt remains distinct from receiver attestation. Custody distinctness, refusability, and could-have-been-withheld posture remain distinct evaluation dimensions. The selected candidate material has already been supplied, received, recorded, and preserved; the selected candidate has already been received and recorded; candidate evaluation remains false. Only after a future candidate evaluation boundary records RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED may one separately bounded candidate evaluation operation be considered. Open means not scheduled, not authorized, and not executed.
