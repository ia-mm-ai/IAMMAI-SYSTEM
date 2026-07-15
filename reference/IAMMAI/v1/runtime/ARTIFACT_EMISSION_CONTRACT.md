# IAMMAI Artifact Emission Contract

## 1. Purpose

This file defines the first v1 runtime-level contract for artifact emission.

Its job is to bridge the v1 artifact-boundary decision into later schema and emitter re-derivation by stating how canonical artifact body, execution or envelope context, and registry or preservation context relate at emission time.

It does not define:

- a constitutional rewrite
- a seam declaration
- an authority or inheritance map
- a schema file
- a schema map
- a code patch note
- an emitter implementation plan
- an API design
- a storage-topology design
- a continuity redesign
- a README

It is a bounded runtime contract.

## 2. Why This Contract Is Needed Now

`v1/03_ARTIFACT_BOUNDARY_DECISION.md` already decided that `run_id` belongs to execution or envelope context rather than to the canonical artifact body.

The current root emitters still remain run-saturated in identity and reference behavior. In the present root body, artifact ids are derived from run occurrence, emitted artifact bodies carry `run_id`, and continuity-turn currently makes `run_id` part of required emitted shape.

V1 therefore needs an explicit bridge before schemas and emitters are re-derived. It cannot solve the problem by removing `run_id` from canonical bodies while silently keeping run-saturated identity and reference law through the back door.

## 3. First Principle

Artifact emission must preserve the distinction between body and envelope.

Execution convenience must not define canonical artifact identity.  
Registry or preservation context must not silently become artifact law.

In v1 terms, emission may preserve relation between artifact, run occurrence, and preservation context, but those relations must remain explicit and non-collapsed.

## 4. Contract Layers

This contract distinguishes three layers:

- canonical artifact body
- execution or envelope context
- registry or preservation context

The canonical artifact body is the artifact as artifact: the bounded content that makes the artifact the lawful record family it is.

Execution or envelope context is the bounded runtime occurrence within which the artifact was emitted, carried, or related to other emitted structures.

Registry or preservation context is the bounded preservation placement through which an emitted artifact or emitted envelope becomes durable, retrievable, and reconstructable.

These layers may relate. They must not collapse.

## 5. Emission Posture

To emit a canonical artifact body is to emit the artifact in its own bounded identity as artifact, without silently flattening execution occurrence or preservation placement into that body.

To emit an envelope-bearing artifact is to emit body and envelope together in one carried emission where both are present and recoverable.

Body and envelope may travel together, but they must not collapse into one undifferentiated emitted shape. If emitted together, the canonical artifact body must remain explicit and separable from the execution or envelope context that accompanies it.

## 6. Identity Law

At high level, v1 identity law is:

- artifact identity identifies the artifact as artifact
- matter identity identifies the matter relation where applicable
- run identity identifies execution occurrence
- registry or preservation identity identifies where and how the artifact was preserved or carried

These identities are not interchangeable.

Artifact identity is not the same as run identity. Matter identity is not the same as artifact identity. Registry or preservation identity is not the same as either. Exact final identifier formatting may remain open here, but v1 identity law must no longer be run-saturated by default.

## 7. Reference Law

Canonical artifact-body references must remain lawful to the artifact itself.

That means canonical references inside the artifact body should point only to lawful canonical artifact relations or matter relations required by what the artifact itself preserves.

Run occurrence may still need to be preserved, but where preserved it belongs in explicit envelope or execution context rather than being silently baked into canonical body reference law.

Canonical references must not secretly re-import run-boundedness by convenience.

## 8. Envelope-Bearing Emission

Envelope-bearing emission is the lawful case in which canonical body and execution context are emitted together.

This is not the same thing as canonical artifact body. It is a carried emission posture in which:

- the body remains the body
- the envelope remains explicit execution or relation context
- the body and envelope can be separated without guesswork

Later schemas and emitters must preserve that distinction explicitly. A combined emission must not flatten body and envelope into one generic shape merely because they travel together.

## 9. Continuity Note

Continuity-turn remains a special case because it preserves accumulation across execution occurrence and is currently entangled with run-centric posture.

This contract does not yet settle final continuity schema. It does, however, make one boundary clear: any preserved run-occurrence relation must not silently become canonical artifact identity by default.

If continuity needs explicit execution relation, that relation must be made explicit as execution or envelope context rather than silently preserving old run-saturated identity law under a cleaner name.

## 10. Anti-Collapse Rules

A conforming v1 emission posture must not allow:

- body or envelope flattening
- run identity to pretend to be canonical artifact identity by default
- registry placement to pretend to be canonical artifact law
- combined emission to destroy recoverability of the body or envelope distinction
- schema re-derivation on top of unresolved identity or reference collapse

## 11. Downstream Consequences

This contract must explicitly govern later v1 schema re-derivation.

It must explicitly govern later emitter updates. It must explicitly constrain later continuity handling where relevant.

That means later schema work must derive from this contract rather than substitute for it, and later emitter updates must preserve explicit body, envelope, and preservation distinction rather than silently carrying forward root-side run saturation in a tidied form.

## 12. Closing Boundary Statement

This file defines the artifact emission contract only.

Later files may implement it in schema and emitter surfaces. This contract exists so v1 can move from artifact-boundary decision into lawful emitted structure without re-importing drift.
