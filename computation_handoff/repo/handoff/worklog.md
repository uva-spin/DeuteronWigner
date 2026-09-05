# Work log

## 2026-07-24 - Polarized transverse-width sensitivity

- Parameterized `compute_gluon_helicity_response.py` by the polarized
  Gaussian width and output stem.
- Repeated the exact full-600-replica AV18 response at widths 0.15 and
  \(0.40\ {\rm GeV}^2\), bracketing the \(0.25\ {\rm GeV}^2\) baseline.
- Added `scripts/analyze_gluon_helicity_uncertainties.py` and generated
  `gluon_helicity_uncertainty_components.npz/.csv`, which preserves PDF,
  wave-function, and width components independently.
- At the grid node nearest the origin, the width envelope has maximum
  relative excursions of 62% for \(g_1^g\) and 168% for \(g_{1T}^g\).
  This is a local shape sensitivity, not a probabilistic error.
- The finite-grid integrated central \(g_1^g\) values are 0.752131,
  0.752115, and 0.751578 for widths 0.15, 0.25, and
  \(0.40\ {\rm GeV}^2\), demonstrating collinear stability within about
  \(7\times10^{-4}\).
- Verification: all 129 tests pass.
- Next: constrain or replace the Gaussian transverse profile using
  independently justified gluon-TMD information before constructing a
  combined presentation band.

## 2026-07-24 - Full BDSSV24 replica uncertainty

- Expanded the project-local BDSSV24 set to all 600 replicas plus member 0;
  verified 601 nonempty data files. The local set occupies about 479 MB.
- Ran the exact AV18 helicity-response kernel over the full ensemble and
  saved `outputs/stage0/uncertainty/gluon_helicity_bdssv24_full.npz/.csv`.
- Near the grid node closest to the origin, the full replica standard
  deviation is 13.85% for \(g_1^g\) and 14.20% for \(g_{1T}^g\), relative
  to their central values.
- The corresponding normalized six-wave-function spreads are about 1.3%
  and 54%. Polarized-PDF uncertainty therefore dominates \(g_1^g\), while
  wave-function dependence dominates the much smaller \(g_{1T}^g\).
- Nested subsets fluctuate appreciably even at several hundred replicas,
  confirming that the full ensemble was preferable to assigning a
  production band from the 31- or 101-member pilots.
- The full \(g_{1LT}^g\) replica field remains numerical zero and is not
  assigned a relative uncertainty.
- Verification: all 129 tests pass.
- Next: add transverse-width sensitivity for the polarized gluon input and
  combine the separately stored PDF, wave-function, and numerical
  components only at the presentation layer.

## 2026-07-24 - Fast BDSSV24 replica pilot

- Downloaded a deterministic 31-replica pilot subset at member indices
  1, 21, ..., 581, 600, spanning the complete BDSSV24 replica index range.
- Added `scripts/compute_gluon_helicity_response.py`. It groups the
  light-front quadrature by active-nucleon fraction and precomputes the
  exact linear response of \(g_1^g\), \(g_{1T}^g\), and \(g_{1LT}^g\) to
  the input values \(\Delta g(z,Q)\).
- The response result matches the independent direct AV18 central grid to
  relative \(L_2\) errors \(1.1\times10^{-15}\) for \(g_1^g\) and
  \(2.5\times10^{-15}\) for \(g_{1T}^g\).
- The 31-replica pilot estimates near-origin relative PDF uncertainties of
  11.5% for \(g_1^g\) and 11.7% for \(g_{1T}^g\).
- Nested subsets spanning the full replica range show that 31 members are
  not converged: the 20-member standard-deviation fields differ from the
  31-member pilot by 9.6% and 11.5%, respectively.
- The T-odd \(g_{1LT}^g\) response remains numerical zero; relative
  uncertainty ratios for that channel have no physical meaning.
- Output:
  `outputs/stage0/uncertainty/gluon_helicity_bdssv24_pilot.npz/.csv`.
- Verification: all 129 tests pass.
- Next: expand to at least about 100 replicas, repeat nested convergence,
  and continue to the full 600 only if the uncertainty field has not
  stabilized.

## 2026-07-24 - Polarized gluon input and circular sectors

- Downloaded the metadata and central member of the current BDSSV24-NLO
  polarized proton set from the official LHAPDF archive into
  `data/raw/lhapdf/BDSSV24-NLO/`; recorded SHA-256 checksums.
- Added `PolarizedLHAPDFProvider`, which prepends the project-local data
  root without modifying the user's global LHAPDF installation.
- Validated the set domain and central value
  \(\Delta g(0.1,Q=2\ {\rm GeV})=0.8274285012\).
- Added deuteron L/T/LT target-channel projection and extended all six
  production gluon TMD grids with \(g_1^g\), \(g_{1T}^g\),
  \(g_{1LT}^g\), and their accompanying projected structures.
- The full-grid maximum is about 0.933 for \(g_1^g\) and
  \(7.71\times10^{-3}\) for \(|g_{1T}^g|\). The T-odd
  \(g_{1LT}^g\) stays below \(1.2\times10^{-17}\).
- Across all nominally T-odd output channels the largest numerical leakage
  is \(1.1\times10^{-12}\), from \(h_{1L}^{\perp g}\); the other checked
  channels lie between \(10^{-13}\) and \(10^{-17}\).
- Near the grid node closest to the origin, the normalized six-wave spread
  is 1.3% for \(g_1^g\) and 54% for the much smaller \(g_{1T}^g\).
- Added two local-PDF tests; all 129 tests pass.
- Next: download a controlled subset or all of the 600 BDSSV24 replicas,
  propagate polarized-PDF uncertainty into \(g_1^g\) and \(g_{1T}^g\),
  and compare it separately with the nuclear wave-function band.

## 2026-07-24 - Gluon TMD convergence and wave-function bands

- Added external AV18 grid checks with 16, 24, and 32 points per transverse
  axis. The \(f_1^g\) marginal error decreases from
  \(1.13\times10^{-4}\) to \(2.17\times10^{-5}\) to
  \(1.42\times10^{-5}\); the \(f_{1LL}^g\) error decreases from
  \(1.49\times10^{-4}\) to \(3.38\times10^{-5}\) to
  \(2.38\times10^{-5}\).
- Compared AV18 internal quadratures \(12\times8\times8\),
  \(16\times12\times8\), and \(24\times16\times12\) at fixed 16-point
  external resolution. The coarse grid is rejected (normalization 0.917
  and about 8.4% U-sector relative \(L_2\) error).
- Relative to the fine internal grid, the production internal grid differs
  by about 0.46% for \(f_1^g\) and \(h_1^{\perp g}\), and below
  \(4.6\times10^{-4}\) for the LL grids.
- Added `scripts/analyze_gluon_tmd_grids.py` and generated the convergence
  summary plus full two-dimensional six-wave-function bands.
- Each wave-function grid is divided by its own recorded smearing
  normalization before forming the envelope.
- At the grid node nearest the origin, the normalized min-to-max spread is
  0.051% for \(f_1^g\), 0.10% for \(h_1^{\perp g}\), 28% for
  \(f_{1LL}^g\), and 19% for \(h_{1LL}^{\perp g}\). Tensor relative spreads
  are large partly because their means are small.
- Verification: all 127 tests pass.
- Next: add a physical polarized-nucleon gluon input for \(g_1^g\), then
  calculate the L/T/LT circular-gluon sectors and separate input-PDF
  uncertainty from nuclear wave-function uncertainty.

## 2026-07-24 - Retained-index gluon TMD grids

- Added `scripts/compute_gluon_tmd_ia.py`, including explicit conversion
  between internal \({\rm fm}^{-1}\) momenta and reported GeV TMD densities.
- Sampled \(f_1^g\), \(h_1^{\perp g}\), \(f_{1LL}^g\), and
  \(h_{1LL}^{\perp g}\) at \(x_N=0.1\), \(Q=2\) GeV for AV18, CD-Bonn, and
  all four Norfolk wave functions.
- Boundary settings are CT18NNLO, Gaussian width
  \(0.25\ {\rm GeV}^2\), `linear_fraction=0.5`,
  \(|k_{x,y}|\le1.6\) GeV, and 24 points on each axis. The linear fraction
  is a sensitivity choice, not a fitted result.
- The first AV18 run exposed an exact factor-two normalization mismatch.
  The cause was omission of the explicit per-nucleon factor in addition to
  the \(x_N=2x_D\) Jacobian. The corrected conversion is
  \(F_N=F_D/(4\hbar c^2)\) for these p+n parent conventions.
- After correction, all six numerical \(f_1^g\) marginals agree with their
  independent collinear convolutions within \(2.18\times10^{-5}\);
  \(f_{1LL}^g\) agrees within \(3.68\times10^{-5}\).
- Positive-rank scalar coefficient integrals are retained only as
  diagnostics; they are not collinear PDFs. Their full tensor structures,
  not the named scalar coefficient alone, must be angularly integrated.
- Direct integration of the reconstructed rank-two matrices on the saved
  square grids gives Frobenius residuals below \(9.4\times10^{-7}\) for
  the U linear-gluon term and \(3.1\times10^{-9}\) for the LL term across
  all six wave functions (the U residual is below \(7\times10^{-8}\)
  relative to the rank-zero marginal).
- The moderate internal quadrature has normalization 0.991--0.996, so a
  dedicated internal-grid convergence scan is required before interpreting
  percent-level wave-function differences in absolute TMD magnitudes.
- Verification: all 127 tests pass.
- Next: perform internal- and external-grid convergence, explicitly verify
  angular cancellation of the rank-two correlator terms, and then form
  wave-function uncertainty bands.

## 2026-07-24 - Nucleon gluon-TMD boundary model

- Added `GaussianSpinHalfGluonGTMD` as a declared, factorized nucleon input
  for the retained-index gluon convolution.
- Its \(f_1^g(x,k_T^2)\) is a normalized Gaussian anchored to a supplied
  collinear gluon PDF. An optional supplied helicity PDF defines
  \(g_1^g\); no helicity distribution is inferred from CT18NNLO.
- Added an optional bounded \(h_1^{\perp g}\) component controlled by the
  explicit `linear_fraction` parameter. This is a boundary assumption, not
  a spectator-model result or extraction from the collinear PDF.
- Added an optional factorized transverse-transfer slope for subsequent
  GTMD/Wigner scans.
- Added `project_deuteron_gluon_u_ll`, including the explicit relation
  between the spin-one LL basis coefficient and the physical named
  \(f_{1LL}^g=-(2/3)\delta_Tf_1^g\) convention.
- Tests verify the Gaussian collinear marginal, the linear-polarization
  bound, helicity sign reversal, transfer dependence, parameter validation,
  and exact U/LL named projection.
- Verification: all 127 tests pass.
- Next: sample the retained-index convolution on a physical \(k_T\) grid,
  integrate it back to the six collinear IA tables, and then quantify the
  induced U/LL/TT transverse structures as functions of the declared width
  and linear-gluon fraction.

## 2026-07-24 - Nucleonic collinear gluon baseline

- Extended the one-body GTMD convolution to retain both the active-nucleon
  helicity pair and the two gluon transverse indices. The nuclear result
  has shape `(deuteron_out,deuteron_in,gluon_i,gluon_j)`.
- Added a spin-1/2 collinear nucleon-gluon correlator containing the
  unpolarized and circular-gluon helicity structures. It has no
  symmetric-traceless gluon-index component.
- Verified structurally that a nuclear TT target projection can be nonzero
  while its symmetric-traceless gluon matrix, and hence collinear
  one-body \(h_{1TT}^g\), remains exactly zero.
- Added `scripts/compute_gluon_collinear_ia.py` and generated CT18NNLO
  \(Q=2\) GeV scans for AV18, CD-Bonn, NV-Ia, NV-Ib, NV-IIa, and NV-IIb in
  `outputs/stage0/gluon_collinear_ia_*.csv`.
- The tables report \(f_1^g\), \(\delta_T f_1^g\),
  \(f_{1LL}^g=-(2/3)\delta_T f_1^g\), their ratio, and the structural
  \(h_{1TT}^g=0\) flag over \(x_N=0.01\) through 0.7.
- The largest finite-quadrature normalization offset is about
  \(2.5\times10^{-3}\) for the Norfolk wave functions; tensor sum rules are
  satisfied at the \(10^{-15}\) level.
- Verification: all 121 tests pass.
- Next: introduce declared nucleon \(k_T\)-dependent gluon inputs for
  \(f_1^g\), \(g_1^g\), and \(h_1^{\perp g}\), then project the induced
  deuteron TMDs without relaxing the collinear \(h_{1TT}^g\) null test.

## 2026-07-24 - Gluon transverse-index correlator layer

- Added `src/deuteron_wigner/gluon_correlator.py` as an operator-only
  implementation of the transverse \(2\times2\) gluon correlator. It does
  not contain or call the spectator model.
- Implemented the unique split of a complex transverse correlator into its
  trace (unpolarized gluon), antisymmetric imaginary (circular gluon), and
  symmetric-traceless (linearly polarized gluon) components.
- Implemented compose/project round trips for the U, L, and LL target
  sectors, corresponding to Eqs. (7), (8), and (10) after translating
  \(g_T^{ij}=-\delta^{ij}\) to Euclidean Cartesian transverse indices.
- Extended the basis to the T, LT, and TT sectors of Eqs. (9), (11), and
  (12). Joint real design-matrix inversion over independent momenta and
  target polarizations recovers all identifiable coefficients and rejects
  rank-deficient or ill-conditioned ensembles.
- Found and encoded the exact two-dimensional TT identity: the
  \(f_{1TT}\) and \(h_{1TT}^{\perp}\) basis matrices differ only by sign, so
  \(\Phi^{ij}\) determines \(f_{1TT}-h_{1TT}^{\perp}\). This is the same
  combination projected in Appendix A of arXiv:2603.15224v1. The registry
  retains both names because the published formal inventory contains both.
- Added tests covering all six sector round trips, general matrix
  reconstruction, rotational covariance of every polarized basis matrix,
  invalid TT tensors, deficient ensembles, and the \(k_T=0\) degeneracy.
- Verification: the complete suite passes, 118 tests total; the focused
  correlator suite has 12 passing tests.
- Next: connect nucleon gluon inputs to the one-body deuteron convolution
  and enforce the spin-1/2 one-body null result for collinear
  \(h_{1TT}^{g}\).

## 2026-07-24 - Complete leading-twist quark/antiquark basis

- Added the authoritative definite-rank classification from
  arXiv:1612.06585 to the local literature archive and visually verified its
  color-coded Table I.
- Implemented complete 18-entry quark and 18-entry antiquark registries over
  U, L, T, LL, LT, and TT target channels. Each set contains nine T-even and
  nine T-odd functions.
- Encoded the four ordinary collinear limits
  \(f_1,g_1,h_1,f_{1LL}\) and the exceptional rank-zero T-odd
  \(h_{1LT}\), whose collinear integral vanishes by hermiticity and time
  reversal.
- Exported the combined 55-entry quark, antiquark, and gluon inventory to
  `outputs/stage0/leading_twist_tmd_registry.csv`.
- Added symmetric-traceless transverse tensors and Gram-normalized
  projectors through rank four, with trace, harmonic-contraction, and
  reconstruction tests.
- Implemented the exact published
  \(F_{U(LL)}^{\cos2\phi_h}\) transverse convolution kernel and verified
  rotational covariance.
- Added the standard convention adapter
  \(f_{1LL}=-(2/3)\delta_T f\).

## 2026-07-24 - Published quark/gluon TMD comparison

- Downloaded, checksummed, extracted, and visually inspected the formalism
  pages of Poudel et al., *Eur. Phys. J. A* 61, 81 (2025), and Xie, Chen,
  and Lu, arXiv:2603.15224v1.
- Established that EPJ A 61:81 is an experimental/formalism review, not a
  numerical deuteron quark-TMD model. Its Eqs. (5a)-(5e) nevertheless give
  the correct longitudinal-tensor SIDIS structure-function benchmark.
- Mapped the current rank-zero SIDIS calculation to
  \(F_{U(LL),T}=\mathcal C[f_{1LL}D_1]\), subject to an explicit
  `deltaT`-to-\(S_{LL}\) normalization adapter.
- Identified missing quark terms: the leading-twist rank-2
  \(F_{U(LL)}^{\cos2\phi_h}\) channel and the twist-3 \(\cos\phi_h\) and
  \(\sin\phi_h\) channels.
- Added a complete machine-readable registry for the 19 leading-twist
  spin-1 gluon TMDs in arXiv:2603.15224v1. It contains 13 T-even functions
  modeled in the paper and six T-odd functions that vanish at tree level.
- Recorded the clarified use boundary: the published gluon spectator model
  is not a project input or phenomenological baseline. The paper is used
  only to compare the operator correlator, tensor decomposition, ranks,
  signs, and resulting TMD definitions. In particular, collinear
  \(h_{1TT}^g\) remains a null test of the simple one-body spin-1/2 nucleon
  baseline.
- Wrote the detailed comparison and implementation sequence in
  `references/tmd_literature_comparison_2025_2026.md`.

## 2026-07-24 - Parent x scan, component structure, and convergence

- Extended the parent calculation across the HERMES \(x_N\) grid for the
  charge-weighted \(u,\bar u,d,\bar d\) combination.
- Made the conversion explicit:
  \(x_N=2x_D\), \(q_N(x_N)=q_D(x_D)/2\), and
  \(b_1=\delta_Tq_N/2\).
- Parent-derived \(b_1\) agrees with the independent collinear convolution
  within \(4.4\times10^{-10}\) across all six wave functions. The
  unpolarized finite-grid TMD-to-PDF error is below \(1.5\times10^{-5}\).
- Generated component-resolved Wigner arrays for all six wave functions,
  preserving `SS`, `SD`, `DS`, and `DD` separately.
- Added AV18 \(k_T\)-box, \(\Delta_T\)-resolution, and transfer-cutoff
  studies. Enlarging the \(k_T\) box from 1.2 to 2.0 GeV improves the
  GPD-marginal error from \(5.0\times10^{-3}\) to
  \(1.2\times10^{-4}\).
- The tensor Wigner value retains significant transfer-cutoff dependence;
  this is now a separate transform systematic.
- Large simultaneous internal \(k\) and \(\Delta_T\) can exceed AV18's
  15 fm\(^{-1}\) endpoint. No radial-function extrapolation was introduced.
- Added a checked phase-space plot and six-model parent/component bands.
- Final verification: all 95 unit tests pass; component GTMD/Wigner sums
  reconstruct the full matrices to \(3.6\times10^{-18}\) or better.

## 2026-07-24 - Full fixed-k helicity GTMD/Wigner baseline

- Added a declared factorized Gaussian rank-zero nucleon GTMD boundary model
  and an efficient vectorized convolution over external \(k_T\).
