# IAMMAI v1 Artifact Boundary Decision

## 1. Purpose

This file defines the first explicit v1 law decision on the boundary between canonical artifact body and execution or envelope context.

Its job is to state what belongs to the artifact as artifact, what belongs to runtime, execution, storage, or preservation context, and what consequence that boundary has for later schema and emitter re-derivation.

It does not define:

- a constitutional rewrite
- a seam declaration
- an authority or inheritance map
- a schema file
- a runtime contract
- a fixture taxonomy
- a full re-derivation plan
- a README

It is a bounded artifact-boundary law decision.

## 2. First Principle

Artifact boundary must be explicit.

Canonical artifact body and execution context must not collapse.  
Later schema and emitter alignment depends on this decision.

If the boundary remains undefined, runtime convenience can drift into canonical artifact identity, and canonical artifact shape can drift into envelope or storage residue without clear law.

## 3. Why This Decision Is Needed

Doctrine, schema, runtime, and emitted artifact shape can drift if artifact boundary is not explicit.

The current body already distinguishes canonical records from derivative and convenience surfaces, but the emitted artifact family can still absorb run-bounded execution residue if artifact law is left implicit. V1 therefore requires a lawful boundary before schemas or emitters are re-derived.

## 4. Canonical Artifact Body

The canonical artifact body is what belongs to the artifact as artifact.

At a high level, it should preserve:

- artifact identity
- artifact kind
- matter relation where applicable
- lawful claims and non-claims where applicable
- bounded references required for reconstructing what the artifact itself preserves

The artifact body should therefore contain what makes the artifact the specific canonical artifact that it is, not every surrounding fact about the run, storage path, or emitter process that happened to produce or preserve it.

## 5. Execution / Envelope Context

Execution or envelope context is what belongs to runtime, run-boundedness, execution trace, or storage context rather than to the canonical artifact body.

At a high level, this includes:

- runtime or run occurrence context
- emitter or execution session context
- storage and registry placement context
- envelope metadata used to carry, route, preserve, or retrieve the artifact

This context may still be important, but it is not identical to canonical artifact identity.

## 6. Boundary Decision

V1 will treat `run_id` as execution or envelope context, not as part of the canonical artifact body.

`run_id` names the bounded execution occurrence within which an artifact was emitted or preserved. That is important for traceability, registry relation, and continuity, but it is not the same thing as the artifact’s canonical identity as artifact.

Artifact identity, matter identity, runtime or execution context, and registry or storage context must therefore remain distinct:

- artifact identity identifies the artifact as artifact
- matter identity identifies what matter the artifact relates to
- runtime or execution context identifies the bounded run or emission occurrence
- registry or storage context identifies where and how the artifact was preserved or carried

Run-boundedness therefore belongs outside the canonical artifact body in execution or envelope context.

## 7. Consequences of the Decision

This decision means later schema re-derivation should not silently bake runtime envelope fields into canonical artifact identity.

It means later emitter behavior should produce a clear separation between artifact body and execution or preservation context rather than flattening them into one emitted shape by convenience.

It also means fixture classification must distinguish:

- canonical positive artifact bodies
- execution or envelope-bearing emissions
- broken or refusal-path fixtures that must not be mistaken for canonical output

## 8. Anti-Collapse Rules

The following must not occur:

- silent artifact or envelope mixing
- runtime metadata pretending to be canonical artifact identity unless explicitly ratified
- broken fixture accidentally treated as canonical output
- schema closure built on an undefined artifact boundary

## 9. Closing Boundary Statement

This file defines the first v1 artifact-boundary law decision.

Later files may implement or classify it. This decision exists before schema and emitter re-derivation so that v1 does not inherit ambiguity by default.
