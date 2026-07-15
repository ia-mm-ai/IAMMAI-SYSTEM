# IAMMAI Decision Record Schema Admission Boundary

## 1. Purpose

This file defines the schema-admission boundary for decision record in first-pass form.

Its job is to answer, in one compact place:

- whether decision has now earned schema admission
- what that admission would and would not mean
- where such a schema would lawfully live, if admission is justified
- what still remains open even after this boundary is clarified

It does not define:

- a constitutional rewrite
- an implementation-family master map
- a schema file
- a runtime migration plan
- a storage architecture memo
- a graph or database design
- a distributed systems plan
- a roadmap
- a README
- a project-management note
- a manifesto

This file is additive only. It does not replace implementation, runtime, continuity, admissibility, accession, standing, vessel, bridge, review, current-state, or constitutional surfaces already standing in the body.

## 2. Why This Note Is Needed Now

Decision no longer lacks objecthood.

`implementation/DECISION_RECORD_OVERVIEW.md` already gives decision a bounded implementation-facing room. `implementation/STATE_MACHINE_OVERVIEW.md` already makes decision structurally real as a standing-state role. The visible body also already contains explicit decision surfaces in accession and vessel posture.

That means the exposed question is no longer whether decision exists. The exposed question is schema admission and schema placement.

The body therefore needs one explicit boundary note so later schema work does not proceed from memory, omission, or assumption.

## 3. What Already Stands

The following already stand for decision in the visible body.

- `implementation/DECISION_RECORD_OVERVIEW.md` gives decision explicit implementation-facing objecthood and distinguishes it from governance action, currentness, bridge carry, and generic review prose.
- `implementation/STATE_MACHINE_OVERVIEW.md` already defines decision as a distinct standing-state role: committed direction on the basis of preserved state, not truth itself and not applied effect.
- `implementation/CANONICAL_RECORDS_OVERVIEW.md` already preserves decision at state-model level by explicitly naming decision as one of the standing-state forms that implementation must keep distinct.
- `accession/ADMISSION_DECISION.md` stands as an explicit bounded decision surface for admitted, not-yet, and refused outcomes in the accession layer.
- `vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md` stands as an explicit bounded posture decision in a derivative local branch.
- `v1/34_POST_API_BACKED_POSTURE_BRIDGE.md` shows that the body already distinguishes a decision from its later carried consequence.
- `continuity/FIRST_PASS_CURRENTNESS_RECORD.md` already establishes that currentness is authority-locating rather than authority-generating, which helps keep decision and currentness distinct.

This is enough to say that decision already stands as a real visible concern in implementation-facing language and in actual body surfaces. It is not enough, by itself, to count as schema creation or runtime admission.

## 4. Why Schema Admission Is A Distinct Question

Having an overview is not yet the same as schema admission.

An overview gives decision one lawful room and one bounded set of distinctions. A schema-admission decision goes further. It says the body now has enough bounded clarity that machine-enforceable structure would be lawful rather than premature.

That question is not trivial or cosmetic.

- If decision is admitted too early and too broadly, schema convenience could freeze posture vocabulary, force false equivalence with governance, or force currentness and decision into one envelope.
- If decision is not admitted once it is already visibly real, implementation planning may continue to leave it under review prose, bridge prose, or state atmosphere alone, which would undercut the explicit housing now already created.
- Location matters because a decision schema placed under the wrong layer would distort rank. Put under `runtime/`, it would read too close to runtime merger. Put under `continuity/`, it would invite confusion with currentness housing. Put under governance framing, it would invite force-collapse.

Schema admission is therefore a distinct boundary question about readiness and placement, not a cosmetic continuation of prose.

## 5. Current Best Read Of Schema Admissibility

The current best bounded read is: yes, decision is now schema-admissible in first-pass form, but the family-versus-extension question remains open.

That answer is justified because the visible body already supplies all of the following:

- explicit implementation-facing objecthood through `implementation/DECISION_RECORD_OVERVIEW.md`
- strong state-structure grounding through `implementation/STATE_MACHINE_OVERVIEW.md`
- visible decision reality through `accession/ADMISSION_DECISION.md` and `vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md`
- explicit non-equivalence to currentness and bridge carry through the visible body and continuity notes

The admission claim should still remain bounded.

It does not mean that decision is now fully scheduled into the first schema set named in `implementation/SCHEMA_MAP.md`. It means the body now has enough lawful clarity that decision may be admitted into schema planning rather than left under ambient prose.

The safest first-pass answer is therefore:

- yes, decision has earned schema admission
- yes, that admission is bounded and first-pass only
- no, that admission has not yet been enacted as schema creation
- no, that admission does not settle whether decision becomes a standalone schema family or a bounded extension beside state and transition schema work
- no, that admission does not settle runtime or storage integration