- Generated complete
  \(W_{\Lambda'\Lambda}(x,\boldsymbol{k}_T,\boldsymbol{\Delta}_T)\) arrays
  and their two-dimensional \(\Delta_T\)-Fourier Wigner transforms for
  AV18, CD-Bonn, NV2-Ia, NV2-Ib, NV2-IIa, and NV2-IIb.
- Stored the full complex \(3\times3\) target-helicity matrices rather than
  only scalar projections. The light-front spectral kernel therefore retains
  helicity transitions and coherent \(SS,SD,DS,DD\) interference.
- Used \(x=0.2\), \(Q=2\) GeV, flavor \(u\), CT18NNLO,
  \(\langle k_T^2\rangle=0.25\ {\rm GeV}^2\), and a nucleon transfer slope
  of \(1\ {\rm GeV}^{-2}\). These nucleon-GTMD parameters are an explicitly
  exploratory boundary model.
- Verified \(\Delta\)-hermiticity to at worst \(1.3\times10^{-15}\).
  The finite \(|k_{x,y}|\le1.6\) GeV grid reproduces the analytic GPD
  marginal within \(2.5\)--\(2.7\times10^{-4}\).
- Built the six-wave-function fixed-\(k\) slice band. At \(k_T=0,b=0\),
  the relative half-ranges are 1.64% for the unpolarized Wigner projection
  and 3.67% for its tensor difference.
- Expanded the suite from 91 to 94 tests; all pass.

## 2026-07-24 - Norfolk ensemble propagation while awaiting current correction

- Centralized wave-function selection and domain validation for AV18,
  CD-Bonn, and all four Norfolk choices.
- Produced Norfolk inclusive \(b_1\), TMD/SIDIS, and normalized body-overlap
  outputs. At \(x=0.248\), the Norfolk \(b_1\) values range from
  \(-1.3355\times10^{-3}\) to \(-9.4363\times10^{-4}\). At \(P_{hT}=0\),
  the Norfolk SIDIS tensor ratios range from \(-4.2730\times10^{-4}\) to
  \(-2.1086\times10^{-4}\).
- Produced the body-GTMD integrated-momentum marginal through
  \(\Delta_\perp=1\) GeV and its truncated Fourier--Bessel impact density
  for all six wave functions. This is not yet a full fixed-\(k\) Wigner
  distribution.
- Built six-model wave-function envelopes for one-body elastic observables,
  \(b_1\), TMD/SIDIS, and the body GTMD/impact marginals. At \(x=0.248\),
  the \(b_1\) relative half-range is 16.95%; at \(P_{hT}=0\), the SIDIS
  ratio relative half-range is 36.35%. At \(Q=0.5\) GeV, the one-body
  elastic form-factor relative half-ranges are about 1.7--2.5%.
- Added a finite-Q contact-current diagnostic using the contact moments
  printed in the 2019 Norfolk-current tables. OPE is excluded and the files
  are labeled as using legacy, uncorrected LECs; they are not production
  current predictions.
- The independent OPE discrepancy remains unchanged. Three derivations
  agree with one another and not with printed Table III, so OPE and affected
  fitted contact currents remain excluded pending corrected author values.

## 2026-07-23 - Project intake

### Completed

- Read all 29 pages of `Deuteron_GTMD.pdf`.
- Extracted and visually inspected representative pages containing the GTMD convolution,
  development roadmap, and open derivations.
- Recorded the scientific architecture, development stages, validation requirements, and unresolved
  derivations in `project_context.md`.
- Established initial decisions for tensor normalization and separation of the two transverse
  impact parameters.

### Workspace state observed

- `Deuteron_GTMD.pdf` - primary project brief.
- `1610.04066v1.pdf` - nuclear Wigner-function reference cited as reference [25].
- No implementation source tree or project-specific build configuration was present at intake.

### Local tooling

- System Poppler tools (`pdfinfo`, `pdftotext`, `pdftoppm`) were unavailable.
- Installed user-local Python packages `pypdf` and `pymupdf` to extract and render the brief.
- Temporary renders and extracted text are under `tmp/pdfs/deuteron_gtmd/`; these are scratch
  artifacts and not project deliverables.

### Verification

- Confirmed the PDF has 29 pages.
- Visually inspected equations and layout on pages 10, 25, and 26 after rendering at 2x scale.
- Cross-checked the extracted development roadmap and T1-T9 task list against rendered pages.

### Next recommended action

Create the Stage 0 software skeleton only after selecting or documenting reasonable defaults for
P-001 through P-004 in `decisions.md`. The first executable milestone should demonstrate a
synthetic parent helicity-matrix GTMD whose TMD, GPD, PDF, Wigner, and moment reductions satisfy
normalization and Fourier-inversion tests.

## 2026-07-23 - Neff-Feldmeier Wigner/SRC reference

### Completed

- Read all 15 pages of `1610.04066v1.pdf`, including both appendices.
- Studied the full matrix Wigner definition, coordinate/momentum marginals, spin reductions,
  partial phase-space distributions, angular correlations, SRG comparison, two-Gaussian
  interference model, and Gaussian-basis analytic evaluation.
- Added detailed technical notes and a light-front translation map in
  `references/neff_feldmeier_2016.md`.
- Added project decisions preserving Wigner negativity and coherent \(S\)-\(D\) interference.

### Verification

- Confirmed the PDF has 15 pages.
- Visually inspected page 3 for the spin-matrix definition and marginals, page 9 for tensor/spin
  diagnostics, and page 13 for the analytic Gaussian Wigner formulas and Fourier phases.
- Cross-checked equation numbers and plotted interpretations against the rendered pages.

### Key project consequence

The reference supports a matrix-first Wigner implementation with exact marginal tests. It cannot
be copied directly into the light-front model: instant-form variables, canonical spin, and the
three-dimensional Fourier transform must be replaced by LF variables, LF helicities/spin
rotations, and the transverse off-forward overlap specified in the primary brief.

## 2026-07-23 - Numerical environment and wave-function acquisition

### Accepted inputs

- User selected Python.
- User authorized obtaining authoritative AV18 and CD-Bonn radial wave-function inputs.
- User reported LHAPDF and common scientific libraries in conda base.

### Environment verified

- Conda base: `/Users/dustin/miniforge3`
- Python 3.9.23
- NumPy 1.26.3
- SciPy 1.13.0
- LHAPDF 6.5.5
- PyTorch 2.8.0
- Installed LHAPDF sets:
  `CT18NNLO`, `MSHT20nnlo_as118`, `NNPDF40_nlo_as_01180`,
  `NNPDF40_nnlo_as_01180`

### Data acquired

- Downloaded authoritative AV18 configuration- and momentum-space radial tables and the extended
  deuteron properties file from the Argonne theory site.
- Downloaded the primary CD-Bonn paper containing its Appendix C analytic wave-function
  parameterization.
- Recorded source URLs, units, normalization statements, and SHA-256 checksums in
  `../data/README.md`.

### PDF baseline

Use an abstract LHAPDF provider. `CT18NNLO` is the provisional central baseline because it is
already installed; cross-check against the other installed global fits. Revisit the ensemble and
perturbative order before Stage 1 phenomenology.

### Immediate data task

Implement strict AV18 parsers and a CD-Bonn Appendix C generator. Validate:

- radial normalization;
- \(D\)-state probabilities (AV18 approximately 5.7599%, CD-Bonn approximately 4.85%);
- Fourier consistency between coordinate and momentum representations;
- origin and asymptotic behavior;
- interpolation stability and forbidden extrapolation.

## 2026-07-23 - Wave-function input implementation

### Implemented

- Added a Python package skeleton under `src/deuteron_wigner/`.
- Added a validated `RadialWaveFunction` container with explicit representation, units,
  normalization measure, component norms, \(D\)-state probability, PCHIP interpolation, and
  forbidden extrapolation.
- Added strict readers for the authoritative AV18 `deut.wf` and `deut.wfk` formats.
- Added a separately named AV18 asymptotic-tail normalization calculation. It does not alter or
  append to the raw table.
- Implemented the CD-Bonn Appendix D \(n=11\) analytic parameterization:
  - masses \(m_j=\gamma+(j-1)m_0\);
  - Table XX \(C_j,D_j\) inputs;
  - derived final \(C_j\) constraint;
  - derived final three \(D_j\) values from
    \(\sum D_j=\sum D_jm_j^2=\sum D_j/m_j^2=0\);
  - analytic coordinate- and momentum-space functions;
  - explicit \(L=2\) Fourier phase.
- Added 11 standard-library `unittest` tests covering parsing, grids, normalization, \(D\)-state
  probabilities, derivatives, origin constraints, asymptotics, interpolation boundaries,
  Table XIX values, and Fourier-Bessel consistency.

### Verified numerical results

AV18:

- Coordinate table raw norm through 15 fm: `0.998370146171`.
- Explicit asymptotic completion: `0.001628344654`.
- Completed coordinate norm: `0.999998490825`.
- Completed coordinate \(P_D\): `0.057598542617`.
- Momentum-table norm: `1.000005360539`.
- Momentum-table \(P_D\): `0.057598540741`.
- Published header value: `0.057599`.

CD-Bonn analytic parameterization:

- Coordinate norm: `0.999999826157`.
- Momentum norm: `0.999999826157`.
- Coordinate and momentum \(P_D\): `0.048562073645`.
- Published potential result is approximately `0.0485`; the analytic parameterization is an
  approximation to the underlying numerical solution.
- Coefficient residuals:
  - \(\sum C_j=0\) exactly at printed precision;
  - \(\sum D_j=-1.42\times10^{-13}\);
  - \(\sum D_jm_j^2=-5.46\times10^{-12}\);
  - \(\sum D_j/m_j^2=-4.44\times10^{-15}\).

### Important convention finding

The CD-Bonn momentum \(D\) wave requires a relative minus sign from the \(i^2\) partial-wave
Fourier phase. Without it, the \(j_2\) transform reconstructs the negative of the coordinate-space
\(D\) wave. This is now decision D-010 and has a regression test.

### Verification command

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python -m unittest discover -s tests -v
```

Result: 11 tests passed.

### Next recommended action

Begin the convention-safe Stage 0 core:

1. typed light-front variables and transverse vectors;
2. helicity ordering and \(3\times3\) target matrices;
3. explicit Fourier convention objects separating `b_delta` and `b_tmd`;
4. synthetic GTMD parent fixtures and commuting marginal tests.

## 2026-07-23 - Stage 0 convention-safe GTMD core

### Implemented

- Added typed transverse momentum, momentum-transfer, GTMD-impact, and TMD-impact coordinates.
- Added light-front scalar products and symmetric zero-skewness on-shell external kinematics.
- Added ordered spin-1 helicity matrices, unpolarized/longitudinal/tensor projections, a complete
  orthogonal nine-element polarization basis, reconstruction, and positive-semidefinite checks.
- Added explicit and distinct GTMD-imaging and TMD-coordinate Fourier convention objects.
- Added a dense sampled parent GTMD with TMD, GPD, PDF, Wigner, and commuting-reduction paths.
- Added a baseline quark, antiquark, and gluon TMD registry with rank checks.

### Verification

- Analytic transform inversion and commuting marginal/reduction fixtures pass.
- Spin-basis projection and reconstruction pass for complex Hermitian target matrices.
- Symmetric external states remain on shell for nonzero transverse transfer.

## 2026-07-23 - Light-front wave function and collinear impulse baseline

### Implemented

- Added the equal-mass instant-form to light-front mapping, exact Jacobian, unitary Melosh
  rotations, coupled \(S\)- and \(D\)-wave amplitudes, and forward/off-forward helicity overlaps.
- Added direct light-front and preferred spherical internal-momentum smearing quadratures.
- Added proton/neutron LHAPDF adapters, including the isospin \(u\leftrightarrow d\) mapping.
- Added tensor PDF convolution and leading-order \(b_1\).
- Transcribed and tested HERMES Table II.
- Added explicit deuteron-target versus nucleon-mass scaling-variable handling after studying
  arXiv:1702.05337.

### Numerical validation

At \(n_k=36\), \(n_{\cos\theta}=24\), \(n_\phi=16\):

- CD-Bonn, \(k_{\max}=16\ \mathrm{fm}^{-1}\): unpolarized norm `0.999816273270`;
  tensor sum `8.28e-16`.
- AV18, \(k_{\max}=15\ \mathrm{fm}^{-1}\): unpolarized norm `1.000147906009`;
  tensor sum `4.93e-16`.
- The direct \(y\)-grid formulation was rejected for production because of slow endpoint
  convergence. The spherical formulation converges to the known radial normalization and
  enforces the tensor sum rule to floating-point precision.
- All 41 unit tests pass.

### Provisional HERMES-point results

Using CT18NNLO member 0 as a reproducible shape fixture, the nucleon-mass \(x\) convention, and
per-nucleon normalization:

| \(x\) | \(Q^2\) | CD-Bonn \(b_1^{IA}\) | AV18 \(b_1^{IA}\) | HERMES \(b_1\) |
|---:|---:|---:|---:|---:|
| 0.012 | 0.51 | 0.001096 | 0.000758 | 0.1120 |
| 0.032 | 1.06 | 0.000800 | 0.000581 | 0.0550 |
| 0.063 | 1.65 | 0.0000469 | 0.0000942 | 0.0382 |
| 0.128 | 2.33 | -0.000747 | -0.000425 | 0.0029 |
| 0.248 | 3.11 | -0.001297 | -0.000938 | 0.0029 |
| 0.452 | 4.69 | -0.000320 | -0.000300 | -0.0038 |

The first three points have \(Q<1.295\) GeV and are below the installed CT18NNLO range. All
entries are preliminary leading-order partonic impulse baselines, not precision comparisons.

### Verification command

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python -m unittest discover -s tests -q
```

Result: 41 tests passed.

### Next action

Persist convergence and model-comparison outputs reproducibly, then advance to the first
rank-zero spin-1 TMD layer while retaining the GTMD-parent reduction tests.

### Persisted artifacts

- `../outputs/stage1/b1_cd_bonn_ct18nnlo.csv`
- `../outputs/stage1/b1_av18_ct18nnlo.csv`

The generating commands and validity caveats are recorded in `../outputs/README.md`.

## 2026-07-23 - Stage 2 forward rank-zero TMD bridge

### Implemented

- Added a spherical light-front transverse-smearing quadrature that retains each
  \((y,p_x,p_y)\) node and the U/LL nuclear densities.
- Added the Eq. (84) \(b_{\rm TMD}\)-space impulse convolution for scalar rank-zero nucleon TMD
  inputs, including the phase \(\exp[i(x/y)b_{\rm TMD}\cdot p_T]\).
- Kept this coordinate explicitly distinct from the GTMD imaging coordinate.

### Verification

- At \(b_{\rm TMD}=0\), the U and LL results reproduce the collinear impulse convolution to
  floating-point precision.
- For CD-Bonn at the Stage 1 grid, the retained transverse kernel has 13,824 nodes,
  norm `0.999816273270`, and tensor sum `8.01e-16`.
- All 44 unit tests pass.

### Remaining Stage 2 work

- Attach a declared nucleon TMD input model and compare nuclear broadening in U and LL.
- Add Fourier-Bessel inversion to \(k_T\) and verify the collinear integral numerically.
- Add the first direct tensor SIDIS structure-function ratio.
- Generalize from scalar nucleon inputs to the full nucleon spin-density matrix and spin-transfer
  terms.

## 2026-07-23 - Stage 2 Fourier inversion and minimal SIDIS observable

### Implemented

- Added rank-aware radial Fourier--Bessel transforms corresponding to Eqs. (102)-(103).
- Added an explicitly normalized Gaussian rank-zero nucleon TMD boundary fixture.
- Added the radial rank-zero SIDIS W term of Eq. (106) and the convention-safe
  \(\delta_TW/W_U\) ratio.
- Added a reproducible script and persisted CD-Bonn and AV18 \(k_T\)-space TMD and SIDIS tables.

### Verification

- Analytic Gaussian forward and inverse transforms agree to below `2e-7`.
- The analytic \(k_T\) integral recovers the collinear normalization.
- For the realistic CD-Bonn kernel, numerical inversion recovers U and LL \(b=0\) values with
  relative errors `7.47e-4` and `6.86e-4`.
- For AV18, the corresponding errors are `7.47e-4` and `7.59e-4`.
- All 48 unit tests pass.

### Fixture result at \(x_D=0.064\), \(Q=2\) GeV, \(z_h=0.5\)

- At \(P_{hT}=0\), CD-Bonn gives \(\delta_TW/W_U=-3.94\times10^{-4}\).
- At \(P_{hT}=0\), AV18 gives \(\delta_TW/W_U=-1.86\times10^{-4}\).
- The order-of-magnitude model spread is a useful sensitivity diagnostic, not yet a physical
  uncertainty band.

### Next action

Promote the nuclear kernel from scalar U/LL densities to the full active-nucleon helicity density
matrix, then add spin-transfer terms and test Hermiticity, positivity, and the scalar-limit
reduction.

### Active-nucleon spin-density promotion begun

- Added the forward density
  \(S_{\Lambda'\Lambda;\lambda'_N\lambda_N}\) obtained by tracing only the spectator helicity.
- Verified the combined \(6\times6\) target/active-nucleon matrix is Hermitian and positive
  semidefinite.
- Verified tracing the active helicities exactly reproduces the previous scalar target density.
- Verified U and LL target projections reduce to the existing unpolarized and tensor-difference
  channels.
- All 50 unit tests pass.

## 2026-07-23 - Full active-nucleon spin contraction

### Implemented

- Added a transverse nuclear quadrature retaining the active nucleon's complex \(2\times2\)
  helicity matrix in both U and LL target channels.
- Added a general \(b_{\rm TMD}\)-space contraction with proton and neutron spin-dependent
  nucleon correlator matrices.
- Added the off-forward retained-spin overlap
  \(S_{\Lambda'\Lambda;\lambda'_N\lambda_N}(y,p_T,\Delta_T)\).

### Verification

- An identity nucleon correlator reproduces the scalar convolution exactly, including its complex
  transverse phase.
- A Pauli-\(\sigma_z\) fixture produces the analytically expected helicity-transfer term.
- The realistic 13,824-node CD-Bonn spin kernel is exactly Hermitian node by node; its scalar view
  has norm `0.999816273270` and tensor sum `8.10e-16`.
- Tracing the off-forward active helicities reproduces the scalar off-forward overlap.
- The retained-spin overlap satisfies
  \(S(\Delta)^\dagger=S(-\Delta)\), including both target and active-nucleon indices.
- All 53 unit tests pass.

### Next action

Use the off-forward retained-spin overlap in the callable GTMD convolution and settle the
active-nucleon transfer map by simultaneous TMD, GPD/form-factor, and normalization tests.

## 2026-07-23 - Callable retained-spin GTMD convolution

### Implemented

- Added a fixed-transfer off-forward nuclear spectral quadrature with explicit index ordering.
- Added a callable Eq. (45) one-body GTMD convolution with the shift
  \(k_{T,N}=k_T-(x/y)p_T\).
- Added an explicit transfer-mapping enum and the provisional identity choice
  \(\Delta_{T,N}=\Delta_T\).
- Persisted normalized CD-Bonn and AV18 one-body transverse overlap form factors.

### Parent-level verification

- The \(\Delta_T=0\) GTMD target matrix is Hermitian.
- Numerical \(k_T\) integration of a normalized Gaussian nucleon GTMD reproduces the
  shift-independent GPD convolution to `2e-10`.
- The complete convolution obeys
  \(W_D(\Delta_T)^\dagger=W_D(-\Delta_T)\).
- At \(\Delta_T=0\), the realistic CD-Bonn off-forward kernel recovers norm
  `0.999816273270`.
- Direct realistic \(+\Delta/-\Delta\) kernels satisfy the full target-and-nucleon-index
  Hermiticity relation exactly on the sampled grid.
- All 57 unit tests pass.

### One-body transverse overlap results

On the \(36\times24\times16\) spherical grid:

- CD-Bonn forward overlap: `0.999816273270`, with normalized overlap
  `0.157351` at \(-t=0.25 GeV^2\).
- AV18 forward overlap with the conservative \(k_{\max}=10\ \mathrm{fm}^{-1}\) domain:
  `1.000229787704`, with normalized overlap `0.152545` at the same transfer.
- The AV18 overlap crosses zero below \(1\ \mathrm{GeV}^2\), while CD-Bonn remains positive at
  the final sampled point. This is a model diagnostic, not yet a comparison to a physical charge
  form factor.

### Input-domain finding

Using the AV18 table's nominal 15 fm\(^{-1}\) cutoff off forward is invalid: the
\((1-y)\Delta_T/2\) wave-function shifts can request momenta above the table boundary. The
production scan therefore uses 10 fm\(^{-1}\) and preserves the no-extrapolation policy.

### Next action

Attach physical nucleon current form factors to the GPD moment, compare the one-body deuteron
form-factor combinations to data or a trusted calculation, and use that comparison to choose
between identity and \(y\)-dependent active-nucleon transfer mappings.

## 2026-07-23 - Electromagnetic current and transfer-map benchmark

### Implemented

- Added strict parsers for the Kelly isoscalar \(G_E^s,G_M^s\), AV18 body-integral
  \(C_E,C_L,C_S,C_Q\), and impulse \(G_C,G_M,G_Q\) tables in `fdeut.av18`.
- Added the local-current moment of the GTMD convolution, with the \(dx=y\,dz\) Jacobian
  explicitly canceling Eq. (45)'s \(1/y\).
- Added and tested an alternative `ACTIVE_FRACTION` mapping
  \(\Delta_{T,N}=y\Delta_T\).
- Added a reproducible light-front versus AV18 charge-current comparison table.

### Reference reproduction

- The parsed relation \(G_C=2G_E^sC_E\) reproduces the authoritative AV18 table to
  `3e-9` relative tolerance.
- Static inputs are recovered: \(G_E^s(0)=0.5\),
  \(G_M^s(0)=0.43990235\), and \(G_C(0)\simeq1\).

### Transfer-map result

For `IDENTITY`, relative differences from the AV18 impulse \(G_C\) are approximately:

- `-0.056%` at 0.1 GeV;
- `-0.117%` at 0.2 GeV;
- `-0.045%` at 0.3 GeV;
- `+0.32%` at 0.4 GeV;
- `+1.33%` at 0.5 GeV.

For `ACTIVE_FRACTION`, the corresponding low-transfer disagreement grows to roughly 2%, 8%,
and 17% by 0.1, 0.2, and 0.3 GeV. Identity transfer is therefore accepted for the one-body
baseline. Relative differences near the charge-form-factor zero are not a stable error measure.

### Verification

- All 61 unit tests pass.
- Results are persisted in `../outputs/stage0/body_form_factor_av18.csv` and
  `../outputs/stage0/av18_charge_current_comparison.csv`.

### Next action

Implement the magnetic and quadrupole current/body-integral combinations and compare
\(G_M,G_Q,A,B,t_{20}\) against the remaining authoritative AV18 tables. Keep these
nonrelativistic impulse benchmarks distinct from the later fully covariant light-front current and
two-body-current calculation.

### Magnetic, quadrupole, and elastic-observable benchmark completed

- Implemented the AV18/Wiringa one-body combinations
  \(G_M=(M_D/m_r)(G_E^sC_L+2G_M^sC_S)\) and \(G_Q=2G_E^sC_Q\), alongside \(G_C\).
- Implemented \(A(Q^2)\), \(B(Q^2)\), and \(t_{20}(Q^2,70^\circ)\) with the table's exact
  normalization.
- Reproduced all parsed \(G_C,G_M,G_Q,A,B,t_{20}\) columns within their printed numerical
  precision.
- All 62 unit tests pass.

The remaining current task is not another table transcription: it is the independent covariant
light-front helicity-current calculation, including its angular-condition diagnostic, followed by
a comparison to this nonrelativistic impulse benchmark.

## 2026-07-23 - Independent light-front helicity current

### Reference studied

- Read all 24 pages of Carlson and Ji, arXiv:hep-ph/0301213.
- Visually verified Eq. (4.7) and its \(I_{0+}=-I_{+0}\) time-reversal sign on rendered page 16.
- Recorded the source and checksum in `../data/README.md`.

### Implemented

- Added the four normalized spin-1 \(J^+\) helicity amplitudes.
- Added the Carlson-Ji angular condition and a scale-independent relative violation measure.
- Added Sachs-to-Dirac/Pauli conversion and the normalized nucleon LF helicity current.
- Added all four three-amplitude form-factor extractions and prescription-spread reporting.
- Inserted the retained-spin \(F_1/F_2\) current into the AV18 light-front overlap.

### Production-grid result

The values below were superseded by the corrected angular \(D\)-wave phase described in the
component-attribution section. Corrected relative angular-condition violations are:

- `3.06e-4` at 0.1 GeV;
- `1.16e-3` at 0.2 GeV;
- `2.75e-3` at 0.3 GeV;
- `5.74e-3` at 0.4 GeV;
- `1.07e-2` at 0.5 GeV.

At 0.5 GeV, the corrected extracted \(G_C\) prescription interval is
`[0.08372, 0.08662]`, while the
nonrelativistic AV18 impulse reference is `0.08795`. The prescription spread and common offset
are distinct diagnostics: the first measures rotational-covariance failure within the LF current,
while the second also includes relativistic current/model differences.

### Verification

- Covariant synthetic amplitudes satisfy the angular condition below `2e-16`.
- Every extraction prescription recovers the same input form factors for a covariant current.
- Nucleon current reversal satisfies \(J(\Delta)^\dagger=J(-\Delta)\).
- All 68 unit tests pass.

### Next action

Decompose the violation by wave-function component and nucleon-current term
(\(SS,SD,DS,DD\) and \(F_1/F_2\)), then compare AV18 with CD-Bonn. This will identify whether
the observed prescription dependence is driven primarily by Melosh rotation, the D wave, or the
Pauli current before adding two-body currents.

## 2026-07-23 - Angular-condition component attribution

### Implemented

- Added coherent retained-spin \(SS,SD,DS,DD\) off-forward quadratures.
- Added separate \(F_1\)-only and \(F_2\)-only current contractions.
- Added an explicit identity-spin-rotation diagnostic while preserving Melosh rotation as default.
- Persisted production-grid AV18, CD-Bonn, and no-Melosh AV18 decompositions.

### Component result

The largest individual angular-condition term is `SS-F2` with physical Melosh rotations:

- AV18: `5.11e-4`, `1.60e-3`, `1.71e-3` at 0.1, 0.3, 0.5 GeV.
- CD-Bonn: `5.17e-4`, `1.65e-3`, `1.85e-3` at the same transfers.

At 0.5 GeV, corrected AV18 contributions include:

- `SS-F2 = +1.706e-3`;
- `DS-F1 = +7.359e-4`;
- `SD-F2 = -4.719e-4`;
- smaller terms sum with these to the final `+2.252e-3`.

Thus the residual is not a D-state probability observable; coherent S-D terms provide important
cancellations.

### Wave-function comparison

- AV18 and CD-Bonn relative violations are essentially identical at 0.1 and 0.3 GeV.
- At 0.5 GeV they are `1.07e-2` and `1.17e-2`, respectively.
- This modest spread is much smaller than the effect of changing the spin rotation.

### Melosh diagnostic

Replacing Melosh rotations by identity rotations worsens the AV18 relative violation:

- from `3.06e-4` to `8.23e-4` at 0.1 GeV;
- from `2.75e-3` to `6.60e-3` at 0.3 GeV;
- from `1.07e-2` to `1.64e-2` at 0.5 GeV.

Melosh rotation therefore repairs a substantial part of the rotational-covariance defect in this
model; it is not the source of the observed violation.

### Verification

- Component kernels reconstruct the full off-forward density below `3e-15`.
- Component/current residuals reconstruct the full result below `2e-14`.
- All 71 unit tests pass.

### Next action

Quantify the residual gap as an effective missing-current amplitude, test which helicity component
would restore the angular condition under GK and alternative prescriptions, and keep that
correction separate from a genuine chiral/two-body-current model.

### Effective missing-current completion

- Added exact one-amplitude angular-condition completions for each of
  \(I_{++},I_{+0},I_{+-},I_{00}\).
- Every completion restores the residual below `1e-14`; none is interpreted as a dynamical
  current.
- For AV18 at 0.5 GeV:
  - assigning the correction to \(I_{00}\) requires `+0.002252`, about 3.69% of that amplitude;
  - assigning it to \(I_{++}\) requires `-0.002175`, about 2.13%;
  - assigning it to \(I_{+-}\) requires `-0.002252`, about 5.18%;
  - assigning it to the small \(I_{+0}\) requires a 199% correction and is therefore poorly
    conditioned.
- CD-Bonn shows the same pattern; its \(I_{00}\) completion is about 3.88% at 0.5 GeV.

This supports using an \(I_{00}\)-omitting/GK-style extraction as the first reported LF
prescription while retaining the full prescription band as systematic information. It does not
prove that the physical missing current resides only in \(I_{00}\).

### Next action

Add explicit GK and BH named extraction adapters, report \(G_C,G_M,G_Q\) prescription bands for
both wave functions, and compare their elastic \(A,B,t_{20}\) consequences with the AV18 impulse
benchmark.

## 2026-07-23 - D-wave phase correction and named LF prescriptions

### Convention correction

The first named \(G_Q\) extraction exposed a missing angular partial-wave phase. Reduced radial
tables use a real Fourier-Bessel convention, while the complete momentum-space \(L=2\) angular
amplitude carries \(i^2=-1\). Applying that phase in the canonical S/D coupling:

- changes no radial normalization or \(D\)-state probability;
- restores the physical positive sign of \(G_Q\);
- is protected by a direct pure-D regression test;
- required regeneration of all phase-sensitive Stage 1, Stage 2, and current outputs.

### Corrected Stage 1/2 consequences

- CD-Bonn \(b_1^{IA}(x=0.248)\): `-0.001297`.
- AV18 \(b_1^{IA}(x=0.248)\): `-0.000938`.
- At the SIDIS fixture point \(P_{hT}=0\):
  - CD-Bonn \(\delta_TW/W_U=-3.94e-4\);
  - AV18 \(\delta_TW/W_U=-1.86e-4\).

### Named extraction results

Added explicit aliases:

- GK = omit \(I_{00}\);
- BH = omit \(I_{++}\).

At 0.5 GeV the full four-prescription bands are:

- AV18:
  \(G_C=[0.08372,0.08662]\),
  \(G_M=[0.17237,0.23576]\),
  \(G_Q=[2.3135,2.4403]\).
- CD-Bonn:
  \(G_C=[0.08618,0.08942]\),
  \(G_M=[0.17418,0.24506]\),
  \(G_Q=[2.2054,2.3471]\).

The AV18 impulse reference is
\((G_C,G_M,G_Q)=(0.08795,0.17700,2.44803)\).
The charge and quadrupole channels are reasonably bracketed or approached, while the magnetic
channel has substantial prescription sensitivity that propagates strongly into \(B\).

At 0.5 GeV, AV18 GK gives
\((A,B,t_{20})=(0.009534,0.001340,-0.8029)\), compared with the reference
\((0.009789,0.000755,-0.8529)\). This identifies the magnetic current as the clearest next
improvement target.

### Verification

- All 72 unit tests pass after the phase regression was added.
- Every regenerated numerical artifact uses the corrected phase.

## 2026-07-24 - Static magnetic audit and controlled completion

### Diagnosis

Computed the AV18/Melosh current at \(Q=0.01,0.02,0.05,0.1\) GeV and repeated 0.01 and
0.05 GeV with a \(48\times32\times24\) quadrature. The residual and extracted form factors are
stable with resolution. The angular residual scales as \(Q^2\), but the resulting static
prescription ambiguity is finite:

- raw GK extrapolation: \(G_M(0)=2.139095\);
- AV18 impulse-table value: \(G_M(0)=1.691972\);
- the extraction omitting \(I_{+0}\) already tends to the AV18 value.

At 0.01 GeV, the S-wave \(F_2\) term contributes \(0.06382\,Q^2\) to the angular residual;
all other terms are much smaller or cancel. This rules out numerical resolution and D-wave
modeling as the primary source.

### Controlled completion

Added `dipole_magnetic_completion`, which contributes only a covariant \(G_M\) and therefore
does not repair or conceal the raw angular residual. Static calibration and an AV18-shape fit
give:

- \(\delta\mu=-0.447123\);
- \(\Lambda=0.328084\) GeV;
- sampled \(G_M\) RMS error: 0.34746 raw, 0.00987 completed.

At 0.5 GeV, the completion changes \(B\) from 0.001340 to 0.000919 (AV18: 0.000755) and
\(t_{20}\) from -0.8029 to -0.8219 (AV18: -0.8529). Remaining disagreement is consistent with
the unchanged charge/quadrupole prescription effects and the deliberately minimal magnetic
ansatz.

### Artifacts and verification

- `outputs/stage0/lf_static_audit_av18.csv`
- `outputs/stage0/lf_static_prescriptions_av18.csv`
- `outputs/stage0/lf_magnetic_completion_av18.csv`
- 73 unit tests pass.

### Next action

Replace the fitted magnetic completion with a literature-grounded relativistic/two-body current
operator (or establish a systematic operator basis), then propagate its uncertainty before
returning to the GTMD/TMD evolution layer.

## 2026-07-24 - Poincare-covariant longitudinal-Breit current

### Literature conclusion

The large static correction inferred from the raw GK result is not plausibly a conventional
isoscalar meson-exchange current. Carbonell-Karmanov identify additional
light-front-orientation-dependent spin-1 form factors and show that \(G_M\) requires current
information beyond \(J^+\). Lev-Pace-Salme avoid the four-amplitude angular ambiguity by using
a longitudinal Breit frame and the three independent elements \(J^+_{11}\), \(J^+_{00}\), and
\(J^x_{10}-J^x_{01}\).

### Implementation

Added:

- `src/deuteron_wigner/covariant_current.py`
  - spin-one \(R_x(\pi)\);
  - LPS Hermitian completion and current conservation;
  - longitudinal spectator-fraction mapping;
  - node-dependent \(J^+\), \(J^x\), and nucleon virtual transfer from LPS Eqs. (42)-(46);
  - unambiguous Eq. (21) form-factor extraction.
- `scripts/compute_covariant_lps_form_factors.py`
  - contracts the kernels with the existing S/D plus Melosh wave functions;
  - evaluates nucleon form factors at each constituent transfer;
  - reports \(G_C,G_M,G_Q,A,B,t_{20}\).

Two explicit adapters are required: `fdeut.av18` stores half-isoscalar nucleon form factors,
while LPS use proton-plus-neutron sums; and the transverse kernel moment is converted to the
project convention \(G_M=(M_D/m_N)\mu_D\).

### Production results

AV18 \(G_M\) at \(Q=(0.01,0.1,0.3,0.5)\) GeV:

`(1.68341, 1.38788, 0.51829, 0.14427)`.

CD-Bonn:

`(1.69613, 1.40010, 0.52729, 0.14868)`.

The corresponding AV18 impulse-table values are
`(1.68807, 1.42969, 0.57542, 0.17700)`. The static normalization is recovered without a fitted
completion; increasing underprediction with \(Q\) is now a genuine relativistic/current-model
difference.

The higher-resolution AV18 check gives:

- \(Q=0.01\): \(G_C=0.998071\), \(G_M=1.683178\), \(G_Q=24.9854\);
- \(Q=0.5\): \(G_C=0.0791806\), \(G_M=0.144305\), \(G_Q=2.37674\).

Magnetic and charge convergence are strong. Low-\(Q\) quadrupole extraction converges more
slowly because it divides a small diagonal-current difference by \(Q^2\).

### Artifacts and verification

- `outputs/stage0/lps_covariant_form_factors_av18.csv`
- `outputs/stage0/lps_covariant_form_factors_cd_bonn.csv`
- `handoff/references/covariant_light_front_current.md`
- 78 tests pass.

### Next action

Quantify the remaining covariant-current uncertainty: separate convection and spin-current
pieces, assess the nucleon-form-factor and high-momentum truncation dependence, and only then
add the leading isoscalar two-body magnetic operator as a small correction.

## 2026-07-24 - Covariant-current uncertainty and chiral two-body basis

### One-body decomposition

The production tables now carry separate Sachs-electric and Sachs-magnetic kernel
contributions. For AV18, the magnetic sector contributes 93.9%, 91.1%, and 87.4% of \(G_M\)
at \(Q=0.1,0.3,0.5\) GeV; the electric/convection sector supplies the remainder. The component
columns reconstruct \(G_C,G_M,G_Q\) to floating-point precision.

### Controlled one-body sensitivities

At \(Q=0.5\) GeV:

- replacing the exact constituent transfer with external-\(Q\) factorization raises AV18
  \(G_M\) by 2.42%, \(B\) by 4.91%, and changes \(t_{20}\) by 3.50% relative magnitude;
- the same factorization raises CD-Bonn \(G_M\) by 2.75%;
- lowering AV18 \(k_{\max}\) from 8 to 6 fm\(^{-1}\) changes \(G_M\) by only -0.15% and
  \(B\) by -0.29%;
- the wave-function spread at 0.5 GeV is about 3.1% in \(G_M\).

Thus neither numerical tails nor nucleon-form-factor factorization explains the full
one-body-to-AV18-reference difference. The exact node-dependent transfer remains the accepted
calculation because LPS explicitly show that the nucleon form factors cannot be factored out.

### Chiral isoscalar two-body operator

Read Kolling, Epelbaum, and Phillips, arXiv:1209.0837. Their first isoscalar two-body magnetic
current occurs at \(O(eP^4)\) and contains:

- a long-range one-pion term proportional to \(\bar d_9\);
- a short-range M1 contact term proportional to \(L_2\).

Implemented their Eq. (3) in `src/deuteron_wigner/two_body_current.py`. The source fits \(L_2\)
to the magnetic moment and \(\bar d_9\) to data below 400 MeV, with regulator-dependent values.
It estimates breakdown near 600 MeV, where the contact contribution becomes comparable to
impulse approximation.

No numerical two-body correction has been added to the AV18/CD-Bonn results: using the source
LECs without its matched regulator and chiral wave functions would be inconsistent. The
unregularized operator is ready for contraction once P-010 is resolved.

### Artifacts and verification

- `outputs/stage0/lps_sensitivity_av18_kmax6.csv`
- `outputs/stage0/lps_sensitivity_av18_kmax8.csv`
- `outputs/stage0/lps_sensitivity_av18_kmax10.csv`
- `outputs/stage0/lps_sensitivity_av18_external_q.csv`
- corresponding CD-Bonn \(k_{\max}=6,8\) and external-\(Q\) files
- 82 tests pass.

### Next action

Choose between (a) a regulated hybrid AV18/CD-Bonn fit, with \(L_2,\bar d_9\) refit for each
wave function and explicit cutoff variation, or (b) a fully consistent chiral NN
wave-function/current calculation. Option (b) has the cleaner EFT uncertainty interpretation.

## 2026-07-24 - Matched Norfolk current benchmark

Imported all four public NV2 deuteron tables and implemented strict coordinate-
and momentum-space readers. The LPS one-body calculation now supports NV2-Ia,
Ib, IIa, and IIb.

Implemented the Schiavilla et al. configuration-space \(Q=0\) N3LO isoscalar
current with the published Gaussian \(R_S\) regulator, long-range \(R_L\)
regulator, and model-specific \(d_1^S,d_2^S\) and minimal-contact LECs.
The angular contraction is reduced analytically to S-S, S-D, and D-D radial
quadratic forms, making the 20,000-point source grids inexpensive.

The decisive validation result is:

- nonminimal contact: agreement with Table III is 0.13--0.87%;
- minimal contact: absolute agreement is \(1.3\)--\(3.8\times10^{-5}\) n.m.;
- OPE: not validated. The direct Eq. (2.12) contraction gives
  \((-0.0402,-0.0210,-0.0294,-0.0719)\) n.m., while Table III gives
  \((+0.0042,-0.0065,+0.0026,-0.0260)\) n.m.

The contact agreement validates normalization, regulator units, spin
normalization, and magnetic-unit conversion. The OPE discrepancy is isolated
to its tensor/S-D convention (or an undocumented implementation convention);
it is explicitly flagged rather than folded into production form factors.

Artifacts:

- `src/deuteron_wigner/wavefunctions/norfolk.py`
- `src/deuteron_wigner/two_body_current.py`
- `scripts/benchmark_norfolk_current.py`
- `outputs/stage0/norfolk_n3lo_magnetic_moment.csv`
- complete verification suite: 87 tests passing

Next: resolve the OPE Table III convention from the authors' implementation or
an independent analytic magnetic-operator derivation, then extend the validated
contact and OPE contractions to finite momentum transfer.

### OPE regulator-ordering audit

The OPE functions have the exact Hessian representation
\(I_1/K=f'(\mu)/\mu\) and
\(I_2/K=f''(\mu)-f'(\mu)/\mu\), with \(f=e^{-\mu}/\mu\).
Two independently implemented prescriptions were compared:

1. the published Eq. (2.22), \(I_k\to C_{R_L}I_k\);
2. differentiating \(C_{R_L}f\), including first and second derivatives of
   the regulator.

The second prescription gives OPE moments
\((0.0290,0.0173,0.0220,0.0703)\) n.m. for
Ia, Ib, IIa, IIb. It does not reproduce Table III and specifically fails the
a/b sign reversal. Regulator ordering alone is therefore ruled out.

The independent angular reduction gives exact coefficients
\((2,0,-1)\) for the spin term and
\((2/3,2\sqrt{2}/3,1/3)\) for the tensor term in the
\((u^2,uw,w^2)\) basis. These identities now have unit tests. Together with
the contact agreement, the remaining discrepancy points to a source
implementation convention not stated in Eqs. (2.12), (2.19), and (2.22), or
to a published-table/operator mismatch. Obtaining the authors' radial
matrix-element expression or current routine is now the cleanest resolution.

### Public-source and erratum search

Inspected the full arXiv source archives for:

- Schiavilla et al., arXiv:1809.10180 / PRC 99, 034005 (2019);
- Gnech and Schiavilla, arXiv:2207.05528 / PRC 106, 044001 (2022);
- Chambers-Wall et al., arXiv:2407.04744 / PRC 110, 054316 (2024).

The 2024 appendix confirms the same OPE operator, \(I_1/I_2\) functions,
long-range regulator, and magnetic-moment limit used here. No public current
routine or radial deuteron reduction is included.

The 2022 paper identifies a material erratum in the 2019 calculation: the
mapping between its contact LEC basis and the Norfolk-potential basis was
inadvertently omitted. It explicitly says this affects the N3LO(MIN)
contributions in Tables III/IV and the fitted \(d_1^S,d_2^S,d_1^V\) values in
Table I. Corrected tables are stated to be available upon request. Therefore
the original 2019 Table I/Table III pair cannot be treated as a clean
self-consistency benchmark.

The original arXiv source contains the vector Fig. 3 density plot but no
underlying numerical data. Its colored vector markers were raster-digitized
into `outputs/stage0/norfolk_ope_figure3_digitized.csv`. Trapezoidal integrals
over the visible \(0.2<r<4.95\) fm range give approximately:

- Ia: \(I_1=+0.0750\), \(I_2=-0.0721\) n.m.;
- Ib: \(I_1=+0.0316\), \(I_2=-0.0370\) n.m.

Their sums reproduce the small sign-changing Table III contribution up to
the omitted endpoints and digitization accuracy. Our current contraction gives
Ia \((+0.0464,-0.0866)\) and Ib \((+0.0237,-0.0447)\) n.m. Thus the problem is
not a common normalization: the two tensor structures differ independently.
This is strong evidence for an unpublished radial/operator convention or for
the impact of the corrected LEC implementation.

A focused request for corrected LECs, corrected
moment decompositions, and the Fig. 3 radial densities has been drafted at
`handoff/correspondence/norfolk_current_request_draft.md`. It has not been sent.

### Figure 3 inverse convention fit

Jointly fit the digitized Ia/Ib \(I_1\) and \(I_2\) curves while allowing a
separate overall model scale and a common multiplier on the exact tensor
partial-wave coefficients. The optimum tensor multiplier is 0.5355, but the
density RMS remains \(9.13\times10^{-3}\ {\rm fm}^{-1}\), visibly comparable
to the curves themselves and far above raster digitization uncertainty.
Changing the D-wave sign does not repair the component shapes.

Therefore pair normalization, D-wave phase, or one missing tensor factor
cannot explain the published densities. The result is reproducible with
`scripts/fit_ope_figure3_conventions.py` and stored in
`outputs/stage0/norfolk_ope_figure3_convention_fit.json`. The next independent
route is the momentum-space Eq. (cp) contraction with the local regulator
implemented through its Fourier transform.

### Independent Cartesian momentum-space OPE contraction

Implemented `scripts/benchmark_norfolk_ope_fft.py`. It constructs the complete
stretched-deuteron four-spin-component wave function on a \(96^3\) Cartesian
grid, applies the regulated \(I_1/I_2\) operator without using the spherical
partial-wave reduction, FFTs both the wave function and operated state, and
evaluates the momentum-space inner product.

For Ia the Cartesian coordinate result is \(-0.04021195\) n.m., the FFT result
is \(-0.04021195\) n.m., and the independent partial-wave result is
\(-0.04021213\) n.m. The four-model FFT results are:

- Ia: \(-0.04021195\) n.m.;
- Ib: \(-0.02099203\) n.m.;
- IIa: \(-0.02943975\) n.m.;
- IIb: \(-0.07187381\) n.m.

FFT Parseval differences are below \(9\times10^{-14}\) n.m.; Cartesian versus
partial-wave differences are below \(10^{-6}\) n.m. This independently rules
out angular quadrature, Clebsch--Gordan reduction, and coordinate integration
as the discrepancy source.

The momentum-space Eq. (cp) analytically Fourier-transforms to the printed
coordinate Eqs. (2.12)/(2.19), including their normalization. Moreover, using
the positive 2022 set-A \(d_2^S\) values with the public wave functions and
printed operator would give the same OPE sign for all four models, while the
2022 deuteron table again reports an a/b sign flip. The public equations and
wave-function tables are therefore insufficient to reproduce the authors'
numerical implementation. Await corrected radial densities/routine; do not
replace the mismatch by an empirical factor.

### Three-way independent first-principles review

Three independent calculations recalculated the OPE moment by analytic partial-wave
reduction, direct Cartesian/Sobol spin integration, and momentum-space
Fourier-Hessian derivation. All obtained:

| Model | \(I_1\) | \(I_2\) | Sum |
|---|---:|---:|---:|
| Ia | +0.04640307 | -0.08661519 | -0.04021213 |
| Ib | +0.02366418 | -0.04465633 | -0.02099214 |
| IIa | +0.03417829 | -0.06361817 | -0.02943988 |
| IIb | +0.08426663 | -0.15614144 | -0.07187481 |

The common closed result is
\[
\mu_{\rm OPE}={6m_N\over m_\pi}\int dr\left[
I_1(2u^2-w^2)+{I_2\over3}(2u^2+2\sqrt2uw+w^2)\right].
\]

The Cartesian calculation was unchanged from 1,024 through 262,144 Sobol
angular samples. The analytic reviewer independently fixed the S--D phase by
reproducing the Ia quadrupole moment, \(0.267585\) versus the tabulated
\(0.267588\ {\rm fm}^2\); reversing the phase gives
\(-0.300960\ {\rm fm}^2\).

Reports are in `handoff/independent_reviews/`. Consensus: the first-principles
calculation is internally consistent, while the printed 2019 operator,
regulator, public wave functions, and printed LECs cannot yield Table III.
The remaining possibilities are an unreported current/LEC mapping in the
authors' code or a table/equation revision mismatch.

## 2026-07-24: Lattice-QCD and perturbative-QCD gluon-TMD audit

Audited first-principles inputs for nucleon \(f_1^g\), \(g_1^g\), and
\(h_1^{\perp g}\), excluding spectator and phenomenological profiles from
the numerical baseline. The published literature provides one-loop gluon
LaMET matching for unpolarized and helicity TMDs, a clean proposed lattice
linear-polarization ratio, and high-order small-\(b_T\) matching for
\(h_1^{\perp g}\). No published numerical lattice proton TMD was located
that fixes the nonperturbative transverse shape.

Published numerical Collins-Soper lattice results located in the audit are
for quarks. Preliminary conference material reports a first gluon-kernel
calculation, but no stable public numerical table was identified. The quark
kernel will not be copied into the gluon channel as a nonperturbative input.

Recorded the source-by-source assessment and implementation contract in
`references/lattice_gluon_tmd_audit.md`, the machine-readable status table in
`outputs/stage0/lattice_gluon_tmd_input_status.csv`, and decision D-026. The
next implementation is a scheme-explicit \(b_T\)-space matched core using
CT18/BDSSV24, perturbatively generated \(h_1^{\perp g}\), and a separately
reported large-\(b_T\) sensitivity family.

## 2026-07-24: First matched b-space gluon-TMD boundary

Added `src/deuteron_wigner/gluon_tmd_matching.py`. The new
`MatchedGluonTMD` keeps b-space scalar functions separate from the existing
k-space correlator, labels its delta-regulator Collins-TMD and
zeta-prescription convention, and exposes its mixed perturbative accuracy.
The \(f_1^g\) and \(g_1^g\) boundaries are tree-level collinear inputs. The
\(h_1^{\perp g}\) boundary uses the first nonzero one-loop coefficients from
arXiv:1907.03780 Eqs. (3.20)-(3.21), including CT18 gluon and quark-singlet
convolutions.

Extended `LHAPDFProvider` with `gluon`, `quark_singlet`, and `alpha_s`
adapters. Added `scripts/compute_matched_gluon_tmd.py` and generated 255 rows
covering five x values, 17 b values, and three declared large-b profile
members in `outputs/stage0/gluon_tmd_matched_bspace.csv`, with adjacent JSON
metadata. The profiles are sensitivity variations, not a fit.

Added eight focused unit tests. The full suite passes 137 tests in the conda
base environment. The next physics step is Collins-Soper/RG evolution and
the rank-2 Fourier-Bessel adapter needed to connect the b-space
\(h_1^{\perp g}\) scalar to the retained-index nuclear convolution.

## 2026-07-24: CSS evolution and rank-2 Cartesian adapter

Added `src/deuteron_wigner/tmd_evolution.py` with a spin-independent one-loop
gluon CSS Sudakov factor, canonical b-star scale, explicit PDF-scale floor,
and optional low/central/high nonperturbative gluon Collins-Soper profiles.
The `none` profile is the perturbative-only evolution baseline. All theory
labels and limitations are machine-readable.

Added `gluon_tmd_b_to_k` to `fourier.py`. Rank-zero \(f_1^g\) and \(g_1^g\)
use \(J_0\); the standard b-space \(h_1^{\perp g}\) uses the signed \(J_2\)
transform and is converted to the mass-normalized coefficient consumed by
the project's Cartesian correlator. The apparent \(1/k_T^2\) expression is
evaluated analytically at zero momentum and remains finite.

Generated:

- `outputs/stage0/gluon_tmd_evolved_bspace.csv` (3,609 data rows);
- `outputs/stage0/gluon_tmd_evolved_kspace.csv` (549 data rows);
- adjacent JSON metadata.

The scan uses \(x=0.1\), \(Q=2,5,10\) GeV, the central intrinsic boundary
profile, and `none/central/high` CS-kernel profiles. Added six evolution and
two rank-2 adapter tests. The complete suite passes 145 tests.

This is still an intermediate uncertainty study: the unpolarized/helicity
matching is tree level, the Sudakov anomalous dimensions are one loop, the
gluon nonperturbative kernel is unfitted, and no Y term is present. The next
step is to construct an interpolated evolved nucleon correlator callable and
replace the Gaussian nucleon input in a controlled nuclear-convolution
comparison.

## 2026-07-24: Evolved nucleon correlator enters the AV18 convolution

Added `InterpolatedSpinHalfGluonGTMD` in `tmd_models.py`. It performs strict
bilinear interpolation in \((x,k_T)\), converts the nuclear momentum unit to
GeV, and composes the same `(nucleon_out,nucleon_in,gluon_i,gluon_j)`
correlator consumed by `convolve_gluon_gtmd_point`. Attempts to leave the
tabulated domain raise an error.

Replaced adaptive matching convolutions by cached 96-point Gauss-Legendre
quadrature. The analytic coefficient test remains satisfied and endpoint
roundoff warnings in large table builds disappear.

Added `scripts/compare_evolved_gaussian_gluon_tmd.py` and generated
`outputs/stage0/gluon_tmd_evolved_vs_gaussian_av18.csv` plus metadata. The
20-point scan uses \(x_N=0.1\), \(Q=5\) GeV, AV18, identical nuclear
quadrature, and \(0.05<k_T<1.5\) GeV.

The evolved distribution is broader: its \(f_1^g\) ratio to the Gaussian
rises from 0.28 at 0.05 GeV, crosses unity near 0.65 GeV, and reaches 253 at
1.5 GeV where the Gaussian is exponentially tiny. The meaningful linear
polarization ratio \(k_T^2h_1^{\perp g}/(2M_D^2f_1^g)\) rises from
\(1.7\times10^{-5}\) to 0.034 for the evolved input, compared with 0.005 to
0.45 for the arbitrary Gaussian `linear_fraction=0.5` fixture. These numbers
are diagnostic and retain the evolution/profile limitations recorded in
D-028. Three interpolator tests bring the complete suite to 148 passing
tests.

The next step is a convergence and uncertainty scan over nuclear quadrature,
intrinsic large-b profiles, CS-kernel profiles, and wave functions. This
should be performed before interpreting the evolved tail quantitatively.

## 2026-07-25: Evolved gluon-TMD convergence and uncertainty audit

Added `scripts/scan_evolved_gluon_tmd_uncertainty.py`. The scan covers AV18,
CD-Bonn, and four Norfolk wave functions; intrinsic
\(g_2=0.10,0.20,0.40\ {\rm GeV}^2\); Collins-Soper
\(g_K=0,0.05,0.10\ {\rm GeV}^2\); and \(k_T=0.1,0.5,1.0,1.5\) GeV at
\(x_N=0.1,\ Q=5\) GeV. It writes 216 labeled samples and separate
wave/profile/total envelopes under `outputs/stage0/uncertainty/`.

The first \(8\times6\times6\) attempt failed the convergence standard and
was discarded. The final audit compares \(12\times8\times8\) and
\(16\times12\times8\) with a \(24\times16\times12\) AV18 reference. Maximum
medium-grid differences are:

- \(f_1^g\): 0.73%;
- \(g_1^g\): 0.79%;
- \(h_1^{\perp g}\): 0.73%;
- \(f_{1LL}^g\): 3.17%;
- \(h_{1LL}^{\perp g}\): 7.59%.

Thus the rank-zero conclusions are stable at approximately the percent
level on the medium grid, while the tensor channels are not. Across the
current scan, transverse-profile variation is much larger than
wave-function variation; however the very small wave-only rank-zero band is
comparable to or below the remaining quadrature error and cannot yet be
resolved quantitatively. Decision D-031 records this boundary.

## 2026-07-25: Tensor radial-cancellation audit and resolution

Added `scripts/audit_evolved_gluon_tensor_convergence.py` and independently
varied radial order, polar order, azimuthal order, internal cutoff, segmented
order, segmented cutoff, and segment width at \(k_T=0.1,1.5\) GeV.

The global Gauss rule was non-monotonic: changing \(n_k\) moves all nodes
inside a strongly cancelling LL integral. In contrast, azimuthal changes
were below 0.15%, and a fixed segmented calculation showed that the
10--12 fm\(^{-1}\) tail contributes below \(4\times10^{-5}\) relatively to
the tensor observables.

Extended `build_off_forward_spin_quadrature` with an optional `k_min`, then
assembled fixed radial intervals. Six Gauss nodes per 0.5 fm\(^{-1}\)
interval through 12 fm\(^{-1}\) differ from a 0.25 fm\(^{-1}\)-interval
reference by:

- \(f_1^g\): 0.0069%;
- \(h_1^{\perp g}\): 0.0063%;
- \(f_{1LL}^g\): 0.273%;
- \(h_{1LL}^{\perp g}\): 0.594%.

This resolves the earlier 3--8% tensor instability and establishes the
radial component of the next production grid. Decision D-032 records the
new rule. The remaining production check is the angular order on this
segmented grid, followed by regeneration of the tensor uncertainty bands.

## 2026-07-25: Complete constrained spin-1 TMD catalog

Added `complete_tmd_model.py`, which evaluates every registry entry while
distinguishing derived, structural-zero, and constrained-model results.
Positive-rank coefficients use bounded physical modulation shapes; modeled
target-sector corrections obey a conservative block budget. T-odd functions
reverse exactly under future/past gauge-link reversal. Rank-zero quark
\(h_{1LT}\) has an analytic node giving a zero transverse integral.

The complete gluon catalog retains the small-b matched/CSS-evolved
\(f_1^g,g_1^g,h_1^{\perp g}\) calculation and its nine-member intrinsic/CS
profile envelope. Quark transversity is closed at 0.7 of the Soffer ceiling
and explicitly labeled as a model assumption.

Generated:

- `outputs/complete/spin1_tmd_phase_space.csv` (22,860 rows);
- adjacent complete-model metadata;
- `outputs/complete/spin1_tmd_predictive_coverage.csv`;
- adjacent predictive-coverage JSON.

The catalog covers 19 gluon, 18 quark, and 18 antiquark species-level
functions, u/d/s flavors, SIDIS and DY links, six x points, five k points,
and three Q values. Of 31 T-even functions, 29 are sign-resolved everywhere;
99.77% of nonzero T-even phase points are resolved. The full basis is
sign-resolved at 57.81% of nonzero points. The 24 T-odd functions remain
deliberately unresolved in magnitude while their process sign reversal is
exact.

The model and limitations are documented in
`references/complete_spin1_tmd_model.md`. Decisions D-033 and D-034 record
the closure assumptions and refusal to manufacture T-odd precision.
# 2026-07-25: complete production spin-1 TMD phase

- Updated the authoritative objective and accepted D-040: production
  completeness must be obtained from coherent correlator projection rather
  than independent amplitude priors.
- Added `ReducedCorrelatorTMDModel`, which projects six shared
  species-specific reduced helicity structures onto the complete
  definite-rank quark/antiquark/gluon registries.
- Added common nuclear \(D\)-state, spin--orbit, tensor-coherence, gluon
  linear-polarization, evolution-broadening, sea-dilution, and gauge-link
  phase parameters.
- Generated 43,862 dense rows at \(x_N=0.1,Q=5\) GeV for gluon,
  \(u,d,\bar u,\bar d\), SIDIS and DY, and 241 points on
  \(0\le k_T\le2\) GeV.
- Retained dimensional \(F\), supplemental physical ratios, and seven
  separate study envelopes. No combined confidence band was assigned.
- Generated central, seven separate-band, and ratio atlases for every
  requested species/flavor in PDF and PNG.
- Visually inspected representative gluon and quark atlases and corrected
  mathematical label rendering and envelope containment.
- Added table-level validation and five correlator-model unit tests.
  Validation passes, and all 161 repository tests pass in the configured
  LHAPDF Python 3.9 environment.
# 2026-07-25: persistent objective and parent-architecture correction

- Added a mandatory future-session discovery entry point, subsequently
  consolidated into `handoff/README.md`.
- Added `handoff/ROADMAP.md` with nine work packages, dependencies,
  temporary approximations, replacement tests, defects, gates, and the exact
  next command.
- Added the 28-item implementation audit and marked reduced-amplitude
  complete-TMD outputs as superseded production physics.
- Added machine-readable evidence, mechanism, validity, uncertainty, and
  replacement-interface provenance.
- Added proton/neutron-separated impulse convolution.
- Added the full 18-function spin-1 quark Cartesian correlator basis and
  joint projector, including a rank-zero origin projector.
- Added the complete eight-function spin-half nucleon quark correlator with
  flavor-resolved proton/neutron inputs.
- Added one-pass parent quark convolution and retained p/n components.
- Added correlator-level separated shadowing, antishadowing, and EMC-like
  sensitivity mechanisms; these are explicitly temporary, not fits.
- Added the parent-derived quark exporter; a fixture run is the next action.
- Focused tests passing: provenance (2), quark correlator (5), nucleon
  correlator (4), nucleon inputs (2), parent quark (2), nuclear mechanisms
  (2), and existing GTMD convolution (11).
- Current working state is uncommitted in a repository whose Git root is
  above this project; broad status output contains unrelated home files.
  Do not clean them.
- Completed the first end-to-end AV18 parent-derived quark fixture:
  9 \(k_T\) points, four flavors, both gauge links, all 18 functions,
  retained p/n terms, three separated nuclear corrections, and model total
  (9,072 rows).
- Added and passed `validate_parent_derived_quark_tmds.py`. Maximum p+n
  reconstruction residual is \(4.8\times10^{-14}\), mechanism residual is
  \(2.2\times10^{-15}\), real-boundary T-odd values are below
  \(5.3\times10^{-14}\), and coarse-grid azimuth covariance is within 1.7%
  for resolved values. The maximum absolute azimuth difference is
  \(2.7\times10^{-6}\).
- Exact reproduction:
  `PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9
  scripts/validate_parent_derived_quark_tmds.py
  outputs/parent_tmds/quark_av18_fixture.csv --azimuth-partner
  outputs/parent_tmds/quark_av18_fixture_phi091.csv
  --azimuth-relative-tolerance 0.02 --output
  outputs/parent_tmds/quark_av18_fixture.validation.json`.

# 2026-07-25: reproducible analysis and PDF-verification environment

- Declared pandas, Matplotlib, pypdf, and PyMuPDF in the `analysis`
  optional dependency group and added `environment.yml` with LHAPDF 6.5.5.
- PyMuPDF 1.26.5 was installed after Poppler commands were unavailable; it
  rendered the 72-page quark and 18-page gluon atlases for visual QA.
- Exact setup, platform versions, PDF data paths, roles, and citations are
  recorded in `references/environment_setup.md`.
- Import verification succeeded for NumPy, SciPy, pandas, Matplotlib,
  LHAPDF, pypdf, and PyMuPDF. The full 180-test suite passed before the
  subsequent coherent-component additions; focused component tests pass.

# 2026-07-25: six-wave parent ensemble and coherent wave components

- Generated and validated quark/antiquark and matched/CSS-evolved gluon
  parent tables for AV18, CD-Bonn, NV-Ia, NV-Ib, NV-IIa, and NV-IIb.
- Added one-pass coherent `SS`, `SD`, `DS`, and `DD` convolution paths for
  quarks and gluons. Both validators now require their sum to reconstruct
  the impulse result.
- Gluon p+n residuals are below \(4.5\times10^{-16}\); component residuals
  are below \(1.6\times10^{-12}\), or \(3.5\times10^{-13}\) relative to the
  largest raw coefficient. T-odd boundary values are stored as exact zero.
- Added 241-point PCHIP visualization layers and 72-page quark plus 18-page
  gluon PDF atlases. The source knots and metadata state that interpolation
  adds no physical information.
- Rendered representative first, middle, and final PDF pages with PyMuPDF.
  Fixed misleading plots of floating-point T-odd leakage by enforcing the
  exact real-boundary zero and annotating those pages.
- Full suite before component addition: 180 tests passed. Focused current
  tests: parent quark 3/3 and GTMD convolution 14/14 pass.

# 2026-07-25: sourced nuclear interfaces and b1 mechanism benchmark

- Replaced the simple Gaussian shadowing shape with a replaceable
  diffractive input and explicit \(q_L=2m_Nx\) coherence form factor.
- Replaced the quadratic `emc_like` multiplier with a virtuality-dependent
  off-shell response interface; the output mechanism is now `off_shell`.
- Defaults remain temporary functional surrogates and cite the
  Frankfurt-Guzey-Strikman and Kulagin-Petti frameworks. Tests inject
  replacement inputs and verify their use and regime behavior.
- Added `compare_b1_shadowing_to_hermes.py`. The resulting plot demonstrates
  that the leading-twist shadowing sensitivity remains close to impulse and
  does not reproduce the large low-x HERMES central values; no fit was
  manufactured.
- `pip install -e '.[analysis]'` succeeded from the declared pyproject.
- Full suite after coherent components and initial shadowing interface:
  184 tests passed. Current nuclear mechanism suite after off-shell addition:
  5 tests pass.
- Regenerated and validated all six quark tables using the renamed
  `off_shell` mechanism, then rebuilt the dense ensemble tables and atlases.
- Required next action: implement a sum-rule-linked antishadowing input,
  regenerate its affected outputs, and run the full suite.

# 2026-07-25: sum-rule antishadowing and independent quark convention audit

- Antishadowing now integrates the configured shadowing momentum loss for
  each flavor and normalizes its enhancement to restore the declared
  fraction. AV18 lost/restored values agree at machine precision.
- Downloaded arXiv:1612.06585 and audited all 18 quark structures against
  Eqs. (12)-(20).
- Found and fixed a missing epsilon rotation in rank-three `h1TTperp`; the
  previous expression violated light-front parity.
- Added direct contraction, all-18 LF parity, and complete T-odd
  gauge-link-reversal tests.
- Regenerated and validated all six quark parent tables and dense atlases.
  Medium AV18 azimuth covariance is 0.402% relative for resolved values and
  \(6.85\times10^{-9}\) maximum absolute.
- Full repository suite: 191 tests passed.
- Next action: WP3 nucleon positivity-matrix scan and collinear/tensor-charge
  sum-rule validation.

# 2026-07-25: quark convergence and complete gluon TT projection

- Generated `quark_av18_medium.csv` at \(16\times12\times8\) and
  `quark_av18_fine.csv` at \(24\times16\times12\), each with 9 external
  points and 9,072 traced rows.
- The original \(8\times6\times6\) fixture differs from medium by 24.9% in
  L2 norm and is now explicitly regression-only. Medium differs from fine
  by 0.462% in L2; maximum resolved p/n relative deviation is 0.680%.
- Added `project_deuteron_gluon_tt`. It maps the two Cartesian spin-1 TT
  components onto all four independently identifiable leading-twist gluon
  quantities and explicitly returns `f1TT_minus_h1TTperp`.
- Added `convolve_gluon_gtmd_components`, retaining proton and neutron
  correlators separately before their sum.
- All 24 focused gluon-correlator/convolution tests passed after the TT
  change; the expanded convolution module alone has 13 passing tests.
- Next action: connect the existing matched/CSS-evolved
  `InterpolatedSpinHalfGluonGTMD` boundary to a complete traced gluon
  exporter. Do not fall back to the older Gaussian IA script.

# 2026-07-25: nucleon positivity and tensor-charge correction

- Constructed and scanned the complete \(4\times4\) target-helicity/quark-spin
  density matrix for proton and neutron \(u,d,\bar u,\bar d\) inputs at
  2,304 production-support points. The minimum eigenvalue is
  \(3.2149\times10^{-10}\), so the scanned boundary is positive.
- The audit exposed an invalid temporary constant-Soffer boundary:
  \(\delta u=3.4692,\delta d=-1.2713\). Replaced it with a bounded,
  flavor-dependent shape normalized to JAMDiFF Table II
  \(\delta u=0.71,\delta d=-0.200\) at \(\mu=2\) GeV.
- Added a moment-reproduction unit test and a production validator containing
  positivity, valence-number, Gaussian normalization, and tensor-charge
  evidence. The CT18 valence moments are 1.99582 and 0.99775.
- Downloaded and retained `references/arxiv_2306.12998_transversity.pdf`.
- Installed `pytest==8.4.2` into the validated Python 3.9 environment and
  declared `pytest>=8.4,<9` in the analysis dependency group.
- Regenerated and validated all six medium quark parent tables and rebuilt
  the dense quark ensemble/atlas. Full repository suite: 194 tests pass.
- Next executable action: add a replaceable transversity fit-grid/replica
  adapter with covariance and scale evolution, then validate pointwise source
  bands. Do not reinterpret the current bounded central shape as a fit.

# 2026-07-25: JAMDiFF pointwise transversity ingestion

- Cloned the authors' public JAMDiFF library at commit
  `2d601943b003ab03d261d492b565c1ebf54d07cc` and evaluated all 969 `wLQCD`
  replicas on 171 x points and five \(Q^2\) slices.
- Added a reproducible extractor, a compact 3,420-row mean/std table, and a
  non-extrapolating flavor/scale adapter with tests.
- Replaced the production moment-shaped transversity with the evolved JAMDiFF
  central \(u,d,\bar u,\bar d\) functions. Enforced positivity using the
  actual CT18+BDSSV TMD widths, including a documented large-x sea endpoint
  required by the otherwise unconstrained posterior mean.
- The composed moments are 0.680 and -0.193, close to the source 0.710 and
  -0.200 after restricting the table and enforcing cross-PDF positivity.
- Regenerated/validated all six quark parent tables and rebuilt the dense
  central-line/six-wave atlas. Full suite: 196 tests pass.
- Remaining transversity task: preserve individual replica identity rather
  than only mean/std so cross-x/flavor covariance reaches nuclear bands.

# 2026-07-25: complete spin-1 quark positivity audit

- Added the exact \(3\otimes2=6\)-dimensional target-helicity/quark-spin
  density matrix to `Spin1QuarkCorrelator`.
- Extended the parent-table validator to reconstruct that density from all
  18 named TMD coefficients for proton impulse, neutron impulse, their sum,
  and the nuclear model total.
- All six wave functions pass semidefinite positivity. For AV18 the minimum
  eigenvalues are 0.000376 (p), 0.000376 (n), 0.001201 (impulse total), and
  0.001224 (model total), all at resolved antiquark/high-\(k_T\) points.
- Full repository suite: 197 tests pass.
- Next positivity action: formulate and test the spin-1 target x gluon
  helicity density matrix, including the identifiable TT combination.

# 2026-07-25: complete spin-1 gluon positivity audit

- Added the \(3\otimes2=6\)-dimensional target-helicity/transverse-gluon
  density matrix and exact reconstruction from all 18 identifiable named
  coefficients.
- Treated the TT degeneracy without a prior: the stored
  `f1TT_minus_h1TTperp` multiplies the unique fixed-\(k_T\) basis tensor.
- Extended the gluon validator and passed proton, neutron, and impulse-total
  semidefinite checks for AV18, CD-Bonn, NV-Ia, NV-Ib, NV-IIa, and NV-IIb.
  AV18 minima are 0.11557, 0.11557, and 0.23113 respectively.
- Full repository suite: 198 tests pass.
- Next executable action: verify commuting parent TMD/PDF reductions and
  rank-weighted collinear marginal constraints from the same stored
  correlators.

# 2026-07-25: gluon parent collinear reduction and W-term limitation

- Added a real-input \(b_T=0\) retained-index validation against independent
  spherical LF smearing. All six wave functions reproduce f1 at machine
  precision and f1LL within \(1.7\times10^{-11}\) relative.
- Confirmed the one-body collinear h1TT gluon null from the absence of a
  symmetric-traceless gluon-index component in a spin-half collinear parent.
- Generated a 121-point AV18 W-term stress grid through 5 GeV. Its raw
  finite-\(k_T\) integrals differ from exact b=0 by 14.3% (f1) and 54.3%
  (f1LL), demonstrating cutoff sensitivity from the missing Y term.
- Added explicit `full_kT_marginal: false`, low-k W-term scope, and missing-Y
  labels to all six production metadata files. No artificial rescaling was
  introduced.
- Full repository suite remains 198 tests passing.
- Next action: implement the analogous production quark collinear reduction,
  including f1, g1, h1, f1LL and the h1LT zero-marginal constraint.

# 2026-07-25: quark production collinear reduction

- Added a rank-zero collinear parent constructor using the production CT18,
  BDSSV24, and JAMDiFF inputs through the retained LF spectral kernel.
- Validated all \(u,d,\bar u,\bar d\) flavors for all six wave functions at
  \(x_N=0.1,Q=5\) GeV. Independent f1/f1LL LF smearing agrees within the
  declared \(10^{-9}\) tolerance; AV18 h1LT is below \(2.5\times10^{-20}\).
- The validation outputs retain parent f1, g1, h1, f1LL, and h1LT, so the
  inclusive isoscalar equality is visibly distinguished from the separately
  retained proton/neutron flavor structure.
- Added a synthetic rank-zero structural test. Full suite: 199 tests pass.
- Next executable action: complete fine quadrature convergence for the five
  non-AV18 quark wave functions, then set the production rule from the
  six-member evidence rather than the AV18 result alone.

# 2026-07-25: six-wave parent-quark convergence closure

- Generated and fully validated \(24\times16\times12\) and
  \(32\times20\times16\) parent-derived tables for AV18, CD-Bonn, NV-Ia,
  NV-Ib, NV-IIa, and NV-IIb. Each table has 14,256 rows spanning four
  flavors, two gauge links, 11 mechanism/component views, nine external
  momenta, and all 18 leading-twist quark TMDs.
- Added `scripts/audit_quark_parent_convergence.py`, which enforces one-to-one
  physical-key matching, a full-table relative L2 tolerance, and a mixed
  absolute/relative pointwise tolerance while retaining raw diagnostics.
- The former \(16\times12\times8\) candidate fails: worst relative L2 is
  1.283% and worst mixed normalized error is 2.278.
- The \(24\times16\times12\) candidate passes against
  \(32\times20\times16\): worst relative L2 is 0.5653% and worst mixed
  normalized error is 0.792.
- Promoted \(24\times16\times12\) to the exporter default and rebuilt the
  smooth quark ensemble/atlas from the converged tables. Gluon visualization
  continues to use its independently audited medium tables.
- Evidence:
  `outputs/parent_tmds/quark_medium_vs_fine_convergence.json`,
  `outputs/parent_tmds/quark_fine_vs_ultrafine_convergence.json`, and
  `outputs/parent_tmds/ensemble/ensemble.metadata.json`.
- Next executable action: serialize the unprojected quark and gluon parent
  correlators with round-trip projection tests.

# 2026-07-25: production parent-correlator serialization

- Added portable serializers/deserializers for the quark vector, axial, and
  transverse parent matrices and the full spin-1 gluon tensor.
- Both production exporters now write convolution-time
  `*.correlators.csv` companions automatically and record their paths,
  formats, and row counts in metadata.
- Regenerated all six converged quark and all six gluon production datasets.
  Quark files contain 28,512 complex matrix entries each; gluon files contain
  2,268 each.
- Added independent round-trip projection validation. All twelve production
  datasets pass with residuals below \(2\times10^{-11}\ {\rm GeV}^{-2}\).
- Revalidated all parent tables, rebuilt the fine-grid quark/medium-grid
  gluon ensemble atlas, and ran the full suite: 202 tests pass.
- Corrected stale quark metadata to identify the JAMDiFF transversity input
  and current covariance limitation.
- Next executable action: put explicit node-by-node bound-nucleon virtuality
  into the LF spectral kernel and replace the average-virtuality off-shell
  correction.

# 2026-07-25: explicit LF spectral virtuality and off-shell convolution

- Added node-resolved struck-nucleon virtuality with an on-shell spectator:
  \(p^0=M_D-\sqrt{m_N^2+\boldsymbol{k}^2}\) and
  \(v=(p^2-m_N^2)/m_N^2\).
- Added a node-response hook to the coherent quark convolution and moved the
  off-shell response inside the LF integral. The exported off-shell parent is
  the explicit response-weighted result minus the unchanged impulse parent.
- Disabled the superseded average-virtuality correction in production.
- Six-wave weighted mean virtualities span -0.0369 to -0.0448; the retained
  \(v<-0.3\) tail spans 1.18--2.17% of spectral weight and is recorded in
  metadata rather than silently clipped.
- Regenerated fine and ultrafine projection and parent-matrix datasets for
  all six wave functions. The refreshed audit passes with worst relative L2
  0.5662% and mixed pointwise normalized error 0.792.
- All production and ultrafine parent, positivity, and serialized-correlator
  validations pass. Rebuilt the atlas; full suite: 204 tests pass.
- Remaining limitation: `default_off_shell_input()` is still a qualitative
  KP-shaped response with a 50% bracket. Next action is to locate and ingest
  a versioned fitted table/covariance or document why no public numerical
  artifact can be used.

# 2026-07-25: CJ26 fitted off-shell response

- Audited the newly released CJ26 v1 primary source
  (arXiv:2605.31424, May 2026) and its TeX parameter tables.
- Replaced the qualitative KP-shaped response with the midpoint of the CJ26
  additive/multiplicative higher-twist cubic fits. Added exact coefficient
  and marginal-error tests.
- Combined the scenario half-range and diagonal marginal-error propagation
  as the present uncertainty. Recorded that CJ26 does not release the
  off-shell coefficient covariance/Hessian members and that \(x>0.7\) is an
  extrapolation region.
- Archived the paper and added a dedicated provenance/convention document.
- Regenerated all six fine and ultrafine parent/projection datasets,
  revalidated positivity and exact parent round trips, and rebuilt the atlas.
  Fine/ultrafine convergence passes with worst L2 0.5644%.
- At \(x_N=0.1,Q=5\) GeV the fitted off-shell parent is 0.52--0.63% of the
  impulse norm across wave functions.
- Full suite: 205 tests pass.
- Next action: replace the temporary coherent-shadowing fraction with a
  sourced diffractive input carrying a declared normalization and uncertainty
  convention.

# 2026-07-25: anchored shadowing and parent-based mechanism refresh

- Replaced the arbitrary shadowing power law with published deuteron anchors:
  1.5% at \(x=10^{-2}\), 3% at \(x\le10^{-5}\), and zero at \(x=0.1\),
  before the independent LF coherence factor.
- Kept the 50% uncertainty and explicitly classified the gluon enhancement
  and tensor response as model extensions because inclusive deuteron data do
  not fix them.
- Added exact anchor tests.
- Added `refresh_quark_nuclear_corrections.py`, which deserializes stored
  parents, changes only coherent shadowing/antishadowing/model-total
  matrices, reprojects them, updates physical ratios and metadata, and leaves
  impulse/off-shell/wave parents untouched.
- Refreshed all fine and ultrafine datasets without recomputing the LF
  impulse convolution. All convergence, positivity, mechanism, and parent
  round-trip checks pass; rebuilt the atlas.
- Full suite: 206 tests pass.
- Remaining shadowing task: implement a full versioned DPDF/coherence
  integral and covariance. Next software task: explicit mesonic and
  non-nucleonic component interfaces with source-required activation.

# 2026-07-25: explicit mesonic/non-nucleonic baseline sectors

- Added `AdditionalNuclearComponentInput` with mandatory source, evidence
  class, mechanism type, validity domain, and uncertainty.
- Production now exports `meson_exchange` and `non_nucleonic` named rows and
  unprojected matrices. They are exact zeros only in the configured nucleonic
  baseline and are labeled unresolved/inactive in metadata.
- Added tests for sourced activation, automatic out-of-domain deactivation,
  Hermitian return contracts, and exact model-total reconstruction.
- Extended the parent-based refresh path and validator mechanism sum. The
  first refresh attempt correctly failed because matrix rows existed without
  named projection rows; fixed the materialization logic and reran all
  outputs.
- All six production tables, convergence, parent round trips, and atlas
  rebuild pass. Full suite: 207 tests pass.
- Next action: implement a controlled charge-symmetry-breaking/QED component
  while preserving exact isospin as a tested switchable limit.

# 2026-07-25: controlled CSB/QED interface

- Added `ChargeSymmetryBreakingInput`, a source/provenance-bearing,
  validity-bounded relative response resolved by nucleon, flavor, named TMD,
  \(x\), and \(Q\).
- Preserved the exact charge-symmetry rotation as the explicit production
  limit and attached its independently inspectable provenance to both
  nucleon models.
- Added tests showing the exact inclusive isospin relation, a controlled
  nonzero neutron-u response that breaks it without identifying u and d,
  automatic out-of-domain deactivation, and rejection of a hidden nonzero
  “exact” response.
- Production metadata now states that QED/physical CSB is inactive and gives
  the replacement interface; transverse widths are deliberately unchanged.
- Full validation command:
  `/Users/dustin/miniforge3/bin/python3.9 -m pytest -q`
  — 210 tests pass.
- No dependency changes were required. The bare `pytest` command is not on
  the shell PATH; use the recorded project interpreter above.
- Remaining requirement: ingest a versioned QED-evolved or fitted numerical
  proton/neutron CSB input with uncertainty members. Interface completion is
  not numerical physics completion.
- Next executable action: implement the versioned DPDF/coherence shadowing
  adapter and uncertainty-member tests specified in WP5.

# 2026-07-25: official H1-DPDF / FGS coherent shadowing

- Downloaded and checksummed the official H1 2007 Jets DPDF v1.0 singlet,
  gluon, and flux release under `data/raw/h1_2007_dpdf/`; no new software
  dependency was needed.
- Added exact grid parsing and H1 bilinear log interpolation, including the
  released boundary clamp and signed NLO edge values.
- Implemented the FGS deuteron double-scattering integral with reconstructed
  differential flux, wave-specific LF body form factor, real-part correction,
  \(16\pi\) convention conversion, and separate quark/gluon
  \(x_{\mathbb P}\) cutoffs.
- The initial implementation omitted \(16\pi\) and yielded 0.03% at the
  benchmark. Primary-source convention review diagnosed the defect; the
  corrected AV18/CT18 u result is 1.54% at \(x=10^{-2},Q=5\) GeV.
- Added named DPDF normalization and flux-slope scenarios. They are not
  mislabeled as unavailable H1 Hessian members.
- Wired the kernel flavor by flavor into new exports, parent-only refresh,
  and momentum-sum-normalized antishadowing.
- The refresh stopped once on the discoverable `cd-bonn`/`cd_bonn` artifact
  naming mismatch; centralized the mapping and resumed without overwriting
  unrelated data.
- Refreshed all six fine and six ultrafine quark families. All mechanism,
  positivity, serialized-parent, and convergence audits pass. Worst
  fine/ultrafine L2 is 0.56434%; worst mixed pointwise normalized error is
  0.79156. Rebuilt the ensemble atlas.
- Full suite:
  `/Users/dustin/miniforge3/bin/python3.9 -m pytest -q`
  — 214 tests pass.
- Remaining DPDF work: propagate named members into covariance outputs;
  ingest true eigenvectors if released; do not use unpolarized diffraction
  as a measured polarized/tensor DPDF.
- Next executable action: implement member-resolved shadowing covariance
  export from stored parent matrices.

# 2026-07-25: H1/FGS named shadowing response export

- Exported 9,360 central and named H1/FGS response rows over all six wave
  functions, four light flavors, three scales, and 26 x points, plus a
  member envelope and machine-readable provenance.
- Preserved each member coherently across every axis. The output is
  deliberately not called a covariance because the official H1 v1.0 release
  provides central grids rather than replicas or Hessian eigenvectors.
- Added an explicit beta-boundary-clamp flag for diagnostic rows below
  \(x=10^{-4}\), outside the declared production validity.
- Added a production quadrature convergence test: 48 versus 64 points agrees
  below \(10^{-4}\) relative and 32 versus 64 below \(2\times10^{-4}\).
- Next executable action: reproduce and ingest the public BPV20 N3LO
  500-replica Sivers boundary and its arTeMiDe evolution under WP6.

# 2026-07-25: fitted BPV20 Sivers central through the nuclear parent

- Vendored arTeMiDe v2.05 at commit
  `ea0af1a75e21e316c1ac4ece51933988836a6650`, parsed the official BPV20 N3LO
  central plus 500 contiguous replicas, and checksummed the fit/PDF inputs.
- Created the reproducible `.conda-artemide` toolchain from
  `environment-artemide.yml`: Python 3.9, NumPy 1.26, gfortran 15.2,
  LHAPDF 6.5.5, and setuptools 59.8 for historical f2py compatibility.
- Built both the Fortran library and Python harpy binding. The first harpy
  build failed because setuptools 80 removed the numpy.distutils compatibility
  module; pinning 59.8 fixed the diagnosed incompatibility.
- Removed obsolete pion/fragmentation inputs from a generated proton-only
  constants file without changing the BPV20 proton Sivers or evolution
  sectors. Download attempts for obsolete LHAPDF names returned CERN 404
  pages and those files are not used.
- Added a full-momentum TMD component path so the evolved fitted Sivers
  function bypasses the former Gaussian profile assumption.
- A standalone Fortran formula and compiled arTeMiDe probe agree with the
  Python boundary/evolution fixtures to machine precision.
- A direct full exporter run was safely interrupted before writing when its
  redundant T-even recomputation proved too slow. Replaced it with a
  vectorized Sivers-only LF contraction over the same stored quadrature and
  an idempotence guard, then reconstructed nuclear corrections from the
  updated proton/neutron parents.
- Refreshed all six fine and six ultrafine projection and parent-matrix
  families. All 24 validators pass. Fine/ultrafine convergence passes with
  worst relative L2 0.56436% and mixed normalized error 0.83445 using a
  \(5\times10^{-7}\) GeV\(^{-2}\) absolute floor for unresolved off-shell
  Sivers values.
- Full suite: 220 tests pass.
- Known physics tension: BPV20 itself reports parton-model positivity-bound
  violations. Constituent p/n diagnostics expose them; the physical deuteron
  impulse and corrected totals pass positivity and remain hard gates.
- Next executable action: propagate all 500 BPV20 replicas through the
  vectorized nuclear contraction and export smooth 68% bands. Central-member
  completion is not uncertainty completion.

# 2026-07-25: BPV20 fitted-replica nuclear bands

- Generated a compressed, member-preserving Q=5 GeV momentum cache for all
  500 official replicas, four light flavors, 65 logarithmic x nodes, and 121
  low-k-refined transverse-momentum nodes using the native arTeMiDe v2.05
  Ogata transform. The 96-point seeded direct audit gives 0.308% p95 and
  1.776% maximum sampled interpolation error.
- Propagated every member through the exact stored fine-grid LF convolution
  for AV18, CD-Bonn, NV-Ia, NV-Ib, NV-IIa, and NV-IIb, including separately
  stored proton, neutron, impulse, node-wise CJ26 off-shell, and model-total
  contributions. Member identity is retained in compressed outputs.
- Exported separate BPV20 16th-84th percentile intervals and six-wave central
  envelopes. The BPV20 central member 0 remains distinct from the physical
  members 1-500 and from their mean/median. Past/DY intervals are exact signed
  reversals of future/SIDIS intervals.
- Built and rendered a four-page production atlas. Proton/neutron panels
  explicitly show the distinct flavor contributions; equality of deuteron u
  and d totals follows only after exact-charge-symmetry p+n composition.
  BPV20's common fitted light sea remains an explicit source-level assumption.
- Native arTeMiDe reports Ogata convergence warnings for a small subset of
  slow-decaying low-k replica evaluations. No members were clipped. Robust
  percentile bands are primary; heavy-tail mean/std columns are diagnostic.
- Outputs:
  `data/processed/bpv20_sivers_replicas_Q5.npz`,
  `outputs/parent_tmds/uncertainty/bpv20_sivers_*_fine.csv`,
  `outputs/parent_tmds/ensemble/bpv20_sivers_bands.csv`, and
  `outputs/parent_tmds/ensemble/bpv20_sivers_atlas.pdf`.
- Full suite after the optimal-scheme scale guard:
  `/Users/dustin/miniforge3/bin/python3.9 -m pytest -q`
  — 223 tests pass.
- Investigated the next proposed scale/profile band. The released optimal-TMD
  scheme reports c1 and c3 as nonexistent, ignores c4 in Sivers, and applies
  c2 only to process cross sections. A first test expecting a c1 response
  failed identically and exposed the issue. The API now rejects nontrivial
  standalone TMD scale factors instead of silently exporting nominal copies.
  Fit-defining profile parameters remain correlated inside the replicas.
- Next executable action: implement observable-level hard-scale variation and
  a sourced fixed-order Y term or explicit low-k validity gate.

# 2026-07-25: member-level positivity and JAMDiFF covariance

- Added the full 6x6 spin-1 target/quark density eigenvalue audit to every
  propagated BPV20 member. Across six waves, both links, four flavors, and
  impulse/model totals, 296/500 members trigger the tree-level PSD diagnostic;
  the worst eigenvalue is -0.0470732. No clipping or fit redefinition was
  performed because applicability is scheme dependent for evolved
  soft-subtracted TMDs.
- Cloned the official JAMDiFF library at its recorded commit. Its LHAPDF set
  resolves the earlier covariance gap and corrects the member count: member 0
  is central and members 1--968 are physical replicas.
- Added a member-preserving fixed-Q cache. A 384-node x grid has 0.149% p95
  and 0.236% maximum relative interpolation error in the seeded direct audit.
- Propagated all 968 members through AV18, CD-Bonn, and four Norfolk LF
  parents for u,d,ubar,dbar, retaining proton, neutron, impulse, node-wise
  off-shell, and model-total contributions. Each member receives the same
  explicit sea endpoint and composed CT18+BDSSV TMD Soffer projection.
- Independent member-0 recomputation agrees with stored nuclear h1 at better
  than 0.04% of the output scale. Produced and visually verified smooth fit
  intervals and separate six-wave envelopes in
  `outputs/parent_tmds/ensemble/jamdiff_transversity_atlas.pdf`.
- Full suite: 225 tests pass.
- Propagated the same 968 identities through the derived WW h1Lperp integral
  and all six LF parents. Member-0 integration reproduces stored production
  centrals within 0.4% of output scale. Generated and visually verified the
  separate smooth h1Lperp atlas; this is correlated fitted-input uncertainty,
  not a genuine twist-3-breaking band.
- Next executable action: complete matched b-space evolution for remaining
  quark inputs and connect the evolved boundaries to the nuclear parent.

# 2026-07-25: production quark-parent angular covariance

- Added `scripts/audit_quark_parent_azimuth_covariance.py`. It rotates a
  complete covariant synthetic spin-half correlator with radial momentum
  dependence through the physical AV18 light-front parent and projects all
  18 leading-twist spin-1 quark TMDs at three external transverse momenta.
- At production internal quadrature \(24\times16\times12\), the maximum
  absolute azimuthal difference is \(7.61\times10^{-14}\ {\rm GeV}^{-2}\)
  and the maximum resolved relative difference is \(2.12\times10^{-9}\).
  Doubling the internal azimuthal order reduces the resolved relative
  difference to \(2.50\times10^{-11}\). This passes the predeclared 1% and
  0.25% limits by many orders of magnitude.
- Reproduce with:
  `/Users/dustin/miniforge3/bin/python3.9 scripts/audit_quark_parent_azimuth_covariance.py`.
  Evidence is stored in
  `outputs/parent_tmds/quark_parent_azimuth_covariance.validation.json`.
- Next executable action: extend the independent quark and gluon production
  \(b_T=0\) reductions across x, Q, flavor, and all six wave functions. The
  matched quark-evolution task remains open because the existing CSS module
  is explicitly a gluon-only intermediate scheme and cannot be relabeled
  consistently.

# 2026-07-25: multi-kinematic parent collinear reductions

- Added `scripts/audit_parent_collinear_reductions.py`, reusing each physical
  production quadrature while comparing the retained-helicity parent to an
  independently constructed spherical LF collinear smearing.
- Covered AV18, CD-Bonn, and four Norfolk waves; \(x_N=0.03,0.1,0.3\);
  \(Q=2,5\) GeV; \(u,d,\bar u,\bar d\); and gluons. The 180 quark and 36
  gluon points pass.
- Maximum \(f_1\) relative residual is \(2.56\times10^{-14}\). Tensor
  \(f_{1LL}\) uses a mixed criterion because D-state zeros make a
  relative-only test ill-conditioned: relative below \(10^{-9}\) or absolute
  below \(10^{-12}\ {\rm GeV}^{-2}\) at each point. Forbidden quark
  \(h_{1LT}\) leakage is \(3.84\times10^{-20}\ {\rm GeV}^{-2}\).
- Reproduce with:
  `/Users/dustin/miniforge3/bin/python3.9 scripts/audit_parent_collinear_reductions.py`.
  Full point evidence is in
  `outputs/parent_tmds/parent_collinear_reductions.validation.json`.
- Next executable action: implement the scheme-compatible quark matched
  \(b_T\)-space boundary and parent adapter; do not reuse the explicitly
  gluon-only intermediate matching coefficients.

# 2026-07-25: first scheme-explicit quark b-space boundary

- Added `quark_tmd_matching.py` with an LO \(f_1,g_1,h_1\) boundary backed by
  the existing distinct proton/neutron flavor-resolved components. At
  \(b_T=0\) it exactly reproduces the collinear input; at finite \(b_T\) it
  uses the analytic transform
  \(\exp[-\langle k_T^2\rangle b_T^2/4]\).
- Added quark one-loop CSS evolution with
  \(A_q^{(1)}=C_F,\ B_q^{(1)}=-3C_F/2\), canonical \(b_*\) scale selection,
  and an explicitly optional model CS term.
- The interface rejects rank-one/rank-two and fit-native momentum TMDs. This
  is intentional: WW worm gears, pretzelosity, and BPV20 require their own
  tensor or optimal-scheme adapters and are not claimed complete.
- Focused matching/evolution suite: 11 tests pass after catching and fixing a
  missing \(C_F\) import.
- Added the common \(J_0\) b-to-k adapter for the three rank-zero quark
  scalars and an analytic Gaussian transform regression. The first full-suite
  run exposed an order-dependent LHAPDF global-path dependency in the new
  tests after arTeMiDe initialization; the fixture was replaced with a
  deterministic analytic flavor-resolved model. Full suite now passes:
  **231 tests**.
- Next executable action: add the rank-zero Fourier-to-momentum and nuclear
  parent connection, then implement convention-tested rank-one WW adapters.

# 2026-07-25: evolved rank-zero quarks enter the LF parent

- Refactored the named-TMD-to-spin-half-correlator composition into a shared
  function and added `EvolvedRankZeroQuarkModel`. It numerically transforms
  \(f_1,g_1,h_1\) with \(J_0\), leaves all other components in their native
  convention, reconstructs the full correlator, and is called at each
  recoil-shifted nucleon momentum inside the existing parent convolution.
- Analytic zero-evolution tests show that the transform and parent path
  reproduce the native Gaussian model. This explicitly rules out a post-hoc
  multiplicative evolution patch.
- The first physical audit exposed an attempted JAMDiFF evaluation below its
  \(Q^2=2\ {\rm GeV}^2\) grid. The default canonical floor is now
  \(\sqrt{2}\) GeV; no extrapolation was introduced.
- Added `scripts/audit_evolved_quark_parent_connection.py`. For AV18,
  \(x_N=0.1,Q=5\) GeV, \(k_T=0.3\) GeV and all
  \(u,d,\bar u,\bar d\), it retains distinct proton/neutron pieces and passes
  201-to-401 point b-grid refinement with maximum mixed relative change
  \(1.62\times10^{-5}\).
- Current limitation: the connection audit uses reduced \(8\times6\times6\)
  LF order. Production LF convergence and rank-one WW adapters remain next.
- Full regression suite after the parent adapter and source-domain guard:
  **235 tests pass**.

# 2026-07-25: production LF gate and rank-one quark evolution

- Extended the evolved-parent audit to AV18 medium
  \(16\times12\times8\) versus production \(24\times16\times12\). Across
  \(f_1,g_1,h_1\), four flavors, and separate proton/neutron/total pieces,
  the maximum mixed relative change is 0.5408%, below the 2% gate.
- Reused the same cached evolved nucleon boundary through AV18, CD-Bonn, and
  four Norfolk production spectral kernels. All six flavor- and
  nucleon-resolved projections are finite. The calculation confirms that
  nucleon evolution and nuclear wave structure remain modular.
- Implemented the rank-one Fourier map for WW \(g_{1T}\) and
  \(h_{1L}^{\perp}\): evolve \(i\hat b_iR(b)\), invert with \(J_1\), and use
  the analytic \(k_T=0\) limit. Zero-evolution Gaussian tests reproduce the
  native correlator.
- Added a log-scale interpolation for the expensive WW boundary integrals.
  `audit_rank_one_quark_evolution.py` covers proton, neutron,
  \(u,d,\bar u,\bar d\) at \(x=0.1,Q=5\) GeV and \(k_T=0.3\) GeV.
  Refining 25 to 49 scale nodes changes results by at most
  \(1.06\times10^{-7}\).
- Next executable action: propagate rank-one evolution through a cached
  multi-x LF parent grid, then implement the rank-two pretzelosity adapter
  and a nonzero replaceable pretzelosity ensemble.
- Full suite after the rank-one implementation: **236 tests pass**.

# 2026-07-25: rank-two pretzelosity separation and ensemble

- Implemented the \(J_2\) rank-two adapter derived from the project's
  \(-k_T^{ij}h_{1T}^{\perp}/M^2\) correlator convention, including the
  analytic \(k_T=0\) limit. Zero-evolution tests reproduce the native
  Gaussian rather than a rank-zero surrogate.
- Following arXiv:1808.10560, retained zero as the perturbative small-b
  central and added replaceable signed large-b bound-state members at
  \(\pm0.25\) of the transverse-moment positivity bound. These are model
  sensitivities, not a fit interval.
- `audit_pretzelosity_scenarios.py` checks proton/neutron,
  \(u,d,\bar u,\bar d\), four x values, and four transverse momenta.
  All central/signed scenarios pass the complete joint spin-density PSD
  diagnostic; the smallest nonzero-k eigenvalue is \(2.08\times10^{-6}\).
- Added `references/pretzelosity_input.md` with the field-theory rationale,
  convention, limitation, and reproduction commands.
- Full regression suite: **237 tests pass**.
- Next executable action: construct disk-backed multi-x evolved quark tables
  and propagate rank-one/rank-two scenarios through all six LF parents.

# 2026-07-25: disk-backed evolved quarks and six-wave propagation

- Added a portable fixed-\(Q=5\) evolved nucleon grid with 274 x nodes,
  161 momentum nodes through 3 GeV, 401 b nodes, and 25 canonical-scale
  nodes. It stores proton/neutron, four flavors, rank-zero/rank-one/rank-two
  components, and signed pretzelosity scenarios.
- The first 117-node x grid was rejected: direct validation found 5.7% sea
  \(h_{1L}^{\perp}\) bias near the log/linear transition. Refinement to 274
  nodes passes 576 direct comparisons with a 0.98% largest resolved error;
  high-k differences occur only below the \(2\times10^{-6}\) absolute floor.
- Added `EvolvedQuarkGridModel`, which replaces all six T-even components in
  one vector interpolation while retaining native process-dependent T-odd
  inputs and reconstructing the complete spin-half correlator.
- Propagated central and positive members explicitly through all six
  \(24\times16\times12\) LF parents; exact linearity constructs the negative
  member. The output has 19,440 rows covering all 18 spin-1 TMDs, four
  flavors, five external momenta, and proton/neutron/total pieces.
  Proton+neutron closure is \(7.58\times10^{-14}\ {\rm GeV}^{-2}\).
- Outputs:
  `data/processed/evolved_quark_tmd_Q5.npz`,
  `data/processed/evolved_quark_tmd_Q5.validation.json`, and
  `outputs/parent_tmds/evolved_quark_parent_scenarios.csv`.
- Next executable action: build smooth central/scenario/wave envelopes from
  the calculated knots, validate positivity of evolved parent scenarios,
  and connect process-level W+Y validity handling.

# 2026-07-25: evolved-parent positivity and complete atlas

- Reconstructed complete spin-1 correlators from every stored group and
  evaluated their 6x6 target/quark density spectra. All 1,080
  wave/scenario/flavor/momentum/part groups pass; the smallest eigenvalue is
  0.03881. The report retains the soft-subtracted-scheme applicability caveat
  without weakening the numerical gate.
- Built `output/pdf/evolved_quark_parent_atlas.pdf`: 18 pages, one for each
  leading-twist spin-1 quark TMD, with four flavor panels, separate AV18
  proton/neutron/total curves, signed pretzelosity bands, and six-wave
  envelopes. Positive-rank pages begin at the first identifiable nonzero
  momentum rather than plotting the origin projector's conventional zero.
- The accompanying
  `outputs/parent_tmds/ensemble/evolved_quark_parent_bands.csv` contains
  21,672 smooth visualization rows. PCHIP interpolation adds no new physics;
  every calculated knot remains in the source scenario table.
- Poppler was unavailable, so the PDF was rendered with installed PyMuPDF.
  Representative rank-zero, pretzelosity, and smallest-scale final pages
  were visually inspected. A first layout placed the x label over the legend
  and scientific-offset text obscured flavor titles; both defects were fixed.
- Full suite before atlas-only generation: **238 tests pass**.
- Next executable action: implement explicit low-k W validity metadata and a
  process-level fixed-order/Y interface; do not normalize W tails into a
  collinear sum rule.

# 2026-07-25: explicit W+Y validity contract

- Added `w_y_matching.py`. W-only evaluation is accepted only inside the
  declared low-qT domain; outside it the API raises unless a process-specific
  fixed-order Y remainder with process, order, source, and subtraction
  provenance is installed.
- The interface reports W and Y separately and never renormalizes the W tail.
  Synthetic tests verify domain boundaries, high-qT refusal, additive
  matching, and provenance enforcement.
- Full suite: **242 tests pass**.
- Next executable action: connect the contract to a concrete SIDIS observable
  with a sourced hard factor/asymptotic subtraction, then implement
  observable-level scale variations.

# 2026-07-25: SIDIS overlap gate

- Added a contiguous same-sign numerical W/ASY overlap assessment and made a
  passed result mandatory for high-qT W+Y evaluation, even when a Y callable
  exists. Tests cover both successful overlap and refusal after a failed
  assessment.
- Documented the process policy and primary source in
  `references/sidis_matching.md`. arXiv:1412.1383 shows that standard additive
  Y matching can fail at low/intermediate SIDIS energies; therefore no
  nominal high-qT JLab curve is exported without a consistent FO/ASY input.
- The current \(Q=5\) GeV process layer remains W-only inside its declared
  domain. A concrete fixed-order SIDIS implementation, fragmentation input,
  and numerical overlap evidence remain required.
- Focused W/Y suite: **6 tests pass**.
- Next executable action: investigate a maintained fixed-order SIDIS backend
  compatible with the installed fragmentation sets; if unavailable, continue
  the independently implementable numerical QED/CSB and nuclear mechanism
  work without weakening the matching gate.

# 2026-07-25: fixed-order backend audit and numerical QED CSB

- Audited official APFEL++ master and the vendored arTeMiDe SIDIS source.
  APFEL++'s SIDIS coefficient operators are collinear in \(x,z\); its TMD
  documentation and arTeMiDe both implement the resummed W term. Neither is
  a qT-differential FO/ASY backend. The high-qT refusal gate remains active.
- Downloaded the official paired `MSHT20qed_nnlo` DataVersion 2 and
  `MSHT20qed_nnlo_neutron` DataVersion 3 ensembles into
  `data/raw/lhapdf`. Both contain a central member and 38 Hessian pairs.
- Added `MSHT20QEDChargeSymmetryBreaking`. Its same-fit neutron/proton
  isospin-partner ratio isolates QED-driven neutron CSB without importing an
  MSHT-versus-CT18 baseline shift. Only neutron \(f_1\) is modified;
  polarized, T-odd, transversity, and width CSB remain explicit gaps.
- The adapter preserves paired member identity and exposes a 68% CL
  uncertainty. Its positive multiplicative validity ends at x=0.4 because
  the released central anti-up density changes sign near x=0.458 at Q=5 GeV.
- `audit_msht20qed_csb.py` exports 636 flavor/x rows. The largest relative
  correction on the declared grid is 0.334 (in a small sea channel), the
  largest Hessian uncertainty is 0.0530, and released-grid valence moments
  pass the 0.01 finite-grid tolerance with maximum residual 0.00581.
- Propagated the central response through all six production-order LF
  parents. `msht20qed_csb_parent.csv` stores 6,480 exact-isospin/CSB/delta
  rows for all 18 TMDs, four flavors, five momenta, and separate proton,
  neutron, and total pieces. Proton mechanism leakage is exactly zero and
  total-minus-neutron delta closure is \(7.81\times10^{-14}\) GeV\(^{-2}\).
- Full regression suite after the grid adapter and parent export:
  **248 tests pass**.
- Vectorized the neutron vector-projection mechanism across all 77 paired
  members while sharing LF nodes and spectral contractions. The member table
  contains 166,320 rows and the correlated 38-pair band table 2,160 rows.
  Hermiticity is exact numerically; vectorized member 0 agrees with the
  independent central convolution within \(2.01\times10^{-13}\)
  GeV\(^{-2}\).
- Next executable action: ingest a published numerical deuteron meson
  light-cone splitting distribution and pion input, with momentum accounting
  and a separate zero-meson limit.

# 2026-07-25: numerical tensor Sullivan pion parent and HERMES comparison

- Implemented Miller's AV18 tensor-polarized light-cone pion distribution
  from arXiv:1311.4561, including all published S/D interference terms,
  dipole form factor, and a pure-tensor spin-1 correlator adapter.
- Downloaded the official `JAM21PionPDFnlo` set and propagated all 786
  physical replicas. Every file, including member 0, is marked `replica`;
  the ensemble mean is therefore the central result and the sample standard
  deviation the PDF band.
- Added the exact zero-meson switch, AV18 radial-limit and tensor sum-rule
  tests, doubled-quadrature convergence, flavor/convention checks, and full
  nuclear-mechanism reconstruction. Focused suite: **16 tests pass**.
- Produced `output/pdf/b1_ia_pion_vs_hermes.pdf` and machine-readable central,
  replica, and validation tables. Visual PDF inspection passes. The
  experimental-error-only six-bin diagnostic chi-square is 21.34 for
  impulse and 7.55 for impulse plus pion; this is not a fit.
- The component is collinear and tensor-only. Spin-averaged pion momentum
  accounting and a transverse pion profile remain unresolved and are not
  replaced by a Gaussian ansatz.
- Exact reproduction:
  `PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
  tests/test_pion_exchange.py tests/test_nuclear_mechanisms.py` and
  `PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9
  scripts/compare_b1_pion_exchange_to_hermes.py`.
- Next executable action: source and implement the spin-averaged deuteron
  meson distribution for momentum accounting, and add the Miller six-quark
  term only as a distinct model-dependent non-nucleonic scenario.

# 2026-07-25: hidden-color six-quark observable scenario

- Implemented Miller's analytic six-quark \(b_1\) expression with
  \(R=1.2\) fm, \(m=338\) MeV, and exposed one-bin-calibrated
  \(P_{6q}=0.0015\).
- Four tests reproduce the published rounded table, exact probability
  scaling and zero limit, \(0<x<2\) support, variants, and the \(10^{-8}\)
  valence tensor sum rule.
- Updated and visually inspected the HERMES PDF. Diagnostic chi-square is
  3.56 after the fitted six-quark term, 7.55 for impulse plus pion, and
  21.34 for impulse alone.
- The source does not determine a flavor-resolved correlator, so the
  scenario remains observable-level instead of silently assigning flavors
  or a transverse profile.
- Full regression after both non-nucleonic additions: **258 tests pass**.
- Next executable action: source the spin-averaged deuteron meson splitting
  needed for momentum accounting and a non-nucleonic LF state with explicit
  flavor/spin/OAM content.

# 2026-07-25: spin-averaged connected pion and momentum refusal gate

- Derived \((f_\pi^{(0)}+2f_\pi^{(1)})/3\) from the same Miller AV18
  helicity formulas used by the tensor pion term. Independent direct
  \(m=0,\pm1\) integrals reconstruct both the spin average and
  \(f^{(0)}-f^{(1)}\).
- The connected pion number is 0.02129174 and its deuteron plus-momentum
  fraction is 0.00410205. A unit nucleonic parent plus this term totals
  1.00410205; production activation therefore refuses unless the missing NN
  momentum policy is explicitly acknowledged.
- Propagated all 786 JAM21 replicas on a 16-point \(x\) grid at \(Q=5\) GeV.
  The 120/240-node convolution difference is \(2.63\times10^{-6}\).
- Outputs: `outputs/figures/pion/spin_averaged_pion_jam21.csv`, all-member
  table, and `spin_averaged_pion.validation.json`.
- Next executable action: implement a sourced coupled NN/NNπ normalization
  or counterterm and investigate a phenomenologically constrained pion
  transverse profile; do not use a generic Gaussian.

# 2026-07-25: non-Gaussian pion transverse boundary with nuclear recoil

- Audited Vpion19 and the newer JAM 2023 simultaneous pion/proton extraction.
  The latter does not publish a callable replica ensemble; the vendored
  Vpion19 source contains its central and 100 replica parameter triples.
- Implemented the Vpion19 intrinsic nonperturbative factor as an explicit
  JAM18/BSV19-to-JAM21 transfer scenario.
- Retained the Sullivan \(q_T\) integration and inserted the required
  \(J_0(zbq_T)\) recoil factor rather than assigning one Gaussian width to
  both nuclear and pion-internal motion.
- Four tests cover source parameters, replica identity, intrinsic
  normalization, nuclear \(b=0\) reduction, and full collinear convolution
  reduction.
- Routed the boundary through the current rank-zero CSS adapter; a fifth test
  verifies origin reduction, finite nonzero-b evolution, and the
  non-production metadata contract.
- Full regression after the spin-average and transverse-boundary work:
  **266 tests pass**.
- Next executable action: replace the one-loop transfer scenario with an
  order-consistent pion evolution/refit, implement the NN/NNπ normalization,
  and validate Fourier/Hankel behavior before exporting a pion TMD curve.

# 2026-07-25: exact NN/NNπ Fock ledger and minimal nucleon closure

- Implemented \(Z=1+N_\pi=1.02129174\), giving physical NN and NNπ
  probabilities 0.97915215 and 0.02084785.
- Physical pion and NNπ-nucleon plus-momentum fractions are 0.00401653 and
  0.01683132. With the NN-sector entry, momentum closes to exactly 1.
- Applied \(1/Z\) to spin-average, tensor, direct-helicity, and
  transverse-recoil pion kernels.
- Added a replaceable unchanged-shape NNπ-nucleon closure with explicit 100%
  model uncertainty.
- Fock-normalized pion changes the diagnostic HERMES chi-square from 7.552
  to 7.336; the source-style \(Z\approx1\) result remains separate.
- Full regression: **268 tests pass**.
- Next executable action: replace the unchanged-shape closure with a coupled
  NN/NNπ spectral function and replace the one-loop pion transfer evolution.

# 2026-07-25: current hidden-color light-front source audit

- Audited the official source of Phys. Rev. D 113, 054008 (2026),
  arXiv:2507.09886, and the related BLFQ papers arXiv:2503.21371 and
  2505.12889.
- The 2026 cluster model supplies useful normalized spin-1 LFWF equations
  and \(f_1,g_{1L},f_{1LL}\) projections, but explicitly does not determine
  its singlet/octet mixture, uses pointlike S-wave clusters, and describes a
  deeply bound effective system.
- It is therefore a model-comparison target, not a production hidden-color
  probability or flavor/spin/OAM parent. Machine-readable BLFQ amplitudes
  remain the preferred replacement.

# 2026-07-25: effective-cluster scalar parent and spin diagnostic

- Implemented a self-adjoint Gauss-Legendre discretization of the equal-mass
  principal-value 't Hooft equation and the normalized holographic
  transverse \(L=0\) scalar LFWF from arXiv:2507.09886.
- Raised production quadrature to 320 nodes. The central mass is
  \(1.87458\) GeV; the 240-to-480-node longitudinal eigenvalue change is
  \(1.52\times10^{-3}\ {\rm GeV}^2\).
- Added exact spin-1 Clebsch--Gordan coupling and unitary constituent Melosh
  rotations as a controlled diagnostic. It preserves scalar probability
  pointwise and therefore produces exactly zero \(f_{1LL}\).
- This rules out the rotation-only shortcut for the source's nonzero tensor
  density. Next implement \(\bar v\gamma\!\cdot\!\epsilon^\Lambda u\) with
  Dirac, polarization, normalization, and published-curve benchmarks.
- Focused validation: **7 tests pass**. Full regression after integration:
  **275 tests pass in 30.07 s**.

# 2026-07-25: source-equivalent effective-cluster vector-current state

- Implemented explicit Lepage-Brodsky \(u,v\) spinors, gamma matrices,
  polarization vectors, and the incoming-state
  \(\bar v\gamma\!\cdot\!\epsilon^{\Lambda *}u\) vertex.
- Independently normalized longitudinal and transverse target states and
  projected cluster \(f_1,g_{1L},f_{1LL}\) from their helicity densities.
- Extracted all three 100-point vector paths from the official source
  `pdfs.pdf`. Maximum absolute residuals on \(0.05\le z\le0.90\) are
  0.01198, 0.01163, and 0.00164, respectively.
- Generated a comparison PDF/PNG, model CSV, and validation JSON. Bands are
  explicitly the extrema of one-at-a-time quoted parameter variations, not
  fit confidence intervals because no covariance is published.
- Focused validation now has **11 passing tests**. The scenario remains
  outside the production flavor-resolved correlator because the source does
  not specify cluster flavors, evolution, color mixture, or physical
  deuteron binding.

# 2026-07-25: flavor-resolved cluster convolution and HERMES comparison

- Added a replaceable proton/neutron PDF-provider convolution for individual
  quark and antiquark flavors. The source's explicit isoscalar average is
  retained without identifying flavors inside either nucleon input.
- Encoded the standard \(1/2\) hard prefactors for \(g_1\) and \(b_1\).
  Without it the source's quoted \(b_1\) moment is missed by exactly a factor
  two.
- NNPDF3.1 member 0 gives
  \(\int_{0.02}^{0.85}b_1\,dx=0.003615\), compared with the source's
  \(0.0036\pm0.0003\). The six-bin HERMES diagnostic chi-square is 11.34.
- Generated and visually inspected separate \(b_1\) and \(xb_1\) panels,
  with one-at-a-time cluster-parameter sensitivity and explicit uncertainty
  limitations.
- Focused validation now has **14 passing tests**.

# 2026-07-25: native high-order pion TMD transfer route

- Diagnosed that the proton-only BPV20 constants disable pion hadron 2 and
  that the attempted local JAM18 files are CERN error HTML.
- Added a dedicated constants generator restoring two-hadron uTMDPDF grids
  and substituting maintained JAM21 for unavailable JAM18.
- Implemented the native Vpion19 0--100 replica API with NNLO matching and
  BSV19 NNNLO evolution, plus isoscalar flavor averaging.
- Composed the native pion TMD with the exact unintegrated Miller nuclear
  recoil kernel. The one-loop route remains only as a diagnostic.
- Native arTeMiDe built both 250x750 hadron grids without errors. All 101
  Vpion19 identities and the central deuteron pion boundary are finite on
  the persisted \(b\)-space audit grid.
- This remains a low-\(k_T\) W-term transfer scenario, not production:
  JAM21 was not refitted and a fixed-order Y term is absent.
- Full regression after the cluster convolution and native pion route:
  **284 tests pass in 44.01 s**.

# 2026-07-25: conditional NNπ nucleon recoil and transverse kernel

- Replaced the preferred collinear unchanged-shape NNπ closure with
  `NNPiLongitudinalRecoilConvolution`.  For every pion \(y\), it evaluates
  an arbitrary-\(x\) baseline correlator after the exact longitudinal map
  \(\alpha_N'=(1-yM_N/M_D)\alpha_N\).
- The implementation transports complete flavor-resolved vector, axial,
  and transverse-spin correlator matrices.  It therefore preserves the
  conditional scalar-pion spin ratios without collapsing nucleon flavors.
- Tests prove exact nucleon-number and plus-momentum closure and distinguish
  the shifted \(x\) shape from the superseded unchanged-shape diagnostic.
- Exposed the source differential spin average
  \(d\bar f_\pi/dq_T^2\) and the retained-NN transverse recoil
  \(J_0(\alpha bq_T)\), with exact \(b=0\) and \(\alpha=0\) reductions.
- Focused validation: **15 tests pass** in `test_pion_exchange.py`.
- Remaining dynamical gap: a sourced three-body NNπ helicity amplitude with
  coupled transverse/off-forward recoil, nucleon virtuality response, and
  associated uncertainty.
- Next executable action: propagate the conditional builder through
  production flavor/spin parent tables, validate interpolation closure, and
  then implement the full transverse/off-forward spectral coupling.

# 2026-07-25: arbitrary-x serialized LF-parent provider

- Added `TabulatedQuarkCorrelatorProvider` to reconstruct a complete
  four-projection spin-1 quark correlator at arbitrary \(x_N\) from a
  multi-\(x\) serialized LF-parent table.
- It uses componentwise shape-preserving PCHIP interpolation, restores
  target hermiticity against roundoff, forbids implicit scale/sector
  substitution, and returns exactly zero outside supplied support instead
  of extrapolating a parton model.
- Focused correlator/NNπ validation: **20 tests pass**.
- Full regression after this provider: **290 tests pass in 44.20 s**.
- Next executable action: generate a production-quadrature AV18
  flavor-resolved multi-\(x\), \(k_T=0\) parent table; connect each flavor
  provider to `build_longitudinal_recoil_fock_component`; export minimal
  versus conditional-recoil projections and validate x-grid refinement.

# 2026-07-25: production AV18 multi-x NNπ recoil propagation

- Generated complete 24-by-16-by-12 AV18 LF parent tables at \(Q=5\) GeV:
  19 coarse anchors and 37 refined nodes for \(u,d,\bar u,\bar d\), with
  proton, neutron, and total correlators separately serialized.
- The 8,208-row coarse table has exactly zero target-Hermiticity residual.
  Proton \(u-d\) and \(\bar u-\bar d\) matrix distances are 28.78 and 16.00;
  the inclusive exact-isospin deuteron equality is explicitly classified as
  a symmetry limit rather than a flavor collapse.
- Propagated the spin-averaged pion, tensor pion, minimal unchanged-shape
  comparison, and preferred conditional recoil through all four flavors and
  the identifiable rank-zero spin projections.
- Linear-\(x\) PCHIP failed the small-\(x\) refinement audit and was replaced
  by PCHIP in \(\ln x\). The conditional total now changes by at most 0.439%
  of a curve peak under grid refinement; the much smaller
  conditional-minus-minimal correction changes by 6.93% of its own peak.
- Conditional recoil differs from the unchanged-shape model by up to about
  1.24% of valence and 1.49% of sea baseline \(f_1\) over the exported range.
- A dimensional audit found that the first exporter had evaluated the
  momentum-space TMD at \(k_T=0\), not the collinear \(b_T=0\) parent.
  That invalid mixed-dimension output was superseded in place. All tables,
  comparisons, replica bands, and figures were regenerated with the exact
  collinear LF contraction.
- The mechanism/grid audit uses explicitly selected JAM21 member 0; the
  subsequent production collinear central and PDF band propagate all 786
  replicas (see the next checkpoint).
- Next executable action: propagate the JAM21 replica ensemble without
  repeating the nucleon recoil calculation, export central/covariance bands,
  then couple retained-NN \(J_0(\alpha bq_T)\) recoil to the transverse
  parent.

# 2026-07-26: complete JAM21 replica propagation for conditional NNπ recoil

- Propagated all 786 JAM21 replicas through the refined AV18 conditional
  model while evaluating the expensive nucleon recoil only once.
- Persisted a 25 MB member-level table, ensemble-mean central, sample
  standard deviation, and q16/q84 bands for all four light flavors and five
  identifiable rank-zero projections.
- The 160-node fixed integration agrees with adaptive member-0 results to
  \(1.21\times10^{-5}\) relative for \(f_1\) and
  \(1.91\times10^{-5}\) for \(f_{1LL}\).
- Generated PDF/PNG figures with separate \(f_1\) and \(f_{1LL}\) scales;
  visually inspected the PNG and confirmed smooth central curves and visible
  uncertainty bands.
- Full regression: **290 tests pass in 45.22 s**.
- Next executable action: expose the active-nucleon LF fraction at the
  parent-integrand level and compose the retained-NN
  \(J_0(\alpha bq_T)\) factor there. Do not replace \(\alpha\) by 1/2 or
  multiply a collinearly integrated parent by an average recoil factor.

# 2026-07-26: retained-NN transverse recoil through the AV18 LF parent

- Derived the repository-convention recoil phase using \(x_D=x_N/2\):
  \(z\alpha=x_N/[2(1-\eta_\pi)]\). The active residual-NN fraction cancels
  exactly; the implementation does not use an average \(\alpha\).
- Added Fock-normalized b-space splitting and complete-matrix
  `nnpi_nucleon_b`/`nucleon_correction_b` methods.
- Added tests for exact collinear reduction, full spin-matrix transport,
  negative-b refusal, nontrivial finite-b behavior, and the factor-of-two
  Bessel convention.
- Propagated \(f_1\) and \(f_{1LL}\) through the actual AV18 24-by-16-by-12
  LF smearing with matched nucleon b-space inputs at \(x_N=0.1,Q=5\) GeV.
  The maximum b=0 residual against the independent refined collinear parent
  is \(2.91\times10^{-6}\).
- Full regression after the transverse implementation: **293 tests pass in
  44.70 s**.
- Next executable action: combine this retained-NN term with the existing
  native Vpion19 pion-internal \(J_0(zbq_T)\) term in a common ensemble
  output, then extend the three-body mechanism off forward with explicit
  virtuality/helicity correlations.

# 2026-07-26: common Fock-normalized native NNπ b-space scenario

- Corrected the native Vpion19 nuclear scenario to use the same
  \(1/(1+N_\pi)=0.97915215\) normalization as the retained-NN Fock ledger.
- Propagated all 100 physical Vpion19 profile replicas through the full
  nuclear \(J_0(zbq_T)\) convolution and persisted 808 member/b rows plus
  nuclear q16/q84 bands.
- Combined the native pion term with the AV18 retained-NN result for all
  \(u,d,\bar u,\bar d\) at \(x_N=0.1,Q=5\) GeV. The plot separates total and
  pion-component panels so the small profile bands remain visible; PNG was
  visually inspected.
- The scenario remains non-production because JAM21 is not a Vpion19 refit
  and no fixed-order Y term exists. A native tensor-pion TMD is not sourced,
  so no transverse pion \(f_{1LL}\) is invented.
- Next executable action: extend NNπ off forward with explicit pion/nucleon
  transfer sharing, virtuality, and helicity correlations; separately seek a
  sourced tensor-pion transverse input.

# 2026-07-26: off-forward NNπ source boundary audit

- Audited and archived arXiv:2601.13567, the new LF Hamiltonian EFT study of
  nucleon/deuteron multi-pion Fock sectors.
- Its deuteron result is a scalar Wilson--Bloch effective two-body
  Hamiltonian with the NNπ sector integrated out. The authors explicitly
  state that dynamical pions are not yet fully integrated and the full
  four-body solution remains in progress.
- It does not provide helicity, tensor polarization, virtuality-resolved
  three-body amplitudes, off-forward overlaps, or machine-readable data.
  Therefore it cannot responsibly close the spin-resolved NNπ GTMD gate.
- Added an exact replacement-amplitude contract and validation requirements
  in `references/lfheft_nnpi_source_audit.md`. The forward implementation
  remains usable and explicitly model dependent; no arbitrary transfer
  Gaussian was introduced.
- Next executable action: continue independent acceptance work while
  monitoring for a released dynamical NNπ amplitude. Prioritize the complete
  current spin-1 TMD basis/implementation audit and remaining non-impulse
  gluon sectors.

# 2026-07-26: explicit spin-1 representation map

- Completed the persistent map from physical target/quark/gluon Hilbert
  spaces to the \(U,L,T,LL,LT,TT\) target basis, transverse \(SO(2)\) ranks,
  epsilon-rotated structures, gauge-link action, Gram projectors, and joint
  positivity matrices.
- Documented the concrete computational benefit of the algebraic
  organization and the structural gluon TT identifiability combination.
- Recorded why topology and PennyLane are not presently indicated: no
  winding/bundle obstruction or quantum-circuit validation advantage has
  been identified. This is an evidence-based exclusion, not omission.
- Next executable action: implement the open gluon T-odd mechanism contract
  and audit available fitted/lattice inputs without introducing a universal
  phase.

# 2026-07-26: color- and process-resolved gluon T-odd boundary

- Added a strict gluon Sivers contract that independently carries the
  antisymmetric f-type and symmetric d-type color functions, staple
  orientation, validity/provenance, and observable-specific hard weights.
- The interface refuses a one-function universal phase, missing process
  coefficients, mixed links treated as signs, out-of-domain evaluation, and
  nonfinite values.
- Audited the review and CGI-GPM phenomenology. Existing constraints are
  preliminary/framework-dependent and do not supply a validated public
  two-color replica ensemble, so no nonzero production default was invented.
- Focused boundary validation initially reached **5 tests** with
  `/Users/dustin/miniforge3/bin/python -m pytest -q tests/test_gluon_todd.py`.
  Failed environment probes: system `python` is absent; system `python3` and
  `.conda-artemide/bin/python` do not contain pytest.
- Added the transverse-target Sivers operator with explicit sigma-x/sigma-y
  nucleon-spin components. It is Hermitian, has the required
  epsilon(S_T,k_T) angular dependence, reverses with the link, vanishes at
  k_T=0, and refuses an invented nonzero-transfer extension.
- Propagated a controlled spin-sensitive fixture through
  `convolve_gluon_gtmd_point`; the spin-1 parent retains the contribution and
  remains Hermitian.
- Final focused suite: **8 tests pass**. Full regression:
  **301 tests pass in 43.85 s** using
  `/Users/dustin/miniforge3/bin/python -m pytest -q`.
- Next executable action: ingest or reconstruct a source-reproducible
  two-color phenomenological boundary only if its normalization and
  uncertainty information can be validated; otherwise continue the open
  production soft/evolution/Y-term work without inventing gluon T-odd input.

# 2026-07-26: enforceable TMD subtraction and rapidity-scale contract

- Replaced metadata-only scheme labels with typed soft-subtraction, rapidity
  regulator, rapidity-prescription, UV-scheme, and source identifiers shared
  by quark/gluon matching and CSS evolution.
- Added explicit \((\mu_i,\zeta_i)\) and \((\mu_f,\zeta_f)\) endpoints. The
  current one-dimensional solver supports only
  \(\zeta_i=\mu_i^2,\zeta_f=Q^2\) and refuses unsupported paths.
- Boundary/evolution composition now fails if the schemes differ. Fit-native
  arTeMiDe paths remain separate and are not relabeled as this in-house
  scheme.
- Focused validation: **29 tests pass** across scheme, quark/gluon matching,
  and evolution.
- Exact command:
  `/Users/dustin/miniforge3/bin/python -m pytest -q tests/test_tmd_scheme.py tests/test_gluon_tmd_matching.py tests/test_tmd_evolution.py tests/test_quark_tmd_matching.py`.
- Remaining accuracy boundary: this enforces conventions but does not turn
  mixed-order matching, one-loop evolution, or unfitted profiles into a
  precision production calculation.
- Full repository regression after integration:
  **305 tests pass in 44.74 s** using
  `/Users/dustin/miniforge3/bin/python -m pytest -q`.
- Next executable action: add explicit order-consistency accounting and a
  numerical cusp/path-consistency test for a general two-scale backend, or
  adopt a validated fit-native backend for the affected T-even sectors.

# 2026-07-26: separate full-matrix non-impulse gluon mechanism ledger

- Added a mechanism-resolved `(3,3,2,2)` gluon correlator ledger with
  independent coherent-shadowing, antishadowing, off-shell, meson-exchange,
  and non-nucleonic slots.
- Added the best-supported current nonzero builder: inclusive diffractive
  gluon shadowing affects only target-U/gluon-trace structure. No quark
  spin-response factors are imported.
- Absent mechanisms are exact configuration zeros with
  `UNCONSTRAINED` provenance, not physical-zero claims. Validity, mechanism
  identity, shape, finiteness, and Hermiticity fail closed.
- Corrected stale continuity/roadmap instructions that still requested the
  already-complete active-nucleon recoil task.
- Added inclusive gluon antishadowing normalized by the explicit gluon
  shadowing momentum loss; no quark momentum density is reused.
- Propagated named diffractive uncertainty responses as full Hermitian
  correlator members in a separate mechanism/member ledger.
- Focused validation: **16 tests pass** using
  `/Users/dustin/miniforge3/bin/python -m pytest -q tests/test_gluon_nuclear_mechanisms.py tests/test_nuclear_mechanisms.py`.
- Full regression: **311 tests pass in 44.38 s** using
  `/Users/dustin/miniforge3/bin/python -m pytest -q`.
- Next executable action: keep polarized/tensor gluon shadowing and gluon
  off-shell responses inactive until sourced; proceed to the machine-readable
  WP8 validation matrix so open versus passing requirements cannot be hidden
  across separate tests and narrative documents.

# 2026-07-26: authoritative WP8 validation matrix

- Added a versioned 12-requirement manifest mapping tolerances, pytest
  selectors, artifacts, provenance, affected outputs, and open reasons.
- Added a report builder that verifies pytest collection/evidence paths,
  executes the full suite once, and cannot call a partial requirement
  complete merely because tests pass.
- Corrected one stale h1LT selector discovered by the first run; this was an
  evidence-map defect, not a missing physics test.
- Final report: **312 tests collected and passed**, seven requirements
  verified, five partial, zero open, zero missing/failed evidence,
  `completion_ready=false`.
- Output:
  `outputs/validation/wp8_acceptance_report.json`.
- Next executable action: address the `global_moments` partial entry by
  building a common per-species/per-flavor/per-mechanism moment ledger and
  refusing any conservation claim when the required x support or mechanism
  input is absent.

# 2026-07-26: support-aware global moment ledger

- Added typed number, momentum, helicity, tensor, and transversity moments
  keyed by species, flavor, and mechanism.
- Sum-rule claims now fail unless the table spans `[0,1]` or the requested
  observable has a sourced endpoint completion. A number-tail correction
  cannot complete a momentum moment.
- Audited the refined AV18 NNπ parent: 60 named number, momentum, helicity,
  tensor, and transversity entries retain proton, neutron, and total
  identities over 37 nodes in
  \(0.001\le x_N\le0.95\). The report explicitly refuses conservation.
- Added current AV18 collinear gluon momentum and tensor moments over its
  narrower eight-point \(0.01\le x_N\le0.7\) support, bringing the ledger to
  62 entries. Gluon helicity and endpoint completion remain open.
- The conservation candidate selects `impulse_total` only and cannot double
  count it with proton/neutron components.
- Focused ledger tests: **4 pass**. Updated WP8 report:
  **316 tests collected and passed**, seven requirements verified, five
  partial, zero missing evidence, `completion_ready=false`.
- Next executable action: provide controlled endpoint models from the
  underlying nucleon PDF/LF convolution rather than extrapolating the table;
  in parallel extend the ledger to axial/tensor/transversity parent
  coefficients.

# 2026-07-26: complete-basis controlled limiting cases

- Added a common retained-spin LF-parent audit covering free-proton,
  free-neutron, pure-S/zero-D, no-Melosh at rest, zero quark corrections, and
  zero gluon corrections.
- Every check covers the complete 18-name spin-1 quark basis or the full
  mechanism matrix, rather than one representative TMD.
- Corrected an initial guard that compared against the spin-half component
  names instead of the public spin-1 18-name basis. Corrected JSON
  serialization of NumPy booleans in the generated artifact.
- Six checks pass with zero maximum residual against \(2\times10^{-11}\).
  Existing all-flavor tests supply exact-isospin and controlled-CSB coverage.
- Artifact: `outputs/validation/controlled_limits.audit.json`.
- Next executable action: regenerate WP8; if verified, proceed to the
  member-level joint-positivity partial requirement.

# 2026-07-26: member-level gluon wave positivity

- Added reusable member-preserving quark/gluon joint-density auditors that
  report tensions without clipping.
- Audited AV18, CD-Bonn, NV-Ia, NV-Ib, NV-IIa, and NV-IIb full gluon
  correlators for proton impulse, neutron impulse, and total at nine
  transverse momenta: 162 matrices.
- All six members pass at \(10^{-10}\); global minimum eigenvalue is
  0.11496746205104823.
- Added explicit refusal to assemble joint densities from incomplete named
  projections or pointwise envelopes whose components come from different
  members.
- Focused tests: **2 pass**. The joint-positivity WP8 item remains partial
  because full member matrices are not available for every fit/mechanism
  ensemble.
- Next executable action: implement the uncertainty-axis separation contract
  so independent wave, fit, evolution, transform, grid, and nuclear axes
  cannot be collapsed into an invented joint covariance.

# 2026-07-26: typed separation of all uncertainty axes

- Added seven explicit axes for wave choice, internal quadrature, external
  grid, transform, PDF/TMD fit, evolution profile, and nuclear mechanism.
- Every ensemble records its kind, stable member IDs, central member, source,
  and correlated dimensions.
- Joint covariance construction now requires a sourced labeled PSD joint
  probability. The current heterogeneous sources correctly trigger refusal.
- Focused tests: **3 pass**. Artifact:
  `outputs/validation/uncertainty_axes.audit.json`.
- This closes the WP8 uncertainty-separation requirement; it does not pretend
  that a joint probability exists.
- Next executable action: regenerate WP8, then continue the remaining
  positivity, global-moment, and process-factorization partial gates.

# 2026-07-26: WP9 parent-figure provenance and visual audit

- Rendered representative pages of the 72-page quark atlas, 18-page gluon
  atlas, and historical reduced-correlator atlas. PyMuPDF was used because
  Poppler is unavailable. The parent curves and pointwise bands are smooth
  and legible; the historical atlas is polished but not parent derived.
- Moved future exploratory plotting to
  `scripts/plot_exploratory_closure_spin1_tmds.py` and made the misleading
  `plot_production_spin1_tmds.py` entry point fail closed. Existing binary
  artifacts were retained non-destructively and marked superseded.
- Added `outputs/figures/figure_index.json` and the generated
  `outputs/validation/parent_tmd_figure_acceptance.json`.
- The acceptance audit verifies all 72 quark and 18 gluon groups, ordered
  six-wave envelopes containing AV18, finite 241-point common PCHIP grids,
  and distinct pre-assembly proton/neutron light-flavor sources.
- In the AV18 \(f_1\) source, maximum absolute \(u-d\) differences are
  1.5747213704 GeV\(^{-2}\), and \(\bar u-\bar d\) differences are
  0.0950120938 GeV\(^{-2}\), for both separately retained impulse sources.
  Inclusive deuteron equality is the configured exact \(I=0\) limit.
- Added and visually checked a 72-page AV18 source-decomposition atlas and
  dense table showing active proton, active neutron, impulse sum, and
  configured model total for every light-flavor spin-1 TMD.
- Focused validation: **9 tests pass** across figure acceptance and adjacent
  WP8 contracts.
- Full regression initially passed **324 tests in 44.90 s**; after adding the
  source-atlas coverage test, the regenerated report passes **325/325**. It
  records nine verified, three partial, zero missing/failed evidence, and
  `completion_ready=false`.
- Next executable action: continue the remaining full-member positivity,
  support-complete moment, and process-factorization gates without relabeling
  unavailable external inputs.

# 2026-07-26: endpoint-aware physical moment combinations

- Added signed linear sum-rule algebra and corrected the number audit to form
  \(q-\bar q\) before fitting the endpoint. Separate sea-number moments are
  no longer incorrectly expected to converge.
- Added local integrable endpoint powers with hard neighborhood/sign gates
  and adjacent-window sensitivity. Non-asymptotic and sign-changing inputs
  fail closed.
- Generated 37-node \(Q=5\) AV18 parents for all CT18 active partons and a
  separate BDSSV24 retained-spin gluon-helicity parent.
- Per-nucleon valence number is 3.0073525 (expected 3, tolerance 0.03).
  All-active momentum is 1.0015660 (expected 1, tolerance 0.002) with
  0.0001759 endpoint sensitivity. Gluon momentum is 0.4488356 and gluon
  helicity is 0.4350220; both are support complete.
- The sign-changing gluon tensor endpoint and non-impulse all-sector moments
  remain explicitly incomplete. Focused validation: **27 tests pass**.
- Full regression and regenerated acceptance report: **328/328 tests pass**;
  nine WP8 requirements are verified, three remain partial, and
  `completion_ready=false`.

# 2026-07-26: reconstructible-ensemble joint positivity completion

- Added simultaneous multi-component density replacement preserving common
  JAMDiFF identity across \(h_1\) and the member-level WW
  \(h_{1L}^{\perp}\) transform.
- All 968 JAMDiFF members pass across six wave functions, four light flavors,
  impulse/model totals, and nine \(k_T\) knots; the minimum eigenvalue is
  0.0007710674.
- Materialized the default diffractive 50% uncertainty as named low/high
  response functions. Generated an AV18 \(x_N=0.01,Q=5\) full gluon parent
  and audited central/low/high shadowing matrices; all 27 pass with minimum
  7.2354734.
- BPV20's existing 500-member full-density audit remains authoritative:
  296 scheme-dependent tensions are reported without clipping or member
  rejection. Six-wave gluon and evolved-quark audits remain passing.
- Promoted WP8 joint positivity to verified for every implemented ensemble
  with reconstructible correlated members. Projection-only envelopes retain
  a hard refusal and are not treated as ensemble members.
- Focused validation: **10 tests pass**.

# 2026-07-26: final off-forward, figure, and project acceptance

- Added a six-wave physical LF off-forward reduction audit using the declared
  replaceable rank-zero nucleon GTMD boundary. GTMD component closure,
  forward TMD reduction, GPD integration, Wigner transform, and Hermiticity
  pass; the largest truncated-grid GPD error is 0.46734%.
- Corrected the gluon tensor local-moment convention to use its required
  \(x^1\) weight. The support-complete value is
  \(3.06955\times10^{-7}\) with \(2.36372\times10^{-8}\) endpoint
  sensitivity.
- Serialized and visibly hatched the gluon W-only validity boundary above
  \(k_T=1\) GeV at \(Q=5\); no universal observable Y term was invented.
- Rendered and machine-audited all 162 authoritative atlas pages. Contact
  sheet review found and fixed autoscaled \(10^{-14}\)-level projector
  roundoff in exact-zero source panels.
- WP8 final report: **12/12 verified**, **334/334 tests pass**,
  `completion_ready=true`.
- Final project report: **10/10 criteria verified**, zero missing evidence,
  zero unresolved required implementation, **334/334 tests pass**,
  `completion_ready=true`.
- Authoritative artifacts:
  `outputs/validation/wp8_acceptance_report.json` and
  `outputs/validation/final_acceptance_report.json`.
- Future actions are optional external-data or perturbative-order upgrades.
  They must preserve the accepted fail-closed boundaries and add new manifest
  evidence if promoted into production scope.
# 2026-07-26: WP10 rich-structure scope opened

- Reclassified the former 334-test, 10/10 report as the accepted baseline for
  the earlier declared boundary, not current project completion.
- Audited the requested sectors: BPV20 quark Sivers is fit-native; JAMDiFF
  transversity and correlated WW \(h_{1L}^{\perp}\) exist; pretzelosity is a
  signed universal scenario; Boer--Mulders has no production input; gluon
  f/d Sivers has a correct typed interface but no numerical boundary;
  inclusive U/trace shadowing exists while polarized/tensor response is
  incomplete; pion/six-quark/cluster contributions do not yet provide a
  complete unintegrated flavor/spin/color parent; extra OAM appears only
  through the current S/D/Melosh impulse composition.
- Added WP10.1--WP10.7 with explicit gates to `handoff/ROADMAP.md` and
  decision D-105.
- Next executable action: implement the common gauge-link/T-odd input
  contract and flavor-resolved Boer--Mulders boundary, then connect it to the
  nucleon and LF-parent paths with sign, provenance, and positivity tests.

# 2026-07-26: WP10 rich correlator implementation checkpoint

- Added operator/flavor-resolved gauge-link phase inputs, BPV20-derived
  flavor-dependent Boer--Mulders, published CGI-GPM gluon f/d Sivers
  scenarios, and exact future/past reversal tests.
- Added independent WW-breaking, pretzelosity-moment, and Yang et al. 2024
  world-SIDIS g1T inputs. The published sea-zero and missing covariance are
  explicit assumptions, not physical-null claims.
- Added full target-basis quark and gluon polarized/tensor shadowing response
  models. Inclusive U/trace remains the only data anchor; other response
  ratios are named model parameters.
- Added spin-resolved Sullivan-pion and effective-cluster TMD correlators.
  The cluster transverse integral numerically reproduces its established
  collinear convolution.
- Added definite-OAM partial waves and real/imaginary interference
  bilinears, plus full-momentum and integrated adapters. Rotation rank,
  wave-disable limits, and staple reversal are tested.
- Generated six-wave rich quark tables, six independent gluon f/d scenario
  tables, a combined T-odd table, and visually audited the six-page
  `rich_spin1_todd_parent_atlas.pdf`. The figure index now makes the rich
  ensemble authoritative and retains the prior real-boundary ensemble as
  historical.
- Remaining WP10 acceptance work: propagate the Yang/WW-breaking,
  pretzelosity, shadowing, cluster, and OAM scenario axes through a single
  production member ledger; add WP10 machine-readable acceptance evidence;
  rerun and record the complete suite after that integration.

# 2026-07-26: WP10 rich-dynamics production and acceptance completion

- Activated the Yang-2024 \(g_{1T}\) central input, independent
  flavor-resolved pretzelosity, BPV20 Sivers, flavor-dependent Boer--Mulders,
  and MSHT20-QED neutron-\(f_1\) CSB in all six rich quark parents. The
  production \(u,d,\bar u,\bar d\) curves are no longer a naive isoscalar
  collapse.
- Exported a separate PDF-anchored S/P-even/P-odd/D OAM parent and a
  five-function comparison atlas. Its real and imaginary bilinears pass
  rotation-rank, wave-disable, Hermiticity, and link-reversal tests.
- Exported the full six-function leading-twist spin-1 gluon T-odd multiplet
  for independent f- and d-type color structures, three CGI-GPM scenarios,
  both staple directions, and full \((3,3,2,2)\) correlators. Visually
  audited all six atlas pages.
- Exported spin-resolved Sullivan-pion and effective-cluster correlators,
  each over the complete 18-name quark basis with unsupported operator
  structures represented as exact labeled boundaries. The pion Hankel
  transform converges to \(1.77\times10^{-8}\) relative to its peak.
- Exported named quark and gluon polarized/tensor shadowing scenarios at
  \(x_N=0.01\). Quark high-rank inverse projections are production-limited
  to the resolved \(k_T\le1.2\) GeV domain so Gaussian-tail roundoff cannot
  masquerade as physical structure.
- Consolidated central/wave, fit/model T-odd, Boer--Mulders coefficient,
  complete gluon-color, shadowing, pion/cluster, and OAM members into
  `outputs/parent_tmds/wp10_production_member_ledger.csv`: **82,465 rows**.
  Every row retains evidence class, uncertainty axis, combination policy,
  source artifact, stable member ID, amplitude identity, validity,
  flavor/species, mechanism, link, and color where applicable. Alternative
  axes are explicitly not a joint probability.
- Updated the figure index and visually inspected the OAM, pion, cluster,
  quark/gluon shadowing, complete-gluon-T-odd, and representative rich
  quark source/total pages.
- Machine acceptance:
  `outputs/validation/wp10_acceptance_report.json` records **7/7 verified**
  criteria, zero missing evidence, **383/383 tests passing**, and
  `completion_ready=true`. WP8 was regenerated at the same 383-test state.
- No required WP10 implementation remains. Declared limitations are
  replacement upgrades for unavailable covariance/data, not silently
  simplified physics; they are enumerated in `validation/wp10_manifest.json`.

# 2026-07-26: two-stage quark g1LT and g1TT activation

- Traced both missing functions to the axial `gamma+gamma5` projection:
  the existing BPV20 Sivers and modeled Boer--Mulders phases act on different
  quark operators and cannot generate them.
- Added independent low/central/high \(u,d,\bar u,\bar d\) phase scenarios
  for \(g_{1LT}\) and \(g_{1TT}\). Each proposed pair is composed into the
  full \(6\times6\) target–quark density and receives one common positivity
  scale only when required; eigenvalues are never clipped.
- Added a screened one-gluon transverse convolution with rank-one and
  rank-two angular harmonics. The model uses AV18
  \(P_D=0.0575985407\) and normalized signed S--D overlap
  \(C_{SD}=0.3897991321\), together with explicit S--P, S--D, and
  P-even--P-odd interference terms.
- Future/past reversal, mixed-link refusal, phase-zero, pure-S, rotation,
  Hermiticity, positivity, and quadrature convergence are tested. The
  48x56 and 72x88 quadratures agree to
  \(1.20\times10^{-14}\) maximum relative residual on the audit grid.
- Exported 51,840 complete TMD projections and 103,680 retained-helicity
  correlator entries across both stages, three scenarios, four flavors, two
  links, and 60 smooth nonzero momentum knots. Minimum full-density
  eigenvalue is 0.0457654.
- The direct phase central reaches order \(10^{-1}\) GeV\(^{-2}\), while
  screened rescattering gives roughly \(10^{-4}\) for \(g_{1LT}\) and
  \(10^{-5}\) GeV\(^{-2}\) for \(g_{1TT}\). The hierarchy is shown rather
  than normalized away in the five-page
  `output/pdf/quark_g1lt_g1tt_two_stage_atlas.pdf`.
- Added these 51,840 rows to the unified WP10 ledger, now **134,305 rows**,
  retaining stage and amplitude identities.
- Final synchronized regression and acceptance: **393/393 tests pass**;
  WP8 is 12/12 verified, WP10 is 7/7 verified, and final project acceptance
  is 11/11 verified with `completion_ready=true` in all three reports.

# 2026-07-26: source-informed six-function gluon T-odd prediction

- Audited arXiv:2402.17556 source: full \(g_1+g_2\) spectator calculation,
  f/d color factors and link classes, function hierarchy, and the
  \(h_{1L}^{\perp g}\) node near \(k_T^2=0.1\) GeV2 at x=0.1. The 100 fit
  replicas are not deposited.
- Added a new source-informed boundary while retaining the old rank-scaled
  multiplet as comparison. Spin-1 \(g_{1LT}\), \(g_{1TT}\) use AV18
  \(P_D=0.0575985407\), signed S--D coherence 0.3897991321, and screened
  rank-one/rank-two adjoint-eikonal moments.
- Corrected link domains to f-type `[+,+]/[-,-]` and d-type
  `[+,-]/[-,+]`, with exact reversal and independent d-type coupling.
- Shape-preserving interpolation of the validated AV18 parent gives 61
  knots over 0.05--0.95625 GeV. The full 6x6 density is positivity-capped.
  Exports contain 4,392 TMD rows and 26,352 matrix rows.
- Generated and visually audited the two-page dimensional-F atlas. Its band
  is a low/central/high model envelope, not a fabricated replica interval.
- Added the 4,392 predictions to the WP10 ledger, now 138,697 rows. The
  complete suite passes 399/399; WP8 is 12/12, WP10 is 7/7, and final
  acceptance is 11/11 with all completion flags true.
- Reproduce with
  `PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/export_spectator_informed_gluon_todd.py`
  and `scripts/build_gluon_todd_two_stage_atlas.py` using the documented
  Matplotlib cache.

# 2026-07-26: overall quark/gluon consistency audit

- Inventoried 116,164 quark and 22,533 gluon WP10 ledger rows by TMD,
  mechanism, evidence class, uncertainty axis, and combination policy.
- Verified the strong foundations: complete operator bases, retained
  proton/neutron and flavor identity in the main impulse parent, realistic
  S/D convolution, exact link reversal, color separation, and full-matrix
  Hermiticity/positivity.
- Found that the ledger is a collection of alternatives rather than a
  canonical composition graph. Evolution and soft-subtraction treatment are
  heterogeneous across fitted and modeled inputs.
- Reclassified the latest gluon T-odd table as a sensitivity study: it
  attaches source-informed radial coefficients directly to deuteron \(f_1\)
  and does not implement the source paper's complete master-integral and
  spectral-mass calculation.
- Quantified central maxima relative to local gluon \(f_1\):
  0.308 (`h1`), 0.219 (`f1Tperp`), 0.053 (`h1Lperp`), 0.025
  (`h1Tperp`), 0.0099 (`g1LT`), and 0.0024 (`g1TT`). None triggered the
  positivity cap; this is a constraint result, not normalization evidence.
- Recorded seven concrete integration work packages in
  `references/overall_quark_gluon_consistency_audit.md`.

# 2026-07-26: governing objective clarified

- The user established that the fully self-consistent canonical
  quark--gluon synthesis is the project objective, not an optional later
  upgrade.
- Updated the persistent maintainer contract, project context, roadmap, and
  decision log. Component-level WP8/WP10 acceptance remains useful evidence
  but cannot close the project while WP11 is open.
- The controlling rule is now explicit: include every realistically
  supported physical contribution, neither omitting difficult sectors nor
  enhancing weak ones for presentation.

# 2026-07-26: WP11 C2--C4 canonical parent integration

- Obtained the official PVGlue20 arXiv source and recorded its equations,
  parameter replica, checksum, and reproducible provenance in
  `references/pvglue20_benchmark.md`; it is benchmark-only.
- Implemented the project's own spin-half gluon LF/Wilson-line parent and
  the spin-one LT/TT nuclear Wilson-line phase. Generated 15,624 TMD rows
  and 4,464 complete parent-matrix rows at \(x_N=0.1,Q=5\) GeV.
- The new \(g_{1LT}\) and \(g_{1TT}\) are nonzero but naturally small:
  maximum rank-weighted ratios to \(f_1\) are \(5.40\,10^{-5}\) and
  \(2.34\,10^{-5}\). The largest six-function T-odd ratio is 0.0168.
- Exact staple reversal holds to numerical precision; the maximum AV18
  wave-sector closure residual is \(1.86\,10^{-12}\) GeV\(^{-2}\), the
  maximum forbidden-basis residual is 0.007625, and all exported 6x6 parent
  densities are Hermitian and positive (minimum eigenvalue 0.7203).
- Replaced the frozen/WW production \(g_{1T}\) boundary with Yang-2024 in the
  rank-aware Q=5 grid. Direct/grid validation passes all 576 samples under
  the declared mixed tolerance.
- Regenerated the six-wave-function spin-1 parent table: 19,440 rows with
  maximum proton+neutron reconstruction residual
  \(6.03\,10^{-14}\) GeV\(^{-2}\).
- Targeted canonical graph, scheme, gluon analytic/production, quark
  evolution, and worm-gear tests pass. Current commands:
  `PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/generate_evolved_quark_grid.py`,
  `scripts/validate_evolved_quark_grid.py`, and
  `scripts/export_evolved_quark_parent_scenarios.py`.
- Next executable action: WP11 C5 must integrate the fitted Sivers,
  Boer--Mulders, Yang worm gear, WW \(h_{1L}^{\perp}\), and pretzelosity
  members into one evolved flavor-resolved nucleon parent rather than
  leaving the rich-fit and evolved tables as separate alternatives.

# 2026-07-26: WP11 canonical synthesis and governing acceptance complete

- Integrated the evolved, flavor-resolved \(u,d,\bar u,\bar d\) nucleon
  boundary with Sivers, Boer--Mulders, Yang \(g_{1T}\), transversity,
  \(h_{1L}^{\perp}\), pretzelosity, and retained-helicity quark LT/TT phases
  before spin-1 projection. Positivity is enforced on the complete nucleon
  density rather than function by function.
- Added Fock-consistent Miller/JAM21/Vpion19 quark and gluon pion
  correlators with the explicit NNpi momentum counterterm. Propagated
  supported off-shell, shadowing, antishadowing, and meson mechanisms while
  retaining zero-centered unsupported cluster inputs as named sensitivities.
- Production exports are
  `outputs/parent_tmds/quark_av18_rich_medium.csv` (16,848 rows) and
  `outputs/parent_tmds/gluon_av18_canonical_lfwf_todd.csv` (29,016 rows),
  with retained matrix ledgers, metadata, and validation reports.
- Produced smooth dimensional-\(F\) canonical band tables and two 18-page
  PDF atlases for all declared quark and gluon leading-twist spin-1 TMDs.
  The bands are conservative named-axis theory envelopes, not statistical
  confidence intervals. Representative rendered pages were visually
  inspected.
- Added the process/observable manifest: SIDIS/DY link reversal, independent
  gluon f/d hard-color inputs, HERMES \(b_1\), number/momentum reduction,
  positivity, Hermiticity, basis reconstruction, and mechanism closure.
- The governing audit `outputs/validation/wp11_final_acceptance.json` passes
  C1--C7. Exact full-suite command:
  `PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl /Users/dustin/miniforge3/bin/python3.9 -m pytest -q`;
  result: 433 passed in 60.50 s.
- Rebuild figures with
  `PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl /Users/dustin/miniforge3/bin/python3.9 scripts/build_canonical_tmd_atlas.py`;
  rebuild acceptance with
  `PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_wp11_final_audit.py`.
- No required WP11 task remains at the declared leading-twist forward scope.
  Remaining items are explicit replacement axes or process/global-fit work,
  not hidden missing central contributions.

# 2026-07-26: WP12 complete-parent enrichment started

- Added WP12 to the persistent roadmap; items 1--5 are required across every
  quark, antiquark, and gluon TMD before external-constraint item 6.
- Implemented an exponentiated five-channel spin-1 Wilson operator with
  exact future/past inverse relation and density-spectrum preservation.
- Added a normalized shared scalar/axial/quark-gluon Fock ledger covering
  \(L_z=0,\pm1,\pm2\). Its common bilinears generate rank-0, rank-1,
  rank-2, T-even, and T-odd spin-half correlator structures coherently.
- Added a four-sector NNpi/DeltaDelta/hidden-color/SRC probability and
  momentum ledger plus explicit central-versus-sensitivity parent policy.
- Added target-spin and full 6x6 target--quark-spin Kraus response maps.
  Complete positivity, Hermiticity, scalar-limit behavior, and projection
  round-trip are tested.
- Exposed the production quark Wilson phase as separate S-P, S-D, and P-P
  channels without changing its canonical central result.
- Focused enrichment/Wilson tests pass 14/14. Authoritative incomplete gates
  and exact replacement tasks are in `validation/wp12_manifest.json`.
- Next executable action: connect these objects to both production exporters,
  add the gluon Fock/joint-spin analogues, and generate the common
  multi-kinematic all-TMD ledger.

# 2026-07-26: WP12 items 1--5 completed and audited

- Directly recomputed all 18 quark and all 18 gluon leading-twist spin-1
  TMDs at \(x_N=0.02,0.05,0.10,0.20,0.40\), \(Q=5\) GeV. Quarks retain
  \(u,d,\bar u,\bar d\); gluons retain independent f- and d-type color/link
  structures. The high-\(x\) quark parent now uses a single common
  polarized-block scale when complete-parent PSD completion is required.
- Exported soft/central/strong quark S-P/S-D/P-P and gluon S-D/D-D Wilson
  channels across the same x grid, then propagated replacement unitaries
  through all named TMD projections.
- Calibrated the shared scalar/axial/quark-gluon \(L_z=0,\pm1,\pm2\)
  amplitude ledger independently at every x node. Maximum calibration
  residual is \(5.73\times10^{-14}\); generated gluon parents remain
  positive.
- Exported complete zero-centered NNpi, DeltaDelta, hidden-color six-quark,
  and SRC transverse sensitivity parents with explicit sector beta shapes,
  Fock weights, all flavors/species, both staples, and all 18 projections.
  The generic NNpi member remains exclusive with the sourced
  Miller/JAM21/Vpion19 contribution.
- Exported weak/central/strong ordered CP nuclear-response chains for
  shadowing, antishadowing, off-shell, mesonic, and SRC mechanisms.
  Minimum mapped-parent eigenvalue is \(3.94\times10^{-4}\); the maximum
  telescoping residual is \(1.39\times10^{-17}\).
- `outputs/validation/wp12_items1_5_acceptance.json` passes all five gates.
  Item 6 (complete rank-aware multi-Q evolution/external-constraint phase)
  has not been started, matching the requested review checkpoint.
- Full repository regression:
  `PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl /Users/dustin/miniforge3/bin/python3.9 -m pytest -q`
  passed **459 tests in 62.55 s**.
- Reproduce with the `export_wp12_*`, `build_wp12_*_multix_ledger.py`, and
  `build_wp12_items1_5_audit.py` scripts under `PYTHONPATH=src`.

# 2026-07-27: WP12 scientific inspection passed; item 6 ready

- Inspected every composed quark and gluon TMD across five x nodes for
  completeness, exact-zero sectors, flavor identity, rank-weighted
  magnitude, positivity, staple reversal, sampled-k continuity, response
  size, and Wilson identity closure.
- Found and fixed low-k rank-four amplification in the gluon central Wilson
  replacement: the exact central identity now bypasses numerical
  inverse/reapply roundoff.
- Regenerated all five gluon production slices with every mechanism retained
  as a complete matrix block. This made nuclear replacement auditable rather
  than inferential.
- Built one no-double-counted evolution boundary. Ordered CP maps replace
  legacy shadowing, antishadowing, and off-shell blocks; sourced NNpi is
  included once; unsupported generic mesonic/SRC/cluster central terms stay
  off. No final positivity contraction was required.
- The inspection passes all ten scientific gates. Maximum rank-weighted
  ratios are bounded by one; CP recomposition shifts are at most 2.73%
  (quark) and 2.91% (gluon) of local f1; quark/gluon minimum eigenvalues are
  \(4.13\times10^{-4}\) and \(2.09\times10^{-2}\).
- Governing evidence:
  `outputs/validation/wp12_scientific_inspection.json` and
  `references/wp12_scientific_inspection.md`. Item 6 should start from the
  two `wp12_canonical_composed_*` tables only.
- Full regression after inspection:
  `PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl /Users/dustin/miniforge3/bin/python3.9 -m pytest -q`
  passed **463 tests in 64.99 s**.

# 2026-07-27: pre-item-6 visual inspection package

- Generated complete 18-panel dimensional-\(F\) overviews for the inspected
  quark/antiquark and gluon boundaries at \(x_N=0.1,Q=5\) GeV, plus
  rank-weighted physical-ratio overviews and one-page-per-TMD PDF atlases.
- Central curves come only from the `wp12_canonical_composed_*` parents.
  Bands retain the named wave/nuclear/model axes and add the full
  legacy-to-CP-composed displacement. They are conservative theory
  envelopes, not statistical confidence intervals.
- Removed zero-crossing artifacts from the inherited relative wave bands by
  reconstructing absolute wave-function halfwidths directly from the
  six-wave-function ensemble and smoothing only the non-negative uncertainty
  halfwidth. Central curves are never smoothed or altered.
- Outputs and numerical band tables are under
  `output/figures/wp12_inspection/`; tests verify complete bases, flavors,
  color structures, band ordering, and nontrivial rendered artifacts.

# 2026-07-27: resolved constituent model replaces total-only boundary

- Corrected the item-6 contract: the deuteron total is a derived observable,
  not a sufficient representation of the model state.
- Added resolved quark and gluon parent ledgers containing
  proton-in-deuteron, neutron-in-deuteron, nucleon-sum,
  proton-minus-neutron, nuclear-correction, and canonical-total components,
  for every declared TMD and the full correlator matrices.
- Exact reconstruction was verified: maximum quark closure residual is zero
  and maximum gluon residual is \(1.73\times10^{-18}\).
- Added constituent-level valence, antiquark, and focused Sivers plots.
  The proton Sivers input explicitly has \(u<0<d\), with the neutron related
  by the controlled charge-symmetry map; this information is no longer
  hidden by the deuteron sum.
- Item 6 must evolve the resolved ledgers and test closure after evolution.
  It may not replace them with an isoscalar or flavor-averaged projection.
- Reproduce with
  `PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl /Users/dustin/miniforge3/bin/python3.9 scripts/build_wp12_resolved_nuclear_parent.py`
  and
  `PYTHONPATH=src MPLCONFIGDIR=/private/tmp/deuteron-mpl /Users/dustin/miniforge3/bin/python3.9 scripts/build_wp12_constituent_plots.py`.
- Full repository regression after the boundary correction passed:
  **470 tests in 64.22 s**.

# 2026-07-27: production-smooth resolved TMD curves and uncertainties

- Replaced the nine-knot diagnostic line segments in the resolved
  constituent figures by shape-preserving PCHIP functions evaluated at 241
  \(k_T\) points from 0 to 1.5 GeV. Calculated knots and central values are
  unchanged.
- Added a machine-readable dense table,
  `output/figures/wp12_inspection/wp12_quark_constituent_smooth_bands.csv`,
  containing central, lower, upper, and halfwidth columns.
- For Sivers, transversity, and \(h_{1L}^{\perp}\), propagated the available
  direct external-fit replica 16--84% bands together with the wave-function
  envelope. Other TMDs use the absolute six-wave-function/model envelope
  apportioned onto the resolved proton/neutron amplitudes. Nuclear
  uncertainty remains in the explicit nuclear-correction component and is
  not falsely assigned to either constituent.
- Removed inherited relative-band zero-crossing spikes by constructing and
  smoothing only non-negative absolute halfwidths. Central functions are
  never smoothed beyond the declared shape-preserving interpolation.
- Full repository regression passed: **471 tests in 64.32 s**.

# 2026-07-27: corrected observable/diagnostic presentation

- Audited the apparent constituent flavor duplication numerically. At
  \(x_N=0.1,\ k_T=0.1875\) GeV the bound-proton impulse has
  \(f_1^u=3.276,\ f_1^d=2.024\), while the bound neutron has
  \(f_1^u=2.031,\ f_1^d=3.261\). The nucleons and flavors were not equal:
  charge symmetry makes proton \(u\) overlap neutron \(d\), and proton \(d\)
  overlap neutron \(u\), which the four-curve overlay obscured.
- Restored the spin-1 deuteron canonical-total atlas as the primary result
  and relabeled all proton/neutron figures explicitly as constituent audits,
  not deuteron observables.
- No artificial \(u-d\) splitting is introduced into the deuteron. In the
  exact charge-symmetry limit, \(u_D=u_p+u_n=u_p+d_p=d_D\); departures must
  come only from sourced CSB or flavor-dependent nuclear mechanisms already
  represented in the model.

# 2026-07-27: evidence parity restored as a pre-evolution requirement

- Superseded the “item 6 ready” status. Existing WP12 audits certify basis,
  correlator, smoothness, positivity, and composition structure; they do not
  establish \(f_1\)-level phenomenological completeness for every TMD.
- Added WP12-E as the execution gate requiring explicit proton/neutron and
  CSB treatment, source replicas/covariance or honest sensitivities,
  shared-parent consistency, complete channel-appropriate nuclear dressing,
  and physical validation for every quark, antiquark, and gluon TMD.
- Next executable action: generate the machine-readable per-TMD evidence
  matrix, classify every missing cell, and execute replacement work package
  by work package before rank-aware evolution.
- Generated `outputs/validation/wp12_evidence_parity_matrix.json` with one
  row per 18 quark and 18 gluon TMDs. The initial audit correctly remains
  open: the closest sectors are \(f_1\), Sivers, transversity, and
  \(h_{1L}^{\perp}\), while tensor-polarized and most gluon rows have four
  missing evidence cells. The matrix recognizes the existing full
  600-replica BDSSV24 gluon-helicity response rather than marking it absent.
- Propagated all 600 BDSSV24-NLO quark-helicity replicas through the AV18
  proton/neutron LF impulse and off-shell response at
  \(x_N=0.02,0.05,0.10,0.20,0.40\). Replica
  deviations are anchored to the stored evolved production central so the
  public covariance is retained without replacing the common evolution
  scheme. Other nuclear mechanisms remain fixed central and are explicitly
  labeled as such. Output:
  `outputs/parent_tmds/ensemble/bdssv24_quark_g1_bands_x010.csv`.
- Added a zero-centered, replaceable CSB power-counting envelope for every
  canonical quark and gluon TMD. It uses conservative 5% quark and 2% gluon
  amplitude bounds, including a rank-aware \(f_1\) floor at a central zero,
  and never shifts the central prediction. This is explicitly a model
  sensitivity, not a confidence interval; \(f_1\) retains its separate
  sourced MSHT20-QED Hessian treatment. The 14,760-row export cites lattice,
  QCD+QED, and meson-cloud collinear CSV constraints and supplies a strict
  replacement rule for future TMD-specific calculations.
- Regenerated the fail-open WP12-E matrix after these upgrades: 7 of 36 rows
  now pass (`g1`, `h1`, `h1Lperp`, `h1Tperp`, `h1perp`, quark Sivers, and
  gluon `g1`); 29 remain open. Full repository regression passes
  **475 tests in 65.15 s**.
- Propagated the complete CT18NNLO 29-pair Hessian response for quark
  \(f_1\) through resolved proton/neutron impulse and off-shell terms over
  all five production \(x_N\) nodes. Eigenvector deviations are anchored to
  the stored evolved central, preserving the common evolution scheme; the
  sizable direct member-0 Gaussian/evolved-grid mismatch is retained in each
  validation report rather than hidden.
- Extracted the asymmetric 68% intervals of all four implemented Yang-2024
  \(g_{1T}\) parameters from Table IV and exported a 16-corner correlated
  sensitivity hull for proton/neutron and all four light flavors. It is
  explicitly not labeled as the unavailable 1000-replica covariance. The
  published sea-zero boundary is covered separately by the existing
  flavor-resolved shared-Fock/OAM parent sensitivity.
- Closed the tensor-quark evidence linkage for all ten LL/LT/TT
  projections. Their central predictions are projections of the common
  AV18 S--D/OAM/Wilson parent, not independent functions; uncertainty uses
  the six-wave-function ensemble plus named model/response members; nuclear
  dressing uses the operator-valued response correlators; validation uses
  pure-S/S--D limits, positivity/projection closure, and the existing
  \(b_1\) benchmark where applicable.
- Closed the evidence linkage for the 16 non-\(f_1,g_1\) gluon rows. Their
  central members come from the shared gluon LF overlap/OAM/Wilson parent
  with explicit f/d link sectors; uncertainty uses six wave functions,
  Wilson/Fock/nuclear-response scenarios and the complete model bands;
  validation covers link reversal, f/d independence, Hermiticity,
  positivity, forbidden-subspace projection, rank limits, and parent
  closure. These remain model predictions, not fitted gluon TMDs.
- Propagated all 29 CT18 gluon Hessian pairs through exact AV18 LF smearing
  on five \(x_N\) nodes and 61 \(k_T\) points. This supplies the collinear-PDF
  response axis for gluon \(f_1\); deviations are anchored to the canonical
  BSV19/NNPDF31 matched-CSS central, while matching, evolution, transverse
  profile, wave, and nuclear axes remain separately named.
- Regenerated the quark/gluon production band tables and atlases with
  explicit PDF and CSB halfwidth columns. Added and passed the final WP12-E
  audit: all 36 evidence rows and all six acceptance gates pass. The
  remaining declared limitation is complete rank-aware multi-Q evolution,
  which is now the next authorized item.
- Full repository regression after WP12-E closure passes:
  **480 tests in 63.42 s**.

# 2026-07-27: authoritative model-construction note

- Reconciled the original 29-page `Deuteron_GTMD.pdf` formal proposal with
  the implemented correlator chain, decisions D-109--D-121, WP11/WP12
  acceptance reports, evidence matrix, and resolved parent.
- Added `references/model_construction_note.md`, a detailed persistent note
  covering the refocusing history, 18 quark and 18 gluon projections,
  flavor/proton/neutron resolution, gauge links, OAM, six deuteron wave
  functions, nuclear and non-nucleonic mechanisms, evidence classes,
  uncertainty semantics, validation, reproducible artifacts, and the exact
  boundary between completed pre-evolution physics and remaining evolution.
- Added `scripts/build_model_construction_note.py` and generated
  `output/pdf/model_construction_note.pdf`. ReportLab is now declared in the
  `analysis` optional dependency; PyMuPDF is used for page rendering and
  visual QA.
- Exact build command:
  `/Users/dustin/miniforge3/bin/python3.9 scripts/build_model_construction_note.py`.
- Rendered all 15 PDF pages with PyMuPDF and visually inspected the complete
  montage; no clipping, overlap, orphaned headings, or unreadable tables were
  found. The structural extraction audit also passes.
- Full repository regression after the documentation integration passes:
  **480 tests in 64.38 s**.
- Next executable action remains item 6: rank-aware evolution of the resolved
  quark/gluon parents while preserving constituent, flavor, spin, color/link,
  mechanism, and uncertainty labels.

## Technical-manuscript replacement

- The first 15-page ReportLab note was rejected as too elementary. It is now
  explicitly superseded and its renderer writes only
  `model_construction_note_legacy_summary.pdf`.
- Replaced it with `references/model_construction_note.tex`, a standalone
  scientific LaTeX manuscript modeled on the structure of
  `Deuteron_GTMD.pdf`. It contains working operator, representation,
  convolution, gauge-link, OAM/eikonal, nuclear-response, tensor-normalization,
  uncertainty, positivity, matching, and evolution equations; complete basis
  and evidence tables; citations; implementation mapping; validation values;
  and a completion/open-physics audit.
- Added reproducible Tectonic 0.17 environment
  `environment-latex.yml`; the project-local installation is `.conda-latex`.
- The compiled `output/pdf/model_construction_note.pdf` is 21 pages.
  Tectonic reports no errors, undefined references, or overfull boxes; the
  remaining underfull bibliography line is harmless.
- Rendered and visually inspected all 21 final pages with PyMuPDF. Tables,
  equations, citations, headers, footers, and section transitions have no
  clipping or overlap. PDF text extraction contains no unresolved citation
  markers.
- Full repository regression after the LaTeX replacement passes:
  **480 tests in 63.71 s**.

# 2026-07-27: Alex Gnech Norfolk-current reply

- Ingested and visually inspected `comparison.pdf` and
  `Notes_lectures_miami.pdf`; recorded their checksums and the user-supplied
  email in `references/gnech_norfolk_current_reply.md`.
- Downloaded the primary PRC106 source, arXiv:2207.05528, and transcribed
  reference set A from Table II and the deuteron decomposition from Table IV.
- Alex confirmed the long-range prescription
  \(I_k(r)\rightarrow C_{R_L}(r)I_k(r)\), ruling out differentiated-regulator
  alternatives.
- Implemented the PRC106-A \(d_1^S,d_2^S\) inputs and Table-IV targets.
  The calculated \(d_1^S\) contact contribution agrees within the quoted
  uncertainty for all four Norfolk models.
- Added the requested unit-constant and separated OPE diagnostics. The
  \(d_2^S\) OPE result still misses Table IV for all models; the mismatch is
  isolated to the relative \(I_1/I_2\) (sigma and sigma-dot-r) contraction.
- Added a concise reply-ready comparison at
  `handoff/correspondence/norfolk_current_followup_draft.md`.
- Output:
  `outputs/stage0/norfolk_prc106_set_a_isoscalar_benchmark.csv`.
- Focused validation: 6 Norfolk-current tests pass.
- Full repository regression after integrating the reply passes:
  **482 tests in 64.99 s**.

# 2026-07-27: genuinely predictive next-level model requirements

- Added the dedicated eight-page Section 15, “Requirements for a genuinely
  predictive next-level model,” to
  `references/model_construction_note.tex`.
- The section distinguishes the present constrained phenomenological
  synthesis from a generative microscopic model and specifies the required
  light-front Hamiltonian, regulated Fock space, common GTMD overlaps,
  dynamical Wilson lines, microscopic spin-1 Fock state, consistent currents,
  QCD matching/evolution, shared-parameter calibration, correlated
  uncertainty, validation ladder, software architecture, and falsifiability
  standard.
- Added twelve explicit completion criteria and a comparison table that
  prevents complete evolution of the current boundary from being mislabeled
  as a fundamental prediction.
- Recorded the transition as WP13 in `handoff/ROADMAP.md` and as governing
  decision D-124; updated the persistent handoff index so it survives context resets and
  developer handoffs.
- Recompiled `output/pdf/model_construction_note.pdf` with Tectonic. The
  manuscript is now 28 pages. Tectonic reports no errors, undefined
  references, or overfull boxes; one harmless underfull paragraph remains.
- Rendered all 28 pages with PyMuPDF and inspected two complete montages.
  Equations, tables, headers, footers, and section boundaries show no
  clipping, overlap, or unreadable content.
- Full repository regression after the note and persistent-governance update
  passes: **482 tests in 64.09 s**.

# 2026-07-27: algebraic and geometric WP13 research note

- Added the standalone 18-page LaTeX note
  `references/algebraic_geometric_next_level_model_note.tex` and compiled
  `output/pdf/algebraic_geometric_next_level_model_note.pdf`.
- The proposal is a gauge-covariant graded light-front tensor architecture:
  regulated Fock-graded Hilbert spaces; color/flavor/spin/OAM intertwiners;
  a symmetry-preserving tensor-network realization; Wilson links as bundle
  parallel transport represented on a path groupoid; common GTMD morphisms
  and commuting reductions; symplectic transverse phase space; convex
  positive-correlator geometry; controlled nuclear amplitude maps; filtered
  regulator/Fock convergence; and a limited chain-complex provenance and
  no-double-counting audit.
- The note explicitly states that topology does not supply QCD dynamics and
  that non-flat QCD Wilson connections make holonomies path-geometric rather
  than generic homotopy invariants. It also records risks, nonclaims,
  property-based tests, a staged implementation program, and adoption
  questions.
- Tectonic compilation passes without undefined references or overfull
  boxes. All 18 pages were rendered with PyMuPDF and visually inspected;
  no clipping, overlap, broken equations, or unreadable tables were found.

# 2026-08-19: C157 fixed-regulator common-IR/remainder gate boundary

- Added `src/deuteron_wigner/bridge/hqcdmatchir2/` as the narrow continuation
  of C156/HQCDMATCHGRID2. It validates an explicit numerical-evidence schema,
  preserves C156/C155/C153 ancestry, and exposes common-IR, perturbative-
  remainder, combined-gate, candidate-domain, and window APIs.
- C153 supplies symbolic common-IR cancellation and perturbative-order
  records only. No authenticated numerical evaluator or source-backed sample
  was available, so every C157 numerical residual is `None`, every gate is
  rejected, and all scale domains/windows are empty. No arbitrary bracket,
  physical scale, running, inverse matching, Q0, PennyLane, state, or TMD
  object was created.
- Added the C157 runtime root
  `c96d976301317fc07c122c767aa34c28bca2b6c83d41d8ad4c177a3e0537e907` and
  machine-readable contracts/validation records plus the implementation report
  `docs/next_level/c157_implementation_report.md`.
- Focused C156/C157 validation passed: **7 tests**. The full `tests/test_c15*.py`
  bridge regression passed: **47 tests**. Full-suite collection passed at
  **7,127 tests**; broad execution terminated with exit code 2 after the
  initial tests without a traceback, so it is not claimed as a clean full
  regression.
- Exact next package: `C158/HQCDMATCHWINDOW2`, restricted to consuming
  authenticated C157 numeric evidence without physical scale selection or
  resolution averaging.
# 2026-08-20: C161 source-qualified target/evaluator boundary

- Added `src/deuteron_wigner/bridge/hqcdmatchir4/` as the exact continuation
  of C160/HQCDFBTEST. It verifies the C160, C158, and C153 public roots and
  inventories all 25 finite-basis quantity/target-scheme combinations.
- Added an immutable target-evaluator admission schema requiring source and
  evaluator hashes, a safe data-only program root, explicit kinematics and
  active-–N_f records, and independent holdout samples.
- C153's six primary sources remain explicitly non-numeric. Consequently
  target coefficients, common-IR differences, perturbative remainders, and
  scale brackets are returned as structured blocked records; no numerical
  value or interval is fabricated.
- Added C161 runtime and machine-readable contracts, claim boundary, and
  `tests/test_c161_hqcdmatchir4.py`.
- Validation: focused C161 suite **3 passed**; the pre-existing authority
  baseline `tests/test_c156_hqcdmatchgrid2.py`,
  `tests/test_c157_hqcdmatchir2_authoritative.py`, and
  `tests/test_c15_manifests.py` **10 passed**. Pytest emitted only its known
  cache-permission warning for the parent workspace.
- Exact next package: **C162/HQCDMATCHIR5**.

# 2026-08-23: Q0–Q2 conditional quantum backend accepted and frozen

- Read the Q0 closure audit, Q1 implementation/acceptance record, Q2
  implementation/acceptance record, and the dedicated PennyLane worktrees.
  Confirmed the accepted branches and commits: Q0 `q0/plhqcd0` at
  `58596e628ea7cb999d58e0e2dd0f83b81f060d41`, Q1 `q1/plhqcdstate` at
  `e7b6aef3ea4fb8d8a3dd850754cd994873258e1f`, and Q2 `q2/plhqcdobs` at
  `69bc52d70c66db7d86b329898f9786ce43121895`.
- Froze the positive acceptance roots: Q0
  `2848cb692ce20cf21f654107acbcf9ed1a803cdd1c968f576c8271ae27df3b9c`, Q1
  `604c2797f4b12a5409a63643635c093c1653cf3b02ccccb04f7f22e2f0645547`, and
  Q2 `23ee186d0fb292b159a9acbfb9f52468f6d65b9fc13103014637034ae43394c1`.
- Recorded the shared encoding, basis order, padded dimensions, device,
  dtype, shot semantics, public-API dependency boundary, and the exact
  nonclaims in `handoff/quantum_backend_q0_q2_freeze.md`.
- Q0 evidence remains closure-positive with 15 Q0 tests, 17 authority tests,
  reproducibility/restart/sharded checks, safe loading, zero padding
  contamination, and 2,304/2,304 focused mutations. Q1 remains complete with
  exact StatePrep validation, bounded K9 edge-ADAPT replay, K11/K13 holdouts,
  and no physical state or parameter selection. Q2 remains complete with
  471 registry records, 157 K9 records, source-structured measurement terms,
  14 focused tests passing, 384/384 mutation checks, zero production
  `QubitUnitary`, and no physical/hardware/shot activation.
- No Q3 quantum continuation is authorized. Any future extension must use a
  new worktree, consume only the frozen public APIs, publish a new acceptance
  root, and leave the Q0–Q2 commits unchanged.
