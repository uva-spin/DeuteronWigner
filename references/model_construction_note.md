# Superseded summary of the canonical spin-1 deuteron GTMD/TMD model

> **Superseded 2026-07-27.** This short-form Markdown summary and its
> ReportLab renderer are retained only as historical development records.
> The authoritative scientific note is the LaTeX manuscript
> `references/model_construction_note.tex`, rendered as
> `output/pdf/model_construction_note.pdf`.

**Status:** authoritative pre-evolution scientific model note  
**Date:** 2026-07-27  
**Implemented boundary:** leading-twist, forward spin-1 quark, antiquark, and
gluon TMDs at \(Q=5\) GeV and
\(x_N=\{0.02,0.05,0.10,0.20,0.40\}\)  
**Next major phase:** complete common-scheme, rank-aware multi-\(Q\) evolution

## 1. Purpose and interpretation

This note records what went into the model, why the project changed direction
several times, what the present numerical objects mean, and which parts are
known, fitted, inferred, or modeled. It is intended to be readable without the
development conversation and to prevent future work from silently reverting
to an isoscalar toy model or to a collection of unrelated TMD curves.

The governing objective is a self-consistent canonical quark-gluon model of a
spin-1 deuteron with the richest physical content that can presently be
supported. "Canonical" means that named TMDs are projections of retained
parton-target correlators assembled through a documented contribution graph.
It does not mean that every distribution is known with the precision of
unpolarized \(f_1\), nor that all nonperturbative QCD has been calculated from
first principles.

The current accepted result is a **pre-evolution boundary model**. It is
complete at the declared leading-twist forward basis: all declared quark and
gluon projections exist, are flavor or color/link resolved as applicable,
have smooth central functions and named uncertainty or sensitivity axes, and
pass the project constraints. Complete uniform evolution away from \(Q=5\)
GeV is deliberately the next phase and is not claimed here.

## 2. The original GTMD-first proposal

The July 8, 2026 technical draft `Deuteron_GTMD.pdf`, titled *A GTMD-First
Light-Front Wigner and SCET Framework for Spin-1 Deuteron TMDs*, supplied the
original architecture. Its central observation was that a TMD should not be
built in isolation if the project is to use nuclear, form-factor, inclusive,
and transverse-momentum information consistently. The intended chain was

\[
\Psi_D^{\rm LF}
\longrightarrow \rho^{N/D}_{\Lambda'\Lambda;\lambda'\lambda}
\longrightarrow W_{a/N}^{[\Gamma]}
\longrightarrow W_{a/D}^{[\Gamma]}
\longrightarrow \Phi_{a/D}^{[\Gamma]}
\longrightarrow F_{a/D}.
\]

Here \(\Psi_D^{\rm LF}\) is the light-front deuteron wave function,
\(\rho^{N/D}\) its active-nucleon spin density, \(W_{a/N}\) a nucleon-level
quark or gluon GTMD correlator, \(W_{a/D}\) the nuclear correlator,
\(\Phi_{a/D}\) its forward TMD limit, and \(F_{a/D}\) a named TMD projection.
The same parent is meant to supply:

- the forward TMD limit at \(\Delta_T=0\);
- the GPD limit after integrating over \(k_T\);
- the PDF and tensor-PDF limits after the appropriate forward integrations;
- the partonic Wigner distribution after Fourier transformation in
  \(\Delta_T\);
- form-factor and moment constraints after the corresponding integrations.

The original draft also established several distinctions that remain
fundamental:

1. The **nuclear light-front Wigner or spectral density** describes the
   phase-space and spin distribution of nucleons in the deuteron.
2. The **partonic Wigner distribution** is the transverse Fourier transform
   of a QCD GTMD.
3. These objects are coupled by the nuclear convolution but are not the same
   mathematical object.
4. SCET and TMD factorization define operator, soft-subtraction, rapidity,
   matching, and evolution structure; they do not supply the nonperturbative
   deuteron matrix element.
5. Positivity belongs at the retained spin-density-matrix level. A Wigner
   quasi-distribution need not be pointwise positive.

The draft correctly anticipated realistic deuteron S- and D-wave structure,
Melosh rotations, the \(b_1\) tensor benchmark, quark and gluon operators,
the U/L/T/LL/LT/TT spin-1 sectors, gauge links, small-\(b_T\) matching,
Collins-Soper evolution, and factorized observables. It was a formal program,
not yet a fully specified numerical model.

## 3. Why the project had to refocus

### 3.1 The first runnable boundary was too narrow

