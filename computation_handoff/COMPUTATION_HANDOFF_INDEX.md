# Computation Handoff Index

Generated 2026-09-02 to support independent technical review and continued
development. The live continuation tree is
<https://github.com/uva-spin/DeuteronWigner/tree/main/computation_handoff/repo>.
Its `CURRENT_SOURCE_COMMIT.txt` must identify the accepted `main` commit.

## Recommended reading order

1. `README.md` — project purpose, scientific scope, installation, and layout.
2. `handoff/README.md` — durable handoff orientation and governing principles.
3. `handoff/project_context.md` — architecture, normalization anchors, and
   acceptance expectations.
4. `handoff/ROADMAP.md` — authoritative execution queue and current blocker/
   continuation history. The working-tree version is included, including its
   current unstaged modifications.
5. `handoff/quantum_backend_q0_q2_freeze.md` — frozen Q0/Q1/Q2 boundary and
   nonclaims. Q2's separate worktree is not present in this workspace.
6. `pyproject.toml`, `environment.yml`, and `references/` — runtime and
   scientific provenance details.
7. `docs/next_level/` — machine-readable contracts, manifests, audits,
   implementation reports, prompts, and validation evidence.
8. `C401_C410_REPOSITORY_HANDOFF.md` — current C401-C410 scientific,
   numerical-frontier, normalization, and continuation handoff.

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

The current accepted root checkout is on branch `main` at commit
`51d3919e4660f5709cc7bb94c576c8ec17c9de14` (`Merge C410 C117 I2 retained
aggregation boundary`) with remote
`https://github.com/uva-spin/DeuteronWigner.git`. The archive captures the
working tree as found; it does not imply that the working tree was clean.

After every accepted commit on `main`, refresh the published tree, update its
source-commit marker and handoff evidence, refresh contents/checksum manifests
when needed, verify, commit, and push. The marker identifies the accepted
source commit represented by the published tree; a handoff-only publication
commit may follow it. A stale marker means the public handoff is not current.

## Deliberate exclusions

- `.git/` and the nested worktree pointer files: these contain repository
  internals and absolute local paths, and are not needed for handoff review.
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
light-front Hamiltonian solution. The Q0/Q1 frozen backend is a conditional
finite-basis computational/diagnostic stack, not a physical fit, physical
state, spectrum, hardware execution, TMD observable, or production
phenomenology object. Preserve these distinctions when proposing next steps.
