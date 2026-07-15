# IAMMAI State and Data Roles

## 0. Purpose

This document defines the minimum state and data role model required for the IAMMAI implementation body.

It exists to answer a simple question:

**What kinds of things must the runtime be able to hold without collapsing them into one generic data blob?**

The aim is not to finalize a database schema.
The aim is to preserve constitutional distinctions in operational form.

This document therefore defines:
- the main state roles
- the main record roles
- the difference between state, transition, witness, governance, and contribution data
- and the minimum typed categories the runtime must preserve

---

## 1. First Principle

Not all data is the same kind of thing.

A conforming IAMMAI implementation must preserve the difference between:

- candidate material
- standing state
- containment state
- resolution state
- governance records
- contribution records
- witness / validation records
- lineage references

If these collapse into one generic status field or one undifferentiated event log, the implementation may still function operationally but will no longer preserve the constitutional grammar.

---

## 2. Why state and data roles matter

Without typed state and data roles, systems drift in predictable ways:

- candidate material is mistaken for standing state
- transitions disappear into generic “updated” events
- lineage becomes irrecoverable
- governance looks like anonymous mutation
- contribution collapses into authorship blur
- witness becomes indistinguishable from authority
- derived display state replaces canonical state

So the purpose of this document is not database perfection.
It is constitutional non-collapse.

---

## 3. Core Distinction: State vs Record vs Reference

The architecture should preserve three different kinds of things:

### 3.1 State
What currently stands in protocol-relevant form.

Examples:
- truth
- continuity
- decision
- consequence
- held state
- finalized state
- invalidated state
- evolved state

### 3.2 Record
A preserved trace of something that occurred.

Examples:
- governance action record
- contribution record
- witness artifact
- validation result
- resolution record

### 3.3 Reference
A typed relation between entities, states, or records.

Examples:
- matter reference
- predecessor reference
- successor reference
- target state reference
- target transition reference
- artifact reference

These are different roles and must remain typed accordingly.

---

## 4. Candidate Material Roles

Candidate material belongs to the Preparation Regime.

It is not standing state.

### 4.1 Signal
Candidate material made available to the system for possible handling.

### 4.2 Accepted material
Signal that has been admitted for structured protocol handling.

### 4.3 Scoped material
Accepted material bound to the matter within which it may lawfully count.

### 4.4 Present material
Scoped material that has become relevant occurrence within the matter.

### 4.5 Threshold-eligible material
Material whose preparatory conditions are sufficient for truth formation to become eligible.

### 4.6 Rule
Candidate material must not silently become standing state by storage convention.

A system must be able to distinguish:
- candidate
- admissible candidate
- in-scope candidate
- present candidate
- threshold-eligible candidate

from:
- standing truth
- continuity
- decision
- consequence

---

## 5. Standing State Roles

Standing state belongs to the Standing-State Regime.

These are not interchangeable.

### 5.1 Truth state
Standing claim formation.

### 5.2 Continuity state
Lineage-bearing preservation of standing truth.

### 5.3 Decision state
Committed direction based on preserved state.

### 5.4 Consequence state
Applied effect following lawful decision.

### 5.5 Rule
A conforming implementation must preserve enough state typing that:
- truth is not mistaken for decision
- decision is not mistaken for consequence
- continuity is not reduced to raw duration or storage

---

## 6. Containment Roles

Containment is orthogonal to the canonical semantic chain.

### 6.1 Held state
A state in which an otherwise eligible irreversible transition is prevented from proceeding.

### 6.2 Released state
A state in which prior containment has been lifted and permissibility may be restored.

### 6.3 Rule
Containment must not be stored as if it were a canonical phase.
It is a separate state role.

A conforming system must be able to express:
- what is held
- what was released
- and when containment applied

without turning HOLD into standing state.

---

## 7. Resolution Roles

Resolution must be preserved in typed form.

### 7.1 Finalized state / record
Closure in current form.

### 7.2 Invalidated state / record
Removal of standing without erasure of trace.

### 7.3 Evolved state / record
Successor creation in explicit relation to prior standing state.

### 7.4 Rule
A conforming implementation must not reduce all resolution to:
- “closed”
- “updated”
- “changed”
- or generic mutation

It must preserve typed resolution.

---

## 8. Governance Data Roles

Governance data records lawful action.

### 8.1 Governance action record
Preserves:
- governance action id
- authority class
- actor reference
- legitimacy basis
- matter reference
- action type
- time of action

### 8.2 Delegation relation
Preserves:
- delegating source
- delegated actor
- authority scope
- act relation

### 8.3 Rule
Governance records must make it possible to reconstruct:
- who acted
- under what authority
- on what matter
- under what legitimacy basis

Opaque force is non-conformant.

---

## 9. Contribution Data Roles

Contribution records preserve semantic participation in material.

