# Governing Successor Adoption V0-Min Spec

## 1. Purpose

This file defines the first bounded successor-family adoption spec for the v0-min coexistence execution line.

It derives from the current authority, run-family, preserved-run-status, current-governing, governing-transition, and governing re-resolution surfaces:

- `src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py`
- `src/build_integrity_host_v0_min_coexistence_run_family_packet.py`
- `src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py`
- `src/build_current_integrity_host_v0_min_coexistence_governing_packet.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_transition.py`
- `src/resolve_integrity_host_v0_min_coexistence_governing_reresolution.py`
- `spec/CURRENT_EXECUTABLE_LINE_AND_FORCED_SYSTEM_PRESSURES.md`
- `spec/CURRENT_GOVERNING_TRANSITION_BOUNDARY.md`
- `spec/GOVERNING_TRANSITION_V0_MIN_SPEC.md`
- `spec/GOVERNING_RERESOLUTION_V0_MIN_SPEC.md`

Its purpose is to define, in code-ready architectural form, the smallest lawful mechanism by which a coherent successor governing family emitted by governing re-resolution may be adopted as the new current governing family for subsequent bounded work.

A coherent successor family is a preserved successor projection. It is real, readable, and produced by explicit re-resolution checks. It is not yet self-executing current family state. Successor-family emission does not by itself rewrite the current execution-authority resolution, run-family packet, preserved-run status packet, or current-governing packet.

The next forced pressure is successor-family adoption, not more packet packaging. The repository now needs one bounded answer for how a successor projection may become the governing family used by later work without hidden mutation.

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
- promote successor-family emission into self-executing currentness
- define final persistence or registry architecture
- define a minimum lawful system

Its scope is one bounded adoption model for the present canonical execution line only.

## 3. Why This Spec Is Needed Now

The repository can now emit a coherent successor governing family by re-resolution.

That successor family is real. It can include a successor execution-authority resolution artifact, successor run-family packet, successor preserved-run status packet, and successor current-governing packet. Those artifacts make a new governing projection inspectable without mutating the prior current family.

But the successor family remains a preserved successor artifact family. If successor-family emission itself became current family state, re-resolution would collapse into silent currentness mutation. That would bypass the explicit boundary that re-resolution was created to preserve: prior artifacts remain preserved, and later currentness requires an explicit downstream step.

A separate bounded adoption mechanism is therefore required. Adoption is the step that asks whether the successor family may become the current family for subsequent work while keeping the prior family preserved and readable.

## 4. What Now Stands

The current body materially has:

- canonical core execution line: `src/integrity_host_v0_min_coexistence_v2.py`
- current execution-authority resolution
- preserved-run family packet
- preserved-run status packet
- current-governing packet
- governing-transition boundary and spec
- governing-transition resolver and result artifacts
- governing re-resolution spec
- governing re-resolution result artifacts and successor family emission
- explicit non-claims around replay, merge, continuity completion, standing upgrade, final system identity, final governing scope, final governing-transition law, and final re-resolution completion

These surfaces make successor governing projection possible. They do not yet define how a successor projection becomes the current family used by later bounded work.

## 5. Successor-Family Adoption Scope

This adoption slice applies only to the current canonical core execution line:

- `src/integrity_host_v0_min_coexistence_v2.py`

It reads the current authority, run-family, preserved-run status, and current-governing artifacts plus one coherent successor family emitted by governing re-resolution.

It computes whether that successor family may be adopted as the new current governing family for subsequent bounded work.

Adoption is additive. It does not mutate prior artifacts. It does not replay source actions into a live host. It does not merge preserved runs into a synthetic host state. It does not define final governance of all future family chains. It does not define cross-host continuity completion. It does not define final persistence, registry, replay, or merge law.

Adoption is a current-family selection step over already emitted artifact families. It is not hidden update, host execution, or continuity completion.

## 6. Adoption Input Set

A future implementation needs the following bounded input set:

- current execution-authority resolution artifact
- current run-family packet
- current preserved-run status packet
- current-governing packet
- one governing re-resolution result artifact
- successor execution-authority resolution artifact emitted by that re-resolution
- successor run-family packet emitted by that re-resolution
- successor preserved-run status packet emitted by that re-resolution
- successor current-governing packet emitted by that re-resolution

