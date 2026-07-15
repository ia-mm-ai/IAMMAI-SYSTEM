# IAMMAI State Engine Contract

## 1. Purpose

This file defines the first runtime contract for the State Engine inside the IAMMAI body.

Its job is to explain what the State Engine is responsible for, what it may receive, what it may emit, what it depends on, what it must preserve, what it must never absorb, and how it relates to the other runtime parts without collapsing their roles.

It does not yet try to define:
- code
- an API specification
- service design
- infrastructure topology
- a final execution model
- detailed internal engine logic

It is a bounded runtime-contract document.

## 2. First Principle

The State Engine preserves canonical state movement.

It serves the constitutional core.  
It does not invent semantic meaning.  
It does not apply lawful force by itself.  
It does not replace validation, witness, governance, registry, or interface.

In runtime terms, the State Engine is the component that keeps canonical state handling lawful while remaining bounded to state movement rather than absorbing the rest of the body.

## 3. Why a State Engine Contract Is Needed

Runtime state movement needs a bounded contract.

- If state movement is not contract-bounded, it can collapse into generic mutation, convenience updates, or display-driven behavior.
- State transition must not be left to generic mutation because IAMMAI distinguishes preparation from standing state, containment from phase identity, and typed resolution from generic status.
- The State Engine is central but not sovereign because canonical state movement depends on it, while lawful checking, lawful force, trace preservation, and durable preservation remain elsewhere.
- This contract protects against silent collapse in motion by making clear what the State Engine governs and where its authority stops.

## 4. What the State Engine Governs

At a high level, the State Engine governs:

- canonical phase order
- preparation versus standing-state distinction
- lawful state movement
- containment-aware movement
- typed resolution effects
- lineage-preserving successor logic

It governs motion of canonical state.

It does not govern everything in the system. It does not decide governance legitimacy, validation outcome, witness meaning, or registry preservation policy by itself.

## 5. State Engine Inputs

At a high level, the State Engine may receive:

- validated state-relevant inputs
- governance-authorized actions where required
- typed transition instructions
- containment-related conditions
- predecessor or successor relations
- canonical references to state and matter

These are contract-bounded runtime inputs to lawful state handling. They are not blank permission to mutate state arbitrarily.

## 6. State Engine Outputs

At a high level, the State Engine may emit or produce:

- state movement
- state records
- transition references
- lineage-preserving relations
- bounded outputs for registry preservation
- outputs that may later be witnessed

State Engine outputs are not witness artifacts.  
State Engine outputs are not governance acts.  
State Engine outputs are not validation artifacts.

They are bounded results of canonical state handling that other runtime components may preserve, witness, or depend on within their own roles.

## 7. Dependencies and Relations

### 7.1 Validator

Validation may be required before certain lawful movement proceeds. The State Engine depends on bounded checks where admissibility, threshold, transition legality, or related predicates are required, but it does not become the Validator.

### 7.2 Witness Emitter

Witness may preserve state movement, transition occurrence, or related runtime contact without becoming the movement itself. The State Engine does not emit witness meaning by default.

### 7.3 Governor

Governance may be required before certain lawful movement proceeds, especially where hold, release, finalize, invalidate, evolve, or other protocol-significant force is involved. The State Engine depends on governance where lawful force is required, but it does not become the Governor.

### 7.4 Registry / Store

The Registry / Store preserves resulting canonical state, transition, lineage, and related records. The State Engine may hand off bounded outputs for preservation, but it does not become the registry.

### 7.5 Interface Gateway

The Interface Gateway may route requests or inputs toward the State Engine through the proper runtime path, but interface must not define canonical state movement by itself.

## 8. What the State Engine Must Preserve

At minimum, the State Engine must preserve:

- phase distinction
- lawful order
- typed movement
- containment orthogonality
- resolution closure
- lineage recoverability
- non-overwrite of standing state

This means, in practical runtime terms:

- preparation must remain distinct from standing state
- threshold must remain eligibility, not truth
- HOLD must remain orthogonal rather than becoming state identity
- FINALIZE, INVALIDATE, and EVOLVE must remain typed
- predecessor or successor relation must remain recoverable where lawful succession occurs
- standing state must not be silently rewritten in place

## 9. What the State Engine Must Not Absorb

The State Engine must not become:

- validator
- governor
- witness
- registry
- interface logic

It must not silently reinterpret constitutional meaning.

The State Engine keeps canonical state movement lawful. It does not decide what checks passed, what force was authorized, what contact was witnessed, what storage is durable, or what a user interface chooses to display.

## 10. Contract Boundaries in Motion

The State Engine may act when the required bounded inputs for lawful state movement are present.

Before it acts, whatever validation or governance prerequisites apply must already be satisfied in their own runtime roles.

Outside its scope remain:

- condition checking as validation
- lawful force as governance
- trace preservation as witness
- durable preservation as registry
- interaction routing and display as interface

After movement occurs, resulting state, transition, lineage, and related outputs must be handed off to the appropriate runtime participants for preservation, witnessing, or derivative exposure.

## 11. Failure / Refusal Posture

When lawful movement does not proceed, the State Engine must be understood in bounded terms.

- not all non-movement is failure
- containment may lawfully block movement
- absent prerequisites may lawfully prevent movement
- failed or blocked movement must not silently disappear into generic state mutation

Non-movement may therefore mean that a lawful boundary held, not that the runtime malfunctioned. What must not happen is silent fallback into convenience update behavior.

## 12. Anti-Collapse Rules

A conforming State Engine contract must not allow:

- preparation to silently become standing state
- HOLD to become a phase
- resolution to flatten into generic status
- state mutation without transition trace
- consequence to back-authorize upstream legitimacy
- convenience updates to replace canonical movement
- the State Engine to act without required bounded inputs

## 13. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact execution semantics
- synchronous or asynchronous ordering
- retry behavior
- batching behavior
- distributed coordination implications
- finer-grained internal engine logic

These are runtime-design questions, not constitutional ambiguities.

## 14. Summary

This document defines the first runtime contract for the State Engine as the bounded runtime role that keeps canonical state movement lawful across phase order, regime distinction, containment, typed resolution, and lineage-preserving change.

Its purpose is to make clear how the State Engine acts within the IAMMAI body without allowing it to absorb validation, governance, witness, registry, or interface roles.

**One-Line Definition:** `STATE_ENGINE_CONTRACT.md` defines the first bounded runtime contract of the IAMMAI State Engine as the lawful keeper of canonical state movement without becoming validator, governor, witness, registry, or interface.
