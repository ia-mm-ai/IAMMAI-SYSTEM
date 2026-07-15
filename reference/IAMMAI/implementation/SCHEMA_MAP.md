# IAMMAI Schema Map

## 1. Purpose

This file defines the first schema-planning layer for IAMMAI.

Its job is to identify which schemas should exist first, what each schema family governs, what each schema derives from, and in what order schema derivation should proceed.

Schema-planning is needed now because the implementation folder has reached the point where core record and artifact types are defined clearly enough to move toward typed technical closure without yet committing to final infrastructure or product-specific design.

It does not yet try to define:
- final schemas
- JSON Schema bodies
- API contracts
- storage layouts
- service decomposition
- infrastructure topology

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

Schemas must serve the constitutional core.

Schemas must preserve the typed distinctions already established in the architecture and implementation layers. Technical closure must not replace constitutional meaning, and schema convenience must not flatten roles that the protocol keeps distinct.

The constitutional core remains the semantic source of truth. The schema layer exists to preserve that meaning in machine-enforceable form, not to redefine it.

## 3. Why a Schema Layer Is Needed

Architecture prose is not enough for mechanical closure.

- Architecture and implementation documents define the distinctions the runtime must preserve, but they do not yet provide machine-enforceable structure.
- Schemas are the next step in making the body more real because they force explicit field presence, explicit references, typed separation, and bounded artifact shape.
- Machine-enforceable structure matters now because witness, validation, governance, and transition artifacts are already defined closely enough that continued informality would invite drift or flattening.
- This phase should still remain bounded because the goal is not full system closure. The goal is to secure the first constitutional record and artifact families against silent collapse.

This is therefore a planning layer for first schema derivation, not a final schema system.

## 4. Schema Families to Create First

The first schema family set should remain small and centered on the main typed artifacts already defined in the implementation layer.

### 4.1 `witness_artifact.schema.json`

- Governs: the bounded structure of witness artifacts that preserve contact, claims, non-claims, target relation, timing, and optional actor / surface / scope references.
- Derives from: `protocol/canon.json`, `protocol/conformance_tests.md`, `architecture/WITNESS_VALIDATOR_GOVERNOR.md`, `architecture/STATE_AND_DATA_ROLES.md`, `implementation/WITNESS_ARTIFACT_OVERVIEW.md`, and `implementation/CANONICAL_RECORDS_OVERVIEW.md`.
- Belongs in the first set because: witness is already defined as a bounded artifact family with clear claims, non-claims, and reference needs, and it establishes an early anti-collapse baseline for trace preservation.

### 4.2 `validation_artifact.schema.json`

- Governs: the bounded structure of validation artifacts that preserve target, validation type, condition set or rule reference, outcome, timing, and optional reason or witness relation.
- Derives from: `protocol/canon.json`, `protocol/conformance_tests.md`, `architecture/WITNESS_VALIDATOR_GOVERNOR.md`, `architecture/RUNTIME_COMPONENTS.md`, `implementation/VALIDATION_ARTIFACT_OVERVIEW.md`, and `implementation/CANONICAL_RECORDS_OVERVIEW.md`.
- Belongs in the first set because: validation is already defined as typed condition checking and must not collapse into witness, governance, or generic pass/fail logging.

### 4.3 `governance_action.schema.json`

- Governs: the bounded structure of governance action records that preserve action type, authority class, actor reference, legitimacy basis, matter scope, delegation relation where applicable, target references, and time of action.
- Derives from: `protocol/canon.json`, `protocol/conformance_tests.md`, `architecture/WITNESS_VALIDATOR_GOVERNOR.md`, `architecture/STATE_AND_DATA_ROLES.md`, `implementation/GOVERNANCE_ACTION_OVERVIEW.md`, and `implementation/CANONICAL_RECORDS_OVERVIEW.md`.
- Belongs in the first set because: governance action is the main force-bearing record family and must become structurally attributable, legitimacy-bounded, and matter-scoped before other technical layers grow around it.

### 4.4 `transition_record.schema.json`

- Governs: the bounded structure of transition records that preserve source and target state or condition references, matter relation, transition type, timing, related validation or governance references where applicable, and predecessor / successor relation where relevant.
- Derives from: `protocol/canon.json`, `protocol/conformance_tests.md`, `architecture/REFERENCE_ARCHITECTURE_v0.md`, `architecture/STATE_AND_DATA_ROLES.md`, `implementation/STATE_MACHINE_OVERVIEW.md`, `implementation/TRANSITION_RECORD_OVERVIEW.md`, and `implementation/CANONICAL_RECORDS_OVERVIEW.md`.
- Belongs in the first set because: lawful change, typed resolution, containment orthogonality, and lineage recoverability already depend on transition records remaining explicit rather than dissolving into generic updates.

