# IAMMAI Reference Architecture v0

## 0. Purpose

This document defines the first reference architecture for the implementation body that can carry the published constitutional core of IAMMAI.

It does not define:
- a final runtime
- a specific product
- a commercial implementation
- a private deployment
- a complete distributed topology

It defines the minimum lawful body required for the constitutional core to exist as more than text.

---

## 1. First Principle

The body serves the law.

The constitutional core remains the semantic source of truth.

Implementation may:
- execute
- validate
- witness
- preserve
- expose

It may not:
- silently redefine protocol meaning
- collapse constitutional distinctions
- replace the law with product convenience

---

## 2. Scope

This reference architecture covers:

- runtime component roles
- authoritative vs derivative surfaces
- witness / validator / governor separation
- state and data roles
- persistence and lineage needs
- orthogonality rules
- implementation-neutral architectural boundaries

This reference architecture does not yet cover:

- final infrastructure stack
- service decomposition
- storage vendor choice
- UI/UX specifics
- performance/scaling strategy
- private implementation privilege
- full dynamic systems theory
- complete witness ecology

---

## 3. Architectural Layers of the Body

### 3.1 Constitutional Source Layer
Contains the normative constitutional core.

Includes:
- human constitutional protocol
- machine-readable constitutional twin
- protocol identity
- conformance artifacts

Job:
- define constitutional meaning
- preserve invariants
- remain the semantic source of truth

---

### 3.2 Canonical Runtime Layer
The first operational core of the lawful between.

Includes:
- state model
- transition model
- admissibility logic
- containment logic
- resolution logic
- lineage logic
- phase distinctions
- role boundaries

Job:
- make constitutional distinctions executable
- preserve lawful order
- prevent silent collapse in live operation

---

### 3.3 Witness / Validation Layer
The layer that preserves contact and checks conditions.

Includes:
- witness artifacts
- validation events
- attestation traces
- observed interaction records
- transition witness records
- validation outputs

Job:
- preserve contact
- validate bounded conditions
- emit trace
- separate witnessing from authority

---

### 3.4 Governance / Authority Layer
The layer that performs or authorizes protocol-significant acts.

Includes:
- authority classes
- legitimacy basis
- delegation chains
- governance actions
- human or bounded authority surfaces

Job:
- determine who may act
- determine on what matter
- determine under what lawful basis
- keep action attributable

---

### 3.5 Persistence / Registry Layer
The layer that preserves state and trace over time.

Includes:
- append-only records
- state registry
- transition registry
- witness records
- governance records
- predecessor/successor references

Job:
- preserve continuity
- allow reconstruction
- prevent silent disappearance
- support lineage across change

---

### 3.6 Product / Interface Layer
The layer where human, machine, and system actors encounter the implementation.

Includes:
- public surfaces
- operator surfaces
- machine endpoints
- administrative interfaces
- APIs
- display surfaces

Job:
- present canonical state
- receive bounded input
- expose protocol-safe interaction
- remain subordinate to deeper layers

---

## 4. Minimum Component Set

### 4.1 Protocol Core Artifacts
- constitutional protocol document
- `canon.json`
- `protocol-identity.json`
- `conformance_tests.md`

### 4.2 State Engine
Knows:
- canonical phase order
- preparation vs standing-state distinction
- HOLD
- Finalize / Invalidate / Evolve
- predecessor / successor rules
- lawful state transitions

### 4.3 Validator
Checks:
- admissibility
- threshold conditions
- transition legality
- contribution-role consistency where required

### 4.4 Witness Emitter
Emits:
- witness records
- transition traces
- validation traces
- observed interaction artifacts

### 4.5 Governor
Can:
- authorize transitions
- perform protocol-significant acts
- keep legitimacy basis explicit
- preserve attributable force

### 4.6 Registry / Store
Preserves:
- states
- transitions
- lineage
- witness records
- governance actions
- contribution records

### 4.7 Interface Surfaces
Expose:
- public interaction
- operator interaction
- machine endpoints
- bounded protocol-safe access

---

## 5. Witness / Validator / Governor

### 5.1 Witness
Witness preserves contact.

