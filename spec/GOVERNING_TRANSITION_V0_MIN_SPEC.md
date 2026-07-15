# Governing Transition V0-Min Spec

## 1. Purpose

This file defines the first bounded governing-transition spec for the v0-min coexistence execution line.

It derives from the current execution-authority, run-family, preserved-run-status, and current-governing line:

- `src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py`
- `src/build_integrity_host_v0_min_coexistence_run_family_packet.py`
- `src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py`
- `src/build_current_integrity_host_v0_min_coexistence_governing_packet.py`
- `spec/CURRENT_EXECUTABLE_LINE_AND_FORCED_SYSTEM_PRESSURES.md`
- `spec/CURRENT_GOVERNING_TRANSITION_BOUNDARY.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful model by which current governing authority could move from one preserved run to another if a transition is explicitly proposed and passes bounded checks.

The next forced pressure is transition mechanics, not more packaging. The repo can already identify current governing scope and preserved non-governing runs. It now needs a bounded answer for how a governing change could be proposed, checked, refused, or accepted without relying on recency alone.

This spec does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, or a broad governance engine.

## 2. Status And Rank

This spec is additive and repo-local.

It ranks below the constitutional and reference authority surfaces under `reference/IAMMAI/`, including the constitutional protocol, implementation overviews, runtime contract surfaces, and architecture surfaces.

It also ranks below the current executable source, tests, and generated artifacts where those surfaces already stand as concrete behavior.

This spec does not:

- define final governance
- complete continuity
- replace current executable source files
- replace current test surfaces
- replace emitted artifacts
- promote latest-emitted into transition law
- promote latest-eligible into transition law
- define a minimum lawful system

Its scope is one bounded governing-transition model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository now distinguishes:

- current governing run
- preserved eligible non-authority runs
- preserved ineligible runs

Once those roles exist explicitly, their relation over time can no longer remain implicit.

`spec/CURRENT_GOVERNING_TRANSITION_BOUNDARY.md` established that governing transition is not automatic and is not yet implemented. It also established that preserved eligibility is visible but not self-executing.

The body now needs one bounded spec rather than more abstract discussion. This spec gives a future implementation a small target: accept or refuse one proposed governing transition while preserving current authority, candidate identity, refusal, prior-governing preservation, and non-claims.

## 4. What Now Stands

The current body materially has:

- canonical core execution line: `src/integrity_host_v0_min_coexistence_v2.py`
- current execution-authority resolution
- preserved-run family packet
- preserved-run status packet
- current governing packet
- preserved eligible non-authority visibility
- preserved ineligible visibility
- explicit non-claims around replay, merge, continuity completion, standing upgrade, final system identity, and final governance

These surfaces make current governing status visible. They do not yet implement governing transition mechanics.

## 5. Governing Transition Scope

This transition slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It governs bounded change between preserved runs already visible in the preserved-run family and preserved-run status packet.

It does not:

- define cross-host continuity completion
- replay source actions into a live host
- merge preserved runs into a synthetic host state
- define final governance of all future run families
- define final persistence or registry architecture
- create system identity law beyond the current preserved-run family

A governing transition under this spec is an additive artifact-level authority change over preserved runs. It is not a host replay, not a merge, not a continuity completion, and not a standing upgrade.

## 6. Transition Object / Proposal Shape

A future implementation needs one bounded proposal object before it may consider governing change.

Minimum proposal shape:

```text
GoverningTransitionProposal {
  transition_proposal_id: string
  current_governing_source_run_path: string
  candidate_successor_source_run_path: string
  current_governing_ingress_run_path: string
  candidate_successor_ingress_run_path: string
  current_governing_comparison_artifact_path: string
  candidate_successor_comparison_artifact_path: string
  proposal_basis_ref: string
  proposed_at: string
  proposed_by_surface: string
}
```

Rules:

- `transition_proposal_id` must be non-empty and stable within the emitted proposal.
- current-governing paths must refer to the run currently named by the current-governing packet.
- candidate-successor paths must refer to one preserved run already visible in the preserved-run status packet.
- `proposal_basis_ref` must be non-empty.
- `proposed_at` must be explicit.
- `proposed_by_surface` identifies the bounded surface that emitted or submitted the proposal. It is not semantic source and not final governance authority.

This object is intentionally narrow. It is not a broad governance record model.

## 7. Candidate Source Requirements

A candidate successor run may be considered only if all of the following are true:

- the candidate source run is preserved
- the candidate source run is visible in the preserved-run family packet
- the candidate source run is visible in the preserved-run status packet
- the candidate has bounded role `PRESERVED_ELIGIBLE_NON_AUTHORITY`
- the candidate remains eligible under current execution-authority criteria
- the candidate corresponds to its receiving-ingress run
- the candidate corresponds to its source-to-ingress comparison artifact
- the candidate canonical core execution file matches the current canonical core execution file
- the candidate is not already the current governing run

Eligibility alone is not transition. Eligibility only means the candidate may be considered by an explicit proposal.

## 8. Current Governing Requirements

A governing transition may be considered only if the current governing run is still explicit and readable.

Minimum requirements:

- the current governing run is explicit in the current-governing packet
- the current governing run corresponds to the current execution-authority resolution
- the current governing run is present in the preserved-run family packet
- the current governing run is present in the preserved-run status packet with role `CURRENT_EXECUTION_AUTHORITY`
- the current governing run's source run remains readable
- the current governing run's ingress run remains readable
- the current governing run's comparison artifact remains readable
- the current governing run will remain preserved after any accepted transition

Transition must not erase, overwrite, or hide the prior governing run.

## 9. Transition Checks

A future implementation must accept a governing transition only when all bounded checks pass.

Minimum required checks:

- canonical core execution file matches across authority, family, status, governing, current-governing, and candidate surfaces
- current governing source run path in the proposal matches the current-governing packet
- current governing ingress run path in the proposal matches the current-governing packet
- candidate successor source run path is explicit and readable
- candidate successor ingress run path is explicit and readable
- candidate successor comparison artifact path is explicit and readable
- candidate successor has status role `PRESERVED_ELIGIBLE_NON_AUTHORITY`
- candidate successor still passes bounded authority eligibility
- candidate successor is not already current governing
- proposal basis is non-empty
- proposal source surface is non-empty
- replay remains false
- merge remains false
- continuity completion remains false
- standing upgrade remains false
- prior governing run remains preserved after transition
- transition result is explicit and not inferred from latest-emitted or latest-eligible ordering alone

These checks are bounded and implementation-facing. They do not create a broad governance engine.

## 10. Refusal Conditions

Refusal must remain explicit. A future implementation must not collapse refusal into generic invalidity or silent non-movement.

Minimum refusal conditions:

- `CANDIDATE_NOT_PRESERVED`
- `CANDIDATE_NOT_VISIBLE_IN_STATUS_PACKET`
- `CANDIDATE_NOT_ELIGIBLE`
- `CANDIDATE_ALREADY_CURRENT_GOVERNING`
- `CURRENT_GOVERNING_MISSING`
- `CURRENT_GOVERNING_UNREADABLE`
- `CANONICAL_EXECUTION_LINE_MISMATCH`
- `MISSING_PROPOSAL_BASIS`
- `MISSING_PROPOSAL_SOURCE_SURFACE`
- `REPLAY_BASED_TRANSITION_REFUSED`
- `MERGE_BASED_TRANSITION_REFUSED`
- `CONTINUITY_COMPLETION_SHORTCUT_REFUSED`
- `SILENT_STANDING_UPGRADE_REFUSED`
- `PRIOR_GOVERNING_ERASURE_REFUSED`
- `LATEST_EMITTED_INFERENCE_REFUSED`
- `LATEST_ELIGIBLE_INFERENCE_REFUSED`

Each refused transition must preserve:

- the proposal identity
- the current governing run named by the proposal where readable
- the candidate successor named by the proposal where readable
- the refusal code
- the refusal reason
- the non-claims that remain false

Refusal is part of the transition surface. It must not disappear into logs or operator memory.

## 11. Accepted Transition Result

An accepted transition means only the following bounded change:

- the prior governing run becomes preserved non-authority
- the candidate successor becomes current governing
- preserved-run multiplicity remains visible
- preserved eligible non-authority runs remain visible
- preserved ineligible runs remain visible
- no preserved run is erased
- no source artifact is mutated
- no ingress artifact is mutated
- no comparison artifact is mutated
- no authority, family, status, or governing input artifact is overwritten
- no replay is performed
- no merge is performed
- no continuity completion is claimed
- no standing upgrade is claimed
- the result is preserved in an explicit result artifact

Accepted transition does not prove final governance. It proves only that one bounded governing change was proposed, checked, accepted, and preserved under this spec.

## 12. Transition Result Artifact

A future implementation needs one bounded result artifact for each proposed governing transition.

Minimum result shape:

```text
GoverningTransitionResult {
  transition_result_id: string
  transition_result_type: string
  transition_result_version: string
  generated_at: string
  proposal: GoverningTransitionProposal
  current_governing_before: {
    source_run_path: string
    ingress_run_path: string
    comparison_artifact_path: string
  }
  candidate_successor: {
    source_run_path: string
    ingress_run_path: string
    comparison_artifact_path: string
  }
  current_governing_after: {
    source_run_path: string | null
    ingress_run_path: string | null
    comparison_artifact_path: string | null
  }
  outcome: ACCEPTED | REFUSED
  refusal_code: string | null
  refusal_reason: string | null
  result_basis_ref: string
  non_claims: {
    continuity_completed: false
    standing_upgraded: false
    replayed_into_live_host: false
    merged_into_local_state: false
    minimum_lawful_system_completed: false
    final_system_identity_completed: false
    final_preserved_run_governance_completed: false
    final_governing_scope_completed: false
    final_governing_transition_law_completed: false
  }
}
```

Rules:

- accepted results must name the new current governing run in `current_governing_after`
- refused results must not invent a new current governing run
- refusal code and refusal reason must be present when `outcome` is `REFUSED`
- refusal code and refusal reason must be null when `outcome` is `ACCEPTED`
- `result_basis_ref` must be non-empty
- non-claims must be carried forward explicitly

This artifact is a local engineering surface. It is not a registry system or final event-sourcing design.

## 13. Governing Status After Transition

After an accepted transition:

- the prior governing run remains preserved
- the prior governing run is no longer `CURRENT_EXECUTION_AUTHORITY` for the current governing packet emitted after transition
- the prior governing run should become preserved non-authority unless later checks make it ineligible
- the new governing run becomes the current governing run
- other preserved eligible non-authority runs remain preserved and non-governing
- preserved ineligible runs remain preserved and ineligible
- preserved-run multiplicity remains visible

After a refused transition:

- the current governing run remains current
- the candidate successor remains in its prior status
- no preserved run is erased
- refusal remains visible as the result of the proposal

This section does not define final governance hierarchy. It defines only bounded status movement around one proposed transition.

## 14. What This Spec Still Does Not Define

This spec still does not define:

- final governance framework
- final currentness doctrine
- final system identity law
- final continuity completion
- replay or merge law
- persistence architecture
- registry doctrine
- full world-frame
- minimum lawful system
- cross-host continuity
- distributed synchronization
- broad policy engine

It also does not claim that a future accepted governing transition completes continuity or upgrades standing.

## 15. What Should Not Be Added Next

The repo should not add:

- automatic promotion logic by recency alone
- replay-based transition implementation
- merge-based transition implementation
- broad governance engine
- persistence or registry machinery as a substitute for transition law
- new packet surfaces that only restate transition status without adding checks or refusal visibility
- final system identity claims based on one accepted transition

The next implementation, if any, should stay inside this bounded proposal-check-result surface.

## 16. Closing Boundary Statement

The repository now has current authority, preserved-run statuses, and current governing scope.

This spec exists because the next forced pressure is governing transition mechanics.

It defines the smallest bounded transition model now supportable: one explicit proposal, one current governing run, one eligible non-authority candidate, bounded checks, explicit refusal, explicit accepted result, preserved prior governing visibility, and carried-forward non-claims.

It does not claim final transition law, final governance, continuity completion, replay or merge law, or system completion.
