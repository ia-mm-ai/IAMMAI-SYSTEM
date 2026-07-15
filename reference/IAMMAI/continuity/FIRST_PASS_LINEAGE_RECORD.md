# IAMMAI First-Pass Lineage Record

## 1. Purpose

This file defines the first-pass lineage record object as the first practical continuity-housing move for the IAMMAI body.

Its job is to make one bounded continuity object explicit enough that lineage stops living only as posture, file naming, additive succession style, and human carrying, and starts becoming a housed continuity object in its own right.

It does not:

- define a constitutional rewrite
- define a continuity-family master map
- define a storage architecture
- define a graph or database design
- define a schema
- define a distributed systems plan
- replace continuity, admissibility, accession, standing, or vessel surfaces already standing in the body

This file is additive only. It does not replace the continuity surfaces, the admissibility surfaces, the accession family, the standing bridges, or the vessel posture surfaces already standing in the repository.

## 2. Why This Note Is Needed Now

Lineage is central to the body, but it is still underhoused.

At present, additive succession is often carried through file naming, transfer-account posture, bridge posture, readable proof carry, and sober human memory. That has been lawful and often legible, but it is not yet a small explicit continuity object that can house one bounded lineage move directly.

The body therefore needs one first practical move toward explicit continuity housing. It does not need the whole continuity city at once. It needs one small room in which a lineage move can be recorded without atmosphere doing too much of the work.

This note exists to define that move without overbuilding it.

## 3. What The First-Pass Lineage Record Answers

The first-pass lineage record answers the bounded question:

**What is the smallest explicit object that can house one additive lineage move without falsifying continuity?**

This is not yet a full continuity storage question.

It is a narrower object question. The aim is to house one relation between an earlier bounded thing and a later bounded thing in a way that preserves anti-erasure, additive succession, and explicit continuity reading.

## 4. The First-Pass Lineage Record Object

The first-pass lineage record object is a small continuity object for one lineage move only.

It houses:

- what earlier bounded thing is being related
- what later bounded thing is being related
- what kind of lineage move is being claimed
- what remained
- what changed

In first-pass form, the object may be read as:

```json
{
  "lineage_record_id": "...",
  "recorded_at": "...",
  "from_ref": "...",
  "to_ref": "...",
  "relation_type": "...",
  "preserves": ["..."],
  "changes": ["..."]
}
```

This object is anti-erasure and anti-mush.

It houses one lineage move only. It does not attempt to house the whole body, the whole continuity family, or the whole storage system in miniature.

## 5. Minimum Fields

### `lineage_record_id`

What it means:
A bounded identifier for this one lineage record.

Why it is needed:
The lineage move itself must be referable as an object rather than only as ambient relation.

What it must not collapse into:
It must not collapse into a claim that the record itself has become canonical law, standing, or sovereign identity.

### `recorded_at`

What it means:
The time at which this lineage record was recorded as an explicit continuity object.

Why it is needed:
Lineage needs explicit recording posture, not only human reconstruction after the fact.

What it must not collapse into:
It must not collapse into the claim that the recorded time is the whole meaning of lineage. Lineage is not merely chronology.

### `from_ref`

What it means:
The bounded earlier reference from which the lineage move is being read.

Why it is needed:
Later does not erase earlier. The record must say what it is coming from.

What it must not collapse into:
It must not collapse into the claim that `from_ref` is obsolete, invalidated, or replaced merely because a later relation exists.

### `to_ref`

What it means:
The bounded later reference to which the lineage move is being read.

Why it is needed:
Additive continuity needs an explicit later object or surface, not only a vague claim that something changed.

What it must not collapse into:
It must not collapse into a silent supersession claim or a claim that the later reference has absorbed total authority.

### `relation_type`

What it means:
The bounded type of lineage move being claimed between `from_ref` and `to_ref`.

Why it is needed:
Lineage relation should not remain wholly atmospheric. The record must say what kind of move is being claimed.

What it must not collapse into:
It must not collapse into a final relation vocabulary for the whole continuity family. First-pass relation typing should stay small and revisable.

### `preserves`

What it means:
The bounded list of things explicitly preserved across this lineage move.

Why it is needed:
Lineage is not only about difference. It is also about continuity, carry, and what remained.

What it must not collapse into:
It must not collapse into decorative reassurance or generic prose. It names continuity content directly.

### `changes`

What it means:
The bounded list of things explicitly changed across this lineage move.

Why it is needed:
Lineage is not only about preservation. It is also about bounded alteration, rebind, narrowing, addition, or later posture.

What it must not collapse into:
It must not collapse into total narrative explanation or into a claim that everything changed merely because one move occurred.

