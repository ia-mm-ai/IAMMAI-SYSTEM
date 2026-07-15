# IAMMAI Integrity Host V0 Minimum Spec

## 1. Purpose

This file defines the first bounded executable proof-slice for IAMMAI-SYSTEM.

Its purpose is to specify the smallest host mechanism that can carry one integrity-kernel proof-slice in runnable form while preserving the corrected kernel distinctions:

- candidate material is not present occurrence
- present occurrence is not standing
- standing entry is distinct from standing resolution
- HOLD is orthogonal containment
- resolution is standing-only and closed
- EVOLVE preserves explicit predecessor relation
- trace is append-only
- refusal is explicit

This is a hostability proof only.

It is not a constitutional rewrite, a full runtime architecture, a database design, a product design, a deployment plan, a README, or a manifesto.

## 2. Status and Rank

This file is a first executable proof-slice spec.

It ranks below the visible constitutional, implementation, runtime, and architecture surfaces. It derives from them and must not be read as replacing them.

This file defines:

- the first host-local mechanism that can execute one bounded integrity-kernel path
- the minimum object and transition grammar needed for that path
- the refusal posture needed to keep the path from collapsing into convenience behavior
- the proof expectations that a later implementation can turn into executable tests

This file does not define:

- the minimum lawful IAMMAI system
- the first full embodiment cycle
- the full standing-state regime
- the full truth, continuity, decision, and consequence chain
- final runtime admission
- final persistence architecture
- universal system law

The rank of this file is therefore: bounded hostability proof-slice, not full embodiment and not minimum lawful system.

## 3. Why This Slice Exists

The visible reference body already supports an integrity kernel that preserves phase order, preparation versus standing-state distinction, orthogonal HOLD, closed typed resolution, lineage-preserving succession, and trace recoverability.

The next code-ready step is smaller than a full runtime body. It is to prove that the kernel can be hosted by a minimal local mechanism without collapsing:

- `PRESENT -> STANDING` into finalization
- threshold eligibility into a stored standing phase
- HOLD into semantic state
- INVALIDATE into pre-standing rejection
- EVOLVE into in-place overwrite
- refusal into silent no-op
- trace into final state only

This slice exists to freeze that first runnable host boundary.

## 4. Host-Local Simplification

The V0 proof host is intentionally local and narrow.

Host-local assumptions:

- one local host
- one local open matter at a time
- one current open `IntegrityObject` at a time
- append-only local transition record list
- no distributed coordination
- no cross-carrier behavior
- no final database or storage topology
- no final runtime component split

`one local open matter at a time` means the host refuses to create a second unresolved object while one object remains open as `CANDIDATE`, `PRESENT`, or unresolved `STANDING`.

This is a proof-slice simplification only. It is not IAMMAI system law. It does not claim that IAMMAI globally permits only one matter, one host, one carrier, or one open object.

Resolved standing matter remains preserved. It does not block creation of a later unrelated candidate in this host unless a later implementation chooses a stricter local policy.

## 5. Minimum Object Grammar

The grammar below is implementation-facing. It is not a final schema, database model, transport format, or storage design.

### 5.1 IntegrityObject

`IntegrityObject` is the host-local object whose phase and resolution posture are governed by this proof-slice.

Minimum shape:

```text
IntegrityObject {
  object_id: string
  matter_ref: string
  payload_ref: string
  phase_state: CANDIDATE | PRESENT | STANDING
  resolution_type: null | FINALIZE | INVALIDATE | EVOLVE
  predecessor_object_id: string | null
  created_by_record_id: string
  entered_phase_by_record_id: string
  resolved_by_record_id: string | null
}
```

Rules:

- `object_id` is stable after creation.
- `matter_ref` is explicit and non-null.
- `payload_ref` identifies the bounded material carried by the object. This spec does not define payload storage.
- `phase_state` starts as `CANDIDATE`.
- `resolution_type` starts as `null`.
- `predecessor_object_id` is non-null only for a successor object created by `EVOLVE`.
- `resolved_by_record_id` is non-null only after a standing resolution.
- candidate and present objects must have `resolution_type: null`.
- resolved standing objects remain preserved and must not be semantically mutated in place.

