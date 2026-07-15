# OpenAI API Derivative Vessel: Bounded Current-State Read V0-Min Spec

## 1. Purpose

This file defines the first bounded OpenAI API derivative vessel spec for the present `IAMMAI-SYSTEM` repository line.

The v0 body now stands strongly enough as one bounded body through the current-state line, the current-state admissibility / touch-permission bridge, continuity transfer, continuity receipt, received-derivative participation, received-derivative action permission, continuity-memory seam closure, and the v0 body pass.

The next pressure is therefore not another internal branch. It is one bounded derivative vessel / operator case supportable by the body already standing.

This file defines the smallest lawful OpenAI API vessel test supportable by the current body: one shell-owned, bounded derivative read over one already-standing current-state surface, with the model acting only as a derivative reader / operator over one bounded packet.

This file does not define a full OpenAI integration architecture, a general agent framework, a middleware layer, a whole-body orchestration system, a broad participation doctrine, a final vessel doctrine, or final governance.

## 2. Status and Rank

This spec ranks below the constitutional and reference authority surfaces under `reference/IAMMAI/`.

It is additive to the present executable line. It does not replace the canonical executable source, the tests, the emitted artifacts, the current-state surfaces, the derivative support line, the continuity-memory seam, or the v0 body pass.

It does not define final governance. It does not replace the body. It does not make the model a governing participant. It does not assign the model rank, authority, status, or standing.

It is a bounded derivative vessel spec for the present repo only.

## 3. Why This Spec Is Needed Now

The v0 body now stands strongly enough as one bounded body to support one narrow derivative vessel test.

That support does not justify reopening wide-vessel ambition. The earlier lesson from broader API vessel attempts is the opposite: keep the model narrow, keep the packet explicit, keep provenance and refusal local, and keep law in shell-owned code.

Therefore the first vessel use must be as small as possible. It must leave body law, standing, refusal, and result wrapping in local code while allowing the model to perform only one bounded derivative read.

## 4. Cleanest First Vessel Use-Case

The cleanest first vessel use-case is:

- one bounded derivative read
- over one already-standing current-state surface

The preferred first source family is:

- `current_state_what_stands_now_result`

This is the cleanest first case because it is already bounded, already strong, already downstream of the standing line, answerable without broad interpretation, and already shaped for explicit current-state reading.

It also keeps the model derivative and keeps shell law local. The model reads one bounded packet. The shell keeps source selection, packet law, provenance, refusal, validation, and artifact ownership.

## 5. Allowed Source Surface Family

For this first vessel slice, the allowed source family is exactly:

- `current_state_what_stands_now_result`

The shell must select one explicit source artifact from that family.

The shell must then extract one bounded payload from that selected artifact. The shell may not pass the whole repo, the whole artifact family, multiple current-state surfaces, hidden auxiliary files, or implicitly discovered context.

This first vessel slice does not allow:

- whole-repo reading
- multi-surface widening
- implicit source discovery
- latest-file inference
- fallback to other source families because they happen to exist

If the shell cannot name one explicit `current_state_what_stands_now_result`, this vessel slice must refuse rather than widen.

## 6. Admitted Use Class

The admitted use class for this first vessel slice is:

- `BOUNDED_DERIVATIVE_READ`

In this spec, `BOUNDED_DERIVATIVE_READ` means:

- read only
- derivative only
- no authority
- no standing assignment
- no provenance assignment
- no mutation
- no continuation claim
- no participation mythology

The model may read and answer from a shell-provided bounded packet. It may not become source, authority, rank-holder, standing-holder, or body-law interpreter.

## 7. Shell-Owned Contract

The shell / local repo code must own:

- source selection
- allowed source family
- packet construction
- provenance
- rank
- status
- non-claims
- refusal semantics
- output validation
- result wrapping
- artifact writing

The shell decides whether the selected source artifact is admissible. The shell decides which fields are extracted. The shell decides whether the packet is lawful. The shell decides whether the returned model output is within contract. The shell writes any repo-local artifact or result.

The shell is the law.

The model is not.

## 8. Model Role

For this first vessel slice, the model may:

- read one shell-provided bounded packet
- answer one bounded question from that packet
- optionally emit one tiny model-level refusal code if the packet is insufficiently grounded

The model must not:

- assign rank
- assign authority
- assign standing
- decide provenance
- widen source scope
- discover more files on its own
- invent body law
- invent non-claims
- decide whether the body is complete
- convert derivative output into source
- treat its answer as current-state law
- claim operator participation beyond this bounded derivative read

