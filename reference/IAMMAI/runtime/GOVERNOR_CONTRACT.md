# IAMMAI Governor Contract

## 1. Purpose

This file defines the first runtime contract for the Governor inside the IAMMAI body.

Its job is to explain what the Governor is responsible for, what it may receive, what it may emit, what it depends on, what it must preserve, what it must never absorb, and how it relates to the other runtime parts without collapsing their roles.

It does not yet try to define:
- code
- an API specification
- a final governance engine implementation
- service design
- infrastructure topology
- detailed internal governance logic

It is a bounded runtime-contract document.

## 2. First Principle

The Governor exercises lawful protocol force.

Governance must remain attributable.  
Governance must remain legitimacy-bounded.  
Governance must remain matter-scoped.  
Governance must not become semantic source.  
Governance must not replace validation, witness, state engine, registry, or interface.

In runtime terms, the Governor is the component through which lawful force becomes explicit rather than appearing as ambient mutation, convenience behavior, or anonymous power.

## 3. Why a Governor Contract Is Needed

Lawful force needs a bounded runtime contract.

- If governance is not contract-bounded, protocol-significant action can collapse into changed state, privileged access, or convenience-based mutation.
- Governance cannot be reduced to ambient mutation because IAMMAI requires lawful force to remain attributable, legitimacy-bounded, and matter-scoped.
- Governance order matters because validation may need to constrain governance before it acts, and state movement may depend on governance after it acts, while those roles remain distinct.
- This contract protects against anonymous force, scope bleed, and convenience-based action by keeping the force-bearing role explicit and bounded in motion.

## 4. What the Governor Governs

At a high level, the Governor governs typed acts such as:

- authorize
- deny
- hold
- release
- finalize
- invalidate
- evolve

These are lawful force-bearing acts.

Governance does not invent semantic source. It does not replace validation or witness. It does not decide constitutional meaning by prestige, access, or implementation convenience.

## 5. Governor Inputs

At a high level, the Governor may receive:

- authorization requests
- governance action requests
- validated preconditions where required
- matter references
- authority class
- legitimacy basis
- delegation relation where applicable
- target state or transition references where applicable

These are contract-bounded runtime inputs to lawful force. They are not blank permission to act outside authority, legitimacy, or matter scope.

## 6. Governor Outputs

At a high level, the Governor may emit or produce:

- governance action records
- typed action outputs
- matter-scoped force decisions
- hold or release outcomes
- resolution-related outputs where lawful
- outputs that may later be witnessed and preserved

Governance outputs are not validation artifacts.  
Governance outputs are not witness artifacts.  
Governance outputs do not imply semantic source or authorship.

They are bounded force-bearing results that later runtime components may preserve, witness, or depend on within their own roles.

## 7. Dependencies and Relations

### 7.1 State Engine

The State Engine may carry out lawful state movement after governance force is applied where such force is required, but the State Engine is not governance. Governance applies lawful force; the State Engine applies canonical state handling.

### 7.2 Validator

The Validator may provide bounded checks required before certain governance acts proceed, but validation is not governance. Passed validation does not itself authorize, deny, hold, release, finalize, invalidate, or evolve.

### 7.3 Witness Emitter

The Witness Emitter may preserve governance events as trace, but witness is not governance. Witness preserves that a governance event occurred; it does not provide the force of the act.

### 7.4 Registry / Store

The Registry / Store preserves governance trace and related records, but the registry is not governance itself. Preservation is not the same thing as acting.

### 7.5 Interface Gateway

The Interface Gateway may route requests toward governance where governance is required, but interface is not governance. Receipt, display, or routing do not count as lawful force.

## 8. What the Governor Must Preserve

At minimum, the Governor must preserve:

- attributable force
- legitimacy basis
- matter scope
- authority class
- typed action family
- visible relation to state or transition where relevant
- non-collapse between governance and semantic source

This means, in practical runtime terms:

- governance action must remain attributable
- legitimacy basis must remain explicit
- matter-bounded action must remain visible
- authority class must not collapse into actor identity alone
- authorize, deny, hold, release, finalize, invalidate, and evolve must remain typed
- governance force must not be mistaken for semantic authorship or source of meaning

## 9. What the Governor Must Not Absorb

The Governor must not become:

- validator
- witness
- semantic source
- state engine
- registry
- interface logic

It must not silently reinterpret constitutional meaning.

The Governor keeps lawful force explicit and bounded. It does not decide what checks passed, preserve occurrence as witness by itself, apply canonical state movement by itself, store canonical history by itself, or define how an interface presents the runtime body.

## 10. Contract Boundaries in Motion

Governance may act when lawful force is required and the bounded prerequisites for that act are present.

Before governance acts, whatever validation, authority, legitimacy basis, matter relation, target relation, and delegation context apply must already be present in bounded form.

Outside governance scope remain:

- condition checking as validation
- trace preservation as witness
- canonical state movement as state-engine handling
- durable preservation as registry
- interaction routing and display as interface

After governance action completes, the resulting governance record and any related outputs must be handed off to the appropriate runtime participants for state handling, witnessing, preservation, or derivative exposure where applicable.

## 11. Failure / Refusal Posture

When lawful force does not proceed, the Governor must be understood in bounded terms.

- denial must remain typed
- hold must remain distinct from denial and resolution
- refusal must remain attributable
- non-action where governance was invoked must not disappear into ambiguity
- governance refusal is not the same thing as validation failure by default

Non-progression may therefore mean denial, hold, blocked precondition, or another bounded governance outcome rather than absence of runtime meaning.

## 12. Delegation in Motion

Delegation may extend lawful action without erasing attribution.

- delegated flow must preserve source relation
- delegated force must remain bounded
- delegation must not create anonymous governance

In runtime terms, that means delegated action still requires attributable actor relation, source relation where applicable, legitimacy basis, matter scope, and typed action trace.

## 13. Anti-Collapse Rules

A conforming Governor contract must not allow:

- governance to be treated as semantic source
- governance to be treated as authorship by default
- governance to act without legitimacy basis
- governance to act outside matter scope
- governance to silently bypass required validation
- HOLD to be treated as a phase
- resolution to flatten into generic update
- anonymous force to pretend to be governance

## 14. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact synchronous or asynchronous behavior
- escalation paths
- multi-governor coordination
- retry and timeout behavior
- exact delegation mechanics across distributed runtime surfaces

These are runtime-design questions, not constitutional ambiguities.

## 15. Summary

This document defines the first runtime contract for the Governor as the bounded runtime role that keeps authorization, denial, hold, release, finalize, invalidate, and evolve explicit as attributable, legitimacy-bounded, matter-scoped lawful force.

Its purpose is to make clear how the Governor acts within the IAMMAI body without allowing it to absorb validation, witness, state-engine, registry, or interface roles.

**One-Line Definition:** `GOVERNOR_CONTRACT.md` defines the first bounded runtime contract of the IAMMAI Governor as the keeper of typed lawful force in motion without becoming validator, witness, state engine, registry, interface, or semantic source.
