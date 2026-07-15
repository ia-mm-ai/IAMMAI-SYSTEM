# IAMMAI Runtime Components

## 0. Purpose

This document defines the minimum runtime component set required to make the constitutional core of IAMMAI operational as more than text.

It does not define:
- final infrastructure topology
- service decomposition strategy
- vendor choices
- programming language
- deployment stack
- product-specific implementation details

It defines the first component model of the lawful between.

The aim is to make clear:
- what components must exist
- what each component is responsible for
- what each component must not absorb
- and how the runtime body preserves the law without collapsing into product convenience

---

## 1. First Runtime Principle

No runtime component may silently absorb constitutional distinctions that belong elsewhere.

This means:
- a validator may not quietly become a governor
- a witness emitter may not quietly become semantic source
- an interface may not quietly become canonical state
- a registry may not quietly become interpretation
- a product surface may not quietly redefine protocol meaning

Each runtime component must do its own job and stop there.

---

## 2. Minimum Runtime Component Set

The minimum lawful runtime consists of:

1. **State Engine**
2. **Validator**
3. **Witness Emitter**
4. **Governor**
5. **Registry / Store**
6. **Interface Gateway**

These six are enough for the first body.

---

## 3. State Engine

### 3.1 Definition

The State Engine is the component that knows the constitutional phase grammar and enforces lawful state movement.

It is the runtime keeper of:
- canonical phase order
- preparation vs standing-state distinction
- HOLD orthogonality
- resolution family closure
- lineage-preserving transition logic

### 3.2 Core responsibilities

The State Engine must:
- know the canonical phase chain
- preserve preparation vs standing-state distinction
- preserve HOLD as orthogonal containment
- preserve Finalize / Invalidate / Evolve as the only lawful resolution family
- preserve predecessor / successor logic
- prevent silent transition collapse
- prevent in-place overwrite of standing state

### 3.3 What it must not do

The State Engine must not:
- invent semantic meaning beyond the constitutional core
- decide authority by itself
- act as witness by itself
- collapse into interface logic
- become product-specific orchestration
- rewrite the constitutional source

### 3.4 Runtime significance

If the constitutional protocol is the law, the State Engine is the first runtime organ that keeps the law from dissolving under live operation.

---

## 4. Validator

### 4.1 Definition

The Validator is the component that checks whether bounded protocol conditions are satisfied.

It is the checker of:
- admissibility
- threshold conditions
- transition legality
- typed state requirements
- other bounded protocol predicates

### 4.2 Core responsibilities

The Validator must:
- determine whether candidate material satisfies admissibility requirements
- determine whether threshold conditions are met
- determine whether a requested transition is constitutionally lawful
- determine whether a requested act matches bounded criteria
- produce explicit pass/fail style outcomes or equivalent bounded validation outputs

### 4.3 What it must not do

The Validator must not:
- become the governor by default
- invent semantic source
- create standing state by itself
- interpret narrative as protocol truth
- collapse into witness
- silently authorize action

### 4.4 Runtime significance

The Validator prevents the system from treating:
- available material as admissible
- admissible material as standing
- desired transition as lawful transition
without actual bounded checking.

---

## 5. Witness Emitter

### 5.1 Definition

The Witness Emitter is the component that emits machine-readable trace artifacts when observed contact, validation, or protocol-relevant state interaction occurs.

It preserves that something:
- was encountered
- was checked
- was registered
- or was observed in relation to protocol state

### 5.2 Core responsibilities

The Witness Emitter must:
- emit witness records
- emit validation traces
- emit transition witness artifacts where relevant
- preserve claims and non-claims of the witness act
- remain append-oriented
- preserve reference to matter, state, or interaction target

### 5.3 What it must not do

The Witness Emitter must not:
- become semantic source
- become governor
- declare standing by itself
- rewrite the event it preserves
- impersonate human judgment
- fabricate authority

### 5.4 Runtime significance

The Witness Emitter is one of the first runtime answers to the witness problem:
- not by becoming source,
- but by preserving contact in a form that can be reconstructed without silent disappearance.

---

## 6. Governor

### 6.1 Definition

The Governor is the component or bounded authority surface that performs or authorizes protocol-significant acts.

It is responsible for:
- lawful protocol force
- legitimacy-bounded action
- attributable execution of governance acts

### 6.2 Core responsibilities

The Governor must:
- authorize lawful protocol acts where authority is required
- preserve attributable action
- preserve legitimacy basis
- preserve matter-scoped authority
- preserve delegation traceability
- remain bounded to authorized act classes

### 6.3 What it must not do

The Governor must not:
- become semantic source by default
- rewrite witness trace
- collapse into validator
- silently exceed matter scope
- create meaning by prestige or access
- erase the distinction between authority and authorship

