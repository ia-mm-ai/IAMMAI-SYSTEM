# Current State Handoff V0-Min Spec

## 1. Purpose

This file defines the first bounded current-state handoff spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, governing re-resolution, successor-adoption, effective-family, effective-family-consumption, current-work-input, current-work-operation, and current-state-readout surfaces:

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
- `spec/EFFECTIVE_FAMILY_CONSUMPTION_V0_MIN_SPEC.md`
- `spec/CURRENT_WORK_OPERATION_V0_MIN_SPEC.md`
- `spec/CURRENT_STATE_READOUT_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful downstream handoff surface that consumes an emitted current-state readout result and produces one bounded handoff surface for later downstream consumers.

An emitted current-state readout is now the bounded active surface for the first real downstream handoff. It preserves the current-work-operation provenance, the effective authority, family, status, governing, source-run, and ingress-run references, the bounded readout output, checks, outcome, and carried-forward non-claims.

The next forced pressure is handoff, not more governance, currentness, selection, or packet packaging.

This spec does not implement handoff. It does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, an API, a dashboard, or a broad workflow engine.

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
- promote current-state readout emission into final system law
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded current-state handoff model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now emit a bounded current-state readout.

That result is real. It preserves selected current-work-operation provenance, effective readout input references, bounded checks, explicit `EMITTED` or `BLOCKED` outcome, bounded readout output, readout summary, and carried-forward non-claims.

Without one bounded handoff spec, the next consumer can still fail in three ways:

- it can drift back to stale prior-family artifacts because those artifacts remain readable
- it can expand into generic dashboard, app, API, reporting, or workflow machinery larger than the current executable pressure supports
- it can introduce broader ontology than the current body has lawfully made executable

A bounded current-state handoff spec is therefore required before application-level handoff implementations are built. The handoff boundary says: read one emitted current-state readout result, consume only the active references it names, emit one bounded handoff result, and preserve all prior artifacts unchanged.

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
- explicit bounded non-claims around replay, merge, continuity completion, standing upgrade, minimum lawful system completion, final system identity, and final governance completion

These surfaces make one bounded downstream readout visible. They do not yet define the first bounded handoff that consumes the emitted readout result.

## 5. Current-State Handoff Scope

This current-state handoff slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads one emitted current-state readout result and the active input references named by that result.

It governs one bounded downstream handoff step. The handoff may carry forward the emitted readout, selected current-work-operation provenance, effective authority, family, preserved-run status, current-governing, source-run, and ingress-run references, but it must preserve all authority, family, status, governing, transition, re-resolution, adoption, effective-family, consumption, current-work-input, current-work-operation, and current-state readout artifacts unchanged.

The handoff is not a broad dashboard, API, connector, app, reporting, or workflow system. It does not define orchestration, queues, registries, scheduling, persistence topology, cross-host continuity completion, replay, or merge.

Current-state handoff is a checked downstream transfer surface over an already emitted bounded readout. It is not hidden update, host replay, continuity completion, final currentness doctrine, or final system identity law.

## 6. Handoff Input Set

A bounded current-state handoff needs the following input set:

- one emitted current-state readout result artifact
- the effective execution-authority artifact referenced by that result
- the effective run-family packet referenced by that result
- the effective preserved-run status packet referenced by that result
- the effective current-governing packet referenced by that result

The active handoff references are the paths in the current-state readout result's `effective_readout_inputs` section and, where useful, its bounded `readout_output` section:

- `effective_authority_artifact_path`
- `effective_family_packet_path`
- `effective_status_packet_path`
- `effective_current_governing_packet_path`
- `effective_source_run_path`
- `effective_ingress_run_path`
- `current_governing_source_run_path`
- `current_governing_ingress_run_path`

Prior current families may remain preserved and readable. They are not the active handoff inputs when an emitted current-state readout names a different effective family.

Blocked, stale, or non-emitted current-state readout results do not drive handoff. A handoff must not bypass the emitted current-state readout result and decide active handoff inputs by scanning authority, family, status, governing, adoption, effective-family, consumption, current-work-input, or current-work-operation roots on its own.

## 7. Input Correspondence Requirements

Before handoff may be considered, the selected inputs must correspond in bounded form.

At minimum:

- the current-state readout result artifact is readable
- the current-state readout result has a bounded successful outcome: `EMITTED`
- the current-state readout result is not blocked, malformed, or non-emitted
- active handoff references in the result point to readable artifacts
- canonical core execution file matches across the effective authority, family, status, and governing artifacts
- the active handoff input set is internally coherent
- effective authority, family, status, and governing artifacts name the same current governing source run where those surfaces expose it
- effective authority, family, status, and governing artifacts name the same current governing ingress run where those surfaces expose it
- bounded non-claims remain false
- prior family remains preserved and readable where the current-state readout result exposes that posture
- current-family and adopted-family distinction remains visible where adoption was used

Unreadable or mismatched inputs block the handoff. They must not be silently fused into a current-state handoff surface.

## 8. Handoff Checks

A bounded current-state handoff may be emitted only when all bounded checks pass.

Minimum required checks:

- current-state readout result exists and is readable
- current-state readout outcome is `EMITTED`
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
- the handoff uses the emitted current-state readout result explicitly rather than inferring latest authority, family, status, or governing artifacts on its own
- the handoff does not silently use stale prior-family artifacts when current-state readout names a different effective family

These checks are bounded and implementation-facing. They do not create a broad app, API, dashboard, reporting, or workflow engine.

## 9. Refusal / Block Conditions

Blocked current-state handoff must remain explicit. It is not the same thing as transition refusal, re-resolution blocking, adoption blocking, effective-family consumption blocking, current-work-input blocking, current-work-operation blocking, or current-state readout blocking. Those earlier surfaces answer whether earlier selection, work, or readout steps may proceed. Handoff blocking answers whether a downstream handoff may be emitted from a candidate current-state readout result.

Minimum block conditions:

- no current-state readout result is available
- current-state readout result is unreadable
- current-state readout result has an unrecognized, blocked, or non-emitted outcome
- effective handoff artifacts are unreadable
- canonical execution line mismatch
- effective handoff input set is not internally coherent
- effective handoff input set does not correspond to the current-state readout result
- prior family preservation is not evident where required
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent fallback to stale prior-family artifacts attempted
- latest-file inference attempted without explicit current-state readout support
- multiple current-state readout results conflict without an explicit bounded selection surface

Blocked handoff should preserve enough detail to show which current-state readout result was considered, which effective references failed, and which non-claims remained required.

## 10. Handoff Contract

A current-state handoff is any downstream bounded component, resolver, builder, validator, or transfer surface that emits one explicit handoff result using an emitted current-state readout result as its active selector.

A handoff may rely on:

- the emitted current-state readout result as the explicit selector of active handoff inputs
- the effective execution-authority artifact as the active bounded authority artifact
- the effective run-family packet as the active bounded family packet
- the effective preserved-run status packet as the active bounded status packet
- the effective current-governing packet as the active bounded governing packet
- the effective source and ingress run paths where the readout result exposes them
- the bounded readout output emitted by the current-state readout result
- the carried-forward non-claims that remain false
- the fact that preserved prior families remain preserved but are not silently substituted for the active handoff inputs

A handoff must not infer:

- continuity completion
- replay permission
- merge permission
- standing upgrade
- final governance or final system identity
- final currentness doctrine
- persistence or registry law
- automatic latest-emitted fallback without explicit current-state readout support
- authority from stale prior-family artifacts when a different effective family has been selected

## 11. Handoff Result Artifact

A future implementation should emit one bounded current-state handoff result artifact.

At minimum, the artifact should preserve:

- handoff result id
- handoff result type
- handoff result version
- `generated_at`
- current-state readout result artifact path used
- current-state readout result id used
- effective authority artifact path consumed
- effective family packet path consumed
- effective preserved-run status packet path consumed
- effective current-governing packet path consumed
- effective source run path where used
- effective ingress run path where used
- outcome: `HANDED_OFF` or `BLOCKED`
- block code and block reason if blocked
- handoff basis
- checks or bounded check summary
- carried-forward non-claims

For `HANDED_OFF`, the result should preserve the active inputs consumed and the bounded handoff output or handoff reference. The output can be a minimal downstream handoff surface, such as a compact object containing the emitted readout identity, effective input paths, current governing source and ingress run paths, and bounded readout summary.

For `BLOCKED`, the result should preserve the candidate current-state readout identity if any, the block reason, and enough failed-check detail to keep refusal visible.

This section does not design the future implementation. It only states the minimum provenance, outcome, block, and non-claim visibility expected of the first bounded handoff.

## 12. What Remains Preserved

After lawful current-state handoff:

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
- current-state handoff artifacts remain additive
- source runs remain preserved
- ingress runs remain preserved
- source-to-ingress comparison artifacts remain preserved
- preserved runs remain visible

Current-state handoff must not imply hidden mutation. It carries an emitted readout forward; it does not rewrite the artifacts that made the readout possible.

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
- downstream handoff semantics beyond the smallest bounded case
- multi-handoff orchestration beyond the smallest bounded case
- a generic app, API, dashboard, reporting, or workflow framework

## 14. What Should Not Be Added Next

The next step should not expand the repo into packet sprawl or premature application machinery.

Do not add:

- direct stale-artifact reads when an emitted current-state readout exists
- replay-based handoff
- merge-based handoff
- broad dashboard, app, API, connector, reporting, or workflow engines
- a new packet that only restates current-state readout selection without new behavioral pressure
- persistence or registry substitutes for handoff law
- hidden standing upgrade through presentation, export, publication, or transfer

The next legitimate implementation pressure is one bounded handoff resolver that consumes one emitted current-state readout and emits one explicit handoff result or one explicit block.

## 15. Closing Boundary Statement

The repository now has current-state readout emission.

This spec exists because the next forced pressure is the first real current-state handoff.

It defines the smallest bounded handoff model now supportable: read one emitted current-state readout result, verify the active references it names, carry forward the bounded readout and provenance, emit one explicit handoff result, and preserve all prior artifacts unchanged.

It does not claim final governance, final continuity completion, final currentness doctrine, final system identity, minimum lawful system completion, or system completion.
