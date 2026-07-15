# IAMMAI Canonical Records Overview

## 1. Purpose

This file defines the first high-level record model of IAMMAI in implementation-facing form.

It translates the published constitutional core and the current architecture and implementation documents into a bounded view of the canonical record families the implementation body must preserve.

It does not yet try to define:
- code
- schemas
- database tables
- storage engines
- indexing strategy
- vendor choices
- a final database design

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

The record model serves the law.

Records must preserve constitutional distinctions rather than flatten them for storage convenience. The constitutional core remains the semantic source of truth, and the record model exists to preserve what stands, what changed, what was checked, what was witnessed, who acted, and how succession occurred without semantic collapse.

A conforming implementation must not reduce state, transition, witness, governance, contribution, and lineage into one generic record family.

## 3. Why Canonical Records Are Needed

State alone is not enough.

- Current state can show what now stands, but it does not by itself preserve how that state was reached, under what authority, with what validation, or through what successor relation.
- Trace must be typed because not every preserved fact is the same kind of fact. Governance action, witness trace, validation output, contribution role, and lineage relation do different jobs.
- Distinct record families are required so lawful transition, attributable action, preserved contact, and traceable succession can be reconstructed without guesswork.
- Generic logs are insufficient because they flatten typed resolution, hide legitimacy basis, blur contribution roles, and make lineage or record provenance recoverable only by interpretation.

Canonical records are therefore part of the minimum lawful body, not an implementation afterthought.

## 4. Core Record Families

### 4.1 State Records

- Preserve: what currently stands in protocol-relevant form, including preparation-state, standing-state, containment, and resolved state forms.
- Are not: generic event history or display status.
- Must remain distinct because: state meaning cannot be reconstructed from undifferentiated mutation logs alone.

### 4.2 Transition Records

- Preserve: lawful movement between protocol-relevant states.
- Are not: anonymous write events or generic status changes.
- Must remain distinct because: change must remain reconstructable as transition, not merely as before/after surface difference.

### 4.3 Resolution Records

- Preserve: typed resolution as FINALIZE, INVALIDATE, or EVOLVE, together with the state relation it acts upon.
- Are not: generic closure markers or update flags.
- Must remain distinct because: resolution family is closed and constitutionally typed.

### 4.4 Governance Action Records

- Preserve: attributable protocol-significant action, including authority class, legitimacy basis, matter relation, and act identity.
- Are not: semantic source or anonymous mutation.
- Must remain distinct because: lawful force must remain bounded, attributable, and reconstructable.

### 4.5 Contribution Role Records

- Preserve: distinct semantic participation roles in material, including role type and relation to matter, actor, and artifact where relevant.
- Are not: a single undifferentiated authorship field.
- Must remain distinct because: origin, elicitation, formalization, authorization, rendering, and transmission are materially different roles.

### 4.6 Witness Artifacts

- Preserve: bounded trace of contact, observation, registration, or witnessed relation to protocol state.
- Are not: governance action, semantic source, or automatic truth creation.
- Must remain distinct because: contact must be preserved without inflating into authority.

### 4.7 Validation Artifacts

- Preserve: bounded condition checking, including target, condition set, outcome, and time of check.
- Are not: governance authorization or semantic source.
- Must remain distinct because: checked condition must remain visible as checking, not be mistaken for force.

### 4.8 Lineage References

- Preserve: predecessor, successor, and transition relation across lawful change.
- Are not: optional notes or inferential convenience.
- Must remain distinct because: lawful succession depends on explicit relation, not narrative reconstruction.

## 5. State Records

State records preserve what currently stands in typed form. They must keep the main state families apart.

### 5.1 Candidate / Preparation-State Records

These records preserve candidate material moving through:
- signal
- acceptance
- scope
- presence
- threshold

They are preparation-state records, not standing state.

Candidate material must not silently become standing state by storage convention, convenience API behavior, or derivative display logic.

### 5.2 Standing-State Records

These records preserve standing state as:
- truth
- continuity
- decision
- consequence

These states are not interchangeable. A conforming implementation must not let truth read as decision, decision read as consequence, or continuity collapse into raw duration or storage persistence.

### 5.3 Containment State

Containment records preserve held and released state in typed form.

Containment is orthogonal. It is not a canonical phase and not a resolution outcome. Record handling must therefore preserve what was held, what was released, and when containment applied without turning HOLD into standing state.

### 5.4 Resolved State

Resolved state must remain typed as finalized, invalidated, or evolved.

Resolved state must not appear as a generic terminal status. The record model must preserve the specific resolution kind and its relation to prior standing state.

## 6. Transition and Resolution Records

Transitions need their own typed records because state alone cannot show how lawful movement occurred.

- A transition record preserves that movement occurred between protocol-relevant states.
- A transition record allows later reconstruction of what changed, on what matter, and in what order.
- A transition record keeps state change from disappearing into undifferentiated mutation.