The earliest GTMD calculation used a real, helicity-independent, rank-zero
one-body nucleon boundary. It was valuable for checking Fourier transforms,
hermiticity, \(k_T\) marginals, and the \(b_1\) reduction, but it could not
generate the rich leading-twist spin structure. Exact zeros in that boundary
were not predictions that the physical TMDs vanish. They meant that the
necessary helicity interference, orbital amplitude, or imaginary gauge-link
phase had not been included.

In particular:

- T-odd TMDs were zero because a real one-body overlap has no rescattering
  phase;
- many worm-gear, pretzelosity, and tensor structures were zero because the
  necessary off-diagonal spin/OAM amplitudes were absent;
- a spin-1/2 nucleon one-body operator cannot by itself generate every
  spin-1 tensor structure;
- a forward scalar boundary cannot stand in for the complete nucleon
  helicity correlator.

This is now called a **controlled boundary or limiting case**, not the full
model.

### 3.2 A smooth complete-looking closure still bypassed the parent

A subsequent reduced-amplitude model populated every named function with
smooth curves. It was mathematically regular and passed basic sign,
rank-origin, and positivity-ceiling checks, but it mapped a few anchors into
shared generic amplitudes rather than deriving the results through the
light-front parent chain. Common flavor shapes and coefficients caused
unphysical-looking \(u=d\) and \(\bar u=\bar d\) behavior and hid the
difference between proton, neutron, and deuteron quantities.

That output is retained only as an exploratory regression fixture. Smoothness
and basis population are not evidence of physical completeness.

### 3.3 Isoscalar symmetry was being used at the wrong level

In the exact charge-symmetric one-body limit, an inclusive \(I=0\) deuteron
can satisfy

\[
u_D=d_D,\qquad \bar u_D=\bar d_D.
\]

This is a valid Wigner-Eckart consequence for the final inclusive deuteron
projection. It does **not** imply \(u_p=d_p\), \(u_n=d_n\), or identical
proton and neutron TMDs. The architecture must retain
\(u_p,d_p,\bar u_p,\bar d_p\) and neutron partners separately, apply the
controlled charge-symmetry map only where justified, and allow
charge-symmetry breaking (CSB), off-shell effects, tagging, and
electromagnetic flavor weights.

The current resolved parent therefore stores:

- `proton_in_deuteron`;
- `neutron_in_deuteron`;
- `nucleon_sum`;
- `proton_minus_neutron`;
- `nuclear_correction`;
- `canonical_spin1_total`.

The final deuteron total is one derived projection. It does not replace the
constituent dynamics. Current closure residuals are exactly zero for quarks
and \(1.73\times10^{-18}\) for gluons.

### 3.4 Independent named-TMD models were not self-consistent enough

Adding Sivers, Boer-Mulders, tensor phases, gluon spectator patterns, and
other physically motivated curves one by one improved coverage, but it risked
double counting and unequal dynamical depth. The project therefore moved to
a common retained-correlator synthesis:

- contributions are classified as baselines, additive mechanisms, exclusive
  alternatives, or uncertainty members;
- mutually overlapping amplitudes may not be silently summed;
- enrichments act on complete parents or density matrices, not independently
  on named TMD columns;
- projections are regenerated after composition;
- provenance and validity metadata travel with each component.

### 3.5 "Complete basis" was separated from "complete evidence"

Once all 36 declared quark-plus-gluon projections were populated, a further
audit showed that basis completeness alone did not put every TMD at the
evidential level of \(f_1\). WP12-E therefore imposed an evidence-parity gate.
Every row had to identify:

- a central physical source;
- flavor or link/color resolution;
- explicit proton/neutron bookkeeping where applicable;
- fit replicas, Hessians, published intervals, or an explicitly named model
  ensemble;
- CSB treatment;
- projection from the shared parent;
- channel-appropriate nuclear dressing;
- an observable benchmark or controlled-limit validation.

All 36 rows pass this structural evidence gate. A pass means that unknown
physics is represented explicitly and replaceably; it does not transform a
model band into experimental knowledge.

## 4. Declared degrees of freedom and conventions

### 4.1 Kinematics

The production boundary uses the nucleon-scaled momentum fraction \(x_N\).
The dense inspections use \(Q=5\) GeV, with five x nodes
\(0.02,0.05,0.10,0.20,0.40\). The primary figures at the standard inspection
point use \(x_N=0.1\). Transverse momentum is represented by smooth dense
grids; positive-rank structures contain the required powers of \(k_T/M\).
Bare coefficients and physical rank-weighted modulations are not confused.

### 4.2 Spin-1 target density

