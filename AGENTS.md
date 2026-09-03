# DeuteronWigner agent entry point

Read `handoff/CURRENT_PROJECT_HANDOFF.md` before changing code, scientific
documents, phase records, or generated products. It is the current project
status and direction path. Then read the status chapter of
`references/DeuteronWigner_complete_theory_note_current.tex` when the task
touches physics or conventions.

## Source of truth

Use this order when records disagree:

1. the user's current request;
2. the checked-out source, direct mathematical tests, and current Git history;
3. `handoff/CURRENT_PROJECT_HANDOFF.md`;
4. the complete theory note and current phase implementation reports;
5. historical roadmaps, generated manifests, archived handoffs, and controller
   state.

The `.yolo/` C399/C400 controller state and the published
`computation_handoff/repo/` C410 snapshot are historical. They are not the
current development authority. Never restart an old controller automatically.

## Working policy: scientific progress first

Use three clearly labeled lanes:

- **Exploratory:** explicit assumptions and provisional conventions are
  allowed so that derivations, numerical experiments, and sensitivity studies
  can proceed. Do not present the outputs as physical predictions.
- **Validated model:** require coherent equations, units, direct tests, and
  documented assumptions. External provenance is required for inputs that
  materially control the result, but a publication-grade evidence package is
  not a prerequisite for ordinary model development.
- **Physical claim:** require source-qualified inputs, convention ownership,
  uncertainty/covariance treatment, resolution checks, and a reproducible
  end-to-end calculation.

Fail closed only at the boundary between these lanes. A missing physical input
blocks a physical claim; it does not automatically block an exploratory or
validated-model calculation.

Avoid new phase numbers, schema forests, checksum ledgers, mutation campaigns,
or duplicate handoffs unless they protect a concrete scientific result. A
normal scientific change usually needs only the implementation, focused direct
tests, a short explanation, and an update to the current handoff.

## Repository conduct

- Preserve unrelated tracked and untracked user work. Do not clean or reset the
  worktree.
- Prefer focused tests that exercise equations, numerical behavior, and
  scientific limits. Do not use test counts as physics evidence.
- Keep quark/gluon operators, proton/neutron and flavor labels, target spin,
  gauge links, nuclear mechanisms, and uncertainty members resolved until the
  declared composition step.
- Missing information is not a physical zero. In exploratory work it may be an
  explicit parameter or sensitivity range.
- Do not select a production current, physical state, fit, response rank, or
  activation status by software default.
- Do not push or publish unless the user asks.

## Immediate direction

The next scientific sprint is the C117 first-direction normalization and K9
response calculation described in `handoff/CURRENT_PROJECT_HANDOFF.md`. Start
from the actual source conventions and derive as much of the finite-cell
adapter as possible. Treat the existing C411 certificate API as a guardrail,
not as proof that an externally supplied 4-by-4 certificate is the only lawful
route.
