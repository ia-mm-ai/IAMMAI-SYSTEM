# IAMMAI Governance Action Overview

## 1. Purpose

This file defines the first high-level governance action model of IAMMAI in implementation-facing form.

It translates the constitutional core and the current architecture and implementation documents into a bounded view of what governance action is, what a governance action record preserves, and how governance remains distinct from witness, validation, and semantic source.

It does not yet try to define:
- code
- a final schema
- the full governance constitution
- a final authority system design
- identity infrastructure
- service topology

It is implementation-neutral and grants no conceptual or semantic privilege to any private implementation.

## 2. First Principle

Governance action is lawful protocol force.

Governance action must remain:
- attributable
- legitimacy-bounded
- matter-scoped

Governance action must not become semantic source.

The constitutional core remains the source of meaning. Governance acts may authorize, deny, hold, release, finalize, invalidate, or evolve within lawful bounds, but they do not redefine constitutional meaning by prestige, access, or implementation convenience.

## 3. Why Governance Action Records Are Needed

Protocol-significant action must not appear as ambient mutation.

- If a protocol-significant act appears only as a changed state, the implementation cannot show who acted, under what basis, or within what scope.
- Attributable action matters because lawful force must remain traceable to a bounded actor or authority node.
- Legitimacy basis matters because actor identity alone does not explain why the act counted as lawful protocol force.
- Governance records protect against anonymous force, scope bleed, and later reinterpretation of a mutation as though it had always been authorized.

Governance action therefore needs its own reconstructable record family.

## 4. What Governance Action Is

In implementation terms, governance action is:

- an attributable protocol-significant act
- bounded by authority class
- bounded by legitimacy basis
- bounded by matter relation
- preserved as reconstructable record

Governance action is not:

- semantic source
- witness by default
- validation by default
- authorship by default

Governance action is the runtime location of lawful force. It answers what action may lawfully be performed or recognized within bounded authority.

## 5. What a Governance Action Record Preserves

At a high level, a governance action record should preserve:

- governance action id
- action type
- authority class
- actor ref
- legitimacy basis ref
- matter ref
- optional delegation relation
- optional target state refs
- optional target transition refs
- acted_at

This is a conceptual record shape, not a final schema.

The implementation point is that a governance action record should preserve enough typed trace to reconstruct what act occurred, who performed or authorized it, on what basis, on what matter, against what target where relevant, and when it occurred.

## 6. Governance Action Types

A first bounded family of governance-significant actions includes actions functionally equivalent to:

### 6.1 Authorize

Preserves that a bounded act was lawfully authorized within scope.

### 6.2 Deny

Preserves that a bounded requested act was not authorized within scope.

### 6.3 Hold

Preserves application of HOLD to prevent an otherwise eligible irreversible transition from proceeding.

### 6.4 Release

Preserves release of prior containment so permissibility may be restored.

### 6.5 Finalize

Preserves lawful closure in current form.

### 6.6 Invalidate

Preserves removal of standing without erasing trace.

### 6.7 Evolve

Preserves lawful successor creation in explicit relation to prior state.

This family is intentionally bounded. It is enough for the first implementation body without expanding into a full governance taxonomy.

## 7. Authority Class and Legitimacy Basis

Authority class and legitimacy basis must remain distinct.

- Authority class answers what kind of authority is being exercised.
- Legitimacy basis answers on what lawful basis that authority counts in the specific act.

Access or visibility alone do not count as authority.

Governance action must therefore preserve more than actor identity. A conforming implementation must preserve the basis under which the act was treated as lawful, not merely the fact that an actor performed it.

Without that distinction, governance collapses into untyped power.

## 8. Governance vs Witness

Governance applies lawful force.  
Witness preserves contact.

A governance event may be witnessed, and witness may preserve that the act occurred, but governance does not become witness simply by acting.

Likewise, witness does not become governance by preserving a governance event.

These roles remain distinct:
- governance performs or authorizes protocol-significant action
- witness preserves trace of occurrence

## 9. Governance vs Validation

Validation checks conditions.  
Governance decides or performs lawful action.

Validation may determine whether bounded conditions hold, including transition legality or threshold alignment, but passed validation does not automatically imply authorization.

Governance remains a separate force-bearing role:
- validation checks
- governance acts

This distinction prevents checked condition from silently turning into lawful force.

## 10. Governance and Delegation

Delegation extends action without erasing attribution.

- Delegated action must remain traceable to its source relation.
- Delegation must preserve who delegated, to whom, for what act class or scope, and in relation to what matter where relevant.
- Delegated action must still remain bounded by authority and legitimacy.

Delegation is therefore a traceability requirement, not a shortcut for losing source relation.

## 11. Governance and Matter Scope

Authority must remain matter-bounded.

Governance action must not silently bleed across matters. An actor authorized for one matter, or one act in one matter, is not thereby authorized for another matter by convenience or similarity.

Matter relation is therefore a mandatory implementation concern. Governance action records must preserve what bounded matter the act applied to.

## 12. Anti-Collapse Rules

A conforming implementation must not allow:

- anonymous governance force
- governance to be treated as semantic source
- governance to be treated as authorship by default
- passed validation to be treated as automatic governance
- delegation to erase source relation
- governance action to be stored without legitimacy basis
- scope bleed across matters
- governance mutation to appear without attributable actor or authority class
- governance history to be rewritten by convenience

## 13. Open Questions

The following remain open in technical derivation:

- the final governance action envelope
- the exact representation of delegation relation in runtime artifacts
- whether some governance surfaces are purely human-bounded or partially machine-assisted
- how target state and transition references are represented where acts are scoped to both
- how legitimacy basis references are linked to supporting artifacts

These are implementation questions, not constitutional ambiguities.

## 14. Summary

This document defines the first implementation-facing governance action model of IAMMAI as a bounded record model for attributable lawful force.

Its purpose is to keep protocol-significant action reconstructable by actor, basis, scope, target, and time without collapsing governance into witness, validation, or semantic source.

**One-Line Definition:** `GOVERNANCE_ACTION_OVERVIEW.md` defines the first high-level implementation view of IAMMAI governance action as attributable, legitimacy-bounded, matter-scoped protocol force preserved in typed reconstructable form.
