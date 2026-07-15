# IAMMAI Contribution Role Schema Admission Boundary

## 1. Purpose

This file defines the schema-admission boundary for contribution role in first-pass form.

Its job is to answer, in one compact place:

- whether contribution role has now earned schema-family admission
- what that admission would and would not mean
- where such a schema would lawfully live, if admission is justified
- what still remains open even after this boundary is clarified

It does not define:

- a constitutional rewrite
- an implementation-family master map
- a schema file
- a runtime migration plan
- a storage architecture memo
- a graph or database design
- a distributed systems plan
- a roadmap
- a README
- a project-management note
- a manifesto

This file is additive only. It does not replace implementation, runtime, continuity, admissibility, accession, standing, vessel, bridge, review, current-state, or constitutional surfaces already standing in the body.

## 2. Why This Note Is Needed Now

Contribution role no longer lacks objecthood.

`implementation/CONTRIBUTION_ROLE_OVERVIEW.md` already gives it a bounded implementation-facing room. `implementation/CANONICAL_RECORDS_OVERVIEW.md` already names it as a core record family. `runtime/REGISTRY_CONTRACT.md` already permits preservation of contribution records where relevant. `protocol/canon.json` already preserves contribution as a distinct anti-collapse concern with named roles and contribution-role references.

That means the exposed question is no longer whether contribution role exists. The exposed question is schema admission and schema placement.

The body therefore needs one explicit boundary note so later schema work does not proceed from memory, omission, or assumption.

## 3. What Already Stands

The following already stand for contribution role in the visible body.

- `implementation/CANONICAL_RECORDS_OVERVIEW.md` treats contribution role records as a core canonical record family and states that they should preserve role type and relation to matter, actor, artifact, and related governance action where applicable.
- `implementation/CONTRIBUTION_ROLE_OVERVIEW.md` gives contribution role explicit implementation-facing objecthood and distinguishes it from governance, witness, validation, state, transition, generic authorship, and generic actor language.
- `runtime/REGISTRY_CONTRACT.md` allows contribution records to be preserved where relevant and keeps them typed apart from other canonical records.
- `protocol/canon.json` already defines contribution as a distinct constitutional concern, names the contribution role families, prohibits silent role impersonation, and requires preservation of `contribution_role_references` within representation.
- `implementation/SCHEMA_MAP.md` does not yet schedule a contribution-role schema in the first set, which means placement and admission have remained open even after contribution role became implementation-facing.

This is enough to say that contribution role already stands as a real preserved concern in canonical, implementation-facing, and runtime-adjacent language. It is not enough, by itself, to count as schema creation.

## 4. Why Schema Admission Is A Distinct Question

Having an overview is not yet the same as schema admission.

An overview gives a record family explicit room, boundary, and local meaning. A schema-admission decision goes further. It says the body now has enough bounded clarity that machine-enforceable structure would be lawful rather than premature.

That question is not trivial or cosmetic.

- If contribution role is admitted too early, schema convenience could freeze vocabulary, identity linkage, or relation shape before the body has justified that closure.
- If contribution role is not admitted once the record family is already real, schema planning can continue to treat it as secondary, optional, or ambient, which would undercut the anti-collapse work already done.
- Location matters because a contribution-role schema placed under the wrong layer would distort rank. Put under `protocol/`, it would read too close to constitutional source. Put under `runtime/`, it would read too close to runtime merger. Put under identity framing, it would invite a false social-ontology or identity-system read.

Schema admission is therefore a distinct boundary question about readiness and placement, not a cosmetic extension of prose.

## 5. Current Best Read Of Schema Admissibility

The current best bounded read is: yes, contribution role is now schema-admissible in first-pass form.

That answer is justified because the visible body already supplies all of the following:

- constitutional anti-collapse support through `protocol/canon.json`
- core record-family standing through `implementation/CANONICAL_RECORDS_OVERVIEW.md`
- explicit implementation-facing objecthood through `implementation/CONTRIBUTION_ROLE_OVERVIEW.md`
- runtime-adjacent preservation relevance through `runtime/REGISTRY_CONTRACT.md`

