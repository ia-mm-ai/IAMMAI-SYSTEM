# Current Governing Transition Boundary

## 1. Purpose

This file is a bounded transition-boundary note for the current governing run under preserved-run multiplicity in `IAMMAI-SYSTEM`.

It exists because the repository now has:

- current execution authority resolution
- preserved-run family visibility
- preserved-run status roles
- current governing scope

Those surfaces make a new question possible: what would have to be true before current governing authority could lawfully change from one preserved run to another?

The next forced pressure is no longer packaging or visibility. The current stack can already identify a current governing run and preserve non-governing runs. The pressure now is bounded transition: what may change, what may not change, and what must remain explicitly false while any future transition is considered.

This file does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, or a new note family.

## 2. Status And Rank

This note is additive and repo-local.

It ranks below the constitutional and reference authority surfaces under `reference/IAMMAI/`, including the constitutional protocol, implementation overviews, runtime contract surfaces, and architecture surfaces.

It also ranks below executable source, tests, and generated artifacts where those surfaces already stand as concrete behavior.

This note does not:

- define final governance
- complete continuity
- replace executable source files
- replace test surfaces
- replace emitted artifacts
- promote current governing status into final system law
- promote preserved-run eligibility into automatic governing transition

Its function is to state the first governing-transition boundary forced by the current executable stack.

## 3. Why This Note Is Needed Now

The repository now distinguishes:

- current governing run
- preserved eligible non-authority runs
- preserved ineligible runs

Once those roles exist explicitly, their relation over time can no longer remain only implicit. Without one bounded clarification, the repo risks one of two collapses:

- silently assuming that "latest eligible wins"
- silently hardening the current governing run into permanent authority

Neither assumption is justified by the current stack.

The current stack can resolve and package current governing status. It does not yet define lawful transition mechanics between governing runs.

## 4. What Now Stands

The current body materially has:

- canonical core execution line: `src/integrity_host_v0_min_coexistence_v2.py`
- current execution-authority resolver: `src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py`
- preserved-run family packet builder: `src/build_integrity_host_v0_min_coexistence_run_family_packet.py`
- preserved-run status packet builder: `src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py`
- current-governing packet builder: `src/build_current_integrity_host_v0_min_coexistence_governing_packet.py`
- executable tests around authority, family, status, and governing packet behavior
- explicit bounded non-claims around replay, merge, continuity completion, standing upgrade, final system identity, and final governance

These surfaces make current authority and current governing scope visible. They do not implement governing transition law.

## 5. What The Current Stack Already Distinguishes

The current stack now distinguishes, in bounded form:

- current execution authority
- preserved eligible non-authority
- preserved ineligible
- current governing scope
- preserved non-governing visibility

These are explicit statuses, not inferred counts.

`CURRENT_EXECUTION_AUTHORITY` identifies the preserved run that current artifacts treat as governing for the canonical core execution line.

`PRESERVED_ELIGIBLE_NON_AUTHORITY` identifies a preserved run that passed the bounded eligibility checks but is not currently governing.

`PRESERVED_INELIGIBLE` identifies a preserved run that remains visible but lacks the required correspondence, validation, comparison, or non-claim posture to be eligible.

The current-governing packet keeps preserved non-governing runs visible. It does not erase them by selecting one governing run.

## 6. Transition Pressure Now Visible

Once multiple preserved runs can be eligible, preserved, and non-governing, the next forced pressure is transition.

The concrete questions are:

- what allows one eligible non-authority run to become current governing
- what displaces the current governing run
- whether displacement is automatic, explicit, or not yet lawful
- what artifact would preserve the reason for any change
- what happens to the prior governing run after a change

The current stack answers only part of this. It can resolve a current authority from preserved artifacts and package the current governing run. It does not yet preserve a transition relation between a prior governing run and a candidate successor governing run.

## 7. What Must Not Be Assumed

The current stack does not justify assuming any of the following:

- latest emitted run automatically becomes current governing
- latest eligible run automatically becomes current governing
- preserved eligible non-authority has a standing claim to replace current governing by recency alone
- current governing is permanent by default
- transition can occur by replay
- transition can occur by merge
- transition implies continuity completion
- transition upgrades standing silently
- transition upgrades authority silently
- a new current-governing packet by itself proves lawful transition mechanics

