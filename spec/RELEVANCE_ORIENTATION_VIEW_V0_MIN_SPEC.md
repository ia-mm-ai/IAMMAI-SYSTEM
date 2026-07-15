# Relevance Orientation View V0 Minimum Specification

## 1. Purpose

This file defines the first relevance orientation view for the present `IAMMAI-SYSTEM` execution line.

This is an instrument-facing specification after bounded relevance receipt v2.

The view reads one clean bounded relevance receipt v2 artifact and its referenced bounded relevance reception artifact.

The view reports what is inspectably present, what identifiers stand, what cannot be inferred, and what remains unavailable.

This file is not a boundary, not a next-layer selection review, and not a terminal summary.

This file does not itself create resolver, test, live artifact, or terminal summary.

This file does not create source transfer, source receipt, reception authorization, source, authority, currentness, truth, action, synchronization, participation authorization, participant role, runtime permission, public API, participant-facing interface, distributed network behavior, deployment, public release, operation permission, broader reusable permission, derivative reception, vessel relation, adoption, receiving-context governance, publication flow, or follow-on work.

## 2. Status and Rank

- this spec is additive
- this spec ranks below constitutional/reference authority surfaces
- this spec is downstream of `BOUNDED_RELEVANCE_RECEIPT_V2_TERMINAL_SUMMARY_V0.md`
- this spec is downstream of bounded relevance receipt v2 resolver/test/live artifact
- this spec preserves bounded relevance receipt v1 as predecessor evidence only
- this spec is downstream of bounded relevance reception terminal summary and live artifact
- this spec does not replace bounded relevance receipt v2
- this spec does not repair, hide, overwrite, or claim v1 as clean standing
- this spec does not authorize follow-on work

## 3. Why This Spec Is Needed Now

Bounded relevance reception recorded one bounded medium-facing reception posture.

Bounded relevance receipt v2 recorded one inspectable receipt object from the actual bounded relevance reception artifact.

Bounded relevance receipt v2 preserved the actual received identifiers.

Bounded relevance receipt v2 made the received relevance inspectable but did not yet orient a reader.

The next useful step is not another boundary.

The next useful step is the first instrument: a local orientation view.

Without an orientation view, the receipt object exists but still requires the human operator to manually interpret what is present, what stands, what cannot be inferred, and what remains unavailable.

This spec defines the instrument shape without creating action, authority, currentness, synchronization, participation authorization, runtime permission, public interface, distributed behavior, or follow-on work.

## 4. Definitions

`relevance_orientation_view` means a local inspectable view produced from one clean bounded relevance receipt v2 artifact.

`orientation_view` means an instrument output, not authority.

`bounded_relevance_receipt_v2_artifact` means the clean receipt object wrapper that preserved the actual received identifiers.

`referenced_reception_artifact` means the upstream bounded relevance reception artifact referenced by the receipt object.

`inspectably_present` means values visible from the receipt and referenced reception artifacts.

`standing_identifiers` means received identifiers preserved by receipt v2, not authority-standing.

`non_inference` means claims the view explicitly refuses to infer.

`unavailable` means fields not present or not derivable from the bounded receipt/reception artifacts.

`orientation_scope` means `LOCAL_ORIENTATION_ONLY`.

`local_reader` means a bounded repo-local reader; not a participant role.

`instrument` means a bounded object-reading view that helps orientation without creating action or authority.

`source` means source-standing. It is not created here.

`authority` means authority-bearing standing. It is not created here.

`currentness` means operative currentness. It is not created here.

`truth` means standing truth. It is not created here.

`action` means action authorization or action performance. It is not created here.

`synchronization` means shared-state, merge, replay, transfer, or synchronization posture. It is not created here.

`participation_authorization` means authorization for participation. It is not created here.

`participant_role` means a participant role. It is not created here.

`runtime_permission` means permission to run or operate. It is not created here.

`public_api` means an externally consumable public programmatic interface. It is not created here.

`participant_facing_interface` means a participant-facing interaction surface. It is not created here.

