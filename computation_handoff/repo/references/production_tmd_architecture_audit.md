# Audit of the complete-TMD implementation

Date: 2026-07-25

Status: corrective architecture audit; production gate

## Finding

The files under `outputs/production_tmds/` are smooth and internally
consistent outputs of `ReducedCorrelatorTMDModel`, but they are not
reductions of the project's light-front deuteron GTMD parent. They are
therefore superseded as production physics results and retained only as an
exploratory closure/regression fixture.

The invalid substitution was

\[
\{f_1,g_1,f_{1LL},h_1\}_{\rm anchors}
\longrightarrow
\text{six shared reduced amplitudes}
\longrightarrow
\text{complete named TMD table},
\]

instead of the required chain

\[
\Psi_D^{\rm LF}
\longrightarrow
\rho^{N/D}_{\Lambda'\Lambda;\lambda'\lambda}
\longrightarrow
W^{[\Gamma]}_{a/N}
\longrightarrow
W^{[\Gamma]}_{a/D}
\longrightarrow
\Phi^{[\Gamma]}_{a/D}
\longrightarrow
F_{a/D}.
\]

## Simplifications and missing degrees of freedom

### Nucleon structure

1. The quark GTMD boundary connected to the nuclear convolution contains
   only a helicity-independent rank-zero scalar.
2. The complete spin-half leading-twist quark correlator
   \((f_1,g_1,h_1,h_1^\perp,f_{1T}^\perp,g_{1T},
   h_{1L}^\perp,h_{1T}^\perp)\) is absent.
3. Proton and neutron contributions were summed inside the convolution,
   erasing their traceability before observable assembly.
4. The complete table reused common transverse widths and common mechanism
   coefficients across \(u,d,\bar u,\bar d\).
5. Quark transversity was fixed to 0.7 of a Soffer ceiling rather than
   supplied through a replaceable fit with uncertainty.
6. No phenomenological Sivers, Boer--Mulders, worm-gear, or pretzelosity
   input and covariance was connected.
7. The gluon boundary supports only \(f_1^g,g_1^g,h_1^{\perp g}\);
   its Gaussian regression model is not the matched small-\(b_T\)
   production boundary.
8. The nonperturbative gluon large-\(b_T\) profile is not constrained by
   published numerical lattice gluon-TMD data.

### Nuclear structure

9. The complete table did not evaluate the retained \(3\times3\) target and
   \(2\times2\) active-nucleon helicity convolution.
10. AV18 entered the completion mainly through collinear anchors and a
    scalar \(D\)-state probability.
11. \(SS,SD,DS,DD\) interference was not retained per TMD.
12. Proton and neutron spectral terms could not receive distinct
    charge-symmetry-breaking, off-shell, or tagged-observable treatments.
13. Coherent shadowing, antishadowing, EMC/off-shell, meson-exchange, and
    non-nucleonic components were absent from the complete outputs.
14. The wave-function band varied reduced parameters rather than
    propagating AV18, CD-Bonn, and the four Norfolk wave functions through
    every correlator.

### Correlators and projection

15. The reduced-amplitude projection matrix was not the published spin-1
    quark or gluon operator decomposition.
16. A complete quark projector from the three leading-twist Dirac
    projections to all 18 named spin-1 TMDs is missing.
17. The gluon operator/projector algebra exists, including the TT
    identifiability relation, but was not used for the complete output.
18. The output did not retain an auditable parent correlator from which
    TMD, GPD, PDF, and Wigner reductions commute.
19. Positivity tests bounded individual modeled modulations but did not
    establish positivity of the complete quark--target or
    gluon--target helicity density matrix.

### Gauge links and evolution

20. All T-odd functions were generated from one universal phase. This is
    not a substitute for flavor-, operator-, and process-dependent
    initial/final-state interactions.
21. Sign reversal was imposed, but the magnitude was not derived from a
    gauge-link mechanism or phenomenological nucleon input.
22. The complete quark output did not use a declared soft-subtracted TMD
    scheme or Collins--Soper evolution.
23. Gluon small-\(b_T\) matching and evolution existed separately but were
    not propagated through the parent nuclear correlator for the complete
    basis.
24. No fixed-order \(Y\) term controlled the high-\(k_T\) region.

### Uncertainty and claims

25. Percentage anchor variations were labeled as a PDF study without
    propagating the applicable PDF/TMD replica or Hessian ensemble.
26. Several envelopes were parameter brackets, not statistical
    uncertainties; this was documented but insufficiently separated in the
    production claim.
27. Passing smoothness and internal-consistency tests was incorrectly
    treated as evidence that the required physics architecture had been
    implemented.
28. `production_ready_for_model_studies` was too permissive and allowed a
    downstream completion model to pass without parent traceability.

## Controlled isospin statement

In the exact charge-symmetric one-body limit for an inclusive \(I=0\)
deuteron,

\[
u_D=d_D,\qquad \bar u_D=\bar d_D
\]

is a valid Wigner--Eckart consequence, not a flavor-key error. Nevertheless,
the implementation must retain \(u_p,d_p,\bar u_p,\bar d_p\) and their
neutron partners separately until final assembly. This is required for
tagged observables, electromagnetic weighting, uncertainty correlations,
off-shell effects, and controlled charge-symmetry breaking. The equality
must emerge as a tested limit, not be hard-coded as the architecture.

## Production gates

A complete TMD table may be called parent-derived only if every row:

1. identifies its quark, antiquark, or gluon operator projection;
2. retains flavor and active proton/neutron contributions;
3. identifies the light-front wave function and spectral component;
4. identifies impulse, coherent, off-shell, mesonic, non-nucleonic, and
   isospin-breaking mechanism terms separately;
5. is obtained through the published spin-1 projector;
6. carries a machine-readable provenance class and validity domain;
7. satisfies applicable hermiticity, parity, time-reversal, support,
   normalization, marginal, and positivity tests;
8. reproduces \(b_1\) and other applicable reductions from the same parent;
9. separates fitted uncertainty, replica/Hessian uncertainty, lattice
   uncertainty, model sensitivity, and numerical error;
10. contains no untraced generic completion amplitude.

The exporter must fail closed when any gate is missing.
