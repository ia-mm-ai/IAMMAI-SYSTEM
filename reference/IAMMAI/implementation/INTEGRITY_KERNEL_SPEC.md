# IAMMAI Integrity Kernel Spec

## 1. Purpose

This file defines the minimum integrity kernel for IAMMAI.

Its job is to specify the smallest executable constitutional anti-collapse core that another engineer or system could adopt in order to enter IAMMAI lawfully without collapsing candidate material, occurrence, standing, containment, resolution, or lineage.

It does not define:

- a constitutional rewrite
- a full mechanism draft
- a runtime contract
- a storage design
- a distributed carrier design
- a governance subsystem
- a product specification
- a deployment guide
- a roadmap
- a README
- a manifesto

This file is subordinate to the constitutional protocol. It does not supersede `protocol/IAMMAI_Public_Constitutional_Protocol_v1.0.pdf`, the current repository-native constitutional text surface, machine canon surfaces, or any standing constitutional surface.

## 2. Why This Spec Is Lawful Now

This spec is lawful now because the body has enough standing structure to state the executable minimum without pretending to solve the whole mechanism.

The constitutional body already defines the canonical anti-collapse law: fixed phase order, preparation versus standing-state distinction, HOLD as orthogonal containment, closed resolution through FINALIZE / INVALIDATE / EVOLVE, lineage-preserving succession, governance attribution, contribution-role distinction, and representational recoverability.

The implementation body already gives that law first-pass implementation-facing surfaces through state-machine, canonical-record, implementation-currentness, decision-record, and contribution-role work. The admissibility, relation-seam, system-seam, pilot, trace, and supervision surfaces also make clear that usefulness, capability, participation, and relation cannot promote themselves into authority or standing by accumulation.

That makes a kernel specification lawful at boundary level.

It does not make full mechanism drafting complete. The kernel can now be named as the minimum executable anti-collapse core, while runtime implementation, storage design, carrier design, full governance ontology, and full presence doctrine remain later and separate questions.

## 3. What The Integrity Kernel Is

The integrity kernel is the smallest executable constitutional compression of IAMMAI's anti-collapse law.

It is the minimum body that can:

- admit bounded candidate material without treating it as standing
- record relevant occurrence without treating occurrence as standing
- form standing only through an explicit guarded transition
- hold a transition without turning HOLD into a phase
- resolve a standing matter only through FINALIZE, INVALIDATE, or EVOLVE
- preserve trace and lineage strongly enough that later review can reconstruct what happened

The kernel is therefore not the whole organism. It is the minimum lawful ingress and transition core that prevents the most dangerous collapses:

- candidate into presence
- presence into standing
- threshold or usefulness into truth
- HOLD into semantic state
- generic update into resolution
- correction into overwrite
- consequence into proof of upstream validity

## 4. What The Integrity Kernel Is Not

The integrity kernel is not:

- the whole IAMMAI body
- the full constitutional protocol
- a presence doctrine
- an event doctrine
- an identity system
- a value system
- a governance ontology
- a contribution-role grammar
- a runtime architecture
- a storage or registry design
- a carrier or distributed-system design
- a deployment plan
- a checker family
- a product or platform specification

It also is not ready-made final code. It is implementable in principle, but it remains a specification boundary. Later mechanism work may instantiate it only if that work remains subordinate to the constitutional protocol and preserves the kernel's non-collapse rules.

## 5. Minimum Invariants

The kernel must enforce the following minimum invariants.

### 5.1 Bounded Matter

Every kernel object must be bound to a matter or scope. No candidate, occurrence, standing claim, hold, transition, or resolution may float free of context.

### 5.2 Candidate Is Not Present

Candidate material is material admitted for bounded handling. It is not yet relevant occurrence within the matter.

### 5.3 Present Is Not Standing

Presence records that a non-null occurrence is now present within the bounded matter. It does not itself satisfy threshold, form truth, or create standing.

### 5.4 Standing Requires Guarded Transition

Standing may appear only after an explicit typed transition from PRESENT to STANDING under the required threshold and permissibility conditions. No dark standing is allowed.

### 5.5 HOLD Is Orthogonal

HOLD affects permissibility. It is not a semantic phase, not standing, and not a resolution outcome.

### 5.6 Resolution Family Is Closed

The only lawful resolution outcomes are FINALIZE, INVALIDATE, and EVOLVE. No fourth outcome may be introduced as pending, expired, archived, superseded, updated, dismissed, or any other convenience label.

### 5.7 EVOLVE Requires Lineage

