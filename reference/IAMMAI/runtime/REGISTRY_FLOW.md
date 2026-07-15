# IAMMAI Registry Flow

## 1. Purpose

This file defines the first runtime-specific flow of the Registry / Store inside the IAMMAI body.

Its job is to explain when records enter the registry, what kinds of things the registry preserves, what makes a record canonical rather than derivative, how registry flow relates to state, transition, witness, validation, and governance, and what the registry must not become while the body is in motion.

It does not yet try to define:
- code
- database design
- storage vendor selection
- infrastructure topology
- replication strategy
- service topology

It is a bounded runtime-flow document focused on registry behavior.

## 2. First Principle

The registry preserves canonical records.

The registry serves the constitutional core.  
The registry preserves reconstructable history.  
The registry does not become semantic source by itself.  
The registry does not become interpretation engine.  
The registry does not replace governance, validation, witness, or state engine.

In runtime terms, the registry is the authoritative preservation surface through which protocol-relevant records become durable without storage convenience redefining what those records mean.

## 3. Why Registry Flow Matters

Runtime preservation must be explicit.

- If canonical records are not preserved explicitly, they can disappear into convenience storage, cache state, generic logs, or later summaries.
- Canonical records must not disappear into convenience storage because the body needs more than present display state. It needs preservable state, trace, action, and lineage.
- Reconstructable history matters because IAMMAI distinguishes what stands, what changed, what was checked, what was witnessed, who acted, and how succession occurred.
- Append-oriented preservation is important for anti-collapse integrity because silent overwrite, ambiguous replacement, and storage-level mutation can erase the difference between lawful succession and convenience rewrite.

Registry flow is therefore one of the runtime protections against historical collapse.

## 4. What the Registry Preserves

At a high level, the registry may preserve the main canonical record families, including:

- state records
- transition records
- governance action records
- witness artifacts
- validation artifacts
- contribution records where relevant
- lineage relations and references

These are preserved as typed canonical records, not as one generic storage blob.

The registry does not decide what these records mean by itself. It preserves them in authoritative runtime form so they remain reconstructable over time.

## 5. What Makes a Record Canonical

Canonical records are records that preserve protocol-relevant truth, lawful action, lineage, or bounded trace in the authoritative runtime body.

In practical terms, a record is canonical when it preserves one or more of the following in protocol-relevant form:

- what state stood
- what lawful transition occurred
- what governance act applied lawful force
- what validation checked and with what outcome
- what witness contact was preserved
- what lineage relation connects lawful succession

Derivative exports, views, analytics, summaries, mirrored displays, and display caches are not canonical by default.

The registry preserves canonical records. It does not merely mirror presentation surfaces.

## 6. Registry Relation to Other Runtime Components

### 6.1 State Engine

The State Engine produces state and transition consequences that may be preserved in the registry, but the registry is not the State Engine. The State Engine applies lawful movement; the registry preserves its resulting canonical records.

### 6.2 Validator

The Validator produces validation artifacts that may be preserved in the registry, but the registry is not validation. It preserves bounded checking output; it does not perform the checking.

### 6.3 Witness Emitter

The Witness Emitter produces witness artifacts that may be preserved in the registry, but the registry is not witness. It preserves bounded trace; it does not become the witnessing act.

### 6.4 Governor

The Governor produces governance actions that may be preserved in the registry, but the registry is not governance. It preserves attributable lawful force; it does not become the force-bearing actor.

### 6.5 Interface Gateway

The Interface Gateway may read from or route toward registry-backed truth, but interface is not the registry itself. Interface presents and routes; the registry preserves authoritative records.

## 7. Registry Flow Sequences

### 7.1 State Preservation Flow

1. Lawful state handling occurs through the State Engine.
2. A canonical state record is produced or updated through lawful succession handling.
3. The registry preserves that state record with its matter relation and related references where applicable.
4. The preserved state becomes part of reconstructable canonical history.

State preservation must not collapse into display status or convenience cache.

### 7.2 Transition Preservation Flow

1. A lawful transition occurs in relation to protocol state movement.
2. A transition record is produced with source, target, matter, and typed transition relation.
3. The registry preserves the transition record and related lineage references where applicable.
4. The preserved transition becomes part of reconstructable change history.

Transition preservation must not collapse into generic update logging.

### 7.3 Witness Preservation Flow

1. Witnessable contact occurs in runtime.
2. The Witness Emitter emits a witness artifact with bounded claims and non-claims.
3. The registry preserves that witness artifact with target relation and related references where applicable.
4. The preserved witness trace remains available for later reconstruction without becoming governance or semantic source.

### 7.4 Validation Preservation Flow

1. The Validator performs a bounded check.
2. A validation artifact is produced with validation type, target relation, condition-set relation, and outcome.
3. The registry preserves the validation artifact as typed checking trace.
4. The preserved validation output remains distinct from any later governance or state movement.

### 7.5 Governance Preservation Flow

1. The Governor performs or authorizes a protocol-significant act.
2. A governance action record is produced with actor relation, authority class, legitimacy basis, matter scope, and action type.
3. The registry preserves that governance action record and related references where applicable.
4. The preserved governance trace remains attributable and reconstructable over time.

## 8. Registry vs Derivative Surfaces

The registry preserves canonical records.

Websites, dashboards, exports, analytics, summaries, mirrored views, and convenience APIs are derivative unless explicitly typed otherwise within a bounded authoritative role.

Display must not replace canonical history.  
Cache must not silently become source of truth.

Derivative surfaces may expose registry-backed truth, summarize it, or route toward it, but they do not replace the canonical records preserved in the registry.

## 9. Registry and Lineage

Predecessor and successor relation must remain recoverable because lawful succession depends on explicit relation rather than guesswork.

- Silent overwrite is non-conformant because it erases how one state or record succeeded another.
- Canonical preservation must support reconstructable history across state, transition, and governance-relevant change.
- Lineage cannot be left to timestamp guessing, naming similarity, or report reconstruction.

The registry is therefore one of the main runtime surfaces through which lineage becomes durable rather than merely asserted.

## 10. Failure / Absence Posture

When registry write or preservation fails, runtime handling must remain explicit.

- Failure to preserve a canonical record must not disappear silently.
- Missing preservation must remain visible where canonical recording is required.
- Registry absence or failure is not the same thing as interpretation failure; it is a preservation failure.

If canonical preservation does not occur, later display, export, analytics, or cached state must not behave as though canonical durability had already been achieved.

## 11. Anti-Collapse Rules

A conforming registry flow must not allow:

- canonical records to be silently overwritten in place
- derivative views to be treated as registry truth
- analytics to be treated as canonical history
- generic logs to replace typed canonical records
- lineage to be lost because storage convenience flattened references
- the registry to act as interpretation engine
- the registry to be treated as governance or witness by itself

## 12. What Remains Open

The following remain intentionally open for later runtime derivation:

- append-only enforcement mechanism
- replication and distribution strategy
- synchronous or asynchronous persistence behavior
- retention policy
- storage partitioning
- canonical replica strategy

These are runtime-design questions, not constitutional ambiguities.

## 13. Summary

This document defines the first runtime-specific flow of the Registry / Store as the bounded preservation path through which canonical state, transition, governance, witness, validation, contribution, and lineage records become durable in the IAMMAI body.

Its purpose is to keep canonical history reconstructable in motion without allowing storage, display, analytics, or convenience surfaces to replace authoritative preservation.

**One-Line Definition:** `REGISTRY_FLOW.md` defines the first bounded runtime flow of the IAMMAI Registry / Store as the authoritative preservation of canonical records and lineage in motion without collapsing into interpretation, analytics, or display state.
