# TMD soft-subtraction and rapidity-scale contract

Last updated: 2026-07-26

## Declared convention

The in-house quark and gluon small-\(b_T\) layers use a
Collins-subtracted square-root-soft TMD, the delta rapidity regulator,
\(\overline{\mathrm{MS}}\) UV renormalization, and the zeta-prescription
organization used by the matching coefficients in arXiv:1907.03780. The
current one-loop CSS implementation follows only the canonical hard line

\[
  \zeta_i=\mu_i^2,\qquad \zeta_f=Q^2,\quad \mu_f=Q .
\]

The typed implementation is `src/deuteron_wigner/tmd_scheme.py`.
`TMDScalePoint` carries \(\mu\) in GeV and \(\zeta\) in GeV squared.
`TMDScheme` carries the soft subtraction, regulator, rapidity prescription,
UV scheme, and source. Matching and evolution configurations each carry the
same object and refuse composition if any identifier differs.

## What this fixes

Previously, the gluon boundary stored the scheme as a metadata string and the
quark boundary used a different descriptive string. Nothing prevented an
incompatible evolution kernel from consuming either boundary, and numerical
results exposed \(Q\) but not the rapidity-scale endpoints. The new contract:

- rejects incompatible boundary/evolution conventions;
- rejects noncanonical \(\zeta\) paths that the current code does not solve;
- persists \(\mu_i,\zeta_i,\mu_f,\zeta_f\) on evolved values;
- emits identical machine-readable scheme metadata from boundary and
  evolution layers.

## Accuracy boundary

This is an exact bookkeeping and composition constraint, not an upgrade of
the perturbative calculation. The in-house gluon calculation remains mixed
accuracy: tree matching for \(f_1^g,g_1^g\), first-nonzero one-loop matching
for \(h_1^{\perp g}\), and one-loop spin-independent CSS evolution with
unfitted large-\(b_T\) profiles. The analogous quark rank-zero route remains
LO plus a model intrinsic profile. Neither may be labeled precision
production evolution.

Fit-native arTeMiDe BPV20 and Vpion19 paths retain their native scheme and
must not be silently routed through this in-house CSS contract. A future
general two-scale evolution backend must explicitly support arbitrary
\((\mu_i,\zeta_i)\to(\mu_f,\zeta_f)\), test path independence through the
cusp consistency relation at its declared order, and supply correlated
profile/scale uncertainties.

