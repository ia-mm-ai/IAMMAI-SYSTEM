# IAMMAI Witness Contract

## 1. Purpose

This file defines the first runtime contract for the Witness Emitter inside the IAMMAI body.

Its job is to explain what the Witness Emitter is responsible for, what it may receive, what it may emit, what it depends on, what it must preserve, what it must never absorb, and how it relates to the other runtime parts without collapsing their roles.

It does not yet try to define:
- code
- an API specification
- a full witness ecology design
- service design
- infrastructure topology
- detailed internal witness logic

It is a bounded runtime-contract document.

## 2. First Principle

The Witness Emitter preserves contact.

It emits bounded trace.  
It serves the constitutional core.  
It does not become semantic source.  
It does not become governance.  
It does not replace validation, state engine, registry, or interface.

In runtime terms, the Witness Emitter is the component that keeps contact, observation, registration, and related occurrence reconstructable without allowing preserved trace to inflate into authority, force, or semantic source.

## 3. Why a Witness Contract Is Needed

Witness needs a bounded runtime contract.

- If witness is not contract-bounded, contact can remain vapor or be replaced by generic logging, cosmetic status, or later narrative.
- Contact should not remain vapor because the live body needs reconstructable trace of relevant occurrence rather than memory or summary alone.
- Witness must remain typed in motion because not every preserved contact is the same kind of contact. Interaction, validation, governance, transition, and publication-related witness trace do different jobs.
- This contract protects against disappearance, flattening, and cosmetic substitution by keeping witness explicit as bounded trace rather than letting it dissolve into logs, analytics, or presentation surfaces.

## 4. What the Witness Emitter Governs

At a high level, the Witness Emitter governs:

- bounded preservation of contact
- bounded attestation of observed occurrence
- typed witness artifacts
- explicit claims and non-claims
- trace of relevant runtime events where witness is constitutionally important

It governs trace preservation.

It does not govern lawful force or semantic source. It does not decide that preserved contact automatically becomes truth, governance authority, or standing state.

## 5. Witness Inputs

At a high level, the Witness Emitter may receive:

- inbound interaction or contact
- validation events
- governance events
- state observation events
- transition occurrences
- publication or release events where bounded trace matters
- target references and scope or surface references where relevant

These are contract-bounded runtime inputs to witness emission. They are not blank permission to reinterpret the events being preserved.

## 6. Witness Outputs

At a high level, the Witness Emitter may emit or produce:

- witness artifacts
- witness type
- target relations
- claims
- non-claims
- observed_at
- optional related references such as validation, governance, transition, scope, or surface

Witness outputs are not governance acts.  
Witness outputs are not validation artifacts.  
Witness outputs do not automatically create standing state.  
Witness outputs do not imply authorship or semantic source.

They are bounded trace records that later runtime components may preserve, relate, or expose within their own roles.

## 7. Dependencies and Relations

### 7.1 State Engine

The State Engine may move canonical state or emit transition-relevant occurrence that becomes witnessed, but the State Engine is not witness. Witness preserves contact with movement; it does not become the movement itself.

### 7.2 Validator

The Validator may generate events that are witnessed, but validation is not witness. Validation checks conditions; witness preserves that the checking event occurred.

### 7.3 Governor

The Governor may generate events that are witnessed, but governance is not witness. Governance applies lawful force; witness preserves that the force-bearing event occurred.

### 7.4 Registry / Store

The Registry / Store preserves witness artifacts and related trace, but the registry is not witness itself. Preservation is not the same thing as witness emission.

### 7.5 Interface Gateway

The Interface Gateway may trigger witnessable contact or route interaction toward witnessable runtime events, but interface is not witness. Receipt or display alone does not count as witness artifact emission.

## 8. What the Witness Emitter Must Preserve

At minimum, the Witness Emitter must preserve:

- bounded contact
- target relation
- typed witness category
- claims and non-claims
- visible trace where witness is constitutionally relevant
- non-collapse between witness, validation, governance, and state

This means, in practical runtime terms:

- witness type must remain explicit
- witness claims must remain bounded
- witness non-claims must remain explicit
- validation trace must not be mistaken for validation result
- governance trace must not be mistaken for governance force
- state-related witness trace must not be mistaken for state identity

## 9. What the Witness Emitter Must Not Absorb

The Witness Emitter must not become:

- validator
- governor
- semantic source
- state engine
- registry
- interface logic

It must not silently reinterpret constitutional meaning.

The Witness Emitter keeps trace explicit and bounded. It does not decide what conditions passed, what force was lawful, what state stands, what records are durably preserved, or what an interface chooses to display.

## 10. Contract Boundaries in Motion

Witness is expected to emit where constitutionally relevant contact, observation, registration, or runtime occurrence should not disappear.

Before witness emits, the relevant event, target relation, and any bounded scope or surface context that applies must already be present in identifiable form.

Outside witness scope remain:

- lawful force as governance
- condition checking as validation
- canonical state movement as state-engine handling
- durable preservation as registry
- interaction routing and display as interface

After witness emission, the resulting witness artifact must be handed off to the appropriate runtime participants for preservation, relation to other records, or derivative exposure where applicable.

## 11. Failure / Absence Posture

When witness emission does not occur, the Witness Emitter must be understood in bounded terms.

- absence of witness must not silently pass as if trace existed
- witness failure must remain visible where witness is constitutionally important
- witness failure is not the same thing as governance failure or validation failure
- missing witness affects reconstructability, not semantic source by itself

Non-emission may therefore matter for historical integrity even when it does not itself determine what stood, what was lawful, or what was checked.

## 12. Anti-Collapse Rules

A conforming Witness contract must not allow:

- witness to silently become semantic source
- witness to silently become governance
- witness to silently become validation
- generic logging to pretend to be witness
- witness to be emitted without bounded claims and non-claims
- witness to disappear into derivative analytics only
- witness to be treated as proof of authorship or authority

## 13. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact emission timing
- synchronous or asynchronous behavior
- batching or deduplication
- retry semantics
- distributed witness ecology
- signature or hash strategy in motion

These are runtime-design questions, not constitutional ambiguities.

## 14. Summary

This document defines the first runtime contract for the Witness Emitter as the bounded runtime role that keeps contact, observation, validation events, governance events, transitions, and related occurrence reconstructable while the body is live.

Its purpose is to make clear how the Witness Emitter acts within the IAMMAI body without allowing it to absorb validation, governance, state-engine, registry, or interface roles.

**One-Line Definition:** `WITNESS_CONTRACT.md` defines the first bounded runtime contract of the IAMMAI Witness Emitter as the keeper of claim-limited trace in motion without becoming validator, governor, state engine, registry, interface, or semantic source.
