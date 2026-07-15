# IAMMAI Current Decision Record Surfaces Post Conformance

## 1. Purpose

This file defines the post-conformance current-surfaces note for the decision-record branch.

Its job is to make the branch easier to re-enter lawfully now that first-pass conformance artifacts also stand beside the earlier overview, boundary, and schema surfaces.

It does not define:

- a constitutional rewrite
- a decision-family master map
- a schema file
- a runtime migration plan
- a storage architecture memo
- a roadmap
- a README
- a project-management note
- a manifesto

This file is additive only. It does not replace repo-scale current-state, readability, rank, or lineage surfaces. It also does not replace the branch spine or the earlier `implementation/CURRENT_DECISION_RECORD_SURFACES.md`.

## 2. Why This Successor Note Is Needed Now

`implementation/CURRENT_DECISION_RECORD_SURFACES.md` remains a lawful branch re-entry note for the stage at which decision had overview, schema-admission, schema-geometry, and first-pass schema presence.

It is no longer sufficient by itself because the branch has since grown in a bounded way.

- two positive examples now stand
- three invalid fixtures now stand
- one bounded checker now stands

That change is branch growth, not branch failure. The earlier note was not wrong. It now predates the first conformance layer and therefore no longer carries the full current branch state by itself.

The body therefore needs one additive successor note that states the branch as it now stands after first-pass conformance support has landed.

## 3. What Now Stands In The Decision Branch

The decision branch now stands in two clearly different layers.

### A. Branch Spine

The branch spine remains:

- `implementation/DECISION_RECORD_OVERVIEW.md`
- `implementation/DECISION_RECORD_SCHEMA_ADMISSION_BOUNDARY.md`
- `implementation/DECISION_RECORD_SCHEMA_GEOMETRY_BOUNDARY.md`
- `implementation/schemas/decision_record.schema.json`

These surfaces do the main architectural work.

They define decision-record objecthood, clarify schema admission, resolve first-pass schema geometry, and make that geometry real as one explicit schema envelope. They remain the branch spine and should still be read in sequence.

### B. First-Pass Conformance Layer

The first-pass conformance layer now also stands:

- `implementation/examples/first_pass_decision_record.accession_admission_decision.example.json`
- `implementation/examples/first_pass_decision_record.api_backed_posture_decision.example.json`
- `implementation/examples/invalid_first_pass_decision_record.missing_matter_ref.json`
- `implementation/examples/invalid_first_pass_decision_record.missing_decision_posture.json`
- `implementation/examples/invalid_first_pass_decision_record.empty_basis_refs.json`
- `implementation/check_decision_record.py`

These artifacts do not replace the branch spine. They ground it.

They make the schema inspectable as one bounded positive accession-side decision shape, one bounded positive local posture decision shape, and three clear malformed cases that the checker now rejects for the expected broad reasons.

## 4. What Landed In The First-Pass Conformance Layer

The positive examples now show that the decision schema can house:

- one explicit bounded accession decision through `accession/ADMISSION_DECISION.md`
- one explicit bounded local posture decision through `vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md`

The invalid fixtures now show three bounded failure edges:

- missing `matter_ref`
- missing `decision_posture`
- empty `basis_refs`

`implementation/check_decision_record.py` now gives the branch one bounded checker for one decision-record object at a time. It enforces the first-pass structural shape and checks clearly file-like refs without becoming a generic schema framework, a runtime mechanism, a currentness engine, or a broader decision subsystem.

Taken together, this conformance layer grounds schema presence without widening the branch into runtime doctrine, storage doctrine, or a larger checker family.

## 5. What The Current Center Of The Branch Now Is

The current center of the branch is now:

- the first-pass decision schema
- grounded by positive examples
- bounded by invalid fixtures
- checked by one first bounded checker
- still read through the overview, admission, and geometry notes that define what this schema does and does not mean

That is the correct present read.

The branch is no longer centered only on whether decision deserves schema presence. It is now centered on a first-pass schema envelope that is both stated and minimally conformed.

This is also a lawful pause point for this pass.

The branch now has enough explicit housing, schema presence, positive grounding, invalid boundaries, and bounded checking that later work does not need to proceed from memory alone. At the same time, this pause point does not pretend the broader decision area is complete.

## 6. What Remains Open

Important branch questions still remain open.

- direct absorption into `implementation/SCHEMA_MAP.md`
- runtime or registry integration
- final canonical versus derivative rank
- final posture vocabulary closure
- whether later checker refinement is actually needed beyond the first bounded checker
- the later relation between decision records and currentness records
- whether a later broader implementation re-entry refresh becomes lawful and necessary

These questions should remain explicit. The presence of first-pass conformance support does not close them.

## 7. Relationship To Existing Surfaces

This note sits beside existing surfaces as a successor re-entry aid for the decision branch only. It does not become a new authority source.

With `implementation/CURRENT_DECISION_RECORD_SURFACES.md`, it preserves lineage cleanliness. The earlier note remains the pre-conformance current-surfaces read. This file succeeds it additively because the branch now contains more than the earlier note could yet name.

With `implementation/CURRENT_IMPLEMENTATION_SURFACES.md`, it narrows one implementation-facing branch without replacing the broader implementation re-entry surface.

With `CURRENT_STATE__REPO_ENTRY.md`, `CURRENT_READABILITY_SURFACES.md`, `RANKED_SURFACE_INDEX.md`, and `VERSION_LINEAGE.md`, it preserves that repo-scale current-state, readability, rank, and lineage orientation remain broader than the decision branch. This file does not replace those surfaces.

With `implementation/STATE_MACHINE_OVERVIEW.md` and `implementation/CANONICAL_RECORDS_OVERVIEW.md`, it preserves the structural grounding that keeps decision state-adjacent and anti-collapse without flattening the branch back into general standing-state context.

With `continuity/FIRST_PASS_CURRENTNESS_RECORD.md`, it preserves that currentness remains a different object question. Currentness houses what presently governs for a scope; it does not become the decision record itself.

With `accession/ADMISSION_DECISION.md`, `vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md`, and `v1/34_POST_API_BACKED_POSTURE_BRIDGE.md`, it preserves the surrounding grounding surfaces that show explicit decision reality, explicit bounded posture determination, and explicit distinction between decision and later carried consequence.

This note therefore reduces post-conformance re-entry drift. It does not rewrite the branch spine, replace the grounding surfaces, or widen decision into a new subsystem.

## 8. Closing Boundary Statement

This file defines the post-conformance current decision-record surfaces only.

It exists to reduce re-entry drift now that first-pass conformance artifacts also stand beside the branch spine.

It does not pretend the rest of the system is solved.

It is a bounded additive successor note, not a replacement and not a new subsystem.
