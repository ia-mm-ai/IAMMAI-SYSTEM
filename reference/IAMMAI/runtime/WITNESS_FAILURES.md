# IAMMAI Witness Failures

## 1. Purpose

This file defines the first runtime-specific failure model for witness emission in IAMMAI.

Its job is to explain what it means for witness not to be emitted, be incomplete, be blocked, or fail, how witness failure differs from validation failure, governance refusal, HOLD, or registry failure, what must remain visible when witness does not occur where witness is constitutionally important, what witness failure does and does not imply, and what must never be cosmetically substituted or silently dropped.

It does not yet try to define:
- code
- retry logic
- monitoring
- incident response
- a full witness ecology design
- infrastructure transport handling

It is a bounded runtime document focused on witness failure and witness absence as architectural integrity concerns.

## 2. First Principle

Witness failure or absence must remain typed where witness is constitutionally important.

Missing witness must not silently masquerade as existing trace.  
Witness failure is not the same thing as governance failure, validation failure, or semantic invalidity.  
Witness failure handling must serve the constitutional core, not convenience.

In runtime terms, that means missing, incomplete, blocked, indeterminate, or failed witness emission must remain reconstructable as absence or failure of trace rather than being smoothed into apparent presence.

## 3. Why Witness Failures Matter

Witness protects against disappearance and cosmetic substitution.

- Witness absence can damage reconstructability even when validation, governance, state handling, or preservation still otherwise function.
- If runtime contact or occurrence is not witnessed where witness is constitutionally relevant, later readers may be left with summary, memory, or derivative appearance instead of bounded trace.
- Generic `logging failed` language is not enough because witness is not generic logging. Witness preserves bounded claims, non-claims, target relation, and typed trace.
- Missing witness must remain visible when witness is constitutionally relevant so the body does not pretend that trace exists when only the underlying event occurred.

## 4. Main Witness Failure Families

The main witness-failure families include:

- witness not emitted
- witness emitted incompletely
- witness emitted without bounded claims or non-claims
- witness blocked
- witness indeterminate
- witness emitted but not preserved as canonical trace
- witness attempted on wrong target or wrong scope where relevant

These families should remain typed apart. They are not one generic witness error condition.

## 5. Witness Failure vs Other Non-Progression

Witness failure is not the same thing as every other non-progression surface.

- witness failure does not equal validation failure
- witness failure does not equal governance denial
- witness failure does not equal HOLD
- witness failure does not equal registry preservation failure, though the two may relate
- witness failure does not by itself mean the underlying event was false
- witness absence affects trace and reconstructability, not automatic semantic invalidation

This distinction matters because the runtime must not collapse missing trace into failed checking, denied force, containment, or invalidity.

## 6. What Must Remain Visible

When witness does not occur as expected, the runtime must preserve at least:

- where witness was expected
- what witness type was expected
- what target or surface the witness related to
- whether witness was missing, incomplete, blocked, or indeterminate
- what bounded claims or non-claims were absent or compromised
- when the failure occurred

Generic disappearance into logs is not acceptable. Missing or compromised witness must remain visible as typed witness non-passage rather than dissolving into omission or cosmetic continuity.

## 7. Relation to Runtime Components

### 7.1 Interface Gateway

The Interface Gateway may trigger witnessable contact, but it must not pretend witness exists when it does not. Presentation or routing does not substitute for witness emission.

### 7.2 Validator

Validation may still occur without witness, but the distinction must remain visible. Failed or missing witness must not be restated as validation failure, and validation success must not be used to fabricate witness presence.

### 7.3 Governor

Governance may still act where lawfully possible, but it must not fabricate witness. Governance occurrence and witness trace remain distinct even when both concern the same event.

### 7.4 State Engine

State movement is not identical to witness trace. A transition or state-relevant event may occur without successful witness emission, and that absence must remain visible rather than being overwritten by the fact of movement.

### 7.5 Registry / Store

The Registry / Store may preserve witness failure state or missing-witness trace where relevant, but the registry is not witness itself. Preservation does not substitute for the missing witness act.

## 8. Witness Failure Sequences

### 8.1 Interaction / Contact Occurred but Witness Was Not Emitted

1. Bounded interaction or contact occurs.
2. Witness was expected for that contact.
3. No witness artifact is emitted.
4. The absence remains visible rather than being treated as if contact had been witnessed.

### 8.2 Validation Event Occurred but Witness Trace Was Missing

1. The Validator performs bounded checking.
2. A validation event occurs in runtime.
3. Witness trace expected for that event is missing.
4. Validation remains distinct from witness absence, and the missing witness remains visible.

### 8.3 Governance Act Occurred but Witness Trace Was Blocked

1. The Governor performs or authorizes a protocol-significant act.
2. Witness emission is attempted or expected.
3. Witness trace is blocked or does not complete in bounded form.
4. Governance occurrence must not be rewritten as witnessed occurrence by convenience.

### 8.4 Transition Occurred but Witness Was Incomplete

1. A transition or state-relevant occurrence happens.
2. A witness artifact is emitted, but without required bounded completeness.
3. The incompleteness remains visible.
4. Incomplete witness must not be treated as equivalent to a complete bounded witness artifact.

### 8.5 Publication / Release Surface Expected Witness but No Bounded Artifact Was Produced

1. A publication or release surface emits protocol-relevant exposure.
2. Witness was expected for bounded publication trace.
3. No bounded witness artifact is produced.
4. Derivative display or access logs must not substitute for canonical witness presence.

## 9. Anti-Collapse Rules

A conforming runtime must not allow:

- missing witness to be treated as if trace existed
- generic logging to be treated as equivalent to witness
- witness absence to be cosmetically rewritten as continuity
- witness failure to be treated as automatic semantic invalidity
- governance or validation to silently stand in for witness
- derivative analytics or UI traces to substitute for canonical witness absence or presence

## 10. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact retry behavior
- batching or deduplication behavior
- signature or hash fallback strategies
- distributed witness emission timing
- operator-facing messaging for witness absence or failure

These are runtime-design questions, not constitutional ambiguities.

## 11. Summary

This document defines the first runtime-specific failure model for witness emission in IAMMAI as a bounded account of missing, incomplete, blocked, indeterminate, or failed witness trace across interaction, validation, governance, transition, and publication-related occurrence.

Its purpose is to keep witness absence or failure visible and reconstructable so the runtime does not cosmetically rewrite missing trace into apparent presence or false continuity.

**One-Line Definition:** `WITNESS_FAILURES.md` defines the first bounded runtime model of IAMMAI witness failures as typed, visible absence or compromise of witness trace that must remain reconstructable rather than being smoothed into apparent trace.
