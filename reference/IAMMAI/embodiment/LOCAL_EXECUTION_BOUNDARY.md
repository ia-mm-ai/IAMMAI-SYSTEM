# IAMMAI Local Execution Boundary

## 1. Purpose

This file defines the exact local execution boundary for the first lawful embodiment slice.

Its job is to make explicit:

- what the first local run is allowed to read
- what it is allowed to write
- what folders constitute the bounded embodiment workspace
- what remains outside execution scope
- how wide constitutional context and narrow operational scope are applied in practice

It does not yet try to define:

- code
- a deployment guide
- a security policy
- an infrastructure diagram
- broad execution policy
- later wider embodiment boundaries

It is a bounded embodiment-execution boundary document.

## 2. First Principle

The first run may rely on the repo as constitutional context.

The first run must operate only within a narrowly bounded local workspace.  
Execution boundary is part of lawful embodiment.  
Broad ambient access is not required for first proof.

In practice, that means the first run may read the repo as governing reference, but it must not silently behave as though the whole machine, the whole network, or the whole repo were part of the live operational scope.

## 3. Why an Execution Boundary Is Needed

Architecture and embodiment choice are not enough by themselves.

- The constitutional, architecture, implementation, schema, runtime, and embodiment documents define what the first slice means.
- They do not by themselves define what the first local run is allowed to touch.

The first local run therefore needs explicit scope.

Narrow scope protects integrity because it prevents accidental drift, overreach, hidden dependency, and fake proof. If the first run may freely read, write, or reach anywhere by convenience, it becomes difficult to know what actually constituted the proof.

This boundary exists to keep the first embodiment narrow enough to remain honest.

## 4. Constitutional Context vs Operational Scope

Two different scopes matter here.

### Constitutional Context

The broad repo context is the governing reference for the first run. It includes the constitutional protocol, the architecture layer, the implementation layer, the schema family, the runtime layer, and the embodiment definitions already written in the repo.

### Operational Scope

The operational scope is the narrow local zone in which the actual run occurs. It includes only the bounded matter, the bounded embodiment workspace, the required local runtime surfaces, and the canonical artifacts produced by that one selected cycle.

The distinction is central:

- broad repo context governs the run
- narrow operational scope performs the run

Governing reference is not the same thing as live execution permission.

## 5. Bounded Embodiment Workspace

The embodiment workspace is the execution zone for the first run.

Its intended bounded folders are:

- `embodiment/input/`
  The bounded input surface for the selected matter.
- `embodiment/output/`
  The bounded derivative output surface for the first local run.
- `embodiment/registry/`
  The bounded local preservation surface for the canonical artifacts produced by the selected cycle.
- `embodiment/run/`
  The bounded execution workspace for the first cycle.

If any of these folders do not yet exist, they should be understood as the intended local execution boundary for the first embodiment rather than as permission to widen execution elsewhere.

## 6. Allowed Read Scope

The first run may read only what is required to execute and judge the selected first cycle.

Allowed read scope includes:

- the selected matter input in `embodiment/input/`
- the embodiment documents needed to define and judge the cycle
- the required schemas for the artifact families used by the selected cycle
- the required runtime and embodiment definitions needed to execute the cycle lawfully
- the bounded local files in `embodiment/run/`, `embodiment/output/`, and `embodiment/registry/` that are necessary for the first run and its audit

This means the run may read the repo as constitutional and operational reference where needed, but constitutional context does not mean arbitrary live access to everything on the machine.

The first run is not allowed to treat unrelated local files, unrelated projects, personal folders, or ambient machine state as default input.

## 7. Allowed Write Scope

The first run may write only what is required for the selected first cycle.

Allowed write scope includes:

- canonical artifacts into `embodiment/registry/`
- bounded runtime outputs necessary for the chosen first cycle into `embodiment/output/`
- bounded execution notes, logs, or run-local files into `embodiment/run/`, provided they do not pretend to be canonical truth

The first run should treat `embodiment/input/` as the bounded source surface, not as a convenience workspace for rewriting the matter during execution.

Canonical artifacts belong in the bounded embodiment registry surface. Derivative or supporting local outputs belong outside that canonical preservation path.

## 8. Explicitly Excluded Scope

The following are outside the scope of the first run:

- unrelated local machine files
- arbitrary personal folders
- external internet access unless explicitly justified later
- historical artifact ingestion not chosen as the first matter
- broad repo mutation
- private product integration
- public deployment surfaces

The first proof is not allowed to quietly become:

- a machine-wide run
- a network-dependent run
- a repo-wide mutation
- a product-integrated run
- a public-facing run

## 9. Relation to the Chosen First Slice

This boundary supports the selected first slice by keeping the run aligned to:

- the selected matter
- the selected first live cycle
- the required artifact family
- the success and failure criteria

The selected first slice is one internal-first governed truth-formation attempt for one bounded local note matter. That slice needs a narrow execution zone so that:

- the matter remains one matter
- the cycle remains one cycle
- the artifact family remains bounded
- the judgment criteria remain meaningful

Without this boundary, the first slice could widen until it no longer remains the slice that was selected.

## 10. Operator Posture

The operator should know what the run is allowed to touch before the run begins.

The operator should not widen scope ad hoc. If the run appears to require more access than defined here, then the embodiment boundary has not been respected and the first proof should not be treated as lawfully bounded.

The operator’s task is to preserve narrow operational honesty under wide constitutional guidance.

## 11. Anti-Collapse Rules

The following must not happen:

- the local run silently reads beyond the bounded matter or execution workspace
- outputs are written outside the canonical embodiment workspace without explicit reason
- derivative logs or convenience files are treated as canonical artifacts
- broad repo context is mistaken for broad runtime permission
- a hidden external dependency is introduced into the first proof
- the first proof is widened until it no longer remains a bounded slice

If any of these occur, execution scope has blurred and the first embodiment can no longer be judged as a narrow lawful proof.

## 12. What Remains Open

The following remain intentionally open for later execution work:

- the exact script names
- the exact command surface
- the exact local folder creation order
- the later public or interface posture
- the later broader integration boundaries

These are execution-design questions, not constitutional ambiguities.

## 13. Summary

This document defines the local execution boundary for IAMMAI’s first lawful embodiment slice as a narrow embodiment workspace governed by the full repo as constitutional context but limited in practice to one bounded matter, one bounded cycle, and one bounded set of read and write surfaces.

Its purpose is to keep the first proof operationally narrow enough to remain honest, auditable, and free of hidden widening into machine-wide, repo-wide, or network-wide execution.

**One-Line Definition:** `LOCAL_EXECUTION_BOUNDARY.md` defines the first embodiment execution boundary of IAMMAI as wide constitutional context with narrow local operational scope inside the bounded embodiment workspace.
