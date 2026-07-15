# IAMMAI Governor Flow

## 1. Purpose

This file defines the first runtime-specific flow of the Governor inside the IAMMAI body.

Its job is to explain when governance is invoked, what kinds of acts the governor may perform, what inputs governance depends on, what the governor must preserve, what the governor must not claim, and how the governor relates to the other runtime participants while the body is in motion.

It does not yet try to define:
- code
- a final governance engine implementation
- policy essays
- API contracts
- service topology
- infrastructure behavior

It is a bounded runtime-flow document focused on governance behavior.

## 2. First Principle

Governance is lawful protocol force.

Governance must remain:
- attributable
- legitimacy-bounded
- matter-scoped

Governance must not become semantic source.

In runtime terms, that means lawful force must remain explicitly tied to a bounded actor or authority node, a legitimacy basis, a matter relation, and a typed act rather than appearing as ambient mutation.

## 3. Why Governor Flow Matters

Lawful force must be explicit in runtime motion.

- If governance appears only as changed state, the body cannot show who acted, under what basis, on what matter, or within what lawful scope.
- Governance cannot be reduced to ambient mutation because lawful force is a distinct runtime role, not a side effect of storage, display, or convenience.
- Governance order matters because validation may need to constrain governance first, and state movement may depend on governance later, but those roles must remain distinct.
- Governance protects against anonymous or convenience-based action by keeping attributable force visible in motion.

Governor flow is therefore the runtime protection against opaque force.

## 4. Governor Inputs / Trigger Points

At a high level, governor flow may be invoked at moments such as:

- an authorization request
- a denial decision
- a hold or release request
- a finalize, invalidate, or evolve request
- governance action following successful validation where required
- a bounded exceptional pathway where lawful force is needed

These are governance trigger points. They are not proof that governance is always required, but when lawful force is required, governance must appear explicitly.

## 5. What Governor Flow Does

Governor flow may perform several main categories of lawful act.

### 5.1 Authorize

Applies bounded authorization where lawful force is required.

### 5.2 Deny

Applies a typed refusal where the requested act does not lawfully proceed.

### 5.3 Hold

Applies HOLD to prevent an otherwise eligible irreversible transition from proceeding.

### 5.4 Release

Lifts prior containment so permissibility may be restored.

### 5.5 Finalize

Applies lawful closure in current form.

### 5.6 Invalidate

Applies removal of standing without erasing trace.

### 5.7 Evolve

Applies lawful successor creation in explicit relation to prior state.

These are typed lawful acts. Governance applies force. Governance does not invent semantic source.

## 6. What Governor Flow Preserves

Governor flow must preserve, at minimum:

- a governance action record
- actor or authority node
- authority class
- legitimacy basis
- matter relation
- action type
- acted_at
- optional delegation relation
- optional related references to validation, witness, transition, or state

Governance must remain attributable.  
Governance must remain legitimacy-bounded.  
Governance must remain matter-scoped.

Without those preserved relations, runtime force collapses into untyped power.

## 7. Governor Relation to Other Runtime Components

### 7.1 Interface Gateway

The Interface Gateway may route requests toward governance, but interface is not governor. It receives and presents requests; it does not itself apply lawful force.

### 7.2 Validator

The Validator may supply bounded checks, but validation is not governance. Passed validation does not itself authorize, hold, release, finalize, invalidate, or evolve.

### 7.3 Witness Emitter

The Witness Emitter may preserve governance events, but witness is not governance. Witness preserves trace that governance occurred; it does not supply the force of the act.

### 7.4 State Engine

The State Engine may carry out state movement after governance force is applied where such force is required, but governance is not the State Engine. Governance applies lawful force; the State Engine applies canonical state movement.

### 7.5 Registry / Store

The Registry / Store preserves governance trace, but storage is not governance itself. Preservation is not the same thing as acting.

## 8. Governor Flow Sequences

### 8.1 Authorization Flow