The schema-admissible claim should still remain bounded.

It does not mean that contribution role is now first-set mandatory in the sense already assigned in `implementation/SCHEMA_MAP.md`. It means the body now has enough lawful clarity that contribution role may be admitted as its own schema family when schema work is later taken up, rather than being left outside the schema family map by inertia.

So the best first-pass admission answer is:

- yes, contribution role has earned schema-family admission
- yes, that admission is bounded and first-pass only
- no, that admission has not yet been enacted as schema creation
- no, that admission does not settle runtime or storage integration

## 6. Lawful Schema Placement

If contribution role is admitted to schema-family status, its lawful home is the implementation schema layer under `implementation/`, as an additive record-family schema beside the other implementation-derived schema families.

That placement is the best current fit for three reasons.

- `implementation/SCHEMA_MAP.md` is already the body’s schema-planning surface. Even though it does not yet schedule contribution role, it remains the lawful layer within which that admission should be understood.
- `implementation/CANONICAL_RECORDS_OVERVIEW.md` already treats contribution role as a canonical record family. That makes contribution role closer to record-family schema planning than to derivative readability or companion commentary.
- `runtime/REGISTRY_CONTRACT.md` preserves canonical records, but it does not define schema families. Runtime preservation therefore supports the admissibility of contribution records without becoming the schema home.

The lawful placement is therefore:

- in the implementation schema family line
- not in `protocol/`
- not in `runtime/`
- not in `continuity/`

This placement does not yet imply that `implementation/SCHEMA_MAP.md` has already been updated, nor that a contribution-role schema file should be created immediately.

## 7. What Schema Admission Would Not Mean

Schema admission would not mean:

- runtime admission
- final identity linkage
- final vocabulary closure
- final canonical versus derivative storage decision
- governance or authority status
- mechanism or checker implementation by default

It would also not mean that contribution role has become an identity system, a governance engine, or a final social ontology.

Schema admission means only that the body now has enough bounded clarity for contribution role to lawfully exist as its own schema family when and if the schema layer later absorbs it.

## 8. Relationship to Existing Surfaces

This note clarifies a boundary. It does not enact migration.

With `implementation/CONTRIBUTION_ROLE_OVERVIEW.md`, it preserves that contribution role already has implementation-facing objecthood. This note narrows the next question from objecthood to schema admission.

With `implementation/CANONICAL_RECORDS_OVERVIEW.md`, it preserves that contribution role is already a core record family. This note does not create that family. It clarifies that the family is now mature enough for first-pass schema admission.

With `implementation/SCHEMA_MAP.md`, it preserves that the current first schema set still stands as written. This note does not rewrite that file. It clarifies that contribution role has now crossed the boundary from underhoused record-family concern into schema-admissible record-family concern.

With `implementation/CURRENT_IMPLEMENTATION_SURFACES.md`, it preserves that direct schema-family admission for contribution role was still explicitly open. This note narrows that open question without claiming broader implementation closure.

With `runtime/REGISTRY_CONTRACT.md`, it preserves that contribution records may be preserved where relevant, but that runtime preservation and schema admission are not identical questions.

With `protocol/canon.json`, it preserves that contribution role already has constitutional machine-canon grounding through named roles, anti-collapse principles, and representation requirements.

With `protocol/protocol_identity.v1.0.1.json`, it preserves that machine identity is a derived constitutional identity surface for ranked reading, not an identity-system basis for contribution role. Contribution role should not be absorbed into identity merely because actor references may later matter.

## 9. What Remains Open

Even after this admission boundary is clarified, the following remain open.

- the final schema shape
- runtime and registry integration
- the final canonical versus derivative rank
- the final relation to actor or identity references
- the final vocabulary or taxonomy beyond what already visibly stands
- future mechanism or checker work

These remain open on purpose. The present task is to clarify whether contribution role may lawfully become schema, not to force the rest of the system closed.

## 10. Closing Boundary Statement

This file defines the schema-admission boundary for contribution role only.

It exists to clarify whether and where contribution role may lawfully become schema, without pretending the rest of the system is solved.

Later additive work may separately decide whether the schema should actually be created.
