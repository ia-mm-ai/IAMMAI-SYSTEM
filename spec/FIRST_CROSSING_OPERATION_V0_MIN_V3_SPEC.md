# First Crossing Operation V0 Minimum V3 Specification

## 1. Purpose

This additive successor specification gives the existing `FIRST_CROSSING_OPERATION` family an exact current-line executable input classification. It does not create new first-crossing-operation law.

The mature contract remains `spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md`. That contract already owns the operation meaning and identity, shared pair topology, separate A/B evaluation fields, all-or-nothing minimum law, four terminal outcomes, positive authorization/performance/recording semantics, crossing-occurrence semantics, non-conversion law, Candidate A/B and descendant-body preservation, operation-local false posture, and the downstream `RELATION_BOUNDARY` stopping point.

V3 adds only:

- the exact current V2 `FIRST_CROSSING_BOUNDARY` result identity and content identity;
- the exact current boundary and operation-event binding;
- the fresh current descendant-body-creation operation/request binding;
- deterministic same-binding rerender law;
- current/historical non-replay posture; and
- a disjoint path-level executable classification.

The operation question is exactly:

> Given the exact current FIRST_CROSSING_BOUNDARY result permitting separately bounded first-crossing operation consideration over pair-preserved descendant_body_a_001 and descendant_body_b_001, may mature FIRST_CROSSING_OPERATION evaluate both and, only when its ordinary support is true, authorize, perform, and record First Crossing A and First Crossing B without creating standing descendant, relation, currentness, authority, presence, identity, coupling, runtime, or downstream authorization?

## 2. Status, Rank, and Successor Delta

This specification is additive and non-executable. It preserves append-only successor discipline.

Mature law remains authoritative for:

- `FIRST_CROSSING_OPERATION` meaning and persistent identity;
- one shared operation over two separately evaluated descendant bodies;
- First Crossing A and First Crossing B semantics;
- the exact four-outcome family and precedence;
- positive authorization, performance, and recording semantics;
- the all-or-nothing minimum law;
- occurrence, trace, and non-conversion law;
- Candidate A/B and descendant-body preservation;
- the operation-local false posture; and
- `FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY`.

V3 changes none of those. It exists only because the historical executable does not consume the exact fresh current V2 boundary result and current event binding. Historical resolver, test, result, and terminal-summary material remains preserved precedent. It is not repaired, replaced, reinterpreted, or treated as current source or permission.

## 3. Persistent Operation Identity

The persistent constitutional identity remains exactly:

```text
operation_id = first_crossing_operation_001
operation_type = FIRST_CROSSING_OPERATION
operation_version = 0.1.0
operation_scope = EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY
operation_contract_reference = spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md
operation_contract_sha256 = 047460dc058b8d6a8655d0fef03a422e2330fd832dd4b2045b45968517896549
admissible_future_route = FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY
```

V3 creates no new operation identity and does not create `first_crossing_operation_002`.

## 4. Exact Current Source

The canonical current source is the complete positive V2 boundary result:

```text
result_reference = artifacts/first_crossing_boundary_v0_min_v2/first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json
result_sha256 = bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1
result_version = 0.2.0
resolver_module = resolve_first_crossing_boundary_v0_min_v2
outcome = FIRST_CROSSING_BOUNDARY_ALLOWED
first_crossing_boundary_result = FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED
```

The result reference and SHA-256 pin the complete current boundary event and its carried creation-operation/request, pair, source, source-applicability, contract, history, ownership, and non-claim binding. A future executable may carry the bounded projection in Section 8, but that projection does not replace the complete result identity.

`spec/FIRST_CROSSING_BOUNDARY_V0_MIN_V2_TERMINAL_SUMMARY.md` is cooling evidence only. The historical `FIRST_CROSSING_OPERATION` result is precedent only and cannot substitute as current source, support, permission, occurrence, or replay authority.

## 5. Exact Subject and All-or-Nothing Topology

The subject is one shared `FIRST_CROSSING_OPERATION` event over exactly:

```text
descendant_body_a_id = descendant_body_a_001
descendant_body_b_id = descendant_body_b_001
descendant_body_pair_scope = SEPARATE_DESCENDANT_BODY_RECORDS_ONLY
first_crossing_pair_scope = SEPARATE_FIRST_CROSSING_RECORDS_ONLY
```

The operation owns separate A/B evaluation fields. Those fields are not two independent operation occurrences.

The mature minimum law remains:

```text
A supported + B supported -> FIRST_CROSSING_OPERATION_RECORDED
A supported + B unsupported -> FIRST_CROSSING_OPERATION_BLOCKED
A unsupported + B supported -> FIRST_CROSSING_OPERATION_BLOCKED
both unsupported through the single ordinary support posture -> FIRST_CROSSING_OPERATION_NOT_RECORDED
```

No partial crossing outcome exists. One body cannot receive a positive crossing result while the other receives an unsupported result under this operation.

## 6. Current Operation Event Identity

One current event is identified exactly as:

```text
first_crossing_operation_001
+ first_crossing_boundary_001
+ exact current boundary-result reference and SHA-256
+ descendant_body_a_001
+ descendant_body_b_001
+ descendant_body_creation_operation_001
+ descendant_body_creation_operation_request_001
+ exact pair, source, contract, history, ownership, and non-claim binding
= one current FIRST_CROSSING_OPERATION event
```

