# C32/R0 implementation report

## Result

C32 creates the distinct validation root
`C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION`. It extends, but does not relabel,
the historical C11 regulated model density with an explicit fundamental
staple, transverse closure, rapidity-regulator plan, vacuum-soft definition,
inverse-square-root allocation, and zero-bin convention.

The completed operator reduces exactly to C11 at tree level. This is an
executed regression, not a declared zero: the actual PLAN-A C11 helicity
matrices are passed through `H4WilsonKernel` at zero coupling for u, d, ubar,
and dbar at x=0.03, 0.1, and 0.3. All twelve parents are nonzero. Future and
past matrices equal the C11 parent, the link-even matrix equals the parent,
the link-odd matrix vanishes, and both forward-reduction scalar routes agree.
The maximum matrix/scalar residual is exactly zero after applying tree
soft=UV=rapidity=1 and zero-bin=0.

The one-loop calculation then fails at a prior structural gate:
`C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED`. The C11 regulator acts on the
baryon-number-one finite light-front basis and supplies no vacuum Hilbert
sector for the four-eikonal-line Wilson soft operator. The existing C12/C14
soft-overlap objects explicitly remain validation ledgers with an incomplete
continuum soft function and no physical TMD scheme. Importing the continuum
soft factor would not constitute a calculation in the C11 regulator.

The exact outcome branch is therefore **C33/S0 — explicit finite-basis vacuum
soft sector and rapidity-renormalization construction**.

## Frozen identities and plans

The selected microscopic source is PLAN-A
`C11:H4:PLAN:04c40be451b5c7f3a60b`, with the fine C7 regulator
`C7:H0:RESOLUTION:b8196017a6bde7c88eda`. PLAN-B remains a distinct alternative
and is not added.

The frozen three-point C7 trajectory is:

- K=9/2, Nmax=8, bHO=0.40 GeV;
- K=11/2, Nmax=10, bHO=0.45 GeV;
- K=13/2, Nmax=12, bHO=0.50 GeV.

All retain lambda_H=1.2 GeV, x_min=1/18, antiperiodic half-integer quark and
antiquark modes, periodic nonzero-integer gluon modes, and the explicit gluon
zero-mode exclusion ledger. The reported bHO*sqrt(Nmax) and
bHO/sqrt(Nmax) scales remain diagnostic—not exact UV/IR cutoffs.

The partonic plan freezes spacelike off-shell quarks on both sides, momenta 5
and 10 GeV, p^2=-0.04 and -0.09 GeV^2 checks, covariant-gauge parameters
xi=0,1,2, and a modified-delta rapidity regulator. The finite basis is not
silently treated as a rapidity regulator.

## One-loop and distributional audit

Twenty-five real, virtual, Wilson, soft, zero-bin, counterterm,
instantaneous-light-front, basis-boundary, endpoint, zero-mode, and mixing
entries have explicit statuses. None is silently set to zero. The two vacuum
soft entries are structurally undefined; the remaining microscopic one-loop
entries require calculation after a soft-sector definition exists.

Typed delta, logarithmic-plus, regular, lower-limit-plus, convolution, and
Mellin actions are implemented without an endpoint bin or physical epsilon.
An independent algebra oracle closes its quark-number moment at 1.4 with
roundoff-level residual. These are distribution-algebra tests, not invented
microscopic one-loop coefficients.

The continuum project expression is retained only as a target source oracle.
C22 coefficient fixtures are not promoted: C22 itself states that its
polynomials are validation scaffolds and that zero identities are fully
qualified. No same-IR numerical project oracle or microscopic one-loop object
is claimed.

## Fail-closed consequences

Because the soft sector fails, zero-bin, UV, rapidity, common-IR difference,
gauge, anomalous-dimension, state-independence, and regulator-trajectory
residuals are recorded as unavailable rather than zero. Every q<-q, q<-g,
q<-qbar, nonsinglet, and singlet channel remains unresolved at one loop. The
first omitted order is O(alpha_s) with a nonzero-unknown remainder.

No microscopic TMD is exported and the twelve-point bridge is not rerun. All
twelve points remain `BRIDGE_COMMON_DOMAIN_ONLY`; the failed projection is
642 x 0 and is explicitly empty-not-zero. The source bridge covariance remains
the preserved 642 x 11 factor with rank 10, nullity 1, and unchanged hash.

## Isolation and reproduction

No ART25 member, parameter, data point, chi2, bridge residual, or proton-level
ratio enters the operator or matching derivation. Frozen roles, ancestry,
no-double-counting, `NO_JOINT_MEASURE`, 216 production routes, and eight
authoritative artifacts remain unchanged. No fit, calibration, likelihood,
posterior, optimizer, reweighting, emulator, process bridge, or physical,
spin-1, deuteron, T-odd, gluon, inference, or production status is created.

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c32_manifests.py 1167
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c32.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```
