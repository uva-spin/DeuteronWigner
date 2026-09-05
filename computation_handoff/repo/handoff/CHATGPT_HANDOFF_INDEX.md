# ChatGPT/Codex Handoff Index

Originally generated 2026-08-28 and reconciled through 2026-09-04 for
technical direction and repository-connected development.

The archive inventory below describes the 2026-08-28 transfer. For current
work, `AGENTS.md` and `handoff/CURRENT_PROJECT_HANDOFF.md` take precedence.

## Recommended reading order

1. `AGENTS.md` — startup rules and science-first workflow.
2. `handoff/CURRENT_PROJECT_HANDOFF.md` — current status and direction path.
3. `references/DeuteronWigner_complete_theory_note_current.tex` — integrated
   mathematical, physical, and status note.
4. `README.md` and `handoff/project_context.md` — project purpose,
   architecture, normalization anchors, and acceptance expectations.
5. `handoff/quantum_backend_q0_q2_freeze.md` — frozen Q0/Q1/Q2 boundary and
   nonclaims.
6. `handoff/ROADMAP.md`, `handoff/decisions.md`, and `handoff/worklog.md` —
   chronological history, consulted as needed rather than reread before every
   task.
7. `pyproject.toml`, `environment.yml`, and `references/` — runtime and
   scientific provenance details.
8. Relevant `docs/phases/` and `docs/next_level/` records — detailed
   contracts, manifests, audits, implementation reports, prompts, and
   validation evidence.

## Archive scope

The archive contains:

- the current root checkout's Git-tracked source, tests, scripts, references,
  validation manifests, project documentation, tracked data, and selected
  tracked output artifacts;
- current root handoff additions and the current untracked C157 validation
  test and progress/evidence documents;
- the tracked contents of `deuteron_wigner_q0_plhqcd0/` and
  `deuteron_wigner_q1_plhqcdstate/`, preserving their frozen backend source,
  tests, reports, prompts, and acceptance records;
- `MSHT20_REP/MSHT20_REP.info`, the metadata for the locally transferred
  replica source explicitly referenced by the project and its handoff records;
- `PennyLaneBackend/requirements.txt` and its `.gitignore` (the directory has
  no backend source outside its local virtual environment);
- this index and the root `Deuteron_GTMD.pdf` project document.

The archived root checkout was on branch `main` at commit `6ef9827e` (`C399
certify missing physical target authority`). The current represented source
milestone is `e86b6c3fd664817b0d955ec076bbe6c201747ab2`, which commits the
reviewed C411/M2 state-current boundary. The 2026-08-28 archive captures the
earlier working tree as found; it does not describe current development status
and does not imply that the working tree was clean.

## Deliberate exclusions

- `.git/` and the nested worktree pointer files: these contain repository
  internals and absolute local paths, and are not needed for ChatGPT review.
- Conda environments (`.conda-*`), Python virtual environments (`.venv*`,
  `venv`), compiled libraries, caches, bytecode, and package build products.
- Ignored bulk/generated trees such as the workspace's untracked `data/`,
  `outputs/`, and generated runtime products. Tracked manifests, small
  authority payloads, benchmark data, and selected tracked outputs remain.
- The roughly 845 MB raw `MSHT20_REP_*.dat` replica grid is omitted to keep
  this ZIP below 512 MB; the metadata and the project's source locks,
  provenance, acquisition notes, and validation code remain.
- Unrelated loose PDFs and temporary files that are ignored by the project's
  publication/data policy, except for the project-level `Deuteron_GTMD.pdf`.

The `MSHT20_REP` metadata is included for private project review because the
handoff identifies the dataset as a protected direct-author transfer. Its
source permission status is not inferred by this archive; do not publicly
redistribute the replica payload without confirming authorization.

## Important interpretation boundary

The project is a correlator-level, phenomenologically constrained boundary
model and validation framework. It is not yet a single common regulated
light-front Hamiltonian solution. The Q0/Q1/Q2 frozen backend is a conditional
finite-basis computational/diagnostic stack, not a physical fit, physical
state, spectrum, hardware execution, TMD observable, or production
phenomenology object. Preserve these distinctions when proposing next steps.
