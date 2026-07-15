# Portable Source-Body Verification Actual Second-Carrier Live Runbook V0

## 1. Purpose

This runbook defines how to perform one actual other-device / second-carrier live run and capture.

This runbook is downstream of second-carrier output capture.

This runbook exists because the body now has a bounded capture lane, but not yet a result lane.

This file is a runbook only.

This file does not run commands.

This file does not create code.

This file does not create tests.

This file does not create artifact JSON.

This runbook does not create result, success, external result, cross-carrier proof, source, authority, currentness, runtime, final completion, or follow-on work.

The actual other-device run may produce captured output only.

The actual other-device run may now be prepared because bounded second-carrier output capture exists.

The actual other-device run still may not be called verification.

The actual other-device run still may not be called result.

The actual other-device run still may not be called success.

The actual other-device output still may not be called cross-carrier proof.

The actual other-device output capture is capture-only evidence until separately bounded result, success, external result, and cross-carrier evidence review steps are completed.

## 2. Status and Rank

- this runbook is additive
- this runbook ranks below constitutional/reference authority surfaces
- this runbook is downstream of second-carrier output capture terminal summary
- this runbook is downstream of second-carrier output capture live artifact
- this runbook is downstream of second-carrier output capture boundary terminal summary
- this runbook is downstream of second-carrier execution output terminal summary
- this runbook is downstream of second-carrier execution terminal summary
- this runbook does not replace any spec, resolver, test, artifact, or terminal summary
- this runbook does not create result, success, external result, cross-carrier evidence, source, authority, currentness, runtime, final completion, or follow-on work

This runbook does not authorize result boundary.

This runbook does not authorize result.

This runbook does not authorize success.

This runbook does not authorize external result.

This runbook does not authorize cross-carrier evidence review.

This runbook does not authorize runtime.

This runbook does not authorize deployment.

This runbook does not authorize public release.

This runbook does not authorize source transfer.

This runbook does not authorize source receipt.

This runbook does not authorize reception authorization.

This runbook does not authorize authority, currentness, or final completion.

This runbook does not repair, hide, erase, or claim passed any preserved predecessor failure.

This runbook does not rely on carrier possession, copy presence, green tests, artifact existence, artifact path, artifact size, timestamp, repo-local availability, hidden repo state, current working tree, cache, account, vendor, operating system, or environment state as result, success, proof, source, authority, currentness, runtime, final completion, or follow-on work.

## 3. What May Happen Under This Runbook

Under this runbook the operator may:

- prepare one transferable second-carrier live-run packet
- copy it to one actual second carrier/device
- run the selected command once on that second carrier/device
- capture stdout, stderr, exit code, command text, working directory, timestamp, and carrier label
- return the captured output to the original carrier for later bounded review
- preserve failure exactly if the run fails
- preserve partial output exactly if the run partially completes
- mark the returned material as capture-only evidence

Under this runbook the operator may not:

- edit the captured output
- repair the captured output
- summarize the captured output as result
- call a clean exit success
- call matching output verification
- call the second device authoritative
- call the capture cross-carrier proof
- infer runtime, currentness, final completion, or follow-on permission

Copying a packet or copied repository state under this runbook is not source transfer.

Returning captured output under this runbook is not source receipt.

No reception authorization is created by the live run, packet copy, or returned capture.

## 4. Pre-Run Checklist

Before the live run, the operator must confirm:

- the original repo state is intentionally selected for this run
- the second carrier/device is labelled but not treated as authority
- the transfer method is known
- the command to be run is selected from the standing portable-verification command / current active chain surfaces, not invented ad hoc
- the command is recorded before execution
- no secret/API key is required
- no network dependency is required unless explicitly declared
- captured output will include stdout, stderr, exit code, and command text
- any failure will be preserved, not repaired
- no result or success claim will be made from the run

If any checklist item cannot be confirmed, the operator should stop before the live run.

Stopping before the live run does not create failure, result, success, external result, cross-carrier evidence, source, authority, currentness, final completion, runtime, or follow-on work.

## 5. Transfer Packet Guidance

The transferable packet is a bounded carrier-transfer object.

It may include:

- the minimal repository or source subset needed for the run
- the relevant portable verification packet/artifact references
- the selected command text
- the expected capture fields
- a capture-only warning
- checksum/hash fields if available

It must not include:

- secret keys
- private tokens
- hidden local state
- undeclared cache dependency
- authority claim
- currentness claim
- result claim
- success claim
- runtime/deployment/public-release permission

The transferable packet remains a transfer object only.

The transferable packet is not source, authority, currentness, runtime, final completion, or follow-on permission.

Checksum/hash fields, if present, are integrity aids only. They are not result, success, external result, cross-carrier proof, source, authority, currentness, runtime, final completion, or follow-on permission.

## 6. Second-Carrier Execution Guidance

Second-carrier execution under this runbook means:

