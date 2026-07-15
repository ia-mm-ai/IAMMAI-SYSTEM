# IAMMAI v1 Runtime Flow Map

## 1. Purpose

This file defines the bounded v1 runtime flow that follows the body-schema round and the v1 conformance rules, and that precedes concrete emitter re-derivation.

Its job is to map, at runtime-contract level, how v1 moves through canonical body formation, canonical body conformance, optional envelope-bearing emission, envelope-bearing conformance, registry or preservation placement, registry or preservation conformance, and fixture interpretation where relevant.

It does not define:

- a constitutional rewrite
- a seam declaration
- an authority or inheritance map
- an artifact-boundary decision
- a schema file
- an emitter implementation patch
- a validator code note
- a continuity redesign
- a storage topology design
- a project-management roadmap
- a README

It is a bounded runtime flow map.

## 2. Why This Map Is Needed Now

V1 now has canonical body schemas.

V1 also now has an explicit conformance posture across canonical body, envelope-bearing emission, and preservation context. That means runtime flow must now be stated before emitter re-derivation proceeds.

The current root runtime behavior remains important lineage evidence, especially where the root runners still emit run-saturated artifacts and preservation outputs in one bounded execution path. That root behavior is historically real. It is not automatic v1 law.

V1 therefore needs its own runtime flow posture so later emitter work does not silently inherit the v0 run-saturated path by convenience.

## 3. First Principle

Runtime flow must preserve what the body is claiming at each stage.

Canonical body, envelope-bearing emission, and preservation context are distinct runtime stages.  
Later stages must not redefine earlier stages by convenience.

If a runtime stage is claiming to form a canonical artifact body, it must be read as canonical body. If it is claiming to carry body with envelope, it must be read as envelope-bearing emission. If it is claiming preservation, it must be read as preservation. These claims must not collapse into one generic runtime pass.

## 4. Runtime Stages

The bounded v1 runtime flow is:

- canonical body formation
- canonical body conformance
- optional envelope-bearing emission formation
- envelope-bearing emission conformance
- preservation or registry placement
- preservation or registry conformance
- fixture interpretation where applicable

This is the lawful order because artifact identity must first be formed and checked as artifact before any combined carrying or preservation posture is evaluated.

## 5. Canonical Body Stage

Canonical body formation is the runtime stage at which a bounded artifact body is formed as artifact.

At this stage, runtime forms the canonical body for the relevant record family in accordance with the current v1 body law and body schema. This stage is artifact-first, not run-envelope-first.

Canonical body conformance is then checked here as canonical body. That means runtime asks whether the formed validation artifact body, witness artifact body, governance action body, transition record body, or state record body conforms as canonical body.

This stage does not yet settle envelope, transport, or preservation placement.

## 6. Envelope-Bearing Stage

Envelope-bearing emission formation is the runtime stage at which a canonical body may be carried together with explicit execution or envelope context.

This stage is optional and downstream of canonical body conformance. Runtime should not form envelope-bearing emission first and then infer canonical body validity from the combined result.

If body and envelope travel together, their combined travel does not erase body or envelope distinction. Envelope-bearing emission conformance therefore asks whether combined carrying preserved explicit body or envelope separability rather than flattening them into one undifferentiated emitted shape.

## 7. Preservation Stage

Preservation or registry placement is the runtime stage at which a canonical artifact body, or an explicitly separated envelope-bearing emission, is placed into authoritative preservation context.

This stage is downstream again. Preservation is not artifact redefinition. It is the bounded act of preserving what has already been formed and, where relevant, already carried.

Preservation or registry conformance is therefore its own stage. It asks whether authoritative preservation remains typed, reconstructable, retrievable, and non-collapsed without silently changing canonical artifact meaning.

## 8. Fixture Interpretation Stage

Fixture interpretation belongs after the relevant conformance surface, not before it.

Positive fixtures should be read as expected lawful examples for the stage they exercise. Negative fixtures should be read as bounded failures. Refusal-path fixtures should be read as lawful non-passage where a relevant surface intentionally fails or refuses. Other bounded failure fixtures should also be read by stage and layer.

That means fixture meaning must remain stage-aware:

- body fixture meaning follows body conformance
- envelope fixture meaning follows envelope-bearing conformance
- preservation fixture meaning follows preservation conformance
- refusal-path fixture meaning follows the surface at which refusal was lawfully preserved

Deliberate failure is not automatic architectural incoherence.

## 9. Current-v0 / Desired-v1 Distinction

The current root runtime and emitter behavior belongs to v0 lineage reality.

That includes the historically real root runners which form, relate, and preserve artifacts through a run-saturated path in which artifact ids, emitted bodies, and continuity handling remain closely tied to execution occurrence.

The desired v1 runtime flow is the target posture that later emitter updates must serve. This is not a blame note against the root line. It is the explicit statement that v1 runtime law is being re-derived rather than silently copied from the v0 runtime path.

## 10. Continuity Boundary

Continuity remains a special case and is not fully settled by this flow map.

Continuity must later be handled in a way that respects the current v1 distinction between canonical body, envelope-bearing emission, and preservation context.

This map must not silently absorb continuity into the ordinary artifact flow by convenience. Continuity remains unresolved special handling rather than a settled example of ordinary body-schema closure.

## 11. Anti-Collapse Rules

A conforming v1 runtime flow must not allow:

- envelope-first runtime posture
- treating combined emission as if body formation never mattered
- preservation placement redefining artifact identity
- fixture interpretation without stage awareness
- continuity shortcut that bypasses unresolved execution-occurrence handling

It must also not allow later stages to back-authorize earlier stages. Preservation does not prove body formation. Combined travel does not prove canonical body validity. Fixture visibility does not by itself settle runtime law.

## 12. Downstream Consequences

Later emitter re-derivation must follow this runtime flow.

Later validator and runtime work must follow this runtime flow. Later continuity handling must remain consistent with this runtime flow where applicable.

This map is therefore a runtime bridge from conformance law toward emitter work. It states the lawful stage order so later implementation surfaces do not re-import v0 collapse patterns while appearing cleaner.

## 13. Closing Boundary Statement

This file defines runtime flow posture only.

Later files may implement this flow in emitter and runtime surfaces. This map exists so v1 can move from schema and conformance law toward lawful runtime behavior without re-importing v0 collapse patterns.
