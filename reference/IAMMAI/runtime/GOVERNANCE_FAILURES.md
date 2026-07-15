# IAMMAI Governance Failures

## 1. Purpose

This file defines the first runtime-specific failure model for governance in IAMMAI.

Its job is to explain what it means for governance not to proceed, to deny, to hold, to refuse, or to fail, how governance failure differs from validation failure, witness failure, HOLD, or registry failure, what must remain visible when governance does not lawfully proceed, what governance failure does and does not imply, and what must never be cosmetically substituted or silently dropped.

It does not yet try to define:
- code
- retry logic
- incident response
- a policy essay
- operator procedures
- infrastructure transport handling

It is a bounded runtime document focused on governance non-progression and governance failure as architectural integrity concerns.

## 2. First Principle

Governance non-progression must remain typed.

Governance failure must remain attributable where constitutionally relevant.  
Denial, hold, refusal, and failure are not the same thing.  
Governance failure handling must serve the constitutional core, not convenience.  
Governance non-progression must not be cosmetically rewritten as if lawful force occurred.

In runtime terms, that means the body must preserve when force-bearing action did not lawfully proceed, in what form it did not proceed, and under what bounded authority, legitimacy, and matter conditions that non-progression occurred.

## 3. Why Governance Failures Matter

Governance is the runtime location of lawful force.

- Invisible governance failure creates semantic corruption by making absent authorization look present, denied action look merely delayed, or blocked force look like continuity.
- Generic `action not completed` language is not enough because IAMMAI requires governance to remain attributable, legitimacy-bounded, matter-scoped, and typed by act family.
- Governance non-progression must remain reconstructable and attributable so later readers can see whether an act was denied, held, blocked, refused, indeterminate, or failed in attempted execution.
- If governance non-progression disappears, the system becomes vulnerable to anonymous force, scope bleed, and convenience-based reinterpretation of what lawfully occurred.

## 4. Main Governance Failure Families

The main governance-failure families include:

- denial
- hold or release non-progression
- refusal to authorize
- failed finalize, invalidate, or evolve action
- blocked governance due to missing prerequisites
- indeterminate governance state where relevant
- governance attempted without valid legitimacy basis or matter scope

These families should remain typed apart. They are not one generic governance error condition.

## 5. Governance Failure vs Other Non-Progression

Governance failure is not the same thing as every other non-progression surface.

- governance failure does not equal validation failure
- governance failure does not equal witness failure
- governance failure does not equal HOLD as such
- governance refusal does not equal registry preservation failure
- governance non-progression does not automatically falsify the underlying signal or candidate material
- denial, hold, refusal, and failure must not collapse into one generic `no`

This distinction matters because the runtime must not collapse failed or non-proceeding force into checking failure, trace absence, containment, or preservation failure.

## 6. What Must Remain Visible

When governance does not lawfully proceed, the runtime must preserve at least:

- what action was requested
- what matter it related to
- what authority class and legitimacy basis were in play
- whether the result was denial, hold, refusal, blocked, failed, or indeterminate
- when the non-progression occurred
- what prerequisites were missing or unsatisfied where relevant

Generic disappearance into logs is not acceptable. Governance non-progression must remain visible as typed governance trace rather than dissolving into omission, summary language, or cosmetic continuity.

## 7. Relation to Runtime Components

### 7.1 Interface Gateway

The Interface Gateway may route governance requests, but it must not pretend force occurred when it did not. Presentation, receipt, or request capture do not substitute for governance action.

### 7.2 Validator

Validation may block governance lawfully, but governance non-progression is not the same thing as validation failure. Passed validation also does not imply that governance force automatically followed.

### 7.3 Witness Emitter

Witness may preserve governance non-progression, but witness is not governance. Witness preserves that governance denial, hold, refusal, or failure occurred; it does not supply the force or its absence.

### 7.4 State Engine

State movement must not proceed as if governance force occurred when it did not. Governance non-progression therefore constrains later state handling without becoming state movement itself.

### 7.5 Registry / Store

The Registry / Store must preserve governance non-progression where constitutionally relevant so denied, held, blocked, refused, or failed force remains reconstructable rather than disappearing into ambiguity.

## 8. Governance Failure Sequences

### 8.1 Governance Request Denied

1. A governance-significant request is routed into governance handling.
2. Required context and checks are considered in bounded form.
3. The Governor determines that the requested act does not lawfully proceed.
4. A typed denial outcome is produced and preserved.
5. Later runtime participants must not behave as though authorization existed.

### 8.2 Governance Request Held

1. A request reaches a point where force-bearing movement might otherwise proceed.
2. HOLD is applied as bounded containment.
3. The hold remains visible as hold rather than as denial, success, or silent delay.
4. Later movement must remain constrained according to that containment.

### 8.3 Finalize Attempted but Not Lawfully Completed

1. A finalize request is routed into bounded checking and governance handling.
2. Finalize does not lawfully proceed or does not complete in bounded form.
3. The non-progression is preserved as failed, blocked, refused, or indeterminate finalize rather than generic update absence.
4. The State Engine must not behave as though lawful closure occurred.

### 8.4 Invalidate or Evolve Requested but Blocked by Missing Prerequisites

1. An invalidate or evolve request is routed into governance handling.
2. Required prerequisites are not satisfied in bounded form.
3. Governance does not lawfully proceed.
4. The blocked condition remains visible as governance non-progression rather than as completed force.

### 8.5 Governance Request Received Without Sufficient Legitimacy Basis

1. A governance-significant request is presented.
2. Legitimacy basis is absent, insufficient, or invalid within the bounded act context.
3. Governance force does not lawfully proceed.
4. The resulting non-progression remains attributable and visible rather than collapsing into anonymous non-action.

### 8.6 Governance Request Outside Matter Scope

1. A governance request targets a matter outside the lawful scope of the attempted action.
2. Matter-bounded governance cannot lawfully proceed.
3. The non-progression is preserved as scope-bounded governance failure or refusal.
4. Later runtime participants must not treat the act as if it applied across matters.

## 9. Anti-Collapse Rules

A conforming runtime must not allow:

- denied governance to be rewritten as if authorization existed
- hold to be treated as silent continuity or success
- failed governance to disappear into ambiguity
- validation success to be treated as if governance force automatically followed
- state movement to proceed as if governance act occurred when it did not
- anonymous or unattributed non-progression
- derivative UI or analytics to substitute for canonical governance trace

## 10. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact escalation behavior
- timeout or retry semantics
- multi-governor coordination
- distributed delegation handling
- operator-facing messaging for governance non-progression or failure

These are runtime-design questions, not constitutional ambiguities.

## 11. Summary

This document defines the first runtime-specific failure model for governance in IAMMAI as a bounded account of denied, held, refused, blocked, failed, or indeterminate lawful-force non-progression across authorization and typed governance acts.

Its purpose is to keep governance non-progression visible, attributable, and reconstructable so the runtime does not cosmetically rewrite missing or failed force into apparent continuity or silent authorization.

**One-Line Definition:** `GOVERNANCE_FAILURES.md` defines the first bounded runtime model of IAMMAI governance failures as typed, attributable non-progression of lawful force that must remain reconstructable rather than being smoothed into continuity or apparent authorization.
