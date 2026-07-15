# Current State Readout V0-Min Spec

## 1. Purpose

This file defines the first bounded current-state readout spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, governing re-resolution, successor-adoption, effective-family, effective-family-consumption, current-work-input, and current-work-operation surfaces:

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
- `spec/EFFECTIVE_FAMILY_CONSUMPTION_V0_MIN_SPEC.md`
- `spec/CURRENT_WORK_OPERATION_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful downstream readout consumer that consumes a completed current-work-operation result and emits one bounded current-state readout.

A completed current-work-operation result is now the bounded active surface for the first real downstream readout consumer. It preserves the current-work-input provenance, the effective authority, family, status, governing, source-run, and ingress-run references, the bounded work output, checks, outcome, and carried-forward non-claims.

The next forced pressure is readout, not more governance, currentness, selection, or packet packaging.

This spec does not implement the readout. It does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, a dashboard, or a broad workflow engine.

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
- promote current-work-operation completion into final system law
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded current-state readout model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now emit a completed current-work-operation result.

That result is real. It preserves selected current-work-input provenance, effective input references, bounded checks, explicit `COMPLETED` or `BLOCKED` outcome, bounded work output, work summary, and carried-forward non-claims.

Without one bounded readout spec, the next consumer can still fail in three ways:

- it can drift back to stale prior-family artifacts because those artifacts remain readable
- it can expand into generic workflow, dashboard, or reporting machinery larger than the current executable pressure supports
- it can introduce broader ontology than the current body has lawfully made executable

A bounded current-state readout spec is therefore required before application-level readout implementations are built. The readout boundary says: read one completed current-work-operation result, consume only the active references it names, emit one bounded current-state readout, and preserve all prior artifacts unchanged.

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
- current-work-operation v2 resolver and current-work-operation result artifacts
- explicit bounded non-claims around replay, merge, continuity completion, standing upgrade, minimum lawful system completion, final system identity, and final governance completion

These surfaces make one bounded downstream operation visible. They do not yet define the first bounded readout that consumes the completed operation result.

## 5. Current-State Readout Scope

This current-state readout slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads one completed current-work-operation result and the active input references named by that result.

It governs one bounded current-state readout step. The readout may inspect and summarize the completed work result and its effective authority, family, preserved-run status, current-governing, source-run, and ingress-run references, but it must preserve all authority, family, status, governing, transition, re-resolution, adoption, effective-family, consumption, current-work-input, and current-work-operation artifacts unchanged.

The readout is not a broad reporting or dashboard system. It does not define orchestration, queues, registries, scheduling, persistence topology, cross-host continuity completion, replay, or merge.

Current-state readout is a checked downstream observation over already completed bounded work. It is not hidden update, host replay, continuity completion, final currentness doctrine, or final system identity law.

## 6. Readout Input Set

A bounded current-state readout needs the following input set:

- one completed current-work-operation result artifact
- the effective execution-authority artifact referenced by that result
- the effective run-family packet referenced by that result
- the effective preserved-run status packet referenced by that result
- the effective current-governing packet referenced by that result

The active readout references are the paths in the current-work-operation result's `effective_inputs` section and, where useful, its bounded `work_output` section:

- `effective_authority_artifact_path`
- `effective_family_packet_path`
- `effective_status_packet_path`
- `effective_current_governing_packet_path`
- `effective_source_run_path`
- `effective_ingress_run_path`
- `current_governing_source_run_path`
- `current_governing_ingress_run_path`

Prior current families may remain preserved and readable. They are not the active readout inputs when a completed current-work-operation result names a different effective family.

Blocked, stale, or non-completed current-work-operation results do not drive readout. A readout must not bypass the completed current-work-operation result and decide active readout inputs by scanning authority, family, status, governing, adoption, effective-family, consumption, or current-work-input roots on its own.

## 7. Input Correspondence Requirements

Before readout may be considered, the selected inputs must correspond in bounded form.

At minimum:

- the current-work-operation result artifact is readable
- the current-work-operation result has a bounded successful outcome: `COMPLETED`
- the current-work-operation result is not blocked, malformed, or non-completed
- active readout references in the result point to readable artifacts
- canonical core execution file matches across the effective authority, family, status, and governing artifacts
- the active readout input set is internally coherent
- effective authority, family, status, and governing artifacts name the same current governing source run where those surfaces expose it
- effective authority, family, status, and governing artifacts name the same current governing ingress run where those surfaces expose it
- bounded non-claims remain false
- prior family remains preserved and readable where the current-work-operation result exposes that posture
- current-family and adopted-family distinction remains visible where adoption was used

Unreadable or mismatched inputs block the readout. They must not be silently fused into a current-state summary.

## 8. Readout Checks

A bounded current-state readout may be emitted only when all bounded checks pass.

Minimum required checks:

- current-work-operation result exists and is readable
- current-work-operation outcome is `COMPLETED`
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
- the readout uses the completed current-work-operation result explicitly rather than inferring latest authority, family, status, or governing artifacts on its own
- the readout does not silently use stale prior-family artifacts when current-work-operation names a different effective family

These checks are bounded and implementation-facing. They do not create a broad dashboard, reporting system, or workflow engine.

## 9. Refusal / Block Conditions

Blocked current-state readout must remain explicit. It is not the same thing as transition refusal, re-resolution blocking, adoption blocking, effective-family consumption blocking, current-work-input blocking, or current-work-operation blocking. Those earlier surfaces answer whether earlier selection or work steps may proceed. Readout blocking answers whether a downstream readout may be emitted from a candidate current-work-operation result.

Minimum block conditions:

- no current-work-operation result is available
- current-work-operation result is unreadable
- current-work-operation result has an unrecognized, blocked, or non-completed outcome
- effective readout artifacts are unreadable
- canonical execution line mismatch
- effective readout input set is not internally coherent
- effective readout input set does not correspond to the current-work-operation result
- prior family preservation is not evident where required
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent fallback to stale prior-family artifacts attempted
- latest-file inference attempted without explicit current-work-operation support
- multiple current-work-operation results conflict without an explicit bounded selection surface

Blocked readout should preserve enough detail to show which current-work-operation result was considered, which effective references failed, and which non-claims remained required.

## 10. Readout Contract

A current-state readout is any downstream bounded component, resolver, builder, validator, or inspection surface that emits one explicit current-state summary using a completed current-work-operation result as its active selector.

A readout may rely on:

- the completed current-work-operation result as the explicit selector of active readout inputs
- the effective execution-authority artifact as the active bounded authority artifact
- the effective run-family packet as the active bounded family packet
- the effective preserved-run status packet as the active bounded status packet
- the effective current-governing packet as the active bounded governing packet
- the effective source and ingress run paths where the work-operation result exposes them
- the bounded work output emitted by the completed current-work-operation result
- the carried-forward non-claims that remain false
- the fact that preserved prior families remain preserved but are not silently substituted for the active readout inputs

A readout must not infer:

- continuity completion
- replay permission
- merge permission
- standing upgrade
- final governance or final system identity
- final currentness doctrine
- persistence or registry law
- automatic latest-emitted fallback without explicit current-work-operation support
- authority from stale prior-family artifacts when a different effective family has been selected

The readout contract is intentionally narrow: use the completed current-work-operation references as active inputs, preserve provenance, emit one bounded readout, and carry non-claims forward.

## 11. Readout Result Artifact

A future implementation should emit one explicit current-state readout artifact.

Minimum result surface:

- `readout_result_id`
- `readout_result_type`
- `readout_result_version`
- `generated_at`
- resolver or implementation surface name
- current-work-operation result artifact path used
- current-work-operation result id used
- effective authority artifact path consumed
- effective family packet path consumed
- effective preserved-run status packet path consumed
- effective current-governing packet path consumed
- effective source run path where used
- effective ingress run path where used
- outcome: `EMITTED` or `BLOCKED`
- block code and block reason if blocked
- readout basis
- checks or bounded check summary
- carried-forward non-claims

For `EMITTED`, the result should preserve the active inputs consumed and the bounded current-state readout or a readout reference.

For `BLOCKED`, the result should preserve the candidate current-work-operation identity if any, the block reason, and enough failed-check detail to keep refusal visible.

This section does not design the future implementation. It only states the minimum provenance, outcome, block, and non-claim visibility expected of the first bounded current-state readout.

## 12. What Remains Preserved

After lawful current-state readout:

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
- current-state readout artifacts remain additive
- source runs remain preserved
- ingress runs remain preserved
- source-to-ingress comparison artifacts remain preserved
- preserved runs remain visible

Readout is not hidden mutation. It observes and summarizes the active input set selected by completed bounded work while preserving the artifact chain that made that selection lawful and inspectable.

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
- downstream readout semantics beyond the smallest bounded case
- multi-readout orchestration beyond the smallest bounded case
- final rule for many current-work-operation results in conflict
- a generic reporting, dashboard, dependency-injection, scheduling, or workflow framework

This spec defines only the first bounded current-state readout model now supportable by the current executable stack.

## 14. What Should Not Be Added Next

The repo should not add:

- direct stale-artifact reads when a completed current-work-operation result exists
- replay-based readout
- merge-based readout
- broad dashboard or reporting engine
- final persistence or registry machinery as a substitute for readout law
- a new packet that only restates current-work-operation selection without new behavioral pressure
- automatic promotion by latest authority, latest family, latest status, latest governing packet, latest adoption, latest effective-family artifact, latest consumption artifact, latest current-work-input artifact, or latest current-work-operation artifact alone
- hidden mutation of prior current-family artifacts

Additional work should now either implement one bounded current-state readout or refine a forced edge case that blocks readout emission. It should not widen into general dashboard, workflow, or governance theory.

## 15. Closing Boundary Statement

The repository now has current authority, preserved-run family/status/governing surfaces, governing transition, governing re-resolution, successor-family adoption, effective-family resolution, effective-family consumption, current-work-input resolution, and current-work-operation completion.

This spec exists because the next forced pressure is the first real current-state readout.

It defines the smallest bounded model by which downstream readout may consume a completed current-work-operation result as the explicit selector of active inputs without mutating prior artifacts, replaying the host, merging preserved runs, completing continuity, or silently upgrading standing.

It does not claim final governance, final continuity completion, final system identity, or system completion.