1. A bounded request enters runtime.
2. The Interface Gateway routes the matter toward required checks or governance handling.
3. The Validator checks bounded conditions where required.
4. The Governor determines whether lawful authorization applies within authority class, legitimacy basis, and matter scope.
5. A governance action record is produced.
6. The State Engine may then apply later state movement where authorization is a required condition.
7. The Registry / Store preserves governance trace and any resulting related records.

Authorization is a governance act, not a validation result.

### 8.2 Hold / Release Flow

1. A hold or release request is routed into governance handling.
2. The Validator may check bounded preconditions where required.
3. The Governor applies HOLD or release as a typed act.
4. The State Engine preserves containment as orthogonal to state identity.
5. The Registry / Store preserves governance trace, containment relation, and any related transition trace.

HOLD remains distinct from denial and from resolution.

### 8.3 Finalize Flow

1. A finalize request is routed into bounded checking and governance handling.
2. The Validator checks required legality or preconditions where applicable.
3. The Governor applies FINALIZE as typed lawful force.
4. The State Engine applies the corresponding typed closure behavior.
5. The Registry / Store preserves governance trace, transition trace, and resulting state relation.

Finalize is not a generic update.

### 8.4 Invalidate Flow

1. An invalidate request is routed into bounded checking and governance handling.
2. Required checks occur where applicable.
3. The Governor applies INVALIDATE as typed lawful force.
4. The State Engine applies removal of standing without erasing trace.
5. The Registry / Store preserves governance trace and resulting lineage-relevant records.

Invalidate is not deletion.

### 8.5 Evolve Flow

1. An evolve request is routed into bounded checking and governance handling.
2. The Validator checks required legality or preconditions where applicable.
3. The Governor applies EVOLVE as typed lawful force.
4. The State Engine applies lawful successor creation in explicit relation to prior state.
5. The Registry / Store preserves governance trace, predecessor relation, transition trace, and resulting successor state.

Evolve is not overwrite.

### 8.6 Denial Flow

1. A requested act is routed toward governance handling.
2. Required checks may occur first.
3. The Governor determines that the act does not lawfully proceed.
4. A denial record remains attributable, matter-scoped, and legitimacy-bounded.
5. The Registry / Store preserves that denial as typed governance outcome rather than letting the request disappear into ambiguity.

Denial is a typed governance act, not absence of response.

## 9. Delegation in Motion

Delegation may extend lawful action without erasing attribution.

- Delegated flow must preserve source relation.
- Delegated force must remain bounded.
- Delegation must not create anonymous governance.

In runtime terms, that means delegated action still needs attributable actor relation, delegating source relation where applicable, legitimacy basis, matter scope, and typed action trace.

## 10. Governance vs Validation

Governance may depend on validation.

Passed validation does not automatically imply governance.

Governance decides or performs lawful force.  
Validation does not replace governance.

Where bounded checks are required, governance should remain downstream of those checks without collapsing into them.

## 11. Governance vs Witness

Witness may preserve governance events.

Witness is not lawful force.  
Governance does not become witness by acting.

These roles remain distinct in motion:
- governance acts
- witness preserves that the act occurred

## 12. Failure / Refusal Posture

When governance does not proceed, runtime handling must remain explicit and attributable.

- denial must remain typed
- hold must remain distinct from denial and resolution
- refusal must remain attributable
- non-action where governance was invoked must not disappear into ambiguity

If a governance-relevant request does not proceed, the runtime should preserve whether that was denial, hold, blocked precondition, or other bounded non-progression rather than letting absence masquerade as lawful completion.

## 13. Anti-Collapse Rules

A conforming governor flow must not allow:

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

This document defines the first runtime-specific flow of the Governor as the bounded lawful-force path through which authorization, denial, hold, release, finalize, invalidate, and evolve are applied while the body is live.

Its purpose is to keep governance explicit in motion as attributable, legitimacy-bounded, matter-scoped force without allowing it to collapse into witness, validation, semantic source, or ambient mutation.

**One-Line Definition:** `GOVERNOR_FLOW.md` defines the first bounded runtime flow of the IAMMAI Governor as the application of typed lawful force in motion with explicit attribution, legitimacy basis, matter scope, and preserved trace.
