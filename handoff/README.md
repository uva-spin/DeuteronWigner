# DeuteronWigner hand-off notes

This directory is the durable project memory for the DeuteronWigner work. It is intended to make
the scientific assumptions, implementation state, validation results, and unresolved questions
recoverable without relying on conversation history.

Start with `../AGENTS.md`, then `CURRENT_PROJECT_HANDOFF.md`. The current
handoff is the operational source for status and direction. The older roadmap,
phase handoffs, controller records, and published computation handoff are
historical evidence when they disagree with it.

## Contents

- `CURRENT_PROJECT_HANDOFF.md` - authoritative current status, development
  policy, and science-first direction path.
- `project_context.md` - current understanding of the scientific goal and architecture.
- `ROADMAP.md` - long chronological development history; useful evidence, but
  no longer the sole operational queue.
- `references/neff_feldmeier_2016.md` - detailed reading notes on the deuteron
  Wigner/SRC reference.
- `decisions.md` - convention and design decisions, including their rationale and consequences.
- `worklog.md` - chronological record of implementation and verification work.
- `quantum_backend_q0_q2_freeze.md` - frozen Q0–Q2 PennyLane backend boundary,
  acceptance roots, invariants, evidence, nonclaims, and re-entry checklist.
- `../references/model_construction_note.tex` - authoritative scientific
  construction history and complete inventory of the accepted pre-evolution
  model; its rendered edition is
  `../output/pdf/model_construction_note.pdf`.
- `../references/algebraic_geometric_next_level_model_note.tex` - standalone
  research note proposing a physically constrained algebraic/geometric
  architecture for WP13; its rendered edition is
  `../output/pdf/algebraic_geometric_next_level_model_note.pdf`.
- `../references/DeuteronWigner_complete_theory_note_current.tex` - current
  integrated theory and status note, with its bibliography beside it.

## Update policy

For a normal material scientific unit of work:

1. Implement the derivation, code, or analysis.
2. Run focused direct mathematical or numerical tests.
3. Record a convention decision only when a real convention changes.
4. Update the current handoff with the result and next scientific step.

Do not create phase machinery, generated schema families, checksum forests,
mutation campaigns, or duplicate handoffs by default. Use them only when they
protect a reusable scientific artifact or a release. The exploratory,
validated-model, and physical-claim lanes in `CURRENT_PROJECT_HANDOFF.md`
determine how much evidence is required.

## Public continuation handoff

The public handoff tree is:

<https://github.com/uva-spin/DeuteronWigner/tree/main/computation_handoff/repo>

This is a continuation-facing published snapshot of the canonical checkout at
`/Users/dustin/work/DeuteronWigner`. It currently represents C410, not the
local C411 baseline. Refresh it at a deliberate public milestone. Routine
derivations and exploratory calculations do not need to wait for snapshot
publication or manifest regeneration.

If ordinary Git push cannot fast-forward because the public branch is a
published snapshot with a different history, use an authenticated GitHub Git
Database/API commit based on the current public `main`; never force-push or
rewrite the public branch.

The source checkout, current handoff, and direct scientific evidence remain
authoritative. When the published tree is refreshed, its source marker must
point to the represented commit and its claims must match that milestone.

Generated files, temporary PDF renders, and scratch calculations do not belong here.
