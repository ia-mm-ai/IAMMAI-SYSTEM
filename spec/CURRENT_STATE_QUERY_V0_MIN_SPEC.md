# Current State Query V0-Min Spec

## 1. Purpose

This file defines the first bounded current-state query spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, governing re-resolution, successor-adoption, effective-family, effective-family-consumption, current-work-input, current-work-operation, current-state-readout, current-state-handoff, current-state-export, current-state-delivery, current-state-application, and current-state answer/read surface stack:

- `src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py`
- `src/build_integrity_host_v0_min_coexistence_run_family_packet.py`
- `src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py`
- `src/build_current_integrity_host_v0_min_coexistence_governing_packet.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_transition.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_reresolution.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2.py`
- `src/resolve_current_integrity_host_v0_min_coexistence_effective_family.py`
- `src/resolve_integrity_host_v0_min_coexistence_effective_family_consumption.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_work_input.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_work_operation_v2.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_state_readout.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_state_handoff.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_state_export.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_state_delivery.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_state_application.py`
- `src/resolve_integrity_host_v0_min_coexistence_current_state_answer_surface.py`
- `spec/CURRENT_STATE_EXPORT_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_DELIVERY_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_APPLICATION_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_ANSWER_SURFACE_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful query surface that consumes an answered current-state surface and processes one bounded query into one bounded answer result.

An answered current-state result is now the bounded active surface for the first real query consumer. It preserves current-state application provenance, effective authority, family, status, governing, source-run, and ingress-run references, bounded answer/read output, checks, outcome, and carried-forward non-claims.

The next forced pressure is query, not more governance, currentness, export, delivery, application, answer/read, or packet packaging.

This spec does not implement query answering. It does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, a chat system, an API, a dashboard, a reporting system, or a broad workflow engine.

## 2. Status and Rank

This spec is additive and repo-local.

It ranks below the constitutional and reference authority surfaces under `reference/IAMMAI/`, including the constitutional protocol, implementation overviews, runtime contract surfaces, and architecture surfaces.

It also ranks below current executable source, tests, and generated artifacts where those surfaces already stand as concrete behavior.

This spec does not:

- define final governance
- complete continuity
- replace current executable source files
- replace current test surfaces
- replace emitted artifacts
- promote current-state answer/read emission into final system law
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded current-state query model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now emit a bounded current-state answer/read result.

That answer/read result is real. It preserves selected current-state application provenance, effective answer/read input references, bounded checks, explicit `ANSWERED` or `BLOCKED` outcome, bounded answer/read output, answer/read summary, and carried-forward non-claims.

Without one bounded query spec, the next consumer can still fail in three ways:

- it can drift back to stale prior-family artifacts because those artifacts remain readable
- it can expand into generic interface, API, chat, dashboard, reporting, or workflow machinery larger than the current executable pressure supports
- it can introduce broader ontology than the current body has lawfully made executable

A bounded current-state query spec is therefore required before query implementations are built. The query boundary says: read one answered current-state result, read one bounded query request, consume only the active references named by the answered result, emit one bounded query result, and preserve all prior artifacts unchanged.

## 4. What Now Stands

The current body materially has:

- canonical core execution line: `src/integrity_host_v0_min_coexistence_v2.py`
- current execution-authority resolution
- preserved-run family packet
- preserved-run status packet
- current-governing packet
- governing-transition resolver and result artifacts
- governing re-resolution resolver, result artifacts, and successor family emission
- governing successor-adoption v2 resolver and adoption result artifacts
- effective-family resolver and effective-family resolution artifacts
- effective-family consumption resolver and consumption result artifacts
- current-work-input resolver and current-work-input result artifacts
- current-work-operation v2 resolver and completed current-work-operation result artifacts
- current-state readout resolver and emitted current-state readout result artifacts
- current-state handoff resolver and handed-off current-state result artifacts
- current-state export resolver and exported current-state result artifacts
- current-state delivery resolver and delivered current-state result artifacts
- current-state application resolver and applied current-state result artifacts
- current-state answer/read resolver and answered current-state result artifacts
- explicit bounded non-claims around replay, merge, continuity completion, standing upgrade, minimum lawful system completion, final system identity, and final governance completion

These surfaces make one bounded downstream answer/read surface visible. They do not yet define the first bounded query that consumes the answered current-state result.

## 5. Current-State Query Scope

This current-state query slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads one answered current-state result and one bounded query request.

It governs one bounded downstream query step. The query may carry forward the answered surface, selected current-state application provenance, effective authority, family, preserved-run status, current-governing, source-run, and ingress-run references, but it must preserve all authority, family, status, governing, transition, re-resolution, adoption, effective-family, consumption, current-work-input, current-work-operation, current-state readout, current-state handoff, current-state export, current-state delivery, current-state application, and current-state answer/read artifacts unchanged.

The query surface is not a broad chat, API, dashboard, connector, app, reporting, or workflow system. It does not define orchestration, prompt routing, memory, queues, registries, scheduling, persistence topology, cross-host continuity completion, replay, or merge.

Current-state query answering is a checked downstream query over an already answered bounded current-state result. It is not hidden update, host replay, continuity completion, final currentness doctrine, final system identity law, or query output as standing law.

## 6. Query Input Set

A bounded current-state query needs the following input set:

- one answered current-state result artifact
- one bounded query request
- the effective execution-authority artifact referenced by the answered result
- the effective run-family packet referenced by the answered result
- the effective preserved-run status packet referenced by the answered result
- the effective current-governing packet referenced by the answered result

The active query references are the paths in the current-state answer/read result's `effective_answer_read_inputs` section and, where useful, its bounded `answer_read_output` section:

- `effective_authority_artifact_path`
- `effective_family_packet_path`
- `effective_status_packet_path`
- `effective_current_governing_packet_path`
- `effective_source_run_path`
- `effective_ingress_run_path`
- `current_governing_source_run_path`
- `current_governing_ingress_run_path`

Prior current families may remain preserved and readable. They are not the active query inputs when an answered current-state result names a different effective family.

Blocked, stale, or non-answered current-state results do not drive query answering. A query must not bypass the answered current-state result and decide active inputs by scanning authority, family, status, governing, adoption, effective-family, consumption, current-work-input, current-work-operation, current-state readout, current-state handoff, current-state export, current-state delivery, current-state application, or current-state answer/read roots on its own.

## 7. Allowed Query Shape

The first bounded query shape is intentionally narrow.

A query request should be a compact object such as:

```text
CurrentStateQueryRequest {
  query_request_id: string
  query_target: string
  requested_fields: list[string]
  query_basis: string
}
```

Rules:

- `query_request_id` must be non-empty.
- `query_target` must be constrained to the answered current-state result and its bounded answer/read output.
- `requested_fields` must name fields already exposed by the answered current-state result or its bounded output.
- `query_basis` must be non-empty and must identify why this bounded read is being requested.

The first bounded query may ask about:

- current governing source run path
- current governing ingress run path
- current authority artifact path
- current family packet path
- current preserved-run status packet path
- current-governing packet path
- preserved run count where visible
- current authority run count where visible
- preserved eligible non-authority count where visible
- preserved ineligible count where visible
- current-work basis where visible
- readout basis where visible
- handoff basis where visible
- export basis where visible
- delivery basis where visible
- application basis where visible
- answer/read basis where visible
- carried-forward bounded non-claims

The query must not require ontology, facts, hidden provenance, world-state conclusions, final identity, replay, merge, continuity completion, or standing upgrade beyond what the current-state answer/read result already lawfully carries.

## 8. Input Correspondence Requirements

Before query answering may be considered, the selected inputs must correspond in bounded form.

At minimum:

- the current-state answer/read result artifact is readable
- the current-state answer/read result has a bounded successful outcome: `ANSWERED`
- the current-state answer/read result is not blocked, malformed, or non-answered
- active query references in the result point to readable artifacts
- canonical core execution file matches across the effective authority, family, status, and governing artifacts
- the active query input set is internally coherent
- effective authority, family, status, and governing artifacts name the same current governing source run where those surfaces expose it
- effective authority, family, status, and governing artifacts name the same current governing ingress run where those surfaces expose it
- bounded non-claims remain false
- prior family remains preserved and readable where the current-state answer/read result exposes that posture
- the query request is bounded to answerable fields already exposed by the answered current-state result

Unreadable or mismatched inputs, or out-of-scope queries, block the query. They must not be silently fused into a current-state query answer.

## 9. Query Checks

A bounded current-state query may be answered only when all bounded checks pass.

Minimum required checks:

- current-state answer/read result exists and is readable
- current-state answer/read outcome is `ANSWERED`
- effective execution-authority artifact is readable and coherent
- effective run-family packet is readable and coherent
- effective preserved-run status packet is readable and coherent
- effective current-governing packet is readable and coherent
- effective family canonical core execution file matches `src/integrity_host_v0_min_coexistence_v2.py`
- effective authority, family, status, and governing artifacts name the same current governing source run where those surfaces expose it
- effective authority, family, status, and governing artifacts name the same current governing ingress run where those surfaces expose it
- effective family preserves bounded non-claims:
  - `replayed_into_live_host = false`
  - `merged_into_local_state = false`
  - `continuity_completed = false`
  - `standing_upgraded = false`
- the query uses the answered current-state result explicitly rather than inferring latest authority, family, status, or governing artifacts on its own
- the query does not silently use stale prior-family artifacts when current-state answer/read names a different effective family
- the query request stays within the bounded answerable surface already exposed

These checks are bounded and implementation-facing. They do not create a broad chat, API, dashboard, reporting, or workflow engine.

## 10. Refusal / Block Conditions

Blocked current-state query answering must remain explicit. It is downstream current-state query refusal/blocking, not transition refusal, re-resolution blocking, adoption blocking, effective-family consumption blocking, current-work-input blocking, current-work-operation blocking, current-state readout blocking, current-state handoff blocking, current-state export blocking, current-state delivery blocking, current-state application blocking, or current-state answer/read blocking.

Minimum block conditions:

- no current-state answer/read result is available
- current-state answer/read result is unreadable
- current-state answer/read result has an unrecognized, blocked, or non-answered outcome
- effective query artifacts are unreadable
- canonical execution line mismatch
- effective query input set is not internally coherent
- effective query input set does not correspond to the current-state answer/read result
- prior family preservation is not evident where required
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent fallback to stale prior-family artifacts attempted
- latest-file inference attempted without explicit current-state answer/read support
- query request exceeds the bounded answerable surface
- multiple current-state answer/read results conflict without an explicit bounded selection surface

Blocked query answering should preserve enough detail to show which current-state answer/read result was considered, which query request was refused, which effective references failed, and which non-claims remained required.

## 11. Query Contract

A current-state query is any downstream bounded component, resolver, builder, validator, operator-read surface, API-read surface, or vessel-style read surface that emits one explicit query result using an answered current-state result as its active selector.

A query may rely on:

- the answered current-state result as the explicit selector of active query inputs
- the effective execution-authority artifact as the active bounded authority artifact
- the effective run-family packet as the active bounded family packet
- the effective preserved-run status packet as the active bounded status packet
- the effective current-governing packet as the active bounded governing packet
- the effective source and ingress run paths where the answer/read result exposes them
- the bounded answer/read output emitted by the current-state answer/read result
- the carried-forward non-claims that remain false
- the fact that preserved prior families remain preserved but are not silently substituted for the active query inputs

A query must not infer:

- continuity completion
- replay permission
- merge permission
- standing upgrade
- final governance or final system identity
- final currentness doctrine
- persistence or registry law
- automatic latest-emitted fallback without explicit current-state answer/read support
- facts or ontology not already lawfully exposed by the answered current-state surface

## 12. Query Result Artifact

A future bounded implementation should emit one current-state query result artifact.

The smallest useful result artifact preserves:

- query result id
- query result type/version
- generated_at
- current-state answer/read result artifact path used
- current-state answer/read result id used
- bounded query request
- effective authority artifact path consumed
- effective family packet path consumed
- effective preserved-run status packet path consumed
- effective current-governing packet path consumed
- effective source run path where used
- effective ingress run path where used
- outcome: `ANSWERED_QUERY` or `BLOCKED`
- block code and block reason if blocked
- query basis
- checks or bounded check summary
- carried-forward non-claims

A calm implementation-facing artifact shape may use sections such as:

- `query_metadata`
- `selected_current_state_answer_read`
- `query_request`
- `effective_query_inputs`
- `checks`
- `outcome`
- `block`
- `query_answer`
- `query_summary`
- `non_claims`

For `ANSWERED_QUERY`, the result should preserve the active inputs consumed and the bounded query answer output or answer reference. The output should answer only the requested bounded fields and should preserve enough provenance to show that the answer was derived from the selected current-state answer/read result.

For `BLOCKED`, the result should preserve the candidate current-state answer/read identity if any, the bounded query request if any, the block reason, and enough failed-check detail to keep refusal visible.

This section does not design a future chat system, API, dashboard, reporting system, or workflow engine. It only states the minimum provenance, outcome, block, query, answer, and non-claim visibility expected of the first bounded current-state query surface.

## 13. What Remains Preserved

After lawful current-state query answering:

- prior execution-authority artifacts remain preserved
- prior run-family packets remain preserved
- prior preserved-run status packets remain preserved
- prior current-governing packets remain preserved
- governing-transition result artifacts remain preserved
- governing re-resolution result artifacts remain preserved
- successor-adoption result artifacts remain preserved
- effective-family resolution artifacts remain preserved
- effective-family consumption result artifacts remain preserved
- current-work-input resolution artifacts remain preserved
- current-work-operation result artifacts remain preserved
- current-state readout artifacts remain preserved
- current-state handoff artifacts remain preserved
- current-state export artifacts remain preserved
- current-state delivery artifacts remain preserved
- current-state application artifacts remain preserved
- current-state answer/read artifacts remain preserved
- current-state query artifacts remain additive
- source runs remain preserved
- ingress runs remain preserved
- source-to-ingress comparison artifacts remain preserved
- preserved runs remain visible

Query answering must not imply hidden mutation, hidden selection, hidden standing upgrade, hidden continuity completion, hidden replay, hidden merge, or hidden replacement of prior artifacts.

## 14. What This Spec Still Does Not Define

This spec still does not define:

- final governance framework
- final currentness doctrine
- final system identity law
- final continuity completion
- replay or merge law
- persistence architecture
- registry doctrine
- full world-frame
- minimum lawful system
- downstream query semantics beyond the smallest bounded case
- multi-query orchestration beyond the smallest bounded case
- a generic app, API, dashboard, reporting, or workflow framework

## 15. What Should Not Be Added Next

The repo should not move next by adding a broader interface layer that bypasses the answered current-state result.

In compact terms:

- no direct stale-artifact reads when an answered current-state result exists
- no replay-based query answering
- no merge-based query answering
- no broad app, API, dashboard, reporting, chat, or workflow engine
- no new packet that only restates current-state answer/read selection without new behavioral pressure
- no persistence or registry substitute for query law

The next lawful implementation pressure, if pursued, is one bounded query resolver over one answered current-state result and one bounded query request, not a general reader platform.

## 16. Closing Boundary Statement

The repository now has current-state answer/read.

This spec exists because the next forced pressure is the first real current-state query surface.

It defines the smallest bounded query model now supportable: consume one answered current-state result, consume one bounded query request, verify the effective inputs the answered result names, emit one explicit `ANSWERED_QUERY` or `BLOCKED` query result, preserve non-claims, and leave all prior artifacts unchanged.

It does not claim final governance, final continuity completion, final currentness doctrine, final system identity, or system completion.