The deuteron helicity space is three dimensional,
\(\Lambda=-1,0,+1\). Its density is decomposed into:

- U: unpolarized scalar;
- L: longitudinal vector polarization;
- T: transverse vector polarization;
- LL: longitudinal tensor polarization;
- LT: mixed longitudinal-transverse tensor polarization;
- TT: transverse traceless tensor polarization.

The parton space is two dimensional for quark helicity and two dimensional
for gluon circular polarization; gluons additionally carry transverse tensor
indices and link/color labels. Retaining the joint target-parton density
allows hermiticity, positivity, polarization projection, and composition to
be checked before reducing it to named functions.

### 4.3 Quark and antiquark basis

For each of \(u,d,\bar u,\bar d\), the declared leading-twist basis contains
18 functions:

| Target sector | Quark TMDs |
|---|---|
| U | \(f_1,\ h_1^\perp\) |
| L | \(g_1,\ h_{1L}^\perp\) |
| T | \(f_{1T}^\perp,\ g_{1T},\ h_1,\ h_{1T}^\perp\) |
| LL | \(f_{1LL},\ h_{1LL}^\perp\) |
| LT | \(f_{1LT},\ g_{1LT},\ h_{1LT},\ h_{1LT}^\perp\) |
| TT | \(f_{1TT},\ g_{1TT},\ h_{1TT},\ h_{1TT}^\perp\) |

Quarks and antiquarks use the same operator basis but retain independent
flavor inputs and signs. No sea function is generated by copying a valence
function.

### 4.4 Gluon basis

The current declared gluon basis contains 18 projections:

| Target sector | Gluon TMDs |
|---|---|
| U | \(f_1^g,\ g_1^g,\ h_1^{\perp g}\) |
| L | \(h_{1L}^{\perp g}\) |
| T | \(f_{1T}^{\perp g},\ g_{1T}^g,\ h_1^g,\ h_{1T}^{\perp g}\) |
| LL | \(f_{1LL}^g,\ h_{1LL}^{\perp g}\) |
| LT | \(f_{1LT}^g,\ g_{1LT}^g,\ h_{1LT}^g,\ h_{1LT}^{\perp g}\) |
| TT | \(f_{1TT}^g-h_{1TT}^{\perp g},\ g_{1TT}^g,\ h_{1TT}^g,\ h_{1TT}^{\perp\perp g}\) |

The TT combination reflects the identifiability of the implemented forward
correlator decomposition. Older exploratory documentation counted 19 gluon
names by splitting a TT pair that is not independently identifiable in this
forward projection. Those older catalogs are not the canonical registry.

For T-odd gluons, antisymmetric \(f^{abc}\)-type and symmetric
\(d^{abc}\)-type color/link structures remain independent. A physical
process must provide the hard-color weights; the model does not invent a
universal mixture.

## 5. Nucleon-level quark content

### 5.1 Unpolarized distributions

The principal quark \(f_1\) boundary is flavor resolved with CT18NNLO
unpolarized PDFs. CT18 Hessian members are propagated through five x nodes,
not replaced by a generic percentage variation. MSHT20-QED supplies a
sourced neutron/CSB comparison for \(f_1\). The transverse profile is a
declared TMD boundary component rather than a claim that collinear PDFs
determine all \(k_T\) dependence.

### 5.2 Helicity

Quark \(g_1\) uses BDSSV24-NLO polarized inputs. The complete 600-replica
ensemble is propagated through the response rather than using a sparse pilot.
The nuclear spin convolution retains deuteron depolarization and the
wave-function dependence.

### 5.3 Transversity

Quark \(h_1\) uses the JAMDiFF plus lattice-informed transversity ensemble
(968 accepted members in the project input). This replaced the obsolete
closure \(h_1=0.7\) times the Soffer ceiling. Positivity is used as a
consistency constraint, not as the central-value model.

### 5.4 Sivers and gauge-link phase

Quark \(f_{1T}^\perp\) uses the BPV20 arTeMiDe extraction with 500 replicas.
The future-pointing and past-pointing staples are retained, and the expected
SIDIS/Drell-Yan T-odd sign reversal is tested. The fitted Sivers input is not
reused as a universal phase for every T-odd operator.

### 5.5 Boer-Mulders

Quark \(h_1^\perp\) is a BPV20-linked Boer-Mulders sign and flavor-hierarchy
scenario. It uses the Sivers evidence to organize plausible rescattering
strengths, but it is explicitly a model relation rather than a joint
Boer-Mulders fit. Alternative hierarchy members define a sensitivity axis.

### 5.6 Worm gears

