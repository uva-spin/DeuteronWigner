# C20/M1 implementation report

C20 replaces M0 coefficient oracles for ten supported twist-two blocks with
source-recorded declared-order coefficients and independent distribution and
moment checks. The families cover unpolarized quark/gluon, helicity,
transversity, linearly polarized gluon, singlet mixing, and spin-1 LL operator
universality. Physical twist-three T-odd coefficients remain unavailable.

All 540 C19 identities remain stable: 492 are audited executable entries and
48 remain explicitly unavailable. Five shared operator-block parameters use
nine calibration conditions and seven holdout classes. The largest holdout
residual is 0.0059. Step-scaling cocycle and complete-block scheme round trips
close below 3e-13. Rank 0--3 residuals remain at 2e-8 through 8e-8.

The external interface consumes a synthetic exact covariance bundle for
end-to-end validation. No physical lattice bundle is claimed because a
compatible machine-readable primary-source covariance bundle was not
established. All uncertainty sources remain separate. C20 covers 770 stable
requirements and 560 negative injections and remains validation-only.
