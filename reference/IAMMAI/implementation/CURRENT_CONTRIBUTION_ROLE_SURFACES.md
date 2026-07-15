# IAMMAI Current Contribution Role Surfaces

## 1. Purpose

This file defines the current-surfaces note for the contribution-role branch.

Its job is to make the branch easier to re-enter lawfully now that first-pass conformance artifacts stand beside the earlier overview, schema-admission, and schema surfaces.

It does not define:

- a constitutional rewrite
- a contribution-family master map
- a schema file
- a runtime migration plan
- a storage architecture memo
- a roadmap
- a README
- a project-management note
- a manifesto

This file is additive only. It does not replace repo-scale current-state, readability, rank, or lineage surfaces. It also does not replace the branch spine already standing in the contribution-role line.

## 2. Why This Note Is Needed Now

The contribution branch now has enough internal structure that re-entry can drift without one bounded branch-specific note.

That structure is now more than overview and schema-admission posture alone. First-pass conformance artifacts now also stand:

- two positive examples
- three invalid fixtures
- one bounded checker

The reason for this note is branch growth and re-entry clarity, not failure. The branch now needs one compact surface that states what presently stands, what the current center is, and what remains open without widening contribution role into a larger subsystem.

## 3. What Now Stands In The Contribution Branch

The contribution branch now stands in two clearly different layers.

### A. Branch Spine

The branch spine is:

- `implementation/CONTRIBUTION_ROLE_OVERVIEW.md`
- `implementation/CONTRIBUTION_ROLE_SCHEMA_ADMISSION_BOUNDARY.md`
- `implementation/schemas/contribution_role_record.schema.json`

These surfaces do the main architectural work.

They give contribution role explicit implementation-facing objecthood, clarify that it has crossed into schema-admissible status, and make that admission real as one bounded first-pass schema envelope in the implementation schema line.

### B. First-Pass Conformance Layer

The first-pass conformance layer is:

- `implementation/examples/first_pass_contribution_role_record.formalization.example.json`
- `implementation/examples/first_pass_contribution_role_record.authorization.example.json`
- `implementation/examples/invalid_first_pass_contribution_role_record.missing_role_type.json`
- `implementation/examples/invalid_first_pass_contribution_role_record.missing_matter_ref.json`
- `implementation/examples/invalid_first_pass_contribution_role_record.empty_actor_ref.json`
- `implementation/check_contribution_role_record.py`

These artifacts do not replace the branch spine. They ground it.

They make the schema inspectable as one bounded formalization example, one bounded authorization example, three clear malformed cases, and one bounded checker that reads one contribution-role record object at a time.

## 4. What Landed In The First-Pass Conformance Layer

The positive examples now show that the schema can lawfully house:

- one `FORMALIZATION` record tied to the contribution-role overview surface
- one `AUTHORIZATION` record tied to the contribution-role schema-admission boundary surface

The invalid fixtures now show three bounded failure edges:

- missing `role_type`
- missing `matter_ref`
- empty `actor_ref`

`implementation/check_contribution_role_record.py` now gives the branch one first bounded checker. It enforces the first-pass structural shape, checks the visible bounded role enum, rejects empty required and optional strings where present, and checks only the file-like refs the branch already justifies.

Taken together, this conformance layer grounds schema presence without widening the branch into runtime doctrine, storage doctrine, identity infrastructure, governance machinery, or a larger checker family.

## 5. What The Current Center Of The Branch Now Is

The current center of the branch is now:

- the first-pass contribution-role schema
- grounded by positive examples
- bounded by invalid fixtures
- checked by one first bounded checker
- still read through the prior overview and schema-admission boundary that define what this schema does and does not mean

That is the correct present read.

The branch is no longer centered only on whether contribution role deserves explicit implementation-facing housing or schema admission. It is now centered on a first-pass schema envelope that is both stated and minimally conformed.

This is also a lawful pause point for this pass.

The branch now has enough explicit housing, schema presence, positive grounding, invalid boundaries, and bounded checking that later work does not need to proceed from memory alone. At the same time, this pause point does not pretend the broader contribution area is complete.

## 6. What Remains Open

Important branch questions still remain open.

- direct absorption into `implementation/SCHEMA_MAP.md`
- runtime or registry integration
- final canonical versus derivative rank
- final relation to actor or identity references
- final vocabulary or taxonomy refinement
- whether later checker refinement is actually needed beyond the first bounded checker
- whether a later broader implementation re-entry refresh becomes lawful and necessary

These questions should remain explicit. The presence of first-pass conformance support does not close them.

## 7. Relationship To Existing Surfaces

This note sits beside existing surfaces as a re-entry aid for the contribution branch only. It does not become a new authority source.

With `implementation/CURRENT_IMPLEMENTATION_SURFACES.md`, it narrows one implementation-facing branch without replacing the broader implementation re-entry surface.

With `CURRENT_STATE__REPO_ENTRY.md`, `CURRENT_READABILITY_SURFACES.md`, `RANKED_SURFACE_INDEX.md`, and `VERSION_LINEAGE.md`, it preserves that repo-scale current-state, readability, rank, and lineage orientation remain broader than the contribution branch. This file does not replace those surfaces.

With `implementation/CANONICAL_RECORDS_OVERVIEW.md`, it preserves the structural grounding that contribution role is already a core canonical record family and should remain distinct from governance, witness, validation, state, transition, and generic authorship.

With `implementation/SCHEMA_MAP.md`, it preserves that the current first schema-planning surface still stands as written. This note does not claim that `SCHEMA_MAP.md` has already absorbed the contribution-role schema line.

With `runtime/REGISTRY_CONTRACT.md`, it preserves that runtime preservation relevance and contribution-role schema presence are adjacent but not identical questions. This note does not claim that contribution-role runtime integration is settled.

This note therefore reduces contribution-branch re-entry drift. It does not rewrite the branch spine, replace the surrounding grounding surfaces, or widen contribution role into a new subsystem.

## 8. Closing Boundary Statement

This file defines the current contribution-role surfaces only.

It exists to reduce re-entry drift now that first-pass conformance artifacts also stand.

It does not pretend the rest of the system is solved.

It is a bounded additive current-surfaces note, not a replacement and not a new subsystem.
