# Operator-Facing Terminal Brief: Bounded Current-State Read V0-Min Spec

## 1. Purpose

This file defines the first bounded operator-facing terminal brief spec for the present `IAMMAI-SYSTEM` repository line.

The bounded current-state vessel line already stands across the original vessel, the v2 successor, and the v3 successor. The next pressure is therefore not another vessel branch. It is one real downstream operator-facing use that can be supported by the vessel line already standing.

This file defines the smallest lawful terminal-brief slice supportable by the current body and vessel line: one shell-owned operator-facing terminal brief rendered from one already-emitted bounded current-state vessel result.

This file does not define:

- a chat product
- a dashboard
- a workflow engine
- a middleware layer
- a broad operator framework
- a new governing surface
- a constitutional rewrite
- a roadmap
- a manifesto

## 2. Status and Rank

This spec ranks below the constitutional and reference authority surfaces under `reference/IAMMAI/`.

It is additive. It does not replace the body, the current executable vessel line, the current-state stack, the tests, or emitted artifacts.

It does not define final governance. It does not make the terminal brief a governing participant. It does not make the brief source, authority, rank, standing, or law.

It is a bounded operator brief spec for the present repo only.

## 3. Why This Spec Is Needed Now

The bounded current-state vessel now stands strongly enough to support one downstream consumer.

That does not justify reopening wide-vessel ambition. It justifies one narrow downstream operator-facing use.

The cleanest first consumer is one bounded operator-facing terminal brief because it is concrete, local, and useful while still preserving shell law, source lineage, and derivative status.

The brief must therefore remain shell-owned and derivative rather than becoming a new authority surface.

## 4. Cleanest First Downstream Use-Case

The cleanest first downstream use-case is:

- one operator-facing terminal brief
- rendered from one successful bounded current-state vessel result
- over the same allowed current-state source family already standing

This is the cleanest first consumer because it:

- gives one real operator-facing use
- is narrow enough to preserve law
- does not widen source family
- does not require new model behavior
- keeps shell law local

In this first slice, the brief is a downstream render over one already-emitted vessel result. It is not a second vessel branch and does not require a new model-owned interpretation layer.

## 5. Allowed Source Result Family

For this first brief slice, the allowed source result family is exactly:

- `openai_api_derivative_vessel_bounded_current_state_read_v3_result`

The corresponding selected result should preserve the v3 vessel result type:

- `IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT`

The selected vessel result must have:

- outcome `ANSWERED_DERIVATIVE_READ`

The upstream allowed source family remains:

- `current_state_what_stands_now_result`

The brief reads one selected vessel result only.

The brief does not:

- read the whole repo
- re-open source-family discovery across the repo
- widen to other vessel families
- widen to other current-state families
- bypass the selected vessel result and read upstream artifacts directly

## 6. Admitted Use Class

The admitted use class for this first brief slice is:

- `OPERATOR_TERMINAL_BRIEF_READ`

`OPERATOR_TERMINAL_BRIEF_READ` means:

- read/render only
- derivative only
- no authority
- no standing assignment
- no provenance reassignment
- no mutation
- no continuation claim
- no orchestration claim

This use class permits one operator-facing brief render from one selected successful vessel result. It does not permit re-resolution, re-ranking, or reinterpretation of the body as law.

## 7. Shell-Owned Contract

The shell / local repo code must own:

- source result selection
- allowed source result family
- brief packet construction
- provenance
- rank
- status
- non-claims
- refusal semantics
- output validation
- result wrapping
- artifact writing

The shell decides whether the selected vessel result is admissible. The shell decides whether the selected vessel result still preserves the upstream `current_state_what_stands_now_result` family. The shell decides whether the brief packet is lawful. The shell decides whether the emitted brief output is within contract.

The shell is the law.

The brief is not.

## 8. What the Terminal Brief Is

In this first slice, the terminal brief is:

- one concise operator-facing derivative rendering
- built from one successful bounded vessel result
- carrying only bounded already-derived information
- preserving source lineage and derivative status

It is not:

- source
- governing law
- a new current-state resolver
- a standing surface
- a recap engine
- whole-body memory
- orchestration

The brief exists to make one already-derived vessel result readable to an operator in terminal form without changing the source rank, the vessel rank, or the body law.

## 9. Input Packet

The shell must construct one bounded brief input packet with this shape:

```text
OperatorTerminalBriefRequest {
  brief_request_id: string
  brief_use_case: "BOUNDED_OPERATOR_FACING_TERMINAL_BRIEF"
  admitted_use_class: "OPERATOR_TERMINAL_BRIEF_READ"
  allowed_source_result_family: "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
  selected_vessel_result_id: string
  selected_vessel_result_path: string
  selected_source_surface_id: string
  question: string
  derivative_answer: string
  brief_instructions: string
}
```

