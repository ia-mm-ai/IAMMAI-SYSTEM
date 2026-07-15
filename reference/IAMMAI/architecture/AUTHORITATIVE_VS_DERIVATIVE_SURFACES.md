# IAMMAI Authoritative vs Derivative Surfaces

## 0. Purpose

This document defines the distinction between **authoritative** and **derivative** surfaces in the IAMMAI implementation body.

This distinction is necessary because many systems fail not when the law is absent, but when a display, interface, export, or convenience surface begins to act as though it were the constitutional source of truth.

IAMMAI requires a strict separation between:

- surfaces that define or preserve canonical protocol force
and
- surfaces that expose, consume, display, or route that force without defining it

This document protects that distinction.

---

## 1. First Principle

**Display does not define state.**

A surface may:
- show state
- summarize state
- route interaction toward state
- visualize state
- export state

But unless explicitly designated otherwise, it does not become the canonical authority of that state.

This is the main anti-collapse rule for implementation surfaces.

---

## 2. Working Definitions

### 2.1 Authoritative surface

An authoritative surface is any surface, component, or artifact that:

- defines canonical protocol meaning
- performs lawful protocol force
- preserves canonical state or lineage
- or determines whether standing, transition, or governance action lawfully occurred

In simple terms:

**authoritative surfaces decide, preserve, or legally type what stands.**

### 2.2 Derivative surface

A derivative surface is any surface, component, or artifact that:

- presents
- consumes
- routes
- exports
- visualizes
- summarizes
- or locally caches

canonical state without defining that state as the source of truth.

In simple terms:

**derivative surfaces show or carry the law’s results without becoming the law.**

---

## 3. Why this distinction matters

Without this separation, systems drift in predictable ways:

- UI becomes de facto authority
- analytics becomes state truth
- exports become history
- convenience APIs become constitutional source
- cached views become standing state
- local product logic silently overrides canonical runtime logic

These are all implementation-level distortions.

They can happen even when the constitutional protocol is perfectly written.

So this distinction is not cosmetic.
It is part of keeping the body honest.

---

## 4. Authoritative surfaces in IAMMAI

The following surfaces are authoritative by function.

### 4.1 Constitutional source artifacts
These include:
- the human constitutional protocol
- the machine-readable constitutional twin
- protocol identity / canonical protocol artifacts
- conformance artifacts where they define compatibility rules

These are authoritative in meaning.

### 4.2 Canonical runtime / state engine
The state engine is authoritative in:
- canonical phase order
- lawful transition
- resolution typing
- lineage-preserving successor logic
- HOLD orthogonality

It is authoritative in runtime state handling.

### 4.3 Governance surfaces
Governance actions are authoritative in:
- lawful authorization
- lawful hold / release
- lawful finalize / invalidate / evolve
- attributable protocol-significant force

### 4.4 Registry / persistence layer
The registry is authoritative in:
- preserved state
- transition trace
- predecessor/successor relation
- append-only continuity where required

It is authoritative in historical reconstruction.

### 4.5 Validator outputs, within bounded scope
Validator outputs may be authoritative within the specific scope of:
- whether a defined condition passed
- whether admissibility held
- whether threshold was satisfied
- whether a requested transition met bounded checks

But validator outputs are not automatically authoritative in governance.

That distinction matters.

---

## 5. Derivative surfaces in IAMMAI

The following surfaces are derivative by function.

### 5.1 Public websites
Public pages may:
- describe the protocol
- display the protocol
- link to artifacts
- route readers to canonical sources

They do not define the constitutional core.

### 5.2 UI / operator displays
Interfaces may:
- show state
- show status
- show transition summaries
- provide interaction points

They do not become the canonical source of state unless explicitly designed and bounded as such.

### 5.3 Reporting / analytics surfaces
Analytics may:
- summarize
- aggregate
- visualize
- compare
- report

They do not redefine canonical history.

