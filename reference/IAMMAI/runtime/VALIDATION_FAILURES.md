# IAMMAI Validation Failures

## 1. Purpose

This file defines the first runtime-specific failure model for validation in IAMMAI.

Its job is to explain what it means for validation not to pass, how validation failure differs from denial, HOLD, or governance refusal, what must remain visible when validation does not pass, what validation failure produces or preserves, and what must never be cosmetically substituted or silently dropped.

It does not yet try to define:
- code
- retry logic
- monitoring
- incident response
- user-interface wording
- infrastructure transport handling

It is a bounded runtime document focused on validation non-passage and validation failure as architectural integrity concerns.

## 2. First Principle

Failed or non-passing validation must remain typed.

Validation failure must remain visible where constitutionally relevant.  
Failure to pass is not the same thing as governance denial.  
Validation non-passage does not create standing state.  
Validation failure handling must serve the constitutional core, not convenience.

In runtime terms, that means failed, blocked, or indeterminate checking must remain reconstructable as validation output rather than being smoothed into absence, ambiguity, or false passage.

## 3. Why Validation Failures Matter

Validation is one of the first anti-collapse gates in the runtime body.

- Invisible validation failure creates semantic corruption by allowing inadmissible material to look admissible, threshold non-passage to look like truth-eligibility, or unlawful transition requests to look merely delayed.
- Generic `invalid` messaging is not enough because IAMMAI requires typed checking with target relation, condition-set relation, and typed outcome.
- Non-passage must remain reconstructable so later readers can see what failed, what was blocked, what remained indeterminate, and why later movement did not lawfully proceed.
- If validation non-passage disappears, the system becomes structurally vulnerable to premature standing, unlawful transition, and convenience-based reinterpretation.

## 4. Main Validation Failure Families

The main validation-failure families include:

- admissibility failure
- threshold non-passage
- transition legality failure
- governance precondition failure
- bounded consistency failure
- indeterminate or blocked validation outcome where relevant

These families should remain typed apart. They are not one generic validation error condition.

## 5. Validation Failure vs Other Non-Progression

Validation failure is not the same thing as every other non-progression surface.

- validation failure does not equal governance denial
- validation failure does not equal HOLD
- validation failure does not equal missing witness
- validation failure does not equal registry preservation failure
- validation failure may prevent movement, but it is not itself governance force

This distinction matters because the runtime must not collapse checked non-passage into refusal, containment, absence of trace, or storage failure.

## 6. What Must Remain Visible

When validation does not pass, the runtime must preserve at least:

- target relation
- validation type
- condition-set relation
- typed outcome
- reason references where relevant
- time of check

The runtime must also preserve the difference between:

- pass
- fail
- blocked
- indeterminate

Generic disappearance into logs is not acceptable. Validation non-passage must remain visible as typed validation trace rather than dissolving into summary language or silent non-action.

## 7. Relation to Runtime Components

### 7.1 Interface Gateway

The Interface Gateway may surface or route around failed validation, but it must not redefine validation non-passage by presentation smoothing, omission, or convenience status.

### 7.2 Witness Emitter

The Witness Emitter may preserve validation-failure events as trace, but witness is not the failure itself. Witness preserves that checking occurred; validation defines the typed non-passage outcome.

### 7.3 Governor

The Governor may never silently treat validation failure as successful precondition. Governance may later deny, hold, or otherwise not proceed, but that remains distinct from the validation failure itself.

### 7.4 State Engine

The State Engine must not move as if validation passed where validation is required. Failed, blocked, or indeterminate validation therefore constrains later state handling without becoming state movement itself.

### 7.5 Registry / Store

The Registry / Store must preserve relevant validation-failure trace where constitutionally important so non-passage remains reconstructable rather than disappearing into absence.

## 8. Validation Failure Sequences

### 8.1 Candidate Material Failing Admissibility

1. Candidate material enters bounded checking.
2. The Validator performs admissibility checking.
3. Admissibility does not pass.
4. A typed validation outcome is produced and preserved.
5. Later preparation-side movement must not proceed as though admissibility held.

### 8.2 Threshold Not Being Met

1. Threshold-relevant matter is routed into threshold checking.
2. The Validator checks threshold conditions.
3. Threshold does not pass.
4. A typed validation outcome is produced and preserved.
5. Truth formation must not proceed as though threshold satisfaction existed.

### 8.3 Transition Legality Failure

1. A requested state movement is routed into legality checking.
2. The Validator checks the requested move against lawful transition constraints.
3. Legality does not pass.
4. A typed validation outcome is produced and preserved.
5. The State Engine must not move as though the requested transition were lawful.

### 8.4 Governance Precondition Failure

1. A governance-significant matter is routed into precondition checking.
2. The Validator checks the required preconditions.
3. Preconditions do not pass.
4. A typed validation outcome is produced and preserved.
5. The Governor must not treat the failed precondition as satisfied by convenience.

### 8.5 Indeterminate Validation Outcome

1. A bounded check is attempted.
2. Required conditions cannot yet be resolved in bounded form, or checking remains blocked.
3. An indeterminate or blocked validation outcome is produced and preserved.
4. Later runtime participants must treat that outcome distinctly from both pass and fail.

## 9. Anti-Collapse Rules

A conforming runtime must not allow:

- failed validation to disappear into ambiguity
- failed validation to be treated as governance denial without distinction
- failed validation to be cosmetically rewritten as `not ready yet` when the type matters
- pass or fail to lose relation to target or condition context
- interface smoothing to override canonical validation non-passage
- state movement to proceed as if required validation passed

## 10. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact retry behavior
- batching behavior
- escalation paths
- user or operator-facing messaging
- infrastructure-level transport failures

These are runtime-design questions, not constitutional ambiguities.

## 11. Summary

This document defines the first runtime-specific failure model for validation in IAMMAI as a bounded account of typed validation non-passage across admissibility, threshold, legality, governance preconditions, consistency, and indeterminate checking.

Its purpose is to keep failed, blocked, or indeterminate validation visible and reconstructable so the runtime does not cosmetically rewrite non-passage into apparent success or ambiguity.

**One-Line Definition:** `VALIDATION_FAILURES.md` defines the first bounded runtime model of IAMMAI validation failures as typed, visible non-passage that must remain reconstructable rather than being smoothed into denial, delay, or apparent success.
