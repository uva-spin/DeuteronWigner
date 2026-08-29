# Overall quark/gluon TMD consistency audit

Date: 2026-07-26

Status: scientific integration audit; canonical-production gate reopened

## Executive finding

The repository has a complete leading-twist spin-1 operator basis, retained
helicity correlators, extensive symmetry/positivity tests, realistic
deuteron S/D wave functions, and many well-separated phenomenological and
model inputs. It is therefore a strong framework. It does **not** yet have a
single canonical quark-plus-gluon prediction in which every contribution is
composed through the same parent chain at a common TMD scheme and scale.

The main problem is not missing names. It is unequal dynamical depth:

- \(f_1\), \(g_1\), quark transversity, quark Sivers, and the collinear
  tensor benchmark have the strongest phenomenological anchors.
- quark Boer--Mulders, pretzelosity, genuine WW breaking, polarized/tensor
  shadowing, and non-nucleonic transverse structure are controlled model
  sectors.
- quark \(g_{1LT}\), \(g_{1TT}\) and all non-Sivers gluon T-odd structures
  are exploratory phase/rescattering predictions.
- the latest gluon T-odd model is attached to the assembled deuteron
  \(f_1^g\), rather than generated first at proton/neutron amplitude level
  and propagated through the nuclear light-front convolution. It therefore
  bypasses the governing parent architecture and cannot be the canonical
  central result.

No evidence of deliberate numerical inflation was found in the fitted
inputs. However, several model coefficients set absolute sizes without data
or a derived normalization. Positivity is a necessary ceiling, not evidence
that a value near the ceiling is likely.

## Evidence hierarchy by sector

| Sector | Present input | Assessment |
|---|---|---|
| quark \(f_1\) | CT18/MSHT20-QED, flavor and nucleon resolved | strong collinear anchor; transverse widths remain model/fit-informed |
| quark \(g_1\) | BDSSV24 with retained nuclear spin convolution | strong phenomenological anchor |
| quark \(h_1\) | JAMDiFF plus lattice-informed ensemble | strong, with documented positivity projection |
| quark Sivers | BPV20 500 replicas and released arTeMiDe evolution | strongest T-odd sector |
| quark Boer--Mulders | flavor coefficients proportional to Sivers | realistic sensitivity model, not a joint fit |
| quark \(g_{1T}\) | Yang-2024 central; sea-zero fit boundary | phenomenological central but incomplete covariance/evolution |
| quark \(h_{1L}^{\perp}\) | WW relation plus configurable breaking | theoretically organized; genuine term unconstrained |
| quark pretzelosity | fraction of positivity moment or OAM scenario | plausible nonperturbative sensitivity, not a determination |
| quark \(g_{1LT},g_{1TT}\) | direct phase envelope and screened eikonal | exploratory; direct phase magnitude is not data normalized |
| gluon T-even | PDF/helicity anchors plus spin-1 convolution | structurally sound; nonperturbative transverse profile weakly constrained |
| gluon Sivers | CGI-GPM f/d scenarios | phenomenological/model boundary with independent color classes |
| other spin-half gluon T-odd | source-informed spectator hierarchy | current code does not evaluate the published full formula |
| gluon \(g_{1LT},g_{1TT}\) | AV18 S--D factor times screened eikonal | exploratory spin-1 extension; coefficients are model choices |
| shadowing | inclusive DPDF/FGS anchor | U channel supported; polarized/tensor ratios are model scenarios |
| pion exchange | Miller spin-resolved kernel and JAM21/Vpion inputs | strong tensor-collinear contribution; transverse coupled NNpi amplitude incomplete |
| effective cluster | sourced cluster LFWF sensitivity | not yet a color-resolved production parton TMD |

## Cross-sector consistency checks

### Constraints that are implemented correctly

1. The 18 quark and 19 gluon leading-twist names are defined through the
   spin-1 correlator decomposition rather than a common quark/gluon ansatz.
2. Quark flavors \(u,d,\bar u,\bar d\) and active proton/neutron sources are
   retained through the impulse calculation.
3. Hermiticity, target-spin representation structure, transverse rank,
   future/past reversal, f/d gluon color identity, support, and full-density
   positivity have direct tests.
4. AV18, CD-Bonn, and Norfolk wave-function dependence is propagated in the
   main impulse ensemble with explicit SS/SD/DS/DD terms.
5. Alternative fit, phase, OAM, shadowing, pion, cluster, and color members
   have non-additive combination policies. The ledger does not silently sum
   them.
6. Model envelopes are generally labeled as sensitivity rather than
   confidence intervals.

### Material inconsistencies and omissions

1. **No canonical composition graph.** The WP10 ledger is an inventory of
   alternative members, not one physically composable prediction. It does
   not prove that every selected contribution can be summed without overlap.
2. **Gluon T-odd parent bypass.** `SpectatorInformedGluonTOdd` multiplies the
   assembled deuteron \(f_1^g\). It does not construct distinct proton and
   neutron spectator correlators or propagate them through the LF nuclear
   kernel. Spin-1 tensor functions are added downstream.
3. **Published spectator calculation not reproduced.** The present
   \(0.22,0.31,0.055,-0.018\) coefficients and analytic tail encode the
   reported hierarchy and nodes, but are not the full spectral-mass and
   master-integral calculation of arXiv:2402.17556.
