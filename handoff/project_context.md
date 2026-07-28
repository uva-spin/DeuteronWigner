# Project context

Last updated: 2026-07-25

Primary brief: `../Deuteron_GTMD.pdf`, 29 pages, technical draft dated July 8, 2026.

Related source currently present: `../1610.04066v1.pdf`, Neff and Feldmeier, *The Wigner
function and short-range correlations in the deuteron*.

Detailed reading notes for that reference are in
`references/neff_feldmeier_2016.md`.

## Objective

Build a fully self-consistent canonical quark--gluon model for the full
leading-power spin-1 partonic structure of the deuteron over practical phase
space in

\[
(x,k_T,b_T,Q)
\]

for quarks, antiquarks, and gluons and for the target-polarization channels

\[
U,\ L,\ T,\ LL,\ LT,\ TT.
\]

The organizing object is a zero-skewness generalized transverse-momentum-dependent correlator
(GTMD), equivalently related by a transverse Fourier transform to a partonic
light-front Wigner distribution. TMDs, GPDs, PDFs, and
local-current/form-factor moments must be reductions of the same parent
object rather than independent models.

The canonical model must include as much physically known structure and
every realistically supported contribution available to date:
flavor-resolved nucleon dynamics, spin and OAM interference,
process-dependent gauge links, realistic spin-1 nuclear motion and tensor
structure, off-shell/coherent/exchange/non-nucleonic mechanisms, consistent
matching/evolution, and observable constraints.

Completion means one explicit, non-double-counted, scheme-consistent
canonical composition. A collection of individually valid alternatives,
complete named TMD tables, or sensitivity plots is not completion. Poorly
constrained contributions must be represented honestly and replaceably, but
must neither be silently omitted nor artificially enlarged.

## Immediate production objective: complete spin-1 TMD model

The current phase must construct internally coherent quark and gluon
correlator models and project from them the complete leading-twist spin-1
TMD basis:

- all 19 gluon TMDs;
- all 18 quark TMDs for each of \(u\) and \(d\);
- all 18 antiquark TMDs for each of \(\bar u\) and \(\bar d\);
- all target-polarization sectors \(U,L,T,LL,LT,TT\).

Completeness must arise from a common set of model degrees of freedom,
helicity amplitudes, nuclear kernels, and projection conventions. Missing
functions must not be filled by independent channel-level amplitude priors.
A zero is a valid prediction when it follows from the model, symmetry, a
real tree-level boundary condition, or an explicitly documented parameter
choice.

The baseline presentation point is

\[
x_N=0.1,\qquad Q=5\ {\rm GeV},
\]

with a future-pointing SIDIS gauge link. Past-pointing Drell--Yan results
must be available for checking and presenting the exact sign reversal of
T-odd functions. The primary plotted quantity is the dimensional named TMD
\(F(x,k_T;Q)\), including \(f_1\), with a common unit convention.
Rank-weighted ratios to \(f_1\) are supplemental diagnostics and must not
replace the dimensional TMD plots.

Production curves must be evaluated on a sufficiently dense \(k_T\) grid
to resolve nodes, extrema, origin limits, and band boundaries. Sparse
points connected by line segments are not a production result. Figures
must provide smooth central lines, smooth filled bands, consistent axes and
conventions across species, publication-quality vector output, and
machine-readable source tables.

Every canonical quark and gluon row must also belong to one
machine-auditable contribution graph, share a compatible scale and
soft-subtraction/evolution contract, and derive through the
nucleon-to-nucleus parent chain. Alternative models may remain as sensitivity
studies, but cannot substitute for or be silently mixed into the preferred
canonical member.

Uncertainty and sensitivity components must be propagated through the same
model and retained separately, including where applicable:

- proton/neutron PDF or fitted-TMD uncertainty;
- deuteron wave-function dependence;
- transverse-profile or width sensitivity;
- scale and TMD-evolution sensitivity;
- coherent, exchange-current, non-nucleonic, and gauge-link-phase model
  variations;
- numerical quadrature, transform, interpolation, and grid convergence.

Components without a justified probability measure are sensitivity
envelopes, not confidence intervals. They must not be silently combined in
quadrature or labeled as a nominal 95% confidence band. A combined display
is permitted only with an explicit combination prescription and must remain
traceable to its separate components.

### Model-building principles

Use as much established physics as possible: proton and neutron
phenomenology, isospin, deuteron light-front convolution, realistic
\(S\)- and \(D\)-wave structure, hermiticity, parity, time reversal,
gauge-link reversal, angular momentum, transverse-rank regularity,
positivity, collinear limits, sum rules, and known nuclear effects.
Representation theory and algebraic or geometric topology may be used to
organize symmetry sectors, phase structure, positivity domains, or global
consistency when they add real constraints. They must not be used
decoratively or as a substitute for missing dynamics. Quantum simulation
may be used only when it supplies a concrete construction or independent
validation not obtained more directly.

Every delivered TMD must identify:

