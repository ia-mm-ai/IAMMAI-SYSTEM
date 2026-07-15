# IAMMAI Validator Flow

## 1. Purpose

This file defines the first runtime-specific flow of the Validator inside the IAMMAI body.

Its job is to explain when validation is invoked, what kinds of checks it performs, what it produces, what it must not decide, and how it relates to the other runtime participants while the body is in motion.

It does not yet try to define:
- code
- validator engine implementation
- API contracts
- service topology
- infrastructure behavior
- full rule-language design

It is a bounded runtime-flow document focused on validator behavior.

## 2. First Principle

Validation checks bounded conditions.

Validation does not become lawful force by default.  
Validation does not become semantic source.

Validation must remain:
- typed
- attributable as process
- bounded to explicit condition sets

In runtime terms, that means the body must be able to show what was checked, against what target, under what condition set, with what outcome, at what time, and with what bounded process attribution where such attribution is preserved.

## 3. Why Validator Flow Matters

Validation order matters in runtime.

- If validation does not appear in the runtime sequence where it is required, the body can begin treating available material as admissible, threshold as truth, or desired movement as lawful transition.
- Generic `checks passed` language is not enough because validation must remain typed by target, condition set, and outcome.
- Validation must be visible in motion, not only in schema, because runtime order determines whether bounded checking actually constrains action.
- Validation protects against premature standing and unlawful transition by forcing explicit condition checking before later state movement or governance action depends on it.

Validator flow is therefore one of the main runtime protections against silent collapse.

## 4. Validator Inputs

At a high level, the Validator may receive:

- candidate material in preparation
- threshold-related matter
- a requested transition
- a governance precondition check request
- a bounded consistency or typed-state check

These are runtime inputs to bounded checking. They are not yet governance acts, and they are not yet canonical state movement by themselves.

## 5. Validator Checks

The Validator may perform several typed categories of checks.

### 5.1 Admissibility

Checks whether candidate material satisfies admissibility requirements for structured protocol handling.

### 5.2 Threshold

Checks whether threshold conditions hold without turning threshold into truth.

### 5.3 Transition Legality

Checks whether a requested transition or typed resolution move is constitutionally lawful.

### 5.4 Governance Preconditions

Checks whether bounded preconditions for a governance-significant act hold without authorizing that act by itself.

### 5.5 Bounded Consistency

Checks whether required typed relations or bounded consistency constraints hold within the relevant matter, state, transition, or artifact context.

These checks must remain typed. Validator flow must not collapse them into one generic validation blob.

## 6. Validator Outputs

Validator flow produces validation output in bounded form.

At minimum, that output should preserve:
- a validation artifact
- a typed outcome
- target relation
- condition-set relation
- time of check
- optional reason references
- optional relation to witness where witness trace is emitted

The outcome may be expressed in bounded forms such as:
- pass
- fail
- blocked
- indeterminate

Validation output does not automatically authorize action.  
Validation output does not automatically create standing state.

It remains a typed checking result that later runtime participants may depend on within their own lawful bounds.

## 7. Validator Relation to Other Runtime Components

### 7.1 Interface Gateway

The Interface Gateway routes bounded input toward validation where validation is required. It does not declare that something has passed merely because it has been received.

### 7.2 Witness Emitter

The Witness Emitter may preserve validation events as trace, but validation is not witness. Validation checks conditions; witness preserves that checking occurred.

### 7.3 Governor

The Governor may depend on validation where bounded checks are required, but validation is not governance. Passed validation does not itself authorize, hold, release, finalize, invalidate, or evolve.

### 7.4 State Engine

The State Engine depends on lawful checks where state movement requires them, but validation is not the State Engine. Validation checks; the State Engine applies canonical state movement.

### 7.5 Registry / Store

The Registry / Store preserves validation trace, but it is not validation itself. Preservation is not the same thing as checking.

## 8. Validator Flow Sequences

### 8.1 Preparation-Side Validation Flow

1. The Interface Gateway receives candidate material.
2. The Validator checks admissibility or other required preparation-side conditions.
3. The Witness Emitter may preserve contact or validation trace where runtime-relevant occurrence should remain reconstructable.
4. If conditions pass, later preparation-state movement may proceed through the State Engine.
5. The Registry / Store preserves validation output and any resulting trace.

Preparation-side passage does not create standing state.

### 8.2 Threshold-Related Validation Flow

1. Threshold-relevant matter is routed into bounded checking.
2. The Validator checks threshold conditions explicitly.
3. A typed validation output is produced.
4. If threshold passes, that result may support later lawful movement toward truth where other required conditions also hold.
5. If threshold does not pass, the non-passage remains preservable and does not silently disappear.

Threshold passage is not truth.

### 8.3 Governance Precondition Validation Flow

1. A governance-significant request or matter is routed into bounded precondition checking.
2. The Validator checks the required preconditions.
3. A typed validation output is produced.
4. The Governor may later act if lawful force is required and if authority, legitimacy basis, and matter scope also hold.
5. The Registry / Store preserves both the validation trace and any later governance trace as distinct records.

Passed governance precondition validation is not governance action.

### 8.4 Transition Legality Validation Flow

1. A requested state movement or typed resolution move is routed into legality checking.
2. The Validator checks whether the requested move is constitutionally lawful.
3. A typed validation output is produced with target and condition context.
4. If lawful and otherwise permitted, the State Engine may later apply the movement, with governance participating where required.
5. The Registry / Store preserves the validation and any resulting transition trace separately.

Passed transition-legality validation is not the transition itself.

## 9. Failure / Non-Passage Posture

When conditions do not pass, validator flow must remain explicit and preservable.

- Failure must remain typed.
- Non-passage must remain preservable.
- Failed validation does not become governance by itself.
- Failed validation must not disappear into generic logs.

A failed, blocked, or indeterminate result may stop later movement, but it must still remain reconstructable as validation output rather than dissolving into absence or narrative explanation.

## 10. Anti-Collapse Rules

A conforming validator flow must not allow:

- validation to silently become governance
- validation to silently become witness
- a pass result to be treated as automatic authorization
- failed validation to disappear without trace
- validation to detach from target or condition context
- generic check results to replace typed validation outcomes
- validation to create standing state by default
- validation trace to be overwritten by later state or governance events

## 11. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact synchronous or asynchronous behavior
- retry semantics
- batching behavior
- queueing and buffering model
- detailed validator engine logic

These are runtime-design questions, not constitutional ambiguities.

## 12. Summary

This document defines the first runtime-specific flow of the Validator as the bounded checking path through which candidate material, threshold-related matter, transition requests, and governance preconditions are evaluated before later runtime participants act on them.

Its purpose is to keep validation visible in motion as typed condition checking without allowing it to become witness, governance, semantic source, or standing-state creation.

**One-Line Definition:** `VALIDATOR_FLOW.md` defines the first bounded runtime flow of the IAMMAI Validator as typed condition checking in motion before later lawful state or governance action depends on it.