## 6. Lawful Schema Placement

If decision is admitted to schema status, its lawful home is the implementation schema layer under `implementation/`, with primary adjacency to state and transition schema planning rather than to governance or continuity schema work.

That placement is the best current fit for three reasons.

- `implementation/SCHEMA_MAP.md` is already the body’s schema-planning surface. Even though it does not yet name decision, it remains the lawful layer within which that admission should be understood.
- `implementation/STATE_MACHINE_OVERVIEW.md` makes decision structurally real as a standing-state role, which places decision schema pressure nearest state and transition distinction rather than review prose.
- `implementation/GOVERNANCE_ACTION_OVERVIEW.md` already makes clear that governance is lawful force, not the same thing as decision. That rules out governance as the schema home.

The lawful placement is therefore:

- in the implementation schema line
- adjacent to state and transition schema planning
- not in `runtime/`
- not in `continuity/`
- not under governance as though decision were merely force-bearing action

The family-versus-extension question remains open in bounded form.

The visible body supports schema admission more clearly than it supports a final answer to whether decision should become:

- a standalone `decision_record.schema.json`
- or a bounded record-family extension within later state-record or standing-state schema work

That openness should remain explicit. Admission is justified. Final envelope geometry is not yet settled.

## 7. What Schema Admission Would Not Mean

Schema admission would not mean:

- runtime admission
- final vocabulary closure
- final canonical versus derivative storage decision
- governance or authority status
- currentness equivalence
- mechanism or checker implementation by default

It would also not mean that decision has become a currentness engine, a governance engine, or a state-machine implementation.

Schema admission means only that the body now has enough bounded clarity for decision to lawfully exist in the schema-planning layer when and if later schema work takes it up.

## 8. Relationship to Existing Surfaces

This note clarifies a boundary. It does not enact migration.

With `implementation/DECISION_RECORD_OVERVIEW.md`, it preserves that decision already has implementation-facing objecthood. This note narrows the next question from objecthood to schema admission.

With `implementation/CANONICAL_RECORDS_OVERVIEW.md`, it preserves that decision is already structurally present inside the standing-state model even though it has not yet been given explicit record-family treatment there. This note does not rewrite that file.

With `implementation/SCHEMA_MAP.md`, it preserves that the current first schema set still stands as written. This note does not update that file. It clarifies only that decision has now crossed the boundary from underhoused concern into schema-admissible concern.

With `implementation/STATE_MACHINE_OVERVIEW.md`, it preserves that decision is already a distinct standing-state role. This note depends on that fact rather than inventing a new decision theory.

With `implementation/GOVERNANCE_ACTION_OVERVIEW.md`, it preserves that governance and decision are adjacent but non-identical. Governance may perform or authorize acts around decision, but schema admission for decision does not promote governance-collapse.

With `implementation/CURRENT_IMPLEMENTATION_SURFACES.md`, it preserves that implementation still has open schema-admission questions for newer additive surfaces. This note narrows one of those questions without claiming broader closure.

With `runtime/REGISTRY_CONTRACT.md`, it preserves that runtime preservation and schema admission are not identical questions. The registry preserves canonical records, but this note does not claim that decision is already runtime-integrated.

With `accession/ADMISSION_DECISION.md`, it preserves that explicit bounded decision surfaces already stand in the body. This note treats that as evidence of decision reality, not as schema by implication.

With `vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md`, it preserves that a derivative branch can still produce a real bounded decision surface without thereby settling final implementation record shape.

With `v1/34_POST_API_BACKED_POSTURE_BRIDGE.md`, it preserves that decision and bridge carry are already visibly distinct in the body. This note depends on that distinction and does not erase it.

With `continuity/FIRST_PASS_CURRENTNESS_RECORD.md`, it preserves that currentness locates what governs and does not become the governed surface itself. This note therefore keeps decision and currentness distinct even where later currentness may point toward a decision surface as current for one scope.

## 9. What Remains Open

Even after this admission boundary is clarified, the following remain open.

- the final schema shape
- the family-versus-extension question
- runtime or registry integration
- the final canonical versus derivative rank
- the relation between decision and currentness records
- the relation between decision and posture vocabulary
- future mechanism or checker work

These remain open on purpose. The present task is to clarify whether decision may lawfully become schema, not to force the rest of the system closed.

## 10. Closing Boundary Statement

This file defines the schema-admission boundary for decision record only.

It exists to clarify whether and where decision may lawfully become schema, without pretending the rest of the system is solved.

Later additive work may separately decide whether the schema should actually be created.