- one manual run
- on one labelled second carrier/device
- from a copied packet or copied repo state
- using the preselected command
- with no repair during execution
- with capture of actual terminal output

A failed run is still valid capture material if it is captured exactly.

A partially completed run is still valid capture material if partial output and failure posture are captured exactly.

A passing run is not automatically result, success, or proof.

A matching output is not automatically verification.

The second carrier/device remains labelled context only. It is not source, authority, currentness, runtime, final completion, or follow-on permission.

## 7. Capture Envelope

The capture envelope must include:

- `capture_id`
- `carrier_label`
- `carrier_type`
- `operator_label`
- `run_started_at`
- `run_completed_at`
- `working_directory`
- `command_text`
- `exit_code`
- `stdout_text`
- `stderr_text`
- `combined_terminal_log`
- `copied_packet_reference`
- `source_packet_reference`
- `capture_notes`
- `non_claims`
- `capture_only_statement`

The `non_claims` must preserve false posture for:

- `second_carrier_result_created`
- `second_carrier_success_created`
- `external_result_created`
- `cross_carrier_evidence_created`
- `source_transfer_occurred`
- `source_receipt_occurred`
- `reception_authorization_created`
- `source_created`
- `authority_created`
- `currentness_created`
- `final_completion_claimed`
- `runtime_hosting_created`
- `deployment_created`
- `public_release_created`
- `operation_permission_created`
- `continuation_authorized`
- `reusable_permission_created`
- `follow_on_work_authorized`

The `capture_only_statement` must say:

- this is captured output only
- this is not result
- this is not success
- this is not external result
- this is not cross-carrier evidence
- this is not source
- this is not authority
- this is not currentness
- this is not final completion
- this is not runtime
- this is not follow-on authorization

The capture envelope must preserve failure output exactly when failure occurs.

The capture envelope must preserve partial output exactly when partial completion occurs.

The capture envelope must not convert exit code, matching output, absence of stderr, carrier label, artifact path, artifact size, timestamp, operating system, vendor, account, repo-local availability, hidden repo state, or current working tree into result, success, verification, proof, source, authority, currentness, runtime, final completion, or follow-on work.

## 8. Return-to-Original-Carrier Guidance

Returned capture material must be copied back without editing.

The original carrier may preserve it as capture-only material.

The returned capture may later be used as basis for a separately bounded second-carrier result boundary.

That later use is not authorized by this runbook.

Returning captured output does not merge carriers.

Returning captured output does not make the second carrier source, authority, currentness, runtime, or final completion.

Returning captured output does not create result, success, external result, cross-carrier evidence, source transfer, source receipt, reception authorization, operation permission, continuation, reusable permission, or follow-on work.

## 9. Required Operator Warnings

- do not screenshot-only if text capture is available
- do not paraphrase output
- do not omit failure output
- do not clean terminal output after the fact
- do not convert exit code into success claim
- do not convert matching output into verification claim
- do not convert second device run into runtime permission
- do not convert capture into result
- do not convert capture into cross-carrier proof

The operator must preserve failed, noisy, partial, unexpected, or non-matching output as captured output only.

The operator must not repair output to match expectation.

The operator must not treat a clean terminal display as authority.

## 10. What Happens After the Live Run

After actual second-carrier live run/capture:

- the immediate next repo step is not automatic
- the captured material should be reviewed as capture-only
- if clean, the next lawful repo step is likely a second-carrier result boundary consuming real captured output
- if failed, the failure should be preserved as capture-only evidence
- no success, external result, or cross-carrier proof is created by the live run itself

The likely next lawful repo step remains separately bounded and unselected by this runbook.

No result boundary is opened by this runbook.

No result, success, external result, cross-carrier evidence review, source transfer, source receipt, reception authorization, runtime hosting, deployment, public release, authority, currentness, final completion, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work is authorized by this runbook.

## 11. What Remains Closed

Closed and not authorized:

- second-carrier result
- second-carrier success
- external result
- cross-carrier evidence
- source transfer
- source receipt
- reception authorization
- source
- authority
- currentness
- final completion
- runtime
- deployment
- public release
- continuation
- reusable permission
- follow-on work

Closed means not scheduled.

Closed means not authorized.

Closed means not executed.

## 12. Closing Statement

This runbook permits preparation for one actual second-carrier live run and capture only. It may allow a copied packet or copied repository state to be run on one labelled second carrier/device and may allow the resulting stdout, stderr, exit code, command text, and terminal log to be captured and returned as capture-only material. It does not create second-carrier result, second-carrier success, external result, cross-carrier evidence, source transfer, source receipt, reception authorization, source, authority, currentness, final completion, runtime, deployment, public release, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work. A passing second-carrier run is not success. A matching second-carrier output is not verification. Returned captured output is not cross-carrier proof. Any result, success, external result, cross-carrier evidence review, source transfer, source receipt, reception authorization, runtime hosting, deployment, public release, authority, currentness, final completion, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work still requires a separately bounded step.
