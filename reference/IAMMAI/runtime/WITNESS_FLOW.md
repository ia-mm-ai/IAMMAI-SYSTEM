# IAMMAI Witness Flow

## 1. Purpose

This file defines the first runtime-specific flow of the Witness Emitter inside the IAMMAI body.

Its job is to explain when witness is emitted, what kinds of contact it preserves, what witness flow produces, what witness must not claim, and how witness relates to the other runtime participants while the body is in motion.

It does not yet try to define:
- code
- a full witness ecology design
- surveillance logic
- API contracts
- service topology
- infrastructure behavior

It is a bounded runtime-flow document focused on witness behavior.

## 2. First Principle

Witness preserves contact.

Witness emits bounded trace.  
Witness does not become semantic source.  
Witness does not become governance.

Witness must preserve claims and non-claims explicitly so runtime trace remains reconstructable without inflating into authorship, authority, standing state, or lawful force.

## 3. Why Witness Flow Matters

Contact should not remain vapor.

- If runtime contact is not preserved where it matters, later reconstruction can collapse into memory, summary, or cosmetic substitution.
- Witness must exist in runtime motion, not only in schema, because contact and observation arise while the body is live.
- Witness helps prevent disappearance, flattening, and cosmetic substitution by preserving that something was encountered, observed, checked, registered, or emitted in relation to protocol state.
- Witness must remain bounded in claim because preserved contact is not the same thing as semantic source, governance force, or automatic standing creation.

Witness flow is therefore one of the body’s runtime protections against silent disappearance.

## 4. Witness Inputs / Trigger Points

At a high level, witness flow may be invoked at moments such as:

- inbound interaction or contact
- a validation event
- a governance event
- a state observation
- a transition occurrence
- a publication or release surface where bounded trace matters

These are witness trigger points, not proof that witness becomes the thing it preserves.

## 5. What Witness Flow Preserves

Witness flow may preserve:

- interaction contact
- observed relation to state
- validation trace
- governance trace
- transition trace
- bounded publication trace

Witness preserves contact.  
Witness does not create standing by itself.

Its runtime job is to keep relevant contact and occurrence reconstructable without becoming the source of truth for what the contact ultimately means.

## 6. Witness Outputs

Witness flow produces witness output in bounded form.

At minimum, that output should preserve:
- a witness artifact
- target relation
- witness type
- claims
- non-claims
- observed_at
- optional related references such as validation, transition, governance, scope, or surface

Witness output is not semantic source.  
Witness output is not lawful force.  
Witness output is not authorship by default.

It remains bounded trace of contact or observed relation.

## 7. Witness Relation to Other Runtime Components

### 7.1 Interface Gateway

The Interface Gateway may trigger witnessable contact, but interface is not witness. It receives and presents interaction; the Witness Emitter preserves bounded trace where that interaction should not disappear.

### 7.2 Validator

The Validator may produce events that are witnessed, but validation is not witness. Validation checks conditions; witness preserves that checking occurred.

### 7.3 Governor

Governor actions may be witnessed, but governance is not witness. Governance applies lawful force; witness preserves trace that the event occurred.

### 7.4 State Engine

The State Engine may change state that becomes witnessed, but state is not witness. State movement and observed contact remain distinct runtime roles.

### 7.5 Registry / Store

The Registry / Store preserves witness artifacts, but storage is not witness itself. Preservation is not the same thing as emitting bounded trace.

## 8. Witness Flow Sequences

### 8.1 Interaction-Contact Witness Flow

1. The Interface Gateway receives bounded contact or interaction.
2. The Witness Emitter determines whether that contact should be preserved as witness trace.
3. A witness artifact is emitted with target relation, witness type, claims, non-claims, and observed time.
4. The Registry / Store preserves the witness artifact as authoritative trace.

This does not by itself create standing state or authorization.

### 8.2 Validation-Event Witness Flow

1. The Validator performs bounded checking.
2. A validation event occurs in runtime.
3. The Witness Emitter may preserve that event as witness trace without replacing the validation artifact itself.
4. The Registry / Store preserves both validation and witness outputs as distinct records.

Witnessed validation is still not witness authority over validation outcome.

### 8.3 Governance-Event Witness Flow

1. The Governor performs or authorizes a protocol-significant act.
2. The Witness Emitter may preserve that governance event as witnessed occurrence.
3. A witness artifact is emitted with bounded claims and explicit non-claims.
4. The Registry / Store preserves governance trace and witness trace separately.

Witnessed governance is still not governance force.

### 8.4 Transition Witness Flow

1. A lawful transition occurs or is emitted in relation to state movement.
2. The Witness Emitter may preserve that transition-relevant occurrence.
3. A transition witness artifact is emitted with target relation and bounded claims.
4. The Registry / Store preserves transition and witness trace as distinct but related records.

Witnessed transition is still not the transition itself.

### 8.5 Publication / Release Witness Flow

1. A bounded publication or release surface emits protocol-relevant exposure.
2. The Witness Emitter determines whether that exposure should remain reconstructable as publication trace.
3. A witness artifact is emitted with bounded publication-oriented claims and non-claims.
4. The Registry / Store preserves the resulting witness trace.

This preserves that publication or release contact occurred without treating publication as semantic source.

## 9. Claims and Non-Claims in Motion

In runtime flow, witness may claim things such as:

- contact occurred
- observation occurred
- registration occurred
- bounded interaction was preserved
- a validation event was observed
- a transition-relevant event was observed

In runtime flow, witness must explicitly not claim things such as:

- authorship
- semantic source
- final authority
- automatic truth creation
- governance force

These non-claims are part of the witness role, not decorative schema detail. Without them, witness trace becomes structurally easy to misread as authority, authorship, or lawful force.

## 10. Failure / Absence Posture

When witness is absent, blocked, or not emitted, runtime handling must remain honest about that absence.

- Witness absence must not silently pass as if trace existed.
- Failure to emit witness should remain visible where witness is constitutionally important for reconstructability.
- Witness failure is not equivalent to governance failure, but it may still matter for historical integrity and later reconstruction.

The body must therefore preserve the difference between no witness emitted, witness emission attempted but failed, and witness trace successfully preserved where those distinctions matter in runtime derivation.

## 11. Anti-Collapse Rules

A conforming witness flow must not allow:

- witness to silently become semantic source
- witness to silently become governance
- witness to silently become validation
- generic logging to pretend to be witness
- witness to be emitted without bounded claims and non-claims
- witness to disappear into derivative analytics only
- witness to be treated as proof of authorship or authority
- witness trace to overwrite the events it merely preserves

## 12. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact emission timing
- synchronous or asynchronous behavior
- batching or deduplication
- retry semantics
- distributed witness ecology
- signature or hash strategy in motion

These are runtime-design questions, not constitutional ambiguities.

## 13. Summary

This document defines the first runtime-specific flow of the Witness Emitter as the bounded trace path through which interaction, validation, governance, transition, and publication-related contact may be preserved while the body is live.

Its purpose is to keep contact reconstructable in motion without allowing witness to become semantic source, governance, validation, or authorship.

**One-Line Definition:** `WITNESS_FLOW.md` defines the first bounded runtime flow of the IAMMAI Witness Emitter as the emission of claim-limited trace in motion so contact does not disappear without witness becoming authority or force.