The event law is:

```text
same persistent operation identity
+ same exact current boundary-result identity
+ same complete exact binding
= same current FIRST_CROSSING_OPERATION event
```

Repeated pure resolver evaluation is deterministic rerendering of the same event. It is not another crossing occurrence. Resolver-call count is not constitutional event count.

Any changed binding under this identity must return `FIRST_CROSSING_OPERATION_BLOCKED`. No sibling or new operation identity is allocated here. A sibling identity inherits no permission or result. Filesystem presence, timestamp, filename order, artifact count, repository state, latest-file posture, or historical success cannot establish event identity or multiplicity.

## 7. Exact Supplied Envelope and Classification Law

A future pure resolver input must be exactly one closed mapping with these five top-level keys:

1. `intent`
2. `operation_question`
3. `constitutional_event_key`
4. `ordinary_operation_basis`
5. `required_non_claims`

It must contain no caller-selected outcome, result, check, block, summary, metadata, receipt, artifact, occurrence, crossing, invocation, execution, success, standing, or successor selector.

Every required leaf path belongs to exactly one class:

1. `CONTROL`
2. `CONSTITUTIONAL_EVENT_KEY`
3. `ORDINARY_BOUNDARY_ALLOWANCE`
4. `ORDINARY_FIRST_CROSSING_BASIS`
5. `REQUIRED_NON_CLAIM`

Containers are structural only. Containment does not transfer class membership. No path has dual membership. Any unlisted supplied field is unsupported and must block.

The allocation law is:

| Class | Missing | Malformed, contradictory, substituted, widened, misattributed, changed, or unsupported | Valid consequence |
| --- | --- | --- | --- |
| `CONTROL` | `FIRST_CROSSING_OPERATION_BLOCKED` | `FIRST_CROSSING_OPERATION_BLOCKED` | proceed to event-key verification |
| `CONSTITUTIONAL_EVENT_KEY` | `FIRST_CROSSING_OPERATION_BLOCKED` | `FIRST_CROSSING_OPERATION_BLOCKED` | identify this event for review only |
| `REQUIRED_NON_CLAIM` | `FIRST_CROSSING_OPERATION_BLOCKED` | `FIRST_CROSSING_OPERATION_BLOCKED` | preserve bounded false posture |
| `ORDINARY_BOUNDARY_ALLOWANCE` | `FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE` | `FIRST_CROSSING_OPERATION_BLOCKED` | make mature boundary allowance available |
| `ORDINARY_FIRST_CROSSING_BASIS` | `FIRST_CROSSING_OPERATION_NOT_RECORDED` | `FIRST_CROSSING_OPERATION_NOT_RECORDED` | Boolean `true` makes support available |

Validation and outcome precedence are fixed in Sections 12 and 13.

## 8. Exact Field-Class Manifest

This section is exhaustive. Broad prose, source-object shape, or implementation convenience cannot add, omit, inherit, or reclassify a required path.

### 8.1 CONTROL

The complete `CONTROL` set is exactly:

- `$::mapping_cardinality`
- `intent`
- `operation_question`

`$::mapping_cardinality` requires exactly one mapping with exactly the five root keys in Section 7. `intent` must equal `RECORD_FIRST_CROSSING_OPERATION`. `operation_question` must equal the exact question in Section 1.

### 8.2 CONSTITUTIONAL_EVENT_KEY

The complete `CONSTITUTIONAL_EVENT_KEY` set is exactly the following 114 leaf paths. Each path must carry the exact value shown.

#### Persistent Target

```text
constitutional_event_key.target.operation_id = first_crossing_operation_001
constitutional_event_key.target.operation_type = FIRST_CROSSING_OPERATION
constitutional_event_key.target.operation_version = 0.1.0
constitutional_event_key.target.operation_scope = EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY
constitutional_event_key.target.operation_contract_reference = spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md
constitutional_event_key.target.operation_contract_sha256 = 047460dc058b8d6a8655d0fef03a422e2330fd832dd4b2045b45968517896549
constitutional_event_key.target.admissible_future_route = FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY
```

#### Current Boundary Result

```text
constitutional_event_key.current_boundary_result.result_reference = artifacts/first_crossing_boundary_v0_min_v2/first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json
constitutional_event_key.current_boundary_result.result_sha256 = bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1
constitutional_event_key.current_boundary_result.result_version = 0.2.0
constitutional_event_key.current_boundary_result.resolver_module = resolve_first_crossing_boundary_v0_min_v2
constitutional_event_key.current_boundary_result.blocked = false
constitutional_event_key.current_boundary_result.block_code = null
constitutional_event_key.current_boundary_result.block_issue_path = null
constitutional_event_key.current_boundary_result.requires_descendant_body_creation = false
```

The complete result identity pins the current positive boundary event. Under that identity, changed boundary outcome, changed boundary result, false operation-consideration posture, or `blocked = true` is event corruption and must block.

#### Persistent Boundary