EVOLVE must preserve explicit predecessor and successor relation. Correction enters by successor relation, not by overwriting the prior standing record.

### 5.8 Trace Must Be Preservable

Every transition and resolution must emit enough trace that later review can reconstruct what moved, from where, to where, under what bounded basis, and when.

### 5.9 Convenience Does Not Override Law

Implementation convenience, storage shape, runtime availability, successful execution, branch maturity, or operational usefulness may not bypass these invariants.

## 6. Minimum State Machine

The kernel preserves three semantic states and one orthogonal containment control.

### 6.1 CANDIDATE

CANDIDATE means bounded material has been admitted for handling in relation to a matter or scope.

CANDIDATE is not occurrence, presence, threshold satisfaction, truth, standing, decision, consequence, or authority.

### 6.2 PRESENT

PRESENT means a non-null occurrence has been recorded within the bounded matter.

PRESENT is stronger than CANDIDATE because something has occurred in matter-bound form. It remains weaker than STANDING. It is not threshold satisfaction, truth, continuity, decision, consequence, or lawful closure.

### 6.3 STANDING

STANDING means the matter has crossed from present occurrence into a standing protocol state through an explicit guarded transition.

In the kernel, STANDING is a compressed standing-state entry point. It does not by itself implement the full truth, continuity, decision, and consequence doctrine. It preserves only that standing exists lawfully and traceably for the bounded matter.

### 6.4 HOLD

HOLD is orthogonal containment.

HOLD may attach to a matter or transition posture to block an otherwise eligible irreversible transition. It is not CANDIDATE, PRESENT, STANDING, or RESOLUTION. Release of HOLD restores permissibility only; it does not create standing or resolution.

### 6.5 Resolution Posture

FINALIZE, INVALIDATE, and EVOLVE are typed resolution outcomes for standing matters. They are not ordinary states in the candidate-present-standing chain and must not be replaced by a generic terminal status.

## 7. Minimum Transition Set

The kernel preserves five transition families.

### 7.1 Admit

Admit creates the matter-bound CANDIDATE posture.

It answers whether candidate material may enter bounded kernel handling. It does not create occurrence, standing, authority, or consequence.

### 7.2 Occur

Occur moves CANDIDATE to PRESENT by recording a non-null occurrence within the bounded matter.

It answers what occurrence is now present. It does not create standing.

### 7.3 Stand

Stand moves PRESENT to STANDING when threshold and transition guards are satisfied and no active HOLD blocks the movement.

It answers that the matter now stands in kernel form. It must remain explicit, typed, and trace-preserving.

### 7.4 Hold

Hold applies or releases orthogonal containment.

It answers whether an otherwise eligible transition may proceed now. It does not answer what the matter means and does not resolve the matter.

### 7.5 Resolve

Resolve records FINALIZE, INVALIDATE, or EVOLVE for a standing matter.

Resolve must not accept untyped closure. EVOLVE must carry explicit predecessor and successor relation.

## 8. Minimum Record Grammar

The kernel must emit typed records sufficient to preserve state, transition, containment, resolution, and lineage. The following grammar is conceptual and bounded; it is not a storage schema.

### 8.1 CandidateRecord

CandidateRecord preserves bounded candidate handling.

Minimum fields:

- `candidate_record_id`
- `matter_ref`
- `candidate_ref`
- `admitted_at`
- `basis_ref`

It must not be stored or displayed as standing state.

### 8.2 PresenceRecord

PresenceRecord preserves non-null occurrence within a matter.

Minimum fields:

- `presence_record_id`
- `matter_ref`
- `candidate_record_ref`
- `occurrence_ref`
- `occurred_at`
- `basis_ref`

`occurrence_ref` must be non-null. PresenceRecord does not imply standing.

### 8.3 StandingRecord

StandingRecord preserves the explicit transition into standing kernel posture.

Minimum fields:

- `standing_record_id`
- `matter_ref`
- `presence_record_ref`
- `threshold_basis_ref`
- `stood_at`
- `transition_ref`

StandingRecord must not appear without a PresenceRecord and a threshold basis.

### 8.4 HoldRecord

HoldRecord preserves orthogonal containment.

Minimum fields:

- `hold_record_id`
- `matter_ref`
- `target_transition_ref`
- `hold_status`
- `acted_at`
- `basis_ref`

`hold_status` may record applied or released containment. It must not be treated as a semantic phase or as resolution.

### 8.5 ResolutionRecord

ResolutionRecord preserves typed resolution.

Minimum fields:

- `resolution_record_id`
- `matter_ref`
- `standing_record_ref`
- `resolution_type`
- `acted_at`
- `basis_ref`

