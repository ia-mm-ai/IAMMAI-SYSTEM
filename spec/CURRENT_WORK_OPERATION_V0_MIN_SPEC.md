# Current Work Operation V0-Min Spec

## 1. Purpose

This file defines the first bounded current work-operation spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, governing re-resolution, successor-adoption, effective-family, effective-family-consumption, and current-work-input surfaces:

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
- `spec/EFFECTIVE_FAMILY_CONSUMPTION_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful downstream operation that consumes `current_work_input` as its active input surface.

`current_work_input` is now the bounded active input set for downstream work. It identifies the effective authority, family, preserved-run status, current-governing, source-run, and ingress-run references that a later bounded operation may use without scanning stale prior-family artifacts or inventing latest-file currentness.

The next forced pressure is the first real downstream work operation, not more selection, currentness, or governance packet packaging.

This spec does not implement that operation. It does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, or a broad workflow engine.

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
- promote current-work-input resolution into final system law
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded work-operation model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now resolve `current_work_input`.

That result is real. It preserves a bounded outcome, selected effective-family consumption provenance, effective work-input references, resolved work-input references, checks, a work-input summary, and carried-forward non-claims.

But downstream work can still fail in two ways if the next boundary is not stated:

- it can drift back to stale prior-family artifacts because those artifacts remain readable
- it can expand into vague generic workflow machinery that is larger than the current executable pressure supports

A bounded work-operation spec is therefore required before further downstream implementations are built. The operation boundary says: read `current_work_input`, consume the active references it names, run one bounded work step, emit an explicit work result, and preserve all prior artifacts unchanged.

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
- explicit non-claims around replay, merge, continuity completion, standing upgrade, minimum lawful system completion, final system identity, and final governance completion

These surfaces make active downstream input selection visible. They do not yet define the first bounded work operation that consumes that selection.

## 5. Current Work Operation Scope

This work-operation slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads one `current_work_input` resolution artifact and the active input references named by that artifact.

It governs one bounded downstream work step. The work step may inspect, derive, validate, or produce one additive result from the resolved active input set, but it must preserve the authority, family, status, governing, transition, re-resolution, adoption, effective-family, consumption, and current-work-input artifacts unchanged.

The operation is not a broad workflow system. It does not define orchestration, queues, registries, scheduling, persistence topology, cross-host continuity completion, replay, or merge.

Current work operation is a checked downstream action over already selected active inputs. It is not hidden update, host replay, continuity completion, or final currentness doctrine.

## 6. Work Input Set

A bounded current work operation needs the following input set:

- one current-work-input resolution artifact
- the effective execution-authority artifact referenced by that resolution
- the effective run-family packet referenced by that resolution
- the effective preserved-run status packet referenced by that resolution
- the effective current-governing packet referenced by that resolution

The active input references are the paths in the current-work-input resolution's `effective_work_inputs` and `resolved_work_input_references` sections:

- `effective_authority_artifact_path`
- `effective_family_packet_path`
- `effective_status_packet_path`
- `effective_current_governing_packet_path`
- `effective_source_run_path`
- `effective_ingress_run_path`

Prior current families may remain preserved and readable. They are not the active work inputs when a current-work-input resolution names a different effective family.

Blocked or stale current-work-input results do not drive work execution. A work operation must not bypass `current_work_input` and decide active inputs by scanning authority, family, status, governing, adoption, effective-family, or consumption roots on its own.

## 7. Input Correspondence Requirements

Before work may be considered, the selected inputs must correspond in bounded form.

At minimum:

- the current-work-input resolution artifact is readable
- the current-work-input resolution has a bounded successful outcome: `CURRENT_WORK_INPUT_RESOLVED`
- the current-work-input resolution is not blocked, malformed, or non-resolved
- effective work-input references in the resolution point to readable artifacts
- canonical core execution file matches across the effective authority, family, status, and governing artifacts
- the effective work-input set is internally coherent
- effective authority, family, status, and governing artifacts name the same current governing source run where those surfaces expose it
- effective authority, family, status, and governing artifacts name the same current governing ingress run where those surfaces expose it
- bounded non-claims remain false
- prior family remains preserved and readable where the current-work-input resolution exposes that posture
- current-family and adopted-family distinction remains visible where adoption was used

Unreadable or mismatched inputs block the work operation. They must not be silently fused into a downstream work state.

## 8. Work Checks

A bounded work operation may proceed only when all bounded checks pass.

Minimum required checks:

- current-work-input resolution exists and is readable
- current-work-input outcome is `CURRENT_WORK_INPUT_RESOLVED`
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
- the work operation uses `current_work_input` explicitly rather than inferring latest authority, family, status, or governing artifacts on its own
- the work operation does not silently use stale prior-family artifacts when `current_work_input` names a different effective family

These checks are bounded and implementation-facing. They do not create a broad workflow engine.

## 9. Refusal / Block Conditions

Blocked work-operation execution must remain explicit. It is not the same thing as transition refusal, re-resolution blocking, adoption blocking, effective-family consumption blocking, or current-work-input blocking. Those earlier surfaces answer whether earlier selection or projection steps may proceed. Work-operation blocking answers whether downstream work may proceed from a candidate current-work-input result.

Minimum block conditions:

- no current-work-input resolution is available
- current-work-input resolution is unreadable
- current-work-input resolution has an unrecognized, blocked, or non-resolved outcome
- effective work-input artifacts are unreadable
- canonical execution line mismatch
- effective work-input set is not internally coherent
- effective work-input set does not correspond to the current-work-input resolution
- prior family preservation is not evident where required
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent fallback to stale prior-family artifacts attempted
- latest-file inference attempted without explicit current-work-input support
- multiple current-work-input resolutions conflict without an explicit bounded selection surface

Blocked work-operation execution should preserve enough detail to show which current-work-input resolution was considered, which effective references failed, and which non-claims remained required.

## 10. Work Operation Contract

A current work operation is any downstream bounded component, resolver, builder, validator, or inspection surface that performs one explicit work step using `current_work_input` as its active input selector.

A work operation may rely on:

- the current-work-input resolution as the explicit selector of active work inputs
- the effective execution-authority artifact as the active bounded authority artifact
- the effective run-family packet as the active bounded family packet
- the effective preserved-run status packet as the active bounded status packet
- the effective current-governing packet as the active bounded governing packet
- the effective source and ingress run paths where the resolution exposes them
- the carried-forward non-claims that remain false
- the fact that preserved prior families remain preserved but are not silently substituted for the active work inputs

A work operation must not infer:

- continuity completion
- replay permission
- merge permission
- standing upgrade
- final governance or final system identity
- final currentness doctrine
- persistence or registry law
- automatic latest-emitted fallback without explicit current-work-input support
- authority from stale prior-family artifacts when a different effective family has been selected

The work contract is intentionally narrow: use the current-work-input references as active inputs, preserve provenance, run one bounded work step, and carry non-claims forward.

## 11. Work Result Artifact

A future implementation should emit one explicit work result artifact.

Minimum result surface:

- `work_result_id`
- `work_result_type`
- `work_result_version`
- `generated_at`
- resolver or implementation surface name
- current-work-input resolution artifact path used
- current-work-input resolution id used
- effective authority artifact path consumed
- effective family packet path consumed
- effective preserved-run status packet path consumed
- effective current-governing packet path consumed
- effective source run path where used
- effective ingress run path where used
- outcome: `COMPLETED` or `BLOCKED`
- block code and block reason if blocked
- work basis
- checks or bounded check summary
- carried-forward non-claims

For `COMPLETED`, the result should preserve the active inputs consumed and the bounded work output or output reference.

For `BLOCKED`, the result should preserve the candidate current-work-input identity if any, the block reason, and enough failed-check detail to keep refusal visible.

This section does not design the future implementation. It only states the minimum provenance, outcome, block, and non-claim visibility expected of the first bounded downstream work operation.

## 12. What Remains Preserved

After lawful work execution:

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
- source runs remain preserved
- ingress runs remain preserved
- source-to-ingress comparison artifacts remain preserved
- preserved runs remain visible

Work execution is not hidden mutation. It consumes the active input set for one bounded downstream operation while preserving the artifact chain that made the input selection lawful and inspectable.

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
- downstream operation semantics beyond the smallest bounded case
- multi-work-operation orchestration beyond the smallest bounded case
- final rule for many current-work-input resolutions in conflict
- a generic workflow, dependency-injection, scheduling, or registry framework

This spec defines only the first bounded work-operation model now supportable by the current executable stack.

## 14. What Should Not Be Added Next

The repo should not add:

- direct stale-artifact reads when a current-work-input resolution exists
- replay-based work execution
- merge-based work execution
- broad workflow engine
- final persistence or registry machinery as a substitute for work law
- a new packet that only restates current-work-input selection without new behavioral pressure
- automatic promotion by latest authority, latest family, latest status, latest governing packet, latest adoption, latest effective-family artifact, latest consumption artifact, or latest current-work-input artifact alone
- hidden mutation of prior current-family artifacts

Additional work should now either implement one bounded work operation or refine a forced edge case that blocks work execution. It should not widen into general workflow theory.

## 15. Closing Boundary Statement

The repository now has current authority, preserved-run family/status/governing surfaces, governing transition, governing re-resolution, successor-family adoption, effective-family resolution, effective-family consumption, and current-work-input resolution.

This spec exists because the next forced pressure is the first real downstream work operation.

It defines the smallest bounded model by which downstream work may consume `current_work_input` as the explicit selector of active inputs without mutating prior artifacts, replaying the host, merging preserved runs, completing continuity, or silently upgrading standing.

It does not claim final governance, final continuity completion, final system identity, or system completion.