```text
constitutional_event_key.boundary.boundary_id = first_crossing_boundary_001
constitutional_event_key.boundary.boundary_type = FIRST_CROSSING_BOUNDARY
constitutional_event_key.boundary.boundary_version = 0.1.0
constitutional_event_key.boundary.boundary_scope = CONSIDER_FIRST_CROSSING_AFTER_DESCENDANT_BODY_CREATION_ONLY
constitutional_event_key.boundary.boundary_contract_reference = spec/FIRST_CROSSING_BOUNDARY_V0_MIN_SPEC.md
constitutional_event_key.boundary.boundary_contract_sha256 = 87680155b33852d3b5bca2848df8b68a50c053878c5b49eeeb2fba61e3a007e2
constitutional_event_key.boundary.admissible_future_route = FIRST_CROSSING_BOUNDARY_THEN_FIRST_CROSSING_OPERATION_ONLY
```

#### Current First-Crossing Operation Event

```text
constitutional_event_key.operation_event.persistent_operation_id = first_crossing_operation_001
constitutional_event_key.operation_event.persistent_boundary_id = first_crossing_boundary_001
constitutional_event_key.operation_event.current_boundary_result_reference = artifacts/first_crossing_boundary_v0_min_v2/first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json
constitutional_event_key.operation_event.current_boundary_result_sha256 = bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1
constitutional_event_key.operation_event.persistent_creation_operation_id = descendant_body_creation_operation_001
constitutional_event_key.operation_event.fresh_creation_operation_request_id = descendant_body_creation_operation_request_001
constitutional_event_key.operation_event.descendant_body_a_id = descendant_body_a_001
constitutional_event_key.operation_event.descendant_body_b_id = descendant_body_b_001
constitutional_event_key.operation_event.same_identity_same_binding_is_deterministic_rerender = true
constitutional_event_key.operation_event.resolver_call_count_is_event_count = false
constitutional_event_key.operation_event.sibling_event_identity_allocated = false
```

#### Persistent Creation Operation

```text
constitutional_event_key.creation_operation.operation_family = DESCENDANT_BODY_CREATION_OPERATION
constitutional_event_key.creation_operation.operation_id = descendant_body_creation_operation_001
constitutional_event_key.creation_operation.operation_type = DESCENDANT_BODY_CREATION_OPERATION
constitutional_event_key.creation_operation.operation_version = 0.1.0
constitutional_event_key.creation_operation.operation_scope = EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY
```

#### Fresh Creation Operation Event

```text
constitutional_event_key.creation_operation_event.fresh_operation_request_id = descendant_body_creation_operation_request_001
constitutional_event_key.creation_operation_event.persistent_operation_id = descendant_body_creation_operation_001
constitutional_event_key.creation_operation_event.operation_request_result_reference = artifacts/descendant_body_creation_operation_request_v0_min/descendant_body_creation_operation_request_001__descendant_body_creation_operation_request_v0_min_result.json
constitutional_event_key.creation_operation_event.operation_request_result_sha256 = dd95b114773c8ff1b1f0a271530f282c2360b3aa58c07231886f111808d6e744
constitutional_event_key.creation_operation_event.same_identity_same_binding_is_deterministic_rerender = true
constitutional_event_key.creation_operation_event.resolver_call_count_is_event_count = false
```

#### Descendant Body A

```text
constitutional_event_key.descendant_body_a.descendant_body_id = descendant_body_a_001
constitutional_event_key.descendant_body_a.candidate_standing_source_id = descendant_body_basis_candidate_a_001
constitutional_event_key.descendant_body_a.candidate_role = CANDIDATE_A
constitutional_event_key.descendant_body_a.candidate_standing_label = CANDIDATE_A_STANDING
constitutional_event_key.descendant_body_a.candidate_basis_id = descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis
constitutional_event_key.descendant_body_a.candidate_basis_label = CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS
constitutional_event_key.descendant_body_a.candidate_basis_scope = Motion-side admissible variation
```

#### Descendant Body B

```text
constitutional_event_key.descendant_body_b.descendant_body_id = descendant_body_b_001
constitutional_event_key.descendant_body_b.candidate_standing_source_id = descendant_body_basis_candidate_b_001
constitutional_event_key.descendant_body_b.candidate_role = CANDIDATE_B
constitutional_event_key.descendant_body_b.candidate_standing_label = CANDIDATE_B_STANDING
constitutional_event_key.descendant_body_b.candidate_basis_id = descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis
constitutional_event_key.descendant_body_b.candidate_basis_label = CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS
constitutional_event_key.descendant_body_b.candidate_basis_scope = Regulation-side admissibility bounds
```

#### Pair Preservation

```text
constitutional_event_key.pair.descendant_body_pair_scope = SEPARATE_DESCENDANT_BODY_RECORDS_ONLY
constitutional_event_key.pair.complete_pair_preserved = true
constitutional_event_key.pair.descendant_bodies_remain_sibling = true
constitutional_event_key.pair.descendant_body_non_hierarchy_preserved = true
constitutional_event_key.pair.candidate_standing_non_hierarchy_preserved = true
constitutional_event_key.pair.candidate_basis_non_hierarchy_preserved = true
constitutional_event_key.pair.motion_does_not_erase_regulation = true
constitutional_event_key.pair.regulation_not_sovereign_over_motion = true
```

#### Source Identity and Ownership

