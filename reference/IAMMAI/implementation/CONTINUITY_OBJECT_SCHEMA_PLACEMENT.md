# IAMMAI Continuity Object Schema Placement

## 1. Purpose

This file defines the current implementation-facing placement clarification for the two first-pass continuity objects that now stand in the repository:

- lineage
- currentness

Its job is to clarify how schema and record planning should presently read those objects without modifying the older implementation files that were written before this split became explicit.

It does not:

- define a constitutional rewrite
- define a continuity-family master map
- define a runtime migration plan
- define a storage engine design
- define a graph or database design
- define a distributed systems plan
- define a schema
- replace continuity, runtime, implementation, admissibility, accession, standing, vessel, bridge, review, or current-state surfaces already standing in the body

This file is additive only. It does not replace the continuity notes, the runtime registry contract, the implementation record overview, the schema-planning note, or the standing continuity examples and checker.

## 2. Why This Note Is Needed Now

Continuity objecthood already stands.

The open question is no longer whether lineage and currentness should exist. The open question is how implementation and schema planning should presently place them.

The body therefore needs one explicit implementation-facing propagation step that does not require editing `implementation/SCHEMA_MAP.md` or `implementation/CANONICAL_RECORDS_OVERVIEW.md` before the split is even stated plainly at implementation rank.

## 3. What Already Stands

The following already stand in bounded form.

- note-level continuity object definitions for lineage and currentness
- machine-readable first-pass schemas for both
- real lineage examples
- real currentness examples
- a bounded checker for those records
- a continuity surface-map that identifies lineage and currentness objecthood as the current practical continuity-housing line
- a continuity placement note that already distinguishes their storage-rank pressure

That means implementation is no longer dealing with hypothetical continuity objects. It is dealing with already-standing first-pass objecthood whose placement now needs to be read carefully.

## 4. Why Placement Still Matters For Implementation

Schema and record planning still need to know where these objects live.

That matters even before any direct update to implementation files because:

- schema planning should not silently treat lineage and currentness as the same kind of object
- canonical-record planning should not accidentally ignore a lineage object that already resembles preservable relation housing
- currentness should not be mistaken for a candidate canonical record family merely because it now has a schema and examples

Placement therefore matters before implementation finality. It tells adjacent planning surfaces how to read what already stands, not how to complete a migration.

## 5. Lineage Placement

The current best implementation-facing read is that lineage sits closer to preservable additive continuity relation housing than currentness does.

That read is supported by the visible body.

`runtime/REGISTRY_CONTRACT.md` already permits preservation of lineage relations and references and requires lineage recoverability and reconstructable succession. `implementation/CANONICAL_RECORDS_OVERVIEW.md` already treats lineage references as part of the canonical record model and rejects succession by guesswork.

Against that background, the first-pass lineage object should presently be read in implementation terms as:

- continuity-side relation housing that is compatible with registry-near preservation pressure
- closer to canonical record planning than to derivative readability
- a plausible future participant in stronger record or schema planning, if later absorbed lawfully

This remains a bounded read only. It does not mean that lineage has already been merged into runtime or implementation in final form.

## 6. Currentness Placement

The current best implementation-facing read is that currentness is recorded-first, authority-locating, and more derivative than lineage.

That read is also supported by the visible body.

`continuity/FIRST_PASS_CURRENTNESS_RECORD.md` explicitly states that currentness locates what presently governs for one bounded scope, in what posture, on what basis, and against which visible non-current neighbors. It also explicitly refuses to let the object become the governing surface itself.

So from an implementation and schema-planning perspective, currentness should presently be read as:

- real continuity-side housing
- recorded-first rather than computed-first
- necessary for bounded operational clarity
- not a canonical truth artifact
- not runtime authority
- more derivative than lineage, even where it is operationally important

This is why currentness should not presently be treated as just another member of the canonical record families already named in `implementation/CANONICAL_RECORDS_OVERVIEW.md`. It is a different kind of object.

## 7. Relationship to Existing Implementation/Runtime Surfaces

This note clarifies placement only. It does not enact migration.

With `implementation/SCHEMA_MAP.md`, the present clarification is:

- the current schema-planning order does not yet name lineage or currentness as implementation schema families
- that omission should presently be read as historical sequencing, not as a claim that the continuity objects are unreal
- lineage is the stronger candidate for later closer schema-planning adjacency because it already resembles preservable continuity relation housing
- currentness already has a first-pass schema in `continuity/`, but that does not by itself promote it into the same planning rank as canonical record-family schemas

With `implementation/CANONICAL_RECORDS_OVERVIEW.md`, the present clarification is:

- lineage already fits the existing implementation language around lineage references and reconstructable succession
- currentness does not currently fit that same canonical record-family slot and should not be smuggled in as though locating present authority were the same as preserving lawful succession

With `runtime/REGISTRY_CONTRACT.md`, the present clarification is:

- lineage is more naturally legible as registry-near because the contract already preserves lineage relations and references
- currentness is not presently justified at that same rank because the registry preserves canonical records, while currentness points to governing surfaces without becoming them

No runtime or schema migration is enacted by this note.

## 8. What This Note Does Not Yet Settle

This note does not yet settle:

- direct update or integration into `implementation/SCHEMA_MAP.md`
- direct update or integration into `implementation/CANONICAL_RECORDS_OVERVIEW.md`
- runtime or registry merger
- the final canonical versus derivative storage split
- computed currentness
- storage architecture
- distributedness
- final posture vocabulary
- final relation vocabulary

These remain open on purpose. The present task is propagation of placement clarity, not completion of the future system.

## 9. Closing Boundary Statement

This file defines the current implementation-facing placement clarification for lineage and currentness only.

It exists to propagate the split into adjacent schema and record planning without modifying existing files.

Later additive work may separately decide whether and how the older implementation and runtime surfaces should absorb this distinction.
