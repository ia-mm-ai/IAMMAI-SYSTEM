# Portable Source-Body Verification Actual Second-Carrier Live Capture Packet V0

## 1. Purpose

This packet prepares one actual second-carrier live run and capture.

This packet is downstream of `PORTABLE_SOURCE_BODY_VERIFICATION_ACTUAL_SECOND_CARRIER_LIVE_RUNBOOK_V0.md`.

This packet is downstream of second-carrier output capture.

This packet records the selected command and capture envelope for operator use.

This packet does not execute anything.

This packet does not create code.

This packet does not create tests.

This packet does not create artifact JSON.

This packet does not create executable scripts.

This packet does not create result, success, external result, cross-carrier evidence, source, authority, currentness, runtime, final completion, or follow-on work.

The body now has a bounded capture lane.

The actual second carrier may now be allowed to produce captured output.

The captured output must remain capture-only material.

The captured output is not result.

The captured output is not success.

The captured output is not verification.

The captured output is not external result.

The captured output is not cross-carrier proof.

The second carrier is not source, authority, currentness, runtime, final completion, or follow-on permission.

## 2. Status and Rank

- this packet is additive
- this packet ranks below constitutional/reference authority surfaces
- this packet is downstream of the actual second-carrier live runbook
- this packet is downstream of second-carrier output capture terminal summary
- this packet is downstream of second-carrier output capture live artifact
- this packet does not replace any spec, resolver, test, artifact, terminal summary, or runbook
- this packet is an operator packet only
- this packet does not authorize result boundary/result/success/external result/cross-carrier evidence review
- this packet does not authorize runtime/deployment/public release
- this packet does not authorize source transfer/source receipt/reception authorization
- this packet does not authorize source/authority/currentness/final completion/follow-on work

This packet does not repair, hide, erase, or claim passed any preserved predecessor failure.

This packet does not rely on carrier possession, copy presence, green tests, artifact existence, artifact path, artifact size, timestamp, repo-local availability, hidden repo state, current working tree, cache, account, vendor, operating system, or environment state as result, success, proof, source, authority, currentness, runtime, final completion, or follow-on work.

## 3. Live Run Identity

Fillable live-run identity fields:

- `live_run_id`:
- `operator_label`:
- `original_carrier_label`:
- `second_carrier_label`:
- `second_carrier_type`:
- `transfer_method`:
- `source_repo_or_packet_reference`:
- `copied_repo_or_packet_location`:
- `run_started_at`:
- `run_completed_at`:
- `capture_return_method`:

Labels identify context only.

Labels do not create authority, source, currentness, runtime, final completion, or follow-on work.

Second-carrier label does not make the second carrier source, authority, currentness, runtime, final completion, or follow-on permission.

Carrier possession, copy presence, path presence, timestamp, operating system, vendor, account, environment state, repo-local availability, hidden repo state, current working tree, cache, artifact existence, artifact path, or artifact size does not create result, success, verification, proof, source, authority, currentness, runtime, final completion, or follow-on work.

## 4. Selected Command

The selected command must be recorded before execution.

The selected command is the active successor-chain unittest command.

The operator may run either:

- the narrow second-carrier-output-capture test only, or
- the full active successor chain.

The narrow test command is:

```bash
cd <COPIED_IAMMAI_SYSTEM_REPO_PATH>
python3 -m unittest \
  tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py
```

The full active successor-chain command is:

```bash
cd <COPIED_IAMMAI_SYSTEM_REPO_PATH>
python3 -m unittest \
  tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_output_capture_boundary.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_execution_output.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_execution_output_boundary.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_execution.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_execution_boundary.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_receipt.py \
  tests/test_resolve_portable_source_body_verification_second_carrier_receipt_boundary.py \
  tests/test_resolve_portable_source_body_verification_packet_transfer.py \
  tests/test_resolve_portable_source_body_verification_packet_transfer_boundary.py \
  tests/test_resolve_portable_source_body_verification_packet_emission.py \
  tests/test_resolve_portable_source_body_verification_packet_emission_boundary_v2.py \
  tests/test_resolve_portable_source_body_verification_packet_artifact.py \
  tests/test_resolve_portable_source_body_verification_packet_boundary.py \
  tests/test_resolve_portable_source_body_verification_command_success.py \
  tests/test_resolve_portable_source_body_verification_command_success_boundary_v3.py \
  tests/test_resolve_portable_source_body_verification_command_result_v2.py \
  tests/test_resolve_portable_source_body_verification_command_result_boundary.py \
  tests/test_resolve_portable_source_body_verification_command_output_report_artifact.py \
  tests/test_resolve_portable_source_body_verification_command_output_report_artifact_boundary.py \
  tests/test_resolve_portable_source_body_verification_output_capture_v2.py \
  tests/test_resolve_portable_source_body_verification_output_capture_boundary.py \
  tests/test_resolve_portable_source_body_verification_command_output.py \
  tests/test_resolve_portable_source_body_verification_command_output_boundary.py \
  tests/test_resolve_portable_source_body_verification_command_output_containment.py \
  tests/test_resolve_portable_source_body_verification_command_output_containment_boundary.py \
  tests/test_resolve_portable_source_body_verification_post_invocation_command_execution.py \
  tests/test_resolve_portable_source_body_verification_post_invocation_command_execution_boundary.py \
  tests/test_resolve_portable_source_body_verification_command_invocation.py \
  tests/test_resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary.py \
  tests/test_resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization.py \
  tests/test_resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary.py \
  tests/test_resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review.py \
  tests/test_resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary.py \
  tests/test_resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption.py \
  tests/test_resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_v2.py \
  tests/test_resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2.py \
  tests/test_resolve_portable_source_body_verification_command_execution_boundary.py \
  tests/test_portable_source_body_verification_command.py \
  tests/test_resolve_portable_source_body_verification_command_implementation_boundary.py \
  tests/test_resolve_portable_source_body_verification_command_boundary.py \
  tests/test_resolve_artifact_emission_containment_boundary.py \
  tests/test_resolve_portable_source_body_verification_evidence_manifest_boundary.py \
  tests/test_resolve_portable_source_body_verification_boundary.py
```

Preserved failed-lineage tests remain excluded unless intentionally testing old failures:

- `tests/test_resolve_portable_source_body_verification_packet_emission_boundary.py`
- `tests/test_resolve_portable_source_body_verification_command_success_boundary.py`
- `tests/test_resolve_portable_source_body_verification_command_success_boundary_v2.py`
- `tests/test_resolve_portable_source_body_verification_command_result.py`
- `tests/test_resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary.py`
- `tests/test_resolve_portable_source_body_verification_output_capture.py`

A passing command is not success, not result, and not verification.

A failing command is still valid capture-only material if captured exactly.

Running either selected command once under this packet may produce captured output only.

The selected command does not create result boundary, result, success, external result, cross-carrier evidence, source transfer, source receipt, reception authorization, source, authority, currentness, runtime, final completion, continuation, reusable permission, or follow-on work.

## 5. Expected Capture Fields

Fillable capture envelope:

```json
{
  "capture_id": "",
  "carrier_label": "",
  "carrier_type": "",
  "operator_label": "",
  "run_started_at": "",
  "run_completed_at": "",
  "working_directory": "",
  "command_text": "",
  "exit_code": null,
  "stdout_text": "",
  "stderr_text": "",
  "combined_terminal_log": "",
  "copied_packet_reference": "",
  "source_packet_reference": "",
  "capture_notes": "",
  "non_claims": {
    "second_carrier_result_created": false,
    "second_carrier_success_created": false,
    "external_result_created": false,
    "cross_carrier_evidence_created": false,
    "source_transfer_occurred": false,
    "source_receipt_occurred": false,
    "reception_authorization_created": false,
    "source_created": false,
    "authority_created": false,
    "currentness_created": false,
    "final_completion_claimed": false,
    "runtime_hosting_created": false,
    "deployment_created": false,
    "public_release_created": false,
    "operation_permission_created": false,
    "continuation_authorized": false,
    "reusable_permission_created": false,
    "follow_on_work_authorized": false
  },
  "capture_only_statement": "This is captured output only. It is not result, success, external result, cross-carrier evidence, source, authority, currentness, final completion, runtime, or follow-on authorization."
}
```

This envelope is a capture envelope only.

Filling the envelope does not create result, success, external result, cross-carrier evidence, source, authority, currentness, runtime, final completion, or follow-on work.

Filling the envelope does not create source transfer, source receipt, reception authorization, deployment, public release, operation permission, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work.

Exit code is captured terminal material only.

Stdout text is captured terminal material only.

Stderr text is captured terminal material only.

Combined terminal log is captured terminal material only.

Capture notes must not summarize the output as result, success, verification, proof, source, authority, currentness, runtime, final completion, or follow-on work.

## 6. Operator Procedure

