# Gluon T-odd source and implementation boundary

Last audited: 2026-07-26

## Physics that is enforced

A gluon Sivers contribution is not one universal function with a quark-like
SIDIS/DY sign.  The two adjoint color contractions proportional to
\(f^{abc}\) and \(d^{abc}\) define independent universal inputs.  A measured
process selects a linear combination through initial/final-state-interaction
hard factors.  This structure is described in the review
arXiv:1504.04332 and implemented phenomenologically in the CGI-GPM analyses
arXiv:1811.02970, arXiv:1902.02425, and arXiv:2007.03353.

`src/deuteron_wigner/gluon_todd.py` therefore keeps three labels distinct:

1. future versus past staple orientation;
2. antisymmetric f-type versus symmetric d-type color contraction;
3. observable-specific hard coefficients \(C_f,C_d\).

Both universal components reverse under simultaneous future/past staple
reversal. Mixed link pairs are not assigned a sign by analogy and are
refused until their process-specific link calculation is supplied.

`SiversAugmentedSpinHalfGluonGTMD` embeds the resulting forward function in
the spin-half target operator as the two Pauli-matrix components multiplying
\(\epsilon_T^{S k}\delta_T^{ij}/(2M)\). This preserves the full nucleon-spin
indices needed by the deuteron convolution. It deliberately refuses nonzero
transfer: no transverse-transfer profile follows from a forward Sivers TMD.

## What is not claimed

The RHIC CGI-GPM extractions provide preliminary, framework-dependent
constraints, not a public replica ensemble in the same production sense as
the quark BPV20 input. COMPASS's gluon-sensitive asymmetry is an
observable-level constraint and does not separately determine both color
functions. Small-x odderon calculations and spectator calculations have
restricted regimes and are not promoted to a global boundary.

Consequently the production nucleon gluon parent still has an explicit
missing T-odd boundary. The code does not install a nonzero default, average
the f/d functions, or infer hard coefficients. A future adapter must provide:

- both f- and d-type functions in a documented normalization;
- source, evidence class, validity domain, and uncertainty prescription;
- an observable with explicit \(C_f,C_d\) and factorization statement;
- tests against the source convention and any released uncertainty members.

## Replacement validation

A production adapter must pass component independence, simultaneous
time-reversal, finite/domain checks, source benchmarks, positivity bounds in
the same normalization as \(f_1^g\), and full spin-1 correlator Hermiticity
after nuclear convolution. Process predictions must reproduce the supplied
linear color decomposition and must fail if either color coefficient is
implicit.