For the governing re-resolution result:

- only `SUCCESSOR_PROJECTION_EMITTED` results may participate in adoption
- `BLOCKED` re-resolution results remain preserved and inspectable, but they do not drive adoption
- result identity must remain visible
- re-resolution input references must remain visible
- successor artifact paths must remain visible
- successor projection summary must remain visible
- carried-forward non-claims must remain visible

The adoption input is the re-resolution result plus the exact successor artifacts named by that result. A future adoption implementation must not infer a successor family from similarly named files or from lexical latest ordering alone.

## 7. Input Correspondence Requirements

Before adoption may be considered, the selected inputs must correspond in bounded form.

At minimum:

- canonical core execution file matches across current and successor artifact families
- successor family corresponds to the selected re-resolution result
- re-resolution result has `outcome == SUCCESSOR_PROJECTION_EMITTED`
- re-resolution result names the same prior governing family as the current artifacts
- successor authority artifact path matches the re-resolution result's successor authority path
- successor family packet path matches the re-resolution result's successor family path
- successor preserved-run status packet path matches the re-resolution result's successor status path
- successor current-governing packet path matches the re-resolution result's successor governing path
- successor family is internally coherent
- prior current family remains readable
- successor family remains readable
- successor family preserves bounded non-claims as false
- prior family remains preserved and unchanged

Unreadable or mismatched inputs block adoption. They must not be silently fused into a current family.

## 8. Adoption Checks

A future implementation may accept successor-family adoption only when all bounded adoption checks pass.

Minimum required checks:

- input artifact correspondence holds
- selected re-resolution result exists and is readable
- selected re-resolution result has `outcome == SUCCESSOR_PROJECTION_EMITTED`
- successor execution-authority resolution artifact is readable and coherent
- successor run-family packet is readable and coherent
- successor preserved-run status packet is readable and coherent
- successor current-governing packet is readable and coherent
- successor family canonical core execution file matches the current family canonical core execution file
- successor family preserves the prior governing run as preserved non-authority
- successor family names exactly one explicit new current governing run
- successor governing run matches the successor authority, family, and status artifacts
- preserved-run multiplicity remains visible
- successor family preserves bounded non-claims:
  - `replayed_into_live_host = false`
  - `merged_into_local_state = false`
  - `continuity_completed = false`
  - `standing_upgraded = false`
- prior family remains preserved after adoption
- adoption result is explicit, not inferred merely from the existence of a successor family
- adoption is not inferred from latest-emitted, latest-eligible, or latest-successor ordering alone

These checks are bounded and implementation-facing. They do not create a broad governance engine.

## 9. Refusal / Block Conditions

Blocked adoption must remain explicit. It is not the same thing as transition refusal or re-resolution blocking. Transition refusal answers whether a proposed transition was accepted. Re-resolution blocking answers whether an accepted transition can emit a successor projection. Adoption blocking answers whether a successor projection can become the current family used by subsequent bounded work.

Minimum block conditions:

- no successor projection is available
- only blocked re-resolution results are available
- selected re-resolution result is unreadable
- selected re-resolution result does not have `outcome == SUCCESSOR_PROJECTION_EMITTED`
- successor family is unreadable
- successor family does not correspond to current family
- successor family does not correspond to the selected re-resolution result
- canonical execution line mismatch
- successor family is not internally coherent
- prior current family is unreadable
- prior family preservation is not evident
- successor family does not preserve prior governing run as preserved non-authority
- successor family does not name exactly one new current governing run
- replay shortcut attempted
- merge shortcut attempted
- continuity-completion shortcut attempted
- silent standing upgrade shortcut attempted
- silent mutation of prior artifacts attempted
- multiple successor families conflict without an explicit bounded selection surface

Blocked adoption must preserve enough detail to show why no new current family was adopted.

## 10. Accepted Adoption Result

An accepted adoption means only the following bounded change:

- successor family becomes the new current governing family for subsequent bounded work
- prior current family remains preserved unchanged
- prior authority artifact remains readable
- prior run-family packet remains readable
- prior preserved-run status packet remains readable
- prior current-governing packet remains readable
- successor authority, family, status, and governing artifacts become the current bounded governing family
- preserved-run multiplicity remains visible
- prior governing run remains visible as preserved non-authority in the adopted family
- no preserved run is erased
- no source artifact is mutated
- no ingress artifact is mutated
- no comparison artifact is mutated
- no prior authority, family, status, governing, transition, or re-resolution artifact is overwritten
- no continuity completion is claimed
- no standing upgrade is claimed
- no replay or merge is performed
- result is preserved in an explicit adoption result artifact

Accepted adoption does not prove final governance. It proves only that one bounded successor family was checked, accepted for current-family use, and preserved as adopted under this spec.

## 11. Adoption Result Artifact

A future implementation needs one bounded result artifact for successor-family adoption.

Minimum shape:

```text
GoverningSuccessorAdoptionResult {
  adoption_result_id: string
  adoption_result_type: string
  adoption_result_version: string
  generated_at: string
  prior_current_family: {
    authority_artifact_path: string
    family_packet_path: string
    status_packet_path: string
    current_governing_packet_path: string
  }
  selected_reresolution_result: {
    reresolution_result_artifact_path: string
    reresolution_id: string
    outcome: SUCCESSOR_PROJECTION_EMITTED | BLOCKED
  }
  selected_successor_family: {
    successor_authority_artifact_path: string
    successor_family_packet_path: string
    successor_status_packet_path: string
    successor_governing_packet_path: string
  }
  outcome: ADOPTED | BLOCKED
  block_code: string | null
  block_reason: string | null
  adoption_basis: string
  non_claims: object
}
```

For accepted adoption, `outcome` should be `ADOPTED`, block fields should be null, and the selected successor family paths should be explicit.

For blocked adoption, `outcome` should be `BLOCKED`, block code and reason should be explicit, and no current-family adoption should be implied.

This artifact is not a broad governance event system. It is one bounded adoption result surface.

## 12. Current Family Status After Adoption

After accepted adoption:

- prior execution-authority resolution artifact remains preserved unchanged
- prior run-family packet remains preserved unchanged
- prior preserved-run status packet remains preserved unchanged
- prior current-governing packet remains preserved unchanged
- selected governing re-resolution result remains preserved unchanged
- successor execution-authority resolution artifact becomes the adopted current authority artifact for subsequent bounded work
- successor run-family packet becomes the adopted current run-family packet for subsequent bounded work
- successor preserved-run status packet becomes the adopted current status packet for subsequent bounded work
- successor current-governing packet becomes the adopted current-governing packet for subsequent bounded work
- prior current governing run remains visible as preserved non-authority in the adopted successor family
- other preserved eligible non-authority runs remain visible
- preserved ineligible runs remain visible

Supersession is selection for subsequent bounded work, not erasure. The prior family remains part of the preserved artifact chain and must remain reconstructable.

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
- cross-host or cross-carrier adoption
- multi-successor arbitration beyond the smallest bounded case
- final rule for many successor families in conflict
- final lifecycle for adopted family chains

This spec defines only the first bounded successor-family adoption model now supportable by the current executable stack.

## 14. What Should Not Be Added Next

The repo should not add:

- logic that treats successor-family emission as self-executing currentness
- replay-based adoption
- merge-based adoption
- broad governance engine
- final persistence or registry machinery as a substitute for adoption law
- new packets that only restate successor-family status without explicit adoption logic
- automatic promotion by latest-emitted, latest-eligible, or latest-successor ordering
- hidden mutation of prior current-family artifacts

Additional work should now either implement this bounded adoption mechanism or refine a forced edge case that blocks implementation. It should not widen into general governance theory.

## 15. Closing Boundary Statement

The repository now has current governing family artifacts and coherent successor family emission by governing re-resolution.

This spec exists because the next forced pressure is successor-family adoption.

It defines the smallest bounded model by which a successor governing family may be accepted as the new current family for subsequent bounded work without mutating prior artifacts, replaying the host, merging preserved runs, completing continuity, or silently upgrading standing.

It does not claim final governance, final continuity completion, final system identity, or system completion.