### 5.2 HostState

`HostState` is the minimum local host posture needed to run the slice.

Minimum shape:

```text
HostState {
  host_id: string
  current_open_object_id: string | null
  objects: Map<object_id, IntegrityObject>
  transition_records: AppendOnlyList<TransitionRecord>
  hold: {
    active: boolean
    target_object_id: string | null
    basis_ref: string | null
    set_by_record_id: string | null
  }
}
```

Rules:

- `current_open_object_id` may point to one unresolved object only.
- `objects` preserves all objects known to the host, including resolved standing objects.
- `transition_records` is append-only.
- `hold` is a permissibility control, not object phase and not resolution.
- this shape may be represented in memory for a proof host; that does not settle persistence architecture.

### 5.3 TransitionRecord

`TransitionRecord` preserves requested movement, accepted movement, and explicit refusal.

Minimum shape:

```text
TransitionRecord {
  record_id: string
  host_id: string
  action_type: CREATE_OBJECT | PRESENT | STAND | FINALIZE | INVALIDATE | EVOLVE | SET_HOLD | RELEASE_HOLD
  matter_ref: string
  object_id: string | null
  predecessor_object_id: string | null
  successor_object_id: string | null
  source_phase_state: CANDIDATE | PRESENT | STANDING | null
  target_phase_state: CANDIDATE | PRESENT | STANDING | null
  source_resolution_type: null | FINALIZE | INVALIDATE | EVOLVE
  target_resolution_type: null | FINALIZE | INVALIDATE | EVOLVE
  threshold_basis_ref: string | null
  basis_ref: string | null
  hold_before: boolean
  hold_after: boolean
  accepted: boolean
  refusal_code: string | null
  acted_at: string
}
```

Rules:

- a refused request still emits a `TransitionRecord`.
- `accepted: false` is not a resolution type.
- `refusal_code` is a host conformance response, not a hidden fourth kernel outcome.
- `threshold_basis_ref` may appear on `STAND`; it must not create a stored `THRESHOLD` phase in this proof host.
- `predecessor_object_id` and `successor_object_id` are required on accepted `EVOLVE`.
- records preserve visible passage and refusal, not only final state.

### 5.4 ConformanceResult

`ConformanceResult` is the immediate host response to an attempted action.

Minimum shape:

```text
ConformanceResult {
  accepted: boolean
  record_id: string
  object_id: string | null
  successor_object_id: string | null
  refusal_code: string | null
  state_changed: boolean
}
```

Rules:

- every attempted action returns one `ConformanceResult`.
- every `ConformanceResult.record_id` points to an appended `TransitionRecord`.
- `accepted: true` means the requested action was applied by the host.
- `accepted: false` means the request was refused and no semantic state movement occurred.
- `state_changed: false` is required for refused requests.
- refusal is explicit host behavior. It is not `FINALIZE`, `INVALIDATE`, `EVOLVE`, or a fourth resolution outcome.

## 6. Phase State and Resolution Type

The proof host has exactly three phase states:

`phase_state ∈ {CANDIDATE, PRESENT, STANDING}`

The proof host has exactly one nullable resolution field:

`resolution_type ∈ {null, FINALIZE, INVALIDATE, EVOLVE}`

Rules:

- `CANDIDATE` means bounded material has entered host handling for a matter.
- `PRESENT` means the candidate has become a non-null matter-bound occurrence in this host slice.
- `STANDING` means the object entered standing through explicit `STAND`.
- `FINALIZE`, `INVALIDATE`, and `EVOLVE` are resolution types, not phases.
- `null` means no standing resolution has been applied.
- there is no `HELD`, `INVALID`, `FINAL`, `EVOLVED`, `ARCHIVED`, or `DELETED` phase.
- there is no `PENDING`, `EXPIRED`, `SUPERSEDED`, `DISMISSED`, `UPDATED`, or `CLOSED` resolution.

