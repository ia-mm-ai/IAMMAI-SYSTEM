# IAMMAI State Machine Overview

## 1. Purpose

This file defines the first high-level state-machine view of IAMMAI in implementation-facing form.

It translates the published constitutional core and the current architecture documents into a bounded view of:
- state regimes
- state meaning
- lawful transition
- orthogonal containment
- typed resolution
- lineage-preserving change

It does not yet try to define:
- code
- schemas
- APIs
- database design
- service topology
- a final runtime design

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

The state machine must serve the constitutional core.

The constitutional core remains the semantic source of truth. Runtime state handling may execute, validate, witness, preserve, and expose protocol state, but it must not silently redefine constitutional meaning or collapse distinctions for implementation convenience.

## 3. Canonical State Regimes

IAMMAI has two main state regimes:

### 3.1 Preparation Regime

The Preparation Regime contains:
- signal
- acceptance
- scope
- presence
- threshold

This regime handles candidate material on the way toward standing eligibility.

It is not standing state.

### 3.2 Standing-State Regime

The Standing-State Regime contains:
- truth
- continuity
- decision
- consequence

This regime holds what stands in protocol-relevant form.

It is not a continuation of preparation by storage convention. It is a distinct regime with distinct state meaning.

### 3.3 Regime Rule

Preparation and standing state are non-collapsible.

Preparation must not silently become standing state through narrative, display, storage convention, or consequence. Threshold creates eligibility for truth formation; it does not itself create truth.

## 4. Preparation States

### 4.1 Signal

- Means: candidate material is available to the system for possible handling.
- Is not: admissibility, standing state, or truth.
- Enables: movement into acceptance.

### 4.2 Acceptance

- Means: signal has been admitted for structured protocol handling.
- Is not: truth, standing state, or lawful conclusion.
- Enables: movement into scope.

### 4.3 Scope

- Means: accepted material is bound to the matter within which it may lawfully count.
- Is not: presence, threshold satisfaction, or standing state.
- Enables: movement into presence.

### 4.4 Presence

- Means: scoped material has become relevant occurrence within the matter.
- Is not: threshold satisfaction or truth formation.
- Enables: movement into threshold evaluation.

### 4.5 Threshold

- Means: preparatory conditions are sufficient for truth formation to become eligible.
- Is not: truth, continuity, decision, or consequence.
- Enables: lawful transition into truth where the required checks, authority conditions, and containment state permit it.

## 5. Standing-State Roles

### 5.1 Truth

- Means: standing claim formation.
- Is not: threshold, continuity, decision, or consequence.
- Enables: standing preservation and later movement into continuity.

### 5.2 Continuity

- Means: lineage-bearing preservation of standing truth.
- Is not: mere storage duration, surface similarity, or decision.
- Enables: traceable standing preservation and later movement into decision.

### 5.3 Decision

- Means: committed direction on the basis of preserved state.
- Is not: truth itself or applied effect.
- Enables: lawful consequence and typed resolution.

### 5.4 Consequence

- Means: applied effect of lawful decision.
- Is not: proof that upstream truth, authority, or transition validity was lawful.
- Enables: downstream application and trace preservation, but not retroactive authorization of earlier state.

## 6. Orthogonal Containment

HOLD is orthogonal to the canonical semantic chain.

- HOLD is not a phase.
- HOLD is not a resolution outcome.
- HOLD affects permissibility, not state meaning.
- HOLD prevents an otherwise eligible irreversible transition from proceeding.

Release lifts prior containment and restores permissibility only.

Release does not create truth, standing state, or resolution by itself.

## 7. Resolution Layer

Resolution is typed and closed.

The only lawful resolution family is:
- FINALIZE
- INVALIDATE
- EVOLVE

No hidden fourth outcome exists.

### 7.1 FINALIZE

- Means: lawful closure in current form.
- Does not: create a successor by default or erase history.

### 7.2 INVALIDATE