`distributed_network_behavior` means network-distributed protocol or runtime behavior. It is not created here.

`follow_on_work` means authorized successor work. It is not authorized here.

## 5. Required Orientation View Shape

The minimal future orientation view shape is:

- `orientation_view_id`
- `orientation_view_type`
- `orientation_view_version`
- `orientation_scope`
- `source_receipt_artifact`
- `referenced_reception_artifact`
- `receipt_outcome`
- `receipt_result_version`
- `receipt_failed_check_count`
- `receipt_scope`
- `receipt_does_not_expand_reception`
- `received_signal_id`
- `received_relevance_basis_id`
- `received_relevance_scope_id`
- `received_carrier_context_id`
- `received_reception_envelope_id`
- `inspectably_present`
- `standing_identifiers`
- `non_inference`
- `unavailable`
- `orientation_statement`

The expected orientation view should look like:

```json
{
  "orientation_view_id": "relevance_orientation_view_001",
  "orientation_view_type": "relevance_orientation_view",
  "orientation_view_version": "0.1.0",
  "orientation_scope": "LOCAL_ORIENTATION_ONLY",
  "source_receipt_artifact": "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/bounded_relevance_receipt_reference_review_001__bounded_relevance_receipt_v0_min_v2_result.json",
  "referenced_reception_artifact": "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json",
  "receipt_outcome": "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
  "receipt_result_version": "0.2.0",
  "receipt_failed_check_count": 0,
  "receipt_scope": "INSPECTABLE_RECEIPT_ONLY",
  "receipt_does_not_expand_reception": true,
  "received_signal_id": "bounded_relevance_signal_001",
  "received_relevance_basis_id": "bounded_relevance_basis_001",
  "received_relevance_scope_id": "bounded_relevance_scope_001",
  "received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
  "received_reception_envelope_id": "bounded_relevance_reception_envelope_001",
  "inspectably_present": [
    "bounded relevance receipt v2 artifact",
    "referenced bounded relevance reception artifact",
    "received signal id",
    "received relevance basis id",
    "received relevance scope id",
    "received carrier context id",
    "received reception envelope id"
  ],
  "standing_identifiers": {
    "received_signal_id": "bounded_relevance_signal_001",
    "received_relevance_basis_id": "bounded_relevance_basis_001",
    "received_relevance_scope_id": "bounded_relevance_scope_001",
    "received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
    "received_reception_envelope_id": "bounded_relevance_reception_envelope_001"
  },
  "non_inference": {
    "source_created": false,
    "authority_created": false,
    "currentness_created": false,
    "truth_created": false,
    "action_created": false,
    "synchronization_created": false,
    "participation_authorized": false,
    "participant_role_created": false,
    "runtime_permission_created": false,
    "public_api_created": false,
    "participant_facing_interface_created": false,
    "distributed_network_behavior_created": false,
    "follow_on_work_authorized": false
  },
  "unavailable": [
    "source standing",
    "authority standing",
    "operative currentness",
    "truth claim",
    "action authorization",
    "synchronization authorization",
    "participation authorization",
    "participant role",
    "runtime permission",
    "public interface",
    "distributed network behavior",
    "follow-on work authorization"
  ],
  "orientation_statement": "One clean bounded relevance receipt v2 object and its referenced bounded relevance reception artifact are inspectably present. The view orients to preserved identifiers only and does not infer authority, currentness, truth, action, synchronization, participation, runtime permission, public interface, distributed behavior, or follow-on work."
}
```

## 6. Required Orientation Checks

A future resolver or manual review may record one relevance orientation view only when:

- orientation question is declared
- orientation intent is supported
- selected bounded relevance receipt v2 artifact path is declared
- selected bounded relevance receipt v2 artifact outcome is `BOUNDED_RELEVANCE_RECEIPT_RECORDED`
- selected bounded relevance receipt v2 artifact result version is `0.2.0`
- selected bounded relevance receipt v2 artifact failed check count is zero
- selected bounded relevance receipt v2 artifact contains one receipt object
- receipt object has `receipt_scope = INSPECTABLE_RECEIPT_ONLY`
- receipt object has `does_not_expand_reception = true`
- receipt object references one bounded relevance reception artifact
- receipt object preserves received signal id
- receipt object preserves received relevance basis id
- receipt object preserves received relevance scope id
- receipt object preserves received carrier context id
- receipt object preserves received reception envelope id
- orientation scope is `LOCAL_ORIENTATION_ONLY`
- view does not add signal, basis, scope, carrier context, or envelope
- view does not infer source, authority, currentness, truth, action, synchronization, participation authorization, participant role, runtime permission, public API, participant-facing interface, distributed network behavior, operation permission, or follow-on work

## 7. Outcome Family

The future orientation-view outcome family is:

- `RELEVANCE_ORIENTATION_VIEW_RECORDED`
- `RELEVANCE_ORIENTATION_VIEW_NOT_RECORDED`
- `RELEVANCE_ORIENTATION_VIEW_REQUIRES_ADDITIONAL_BASIS`
- `RELEVANCE_ORIENTATION_VIEW_BLOCKED`

Recorded means one local orientation view was recorded from a clean bounded relevance receipt v2 artifact.

Not recorded means the orientation view could not be recorded from readable basis.

Requires additional basis means more orientation basis is needed.

Blocked means malformed, missing, or overreach-shaped orientation input.

Recorded orientation view does not create source transfer, source receipt, reception authorization, source, authority, currentness, truth, action, synchronization, participation authorization, participant role, runtime permission, public API, participant-facing interface, distributed network behavior, deployment, public release, operation permission, broader reusable permission, derivative reception, vessel relation, adoption, receiving-context governance, publication flow, or follow-on work.

## 8. Blocking Conditions

Review must be blocked when:

- orientation question undeclared
- orientation intent unsupported
- selected bounded relevance receipt v2 artifact missing
- selected bounded relevance receipt v2 artifact not recorded
- selected bounded relevance receipt v2 artifact failed checks present
- selected bounded relevance receipt v2 artifact version not `0.2.0`
- receipt object missing
- referenced reception artifact missing from receipt object
- received signal id missing
- received relevance basis id missing
- received relevance scope id missing
- received carrier context id missing
- received reception envelope id missing
- receipt scope is not `INSPECTABLE_RECEIPT_ONLY`
- receipt expands reception
- orientation scope missing
- orientation scope is not `LOCAL_ORIENTATION_ONLY`
- orientation view adds a new signal
- orientation view adds a new relevance basis
- orientation view adds a new relevance scope
- orientation view adds a new carrier context
- orientation view adds a new envelope
- orientation view creates source transfer
- orientation view creates source receipt
- orientation view creates reception authorization
- orientation view creates source
- orientation view creates authority
- orientation view creates currentness
- orientation view creates truth
- orientation view creates action
- orientation view creates synchronization
- orientation view authorizes participation
- orientation view creates participant role
- orientation view creates runtime permission
- orientation view creates public API
- orientation view creates participant-facing interface
- orientation view creates distributed network behavior
- orientation view creates deployment
- orientation view creates public release
- orientation view creates operation permission
- orientation view creates broader reusable permission
- orientation view authorizes follow-on work
- artifact existence alone is treated as orientation authority
- latest file posture is treated as orientation authority
- repo-local availability is treated as orientation authority
- hidden repo state is used as orientation content or authority
- predecessor failure evidence is hidden, repaired, or claimed passed

## 9. Preserved Non-Claims

Preserve false posture for:

- `source_transfer_occurred = false`
- `source_receipt_occurred = false`
- `reception_authorization_created = false`
- `source_created = false`
- `authority_created = false`
- `currentness_created = false`
- `truth_created = false`
- `action_created = false`
- `synchronization_created = false`
- `participation_authorized = false`
- `participant_role_created = false`
- `runtime_permission_created = false`
- `public_api_created = false`
- `participant_facing_interface_created = false`
- `distributed_network_behavior_created = false`
- `deployment_created = false`
- `public_release_created = false`
- `operation_permission_created = false`
- `broader_reusable_permission_created = false`
- `derivative_reception_authorized = false`
- `vessel_relation_authorized = false`
- `adoption_created = false`
- `receiving_context_governance_created = false`
- `publication_flow_created = false`
- `follow_on_work_authorized = false`
- `orientation_added_new_signal = false`
- `orientation_added_new_relevance_basis = false`
- `orientation_added_new_relevance_scope = false`
- `orientation_added_new_carrier_context = false`
- `orientation_added_new_envelope = false`
- `artifact_existence_treated_as_orientation_authority = false`
- `latest_file_posture_treated_as_orientation_authority = false`
- `repo_local_availability_treated_as_orientation_authority = false`
- `hidden_repo_state_used_as_orientation_content = false`
- `hidden_repo_state_used_as_orientation_authority = false`
- `prior_artifacts_mutated = false`
- `predecessor_failure_repaired = false`
- `predecessor_failure_hidden = false`
- `predecessor_failure_claimed_passed = false`

Allowed true fields only in future recorded orientation view outcome:

- `relevance_orientation_view_recorded = true`
- `source_receipt_artifact_preserved = true`
- `referenced_reception_artifact_preserved = true`
- `received_signal_id_preserved = true`
- `received_relevance_basis_id_preserved = true`
- `received_relevance_scope_id_preserved = true`
- `received_carrier_context_id_preserved = true`
- `received_reception_envelope_id_preserved = true`
- `orientation_scope_local_only = true`
- `orientation_does_not_expand_receipt = true`
- `orientation_does_not_expand_reception = true`
- `result_level_non_claims_canonical_false = true`

## 10. Relation to Bounded Relevance Receipt V2

Bounded relevance receipt v2 remains the upstream clean receipt surface.

Relevance orientation view depends on clean bounded relevance receipt v2 artifact.

Relevance orientation view does not mutate bounded relevance receipt v2 artifact.

Relevance orientation view does not reopen the receipt object.

Relevance orientation view does not add signal, basis, scope, carrier context, or envelope.

Relevance orientation view preserves selected receipt identifiers only.

Relevance orientation view orients a local reader to what is inspectably present.

## 11. What Remains Open

Open and not executed:

- relevance orientation view resolver
- relevance orientation view test
- relevance orientation view live artifact
- relevance orientation view terminal summary, if needed
- source transfer
- source receipt
- reception authorization
- derivative reception
- vessel relation
- adoption
- authority creation
- currentness creation
- truth creation
- action
- synchronization
- participation authorization
- participant role
- runtime permission
- public API
- participant-facing interface
- distributed network behavior
- operation permission
- receiving-context governance
- deployment
- public release
- publication flow
- broader reusable permission
- successor reception request
- follow-on work

Open means not scheduled.

Open means not authorized.

Open means not executed.

Open does not mean next unless separately selected.

## 12. Closing Statement

Relevance orientation view may record one local instrument view from a clean bounded relevance receipt v2 artifact and its referenced bounded relevance reception artifact. It reports what is inspectably present, what identifiers stand as received identifiers, what cannot be inferred, and what remains unavailable. It preserves the source receipt artifact, referenced reception artifact, received signal id, relevance basis id, relevance scope id, carrier context id, and received reception envelope id without expanding the receipt or the reception. Relevance orientation view is an instrument, not authority. It does not create source transfer, source receipt, reception authorization, source, authority, currentness, truth, action, synchronization, participation authorization, participant role, runtime permission, public API, participant-facing interface, distributed network behavior, deployment, public release, operation permission, broader reusable permission, derivative reception, vessel relation, adoption, receiving-context governance, publication flow, successor reception request, or follow-on work. Any actual source transfer, source receipt, reception authorization, authority, currentness, truth, action, synchronization, participation authorization, participant role, runtime permission, public API, participant-facing interface, distributed network behavior, deployment, public release, operation permission, broader reusable permission, derivative reception, vessel relation, adoption, receiving-context governance, publication flow, successor reception request, or follow-on work still requires a separately bounded step.