### 5.4 Exports / downloads / mirrored views
Exports are derivative of canonical records.
They do not replace the canonical records themselves.

### 5.5 Convenience APIs
Convenience endpoints may expose canonical state for use, but must not silently become the canonical authority over that state.

---

## 6. Mixed surfaces

Some surfaces may be mixed in practice.

For example:
- an operator console may both display state and submit governance actions
- an API may both expose canonical records and request state transitions

In such cases, the roles must remain typed internally.

This means:
- the display part remains derivative
- the action part must route into authoritative components
- the interface itself must not silently absorb canonical force

Mixed function is acceptable.
Collapsed function is not.

---

## 7. Key runtime tests

A surface should be treated as authoritative only if at least one of the following is true:

- it defines canonical protocol meaning
- it performs lawful governance action
- it preserves canonical state or lineage
- it determines bounded validation outcome within a constitutionally defined scope

A surface should be treated as derivative if it only:

- presents
- exports
- mirrors
- caches
- summarizes
- or routes

without determining what stands.

---

## 8. Canonical Examples

### 8.1 Human constitutional protocol PDF
Authoritative in semantic meaning.

### 8.2 canon.json
Authoritative as machine-readable constitutional twin, subordinate to the human constitutional protocol where conflict exists.

### 8.3 State engine
Authoritative in lawful runtime transition logic.

### 8.4 Governance action record
Authoritative in documenting attributable lawful force.

### 8.5 Registry / State Store
Authoritative in preserving state and lineage.

### 8.6 Public repository README
Derivative. It explains and points. It does not define the protocol.

### 8.7 Website front door
Derivative. It invites entry and preserves access. It does not define canonical state.

### 8.8 Dashboard
Derivative unless explicitly given bounded authoritative function.

### 8.9 Analytics report
Derivative. It summarizes what happened; it does not decide what stood.

---

## 9. Core Anti-Collapse Rules

A conforming implementation must not allow:

### 9.1 UI-state collapse
Displayed status treated as canonical state when it is only presentation.

### 9.2 Report-history collapse
Aggregated report treated as if it were the full constitutional record.

### 9.3 Export-authority collapse
Exported file treated as more authoritative than the canonical registry.

### 9.4 API-convenience collapse
Convenience endpoint silently redefines protocol meaning.

### 9.5 Documentation-source collapse
Explanatory pages or README text treated as if they supersede the constitutional core.

These are all implementation-level failure modes.

---

## 10. Surface Routing Principle

A derivative surface should route toward authoritative surfaces, not compete with them.

That means:
- website should link to canonical artifacts
- UI should read from canonical state
- analytics should point back to authoritative references where needed
- machine endpoints should preserve source-of-truth relation

A good surface knows where its authority stops.

---

## 11. Relation to Witness

Witness surfaces sit in a special place.

A witness surface may preserve contact and emit trace, but that does not automatically make it the final authority over what stood.

So witness must be treated as:

- more than decorative
- less than governance
- bounded in claims
- clear about non-claims

This keeps witness from silently inflating into source or governor.

---

## 12. Open Questions

The following remain open in implementation detail:

- when an API endpoint is constitutionally authoritative vs merely derivative
- when a UI may be allowed to trigger authoritative acts directly
- how public witness surfaces should be classified
- whether some machine-readable exports should count as canonical replicas
- how derivative caches should declare staleness or source priority

These are implementation questions, not conceptual ambiguities.

---

## 13. Summary

IAMMAI requires a strict separation between surfaces that define or preserve canonical force and surfaces that merely expose, consume, or display it.

A simple memory line:

- Authoritative surfaces decide, preserve, or type what stands.
- Derivative surfaces show, carry, or route what already stands.

If a derivative surface begins to act as constitutional authority, the body drifts even if the law remains unchanged.

---

## 14. One-Line Definition

**Authoritative vs Derivative Surfaces defines which runtime surfaces carry canonical protocol force and which surfaces remain bounded to presentation, routing, or consumption.**