The model is a derivative reader / operator over one packet only.

## 9. Input Packet

The shell must construct one bounded vessel input packet with this shape:

```text
OpenAIDerivativeVesselRequest {
  vessel_request_id: string
  vessel_use_case: "BOUNDED_CURRENT_STATE_READ"
  admitted_use_class: "BOUNDED_DERIVATIVE_READ"
  allowed_source_family: "current_state_what_stands_now_result"
  selected_source_surface_id: string
  selected_source_surface_path: string
  question: string
  bounded_source_payload: {
    current_governing_source_run_path: string
    current_governing_ingress_run_path: string
    current_authority_artifact_path: string
    preserved_run_count: integer
    application_basis: string
    delivery_basis: string
    answer_read_basis: string
  }
  instructions: string
}
```

For this first slice, the shell must pass only the bounded source payload above. It does not pass the whole selected artifact, the whole repo, hidden auxiliary files, or silently discovered companion surfaces.

The `question` must be one bounded current-state read question answerable from the bounded source payload alone.

The `instructions` must direct the model to:

- answer only from `bounded_source_payload`
- not use hidden context
- not widen source scope
- not assign rank, authority, provenance, status, or non-claims
- refuse with the tiny refusal code if insufficiently grounded

## 10. Output Contract

The first bounded model success contract is:

```text
{ "answer": string }
```

The optional tiny model-level refusal contract is:

```text
{ "refusal_code": "INSUFFICIENT_GROUNDING" }
```

No other model output contract is admitted in this first slice.

Malformed output, extra output, hidden provenance fields, rank fields, status fields, non-claims, or packet rewrites are treated by the shell as failure or refusal.

The model does not emit provenance, rank, status, non-claims, or result-law.

## 11. Refusal Path

This first vessel slice has two refusal layers.

The tiny model-level refusal is:

- `INSUFFICIENT_GROUNDING`

All real law and refusal semantics remain shell-owned.

The shell-level refusal path must remain explicit for at least:

- `INVALID_SOURCE_FAMILY`
- `MISSING_SOURCE_ARTIFACT`
- `MALFORMED_VESSEL_PACKET`
- `WIDENED_SOURCE_ATTEMPT`
- `UNSUPPORTED_USE_CLASS`
- `MODEL_OUTPUT_MALFORMED`
- `MODEL_OUTPUT_OUTSIDE_CONTRACT`
- `LOCAL_SETUP_FAILURE`
- `API_CALL_FAILURE`

If the model emits `INSUFFICIENT_GROUNDING`, the shell remains responsible for wrapping that result, preserving provenance, preserving non-claims, and refusing any silent widening.

## 12. Local Repo / Runtime Setup

Inside this repository environment, the local runtime must have:

- the OpenAI client package installed in the repo-local environment
- `OPENAI_API_KEY` present
- optional `OPENAI_MODEL`

This setup must be checked inside the local `IAMMAI-SYSTEM` environment at runtime. It must not be assumed from old work, global shell state, or prior machines.

For this first slice:

- missing client package is a local setup failure
- missing `OPENAI_API_KEY` is a local setup failure
- malformed API output is a vessel failure
- silent fake success is not allowed

If `OPENAI_MODEL` is absent, model selection remains a shell-owned configuration decision, not a model-owned one.

## 13. What This First Vessel Still Does Not Do

This first vessel does not do:

- broad agent behavior
- full participation doctrine
- middleware completion
- whole-body orchestration
- repo-wide reading
- source-family widening
- model-owned provenance, rank, or status
- doctrine generation
- autonomous action
- AI participation claims
- source replacement
- continuity completion

It is one bounded derivative read only.

## 14. What Should Not Be Added Next

This repo should not reopen wide-vessel ambition through the back door.

What should probably not be added next:

- whole-body model read
- autonomous orchestration
- model-owned rank or provenance
- hidden source widening
- broad chat, app, tool, or workflow framework
- inflated "AI participation" claims
- middleware mythology
- derivative output treated as source

Further vessel work should remain forced by bounded executable pressure, not by available model capability.

## 15. Closing Boundary Statement

The first lawful vessel test in this repo is one shell-owned, bounded derivative read over one already-standing current-state surface.

The body remains the law.

The vessel remains derivative.

This is the smallest lawful OpenAI API test supportable by the now-closed v0 body.
