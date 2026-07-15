# IAMMAI Embodiment Decision v0

## 1. Purpose

This file makes the first explicit embodiment decision for IAMMAI.

Its job is to decide, in bounded architectural terms, where the first execution slice runs, whether it is internal-first or public-first, which runtime parts must be fully real, which parts may remain simplified without invalidating the slice, how success is observed, how failure remains visible, and what the execution posture of the first slice actually is.

It does not yet try to define:
- code
- a deployment plan
- a product roadmap
- an infrastructure diagram
- broad rollout design
- generalized operating policy

It is a bounded embodiment-decision document.

## 2. First Principle

The embodiment decision must serve the constitutional core.

The first slice must remain bounded.  
The first slice must be real enough to count.  
Execution posture must not silently distort the architecture.

In runtime terms, this means the first execution posture must preserve the minimum lawful runtime body as a real body rather than replacing it with demo convenience, interface theater, or selective role collapse.

## 3. Why an Embodiment Decision Is Needed

Defining the slice is not yet enough.

- `MINIMAL_LAWFUL_EMBODIMENT.md` defines what kind of first live form counts.
- `FIRST_EXECUTION_SLICE.md` selects one bounded first live cycle.
- An embodiment decision is still needed to say how that slice is actually to be run.

The architecture now needs a concrete execution posture because a first live move should be explicit rather than implied. Without that decision, the same slice could be enacted in ways that silently distort neutrality, hide failure, privilege a product surface, or treat partial simulation as proof.

This decision therefore sits between architecture and build. It does not implement the slice, but it constrains what implementation must and must not do if the first embodiment is to count.

## 4. Chosen Execution Posture

The first execution slice shall run **internal-first in a small, controlled, auditable, non-market-facing runtime context**.

This means:

- the first run is not public-first
- the runtime context is bounded to one selected matter and one selected cycle
- the execution surface is neutral and non-productized
- no broad deployment is implied
- no market-facing rollout is implied
- no private product captures the constitutional body by being first

The first slice should therefore run in a controlled environment whose purpose is lawful embodiment and auditability, not public presentation. It may later be selectively shareable, but its first posture is internal-first, bounded, and neutral.

## 5. Runtime Parts That Must Be Fully Real

For the first slice to count, the following runtime parts must be fully real in the selected cycle:

- a real Interface Gateway path for the bounded input or contact
- a real Validator performing the required checks
- a real Witness Emitter producing witness trace where constitutionally relevant
- a real Governor because the selected first slice is governance-required
- a real State Engine performing lawful movement or preserving visible non-movement
- a real Registry / Store preserving the canonical records actually produced

For this slice, none of the proof-bearing runtime roles may be replaced by summary, operator memory, interface display, or generic logging. The selected cycle requires the full minimum runtime body to be present in bounded form.

## 6. Runtime Parts That May Be Stubbed or Bounded

The first slice may remain simplified only at the edges.

The following may be bounded or minimally implemented without invalidating the slice:

- the Interface Gateway may be a minimal structured operator surface rather than a product UI
- execution may be synchronous and single-context rather than distributed
- queueing, retries, buffering, concurrency handling, and orchestration machinery may be absent
- derivative read surfaces such as dashboards, exports, analytics, or convenience APIs may be absent
- unselected transition families, resolution families, and broad multi-matter behavior may remain unimplemented

The following may **not** be stubbed if the slice is to count:

- validation itself
- witness emission where constitutionally required in the selected cycle
- governance action for the chosen governance-required move
- state movement or visible non-movement handling
- canonical preservation

Minimal implementation is allowed. Fake substitution is not.

## 7. Success Observation

Success should be observed through canonical artifacts and visible runtime truth, not through presentation surfaces.

At minimum, a successful slice should allow an internal reader or operator to verify:

- the bounded matter that was selected
- the input or contact that entered the cycle
- the validation artifact for the required checks
- the witness artifact or artifacts that were actually emitted
- the governance action record showing authorize, deny, or HOLD outcome
- the transition record where movement or containment-relevant effect occurred
- the state record where truth formation lawfully occurred
- registry preservation of the canonical records actually produced

A completed lawful cycle is observed when the canonical records show either:

- lawful movement into truth with the required upstream basis and preservation
- or lawful non-passage with typed trace and visible preservation of what did not proceed

The reader must be able to verify the cycle from canonical artifacts rather than from narrative explanation alone.

## 8. Failure Visibility

Failure must remain visible in the first slice or the slice does not count as lawful embodiment.

At minimum, the following must remain visible:

- validation non-passage
- missing witness where witness was constitutionally relevant
- governance non-progression where governance was required
- failed or blocked state movement
- failed, incomplete, or missing canonical preservation

Invisible failure invalidates the integrity of the slice because it allows apparent continuity to replace runtime truth.

Derivative surfaces, operator summaries, or interface state must not hide:

- that validation did not pass
- that witness did not occur
- that governance did not proceed
- that state did not move
- that canonical preservation failed

## 9. Boundaries of the First Embodiment

The first embodiment does not attempt:

- broad adoption
- private privilege
- UI theater
- scale claims
- full environment completion
- generalized ambient intelligence claims

It also does not attempt to prove the whole runtime family at once. It proves one bounded slice in a way that remains structurally neutral and architecturally lawful.

## 10. Relation to the Existing Repo

This decision depends on the existing repo structure as follows:

- the constitutional core defines the law and remains the semantic source of truth
- the architecture layer defines the minimum runtime body and anti-collapse separations
- the implementation layer defines state, records, transition, witness, governance, and validation structure
- the schema family defines the typed artifact surfaces used by the slice
- the runtime layer defines flow, contract, coordination, handoff, and failure logic
- `MINIMAL_LAWFUL_EMBODIMENT.md` defines what counts as first lawful embodiment
- `FIRST_EXECUTION_SLICE.md` selects the specific first cycle this decision now places into execution posture

This document therefore does not introduce a new theory. It makes an execution decision inside the architecture already present in the repo.

## 11. Open Questions

The following remain intentionally open after this decision:

- the exact host implementation
- the operator surface choice
- the technical execution details
- whether the first slice remains fully internal or becomes selectively shareable after first run
- what build artifact comes first after this decision

These are embodiment and build questions, not constitutional ambiguities.

## 12. Summary

This document makes the first embodiment decision for IAMMAI by setting the first execution slice to internal-first, controlled, auditable execution in a neutral runtime context with the full minimum runtime body present for the selected governance-required cycle.

Its purpose is to make the first live move explicit enough to build without allowing public theater, private capture, or partial simulation to masquerade as lawful embodiment.

**One-Line Definition:** `EMBODIMENT_DECISION_v0.md` defines the first execution posture of IAMMAI as an internal-first, bounded, auditable run of the selected first slice in which the proof-bearing runtime roles are fully real and failure remains visible.
