# IAMMAI Accession Intake Pack

## 1. Purpose

This file defines the bounded operator-facing guide for the first accession intake pack.

Its job is to explain what an accession candidate package is, what shape it must take, what the declaration file is for, and what a later first intake checker will verify at receipt time.

It does not:

- rewrite accession doctrine
- act as an intake checker
- act as an admission decision
- act as a vessel contract
- act as a migration guide
- act as a product onboarding memo
- act as a roadmap
- replace the standing accession files

This file is additive only. It does not replace the standing accession files.

## 2. What The Intake Pack Is

The accession intake pack is the first receiving surface for one bounded external candidate package only.

Its function is narrow. It gives the body one inspectable package for first candidacy review. It is not proof, not admission, not vesselhood, and not standing.

The declaration schema in [`ACCESSION_CANDIDATE_DECLARATION.schema.json`](./ACCESSION_CANDIDATE_DECLARATION.schema.json) defines the required machine-readable declaration for that package. It exists so the candidate arrives as one bounded slice with explicit scope, source/export distinction, clean and blocked cases, and one proof-question seed.

## 3. Expected Package Shape

The expected package shape is:

```text
candidate_package/
  candidate_declaration.json
  source/
  export/
  cases/
    clean/
    blocked/
  display/            # optional
```

This shape is intentionally small. It is for one bounded candidate slice only, not for bulk system submission.

## 4. What Each Part Means

`candidate_declaration.json`
: The required machine-readable declaration for the candidate package. It must validate against [`ACCESSION_CANDIDATE_DECLARATION.schema.json`](./ACCESSION_CANDIDATE_DECLARATION.schema.json).

`source/`
: The source-side objects from which the candidate slice is exported or derived. This is where source relation should remain visible.

`export/`
: The concrete exported slice surfaces being handed in for candidacy review. This is the bounded slice under receipt, not the whole external system.

`cases/clean/`
: Clean cases that show the candidate slice in an intended or legible state.

`cases/blocked/`
: Blocked cases that show where the candidate slice fails, stops, or remains non-ready.

`display/`
: Optional display-only material. If present, it should remain visibly distinct from source and export surfaces.

## 5. What A Good First Candidate Package Looks Like

A good first candidate package has the following traits.

- One bounded slice only.
- Source, export, and display-only distinction are visible.
- Clean and blocked cases are both present.
- Excluded scope is explicit rather than left atmospheric.
- The package is easy to inspect without guessing.
- The package is easy to narrow, pause, withdraw, or revoke later because its boundaries are explicit.
- The package remains neutral. It should not rely on founder ownership, product familiarity, usefulness, urgency, or proximity as hidden privilege.

## 6. What Intake Will Check

At a high level, later first intake checking will verify:

- a declaration file exists
- the declaration validates against the schema
- the declared paths exist in the package
- source, export, and case distinction are actually present
- both clean and blocked cases are present
- the package reads as one bounded candidate slice rather than as an amorphous whole-system dump

This is receipt checking only. It is designed to determine whether the package is lawfully shaped for candidacy review, not whether the slice should later pass eligibility, proof, admission, or vessel review.

## 7. What This Does Not Mean

A valid package is not proof.

A valid package is not admission.

A valid package is not vesselhood.

A valid package is not standing.

A valid package does not solve accession. It only makes lawful first receipt possible for one bounded candidate package.

## 8. Closing Boundary Statement

This file defines the intake pack usage only.

It exists to make lawful first receipt possible without widening receipt into accession itself.