## 7. Unresolved and Resolved Standing

This slice keeps standing entry distinct from standing resolution.

Definitions:

- unresolved standing = `phase_state: STANDING` with `resolution_type: null`
- resolved standing = `phase_state: STANDING` with exactly one closed resolution type

Resolved standing types:

- `phase_state: STANDING`, `resolution_type: FINALIZE`
- `phase_state: STANDING`, `resolution_type: INVALIDATE`
- `phase_state: STANDING`, `resolution_type: EVOLVE`

Rules:

- `FINALIZE` does not create standing.
- `INVALIDATE` does not create standing.
- `EVOLVE` does not create standing for the predecessor.
- all three resolution actions apply only to unresolved standing.
- candidate and present material cannot be finalized, invalidated, or evolved.
- resolved standing matter cannot be reopened or semantically mutated in place.

## 8. HOLD Orthogonality

HOLD is orthogonal containment.

In this proof host:

- HOLD is not a phase.
- HOLD is not a resolution.
- HOLD affects permissibility only.
- HOLD must not become hidden kernel branching.
- HOLD must not create `HELD_CANDIDATE`, `HELD_PRESENT`, `HELD_STANDING`, or equivalent encoded phases.
- HOLD must not create `HOLD`, `BLOCKED`, `PAUSED`, or equivalent resolution types.

Host-local HOLD rule:

- an active HOLD on the current object blocks `STAND`, `FINALIZE`, `INVALIDATE`, and `EVOLVE`.
- `SET_HOLD` and `RELEASE_HOLD` are the only actions that may change the host HOLD posture.
- releasing HOLD restores permissibility only. It does not create presence, standing, or resolution.

This rule is a proof-slice simplification. It does not settle the final model for all containment targets or all runtime carriers.

## 9. Allowed Actions

The proof host accepts only the following action family:

- `CREATE_OBJECT`
- `PRESENT`
- `STAND`
- `FINALIZE`
- `INVALIDATE`
- `EVOLVE`
- `SET_HOLD`
- `RELEASE_HOLD`

No other action has protocol effect in this slice.

An implementation may expose these actions through any local interface for proof purposes, but interface naming must map back to this closed action family. Convenience verbs such as `update`, `close`, `archive`, `delete`, `approve`, `reject`, or `supersede` must not become canonical action behavior.

## 10. Transition and Guard Rules

### 10.1 CREATE_OBJECT

Accepted only if:

- the request carries non-null `matter_ref`
- the request carries non-null `payload_ref`
- the host has no current unresolved open object

Effect:

- create one `IntegrityObject`
- set `phase_state: CANDIDATE`
- set `resolution_type: null`
- set `predecessor_object_id: null`
- set `current_open_object_id` to the new object
- append a `TransitionRecord`

Refuse if:

- matter is missing
- payload is missing
- another unresolved object is already open

### 10.2 PRESENT

Accepted only if:

- the target object exists
- the target object is the current open object
- `phase_state: CANDIDATE`
- `resolution_type: null`
- the request carries a non-null occurrence or occurrence basis

Effect:

- move `phase_state` from `CANDIDATE` to `PRESENT`
- leave `resolution_type: null`
- append a `TransitionRecord`

Refuse if:

- the target is not candidate
- occurrence basis is missing
- the request attempts to skip directly to standing

### 10.3 STAND

Accepted only if:

- the target object exists
- the target object is the current open object
- `phase_state: PRESENT`
- `resolution_type: null`
- the request carries `threshold_basis_ref`
- the host threshold predicate passes
- no active HOLD blocks the transition

Effect:

- move `phase_state` from `PRESENT` to `STANDING`
- leave `resolution_type: null`
- append a `TransitionRecord`

Rules:

- `PRESENT -> STANDING` occurs via `STAND`.
- `FINALIZE` is not the transition into standing.
- threshold is a guard or predicate on `STAND`.
- threshold is not stored as an explicit host phase in this proof slice.

