# Governing Re-Resolution V0-Min Spec

## 1. Purpose

This file defines the first bounded governing re-resolution spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, and governing-transition surfaces:

- `src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py`
- `src/build_integrity_host_v0_min_coexistence_run_family_packet.py`
- `src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py`
- `src/build_current_integrity_host_v0_min_coexistence_governing_packet.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_transition.py`
- `spec/CURRENT_EXECUTABLE_LINE_AND_FORCED_SYSTEM_PRESSURES.md`
- `spec/CURRENT_GOVERNING_TRANSITION_BOUNDARY.md`
- `spec/GOVERNING_TRANSITION_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful mechanism by which accepted governing-transition result artifacts may be taken into account to compute a successor governing projection.

Accepted transition result artifacts are preserved typed result surfaces. They are not self-executing governing state. An accepted transition result records that one proposed governing transition passed bounded checks. It does not, by itself, rewrite the current execution-authority resolution, run-family packet, preserved-run status packet, or current-governing packet.

The next forced pressure is downstream re-resolution, not more packet packaging. The repository now needs one bounded answer for how accepted transition results may inform successor governing surfaces without mutating prior artifacts or collapsing proposal/result into governing state.

This spec does not define final governance, final currentness doctrine, replay or merge law, continuity completion, final system identity, persistence architecture, registry doctrine, or a broad governance engine.

## 2. Status And Rank

This spec is additive and repo-local.

It ranks below the constitutional and reference authority surfaces under `reference/IAMMAI/`, including the constitutional protocol, implementation overviews, runtime contract surfaces, and architecture surfaces.

It also ranks below current executable source, tests, and generated artifacts where those surfaces already stand as concrete behavior.

This spec does not:

- define final governance
- complete continuity
- replace current executable source files
- replace current test surfaces
- replace emitted artifacts
- promote accepted transition results into self-executing governing state
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded re-resolution model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now produce governing-transition result artifacts.

Those result artifacts are real. They preserve a proposal, current governing identity before transition, candidate successor identity, accepted or refused outcome, checks, refusal detail where applicable, and carried-forward non-claims.

But a result artifact remains a preserved typed result. If an accepted result artifact itself became current governing state, the repository would collapse proposal/result into governing state. That would bypass the authority, family, status, and governing packet surfaces that exist specifically to preserve currentness and role distinction.

A separate downstream re-resolution mechanism is therefore required. Re-resolution is the bounded step that reads current artifacts plus accepted transition result artifacts and emits successor governing projection artifacts without mutating the prior artifacts.

## 4. What Now Stands

The current body materially has:

- canonical core execution line: `src/integrity_host_v0_min_coexistence_v2.py`
- current execution-authority resolution
- preserved-run family packet
- preserved-run status packet
- current-governing packet
- governing-transition boundary and spec
- governing-transition resolver and result artifacts
- explicit non-claims around replay, merge, continuity completion, standing upgrade, final system identity, final governing scope, and final governing-transition law

These surfaces make governing transition result preservation possible. They do not yet define how accepted transition results are taken into account to emit successor governing surfaces.

## 5. Governing Re-Resolution Scope

This re-resolution slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads preserved authority, run-family, preserved-run-status, current-governing, and governing-transition result artifacts. It computes a successor governing projection.

Re-resolution is additive. It does not mutate prior artifacts. It does not replay source actions into a live host. It does not merge preserved runs into a synthetic host state. It does not define final governance of all future run families. It does not define cross-host continuity completion. It does not define final persistence, registry, replay, or merge law.

A successor governing projection is a new artifact family derived from current artifacts plus accepted transition result artifacts. It is not a hidden update to the old artifact family.

## 6. Re-Resolution Input Set

A future implementation needs the following bounded input set:

- current execution-authority resolution artifact
- current run-family packet
- current preserved-run status packet
- current governing packet
- one or more governing-transition result artifacts

For governing-transition result artifacts:

- only `ACCEPTED` results may participate in re-resolution
- `REFUSED` results remain preserved and inspectable, but they do not drive successor governing state
- result identity must remain visible
- proposal identity must remain visible
- current-governing-before identity must remain visible
- candidate-successor identity must remain visible
- carried-forward non-claims must remain visible

In the first bounded implementation, re-resolution should proceed only when the accepted result input is unambiguous. If multiple accepted transition results conflict or cannot be ordered by an explicit bounded selection surface, re-resolution must block rather than invent arbitration.

## 7. Input Correspondence Requirements

Before re-resolution may be considered, the selected inputs must correspond in bounded form.

At minimum:

- canonical core execution file matches across the current authority, family, status, and governing artifacts
- accepted transition result corresponds to the same canonical core execution line
- accepted transition result names the same current governing run as the current-governing packet in `current_governing_before`
- accepted transition result names the same current governing ingress run as the current-governing packet in `current_governing_before`
- accepted transition result names the same current governing comparison artifact as the current-governing packet in `current_governing_before`
- accepted transition result names a candidate successor visible in the preserved-run family
- accepted transition result names a candidate successor visible in the preserved-run status packet
- accepted transition result names a candidate successor that was eligible non-authority when the transition was accepted
- prior current governing surfaces remain readable
- preserved-run family remains readable
- preserved-run status remains readable
- current-governing packet remains readable

Unreadable or mismatched inputs block re-resolution. They must not be silently fused into a successor projection.

## 8. Re-Resolution Checks

A future implementation must emit successor governing surfaces only when all bounded re-resolution checks pass.

Minimum required checks:

- input artifact correspondence holds
- at least one accepted transition result exists and is readable
- selected transition result has `outcome == ACCEPTED`
- selected accepted result preserves carried-forward non-claims:
  - `replayed_into_live_host = false`
  - `merged_into_local_state = false`
  - `continuity_completed = false`
  - `standing_upgraded = false`
- selected accepted result preserves final-system and final-governance non-claims as false where those fields exist
- prior governing run remains preserved
- successor governing run named in the accepted result is explicit and readable
- successor governing run remains visible in the preserved-run family
- successor governing run remains visible in the preserved-run status packet
- preserved-run multiplicity remains visible
- no preserved run is silently erased
- no prior authority, family, status, or governing artifact is silently mutated
- re-resolution result is explicit, not inferred merely from the existence of an accepted transition artifact somewhere
- re-resolution is not inferred from latest-emitted or latest-eligible ordering alone

These checks are bounded and implementation-facing. They do not create a broad governance engine.

## 9. Refusal / Block Conditions

Blocked re-resolution must remain explicit. It is not the same thing as transition refusal. Transition refusal answers whether a proposed transition was accepted or refused. Re-resolution blocking answers whether preserved transition results can be lawfully projected into successor governing surfaces.

Minimum block conditions:

- no accepted transition result is available
- only refused transition results are available
- accepted transition result is unreadable
- accepted transition result does not correspond to the current governing state
- accepted transition result does not name the current governing packet's current run in `current_governing_before`
- accepted transition result names a successor not visible in the preserved-run family
- accepted transition result names a successor not visible in the preserved-run status packet
- canonical execution line mismatch
- prior governing artifact unreadable
- authority artifact unreadable
- run-family packet unreadable
- preserved-run status packet unreadable
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade attempted
- silent mutation of prior artifacts attempted
- multiple accepted transition results conflict without an explicit bounded arbitration surface

Blocked re-resolution must preserve enough detail to show why no successor projection was emitted.

## 10. Successor Projection

An accepted re-resolution means only the following bounded projection:

- prior authority artifact remains preserved unchanged
- prior run-family packet remains preserved unchanged
- prior preserved-run status packet remains preserved unchanged
- prior current-governing packet remains preserved unchanged
- accepted transition result artifact remains preserved unchanged
- successor authority artifact may be emitted
- successor run-family packet may be emitted
- successor preserved-run status packet may be emitted
- successor current-governing packet may be emitted
- prior governing run becomes preserved non-authority in the successor projection
- new governing run becomes current governing in the successor projection
- preserved eligible non-authority runs remain visible
- preserved ineligible runs remain visible
- no preserved run is erased
- no continuity completion is claimed
- no standing upgrade is claimed
- no replay or merge is performed

The successor projection does not say the old artifacts were wrong. It says a later bounded projection has been emitted from current artifacts plus an accepted transition result.

## 11. Successor Artifact Family

A future implementation needs one bounded successor artifact family.

At minimum, it should emit:

- successor execution-authority resolution artifact
- successor run-family packet
- successor preserved-run status packet
- successor current-governing packet

These are successor artifacts. They do not overwrite prior artifacts. They are derived from the current artifact family plus the selected accepted transition result artifact.

The successor family should preserve, at minimum:

- the canonical core execution file
- the prior authority/family/status/governing artifact references
- the accepted transition result artifact reference
- the prior governing run identity
- the new governing run identity
- preserved-run roles after projection
- non-claims carried forward as false
- explicit statement that replay, merge, continuity completion, and standing upgrade did not occur

## 12. What Remains Preserved

After re-resolution:

- prior authority artifact remains preserved
- prior run-family packet remains preserved
- prior preserved-run status packet remains preserved
- prior current-governing packet remains preserved
- accepted transition result artifact remains preserved
- refused transition result artifacts remain preserved where present
- preserved source runs remain visible
- preserved ingress runs remain visible
- preserved source-to-ingress comparison artifacts remain visible
- prior current governing run remains visible as preserved non-authority in the successor projection
- new current governing run remains traceable to the accepted transition result

Re-resolution must not imply hidden mutation. It must not replace the prior governing surface in place. It must not erase the fact that an earlier governing projection stood.

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
- multi-transition arbitration beyond the smallest bounded case
- final rule for many accepted transition results in conflict
- cross-host or cross-carrier governing continuity
- final lifecycle for successor projection chains

This spec defines only the first bounded re-resolution model now supportable by the current executable stack.

## 14. What Should Not Be Added Next

The repo should not add:

- logic that treats accepted transition results as self-executing governing state
- replay-based re-resolution
- merge-based re-resolution
- broad governance engine
- final persistence or registry machinery as a substitute for re-resolution law
- new packets that only restate successor statuses without explicit re-resolution logic
- automatic promotion by latest-emitted or latest-eligible ordering
- hidden mutation of prior currentness artifacts

Additional work should now either implement this bounded re-resolution mechanism or refine a forced edge case that blocks implementation. It should not widen into general governance theory.

## 15. Closing Boundary Statement

The repository now has current authority, preserved-run statuses, current governing scope, and governing-transition result artifacts.

This spec exists because the next forced pressure is downstream re-resolution.

It defines the smallest bounded model by which accepted transition result artifacts may inform successor governing projection artifacts without mutating prior artifacts, replaying the host, merging preserved runs, completing continuity, or silently upgrading standing.

It does not claim final governance, final continuity completion, final system identity, or system completion.