```text
constitutional_event_key.source.selected_surface_identity = descendant_body_candidate_standing_operation_001
constitutional_event_key.source.selected_surface_type = DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION
constitutional_event_key.source.selected_surface_version = 0.1.0
constitutional_event_key.source.selected_surface_scope = EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY
constitutional_event_key.source.selected_surface_family = DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION
constitutional_event_key.source.selected_surface_semantic_owner = DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION
constitutional_event_key.source.selected_surface_result_reference = artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_standing_operation_v0_min/descendant_body_candidate_standing_operation_001__candidate_standing_operation_v0_min_result.json
constitutional_event_key.source.selected_surface_result_sha256 = ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961
constitutional_event_key.source.source_standing_contract_reference = spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md
constitutional_event_key.source.source_standing_contract_sha256 = b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3
constitutional_event_key.source.source_standing_contract_version = 0.1.0
constitutional_event_key.source.source_custody_preserved = true
constitutional_event_key.source.source_lineage_preserved = true
constitutional_event_key.source.source_rank_preserved = true
constitutional_event_key.source.source_scope_preserved = true
```

Candidate A and Candidate B remain semantically owned by `DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION`. This operation may verify carried identity and preservation posture but may not reinterpret either candidate's source semantics.

#### Prior Source Applicability

```text
constitutional_event_key.source_applicability.source_applicability_id = descendant_body_candidate_standing_effect_applicability_boundary_001
constitutional_event_key.source_applicability.source_applicability_type = DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY
constitutional_event_key.source_applicability.source_applicability_version = 0.1.0
constitutional_event_key.source_applicability.source_applicability_scope = ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_ONE_EXACT_DECLARED_DOWNSTREAM_USE_ONLY
constitutional_event_key.source_applicability.source_applicability_outcome = DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED
constitutional_event_key.source_applicability.result_reference = artifacts/descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2/descendant_body_candidate_standing_effect_applicability_boundary_001__descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2_result.json
constitutional_event_key.source_applicability.source_route = CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY
constitutional_event_key.source_applicability.source_declared_matter_use = CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY
constitutional_event_key.source_applicability.complete_review_reached = true
```

This applicability is carried lineage only. It is not widened into first-crossing permission.

#### Freshness and Non-Replay

```text
constitutional_event_key.freshness.fresh_operation_request_identity_declared = true
constitutional_event_key.freshness.operation_request_identity_distinct_from_operation_identity = true
constitutional_event_key.freshness.operation_request_identity_distinct_from_historical_occurrence = true
constitutional_event_key.freshness.historical_operation_result_is_current_permission = false
constitutional_event_key.freshness.historical_operation_result_is_current_source = false
constitutional_event_key.freshness.historical_operation_result_is_current_occurrence = false
constitutional_event_key.freshness.historical_operation_occurrence_reused = false
constitutional_event_key.freshness.historical_operation_material_reused = false
constitutional_event_key.freshness.historical_operation_result_replayed = false
constitutional_event_key.freshness.historical_success_treated_as_fresh_permission = false
```

#### Historical Operation Evidence

```text
constitutional_event_key.historical_operation.historical_operation_id = first_crossing_operation_001
constitutional_event_key.historical_operation.result_reference = artifacts/integrity_host_v0_min_coexistence_first_crossing_operation_v0_min_v2/first_crossing_operation_001__first_crossing_operation_v0_min_v2_result.json
constitutional_event_key.historical_operation.result_sha256 = 8b66349ff6d75670d91f4e9b202d0a4210dfb8d47065258a1103600d8dd99871
constitutional_event_key.historical_operation.outcome = FIRST_CROSSING_OPERATION_RECORDED
constitutional_event_key.historical_operation.first_crossing_result = FIRST_CROSSING_SUPPORTED
constitutional_event_key.historical_operation.result_is_current_permission = false
constitutional_event_key.historical_operation.result_is_current_source = false
constitutional_event_key.historical_operation.result_is_current_occurrence = false
constitutional_event_key.historical_operation.result_replayed = false
constitutional_event_key.historical_operation.success_treated_as_fresh_permission = false
```

#### Non-Claim Owner Attribution

```text
constitutional_event_key.non_claim_attribution.source_boundary.owner = FIRST_CROSSING_BOUNDARY
constitutional_event_key.non_claim_attribution.source_creation_operation.owner = DESCENDANT_BODY_CREATION_OPERATION
constitutional_event_key.non_claim_attribution.source_family.owner = DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION
constitutional_event_key.non_claim_attribution.target_local.owner = FIRST_CROSSING_OPERATION
```

Owner paths are event-key members. Non-claim maps and their values remain `REQUIRED_NON_CLAIM` members.

### 8.3 ORDINARY_BOUNDARY_ALLOWANCE

The complete `ORDINARY_BOUNDARY_ALLOWANCE` set is exactly these seven paths:

```text
ordinary_operation_basis.source_outcome = FIRST_CROSSING_BOUNDARY_ALLOWED
ordinary_operation_basis.source_boundary_result = FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED
ordinary_operation_basis.first_crossing_operation_consideration_allowed = true
ordinary_operation_basis.descendant_body_creation_referenced = true
ordinary_operation_basis.descendant_body_a_referenced = true
ordinary_operation_basis.descendant_body_b_referenced = true
ordinary_operation_basis.descendant_body_created_referenced = true
```

