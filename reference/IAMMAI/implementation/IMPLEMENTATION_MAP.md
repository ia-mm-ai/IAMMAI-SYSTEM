# IAMMAI Implementation Map

## 1. Purpose

This folder defines the first implementation-facing derivative layer of IAMMAI.

Its job is to translate the constitutional core and the architecture set into bounded technical overviews that an implementation body can use without collapsing the underlying distinctions.

It is not:
- code
- a schema set
- a database design
- a final runtime design
- a product specification

## 2. Relation to the Constitutional Core

The constitutional core remains the semantic source of truth.

These implementation documents derive from the protocol and do not supersede it. They translate constitutional meaning into implementation-facing form, but they do not redefine the law.

If an implementation document and the constitutional core diverge, the constitutional core governs.

## 3. Relation to the Architecture Folder

The architecture folder defines the body at a structural level.

It establishes the main layers, runtime roles, anti-collapse boundaries, and typed distinctions that the implementation body must preserve.

This implementation folder begins the technical derivative layer. It takes those architectural boundaries and expresses them in a more implementation-facing form without turning them into code, schemas, or vendor-specific design.

## 4. Reading Order

A clean reading order for this folder is:

1. `STATE_MACHINE_OVERVIEW.md`
2. `CANONICAL_RECORDS_OVERVIEW.md`
3. `VALIDATION_ARTIFACT_OVERVIEW.md`
4. `TRANSITION_RECORD_OVERVIEW.md`
5. `WITNESS_ARTIFACT_OVERVIEW.md`
6. `GOVERNANCE_ACTION_OVERVIEW.md`

This order moves from state movement, to preserved records, to bounded checking, to typed transition trace, to witness trace, and then to governance action.

## 5. File Roles

### `STATE_MACHINE_OVERVIEW.md`

This document governs the first implementation-facing view of canonical state regimes, lawful transition, orthogonal containment, typed resolution, and lineage-preserving change.

### `CANONICAL_RECORDS_OVERVIEW.md`

This document governs the first implementation-facing view of the main record families the body must preserve, including state, transition, resolution, governance, contribution, witness, validation, and lineage.

### `VALIDATION_ARTIFACT_OVERVIEW.md`

This document governs the first implementation-facing view of validation artifacts as typed, bounded checking records that preserve admissibility, threshold, transition-legality, and related condition evaluation without becoming governance or semantic source.

### `TRANSITION_RECORD_OVERVIEW.md`

This document governs the first implementation-facing view of transition records as typed, reconstructable records of lawful protocol change across preparation, standing state, containment, resolution, and lineage.

### `WITNESS_ARTIFACT_OVERVIEW.md`

This document governs the first implementation-facing view of witness artifacts as bounded trace records that preserve contact without becoming semantic source, governance, or authorship.

### `GOVERNANCE_ACTION_OVERVIEW.md`

This document governs the first implementation-facing view of governance action as attributable, legitimacy-bounded, matter-scoped protocol force preserved in reconstructable record form.

## 6. Folder Boundary

This folder currently covers:
- the first implementation-facing state-machine view
- the first implementation-facing record model
- the first implementation-facing validation artifact model
- the first implementation-facing transition record model
- the first implementation-facing witness artifact model
- the first implementation-facing governance action model

This folder intentionally leaves open:
- final schemas
- storage design
- service decomposition
- runtime topology
- validator engine design details
- event-sourcing or transition-log design details
- identity and delegation infrastructure details
- full witness ecology
- full governance-system detail

These documents are technical derivations of the constitutional and architectural layers, not final implementation blueprints.

## 7. Summary

Read this folder as one bounded implementation set.

The constitutional core remains the source of truth. The architecture folder defines the structure of the body. This folder begins the technical derivative layer that makes those structures easier to implement across state movement, records, validation, transition trace, witness trace, and governance action without collapsing their distinctions.

**One-Line Definition:** `IMPLEMENTATION_MAP.md` defines the orientation layer for the implementation folder as the first bounded technical derivative set beneath the constitutional and architectural layers of IAMMAI.