### 6.4 Runtime significance

The Governor is the runtime location of lawful force.

Without it, actions may still occur.
They simply would not be typed as lawfully governed actions.

---

## 7. Registry / Store

### 7.1 Definition

The Registry / Store is the persistence component that preserves protocol-relevant state, transition, lineage, witness, and governance records over time.

It is not just “storage.”
It is the keeper of reconstructable history.

### 7.2 Core responsibilities

The Registry / Store must preserve:
- state records
- transition records
- predecessor / successor references
- witness artifacts
- governance actions
- contribution records where relevant
- temporal order
- append-only preservation where constitutionally required

### 7.3 What it must not do

The Registry / Store must not:
- silently overwrite standing state
- erase predecessor relation
- collapse typed records into generic logs
- become interpretation engine
- mutate trace for convenience
- replace governance with storage events

### 7.4 Runtime significance

The Registry / Store is the runtime preservation surface through which lineage becomes durable rather than merely asserted.

---

## 8. Interface Gateway

### 8.1 Definition

The Interface Gateway is the bounded interaction surface through which human, machine, or system actors encounter the runtime body.

It may take forms such as:
- UI surfaces
- APIs
- operator consoles
- machine endpoints
- public-facing access surfaces

### 8.2 Core responsibilities

The Interface Gateway must:
- accept bounded input
- expose protocol-safe interaction
- present derivative state representations
- route interaction toward the correct runtime components
- remain subordinate to the canonical runtime, governance, and registry layers

### 8.3 What it must not do

The Interface Gateway must not:
- define canonical state on its own
- silently reinterpret protocol meaning
- absorb governance by convenience
- replace runtime validation
- replace registry truth with display state
- collapse presentation into authority

### 8.4 Runtime significance

The Interface Gateway is where contact occurs,
but it must remain only the surface of contact, not the constitutional center of the system.

---

## 9. Component Separation Rules

The minimum runtime depends on the following separations staying intact:

- State Engine ≠ Validator
- Validator ≠ Governor
- Witness Emitter ≠ Governor
- Witness Emitter ≠ semantic source
- Registry / Store ≠ interpretation engine
- Interface Gateway ≠ canonical state
- Interface Gateway ≠ authority
- Registry / Store ≠ product display

These separations are not implementation niceties.
They are constitutional protections in runtime form.

---

## 10. Component Interaction Model

The minimum lawful interaction pattern is:

### 10.1 Input enters through Interface Gateway
An actor or system requests interaction.

### 10.2 Validator checks bounded conditions
The request is checked for admissibility, legality, or threshold alignment.

### 10.3 Witness Emitter preserves contact
The interaction, validation event, or observed state relation may produce trace.

### 10.4 Governor performs or authorizes protocol-significant action
If the request requires protocol force, a lawful governance act may occur.

### 10.5 State Engine performs lawful state handling
The runtime updates or preserves protocol state within constitutional bounds.

### 10.6 Registry / Store preserves the resulting trace and state relation
The relevant records, transitions, and lineage references are preserved.

This does not fix all runtime details.
It defines the lawful order of role interaction.

---

## 11. Authoritative vs Derivative Runtime Components

### 11.1 Authoritative runtime components
These components participate in canonical protocol force or its preservation:

- State Engine
- Governor
- Registry / Store
- Validator, where bounded constitutional checking is required

### 11.2 Derivative runtime component
This component is derivative in itself:

- Interface Gateway

### 11.3 Special case: Witness Emitter
Witness is neither simply authoritative nor merely decorative.

It is:
- constitutionally important
- preservation-oriented
- bounded in claim
- non-governing by default

It preserves contact without claiming final semantic force.

---

## 12. Open Component Questions

The following remain open in implementation detail:

- whether the State Engine and Validator are one service or separated
- whether Witness Emitter writes directly to Registry / Store or through another event path
- whether Governor is purely human, hybrid, or partially machine-assisted
- whether Interface Gateway splits into public/operator/machine surfaces
- how append-only preservation is technically enforced
- what witness record format becomes canonical
- what contribution record granularity is required in practice

These are implementation questions, not runtime-role ambiguities.

---

## 13. Summary

The minimum runtime body of IAMMAI consists of:

- a State Engine
- a Validator
- a Witness Emitter
- a Governor
- a Registry / Store
- an Interface Gateway

Each component must preserve its own role without absorbing constitutional distinctions that belong elsewhere.

A simple memory line:

**State Engine keeps the law in motion.  
Validator checks conditions.  
Witness preserves contact.  
Governor applies lawful force.  
Registry preserves history.  
Interface exposes the system without becoming it.**

---

## 14. One-Line Definition

**Runtime Components define the minimum operational organs required for the constitutional core of IAMMAI to function as a lawful implementation body.**