No omitted ordinary allowance may be inferred from event-key identity. If one or more paths are absent while all higher-precedence classes remain exact, the outcome is `FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE`.

Any present allowance value that is malformed, contradictory, substituted, or conflicts with the pinned current result identity must return `FIRST_CROSSING_OPERATION_BLOCKED`. In particular, a changed source outcome, changed boundary result, false operation-consideration posture, or a false reference posture under the pinned positive source identity is contradiction, not ordinary absence.

### 8.4 ORDINARY_FIRST_CROSSING_BASIS

The complete `ORDINARY_FIRST_CROSSING_BASIS` set is exactly one path:

```text
ordinary_operation_basis.first_crossing_support_found
```

Exact Boolean `true` makes mature support available for positive recording. Missing, Boolean `false`, malformed, non-Boolean, or otherwise non-exact posture produces `FIRST_CROSSING_OPERATION_NOT_RECORDED`.

This class creates no `REQUIRES_ADDITIONAL_BASIS` outcome. `NOT_RECORDED` creates no retry, repair, resubmission, continuation, or successor permission.

### 8.5 REQUIRED_NON_CLAIM

The two structural maps are:

- `required_non_claims.source_boundary`
- `required_non_claims.operation_local`

The maps are not classified leaves. Every member path below belongs only to `REQUIRED_NON_CLAIM`. Each map must contain exactly its listed keys, and every value must be Boolean `false`.

Source-boundary required non-claims are exactly these nine paths:

```text
required_non_claims.source_boundary.first_crossing_authorized
required_non_claims.source_boundary.crossing_authorized
required_non_claims.source_boundary.first_crossing_performed
required_non_claims.source_boundary.crossing_performed
required_non_claims.source_boundary.relation_created
required_non_claims.source_boundary.coupling_created
required_non_claims.source_boundary.presence_established
required_non_claims.source_boundary.identity_created
required_non_claims.source_boundary.follow_on_authorized
```

They preserve that the current boundary allowed operation consideration only.

Operation-local required non-claims are exactly these 62 paths:

```text
required_non_claims.operation_local.relation_created
required_non_claims.operation_local.field_machinery_created
required_non_claims.operation_local.runtime_created
required_non_claims.operation_local.api_created
required_non_claims.operation_local.currentness_created
required_non_claims.operation_local.authority_created
required_non_claims.operation_local.standing_created
required_non_claims.operation_local.output_authorized
required_non_claims.operation_local.action_authorized
required_non_claims.operation_local.derivative_reception_authorized
required_non_claims.operation_local.synchronization_authorized
required_non_claims.operation_local.coupling_assigned_to_descendant_body_a
required_non_claims.operation_local.coupling_assigned_to_descendant_body_b
required_non_claims.operation_local.coupling_assigned_to_candidate_a
required_non_claims.operation_local.coupling_assigned_to_candidate_b
required_non_claims.operation_local.coupling_created
required_non_claims.operation_local.third_candidate_created
required_non_claims.operation_local.third_model_admitted
required_non_claims.operation_local.presence_established
required_non_claims.operation_local.identity_created
required_non_claims.operation_local.standing_descendant_created
required_non_claims.operation_local.descendant_standing_check_performed
required_non_claims.operation_local.follow_on_authorized
required_non_claims.operation_local.follow_on_work_authorized
required_non_claims.operation_local.prior_unsupported_candidate_a_claim_validated
required_non_claims.operation_local.prior_unsupported_candidate_b_claim_validated
required_non_claims.operation_local.prior_unsupported_derivation_event_claim_validated
required_non_claims.operation_local.valid_derivation_event_recorded
required_non_claims.operation_local.affected_file_repaired
required_non_claims.operation_local.affected_file_edited
required_non_claims.operation_local.affected_file_deleted
required_non_claims.operation_local.affected_file_overwritten
required_non_claims.operation_local.affected_file_replaced
required_non_claims.operation_local.affected_file_redeemed
required_non_claims.operation_local.affected_file_treated_as_clean_basis
required_non_claims.operation_local.contaminated_lineage_treated_as_clean_basis
required_non_claims.operation_local.first_crossing_boundary_overridden
required_non_claims.operation_local.first_crossing_boundary_bypassed
required_non_claims.operation_local.descendant_body_creation_operation_overridden
required_non_claims.operation_local.descendant_body_creation_operation_bypassed
required_non_claims.operation_local.scan_performed
required_non_claims.operation_local.repository_scan_performed
required_non_claims.operation_local.file_discovery_performed
required_non_claims.operation_local.repair_performed
required_non_claims.operation_local.validation_enforced
required_non_claims.operation_local.hidden_repair_performed
required_non_claims.operation_local.silent_overwrite_performed
required_non_claims.operation_local.direct_first_crossing_operation_spec_to_first_crossing_operation_completion
required_non_claims.operation_local.direct_boundary_allowance_to_first_crossing_without_operation
required_non_claims.operation_local.direct_descendant_body_creation_to_first_crossing_without_boundary_and_operation
required_non_claims.operation_local.direct_first_crossing_to_relation
required_non_claims.operation_local.direct_first_crossing_to_runtime
required_non_claims.operation_local.direct_first_crossing_to_authority_currentness
required_non_claims.operation_local.direct_first_crossing_to_coupling_creation
required_non_claims.operation_local.direct_first_crossing_to_third_candidate_route
required_non_claims.operation_local.direct_first_crossing_to_third_model_route
required_non_claims.operation_local.direct_first_crossing_to_presence
required_non_claims.operation_local.direct_first_crossing_to_identity
required_non_claims.operation_local.direct_first_crossing_to_standing_descendant
required_non_claims.operation_local.direct_first_crossing_to_descendant_standing
required_non_claims.operation_local.direct_first_crossing_to_output_action
required_non_claims.operation_local.direct_first_crossing_to_follow_on_work
```