`resolution_type` must be one of:

- `FINALIZE`
- `INVALIDATE`
- `EVOLVE`

For EVOLVE, additional lineage fields are required:

- `predecessor_standing_ref`
- `successor_standing_ref`
- `evolve_delta_ref`

EVOLVE without explicit predecessor and successor lineage is invalid kernel behavior.

## 9. Minimum Transition Guards

The kernel must enforce the following guards before accepting state movement or resolution.

### 9.1 Bounded Context Guard

The matter or scope must be explicit before any record is emitted.

### 9.2 Matter / Scope Binding Guard

The object being handled must be bound to the matter it is claimed to affect. Contextless candidate material cannot proceed.

### 9.3 CANDIDATE To PRESENT Occurrence Guard

CANDIDATE may move to PRESENT only if a non-null occurrence is recorded. Availability, intention, or narrative relevance is not enough.

### 9.4 PRESENT To STANDING Threshold Guard

PRESENT may move to STANDING only if a threshold condition or threshold basis is explicit. Presence alone is not standing.

### 9.5 HOLD Guard

No transition may proceed while an active HOLD blocks that transition. HOLD must be checked as orthogonal permissibility, not as semantic state.

### 9.6 Typed Transition Guard

Every movement must be one of the kernel transition families: Admit, Occur, Stand, Hold, or Resolve. Generic mutation is not a lawful kernel transition.

### 9.7 Typed Resolution Guard

Resolve may emit only FINALIZE, INVALIDATE, or EVOLVE. Generic closure, update, archive, supersession, or disappearance must fail.

### 9.8 EVOLVE Lineage Guard

EVOLVE must preserve predecessor and successor relation. A successor without predecessor is an orphan successor and must fail.

### 9.9 Trace Preservability Guard

Every transition must preserve enough trace to reconstruct matter, source record, target record, transition type, basis, time, and lineage relation where applicable.

## 10. The Critical Anti-Collapse Seam

The critical seam is:

**CANDIDATE -> PRESENT -> STANDING**

This seam is the smallest executable form of the constitutional distinction between candidate material, relevant occurrence, and standing state.

CANDIDATE is not PRESENT. A candidate may be admitted for bounded handling and still never occur in the relevant matter.

PRESENT is not STANDING. An occurrence may be matter-bound and still fail threshold, remain held, or never lawfully cross into standing.

STANDING must not appear by storage convention, display, successful processing, repeated use, implementation maturity, or operational dependence. It must appear only through an explicit guarded transition from PRESENT.

If this seam collapses, the kernel fails even if its storage, interface, runtime, or checker behavior appears useful.

## 11. What Remains Outside The Kernel

The following remain outside the integrity kernel:

- full presence doctrine
- full event doctrine
- identity ontology
- value ontology
- broad governance ontology
- contribution-role grammar beyond excluding collapse into authority or standing
- witness and validation artifact families beyond minimum trace preservability
- storage architecture
- carrier architecture
- registry design
- runtime component boundaries
- deployment specifics
- API or vessel operation
- distributed-system behavior
- product posture

These exclusions are intentional. The kernel is small because its job is to preserve constitutional anti-collapse minimums, not to become full IAMMAI by compression.

## 12. Relationship To The Constitutional Body

The integrity kernel is a bounded executable compression subordinate to the constitutional protocol.

The constitutional body remains the source of meaning. The kernel only states the minimum structure that must be executable for a system to preserve IAMMAI's anti-collapse core in practice.

The kernel relates to the constitutional body as follows:

- CANDIDATE compresses bounded preparation-side handling without replacing signal, acceptance, and scope doctrine.
- PRESENT preserves the occurrence seam named by presence without solving full presence doctrine.
- STANDING preserves guarded crossing into standing without implementing the full truth, continuity, decision, and consequence chain.
- HOLD preserves constitutional containment as orthogonal permissibility.
- FINALIZE / INVALIDATE / EVOLVE preserve the closed resolution family.
- EVOLVE lineage preserves no-overwrite and no-orphan-successor law.
- Typed records preserve representational recoverability without imposing storage architecture.

The kernel therefore makes lawful ingress specifiable for later mechanism work. It does not replace constitutional law, conformance doctrine, governance law, contribution-role law, currentness law, runtime law, or vessel posture.

## 13. Closing Boundary Statement

This file defines the minimum integrity kernel only.

It exists to make lawful ingress specifiable without collapsing the body into implementation.

It does not replace the constitutional protocol, does not claim to be the whole IAMMAI body, and does not yet function as a full mechanism draft.