1. its registry and convention definition;
2. the common correlator/model degrees of freedom that generate it;
3. whether its value is nonzero, structurally zero, or numerically
   consistent with zero;
4. which phenomenological inputs and nuclear mechanisms enter;
5. which uncertainty or sensitivity components apply;
6. its gauge-link/process behavior and collinear or weighted-moment limit.

### Acceptance criteria

The phase is complete only when the full flavor/species basis is generated,
all curves and separate bands pass numerical and visual checks, symmetry
and positivity constraints are tested, dimensional and ratio tables are
exported, plots include every requested flavor and \(f_1\), and the
remaining assumptions and limitations are stated without presenting model
sensitivity as fitted experimental uncertainty.

### Required rich-structure extension (2026-07-26)

The following are required production sectors, not optional upgrades:

- fitted or explicitly modeled, process-labeled gauge-link phases;
- flavor-resolved quark Sivers and Boer--Mulders inputs and gluon T-odd
  inputs;
- fit/lattice-informed pretzelosity and both worm-gear structures, with
  genuine-WW-breaking separated from the WW limit;
- independent gluon \(f^{abc}\)-type and \(d^{abc}\)-type T-odd boundaries
  and observable-specific hard weights;
- polarized and tensor coherent shadowing rather than an unpolarized
  correction copied across spin sectors;
- meson-exchange or non-nucleonic contributions represented as correlators
  wherever source information supports them; observable-only inputs must
  remain explicitly non-promotable;
- additional spin--orbit and OAM interference amplitudes beyond those
  induced by the existing S/D/Melosh impulse kernel.

An exact zero in a real one-body boundary is only a component limit. It does
not satisfy these requirements and must not be plotted or documented as a
physical null prediction. Completion is governed by WP10 of
`handoff/ROADMAP.md`.

### Governing correction and execution authority

The final model must be derived through the light-front parent chain and
must preserve flavor, active nucleon, helicity, operator, wave-function
component, mechanism, and gauge-link identity. A quick, minimal, toy,
merely runnable, or downstream-completed model is not an acceptable
objective. The reduced-amplitude outputs under `outputs/production_tmds/`
are superseded exploratory fixtures.

`handoff/ROADMAP.md` is the authoritative execution queue and acceptance
gate for all future sessions. Where the historical stage language below
suggests an “initial,” “first,” or minimal boundary, that language describes
development history rather than the completion criterion.

## Scientific architecture

The intended dependency chain is:

1. Light-front deuteron wave function.
2. Nuclear light-front helicity-density matrix and Wigner/spectral kernel.
3. Spin-1 quark, antiquark, and gluon GTMD helicity matrices.
4. TMD, GPD, PDF, form-factor, and partonic-Wigner reductions.
5. Tensor-polarized collinear PDFs and the inclusive \(b_1\) constraint.
6. Soft-subtracted TMDs, small-\(b_T\) matching, Collins-Soper evolution, and SCET-factorized
   observables.

SCET determines the hard/collinear/soft separation, Wilson-line structure, soft subtraction,
rapidity evolution, and perturbative matching. It does not determine the nonperturbative deuteron
matrix element.

## Core normalization anchor

Use the convention-independent target-helicity tensor difference

\[
\delta_T F =
F^{\Lambda=0}-\frac12\left(F^{\Lambda=+1}+F^{\Lambda=-1}\right).
\]

At leading order and leading twist,

\[
b_1^D(x,Q^2)=\frac12\sum_q e_q^2
\left[\delta_Tq_D(x,Q^2)+\delta_T\bar q_D(x,Q^2)\right]
+O(\alpha_s,1/Q^2).
\]

This is the first mandatory phenomenological normalization test. Conversion to a named
\(f_{1LL}\) convention occurs only after fixing the \(S_{LL}\) normalization and sign.

## Parent GTMD reductions

At zero skewness, the parent object depends on \(x,k_T,\Delta_T\). Required reductions include:

- TMD: set \(\Delta_T=0\).
- Partonic transverse Wigner distribution: Fourier transform \(\Delta_T\) to \(b_\Delta\).
- Zero-skewness GPD: integrate over \(k_T\).
- PDF: set \(\Delta_T=0\) and integrate over \(k_T\).
- Local-current and form-factor constraints: take appropriate \(x\) moments of the GPD limit.

The transverse coordinate \(b_\Delta\), conjugate to GTMD momentum transfer, is distinct from
the TMD impact parameter \(b_{\mathrm{TMD}}\), conjugate to measured transverse momentum and
used in TMD evolution. The implementation must keep these as distinct types or variables.

## Nuclear model

The baseline is a two-nucleon light-front wave function

\[
\Psi_{\Lambda}^{\lambda_p\lambda_n}(y,p_T)
\]

constructed from realistic instant-form deuteron \(S\)- and \(D\)-wave inputs, an exact Jacobian,
and a specified canonical-to-light-front spin rotation. AV18 and CD-Bonn are the requested
baseline alternatives; chiral EFT inputs may follow.