Witness may:
- record
- attest to observed occurrence
- emit trace
- preserve that something was encountered

Witness may not:
- claim authorship
- claim semantic source
- claim final authority
- silently determine standing

### 5.2 Validator
Validator checks conditions.

Validator may:
- evaluate rules
- determine pass/fail within bounded scope
- confirm admissibility or legality of transition

Validator may not:
- become governor by default
- invent semantic truth
- collapse into witness

### 5.3 Governor
Governor exercises lawful force.

Governor may:
- authorize
- finalize
- invalidate
- evolve
- hold
- release

Governor must:
- remain attributable
- remain legitimacy-bounded
- remain matter-scoped

### 5.4 Memory line
**Witness preserves.  
Validator checks.  
Governor acts.**

---

## 6. Authoritative vs Derivative Surfaces

### 6.1 Authoritative Surfaces
These determine or preserve canonical protocol force.

Examples:
- constitutional source artifacts
- canonical runtime / state engine
- governance actions
- validated transition records
- append-only lineage-preserving registry

### 6.2 Derivative Surfaces
These display, consume, route, or interface with canonical state without defining it.

Examples:
- public websites
- dashboards
- UI surfaces
- exports
- analytics views
- notifications
- convenience APIs

### 6.3 Principle
**Display does not define state.  
Canonical state must be recoverable beneath display.**

---

## 7. State and Data Roles

### 7.1 Candidate Material
Pre-standing material moving through preparation:
- signal
- accepted
- scoped
- present
- threshold-eligible

### 7.2 Standing State
Protocol standing forms:
- truth
- continuity
- decision
- consequence

### 7.3 Containment State
- held
- released
- optional reason references

### 7.4 Resolution State
- finalized
- invalidated
- evolved

### 7.5 Governance Records
- authority class
- actor
- legitimacy basis
- matter
- delegation
- acted_at

### 7.6 Contribution Records
- origin
- elicitation
- formalization
- authorization
- rendering
- transmission

### 7.7 Witness / Validation Records
- witness type
- validation type
- observed_at
- claims
- non-claims
- target references
- optional signature / hash fields

### 7.8 Lineage References
- predecessor
- successor
- transition references

---

## 8. Orthogonality Rules

The implementation must preserve these separations:

- witness ≠ governance
- validator ≠ governor
- contribution ≠ authority
- display ≠ canonical state
- interface ≠ constitutional source
- persistence ≠ interpretation
- derivative analytics ≠ authoritative records

If these distinctions collapse, the implementation no longer preserves the law.

---

## 9. Lawful Between

The lawful between is not a single service or screen.

It is the implementation-grade zone where:
- human actors
- machine actors
- system interfaces
- canonical state
- witness
- validation
- governance
- lineage

can meet without collapsing constitutional distinctions.

In this reference architecture, the lawful between is composed primarily of:

- canonical runtime
- witness / validation
- governance
- persistence / registry

with interface surfaces exposed above them.

**The lawful between is the body that keeps contact, action, and state honest across the seam between human and machine.**

---

## 10. Neutrality Toward Private Implementations

This reference architecture is intentionally neutral with respect to private implementations.

No private product, company, or interface is granted:
- conceptual priority
- semantic privilege
- early-entry constitutional status

Products may implement or host parts of this architecture.
They do not pre-own it.

---

## 11. Open Questions

The following remain open in implementation detail:

- final storage model
- final distributed topology
- specific service decomposition
- witness artifact format
- validator engine design
- registry implementation
- authentication / identity strategies
- interface protocol details
- performance / scaling concerns
- witness ecology scope

These are implementation questions, not constitutional uncertainties.

---

## 12. Summary

Reference Architecture v0 defines the minimum lawful body required for the constitutional core of IAMMAI to exist as more than text.

It consists of:
- a constitutional source layer
- a canonical runtime layer
- a witness / validation layer
- a governance / authority layer
- a persistence / registry layer
- derivative interface surfaces

This is the minimum architectural body, not a complete implementation description.

---

## 13. One-Line Definition

**Reference Architecture v0 defines the minimum lawful body required for the constitutional core of IAMMAI to exist as more than text.**