These are the mature 76 false fields minus the 14 operation-owned positive fields in Section 14. Those 14 positive fields must not appear in `operation_local`.

`automatic_successor_created` remains source-owned and is not reattributed into operation-local ownership. `relation_boundary_invoked` is a stopping-point field, not a required operation-local input.

For either map, a missing map, missing key, extra key, non-mapping value, non-Boolean value, or any `true` value must return `FIRST_CROSSING_OPERATION_BLOCKED`.

### 8.6 Manifest Cardinality and Disjointness

The exact classified counts are:

```text
CONTROL = 3
CONSTITUTIONAL_EVENT_KEY = 114
ORDINARY_BOUNDARY_ALLOWANCE = 7
ORDINARY_FIRST_CROSSING_BASIS = 1
SOURCE_BOUNDARY REQUIRED_NON_CLAIM = 9
OPERATION_LOCAL REQUIRED_NON_CLAIM = 62
REQUIRED_NON_CLAIM = 71
total required classified semantic items = 196
```

Every listed path is unique. The five classes are pairwise disjoint. No required leaf is unclassified. No container is a classified leaf. No class is inferred by containing-map ancestry.

## 9. Pair, Candidate, Body, and Source Preservation

Successful operation completion preserves:

- `descendant_body_a_001` bound only to Candidate A and its exact Motion-side basis;
- `descendant_body_b_001` bound only to Candidate B and its exact Regulation-side basis;
- separate sibling descendant-body records;
- complete pair preservation;
- descendant-body, candidate-standing, and candidate-basis non-hierarchy;
- `motion_does_not_erase_regulation = true`;
- `regulation_not_sovereign_over_motion = true`; and
- source semantic ownership by `DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION`.

The operation does not merge, rank, swap, reinterpret, or couple the bodies. It transfers no semantic ownership and creates no third body, third candidate, or third model.

## 10. Historical and Current Separation

Historical operation evidence is exactly:

```text
operation_id = first_crossing_operation_001
result_reference = artifacts/integrity_host_v0_min_coexistence_first_crossing_operation_v0_min_v2/first_crossing_operation_001__first_crossing_operation_v0_min_v2_result.json
result_sha256 = 8b66349ff6d75670d91f4e9b202d0a4210dfb8d47065258a1103600d8dd99871
outcome = FIRST_CROSSING_OPERATION_RECORDED
first_crossing_result = FIRST_CROSSING_SUPPORTED
```

It supplies operation-contract, result-shape, and semantic precedent only. It supplies no current source, boundary allowance, support, permission, occurrence, or replay authority.

```text
persistent operation identity != historical occurrence reuse
historical success != current permission
artifact persistence != current authority
```

## 11. Deterministic Rerender and Non-Replay Law

Same persistent identity plus the same complete exact current binding is the same operation event. Pure evaluation of that exact envelope may render the same result repeatedly without multiplying the constitutional event or crossing occurrence.

Any changed event-key leaf under this identity is contradictory and blocks. Historical result substitution blocks. No event is inferred from resolver calls, writes, timestamps, artifact counts, filename suffixes, Git history, or repository presence.

No sibling or successor event is allocated. No automatic successor permission is created.

## 12. Deterministic Validation and Probe Law

Validation order is:

1. `CONTROL`
2. `CONSTITUTIONAL_EVENT_KEY`
3. `REQUIRED_NON_CLAIM`
4. `ORDINARY_BOUNDARY_ALLOWANCE`
5. `ORDINARY_FIRST_CROSSING_BASIS`

This order preserves the terminal precedence in Section 13. Ordinary absence is considered only after all blocking classes are exact.

For an otherwise canonical envelope, each probe has exactly one outcome:

| Probe | Sole outcome |
| --- | --- |
| missing current boundary-result reference | `FIRST_CROSSING_OPERATION_BLOCKED` |
| changed current boundary-result SHA-256 | `FIRST_CROSSING_OPERATION_BLOCKED` |
| changed current boundary outcome or boundary result | `FIRST_CROSSING_OPERATION_BLOCKED` |
| false `first_crossing_operation_consideration_allowed` under pinned identity | `FIRST_CROSSING_OPERATION_BLOCKED` |
| current boundary `blocked = true` | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing Descendant Body A identity | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing Descendant Body B identity | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing pair preservation | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing sibling posture | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing Candidate A basis | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing Candidate B basis | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing source semantic owner | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing creation operation id | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing fresh creation-operation request id | `FIRST_CROSSING_OPERATION_BLOCKED` |
| missing mature operation contract | `FIRST_CROSSING_OPERATION_BLOCKED` |
| historical operation substituted as current permission | `FIRST_CROSSING_OPERATION_BLOCKED` |
| freshness or non-replay member missing | `FIRST_CROSSING_OPERATION_BLOCKED` |
| required non-claim missing | `FIRST_CROSSING_OPERATION_BLOCKED` |
| required non-claim true or malformed | `FIRST_CROSSING_OPERATION_BLOCKED` |
| one ordinary boundary-allowance path absent | `FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE` |
| one present ordinary boundary-allowance path malformed or conflicting | `FIRST_CROSSING_OPERATION_BLOCKED` |
| `first_crossing_support_found` absent | `FIRST_CROSSING_OPERATION_NOT_RECORDED` |
| `first_crossing_support_found = false` | `FIRST_CROSSING_OPERATION_NOT_RECORDED` |
| `first_crossing_support_found` malformed | `FIRST_CROSSING_OPERATION_NOT_RECORDED` |
| A supported and B unsupported | `FIRST_CROSSING_OPERATION_BLOCKED` |
| A unsupported and B supported | `FIRST_CROSSING_OPERATION_BLOCKED` |
| both unsupported through the single support posture | `FIRST_CROSSING_OPERATION_NOT_RECORDED` |
| exact complete current envelope with support true | `FIRST_CROSSING_OPERATION_RECORDED` and `FIRST_CROSSING_SUPPORTED` |

Per-body support is not an accepted caller input. The single ordinary support field derives both supported postures together. Any mixed supplied or internally derived A/B posture is contradictory to mature all-or-nothing law and must block.

No probe has two lawful outcomes.

## 13. Terminal Outcome Family and Precedence

The exact mature outcome family, in precedence order, remains:

1. `FIRST_CROSSING_OPERATION_BLOCKED`
2. `FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE`
3. `FIRST_CROSSING_OPERATION_NOT_RECORDED`
4. `FIRST_CROSSING_OPERATION_RECORDED`

Precedence is exactly that order:

1. structural, control, event identity, source identity, content identity, binding, contract, pair, ownership, attribution, freshness, history, prohibited-posture, mixed-pair, or non-claim failure produces `BLOCKED`;
2. an otherwise exact envelope missing one or more ordinary boundary-allowance paths produces `REQUIRES_BOUNDARY_ALLOWANCE`;
3. an otherwise exact envelope with complete allowance but support not exact Boolean `true` produces `NOT_RECORDED`;
4. an exact complete envelope with support true produces `RECORDED`.

No caller may select an outcome. V3 adds no outcome.

`REQUIRES_BOUNDARY_ALLOWANCE` and `NOT_RECORDED` create no retry, repair, resubmission, continuation, or successor permission. A blocked, requires, or not-recorded result is a lawful terminal operation posture, not authorization for another event.

## 14. Exact Positive Operation Result

For an exact current event, complete allowance, and `first_crossing_support_found = true`:

```text
outcome = FIRST_CROSSING_OPERATION_RECORDED
first_crossing_result = FIRST_CROSSING_SUPPORTED
```

The operation owns exactly these 14 Boolean-positive fields:

```text
first_crossing_operation_recorded = true
first_crossing_evaluation_performed = true
first_crossing_result_recorded = true
first_crossing_a_evaluated = true
first_crossing_b_evaluated = true
first_crossing_a_supported = true
first_crossing_b_supported = true
first_crossing_supported = true
first_crossing_authorized = true
crossing_authorized = true
first_crossing_performed = true
crossing_performed = true
first_crossing_a_recorded = true
first_crossing_b_recorded = true
```

There is no fifteenth Boolean-positive field and no additional positive constitutional consequence. Generic `crossing_occurrence_established` and `operation_occurrence_established` fields are not created.

## 15. Per-Body and Pair Result Material

Positive First Crossing A material preserves exactly its identity binding and mature posture:

```text
first_crossing_id = first_crossing_a_001
descendant_body_id = descendant_body_a_001
candidate_standing_source_id = descendant_body_basis_candidate_a_001
candidate_role = CANDIDATE_A
candidate_standing_label = CANDIDATE_A_STANDING
candidate_basis_id = descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis
candidate_basis_label = CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS
candidate_basis_scope = Motion-side admissible variation
descendant_body_created = true
descendant_body_is_first_crossing = false
first_crossing_supported = true
first_crossing_authorized = true
crossing_authorized = true
first_crossing_performed = true
crossing_performed = true
first_crossing_recorded = true
```

Positive First Crossing B material preserves exactly its identity binding and mature posture:

```text
first_crossing_id = first_crossing_b_001
descendant_body_id = descendant_body_b_001
candidate_standing_source_id = descendant_body_basis_candidate_b_001
candidate_role = CANDIDATE_B
candidate_standing_label = CANDIDATE_B_STANDING
candidate_basis_id = descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis
candidate_basis_label = CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS
candidate_basis_scope = Regulation-side admissibility bounds
descendant_body_created = true
descendant_body_is_first_crossing = false
first_crossing_supported = true
first_crossing_authorized = true
crossing_authorized = true
first_crossing_performed = true
crossing_performed = true
first_crossing_recorded = true
```

