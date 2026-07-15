# IAMMAI Integrity Host V0-Min World Assumptions

## 1. Purpose

This note extracts the world assumptions revealed by the current v0-min integrity host proof-slice.

It is derived from:

- `spec/INTEGRITY_HOST_V0_MIN_SPEC.md`
- `src/integrity_host_v0_min.py`
- `tests/test_integrity_host_v0_min.py`
- the visible reference surfaces under `reference/IAMMAI/`

Its purpose is to make explicit what the current proof host had to assume in order to run, what it actually proves, and what remains open beyond the host.

This note is not a constitutional rewrite, a full system/world-frame definition, a minimum lawful system declaration, a relation-layer doctrine, a presence doctrine, a runtime architecture rewrite, a roadmap, a README, or a manifesto.

## 2. Status and Rank

The current v0-min host now exists as a bounded runnable proof, not only as theory.

The host demonstrates that a small in-memory mechanism can preserve the integrity-kernel proof-slice in executable form. This note extracts the assumptions exposed by that runnable mechanism.

This note ranks below the constitutional protocol, the visible implementation and runtime reference surfaces, and the local v0-min host spec. It is additive. It does not replace or reinterpret those surfaces.

This note does not define minimum lawful system. It does not claim that the v0-min host is full IAMMAI embodiment, full runtime, final persistence architecture, or global system law.

## 3. Why This Note Is Needed Now

Before implementation, some host assumptions could remain implicit inside a proposed mechanism.

Once the host became runnable, those assumptions became inspectable:

- the host accepts specific object shapes
- the host enforces a specific phase compression
- the host keeps one unresolved open object at a time
- the host treats threshold as a guard rather than a stored phase
- the host requires explicit occurrence handling for presentation
- the host records every attempted action
- the host resolves only standing matter

These assumptions should be visible rather than hidden inside code.

This note separates:

- what the host proves
- what the host assumes
- what remains open beyond the host

The aim is not to widen doctrine. The aim is to preserve rank clarity after the first runnable proof.

## 4. What The Current Host Proves

In bounded form, the current host proves that:

- one local host can carry one matter-bound integrity object through `CANDIDATE -> PRESENT -> STANDING`
- `STAND` can be mechanized as distinct from `FINALIZE`
- `FINALIZE`, `INVALIDATE`, and `EVOLVE` can be enforced as standing-only resolutions
- HOLD can be represented as orthogonal permissibility, not as phase or resolution
- append-only transition records can preserve accepted and refused attempts
- refusal can be explicit, typed, and non-mutating
- `EVOLVE` can preserve an explicit predecessor/successor relation
- resolved standing matter can remain preserved without in-place semantic overwrite

This proves hostability of the kernel slice. It does not prove full system completion, full embodiment, distributed behavior, final relation law, or final presence doctrine.

## 5. Host-Local World Assumptions

The current host makes the following assumptions in order to run.

### 5.1 Matter / Object Assumption

The host assumes that one explicit matter-bound object is the current unit of movement.

The object carries:

- `object_id`
- `matter_ref`
- `payload_ref`
- phase posture
- resolution posture
- occurrence reference when present
- predecessor reference when created by evolution
- creation and resolution record references

The host does not model the full world around the matter. It assumes `matter_ref` and `payload_ref` are already meaningful enough for bounded local handling.

### 5.2 Host Boundary Assumption

The host assumes one local host as the execution boundary.

The host has one `host_id`, one in-memory `HostState`, one object map, one HOLD posture, and one append-only record tuple. It does not model host-to-host relation, carrier-to-carrier continuity, distributed agreement, shared authority, or external registry behavior.

### 5.3 Openness Assumption

The host assumes one unresolved open object at a time.

It refuses creation of a second unresolved open object while one current object remains open as candidate, present, or unresolved standing.

This is a host-local proof simplification. It is not global IAMMAI law and does not settle how larger systems handle many concurrent matters.

### 5.4 Phase Assumption

The host compresses movement to:

`CANDIDATE -> PRESENT -> STANDING`

This preserves the anti-collapse seam between candidate material, present occurrence, and standing state. It does not implement the full preparation regime or the full standing-state regime.

The host does not separately mechanize signal, acceptance, scope, threshold, truth, continuity, decision, or consequence as full runtime phases.

### 5.5 Threshold Assumption

The host treats threshold as a guard on `STAND`.

The host requires a non-empty `threshold_basis_ref` and a passing threshold predicate before present material may enter standing. It does not store `THRESHOLD` as a separate host phase.

This preserves the visible reference distinction that threshold is not truth. It does not settle final threshold representation for a larger runtime.

### 5.6 Presence / Occurrence Assumption

The host requires explicit occurrence handling before presentation.

`PRESENT` requires a non-empty `occurrence_ref` and `basis_ref`. The object remains unresolved and non-standing after presentation.

This confirms that presence matters to the proof host. It does not settle full presence doctrine, event doctrine, or all possible ways occurrence may be witnessed, validated, or preserved in later runtime work.

### 5.7 HOLD Assumption

The host assumes HOLD is a local orthogonal permissibility control.

An active HOLD binds to one target object and blocks `STAND`, `FINALIZE`, `INVALIDATE`, and `EVOLVE` on that target. Setting or releasing HOLD appends records but does not change phase or resolution.

The host does not settle all possible containment targets, all authority requirements for HOLD, or all runtime patterns for HOLD across carriers.

