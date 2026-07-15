# IAMMAI Validator Contract

## 1. Purpose

This file defines the first runtime contract for the Validator inside the IAMMAI body.

Its job is to explain what the Validator is responsible for, what it may receive, what it may emit, what it depends on, what it must preserve, what it must never absorb, and how it relates to the other runtime parts without collapsing their roles.

It does not yet try to define:
- code
- an API specification
- a validator engine implementation
- service design
- infrastructure topology
- detailed internal validator logic

It is a bounded runtime-contract document.

## 2. First Principle

The Validator checks bounded conditions.

It serves the constitutional core.  
It does not apply lawful force by default.  
It does not invent semantic source.  
It does not replace witness, governance, state engine, registry, or interface.

In runtime terms, the Validator is the component that keeps condition checking explicit, typed, and bounded without allowing checked condition to inflate into authority, standing, or semantic source.

## 3. Why a Validator Contract Is Needed

Validation needs a bounded runtime contract.

- If validation is not contract-bounded, it can collapse into generic `checks passed` behavior, convenience flags, or narrative interpretation.
- Generic `checks passed` is insufficient because IAMMAI requires checking to remain typed by validation kind, target relation, condition-set relation, and outcome.
- Validation must remain typed in motion because the live system needs to show what was checked, against what, and with what result before later movement or force depends on it.
- This contract protects against premature standing and unlawful transition by keeping validation explicit rather than letting admissibility, threshold, legality, or precondition checks dissolve into generic runtime approval.

## 4. What the Validator Governs

At a high level, the Validator governs:

- admissibility checks
- threshold checks
- transition legality checks
- governance precondition checks
- bounded consistency checks

It governs condition checking.

It does not govern lawful force or semantic source. It does not decide that a checked condition automatically becomes governance action, canonical state, or standing truth.

## 5. Validator Inputs

At a high level, the Validator may receive:

- candidate material
- target references
- condition-set references
- transition requests
- state-relevant inputs
- governance precondition requests
- scope or matter references where relevant

These are contract-bounded runtime inputs to checking. They are not blank permission to authorize action or move state by themselves.

## 6. Validator Outputs

At a high level, the Validator may emit or produce:

- validation artifacts
- typed outcomes
- target relations
- rule or condition-set references
- optional reason references
- outputs that may later be witnessed or preserved

Validator outputs are not governance acts.  
Validator outputs are not witness artifacts.  
Validator outputs do not automatically create standing state.

They are bounded checking results that later runtime components may depend on within their own lawful roles.

## 7. Dependencies and Relations

### 7.1 State Engine

The State Engine depends on lawful checks where state movement requires them, but the State Engine is not validation. Validation checks whether required conditions hold before certain movement may proceed.

### 7.2 Witness Emitter

The Witness Emitter may preserve validation events as trace, but witness is not validation. Validation checks conditions; witness preserves that the checking event occurred.

### 7.3 Governor

The Governor may depend on validation where bounded checks are required, but governance is not validation. Passed validation does not itself authorize, deny, hold, release, finalize, invalidate, or evolve.

### 7.4 Registry / Store

The Registry / Store preserves validation artifacts and related trace, but the registry is not validation. Preservation is not the same thing as checking.

### 7.5 Interface Gateway

The Interface Gateway may route inputs toward validation where validation is required, but interface is not validation. Receipt of input does not count as validation outcome.

## 8. What the Validator Must Preserve

At minimum, the Validator must preserve:

- bounded condition context
- target relation
- typed outcomes
- non-collapse between validation types
- separation between validation and authorization
- visible failure where validation does not pass

This means, in practical runtime terms:

- admissibility must remain distinct from threshold
- threshold must remain distinct from truth
- transition legality must remain distinct from governance authorization
- governance precondition checking must remain distinct from governance action
- blocked, failed, and indeterminate results must remain visible where they matter

## 9. What the Validator Must Not Absorb

The Validator must not become:

- governor
- witness
- semantic source
- state engine
- registry
- interface logic

It must not silently reinterpret constitutional meaning.

The Validator keeps checking explicit and bounded. It does not decide lawful force, preserve trace by itself, move canonical state by itself, store canonical history by itself, or define how interfaces present the runtime body.

## 10. Contract Boundaries in Motion

Validation is expected before movement or action where constitutional checking is required.

Before validation runs, the relevant target, matter or scope relation, and condition-set context must already be present in bounded form.

Outside validator scope remain:

- lawful force as governance
- state movement as state-engine handling
- trace preservation as witness
- durable preservation as registry
- interaction routing and display as interface

After validation completes, its typed output must be handed off to the appropriate runtime participants for preservation, witnessing, governance dependence, or state-handling dependence where applicable.

## 11. Failure / Refusal Posture

When conditions do not pass, the Validator must be understood in bounded terms.

- failure must remain typed
- failure must remain preservable
- failed validation must not silently disappear
- failed validation must not be mistaken for governance denial by default
- indeterminate or blocked cases must remain distinguishable where relevant

Non-passage may prevent later movement or action, but it remains validation output rather than governance refusal unless governance later acts in its own role.

## 12. Anti-Collapse Rules

A conforming Validator contract must not allow:

- validation to silently become governance
- validation to silently become witness
- a pass result to be treated as automatic authorization
- failed validation to disappear into generic logs
- validation to detach from target or condition context
- generic check results to replace typed validation outcomes
- validation bypass where constitutional checking is required

## 13. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact execution semantics
- synchronous or asynchronous ordering
- retry behavior
- batching behavior
- distributed coordination implications
- finer-grained validator engine logic

These are runtime-design questions, not constitutional ambiguities.

## 14. Summary

This document defines the first runtime contract for the Validator as the bounded runtime role that keeps admissibility, threshold, legality, governance-precondition, and consistency checking explicit before later movement or force depends on it.

Its purpose is to make clear how the Validator acts within the IAMMAI body without allowing it to absorb witness, governance, state-engine, registry, or interface roles.

**One-Line Definition:** `VALIDATOR_CONTRACT.md` defines the first bounded runtime contract of the IAMMAI Validator as the keeper of typed condition checking in motion without becoming witness, governor, state engine, registry, or interface.
