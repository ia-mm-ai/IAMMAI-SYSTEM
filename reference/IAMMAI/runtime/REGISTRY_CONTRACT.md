# IAMMAI Registry Contract

## 1. Purpose

This file defines the first runtime contract for the Registry / Store inside the IAMMAI body.

Its job is to explain what the Registry / Store is responsible for, what it may receive, what it may preserve, what it depends on, what it must preserve, what it must never absorb, and how it relates to the other runtime parts without collapsing their roles.

It does not yet try to define:
- code
- database design
- storage vendor selection
- infrastructure topology
- service design
- detailed internal storage logic

It is a bounded runtime-contract document.

## 2. First Principle

The Registry / Store preserves canonical records.

It serves the constitutional core.  
It preserves reconstructable history.  
It does not become semantic source by itself.  
It does not become interpretation engine.  
It does not replace witness, validation, governance, state engine, or interface.

In runtime terms, the Registry / Store is the authoritative preservation surface through which canonical records become durable without storage convenience redefining what they mean.

## 3. Why a Registry Contract Is Needed

Preservation needs a bounded runtime contract.

- If preservation is not contract-bounded, canonical records can disappear into generic storage, convenience caches, summary surfaces, or untyped logs.
- Canonical records must not disappear into generic storage because the body needs durable state, transition, witness, validation, governance, and lineage records rather than only present display state.
- Reconstructable history matters because IAMMAI distinguishes what stood, what changed, what was checked, what was witnessed, who acted, and how succession occurred.
- This contract protects against silent overwrite and derivative substitution by making clear that authoritative preservation is a distinct runtime role, not an accidental side effect of storage.

## 4. What the Registry / Store Preserves

At a high level, the Registry / Store may preserve:

- state records
- transition records
- governance action records
- witness artifacts
- validation artifacts
- contribution records where relevant
- lineage relations and references

The Registry preserves canonical records.

It does not interpret them into new meaning. It does not replace the constitutional source of truth. It preserves the typed runtime records through which canonical history remains reconstructable.

## 5. Registry Inputs

At a high level, the Registry / Store may receive:

- state outputs from the State Engine
- transition outputs from the State Engine
- validation artifacts from the Validator
- witness artifacts from the Witness Emitter
- governance action records from the Governor
- bounded contribution or lineage relations where relevant

These are contract-bounded runtime inputs to preservation. They are not blank permission for the registry to reinterpret or collapse what it receives.

## 6. Registry Outputs

At a high level, the Registry / Store may emit or produce:

- preserved canonical records
- retrievable references
- reconstructable historical sequence
- canonical read surfaces for runtime consumers
- bounded outputs that derivative surfaces may later consume

Registry outputs are not witness artifacts.  
Registry outputs are not governance acts.  
Registry outputs are not validations.  
Registry outputs are not derived analytics by default.

They are preserved canonical records and related retrieval surfaces through which later runtime components or derivative consumers may access authoritative history.

## 7. Dependencies and Relations

### 7.1 State Engine

The State Engine may produce canonical state and transition outputs that the Registry preserves, but the Registry is not the State Engine. The State Engine applies lawful state handling; the Registry preserves its resulting records.

### 7.2 Validator

The Validator may produce validation artifacts that the Registry preserves, but the Registry is not validation. It preserves typed checking output; it does not perform the checking.

### 7.3 Witness Emitter

The Witness Emitter may produce witness artifacts that the Registry preserves, but the Registry is not witness. It preserves bounded trace; it does not become the witnessing act.

### 7.4 Governor

The Governor may produce governance action records that the Registry preserves, but the Registry is not governance. It preserves attributable force records; it does not become the force-bearing actor.

### 7.5 Interface Gateway

The Interface Gateway may consume registry-backed truth, but interface is not the registry itself. Interface presents and routes; the Registry preserves authoritative records.

## 8. What the Registry / Store Must Preserve

At minimum, the Registry / Store must preserve:

- canonical records
- typed record families
- lineage recoverability
- predecessor or successor relation where relevant
- append-oriented preservation posture
- non-collapse between canonical and derivative surfaces
- enough structure for later reconstruction

This means, in practical runtime terms:

- state, transition, witness, validation, governance, contribution, and lineage records must remain typed apart
- predecessor and successor relation must remain recoverable where lawful succession applies
- preservation must resist silent in-place overwrite
- derivative surfaces must not be allowed to impersonate canonical history
- the record body must remain structured enough to reconstruct what stood, what changed, and how it was preserved

## 9. What the Registry / Store Must Not Absorb

The Registry / Store must not become:

- witness
- validator
- governor
- state engine
- interface logic
- analytics or interpretation engine

It must not silently reinterpret constitutional meaning.

The Registry / Store keeps preservation explicit and bounded. It does not decide what was witnessed, what conditions passed, what force was lawful, what state movement occurred, or what a display surface should show beyond the preserved records it serves.

## 10. Contract Boundaries in Motion

Records should enter preservation when a bounded runtime participant has produced a canonical record or a canonical preservation-worthy output.

Before registry preservation occurs, the relevant typed record, target relation, lineage relation where applicable, and any required bounded metadata must already be present in identifiable form.

Outside registry scope remain:

- condition checking as validation
- trace emission as witness
- lawful force as governance
- canonical state movement as state-engine handling
- interaction routing and display as interface

After preservation occurs, other runtime participants and derivative surfaces may depend on registry-backed references, retrieval, and authoritative historical sequence where their own roles require it.

## 11. Failure / Absence Posture

When preservation fails or does not occur, the Registry / Store must be understood in bounded terms.

- failure to preserve canonical record must not disappear silently
- missing preservation must remain visible where canonical recording is required
- registry failure is not interpretation failure; it is preservation failure
- derivative surfaces must not silently substitute for missing canonical preservation

If authoritative preservation does not occur, later display, export, summary, or cache behavior must not behave as though durable canonical history already exists.

## 12. Registry vs Derivative Surfaces

The Registry / Store preserves canonical records.

Websites, dashboards, exports, analytics, summaries, and convenience APIs are derivative unless explicitly typed otherwise within a bounded authoritative role.

Display must not replace canonical history.  
Cache must not silently become source of truth.

Derivative surfaces may read from, summarize, or route toward registry-backed truth, but they do not replace the preserved canonical records themselves.

## 13. Anti-Collapse Rules

A conforming Registry contract must not allow:

- canonical records to be silently overwritten in place
- derivative views to be treated as registry truth
- analytics to be treated as canonical history
- generic logs to replace typed canonical records
- lineage to be lost because storage convenience flattened references
- the registry to act as interpretation engine
- the registry to be treated as governance or witness by itself

## 14. What Remains Open

The following remain intentionally open for later runtime derivation:

- append-only enforcement mechanism
- replication or distribution strategy
- synchronous or asynchronous persistence behavior
- retention policy
- storage partitioning
- canonical replica strategy

These are runtime-design questions, not constitutional ambiguities.

## 15. Summary

This document defines the first runtime contract for the Registry / Store as the bounded runtime role that keeps canonical state, transition, governance, witness, validation, contribution, and lineage records durably preserved for reconstructable history.

Its purpose is to make clear how the Registry / Store acts within the IAMMAI body without allowing it to absorb witness, validation, governance, state-engine, or interface roles.

**One-Line Definition:** `REGISTRY_CONTRACT.md` defines the first bounded runtime contract of the IAMMAI Registry / Store as the keeper of authoritative preservation and reconstructable history in motion without becoming witness, validator, governor, state engine, interface, or interpretation engine.
