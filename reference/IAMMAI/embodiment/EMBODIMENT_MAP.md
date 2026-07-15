# IAMMAI Embodiment Map

## 1. Purpose

This file acts as the orientation map for the `embodiment/` folder.

Its job is to explain what the embodiment folder is for, how it relates to the constitutional core and the repo’s other layers, what the first-build chunk is trying to do, what files belong in this folder, what order to read them in, and what this layer does and does not try to solve yet.

It is not:

- code
- a deployment guide
- a product page
- a broad rollout workspace
- a substitute for the constitutional or runtime layers

It is a bounded embodiment-orientation document.

## 2. Relation to the Constitutional Core

The constitutional core remains the source of truth.

Embodiment artifacts derive from the constitutional protocol and do not supersede it. They exist to carry one bounded lawful slice into live form without redefining the law, the state grammar, the governance rules, the witness role, or the preservation rules.

If an embodiment artifact and the constitutional core diverge, the constitutional core governs.

## 3. Relation to the Architecture / Implementation / Schema / Runtime Layers

The repo layers relate as follows:

- the architecture layer defines the body and its main role separations
- the implementation layer defines the first technical derivatives of state, records, witness, governance, validation, and transition
- the schema family defines the first machine-checkable artifact surfaces
- the runtime layer defines motion, contracts, failures, coordination, and handoff
- the embodiment layer defines the first bounded live slice

This embodiment folder therefore does not replace the earlier layers. It takes their already-defined law and structure and gives them one bounded local workspace for first execution.

## 4. Why an Embodiment Folder Is Needed

A first live slice should have its own bounded workspace.

- The constitutional, architecture, implementation, schema, and runtime layers are primarily descriptive and constraining.
- The embodiment layer is where one selected lawful slice becomes an actual bounded first-build target.

Embodiment should remain distinct from the repo’s descriptive layers because first execution introduces choices about matter selection, local run posture, operator action, success observation, and failure visibility that should not be blurred into the underlying law.

The first proof should also not be confused with productization. A bounded embodiment workspace helps keep local lawful execution separate from UI theater, broad rollout pressure, or private implementation capture.

## 5. What Belongs in This Folder

This folder is intended to hold the first embodiment workspace.

Its intended file family includes:

- `EMBODIMENT_MAP.md`
  The orientation map for the embodiment layer.
- `FIRST_LIVE_CYCLE.md`
  The concrete local statement of the selected first cycle to be run in this folder.
- `MATTER_DEFINITION.md`
  The bounded definition of the one matter selected for the first embodiment.
- `SUCCESS_AND_FAILURE_CRITERIA.md`
  The concrete embodiment-facing success and failure conditions for the selected cycle.
- `OPERATOR_RUNBOOK.md`
  The bounded operator-facing instructions for running the first local cycle without expanding the embodiment scope.
- `input/`
  The bounded input surface for the selected matter and selected run.
- `output/`
  The bounded output surface for derivative local run results.
- `registry/`
  The local preservation surface for the canonical artifacts produced by the first embodiment.
- `run/`
  The local build and execution workspace for the first bounded cycle.

If any of these files or folders do not yet exist, they should be understood as the intended first embodiment workspace rather than as a requirement that the whole folder already be complete.

## 6. Reading Order

A clean reading order for the embodiment folder is:

1. `EMBODIMENT_MAP.md`
2. `FIRST_LIVE_CYCLE.md`
3. `MATTER_DEFINITION.md`
4. `SUCCESS_AND_FAILURE_CRITERIA.md`
5. `OPERATOR_RUNBOOK.md`
6. `input/`
7. `run/`
8. `output/`
9. `registry/`

This order moves from orientation, to selected cycle, to selected matter, to evaluation rules, to operator posture, and then into the bounded local execution surfaces.

## 7. Folder Boundary

This folder currently aims to do one thing: hold the first bounded embodiment workspace for one lawful local cycle.

It intentionally does not yet try to do:

- broad rollout
- private implementation privilege
- UI theater
- market-facing product capture
- full system completion claims
- generalized embodiment of the whole runtime family

This folder is for one bounded proof of lawful embodiment, not for proving everything at once.

## 8. First-Build Chunk Summary

This folder is for the first-build chunk that:

- selects one bounded matter
- defines one lawful local cycle
- runs one success path
- runs visible failure paths
- audits the resulting canonical artifacts

Its purpose is to make the first embodiment small enough to be real, auditable, and failure-visible without widening it into a platform or product posture.

## 9. Open Questions

The following remain intentionally open before the first local cycle is actually built and run:

- the exact host form
- the exact operator surface
- the exact local runtime implementation details
- internal-first versus selectively shareable posture after first run
- what build artifact comes first in `run/`

These are embodiment-build questions, not constitutional ambiguities.

## 10. Summary

This document defines the `embodiment/` folder as the bounded workspace in which IAMMAI’s first lawful live slice is oriented, specified, run, and audited without being widened into product form or confused with the repo’s descriptive layers.

Its purpose is to keep first embodiment local, execution-facing, and structurally lawful while the constitutional, architecture, implementation, schema, and runtime layers remain upstream sources of definition and constraint.

**One-Line Definition:** `EMBODIMENT_MAP.md` defines the embodiment folder as the bounded local workspace for IAMMAI’s first lawful live slice and its audit surfaces.