Resolution records preserve FINALIZE, INVALIDATE, and EVOLVE as typed outcomes.

- FINALIZE closes in current form.
- INVALIDATE removes standing without erasing trace.
- EVOLVE creates lawful successor relation in explicit relation to prior state.

These must not collapse into generic updates such as `updated`, `changed`, or `closed`.

Where EVOLVE occurs, predecessor / successor relation must remain recoverable by explicit reference. Correction enters through successor relation, not in-place replacement.

## 7. Governance Records

Governance records preserve lawful protocol-significant action.

A governance action record must preserve, at minimum, enough information to reconstruct:
- what act occurred
- who acted
- under what authority class
- under what legitimacy basis
- on what matter
- when the act occurred
- what delegation relation applied where relevant

Attribution and legitimacy basis matter because governance is bounded force, not mere access or visibility.

If governance records collapse into anonymous mutation, the system may still change state operationally, but it can no longer show that the change was lawfully governed.

## 8. Contribution Records

Contribution records preserve distinct semantic participation in material.

A contribution role record should preserve, at minimum, the role type and its relation to the relevant matter, actor, artifact, and related governance action where applicable.

The contribution role families that must remain typed are:
- ORIGIN
- ELICITATION
- FORMALIZATION
- AUTHORIZATION
- RENDERING
- TRANSMISSION

`author` alone is insufficient because it collapses materially different semantic roles into one label and makes co-produced material falsely simple.

## 9. Witness and Validation Records

Witness and validation records preserve different kinds of trace and must remain distinct.

### 9.1 Witness

Witness preserves contact.

A witness artifact preserves that something was encountered, observed, checked, or registered in relation to protocol state. It may preserve claims and non-claims, target relation, and time of observation.

Witness is not governance, semantic source, or standing state.

### 9.2 Validation

Validation preserves condition checking.

A validation artifact preserves what was checked, under what condition set or rule reference, with what outcome, and at what time.

Validation is not governance authorization, even when its outcome is authoritative within bounded checking scope.

### 9.3 Separation Rule

Witness and validation must not collapse into governance, and neither may collapse into semantic source.

Witness preserves contact.  
Validation preserves bounded checking.  
Governance applies lawful force.

## 10. Lineage References

Lineage references preserve lawful succession explicitly.

### 10.1 Predecessor Reference

Identifies what prior state a current state explicitly succeeds or depends on.

### 10.2 Successor Reference

Identifies what later state succeeded the prior state.

### 10.3 Transition Reference

Identifies the lawful movement between two protocol-relevant states.

### 10.4 Lineage Rule

Explicit lineage reference is required because lawful succession must not be recoverable only by timestamps, naming, or narrative guesswork.

Where successor creation occurs, predecessor / successor relation is part of the canonical record model.

## 11. Authoritative vs Derivative Relation

Canonical records are the records preserved by the authoritative runtime and persistence layers in support of constitutional meaning and lawful reconstruction.

This includes, in their proper bounded scope:
- state records
- transition records
- resolution records
- governance action records
- contribution role records
- witness artifacts
- validation artifacts
- lineage references

Derived outputs may include:
- exports
- reports
- analytics
- dashboards
- mirrored views
- convenience endpoints

These may expose canonical records, summarize them, or route toward them, but they do not replace canonical records as the authoritative basis of state, trace, or history.

## 12. Anti-Collapse Rules

A conforming implementation must not allow:

- state and record families to collapse into one generic blob or event log
- candidate material to be stored as if it were standing state
- generic update markers to replace FINALIZE / INVALIDATE / EVOLVE
- silent overwrite to replace typed succession
- governance to collapse into anonymous mutation
- witness to be treated as governance or semantic source
- validation success to be treated as automatic authorization
- contribution roles to collapse into one authorship field
- lineage to be recoverable only by guesswork
- derivative exports, reports, or analytics to be treated as canonical truth

## 13. Open Questions

The following remain open in technical derivation:

- the exact envelope or serialization shape of the main record families
- whether some record families share a common store or remain physically separated
- whether witness artifacts require hash or signature fields by default
- how derivative replicas and exports declare staleness and source priority

These are implementation questions, not constitutional ambiguities.

## 14. Summary

This document defines the first implementation-facing record model of IAMMAI as a typed set of canonical record families for state, transition, resolution, governance, contribution, witness, validation, and lineage.

Its purpose is to keep what stands, what changed, who acted, what was checked, and how succession occurred reconstructable without semantic collapse.

**One-Line Definition:** `CANONICAL_RECORDS_OVERVIEW.md` defines the first high-level implementation view of the typed record families IAMMAI must preserve so state, transition, governance, contribution, witness, validation, and lineage remain reconstructable in lawful form.