## 6. Why `preserves` and `changes` Matter

Lineage is not only “what changed.”

Lineage is also “what remained.”

Without `changes`, the object becomes an inert continuity claim that cannot say what the move actually did.

Without `preserves`, the object collapses toward generic transition logging, because it can only report difference and cannot house continuity carry.

Together, `preserves` and `changes` keep the record lineage-bearing rather than merely sequential. They force the record to say, in bounded form, what continuity was kept and what alteration was made.

## 7. What This Object Is Not

This object is not:

- the final continuity model
- the final storage architecture
- the final geometry or topology of continuity
- the whole continuity family
- a graph or database solution
- a canonical replacement for law, proof, decision, bridge, or revocation surfaces themselves

It is also not a claim that all continuity can now be reduced to one lineage record. It is the first practical continuity-housing move only.

The reduced shape is preferred at this stage because the body needs explicit continuity housing more urgently than it needs a large ontology. A smaller object can be used, inspected, and stabilized without pretending the full continuity system is already known.

## 8. Relationship to Existing Surfaces

The first-pass lineage record sits beside existing surfaces by housing continuity relation, not by replacing the content those surfaces already carry.

With [`continuity/LAWFUL_TRANSFER_SEAM_v0.md`](./LAWFUL_TRANSFER_SEAM_v0.md) and [`continuity/RELEASE_AND_INGRESS_v0.md`](./RELEASE_AND_INGRESS_v0.md), it helps house bounded crossing relation while preserving origin, carried relation, and jurisdiction distinction.

With [`admissibility/ADMISSIBILITY_LAYER.md`](../admissibility/ADMISSIBILITY_LAYER.md) and [`admissibility/CANON_AND_STANDING_ADMISSIBILITY.md`](../admissibility/CANON_AND_STANDING_ADMISSIBILITY.md), it helps prevent continuity from dissolving into visibility, atmosphere, or untyped carry.

With the accession family, especially [`accession/ACCESSION_LAYER.md`](../accession/ACCESSION_LAYER.md) through [`accession/REVOCATION_AND_WITHDRAWAL.md`](../accession/REVOCATION_AND_WITHDRAWAL.md), it provides a small object form in which additive accession moves, preserved conditions, and later narrowing or revocation can be housed without erasing earlier stages.

With [`v1/23_POST_SLICE_STANDING_BRIDGE.md`](../v1/23_POST_SLICE_STANDING_BRIDGE.md), [`v1/24_OPEN_BLOCKERS__POST_ADMISSIBILITY_SLICE.md`](../v1/24_OPEN_BLOCKERS__POST_ADMISSIBILITY_SLICE.md), [`v1/26_WHOLE_LINE_05_CRITERIA_BINDING_REVIEW.md`](../v1/26_WHOLE_LINE_05_CRITERIA_BINDING_REVIEW.md), [`v1/33_POST_PROOF_004_SEAM_GATE_STATUS_BRIDGE.md`](../v1/33_POST_PROOF_004_SEAM_GATE_STATUS_BRIDGE.md), and [`v1/34_POST_API_BACKED_POSTURE_BRIDGE.md`](../v1/34_POST_API_BACKED_POSTURE_BRIDGE.md), it gives posture carry, proof carry, blocker carry, and API-posture carry a possible continuity object form rather than leaving them only as bridge style and naming style.

With the vessel posture surfaces, including [`vessel/current_state_what_stands_reader_v1/CONTRACT.md`](../vessel/current_state_what_stands_reader_v1/CONTRACT.md) and [`vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md`](../vessel/current_state_what_stands_reader_v1/API_BACKED_POSTURE_DECISION__POST_ALIGNMENT_REVIEW.md), it may later help house contract-to-posture relation or posture-to-bridge relation without turning those surfaces themselves into continuity storage.

The lineage record therefore houses relation between surfaces. It does not replace the surfaces being related.

## 9. What Remains Open

This note still leaves open:

- the final relation-type vocabulary
- whether provenance or state should later live inside the lineage object itself or beside it
- the final storage architecture
- the final canonical versus derivative storage split
- the final geometry or topology of continuity
- whether this object should later become schema, storage record, or something richer

These open questions matter. They are left open on purpose so the body can house lineage explicitly without pretending the whole continuity system is already solved.

## 10. Closing Boundary Statement

This file defines the first-pass lineage record object only.

It is the first practical continuity-housing move, not the final continuity system.

Later additive work may separately decide whether this object should become schema, storage, or something richer.

This file exists to stop lineage from living only in atmosphere and memory, without pretending continuity is now solved.
