# IAMMAI Transition Record Overview

## 1. Purpose

This file defines the first high-level transition record model of IAMMAI in implementation-facing form.

It translates the constitutional core and the current architecture and implementation documents into a bounded view of what a transition is, what a transition record preserves, and how lawful change remains reconstructable without semantic collapse.

It does not yet try to define:
- code
- a final schema
- a final event-sourcing design
- storage topology
- transport design
- database or infrastructure choices

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

Transitions must be preserved as typed protocol change.

Transition records must serve the constitutional core. They must not flatten lawful change into generic mutation, and they must preserve relation to state, matter, and lineage so the runtime can show not only what stands, but how it lawfully moved.

The constitutional core remains the semantic source of truth. Transition records preserve lawful movement; they do not redefine the meaning of the states they connect.

## 3. Why Transition Records Are Needed

State alone is insufficient.

- Current state can show what now stands, but it cannot by itself show how that state was reached, what lawful movement occurred, or whether successor relation was preserved.
- Lawful change must remain reconstructable because IAMMAI distinguishes preparation, standing state, containment, and typed resolution rather than treating all change as one generic update stream.
- Generic `updated` events are non-conformant because they hide whether the change was preparation progression, lawful standing-state movement, containment application, release, FINALIZE, INVALIDATE, or EVOLVE.
- Transition records protect against silent overwrite and ambiguous succession by preserving explicit movement and its relation to source state, target state, matter, and lineage.

Transition records therefore keep protocol change visible as typed change rather than letting it disappear into storage mutation or derivative display state.

## 4. What a Transition Is

In implementation terms, a transition is a lawful movement between protocol-relevant conditions or states.

A transition is:
- bounded by canonical order
- bounded by containment rules
- bounded by resolution rules
- distinct from raw activity or generic system change

Not every observed system event is a protocol transition. A protocol transition is a state-relevant movement that counts within the constitutional grammar of the implementation body.

## 5. What a Transition Record Preserves

At a high level, a transition record should preserve:

- transition id
- matter ref
- source state or condition ref
- target state or condition ref
- transition type
- acted_at or occurred_at
- optional related validation ref
- optional related governance action ref
- optional related witness ref
- optional predecessor or successor relation where relevant

This is a conceptual record shape, not a final schema.

The implementation point is that a transition record should preserve enough typed trace to reconstruct what moved, in what direction, on what matter, under what related checks or acts where applicable, and with what lineage relation where succession applies.

## 6. Transition Families

A first bounded family of transition types may include:

### 6.1 Preparation Progression Transitions

Preserve lawful movement through the Preparation Regime, including movement such as:
- signal to acceptance
- acceptance to scope
- scope to presence
- presence to threshold

These transitions narrow candidate material. They do not create standing state by default.

### 6.2 Threshold Eligibility Transition

Preserves movement into threshold-eligible condition.

This is still preparation-state movement. It marks eligibility for truth formation; it is not truth itself.

### 6.3 Truth Formation Transition

Preserves lawful movement from threshold eligibility into truth where the required checks, authority conditions, and containment state permit it.

This is the regime boundary at which standing state first appears.

### 6.4 Continuity Transition

Preserves lawful movement into continuity as lineage-bearing preservation of standing truth.

### 6.5 Decision Transition

Preserves lawful movement into decision as committed direction on the basis of preserved state.

### 6.6 Consequence Transition

Preserves lawful movement into consequence as applied effect following lawful decision.

Consequence remains downstream effect, not proof of upstream legitimacy.

### 6.7 Containment Application / Release Transition

Preserves application of HOLD and later release where containment applies.

These transitions affect permissibility, not state meaning, and must remain distinct from the canonical standing-state chain.

### 6.8 Resolution Transitions

Preserve typed resolution as:
- FINALIZE
- INVALIDATE
- EVOLVE

These transitions are a special bounded family. They must remain explicit and must not collapse into generic change markers.

## 7. Transition vs State

State is what stands.  
Transition is the lawful movement between states or conditions.

