# IAMMAI Failure Surfaces

## 1. Purpose

This file defines the first runtime-level failure model for IAMMAI.

Its job is to explain what kinds of failure or non-passage the runtime must preserve explicitly, why failure is not a side-case in IAMMAI, how failure differs across the main runtime participants, and why failed, blocked, denied, absent, or non-proceeding events must not be cosmetically edited into apparent continuity.

It does not yet try to define:
- code
- incident response
- infrastructure failure handling
- retry logic
- queue design
- monitoring or alerting implementation

It is a bounded runtime architecture document about failure surfaces as constitutional and runtime-integrity concerns.

## 2. First Principle

Failure must remain typed.

Non-passage must remain visible.  
Blocked, denied, absent, or failed runtime events must not be silently rewritten into apparent continuity.  
Failure handling must serve the constitutional core, not convenience.

In runtime terms, that means the live body must preserve not only what lawfully proceeds, but also what did not proceed, why it did not proceed, and which runtime role the non-progression belonged to.

## 3. Why Failure Surfaces Matter

IAMMAI cannot treat failure as generic background noise.

- Lawful systems must preserve not only what proceeds, but what does not proceed, because non-passage is often part of the bounded truth of runtime behavior.
- Invisible failure creates semantic collapse by making blocked checking look like clean passage, missing witness look like present trace, governance non-action look like lawful continuity, or failed preservation look like durable history.
- Cosmetic substitution of missing or failed runtime actions is architecturally unacceptable because it allows derivative appearance to replace canonical runtime truth.
- Failure is therefore not a side-case. It is part of keeping lawful motion reconstructable.

## 4. Main Failure Surface Families

The main failure-surface families include:

- validation non-passage
- missing or failed witness emission
- governance refusal or non-proceeding action
- failed or blocked state movement
- failed or missing registry preservation
- interface-level appearance that does not match canonical runtime truth

These families should remain typed apart. They are not one generic runtime error concept.

## 5. Failure vs Refusal vs Containment

Not all non-progression is failure.

- HOLD is not failure. HOLD is orthogonal containment that lawfully prevents an otherwise eligible irreversible transition from proceeding.
- Governance denial is not the same thing as system failure. It is a typed governance outcome.
- Validation non-passage is not the same thing as governance refusal. A failed or blocked check remains validation output unless governance later acts in its own role.
- Absence of witness is not the same thing as invalidity. Missing trace affects reconstructability, not semantic source by itself.
- Preservation failure is not the same thing as interpretive disagreement. It is failure of canonical durability, not a narrative dispute about meaning.

This distinction matters because runtime integrity depends on keeping held, denied, failed, blocked, absent, and merely non-occurring conditions visibly distinct.

## 6. Runtime Visibility Requirement

Failure must remain visible at the runtime level where it matters.

- Failure must not silently disappear into logs, UI smoothing, or later summary.
- Typed non-passage is part of reconstructable history.
- The runtime must preserve the difference between:
  - nothing happened
  - something was blocked
  - something failed
  - something was denied
  - something was held

Without that visibility, later surfaces can cosmetically replace non-passage with apparent continuity.

## 7. Relation to Runtime Components

### 7.1 State Engine

The State Engine can encounter blocked or non-proceeding movement. Not all non-movement is failure, but failed or blocked movement must remain distinct from successful state mutation.

### 7.2 Validator

The Validator can produce non-passage such as fail, blocked, or indeterminate outcomes. These must remain typed as validation results rather than disappearing into ambiguity.

### 7.3 Witness Emitter

The Witness Emitter can fail to emit or fail to preserve trace. Missing witness must remain visible where witness is constitutionally relevant, and it must not be restated as though trace existed.

### 7.4 Governor

The Governor can deny, hold, or otherwise not proceed. Governance refusal or bounded non-action must remain attributable and typed rather than being cosmetically rewritten as continuity.

### 7.5 Registry / Store

The Registry / Store can fail to preserve canonical records. Preservation failure must remain visible as preservation failure, not be hidden by derivative surfaces or caches.

### 7.6 Interface Gateway

The Interface Gateway can misrepresent runtime truth by smoothing over absence, failure, denial, or missing preservation. Interface must therefore remain subordinate to canonical runtime state and typed failure visibility.

Each component can fail or not proceed in different ways. Components must not silently absorb each other’s failures.

## 8. Failure Anti-Collapse Rules

A conforming runtime must not allow:

- failed validation to disappear into ambiguity
- missing witness to be treated as if trace existed
- governance non-action to be cosmetically rewritten as continuity
- blocked state movement to appear as successful state mutation
- registry preservation failure to be hidden by derivative views
- interface presentation to smooth over canonical runtime absence
- consequence to be inferred where the runtime did not lawfully proceed

## 9. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact retry behavior
- exact escalation behavior
- transport or infrastructure failure taxonomy
- queue or buffering semantics
- monitoring or alerting implementations

These are runtime-design questions, not constitutional ambiguities.

## 10. Summary

This document defines the first runtime-level failure model of IAMMAI as a bounded account of typed non-passage across validation, witness, governance, state movement, preservation, and interface appearance.

Its purpose is to keep failed, blocked, denied, absent, and held runtime conditions visible so the live body does not cosmetically rewrite non-progression into false continuity.

**One-Line Definition:** `FAILURE_SURFACES.md` defines the first bounded runtime model of IAMMAI failure surfaces as typed, visible non-passage that must remain reconstructable rather than being smoothed into apparent continuity.