### 5.8 Resolution Assumption

The host assumes resolution is closed and standing-only.

The only resolution types are:

- `FINALIZE`
- `INVALIDATE`
- `EVOLVE`

Candidate and present material cannot be resolved. Resolved standing cannot be resolved again.

This appears required by the visible body. The host does not define all consequences of each resolution in a full runtime or world frame.

### 5.9 Lineage Assumption

The host assumes that lawful correction or change after standing requires explicit successor relation.

`EVOLVE` resolves the predecessor standing object and creates a successor candidate with `predecessor_object_id`. The successor does not inherit standing.

This preserves no-overwrite behavior. It does not define a full relation layer among many predecessors, many successors, branches, merges, or cross-host successors.

### 5.10 Trace Assumption

The host assumes every attempted action must remain reconstructable through append-only records.

Accepted and refused actions both append transition records. Records preserve action type, object relation, predecessor/successor relation where relevant, source and target posture, basis references, HOLD before/after, outcome, refusal code where relevant, and timestamp.

This proves local reconstructability. It does not settle final registry design, storage enforcement, event sourcing, signatures, witness artifacts, or long-term persistence.

## 6. What Appears Host-Local Only

The following are proof-host simplifications only:

- one local host as the whole execution boundary
- one current open object at a time
- in-memory state as the preservation surface
- one local HOLD posture
- local object ids and record ids
- one compressed object grammar
- threshold represented only as a guard argument
- refusal codes as a local closed enum
- transition records kept as an in-memory tuple
- absence of separate validator, governor, witness emitter, registry, and interface components

These choices make the proof slice runnable and inspectable. They must not be promoted into global IAMMAI law.

## 7. What Appears Semantically Required

The following are not merely incidental host choices. They are supported by the visible constitutional, implementation, runtime, and local proof surfaces:

- candidate material must not silently become standing
- present occurrence must not silently become standing
- standing entry must be explicit and guarded
- `STAND` must remain distinct from `FINALIZE`
- resolution must be closed to `FINALIZE`, `INVALIDATE`, and `EVOLVE`
- resolution must apply only to standing matter
- HOLD must remain orthogonal to phase and resolution
- refused action must remain visible where it matters
- transition trace must preserve visible movement and non-movement
- evolution must preserve predecessor/successor relation
- correction must not overwrite standing matter in place

These are the anti-collapse commitments the host preserves. This note does not expand them into a full system doctrine.

## 8. Relation Pressure Exposed By The Host

The current host exposes relation questions without answering them.

The one-open-object simplification avoids relation among concurrent open objects. A larger mechanism will need to decide how many candidate, present, unresolved standing, and resolved standing matters may coexist, and how their relations are represented without collapsing them.

The host also leaves open:

- how objects relate when they share a matter
- how objects relate when matters overlap
- how successor chains relate beyond one predecessor and one successor
- how multiple hosts relate to the same or adjacent matters
- how local records relate to later registry records
- how local HOLD posture relates to broader containment authority
- how context is identified when more than one host, carrier, or matter is active

These are relation pressures, not settled relation doctrine.

## 9. System Pressure Exposed By The Host

The current host is not minimum lawful system.

Because the host now runs, it exposes legitimate system questions for later work:

- multiplicity: how many matters, objects, hosts, or kernel slices may coexist
- coexistence: how concurrent open matters avoid silent collapse or hidden priority
- relation between standing matters: how standing objects affect, depend on, succeed, or contradict one another
- host-to-host continuity: how a state or transition remains continuous across hosts or carriers
- persistence beyond local memory: how append-only preservation becomes durable without flattening record types
- context/world boundary: what counts as the relevant bounded context beyond one local host
- runtime role separation: what additional conditions are needed when validator, witness, governor, registry, and interface roles are separated

The host currently assumes these away. That is lawful for the proof-slice. It is not enough for a larger lawful system.

## 10. Presence Boundary

Presence is materially important in the current host.

The host requires explicit `occurrence_ref` handling before an object can become `PRESENT`, and standing cannot occur until the object is present. This preserves the seam between admitted candidate material and matter-bound occurrence.

Presence may later prove to be a cross-layer continuity seam because it touches candidate handling, occurrence, threshold eligibility, trace, and later standing entry.

This note does not settle presence doctrine. It does not define all forms of occurrence, all witness requirements, all event boundaries, or all relation between presence and context. It only records that the current runnable host could not preserve the proof-slice without an explicit presentation/occurrence seam.

## 11. Explicit Non-Claims

This note does not define:

- full IAMMAI system or world-frame
- full relation layer
- full presence doctrine
- full event doctrine
- many-kernel coexistence law
- final multiplicity law
- final persistence architecture
- final runtime embodiment
- distributed host or cross-carrier law
- final context/world ontology
- final validator, governor, witness, registry, or interface design
- product behavior
- deployment posture

This note also does not claim that the v0-min host is the minimum lawful system or the first full embodiment cycle.

## 12. Closing Boundary Statement

The current v0-min host is a lawful bounded proof-slice.

This note exists to expose the world assumptions hidden inside that runnable slice: one local host, one matter-bound object, one unresolved open object, compressed phase movement, guarded standing entry, orthogonal HOLD, standing-only resolution, explicit lineage, and append-only trace.

Later work may derive wider relation, multiplicity, persistence, runtime, and context questions from these assumptions.

This note itself does not settle those wider questions.
