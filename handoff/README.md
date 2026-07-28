# DeuteronWigner hand-off notes

This directory is the durable project memory for the DeuteronWigner work. It is intended to make
the scientific assumptions, implementation state, validation results, and unresolved questions
recoverable without relying on conversation history.

## Contents

- `project_context.md` - current understanding of the scientific goal and architecture.
- `ROADMAP.md` - authoritative executable plan, status, gates, defects, and next action.
- `references/neff_feldmeier_2016.md` - detailed reading notes on the deuteron
  Wigner/SRC reference.
- `decisions.md` - convention and design decisions, including their rationale and consequences.
- `worklog.md` - chronological record of implementation and verification work.
- `../references/model_construction_note.tex` - authoritative scientific
  construction history and complete inventory of the accepted pre-evolution
  model; its rendered edition is
  `../output/pdf/model_construction_note.pdf`.
- `../references/algebraic_geometric_next_level_model_note.tex` - standalone
  research note proposing a physically constrained algebraic/geometric
  architecture for WP13; its rendered edition is
  `../output/pdf/algebraic_geometric_next_level_model_note.pdf`.

## Update policy

For every material unit of work:

1. Record implemented behavior and affected files in `worklog.md`.
2. Record tests run and their results, including numerical tolerances.
3. Add any convention or architecture choice to `decisions.md`.
4. Preserve unresolved issues explicitly; do not silently replace them with assumptions.
5. Keep equations tied to equation or section numbers in `Deuteron_GTMD.pdf` when possible.
6. Before handoff or context compaction, update `ROADMAP.md` with the exact
   next command, current defects, tests, and changed files.

The root `AGENTS.md` is the mandatory discovery entry point for future
sessions. The reduced-amplitude complete-TMD outputs are superseded; see the
architecture audit referenced there.

Generated files, temporary PDF renders, and scratch calculations do not belong here.