Each body material also preserves `relation_created = false`, `coupling_created = false`, `presence_established = false`, and `identity_created = false`.

The positive pair result preserves:

```text
first_crossing_pair_scope = SEPARATE_FIRST_CROSSING_RECORDS_ONLY
both_first_crossings_supported = true
both_first_crossings_authorized = true
both_first_crossings_performed = true
both_first_crossings_recorded = true
first_crossing_a_recorded = true
first_crossing_b_recorded = true
descendant_bodies_remain_sibling = true
descendant_body_non_hierarchy_preserved = true
candidate_standing_non_hierarchy_preserved = true
motion_does_not_erase_regulation = true
regulation_not_sovereign_over_motion = true
```

The pair result preserves relation, coupling, third-candidate, third-model, presence, identity, standing-descendant, descendant-standing-check, and follow-on posture false.

## 16. Authorization, Occurrence, Trace, and Standing

Mature occurrence law remains:

```text
first_crossing_authorized = true
+ crossing_authorized = true
= crossing may happen

first_crossing_performed = true
+ crossing_performed = true
= crossing happened
```

Operation-owned trace/result posture is preserved by:

```text
first_crossing_result_recorded = true
+ first_crossing_a_recorded = true
+ first_crossing_b_recorded = true
+ per-body first_crossing_recorded = true
```

A later persisted result artifact may preserve evidence of the occurrence. Artifact persistence does not create the occurrence.

The layers remain separate:

```text
creation occurrence != creation trace
creation trace != current FIRST_CROSSING_BOUNDARY event
boundary event != boundary artifact
boundary allowance != crossing authorization
crossing authorization != crossing occurrence
crossing occurrence != crossing result artifact
crossing trace != standing descendant
first crossing != relation
first crossing != currentness
first crossing != authority
first crossing != presence
first crossing != identity
first crossing != coupling
first crossing != runtime
```

The standing lock is exact:

```text
FIRST_CROSSING_OPERATION_DOES_NOT_CREATE_STANDING_DESCENDANT
standing_descendant_created = false
standing_created = false
descendant_standing_check_performed = false
```

Positive crossing does not create or check standing descendant.

## 17. Downstream Stopping Point

Positive completion names only:

```text
admissible_future_route = FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY
next_separately_bounded_rank = RELATION_BOUNDARY
```

The stopping posture remains:

```text
relation_boundary_invoked = false
relation_created = false
standing_descendant_created = false
currentness_created = false
authority_created = false
presence_established = false
identity_created = false
coupling_created = false
runtime_created = false
api_created = false
output_authorized = false
action_authorized = false
follow_on_work_authorized = false
automatic_successor_created = false
```

`RELATION_BOUNDARY` is merely open for separate consideration. It is not invoked, authorized, scheduled, executed, or externalized here.

## 18. Explicitly Open

The following remain open, unscheduled, unauthorized, and unexecuted:

- resolver machinery for this V3 specification;
- dedicated tests;
- request material;
- live current operation result;
- artifact receipt;
- terminal summary;
- `RELATION_BOUNDARY`;
- standing-descendant machinery;
- relation;
- currentness;
- authority;
- presence;
- identity;
- coupling;
- FIELD machinery;
- runtime;
- API;
- output or action authorization;
- derivative reception;
- synchronization; and
- follow-on work.

Open does not mean next, selected, scheduled, authorized, required, automatic, or executed.

## 19. Anti-Overlap and Closing Lock

Mature `FIRST_CROSSING_OPERATION` law already stands. This V3 specification changes no crossing semantics, pair law, outcome family, positive consequence, occurrence law, non-conversion law, or downstream rank. It only connects the exact fresh current V2 boundary event to mature operation law through an exact current source identity, current event binding, deterministic rerender/non-replay law, and disjoint executable classification.

The exact current source remains the V2 `FIRST_CROSSING_BOUNDARY` result at `artifacts/first_crossing_boundary_v0_min_v2/first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json`, pinned by SHA-256 `bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1`. The persistent operation remains `first_crossing_operation_001`. The current subject remains `descendant_body_a_001` and `descendant_body_b_001` under one shared operation with separate A/B evaluations and all-or-nothing minimum law.

The exact executable classification contains 3 controls, 114 event-key paths, 7 ordinary boundary-allowance paths, 1 ordinary support path, 9 source-boundary non-claims, and 62 operation-local non-claims: 196 required classified semantic items, with no overlap or unclassified required leaf.

On exact positive completion, exactly 14 operation-owned fields become true and the result is `FIRST_CROSSING_SUPPORTED`. That posture authorizes, performs, and records First Crossing A and First Crossing B together as separate first-crossing records only. It does not create standing descendant, relation, currentness, authority, presence, identity, coupling, runtime, API, output/action authority, follow-on authorization, or automatic successor permission.

Historical operation completion remains precedent only. Same identity plus the same complete binding is deterministic rerendering of the same current event; changed binding blocks. `RELATION_BOUNDARY` remains the sole named separately bounded future route and is not invoked or authorized here.

The completed V3 specification creates no automatic successor permission.
