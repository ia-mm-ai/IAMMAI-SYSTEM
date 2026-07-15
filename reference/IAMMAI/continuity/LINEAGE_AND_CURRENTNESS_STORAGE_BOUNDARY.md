# IAMMAI Lineage and Currentness Storage Boundary

## 1. Purpose

This file clarifies the current placement and storage-rank boundary for the two first-pass continuity objects that now stand in the repository:

- lineage
- currentness

Its job is to answer, in one compact place, where these objects actually live in the body now and what kind of rank they do and do not have.

It does not:

- define a constitutional rewrite
- define a continuity-family master map
- define a storage engine
- define a runtime migration plan
- define a graph or database design
- define a distributed systems plan
- define a schema
- replace continuity, runtime, implementation, admissibility, accession, standing, vessel, bridge, review, or current-state surfaces already standing in the body

This file is additive only. It does not replace the continuity notes, the runtime registry contract, the implementation-facing record and schema notes, or the existing bridge and review surfaces.

## 2. Why This Note Is Needed Now

First-pass lineage and currentness objecthood already stand.

The question is no longer whether these objects should exist. The question is where they actually live in the body, what kind of preservation they may deserve, and what rank they should and should not be read as carrying.

The body therefore needs one explicit placement clarification so that lineage is not mistaken for a mere readability convenience and currentness is not mistaken for canonical truth or operative authority. This note exists to reduce that ambiguity without overbuilding it.

## 3. What Already Stands

The following already stand in bounded form.

- `continuity/FIRST_PASS_LINEAGE_RECORD.md`
- `continuity/FIRST_PASS_LINEAGE_RECORD.schema.json`
- `continuity/examples/first_pass_lineage_record.api_backed_posture_narrowing.example.json`
- `continuity/examples/first_pass_lineage_record.proof_004_to_post_proof_bridge.example.json`
- `continuity/FIRST_PASS_CURRENTNESS_RECORD.md`
- `continuity/FIRST_PASS_CURRENTNESS_RECORD.schema.json`
- `continuity/examples/first_pass_currentness_record.api_backed_scope.example.json`
- `continuity/examples/first_pass_currentness_record.proof_004_seam_scope.example.json`
- `continuity/check_continuity_record.py`
- `continuity/CURRENT_CONTINUITY_SURFACES.md`

That means first-pass continuity objecthood is already real at note, schema, example, and checker level. The open question is placement, not existence.

## 4. Why Placement Matters

Object existence is not yet enough.

The body still needs to know how these objects relate to:

- `runtime/REGISTRY_CONTRACT.md`
- `implementation/CANONICAL_RECORDS_OVERVIEW.md`
- `implementation/SCHEMA_MAP.md`
- derivative and readability surfaces

Without that placement clarification, lineage can drift downward into optional convenience, or currentness can drift upward into counterfeit authority.

Placement is therefore about rank and housing, not final implementation. It asks where these objects belong in the present body and how they should presently be read. It does not decide database design, runtime merger, or final storage topology.

## 5. Lineage Placement

The current best bounded read is that lineage belongs closer to preservable additive continuity truth than currentness does.

That read is supported by the visible body.

`runtime/REGISTRY_CONTRACT.md` already states that the Registry / Store may preserve canonical records including lineage relations and references, and that lineage recoverability, predecessor or successor relation where relevant, append-oriented preservation posture, and reconstructable history are part of what authoritative preservation must keep.

`implementation/CANONICAL_RECORDS_OVERVIEW.md` also already treats lineage references as part of the canonical record model. It explicitly preserves predecessor, successor, and transition relation as distinct and rejects recovery of lawful succession by naming, timestamps, or guesswork alone.

Against that background, the first-pass lineage object now reads as continuity-side housing that is registry-near and canon-adjacent in the following bounded sense:

- it houses additive succession rather than convenience summary
- it preserves anti-erasure relation that the body already treats as necessary for reconstructable history
- it is closer to preservable continuity truth than to derivative readability

This does not mean that the present first-pass lineage object is already fully integrated into runtime or registry in final form.

It does mean that the body’s best current read is that lineage belongs on the preservable side of the continuity boundary, nearer canonical relation housing than derivative display housing.

## 6. Currentness Placement

The current best bounded read is that currentness belongs to real continuity housing, but at a more derivative rank than lineage.

That read is also supported by the visible body.

`continuity/FIRST_PASS_CURRENTNESS_RECORD.md` explicitly defines currentness as authority-locating rather than authority-generating. It records what presently governs for one bounded scope, in what posture, on what basis, and against which visible non-current neighbors. It repeatedly refuses to let the currentness object become the governing surface itself.

That means currentness should not presently be read as canonical truth artifact equal to law, proof, decision, bridge, or review surfaces. Its job is to locate present governing relation, not to become that relation.

The best current placement read is therefore:

- currentness is real and necessary
- currentness belongs within continuity-side housing rather than mere convenience prose
- currentness is more likely derivative continuity housing than continuity-canonical record family
- if preserved, it must preserve its locating function rather than impersonate operative authority

This is why currentness is not well read as pure readability and also not well read as canonical truth. It sits between those poles as bounded recorded-first continuity housing whose output remains subordinate to the ranked surfaces it points at.

## 7. Relationship to Runtime and Canonical Records

This note clarifies placement. It does not merge these objects into runtime or registry.

With `runtime/REGISTRY_CONTRACT.md`, the most important present distinction is:

- lineage already fits the visible registry contract more naturally because the contract explicitly preserves lineage relations and reconstructable succession
- currentness does not yet fit that same contract at the same rank because the registry preserves canonical records, while currentness only locates what currently governs

With `implementation/CANONICAL_RECORDS_OVERVIEW.md`, the most important present distinction is:

- lineage is consonant with the already typed canonical family of lineage references
- currentness does not appear there as a canonical record family and should not be smuggled in as though locating present authority were the same as preserving canonical succession

With `implementation/SCHEMA_MAP.md`, the most important present distinction is:

- the current schema-planning layer has not yet bound lineage or currentness into a final schema family sequence
- schema planning remains open and bounded, which means this note must not pretend a runtime merger or schema migration has already been chosen

The result is a careful split.

- Lineage presently reads as registry-near continuity relation housing and potentially preservable at a continuity-canonical or canon-adjacent rank.
- Currentness presently reads as continuity-side recorded housing that remains derivative with respect to authority, even where it is operationally important.

## 8. What This Note Does Not Yet Settle

This note does not yet settle:

- the final canonical versus derivative storage split
- the final runtime or registry integration posture
- computed currentness
- storage architecture
- distributedness
- final relation vocabulary
- final posture vocabulary
- whether provenance or state later belong inside the first-pass objects

These remain open on purpose. The body now needs placement clarity more urgently than it needs final architecture.

## 9. Closing Boundary Statement

This file defines the current placement boundary for lineage and currentness only.

It exists to clarify where these objects live in the body now, without pretending their final storage architecture is solved.

Later additive work may separately decide whether and how these objects move closer to runtime or registry or remain continuity-local.