Rules:

- the packet is constructed from one already-emitted vessel result
- `selected_vessel_result_id` and `selected_vessel_result_path` identify the selected v3 vessel result
- `selected_source_surface_id` preserves the upstream `current_state_what_stands_now_result` identity carried by the vessel result
- `question` is the bounded current-state question already preserved by the vessel result
- `derivative_answer` is the already-derived vessel answer, not a new repo read
- `brief_instructions` must state that the brief renders only the selected vessel result, does not widen source scope, and does not assign rank, authority, or standing

The brief packet is constructed from the already-emitted vessel result, not from the whole repo.

## 10. Output / Result Contract

The shell must emit one bounded operator-terminal-brief result artifact with this shape:

```text
OperatorTerminalBriefResult {
  operator_terminal_brief_metadata: {
    brief_result_id: string
    brief_result_type: string
    brief_result_version: string
    generated_at: string
    resolver_module: string
  }
  selected_vessel_result: {
    selected_vessel_result_path: string
    selected_vessel_result_id: string
    selected_vessel_result_family: "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
    selected_vessel_result_outcome: "ANSWERED_DERIVATIVE_READ"
    selected_source_surface_id: string
    selected_source_surface_family: "current_state_what_stands_now_result"
  }
  brief_request: {
    brief_request_id: string
    brief_use_case: "BOUNDED_OPERATOR_FACING_TERMINAL_BRIEF"
    admitted_use_class: "OPERATOR_TERMINAL_BRIEF_READ"
    allowed_source_result_family: "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
    question: string
  }
  brief_output: {
    brief_text: string | null
    brief_basis: "bounded_derivative_vessel_result"
    source_remains_source: true
    vessel_output_remains_derivative: true
    brief_remains_derivative: true
  }
  outcome: "BRIEF_RENDERED" | "REFUSED"
  block: {
    block_code: string | null
    block_reason: string | null
  }
  brief_summary: {
    selected_vessel_result_id: string
    selected_source_surface_id: string
    question: string
    outcome: string
  }
  non_claims: {
    source_replaced: false
    rank_assigned_by_brief: false
    authority_assigned_by_brief: false
    standing_assigned_by_brief: false
    source_scope_widened: false
    continuity_completed: false
  }
}
```

Success outcome:

- `BRIEF_RENDERED`

Refusal outcome:

- `REFUSED`

This contract is additive and non-authoritative. The brief text is derivative only. It does not become source or law by being terminal-facing.

## 11. Refusal / Block Path

The refusal path for this first brief slice must remain explicit and shell-owned.

At minimum, the shell must preserve refusal for:

- `INVALID_SOURCE_RESULT_FAMILY`
- `MISSING_VESSEL_RESULT`
- `VESSEL_RESULT_UNREADABLE`
- `VESSEL_RESULT_MALFORMED`
- `VESSEL_RESULT_NOT_SUCCESSFUL`
- `INVALID_UPSTREAM_SOURCE_FAMILY`
- `WIDENED_SOURCE_ATTEMPT`
- `MALFORMED_BRIEF_PACKET`
- `BRIEF_OUTPUT_OUTSIDE_CONTRACT`

Refusal here means the brief is not lawful to emit from the selected vessel result in this slice. It does not mean that source, vessel, or body law has changed.

Law and refusal semantics remain shell-owned.

## 12. What the Brief Must Not Do

The brief must not:

- assign rank
- assign authority
- assign standing
- widen source scope
- recompute current-state law
- mutate artifacts
- rewrite lineage
- replace source
- claim continuity completion
- become a governance surface
- become a workflow engine

It must also not:

- treat the selected vessel result as source
- treat the brief as a new interpretation-law surface
- hide the upstream `current_state_what_stands_now_result` lineage

## 13. What This First Brief Still Does Not Do

This first brief does not do:

- chat behavior
- dashboards
- orchestration
- multi-source synthesis
- participation claims
- new doctrine
- whole-body summarization
- repo-wide reading
- source-family widening

It is one bounded operator-facing terminal brief only.

## 14. What Should Not Be Added Next

What should probably not happen next:

- no dashboard framework
- no chat shell
- no workflow engine
- no multi-surface synthesis
- no hidden source widening
- no operator mythology
- no brief treated as authority

The repo should not widen one lawful downstream consumer into a product branch.

## 15. Closing Boundary Statement

The bounded current-state vessel now stands strongly enough to support one bounded downstream operator-facing use.

The first lawful downstream consumer is one shell-owned terminal brief rendered from one successful bounded current-state vessel result.

The body remains the law.

The vessel remains derivative.

The brief remains derivative.

This is the smallest lawful downstream operator surface now supportable by the present repo line.
