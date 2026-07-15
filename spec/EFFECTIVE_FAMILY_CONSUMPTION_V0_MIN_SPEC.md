# Effective Family Consumption V0-Min Spec

## 1. Purpose

This file defines the first bounded effective-family consumption spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, governing re-resolution, successor-adoption, and effective-family surfaces:

- `src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py`
- `src/build_integrity_host_v0_min_coexistence_run_family_packet.py`
- `src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py`
- `src/build_current_integrity_host_v0_min_coexistence_governing_packet.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_transition.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_reresolution.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2.py`
- `src/resolve_current_integrity_host_v0_min_coexistence_effective_family.py`
- `spec/GOVERNING_TRANSITION_V0_MIN_SPEC.md`
- `spec/GOVERNING_RERESOLUTION_V0_MIN_SPEC.md`
- `spec/GOVERNING_SUCCESSOR_ADOPTION_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful model for how downstream bounded work may consume an effective-family resolution artifact.

An effective-family resolution identifies which authority, family, preserved-run status, and current-governing artifacts are effective for subsequent bounded work. It does not by itself define every downstream consumer, complete continuity, create replay or merge permission, settle final system identity, or define final governance.

The next forced pressure is consumption, not more packet packaging. Once an effective family exists, downstream work needs one bounded way to use it without drifting back to stale prior-family artifacts or inventing currentness by latest-file discovery.

This spec does not implement a consumer. It does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, or a broad governance engine.

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
- promote effective-family resolution into final system law
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded consumption model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now emit an effective-family resolution artifact.

That artifact is real. It preserves a bounded outcome, a canonical execution line, prior current-family references, any selected adoption result, effective family references, checks, non-effective preserved-family visibility, and carried-forward non-claims.

But downstream consumers can still create drift if they read authority, family, status, or governing artifacts ad hoc. A consumer that selects latest local artifacts on its own, or falls back to prior current-family artifacts after adoption, can silently bypass the effective-family selection that now exists.

A bounded consumption spec is therefore required before further downstream mechanisms are built. Consumption is the step that says: when current family references are needed, read the effective-family resolution first and use the family it explicitly names, subject to bounded correspondence checks.

## 4. What Now Stands

The current body materially has:

- canonical core execution line: `src/integrity_host_v0_min_coexistence_v2.py`
- current execution-authority resolution
- preserved-run family packet
- preserved-run status packet
- current-governing packet
- governing-transition spec, resolver, and result artifacts
- governing re-resolution spec, resolver, result artifacts, and successor family emission
- governing successor-adoption spec, v2 resolver, and adoption result artifacts
- effective-family resolver and effective-family resolution artifacts
- explicit non-claims around replay, merge, continuity completion, standing upgrade, final system identity, final governing scope, final transition law, final re-resolution law, final successor-adoption law, and final effective-family completion

These surfaces make effective current-family selection visible. They do not yet define how every later bounded consumer must use that selection.

## 5. Effective-Family Consumption Scope

This consumption slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads one effective-family resolution artifact and the family artifacts that resolution designates as effective.

It governs downstream bounded work that needs current family references, including any later bounded resolver or inspection surface that must know which authority, family, status, and governing artifacts are active inputs.

Consumption is additive. It does not mutate prior artifacts. It does not replay source actions into a live host. It does not merge preserved runs into a synthetic host state. It does not define final governance of all future consumers. It does not define cross-host continuity completion. It does not define final persistence, registry, replay, or merge law.

Effective-family consumption is a checked input-selection posture. It is not hidden update, host execution, continuity completion, or final currentness doctrine.

## 6. Consumption Input Set

A bounded downstream consumer needs the following input set:

- one effective-family resolution artifact
- the effective execution-authority artifact referenced by that resolution
- the effective run-family packet referenced by that resolution
- the effective preserved-run status packet referenced by that resolution
- the effective current-governing packet referenced by that resolution

The active input references are the paths in the effective-family resolution's `effective_family` section:

- `effective_authority_artifact_path`
- `effective_family_packet_path`
- `effective_status_packet_path`
- `effective_current_governing_packet_path`

Where available, the consumer may also use:

- `effective_source_run_path`
- `effective_ingress_run_path`
- the effective-family resolution id
- the selected adoption-result id and path
- the resolution basis
- carried-forward non-claims

Prior current-family artifacts may remain preserved and readable. They are not the active current inputs when an effective-family resolution names a different effective family.

Blocked or stale adoption artifacts do not drive consumption. A consumer must not bypass the effective-family resolution and decide active family by scanning adoption, re-resolution, transition, or current-family roots on its own.

## 7. Input Correspondence Requirements

Before consumption may be considered, the selected inputs must correspond in bounded form.

At minimum:

- the effective-family resolution artifact is readable
- the effective-family resolution has a bounded effective outcome: `CURRENT_FAMILY_EFFECTIVE` or `ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE`
- the effective-family resolution is not a blocked, malformed, or non-effective surface
- effective artifact references in the resolution point to readable artifacts
- canonical core execution file matches across the effective authority, family, status, and governing artifacts
- effective family artifacts correspond to one internally coherent selected authority/governing run
- effective family preserves bounded non-claims as false
- prior family references remain preserved and readable where the effective-family resolution exposes them
- current-family and adopted-family distinction remains visible where adoption was used

Unreadable or mismatched inputs block consumption. They must not be silently fused into a downstream current-family view.

## 8. Consumption Checks

A downstream consumer may lawfully consume the effective family only when all bounded checks pass.

Minimum required checks:

- effective-family resolution exists and is readable
- effective-family outcome is one of the bounded effective postures currently used by the implementation: `CURRENT_FAMILY_EFFECTIVE` or `ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE`
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
- prior family remains preserved after effective-family selection
- downstream consumer references the effective family explicitly rather than inferring latest authority, latest family, latest status, or latest governing artifacts on its own
- downstream consumer does not silently use stale prior-family artifacts when the effective-family resolution names a different effective family

These checks are bounded and implementation-facing. They do not create a broad governance engine.

## 9. Refusal / Block Conditions

Blocked consumption must remain explicit. It is not the same thing as transition refusal, re-resolution blocking, or adoption blocking. Transition refusal answers whether a proposed governing transition was accepted. Re-resolution blocking answers whether successor projection could be emitted. Adoption blocking answers whether a successor family could become adopted current family. Consumption blocking answers whether downstream work may use an effective-family resolution as its active input selector.

Minimum block conditions:

- no effective-family resolution is available
- effective-family resolution is unreadable
- effective-family resolution has an unrecognized, blocked, or non-effective outcome
- effective family artifacts are unreadable
- canonical execution line mismatch
- effective family is not internally coherent
- effective family does not correspond to the selected effective-family resolution
- prior family preservation is not evident where required by the effective-family resolution
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent fallback to stale prior-family artifacts attempted
- latest-file inference attempted without an explicit effective-family resolution
- multiple effective-family resolutions conflict without an explicit bounded selection surface

Blocked consumption should preserve enough detail to show which effective-family resolution was considered, which references failed, and which non-claims remained required.

## 10. Effective Consumer Contract

An effective-family consumer is any downstream bounded component, resolver, builder, validator, or inspection surface that needs the current family for subsequent bounded work.

A consumer may rely on:

- the effective-family resolution as the explicit selector of current family inputs
- the effective execution-authority artifact as the current bounded authority artifact
- the effective run-family packet as the current bounded family packet
- the effective preserved-run status packet as the current bounded status packet
- the effective current-governing packet as the current bounded governing packet
- the effective source and ingress run paths where the resolution exposes them
- the carried-forward non-claims that remain false
- the fact that preserved prior families remain preserved but are not silently substituted for the active current family

A consumer must not infer:

- continuity completion
- replay permission
- merge permission
- standing upgrade
- final governance or final system identity
- final currentness doctrine
- persistence or registry law
- automatic latest-emitted fallback without explicit effective-family resolution support
- authority from stale prior-family artifacts when an adopted successor family has become effective

The consumer contract is intentionally narrow: use the effective-family references as active inputs, preserve provenance, and carry non-claims forward.

## 11. Downstream Result Expectation

Any future downstream consumer should preserve, in its own result surface:

- the effective-family resolution id it used
- the effective-family resolution artifact path it used
- the effective authority artifact path it consumed
- the effective family packet path it consumed
- the effective preserved-run status packet path it consumed
- the effective current-governing packet path it consumed
- the effective source and ingress run paths where used
- carried-forward non-claims
- explicit refusal or block detail if the effective family could not be lawfully consumed

This section does not design the future consumer implementation. It only states the minimum provenance and non-claim visibility expected of later bounded work.

## 12. What Remains Preserved

After lawful effective-family consumption:

- prior execution-authority artifacts remain preserved
- prior run-family packets remain preserved
- prior preserved-run status packets remain preserved
- prior current-governing packets remain preserved
- governing-transition result artifacts remain preserved
- governing re-resolution result artifacts remain preserved
- successor-adoption result artifacts remain preserved
- effective-family resolution artifacts remain preserved
- source runs remain preserved
- ingress runs remain preserved
- source-to-ingress comparison artifacts remain preserved
- preserved runs remain visible

Consumption is not mutation. It selects active inputs for downstream bounded work while preserving the artifact chain that made the selection lawful and inspectable.

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
- downstream consumer semantics beyond the smallest bounded case
- multi-effective-family arbitration beyond the smallest bounded case
- final rule for many effective-family resolutions in conflict
- a generic dependency-injection, registry, or discovery framework

This spec defines only the first bounded consumption model now supportable by the current executable stack.

## 14. What Should Not Be Added Next

The repo should not add:

- direct stale-artifact reads when an effective-family resolution exists
- replay-based consumption
- merge-based consumption
- broad governance engine
- final persistence or registry machinery as a substitute for consumption law
- a new packet that only restates effective-family selection without new behavioral pressure
- automatic promotion by latest authority, latest family, latest status, latest governing packet, latest adoption, or latest effective-family artifact alone
- hidden mutation of prior current-family artifacts

Additional work should now either implement a bounded consumer contract or refine a forced edge case that blocks consumption. It should not widen into general governance theory.

## 15. Closing Boundary Statement

The repository now has current authority, preserved-run family/status/governing surfaces, governing transition, governing re-resolution, successor-family adoption, and effective-family resolution.

This spec exists because the next forced pressure is downstream consumption.

It defines the smallest bounded model by which downstream work may consume an effective-family resolution as the explicit selector of active current-family inputs without mutating prior artifacts, replaying the host, merging preserved runs, completing continuity, or silently upgrading standing.

It does not claim final governance, final continuity completion, final system identity, or system completion.
