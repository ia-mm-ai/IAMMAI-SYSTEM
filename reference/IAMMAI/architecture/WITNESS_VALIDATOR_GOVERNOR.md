# IAMMAI Witness / Validator / Governor

## 0. Purpose

This document defines the distinction between three runtime-critical roles in the IAMMAI implementation body:

- **Witness**
- **Validator**
- **Governor**

These roles are often collapsed in ordinary systems.
IAMMAI requires that they remain distinct.

This document exists to prevent:
- witness becoming authority,
- validation becoming governance,
- governance becoming semantic source,
- and runtime force being exercised without typed role separation.

---

## 1. First Principle

Witness, validation, and governance are not interchangeable.

A system that collapses them may still function operationally, but it will not preserve the constitutional integrity of IAMMAI.

A simple memory line:

**Witness preserves.  
Validator checks.  
Governor acts.**

---

## 2. Why this distinction matters

In many systems, the following collapse happens:

- the thing that observes also decides
- the thing that checks also authorizes
- the thing that records also becomes source
- the thing that acts also claims truth

That may be efficient in low-stakes systems.
It is not acceptable in a constitutional architecture designed to preserve:
- lawful standing
- attributable action
- bounded authority
- lineage
- and anti-collapse distinctions

IAMMAI therefore requires a typed separation of these roles.

---

## 3. Witness

### 3.1 Definition

Witness is the runtime role that preserves contact.

Witness may record that:
- something was encountered
- something was observed
- something was checked
- something was registered
- something occurred in relation to protocol state

Witness is a trace-preserving role.

### 3.2 Core job

Witness answers:

**What contact, occurrence, or observed relation should be preserved as trace?**

Witness protects against:
- disappearance
- unrecorded contact
- loss of relation to what occurred
- subsequent flattening by absence of trace

### 3.3 What witness may do

Witness may:
- emit witness artifacts
- preserve observed interaction
- preserve observed transition relation
- preserve bounded claims about contact
- preserve timing and target references
- preserve non-claims alongside claims

### 3.4 What witness must not do

Witness must not:
- claim semantic source by default
- create standing state by itself
- authorize action by itself
- finalize by itself
- replace governance
- replace validation
- rewrite what it preserves

### 3.5 Witness claims and non-claims

A witness artifact should make clear:

#### Claims
- contact occurred
- observation occurred
- trace was emitted
- bounded registration happened

#### Non-claims
- not authorship
- not semantic source
- not final authority
- not automatic truth creation
- not governance force

### 3.6 Witness significance

Witness is what allows the system to say:

**this did not simply vanish.**

That does not make witness the source of truth.
It makes witness the lawful carrier of preserved contact.

---

## 4. Validator

### 4.1 Definition

Validator is the runtime role that checks whether bounded protocol conditions are satisfied.

Validator does not preserve contact for its own sake.
Validator determines whether:
- admissibility holds
- threshold holds
- transition legality holds
- a condition passes or fails within defined rules

### 4.2 Core job

Validator answers:

**Do the defined conditions hold?**

This is a checking role, not a governing role.

### 4.3 What validator may do

Validator may:
- perform admissibility checks
- perform threshold checks
- perform transition legality checks
- emit bounded pass/fail outcomes
- emit validation traces
- reference the conditions it evaluated

### 4.4 What validator must not do

Validator must not:
- become governor by default
- create semantic source
- rewrite protocol meaning
- finalize or invalidate by itself unless explicitly granted governance authority
- replace witness
- claim authorship of what it evaluates

### 4.5 Validation output

A validation output should preserve:
- target matter / state / transition
- condition set used
- outcome
- time of check
- optional reason codes / references
- separation from governance action

### 4.6 Validator significance

Validator protects against:
- availability being mistaken for admissibility
- desire being mistaken for lawful transition
- “it seems fine” replacing bounded checks

Validator is the runtime defender of:
**conditions before force.**

---

## 5. Governor

### 5.1 Definition

Governor is the runtime role that exercises lawful protocol force.

