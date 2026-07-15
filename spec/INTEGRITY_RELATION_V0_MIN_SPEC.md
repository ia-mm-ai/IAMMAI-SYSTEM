# IAMMAI Relation V0-Min Spec

## 1. Purpose

This file defines the first code-ready relation spec for the selected v0-min relation lane: bounded same-host multiplicity / coexistence.

It derives from:

- the completed v0-min integrity host proof-slice
- `spec/INTEGRITY_HOST_V0_MIN_WORLD_ASSUMPTIONS.md`
- `spec/INTEGRITY_RELATION_V0_MIN_BOUNDARY.md`
- the visible reference surfaces under `reference/IAMMAI/`

Its purpose is to define the smallest lawful same-host coexistence model that can be derived after the current host proof without reopening that host proof or widening into full system work.

This spec answers, in bounded first-pass form:

- what multiplicity is allowed inside one host
- what multiplicity remains refused
- what explicit relation marking is required when more than one unresolved object exists
- how coexistence affects open objects, standing objects, HOLD, records, and refusal
- what remains out of scope after this relation slice

This file is not a constitutional rewrite, full relation doctrine, full many-kernel coexistence law, full system/world-frame definition, minimum lawful system declaration, presence doctrine note, runtime architecture rewrite, roadmap, README, manifesto, or project-management note.

## 2. Status and Rank

This is the first bounded same-host coexistence spec.

It ranks below the constitutional protocol, the visible implementation and runtime reference surfaces, the v0-min host spec, the v0-min host implementation and tests, the world-assumptions note, and the relation-boundary selection note.

This spec does not invalidate the completed v0-min host slice. That host remains valid at its own rank as a one-open-object hostability proof.

This spec defines the next derivation boundary only: a successor host line may use it to implement bounded same-host coexistence. It does not define the full relation layer, final multiplicity law, full presence doctrine, cross-host continuity, persistence architecture, registry design, or minimum lawful system.

## 3. Why This Spec Is Needed Now

The current host stands at its own rank. It proves that one local host can carry one integrity object through `CANDIDATE -> PRESENT -> STANDING`, preserve standing-only resolution, keep HOLD orthogonal, record every attempt, refuse explicitly, and preserve predecessor relation on `EVOLVE`.

The current host avoids multiplicity through a one-open-object simplification. That simplification was lawful for hostability proof, but it leaves relation pressure exposed.

`INTEGRITY_RELATION_V0_MIN_BOUNDARY.md` selected bounded same-host multiplicity / coexistence as the first lawful relation lane. The body now needs one code-ready coexistence spec rather than more abstract discussion.

This spec exists to make the next implementation target small, explicit, and testable.

## 4. What Now Stands

The prior slice now materially has:

- a runnable host proof-slice
- tested phase movement through `CANDIDATE -> PRESENT -> STANDING`
- standing-entry distinct from standing-resolution
- standing-only `FINALIZE`, `INVALIDATE`, and `EVOLVE`
- orthogonal HOLD
- explicit predecessor relation on `EVOLVE`
- append-only records and explicit refusal
- a world-assumptions note exposing host-local assumptions
- a relation-boundary note selecting same-host coexistence as the next lane

This is enough to derive a bounded same-host relation spec. It is not enough to claim full relation doctrine or full IAMMAI system closure.

## 5. Candidate Same-Host Coexistence Shapes

### 5.1 Keep Global One-Open-Object

This shape keeps the current host rule unchanged: only one unresolved open object may exist in one host at a time.

It is visible and already proven. It remains lawful as the completed hostability slice.

It is not the best next relation step because it does not answer the pressure selected by the boundary note. It preserves proof-host simplicity but adds no real coexistence model.

Risk: relation remains avoided rather than specified.

### 5.2 Bounded Multiplicity With Tightly Governed Unresolved Openness

This shape allows more than one object in one host and allows more than one unresolved object only under explicit same-host coexistence guards.

It is the nearest lawful extension because it derives directly from the one-open-object simplification without jumping to cross-host continuity, persistence architecture, or world-boundary modeling.

Risk: if the guards are too loose, same-host coexistence can hide contradiction, priority, or replacement. That risk is controlled by requiring explicit relation marking and refusing same-matter unresolved coexistence in this first pass.

### 5.3 Broad Unrestricted Multiple Open Objects

This shape allows any number of unresolved objects in one host with minimal relation marking.

It is visible because a larger host will eventually need multiplicity, but it is not lawful as the immediate next step.

Risk: unresolved objects could silently contradict one another, share a matter without visible relation, create hidden priority by ordering, or let storage convention decide what counts. This would collapse relation into implementation convenience.

## 6. Selected First-Pass Coexistence Model

This spec selects the narrowest lawful coexistence extension beyond the current host:

**bounded distinct-matter same-host coexistence**