- Means: removal of standing without erasing trace.
- Does not: delete history or act as silent overwrite.

### 7.3 EVOLVE

- Means: lawful successor creation in explicit relation to prior standing state.
- Does: preserve predecessor / successor relation.
- Does not: permit in-place correction or orphan successor creation.

### 7.4 Resolution Rule

Resolution must remain typed.

A conforming implementation must not replace FINALIZE, INVALIDATE, or EVOLVE with generic status changes such as `updated`, `changed`, or `closed`.

## 8. State Transition Logic

Lawful transition means movement between typed states, or into typed resolution, in a way that preserves canonical order, regime distinction, validation, authority, trace, and lineage.

- The canonical phase order is fixed. Phases must not be silently skipped, reordered, or absorbed into one another.
- Preparation moves forward through signal, acceptance, scope, presence, and threshold. These steps narrow candidate material; they do not create standing state.
- Threshold creates eligibility for truth formation. Truth is the first standing state and must not appear without its required upstream basis.
- Standing-state movement preserves the difference between truth, continuity, decision, and consequence. Later standing states do not absorb earlier ones.
- Irreversible transitions in protocol kind must remain explicit, typed, and recoverable. HOLD exists because an otherwise eligible irreversible transition may need to be prevented from proceeding.
- Where successor creation occurs, predecessor / successor relation is part of the state-machine logic, not optional metadata.
- Correction enters through successor relation, not in-place replacement.
- Consequence cannot back-authorize upstream validity. Applied effect is not proof of lawful truth formation, lawful governance, or lawful transition.

## 9. State Machine Anti-Collapse Rules

A conforming implementation must not allow:

- preparation to silently become standing state
- threshold to be treated as truth
- truth to be treated as decision
- decision to be treated as consequence
- HOLD to be treated as a phase
- HOLD to be treated as a resolution outcome
- generic mutation to replace FINALIZE / INVALIDATE / EVOLVE
- silent overwrite of standing state
- successor creation without predecessor relation
- consequence to be treated as proof of upstream legitimacy or validity
- dark standing or dark consequence to appear without typed upstream basis

## 10. Relation to Runtime Components

### 10.1 State Engine

The State Engine keeps the canonical phase order, the preparation vs standing-state distinction, HOLD orthogonality, resolution family closure, and predecessor / successor logic.

### 10.2 Validator

The Validator checks admissibility, threshold conditions, typed state requirements, and transition legality before protocol-significant state movement is treated as lawful.

### 10.3 Witness Emitter

The Witness Emitter preserves traces of contact, validation, and transition without becoming semantic source, canonical state, or governance authority.

### 10.4 Governor

The Governor performs or authorizes HOLD, release, FINALIZE, INVALIDATE, EVOLVE, and other protocol-significant acts where bounded authority is required.

### 10.5 Registry / Store

The Registry / Store preserves state records, transition records, lineage, witness traces, governance traces, and temporal order. It must not silently overwrite standing state or erase predecessor relation.

### 10.6 Interface Gateway

The Interface Gateway accepts bounded input and presents derivative state representations. It routes interaction toward authoritative runtime components and must not become the canonical authority of state meaning.

## 11. Open Questions

The following remain open in technical derivation:

- the exact runtime representation of transition and resolution records
- whether the State Engine and Validator are separated or co-located
- how HOLD and release are represented in concrete runtime artifacts
- how witness and validation traces attach to state transitions
- how append-only lineage enforcement is technically realized

These are implementation questions, not constitutional ambiguities.

## 12. Summary

This document defines the first implementation-facing state-machine view of IAMMAI as a non-collapsed operational map of preparation, standing state, orthogonal containment, typed resolution, and lineage-preserving transition.

It is meant to guide implementation structure without fixing a final runtime design.

**One-Line Definition:** `STATE_MACHINE_OVERVIEW.md` defines the first high-level implementation view of IAMMAI as a lawful state machine that preserves regime distinction, orthogonal containment, typed resolution, and traceable lineage.