The \(g_{1T}\) central input follows Yang et al. (2024). Public covariance or
replicas are not available, so the project propagates the published
asymmetric parameter intervals through all 16 corners. This envelope is a
published-interval hull, not a confidence region. The fit's zero-sea
boundary is supplemented by a shared-Fock/OAM sea sensitivity rather than
silently declaring the sea exactly zero.

The \(h_{1L}^\perp\) boundary is linked to JAMDiFF \(h_1\) through the
Wandzura-Wilczek-type relation, with a separate configurable genuine
twist/interference-breaking sensitivity. The relation is an organized model
constraint, not an exact identity of QCD.

### 5.7 Pretzelosity

\(h_{1T}^\perp\) is a flavor-resolved nonperturbative/OAM model bounded by
the applicable positivity moment. Its size and sign are tested through
alternative OAM scenarios. Positivity limits the allowed answer but is not
used to argue that a near-bound value is probable.

### 5.8 Tensor-polarized quark structures

The LL, LT, and TT quark functions arise from the shared deuteron
spin-density parent, S-D and OAM interference, Wilson-channel response, and
operator-valued nuclear maps. In particular, \(g_{1LT}\) and \(g_{1TT}\)
were added in two controlled stages:

1. direct helicity/OAM interference envelopes with correct rank and spin
   transformation properties;
2. a screened eikonal/gauge-link realization benchmarked against its
   zero-phase and weak-phase limits.

The two are not averaged into a fake precision result. They are correlated
model alternatives inside the named phase/OAM axes. The tensor functions
are constrained by the common parent, positivity, symmetry, pure-S and
zero-phase limits, and the inclusive tensor benchmark, but most are not
direct experimental extractions.

## 6. Nucleon-level gluon content

### 6.1 Unpolarized and helicity anchors

The canonical gluon \(f_1^g\) central boundary uses the matched BSV19/NNPDF31
construction, with an additional CT18 29-pair Hessian linear-response study
propagated through the AV18 light-front smearing at all five x nodes and 61
transverse-momentum points. The matched central and the CT18 uncertainty
response are retained as distinct provenance layers.

Gluon \(g_1^g\) uses BDSSV24-NLO. All 600 replicas are propagated. The
transverse-width envelope is stored separately because it reshapes the local
TMD while leaving the finite-grid collinear integral nearly stable.

### 6.2 T-even linear polarization and spin-orbit functions

\(h_1^{\perp g}\), \(g_{1T}^g\), \(h_1^g\), and
\(h_{1T}^{\perp g}\) are projections of a retained gluon light-front
overlap/OAM/Wilson parent. They are not copies of quark functions. The
construction includes gluon polarization tensors, the allowed transverse
ranks, parton-target helicity interference, and positivity of the joint
density.

### 6.3 Gluon T-odd dynamics

The project first used a downstream spectator-inspired rescaling of the
assembled deuteron \(f_1^g\). That was useful as a literature comparison but
bypassed the common parent and is not canonical.

The accepted construction instead generates the gluon T-odd channels in the
project's nucleon-level light-front correlator, keeps \(f\)-type and
\(d\)-type link/color vertices independent, and then propagates them through
the nuclear kernel. External spectator calculations are benchmarks for
nodes, signs, and hierarchy, not replacements for the project's parent.
This supplies \(f_{1T}^{\perp g}\), \(h_{1L}^{\perp g}\), \(h_1^g\), and
\(h_{1T}^{\perp g}\) without assuming one universal phase.

Absolute gluon T-odd magnitudes are still model dependent. Process-level
predictions must apply the appropriate color weights and keep the f/d
uncertainty explicit.

### 6.4 Tensor-polarized gluons

All declared LL, LT, and TT gluon functions are produced from the shared
gluon light-front/OAM parent with deuteron spin-density projections and
operator nuclear response. The previously missing \(g_{1LT}^g\) and
\(g_{1TT}^g\) receive predictions through S-D/OAM interference and screened
eikonal phases, with pure-S, zero-phase, link-reversal, rank, and positivity
tests. As in the quark sector, these are physically constrained predictions,
not fitted measurements.

## 7. Deuteron light-front and nuclear structure

### 7.1 Realistic two-nucleon wave functions

The central deuteron wave function is AV18. Nuclear model dependence is
estimated with CD-Bonn and four Norfolk chiral interactions (NV-Ia, NV-Ib,
NV-IIa, NV-IIb). The light-front construction includes:

- S-wave and D-wave radial components;
- SS, SD, DS, and DD overlap terms;
- target and active-nucleon helicity indices;
- Melosh/light-front spin rotations;
- normalization and finite-quadrature audits;
- pure-S and nonrelativistic controlled limits.