State records and transition records are related but not interchangeable.

- A state record preserves what currently stands in typed form.
- A transition record preserves how movement occurred between protocol-relevant conditions or states.
- State without transition loses reconstructable change.
- Transition without state loses what actually stands.

The runtime must preserve both.

## 8. Transition vs Resolution

Not every transition is a resolution.

Resolution transitions are a special typed family within the broader transition model.

- Preparation progression is transition, not resolution.
- Truth, continuity, decision, and consequence movement are transition, not necessarily resolution.
- FINALIZE, INVALIDATE, and EVOLVE are resolution transitions and must remain explicit.
- EVOLVE must preserve successor relation and must not collapse into generic change, in-place correction, or overwrite.

Resolution therefore remains a closed, typed transition family rather than a generic terminal status.

## 9. Transition and Containment

HOLD is orthogonal.

- HOLD is not a phase.
- HOLD is not a resolution outcome.
- HOLD affects permissibility, not state meaning.

Containment-related transitions must therefore remain distinguishable from standing-state transitions.

Applying HOLD does not create a new semantic phase. Releasing HOLD does not create truth, continuity, decision, consequence, or resolution by itself. Transition records must preserve this orthogonality rather than absorbing containment into the canonical semantic chain.

## 10. Transition and Lineage

Predecessor / successor relation matters because lawful succession must remain explicit.

- Where successor creation occurs, predecessor relation must remain recoverable.
- Where a prior state has been succeeded, successor relation must remain recoverable.
- Transition records support reconstructable history by preserving movement and its lineage relation together where relevant.
- Transition records help prevent silent overwrite by making lawful change visible as succession rather than replacement.

Lawful succession therefore depends on explicit relation, not timestamp ordering, naming similarity, or narrative reconstruction.

## 11. Transition and Runtime Components

### 11.1 State Engine

The State Engine determines whether requested state movement fits canonical order, regime distinction, containment rules, resolution family closure, and predecessor / successor logic.

### 11.2 Validator

The Validator checks admissibility, threshold conditions, transition legality, and other bounded predicates that may be required before a transition is treated as lawful.

### 11.3 Witness Emitter

The Witness Emitter may preserve transition-related trace as witness artifact without becoming the transition's semantic source, governance basis, or lawful force.

### 11.4 Governor

The Governor performs or authorizes protocol-significant transition acts where bounded authority is required, including HOLD, release, FINALIZE, INVALIDATE, and EVOLVE.

### 11.5 Registry / Store

The Registry / Store preserves transition records, related state references, lineage references, and temporal order so lawful change remains durable and reconstructable over time.

### 11.6 Interface Gateway

The Interface Gateway accepts bounded transition requests and presents derivative transition views, but it must not become the canonical authority over transition meaning or legality.

## 12. Anti-Collapse Rules

A conforming implementation must not allow:

- transition to flatten into generic update
- resolution to be hidden inside untyped mutation
- consequence to be treated as proof of upstream legitimacy
- EVOLVE to be treated as overwrite
- containment to be treated as a phase
- transition records to detach from matter or state context
- successor relation to disappear from EVOLVE handling
- lineage to be inferred only by guesswork
- derivative display state to replace canonical transition trace

## 13. Open Questions

The following remain open in technical derivation:

- the final transition record envelope
- how source and target references are represented across preparation-state and standing-state transitions
- how containment application and release are represented in concrete runtime artifacts
- how transition records attach to related witness, validation, and governance records
- whether some transition families need distinct reference conventions

These are implementation questions, not constitutional ambiguities.

## 14. Summary

This document defines the first implementation-facing transition record model of IAMMAI as a bounded record model for typed lawful change.

Its purpose is to keep preparation progression, standing-state movement, containment application, resolution, and succession reconstructable without collapsing transition into generic mutation.

**One-Line Definition:** `TRANSITION_RECORD_OVERVIEW.md` defines the first high-level implementation view of IAMMAI transition records as typed, reconstructable records of lawful protocol change across state, containment, resolution, and lineage.