1. Copy the selected repository/packet to the second carrier.
2. Label the second carrier.
3. Open terminal on the second carrier.
4. Record working directory.
5. Record exact selected command before execution.
6. Run the selected command once.
7. Capture stdout, stderr, exit code, and terminal log exactly.
8. Do not repair or clean output.
9. Fill the capture envelope.
10. Return the capture envelope and raw terminal log to the original carrier.
11. Preserve the returned material as capture-only material.

Copying the selected repository/packet for this run is operational packet movement only.

Copying does not create source transfer.

Returning the capture envelope does not create source receipt.

No reception authorization is created by this procedure.

The procedure stops at capture-only material.

## 7. Capture Handling Rules

- preserve exact stdout
- preserve exact stderr
- preserve exact exit code
- preserve exact command text
- preserve failure output
- preserve partial output
- preserve unexpected output
- do not paraphrase
- do not summarize as result
- do not convert matching output into verification
- do not convert clean exit into success
- do not convert returned capture into cross-carrier proof

Do not edit captured output.

Do not repair captured output.

Do not normalize captured output into a cleaner story.

Do not omit failure output.

Do not omit stderr because stdout appears clean.

Do not convert absence of stderr into success.

Do not convert a zero exit code into success.

Do not convert a nonzero exit code into final failure.

Do not convert matching output into verification.

Do not convert second-carrier execution into runtime permission.

Do not convert returned captured output into cross-carrier proof.

Do not rely on carrier possession, copy presence, green tests, artifact existence, artifact path, artifact size, timestamp, repo-local availability, hidden repo state, current working tree, cache, account, vendor, operating system, or environment state as result, success, proof, source, authority, currentness, runtime, final completion, or follow-on work.

## 8. Return Guidance

- returned material must be copied back without editing
- returned material may later serve as basis for a separately bounded second-carrier result boundary
- this packet does not authorize that result boundary
- returning captured output does not merge carriers
- returning captured output does not make the second carrier source, authority, currentness, runtime, or final completion

Returned material remains capture-only material.

Returned material does not create result.

Returned material does not create success.

Returned material does not create external result.

Returned material does not create cross-carrier evidence.

Returned material does not create source transfer.

Returned material does not create source receipt.

Returned material does not create reception authorization.

Returned material does not create source, authority, currentness, runtime, final completion, deployment, public release, operation permission, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work.

## 9. Closed Claims

Closed and not authorized:

- result
- success
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
- derivative reception
- vessel relation
- another reception request
- follow-on work

Closed means not scheduled.

Closed means not authorized.

Closed means not executed.

This packet does not create result boundary.

This packet does not create result.

This packet does not create success.

This packet does not create external result.

This packet does not create cross-carrier evidence.

This packet does not create source transfer.

This packet does not create source receipt.

This packet does not create reception authorization.

This packet does not authorize runtime, deployment, or public release.

This packet does not authorize authority, currentness, or final completion.

This packet does not authorize continuation, reusable permission, or follow-on work.

## 10. After Capture

- after actual capture, stop
- do not proceed automatically to result boundary
- preserve returned capture material
- review as capture-only
- only after review may a separately bounded second-carrier result boundary be selected
- if the run fails, preserve failure as capture-only evidence
- if the run passes, preserve pass as capture-only evidence
- neither failure nor pass creates result, success, external result, or cross-carrier proof

The immediate post-capture posture is pause / observation.

The next repo step is not automatic.

Any second-carrier result boundary must be selected separately.

Any second-carrier result must be created separately.

Any second-carrier success must be created separately.

Any external result must be created separately.

Any cross-carrier evidence review must be created separately.

Any source transfer, source receipt, reception authorization, runtime hosting, deployment, public release, authority, currentness, final completion, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work still requires a separately bounded step.

## 11. Closing Statement

This live capture packet prepares one actual second-carrier live run and capture only. It records selected command options and a capture envelope for stdout, stderr, exit code, command text, working directory, carrier label, and terminal log. It does not execute the run, does not create result, does not create success, does not create external result, does not create cross-carrier evidence, does not create source transfer, does not create source receipt, does not create reception authorization, and does not create source, authority, currentness, final completion, runtime, deployment, public release, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work. A passing second-carrier run is not success. A matching second-carrier output is not verification. Returned captured output is not cross-carrier proof. Any result, success, external result, cross-carrier evidence review, source transfer, source receipt, reception authorization, runtime hosting, deployment, public release, authority, currentness, final completion, continuation, reusable permission, derivative reception, vessel relation, another reception request, or follow-on work still requires a separately bounded step.
