# Cross-Carrier Surface Receipt Boundary V0 Minimum Specification

## 1. Purpose

This file defines the bounded boundary for cross-carrier surface receipt within the present `IAMMAI-SYSTEM` execution line.

Receipt is not byte transfer.

A copied file on another carrier is passive storage. It is not lawful receipt. Lawful receipt requires a bounded receiving surface that preserves the source carrier, receiving carrier, carried surface identity, carried surface outcome, integrity evidence where available, source/downstream posture, and non-claims.

The purpose of this boundary is to prevent the statement "this artifact exists on another carrier" from becoming source replacement, currentness creation, authority, permission, successor standing, carrier merge, body creation, or continuation.

This file is a boundary specification only. It does not implement a resolver, test, carrier registry, persistence layer, multi-carrier law, distributed standing, repository synchronization, full body transfer, second-body creation, carrier participation law, external contact law, presence surface, threshold surface, truth surface, action surface, consequence surface, signal series logic, body relevance medium, workflow, router, event bus, roadmap, README, or manifesto.

## 2. Status and Rank

This specification ranks below constitutional and reference authority surfaces, including the preserved `reference/IAMMAI/` surfaces.

This specification is additive. It does not replace:

- current self-orientation
- current-body conformance
- post-conformance standing closure
- cross-surface correspondence
- body-signal recognition, acceptance, or scope
- derivative-vessel relation boundary
- current executable source
- tests
- emitted artifacts
- current governing/reference surfaces

This specification does not create authority.

This specification does not create permission.

This specification does not create currentness.

This specification does not define final governance.

This specification does not complete continuity.

This specification does not complete final system identity.

This specification is bounded to the present execution line.

## 3. Why This Spec Is Needed Now

Current self-orientation v6 mirrors current standing posture across upstream current/governing basis and downstream re-entry, body-signal, derivative-vessel relation, derivative vessel, operator-facing, and closure surfaces.

Current-body conformance proves that selected standing surfaces cohere as one lawful body when its checks pass and integrated non-claims remain false.

Post-conformance standing closure records `BODY_CONFORMANT` as meaning, not permission, currentness, signal, action, completion, or continuation.

Cross-surface correspondence permits selected standing surfaces to be read together under bounded relation while preserving rank, source, scope, lineage, outcome locality, and non-claims.

The next carrier question is narrower than multi-carrier law. It asks only what minimum condition allows one standing surface to be received by a carrier that does not contain the full body.

An empty receiving carrier exposes the minimum receipt condition. It may hold bytes, but bytes alone do not preserve lawful receipt.

Without a cross-carrier receipt boundary, copying a standing surface to another carrier could be misread as currentness, authority, source replacement, successor standing, body creation, participation, or continuation.

Therefore one bounded cross-carrier surface receipt boundary is lawful as a protective seam before any future portable receipt implementation.

## 4. Definitions

`carrier` means a bounded environment that can hold, read, receive, copy, or emit artifacts. A carrier is not source by default.

`source carrier` means the carrier from which a carried packet or carried surface is transmitted or copied for one receipt question. This role is local to the carried packet and does not create universal source authority.

`receiving carrier` means the carrier that receives or holds the carried packet or carried surface. A receiving carrier does not become source, currentness, authority, permission, successor, or body by receiving bytes.

`carried surface` means one standing surface selected for receipt across a carrier boundary, including its identity, outcome/status, path or filename where available, source/downstream posture, and non-claims.

`carried packet` means the bounded transfer package that carries one carried surface and its receipt basis fields from a source carrier toward an intended receiving carrier.

`receipt` means the bounded recording that a receiving carrier has received one carried surface as carried evidence while preserving source carrier identity, receiving carrier identity, carried surface identity, carried surface outcome, integrity evidence where available, and non-claims.

`receipt basis` means the declared source carrier, receiving carrier, carried surface, carried surface outcome, integrity evidence, receipt purpose, source/downstream posture, and explicit non-claims that permit lawful receipt.

`receipt claim` means the bounded assertion that one carried surface was received by one receiving carrier as carried evidence.

`receipt refusal` means an explicit refusal to recognize receipt because the carrier basis, carried surface basis, integrity evidence, receipt purpose, or non-claims do not support lawful receipt.

`passive storage` means bytes are present on a carrier.

`lawful receipt` means the carrier preserves and records receipt under explicit basis and non-claims.