Refuse if:

- the target is `CANDIDATE`
- the target is already `STANDING`
- threshold basis is missing
- threshold predicate fails
- active HOLD blocks the transition

### 10.4 FINALIZE

Accepted only if:

- the target object exists
- `phase_state: STANDING`
- `resolution_type: null`
- no active HOLD blocks the action
- the request carries non-null `basis_ref`

Effect:

- set `resolution_type: FINALIZE`
- clear `current_open_object_id` if it points to the target
- append a `TransitionRecord`

Rules:

- finalization is resolution of unresolved standing.
- finalization is not standing entry.
- finalization does not erase trace or create a successor by default.

### 10.5 INVALIDATE

Accepted only if:

- the target object exists
- `phase_state: STANDING`
- `resolution_type: null`
- no active HOLD blocks the action
- the request carries non-null `basis_ref`

Effect:

- set `resolution_type: INVALIDATE`
- clear `current_open_object_id` if it points to the target
- append a `TransitionRecord`

Rules:

- invalidation is standing-only resolution.
- invalidation removes current standing force without deleting the prior standing object or its records.
- invalidation must not extend into candidate or present material.
- there is no fake invalid phase.

### 10.6 EVOLVE

Accepted only if:

- the target predecessor object exists
- predecessor `phase_state: STANDING`
- predecessor `resolution_type: null`
- no active HOLD blocks the action
- the request carries non-null `basis_ref`
- the request carries non-null successor `payload_ref`

Effect:

- set predecessor `resolution_type: EVOLVE`
- create one successor `IntegrityObject`
- set successor `phase_state: CANDIDATE`
- set successor `resolution_type: null`
- set successor `predecessor_object_id` to predecessor `object_id`
- set `current_open_object_id` to the successor object
- append a `TransitionRecord` with predecessor and successor references

Rules:

- evolution resolves the predecessor standing object and creates a successor candidate.
- evolution is not in-place correction.
- successor creation without explicit predecessor relation is refused.
- the successor does not inherit standing automatically.
- the successor must move through `PRESENT` and `STAND` under the ordinary guards if it is to stand.

### 10.7 SET_HOLD

Accepted only if:

- the target object exists
- no host HOLD is currently active
- the request carries non-null `basis_ref`

Effect:

- set `hold.active: true`
- set `hold.target_object_id` to the target
- set `hold.basis_ref`
- append a `TransitionRecord`

Rules:

- setting HOLD does not change `phase_state`.
- setting HOLD does not change `resolution_type`.
- setting HOLD does not resolve the matter.

### 10.8 RELEASE_HOLD

Accepted only if:

- a host HOLD is active
- the release targets the held object
- the request carries non-null `basis_ref`

Effect:

- set `hold.active: false`
- clear `hold.target_object_id`
- clear `hold.basis_ref`
- append a `TransitionRecord`

Rules:

- releasing HOLD restores permissibility only.
- release does not create presence, standing, finalization, invalidation, or evolution.

## 11. Refusal and Anti-Collapse Rules

The proof host must refuse the following requests and append a refusal record.

Standing-entry refusals:

- `STAND(CANDIDATE)`
- `STAND(PRESENT)` with missing threshold basis
- `STAND(PRESENT)` when threshold predicate fails
- `STAND(PRESENT)` while active HOLD blocks the transition
- any attempt to enter `STANDING` without `STAND`

Standing-resolution refusals:

- `FINALIZE(CANDIDATE)`
- `FINALIZE(PRESENT)`
- `INVALIDATE(CANDIDATE)`
- `INVALIDATE(PRESENT)`
- `EVOLVE(CANDIDATE)`
- `EVOLVE(PRESENT)`
- `FINALIZE`, `INVALIDATE`, or `EVOLVE` on already resolved standing matter
- `FINALIZE`, `INVALIDATE`, or `EVOLVE` while active HOLD blocks the action

Mutation and deletion refusals:

- attempts to mutate resolved standing matter in place
- attempts to overwrite a predecessor with successor content
- attempts to delete objects
- attempts to delete, rewrite, reorder, or compact prior transition records
- attempts to clear lineage by editing object fields or records

HOLD collapse refusals:

- attempts to store HOLD as `phase_state`
- attempts to store HOLD as `resolution_type`
- attempts to treat HOLD release as standing entry
- attempts to treat HOLD release as resolution
- attempts to branch into hidden held phases or held resolutions

Resolution-family refusals:

- attempts to create a non-canonical resolution type
- attempts to map `archive`, `close`, `dismiss`, `expire`, `reject`, `supersede`, `update`, or `delete` onto resolution behavior
- attempts to treat refusal as a resolution outcome
- attempts to introduce a hidden fourth outcome

Lineage refusals:

- accepted `EVOLVE` without successor creation
- accepted `EVOLVE` without predecessor relation
- successor candidate with no explicit predecessor when created by evolution
- orphan successor standing created by name, timestamp, or narrative relation alone

Host-boundary refusals:

- attempts to create a second open object while the host already has one unresolved open object
- attempts to treat the one-open-matter simplification as global IAMMAI law
- attempts to treat this proof host as the minimum lawful system

## 12. Lineage and Append-Only Trace

Lineage rule:

- `EVOLVE` creates a successor candidate with explicit `predecessor_object_id`.
- the predecessor is resolved as `STANDING` with `resolution_type: EVOLVE`.
- the successor starts as `CANDIDATE`.
- no standing force transfers silently from predecessor to successor.

Append-only trace rule:

- every attempted action appends exactly one `TransitionRecord`.
- accepted state movement appends a record before the host reports success.
- refused movement appends a record before the host reports refusal.
- prior records must not be deleted, rewritten, reordered, or compacted as a semantic operation.

The record list exists to preserve visible passage. It is not only an audit convenience and not only a way to reconstruct final state.

Minimum reconstruction expectation:

- a reader can see what action was requested
- a reader can see whether it was accepted or refused
- a reader can see source and target phase or resolution posture
- a reader can see the threshold basis used for `STAND` when applicable
- a reader can see active HOLD posture before and after the attempt
- a reader can see predecessor and successor relation for `EVOLVE`
- a reader can distinguish standing entry from standing resolution

## 13. Proof Expectations / Test Families

These are proof expectations for later executable tests. This file does not create tests.

### 13.1 Standing-Entry Path

Expected valid path:

1. `CREATE_OBJECT`
2. `PRESENT`
3. `STAND` with passing threshold basis and no active HOLD

Expected proof:

- object starts as `CANDIDATE`
- object moves to `PRESENT`
- object moves to unresolved `STANDING`
- `resolution_type` remains `null`
- threshold basis is recorded on the `STAND` record
- `FINALIZE` is not used to enter standing
- all records are appended in order

### 13.2 Finalization of Standing Matter

Expected valid path:

1. create unresolved standing object through the standing-entry path
2. `FINALIZE`

Expected proof:

- finalization applies only after `STANDING`
- final object posture is `phase_state: STANDING`, `resolution_type: FINALIZE`
- prior records remain visible
- no successor is created by default
- later in-place mutation is refused

### 13.3 Invalidation of Standing Matter

Expected valid path:

1. create unresolved standing object through the standing-entry path
2. `INVALIDATE`

Expected proof:

- invalidation applies only after `STANDING`
- final object posture is `phase_state: STANDING`, `resolution_type: INVALIDATE`
- trace remains preserved
- the object is not deleted
- candidate and present invalidation attempts are refused

### 13.4 Evolution Into Successor Candidate

Expected valid path:

1. create unresolved standing predecessor through the standing-entry path
2. `EVOLVE` with successor payload

Expected proof:

- predecessor remains preserved
- predecessor posture becomes `phase_state: STANDING`, `resolution_type: EVOLVE`
- successor object is created as `phase_state: CANDIDATE`, `resolution_type: null`
- successor carries `predecessor_object_id`
- successor does not stand automatically
- predecessor and successor relation is visible in the appended record

