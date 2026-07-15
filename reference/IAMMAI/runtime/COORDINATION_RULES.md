# IAMMAI Coordination Rules

## 1. Purpose

This file defines the first runtime coordination rules for IAMMAI.

Its job is to explain how runtime parts coordinate without collapsing roles, what lawful coordination means, what must already be true before one part hands off to another, what coordination must preserve, and what coordination must never silently absorb or skip.

It does not yet try to define:
- code
- orchestration software design
- event bus design
- infrastructure topology
- transport semantics
- queue or buffer strategy

It is a bounded runtime coordination document.

## 2. First Principle

Coordination must serve the constitutional core.

Coordination must preserve role separation.  
Handoff is lawful only if the receiving and sending roles remain typed.  
Coordination must not silently create truth, authority, or continuity by convenience.

In runtime terms, coordination is lawful only when a bounded output from one runtime role is handed to another runtime role without changing what that output is, what it means, or what it is allowed to do next.

## 3. Why Coordination Rules Are Needed

Flows and contracts are not enough by themselves.

- Flow documents explain motion.
- Contract documents explain role boundaries.
- Coordination rules explain how bounded outputs move between those roles without semantic collapse.

Runtime parts need lawful coordination because validation, witness, governance, state handling, preservation, and interface exposure do not occur in isolation.

Untyped handoff produces semantic collapse by making one role appear to authorize another, making preserved trace appear to be source, or making stored records appear to define meaning by themselves.

Coordination is therefore not merely components talking to each other. It is the bounded preservation of typed relation while the runtime body moves.

## 4. Runtime Participants in Coordination

The main runtime participants are:

- Interface Gateway
- Validator
- Witness Emitter
- Governor
- State Engine
- Registry / Store

Each participant coordinates with the others, but none may absorb the role of another through handoff.

## 5. General Coordination Rules

The main runtime coordination rules are:

- no role may silently absorb another role through handoff
- no handoff may imply force or truth that was not typed
- validation does not automatically become governance
- witness does not automatically become source
- registry does not become interpretation
- interface does not become canonical state
- state movement must remain constitutionally bounded

Coordination may carry references, typed outputs, and bounded prerequisites forward.

Coordination must not silently add:
- legitimacy
- authorship
- semantic source
- governance force
- standing state

## 6. Preconditions for Lawful Handoff

A handoff is lawful only when the required bounded context is already present.

At minimum, that means:

- a typed target relation
- a typed matter relation where relevant
- typed role identity of sender and receiver
- the required prior validation where applicable
- the required prior governance where applicable
- visible non-passage where required prerequisites are absent

If a required prerequisite is not present, the handoff must not be cosmetically treated as complete. Missing preconditions must remain visible as blocked, denied, failed, absent, or otherwise non-proceeding in the role to which they belong.

## 7. Handoff Boundaries

Each runtime part may hand off bounded outputs that belong to its role.

- The Interface Gateway may hand off routed input, target relation, matter relation, and request context. It must not hand off canonical meaning by itself.
- The Validator may hand off typed validation outcomes, target relations, condition-set relations, and related references. It must not hand off governance force or standing state.
- The Witness Emitter may hand off witness artifacts, target relations, claims, non-claims, and related references. It must not hand off semantic source, authorship, or governance force.
- The Governor may hand off typed governance actions, legitimacy-bounded action context, and related matter or target references. It must not hand off validation as though it had performed it.
- The State Engine may hand off state movement results, state records, transition references, and lineage-preserving relations. It must not hand off lawful force as though movement authorized itself.
- The Registry / Store may hand off preserved canonical records and retrievable canonical references. It must not hand off interpretation as though preservation defined meaning.

What may be referenced is not always what may be acted upon. A downstream component may depend on a prior typed output without being entitled to reinterpret it.

Outputs must therefore remain typed in motion.

## 8. Coordination by Runtime Family

### 8.1 Validation Coordination

Validation coordinates by supplying typed checks to later runtime roles where those checks are required.

It may constrain governance or state movement. It does not automatically authorize either one.

### 8.2 Witness Coordination

Witness coordinates by preserving contact and occurrence in bounded form around runtime events that should not disappear.

It may refer to validation, governance, state observation, transition, or publication-related events. It does not replace any of them.

### 8.3 Governance Coordination

Governance coordinates by applying lawful force where lawful force is required.

It may depend on prior validation, may later be witnessed, and may precede state movement or preservation. It does not turn prior checks or later records into governance.

### 8.4 State Movement Coordination

State movement coordinates by applying canonical phase order, lawful transition logic, containment orthogonality, typed resolution effects, and lineage-preserving succession.

It may depend on prior validation or governance where required. It does not back-authorize those prerequisites by consequence.

### 8.5 Registry Preservation Coordination

Registry preservation coordinates by durably preserving canonical records and lineage after bounded runtime outputs have been produced.

It may preserve outputs from validation, witness, governance, and state handling. It does not convert preservation into interpretation or force.

## 9. Coordination Anti-Collapse Rules

A conforming runtime must not allow:

- validation to be silently treated as authorization
- witness to be silently treated as governance
- interface output to be treated as canonical state
- registry persistence to be treated as semantic interpretation
- handoff to occur without typed prerequisites
- blocked or failed handoff to be cosmetically rewritten as continuity
- consequence to be inferred where lawful coordination never completed

## 10. Relation to Failure Surfaces

Coordination rules must remain valid not only in success but also in non-passage.

Denied, held, missing, blocked, or failed runtime actions must still preserve coordination truth. A failed handoff does not erase the requirement that sender role, receiver role, prerequisite state, and non-passage type remain visible.

Failure therefore does not remove typed handoff boundaries. It makes them more important.

## 11. What Remains Open

The following remain intentionally open for later runtime derivation:

- synchronous or asynchronous specifics
- transport semantics
- queue or buffer strategy
- distributed ordering issues
- implementation-level retry patterns

These are runtime-design questions, not constitutional ambiguities.

## 12. Summary

This document defines the first runtime coordination rules for IAMMAI as the bounded conditions under which typed outputs may move between interface, validation, witness, governance, state handling, and registry preservation without collapsing their roles.

Its purpose is to keep runtime handoff lawful, typed, and reconstructable so the body does not create truth, authority, or continuity by convenience.

**One-Line Definition:** `COORDINATION_RULES.md` defines the first bounded runtime coordination rules of IAMMAI as the lawful handoff conditions by which distinct runtime roles may coordinate without absorbing one another.