The full model separates matrix-element contributions:

\[
F_{a/D}=F^{\mathrm{IA}}_{a/D}+F^{\mathrm{coh}}_{a/D}
       +F^{\mathrm{exch}}_{a/D}+F^{\mathrm{nonN}}_{a/D}.
\]

Impulse approximation is expected to dominate many moderate- and large-\(x\) quark channels.
Coherent/shadowing effects matter at small \(x\). Exchange currents and non-nucleonic components
must remain independently extensible. Gluon double-helicity-flip channels may have a suppressed
or vanishing one-body nucleon baseline.

## Operator-level separation

Quark/antiquark and gluon correlators have distinct operators, representations, tensor
decompositions, matching coefficients, and process-dependent gauge links. They must not be
collapsed into a common microscopic correlator. They are unified only through a common
machine-readable registry and observable assembly layer.

Minimum registry fields from Section 19:

- name
- species
- parent GTMD
- operator projection
- target-polarization channel
- parton polarization
- transverse rank
- gauge-link label
- available marginals
- collinear-limit status
- matching status
- positivity-matrix block

## Numerical module plan

The brief specifies:

- M1: kinematics and conventions
- M2: deuteron wave functions
- M3: Wigner/spectral densities
- M4: GTMD parent layer and marginal views
- M5: nucleon PDF/TMD/GTMD/GPD and fragmentation inputs
- M6: impulse, coherent, exchange-current, and non-nucleonic mechanisms
- M7: TMD evolution
- M8: DIS, SIDIS, Drell-Yan, and gluon-sensitive observable kernels
- M9: \(b_1\), positivity, sum rules, small-\(b_T\) matching, and uncertainty constraints

## Development order

### Stage 0 - GTMD parent layer and consistency algebra

1. Fix the zero-skewness convention, Wilson-line labels, Fourier signs, and recoil mapping.
2. Implement quark and gluon parent containers with \(3\times3\) target-helicity matrices.
3. Implement TMD, GPD, PDF, Wigner, and local-current/form-factor reductions.
4. Build symbolic or numerical projectors from helicity matrices to named spin-1 TMDs.

### Stage 1 - Inclusive tensor PDFs

1. Implement light-front wave functions and helicity-density matrices.
2. Compute \(\delta_T\rho^N(y,p_T)\) and impulse-approximation \(\delta_Tq_D(x)\).
3. Reproduce the \(b_1\) relation and compare with data.
4. Add non-impulse components if required.

### Stage 2 - Rank-zero and low-rank TMDs

Build \(f_1^{a/D}\) and \(f_{1LL}^{a/D}\) in \(b_T\) and \(k_T\) space, validate their
collinear limits, and add the most direct SIDIS tensor observables.

### Stages 3-5

Complete the quark/antiquark/gluon registry and positivity matrices; add fixed-scheme SCET/TMD
evolution and \(W+Y\) observables; then perform global inference and uncertainty propagation.

## Mandatory validation philosophy

- Treat all GTMD marginals as views of one parent object and test that they commute.
- Validate baryon-number and momentum normalization.
- Test Hermiticity, parity, and applicable time-reversal relations.
- Construct tensor projectors by Gram-matrix inversion and test
  \(P_A^{ij}B_{B,ij}=\delta_{AB}\).
- Check density and partonic helicity matrices for positive semidefiniteness where positivity
  applies. Do not impose pointwise positivity on a Wigner quasi-distribution.
- Preserve wave-function interference terms explicitly. Negative Wigner regions and negative
  partial phase-space integrals can be necessary for the short-distance correlation hole.
- Do not infer that all high-momentum strength is localized at short distance; nonlocal regulators
  can generate high momentum through longer-distance wave-function curvature.
- Store transverse rank and Fourier-Bessel convention for every TMD.
- Verify rank-zero collinear integrals and the vanishing of unweighted rank-\(r>0\) integrals under
  the selected tensor convention.
- Check consistency of \(\mu\) and rapidity evolution and the cusp relation.
- Label gluon-sensitive observables by factorization status: established, assumed, or exploratory.

## Explicitly unresolved derivations

The draft labels these T1-T9; they remain open until recorded in `decisions.md`:

1. GTMD Fourier signs, gauge links, recoil factors, and \(b_\Delta\)/\(b_{\mathrm{TMD}}\) mapping.
2. Proof that one nuclear kernel yields the TMD, PDF, and GPD/form-factor convolutions.
3. Exact light-front Jacobian and spin-rotation convention.
4. Full nucleon spin-density convolution and vector-to-tensor spin recoupling.
5. Complete quark/gluon projector library and convention dictionaries.
6. Status of tensor-polarized small-\(b_T\) matching coefficients.
7. Semidefinite positivity for full spin-1 helicity matrices.
8. Minimal coherent/shadowing model needed for low-\(x\) \(b_1\).
9. Process-specific Wilson lines and possible Glauber/factorization-breaking issues.