Governor determines or performs:
- authorization
- HOLD
- release
- Finalize
- Invalidate
- Evolve
- and other protocol-significant acts that require bounded authority

### 5.2 Core job

Governor answers:

**What now lawfully stands as action?**

This is the force-bearing role.

### 5.3 What governor may do

Governor may:
- authorize acts
- deny acts
- hold transitions
- release held transitions
- finalize
- invalidate
- evolve
- preserve legitimacy basis for action
- preserve attributable force

### 5.4 What governor must not do

Governor must not:
- claim semantic source by default
- fabricate witness
- bypass validation where bounded checks are required
- silently exceed matter scope
- erase delegation chains
- rewrite constitutional distinctions

### 5.5 Governance basis

A governor action should preserve:
- actor / authority node
- authority class
- legitimacy basis
- matter relation
- action performed
- time of action
- delegation relation if applicable

### 5.6 Governor significance

Governor protects against:
- anonymous force
- convenience-based mutation
- untyped authority
- action without attributable legitimacy

Governor is the runtime answer to:
**who may lawfully make it stand?**

---

## 6. Clean Role Distinctions

### 6.1 Witness ≠ Validator
Witness preserves contact.  
Validator checks conditions.

A witness can exist without validation.  
A validation act may emit witness trace, but that does not make witness identical to validation.

### 6.2 Validator ≠ Governor
Validator determines whether conditions are satisfied.  
Governor determines whether lawful force is exercised.

A passed validation does not automatically imply authorization.

### 6.3 Witness ≠ Governor
Witness preserves that something was encountered or observed.  
Governor performs or authorizes lawful action.

Witness does not rule.
Governor does not become witness simply by acting.

### 6.4 Combined systems
One runtime system may host multiple roles.
That is acceptable only if the roles remain typed and non-collapsed internally.

Functional combination is not an excuse for semantic collapse.

---

## 7. Typical Lawful Sequence

A clean runtime sequence is:

1. **Interface receives interaction**
2. **Witness may preserve initial contact**
3. **Validator checks bounded conditions**
4. **Witness may preserve validation event**
5. **Governor authorizes or performs lawful act**
6. **Witness may preserve governance event**
7. **Registry preserves resulting state / transition / lineage**

This sequence can vary in timing or orchestration,
but the roles must remain distinguishable.

---

## 8. Anti-Collapse Rules

A conforming implementation must not allow:

### 8.1 Witness collapse
Witness record treated as semantic source or final authority

### 8.2 Validator collapse
Validation success treated as automatic authorization

### 8.3 Governance collapse
Governor act treated as proof of semantic origin

### 8.4 Role opacity
No way to tell whether a runtime output came from witness, validator, or governor

### 8.5 Trace laundering
Later governance rewriting witness or validation history for convenience

These are all non-conformant patterns.

---

## 9. Minimal Runtime Artifacts

The architecture should be capable of preserving at least:

### 9.1 Witness artifact
Contains:
- witness id
- target reference
- witness type
- claims
- non-claims
- observed_at

### 9.2 Validation artifact
Contains:
- validation id
- target reference
- condition set
- outcome
- checked_at

### 9.3 Governance artifact
Contains:
- governance action id
- authority class
- actor reference
- legitimacy basis reference
- matter reference
- action type
- acted_at

These may be expanded, but the roles should remain typed.

---

## 10. Open Questions

The following remain open in implementation detail:

- whether witness should be append-only by architecture or by infrastructure
- how validation results are expressed in final machine-readable forms
- whether governor is always human-bounded or sometimes machine-assisted
- what exact witness record schema becomes canonical
- how much witness ecology is needed across distributed surfaces

These are implementation questions, not role-identity ambiguities.

---

## 11. Summary

Witness, Validator, and Governor form one of the most important separation triads in the IAMMAI body.

- Witness preserves contact
- Validator checks bounded conditions
- Governor exercises lawful force

If these roles collapse, the body will drift even if the constitutional core remains perfectly written.

---

## 12. One-Line Definition

**Witness / Validator / Governor defines the typed separation between preserved contact, checked condition, and lawful action inside the IAMMAI runtime body.**
