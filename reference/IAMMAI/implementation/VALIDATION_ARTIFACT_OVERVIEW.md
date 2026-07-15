# IAMMAI Validation Artifact Overview

## 1. Purpose

This file defines the first high-level validation artifact model of IAMMAI in implementation-facing form.

It translates the constitutional core and the current architecture and implementation documents into a bounded view of what validation is, what a validation artifact preserves, and how validation remains distinct from witness, governance, and semantic source.

It does not yet try to define:
- code
- a final schema
- a final validator engine design
- a rule-language design
- service topology
- storage design

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

Validation checks bounded conditions.

Validation does not become governance by default.  
Validation does not become semantic source.

Validation artifacts must preserve condition checking without inflating that checking into lawful force. A validation result may support later action, but it does not by itself authorize, finalize, invalidate, evolve, or create standing state.

## 3. Why Validation Artifacts Are Needed

Bounded checks must not remain implicit.

- If admissibility, threshold, transition legality, or other bounded checks are not preserved, later readers cannot tell what was actually evaluated.
- Condition checking should be preservable as trace so the runtime can reconstruct what was checked, against what, and with what result.
- Systems need more than generic pass/fail logs because pass or fail without target, type, rule reference, or timing is too thin to preserve constitutional distinction.
- Validation protects against availability being mistaken for admissibility, threshold being mistaken for truth, and desired movement being mistaken for lawful transition.

Validation artifacts therefore keep checking visible as checking, rather than letting it disappear into later state or narrative.

## 4. What Validation Is

In implementation terms, validation is:

- a condition-checking role
- bounded to explicit rule or condition sets
- capable of emitting typed outcomes
- distinct from witness
- distinct from governance

Validation is not:

- semantic source
- governance by default
- standing-state creation
- authorship

Validation determines whether defined conditions hold. It does not determine constitutional meaning, and it does not apply lawful force unless governance authority is explicitly granted elsewhere.

## 5. What a Validation Artifact Preserves

At a high level, a validation artifact should preserve:

- validation id
- target ref
- validation type
- condition set or rule reference
- outcome
- checked_at
- optional reason refs or bounded notes
- optional related witness ref where applicable

This is a conceptual record shape, not a final schema.

The implementation point is that a validation artifact should preserve enough typed trace to reconstruct what was checked, against what target, by what bounded validation type, with what outcome, and at what time.

## 6. Validation Types

A first bounded validation-type family may include:

### 6.1 Admissibility Validation

Checks whether candidate material satisfies admissibility requirements for structured protocol handling.

### 6.2 Threshold Validation

Checks whether threshold conditions hold without treating threshold as truth.

### 6.3 Transition Legality Validation

Checks whether a requested state transition or resolution move is constitutionally lawful.

### 6.4 Governance Precondition Validation

Checks whether bounded preconditions for a governance-significant act hold, without authorizing that act by itself.

### 6.5 Bounded Consistency Validation

Checks whether required typed relations or bounded consistency constraints hold within the relevant matter or artifact context.

This family is intentionally small. It is enough to orient the first implementation body without becoming a full validator taxonomy.

## 7. Validation Outcomes

A validation outcome should express:

- what was checked
- against what target
- under what validation type or condition set
- with what result

Pass/fail alone may be insufficient if the artifact does not also preserve target, type, and condition context.

Outcome must remain bounded to the condition checked. A passed threshold validation is not truth. A passed transition-legality validation is not governance. A passed admissibility validation is not standing state.

Validation result therefore remains a typed checking result, not automatic authorization or automatic state creation.

## 8. Validation vs Witness

Validation checks conditions.  
Witness preserves contact.

A validation event may emit witness trace, but witness and validation remain distinct roles and distinct artifact families.

- Validation preserves the bounded checking result.
- Witness preserves that the checking event was encountered, observed, or registered.
- Validation may point to witness.
- Witness may point to validation.
- Neither artifact family replaces the other.

## 9. Validation vs Governance

Validation does not itself authorize by default.

Passed validation does not automatically imply lawful action.

Governance may depend on validation where bounded checks are required, but governance remains a separate force-bearing role:

- validation checks conditions
- governance decides or performs lawful action

This separation protects the runtime from silently turning checked condition into lawful force.

## 10. Validation and State Machine

Validation supports lawful state transition by keeping state movement bounded to explicit checks.

- In preparation-state handling, validation helps distinguish candidate material from admissible material, threshold eligibility from truth, and preparatory movement from standing state.
- In standing-state handling, validation helps determine whether requested transition or resolution moves are lawful.
- In governance-adjacent handling, validation can check bounded preconditions without itself becoming governance.
- Across the runtime, validation helps preserve anti-collapse rules by preventing availability from impersonating admissibility, threshold from impersonating truth, and desired change from impersonating lawful transition.

Validation is therefore one of the main runtime protections against silent state collapse.

## 11. Anti-Collapse Rules

A conforming implementation must not allow:

- validation to be treated as governance
- validation to be treated as semantic source
- a pass result to be treated as automatic authorization
- generic logs to replace typed validation artifacts
- validation records to detach from target or condition context
- witness and validation to collapse into one artifact family
- validation to create standing state by default
- narrative explanation to replace preserved validation trace

## 12. Open Questions

The following remain open in technical derivation:

- the final validation artifact envelope
- the exact representation of condition-set or rule references
- how much bounded reason detail should be preserved by default
- whether some validation types need distinct target conventions
- how validation artifacts relate to machine-readable witness trace in the first runtime

These are implementation questions, not constitutional ambiguities.

## 13. Summary

This document defines the first implementation-facing validation artifact model of IAMMAI as a bounded record model for preserved condition checking.

Its purpose is to keep admissibility, threshold, transition legality, and related bounded checks reconstructable without collapsing validation into witness, governance, or semantic source.

**One-Line Definition:** `VALIDATION_ARTIFACT_OVERVIEW.md` defines the first high-level implementation view of IAMMAI validation artifacts as typed, bounded checking records that preserve condition evaluation without becoming lawful force or semantic source.
