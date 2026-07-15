# BODY SIGNAL RECOGNITION V0 MIN SPEC

## 1. Purpose

This file defines the first bounded body-signal recognition surface for the
present `IAMMAI-SYSTEM` execution line.

`spec/BODY_SIGNAL_BOUNDARY_V0_MIN_SPEC.md` now defines what body-relevant signal
may be and what signal must never become. The next pressure is not to build a
signaling system. The next pressure is to define how one candidate indication
from one standing source artifact/result may be checked as signal.

Body-signal recognition is the bounded determination:

```text
one standing source artifact/result
+ one candidate signal declaration
-> SIGNAL_RECOGNIZED or BLOCKED
```

Recognition is not permission. Recognition is not admissibility to act.
Recognition is not routing. Recognition is not authority. Recognition is only
the bounded determination that one claimed indication qualifies as
body-relevant signal.

This file does not implement RADIO 22, a signal router, an event bus, signal
priority, signal scheduling, signal storage semantics, a regulation loop,
workflow machinery, roadmap/autonomy machinery, next-step generation, action
authorization, general continuation permission, persistence/registry law, or a
governance engine.

## 2. Status and Rank

This spec ranks below constitutional/reference authority surfaces.

It is additive. It does not create authority. It does not define final
governance. It does not complete continuity. It does not complete final system
identity. It does not replace current executable source, tests, artifacts, or
standing result surfaces.

This is a bounded signal-recognition spec for the present execution line only.
It does not introduce a general signaling doctrine and does not make signal
current, governing, permissive, or authoritative.

## 3. Why This Spec Is Needed Now

The body now has post-receipt self-orientation v3. The body-signal boundary now
defines what signal may indicate and what signal must not become.

Without a recognition surface, signal remains only a boundary category and
cannot yet be checked concretely. Without recognition checks, future signal work
could smuggle authority, permission, latest-file recency, workflow, roadmap,
priority, routing, or continuation through a claimed signal.

Therefore one bounded body-signal recognition spec is lawful before any signal
recognition resolver is built.

## 4. What Now Stands

The standing surfaces relevant to this recognition boundary include:

- current self-orientation v3
- body-signal boundary
- re-entry admissibility
- re-entry receipt
- current-state standing, open, and admissibility/touch surfaces
- continuity transfer and continuity transfer receipt
- received derivative participation and received derivative action permission
- continuity memory seam
- v0 body pass
- bounded OpenAI derivative vessel v3
- operator-facing terminal brief
- carried non-claims that remain false

This is only the compact material context for signal recognition. It is not a
whole-body recap.

## 5. Body-Signal Recognition Scope

This spec applies only to one source artifact/result and one candidate signal
declaration.

It decides recognition or blocking for that one candidate only. It does not
route signals. It does not rank signals. It does not aggregate multiple
signals. It does not create priority. It does not create scheduling. It does
not create storage semantics. It does not create a signal bus or event bus. It
does not create regulation. It does not create workflow. It does not create a
next-step generator. It does not authorize action. It does not create general
continuation. It does not mutate prior artifacts. It does not explain the repo
for outsiders.

## 6. Required Input Pair

Body-signal recognition requires exactly two inputs:

1. one standing source artifact/result
2. one candidate signal declaration

Both inputs are required. A candidate signal cannot be recognized without a
readable standing source artifact/result. A source artifact does not
automatically emit signal. A candidate declaration does not become signal by
declaring itself signal.

Recognition must be derived from correspondence between the candidate
declaration and the selected source artifact/result.

## 7. Candidate Signal Declaration Shape

The candidate declaration is a candidate, not a signal by itself and not a
permission object.

### 7.1 `candidate_signal_metadata`

The declaration must preserve:

- `candidate_signal_id`
- `candidate_signal_type`
- `candidate_signal_version`
- `declared_at`
- `declared_by_surface`

`declared_by_surface` records where the declaration was made. It does not imply
authority.

### 7.2 `source_artifact_basis`

The declaration must preserve:

- `source_artifact_path`
- `source_artifact_id`
- `source_artifact_family`
- `source_artifact_type`
- `source_artifact_outcome`
- `source_artifact_resolver_or_emitter_module` where exposed

Required posture:

- the source artifact/result must be readable
- the source artifact/result must already stand
- the candidate signal must preserve source identity and outcome

### 7.3 `claimed_signal`

The declaration must preserve:

- `signal_category`
- `claimed_signal_family`
- `claimed_signal_posture`
- `claimed_signal_reason`
- `claimed_relevance`
- `claimed_carried_fields`

`signal_category` must be one of the bounded boundary categories:

