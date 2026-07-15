# IAMMAI Registry Failures

## 1. Purpose

This file defines the first runtime-specific failure model for registry preservation in IAMMAI.

Its job is to explain what it means for canonical preservation not to occur, to fail, to be incomplete, or to be unavailable, how registry failure differs from validation failure, witness failure, governance non-progression, or state-engine non-movement, what must remain visible when canonical preservation does not occur where it is constitutionally required, what registry failure does and does not imply, and what must never be cosmetically substituted or silently dropped.

It does not yet try to define:
- code
- incident response
- storage vendor selection
- infrastructure topology
- transport mechanics
- recovery procedures

It is a bounded runtime document focused on registry preservation failure as an architectural integrity concern.

## 2. First Principle

Failure to preserve canonical record must remain typed where constitutionally relevant.

Missing canonical preservation must not silently masquerade as preserved truth.  
Registry failure handling must serve the constitutional core, not convenience.  
Derivative surfaces must not substitute for missing canonical preservation.

In runtime terms, that means the body must preserve when canonical durability did not occur, what record or relation was affected, and what later surfaces must not pretend in its absence.

## 3. Why Registry Failures Matter

Canonical preservation is part of constitutional integrity.

- Reconstructable history depends on preservation actually occurring rather than merely being assumed.
- If canonical records are not durably preserved, the runtime can still appear continuous while authoritative history is in fact missing, incomplete, or unavailable.
- Generic `save failed` language is not enough because registry preservation concerns typed canonical record families, lineage relation, and authoritative versus derivative distinction.
- Silent registry failure creates semantic corruption and false continuity by letting dashboards, exports, caches, or convenience views look like canonical history when canonical preservation did not occur.

## 4. Main Registry Failure Families

The main registry-failure families include:

- canonical record not written
- canonical record written incompletely
- lineage reference not preserved
- typed record preserved as generic log only
- canonical record unavailable after expected preservation
- preservation blocked or indeterminate
- derivative surface visible while canonical preservation failed

These families should remain typed apart. They are not one generic storage error condition.

## 5. Registry Failure vs Other Non-Progression

Registry failure is not the same thing as every other non-progression surface.

- registry failure does not equal validation failure
- registry failure does not equal witness failure
- registry failure does not equal governance denial or hold
- registry failure does not equal state-engine non-movement
- a lawful event may have occurred even if its canonical preservation failed
- preservation failure damages reconstructability and continuity, not semantic source by itself

This distinction matters because the runtime must not collapse failed preservation into failed checking, missing witness, denied governance, or absent state movement.

## 6. What Must Remain Visible

When canonical preservation does not occur as required, the runtime must preserve at least:

- what canonical record or record family was expected
- what matter, state, transition, governance, witness, or validation relation it applied to
- whether preservation failed, was incomplete, was blocked, or was indeterminate
- when the preservation failure occurred
- what derivative surfaces must not pretend in its absence

Generic disappearance into logs is not acceptable. Registry failure must remain visible as typed preservation non-passage rather than dissolving into omission, convenience status, or later display continuity.

## 7. Relation to Runtime Components

### 7.1 Interface Gateway

The Interface Gateway may still show something, but it must not silently replace missing canonical preservation with display continuity, cached state, or convenience summaries.

### 7.2 Validator

Validation may have occurred even if registry preservation failed. Registry failure is a preservation failure, not automatic nullification of the validation event or its typed output.

### 7.3 Witness Emitter

Witness may have emitted trace even if canonical witness preservation later failed. Missing registry durability must not be restated as though witness never occurred, and witness trace itself must not substitute for registry success.

### 7.4 Governor

Governance may have acted even if governance record preservation later failed. Registry failure is not governance refusal, denial, or absence of lawful force by itself.

### 7.5 State Engine

State movement may have occurred even if state or transition records were not canonically preserved. Upstream components must not assume preservation happened when it did not.

## 8. Registry Failure Sequences

### 8.1 State Movement Occurred but State Record Was Not Canonically Preserved

1. The State Engine performs lawful state handling.
2. A state record should enter canonical preservation.
3. Preservation does not occur.
4. The preservation failure remains visible, and derivative views must not pretend durable canonical state history exists.

### 8.2 Governance Action Occurred but Governance Record Preservation Failed

1. The Governor performs or authorizes a protocol-significant act.
2. A governance action record should enter canonical preservation.
3. Preservation fails or remains incomplete.
4. The missing preservation remains visible rather than being replaced by interface or analytics summaries.

### 8.3 Witness Artifact Emitted but Canonical Witness Preservation Failed

1. The Witness Emitter emits a witness artifact.
2. The witness artifact should be canonically preserved.
3. Canonical preservation fails or becomes unavailable.
4. The runtime must distinguish emitted witness from durably preserved witness.

### 8.4 Transition Record Partially Preserved Without Lineage Relation

1. A transition record is produced.
2. Preservation occurs only partially, without required lineage relation.
3. The incompleteness remains visible.
4. Partial storage must not be treated as complete canonical preservation.

### 8.5 Derivative UI / Export Visible While Canonical Record Write Failed

1. A runtime event occurs and derivative surfaces display or export related information.
2. Canonical preservation did not occur.
3. The derivative surface remains derivative.
4. It must not be treated as substitute registry truth.

## 9. Anti-Collapse Rules

A conforming runtime must not allow:

- missing canonical preservation to be treated as if canonical record exists
- derivative views to be treated as registry truth
- analytics or exports to substitute for canonical preservation
- incomplete canonical preservation to be masked as completeness
- lineage loss to be flattened into generic storage success
- registry failure to rewrite runtime non-passage into apparent continuity

## 10. What Remains Open

The following remain intentionally open for later runtime derivation:

- exact retry semantics
- append-only enforcement strategy
- replica and synchronization behavior
- durability thresholds
- operator-facing messaging for registry failure
- recovery or audit strategies after failed preservation

These are runtime-design questions, not constitutional ambiguities.

## 11. Summary

This document defines the first runtime-specific failure model for registry preservation in IAMMAI as a bounded account of missing, incomplete, blocked, indeterminate, or unavailable canonical records and relations.

Its purpose is to keep preservation failure visible and reconstructable so the runtime does not cosmetically rewrite missing canonical durability into apparent continuity, stored truth, or derivative replacement.

**One-Line Definition:** `REGISTRY_FAILURES.md` defines the first bounded runtime model of IAMMAI registry failures as typed, visible non-passage of canonical preservation that must remain reconstructable rather than being smoothed into apparent continuity or substitute truth.