### 9.1 Contribution role record
A contribution record should preserve at least:
- contribution role id
- matter reference
- role type
- actor reference where applicable
- related artifact reference where applicable
- related governance action reference where applicable
- recorded_at

### 9.2 Role types
At minimum:
- ORIGIN
- ELICITATION
- FORMALIZATION
- AUTHORIZATION
- RENDERING
- TRANSMISSION

### 9.3 Rule
Contribution data must not silently collapse into one undifferentiated authorship field where materially distinct roles exist.

---

## 10. Witness / Validation Data Roles

These records preserve contact and condition checks.

### 10.1 Witness artifact
A witness artifact should preserve:
- witness id
- witness type
- target reference
- claims
- non-claims
- observed_at

### 10.2 Validation artifact
A validation artifact should preserve:
- validation id
- target reference
- condition set or rule reference
- outcome
- checked_at

### 10.3 Rule
Witness and validation data must remain typed separately from:
- governance
- semantic source
- standing state

Witness preserves contact.  
Validation preserves condition checking.

They are not interchangeable.

---

## 11. Lineage Data Roles

Lineage is a relation role, not just a note.

### 11.1 Predecessor reference
Identifies what prior state a current state explicitly succeeds or depends on.

### 11.2 Successor reference
Identifies what later state succeeded the prior one.

### 11.3 Transition reference
Identifies the lawful movement between two protocol-relevant states.

### 11.4 Rule
Where lawful succession occurs, the implementation must preserve explicit predecessor / successor relation.

A conforming implementation must not require a human to guess lineage from timestamps or naming alone.

---

## 12. Matter and Target References

References must remain typed.

### 12.1 Matter reference
What bounded matter the state, act, or record applies to.

### 12.2 State reference
What protocol state is being referred to.

### 12.3 Transition reference
What protocol transition is being referred to.

### 12.4 Artifact reference
What artifact or content unit is being referred to.

### 12.5 Rule
A conforming implementation must preserve the difference between:
- matter
- state
- transition
- artifact
- actor

Reference collapse is a major implementation failure mode.

---

## 13. Canonical Data-Role Families

A first clean family map is:

### 13.1 Candidate family
- signal
- accepted
- scoped
- present
- threshold-eligible

### 13.2 Standing family
- truth
- continuity
- decision
- consequence

### 13.3 Containment family
- held
- released

### 13.4 Resolution family
- finalized
- invalidated
- evolved

### 13.5 Governance family
- governance action
- legitimacy basis
- delegation relation

### 13.6 Contribution family
- origin
- elicitation
- formalization
- authorization
- rendering
- transmission

### 13.7 Witness / validation family
- witness artifact
- validation artifact

### 13.8 Lineage family
- predecessor reference
- successor reference
- transition reference

This family map is enough for v0.

---

## 14. Anti-Collapse Requirements

A conforming implementation must not allow:

### 14.1 Candidate / standing collapse
Preparation-state data stored as if it were standing state

### 14.2 Resolution flattening
Finalize / Invalidate / Evolve stored as generic state mutation

### 14.3 Governance opacity
Action records without attributable authority

### 14.4 Contribution collapse
All semantic roles stored as “author”

### 14.5 Witness-governance collapse
Witness record treated as governance action

### 14.6 Lineage disappearance
Successor relation recoverable only through guesswork

### 14.7 Reference flattening
Matter, state, transition, and artifact references treated as the same generic link

---

## 15. Practical Audit Questions

A serious implementation review should be able to ask:

- Is this candidate material or standing state?
- If standing state, what kind?
- If change occurred, was it Finalize, Invalidate, or Evolve?
- If a record exists, is it witness, validation, governance, contribution, or lineage?
- Can predecessor and successor relation be recovered explicitly?
- Can matter, state, transition, and artifact references be distinguished?
- Can governance be reconstructed without reading narrative explanation?
- Can contribution be reconstructed without collapsing into authorship blur?

If the answer is no, the data model is too collapsed.

---

## 16. Open Questions

The following remain open in implementation detail:

- whether state roles map to separate stores or one typed store
- how much normalization is required between governance and contribution records
- whether witness artifacts need hash/signature fields by default
- how much denormalized display state is acceptable
- whether some derivative caches can be treated as canonical replicas under strict conditions

These are implementation questions, not constitutional ambiguities.

---

## 17. Summary

IAMMAI requires a typed state and data role model because not all protocol-relevant information is the same kind of thing.

A conforming body must preserve the difference between:
- candidate material
- standing state
- containment
- resolution
- governance
- contribution
- witness / validation
- and lineage

Without that distinction, the implementation becomes too collapsed to preserve the protocol.

---

## 18. One-Line Definition

**State and Data Roles defines the minimum typed categories required for IAMMAI to preserve constitutional distinctions in operational form.**