4. **Potential artificial gluon normalization.** At the central scenario,
   maxima of \(|F|/f_1^g\) are approximately 0.31 for \(h_1^g\), 0.22 for
   Sivers, 0.053 for \(h_{1L}^{\perp g}\), and 0.025 for
   \(h_{1T}^{\perp g}\). These pass positivity without any cap, but their
   absolute scale is selected by model coefficients rather than a Q=5 fit.
5. **Quark tensor-phase gap.** The direct quark \(g_{1LT},g_{1TT}\) phase
   envelope is orders of magnitude above the explicit one-gluon result.
   Both are valid alternatives, but neither supplies a preferred
   probability-weighted central prediction.
6. **Evolution is heterogeneous.** BPV20 Sivers uses its released optimal
   TMD evolution; several Gaussian, WW, pretzelosity, tensor-phase, and
   gluon spectator inputs are frozen, broadened, or transplanted to Q=5
   under different prescriptions. Comparing them on one plot does not make
   them one common soft-subtracted scheme.
7. **Nuclear corrections are not uniformly propagated.** The rich quark
   parent applies impulse, off-shell, shadowing, and antishadowing at
   correlator level. The new gluon T-odd export uses the AV18 impulse base
   only. Pion and cluster sectors remain separate and are not yet composed
   with all compatible channels.
8. **Polarized/tensor shadowing is weakly determined.** The inclusive
   diffractive anchor is sound, but axial, transverse, LL, LT, TT, circular,
   and linear responses are independent ratios. They should not define a
   preferred central curve until constrained.
9. **High-\(k_T\) completion remains observable dependent.** The intrinsic
   low-\(k_T\) W term has no sourced fixed-order Y term. All comparisons must
   retain their declared low-\(k_T\) validity.
10. **Positivity does not choose dynamics.** Full-matrix positivity tests
    successfully reject impossible amplitudes, but cannot rank allowed
    phase models or justify saturation fractions.

## Required canonical-model work packages

### C1 — Contribution graph and no-double-counting contract

For every TMD, classify each contribution as baseline, additive mechanism,
exclusive alternative, or uncertainty member. Define amplitude identities
and forbid combinations sharing the same physical interference. Completion:
one machine-readable graph and tests that every canonical row has exactly
one allowed composition path.

### C2 — Common scale/scheme contract

Assign every input an initial scale, soft-subtraction scheme, rapidity scale,
matching order, rank-aware transform, and Q=5 evolution route. Inputs without
a valid route remain comparison-only. Completion: scheme metadata for every
canonical TMD and round-trip/evolution tests by transverse rank.

### C3 — Nucleon-level gluon T-odd calculation

Implement the published full \(g_1+g_2\) spectator master integrals and
spectral-mass distribution for the four spin-half functions. Keep f/d
vertices independent. Build proton and neutron correlators before nuclear
convolution. Completion: reproduce representative source curves at
\(Q_0=1.64\) GeV, including the \(h_{1L}^{\perp g}\) node and hierarchy,
then propagate through the same LF kernel and documented evolution
scenarios.

### C4 — Spin-1 tensor T-odd amplitude construction

Replace downstream \(f_1^D\)-scaled \(g_{1LT},g_{1TT}\) with interference
matrix elements of the nuclear LF amplitudes and the eikonal kernel.
Completion: explicit SS/SD/DS/DD and proton/neutron component closure,
pure-S and zero-phase limits, rank covariance, and positivity after full
composition.

### C5 — Quark model-sector calibration

Keep BPV20/JAMDiFF/Yang inputs as anchors. Compare Boer--Mulders,
pretzelosity, WW breaking, and tensor phases against all applicable SIDIS,
DY, lattice, and weighted-moment constraints without reusing one fitted
phase as another operator. Completion: a preferred conservative central
member only where evidence supports it; otherwise zero-centered or
multi-model sensitivity bands.

### C6 — Nuclear mechanism propagation

Compose off-shell, antishadowing, shadowing, pion, and cluster contributions
only into channels supported by their operators. Apply the same mechanism
ledger to quark and gluon parents without copying response factors.
Completion: component closure, number/momentum/tensor sum rules, and
no-double-counting tests at representative small, intermediate, and large x.

### C7 — Global validation observables

Validate not only individual TMDs but compatible sets through \(b_1\),
unpolarized and polarized PDFs, tensor moments, SIDIS/DY sign reversal,
available azimuthal asymmetries, lattice moments/ratios, and prospective EIC
gluon observables. Completion: observable predictions assembled with
process-specific hard/color weights and a residual table by input sector.

## Canonical-status recommendation

Until C1--C4 are complete:

- retain the parent-derived T-even quark/gluon ensemble and fitted quark
  TMD inputs as the canonical baseline;
- present OAM, tensor-phase, polarized-shadowing, cluster, and non-Sivers
  gluon T-odd results as named sensitivity studies;
- do not combine the old rank-scaled and new spectator-informed gluon T-odd
  tables;
- do not describe the new gluon T-odd band as production uncertainty or a
  published spectator-model reproduction;
- do not use positivity saturation or the absence of a cap as a likelihood
  argument.

## Source anchors

- Complete spin-1 quark/gluon leading-twist decomposition:
  arXiv:1612.06585.
- T-odd spin-half gluon spectator calculation:
  arXiv:2402.17556.
- Small-x worm-gear/pretzelosity constraints:
  arXiv:2310.02231.
- Detailed component provenance is retained in
  `references/rich_spin1_extensions.md`,
  `references/pretzelosity_input.md`,
  `references/quark_axial_tensor_todd.md`, and the WP10 ledger.
