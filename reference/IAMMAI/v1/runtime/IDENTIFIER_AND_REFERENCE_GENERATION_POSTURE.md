# IAMMAI v1 Identifier and Reference Generation Posture

## 1. Purpose

This file defines the bounded v1 generation posture for identifiers and references.

Its job is to state how identifiers and references are to be generated or assigned across canonical artifact bodies, continuity turns, matter relations, explicit execution or envelope relations, and preservation context without silently re-importing the old v0 run-centric posture through generation convenience.

It does not define:

- a constitutional rewrite
- a seam declaration
- an authority or inheritance map
- an artifact-boundary decision
- a schema file
- an emitter implementation patch
- a validator code note
- a storage topology design
- a project-management roadmap
- a README

It is a bounded generation-posture document.

## 2. Why This File Is Needed Now

V1 identity and reference law is now explicit.

V1 schemas deliberately avoid run-saturated canonical bodies. The canonical body schemas for ordinary artifacts and continuity turn exclude `run_id` from canonical body shape, and the surrounding v1 runtime and preservation law now distinguishes body, execution relation, and preservation context at contract level.

Implementation now needs generation posture before code hardens convenience into drift. V1 cannot remove `run_id` from canonical bodies while still generating canonical-seeming identifiers and references by default from execution occurrence.

Exact final string syntax remains intentionally bounded here rather than prematurely frozen. What must now be settled is the lawful generation posture, not final formatting detail.

## 3. First Principle

Generation must generate what actually stands.

Generation must preserve identity class and reference class distinction.  
No later carrying or preservation layer may silently redefine earlier identity through generation convenience.

In v1 terms, identifiers are to be generated or assigned for the bounded thing that stands as artifact, continuity turn, matter, execution occurrence, or preservation placement. References are to be generated or assigned according to the lawful relation that actually holds between those things, not according to whichever label is easiest to derive from a runtime path.

## 4. Identity Generation Classes

This generation posture distinguishes the following bounded identity-generation classes:

- canonical artifact identity generation
- continuity turn identity generation
- matter identity generation
- execution identity generation
- preservation identity generation

Canonical artifact identity generation generates or assigns identity for a canonical artifact body as artifact. It follows canonical artifact standing and must not be derived by default from execution occurrence.

Continuity turn identity generation generates or assigns identity for the continuity turn as continuity artifact. It remains a canonical continuity identity even where continuity later carries explicit execution relation.

Matter identity generation generates or assigns identity for the bounded matter to which canonical artifacts or continuity may lawfully relate.

Execution identity generation generates or assigns identity for execution occurrence where execution relation must remain explicit.

Preservation identity generation generates or assigns identity for preservation placement, preserved grouping, or retrieval-bearing context where such identity is needed for reconstructability.

These identity classes are related but non-equivalent. V1 requires the class distinction to be preserved even where later implementation chooses compact string forms.

## 5. Canonical Artifact and Continuity Generation

Canonical artifact identities must not be run-saturated by default.

That means canonical artifact identity generation must not treat execution identity as the ordinary source of artifact identity merely because the root line historically generated artifact ids from run occurrence and propagated that occurrence across validation, witness, governance, transition, and state outputs.

Continuity turn identities must not use execution occurrence as default continuity identity. Continuity remains more entangled with execution occurrence than the five ordinary canonical body families, but that relation does not authorize continuity identity generation to collapse into execution identity generation.

Continuity identity must remain continuity identity even where continuity later carries explicit execution relation. If continuity later travels with explicit execution relation, the carried relation remains relation. It does not become the default generator of continuity identity.

## 6. Matter / Execution / Preservation Generation

Matter identity generation must remain distinct from artifact identity generation.

Matter identity may be generated or assigned independently and then referenced by canonical artifacts or continuity where matter relation is part of standing. It must not be treated as a substitute for artifact identity, continuity identity, or preservation identity.

Execution identity generation may remain explicit where lawful. It may identify bounded runtime occurrence and may later support explicit execution-relation references where that relation is actually needed.

Preservation identity generation may support retrieval and reconstructability. It may identify preserved placement, preserved grouping, or read surface where preservation context itself needs to be referable.

None of these identity-generation classes may silently stand in for one another. Matter identity is not artifact identity. Execution identity is not continuity identity. Preservation identity is not canonical identity.

## 7. Reference Generation Posture

Reference generation must follow lawful relation rather than convenience naming.

This generation posture distinguishes the following bounded reference-generation classes:

- canonical artifact references point to canonical artifact identities
- matter references point to matter identities
- predecessor continuity references point to prior lawful continuity turn identities
- explicit execution references point to execution identities only where execution relation must remain explicit
- preservation or context references point to preservation or context identities where relevant

Canonical artifact references are generated or assigned to preserve lawful artifact-to-artifact relation. They must not silently point to execution identity or preservation identity merely because those surfaces were easier to name at generation time.

Matter references are generated or assigned to preserve bounded matter relation.

Predecessor continuity references are generated or assigned to preserve append-oriented lawful succession across continuity turns.

Explicit execution references are generated or assigned only where execution relation must remain explicit as execution relation.

Preservation or context references are generated or assigned where preserved placement or retrieval-bearing context itself needs referential visibility without claiming canonical standing.

No reference class may be generated as a disguised stand-in for another class.

## 8. Anchor and Predecessor Generation Distinction

Canonical artifact anchoring and predecessor succession are different relations.

Canonical artifact anchoring keeps continuity subordinate to preserved canonical reality by linking continuity to the preserved canonical artifacts that actually anchor the continuity turn.

Predecessor succession may support append-oriented continuity by making lawful succession explicit across continuity turns.

Predecessor generation must not silently replace canonical artifact anchoring. A generated predecessor reference is not, by itself, a lawful substitute for generated canonical artifact anchor references where continuity standing still depends on preserved canonical reality.

Continuity must therefore remain subordinate to preserved canonical reality rather than to generic sequence, generic memory, or generic event accumulation.

## 9. Current-v0 / Desired-v1 Distinction

Current root identifier and reference generation posture remains historically real v0 lineage.

V0 generation behavior was strongly run-centric. The root line commonly generated artifact and continuity identifiers from run identity and then propagated that occurrence through related references and preservation reading.

V1 generation posture must therefore be stated explicitly rather than silently inherited from that convenience path. This is not blame language. It is the explicit statement that later implementation cannot claim v1 closure while still letting execution-first generation define canonical artifact identity under cleaner wording.

## 10. Anti-Collapse Rules

A conforming v1 posture must not allow:

- run-centric identifier generation standing in for canonical artifact identity
- predecessor-only generation posture that severs continuity from canonical artifact anchoring
- preservation handle generation pretending to be artifact identity
- execution handle generation pretending to be canonical reference
- grouped retrieval surface erasing reference-class distinctions through generated naming convenience

It must also not allow continuity and ordinary artifacts to collapse into one undifferentiated generation surface merely because both later participate in preserved relation.

## 11. Downstream Consequences

Later emitter re-derivation must follow this generation posture.

Later preservation implementation must follow this posture. Later fixture generation and retrieval must remain readable through this posture.

This file is the last bounded bridge before concrete implementation work. It requires later implementation surfaces to generate identities and references in ways that preserve class distinction, lawful relation, and layer readability rather than quietly re-importing v0 collapse patterns through naming convenience.

## 12. Closing Boundary Statement

This file defines bounded v1 identifier and reference generation posture only.

Later files or implementation work may realize this posture in emitter and preservation surfaces. This file exists so v1 can move into implementation without re-importing v0 collapse patterns through generation convenience.