## 5. What Cross-Carrier Receipt Means

Cross-carrier receipt means:

- one carried surface has crossed from a source carrier to a receiving carrier
- the carried surface identity is preserved
- the source carrier identity is preserved
- the receiving carrier identity is declared
- the carried surface outcome/status is preserved
- the carried surface path or filename is preserved where available
- integrity evidence is preserved where available
- the carried surface remains carried/downstream on the receiving carrier
- source/downstream posture remains bounded
- non-claims remain false
- receipt may later support bounded assessment only if separately admitted

Receipt may help a later implementation or manual review see that one carrier received one carried surface as evidence. It does not command work.

## 6. What Cross-Carrier Receipt Does Not Mean

Cross-carrier receipt does not mean:

- the receiving carrier becomes source
- the receiving carrier becomes current
- the receiving carrier becomes authority
- the receiving carrier receives permission
- the receiving carrier becomes successor
- the receiving carrier becomes body
- the carried surface replaces source
- the carried surface becomes local currentness
- the carried surface authorizes execution
- the carried surface authorizes continuation
- the carried surface becomes signal by default
- the carried surface establishes presence
- the carried surface establishes threshold
- the carried surface creates truth
- the carried surface authorizes action
- the carried surface creates consequence
- full repository transfer
- repository synchronization
- distributed standing
- multi-carrier law
- merge

Availability on a carrier is not authority. Local copy is not currentness. Receipt is not body formation.

## 7. Required Receipt Basis

A future implementation or manual receipt review may recognize receipt only when:

- source carrier identity is declared
- receiving carrier identity is declared
- carried surface identity is declared
- carried surface outcome/status is declared
- carried surface path or filename is preserved where available
- carried surface hash or equivalent integrity evidence is preserved where available
- receipt purpose is declared
- carried surface source/downstream posture is known or explicitly bounded
- receipt non-claims are explicit
- receipt does not create source replacement
- receipt does not create currentness
- receipt does not create authority
- receipt does not create permission
- receipt does not create successor standing
- receipt does not merge carriers
- receipt does not mutate the carried surface

If any required receipt basis cannot be preserved, receipt must be refused.

## 8. Minimum Carried Packet

A future carried packet should preserve at minimum:

- `carried_packet_metadata`
- `source_carrier`
- `intended_receiving_carrier`
- `carried_surface`
- `carried_surface_integrity`
- `receipt_purpose`
- `non_claims`

Minimum `carried_packet_metadata` should preserve:

- carried packet id
- carried packet type
- carried packet version
- created/exported timestamp where available
- emitter or exporter surface where available

Minimum `source_carrier` should preserve:

- carrier label or id
- carrier role: source carrier for this carried packet only
- local path context where available
- non-claim that carrier source role does not create universal source authority

Minimum `intended_receiving_carrier` should preserve:

- carrier label or id
- carrier role: receiving carrier
- non-claim that receiving carrier does not become source/current/authority

Minimum `carried_surface` should preserve:

- surface id
- surface path where available
- surface filename
- surface outcome/status
- surface type where available
- selected upstream basis where available
- source/downstream posture where available

Minimum `carried_surface_integrity` should preserve:

- hash where available
- hash algorithm where available
- byte length where available
- created/exported timestamp where available

This specification defines the future packet shape only. It does not implement it.

## 9. Minimum Receipt Result Shape

If a future implementation records cross-carrier surface receipt, its minimum outcome family is:

- `CARRIED_SURFACE_RECEIVED`
- `BLOCKED`

The minimum future result sections are:

- `cross_carrier_surface_receipt_metadata`
- `source_carrier_basis`
- `receiving_carrier_basis`
- `carried_surface_basis`
- `carried_surface_integrity_check`
- `receipt_checks`
- `receipt_statement`
- `receipt_non_meaning`
- `what_remains_open`
- `non_claims`
- `outcome`
- `block`

Minimum metadata should preserve:

- receipt result id
- receipt result type
- receipt result version
- generated timestamp
- resolver or recorder module where implemented

For `CARRIED_SURFACE_RECEIVED`, the result should preserve selected source carrier identity, receiving carrier identity, carried surface identity, carried surface path or filename where available, carried surface outcome/status, integrity evidence where available, passed checks, receipt statement, and non-claims.

For `BLOCKED`, the result should preserve selected basis where available, block code, block reason, failed checks, and non-claims.

