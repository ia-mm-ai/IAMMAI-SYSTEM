# IAMMAI v1 Validation and Conformance Rules

## 1. Purpose

This file defines the v1 runtime-level conformance posture that follows the canonical body-schema round and precedes emitter updates and continuity-specific re-derivation.

Its job is to state how conformance is evaluated across canonical artifact body, envelope-bearing emission, and registry or preservation context without collapsing those layers into one validation surface.

It does not define:

- a constitutional rewrite
- a seam declaration
- an authority or inheritance map
- an artifact-boundary decision
- a schema file
- an envelope schema
- an emitter implementation plan
- a continuity redesign
- a runtime flow map
- a validator code patch

It is a bounded runtime contract.

## 2. Why This File Is Needed Now

The canonical body-schema round is now present in v1.

V1 now has canonical body schemas for:

- validation artifact
- witness artifact
- governance action
- transition record
- state record

That changes the runtime posture. Conformance law must now distinguish body, envelope, and preservation layers before emitter work proceeds.

Body-schema completion does not yet settle continuity. It gives v1 a lawful canonical-body baseline. It does not by itself determine how combined emission should be validated, how preserved artifacts should be judged in placement context, or how continuity-turn should later be re-derived under the new line.

## 3. First Principle

Conformance must evaluate what is actually being claimed.

Canonical body, envelope-bearing emission, and preservation context are distinct conformance surfaces.  
No combined emission may pass as canonical body merely because the body is embedded inside it.

In v1 terms, the validation target must remain explicit. A body claim should be checked as body. An envelope-bearing claim should be checked as envelope-bearing emission. A preservation claim should be checked as preservation posture. These are related, but they are not interchangeable.

## 4. Conformance Surfaces

This contract distinguishes three bounded conformance surfaces:

- canonical artifact body conformance
- envelope-bearing emission conformance
- registry or preservation conformance

Canonical artifact body conformance is responsible for whether the artifact body, as artifact, conforms to the v1 canonical body law and the relevant canonical body schema.

Envelope-bearing emission conformance is responsible for whether a carried emission that includes body and envelope preserves explicit body or envelope separability without flattening them into one undifferentiated emitted shape.

Registry or preservation conformance is responsible for whether preserved placement, receipt, retrieval, and typed preservation posture remain lawful without silently redefining canonical artifact meaning.

These surfaces may relate in one runtime path. They must still remain distinguishable in conformance posture.

## 5. Canonical Body Conformance

Body schemas validate canonical body only.

Canonical body conformance therefore asks whether a validation artifact body, witness artifact body, governance action body, transition record body, or state record body conforms as canonical body.

Body conformance does not validate envelope content, runtime packaging, receipt posture, or preservation placement. Passing body schema does not by itself prove lawful transport, lawful preservation, or lawful runtime packaging.

Body conformance is the first bounded conformance surface, not the whole runtime answer.

## 6. Envelope-Bearing Emission Conformance

Where body and envelope travel together, conformance must preserve explicit body or envelope separability.

A combined emission must not flatten body and envelope into one undifferentiated validation target. It is lawful for body and envelope to travel together. It is not lawful for their distinction to disappear because a runtime emitter found a simpler emitted shape convenient.

Envelope-bearing conformance is downstream of body conformance, not a substitute for it. A combined emission may therefore contain a canonical body that conforms while the combined emission still fails envelope-bearing conformance because the body or envelope distinction was not preserved explicitly enough.

## 7. Registry and Preservation Conformance

Preservation placement, receipt, or retrieval context may also need conformance.

Registry or preservation conformance asks whether preserved artifacts remain typed, reconstructable, retrievable, and non-collapsed in authoritative preservation context.

Preservation conformance must not silently redefine canonical artifact law. A preserved artifact is not a different artifact merely because preservation context exists. Preservation may add bounded context around an artifact. It must not rewrite what the canonical artifact body is.

## 8. Fixture and Failure Posture

Positive fixtures should demonstrate expected lawful conformance on the surface they claim to exercise.

Negative fixtures may demonstrate bounded failure. Refusal-path fixtures may fail intentionally and lawfully. Illegibility fixtures and conformance-failure fixtures may also fail intentionally and lawfully where their purpose is to show that a boundary holds.

Failure must therefore be read by layer:

- body failure
- envelope failure
- preservation failure
- deliberate refusal-path failure

Fixture failure must not automatically be read as architectural incoherence. A deliberately broken fixture or lawful refusal-path artifact is not the same thing as accidental downstream drift. Fixture class and conformance surface must both remain explicit.

## 9. Continuity Boundary

Continuity-turn remains a special case under the current v1 line.

This file does not settle final continuity conformance. Continuity remains entangled with execution occurrence more directly than the current canonical body-schema round has yet fully resolved.

Continuity must not silently bypass these conformance distinctions by preserving old run-saturated posture under cleaner wording. If continuity later preserves execution-occurrence relation, that relation must still respect the v1 separation between canonical body, envelope-bearing emission, and preservation context.

## 10. Anti-Collapse Rules

A conforming v1 posture must not allow:

- treating combined emission as canonical body by convenience
- treating preservation placement as canonical law
- validator posture that collapses body, envelope, and preservation into one undifferentiated pass or fail
- fixture interpretation that confuses lawful refusal-path failure with accidental drift
- continuity shortcut that bypasses unresolved execution-occurrence questions

It must also not allow one surface to borrow legitimacy from another surface without explicit conformance relation. Body conformance is not automatic emission conformance. Emission conformance is not automatic preservation conformance.

## 11. Downstream Consequences

Emitter updates must later conform to these rules.

Later runtime flow mapping must conform to these rules. Later continuity handling must conform to these rules where applicable.

This file is therefore a runtime contract bridge, not a substitute for later implementation work. Schema work has already defined the canonical body baseline. Emitter and runtime updates must now follow that baseline rather than silently redefining it.

## 12. Closing Boundary Statement

This file defines conformance posture only.

Later files may implement these rules in emitter, validator, and continuity-specific surfaces. This file exists so v1 can move from body schemas toward lawful runtime behavior without re-collapsing body, envelope, and preservation context.
