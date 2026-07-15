# Current State Application V0-Min Spec

## 1. Purpose

This file defines the first bounded current-state application spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, governing re-resolution, successor-adoption, effective-family, effective-family-consumption, current-work-input, current-work-operation, current-state-readout, current-state-handoff, current-state-export, and current-state-delivery stack:

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
- `spec/EFFECTIVE_FAMILY_CONSUMPTION_V0_MIN_SPEC.md`
- `spec/CURRENT_WORK_OPERATION_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_READOUT_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_HANDOFF_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_EXPORT_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_DELIVERY_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful downstream application-level consumer that consumes a delivered current-state result and performs one bounded application step.

A delivered current-state result is now the bounded active surface for the first real downstream application. It preserves current-state export provenance, effective authority, family, status, governing, source-run, and ingress-run references, bounded delivery output, checks, outcome, and carried-forward non-claims.

The next forced pressure is application, not more governance, currentness, selection, export, delivery, or packet packaging.

This spec does not implement application. It does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, an app framework, an API, a dashboard, a reporting system, or a broad workflow engine.

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
- promote current-state delivery into final system law
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded current-state application model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now emit a bounded current-state delivery.

That delivery is real. It preserves selected current-state export provenance, effective delivery input references, bounded checks, explicit `DELIVERED` or `BLOCKED` outcome, bounded delivery output, delivery summary, and carried-forward non-claims.

Without one bounded application spec, the next consumer can still fail in three ways:

- it can drift back to stale prior-family artifacts because those artifacts remain readable
- it can expand into generic app, API, dashboard, reporting, or workflow machinery larger than the current executable pressure supports
- it can introduce broader ontology than the current body has lawfully made executable

A bounded current-state application spec is therefore required before application-level implementations are built. The application boundary says: read one delivered current-state result, consume only the active references it names, perform one bounded application step, emit one explicit application result, and preserve all prior artifacts unchanged.

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
- explicit bounded non-claims around replay, merge, continuity completion, standing upgrade, minimum lawful system completion, final system identity, and final governance completion

These surfaces make one bounded downstream delivery visible. They do not yet define the first bounded application step that consumes the delivered current-state result.

## 5. Current-State Application Scope

This current-state application slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads one delivered current-state result and the active input references named by that result.

It governs one bounded downstream application step. The application may carry forward the delivered surface, selected current-state export provenance, effective authority, family, preserved-run status, current-governing, source-run, and ingress-run references, but it must preserve all authority, family, status, governing, transition, re-resolution, adoption, effective-family, consumption, current-work-input, current-work-operation, current-state readout, current-state handoff, current-state export, and current-state delivery artifacts unchanged.

The application is not a broad dashboard, API, connector, app, reporting, or workflow system. It does not define orchestration, queues, registries, scheduling, persistence topology, cross-host continuity completion, replay, or merge.

Current-state application is a checked downstream application-level consumer over an already delivered bounded current-state result. It is not hidden update, host replay, continuity completion, final currentness doctrine, final system identity law, or application as standing law.

## 6. Application Input Set

A bounded current-state application needs the following input set:

- one delivered current-state result artifact
- the effective execution-authority artifact referenced by that result
- the effective run-family packet referenced by that result
- the effective preserved-run status packet referenced by that result
- the effective current-governing packet referenced by that result

The active application references are the paths in the current-state delivery result's `effective_delivery_inputs` section and, where useful, its bounded `delivery_output` section:

- `effective_authority_artifact_path`
- `effective_family_packet_path`
- `effective_status_packet_path`
- `effective_current_governing_packet_path`
- `effective_source_run_path`
- `effective_ingress_run_path`
- `current_governing_source_run_path`
- `current_governing_ingress_run_path`

Prior current families may remain preserved and readable. They are not the active application inputs when a delivered current-state result names a different effective family.

Blocked, stale, or non-delivered current-state results do not drive application. An application must not bypass the delivered current-state result and decide active application inputs by scanning authority, family, status, governing, adoption, effective-family, consumption, current-work-input, current-work-operation, current-state readout, current-state handoff, current-state export, or current-state delivery roots on its own.

## 7. Input Correspondence Requirements

Before application may be considered, the selected inputs must correspond in bounded form.

At minimum:

- the current-state delivery result artifact is readable
- the current-state delivery result has a bounded successful outcome: `DELIVERED`
- the current-state delivery result is not blocked, malformed, or non-delivered
- active application references in the result point to readable artifacts
- canonical core execution file matches across the effective authority, family, status, and governing artifacts
- the active application input set is internally coherent
- effective authority, family, status, and governing artifacts name the same current governing source run where those surfaces expose it
- effective authority, family, status, and governing artifacts name the same current governing ingress run where those surfaces expose it
- bounded non-claims remain false
- prior family remains preserved and readable where the current-state delivery result exposes that posture
- current-family and adopted-family distinction remains visible where adoption was used

Unreadable or mismatched inputs block the application. They must not be silently fused into a current-state application surface.

## 8. Application Checks

A bounded current-state application may be emitted only when all bounded checks pass.

Minimum required checks:

- current-state delivery result exists and is readable
- current-state delivery outcome is `DELIVERED`
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
- the application uses the delivered current-state result explicitly rather than inferring latest authority, family, status, or governing artifacts on its own
- the application does not silently use stale prior-family artifacts when current-state delivery names a different effective family

These checks are bounded and implementation-facing. They do not create a broad app, API, dashboard, reporting, or workflow engine.

## 9. Refusal / Block Conditions

Blocked current-state application must remain explicit. It is not the same thing as transition refusal, re-resolution blocking, adoption blocking, effective-family consumption blocking, current-work-input blocking, current-work-operation blocking, current-state readout blocking, current-state handoff blocking, current-state export blocking, or current-state delivery blocking. Those earlier surfaces answer whether earlier selection, work, readout, handoff, export, or delivery steps may proceed. Application blocking answers whether a downstream application step may proceed from a candidate current-state delivery result.

Minimum block conditions:

- no current-state delivery result is available
- current-state delivery result is unreadable
- current-state delivery result has an unrecognized, blocked, or non-delivered outcome
- effective application artifacts are unreadable
- canonical execution line mismatch
- effective application input set is not internally coherent
- effective application input set does not correspond to the current-state delivery result
- prior family preservation is not evident where required
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent fallback to stale prior-family artifacts attempted
- latest-file inference attempted without explicit current-state delivery support
- multiple current-state delivery results conflict without an explicit bounded selection surface

Blocked application should preserve enough detail to show which current-state delivery result was considered, which effective references failed, and which non-claims remained required.

## 10. Application Contract

A current-state application is any downstream bounded component, resolver, builder, validator, application-level consumer, or application surface that emits one explicit application result using a delivered current-state result as its active selector.

An application may rely on:

- the delivered current-state result as the explicit selector of active application inputs
- the effective execution-authority artifact as the active bounded authority artifact
- the effective run-family packet as the active bounded family packet
- the effective preserved-run status packet as the active bounded status packet
- the effective current-governing packet as the active bounded governing packet
- the effective source and ingress run paths where the delivery result exposes them
- the bounded delivery output emitted by the current-state delivery result
- the carried-forward non-claims that remain false
- the fact that preserved prior families remain preserved but are not silently substituted for the active application inputs

An application must not infer:

- continuity completion
- replay permission
- merge permission
- standing upgrade
- final governance or final system identity
- final currentness doctrine
- persistence or registry law
- automatic latest-emitted fallback without explicit current-state delivery support
- authority from stale prior-family artifacts when a different effective family has been selected

The application contract is intentionally narrow: use the delivered current-state result references as active inputs, preserve provenance, emit one bounded application result, and carry non-claims forward.

## 11. Application Result Artifact

A future implementation should emit one bounded current-state application result artifact.

At minimum, the artifact should preserve:

- application result id
- application result type
- application result version
- `generated_at`
- current-state delivery result artifact path used
- current-state delivery result id used
- effective authority artifact path consumed
- effective family packet path consumed
- effective preserved-run status packet path consumed
- effective current-governing packet path consumed
- effective source run path where used
- effective ingress run path where used
- outcome: `APPLIED` or `BLOCKED`
- block code and block reason if blocked
- application basis
- checks or bounded check summary
- carried-forward non-claims

For `APPLIED`, the result should preserve the active inputs consumed and the bounded application output or application reference. The output can be a minimal downstream application surface, such as a compact object containing the delivered result identity, effective input paths, current governing source and ingress run paths, bounded delivery summary, and any bounded application reference needed by a later downstream consumer.

For `BLOCKED`, the result should preserve the candidate current-state delivery identity if any, the block reason, and enough failed-check detail to keep refusal visible.

This section does not design the future implementation. It only states the minimum provenance, outcome, block, and non-claim visibility expected of the first bounded application.

## 12. What Remains Preserved

After lawful current-state application:

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
- current-state application artifacts remain additive
- source runs remain preserved
- ingress runs remain preserved
- source-to-ingress comparison artifacts remain preserved
- preserved runs remain visible

Current-state application must not imply hidden mutation. It carries a delivered current-state result forward; it does not rewrite the artifacts that made the delivery possible.

## 13. What This Spec Still Does Not Define

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
- downstream application semantics beyond the smallest bounded case
- multi-application orchestration beyond the smallest bounded case
- a generic app, API, dashboard, reporting, or workflow framework

## 14. What Should Not Be Added Next

The next step should not expand the repo into packet sprawl or premature application machinery.

Do not add:

- direct stale-artifact reads when a delivered current-state result exists
- replay-based application
- merge-based application
- broad app, API, dashboard, connector, reporting, or workflow engines
- a new packet that only restates current-state delivery selection without new behavioral pressure
- persistence or registry substitutes for application law
- hidden standing upgrade through presentation, export, delivery, application, publication, transfer, or display

The next legitimate implementation pressure is one bounded application resolver that consumes one delivered current-state result and emits one explicit application result or one explicit block.

## 15. Closing Boundary Statement

The repository now has current-state delivery.

This spec exists because the next forced pressure is the first real current-state application.

It defines the smallest bounded application model now supportable: read one delivered current-state result, verify the active references it names, carry forward the bounded delivery and provenance, perform one bounded application step, emit one explicit application result, and preserve all prior artifacts unchanged.

It does not claim final governance, final continuity completion, final currentness doctrine, final system identity, minimum lawful system completion, or system completion.
