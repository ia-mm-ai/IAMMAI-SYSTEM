# CURRENT SELF-ORIENTATION RE-ENTRY RECEIPT V0 MIN SPEC

## 1. Purpose

This file defines the first bounded current-self-orientation re-entry receipt
spec for the present `IAMMAI-SYSTEM` execution line.

Current self-orientation re-entry receipt is a bounded verification surface
that decides whether one previously admitted next step was actually performed
within admitted bounds, and whether that admission is now exhausted without
creating follow-on permission.

The clean sequence is:

- self-orientation lets the body find itself
- re-entry admissibility lets one declared next step enter from that exact
  basis
- re-entry receipt proves that the admitted step was actually performed within
  bounds and that the permission is now exhausted

The question here is not:

`May this step enter?`

That was re-entry admissibility.

The question here is:

`Was this exact admitted step actually received/performed within bounds, and
is that admission now closed?`

This file defines the smallest lawful closure and exhaustion surface after
admission. It does not define implementation code, tests, schemas, generated
views, workflows, orchestration, roadmap tracking, final governance,
continuity completion, final system identity, or persistence architecture.

## 2. Status and Rank

This is an additive v0-min re-entry receipt spec for the present execution
line only.

It ranks below constitutional and reference authority surfaces, including the
preserved `reference/IAMMAI/` surfaces and the current executable source,
tests, and artifacts that already stand in the repository.

This spec does not create authority. It does not define final governance. It
does not complete continuity. It does not complete final system identity. It
does not replace current executable source, tests, standing artifacts,
self-orientation results, or re-entry admissibility results.

This spec defines a bounded receipt/refusal surface. Receipt through this
surface is not source creation, not authority creation, not a standing
upgrade, not general permission, and not permission for follow-on work.

## 3. Why This Spec Is Needed Now

The body can now find itself from preserved artifacts through current
self-orientation.

One next declared step can now be admitted through current self-orientation
re-entry admissibility.

That creates the next structural pressure: if an admitted result is not closed
by a receipt, the admission can remain as a hanging permission token. That
would create a new sovereignty leak: `admitted once` drifting into `usable
again`, `usable generally`, or `permission for continuation`.

Therefore one bounded re-entry receipt surface is required. It must prove that
the admitted step was actually performed within the admitted bounds and that
the admission is now consumed. It must not turn admission into reusable
permission and must not turn receipt into workflow machinery.

## 4. What Now Stands

The following surfaces now materially stand as relevant context for this
receipt surface:

- current self-orientation v2 as an internal derived recognition surface
- current self-orientation re-entry admissibility as the single-step gate
  between recognition and continuation
- current-state answer/read, query, what-stands-now, what-remains-open, and
  admissibility/touch-permission surfaces
- continuity transfer unit and continuity transfer receipt surfaces
- received derivative participation and received derivative action-permission
  surfaces
- continuity memory seam surface
- v0 body-pass surface
- bounded OpenAI API derivative vessel v3 surface
- operator-facing terminal brief surface
- carried non-claims that remain false

This is not a whole-body recap. These surfaces are named only because a
receipt must verify that the admitted basis, performed step, hierarchy, and
non-claims did not drift during performance.

## 5. Re-Entry Receipt Scope

This surface applies only to one `REENTRY_ADMITTED` result and one actual
performed step, result, or artifact claimed to satisfy that admitted step.

It decides receipt or refusal for that one admitted step only.

It does not:

- authorize any further step
- generate the next task
- decide the body's roadmap
- track a roadmap
- mutate prior artifacts
- overwrite upstream surfaces
- define workflow machinery
- define orchestration
- define signaling or regulation
- define replay or merge law
- explain the repository for outsiders
- turn admission into a reusable permission token
- turn receipt into source, governing, current, derivative, or operator
  authority

Re-entry receipt is not general continuation permission. It is the narrow
post-admission verification that one admitted step was actually performed
within bounds and that the admission is now closed.

## 6. Required Input Pair

The receipt surface requires exactly two inputs:

1. one `REENTRY_ADMITTED` result
2. one actual performed step, result, or artifact claimed to satisfy that
   admitted step

Both inputs are required.

A blocked, refused, unreadable, or malformed re-entry admissibility result
cannot drive receipt.

A missing, unreadable, malformed, promissory, or vague performed-step artifact
cannot be received lawfully.

The receipt surface must not infer performance from narration, intention,
operator memory, recency, or the fact that an admission exists. It must verify
one actual performed artifact or result against the admitted step.

## 7. Receipt Input Shape

The receipt input is a candidate for closure. It is not proof by itself and is
not a permission slip.

### 7.1 `admitted_reentry_basis`

The receipt input must preserve:

- `reentry_admissibility_result_path`
- `reentry_admissibility_result_id`
- `reentry_admissibility_result_version`
- `reentry_admissibility_outcome`
- `reentry_admissibility_resolver_module`

Required posture:

- `reentry_admissibility_outcome` must be `REENTRY_ADMITTED`
- the selected admissibility result may be used as the admitted basis only
- the admissibility result may not become source authority, current authority,
  or reusable permission

### 7.2 `locked_admitted_basis`

This section is required.

The receipt surface must preserve and verify the locked admitted basis already
carried through the admissibility result.

At minimum it must preserve:

- `selected_body_pass_result_id`
- `selected_body_pass_result_path`
- `selected_source_surface_id`
- `selected_source_surface_path`
- `selected_current_state_answer_read_id`
- `selected_current_state_answer_read_path`
- `selected_what_stands_now_id`
- `selected_what_stands_now_path`
- selected effective references, including:
  - `effective_authority_artifact_path`
  - `effective_family_packet_path`
  - `effective_status_packet_path`
  - `effective_current_governing_packet_path`
  - `effective_source_run_path`
  - `effective_ingress_run_path`

Receipt must not re-resolve a different basis. It must not silently substitute
a newer or fresher basis. It must verify continuity of the exact admitted
basis.

The lock preserves hierarchy. It does not create new authority.

### 7.3 `admitted_next_step`

The receipt input must preserve the admitted next-step declaration from the
admissibility result, including:

- `next_step_family`
- `next_step_kind`
- `target_surface_family`
- `target_surface_path`
- `target_surface_id`
- `declared_purpose`
- `declared_expected_output_family`
- `requested_relation_to_basis`

This section is the step that was admitted. Receipt must verify performance
against this declaration rather than against a later narrative about what was
done.

### 7.4 `performed_step_receipt_candidate`

The receipt input must identify one actual performed step, result, or artifact.

At minimum it must preserve:

- `performed_step_path`
- `performed_step_id`
- `performed_step_family`
- `performed_step_outcome`
- `performed_step_type`
- `performed_step_generated_at`
- `performed_step_resolver_or_emitter_module`

The receipt candidate must be one actual performed artifact or result. It may
not be a promise, roadmap, task description, implementation plan, informal
summary, human narration fallback, or vague statement.

The candidate must correspond to the admitted next step. It must not smuggle
in extra outputs, broadened scope, source replacement, mutation, replay, merge,
or follow-on authorization.

## 8. What Receipt Must Verify

A future implementation must perform at least these checks before emitting
`REENTRY_RECEIVED`:

- the selected re-entry admissibility result is readable
- the selected re-entry admissibility result is well-formed
- the selected re-entry admissibility result has outcome `REENTRY_ADMITTED`
- the locked admitted basis still matches the admissibility result
- the locked upstream basis remains readable where required
- the performed step or result exists
- the performed step or result is readable
- the performed step or result is well-formed
- the performed step or result matches the admitted `next_step_family`
- the performed step or result matches the admitted `next_step_kind`
- the performed step or result matches the admitted target surface family,
  path, and id where applicable
- the performed step or result matches the admitted expected output family
- the performed step or result remains within `one_step_only` scope
- no mutation, replay, or merge occurred
- no overwrite, extra write, or broadened scope occurred
- derivative, API, and operator-facing surfaces remain downstream only
- current and governing basis remain upstream-derived
- open surfaces remain open
- blocked and refused surfaces remain visible where selected
- non-claims remain false
- the admission is now exhausted rather than reusable
- receipt does not authorize follow-on steps

`REENTRY_RECEIVED` may be emitted only when the performed artifact or result is
lawfully proportioned to the admitted result and the admission is closed by
that one performance.

## 9. Exhaustion / Closure Principle

Receipt is not just `we saw an output`.

Receipt must prove all of the following:

- the admitted step was the step actually performed
- the performed step stayed within the admitted scope
- the admission has now been consumed by that one performed step
- the admission may not be reused as a standing permission object
- the admission may not authorize another step by implication
- nothing in receipt creates follow-on authorization

The receipt closes the admitted permission. It does not extend it.

If a result says or implies that the admission remains available for later
use, that receipt must block. If a result says or implies that the performed
step creates general continuation permission, that receipt must block.

Exhaustion is central to this surface because without it, admission becomes a
reusable token. The lawful receipt posture is single-use, additive, preserved,
and closed.

## 10. Refusal / Block Conditions

The re-entry receipt result must block explicitly for at least these
conditions:

- admissibility result is not `REENTRY_ADMITTED`
- admissibility result is unreadable
- admissibility result is malformed
- locked admitted basis is missing
- locked admitted basis mismatches the admissibility result
- locked upstream basis is no longer readable where required
- performed step is missing
- performed step is unreadable
- performed step is malformed
- performed step family mismatches the admitted step
- performed step kind mismatches the admitted step
- target surface family, path, or id mismatches the admitted step
- expected output family mismatches the admitted step
- admission scope is exceeded
- mutation, replay, or merge is detected
- overwrite, extra output, or broadened scope is detected
- derivative, API, or operator-facing surfaces are treated as authority
- current or governing basis is inferred from derivative, API, or
  operator-facing surfaces
- open surfaces are treated as completed
- blocked or refused surfaces are hidden
- non-claims are missing or flipped
- receipt attempts to authorize follow-on steps
- receipt attempts to create general continuation permission
- admission is not exhausted
- reusable permission is implied
- latest-file recency is used to substitute basis or performed output
- human narration is used instead of bounded performed evidence

Blocked receipt is not blocked re-entry admissibility. It is refusal of
closure and exhaustion for the admitted step.

## 11. Result Artifact

A future implementation must emit one bounded result artifact with at least
these top-level sections:

- `current_self_orientation_reentry_receipt_metadata`
- `selected_reentry_admissibility_result`
- `locked_admitted_basis`
- `selected_performed_step`
- `reentry_receipt_checks`
- `outcome`
- `block`
- `reentry_receipt_basis`
- `non_claims`

Minimum metadata:

- `reentry_receipt_result_id`
- `reentry_receipt_result_type`
- `reentry_receipt_result_version`
- `generated_at`
- `resolver_module`

Minimum outcome family:

- `REENTRY_RECEIVED`
- `BLOCKED`

`selected_reentry_admissibility_result` must preserve the selected
admissibility result id, path, version, resolver module, and outcome.

`locked_admitted_basis` must preserve the admitted locked basis as verified
against the admissibility result.

`selected_performed_step` must preserve the performed step id, path, family,
kind where exposed, type, outcome, generated-at value, and resolver or emitter
module.

`reentry_receipt_checks` must show the bounded checks actually used, including
basis matching, performed-step correspondence, single-step scope, non-mutation,
hierarchy preservation, non-claim preservation, and exhaustion.

`reentry_receipt_basis` must explain only why this one admitted step was
received or blocked. It must not become a roadmap, workflow state, standing
permission, governance result, or authority surface.

`non_claims` must remain explicit and false where the result carries false
posture. At minimum, the receipt result must not claim:

- authority creation
- continuity completion
- final governance completion
- final system identity completion
- standing upgrade
- source replacement
- derivative or operator authority upgrade
- general permission creation
- follow-on authorization
- admission reusability
- mutation performed
- replay performed
- merge performed
- roadmap generation
- workflow engine creation

For `REENTRY_RECEIVED`, the result proves only that the one admitted step was
performed within bounds and that the admission is exhausted.

For `BLOCKED`, the result should preserve the selected admissibility identity,
the locked admitted basis where available, the performed-step candidate where
available, the block code, the block reason, bounded check details, and
non-claims.

## 12. What Remains Preserved

After receipt or refusal:

- the self-orientation artifact remains preserved
- the re-entry admissibility artifact remains preserved
- the locked basis remains preserved
- the performed-step artifact remains preserved
- upstream current, governing, current-state, continuity, derivative, API, and
  operator-facing artifacts remain preserved
- source remains source
- derivative remains derivative
- operator-facing derivative remains operator-facing derivative
- open remains open
- blocked or refused remains visible when selected
- receipt of one step does not authorize the next step
- refusal does not rewrite the admissibility result
- refusal does not rewrite the performed-step candidate
- refusal does not rewrite upstream current-state or continuity posture

The receipt surface is additive. It does not mutate prior artifact families.

## 13. What This Spec Still Does Not Define

This spec still does not define:

- a workflow engine
- orchestration
- roadmap generation
- autonomous continuation
- autonomous next-organ determination
- body-wide signaling or regulation
- final governance
- continuity completion
- final system identity
- broad participation doctrine
- persistence or registry architecture
- general permission surfaces
- replay or merge machinery
- external-reader orientation
- generated markdown views
- README or onboarding output

## 14. What Should Not Be Added Next

The next step should not add:

- a reusable permission token
- general continuation permission
- workflow machinery hidden inside receipt
- follow-on authorization leakage
- derivative, API, or operator authority upgrades
- recency-based basis substitution
- roadmap or autonomy signaling through closure language
- mutation, replay, or merge by receipt
- final governance claims
- continuity completion claims
- final system identity claims

The next lawful implementation, if built, should remain one bounded
receipt/refusal resolver over the exact input pair defined here.

## 15. Closing Boundary Statement

Self-orientation lets the body find itself.

Re-entry admissibility lets one next step enter through that found-self.

Re-entry receipt proves that this admitted step was actually performed within
bounds.

Receipt exhausts the admission rather than extending it.

Nothing in this surface becomes sovereignty.