The selected model is:

- multiple objects may exist in one host
- resolved standing objects are preserved and may coexist as trace
- more than one unresolved open object may coexist only when each unresolved object is bound to a distinct matter and the coexistence relation is explicitly marked
- same-matter unresolved coexistence is refused in this first pass
- known or asserted overlapping-matter unresolved coexistence is refused in this first pass
- `EVOLVE` remains the only same-matter successor path currently accepted
- relation must be visible in records, not inferred from object names, timestamps, storage order, or narrative continuity

This model preserves the completed host slice as valid at its original rank. It does not say that IAMMAI globally allows only distinct-matter unresolved coexistence. It only defines the first host-local relation step after the v0-min proof host.

## 7. Coexistence Scope

### 7.1 Host Boundary

All rules in this spec apply inside one local host boundary only.

They do not define cross-host continuity, distributed coordination, registry relation, or global system law.

### 7.2 Object Existence

More than one object may exist in one host.

The host must preserve all objects it has accepted, including:

- candidate objects
- present objects
- unresolved standing objects
- resolved standing objects
- successor candidates created by `EVOLVE`

No accepted object may be deleted, overwritten, or treated as replaced by a later object.

### 7.3 Open Objects

For this spec:

- unresolved object = an object with `resolution_type: null`
- open object = unresolved `CANDIDATE`, unresolved `PRESENT`, or unresolved `STANDING`
- resolved object = `phase_state: STANDING` with `resolution_type` in `{FINALIZE, INVALIDATE, EVOLVE}`

More than one open object may exist in one host only under the distinct-matter coexistence guard.

### 7.4 Candidate Coexistence

Multiple candidate objects may coexist only when:

- each candidate has a distinct `matter_ref`
- each candidate is explicitly marked as cohosted with every already open object it coexists with
- the relation marker carries a non-empty basis
- no same-matter or known overlapping-matter unresolved coexistence is being introduced

Candidate coexistence does not create presence, threshold satisfaction, standing, relation priority, or authority.

### 7.5 Present Coexistence

Multiple present objects may coexist only when their underlying open objects satisfied the same distinct-matter coexistence guard.

Each present object must still have its own explicit `occurrence_ref` and presentation basis. Presence on one object does not supply presence for another object.

### 7.6 Unresolved Standing Coexistence

Multiple unresolved standing objects may coexist only when their objects satisfied the same distinct-matter coexistence guard.

Standing on one object does not create standing, priority, contradiction resolution, or authority for another object.

Unresolved standing objects with the same `matter_ref` are refused in this first pass.

### 7.7 Resolved Standing Coexistence

Resolved standing objects may coexist as preserved trace.

Resolved standing objects do not block preservation of other objects by existing. They also do not authorize silent reset, replacement, or same-matter reinterpretation.

If later same-matter change is intended after standing, the accepted first-pass path remains `EVOLVE`: the predecessor is resolved as `EVOLVE`, the successor is created as `CANDIDATE`, and the predecessor/successor relation is explicit.

This spec does not yet define a broader same-matter "new episode" relation after `FINALIZE` or `INVALIDATE`. A successor implementation must refuse that case unless it is represented through an already lawful relation path.

### 7.8 Same-Matter And Overlapping-Matter Rule

Same-matter unresolved coexistence is refused in this first pass.

Known or asserted overlapping-matter unresolved coexistence is also refused in this first pass.

The host may accept distinct-matter unresolved coexistence only when the request explicitly marks that the new object and the relevant existing open objects are being treated as distinct matter-bound threads inside this host.

The host must not infer distinctness from different strings alone when accepting multiple unresolved open objects. A distinct `matter_ref` is necessary but not sufficient; explicit relation marking is also required.

## 8. Relation Marking Requirements

### 8.1 Existing Lineage Relation

The predecessor/successor relation required for `EVOLVE` remains mandatory.

An accepted `EVOLVE` must preserve:

- predecessor object id
- successor object id
- resolution of predecessor as `EVOLVE`
- successor phase as `CANDIDATE`
- record visibility of the predecessor/successor relation

This relation is not enough for all coexistence cases. It covers lawful succession only.

### 8.2 New Minimal Coexistence Marker

This spec adds one host-local relation marker for first-pass unresolved coexistence:

`DISTINCT_MATTER_COHOSTED`

Minimum shape:

```text
CoexistenceRelation {
  relation_type: DISTINCT_MATTER_COHOSTED
  object_id: string
  related_object_id: string
  basis_ref: string
  created_by_record_id: string
}
```

Rules:

- the marker is pairwise
- both objects must be in the same local host
- both objects must have distinct `matter_ref` values
- `basis_ref` must be non-empty
- the marker must be created as part of an accepted action record
- the marker does not claim global independence
- the marker does not claim cross-host relation
- the marker does not resolve contradiction
- the marker does not create standing or resolution