Recency may be used by current tooling only after bounded eligibility checks. That is not the same thing as transition law.

## 8. Candidate Transition Models

### A. Automatic Latest-Eligible Transition

This model says the latest preserved run that passes bounded eligibility checks becomes current governing automatically.

This is visible as a temptation because the execution-authority resolver selects the lexically latest eligible candidate. But it is too strong as governing-transition law.

The current resolver answers "which candidate is current under this bounded resolution pass." It does not preserve a transition trigger, transition proposal, displacement reason, prior-governing disposition, or transition-specific refusal path.

Automatic latest-eligible transition would risk collapsing currentness into recency.

### B. Explicit Bounded Transition Only

This model says transition is not automatic. A governing change would require an explicit bounded condition or decision surface that names the current governing run, names the candidate successor run, checks the relation between them, preserves the result, and keeps non-claims intact.

This is the safest current read.

It respects the current authority resolver while refusing to treat selection as full transition mechanics. It keeps preserved eligible non-authority visible without giving it a self-executing promotion path.

### C. No Transition Currently Lawful

This model says no governing change is currently lawful because the repository has no transition mechanism at all.

This is also a plausible bounded read if the current stack is judged strictly. The current body can produce a current governing packet, but it does not yet define how one governing run lawfully yields to another.

Under this read, a future governing change would require new bounded transition work before it could be called a lawful transition rather than a newly emitted currentness surface.

## 9. Current Best Boundary Read

The best current boundary read is:

- current governing transition is not automatic
- current governing transition is not yet lawfully implemented
- preserved eligible non-authority is a visible bounded status, not a self-executing promotion path
- any future governing change requires an additional explicit bounded mechanism or decision surface
- until that exists, current governing remains current by resolved authority, not by permanent metaphysical status and not by automatic recency logic

This does not deny that the authority resolver can identify a current run from eligible candidates. It says that current selection and governing transition are not the same artifact or the same claim.

## 10. Minimum Preconditions A Future Transition Mechanism Would Likely Need

Without defining the mechanism, a future lawful governing-transition surface would likely need at least:

- explicit transition trigger or proposal surface
- explicit identity of the current governing run
- explicit identity of the candidate successor run
- explicit relation between current governing run and candidate successor run
- explicit check that the candidate remains eligible under bounded authority rules
- explicit check that preserved non-claims remain intact
- explicit refusal paths when transition is not lawful
- explicit result artifact
- explicit rule for what happens to the prior governing run after transition
- no replay shortcut
- no merge shortcut
- no continuity completion shortcut
- no standing upgrade shortcut

Those are minimum pressures, not a mechanism design.

## 11. What Should Not Be Added Next

The repo should not add:

- automatic promotion logic by recency alone
- replay-based governing transition
- merge-based governing transition
- broad governance engine
- final persistence or registry machinery as a substitute for transition law
- new packet surfaces that only restate current statuses without new transition pressure
- abstract theory notes that do not constrain the next executable or decision boundary

The current stack is large enough that additional work should answer a forced transition question, not merely add another inspection layer.

## 12. What The Next Lawful Step Likely Is

The next lawful step should likely be one bounded governing-transition mechanism, spec, or decision surface.

That surface should answer, in small executable or specification form:

- what triggers a proposed governing change
- what candidate run may be considered
- what checks are required before change
- what refusal looks like
- what artifact preserves the result
- how the prior governing run remains preserved

It should not be another comparison helper by default. It should not be another packet unless a genuine transition pressure forces packet form. It should not become a broad theory note family.

## 13. Explicit Non-Claims

This note does not define:

- final governing transition law
- final currentness doctrine
- final system identity law
- final continuity completion
- final replay or merge law
- final governance framework
- minimum lawful system
- final world-frame
- final persistence architecture
- final registry doctrine

It also does not claim that current execution-authority resolution, run-family packet creation, preserved-run status packet creation, or current-governing packet creation completes lawful transition mechanics.

## 14. Closing Boundary Statement

The repository now has explicit current authority, preserved-run statuses, and current governing scope.

This note exists because the next forced pressure is transition, not packaging.

It bounds what must not yet be assumed: no automatic latest-run promotion, no replay or merge transition, no continuity completion, no silent standing upgrade, and no final governance claim.

It does not yet claim lawful governing-transition implementation.