The D state is not represented only by one scalar probability. Its
interference with the S state and its helicity dependence feed the vector,
tensor, OAM, and spin-orbit sectors.

### 7.2 Impulse approximation and resolved constituents

Proton and neutron correlators are embedded separately in the deuteron
spectral density. The impulse result retains constituent flavor and
helicity information until observable assembly. This supports inclusive and
tagged projections, controlled charge symmetry, CSB, and different nuclear
responses.

### 7.3 Binding, Fermi motion, and off-shell response

Longitudinal light-front smearing supplies binding and Fermi motion. Off-shell
response is applied through channel-aware correlator maps, not through one
universal multiplicative factor. Number, momentum, and tensor moments are
tracked in a ledger so incompatible corrections cannot be hidden by final
renormalization.

### 7.4 Shadowing and antishadowing

The unpolarized small-x shadowing baseline is tied to a diffractive
PDF/Frankfurt-Guzey-Strikman-type input. Polarized and tensor responses are
implemented as separate configurable operator maps because inclusive data do
not fix them. Antishadowing is treated as a distinct compensating mechanism
with its own domain and moment constraints.

The final WP12 composition uses ordered completely positive (Kraus) maps on
the joint target-spin x parton-spin density for shadowing, antishadowing, and
off-shell blocks. This preserves hermiticity and positivity and makes the
order of noncommuting responses explicit. Maximum recomposition shifts in
the inspected boundary are about 2.73% of local \(f_1\) for quarks and 2.91%
for gluons.

### 7.5 Pion exchange and the \(NN\pi\) component

The pion/meson sector is based on a sourced Sullivan-type convolution and a
spin-resolved light-front \(NN\pi\) correlator. It uses the project pion
parton/TMD inputs and contributes only in operator channels supported by the
mechanism. The pion term is included once in the composition graph; it is
not double counted as both a wave-function member and an additive correction.

The HERMES \(b_1\) comparison tests the sum of the one-body tensor impulse
piece and the allowed pion contribution. This is a benchmark of a specific
collinear tensor marginal, not a fit of every tensor TMD.

### 7.6 Non-nucleonic, SRC, Delta-Delta, and hidden-color sectors

The architecture provides replaceable interfaces and correlated sensitivity
members for short-range/cluster structure, Delta-Delta-like components, and
hidden-color configurations. These sectors are not inserted
indiscriminately:

- a sourced transverse/color-resolved correlator is required for a nonzero
  preferred central term;
- otherwise the mechanism is zero-centered with an explicit sensitivity
  envelope;
- overlap with pion, SRC, or shared-Fock amplitudes is forbidden by the
  composition graph;
- each member carries its domain, moment effect, and provenance.

The intrinsic hidden-color central contribution is currently excluded, not
silently set equal to an arbitrary fraction of \(f_1\).

## 8. OAM, spin-orbit, gauge-link, and representation structure

The correlator construction retains orbital sectors sufficient to represent
\(L_z=0,\pm1,\pm2\) interference patterns. The allowed change in target,
parton, and orbital helicity determines the transverse rank and the azimuthal
tensor multiplying each named TMD. This is the concrete use of
representation theory in the project: the spin-1 density decomposes into
scalar, vector, and rank-2 tensor irreducible sectors, and the transverse
rotation weight organizes the allowed projections.

The algebraic machinery has four practical purposes:

1. it prevents a coefficient with one transverse rank from being reused for
   another;
2. it maps retained helicity matrices to the U/L/T/LL/LT/TT basis;
3. it exposes null limits caused by missing helicity/OAM interference;
4. it allows positivity to be tested on the full density rather than on
   unrelated curves.

No topological or quantum-circuit construction was added decoratively.
PennyLane was investigated as an optional representation/validation tool,
but no circuit was adopted because the analytic finite-dimensional
spin-coupling maps and density-matrix tests already provide a clearer,
exactly benchmarkable implementation. This remains replaceable if a future
quantum-state parameterization supplies a concrete computational advantage.

Gauge-link dependence is represented by Wilson-channel amplitudes and
future/past staple orientation. T-even functions remain invariant under
staple reversal; T-odd functions reverse sign. Quark process dependence and
the two gluon color/link classes remain distinct. A phase is attached to the
physical interference that produces a T-odd projection, not multiplied
universally onto every function.

## 9. Nuclear composition and no-double-counting rules

Every canonical contribution is labeled as one of:

- **baseline:** the unique parent component required for the central model;
- **additive mechanism:** a physically distinct operator contribution that
  may be summed once;
