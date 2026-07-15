# IAMMAI Continuity Turn Overview

## 1. Purpose

This file defines the first bounded continuity-turn concept for IAMMAI.

Its job is to explain what a continuity turn is, why it becomes useful once the body has already moved across multiple runs or turns, how it relates to runs, matters, and canonical artifacts, and what the smallest safe first continuity-turn shape likely needs to reference.

It does not yet try to define:

- code
- a schema
- a graph model
- a visualization system
- a continuity database design
- a final automatic-emission policy

It is a bounded architectural document for the first continuity-turn concept.

## 2. First Principle

A continuity turn preserves lawful relation across one bounded run or turn.

It depends on preserved canonical artifacts.  
It does not replace those artifacts.  
It does not create truth by itself.  
It remains append-oriented and lineage-respecting.

In practical terms, a continuity turn can only stand in relation to a run or turn whose preserved artifacts are already recoverable. It does not authorize, validate, witness, govern, or preserve by summary.

## 3. Why a Continuity Turn Is Needed

Repeated successful and failed runs create a continuity question.

Once the body has more than one preserved run, registry preservation still tells later readers what records were preserved, but it may not fully express how those preserved turns remain related across time without additional interpretation.

A continuity turn is useful because it can make lawful sequence more explicit without changing the existing canonical artifact families. It gives one bounded relation surface for one run or turn while leaving validation, witness, governance, transition, state, and registry preservation exactly where they already belong.

This question is relevant now only because the body has already moved. Before repeated runs existed, continuity-turn handling would have been premature.

## 4. What a Continuity Turn Is

A continuity turn is a bounded continuity record for one lawful run or turn.

At a high level, it is:

- linked to one specific run
- linked to one specific matter
- linked to the canonical artifacts preserved for that run
- optionally linked to a predecessor turn where lawful sequence needs to be made explicit

It is architectural and neutral. It is not a new runtime role, not a new matter category, and not a broad continuity engine.

## 5. What a Continuity Turn Preserves

At a high level, a continuity turn would likely preserve:

- turn identity
- run identity
- matter relation
- predecessor turn relation where relevant
- references to the canonical artifacts produced in the turn
- `recorded_at`

Where a run ends in visible non-passage or partial completion, the continuity turn should relate only to the artifacts that were actually preserved. It must not fabricate downstream artifact relation that the run did not lawfully produce.

This remains a conceptual description only. It is not yet a full schema.

## 6. Continuity Turn vs Canonical Records

Canonical artifacts remain the primary records of what occurred.

A continuity turn relates preserved artifacts across turns. It does not replace them.

A continuity turn is not:

- a state record
- a transition record
- a witness artifact
- a validation artifact
- a governance action record
- registry preservation itself

If a later reader needs to know what was checked, witnessed, authorized, moved, or preserved, the answer still comes from the canonical artifacts. The continuity turn only helps keep their cross-turn relation explicit.

## 7. Continuity Turn vs Summary

A continuity turn is not a narrative recap.

It must remain artifact-linked. It must not flatten multiple events into one vague story. It must not become a cosmetic continuity wrapper placed above runs whose preserved artifact structure is missing, unclear, or detached.

Its purpose is not to make the history sound coherent. Its purpose is to keep lawful sequence explicit without replacing preserved runtime truth.

## 8. Minimal First Continuity-Turn Shape

The smallest safe first continuity-turn shape is conceptual and bounded.

At a high level, it would likely include references such as:

- `turn_id`
- `run_id`
- `matter_ref`
- `predecessor_turn_ref` where present
- refs to validation, witness, governance, transition, and state artifacts where relevant
- `recorded_at`

This first shape should stay small. It should reference the preserved run and the preserved artifacts actually produced, without becoming a generalized event model or a hidden replacement for lineage.

## 9. Anti-Collapse Rules

A conforming continuity-turn concept must not allow:

- a continuity turn to stand in for missing canonical artifacts
- a continuity turn to invent truth or authority
- a continuity turn to detach from preserved runs
- a continuity turn to collapse multiple distinct runs into one pseudo-event
- a continuity turn to become a narrative fiction over incomplete preservation
- a continuity turn to be treated as geometry or visualization alone

## 10. Relation to Future Continuity Work

This is the first bounded continuity-turn concept only.

Later work may include:

- a continuity-turn schema
- automatic emission rules
- explicit predecessor or successor continuity across runs
- richer continuity geometry later, if lawfully justified

Those are later derivation questions. They should not be smuggled into this first concept.

## 11. Summary

This document defines the first continuity-turn concept of IAMMAI as a bounded continuity record for one preserved run or turn, linked to its matter and preserved canonical artifacts, and used to keep lawful sequence explicit across multiple runs without replacing canonical records.

Its purpose is to make cross-turn continuity clearer now that the body has already moved, while keeping continuity small, append-oriented, artifact-linked, and non-sovereign.

**One-Line Definition:** `CONTINUITY_TURN_OVERVIEW.md` defines the first bounded continuity-turn concept of IAMMAI as an append-oriented continuity record for one preserved run or turn that links matter, run, predecessor relation where present, and related canonical artifacts without replacing them.
