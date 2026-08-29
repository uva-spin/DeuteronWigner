# C310 Infrastructure-Recovery Launch Authority

## Classification

The prior persistent process stopped for an **infrastructure condition**, not
a mathematical or physical blocker.

Freeze:

```text
last completed scientific job:
C309/HQCDRIMASSV0GRAMEVAL1

last completed commit:
96561173f53da8a72af376acd7f41783d27c358e

C309 package root:
0236468d261bf81f3efc380d5af7dce7540f0cde6bc11ebac42e7e1d7467c5eb

current uncompleted job:
C310/HQCDRIMASSSHAPETAIL1

controller state at the independent audit:
INFRASTRUCTURE_BLOCKER

activation gate:
NOT_READY
```

The transport/session failure does not alter C309 and does not resolve C310.
Do not create a new scientific continuation contract. Use the existing
C309-to-C310 contract and the existing C310 prompt recorded in
`AUTOPILOT_STATE.json`.

## Recovery rule

A prior C310 process may have created uncommitted files, generated evidence, or
partial calculations. Treat the scientific worktree as a recovery surface.

Do not:

```text
git reset --hard;
git clean;
discard, overwrite, or blindly regenerate partial C310 files;
create a duplicate C310 completion commit;
modify unrelated user files;
or interpret the infrastructure stop as a C310 scientific result.
```

First:

1. verify that `HEAD` is exactly the C309 completion commit;
2. read the current state and existing C310 contract/prompt completely;
3. inventory all tracked, staged, and untracked C310 artifacts;
4. compare them with C309 and the C310 contract;
5. validate and reuse lawful partial work;
6. repair or complete only what remains.

## Exact C310 scientific object

C309 established that both `CHI8` and `RE_TF3` contain nonconstant logarithmic
mode-cutoff tails. C310 must close the **shape-tail subtraction** before any
wall-distance/epsilon extrapolation.

C310 must:

```text
extend fixed-epsilon scans to larger mode cutoffs;

fit CHI8 and RE_TF3 tails separately over multiple independent cutoff
windows;

derive or rigorously enclose the tail coefficients from the authenticated
C303 AST and its descendant authority;

never guess exact rational coefficients from floating-point fits;

separate center-mode, CHI8, and RE_TF3 subtraction owners;

publish fit-window, cutoff-range, regulator, and correlated-tail covariance;

subtract the two logarithmic shape tails separately;

publish fixed-epsilon finite remainders with outward enclosures;

test stability under cutoff windows, fit forms, mode order, and resolution;

preserve the C308 symmetric finite remainder and C309 full-Gram authority
read-only;

and only after shape-tail closure create the exact epsilon-limit
continuation.
```

A useful schematic form is:

```text
G_CHI8(N, epsilon) =
    a_CHI8(epsilon) log N + b_CHI8(epsilon) + r_CHI8(N, epsilon)

G_RE_TF3(N, epsilon) =
    a_RE_TF3(epsilon) log N + b_RE_TF3(epsilon) + r_RE_TF3(N, epsilon)
```

but the exact basis, normalization, fit variables, and asymptotic form must
come from the committed C303-C309 authority, not from this schematic notation.

## Positive and fail-closed outcomes

A positive result requires separately source-qualified tail coefficients or
outward enclosures, stable finite remainders, correlated covariance, route
agreement, and one exact epsilon-limit continuation.

Fail closed on the smallest scientific object when:

```text
the authenticated C303 AST cannot support the required asymptotic
classification;

independent lawful tail routes disagree after convention and cutoff audits;

the residual after every source-qualified subtraction remains
nonconvergent;

or a finite remainder would require a guessed coefficient or silent fit
choice.
```

Ordinary numerical instability, insufficient initial cutoff range, stale
generated files, or software/test defects are not scientific blockers; repair
or extend them.

## Persistence and preservation

Preserve:

```text
C309 and all prior package roots;
state revision during this infrastructure-only restart;
the user's handoff/ROADMAP.md change;
protected quantum worktrees;
the C134 quarantine;
the inherited C157 boundary;
C166 graphs;
Q0/Q1/Q2;
all physical and activation nonclaims.
```

No physical mass coefficient, boundary ensemble, physical Hamiltonian,
counterterm/null representative, PennyLane state, spectrum, TMD, or
activation claim is authorized in C310.

Complete C310 with one local scientific commit, create exactly one next
continuation, atomically advance the persistent state, and continue. Never
push.