This specification defines the future result shape only. It does not implement it.

## 10. Permitted First Carried Surface Class

The safest first carried surface class is a closed standing surface, especially a post-conformance closure artifact, because that surface already preserves that conformance is meaning, not permission.

This does not require that exact artifact forever.

A first receipt proof should prefer a carried surface that is:

- closed
- non-operative
- explicit about non-claims
- explicit about identity and outcome/status
- explicit about selected basis where exposed
- explicit about zero failed checks where exposed
- explicit that it does not authorize follow-on work

The first carried surface should not be selected because it is latest. It should be selected because it is closed, bounded, and non-inflationary.

## 11. Receipt Refusal

Receipt must be refused when:

- source carrier is missing
- receiving carrier is missing
- carried surface is missing
- carried surface is malformed
- carried surface lacks identity
- carried surface lacks outcome/status
- integrity evidence is missing where required
- hash does not match where hash checking is required
- receipt purpose is undeclared
- receipt would treat receiving carrier as source
- receipt would create currentness
- receipt would create authority
- receipt would create permission
- receipt would create successor standing
- receipt would merge source and receiving carrier
- receipt would treat latest local copy as current
- receipt would mutate the carried surface
- receipt would replay source body
- receipt would run upstream mechanisms
- receipt would authorize continuation
- receipt would create signal by default
- receipt would establish presence
- receipt would establish threshold
- receipt would create truth
- receipt would authorize action
- receipt would create consequence
- receipt would treat byte transfer as lawful receipt

Blocked receipt does not invalidate the carried surface. It means the receiving carrier may not recognize the requested receipt as lawful receipt.

## 12. Relation to Cross-Surface Correspondence

Cross-surface correspondence compares selected standing surfaces under a declared relation.

Cross-carrier receipt records that one carried surface was received by another carrier.

Receipt is not correspondence.

Correspondence may later compare a source surface and a received carried surface only if a correspondence question is separately declared and the correspondence boundary is satisfied.

Receipt does not automatically create correspondence.

Correspondence does not automatically create receipt.

## 13. Relation to Self-Orientation

Receipt does not replace self-orientation.

Receipt does not force a self-orientation successor.

Receiving a carried surface does not materially change current posture by default.

A future self-orientation successor would require separate bounded pressure and basis. Receipt alone is not enough.

Self-orientation should not become the metabolizer of every carrier copy.

## 14. Relation to Current-Body Conformance and Post-Conformance Closure

Receipt does not prove body conformance on the receiving carrier.

Receipt does not reopen conformance closure.

Receipt does not transfer conformance as permission.

Receipt does not allow the receiving carrier to claim body conformance by holding the artifact.

Receipt may preserve a closure artifact as carried evidence only.

## 15. Relation to Signal

Receipt is not signal recognition.

A received carried surface is not automatically a signal.

Any future signal use must pass body-signal recognition, acceptance, and scope.

Receipt cannot bypass signal gates.

Receipt does not establish signal presence, threshold, truth, action, routing, workflow, or body relevance medium.

## 16. Relation to Multi-Carrier Law

This specification is not multi-carrier law.

This specification handles one carried surface crossing one carrier boundary.

This specification does not define simultaneous carrier relation.

This specification does not define competing carrier currentness.

This specification does not define distributed standing.

This specification does not authorize multiple carriers to relate by default.

This specification may later provide a primitive for multi-carrier law only if separately admitted by a later bounded surface.

## 17. Relation to Passive Storage

A copied file on another carrier is passive storage.

Passive storage does not create receipt.

Passive storage does not preserve lawful status by itself.

Lawful receipt requires explicit receipt basis and non-claims.

A carrier without a receipt surface can hold bytes but cannot lawfully receive as IAMMAI carrier.

Passive storage may be useful operationally. Usefulness is not receipt, standing, currentness, permission, authority, or body formation.

## 18. What Remains Open

After this boundary spec, these remain open and not executed:

- portable receipt implementation
- cross-carrier receipt test
- multi-carrier relation law
- distributed standing
- persistence/registry law
- presence law
- threshold law
- truth law
- action/consequence law
- generalized vessel relation lifecycle
- body relevance medium
- signal series or accumulation logic
- any future self-orientation successor unless separately justified

Open means not scheduled.

Open means not authorized.

Open means not executed.

## 19. Future Refusal / Block Conditions