### 4.5 `state_record.schema.json` (Optional / Later)

- Governs: the bounded structure of state records across preparation-state, standing-state, containment state, and resolved state.
- Derives from: `protocol/canon.json`, `architecture/STATE_AND_DATA_ROLES.md`, `implementation/STATE_MACHINE_OVERVIEW.md`, and `implementation/CANONICAL_RECORDS_OVERVIEW.md`.
- Belongs later rather than first because: state typing is already well defined, but closing state schema safely depends on the transition, containment, resolution, and lineage conventions becoming clearer first.

## 5. Recommended Schema Creation Order

The safest schema derivation order is:

1. `witness_artifact.schema.json`
2. `validation_artifact.schema.json`
3. `governance_action.schema.json`
4. `transition_record.schema.json`
5. `state_record.schema.json` (optional / later)

This order is safest because:

- witness artifact is the most bounded trace artifact and establishes early reference and anti-inflation discipline
- validation artifact builds next on bounded checking without yet introducing lawful force
- governance action follows once attribution, legitimacy basis, and matter scope can be expressed clearly
- transition record comes after witness, validation, and governance because it may need to point to those artifact families while preserving lineage and typed change
- state record is safest later because its closure depends on the runtime’s settled treatment of transition, containment, resolution, and successor relation

## 6. What Each Schema Must Preserve

Across the first schema set, schema design must preserve:

- typed role separation between witness, validation, governance, transition, and state
- required references where constitutional reconstructability depends on them
- claims versus non-claims where witness artifacts require that boundary
- matter scope where governance or transition logic depends on bounded matter relation
- lineage recoverability where predecessor / successor relation applies
- typed outcome and typed action distinctions rather than generic status or update fields
- non-collapse between preparation-state, standing-state, containment, and resolution where state or transition schemas later touch those boundaries

The schema layer should therefore preserve constitutional distinctions structurally, not just descriptively.

## 7. What Should Remain Deferred

The schema layer should not yet close:

- final infrastructure topology
- storage engine decisions
- API design
- service decomposition
- final validator engine design
- final event-sourcing or transition-log design
- full witness ecology
- companion theory
- private implementation surfaces

Those questions remain downstream of first schema derivation and should not be smuggled into schema planning as if they were already settled.

## 8. Relation to Existing Implementation Files

### `STATE_MACHINE_OVERVIEW.md`

Provides the canonical state regimes, lawful transition logic, containment orthogonality, resolution family closure, and lineage rules that later constrain transition and state schema design.

### `CANONICAL_RECORDS_OVERVIEW.md`

Provides the main record-family map and the baseline distinction between state, transition, governance, witness, validation, and lineage that the schema layer must preserve mechanically.

### `WITNESS_ARTIFACT_OVERVIEW.md`

Provides the bounded witness model, including claims, non-claims, witness types, and target relation, from which the witness artifact schema should derive.

### `GOVERNANCE_ACTION_OVERVIEW.md`

Provides the governance action model, including authority class, legitimacy basis, matter scope, delegation relation, target references, and action types, from which the governance schema should derive.

### `VALIDATION_ARTIFACT_OVERVIEW.md`

Provides the validation model, including validation types, outcomes, target relation, and bounded condition checking, from which the validation schema should derive.

### `TRANSITION_RECORD_OVERVIEW.md`

Provides the transition model, including transition families, source and target relation, containment distinction, resolution typing, and lineage relation, from which the transition schema should derive.

## 9. Anti-Collapse Rules for Schema Derivation

A conforming schema derivation process must not allow:

- witness to flatten into generic logs
- validation to flatten into generic pass/fail events
- governance action to exist without legitimacy basis or matter scope
- transition record to collapse into generic update
- state record to silently replace lineage-bearing structure
- schema convenience to override constitutional distinctions
- shared envelope design to erase witness / validation / governance / transition differences
- derivative product needs to redefine canonical artifact meaning

## 10. Open Questions

The following remain intentionally open before actual schema drafting begins:

- whether a shared reference convention should be defined before the first schema files are written
- how much optional metadata each first schema should permit without inviting flattening
- whether `state_record.schema.json` should wait until the first four schemas stabilize
- how cross-schema references should be named without implying infrastructure design

These are schema-planning questions, not constitutional ambiguities.

## 11. Summary

This document defines the first schema-planning layer of IAMMAI as a bounded map from implementation overviews into an initial set of typed schema families.

Its purpose is to make first schema derivation orderly, constitutional, and mechanically useful without turning schema planning into a premature full-system design.

**One-Line Definition:** `SCHEMA_MAP.md` defines the first implementation-facing schema-planning layer of IAMMAI as a bounded map for deriving the first typed schema families without collapsing constitutional distinctions.
