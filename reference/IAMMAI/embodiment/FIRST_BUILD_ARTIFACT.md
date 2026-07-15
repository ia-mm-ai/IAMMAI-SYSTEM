# IAMMAI First Build Artifact

## 1. Purpose

This file defines the first actual build-adjacent artifact for IAMMAI: the minimal local runner or harness that executes the first lawful cycle.

Its job is to explain:

- what the first build artifact is
- what it must do
- what it must not do
- what runtime parts it must instantiate or call
- what canonical artifacts it must produce
- how it stays smaller than a product while still being real enough to count

It does not yet try to define:

- code
- a deployment plan
- a product specification
- a UI design
- generalized build architecture
- broad runtime tooling

It is a bounded build-adjacent embodiment document.

## 2. First Principle

The first build artifact must serve the constitutional core.

It must remain smaller than a product.  
It must be real enough to execute one lawful cycle.  
It must preserve typed runtime distinctions.  
It must not fake missing roles or artifacts.

In practice, this means the first build artifact must be only a bounded local execution mechanism for the selected first cycle, not a platform surface, not a demo shell, and not a substitute for the runtime roles it invokes.

## 3. Why a First Build Artifact Is Needed

Embodiment documents are not yet execution.

- The embodiment layer now defines the matter, cycle, criteria, operator posture, and execution boundary.
- A first local run still needs one concrete build target that can carry those definitions into real motion.

Choosing the build artifact explicitly protects against drift into demo theater or productization. Without this choice, the first implementation step can easily widen into UI work, broad orchestration, or generic tooling that obscures what the first proof actually is.

Build should therefore remain bounded and auditable. The first build artifact exists to execute one lawful cycle honestly, not to imply a complete system.

## 4. Chosen First Build Artifact

The chosen first build artifact is:

**a minimal operator-invoked local runner or harness in the bounded embodiment workspace, capable of executing exactly one selected lawful cycle on one bounded matter.**

In practical terms, this means:

- local-first
- operator-invoked
- bounded to one selected note matter
- bounded to one governed truth-formation attempt
- bounded to the embodiment execution boundary

It is not:

- a broad app
- a dashboard
- a marketplace surface
- a public interface
- a generalized runtime environment

## 5. What the Artifact Must Do

The first build artifact must be capable of:

- receiving one bounded input matter from the embodiment workspace
- invoking validation for the selected cycle
- invoking witness emission where required
- invoking governance where required
- invoking state and transition handling where applicable
- writing canonical artifacts into the bounded registry or output space
- stopping visibly if a required step does not lawfully proceed

For the selected first cycle, that means the runner must be able to:

- take one bounded local note matter in threshold-eligible condition
- run the required threshold, transition-legality, and governance-precondition checks
- cause witness trace to be emitted for the contact and required runtime occurrence
- obtain a typed governance result of authorize, deny, or HOLD
- produce truth-formation transition and truth-state outputs only if authorized and not held
- preserve the resulting canonical artifacts, or preserve visible non-completion where they do not arise

## 6. What the Artifact Must Not Do

The first build artifact must not become:

- a general-purpose platform
- a broad runtime environment
- a UI-first demo
- a market-facing surface
- a private implementation privilege case
- a fake simulation that bypasses required runtime parts
- a broad access layer outside the local execution boundary

It must also not:

- invent missing artifacts
- silently skip required validation
- replace witness with generic logging
- replace governance with operator assertion
- replace canonical preservation with derivative display output

## 7. Runtime Roles Involved

The artifact must instantiate, invoke, or preserve the following runtime roles in the chosen first cycle:

- `Interface Gateway / operator entry surface`
  Minimal and local, but real as the bounded intake path.
- `Validator`
  Real as the checker of the required conditions.
- `Witness Emitter`
  Real as the emitter of the required witness trace.
- `Governor`
  Real where required, and required for the selected first cycle.
- `State Engine`
  Real as the performer of lawful movement or visible non-movement.
- `Registry / Store`
  Real as the preservation surface for the canonical artifacts actually produced.

All required roles are real, even if minimally embodied.

## 8. Inputs and Outputs

At a high level, the artifact consumes:

- one bounded matter input from `embodiment/input/`
- the selected embodiment definitions needed to run the cycle lawfully
- the schemas and runtime constraints needed to know what artifact family is expected

At a high level, the artifact must produce:

- canonical artifacts into `embodiment/registry/`
- bounded derivative outputs or run-local outputs into `embodiment/output/` or `embodiment/run/` where such outputs are needed for execution visibility

For the selected first cycle, the canonical outputs should include, where the success path is achieved:

- validation artifact
- witness artifact
- governance action record
- transition record
- state record
- registry-preserved canonical records

The output set must remain consistent with the success and failure criteria. If a required output is missing, the artifact must not present the cycle as complete.

## 9. Success and Failure Posture

Success for the build artifact means:

- it executed one bounded cycle on one bounded matter
- it preserved required runtime role distinctions
- it produced the required canonical artifacts on the selected success path
- it made the resulting runtime path reconstructable

Failure must remain visible.

That means missing witness, failed validation, failed governance, failed state movement, or failed preservation must not be hidden, reworded into success, or replaced by narrative output.

The artifact counts only if it preserves truthful non-completion as well as truthful completion. A runner that can only display apparent success but cannot surface lawful non-passage does not count as a valid first build artifact.

## 10. Relation to the Embodiment Folder

This artifact depends on:

- `MATTER_DEFINITION.md`
  for the selected bounded matter
- `FIRST_LIVE_CYCLE.md`
  for the exact selected cycle
- `SUCCESS_AND_FAILURE_CRITERIA.md`
  for how the run is judged
- `OPERATOR_RUNBOOK.md`
  for how the run is carried out operationally
- `LOCAL_EXECUTION_BOUNDARY.md`
  for what the runner is allowed to read and write

The first build artifact should therefore be understood as the executable local carrier of the embodiment folder’s already-defined first proof.

## 11. Build Boundary

This is the first build-adjacent artifact only.

It is:

- local-first
- controlled
- auditable
- neutral
- not yet the public system
- not evidence of broad deployment readiness

Its value lies in enabling one lawful bounded run, not in signaling product maturity or broad operational coverage.

## 12. Open Questions

The following remain intentionally open before implementation begins:

- the exact implementation language
- the exact command surface
- the exact file and folder naming inside `embodiment/run/`
- whether the operator surface is CLI-only or minimally local UI
- the exact internal modularization of the runner

These are build-design questions, not constitutional ambiguities.

## 13. Summary

This document defines IAMMAI’s first build-adjacent artifact as a minimal local runner or harness that executes one selected lawful cycle on one bounded matter inside the embodiment workspace without widening into platform behavior or product form.

Its purpose is to make the first embodiment executable in a real but tightly bounded way, with the full required runtime roles present, the required canonical artifacts produced, and non-completion kept visible rather than cosmetically hidden.

**One-Line Definition:** `FIRST_BUILD_ARTIFACT.md` defines the first build-adjacent artifact of IAMMAI as a minimal local runner that can execute one auditable lawful cycle on one bounded matter without collapsing runtime roles or widening beyond the first embodiment boundary.