- `CURRENT_BASIS_SIGNAL`
- `CURRENT_STATE_SIGNAL`
- `OPEN_SURFACE_SIGNAL`
- `BLOCKED_REFUSED_SIGNAL`
- `TOUCH_ADMISSIBILITY_SIGNAL`
- `CONTINUITY_TRANSFER_SIGNAL`
- `CONTINUITY_RECEIPT_SIGNAL`
- `DERIVATIVE_PARTICIPATION_SIGNAL`
- `DERIVATIVE_ACTION_PERMISSION_SIGNAL`
- `MEMORY_SEAM_SIGNAL`
- `BODY_PASS_SIGNAL`
- `DERIVATIVE_VESSEL_SIGNAL`
- `OPERATOR_FACING_SIGNAL`
- `REENTRY_ADMISSIBILITY_SIGNAL`
- `REENTRY_RECEIPT_SIGNAL`
- `EXHAUSTION_CLOSURE_SIGNAL`
- `NON_CLAIM_SIGNAL`

These are recognition categories for this surface only. They do not create
routing, priority, scheduling, permission, currentness, or governance.

### 7.4 `carried_posture`

The declaration must preserve relevant carried posture, including:

- source outcome/posture carried
- source path/id/family carried
- open status if relevant
- blocked/refused status if relevant
- receipt status if relevant
- exhaustion status if relevant
- derivative status if relevant
- operator-facing status if relevant
- non-claims carried if relevant

### 7.5 `hierarchy_constraints`

The declaration must preserve:

- `signal_allowed_as_authority`
- `signal_allowed_as_permission`
- `signal_allowed_as_currentness_selector`
- `derivative_signal_allowed_as_source`
- `operator_signal_allowed_as_source`
- `reentry_signal_allowed_as_governing_basis`
- `latest_file_recency_allowed`

Required posture: all of these must be `false`.

### 7.6 `correspondence_requirements`

The declaration must preserve:

- `must_preserve_source_identity`
- `must_preserve_source_outcome`
- `must_preserve_signal_category_source_match`
- `must_preserve_derivative_source_distinction`
- `must_preserve_open_blocked_receipt_exhaustion_distinctions`
- `must_preserve_non_claims`
- `must_prevent_over_mirroring`
- `must_prevent_under_mirroring`

Required posture: all of these must be `true`.

### 7.7 `declared_non_claims`

The declaration must preserve these explicit true non-claims:

- `does_not_create_authority = true`
- `does_not_create_permission = true`
- `does_not_create_currentness = true`
- `does_not_authorize_action = true`
- `does_not_authorize_follow_on_work = true`
- `does_not_create_workflow = true`
- `does_not_create_roadmap = true`
- `does_not_create_signal_router = true`
- `does_not_create_event_bus = true`
- `does_not_replace_source_surface = true`
- `does_not_upgrade_derivative_to_source = true`
- `does_not_turn_receipt_into_permission = true`

## 8. Source-to-Signal Category Correspondence

Source family and outcome must correspond to the claimed signal category.

Minimum correspondence:

- current/effective/governing/current-state source may support `CURRENT_BASIS_SIGNAL` or `CURRENT_STATE_SIGNAL`
- what-remains-open source may support `OPEN_SURFACE_SIGNAL`
- blocked/refused source may support `BLOCKED_REFUSED_SIGNAL`
- touch/admissibility source may support `TOUCH_ADMISSIBILITY_SIGNAL`
- continuity transfer source may support `CONTINUITY_TRANSFER_SIGNAL`
- continuity transfer receipt source may support `CONTINUITY_RECEIPT_SIGNAL`
- received derivative participation source may support `DERIVATIVE_PARTICIPATION_SIGNAL`
- received derivative action-permission source may support `DERIVATIVE_ACTION_PERMISSION_SIGNAL`
- continuity memory seam source may support `MEMORY_SEAM_SIGNAL`
- v0 body pass source may support `BODY_PASS_SIGNAL`
- bounded derivative vessel source may support `DERIVATIVE_VESSEL_SIGNAL`
- operator terminal brief source may support `OPERATOR_FACING_SIGNAL`
- re-entry admissibility source may support `REENTRY_ADMISSIBILITY_SIGNAL`
- re-entry receipt source may support `REENTRY_RECEIPT_SIGNAL` or `EXHAUSTION_CLOSURE_SIGNAL`
- non-claim-bearing source may support `NON_CLAIM_SIGNAL`

Category mismatch must block. Category match does not create permission.

A source may support more than one candidate signal category only if each
candidate is separately declared, checked, and recognized.

## 9. Recognition Checks

A future implementation must perform at least these checks before emitting
`SIGNAL_RECOGNIZED`:

- source artifact is readable
- source artifact is well-formed enough to inspect
- source artifact outcome is present
- candidate signal declaration is well-formed
- signal category is one of the bounded categories
- signal category corresponds to source artifact family/outcome
- candidate preserves source id/path/family/outcome
- candidate preserves relevant posture
- candidate preserves hierarchy constraints
- candidate preserves non-claims
- candidate does not create authority
- candidate does not create permission
- candidate does not create currentness
- candidate does not authorize action or follow-on work
- candidate does not create workflow, roadmap, router, event bus, or regulation
- candidate does not treat derivative/API/operator/re-entry source as governing/current basis
- candidate does not infer currentness by latest-file recency
- candidate does not over-mirror into whole-body replacement
- candidate does not under-mirror required source posture

Recognition checks must be proportioned to the selected source. They must be
strong enough to preserve source posture and bounded enough not to become the
source, authority, workflow, or a whole-body replacement.

## 10. Refusal / Block Conditions

The signal recognition result must block explicitly when any of these occur:

- no source artifact basis
- source artifact unreadable
- source artifact malformed
- source outcome missing
- candidate signal declaration missing
- candidate signal declaration malformed
- signal category unknown
- signal category mismatches source
- source identity not preserved
- source outcome not preserved
- relevant posture omitted
- non-claim missing or flipped
- signal attempts to create authority
- signal attempts to create permission
- signal attempts to create currentness
- signal attempts to authorize action
- signal attempts to authorize follow-on work
- signal treats derivative/API/operator surface as source
- signal treats re-entry surface as governing/current basis
- signal treats re-entry receipt as reusable permission
- signal infers currentness by recency
- signal hides blocked/refused posture
- signal converts open to completed
- signal omits receipt posture where receipt is the source
- signal omits exhaustion posture where re-entry receipt is the source
- signal becomes workflow, roadmap, autonomy, router, event bus, or next-step language
- signal over-mirrors into whole-body replacement
- signal under-mirrors required posture
- signal widens source scope beyond selected source

Blocked signal recognition does not mean the source artifact is invalid. It
means the candidate indication is refused as body-relevant signal.

## 11. Result Artifact

A future implementation should emit the smallest bounded result artifact needed
to preserve the recognition decision.

Minimum top-level sections:

- `body_signal_recognition_metadata`
- `selected_source_artifact`
- `selected_candidate_signal`
- `signal_recognition_checks`
- `outcome`
- `block`
- `recognized_signal`
- `body_signal_recognition_basis`
- `non_claims`

Minimum metadata:

- `body_signal_recognition_result_id`
- `body_signal_recognition_result_type`
- `body_signal_recognition_result_version`
- `generated_at`
- `resolver_module`

Minimum outcome family:

- `SIGNAL_RECOGNIZED`
- `BLOCKED`

For `SIGNAL_RECOGNIZED`, `recognized_signal` should preserve:

- signal category
- source artifact id/path/family/outcome
- carried posture
- non-authoritative status
- non-permission status
- non-currentness status
- bounded relation to current self-orientation where relevant

For `BLOCKED`, the result should preserve:

- selected source artifact where available
- selected candidate signal where available
- block code/reason
- failed checks
- non-claims

## 12. What Remains Preserved

After signal recognition or blocking:

- source artifact remains preserved
- candidate declaration remains preserved where available
- recognized signal result remains additive
- source remains source
- derivative remains derivative
- operator-facing remains operator-facing
- re-entry remains downstream
- open remains open
- blocked/refused remains visible
- receipt remains receipt
- exhaustion remains exhaustion
- signal does not authorize action
- signal does not authorize follow-on work

## 13. What This Spec Still Does Not Define

This spec still does not define:

- RADIO 22
- final body signaling system
- signal routing
- event bus
- regulation loop
- nervous system
- workflow engine
- orchestration framework
- roadmap generation
- autonomous continuation
- next-step generation
- general permission surfaces
- final governance
- continuity completion
- final system identity
- persistence/registry law
- distributed network
- signal priority
- signal scheduling
- signal storage semantics
- multi-signal aggregation

## 14. What Should Not Be Added Next

The next slice should avoid:

- no `RADIO_22.py`
- no body-wide signal router
- no event bus
- no nervous-system implementation
- no workflow loop
- no roadmap/autonomy machinery
- no signal priority/scheduling/storage semantics
- no multi-signal aggregation
- no signal-to-permission shortcut
- no derivative/operator/re-entry authority upgrade
- no recency-based currentness
- no generalized continuation lane

## 15. Closing Boundary Statement

The body-signal boundary defines what signal may be and what signal must not
become. Body-signal recognition checks one candidate indication against that
boundary.

Recognition may identify body-relevant posture. Recognition may not create
authority, permission, currentness, routing, priority, workflow, roadmap, or
continuation.

Nothing in this surface becomes sovereignty.