### 13.5 HOLD Orthogonality

Expected valid path:

1. create object
2. set HOLD on that object
3. attempt blocked `STAND` or standing resolution
4. release HOLD
5. retry eligible action

Expected proof:

- HOLD changes only host permissibility posture
- blocked action is refused with a record
- HOLD does not change phase
- HOLD does not change resolution
- release does not create state movement by itself
- eligible action after release still has to satisfy its ordinary guards

### 13.6 Refusal Cases

Expected refusal families:

- `STAND(CANDIDATE)`
- `STAND(PRESENT)` when threshold basis is missing
- `STAND(PRESENT)` when threshold predicate fails
- `FINALIZE(PRESENT)`
- `INVALIDATE(PRESENT)`
- `EVOLVE(PRESENT)`
- resolution of candidate material
- resolution of already resolved standing matter
- in-place mutation of resolved standing matter
- deletion of objects or prior records
- HOLD encoded as phase or resolution
- non-canonical resolution behavior
- EVOLVE without explicit predecessor relation
- second open object creation during an unresolved open matter

Expected proof:

- each refused request returns `accepted: false`
- each refused request appends one refusal record
- no refused request changes semantic object posture
- refusal is not treated as resolution

## 14. Invariants

The proof host must preserve these invariants.

Phase and resolution separation:

- phase and resolution are separate fields.
- phase movement is limited to `CANDIDATE -> PRESENT -> STANDING`.
- resolution is limited to `null -> FINALIZE`, `null -> INVALIDATE`, or `null -> EVOLVE` on standing matter.

Standing-only resolution:

- `FINALIZE`, `INVALIDATE`, and `EVOLVE` apply only to unresolved standing.
- pre-standing material cannot be resolved.

HOLD orthogonality:

- HOLD is not phase.
- HOLD is not resolution.
- HOLD affects permissibility only.

Threshold guard:

- threshold is checked as a guard on `STAND`.
- threshold is not a stored explicit host phase in this proof slice.

Append-only trace:

- every attempted action appends a record.
- previous records are never deleted, rewritten, or reordered.

Resolved matter immutability:

- resolved standing matter is not semantically mutated in place.
- later correction must use explicit successor relation where evolution is lawful.

Explicit successor relation:

- accepted `EVOLVE` creates successor candidate with predecessor relation.
- successor standing cannot be inferred by timestamp, name, or narrative continuity.

Closed resolution family:

- the only resolution types are `FINALIZE`, `INVALIDATE`, and `EVOLVE`.
- refusal, hold, archive, deletion, and generic update are not resolution types.

Host-local simplification boundary:

- one local host and one local open matter are proof-slice simplifications only.
- they are not global IAMMAI system law.

Rank boundary:

- this host slice is not the minimum lawful system.
- this host slice is not the first full embodiment cycle.
- this host slice does not complete the full standing-state regime.

## 15. Explicit Non-Claims

This file does not define:

- the full IAMMAI system or world-frame
- multiplicity or many-kernel coexistence law
- full relation layer
- full presence doctrine
- full event doctrine
- final persistence architecture
- final runtime admission
- full embodiment, governor, and witness cycle
- final validator internals
- final registry or storage design
- distributed or cross-carrier system behavior
- full contribution-role grammar
- full governance ontology
- product behavior
- deployment posture
- UI or API design
- universal system law

This file also does not claim that a host implementing this proof slice is IAMMAI complete.

## 16. Closing Boundary Statement

`INTEGRITY_HOST_V0_MIN_SPEC.md` defines the smallest bounded local host mechanism needed to run one integrity-kernel proof-slice without collapsing phase, standing entry, resolution, HOLD, lineage, trace, or refusal.

It proves only hostability of the kernel slice.

It does not prove full IAMMAI embodiment, does not define the minimum lawful system, and does not promote host-local simplifications into constitutional law.
