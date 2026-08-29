# Classical Phase-Package Policy from C391 to the PennyLane Handoff

## Scope

This policy begins after the accepted C390 checkpoint and remains active
through the last accepted classical physical-state/observable and
classical-to-Q0/Q1/Q2 handoff package.

It ends when an exact continuation contract authorizes the first physical
PennyLane package.

## Package boundary

A top-level C package represents a coherent scientific phase, not one
technical substep.

Create a new top-level package only at an authority discontinuity:

```text
new authenticated external source;
new renormalization or matching scheme;
new physical input or boundary ensemble;
new operator or Hilbert-space sector;
new classical-to-quantum interface;
a certified mathematical/physical blocker;
or a final accepted physical object.
```

Do not split a phase merely because it requires:

```text
additional distributional kernels;
larger scans;
several Laurent orders;
regular/plus decomposition;
real/virtual cancellation;
separator checks;
finite-remainder extraction;
covariance propagation;
resolution holdouts;
fit-window or regulator variants;
or more tests of the same scientific object.
```

## Internal stage records

Every phase contains ordered stage records with:

```text
stage ID;
first exact object;
input roots;
allowed derivation/evaluation routes;
status;
scientific result or exact blocker;
unresolved remainder;
output root;
validation root;
and next internal stage.
```

Internal stages are checkpointed externally under:

```text
/Users/dustin/work/DeuteronWigner-yolo/state/phases/<phase-id>/
```

They are not accepted scientific commits or top-level continuation contracts.

## Accepted phase boundary

One accepted phase requires:

```text
one local scientific completion commit;
one phase package root;
one phase implementation report;
one external continuation contract;
one exact next phase or quantum handoff;
at least 384 focused live mutations;
two deterministic clean builds;
full internal-stage root reconciliation;
adjacent accepted regressions;
source, unit, orientation, distribution, topology, and count-once audits;
K9/K11/K13 separation wherever applicable;
and unchanged activation nonclaims unless explicitly closed.
```

## Tiered validation

Internal stage:

```text
focused unit tests;
two independent routes where source qualified;
source/root checks;
32-64 focused live mutations;
stage invariants;
restartable checkpoint hash.
```

Phase completion:

```text
full 384+ mutation gate;
two deterministic clean builds;
phase-wide route and covariance checks;
adjacent accepted regressions;
safe-loading and no-recomputation checks;
completeness certificate;
and exact continuation.
```

Major milestone:

```text
broad inherited regression;
complete package-root census;
activation-gate audit.
```

## Immutable upstream verification

When an upstream Git tree, implementation-report hash, public-loader root, and
package root are unchanged, verify them by hash and public loading. Do not
recalculate the full upstream science at every internal stage.

Run broader inherited calculations only at phase boundaries or when a
current-stage dependency actually changes.

## Heavy computation

A stage may offload large scans to CPU/GPU/HPC through immutable compute
capsules. Offloaded jobs:

```text
must use the exact Git commit and input-root hashes;
must write into job-specific result directories;
must not edit or commit the main worktree;
must report software/hardware/precision metadata and output hashes;
and must be imported and validated by the persistent controller.
```

A larger scan is not a reason to create another top-level package.

## Stop policy

Do not stop at the failure of one numerical or algebraic route.

Continue through lawful alternatives, precision escalation, larger cutoffs,
alternative stable decompositions, independent source-derived routes, and
HPC offload.

Stop scientifically only when all lawful routes establish a certified
mathematical/physical blocker. Ordinary software, transport, resource,
generated-file, or test-harness failures are infrastructure issues and must
not be mislabeled as physics blockers.

## Classical phases expected after C391

The exact frontier controls the sequence, but the intended structure is:

```text
JMY distribution/Laurent/real-virtual finite-remainder phase;

physical finite-basis/continuum matching and common-IR phase;

running, thresholds, active-flavor, and standard-scheme phase;

physical boundary/holonomy ensemble and parameter-closure phase;

renormalized K9/K11/K13 Hamiltonian-acceptance phase;

classical physical-state, observable, and uncertainty phase;

exact Q0/Q1/Q2 physical-handoff phase.
```

Do not force this list when an exact authority discontinuity requires a
different split.

## Quantum boundary

Do not modify the frozen Q0/Q1/Q2 authorities during classical phase mode.

Start separately accepted PennyLane packages only after the classical
activation capsule proves:

```text
complete physical Hamiltonians at K9/K11/K13;
physical state/observable acceptance;
all Hamiltonian-relevant counterterm/null directions fixed or irrelevant;
matching/running/input/boundary authorities closed;
leakage, Hermiticity, units, gauge/BRST, and count-once gates passed;
Q0/Q1/Q2 interface compatibility verified;
and an exact physical PennyLane continuation contract exists.
```