### 8.3 When Marking Is Required

When accepting creation of a new unresolved object while any other unresolved object already exists in the host, the host must preserve a `DISTINCT_MATTER_COHOSTED` marker between the new object and each already open object.

If the request cannot supply the required relation basis for every already open object, the creation must be refused.

The host must not accept unresolved coexistence by relying on:

- matter name difference alone
- object id difference alone
- timestamp order
- storage order
- "current" pointer convention
- payload similarity or dissimilarity
- narrative explanation outside the record

## 9. Refusal and Anti-Collapse Rules

The successor host line governed by this spec must refuse and append a refusal record for at least the following cases.

Unlawful unresolved coexistence:

- creating a second unresolved object without required relation marking
- creating a second unresolved object without relation basis
- creating an unresolved object with the same `matter_ref` as an existing unresolved object
- creating an unresolved object where known or asserted matter overlap exists with an existing unresolved object
- creating unresolved coexistence by object naming, timestamp, or storage order

Standing contradiction:

- creating or moving an object in a way that silently contradicts unresolved standing force on the same matter
- treating later object creation as replacing an unresolved standing object
- treating a same-matter candidate as correction of standing matter without `EVOLVE`
- hiding priority between unresolved standing objects through ordering or display

Lineage and overwrite:

- overwriting prior object fields to simulate coexistence
- overwriting resolved standing matter in place
- replacing predecessor content with successor content
- creating same-matter successor behavior without explicit predecessor relation

Relation omission:

- accepting coexistence where an explicit relation marker is required but missing
- treating predecessor/successor lineage as a generic relation marker for unrelated coexistence
- treating distinct-matter cohosting as global system relation

HOLD collapse:

- using HOLD to counterfeit relation
- using HOLD to resolve contradiction
- using HOLD as phase, resolution, priority, or relation marker
- using HOLD release as standing-entry, resolution, or coexistence authorization

Rank collapse:

- treating this same-host coexistence allowance as global IAMMAI law
- treating this spec as full relation doctrine
- treating this spec as minimum lawful system

Refusal remains explicit host behavior. It is not phase, resolution, relation, HOLD, or hidden fourth outcome.

## 10. HOLD Under Coexistence

HOLD remains orthogonal under same-host multiplicity.

First-pass HOLD model:

- HOLD is target-specific
- a HOLD binds to one target object
- more than one HOLD may exist at once only when each HOLD targets a distinct object
- duplicate active HOLD on the same target is refused
- HOLD blocks `STAND`, `FINALIZE`, `INVALIDATE`, and `EVOLVE` only for its target object
- HOLD does not block unrelated distinct-matter objects by default
- HOLD does not create, remove, or alter a coexistence relation
- HOLD does not resolve contradiction between objects

The host may represent active HOLD as a map keyed by object id in a successor implementation. That representation remains local and does not define final containment architecture.

HOLD records must preserve the target object id, matter ref, basis ref, hold-before/hold-after posture for the target, and accepted/refused outcome.

## 11. Append-Only Trace Under Coexistence

Append-only trace remains mandatory.

Once more than one object may exist, records must preserve enough detail to reconstruct:

- the target object of every attempted action
- all object ids created by accepted creation
- all open objects considered by a coexistence guard
- all `DISTINCT_MATTER_COHOSTED` markers created by an accepted action
- predecessor/successor relation on accepted `EVOLVE`
- same-matter or overlap refusal where coexistence is refused
- contradiction/conflict refusal where standing force would be silently crossed
- HOLD target and target-specific blocked action
- accepted/refused outcome and refusal code
- source and target phase posture
- source and target resolution posture
- basis references used for creation, presentation, standing, resolution, relation marking, and HOLD

Prior records must not be deleted, rewritten, reordered, compacted, or reinterpreted to make coexistence appear cleaner after the fact.

This trace posture does not define final persistence architecture, registry design, event-sourcing design, signatures, replication, or cross-host record continuity.

## 12. Proof Expectations / Test Families

These are proof expectations for later executable tests. This file does not create tests.

### 12.1 Lawful Distinct-Matter Coexistence

Expected path:

1. create object A for matter A
2. create object B for matter B while A remains open
3. include a `DISTINCT_MATTER_COHOSTED` relation marker with basis

Expected proof:

- both objects exist
- both objects are unresolved
- both matter refs are distinct
- relation marker is visible
- creation records remain append-only
- neither object is treated as replacing the other

### 12.2 Refused Missing Relation Marker

Expected path:

1. create object A
2. attempt to create object B while A remains open without the required relation marker or relation basis

Expected proof:

- request is refused
- refusal record is appended
- object A is unchanged
- object B is not created
- refusal is not phase, resolution, HOLD, or relation