- **exclusive alternative:** a model choice that replaces, rather than adds
  to, another amplitude;
- **uncertainty member:** a replica, Hessian member, parameter corner, wave
  function, or scenario used to make a named band.

The composition graph rejects ambiguous paths. Named TMDs are projected only
after compatible correlator components have been composed. This is essential
because two models can produce similar-looking \(F(x,k_T)\) while
representing the same underlying rescattering or OAM amplitude and therefore
must not both be added.

The currently inspected total includes the impulse parent, the supported
operator-valued nuclear responses, and the sourced \(NN\pi\) contribution.
Shared-Fock/OAM, Delta-Delta, hidden-color/SRC, phase, wave-function, and
color alternatives remain correlated axes unless the contribution graph
specifically marks them additive.

## 10. Uncertainty and evidence architecture

The project does not combine all bands into a single confidence interval.
The following meanings are kept separate:

| Axis | Meaning |
|---|---|
| PDF/TMD replica | Statistical or posterior member variation supplied by an external fit |
| Hessian | Eigenvector propagation supplied by a PDF fit |
| Published interval hull | Extremal propagation of reported parameter intervals; not automatically a confidence region |
| Wave-function envelope | Dependence on AV18, CD-Bonn, and Norfolk nuclear wave functions |
| Transverse-profile envelope | Sensitivity to nonperturbative \(k_T\) or \(b_T\) shape |
| Gauge-phase/color scenario | Model dependence of rescattering and gluon f/d structure |
| Nuclear-mechanism envelope | Off-shell, shadowing, antishadowing, pion, and non-nucleonic response choices |
| OAM/Fock envelope | Alternative allowed spin-orbit interference content |
| CSB power-counting envelope | Zero-centered estimate of omitted isospin breaking; not a fit uncertainty |
| Numerical error | Quadrature, transform truncation, interpolation, and closure residuals |

The global CSB envelope is 5% for quark TMDs and 2% for gluon TMDs, with a
rank-aware \(f_1\) floor. It is a sourced power-counting sensitivity, not a
confidence interval. Quark \(f_1\) additionally retains the independent
MSHT20-QED CSB calculation.

Smooth production curves are built from dense evaluations and shape-preserving
PCHIP interpolation. Earlier nine-knot lines are diagnostic sketches and are
not used as production figures. Bands are regenerated from named ensembles,
not obtained by adding visual percentages to the central line.

## 11. Evidence status of all 36 projections

### 11.1 Quarks and antiquarks

| Function(s) | Central evidence | Current interpretation |
|---|---|---|
| \(f_1\) | CT18NNLO; MSHT20-QED CSB; CT18 Hessian | strongest collinear anchor plus modeled transverse profile |
| \(g_1\) | BDSSV24-NLO, 600 replicas | phenomenological polarized anchor |
| \(h_1\) | JAMDiFF plus lattice-informed ensemble | fit+lattice anchor |
| \(f_{1T}^\perp\) | BPV20 arTeMiDe, 500 replicas | fitted T-odd anchor with process reversal |
| \(g_{1T}\) | Yang et al. 2024 | central fit plus asymmetric interval hull and sea sensitivity |
| \(h_{1L}^\perp\) | JAMDiFF \(h_1\) plus WW relation | fit+lattice+model |
| \(h_1^\perp\) | BPV20-linked hierarchy scenarios | model, not a direct fit |
| \(h_{1T}^\perp\) | positivity-bounded OAM model | model sensitivity |
| all LL/LT/TT functions | shared AV18 S-D/OAM/Wilson parent plus operator nuclear response | wave-function+model+phenomenology; mostly predictions |

### 11.2 Gluons

| Function(s) | Central evidence | Current interpretation |
|---|---|---|
| \(f_1^g\) | BSV19/NNPDF31 central; CT18 Hessian response | phenomenological anchor plus nuclear/profile systematics |
| \(g_1^g\) | BDSSV24-NLO, 600 replicas | polarized phenomenological anchor |
| all other U/L/T/LL/LT/TT functions | shared gluon LF overlap/OAM/Wilson parent with independent f/d link sectors | wave-function+model predictions with named evidence axes |

Thus every projection has a reproducible prediction and an uncertainty or
sensitivity representation, but only a subset has direct fit or lattice
precision. The term "at the \(f_1\) level" refers to provenance,
replaceability, constituent resolution, nuclear dressing, and validation,
not equal experimental information.

## 12. Validation performed

### 12.1 Exact and representation-level tests

The implementation tests:

- hermiticity of quark and gluon correlators;
- parity transformation rules;
- future/past staple reversal and T-even/T-odd behavior;
- independent gluon f/d link/color identity;
- spin-1 target-density reconstruction;
- allowed transverse rank and origin limits;
- support in x and declared kinematic domain;
- projection closure from retained correlators to named TMDs;
- proton/neutron and charge-symmetric limits;
- pure-S, zero-phase, and weak-phase limits;
- common-parent and component recomposition closure.

### 12.2 Positivity and normalization

Positivity is checked through eigenvalues of the joint target-parton density
and through applicable rank-weighted bounds. At the WP12 inspection:

- minimum quark density eigenvalue: approximately \(4.13\times10^{-4}\);
- minimum gluon density eigenvalue: approximately \(2.09\times10^{-2}\);
- no final positivity contraction was required;
- the common completion scale remained exactly one.

Wave-function normalization, finite quadrature, Fourier-Bessel transforms,
TMD/PDF marginals, and number/momentum/tensor moment ledgers have independent
checks.

### 12.3 Physical benchmarks

The benchmark set includes:

- flavor-resolved unpolarized and helicity PDFs;
- transversity and Sivers input reproduction;
- HERMES \(b_1\) with impulse and pion components;
- deuteron body form factors and current/angular-condition diagnostics;
- TMD-to-PDF and GTMD-to-GPD reductions;
- SIDIS/Drell-Yan T-odd sign reversal;
- wave-function comparisons across six deuteron models;
- controlled small-phase, pure-S, and one-body boundaries;
- literature hierarchy and node comparisons for model-dependent gluon
  structures.

### 12.4 Acceptance state

The final WP12-E audit reports:

- 36 of 36 evidence rows pass;
- resolved parent closure passes;
- complete quark and gluon bases pass;
- PDF uncertainty propagation passes;
- CSB treatment passes;
- all bands are ordered.

The full repository regression after WP12-E closure passed 480 tests. The
accepted scope is explicitly the leading-twist forward boundary at \(Q=5\)
GeV before complete rank-aware evolution.

## 13. What the present plots show

The primary atlases show the **deuteron** TMD \(F(x,k_T;Q)\), not separate
free-proton and free-neutron predictions. Constituent audit plots are
secondary diagnostics and are labeled accordingly. Close \(u_D\) and
\(d_D\) curves can emerge in an isoscalar deuteron, but the resolved parent
must show the unequal proton flavor content and its neutron mapping.

Every panel uses the same named-TMD convention and smooth central line.
Positive-rank coefficients may be finite at \(k_T=0\), while their physical
tensor modulation vanishes with the required power of \(k_T/M\). Therefore
one must distinguish:

- the named coefficient \(F\);
- a rank-weighted physical modulation;
- the optional ratio of that modulation to \(f_1\).

The preferred all-TMD comparison plots use \(F\) consistently. Ratios are
supplemental diagnostics rather than the primary presentation.

## 14. What is complete and what is not

### Complete at the declared pre-evolution scope

- the 18 quark/antiquark and 18 gluon leading-twist forward projections;
- explicit \(u,d,\bar u,\bar d\) and proton/neutron resolution;
- independent gluon f/d link/color sectors;
- vector and tensor U/L/T/LL/LT/TT target structure;
- shared GTMD/correlator parent and projection machinery;
- realistic deuteron S/D wave functions with six-model envelope;
- spin, OAM, spin-orbit, and gauge-phase interference structures;
- impulse, off-shell, shadowing, antishadowing, pion, and configurable
  non-nucleonic mechanisms with no-double-counting rules;
- named uncertainty/evidence axes;
- smooth dense tables and plots;
- symmetry, positivity, marginal, closure, moment, and benchmark tests.

### Model dependent but explicitly represented

- Boer-Mulders absolute normalization;
- pretzelosity and genuine WW-breaking amplitudes;
- most tensor-polarized TMDs beyond the \(b_1\) marginal;
- polarized and tensor shadowing;
- gluon linear-polarization and T-odd absolute magnitudes;
- process-specific gluon f/d mixtures;
- shared-Fock/OAM, Delta-Delta, SRC, and hidden-color sensitivities;
- nonperturbative transverse profiles in poorly constrained sectors.

### Not yet complete

- a uniform common-scheme, rank-aware evolution of every projection over
  multiple Q values;
- a complete process-specific fixed-order \(Y\) term at high transverse
  momentum;
- a global simultaneous fit of all quark, gluon, vector, and tensor sectors;
- complete cross-section predictions with process hard factors and
  fragmentation functions for every channel;
