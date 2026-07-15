# IAMMAI Witness Artifact Overview

## 1. Purpose

This file defines the first high-level witness artifact model of IAMMAI in implementation-facing form.

It translates the constitutional core and the current architecture and implementation documents into a bounded view of what a witness artifact is, what it preserves, and how it remains distinct from validation, governance, and semantic source.

It does not yet try to define:
- code
- a final schema
- a full witness ecology
- storage design
- transport design
- a final runtime topology

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

Witness preserves contact.

Witness does not become semantic source.  
Witness does not become governance.

A witness artifact must preserve claims and non-claims explicitly so that preserved trace remains bounded in meaning and does not silently inflate into authorship, authority, or standing state.

## 3. Why Witness Artifacts Are Needed

Observed contact should not remain vapor.

- If contact, observation, registration, or state-relevant occurrence is not preserved as trace, it can disappear into later summary, memory, or interpretation.
- Witness matters for anti-erasure because it preserves that something was encountered, checked, or observed even when witness is not itself the final authority over what stood.
- Witness must be preservable as trace so later reconstruction does not depend on narrative recall alone.
- Witness must remain bounded in claim because preserved contact is not the same thing as semantic source, lawful force, or automatic truth creation.

Witness artifacts therefore help the system say that something did not simply vanish, without pretending that witness alone decides what stands.

## 4. What Witness Is

In implementation terms, witness is:

- a trace-preserving role
- a bounded attestation role
- a lawful carrier of preserved contact

Witness is not:

- authorship
- final authority
- semantic source
- governance by default

Witness preserves relation to occurrence. It does not, by itself, create standing state, authorize protocol-significant action, or redefine constitutional meaning.

## 5. What a Witness Artifact Preserves

At a high level, a witness artifact should preserve:

- witness id
- target ref
- witness type
- observed_at
- claims
- non-claims
- optional actor references where applicable
- optional surface references where applicable
- optional scope references where applicable

This is a conceptual record shape, not a final schema.

The implementation point is that a witness artifact should preserve enough typed trace to reconstruct what kind of contact was preserved, what it pointed at, when it was observed, and what it did and did not claim.

## 6. Claims and Non-Claims

Witness artifacts must preserve both.

### 6.1 What a Witness Artifact May Claim

A witness artifact may claim, within bounded scope, that:

- contact occurred
- observation occurred
- registration occurred
- bounded interaction was preserved
- a validation event was observed
- a transition-relevant event was observed

These are witness claims about preserved contact or occurrence.

### 6.2 What a Witness Artifact Must Explicitly Not Claim

A witness artifact must make clear non-claims such as:

- not authorship
- not semantic source
- not final authority
- not automatic truth creation
- not governance force

This boundary matters because witness without non-claims becomes structurally easy to misread as authority.

## 7. Witness Types

A first bounded witness-type family may include:

### 7.1 Interaction Witness

Preserves that a bounded interaction occurred between an actor or surface and the runtime body.

### 7.2 Validation Witness

Preserves that a validation event occurred, without turning witness into the validation result itself.

### 7.3 Transition Witness

Preserves that a protocol-relevant transition event was observed or emitted in relation to state change.

### 7.4 Publication Witness

Preserves that a bounded publication event occurred in relation to a protocol artifact or state exposure.

### 7.5 State-Observation Witness

Preserves that a protocol-relevant state observation occurred on a bounded surface.

This family is intentionally small. It is enough to orient the first implementation body without becoming a full witness-ecology model.

## 8. Witness vs Validation

Witness preserves contact.  
Validation preserves condition checking.

A validation event may emit witness trace, but witness and validation remain distinct.

- Witness preserves that something was checked, observed, or registered.
- Validation preserves what condition set was checked and with what outcome.
- Witness may point to validation.
- Witness does not replace validation output.
- Validation does not absorb witness simply because a validation act produced trace.

## 9. Witness vs Governance

Witness preserves trace.  
Governance performs lawful force.

By default, witness cannot:

- finalize
- invalidate
- evolve
- hold
- release
- authorize protocol-significant action

Governance action may itself be witnessed, but witness does not become governor by preserving governance trace.

Likewise, a governance record does not replace witness simply because governance occurred.

## 10. Witness and Lineage

Witness supports reconstructability.

- Witness helps preserve that a contact, observation, or interaction related to state change did not silently disappear.
- Witness strengthens the historical integrity of state change by preserving bounded trace alongside state, transition, and governance records.
- Witness helps later reconstruction of what was encountered or observed around a change.

Witness is still not the same thing as lineage itself.

Lineage preserves predecessor / successor and transition relation. Witness preserves contact with occurrence. These support one another, but they do different jobs and must remain typed apart.

## 11. Witness Surfaces

Witness may be emitted across multiple bounded surfaces, including:

- runtime interaction
- validation event
- state transition
- publication event
- machine-readable trace surface

This does not define a full witness ecology. It only marks the main places where witness artifacts may lawfully arise in the first implementation body.

## 12. Anti-Collapse Rules

A conforming implementation must not allow:

- witness to be treated as semantic source
- witness to be treated as governance
- witness to be treated as authorship
- witness artifact to exist without non-claim boundary
- witness to flatten into generic logs
- witness to disappear into derivative analytics only
- validation success to be restated as witness authority
- governance action to overwrite or launder witness trace

## 13. Open Questions

The following remain open in technical derivation:

- the final witness artifact envelope
- whether witness is append-only by architecture or by infrastructure
- how much witness-type granularity is needed in the first runtime
- how public or replicated witness surfaces are classified
- whether hash or signature fields are required by default

These are implementation questions, not constitutional ambiguities.

## 14. Summary

This document defines the first implementation-facing witness artifact model of IAMMAI as a bounded trace model for preserved contact.

Its purpose is to keep observation, registration, and interaction reconstructable without collapsing witness into validation, governance, or semantic source.

**One-Line Definition:** `WITNESS_ARTIFACT_OVERVIEW.md` defines the first high-level implementation view of IAMMAI witness artifacts as bounded, claim-limited records that preserve contact without becoming authority, governance, or semantic source.