A future implementation must block explicitly when any of the following are present:

- source carrier missing
- receiving carrier missing
- carried surface missing
- carried surface malformed
- carried surface lacks identity
- carried surface lacks outcome
- carried surface integrity missing where required
- hash mismatch
- receipt purpose undeclared
- receipt treats receiving carrier as source
- receipt creates currentness
- receipt creates authority
- receipt creates permission
- receipt creates successor standing
- receipt merges carriers
- receipt treats local copy as current
- receipt mutates carried surface
- receipt replays source body
- receipt runs upstream mechanisms
- receipt authorizes continuation
- receipt creates signal by default
- receipt establishes presence
- receipt establishes threshold
- receipt creates truth
- receipt authorizes action
- receipt creates consequence
- receipt treats byte transfer as lawful receipt

Representative future block codes may include:

- `SOURCE_CARRIER_MISSING`
- `RECEIVING_CARRIER_MISSING`
- `CARRIED_SURFACE_MISSING`
- `CARRIED_SURFACE_MALFORMED`
- `CARRIED_SURFACE_IDENTITY_MISSING`
- `CARRIED_SURFACE_OUTCOME_MISSING`
- `CARRIED_SURFACE_INTEGRITY_MISSING`
- `CARRIED_SURFACE_HASH_MISMATCH`
- `RECEIPT_PURPOSE_UNDECLARED`
- `RECEIPT_TREATS_RECEIVER_AS_SOURCE`
- `RECEIPT_CREATES_CURRENTNESS`
- `RECEIPT_CREATES_AUTHORITY`
- `RECEIPT_CREATES_PERMISSION`
- `RECEIPT_CREATES_SUCCESSOR_STANDING`
- `RECEIPT_MERGES_CARRIERS`
- `RECEIPT_TREATS_LOCAL_COPY_AS_CURRENT`
- `RECEIPT_MUTATES_CARRIED_SURFACE`
- `RECEIPT_REPLAYS_SOURCE_BODY`
- `RECEIPT_RUNS_UPSTREAM_MECHANISMS`
- `RECEIPT_AUTHORIZES_CONTINUATION`
- `RECEIPT_CREATES_SIGNAL_BY_DEFAULT`
- `RECEIPT_ESTABLISHES_PRESENCE`
- `RECEIPT_ESTABLISHES_THRESHOLD`
- `RECEIPT_CREATES_TRUTH`
- `RECEIPT_AUTHORIZES_ACTION`
- `RECEIPT_CREATES_CONSEQUENCE`
- `BYTE_TRANSFER_MISTAKEN_FOR_RECEIPT`
- `NON_CLAIM_MISSING_OR_FLIPPED`

Blocked receipt does not mean the source carrier or carried surface is invalid. It means the receiving carrier refused lawful receipt.

## 20. Preserved Non-Claims

Cross-carrier surface receipt preserves false posture for:

- `authority_created = false`
- `permission_created = false`
- `currentness_created = false`
- `source_replaced = false`
- `receiving_carrier_became_source = false`
- `receiving_carrier_became_current = false`
- `receiving_carrier_became_authority = false`
- `receiving_carrier_became_successor = false`
- `carried_surface_became_source = false`
- `carried_surface_became_currentness = false`
- `carried_surface_became_permission = false`
- `carried_surface_became_signal_by_default = false`
- `presence_established = false`
- `threshold_met = false`
- `truth_created = false`
- `action_authorized = false`
- `consequence_created = false`
- `carrier_merge_performed = false`
- `local_copy_currentness = false`
- `source_body_replayed = false`
- `upstream_mechanisms_run = false`
- `continuation_authorized = false`
- `multi_carrier_law_created = false`
- `distributed_standing_created = false`
- `latest_file_currentness = false`
- `recency_fraud = false`
- `mutation_performed = false`
- `replay_performed = false`
- `merge_performed = false`

These non-claims remain false before, during, and after lawful receipt. They are not pending permissions.

## 21. Closing Boundary Statement

Cross-carrier surface receipt permits one carried standing surface to be received by another carrier only as carried evidence, with source carrier, receiving carrier, carried surface identity, integrity evidence, and non-claims preserved.

It closes the question:

`Can this carrier receive this carried surface without becoming source, currentness, authority, permission, successor, or body?`

It does not open the question:

`Do multiple carriers now stand in relation?`