- full nonzero-skewness GTMD phenomenology and polynomiality validation;
- first-principles lattice determinations for most gluon and tensor TMDs.

These limitations are not replaced by zeros or arbitrary universal ansatze.
They have interfaces, configurable defaults, evidence labels, and tests.

## 15. Reproducible artifacts

The authoritative resolved and composed parents are:

- `outputs/parent_tmds/wp12_resolved_quark_parent.csv`;
- `outputs/parent_tmds/wp12_resolved_quark_parent.correlators.csv`;
- `outputs/parent_tmds/wp12_resolved_gluon_parent.csv`;
- `outputs/parent_tmds/wp12_resolved_gluon_parent.correlators.csv`;
- `outputs/parent_tmds/wp12_canonical_composed_quark.csv`;
- `outputs/parent_tmds/wp12_canonical_composed_gluon.csv`.

The principal machine-readable audits are:

- `outputs/validation/wp12_items1_5_acceptance.json`;
- `outputs/validation/wp12_scientific_inspection.json`;
- `outputs/validation/wp12_resolved_nuclear_parent.json`;
- `outputs/validation/wp12_evidence_parity_matrix.json`;
- `outputs/validation/wp12e_acceptance.json`.

The primary inspection plots and their dense band tables are:

- `output/figures/wp12_inspection/wp12_quark_all_tmd_F_x010.png`;
- `output/figures/wp12_inspection/wp12_gluon_all_tmd_F_x010.png`;
- `output/figures/wp12_inspection/wp12_quark_inspection_bands.csv`;
- `output/figures/wp12_inspection/wp12_gluon_inspection_bands.csv`.

The current full validation command is:

```bash
PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl \
  /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

The note's PDF edition is generated with:

```bash
/Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_model_construction_note.py
```

## 16. Provenance map

The following repository notes provide the detailed evidence behind this
synthesis:

- `Deuteron_GTMD.pdf`: original GTMD-first formal proposal;
- `references/production_tmd_architecture_audit.md`: why the reduced
  complete-looking closure was superseded;
- `references/overall_quark_gluon_consistency_audit.md`: unequal-depth audit
  and canonical work packages;
- `references/wp11_final_acceptance_audit.md`: common-parent C1-C7 closure;
- `references/wp12_scientific_inspection.md`: pre-evolution physics
  inspection;
- `references/wp12e_acceptance.md`: evidence-parity acceptance;
- `references/quark_correlator_conventions.md` and
  `references/spin1_representation_map.md`: operator and spin conventions;
- `references/bpv20_sivers_input.md`,
  `references/transversity_input.md`,
  `references/pretzelosity_input.md`, and
  `references/quark_axial_tensor_todd.md`: quark-sector inputs;
- `references/gluon_todd_source_audit.md`,
  `references/lattice_gluon_tmd_audit.md`, and
  `references/pvglue20_benchmark.md`: gluon evidence and limits;
- `references/lfheft_nnpi_source_audit.md`,
  `references/pion_transverse_boundary.md`,
  `references/h1_dpdf_shadowing_input.md`, and
  `references/gluon_nuclear_mechanism_boundary.md`: nuclear mechanisms;
- `references/uncertainty_axis_contract.md`,
  `references/tmd_scheme_contract.md`, and
  `references/moment_ledger_contract.md`: numerical contracts;
- `handoff/decisions.md`: living record of consequential choices;
- `handoff/worklog.md`: chronological implementation and validation record.

## 17. Bottom line before evolution

The project began with the correct GTMD-first idea but initially realized
only a narrow real one-body boundary. It then briefly produced a smooth but
overly generic complete-looking TMD closure. The decisive refocusing was to
restore the full parent machinery, keep proton/neutron and flavor information
until final deuteron assembly, introduce physically distinct gauge-link,
spin/OAM, tensor, and nuclear mechanisms, and make evidence quality a
machine-enforced property rather than an implication of smooth plots.

The result is now a complete, flavor-resolved, spin-resolved, leading-twist
forward boundary model at \(Q=5\) GeV. Its strongest sectors inherit modern
PDF, helicity, transversity, and Sivers ensembles. Its less constrained
tensor and gluon sectors are genuine shared-parent predictions with explicit
model axes, not hidden universal rescalings. The deuteron contains realistic
S/D light-front dynamics, constituent resolution, nuclear corrections, and
non-nucleonic interfaces. Symmetry, positivity, closure, moments, controlled
limits, and benchmark observables are tested.

This is the appropriate boundary to evolve. Evolution should now transport
this structure without erasing rank, flavor, polarization, color/link,
constituent, mechanism, or uncertainty provenance.
