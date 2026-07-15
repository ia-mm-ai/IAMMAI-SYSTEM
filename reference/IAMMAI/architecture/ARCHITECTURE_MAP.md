# IAMMAI Architecture Map

## Purpose

This folder defines the first architecture of the IAMMAI implementation body.

Its job is to make the constitutional core operational as architecture without replacing the constitutional core as the source of meaning.

It is an orientation layer for:
- the minimum lawful body
- the main runtime boundaries
- the main role separations
- the main state and data distinctions

## Relation to the Constitutional Core

The constitutional core remains the semantic source of truth.

This architecture layer does not redefine the law. It carries the law into runtime, governance, witness, persistence, and interface form while keeping constitutional distinctions intact.

If an architecture document and the constitutional core diverge, the constitutional core governs.

## Reading Order

Read the folder in this order:

1. `REFERENCE_ARCHITECTURE_v0.md`
2. `RUNTIME_COMPONENTS.md`
3. `WITNESS_VALIDATOR_GOVERNOR.md`
4. `AUTHORITATIVE_VS_DERIVATIVE_SURFACES.md`
5. `STATE_AND_DATA_ROLES.md`

This order moves from the whole-body frame to runtime organs, then to the key anti-collapse distinctions inside that body.

## Where the Lawful Between Sits

The lawful between sits inside the implementation body.

It is not the constitutional source itself, and it is not a derivative interface surface. In this file family, it is carried primarily by the canonical runtime, witness / validation, governance / authority, and persistence / registry layers, with interface surfaces exposed above them.

The constitutional core remains the governing source over that body.

## File Roles

### `REFERENCE_ARCHITECTURE_v0.md`

This is the entry document for the set. It defines the overall reference architecture: the main layers of the body, the minimum component set, the core orthogonality rules, and the place of the lawful between.

### `RUNTIME_COMPONENTS.md`

This document defines the minimum runtime organs required for the body to operate lawfully. It governs what each core component is responsible for, what each component must not absorb, and the basic order of interaction between components.

### `WITNESS_VALIDATOR_GOVERNOR.md`

This document governs the separation between preserved contact, bounded checking, and lawful action. It keeps witness, validation, and governance typed apart so runtime force does not collapse into observation or checking.

### `AUTHORITATIVE_VS_DERIVATIVE_SURFACES.md`

This document governs source-of-truth boundaries across surfaces. It distinguishes what is authoritative from what is derivative so display, export, routing, or convenience layers do not silently become constitutional authority.

### `STATE_AND_DATA_ROLES.md`

This document governs the minimum typed categories the runtime must preserve. It keeps state, record, and reference roles distinct across candidate material, standing state, containment, resolution, governance, contribution, witness / validation, and lineage.

## Boundary of the Folder

This folder does:
- define the minimum architecture of the implementation body
- preserve constitutional distinctions in operational form
- establish the main runtime, surface, role, and data boundaries
- grant no conceptual or semantic privilege to any private implementation

This folder does not yet:
- choose a final infrastructure stack
- choose a final service decomposition
- finalize storage formats or deployment topology
- define product surfaces, APIs, or UI/UX
- settle performance, scaling, or vendor choices

## Open for Technical Derivation

Technical derivation remains open where concrete implementation choices are still needed, such as storage models, service boundaries, witness formats, validation machinery, interface protocols, identity strategies, and related enforcement details.

Those questions remain subordinate to the architectural boundaries already set here.

## Summary

Read this folder as one bounded architecture set.

`REFERENCE_ARCHITECTURE_v0.md` gives the whole-body frame. The other documents define the main runtime distinctions that keep the body lawful, typed, and non-collapsed in operation.
