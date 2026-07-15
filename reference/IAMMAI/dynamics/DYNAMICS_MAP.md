# IAMMAI Dynamics Map

## 1. Purpose

This file defines the orientation map for the `dynamics/` folder.

Its job is to explain what the dynamics folder is for, how it relates to the constitutional core and the other repo layers, what each dynamics file governs, what order to read them in, and what this layer does and does not try to solve yet.

It is not:

- code
- a theory-of-everything manifesto
- a replacement constitutional layer
- a control-system design
- a schema set
- a runtime implementation plan

It is a bounded architectural orientation document.

## 2. Relation to the Constitutional Core

The constitutional core remains the source of truth.

Dynamics is subordinate to constitutional invariants.  
Integrity remains constitutional first, not born in dynamics.

These documents do not define what may count, stand, change, or remain distinct. They ask how lawful motion behaves over time relative to those prior conditions. If a dynamics document and the constitutional core diverge, the constitutional core governs.

## 3. Relation to Other Layers

The architecture layer defines the body.

The runtime layer defines motion in bounded execution.

The embodiment layer defines the first live slice and its bounded execution posture.

The continuity layer preserves lawful relation across turns.

The dynamics layer asks how lawful motion behaves over time relative to the constitutional invariant once that body already exists, already moves, already varies, and already preserves continuity.

## 4. Why a Dynamics Folder Is Needed

These questions would have been premature before the body existed.

Before lawful runtime, embodiment, repeated runs, visible failure, controlled variation, and continuity, motion questions at this level would have been speculative. There would have been no living body to regulate, no drift to name, no stability to evaluate, and no lawful adaptation question to open.

Repeated runs, visible failure, controlled variation, and continuity now make motion questions relevant.

Dynamics should remain a distinct layer because these questions are not identical to runtime execution detail or continuity preservation detail. Runtime explains how the body moves in bounded operation. Continuity explains how preserved turns remain linked. Dynamics asks how that lawful motion behaves over time under pressure, deviation, steadiness, and possible lawful reconfiguration.

## 5. Reading Order

A clean reading order for this folder is:

1. `DYNAMICS_MAP.md`
2. `DYNAMICS_OVERVIEW.md`
3. `REGULATION_OVERVIEW.md`
4. `DRIFT_OVERVIEW.md`
5. `STABILITY_OVERVIEW.md`
6. `ADAPTATION_OVERVIEW.md`

This order moves from the orientation map of the folder to the general dynamics frame, then through the first necessary motion concepts in the order already established by the current body.

## 6. File Roles

### `DYNAMICS_OVERVIEW.md`

This document governs the first bounded introduction to the dynamics layer as the derivative account of how lawful motion behaves over time relative to constitutional invariants, runtime execution, embodiment, and continuity.

### `REGULATION_OVERVIEW.md`

This document governs the first bounded regulation concept as the problem of preserving lawful distinction and sequence under repeated motion and pressure.

### `DRIFT_OVERVIEW.md`

This document governs the first bounded drift concept as patterned deviation away from lawful integrity conditions across repeated motion and variation.

### `STABILITY_OVERVIEW.md`

This document governs the first bounded stability concept as lawful steadiness across repeated turns, visible failure, variation, and preserved continuity without collapsing into cosmetic smoothness or rigid stasis.

### `ADAPTATION_OVERVIEW.md`

This document governs the first bounded adaptation concept as lawful reconfiguration under repeated motion and pressure that remains subordinate to constitutional invariants and does not optimize integrity away.

## 7. Folder Boundary

This folder currently does:

- introduce the first bounded dynamics layer for the living IAMMAI body
- define the first bounded concepts of regulation, drift, stability, and adaptation
- keep those motion concepts subordinate to constitutional invariants
- provide the first bounded motion and regulation layer for the living body

This folder does not yet:

- replace law
- replace runtime
- define code or schemas
- finalize a total theory
- settle operational mechanics for dynamics handling

These documents are architectural and theory-facing. They exist to keep higher-order motion questions explicit and bounded rather than leaving them scattered across runtime, embodiment, or continuity surfaces.

## 8. Open Questions

The following remain intentionally open for later dynamics work:

- when any dynamics concepts need runtime or code translation
- whether some dynamics concepts later need schemas
- how continuity and dynamics will relate more deeply over time
- whether later formalization is needed beyond overview documents

## 9. Summary

This document defines the orientation map for the `dynamics/` folder as the bounded entry surface for IAMMAI’s first motion-regulation layer above runtime and continuity but below the constitutional core that governs it.

Its purpose is to keep the dynamics set readable as one derivative folder: a small architectural family that asks how the already-living body behaves over time without pretending to found law, replace runtime, or explain the whole system.

**One-Line Definition:** `DYNAMICS_MAP.md` defines the orientation layer for the dynamics folder as the first bounded map of IAMMAI’s regulation, drift, stability, and adaptation documents, all subordinate to the constitutional core and focused on lawful motion over time.
