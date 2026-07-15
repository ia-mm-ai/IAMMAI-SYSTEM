# IAMMAI Continuity Overview

## 1. Purpose

This file defines the first bounded continuity layer for IAMMAI.

Its job is to explain why continuity becomes relevant once the body has moved across multiple runs or turns, how continuity relates to canonical records and registry preservation, what continuity must and must not do, and what the smallest safe first continuity artifact could be.

It does not yet try to define:

- code
- a graph database
- a visualization system
- geometry or SPIRAL formalization
- a final schema
- a sovereign continuity engine

It is a bounded architectural document for the next continuity layer.

## 2. First Principle

Continuity serves the constitutional core.

Continuity sits above canonical preservation, not instead of it.  
Continuity preserves lawful becoming across turns.  
Continuity must not erase, overwrite, or reinterpret canonical artifacts.

In practical terms, continuity depends on preserved canonical records and their lawful relations. It does not create canonical truth by summary, visualization, or later reconstruction convenience.

## 3. Why Continuity Is Needed Now

One run can be preserved by registry alone.

A single run can remain reconstructable from its validation, witness, governance, transition, state, and registry-preserved records without needing an additional cross-turn layer.

Repeated runs begin to create a different question.

Once the body has actually moved across multiple runs or turns, append-only preservation is still necessary but may not by itself express lawful sequence across those turns clearly enough. The records can preserve what occurred, but the relation between preserved turns may otherwise remain recoverable only by interpretation.

Continuity is therefore relevant now only because the body has already moved. Before repeated truthful turns existed, a continuity layer would have been premature.

## 4. Registry vs Continuity

Registry preserves canonical records.

Continuity preserves lawful relation across turns and runs.

Registry answers `what was preserved`.

Continuity answers `how preserved turns remain linked without collapse`.

The registry keeps state, transition, validation, witness, governance, and lineage-bearing records durable in authoritative form. A continuity layer would relate preserved runs or turns by reference to that canon so lawful becoming remains reconstructable across time.

Continuity therefore depends on registry-backed canon. It does not compete with it.

## 5. What Continuity Does Not Replace

Continuity does not replace:

- state
- transition
- validation
- witness
- governance
- registry
- runtime coordination

State still preserves what stands.  
Transition still preserves lawful movement.  
Validation still preserves bounded checking.  
Witness still preserves contact.  
Governance still preserves lawful force.  
Registry still preserves canonical records.  
Runtime coordination still governs lawful handoff between runtime roles.

This layer also does not redefine continuity as a standing-state category. That remains a matter for state and transition handling, not for continuity-layer summary.

## 6. Smallest Safe First Continuity Artifact

The smallest safe first continuity artifact is a bounded continuity turn record.

At a high level, such a record would likely relate:

- the current run id
- a predecessor turn ref where one exists
- the matter ref for the run
- the related canonical artifact refs
- `recorded_at`

Its purpose would be modest: to preserve one explicit append-oriented continuity relation between preserved turns without summarizing away the underlying canonical records.

It should point to preserved canon, not replace it.

This document does not yet define the schema, storage form, or emission policy for that artifact.

## 7. Continuity and Lineage

Lineage already exists as an invariant in IAMMAI because lawful succession cannot be left to timestamp guessing, naming similarity, or narrative reconstruction.

Continuity would make lawful sequence across runs more explicit by relating one preserved turn to its lawful predecessor without collapsing the underlying state, transition, matter, or artifact distinctions.

Continuity is not decorative. Once the body has multiple truthful turns, lawful becoming needs more than isolated preserved runs if later readers are to reconstruct sequence without guesswork.

Continuity must therefore remain append-oriented. New turns should relate to prior preserved turns by addition, not by in-place rewrite or retrospective smoothing.

## 8. Continuity Anti-Collapse Rules

A conforming continuity layer must not allow:

- continuity to replace canonical records
- continuity to reinterpret truth by itself
- continuity to become a summary fiction detached from preserved artifacts
- continuity to collapse multiple runs into one vague narrative
- geometry or visualization to be mistaken for continuity itself
- silent overwrite of prior turn relation
- derivative summaries to impersonate lawful sequence

## 9. What Remains Open

The following remain intentionally open for later continuity work:

- the exact artifact name
- the exact schema shape
- whether the first continuity artifact is run-centric or turn-centric
- how much continuity should be emitted automatically
- when richer continuity or SPIRAL geometry becomes appropriate

## 10. Summary

This document defines the first bounded continuity layer of IAMMAI as a small architectural layer above canonical preservation that keeps preserved runs or turns lawfully related without replacing the registry, collapsing runtime roles, or rewriting preserved canon.

Its purpose is to make lawful becoming reconstructable once the body has actually moved across multiple truthful turns.

**One-Line Definition:** `CONTINUITY_OVERVIEW.md` defines the first bounded continuity layer of IAMMAI as append-oriented preservation of lawful relation across preserved turns and runs, built above canonical records and never in place of them.