### 12.3 Refused Same-Matter Unresolved Coexistence

Expected path:

1. create unresolved object A for matter A
2. attempt to create unresolved object B for matter A

Expected proof:

- request is refused
- refusal record identifies same-matter unresolved coexistence
- object A is unchanged
- no hidden priority or replacement is created

### 12.4 Distinct-Matter Present And Standing Coexistence

Expected path:

1. create two distinct-matter cohosted objects
2. present each object with its own occurrence ref and basis
3. stand each object with its own threshold basis, if no HOLD blocks it

Expected proof:

- presence remains object-specific
- standing remains object-specific
- standing-entry still occurs only through `STAND`
- neither object supplies occurrence, threshold, or standing for the other

### 12.5 Resolved Standing Coexistence

Expected path:

1. create object A through standing
2. resolve A through `FINALIZE`, `INVALIDATE`, or `EVOLVE`
3. preserve A while other objects exist

Expected proof:

- resolved A remains preserved
- A is not mutated in place
- A does not block distinct-matter coexistence merely by existing
- if `EVOLVE` is used, successor relation is explicit and successor starts as `CANDIDATE`

### 12.6 HOLD Under Coexistence

Expected path:

1. create two distinct-matter cohosted objects
2. set HOLD on object A
3. attempt blocked movement on A
4. perform otherwise eligible movement on B
5. release HOLD on A

Expected proof:

- HOLD is target-specific
- HOLD blocks only its target
- HOLD does not become relation, phase, resolution, or priority
- HOLD records identify the target object
- release restores permissibility only

### 12.7 Append-Only Refusal Visibility

Expected path:

1. create a bounded mix of accepted and refused coexistence attempts
2. inspect transition records

Expected proof:

- every attempted action appends exactly one record
- refused requests return `accepted: false`
- refused requests do not change semantic object posture
- relation markers appear only on accepted relation-bearing actions
- refusal codes remain distinct from phase, resolution, HOLD, and relation markers

## 13. Invariants

The same-host coexistence slice must preserve these invariants.

Host boundary:

- coexistence choices apply only inside one local host boundary.
- this spec does not define cross-host continuity or global system law.

Host slice preservation:

- the current one-open-object host remains valid at its original proof rank.
- this spec defines a successor relation slice, not a correction of the prior slice.

Explicit coexistence:

- coexistence must be explicit where relation matters.
- distinct matter string difference is not enough by itself once multiple open objects coexist.

Lineage:

- predecessor/successor lineage remains explicit on `EVOLVE`.
- successor relation must not be inferred from timestamp, name, or payload similarity.

No overwrite:

- no object is silently overwritten.
- resolved standing matter is not mutated in place.

No hidden contradiction:

- contradiction must not be hidden by ordering, storage convention, display priority, or current pointer behavior.
- same-matter unresolved coexistence is refused in this first pass.

HOLD orthogonality:

- HOLD remains permissibility control only.
- HOLD is not phase, resolution, relation, or contradiction handling.

Refusal visibility:

- refused coexistence remains visible in append-only records.
- refusal is not a hidden fourth outcome.

Rank boundary:

- this coexistence slice is not full relation doctrine.
- this coexistence slice is not minimum lawful system.

## 14. Presence Boundary

Presence remains relevant under coexistence because multiple present objects require occurrence distinction.

This spec preserves that:

- each present object requires its own occurrence handling
- occurrence on one object does not create presence for another object
- multiple present objects may coexist only under the selected distinct-matter guard
- same-matter presence coexistence remains refused in this first pass unless later work defines a lawful relation path

This spec does not settle full presence doctrine, event doctrine, witness requirements, occurrence ontology, or cross-layer presence continuity.

Presence may constrain later relation work. It does not replace the coexistence task in this spec.

## 15. Explicit Non-Claims

This spec does not define:

- full relation layer
- full many-kernel coexistence law
- full multiplicity law
- cross-host continuity
- host-to-host transfer law
- persistence architecture
- registry design
- distributed or cross-carrier law
- final context/world ontology
- full presence doctrine
- full event doctrine
- minimum lawful system
- full embodiment or runtime closure
- final validator, governor, witness, registry, or interface design
- product behavior
- deployment posture

This spec also does not claim that bounded same-host coexistence is globally sufficient for IAMMAI.

## 16. Closing Boundary Statement

The v0-min host slice stands.

This spec defines the first bounded same-host coexistence derivation after that slice: multiple objects may exist in one host, unresolved coexistence is allowed only for explicitly marked distinct matters, same-matter unresolved coexistence remains refused, HOLD stays target-specific and orthogonal, and append-only refusal remains mandatory.

Later work may implement and test this relation slice through a successor code line.

This spec itself does not solve the wider relation layer, persistence architecture, cross-host continuity, presence doctrine, system frame, or world boundary.
