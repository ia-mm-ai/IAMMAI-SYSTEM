# IAMMAI Operator Runbook

## 1. Purpose

This file defines the first operator-facing runbook for executing the first lawful local cycle of IAMMAI.

Its job is to explain, in simple but precise operational terms:

- what the operator is about to do
- what must be prepared before running the cycle
- what order to perform actions in
- what artifacts to expect
- what to inspect afterward
- what to do if the cycle does not complete
- what not to fake, skip, or cosmetically substitute

It is for the operator or bounded internal runner of the first local embodiment slice.

It does not yet try to define:

- code
- an API spec
- a product manual
- a user-facing onboarding page
- broad operating policy
- generalized runbooks for later embodiments

It is a bounded operator runbook for the first local embodiment slice.

## 2. First Principle

The operator must preserve lawful distinction, not just get an output.

Visible failure is preferable to false completion.  
The cycle counts only if required artifacts and runtime steps are real.  
Nothing should be manually faked to make the run look complete.

The operator’s job is therefore not to force success. It is to run one bounded lawful cycle honestly enough that success, non-passage, or failure can be reconstructed afterward.

## 3. Preconditions

Before a run begins, the following must already be in place:

- the bounded matter is defined
- the first live cycle is defined
- the success and failure criteria are available
- the required runtime roles are available in the selected local form
- the registry location is known
- the artifact expectations are known
- the chosen local execution posture is understood

For the selected first cycle, this also means:

- the selected matter is the one bounded local note matter
- the note exists in exact received form for the run
- the matter is being handled in threshold-eligible condition
- the cycle is being run in the internal-first controlled context

If these conditions are not true, do not start the run.

## 4. Operator Checklist Before Run

Before running, verify:

- the matter is the correct bounded matter
- the input or contact is bounded to one note and one matter id
- the Validator is available
- the Witness Emitter is available
- the Governor is available where required
- state and transition handling is available
- the Registry / Store is available
- the output and registry locations are known

If any required role or location is unknown, stop before beginning the cycle.

## 5. Lawful Run Sequence

Run the cycle in the following order:

1. Prepare the bounded note input in its exact received form.
2. Confirm that the selected matter id and selected note correspond to the defined first matter.
3. Initiate the cycle through the local Interface Gateway or minimal local operator surface.
4. Confirm that validation runs for the required threshold, transition-legality, and governance-precondition checks.
5. Confirm that witness emits for the constitutionally relevant contact and validation occurrence.
6. Confirm that governance acts where required by authorizing, denying, or applying HOLD to the truth-formation attempt.
7. If governance authorizes and does not hold the move, confirm that state and transition outputs are produced by the State Engine.
8. Confirm that the Registry / Store preserves the canonical records actually produced.
9. Stop if any required step does not lawfully proceed.

Do not continue past a missing required step as though it had completed.

## 6. Expected Artifacts on Success

After a successful run, expect the following canonical artifacts where applicable:

- validation artifact
- witness artifact
- governance action record
- transition record
- state record
- registry-preserved canonical records

For the selected first cycle, success specifically requires:

- a validation artifact showing the required checks passed
- the required witness artifact or artifacts
- a governance action record authorizing the move
- a transition record for the threshold-eligible-to-truth move
- a state record for the resulting truth state
- canonical preservation of the artifacts actually produced

## 7. What to Inspect After Run

After execution, inspect the result in this order:

- did the required artifacts appear
- do the artifacts correspond to the chosen matter
- do the artifacts preserve typed distinctions
- is the runtime path reconstructable
- did registry preservation actually occur
- did the result meet the success criteria rather than only looking successful

The operator should judge the run by canonical artifacts and visible runtime truth, not by interface appearance, narrative plausibility, or partial display output.

## 8. Non-Completion / Failure Handling

If the cycle does not complete:

- do not fake completion
- do not replace missing canonical artifacts with summaries
- record where the cycle stopped
- classify non-completion according to the success and failure criteria
- preserve failure visibility
- distinguish fail, hold, deny, blocked, and indeterminate where relevant

In practice, that means:

- if validation does not pass, preserve typed validation non-passage
- if witness is missing or incomplete, preserve that absence visibly
- if governance does not proceed, preserve whether that was denial or HOLD
- if state movement does not occur, preserve non-movement rather than cosmetic continuity
- if registry preservation fails, preserve that preservation failure rather than treating the run as durably complete

## 9. What the Operator Must Not Do

The operator must not:

- manually invent missing artifacts
- cosmetically rewrite failure into success
- treat UI or surface output as canonical proof
- skip required runtime roles
- collapse validation into governance
- collapse witness into generic logging
- proceed as if registry preservation happened when it did not

The operator must also not continue the run by narrative or manual assertion once a required lawful step has not actually occurred.

## 10. Relation to the Repo

This runbook depends on:

- the constitutional core as the source of truth
- the runtime layer as the definition of lawful motion, contracts, failures, coordination, and handoff
- the embodiment decision as the chosen execution posture
- the first live cycle as the bounded selected run
- the success and failure criteria as the judgment standard for the run

This runbook does not replace those documents. It operationalizes them for one bounded local run.

## 11. What Remains Open

The following remain intentionally open before the first actual run:

- the exact local host form
- the exact script names or command surface
- the exact folder and output conventions
- the exact operator UI, if any

These are embodiment-build questions, not constitutional ambiguities.

## 12. Summary

This document defines the operator-facing runbook for IAMMAI’s first lawful local cycle as the bounded procedure for preparing, initiating, inspecting, and honestly classifying one governed truth-formation attempt on one local note matter.

Its purpose is to ensure that the first run is performed as a lawful, auditable cycle whose success path and non-completion states remain real, visible, and canonically grounded rather than cosmetically staged.

**One-Line Definition:** `OPERATOR_RUNBOOK.md` defines the first operator-facing procedure for executing and honestly judging IAMMAI’s first lawful local cycle without faking completion or collapsing required runtime roles.
