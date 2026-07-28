# Decision log

## D-044: Temporary nucleon TMD boundaries cannot become production defaults

- Date: 2026-07-25
- Question: How should unavailable fitted nucleon TMD inputs be represented
  while parent development proceeds?
- Adopted choice: Use replaceable flavor-resolved components with explicit
  provenance, validity, parameter uncertainty, and replacement tests.
  Current Gaussian widths, signed-Soffer transversity, WW worm gears, zero
  pretzelosity, and real-boundary T-odd zeros are temporary as specified in
  `handoff/ROADMAP.md`.
- Justification: This permits parent implementation without hiding missing
  physics or converting a boundary assumption into a named deuteron TMD.
- Alternatives considered: universal Gaussian amplitudes (rejected);
  omitting the full operator (rejected when an explicit zero/parameter
  component is meaningful); claiming current fit values without ingesting
  their tables/covariance (rejected).
- Classification: model dependent or unconstrained, except the T-odd zero
  of the explicitly real one-body component.
- Files/tests: `nucleon_inputs.py`, `nucleon_quark_correlator.py`,
  `test_nucleon_inputs.py`, `test_nucleon_quark_correlator.py`.
- Revision trigger: vendored fit/lattice tables with conventions,
  covariance/replicas, and compatible validity domain.

## D-043: Provenance classes and fail-closed production tracing

- Date: 2026-07-25
- Question: How can exact constraints be kept distinct from fitted, lattice,
  model, and unconstrained components?
- Adopted choice: Every component carries an `EvidenceClass`, mechanism,
  source, assumptions, validity domain, uncertainty kind, and replacement
  interface. Unconstrained components without parameter uncertainty fail.
- Justification: Prevents model assumptions from silently acquiring the
  status of data or exact symmetry.
- Alternatives considered: prose-only metadata (rejected as unenforceable);
  one generic “model uncertainty” label (rejected as noncompositional).
- Classification: software architecture enforcing a scientific distinction.
- Files/tests: `provenance.py`, `test_provenance.py`.
- Revision trigger: a richer inference backend may extend, but not erase,
  the evidence classes.

## D-042: Retain proton and neutron contributions through convolution

- Date: 2026-07-25
- Question: At what stage may proton and neutron terms be combined?
- Adopted choice: Retain them separately through the parent correlator and
  combine only in an explicitly labeled inclusive mechanism/observable.
- Justification: Required for flavor tracing, tagged observables,
  uncertainty correlations, off-shell differences, electromagnetic
  weighting, and controlled isospin breaking. Exact \(I=0\) equality must
  emerge as a tested limit.
- Alternatives considered: sum p+n at each quadrature node (superseded);
  hard-code \(u_D=d_D\) (rejected as architecture).
- Classification: exact bookkeeping requirement; charge symmetry remains a
  controlled theoretical constraint.
- Files/tests: `gtmd_convolution.py`, `parent_quark_tmd.py`,
  `test_parent_quark_tmd.py`, `test_nucleon_inputs.py`.
- Revision trigger: none; tagged and inclusive assembly may add consumers.

## D-041: Parent traceability is a non-negotiable production gate

- Date: 2026-07-25
- Question: Can missing parent correlator layers be replaced by a complete
  downstream amplitude table?
- Adopted choice: No. Every production TMD must be projected from the
  nucleon operator correlator convolved with the spin-1 LF nuclear kernel,
  with mechanisms and provenance retained.
- Justification: TMDs, GPDs, PDFs, and Wigner distributions are required
  reductions of one parent object; downstream completion breaks that
  consistency.
- Alternatives considered: the D-033 constrained completion and D-040
  reduced-amplitude model (both superseded as production physics).
- Classification: governing architecture and acceptance constraint.
- Files/tests: `AGENTS.md`, `handoff/ROADMAP.md`,
  `production_tmd_architecture_audit.md`, parent correlator modules.
- Revision trigger: only a change to the project’s scientific research
  objective, not implementation difficulty.

## Superseded decisions

- D-033 “constraint-based completion” and D-040
  “production completion must be correlator-derived” did not enforce the
  actual project light-front parent chain. Their generated complete tables
  remain regression fixtures only and cannot satisfy production gates.

## D-040: Production completion must be correlator-derived

- Date: 2026-07-25
- Status: accepted
- Scope: Produce all 19 gluon TMDs and all 18 quark TMDs for each of
  \(u,d,\bar u,\bar d\) from coherent species-specific correlator models.
- Prohibition: Do not complete the basis by attaching independent generic
  amplitude priors to uncalculated registry entries.
- Zeros: Exact or numerical zeros are valid model predictions when their
  dynamical or symmetry origin is recorded.
- Presentation point: Use \(x_N=0.1\), \(Q=5\) GeV and SIDIS as the primary
  view; retain DY for T-odd sign-reversal checks.
- Observable: Plot dimensional named TMDs \(F(x,k_T;Q)\), including \(f_1\),
  on a dense grid. Ratios to \(f_1\) are supplemental.
- Uncertainties: Keep PDF, wave-function, transverse-profile,
  evolution/scale, mechanism, gauge-link-phase, and numerical components
  separate unless an explicit probabilistic combination is justified.
- Mathematical structure: Representation theory and algebraic/geometric
  topology may organize or validate symmetry and phase constraints when
  physically operative, but cannot replace nonperturbative dynamics.

## D-039: Polarized transverse width is a sensitivity bracket

- Date: 2026-07-24
- Status: accepted
- Range: Evaluate polarized widths 0.15, 0.25, and
  \(0.40\ {\rm GeV}^2\).
- Interpretation: Treat the min/max envelope as model sensitivity, not a
  one-sigma uncertainty. No prior probability has been assigned to these
  widths.
- Consistency: Require the integrated rank-zero \(g_1^g\) result to remain
  stable across widths; local TMD densities may change strongly as the
  transverse shape is redistributed.
- Combination: Store width, BDSSV24 replica, wave-function, and numerical
  components separately. Do not add them in quadrature until the width has
  an independently justified probabilistic interpretation.

## D-038: Production helicity-PDF uncertainty uses all 600 replicas

- Date: 2026-07-24
- Status: accepted
- Decision: Use the complete BDSSV24 replica ensemble for the production
  \(g_1^g\) and \(g_{1T}^g\) PDF uncertainty fields.
- Reason: Nested 80- and 101-member studies retained several-percent
  differences, and subset estimates continued to fluctuate at larger
  counts. The exact response makes the full propagation inexpensive once
  the files are local.
- Separation: Store PDF standard deviations and percentiles independently
  of wave-function envelopes and numerical convergence errors.
- Interpretation: Do not form or quote relative uncertainty for the
  numerical-zero T-odd \(g_{1LT}^g\) channel.

## D-037: Replica propagation uses an exact linear response

- Date: 2026-07-24
- Status: accepted
- Method: Precompute the nuclear response to \(\Delta g(z,Q)\) at each
  unique light-front fraction, then contract that response with each PDF
  replica. Do not rerun the full retained-index convolution per member.
- Validation: Require machine-precision agreement with the direct central
  calculation before using the response for uncertainty propagation.
- Pilot status: The 31 deterministic replicas give an uncertainty scale,
  not a production band. A 20-member nested subset remains 10%-level
  different from the 31-member standard-deviation field.
- Expansion rule: Increase to at least about 100 members and assess nested
  convergence before deciding whether all 600 replicas are needed.
- T-odd rule: Do not quote relative PDF uncertainties for channels whose
  central value is numerical zero.

## D-036: Use BDSSV24 as the independent gluon-helicity input

- Date: 2026-07-24
- Status: accepted
- Input: Use the BDSSV24-NLO polarized proton PDF for the first physical
  \(\Delta g\) input, independently of the CT18NNLO unpolarized gluon PDF.
- Storage: Vendor the official LHAPDF metadata and member 0 under
  `data/raw/lhapdf`; do not alter the global conda LHAPDF installation.
- Scope: The central member enables the L/T/LT circular-gluon calculation.
  It does not provide a complete uncertainty estimate.
- Time reversal: With real one-body wave functions and no gauge-link phase,
  all T-odd gluon TMDs must remain zero up to numerical precision.
- Uncertainty separation: Keep BDSSV24 replica uncertainty distinct from
  deuteron wave-function and numerical-integration uncertainties.

## D-035: Separate numerical convergence from wave-function spread

- Date: 2026-07-24
- Status: accepted
- External convergence: Track the finite \(k_T\) box/grid error through
  direct comparison of TMD marginals with the matching collinear
  convolution.
- Internal convergence: Compare full grids in relative \(L_2\) norm and
  record smearing normalization; marginal closure alone can hide internal
  quadrature error because both sides use the same quadrature.
- Rejection: Do not use the \(12\times8\times8\) internal grid for physics
  comparisons.
- Envelope normalization: Divide each finite-quadrature wave-function grid
  by its recorded unpolarized smearing norm before constructing the
  wave-function envelope.
- Reporting: Keep raw grids and normalization metadata intact. Quote tensor
  relative bands together with absolute values because near-zero tensor
  means amplify percentage spreads.

## D-034: Gluon TMD grid normalization and positive-rank marginals

- Date: 2026-07-24
- Status: accepted
- Unit conversion: The retained parent is evaluated in
  \({\rm fm}^{-1}\); report TMD densities per \({\rm GeV}^2\) with the
  appropriate \((\hbar c)^{-2}\) factor.
- Parent conversion: For the current p+n parent normalization, conversion
  to the per-nucleon \(x_N=2x_D\) tables supplies a total factor \(1/4\),
  separate from the transverse-unit conversion.
- Marginal test: Validate rank-zero \(f_1^g\) and \(f_{1LL}^g\) against
  independent collinear convolutions using the identical internal
  quadrature.
- Positive-rank rule: Never interpret
  \(\int d^2k_T\,h_1^{\perp g}\) or
  \(\int d^2k_T\,h_{1LL}^{\perp g}\) as a collinear PDF. Integrate the full
  rank-two correlator tensor, whose angular marginal vanishes under
  rotationally symmetric coverage.
- Convergence status: The 24-by-24 external grids close the rank-zero
  marginal at better than \(4\times10^{-5}\), but the moderate internal
  quadrature normalization is only 0.991--0.996. Treat the present grids as
  validated marginal fixtures, not final precision bands.

## D-033: First nucleon gluon-TMD input is a declared boundary model

- Date: 2026-07-24
- Status: accepted
- Unpolarized input: Normalize a Gaussian transverse profile to a supplied
  collinear \(f_1^g(x)\), provisionally CT18NNLO for numerical scans.
- Helicity input: Require a separate polarized gluon PDF provider for
  \(g_1^g\). Do not derive it from the unpolarized CT18NNLO density.
- Linear input: Parameterize \(h_1^{\perp g}\) through a dimensionless
  `linear_fraction` whose correlator contribution is bounded in magnitude
  by that fraction of the trace contribution and is regular at \(k_T=0\).
- Interpretation: Width, linear fraction, and transfer slope are explicit
  sensitivity parameters. They are not fitted values and do not import the
  gluon spectator model.
- Projection convention: Convert the coefficient of the code's `LL`
  spin-one basis to the physical named LL correlator with an explicit minus
  sign, equivalent to \(f_{1LL}=-(2/3)\delta_Tf_1\).

## D-032: Collinear one-body gluon baseline and transversity null test

- Date: 2026-07-24
- Status: accepted
- Baseline input: Use the CT18NNLO central gluon PDF at \(Q=2\) GeV for the
  first unpolarized nucleonic IA scan. Proton and neutron gluon inputs are
  identical under isospin.
- Scaling: Quote results per nucleon versus nucleon-mass \(x_N\), with
  \(x_D=x_N/2\), consistently with the quark parent calculations.
- Tensor convention: Store both the direct helicity difference
  \(\delta_Tf_1^g\) and the named
  \(f_{1LL}^g=-(2/3)\delta_Tf_1^g\).
- Null result: Set collinear one-body \(h_{1TT}^g=0\) only after verifying
  that the spin-1/2 collinear nucleon correlator has no
  symmetric-traceless gluon-index component. A nonzero result must enter
  through a separately declared coherent, exchange-current, or
  non-nucleonic mechanism.
- Limitation: CT18NNLO supplies the collinear unpolarized gluon density; it
  does not determine gluon transverse profiles or polarized gluon TMDs.

## D-031: Gluon correlators use a Euclidean transverse-index adapter

- Date: 2026-07-24
- Status: accepted
- Decision: Store numerical gluon correlators as complex \(2\times2\)
  Cartesian arrays with \(-g_T^{ij}\) represented by
  \(\delta^{ij}\) and \(\epsilon_T^{12}=+1\).
- Decomposition: Separate each array into trace, imaginary antisymmetric,
  and real symmetric-traceless pieces before applying named TMD projectors.
- Scope boundary: The basis formulas are operator identities. No spectator
  vertex, mass spectrum, fitted parameter, or spectator-model TMD enters
  this implementation.
- Degeneracy rule: Reject positive-rank projections at \(k_T=0\), where
  their tensor basis vanishes and the named coefficient is not separately
  identifiable.
- Consequence: U, L, and LL projections are inverted directly. T, LT, and
  TT use a joint real design system over independent target polarizations.
- TT identity: Keep `f1TT` and `h1TTperp` as separate formal registry
  entries, but project only `f1TT_minus_h1TTperp` from the transverse
  correlator. Separating them requires additional convention/model
  information and must never be inferred from a numerically singular fit.

## D-030: Complete definite-rank leading-twist TMD inventories

- Date: 2026-07-24
- Status: accepted
- Decision: Use the definite-rank basis of arXiv:1612.06585 as the
  authoritative common inventory for quarks, antiquarks, and gluons.
- Counts: 18 quark, 18 antiquark, and 19 gluon TMDs across U, L, T, LL, LT,
  and TT target channels.
- Rank policy: Construct all transverse structures from symmetric-traceless
  two-dimensional tensors. The Fourier-Bessel order equals the stored rank.
- Time-reversal policy: Keep T-odd functions in the operator registry even
  when a tree-level boundary model makes them vanish. Gauge-link direction
  remains part of their identity.
- Collinear exception: `h1LT` is rank zero but has no collinear PDF because
  it is T-odd; rank alone is not sufficient to determine its limit.
- Tensor convention: Use \(S_{LL}(\pm1)=1/2\), \(S_{LL}(0)=-1\), implying
  \(f_{1LL}=-(2/3)\delta_Tf\).

## D-029: Published TMD basis is authoritative for registry expansion

- Date: 2026-07-24
- Status: accepted
- Quark benchmark: Use Eqs. (5a)-(5e) of Poudel et al., EPJ A 61:81, as the
  longitudinal-tensor SIDIS structure-function checklist. Do not describe
  that paper as a numerical deuteron quark-TMD calculation.
- Gluon benchmark: Use Eqs. (7)-(12) and Table I of arXiv:2603.15224v1 only
  to compare names, target channels, gluon polarizations, transverse ranks,
  tensor factors, and correlator/projector algebra for the 19 leading-twist
  gluon TMDs.
- Spectator-model boundary: Do not adopt, fit, reproduce, or use the paper's
  spectator model as a phenomenological baseline or project input.
- Mechanism separation: Generate project gluon TMDs from the project's own
  nucleonic, coherent, exchange-current, and non-nucleonic mechanism layers.
- Null baseline: Treat collinear \(h_{1TT}^g\) as zero in the simple
  spin-1/2 nucleon one-body baseline; a nonzero direct-deuteron result is a
  distinct physics contribution.
- Convention requirement: Add an explicit adapter before equating the
  internal `deltaT_f1` with named \(f_{1LL}\) or an experimental
  \(T_{\parallel\parallel}\) coefficient.

## D-028: Parent marginal convention and Wigner cutoff status

- Date: 2026-07-24
- Status: accepted
- Scaling convention: For nucleon-mass Bjorken \(x_N\), sample the parent at
  \(x_D=x_N/2\) and use \(q_N(x_N)=q_D(x_D)/2\). Then apply the standard
  factor \(b_1=\delta_Tq_N/2\) after charge weighting.
- Component policy: Preserve `SD` and `DS` independently in machine-readable
  arrays; combine them only in presentation-level `SD+DS` views.
- Cutoff policy: Quote the current Wigner calculation as a finite-transfer
  transform and keep its cutoff sensitivity separate from wave-function
  model spread.
- Domain policy: Do not extrapolate finite tabulated radial functions to
  accommodate shifted off-forward momenta. Reduce the internal domain or
  obtain a longer authoritative table.
- Detection: Parent-derived and independently convolved \(b_1\) must agree
  point by point; component matrices must reconstruct the full parent.

## D-027: First fixed-k partonic Wigner production boundary

- Date: 2026-07-24
- Status: accepted
- Decision: Use a normalized factorized Gaussian, helicity-independent
  rank-zero nucleon GTMD as the first production boundary input. Keep the
  complete deuteron \(3\times3\) helicity matrix through convolution and
  Fourier transformation.
- Parameters: CT18NNLO at \(x=0.2,Q=2\) GeV, \(u\) flavor,
  \(\langle k_T^2\rangle=0.25\ {\rm GeV}^2\), transfer slope
  \(1\ {\rm GeV}^{-2}\), future-pointing `[+,+]` gauge-link label, and
  \(\Delta_N=\Delta_D\).
- Reason: This supplies a reproducible fixed-\(k\) parent and tests the full
  nuclear helicity/Wigner machinery without claiming unavailable empirical
  nucleon-GTMD knowledge.
- Consequence: Results may be called the impulse-approximation baseline under
  the declared boundary model, but not a model-independent Wigner
  extraction. Both finite Fourier boxes must remain explicit metadata.
- Detection: The finite-grid \(k_T\) marginal must agree with the analytic
  GPD convolution, and
  \(W(-\Delta)=W(\Delta)^\dagger\) must hold before transformation.

## D-026: Six-wave-function propagation during the current-operator hold

- Date: 2026-07-24
- Status: accepted
- Decision: Use AV18, CD-Bonn, NV2-Ia, NV2-Ib, NV2-IIa, and NV2-IIb as the
  standard ensemble for wave-function model-spread bands.
- Scope: The body-overlap transform may be labeled an integrated-momentum
  GTMD/impact-space marginal, but not a full fixed-momentum Wigner
  distribution.
- Current caveat: Printed-2019 Norfolk contact coefficients may be used only
  in explicitly labeled legacy diagnostics. OPE and affected fitted contact
  terms remain excluded from validated production results until corrected
  values are obtained.
- Detection: Output tables must carry enough metadata to distinguish
  wave-function spread from transform, numerical, PDF/fragmentation, and
  current-operator uncertainties.

Record settled scientific conventions and software architecture here. Every entry should state the
reason and the observable or test that detects an inconsistent choice.

## D-001: Hand-off notes location

- Date: 2026-07-23
- Status: accepted
- Decision: Keep durable project notes under `handoff/`.
- Reason: Conversation history and scratch files are not sufficient project memory.
- Consequence: Material implementation work must update `worklog.md`; scientific and
  architectural choices must update this file.

## D-002: Tensor normalization during early implementation

- Date: 2026-07-23
- Status: accepted
- Decision: Store the convention-independent helicity difference
  \(\delta_TF=F^0-\tfrac12(F^++F^-)\) as the primary tensor quantity.
- Reason: Published \(S_{LL}\) conventions differ in sign and normalization.
- Consequence: Convert to \(f_{1LL}\) only through an explicit convention adapter. The \(b_1\)
  test operates directly on \(\delta_Tq\) and \(\delta_T\bar q\).
- Detection: Equation (23) of the brief and inverse helicity relations (120)-(122).

## D-003: Separate transverse impact parameters

- Date: 2026-07-23
- Status: accepted
- Decision: Treat the coordinate conjugate to GTMD transfer, `b_delta`, and the coordinate
  conjugate to TMD momentum, `b_tmd`, as distinct quantities.
- Reason: They describe transverse imaging and TMD evolution respectively and are often
  confusingly denoted by the same symbol in the literature.
- Consequence: APIs must not accept an untyped generic `bT` where the distinction matters.
- Detection: GTMD-Wigner and TMD Fourier transforms must independently invert.

## D-004: Positivity boundary for the nuclear Wigner layer

- Date: 2026-07-23
- Status: accepted
- Decision: Require positive semidefiniteness of the underlying helicity density matrix, but do
  not impose pointwise positivity on its Wigner transform or on partial phase-space integrals.
- Reason: Neff and Feldmeier show that negative interference contributions are essential to the
  short-distance correlation hole and intermediate-momentum structure.
- Consequence: Wigner negativity is a diagnostic, not automatically a numerical failure.
- Detection: Density-matrix eigenvalue tests before transformation; exact marginal reconstruction
  after transformation.

## D-005: Retain wave-function component interference

- Date: 2026-07-23
- Status: accepted
- Decision: Preserve and expose \(S\)-\(S\), \(S\)-\(D\), \(D\)-\(S\), and \(D\)-\(D\)
  contributions in the nuclear kernel.
- Reason: Tensor correlations and short-range Wigner oscillations are driven substantially by
  interference rather than diagonal high-momentum probability alone.
- Consequence: Internal APIs cannot reduce wave-function inputs to incoherent component
  probabilities before forming the density matrix.
- Detection: Component sums must reproduce the full complex overlap and all marginals.

## D-006: Implementation language and baseline environment

- Date: 2026-07-23
- Status: accepted
- Decision: Implement the project in Python, initially targeting the existing conda base
  environment at `/Users/dustin/miniforge3`.
- Available baseline: Python 3.9.23, NumPy 1.26.3, SciPy 1.13.0, LHAPDF 6.5.5, and
  PyTorch 2.8.0.
- Reason: Explicit user direction and an existing scientific Python/LHAPDF environment.
- Consequence: NumPy/SciPy are the default numerical backend. PyTorch should be introduced only
  when automatic differentiation, accelerators, or inference workloads justify it.

## D-007: Raw wave-function input policy

- Date: 2026-07-23
- Status: accepted
- Decision: Preserve authoritative downloads under `data/raw/` without modification and record
  URLs, checksums, units, normalization, and references in `data/README.md`.
- Reason: Radial-function conventions and silent normalization changes are a major scientific
  failure mode.
- Consequence: Parsers never overwrite raw inputs. Convention conversion and interpolation produce
  separate processed data with reproducible generators and validation reports.

## D-008: Initial nucleon PDF baseline

- Date: 2026-07-23
- Status: provisional
- Decision: Use LHAPDF through an abstract PDF-provider interface. Start numerical fixtures with
  the installed `CT18NNLO` central member; retain `MSHT20nnlo_as118`,
  `NNPDF40_nlo_as_01180`, and `NNPDF40_nnlo_as_01180` for cross-checks and uncertainty studies.
- Reason: CT18NNLO is already installed, well-established, and suitable as a stable nucleon
  baseline while the factorization order and fitting strategy are finalized.
- Consequence: No physics module may depend directly on CT18-specific APIs or member numbering.
  The perturbative order used in an observable must be recorded and checked against its hard and
  matching coefficients.
- Revisit: Before Stage 1 phenomenology and any comparison to \(b_1\) data.

## D-009: Instant-form reduced radial normalization

- Date: 2026-07-23
- Status: accepted
- Decision: Represent coordinate-space inputs as reduced radial functions \(u(r),w(r)\) in
  \(\mathrm{fm}^{-1/2}\), normalized by
  \(\int_0^\infty dr\,[u^2+w^2]=1\). Represent momentum-space inputs as
  \(u(k),w(k)\) in \(\mathrm{fm}^{3/2}\), normalized by
  \(\int_0^\infty dk\,k^2[u^2+w^2]=1\).
- Reason: These are the explicit conventions of the authoritative AV18 tables and CD-Bonn
  Appendix D.
- Consequence: Factors of \(r\), \(k\), \(4\pi\), or \((2\pi)^3\) may not be inserted implicitly.
  Any conversion to a full three-dimensional wave function requires a named adapter.
- Detection: Coordinate and momentum normalization tests and Fourier-Bessel reconstruction.

## D-010: CD-Bonn D-wave Fourier phase

- Date: 2026-07-23
- Status: accepted
- Decision: The momentum-space CD-Bonn \(D\)-wave implementation carries the relative
  \(i^L=i^2=-1\) phase with respect to the coordinate-space reduced \(D\) wave.
- Reason: With the sign shown naively by the extracted Appendix D rational sum, the numerical
  \(j_2\) Fourier-Bessel transform returns \(-w(r)\). Including the phase reconstructs Table XIX
  and Eq. (D13).
- Consequence: The phase is explicit in `wavefunctions/cd_bonn.py` and protected by a transform
  test at four radii.
- Detection: Coordinate/momentum Fourier-Bessel consistency fails by a sign if omitted.

Clarification added after the electromagnetic-current benchmark: the stored reduced radial
\(w(k)\) reconstructs positive coordinate-space \(w(r)\) under the paper's radial
Fourier-Bessel formula. The full angular momentum-space wave function requires a further
\(i^2=-1\) multiplier when coupling \(w(k)Y_{2m}\). This phase belongs in
`canonical_deuteron_amplitude`, applies to both AV18 and CD-Bonn, and is distinct from the
analytic coefficient sign inside the CD-Bonn radial generator.

## D-011: Interpolation and extrapolation policy

- Date: 2026-07-23
- Status: accepted
- Decision: Use shape-preserving PCHIP interpolation for tabulated radial functions and reject
  extrapolation.
- Reason: High-order unconstrained splines can introduce artificial nodes or oscillations, while
  silent extrapolation can corrupt normalization and high-momentum behavior.
- Consequence: Analytic tails or origin limits must be introduced as explicit, separately tested
  models. The AV18 normalization diagnostic uses its published asymptotic constants without
  modifying the raw table.
- Detection: Out-of-domain interpolation requests raise `ValueError`.

## D-012: Stage 0 Fourier and external-state conventions

- Date: 2026-07-23
- Status: accepted
- Decision: Use
  \(\int d^2\Delta_T/(2\pi)^2\,e^{-i\Delta_T\cdot b_\Delta}\) for GTMD imaging and
  \(\int d^2k_T\,e^{+ib_{\rm TMD}\cdot k_T}\) for the TMD coordinate transform. At zero
  skewness, construct symmetric external states with transverse momenta
  \(\mp\Delta_T/2\), retaining the resulting \(\Delta_T^2/4\) term in the average minus
  component.
- Reason: These conventions match the project brief and keep both external deuteron states
  on shell.
- Consequence: The two conjugate coordinates have separate types and convention objects.
- Detection: Analytic Fourier inversion, commuting marginal tests, and external-state
  mass-shell tests.

## D-013: Equal-mass light-front mapping and normalization

- Date: 2026-07-23
- Status: accepted
- Decision: For constituent fraction \(y=p_N^+/P_D^+\), use
  \(M_0^2=(m_N^2+p_T^2)/[y(1-y)]\),
  \(k_z=(y-\tfrac12)M_0\), and
  \(dk_z/dy=M_0/[4y(1-y)]\). Apply unitary constituent Melosh rotations and absorb the
  square-root Jacobian into the light-front amplitude. The baseline smearing density is
  normalized with the flat measure \(dy\,d^2p_T\).
- Reason: This mapping gives an exact one-to-one conversion to the normalized instant-form
  relative momentum for equal masses.
- Consequence: Production smearing integrals use spherical internal-momentum quadrature; direct
  endpoint-sensitive \(y\) quadrature remains available only as a diagnostic.
- Detection: Unitary Melosh tests, wave-function norm reconstruction, helicity-sum rules, and
  convergence against radial normalization.

## D-014: Experimental \(x\), constituent fraction, and per-nucleon \(b_1\)

- Date: 2026-07-23
- Status: accepted
- Decision: Distinguish target \(x_D=Q^2/(2P_D\cdot q)\) from the HERMES nucleon-mass variable
  \(x_N=Q^2/(2M_N\nu)\simeq2x_D\). With \(y=p_N^+/P_D^+\), use constituent fraction \(y\)
  for \(x_D\) convolutions and \(2y\) for \(x_N\) convolutions. Report the HERMES comparison
  per nucleon.
- Reason: The convention mapping is stated explicitly in the standard-convolution analysis
  arXiv:1702.05337 and prevents a factor-of-two error in both support and normalization.
- Consequence: Observable APIs require an explicit `ScalingVariable`; the HERMES script defaults
  to `NUCLEON` and applies the per-nucleon factor.
- Detection: Rescaling tests relate \(x_N=2x_D\), and the tensor smearing integral vanishes.

## D-015: Status of the first \(b_1\) baseline

- Date: 2026-07-23
- Status: provisional
- Decision: Use CT18NNLO member 0 only as a reproducible PDF-shape fixture for the first
  leading-order partonic impulse calculation.
- Reason: No LO set is currently installed, and three of the six HERMES points have
  \(Q<1.295\) GeV, below the CT18NNLO validity range. The low-\(Q^2\) data also require care
  beyond a pure leading-twist comparison.
- Consequence: Every table flags points below the PDF range. These predictions are validation
  baselines, not a precision phenomenology result; perturbative consistency and finite-\(Q^2\)
  treatment remain open.
- Detection: The command-line report prints the LHAPDF \(Q\) range and a per-point validity flag.

## D-016: Forward rank-zero TMD convolution

- Date: 2026-07-23
- Status: accepted
- Decision: Implement the deuteron-target-\(x\) forward convolution in \(b_{\rm TMD}\) space
  with the phase
  \(\exp[i(x/y)b_{\rm TMD}\cdot p_T]\), as in Eq. (84) of the brief. Retain individual
  \((y,p_x,p_y)\) nuclear quadrature nodes rather than azimuthally averaging before applying
  the phase.
- Reason: The \(b\)-space form cleanly separates nuclear transverse broadening from the nucleon
  TMD and is the appropriate representation for later evolution.
- Consequence: The first implementation covers scalar rank-zero nucleon inputs in the U and LL
  target channels. Spin-transfer terms and evolution are separate additions.
- Detection: At \(b_{\rm TMD}=0\), both channels reproduce the collinear convolution exactly.
  The full realistic kernel reproduces the wave-function norm and zero tensor sum.

## D-017: First TMD and SIDIS numerical fixture

- Date: 2026-07-23
- Status: provisional
- Decision: Use a normalized Gaussian nucleon rank-zero boundary profile,
  \(\widetilde F(b)=f(x)\exp[-\langle k_T^2\rangle b^2/4]\), solely to validate nuclear
  broadening, Fourier--Bessel inversion, and the radial SIDIS W term. Use the convention-safe
  ratio \(\delta_TW/W_U\) until the chosen \(f_{1LL}\) and experimental asymmetry convention
  is applied.
- Reason: A declared analytic input isolates nuclear and numerical effects without implying that
  the Gaussian is a fitted or evolved physical TMD.
- Consequence: Generated Stage 2 tables must list the Gaussian widths and omitted hard,
  evolution, Y, spin-transfer, and non-impulse terms.
- Detection: The analytic Gaussian transform pair passes regression tests; the realistic
  \(k_T\)-integrated result recovers its \(b=0\) value to better than \(8\times10^{-4}\).

## D-018: Active-nucleon spin-density ordering and contraction

- Date: 2026-07-23
- Status: accepted
- Decision: Store the nuclear spin kernel as
  \(S_{\Lambda'\Lambda;\lambda'_N\lambda_N}\), with array order
  `(target_out, target_in, nucleon_out, nucleon_in)`. Contract a nucleon correlator as
  \(S_{\lambda'\lambda}F_{\lambda\lambda'}=\mathrm{Tr}(SF)\).
- Reason: This ordering makes the combined target/active matrix Hermitian and positive
  semidefinite in the forward limit and makes spectator tracing explicit.
- Consequence: Identity nucleon correlators exactly reproduce the earlier scalar U/LL
  convolution; Pauli components generate spin-transfer terms without a separate ad hoc formula.
- Detection: Combined-matrix PSD, active-helicity trace, U/LL scalar reduction, and explicit
  helicity-asymmetry contraction tests.

## D-019: Initial active-nucleon GTMD transfer map

- Date: 2026-07-23
- Status: accepted for the one-body baseline
- Decision: Use the callable one-body GTMD parent with the explicit identity mapping
  \(\Delta_{T,N}=\Delta_T\), represented by `TransferMapping.IDENTITY`.
- Reason: Besides being the simplest mapping stated in the brief, it reproduces the authoritative
  AV18/Kelly impulse \(G_C\) benchmark at the percent level through 0.5 GeV. The tested
  alternative \(\Delta_{T,N}=y\Delta_T\) is already wrong by about 2%, 8%, and 17% at
  0.1, 0.2, and 0.3 GeV respectively.
- Consequence: The mapping is a required object in the convolution API and must be revisited
  for mechanisms beyond the one-body impulse baseline. Alternative mappings remain separately
  named enum values; `ACTIVE_FRACTION` is retained as a rejected-comparison fixture and never
  changes the meaning of `IDENTITY`.
- Detection: The same parent passes its forward TMD view, \(k_T\)-integrated GPD view,
  \(\Delta\)-Hermiticity, forward normalization, and AV18 impulse-current tests.

## D-020: Electromagnetic-current benchmark

- Date: 2026-07-23
- Status: accepted
- Decision: Use the immutable `fdeut.av18` Kelly isoscalar form-factor and AV18 impulse tables as
  the first electromagnetic-current benchmark.
- Reason: The file supplies the exact nucleon inputs, body integrals, and \(G_C,G_M,G_Q\)
  outputs from one provenance-matched calculation, avoiding ambiguity from mixing fits and wave
  functions.
- Consequence: The first current test uses Wiringa's relation \(G_C=2G_E^s C_E\). Magnetic and
  quadrupole comparisons will use the accompanying \(C_L,C_S,C_Q\) tables before introducing
  newer nucleon fits or two-body currents.
- Detection: Parsing tests reproduce the tabulated \(G_C\) column from \(2G_E^sC_E\) to
  `3e-9` relative tolerance, reproduce \(G_M,G_Q,A,B,t_{20}\) within printed table precision,
  and reject extrapolation.

## D-021: Light-front helicity-current and angular-condition convention

- Date: 2026-07-23
- Status: accepted
- Decision: Store amplitudes normalized as
  \(I_{\lambda'\lambda}=J^+_{\lambda'\lambda}/(2P^+)\), with explicit
  \(I_{0+}=-I_{+0}\). Use the Carlson-Ji condition
  \((1+2\eta)I_{++}+\sqrt{8\eta}I_{0+}+I_{+-}-I_{00}=0\),
  \(\eta=Q^2/(4M_D^2)\).
- Reason: It fixes the time-reversal sign that otherwise changes the single-flip term and anchors
  the diagnostic to a primary derivation.
- Consequence: Nucleon inputs use
  \(J_N^+/(2p_N^+)=F_1\) on the diagonal and
  \(QF_2/(2m_N)\) in the helicity-flip element. Form-factor extraction is implemented from every
  choice of three amplitudes; prescription spread is a covariance diagnostic.
- Detection: Covariant synthetic currents satisfy the angular condition to machine precision and
  all four extraction prescriptions recover identical \(G_C,G_M,G_Q\).

## D-022: Wave/current component diagnostics

- Date: 2026-07-23
- Status: accepted
- Decision: Preserve coherent \(SS,SD,DS,DD\) off-forward kernels and separately contract their
  \(F_1\) and \(F_2\) current pieces. Provide `SpinRotation.IDENTITY` only as a named diagnostic;
  `MELOSH` remains the physical baseline.
- Reason: Angular-condition violations contain large cancellations and cannot be attributed from
  incoherent S/D probabilities. Turning off Melosh rotations tests their role without silently
  changing the production wave function.
- Consequence: Every decomposition must reconstruct the full complex current and angular residual
  at floating-point precision.
- Detection: Component sums reconstruct the retained-spin overlap below `3e-15`; all eight
  current pieces reconstruct the full angular residual below `2e-14`.

## D-023: Static magnetic audit and phenomenological completion

- Date: 2026-07-24
- Status: accepted as a diagnostic benchmark, not as final dynamics
- Decision: Diagnose the \(Q\to0\) limit before adding missing-current physics. Preserve the raw
  one-body current and add any sensitivity term as a separate covariant, purely magnetic
  completion
  \(\delta G_M(Q)=\delta\mu/[1+(Q/\Lambda)^2]^2\).
- Reason: The raw GK/BH extraction approaches \(G_M(0)=2.13910\), whereas omitting
  \(I_{+0}\) approaches the AV18 impulse value \(1.69197\). The absolute angular residual scales
  as \(Q^2\), so it vanishes while leaving a finite form-factor prescription ambiguity. A
  higher-resolution check confirms this is not quadrature noise; the S-wave Pauli-current term
  dominates the residual.
- Consequence: Calibrating the static offset gives \(\delta\mu=-0.44712\). A one-parameter fit to
  the AV18 \(G_M\) shape through 0.5 GeV gives \(\Lambda=0.32808\) GeV and reduces the sampled
  \(G_M\) RMS error from 0.3475 to 0.00987. This fit measures the size/shape a missing covariant
  magnetic current would need; it is not evidence that the dipole ansatz is the underlying
  two-body current.
- Detection: The completion satisfies the angular condition to machine precision and extracts
  the same added \(G_M\) under all four prescriptions. The complete suite has 73 passing tests.

## D-024: Longitudinal-Breit covariant current replaces fitted completion

- Date: 2026-07-24
- Status: accepted as the preferred one-body current benchmark
- Decision: Use the Lev-Pace-Salme longitudinal Breit construction with
  \(J^+_{11}\), \(J^+_{00}\), and \(J^x_{10}-J^x_{01}\). Keep the old
  \(q^+=0\), \(J^+\)-only prescriptions and fitted dipole only as diagnostics.
- Reason: Carbonell-Karmanov show that a physical spin-1 magnetic form factor
  cannot in general be separated from spurious light-front structures using
  \(J^+\) alone. LPS provide a Poincare-covariant, Hermitian, conserved current
  built from one-body constituent terms in a longitudinal Breit frame.
- Consequence: The static AV18 magnetic result is \(G_M(0.01)=1.6834\), versus
  1.6881 in the AV18 impulse table, without a fitted magnetic term. At 0.5 GeV
  the covariant AV18/CD-Bonn values are 0.1443/0.1487; their difference is a
  wave-function model band rather than an angular-prescription band.
- Detection: The implementation preserves spectator plus momentum, retains the
  node-dependent nucleon transfer, has the correct zero-transfer constituent
  kernels, enforces LPS Hermiticity and \(j^-=j^+\), and passes 78 tests.
  A \(48\times32\times24\) check changes AV18 \(G_M(0.5)\) by \(3.0\times10^{-5}\).

## D-025: Chiral isoscalar two-body operator boundary

- Date: 2026-07-24
- Status: operator basis accepted; numerical contraction pending a consistent regulator choice
- Decision: Adopt Kolling-Epelbaum-Phillips Eq. (3) as the minimal isoscalar two-body magnetic
  basis: the long-range \(\bar d_9\) one-pion current and the short-range \(L_2\) M1 contact
  current. Do not insert tabulated LECs into AV18/CD-Bonn matrix elements without declaring and
  implementing the associated regulator.
- Reason: Both LECs are regulator dependent. The source fits \(L_2\) to the deuteron magnetic
  moment and \(\bar d_9\) to \(G_M\) below 400 MeV using chiral wave functions and matched
  cutoffs. Direct reuse with phenomenological wave functions would be an uncontrolled hybrid.
- Consequence: `two_body_current.py` supplies the exact unregularized spin operator and symmetry
  tests. The next numerical step must choose a regulator family and refit the two LECs separately
  for AV18 and CD-Bonn (or switch to consistent chiral wave functions).
- Detection: The operator is transverse, symmetric under nucleon exchange, vanishes at zero
  photon momentum, and the full suite has 82 passing tests.

## D-026: Lattice and perturbative boundary for gluon TMD profiles

- Date: 2026-07-24
- Status: accepted
- Decision: Do not use other phenomenological gluon-TMD profiles as project
  inputs. Replace the Gaussian production ambition with a \(b_T\)-space
  construction matched to collinear PDFs at small \(b_T\), while retaining
  an explicit family of large-\(b_T\) nuisance profiles. Keep the Gaussian
  only as a diagnostic fixture.
- Reason: Published work supplies gluon LaMET definitions and matching for
  \(f_1^g\), \(g_1^g\), and a clean proposed lattice ratio for
  \(h_1^{\perp g}/f_1^g\), but no published numerical lattice proton data
  were located that constrain these transverse profiles. Numerical lattice
  Collins-Soper kernels located in published work are quark results; the
  first gluon calculation remains preliminary.
- Consequence: Use CT18 and BDSSV24 for the collinear boundary, generate
  \(h_1^{\perp g}\) perturbatively at small \(b_T\), and report large-\(b_T\)
  dependence as model sensitivity. Do not promote perturbative Casimir
  scaling into an assumed nonperturbative quark-to-gluon kernel relation.
- Detection: Every future numerical result must identify perturbative order,
  TMD/rapidity scheme, transition prescription, and nonperturbative-profile
  member. A future lattice import must retain covariance and ensemble,
  momentum, renormalization, scale, and matching metadata.
- Evidence: `references/lattice_gluon_tmd_audit.md` and
  `outputs/stage0/lattice_gluon_tmd_input_status.csv`.

## D-027: Initial small-\(b_T\) gluon matching implementation

- Date: 2026-07-24
- Status: accepted as an intermediate QCD boundary, not production evolution
- Decision: Implement the first scheme-explicit \(b_T\)-space layer with
  tree-level matching for \(f_1^g\) and \(g_1^g\), and the first nonzero
  one-loop matching for \(h_1^{\perp g}\) in the delta-regulator
  Collins-TMD/zeta-prescription convention. Include both gluon and quark
  singlet channels in the linearly polarized coefficient.
- Reason: This removes the arbitrary `linear_fraction` from the QCD-matched
  path while using only controlled collinear inputs and published
  perturbative coefficients. It also keeps the b-space scalar distinct from
  the existing k-space Cartesian correlator convention.
- Consequence: `MatchedGluonTMD` returns inspectable perturbative and
  profile-completed values, along with machine-readable accuracy metadata.
  CT18 supplies \(g\), the quark singlet, and \(\alpha_s\); BDSSV24 supplies
  \(\Delta g\). Three unfitted Gaussian large-b factors are emitted strictly
  as a sensitivity family.
- Detection: The analytic constant-PDF convolution, endpoint behavior,
  collinear b=0 boundary, b-star bound, profile ordering, invalid domains,
  and approximation metadata are tested. The complete suite passes 137
  tests.

## D-028: Intermediate gluon CSS evolution and rank-2 transform

- Date: 2026-07-24
- Status: accepted as an intermediate uncertainty study, not a precision
  evolution baseline
- Decision: Evolve the matched boundary with a spin-independent one-loop CSS
  Sudakov exponent using \(A_g^{(1)}=C_A\) and
  \(B_g^{(1)}=-(11C_A-2n_f)/6\). Use
  \(\mu_b=\min[Q,\max(\mu_{\min},c_0/b_*)]\). Keep the unknown
  nonperturbative gluon Collins-Soper term optional and expose it as
  \(g_K b^2\ln(Q/Q_0)\) sensitivity members, including a zero member.
- Reason: This introduces genuine scale broadening while making the
  presently unconstrained gluon-kernel assumption removable. The same
  evolution factor is applied to all leading-twist gluon polarizations.
- Consequence: The b-space linearly polarized scalar is converted using
  \(h_{\rm paper}(k)=-\int b\,db\,J_2(bk)h(b)/(2\pi)\), followed by
  \(h_{\rm project}(k)=2M_N^2h_{\rm paper}(k)/k^2\), so it can be passed
  without a normalization change to the retained-index Cartesian
  correlator. The \(k=0\) value uses the analytic \(J_2(z)/z^2\) limit.
- Detection: Tests cover the zero-b evolution identity, canonical-scale
  bounds, CS-profile ordering, spin-independent ratio preservation,
  backward-evolution rejection, finite rank-2 zero-momentum limit, and
  Cartesian compose/project reconstruction. The complete suite passes 145
  tests.

## D-029: Strict evolved-table adapter for the nuclear convolution

- Date: 2026-07-24
- Status: accepted
- Decision: Connect evolved nucleon TMD tables to the one-body deuteron
  convolution through a radial \((x,k_T)\) interpolator that returns the full
  nucleon-helicity and transverse-gluon-index correlator. Convert nuclear
  momentum units to GeV inside the adapter and forbid extrapolation.
- Reason: The evolved boundary is expensive to reconstruct at every nuclear
  node, while the one-body convolution samples thousands of repeated points.
  A strict tabulated adapter preserves the existing retained-index API and
  makes its support limitations detectable.
- Consequence: The same nuclear contraction can now compare the evolved
  boundary with the historical Gaussian. The perturbative matching
  convolution uses cached 96-point Gauss-Legendre nodes rather than adaptive
  integration, removing harmless endpoint roundoff warnings and accelerating
  table generation.
- Detection: Tests cover bilinear interpolation, momentum-unit conversion,
  strict domain failure, and the returned `(2,2,2,2)` index structure. The
  full suite passes 148 tests.

## D-030: First evolved-versus-Gaussian AV18 comparison

- Date: 2026-07-24
- Status: accepted as a diagnostic, not a converged prediction
- Decision: Compare at \(x_N=0.1\), \(Q=5\) GeV using identical AV18 nuclear
  quadrature. Use the central evolved boundary/CS sensitivity member and the
  historical Gaussian width \(0.25\ {\rm GeV}^2\) with
  `linear_fraction=0.5`.
- Reason: This isolates the consequence of replacing the nucleon transverse
  input while leaving the nuclear mechanism fixed.
- Consequence: The evolved \(f_1^g\) is lower than the Gaussian below roughly
  \(k_T=0.65\) GeV and develops the expected much broader perturbative tail.
  The physically weighted linear-polarization ratio is small in the evolved
  result (about \(1.7\times10^{-5}\) at 0.05 GeV and \(3.4\times10^{-2}\) at
  1.5 GeV), whereas the arbitrary Gaussian fraction gives about 0.005 to
  0.45 over the same interval.
- Detection: The output stores both raw coefficients and
  \(k_T^2h_1^{\perp g}/(2M_D^2f_1^g)\), avoiding a misleading comparison of
  the raw mass-normalized coefficient near zero momentum.

## D-031: Evolved-TMD convergence and uncertainty separation

- Date: 2026-07-25
- Status: rank-zero audit accepted; LL tensor bands provisional
- Decision: Keep wave-function, intrinsic large-b, and nonperturbative
  Collins-Soper variations as separately reported uncertainty components.
  Benchmark nuclear quadrature against \(24\times16\times12\) rather than
  treating the original \(8\times6\times6\) scan as adequate.
- Reason: The initial coarse audit exposed 10--15% rank-zero errors and much
  larger tensor errors. With a \(16\times12\times8\) grid, maximum
  differences from the fine reference fall to 0.73%, 0.79%, and 0.73% for
  \(f_1^g\), \(g_1^g\), and \(h_1^{\perp g}\), respectively. The corresponding
  \(f_{1LL}^g\) and \(h_{1LL}^{\perp g}\) differences remain 3.2% and 7.6%.
- Consequence: Profile uncertainty clearly dominates the rank-zero
  wave-function spread in this scan, but the small wave-only envelope should
  not yet be interpreted below the quadrature floor. Tensor-polarized
  uncertainties require a dedicated higher-resolution study.
- Detection: Four \(k_T\) points from 0.1 to 1.5 GeV were checked on
  \(12\times8\times8\), \(16\times12\times8\), and
  \(24\times16\times12\) grids. All 216 wave/profile samples and the separated
  bands retain their exact configuration in adjacent metadata.

## D-032: Segmented radial quadrature for tensor gluon TMDs

- Date: 2026-07-25
- Status: accepted for the next tensor production scan
- Decision: Replace a single global radial Gauss-Legendre rule by fixed
  0.5 fm\(^{-1}\) intervals, each with six Gauss nodes, extending through
  12 fm\(^{-1}\). Retain independent angular quadratures.
- Reason: Varying the global radial order or cutoff relocates every node and
  produces non-monotonic 3--12% changes in the small LL difference. Azimuthal
  effects are below 0.15%, and extending a fixed segmented calculation from
  10 to 12 fm\(^{-1}\) changes the tensor channels below \(4\times10^{-5}\).
  The instability is therefore quadrature cancellation, not a physical
  high-momentum tail.
- Consequence: Relative to a 0.25 fm\(^{-1}\)-segment reference, the accepted
  0.5 fm\(^{-1}\) rule differs by 0.27% in \(f_{1LL}^g\) and 0.59% in
  \(h_{1LL}^{\perp g}\) at \(k_T=0.1,1.5\) GeV. `k_min` support was added to
  the off-forward quadrature builder so fixed radial pieces can be assembled
  without changing existing callers.
- Detection: Separate CSV/JSON audits vary global radial order, polar order,
  azimuthal order, cutoff, segment order, segment cutoff, and segment width.
  The radial-subinterval API has a focused unit test.

## D-033: Constraint-based completion of the full spin-1 TMD basis

- Date: 2026-07-25
- Status: accepted as the complete phenomenological model layer
- Decision: Supply every leading-twist quark, antiquark, and gluon TMD with
  either a derived anchor or a channel-correlated, rank-safe constrained
  completion. Preserve an explicit status on every output row.
- Reason: The full basis contains functions that cannot be generated by the
  present T-even spin-half nucleon impulse boundary. Leaving them absent
  prevents complete observable studies; narrow unconstrained curves would
  overstate knowledge.
- Consequence: Derived anchors are used for evolved gluon
  \(f_1,g_1,h_1^\perp\), impulse \(f_1,f_{1LL}\), depolarized quark \(g_1\),
  and Soffer-constrained quark \(h_1\). All other physical modulations obey
  individual and target-block unit budgets. Rank-zero quark \(h_{1LT}\) has
  an exact zero transverse integral.
- Detection: The catalog contains all 55 species-level functions and 22,860
  rows. Tests require registry coverage, rank bounds, block budgets,
  gauge-link reversal, direct rank conversion, and the \(h_{1LT}\) integral.

## D-034: Predictive-resolution boundary

- Date: 2026-07-25
- Status: accepted
- Decision: Do not force T-odd bands away from zero without gauge-link
  dynamics or process data. Use sign-resolved majority coverage rather than
  artificial universal precision as the completion criterion.
- Reason: Positivity, symmetry, endpoint behavior, and process reversal
  constrain T-odd functions but do not determine their absolute sign.
- Consequence: 99.77% of nonzero T-even phase points are sign resolved.
  Across the full basis, 57.81% are sign resolved. T-odd functions reverse
  exactly between SIDIS and DY but retain zero inside their 95% bands.
  High-k gluon W-term exceptions are flagged as requiring a Y term.
- Detection: `outputs/complete/spin1_tmd_predictive_coverage.csv` and its
  JSON summary are generated from the complete catalog.

## Pending decisions

## D-049: Do not renormalize the CSS W term into a full TMD marginal

- Date: 2026-07-25
- Status: accepted; fixed-order Y term remains required
- Question: Should the finite-b numerical W transform be rescaled so its
  finite-\(k_T\) integral equals the collinear parent result?
- Adopted choice: No. Validate the exact \(b_T=0\) parent limit independently,
  label production output as a low-\(k_T\) W term, and retain the observed
  marginal mismatch as a diagnostic requiring the fixed-order Y term.
- Justification: CSS factorization gives W+Y across transverse momentum.
  Multiplicative renormalization of W would hide missing fixed-order physics
  and distort the sourced small-b matching.
- Alternatives: Rescaling each channel to its collinear moment was rejected
  as an arbitrary universal correction. Calling the finite transform a
  sum-rule failure was rejected because the exact b=0 reduction passes.
- Classification: factorization-theoretic separation is exact; the current
  low-k cutoff and profile are model/numerical choices.
- Files/tests: `validate_parent_gluon_collinear_limit.py`,
  `audit_gluon_wterm_marginal.py`, six collinear validation JSON files,
  `gluon_av18_wterm_marginal.audit.json`, gluon metadata.
- Evidence: all six \(b_T=0\) f1/f1LL comparisons pass below
  \(1.7\times10^{-11}\) relative. The AV18 W-only stress test differs by
  14.3% for f1 and 54.3% for f1LL.
- Revision trigger: implementation of a sourced fixed-order gluon Y term and
  demonstrated cutoff-stable W+Y marginal.

## D-048: JAMDiFF pointwise transversity with composed-TMD positivity

- Date: 2026-07-25
- Status: accepted and implemented as the current central boundary; fit
  replicas and transversity evolution remain required
- Question: How should flavor-resolved nucleon transversity replace the
  physically invalid constant signed fractions of the Soffer ceiling?
- Adopted choice: Extract the 969-replica JAMDiFF `wLQCD` pointwise mean and
  standard deviation for \(u,d,\bar u,\bar d\) on five \(Q^2\) slices.
  Interpolate the evolved grid and project its mean onto the TMD-level Soffer
  interval of the CT18+BDSSV Gaussian boundary. Apply a configurable
  \((1-x)^8\) endpoint only to the unconstrained sea mean above \(x=0.5\).
- Justification: The bounded map enforces the pointwise Soffer inequality,
  while moment normalization prevents an arbitrary shape choice from
  generating unphysical tensor charges. JAMDiFF Table II provides a
  flavor-separated combined phenomenology+lattice benchmark.
- Alternatives: Constant Soffer fractions were rejected after producing
  \(\delta u=3.47,\delta d=-1.27\). A moment-normalized bounded shape was
  implemented as a tested fallback, then superseded in production by the
  authors' pointwise fit grid.
- Classification: source mean/std and scale dependence are
  phenomenology+lattice informed; Soffer positivity is exact; the
  cross-PDF positivity projection and sea endpoint are model-dependent
  compatibility choices.
- Files/tests: `nucleon_inputs.py`, `test_nucleon_inputs.py`,
  `validate_nucleon_quark_inputs.py`,
  `nucleon_quark_input_validation.json`.
- Evidence: projected moments are 0.680 and -0.193 versus source 0.710 and
  -0.200; the 2,304-point production joint-spin grid has minimum eigenvalue
  \(1.46\times10^{-10}\); all 196 tests pass; six wave-function tables and
  the ensemble atlas were regenerated.
- Revision trigger: availability of fit grids/replicas with covariance,
  nonzero sea constraints, or matched transversity evolution.

## D-047: Correct rank-three quark TT projection and test LF parity

- Date: 2026-07-25
- Status: accepted and implemented
- Question: Does the Cartesian basis independently reproduce the covariant
  quark decomposition, including parity and chiral-odd sigma conventions?
- Adopted choice: Convert every \(\sigma^{\mu+}\) chiral-odd term to the
  stored \(i\sigma^{i+}\gamma_5\) projection with the required transverse
  epsilon tensor. Test all 18 structures under the \(y\to-y\) light-front
  parity reflection and test the published T-odd link-reversal set.
- Justification: Direct comparison with arXiv:1612.06585 Eqs. (12)-(20)
  showed that rank-three `h1TTperp` alone omitted this epsilon rotation and
  transformed with the wrong parity sign.
- Alternatives: A transverse \(k\to-k\) check was rejected because it is not
  a complete light-front parity operation. Leaving the error hidden by the
  current zero T-odd boundary was rejected because replacement inputs would
  activate the wrong tensor.
- Classification: exact covariant/symmetry correction.
- Files/tests: `quark_correlator.py`,
  `quark_correlator_conventions.md`, `test_quark_correlator.py`.
- Evidence: all 18 parity identities and direct equation contractions pass;
  full suite 191/191; six-wave outputs regenerated.
- Revision trigger: a deliberate change of gamma-matrix, epsilon, helicity,
  or target-polarization convention.

## D-046: Mechanism interfaces replace universal nuclear multipliers

- Date: 2026-07-25
- Status: partial acceptance; fitted DPDF and off-shell tables still required
- Question: How should coherent shadowing and bound-nucleon modification
  enter without hiding them in a universal \(x\)-dependent factor?
- Adopted choice: Use replaceable diffractive and off-shell response
  interfaces. Shadowing multiplies the input by the deuteron longitudinal
  coherence form factor at \(q_L=2m_Nx\); off-shell response multiplies a
  declared average nucleon virtuality. Both act at correlator level on
  explicit spin-1 irreps.
- Justification: Leading-twist shadowing is related to nucleon diffraction
  (Frankfurt-Guzey-Strikman, arXiv:1106.2091). Deuteron global fits constrain
  virtuality-dependent bound-nucleon PDFs (Kulagin-Petti analyses,
  arXiv:1609.08463 and arXiv:2312.00809).
- Alternatives: The former Gaussian shadowing and quadratic `emc_like`
  multipliers are superseded. A direct fitted-table implementation is
  preferred but tables have not yet been vendored.
- Classification: physical composition and coherence are theory-informed;
  current default response functions are explicitly temporary model
  surrogates with 50% sensitivity ranges.
- Files/tests: `nuclear_mechanisms.py`,
  `test_nuclear_mechanisms.py`,
  `compare_b1_shadowing_to_hermes.py`.
- Revision trigger: a versioned DPDF grid, fitted Kulagin-Petti response
  table, or spin-dependent off-shell extraction.

## D-045: Quark production quadrature reference and gluon TT identifiability

- Date: 2026-07-25
- Status: quark quadrature portion superseded by D-050; gluon TT
  identifiability portion remains accepted
- Decision: Treat \(24\times16\times12\) as the present parent-quark
  reference, \(16\times12\times8\) as a candidate production rule, and
  \(8\times6\times6\) as regression-only. In the gluon TT sector expose
  \(f_{1TT}-h_{1TT}^{\perp}\) at fixed transverse momentum rather than
  inventing two separately identifiable coefficients.
- Reason: The coarse-to-medium quark shift is 24.9% in L2, whereas
  medium-to-fine is 0.462% and below 0.680% for resolved p/n terms. The
  two-dimensional TT correlator basis makes the \(f_{1TT}\) and
  \(h_{1TT}^{\perp}\) matrices equal up to sign.
- Alternatives: Retaining the coarse rule was rejected numerically.
  Separating the TT pair by a prior was rejected because it would conceal an
  exact projection degeneracy.
- Classification: numerical/model choice for quadrature; exact
  representation-theoretic statement for TT identifiability.
- Files/tests: `outputs/parent_tmds/quark_av18_{fixture,medium,fine}.csv`,
  `gtmd_convolution.py`, `test_gtmd_convolution.py`.
- Revision trigger: finer grids or other wave functions exceeding the
  documented tolerance; a new observable or operator projection that
  independently separates the TT pair.

## D-050: Six-wave parent-quark production quadrature

- Date: 2026-07-25
- Status: accepted production rule
- Question: Is the \(16\times12\times8\) internal quadrature adequate for
  production across every supported deuteron wave function?
- Decision: No. Use \(24\times16\times12\) as the minimum production
  quadrature. Retain \(16\times12\times8\) only as a diagnostic grid and
  \(32\times20\times16\) as the present independent convergence reference.
- Evidence: One-to-one comparison over 14,256 rows per wave function shows
  medium-to-fine global relative L2 errors up to 1.283%, failing the declared
  1% criterion. Fine-to-ultrafine errors are at most 0.5653% and all entries
  satisfy
  \[
  |\Delta F|\leq 2\times10^{-8}\ {\rm GeV}^{-2}
     +0.02\max(|F_{\rm fine}|,|F_{\rm ultrafine}|).
  \]
  A mixed tolerance is used because pure relative errors in nearly cancelled
  S--D interference entries are ill-conditioned; raw relative diagnostics
  remain in the report.
- Alternatives: Keeping the medium grid was rejected by the six-wave
  numerical audit. Making \(32\times20\times16\) the default was unnecessary
  after the finer-reference test and would not improve the declared accuracy
  class.
- Classification: numerical convergence choice.
- Files/tests: `scripts/audit_quark_parent_convergence.py`,
  `scripts/export_parent_derived_quark_tmds.py`,
  `outputs/parent_tmds/quark_medium_vs_fine_convergence.json`,
  `outputs/parent_tmds/quark_fine_vs_ultrafine_convergence.json`, and the
  six `quark_*_{fine,ultrafine}.csv` tables.
- Revision trigger: extending the external \(x,Q,k_T\) domain, changing the
  wave-function family/integration map, or a finer reference that violates
  either accepted tolerance.

## D-051: Portable parent-correlator persistence

- Date: 2026-07-25
- Status: accepted
- Question: How are parent objects made inspectable and independently
  reprojectable without binding the scientific record to Python pickles?
- Decision: Store every complex matrix element in a deterministic long CSV.
  Quarks retain separate vector, axial, and two transverse-operator
  projections; gluons retain the full \(3\times3\times2\times2\) tensor.
  Physical labels identify flavor, mechanism, gauge link, and kinematics.
- Justification: CSV is language-neutral and auditable. Splitting real and
  imaginary parts avoids nonportable complex-number parsing. Thirty-six
  entries per parent object preserve the complete leading-twist spin density.
- Alternatives: NPZ was rejected as the sole record because it is less
  inspectable. Reconstructing matrices from named TMDs was rejected because
  it would make the stored parent circular rather than convolution-derived.
- Classification: exact software representation of the calculated parent.
- Files/tests: `correlator_io.py`, `test_correlator_io.py`,
  `validate_serialized_parent_correlators.py`, all
  `*.correlators.csv` and `*.correlators.validation.json` production files.
- Revision trigger: storage volume requiring a columnar companion format;
  the CSV remains the portable reference unless a migration includes exact
  round-trip tests.

## D-052: Node-resolved bound-nucleon virtuality

- Date: 2026-07-25
- Status: accepted kinematics; response function remains temporary
- Question: Where should the deuteron off-shell correction enter?
- Decision: Compute
  \(v=(p_{\rm active}^2-m_N^2)/m_N^2\) at each LF spectral node with an
  on-shell spectator and physical deuteron mass. Multiply the nucleon
  correlator by \(1+v\,\delta f(z,Q)\) before its contraction with each
  SS/SD/DS/DD spectral component. Export the difference from impulse as the
  independently switchable `off_shell` parent.
- Justification: Bound-nucleon virtuality is correlated with internal
  momentum and partonic \(z=x/y\); a post-convolution mean multiplier loses
  both correlations. The resulting spectral means (-0.0369 to -0.0448)
  independently reproduce the physical scale assumed previously.
- Alternatives: The universal \(v=-0.045\) multiplier is superseded.
  Clipping \(v<-0.3\) was rejected because it would silently remove
  1.18--2.17% of model-dependent spectral weight. That tail is exposed in
  metadata instead.
- Classification: spectator-on-shell virtuality kinematics are
  model-theoretic; the current \(\delta f\) shape remains a temporary
  Kulagin-Petti-inspired model pending a versioned fitted input.
- Files/tests: `gtmd_convolution.py`, `parent_quark_tmd.py`,
  `export_parent_derived_quark_tmds.py`,
  `test_gtmd_convolution.py`, `test_parent_quark_tmd.py`,
  `quark_fine_vs_ultrafine_convergence.json`, and all production metadata.
- Validation: all six fine/ultrafine comparisons pass (worst L2 0.5662%);
  all production and ultrafine positivity/round-trip validators pass; 204
  repository tests pass.
- Revision trigger: a covariant two-body spectral function, tagged-DIS
  virtuality constraints, or a fitted off-shell response with a declared
  alternative spectator prescription.

## D-053: CJ26 fitted off-shell response

- Date: 2026-07-25
- Status: accepted production central; covariance limitation open
- Question: Which available phenomenological response should multiply the
  node-resolved virtuality?
- Decision: Use the cubic CJ26 v1 fit released in May 2026. Production takes
  the pointwise midpoint of the additive- and multiplicative-higher-twist
  coefficient sets. Uncertainty combines their central half-range with
  diagonal propagation of the larger published marginal coefficient errors.
- Justification: CJ26 incorporates the latest JLab 6 and 12 GeV data and
  explicitly fits the leading-twist off-shell deformation while varying the
  higher-twist treatment. It supersedes the qualitative KP-shaped surrogate.
- Exact inputs: additive `(-0.474, 3.9, -15.1, 16.2)` with errors
  `(0.090, 1.3, 5.2, 5.6)`; multiplicative
  `(-0.408, 5.2, -20.6, 20.5)` with errors
  `(0.088, 1.1, 4.4, 4.4)`.
- Limitations: CJ26 v1 does not release the off-shell coefficient covariance
  or separate Hessian members. Its data constrain the response only to about
  \(x=0.7\); behavior above \(x\simeq0.75\) is extrapolative. The fit is
  flavor independent and unpolarized, so applying it equally to polarized
  correlator projections remains model dependent.
- Classification: phenomenologically fitted central and marginal
  uncertainty; model-dependent spin extension.
- Files/tests: `nuclear_mechanisms.py`,
  `references/cj26_off_shell_input.md`,
  `references/arxiv_2605.31424_cj26.pdf`,
  `test_nuclear_mechanisms.py`, production metadata, and refreshed
  fine/ultrafine datasets.
- Validation: six-wave convergence passes (worst L2 0.5644%); all positivity
  and correlator round trips pass; 205 repository tests pass.
- Revision trigger: released CJ26 covariance/Hessian members,
  flavor-dependent tagged-DIS constraints, or polarized off-shell data.

## D-054: Anchored deuteron shadowing central

- Date: 2026-07-25
- Status: accepted quark normalization anchors; gluon/tensor extensions
  remain model dependent
- Question: What replaces the arbitrary power-law shadowing fraction while
  a full deuteron DPDF covariance implementation is unavailable?
- Decision: Anchor the quark shadowing fraction to the published weak-binding
  deuteron correction: 1.5% at \(x=10^{-2}\), rising linearly in
  \(\log_{10}x\) to 3% at \(x\le10^{-5}\), and falling to zero at \(x=0.1\).
  Apply the LF longitudinal coherence factor separately. Retain a 50%
  uncertainty and mark the 1.5 gluon/quark ratio and tensor response as model
  extensions.
- Justification: These anchors are direct deuteron phenomenology and agree
  with leading-twist DPDF expectations, whereas the superseded power and
  scale exponents were arbitrary. No public deuteron DPDF covariance grid
  suitable for the full flavor/spin parent was found.
- Alternatives: A generic nPDF was rejected because deuterium is normally a
  baseline rather than a fitted nuclear member. Direct H1 DPDF integration
  remains preferred once its flux, \(t\), coherence, and covariance
  conventions are implemented consistently.
- Classification: phenomenological inclusive-quark normalization;
  leading-twist mechanism; model-dependent sector/spin extensions.
- Files/tests: `nuclear_mechanisms.py`,
  `refresh_quark_nuclear_corrections.py`,
  `test_nuclear_mechanisms.py`, production metadata and parent tables.
- Validation: exact anchor tests, six-wave convergence, positivity,
  mechanism reconstruction, and parent round trips pass; 206 tests pass.
- Revision trigger: a versioned H1/ZEUS DPDF adapter with deuteron coherence
  integration and uncertainty members, or direct deuteron small-x data.

## D-055: Source-required mesonic and non-nucleonic components

- Date: 2026-07-25
- Status: interface accepted; physical inputs unresolved
- Question: Should missing meson-exchange or hidden-color/six-quark dynamics
  be represented by an arbitrary ansatz or omitted silently?
- Decision: Neither. Export explicit `meson_exchange` and `non_nucleonic`
  zero parent matrices in the declared nucleonic baseline, with provenance
  stating that zero means “inactive/unresolved,” not physical absence.
  Activation requires `AdditionalNuclearComponentInput` with a source,
  evidence class, mechanism, validity domain, and uncertainty.
- Justification: This keeps mechanism bookkeeping and total reconstruction
  complete without inventing a universal shape or allowing a missing sector
  to disappear from outputs and handoffs.
- Alternatives: Arbitrary percent-level rescalings were rejected. Omitting
  the rows was rejected because downstream users could mistake absence for
  implementation.
- Classification: exact software/provenance contract; unresolved physical
  amplitudes.
- Files/tests: `nuclear_mechanisms.py`,
  `refresh_quark_nuclear_corrections.py`,
  `validate_parent_derived_quark_tmds.py`,
  `test_nuclear_mechanisms.py`, all refreshed parent/projection tables.
- Validation: source-required activation and out-of-domain null tests pass;
  all six production tables pass positivity/reconstruction/round trips;
  207 repository tests pass.
- Revision trigger: a versioned deuteron pion/meson splitting function plus
  meson TMD/PDF, or a constrained non-nucleonic probability and spin
  correlator.

## D-056: Controlled charge-symmetry-breaking interface and exact limit

- Date: 2026-07-25
- Status: interface and limiting tests accepted; numerical QED/CSB input
  unresolved
- Question: How can physical charge-symmetry breaking be added without
  collapsing proton/neutron flavor structure or silently treating exact
  isospin as physical truth?
- Decision: Add `ChargeSymmetryBreakingInput`, whose response is resolved by
  nucleon, PDG flavor, named nucleon TMD, \(x\), and \(Q\), and is applied as
  an amplitude correction only inside its declared validity domain.
  Production explicitly configures the exact \(m_u=m_d\), QED-off limit.
  Store the CSB provenance independently from each underlying PDF/TMD
  provenance. Do not infer transverse-width CSB from an amplitude input.
- Justification: Exact charge symmetry is a controlled QCD limit, not an
  empirical statement. A separate response preserves the independently
  assembled proton and neutron parents and allows future QED-evolved or
  fitted CSV inputs without rewriting the correlator or nuclear convolution.
- Alternatives: An arbitrary percent-level u/d rescaling was rejected.
  Folding CSB into neutron PDF mapping was rejected because it would obscure
  provenance and make the exact limit difficult to audit.
- Classification: exact symmetry limit and software contract; physical
  QED/CSB amplitude remains phenomenological/unresolved.
- Files/tests: `nucleon_inputs.py`, `nucleon_quark_correlator.py`,
  `export_parent_derived_quark_tmds.py`, `test_nucleon_inputs.py`.
- Validation: exact isospin inclusive relation, synthetic nonzero
  flavor-resolved breaking, validity-domain deactivation, hidden-nonzero
  exact-limit rejection, and complete correlator positivity all pass; 210
  repository tests pass.
- Revision trigger: a versioned QED-evolved proton/neutron PDF/TMD input or
  fitted flavor-resolved CSV distribution with uncertainty members.

## D-057: H1-DPDF/FGS central coherent shadowing

- Date: 2026-07-25
- Status: unpolarized central accepted; statistical and polarized/tensor
  covariance partial
- Question: What replaces the inclusive anchored interpolation with a
  mechanism-level diffractive calculation?
- Decision: Vendor the official H1 2007 Jets DPDF v1.0 singlet/gluon grids
  and flux routines and implement the FGS deuteron double-scattering
  integral. Reconstruct the differential \(t\) flux, include the explicit
  \(16\pi\) diffraction-to-rescattering conversion and real-part factor, use
  wave-specific LF body form factors, and retain the FGS quark/gluon
  \(x_{\mathbb P}\) cutoffs. Use named \(\pm20\%\) DPDF normalization and
  \(\pm1.1\ {\rm GeV}^{-2}\) slope scenarios; renormalize slope variations to
  the H1 flux convention.
- Justification: This maps every factor to a released DPDF artifact or the
  leading-twist nuclear-shadowing equation. The independent AV18/CT18 result
  at \(x=10^{-2},Q=5\) GeV is 1.54%, reproducing the deuteron benchmark. The
  missing \(16\pi\) factor initially produced 0.03%; the benchmark and the
  primary FGS convention identified and closed that normalization defect.
- Alternatives: The prior log-linear inclusive anchor remains a comparison
  model but is no longer production central. A generic heavy-nucleus nPDF
  was rejected for deuterium.
- Classification: phenomenological H1 DPDF input and exact implemented
  convention; scenario uncertainty; polarized/tensor extension unresolved.
- Files/tests: `diffractive_shadowing.py`, `nuclear_mechanisms.py`, both
  quark export/refresh scripts, official files under
  `data/raw/h1_2007_dpdf`, `h1_dpdf_shadowing_input.md`,
  `test_diffractive_shadowing.py`.
- Validation: official grid shape/clamping, flux normalization, fixed
  full-integral fixture, domain cutoffs, signed NLO grid retention, and named
  members pass. All 12 refreshed datasets pass mechanism, positivity,
  parent round-trip, and convergence audits; 214 tests pass.
- Revision trigger: released H1/ZEUS eigenvector grids or a newer DPDF
  ensemble, measured polarized diffraction, or wave-specific three-
  dimensional form-factor improvements.

## D-058: H1 shadowing responses remain named scenarios

- Date: 2026-07-25
- Status: accepted
- Question: Can the available H1 normalization and flux-slope variations be
  represented as a statistical covariance?
- Decision: Export central and four named responses coherently across wave
  function, flavor, \(x\), and \(Q\), together with their envelope. Do not
  construct a covariance matrix: the official v1.0 artifacts contain no
  eigenvectors or replicas. Mark \(x<10^{-4}\) rows as diagnostic
  extrapolations using the official beta-boundary clamp.
- Justification: A shared member identity supplies the physically meaningful
  correlation rule that is actually known. Turning five hand-defined
  scenarios into a covariance would invent statistical information.
- Alternatives: A diagonal covariance and a sample covariance over the five
  scenarios were rejected because neither has a probability measure supplied
  by H1.
- Classification: phenomenological systematic scenarios; exact bookkeeping
  constraint; statistical covariance unresolved.
- Files/tests: `export_h1_shadowing_scenarios.py`,
  `outputs/parent_tmds/shadowing/h1_fgs_scenarios.csv`, its envelope and
  metadata, and `test_diffractive_shadowing.py`.
- Validation: all member identities share the same grid; the production
  integral converges at better than \(2\times10^{-4}\) from 32 to 64
  quadrature points.
- Revision trigger: a released H1/ZEUS DPDF replica or Hessian ensemble.

## D-059: BPV20 is the fitted quark Sivers boundary

- Date: 2026-07-25
- Status: accepted and propagated at fitted-replica scope
- Question: What replaces the exact-zero one-body quark Sivers boundary?
- Decision: Use the public BPV20 N3LO extraction and all 500 released Monte
  Carlo replicas. Evaluate the optimal-zeta boundary and its \(Q\) evolution
  with the exact vendored arTeMiDe v2.05 implementation. Treat SIDIS as the
  future-link reference, reverse the sign for past links, and construct the
  neutron by the explicit charge-symmetry map.
- Justification: BPV20 is a global SIDIS, DY, and electroweak fit with TMD
  evolution and direct public replicas. The independent Python FNP expression
  agrees with a standalone Fortran fixture and arTeMiDe at machine precision.
  At \(x=0.1,b=1\) GeV\(^{-1}\), distinct u and d boundaries are retained.
- Alternatives: An arbitrary Gaussian Sivers ansatz and hidden complex phase
  were rejected. The newer 2024 extraction was not used because its numerical
  replicas were not publicly released with the paper.
- Classification: phenomenology-constrained boundary and Monte Carlo
  uncertainty; exact implemented process-sign rule; charge-symmetry limit.
- Positivity: BPV20 explicitly documents violations of the parton-model
  inequality. Constituent proton/neutron eigenvalue tensions are therefore
  reported rather than clipped. Physical deuteron impulse and corrected
  totals remain mandatory positivity gates and pass.
- Files/tests: `bpv20_sivers.py`, `nucleon_inputs.py`,
  `nucleon_quark_correlator.py`, both BPV20 preparation/probe tools,
  `refresh_bpv20_sivers_parents.py`, `generate_bpv20_replica_grid.py`,
  `propagate_bpv20_sivers_replicas.py`, `build_bpv20_sivers_atlas.py`,
  `test_bpv20_sivers.py`, and all 12 refreshed fine/ultrafine quark parent
  families.
- Validation: 500 contiguous replicas parsed; boundary fixture, exact
  evolution fixture, flavor/isospin relations, domain cutoff, future/past
  reversal, 24 projection/parent validations, and 220 repository tests pass.
  Fine/ultrafine worst relative L2 is 0.56436%; the mixed absolute floor is
  \(5\times10^{-7}\) GeV\(^{-2}\) for tiny off-shell Sivers differences.
  The 500-member cache preserves member identity across flavor, x, k, and
  wave functions. A seeded 96-point exact-reference audit has 0.308% p95 and
  1.776% maximum sampled interpolation error. Future/past quantile endpoints
  obey the exact reversed-sign ordering. All 223 repository tests pass.
- Numerical caveat: released arTeMiDe emits native Ogata convergence warnings
  for a small number of slow-decaying replica/low-k evaluations and produces
  heavy outliers. Values are retained rather than clipped; the primary fit
  interval is therefore the robust 16th-84th percentile band, while means and
  standard deviations are diagnostic.
- Revision trigger: a newer public fitted ensemble with reproducible
  evolution, or data requiring a non-charge-symmetric neutron input.

## D-060: do not manufacture a standalone BPV20 TMD scale band

- Date: 2026-07-25
- Status: accepted
- Question: Can arTeMiDe c1-c4 factors provide a scale/profile band for the
  released BPV20 standalone momentum-space TMD?
- Decision: No. Reject non-unit factors in the standalone BPV20 adapter.
  Apply hard-scale variations only in a process-level observable, where c2
  and the hard factor exist. Do not vary fit-defining nonperturbative profile
  parameters independently of their correlated fitted replicas.
- Justification: With the released optimal-TMD constants, arTeMiDe explicitly
  reports c1 and c3 as nonexistent, ignores c4 for Sivers, and routes c2 to
  DY/SIDIS cross sections rather than the standalone TMD. A non-unit c1 test
  returned the nominal value exactly. Treating that as uncertainty would be
  false precision and duplicate curves.
- Alternatives: a seven-point c1/c3 envelope was attempted diagnostically and
  rejected after the implementation reported both variations as senseless.
  Arbitrary b-star/profile changes without refitting were rejected because
  they break the meaning of the BPV20 replica distribution.
- Classification: exact software/scheme constraint; process-level perturbative
  uncertainty remains unresolved.
- Files/tests: `bpv20_sivers.py`, `test_bpv20_sivers.py`, WP6 roadmap.
- Revision trigger: a process-level BPV20 observable implementation or an
  updated release with active resummation-scale members.

## D-061: BPV20 member positivity is a reported scheme diagnostic

- Date: 2026-07-25
- Status: accepted
- Question: Should propagated BPV20 replicas that violate the complete
  tree-level spin-1 joint-density PSD test be clipped or discarded?
- Decision: No. Evaluate and retain every result, publish the member-level
  diagnostic, and keep the official 16th--84th percentile fit interval.
  Do not present the compatible subset as a BPV20 confidence interval.
- Justification: 296/500 members develop a negative eigenvalue somewhere in
  the six-wave, two-link, four-flavor impulse/model scan; the worst is
  -0.0470732. BPV20 explicitly documents parton-model Sivers-bound
  violations, while positivity of soft-subtracted evolved TMDs is not a
  scheme-independent probability theorem beyond tree level.
- Classification: exact numerical diagnostic; factorization-scheme
  applicability limitation.
- Files/tests: `uncertainty_validation.py`,
  `validate_bpv20_replica_positivity.py`,
  `bpv20_replica_positivity_members.csv`, and `test_quark_correlator.py`.
- Revision trigger: a common-order probability-preserving TMD scheme or a
  refit imposing a justified positivity condition.

## D-062: retain the official JAMDiFF member identities

- Date: 2026-07-25
- Status: accepted; h1 and correlated WW h1Lperp propagated
- Question: Can the pointwise JAMDiFF mean/std table be replaced by its
  released correlated ensemble?
- Decision: Yes. Vendor upstream commit
  `2d601943b003ab03d261d492b565c1ebf54d07cc`; treat LHAPDF member 0 as the
  central and members 1--968 as the physical replicas. Apply the documented
  sea endpoint and CT18+BDSSV composed-TMD Soffer projection to each member
  before the LF convolution.
- Justification: member 0 reproduces the compact collaboration mean, while
  the population standard deviation of members 1--968 reproduces its compact
  std. The previous “969 replicas” wording incorrectly counted the central.
- Classification: phenomenological Monte Carlo ensemble plus an explicit
  model-dependent compatibility projection.
- Files/tests: `transversity.py`, `generate_jamdiff_replica_grid.py`,
  `propagate_jamdiff_transversity_replicas.py`,
  `build_jamdiff_transversity_atlas.py`, `test_transversity.py`.
- Validation: 968 stable IDs; cache audit p95 0.149% and maximum 0.236%;
  member-0 nuclear h1 roundtrip below 0.04% and WW h1Lperp roundtrip below
  0.4% of output scale; 225 tests pass.
- Revision trigger: a common-fit \(f_1,g_1,h_1\) TMD ensemble or updated
  JAMDiFF release.

## D-063: use mixed tensor tolerances at collinear zeros

- Date: 2026-07-25
- Status: accepted
- Question: How should the parent/independent-smearing \(f_{1LL}\) reduction
  be tested across wave functions and kinematics where the D-state tensor
  signal can approach zero?
- Decision: Require at every point either relative residual below \(10^{-9}\)
  or absolute residual below \(10^{-12}\ {\rm GeV}^{-2}\), while retaining a
  relative-only \(10^{-10}\) requirement for nonzero unpolarized \(f_1\).
- Justification: A relative-only tensor criterion amplified floating-point
  differences near a physical cancellation to \(7.19\times10^{-9}\), while
  the full audit retains machine-level unpolarized agreement and negligible
  forbidden-rank leakage. The mixed norm tests the correlator rather than
  division by a near-zero observable.
- Alternatives: weakening the global relative threshold was rejected;
  omitting tensor-zero regions was rejected.
- Classification: numerical validation convention grounded in the physical
  tensor cancellation.
- Files/tests: `audit_parent_collinear_reductions.py` and
  `parent_collinear_reductions.validation.json`.
- Revision trigger: higher-precision arithmetic or a normalized matrix norm
  adopted uniformly across parent validation.

## D-064: start quark matching with explicit rank-zero LO support

- Date: 2026-07-25
- Status: accepted; intermediate, not production complete
- Question: Can the existing gluon CSS implementation be generalized by
  treating every quark TMD as the same scalar?
- Decision: No. Implement only the T-even rank-zero \(f_1,g_1,h_1\) boundary
  first, with its exact flavor-dependent Gaussian Fourier transform and
  quark coefficients \(A_q^{(1)}=C_F,\ B_q^{(1)}=-3C_F/2\). Reject all
  unsupported tensor ranks and fit-native momentum inputs.
- Justification: the Sudakov kernel is spin independent at this accuracy, but
  tensor-rank Fourier adapters, small-b matching, and T-odd fit schemes are
  not interchangeable. Explicit rejection prevents the gluon-only shortcut
  and prevents a rank-zero transform from silently changing a worm gear or
  pretzelosity convention.
- Alternatives: copying the gluon kernel and coefficients was rejected;
  converting BPV20 out of its released optimal-TMD scheme was rejected.
- Classification: exact tensor-convention guard plus model-dependent LO
  perturbative boundary.
- Files/tests: `quark_tmd_matching.py`, `tmd_evolution.py`, and
  `test_quark_tmd_matching.py`.
- Revision trigger: order-consistent coefficient functions and validated
  tensor-rank/fit-native adapters.

## D-065: enforce the common fitted-input scale domain

- Date: 2026-07-25
- Status: accepted
- Question: May the canonical quark \(b_*\) scale fall below the lowest scale
  of a constituent fitted input?
- Decision: No. Set the default quark floor to
  \(\sqrt{2}\) GeV, matching the lowest JAMDiFF grid point
  \(Q^2=2\ {\rm GeV}^2\).
- Justification: the first physical LF-parent audit reached 1.389 GeV at
  large \(b_T\), below JAMDiFF's declared domain. Extrapolating transversity
  there would silently invent fitted information. The composed boundary must
  respect the intersection of its inputs' validity domains.
- Alternatives: extrapolating the JAMDiFF interpolation and dropping
  transversity at those nodes were rejected.
- Classification: exact source-domain constraint.
- Files/tests: `tmd_evolution.py`, `test_quark_tmd_matching.py`,
  `audit_evolved_quark_parent_connection.py`.
- Revision trigger: an evolved transversity input valid at a lower scale.

## D-066: evolve rank-one quark correlator coefficients, not scalar labels

- Date: 2026-07-25
- Status: accepted
- Question: How should the WW \(g_{1T}\) and \(h_{1L}^{\perp}\) inputs enter
  b-space evolution?
- Decision: Fourier transform the physical vector
  \(k_i F(k)/M\) to \(i\hat b_i R(b)\), multiply \(R(b)\) by the common
  quark Sudakov, and invert with
  \(F(k)=M[2\pi k]^{-1}\int b\,db\,J_1(bk)R(b)\), using its analytic
  \(k=0\) limit.
- Justification: a \(J_0\) scalar transform would erase the tensor rank and
  produce an inconsistent parent correlator. The analytic zero-evolution
  Gaussian round trip passes for both rank-one structures.
- Alternatives: rank-zero relabeling was rejected; leaving WW functions
  permanently unevolved was retained only as an explicit diagnostic switch.
- Classification: exact Fourier/tensor convention; WW collinear boundary
  remains model dependent.
- Files/tests: `evolved_quark_model.py`, `test_quark_tmd_matching.py`,
  `audit_rank_one_quark_evolution.py`.
- Revision trigger: fitted genuine twist-3 inputs or a fit-native rank-one
  TMD evolution implementation.

## D-067: separate perturbative-zero and bound-state pretzelosity

- Date: 2026-07-25
- Status: accepted
- Question: Should pretzelosity be generated by copying the transversity
  small-b boundary?
- Decision: No. Keep the perturbative small-b central zero and provide signed
  nonperturbative Gaussian sensitivity members at \(\pm0.25\) of
  \(|h_{1T}^{\perp(1)}|\le(f_1-g_1)/2\). Evolve the rank-two directional
  coefficient and invert it with \(J_2\).
- Justification: arXiv:1808.10560 finds vanishing perturbative matching for a
  single massless quark and relates nonzero hadronic pretzelosity to
  quark-gluon/bound-state structure. Copying \(h_1\) would misstate the OPE.
- Alternatives: permanent zero-only physics was rejected as incomplete;
  a transversity-proportional central was rejected as field-theoretically
  unjustified.
- Classification: exact perturbative/tensor constraint plus explicitly
  model-dependent large-b sensitivity.
- Files/tests: `nucleon_inputs.py`, `evolved_quark_model.py`,
  `pretzelosity_input.md`, `audit_pretzelosity_scenarios.py`,
  `test_nucleon_inputs.py`, `test_quark_tmd_matching.py`.
- Revision trigger: a process-compatible fitted or lattice pretzelosity
  input with quantified covariance.

## D-068: cache evolved nucleon physics before nuclear composition

- Date: 2026-07-25
- Status: accepted
- Question: At what layer should the expensive evolved quark calculation be
  persisted for multi-wave production?
- Decision: Cache the proton/neutron, flavor-resolved momentum-space nucleon
  TMDs after rank-aware evolution but before LF nuclear convolution.
- Justification: all six wave functions share the same nucleon boundary and
  differ through their spectral kernels. Persisting parent outputs would
  duplicate nucleon physics and obstruct replacement; recomputing WW/JAMDiFF
  integrals at every LF node is unnecessary and slow.
- Validation: the first 117-node x grid failed the direct sea
  \(h_{1L}^{\perp}\) test by 5.7%. Refining to 274 nodes reduces all resolved
  direct comparisons below 0.98%; no tolerance was weakened.
- Classification: numerical architecture with physics-preserving module
  boundary.
- Files/tests: `evolved_quark_grid.py`, `generate_evolved_quark_grid.py`,
  `validate_evolved_quark_grid.py`, `export_evolved_quark_parent_scenarios.py`,
  and `test_quark_tmd_matching.py`.
- Revision trigger: multi-Q production, fit-native evolved grids, or a faster
  validated on-demand backend.

## D-069: refuse high-qT W-only predictions without a sourced Y term

- Date: 2026-07-25
- Status: accepted
- Question: May the finite-b W transform be extrapolated and presented as a
  full transverse-momentum prediction?
- Decision: No. Declare a low-qT domain
  \(q_T/Q\le0.25,\ q_T\le1\) GeV by default. Outside it, evaluation requires
  a process/order/subtraction-labeled fixed-order
  \(Y=\mathrm{FO}-\mathrm{asymptotic}\) remainder.
- Justification: the W term is the resummed low-qT contribution and cannot
  satisfy the full collinear marginal or high-qT fixed-order limit by itself.
  Inventing a generic Y term would hide process-specific hard physics.
- Alternatives: renormalizing the W tail and silently extrapolating it were
  rejected.
- Classification: factorization-domain guard; the default numerical boundary
  is configurable and model dependent.
- Files/tests: `w_y_matching.py`, `test_w_y_matching.py`.
- Revision trigger: implemented SIDIS/DY hard factors and sourced fixed-order
  asymptotic subtraction at a declared order.

## D-070: require numerical SIDIS W/asymptotic overlap

- Date: 2026-07-25
- Status: accepted
- Question: Is the formal availability of
  \(Y=\mathrm{FO}-\mathrm{ASY}\) sufficient to enable high-qT matching?
- Decision: No. Require at least three contiguous, same-sign W/ASY points
  within 25% relative difference in \(0.1\le q_T/Q\le1\), with configurable
  thresholds recorded in the evidence.
- Justification: arXiv:1412.1383 explicitly demonstrates SIDIS configurations
  where W and ASY change sign at different momenta and standard W+Y never
  approaches NLO. The effect is especially relevant at few-GeV hard scales.
- Alternatives: formal additive matching without an overlap test was
  rejected; declaring all \(Q=5\) kinematics invalid without a calculation
  was also rejected.
- Classification: numerical factorization-applicability criterion informed
  by primary phenomenology; thresholds are configurable.
- Files/tests: `w_y_matching.py`, `test_w_y_matching.py`,
  `sidis_matching.md`.
- Revision trigger: a process-specific profile-matching prescription with a
  different validated overlap criterion.

## D-071: do not use APFEL++ collinear SIDIS operators as a Y term

- Date: 2026-07-25
- Status: accepted
- Question: Can APFEL++ or the vendored arTeMiDe provide the missing
  fixed-order SIDIS remainder for high-\(q_T\) matching?
- Decision: No at their audited scope. APFEL++ `SIDIS.h` provides collinear
  \(x,z\) coefficient operators and its TMD layer provides the resummed W
  term; arTeMiDe `TMDX_SIDIS` also provides the TMD W term. Neither supplies
  a \(q_T\)-differential FO result and its same-order ASY expansion.
- Justification: substituting a transverse-momentum-integrated coefficient
  function for FO or subtracting an expansion from a different scheme would
  not define \(Y=\mathrm{FO}-\mathrm{ASY}\).
- Alternatives considered: installing APFEL++ despite the API mismatch and
  treating arTeMiDe W as fixed order were rejected.
- Classification: exact factorization-interface compatibility decision based
  on source inspection.
- Files/tests: `references/sidis_matching.md`, `w_y_matching.py`.
- Revision trigger: a new upstream qT-differential SIDIS FO/ASY API or a
  separately validated backend at a declared order.

## D-072: isolate numerical neutron CSB with paired MSHT20 QED ratios

- Date: 2026-07-25
- Status: accepted
- Question: How should public QED-evolved neutron PDFs enter without replacing
  CT18 by an unrelated baseline fit difference?
- Decision: For neutron \(f_1\), multiply the existing baseline by the ratio
  \(q_n^{MSHT20QED}/q_{p,\mathrm{isospin\ partner}}^{MSHT20QED}\). Preserve
  paired proton/neutron identity through all 38 Hessian eigenvector pairs.
  Apply no numerical CSB to other TMDs or transverse widths.
- Justification: the within-family ratio isolates the published QED-driven
  isospin violation, while a direct MSHT/CT18 ratio would mix CSB with global
  fit differences. The source supplies unpolarized PDFs, not polarized TMD
  CSB.
- Alternatives considered: changing the full baseline to MSHT20 QED and
  applying the unpolarized ratio universally to every TMD were rejected.
- Classification: phenomenology-constrained unpolarized amplitude input;
  polarized and transverse-profile CSB remain unresolved.
- Files/tests: `csb_inputs.py`, `nucleon_inputs.py`,
  `audit_msht20qed_csb.py`, `test_csb_inputs.py`,
  `msht20qed_csb_input.md`.
- Revision trigger: a joint QED global fit aligned with the full baseline,
  polarized QED evolution, lattice CSV distributions, or fitted transverse
  CSB information.

## D-073: propagate f1-only CSB as a vector-projection ensemble

- Date: 2026-07-25
- Status: accepted
- Question: How can all 77 MSHT20 QED members reach the LF parent without 76
  redundant full spin-correlator convolutions?
- Decision: Use the exact linear map from the multiplicative neutron \(f_1\)
  shift to the identity term of the nucleon vector projection. Share LF
  nodes, evolved baseline \(f_1\), and spectral contractions across members,
  then project every member's spin-1 correlator and form paired Hessian bands.
- Justification: the sourced mechanism changes no axial or transverse quark
  projection. Linearity makes this construction algebraically identical to
  independent full convolutions and preserves member identity.
- Alternatives considered: pointwise independent uncertainty bars and 76
  duplicate full convolutions were rejected.
- Classification: exact computational factorization of a
  phenomenology-constrained mechanism ensemble.
- Files/tests: `export_msht20qed_csb_parent_hessian.py`,
  `test_csb_inputs.py`; independent-central agreement is
  \(2.01\times10^{-13}\) GeV\(^{-2}\).
- Revision trigger: a future CSB input affecting axial, transverse, T-odd,
  or transverse-width structures.

## D-074: implement the Miller tensor Sullivan term without inventing a pion TMD

- Date: 2026-07-25
- Status: accepted
- Question: How should a sourced numerical pion contribution enter the
  spin-1 correlator, and what is the central JAM21 pion PDF member?
- Decision: Evaluate Miller's published AV18 tensor pion distribution and
  install it as a separate pure-tensor `meson_exchange` parent. Convolve it
  with the isoscalar average of every one of the 786 JAM21 pion replicas;
  use their ensemble mean and sample standard deviation because every
  released member, including member 0, is labeled `replica`. Expose the
  \(M_A=1.03\pm0.04\) GeV variation and exact zero-strength limit. Do not
  manufacture a transverse profile or spin-averaged pion distribution.
- Justification: the source determines \(\delta f_\pi(y)\) and its collinear
  \(b_1\) convolution, not a complete pion TMD. The pure-tensor embedding
  preserves exactly what is calculated while preventing an unsupported
  universal ansatz from becoming production physics.
- Alternatives considered: treating JAM member 0 as central, assigning a
  Gaussian pion width, or interpreting \(\delta f_\pi\) as the full
  spin-averaged pion excess were rejected.
- Classification: phenomenological/model-dependent nuclear input with exact
  spin-1 correlator bookkeeping and explicit numerical uncertainty ensemble.
- Files/tests: `pion_exchange.py`, `test_pion_exchange.py`,
  `compare_b1_pion_exchange_to_hermes.py`,
  `miller_pion_exchange_input.md`; focused suite 16/16 passes and doubled
  quadrature differs by at most \(2.61\times10^{-8}\).
- Revision trigger: a joint pion PDF fit with a defined central estimator, a
  sourced deuteron pion TMD/GTMD, or a spin-averaged splitting distribution
  supporting complete momentum accounting.

## D-075: keep Miller six-quark b1 at observable level

- Date: 2026-07-25
- Status: accepted
- Question: Can Miller's hidden-color equation be installed as a
  flavor-resolved non-nucleonic TMD parent?
- Decision: Implement and validate the charge-weighted \(b_1\) equation,
  support, parameter variants, zero switch, and tensor sum rule, but do not
  infer a flavor decomposition absent from the source.
- Justification: the source fixes an \(s\)-\(d\) interference observable and
  fits \(P_{6q}=0.0015\) at one HERMES bin. Flavor or \(k_T\) extension would
  be a new assumption rather than a published projection.
- Alternatives considered: equal-flavor and valence-counting allocations
  were rejected as underdetermined.
- Classification: explicitly model-dependent and one-bin-calibrated
  observable scenario.
- Files/tests: `hidden_color.py`, `test_hidden_color.py`,
  `miller_hidden_color_input.md`; four focused tests pass and published table
  values agree within printed rounding.
- Revision trigger: a six-quark LF wave function or correlator calculation
  with explicit flavor, helicity, OAM, and transverse dependence.

## D-076: derive the pion spin average from the same helicity-resolved source

- Date: 2026-07-25
- Status: accepted
- Question: Should spin-averaged pion momentum accounting use an unrelated
  parametrization or the helicity projections already underlying the tensor
  Sullivan term?
- Decision: Algebraically average Miller's published \(F_0,F_{\pm1}\)
  projections and validate the simplified result against independent direct
  helicity integrals. Interpret the first radial factor in the printed
  \(F_0^{ww}\) line as \(I_{ww0}\), not the repeated \(I_{ww2}\), because
  that is required by the channel labels and subsequent tensor identity.
  Refuse correlator activation by default until NN-sector momentum
  compensation is explicitly acknowledged.
- Justification: this preserves one wave function, regulator, and spin
  algebra across unpolarized and tensor sectors. The connected pion carries
  0.00410205 of deuteron plus momentum, so naive addition to a unit NN parent
  violates the sum rule.
- Alternatives considered: Kamano-Lee's three-body expression requires
  unpublished fitted form-factor output and extensive spinor integration;
  a generic pion-excess curve or universal Gaussian/rescaling was rejected.
- Classification: model-derived collinear spin projection plus exact
  bookkeeping safeguard; the NN normalization counterterm remains unresolved.
- Files/tests: `pion_exchange.py`, `test_pion_exchange.py`,
  `audit_spin_averaged_pion.py`; direct helicity reconstruction, moments,
  refusal gate, correlator identity, 786 replicas, and quadrature convergence.
- Revision trigger: a coupled NN/NNπ light-front calculation or a fitted pion
  TMD/GTMD with consistent Fock-sector normalization.

## D-077: compose pion-internal and nuclear transverse motion in b space

- Date: 2026-07-25
- Status: accepted boundary scenario
- Question: Can a fitted pion TMD profile be applied directly to the
  deuteron pion contribution?
- Decision: No. Use the 100-replica Vpion19 intrinsic factor for motion
  inside the pion, retain the Miller Sullivan \(q_T\) kernel, and compose
  momenta through \(k_{T,D}=k_{T,q/\pi}+zq_{T,\pi/D}\), yielding
  \(J_0(zbq_T)\). Require exact \(b=0\) reduction.
- Justification: the two transverse momenta have different physical origins
  and convolution kinematics. A single width would erase nuclear recoil.
- Alternatives considered: a universal Gaussian and using Vpion19 as the
  complete deuteron TMD were rejected. The JAM 2023 extraction was audited,
  but its replica parameters/grids are not published in the paper.
- Classification: phenomenology-constrained intrinsic boundary transferred
  from JAM18/BSV19 to a JAM21 scenario, plus model-derived nuclear recoil.
- Files/tests: `pion_tmd.py`, `test_pion_tmd.py`,
  `pion_transverse_boundary.md`; central/replica parsing, normalization,
  recoil, full collinear reductions, and the explicitly non-production
  one-loop rank-zero evolution route pass.
- Revision trigger: a public JAM 2023 TMD ensemble or joint nuclear-pion TMD
  fit in the project's evolution scheme.

## D-078: normalize NN and NNπ Fock sectors without dropping NNπ nucleons

- Date: 2026-07-25
- Status: accepted with temporary closure model
- Question: How should pion momentum be compensated in the nucleonic parent?
- Decision: Use \(Z=1+N_\pi\), retain NN nucleon, NNπ nucleon, and pion
  momentum entries, and normalize every pion spin projection by \(1/Z\).
  Use an unchanged-shape NN correlator for the minimal NNπ-nucleon closure,
  with 100% model uncertainty.
- Justification: subtracting the pion from the NN probability omits the two
  nucleons inside the NNπ sector. The three-component ledger closes exactly
  while keeping the unresolved spectral shape visible.
- Alternatives considered: ignoring \(Z\), removing the entire NNπ
  probability from nucleons, and rescaling only \(f_1\) were rejected.
- Classification: exact Fock normalization and momentum algebra plus a
  temporary model-dependent NNπ-nucleon shape.
- Files/tests: `pion_exchange.py`, `test_pion_exchange.py`,
  `compare_b1_pion_exchange_to_hermes.py`; probability/momentum closure,
  common spin normalization, and identifiable pion/counterterm matrices pass.
- Revision trigger: a coupled NN/NNπ light-front spectral function with
  explicit nucleon spin, flavor, virtuality, and transverse distributions.

## D-079: do not relabel the 2026 effective cluster LFWF as a quantified hidden-color parent

- Date: 2026-07-25
- Status: accepted
- Question: Can arXiv:2507.09886 replace the observable-only six-quark term?
- Decision: Retain it as a future deep-binding cluster sensitivity model,
  not a production hidden-color parent. Prefer machine-readable BLFQ
  six-quark amplitudes from arXiv:2503.21371/2505.12889 when available.
- Justification: the paper explicitly cannot identify singlet–singlet versus
  octet–octet proportions, uses pointlike \(L=0\) clusters, lacks evolution,
  and obtains approximately 200 MeV rather than physical deuteron binding.
- Alternatives considered: assigning the asymptotic 80% octet fraction or
  treating the fitted cluster LFWF as physical-deuteron hidden color were
  rejected.
- Classification: source audit and production refusal; the equations remain
  suitable for a named model-comparison implementation.
- Files/tests: `hidden_color_light_front_audit.md`; source equations and
  limitations checked against the official arXiv source.
- Revision trigger: released helicity-resolved color-sector amplitudes or a
  reproducible BLFQ Hamiltonian/truncation package.

## D-080: require a momentum-dependent spin vertex for cluster tensor structure

- Date: 2026-07-25
- Status: accepted implementation gate
- Question: Is a canonical spin triplet followed only by constituent Melosh
  rotations sufficient for the effective-cluster \(f_{1LL}\)?
- Decision: No. Retain that construction only as an exact zero-tensor
  diagnostic. Production comparison to arXiv:2507.09886 requires its
  momentum-dependent \(\bar v\gamma\!\cdot\!\epsilon^\Lambda u\) vertex,
  independently normalized longitudinal/transverse states, and correlator
  projections.
- Justification: unitary one-body rotations preserve the pointwise
  helicity-summed scalar probability for every target helicity, forcing
  \(f_{1LL}=0\). The source reports nonzero tensor structure.
- Alternatives considered: accepting zero tensor structure or inserting a
  target-helicity normalization by hand were rejected.
- Classification: exact representation-theoretic limiting case and
  validation gate; the vector-current realization remains partial.
- Files/tests: `hidden_color_cluster_lfwf.py`,
  `test_hidden_color_cluster_lfwf.py`; seven focused tests pass.
- Revision trigger: a source-equivalent vector-current implementation
  benchmarked against published wave-function and LMDF curves.

## D-081: accept the effective-cluster vector vertex as a validated comparison parent

- Date: 2026-07-25
- Status: accepted with production gate
- Question: Does the explicit vector-current implementation reproduce the
  source sufficiently to retain as a controlled model scenario?
- Decision: Yes for cluster-level comparison, no for production
  flavor-resolved hidden color. Use incoming \(\epsilon^{\Lambda *}\),
  independently normalize longitudinal/transverse states, and propagate the
  source's quoted parameter errors only as one-at-a-time sensitivity.
- Justification: Clifford, Dirac, polarization, parity, azimuthal, norm, and
  tensor-sum tests pass. Direct official-PDF vector-path residuals are below
  0.012 for \(zf_1,zg_{1L}\) and 0.00165 for \(zf_{1LL}\).
- Alternatives considered: post-hoc helicity sign reversal, treating the
  parameter envelope as a fit confidence interval, or assigning arbitrary
  cluster flavors were rejected.
- Classification: source-reproducing model-dependent cluster parent with
  exact algebraic tests and an explicit flavor/evolution production gate.
- Files/tests: `hidden_color_cluster_lfwf.py`,
  `test_hidden_color_cluster_lfwf.py`,
  `extract_kaur_cluster_lmdf_benchmark.py`,
  `compare_kaur_cluster_lmdfs.py`,
  `kaur_cluster_lfwf_implementation.md`.
- Revision trigger: source fit covariance, flavor-resolved cluster parton
  input, finite-size/OAM extension, or color-resolved BLFQ amplitudes.

## D-082: use physical sector prefactors in cluster structure functions

- Date: 2026-07-25
- Status: accepted
- Question: Should the source's compact \(x\sum e_q^2\mathcal F_q^D\)
  expression be applied identically to \(F_2,g_1,b_1\)?
- Decision: No. Preserve the source convolution but use the standard LO
  factors \(F_2=x\sum e_q^2q\) and
  \(g_1,b_1=\frac12\sum e_q^2(\Delta q,\delta_Tq)\).
- Justification: applying no half to \(b_1\) yields a moment
  \(0.00723\), exactly twice the paper's \(0.0036\). The physical tensor
  prefactor gives \(0.003615\) with the source-specified NNPDF3.1 input.
- Alternatives considered: changing the LFWF normalization or tuning a
  cluster probability were rejected because both would corrupt validated
  LMDF sum rules.
- Classification: exact observable-convention correction to a
  model-dependent cluster convolution.
- Files/tests: `hidden_color_cluster_lfwf.py`,
  `test_hidden_color_cluster_lfwf.py`,
  `compare_kaur_cluster_b1_to_hermes.py`; 14 focused tests pass.
- Revision trigger: an explicit corrigendum defining a different tensor PDF
  normalization together with reproduced source code.

## D-083: replace one-loop pion evolution with native high-order transfer scenario

- Date: 2026-07-25
- Status: accepted with refit/Y-term gate
- Question: Can the vendored Vpion19/arTeMiDe stack provide an
  order-consistent pion TMD route?
- Decision: Yes. Use the native Vpion19 profile, NNLO small-b coefficients,
  BSV19 NNNLO evolution, and exact Miller \(J_0(zbq_T)\) recoil. Substitute
  maintained JAM21 member 0 for unavailable JAM18 and label this as an input
  transfer, not a refit.
- Justification: the official LHAPDF archive no longer distributes JAM18;
  attempted local files were HTML error pages. Dedicated constants initialize
  valid proton and JAM21 pion grids with no missing-hadron errors. All 101
  Vpion19 member identities and the nuclear boundary evaluate finitely.
- Alternatives considered: retaining the one-loop route as preferred,
  accepting invalid fallback values, or calling the JAM21 substitution a
  refit were rejected.
- Classification: fit-native nonperturbative model and high-order evolution,
  with a temporary collinear-input substitution and missing fixed-order Y
  term.
- Files/tests: `pion_tmd.py`, `test_pion_tmd.py`,
  `prepare_vpion19_artemide.py`,
  `build_native_pion_tmd_scenario.py`,
  `pion_transverse_boundary.md`; seven focused tests pass.
- Revision trigger: recovered valid JAM18 grids, a Vpion19/JAM21 refit,
  public JAM 2023 ensemble, or a matched fixed-order Y term.

## D-084: replace unchanged-shape NNπ closure by conditional longitudinal recoil

- Date: 2026-07-25
- Status: accepted for collinear use; transverse spectral gate remains open
- Question: What sourced improvement can replace the unchanged-shape
  NNπ-nucleon counterterm before a complete three-body amplitude exists?
- Decision: Conditional on the Miller pion variable \(y\), use
  \(\eta_\pi=yM_N/M_D\) and
  \(\alpha_N'=(1-\eta_\pi)\alpha_N\), evaluating an arbitrary-\(x\)
  baseline correlator at the shifted fraction. Preserve every flavor and
  vector, axial, and transverse-spin matrix. Retain the unchanged-shape
  model only as a named comparison.
- Justification: this is the exact longitudinal recoil and Fock bookkeeping
  implied by the NNπ state. It preserves nucleon number, removes exactly the
  physical pion plus momentum, and changes the nucleon \(x\) shape rather
  than hiding recoil in a normalization.
- Alternatives considered: retaining unchanged shape as preferred,
  rescaling only \(f_1\), or inventing an unconstrained three-body helicity
  vertex were rejected.
- Classification: exact conditional longitudinal kinematics, Fock
  normalization, and momentum algebra; model-dependent scalar-pion
  inheritance of the conditional nucleon spin density.
- Files/tests: `pion_exchange.py`, `test_pion_exchange.py`,
  `miller_pion_exchange_input.md`; number/momentum closure, shifted-shape,
  full-matrix spin-ratio, differential-kernel reconstruction, and
  \(J_0(\alpha bq_T)\) limits pass.
- Revision trigger: a sourced or fitted three-body NNπ light-front wave
  function with explicit helicity, transverse recoil, virtuality, and
  off-forward dependence.

## D-085: interpolate multi-x LF correlators in log x and preserve the controlled isoscalar limit

- Date: 2026-07-25
- Status: accepted and numerically validated
- Question: How should the arbitrary-\(x\) LF parent required by conditional
  recoil be tabulated, and should exact \(u_D=d_D\) be treated as a defect?
- Decision: Serialize complete proton, neutron, and total matrices at
  production quadrature and use shape-preserving PCHIP in \(\ln x\), with
  exact zero outside supplied support. Treat \(u_D=d_D\) and
  \(\bar u_D=\bar d_D\) as the controlled exact-isospin deuteron limit while
  testing flavor resolution directly in the separate nucleon slices.
- Justification: direct linear-\(x\) interpolation failed at small x.
  Log-\(x\) interpolation reduces the coarse/refined conditional-total
  discrepancy to 0.439% of curve peak. The proton flavor matrix distances
  remain strongly nonzero; forcing an inclusive deuteron flavor inequality
  would violate the selected isospin limit.
- Alternatives considered: linear-\(x\) PCHIP, extrapolation beyond the
  table, treating exact isoscalar cancellation as nucleon flavor collapse,
  and adding arbitrary isospin breaking were rejected.
- Classification: numerical representation choice plus exact symmetry limit;
  MSHT20QED CSB remains the phenomenological symmetry-breaking component.
- Files/tests: `correlator_io.py`, `test_correlator_io.py`,
  `export_nnpi_collinear_parent_grid.py`,
  `compare_nnpi_recoil_parent_models.py`,
  `validate_nnpi_xgrid_convergence.py`; focused 20-test suite and
  coarse/refined production-grid audit pass.
- Revision trigger: a direct adaptive-\(x\) convolution interface, a tighter
  grid requirement, or propagation of the MSHT20QED CSB ensemble through
  this mechanism.

## D-086: define the NNπ pion-PDF central from all JAM21 replicas

- Date: 2026-07-26
- Status: accepted and propagated
- Question: Which JAM21 member defines the production pion-PDF central and
  uncertainty in the conditional NNπ result?
- Decision: Propagate all 786 members, use their ensemble mean as central,
  sample standard deviation as the symmetric replica spread, and retain
  q16/q84 plus every member prediction.
- Justification: the released set marks every member, including member 0,
  as `replica`; member 0 is not a distinguished best fit. Separating the
  replica-independent nucleon recoil avoids recomputing the expensive LF
  parent.
- Alternatives considered: member 0 central, a Hessian interpretation, and
  varying all spin projections with the pion PDF were rejected.
- Classification: phenomenological PDF uncertainty with exact ensemble
  bookkeeping.
- Files/tests: `propagate_nnpi_jam21_replicas.py`,
  `plot_nnpi_jam21_bands.py`; 786-member table and bands persisted.
  Fixed 160-node versus adaptive member-0 residuals are
  \(1.21\times10^{-5}\) for \(f_1\) and \(1.91\times10^{-5}\) for
  \(f_{1LL}\). Full regression: 290 tests pass in 45.22 s.
- Revision trigger: an updated pion PDF/TMD ensemble or a joint nuclear-pion
  fit with correlated nucleon and pion inputs.

## D-087: reject momentum-space kT=0 as a collinear NNπ parent

- Date: 2026-07-26
- Status: corrected; prior generated tables superseded in place
- Question: Did the first multi-x exporter provide the dimensionless
  collinear correlator required by the pion convolution?
- Decision: No. Replace its call to the momentum-space
  `convolve_spin1_quark_wave_components(...,k_T=0)` by the exact
  \(b_T=0\) `convolve_spin1_quark_collinear_correlator` for every coherent
  SS/SD/DS/DD component, then regenerate every dependent artifact.
- Justification: a momentum-space TMD at \(k_T=0\) has GeV\(^{-2}\)
  dimensions and cannot be added to a dimensionless collinear pion PDF.
  Smoothness and passing matrix tests do not cure that dimensional error.
- Alternatives considered: applying an arbitrary transverse-area factor or
  relabeling the mixed result as a TMD were rejected.
- Classification: exact representation/dimensional correction.
- Files/tests: `export_nnpi_collinear_parent_grid.py` and all
  `outputs/.../nnpi_recoil_av18_*` artifacts regenerated. Metadata now states
  `exact b_T=0 collinear`; coarse/refined and 786-replica validations pass.
- Revision trigger: none; this is a required convention invariant.

## D-088: compose retained-NN transverse recoil with the exact xD convention

- Date: 2026-07-26
- Status: accepted and validated on the production LF smearing grid
- Question: Does transverse NNπ recoil require an average active-nucleon
  fraction after the collinear parent has been formed?
- Decision: No. With \(x_D=x_N/2\) and
  \(z=x_D/[\alpha(1-\eta_\pi)]\), use the exact Bessel argument
  \(z\alpha bq_T=x_Nbq_T/[2(1-\eta_\pi)]\). Transport the complete baseline
  correlator at shifted \(x_N/(1-\eta_\pi)\).
- Justification: the active-nucleon fraction cancels algebraically at
  impulse level. This avoids both an \(\alpha=1/2\) shortcut and a
  post-convolution averaged recoil factor.
- Alternatives considered: \(J_0(\alpha bq_T)\) after collinear integration,
  \(\alpha=1/2\), and the initially written argument lacking the repository's
  \(x_D=x_N/2\) factor were rejected.
- Classification: exact impulse-level transverse kinematics plus the same
  model-dependent scalar-pion spin inheritance as D-084.
- Files/tests: `pion_exchange.py`, `test_pion_exchange.py`,
  `export_nnpi_nucleon_bspace_recoil.py`; exact b=0 matrix reduction,
  negative-b refusal, spin transport, and direct Bessel-argument tests pass.
  Production AV18 b=0 residual is \(2.91\times10^{-6}\).
- Revision trigger: a three-body off-forward NNπ amplitude that correlates
  pion recoil with nucleon virtuality or target-helicity transitions beyond
  scalar-pion inheritance.

## D-089: Fock-normalize native Vpion19 and propagate its nuclear profile replicas

- Date: 2026-07-26
- Status: accepted as a non-production high-order transfer scenario
- Question: Can the native pion curve be combined consistently with the
  retained-NN Fock ledger using only intrinsic-pion replica bands?
- Decision: Normalize the Miller splitting by \(1/(1+N_\pi)\), propagate
  Vpion19 members 0--100 through the full \(J_0(zbq_T)\) nuclear convolution,
  and assemble the nuclear q16/q84 band with the retained-NN AV18 term.
- Justification: using the raw splitting double-counted the normalization
  already enforced in the NN/NNπ ledger, while intrinsic-only bands did not
  represent uncertainty after nuclear composition.
- Alternatives considered: retaining raw \(Z\simeq1\), applying the
  intrinsic band multiplicatively after convolution, or inventing a native
  tensor-pion profile were rejected.
- Classification: exact Fock consistency plus fit-native model-profile
  uncertainty; JAM21 transfer and absent Y term remain temporary limitations.
- Files/tests: `build_native_pion_tmd_scenario.py`,
  `assemble_nnpi_native_bspace.py`, `pion_transverse_boundary.md`; 808
  member/b rows, combined CSV/PDF/PNG, finite validation, and visual QA.
- Revision trigger: a Vpion19/JAM21 refit, public JAM 2023 replicas, a
  fixed-order Y term, or a sourced tensor-pion TMD fit.

## D-090: do not promote the 2026 scalar LFHEFT deuteron benchmark to an off-forward NNπ amplitude

- Date: 2026-07-26
- Status: accepted source boundary; replacement interface remains open
- Question: Does arXiv:2601.13567 provide the missing dynamical three-body
  input for spin-resolved/off-forward NNπ GTMDs?
- Decision: No. Use it as evidence for the Fock-space organization and
  multi-pion convergence need, but not as a deuteron NNπ correlator.
- Justification: the source integrates the three-body sector into a scalar
  Wilson--Bloch two-body Hamiltonian and explicitly says dynamical pions are
  not yet fully integrated. It publishes neither helicity amplitudes nor
  off-forward overlaps or machine-readable wave functions.
- Alternatives considered: fitting an arbitrary \(\Delta_T\) slope to the
  plotted scalar LMD, using the 200 MeV strong-binding example as physical,
  or assigning scalar amplitudes to all spin channels were rejected.
- Classification: exact source/provenance boundary and temporary unresolved
  external physics input.
- Files/tests: `lfheft_nnpi_source_audit.md`, archived source PDF; the
  replacement amplitude and its forward/hermiticity/spin/Fock tests are
  enumerated.
- Revision trigger: release of the authors' dynamical three-/four-body
  deuteron amplitudes or another sourced spin-resolved off-forward NNπ
  spectral calculation.

## D-091: keep gluon T-odd color and process structures explicit

- Date: 2026-07-26
- Status: accepted and tested through the spin-1 parent; production input unresolved
- Question: May the missing gluon Sivers sector use one process-reversing
  phase analogous to the quark Sivers function?
- Decision: No. Require independent antisymmetric f-type and symmetric d-type
  universal inputs and require every observable to supply both hard
  coefficients. Future/past reversal acts on each component separately;
  mixed link pairs fail closed.
- Justification: gluon process dependence selects linear combinations of two
  independent color structures. RHIC CGI-GPM studies provide preliminary,
  framework-dependent constraints, not a validated fit-native two-color
  production ensemble for this project.
- Alternatives considered: one universal gluon phase, setting d-type equal to
  f-type, importing a preliminary central curve without replicas, and
  treating mixed links as a sign were rejected.
- Classification: exact color/gauge-link organization plus an unresolved
  phenomenological input.
- Files/tests: `gluon_todd.py`, `test_gluon_todd.py`,
  `gluon_todd_source_audit.md`; component independence, process composition,
  transverse-spin angular embedding, Hermiticity, reversal, forward-only
  refusal, domain/nonfinite guards, and retained-spin spin-1 parent
  propagation pass. Full repository regression is 301 tests.
- Revision trigger: a fit-native f/d release with conventions, validity, and
  uncertainties, together with a factorization-controlled benchmark process.

## D-092: make the in-house TMD scheme an enforceable composition contract

- Date: 2026-07-26
- Status: accepted and validated; perturbative accuracy remains intermediate
- Question: Is a human-readable scheme string sufficient to connect quark or
  gluon small-b boundaries to CSS evolution?
- Decision: No. Carry typed soft subtraction, rapidity regulator,
  prescription, UV scheme, source, and explicit \((\mu,\zeta)\) endpoints.
  Require exact boundary/evolution compatibility and restrict the current
  solver to its implemented canonical \(\zeta=\mu^2\) path.
- Justification: scheme and rapidity-scale compatibility are physical
  composition constraints. A string did not prevent mixing incompatible
  definitions or claiming unsupported two-scale evolution.
- Alternatives considered: retaining metadata-only labels, assuming
  \(\zeta=Q^2\) without storing it, and accepting arbitrary zeta values in a
  one-dimensional CSS exponent were rejected.
- Classification: exact convention/bookkeeping constraint. Matching order,
  truncation, and large-b profiles remain model/perturbative limitations.
- Files/tests: `tmd_scheme.py`, quark/gluon matching and evolution modules,
  `test_tmd_scheme.py`, `tmd_scheme_contract.md`; 29 focused tests pass.
- Revision trigger: a general two-scale evolution backend or a change of
  regulator/subtraction convention with explicit conversion factors.

## D-093: restrict inclusive gluon shadowing to its identifiable matrix sector

- Date: 2026-07-26
- Status: accepted and tested; other non-impulse gluon inputs unresolved
- Question: May the existing quark nuclear response factors be applied to the
  complete spin-1 gluon correlator?
- Decision: No. Introduce a separate full `(3,3,2,2)` gluon mechanism ledger.
  The inclusive diffractive builder modifies only target-U/gluon-trace
  structure; every polarized, tensor, circular, and linear response remains
  inactive unless separately sourced.
- Justification: inclusive diffractive information constrains an
  unpolarized-gluon response and does not determine spin-transfer ratios.
  Applying one scalar to the full matrix would hide missing physics.
- Alternatives considered: reuse all quark channel factors, multiply the
  complete gluon matrix, and treat absent sectors as physical zeros were
  rejected.
- Classification: exact correlator/provenance composition plus a
  model/phenomenology-informed inclusive shadowing component.
- Files/tests: `gluon_nuclear_mechanisms.py`,
  `test_gluon_nuclear_mechanisms.py`,
  `gluon_nuclear_mechanism_boundary.md`; named diffractive members retain
  full correlators, and gluon antishadowing restores the configured momentum
  fraction. Combined nuclear-mechanism suite has 16 passing tests; full
  repository regression has 311 passing tests.
- Revision trigger: polarized/tensor DPDFs, a fitted gluon off-shell response,
  or sourced mesonic/non-nucleonic gluon correlators.

## D-094: WP8 completion is determined by a verified requirement matrix

- Date: 2026-07-26
- Status: accepted and operational
- Question: Can the full pytest count and scattered validation JSONs prove
  the WP8 gate?
- Decision: No. Maintain one versioned manifest mapping every grouped WP8
  requirement to tolerances, collected tests, artifacts, provenance,
  affected outputs, declared status, and open reason. Generate a report that
  executes the full suite and refuses completion while any item is partial,
  open, missing, or failed.
- Justification: passing tests prove only their covered scope. The previous
  evidence was fragmented and could not distinguish an untested requirement
  from a passing one.
- Alternatives considered: cite only the full test count, manually curate a
  narrative checklist, or treat artifact existence as success were rejected.
- Classification: exact validation/completion bookkeeping.
- Files/tests: `validation/wp8_manifest.json`,
  `build_wp8_validation_report.py`, `test_wp8_validation_manifest.py`,
  `wp8_validation_matrix.md`, generated acceptance report. Current run:
  312 collected/passed, seven verified, five partial, zero missing evidence,
  `completion_ready=false`.
- Revision trigger: every material new sector/test/output must update the
  manifest; completion requires all entries to become verified.

## D-095: truncated x integrals are not conservation claims

- Date: 2026-07-26
- Status: accepted and enforced
- Question: May a smooth production table over \(0.001\le x\le0.95\) be used
  directly to claim number or momentum conservation?
- Decision: No. Record the partial integral, support interval, species,
  flavor, mechanism, and source. Permit a sum-rule audit only with exact
  \([0,1]\) support or an observable-specific sourced endpoint completion.
- Justification: unmeasured low-x and high-x tails can contribute
  differently to number, momentum, helicity, tensor, and transversity
  moments. Smooth interpolation does not determine them.
- Alternatives considered: assume zero tails, extrapolate the endpoint
  spline, and use one common correction for every moment were rejected.
- Classification: exact validation/provenance constraint; endpoint physics
  remains input dependent.
- Files/tests: `moment_ledger.py`, `test_moment_ledger.py`,
  `audit_parent_moment_coverage.py`, `moment_ledger_contract.md`; production
  artifact has 62 quark/gluon entries and an explicit conservation refusal. WP8 run has
  316 collected/passed tests and no missing evidence.
- Revision trigger: source-validated endpoint models or production tables
  with controlled full support.

## D-096: controlled limits must cover the complete named parent basis

- Date: 2026-07-26
- Status: accepted and WP8-verified
- Question: Do scattered representative-function limit tests establish the
  pure-S, zero-D, no-Melosh, free-nucleon, isospin, CSB, and zero-correction
  gate?
- Decision: Add one common retained-spin parent audit for all 18 named quark
  TMDs and full quark/gluon mechanism matrices, while retaining dedicated
  all-flavor isospin/CSB tests.
- Justification: a limit can mix target and parton spin structures. Testing
  only f1 or one correlator block cannot exclude contamination elsewhere.
- Alternatives considered: cite existing scattered tests without a common
  artifact or test only rank-zero functions were rejected.
- Classification: exact analytic limiting-case validation.
- Files/tests: `controlled_limits.py`, `test_controlled_limits.py`,
  `audit_controlled_limits.py`, `controlled_limit_audit.md`; six checks pass
  with zero residual versus \(2\times10^{-11}\).
- Revision trigger: adding a named TMD, mechanism slot, or changing LF spin
  coupling requires extending the common audit.

## D-097: positivity envelopes require correlated full matrices

- Date: 2026-07-26
- Status: accepted; wave ensemble audited, overall requirement partial
- Question: May pointwise lower/upper envelopes of named TMDs be assembled
  into a matrix and tested as though they were an ensemble member?
- Decision: No. Audit only correlated full matrices member by member. Refuse
  projection-only or cross-member envelope reconstruction; report negative
  eigenvalues without clipping.
- Justification: extrema of different TMDs can come from different members,
  and their assembled matrix is not a physical ensemble realization.
- Alternatives considered: combine pointwise band edges, clip negative
  eigenvalues, or report central-only positivity were rejected.
- Classification: exact uncertainty/linear-algebra constraint.
- Files/tests: `joint_positivity.py`, `test_joint_positivity.py`,
  `audit_gluon_wave_positivity.py`, `joint_positivity_ensemble_audit.md`.
  Six wave members and 162 matrices pass; global minimum is 0.1149674621.
- Revision trigger: every new full-correlator ensemble must be audited; a
  projection-only release remains explicitly non-reconstructible.

## D-098: heterogeneous uncertainty axes cannot imply a joint covariance

- Date: 2026-07-26
- Status: accepted and WP8-verified
- Question: How should wave, numerical, transform, fit, evolution, and
  nuclear-mechanism uncertainties be combined without a published joint
  probability?
- Decision: Keep seven typed axes separate. Allow a joint covariance only
  through a sourced, labeled, symmetric PSD `JointProbabilityInput`.
- Justification: replicas, Hessians, convergence sequences, correlated named
  scenarios, and nonprobabilistic envelopes do not share a sampling measure.
- Alternatives considered: quadrature addition, treating named scenarios as
  Monte Carlo samples, or building a sample covariance over heterogeneous
  members were rejected.
- Classification: exact statistical/provenance constraint.
- Files/tests: `uncertainty_axes.py`, `test_uncertainty_axes.py`,
  `audit_uncertainty_axes.py`, `uncertainty_axis_contract.md`; all seven axes
  are present and unsourced joint covariance is refused.
- Revision trigger: a published joint fit or probability model can be added
  only with its source, axes, labels, and validated covariance.

## D-099: figure authority follows parent traceability, not presentation quality

- Date: 2026-07-26
- Status: accepted; WP9 figure-source gate verified
- Question: May the polished reduced-correlator atlas remain labeled as a
  production figure tree after the model was superseded?
- Decision: No. Preserve the historical artifacts for reproducibility, mark
  their directory explicitly superseded, fail closed at the old plotting
  entry point, segregate any future closure plots, and publish a
  machine-readable authority index for parent-derived tables and PDFs.
- Justification: visual smoothness and complete panel coverage do not prove
  light-front parent traceability. Conversely, inclusive exact-isospin
  equality is acceptable only when distinct proton/neutron flavor sources
  remain inspectable before assembly.
- Alternatives considered: delete the old figures, silently overwrite them
  with unlike products, or retain the ambiguous `production_tmds` label
  without a guard were rejected.
- Classification: exact provenance and acceptance constraint.
- Files/tests: `figure_index.json`, `SUPERSEDED.md`,
  `figure_acceptance.py`, `audit_parent_tmd_figures.py`,
  `test_figure_acceptance.py`; 72 quark and 18 gluon atlas groups pass, and
  proton/neutron \(u-d\) and sea-flavor differences are nonzero.
- Revision trigger: a future figure tree can become authoritative only after
  its rows pass the same parent-source and basis-completeness audit.

## D-100: endpoint completion follows physical moment combinations

- Date: 2026-07-26
- Status: accepted; global-moment gate narrowed but remains partial
- Question: Should separate quark and antiquark number tails be forced finite,
  and may the old \(x\le0.7\), \(Q=2\) gluon table support a global claim?
- Decision: No. Form \(q-\bar q\) before endpoint fitting, use local power
  completion only for grids reaching both endpoint neighborhoods with stable
  signs, quantify adjacent-window sensitivity, and regenerate retained-parent
  gluon/all-active-parton grids at \(Q=5\).
- Justification: small-\(x\) sea number can diverge while valence number is
  finite. Momentum requires all active flavors, and gluon helicity requires
  the vector-polarized retained-spin parent rather than scalar smearing.
- Alternatives considered: zero tails, independent finite sea-number fits,
  omitting heavy flavors, and scalar convolution of polarized PDFs were
  rejected.
- Classification: field-theoretic sum-rule algebra plus model-dependent,
  explicitly uncertain endpoint completion.
- Files/tests: `moment_ledger.py`, `audit_parent_moment_coverage.py`,
  `compute_all_parton_momentum_parent.py`,
  `compute_gluon_helicity_parent_grid.py`, `test_moment_ledger.py`.
  Valence number and all-parton momentum pass; gluon momentum and helicity
  are support complete. The sign-changing gluon tensor tail remains refused.
- Revision trigger: source-constrained tensor endpoints or non-impulse
  all-sector parents replace the remaining refusal.

## D-101: joint positivity is scoped to correlated reconstructible members

- Date: 2026-07-26
- Status: accepted and WP8-verified
- Question: Must pointwise envelopes or nonexistent fit ensembles keep the
  positivity gate partial after every implemented correlated member can be
  reconstructed as a full density?
- Decision: No. Audit every implemented reconstructible ensemble member,
  preserve shared component identities, report tensions without clipping,
  and refuse projection-only envelope reconstruction. Do not invent members
  for inputs that expose only a central prediction.
- Justification: positivity is a property of one correlated full density,
  not independently selected band edges. Missing uncertainty inputs remain
  provenance/model limitations but are not fictitious positivity members.
- Alternatives considered: combining envelope extrema, ignoring correlated
  WW identity, rejecting BPV20 members, or keeping the gate open for
  nonexistent gluon fits were rejected.
- Classification: exact linear-algebra/provenance rule with a documented
  factorization-scheme applicability caveat.
- Files/tests: `uncertainty_validation.py`,
  `audit_jamdiff_joint_positivity.py`,
  `audit_gluon_shadowing_positivity.py`, `test_joint_positivity.py`.
  JAMDiFF 968/968 pass; shadowing central/low/high pass; BPV20 tensions remain
  unmodified; six gluon wave members pass.
- Revision trigger: every newly added full-member fit or nuclear ensemble
  must enter this audit before its output is accepted.

## D-102: gluon tensor local moments carry the gluon x weight

- Date: 2026-07-26
- Status: accepted and WP8-verified
- Question: Why did the gluon tensor endpoint appear non-integrable while
  momentum and helicity were controlled?
- Decision: Store the moment weight explicitly per ledger input. The leading
  local twist-two gluon tensor moment uses \(x f_{1LL}^g\), whereas the
  quark tensor number-like moment uses \(f_{1LL}^q\).
- Justification: gluon local twist-two operators begin with the momentum-like
  \(x\) moment. Reusing the quark \(x^0\) power generated a spurious
  small-\(x\) divergence.
- Alternatives considered: force an \(x^0\) tail, set the tail to zero, or
  omit the gluon tensor moment were rejected.
- Classification: exact operator/moment convention; endpoint value remains
  model-dependent with quantified fit-window sensitivity.
- Files/tests: `moment_ledger.py`, `audit_parent_moment_coverage.py`,
  `test_moment_ledger.py`; the gluon tensor result is
  \(3.06955\times10^{-7}\) with \(2.36372\times10^{-8}\) endpoint
  sensitivity.
- Revision trigger: a different gluon PDF convention must provide an
  explicit conversion and corresponding moment-weight test.

## D-103: a process Y remainder is not a universal TMD completion

- Date: 2026-07-26
- Status: accepted and WP8-verified
- Question: Does the absence of an unspecified fixed-order SIDIS/DY
  \(Y\)-term make an intrinsic TMD table incomplete?
- Decision: No. Enforce the low-\(q_T\) W domain and refuse high-\(q_T\)
  observable evaluation without a sourced process-specific FO/ASY pair.
  Never add a generic Y term to an intrinsic TMD to repair its marginal.
- Justification: \(Y=\mathrm{FO}-\mathrm{ASY}\) belongs to a named
  differential cross section, including its hard channel and fragmentation
  inputs. The requested products are TMD distributions. Process/link/color
  dependence and the validity/refusal boundary are the applicable model
  requirements.
- Alternatives considered: invent a universal Y term, silently extrapolate
  W, or truncate data without recording validity were rejected.
- Classification: exact factorization/provenance boundary.
- Files/tests: `w_y_matching.py`, `test_w_y_matching.py`,
  `build_parent_tmd_ensemble.py`, `figure_acceptance.py`; gluon tables now
  serialize validity and atlases hatch \(k_T>1\) GeV at \(Q=5\).
- Revision trigger: a named observable with supplied FO, ASY, hard channel,
  and fragmentation/PDF inputs must pass the existing overlap contract.

## D-104: final acceptance uses declared configurable-model scope

- Date: 2026-07-26
- Status: accepted; project completion verified
- Question: How are unavailable external amplitudes/fits distinguished from
  unfinished implementation at final acceptance?
- Decision: A sector is complete when the best-supported configured input,
  validity and uncertainty, typed replacement interface, zero/limit behavior,
  provenance, and distinguishing tests are implemented. Unavailable inputs
  are not invented or added to production totals. They remain explicitly
  classified model/data upgrades, while every requirement in the declared
  TMD scope must have executable evidence.
- Justification: the user required physical completeness supported by present
  information, not fabricated precision. A missing public polarized DPDF,
  full NNπ amplitude, or two-color gluon fit cannot be manufactured; the
  architecture must make replacement safe and the current claim exact.
- Alternatives considered: keep implementation permanently partial for
  nonexistent inputs, silently substitute universal ansätze, or exclude the
  sectors without interfaces were rejected.
- Classification: final scope/provenance decision.
- Files/tests: `final_acceptance_manifest.json`,
  `build_final_acceptance_report.py`, `test_final_acceptance_manifest.py`.
  Ten criteria and 334 tests pass; WP8 verifies all 12 grouped requirements.
- Revision trigger: any new production mechanism, fit ensemble, perturbative
  order, or observable expands the accepted scope and must add manifest
  evidence before being called complete.

- P-010: The regulator family and LEC dataset are now fixed by the Norfolk
  model pairing. The Gaussian contact contraction is validated. The precise
  coordinate-space tensor-phase convention needed to reproduce the published
  OPE magnetic moments remains pending; do not use that term in production
  until its Table III benchmark passes.

- P-001: Package structure, dependency pinning strategy, and supported platforms.
- P-003: Active-nucleon transverse recoil mapping \(\Delta_{T,N}\).
- P-005: Production-grid resolution and whether to persist processed AV18/CD-Bonn tables.
- P-006: Final PDF ensemble and perturbative order for Stage 1 phenomenology.
- P-007: TMD subtraction/evolution scheme and rapidity regulator convention.
- P-008: Numerical integration, interpolation, and precision requirements.
- P-009: First process-specific Wilson-line convention.
# D-105: rich spin-1 dynamical sectors supersede declared-scope completion

- Date: 2026-07-26
- Status: accepted; implementation completed by D-106
- Question: Are fitted/model gauge-link phases, Boer--Mulders, fitted or
  lattice-informed pretzelosity/worm gears, independent gluon f/d T-odd
  inputs, polarized/tensor shadowing, non-impulse correlators, and additional
  OAM interference optional upgrades after the 334-test acceptance report?
- Decision: No. They are required WP10 sectors. Preserve the earlier report
  as a baseline checkpoint but reopen project completion until WP10 is
  implemented and enters both acceptance manifests.
- Justification: exact zeros of a real one-body boundary establish a
  controlled limit, not the full physical spin-1 correlator. Interfaces,
  observable-only scenarios, and universal signed brackets do not constitute
  numerical correlator implementations.
- Alternatives considered: retain the old declared scope, fill all missing
  functions with a common phase, or relabel every zero as structural were
  rejected.
- Classification: governing scientific-scope decision.
- Files/tests: `AGENTS.md`, `handoff/project_context.md`,
  `handoff/ROADMAP.md`; WP10 implementation and tests remain the execution
  queue.
- Revision trigger: only a user-approved reduction of scientific scope or
  completed WP10 acceptance can restore a completion claim.

# D-106: WP10 completion uses separated model axes, not invented covariance

- Date: 2026-07-26
- Status: accepted; WP10 verified
- Question: How can the rich sectors be production-complete when several
  requested functions lack public fit replicas or lattice grids?
- Decision: Implement the best-supported central fit where it exists and
  independent, named, replaceable model scenarios otherwise. Preserve every
  fit, wave, color, link, shadowing, pion/cluster, and OAM identity in the
  WP10 production ledger. Refuse to sum alternative rows or manufacture a
  joint covariance without a sourced probability model.
- Justification: completeness of the physical/computational representation
  is distinct from experimental determination. Yang-2024 fixes a central
  \(g_{1T}\), CGI-GPM fixes gluon-Sivers f/d normalization scenarios, while
  pretzelosity, the other five gluon T-odd structures, polarized/tensor
  diffraction, cluster intrinsic transverse structure, and extra OAM remain
  explicitly model-dependent.
- Alternatives considered: universal phases, flavor collapse, arbitrary
  Gaussian bands, and permanent exact zeros were rejected.
- Classification: mixed phenomenological/model-dependent completion rule.
- Files/tests: `validation/wp10_manifest.json`,
  `build_wp10_acceptance_report.py`, `build_wp10_production_ledger.py`,
  `test_wp10_manifest.py`, and `test_wp10_production_ledger.py`.
- Revision trigger: a public replica ensemble, lattice grid, polarized DPDF,
  coupled NNpi amplitude, or process hard-color calculation replaces only
  its named input and adds a new correlated production axis.

# D-107: quark g1LT/g1TT require axial tensor phases, not Sivers reuse

- Date: 2026-07-26
- Status: accepted and implemented
- Question: How should the missing leading-twist quark \(g_{1LT}\) and
  \(g_{1TT}\) be activated?
- Decision: Keep two non-additive stages. Stage 1 assigns independent
  flavor/operator axial phase coefficients and caps the pair using the full
  retained-spin density. Stage 2 calculates rank-one and rank-two harmonics
  of a screened one-gluon convolution and couples them to explicit
  S--P/S--D/P-even--P-odd interferences using the AV18 \(P_D\) and signed
  S--D radial overlap.
- Justification: both functions live in the axial `gamma+gamma5` tensor
  channels and are T-odd. Neither a real impulse parent nor a copied vector
  Sivers phase can generate the correct operator structure. One-gluon and
  eikonal remnant rescattering are established mechanisms for imaginary
  light-front interference, but do not provide a fit for these spin-1
  functions.
- Alternatives considered: leave exact zeros, reuse the Sivers phase,
  promote arbitrary coefficients without positivity, or tune the explicit
  rescattering result up to the phase envelope were rejected.
- Classification: model-dependent axial phase plus explicit eikonal
  rescattering calculation.
- Files/tests: `axial_tensor_todd.py`,
  `export_axial_tensor_todd_stages.py`,
  `test_axial_tensor_todd.py`,
  `test_axial_tensor_todd_production.py`,
  `axial_tensor_eikonal_convergence.json`, and
  `quark_g1lt_g1tt_two_stage_atlas.pdf`.
- Revision trigger: a dedicated spin-1 extraction, lattice staple-link
  calculation, polarized diffractive amplitude, or QCD-derived rescattering
  kernel should replace the corresponding named stage.

# D-108: gluon T-odd predictions replace universal rank scaling

- Date: 2026-07-26
- Status: accepted and implemented
- Question: How should the six gluon T-odd structures be predicted beyond
  the CGI-GPM-Sivers-times-ratio boundary?
- Decision: Retain that boundary only as a comparison. Use the published
  full \(g_1+g_2\) spectator hierarchy and nodes for the four spin-half
  structures, and calculate spin-1 \(g_{1LT}\), \(g_{1TT}\) from AV18 S--D
  coherence and screened rank-one/rank-two adjoint-eikonal moments. Compose
  all six with the full AV18 density and apply one positivity scale. Keep
  WW f-type and dipole d-type links and couplings independent.
- Justification: arXiv:2402.17556 supplies a physical one-gluon mechanism
  and all four spin-half structures but not the spin-1 tensor channels,
  Q=5 evolution, or its replica files.
- Alternatives considered: exact zeros, reuse of universal ratios, calling
  a reconstructed band the published replica band, and identifying d-type
  with f-type beyond the equal-vertex assumption were rejected.
- Classification: published-model-informed plus model-dependent spin-1
  extension.
- Files/tests: `gluon_todd.py`,
  `export_spectator_informed_gluon_todd.py`,
  `test_spectator_informed_gluon_todd.py`, the production CSV/correlator
  export, and `gluon_todd_two_stage_prediction_atlas.pdf`.
- Revision trigger: released PVGlue20 replicas, a full numerical coefficient
  implementation and evolution fit, spin-1 lattice staple matrix elements,
  or dedicated EIC data.

# D-109: structural completeness is not canonical physical synthesis

- Date: 2026-07-26
- Status: accepted; integration gate reopened
- Question: Does the complete WP10 member ledger already constitute a
  self-consistent overall quark/gluon model?
- Decision: No. Treat it as a provenance-resolved inventory of baselines,
  alternatives, and additive mechanisms. A canonical model additionally
  requires an explicit contribution graph, common scheme/evolution contract,
  and nucleon-to-nucleus composition path for every selected member.
- Justification: several well-constrained inputs do pass through the full LF
  parent, but the latest gluon T-odd layer scales the assembled deuteron
  \(f_1^g\) downstream, and its source-informed functions do not evaluate the
  published spectator master integrals. Positivity and completeness cannot
  repair that parent-chain mismatch.
- Alternatives considered: accept every ledger row as mutually composable,
  promote positivity-allowed amplitudes to a central prediction, or discard
  all model sectors were rejected.
- Classification: governing scientific integration decision.
- Files/tests: `references/overall_quark_gluon_consistency_audit.md`;
  C1--C7 in `handoff/ROADMAP.md`.
- Revision trigger: close C1--C7 with a canonical composition audit and
  observable-level validation.

# D-110: canonical quark--gluon synthesis is the project objective

- Date: 2026-07-26
- Status: governing and permanent
- Question: Is the fully self-consistent canonical quark--gluon synthesis an
  optional improvement after component-level acceptance?
- Decision: No. It is the objective of the project and the only scientific
  completion authority. The model must include as much structure and as many
  contributions as are physically known and realistically supportable to
  date, composed through a common parent without double counting.
- Justification: a complete basis populated by disconnected fits and model
  scenarios cannot establish joint physical consistency. Conversely,
  uncertain physics cannot be excluded solely because it lacks a fit.
- Operational rule: do not artificially enhance weak contributions; do not
  silently omit realistic ones. Classify evidence, use conservative
  replaceable defaults, propagate sensitivities, and reserve the preferred
  central member for defensibly normalized and mutually compatible pieces.
- Classification: user-defined governing scientific objective.
- Files/tests: `AGENTS.md`, `handoff/project_context.md`,
  `handoff/ROADMAP.md`, and
  `references/overall_quark_gluon_consistency_audit.md`.
- Revision trigger: explicit user change of the scientific objective only.

# D-111: external gluon spectator models are benchmarks, not the canonical parent

- Date: 2026-07-26
- Status: accepted and implemented
- Question: Must a published spectator construction replace the project's
  own light-front quark--gluon machinery to obtain gluon T-odd functions?
- Decision: No. The canonical gluon T-odd parent is the project's own
  spin-half light-front overlap dressed by screened adjoint Wilson-line
  harmonics, followed by the AV18 retained-helicity convolution and spin-one
  LT/TT Wilson-line phase. The published PVGlue20 source is retained as an
  independent hierarchy and limiting-case benchmark only.
- Justification: a foreign fitted model cannot make the project's amplitudes
  more canonical. It is useful for checking which structures survive a
  minimal vertex, expected rank hierarchy, and parameter scale. The internal
  construction preserves one parent chain, common T-even normalization,
  independent f/d color channels, and exact staple reversal.
- Alternatives considered: adopting the published normalization as the
  project baseline, downstream scaling of deuteron \(f_1\), and tuning
  function-by-function visibility coefficients were rejected.
- Classification: model architecture and no-double-counting decision.
- Files/tests: `gluon_lfwf_todd.py`, `pvglue20_benchmark.md`,
  `canonical_composition_manifest.json`,
  `test_gluon_lfwf_todd.py`, and
  `test_canonical_gluon_lfwf_todd_production.py`.
- Revision trigger: a future global extraction may replace the internal
  kernel through its declared interface, but remains subject to the same
  scheme, parent-chain, positivity, and no-double-counting tests.

# D-112: Yang-2024 g1T uses the common rank-one evolution as a model route

- Date: 2026-07-26
- Status: accepted and implemented
- Question: Should the Yang-2024 fitted \(g_{1T}\) moment remain frozen at
  its reference scale because fit-native replicas and evolution code are not
  public?
- Decision: No. Use the published central moment as the \(Q_0\) boundary of
  the project's explicit rank-one \(J_1\)/CSS adapter. Classify this as
  common-kernel model evolution, not fit-native evolution, and retain missing
  correlated replicas as an uncertainty limitation.
- Justification: freezing a leading-twist TMD while evolving the other
  canonical parent components is less self-consistent than applying the
  shared spin-independent leading-power Sudakov with the correct transverse
  rank. The boundary retains distinct u/d signs and the published sea-zero
  fit assumption.
- Alternatives considered: frozen \(Q_0\) use, reverting to a WW central
  \(g_{1T}\), and inventing replicas from marginal parameter intervals were
  rejected.
- Classification: phenomenological boundary plus model evolution.
- Files/tests: `worm_gear_inputs.py`, `generate_evolved_quark_grid.py`,
  `validate_evolved_quark_grid.py`, `canonical_scheme_manifest.json`, and
  the regenerated fixed-Q grid and validation report.
- Revision trigger: released Yang fit covariance/replicas or a fit-native
  TMD evolution implementation.

# D-113: uncertainty bands remain named scientific axes

- Date: 2026-07-26
- Status: accepted and implemented
- Decision: Combine wave-function, sourced nuclear, fit-replica, and model
  variations only as an explicitly conservative named-axis envelope in the
  canonical atlas. Do not describe it as a confidence interval.
- Justification: several inputs lack joint likelihoods or covariance, so a
  probabilistic combination would invent information.
- Files/tests: `canonical_uncertainty_manifest.json`,
  `build_canonical_tmd_atlas.py`, `test_canonical_tmd_atlas.py`.
- Revision trigger: a joint fit or a defensible cross-component covariance.

# D-114: WP11 is accepted at the declared leading-twist forward scope

- Date: 2026-07-26
- Status: governing completion decision
- Decision: C1--C7 are closed by the canonical correlator chain, explicit
  scheme/composition manifests, operator-aware nuclear mechanisms,
  process-selection rules, smooth complete atlases, and reproducible
  validation. Earlier WP8/WP10 reports remain component evidence only.
- Justification: the final audit maps every acceptance criterion to files,
  tests, and numerical artifacts; the full suite passes 433 tests.
- Scope: complete leading-twist forward TMD boundary at
  \(x_N=0.1,Q=5\) GeV. A global fit and complete process cross-section
  program are outside that declared deliverable. Unsupported hidden-color
  and unavailable covariance information remain explicit replaceable axes,
  not silent central physics.
- Files/tests: `references/wp11_final_acceptance_audit.md`,
  `outputs/validation/wp11_final_acceptance.json`,
  `test_wp11_final_audit.py`.
- Revision trigger: expansion of the declared twist/off-forward/process
  scope or new data requiring replacement of a named model component.

# D-115: WP12 enrichment acts on complete parents, never named TMDs

- Date: 2026-07-26
- Status: governing and implemented at the core-object level
- Question: May items 1--5 be implemented by separately repairing visible
  functions such as \(h_{1TT}\)?
- Decision: No. Wilson channels, Fock/OAM amplitudes, non-nucleonic sectors,
  and nuclear responses accept and return complete correlators. Named TMDs
  appear only at projection and validation.
- Justification: shared amplitudes and spin-density maps create correlated
  changes across the complete basis and prevent independent ansätze from
  violating symmetry, positivity, or composition.
- Files/tests: `canonical_parent_enrichment.py`,
  `test_canonical_parent_enrichment.py`, `wp12_manifest.json`.
- Revision trigger: none short of changing the governing scientific
  objective.

# D-116: use completely-positive joint-spin maps for nuclear enrichment

- Date: 2026-07-26
- Status: accepted; production integration in progress
- Question: Is separate coefficient scaling sufficient for polarized and
  tensor nuclear responses?
- Decision: Retain it as an audited identity/linear-response limit, but use
  Kraus maps on the complete target-spin x parton-spin density for canonical
  enrichment. The inverse Pauli decomposition restores vector, axial, and
  transverse parent blocks after the map.
- Justification: a CP map preserves Hermiticity and positivity by
  construction while allowing target vector/tensor and parton helicity
  dependence to modify off-diagonal LT/TT coherence.
- Files/tests: `canonical_parent_enrichment.py`,
  `test_canonical_parent_enrichment.py`.
- Revision trigger: a field-theoretic nuclear response kernel may replace
  the parameterized Kraus rates through the same interface.

# D-117: WP12 items 1--5 close at a fixed-Q pre-evolution boundary

- Date: 2026-07-26
- Status: accepted and implemented
- Question: Does completing all-TMD enrichment require beginning the full
  TMD-evolution program before the requested items-1--5 review?
- Decision: No. Recompute every central parent directly at five \(x_N\)
  nodes at \(Q=5\) GeV, propagate every WP12 enrichment family across those
  nodes, and declare multi-\(Q\), rank-aware evolution to be item 6.
- Justification: this cleanly separates boundary-model completeness from
  evolution uncertainty and follows the user's instruction to inspect
  items 1--5 before moving to 6. It is not a frozen-\(Q\) claim about nature.
- Classification: declared-scope and computational-composition decision.
- Files/tests: `wp12_manifest.json`,
  `wp12_items1_5_acceptance.json`, all `test_wp12_*` tests, and the WP12
  production scripts.
- Revision trigger: starting item 6 or changing the boundary scale/grid.

# D-118: nuclear-response members replace legacy coefficient responses

- Date: 2026-07-26
- Status: accepted and implemented
- Question: Should weak/central/strong completely-positive response maps be
  added to the already response-corrected legacy parent?
- Decision: No. Each member is an ordered CP-map chain on a
  positivity-completed retained impulse parent and replaces the legacy
  response family. Its five mechanism increments telescope to the mapped
  parent; members are mutually exclusive.
- Justification: addition would double count nuclear physics and a sum of
  separately positive response increments need not preserve positivity.
- Classification: exact composition rule plus phenomenological CP model.
- Files/tests: `operator_nuclear_response.py`,
  `export_wp12_operator_response_members.py`,
  `wp12_composition_manifest.json`,
  `test_wp12_operator_response_output.py`.
- Revision trigger: a field-theoretic response kernel or fitted joint
  polarized/tensor nuclear response.

# D-119: item 6 uses the resolved constituent boundary

- Date: 2026-07-27
- Status: governing and accepted
- Question: Which parent should rank-aware evolution consume after the WP12
  items-1--5 inspection?
- Decision: Use `wp12_resolved_quark_parent.csv` and
  `wp12_resolved_gluon_parent.csv` (and their correlator companions), keeping
  proton-in-deuteron, neutron-in-deuteron, nucleon-sum,
  proton-minus-neutron, nuclear-correction, and canonical-total components
  distinct. The canonical total is a derived closure projection and must
  never replace the resolved state. The impulse blocks already contain the
  central Wilson operator. Ordered CP maps replace legacy shadowing,
  antishadowing, and off-shell coefficients; the sourced NNpi correlator is
  added once. Generic CP mesonic/SRC and cluster sectors remain
  zero-centered alternatives.
- Justification: a deuteron total alone hides the opposite flavor/OAM
  dynamics present in its proton and neutron constituents and is inadequate
  as the state of a complete model. Evolving the resolved ledger preserves
  those dynamics while exact closure supplies the physical spin-1 sum.
  Evolving the previous `model_total` would retain legacy response
  coefficients, while adding CP response members would double count them.
- Classification: exact composition rule; phenomenological response
  strengths.
- Numerical evidence: all 18+18 functions are present and nonzero somewhere,
  minimum eigenvalues are \(4.13\times10^{-4}\) and \(2.09\times10^{-2}\),
  the maximum CP recomposition shift is below 3% of local \(f_1\), exact
  quark link reversal is restored, and no final positivity contraction is
  required.
- Files/tests: `build_wp12_canonical_composed_parent.py`,
  `resolved_nuclear_parent.py`, `build_wp12_resolved_nuclear_parent.py`,
  `build_wp12_scientific_inspection.py`,
  `wp12_scientific_inspection.json`,
  `test_wp12_canonical_composed_parent.py`,
  `test_resolved_nuclear_parent.py`,
  `test_wp12_resolved_nuclear_output.py`,
  `test_wp12_scientific_inspection.py`.
- Revision trigger: a fitted/lattice-constrained joint-spin nuclear kernel
  or a change of factorization/evolution scheme.

# D-120: basis completion does not authorize evolution before evidence parity

- Date: 2026-07-27
- Status: governing and accepted
- Question: Is a complete, smooth, positive 18+18 TMD basis sufficient to
  begin final evolution?
- Decision: No. Every TMD must first pass WP12-E, an \(f_1\)-level evidence
  standard covering flavor-resolved proton input, explicit neutron
  construction and CSB status, uncertainty, common-parent consistency,
  channel-appropriate nuclear dressing, and physical validation.
- Justification: prior audits established algebraic and numerical
  completeness but allowed heterogeneous evidential quality. Treating those
  as equivalent disguises model-dominated tensor/gluon sectors as being as
  determined as \(f_1\).
- Alternative considered: evolve immediately and improve inputs later;
  rejected because evolution would harden temporary assumptions into the
  production boundary.
- Classification: scientific acceptance rule.
- Revision trigger: the WP12-E machine-readable audit passes every required
  sector without structural-only or unquantified entries.

# D-121: WP12-E evidence parity closes at the declared pre-evolution scope

- Date: 2026-07-27
- Status: governing and accepted
- Decision: Accept all 36 quark/gluon rows for entry into rank-aware
  evolution, with statistical covariance distinguished from interval,
  wave-function, nuclear, and model sensitivity axes.
- Evidence: `wp12_evidence_parity_matrix.json` reports 36/36 pass;
  `wp12e_acceptance.json` passes evidence, resolved closure, complete bases,
  PDF/CSB propagation, and band-ordering gates.
- Important limitation: passing evidence parity does not convert
  tensor-polarized or gluon model predictions into experimental fits.
  Yang-2024 interval corners are not its unavailable replica covariance.
- Revision trigger: new public fit replicas, lattice calculations, or
  process data replace the corresponding named sensitivity interface.

# D-122: one authoritative construction note governs model interpretation

- Date: 2026-07-27
- Status: governing and accepted
- Question: How should the original `Deuteron_GTMD.pdf`, the intervening
  refocusing decisions, and the present pre-evolution implementation be
  reconciled for future sessions?
- Decision: `references/model_construction_note.tex` is the authoritative
  scientific and narrative model description. It preserves the original GTMD-first parent
  architecture, records why the real one-body and reduced-amplitude
  boundaries were insufficient, inventories every accepted physical and
  uncertainty component, and states the exact pre-evolution scope. The PDF
  edition is generated by Tectonic, not edited independently. The former
  Markdown/ReportLab summary is superseded because it did not meet the
  required technical standard.
- Justification: the implementation accumulated across many audits and
  refocusing steps. A single provenance-backed note prevents obsolete
  smooth closures, constituent plots, or old 19-gluon bookkeeping from being
  mistaken for the canonical model.
- Classification: documentation and scientific interpretation contract.
- Files/tests: `references/model_construction_note.tex`,
  `environment-latex.yml`,
  `output/pdf/model_construction_note.pdf`, `AGENTS.md`, `handoff/README.md`.
- Revision trigger: any change to the declared TMD basis, canonical
  composition, input provenance, evidence status, validation state, or
  evolution boundary.

# D-123: PRC106 set A supersedes PRC99 as the Norfolk-current benchmark

- Date: 2026-07-27
- Status: governing and implemented
- Question: Which constants and magnetic-moment decomposition should govern
  the Norfolk current after Alex Gnech's reply?
- Decision: Use PRC106 Table-II set A as the reference LEC set and PRC106
  Table IV as the deuteron magnetic-moment benchmark. Preserve the
  post-Fierz comparison values from `comparison.pdf` as historical mapping
  information only. The confirmed regulator prescription is
  \(I_k\to C_{R_L}I_k\).
- Evidence: With the PRC106-A constants the calculated \(d_1^S\) contact
  contribution agrees with Table IV within the quoted LEC error for every
  Norfolk model. The separated \(d_2^S\) OPE \(I_1/I_2\) pieces do not
  reproduce Table IV; the OPE term remains excluded from production.
- Classification: author-confirmed convention and phenomenological fit
  choice; unresolved operator-level OPE convention.
- Files/tests: `references/gnech_norfolk_current_reply.md`,
  `src/deuteron_wigner/two_body_current.py`,
  `scripts/benchmark_norfolk_prc106_set_a.py`,
  `tests/test_norfolk_current.py`.
- Revision trigger: Alex supplies direct Monte Carlo unit-\(d_2^S\)
  \(I_1/I_2\) values or a corrected operator/radial convention.

# D-124: a genuinely predictive model requires a microscopic model-class transition

- Date: 2026-07-27
- Status: governing and accepted
- Question: Can the present parent-consistent phenomenological assembly, or
  its complete TMD evolution, be described as a fundamental prediction?
- Decision: No. The present model remains a constrained phenomenological
  synthesis. A genuinely predictive next-level model must derive the quark,
  antiquark, gluon, spin/OAM, tensor, nuclear, and process-dependent sectors
  from one renormalized microscopic light-front state (or an explicitly
  equivalent bound-state framework), with controlled Fock/regulator
  convergence, dynamical Wilson lines, common GTMD reductions, consistent
  currents, QCD matching/evolution, correlated parameter inference, and
  withheld-observable validation.
- Justification: assembling individually fitted or modeled TMD inputs can be
  self-consistent and phenomenologically useful, but it does not create the
  cross-channel correlations or falsifiable predictions that follow from a
  common microscopic state.
- Alternatives considered: (i) call the existing common-parent composition
  fundamental; rejected because important parent amplitudes are calibrated
  from separate external inputs; (ii) complete evolution and then relabel the
  result predictive; rejected because evolution transports rather than
  supplies microscopic dynamics.
- Classification: scientific interpretation and architecture requirement.
- Files/tests: `references/model_construction_note.tex`, Section 15;
  `handoff/ROADMAP.md`, WP13; `AGENTS.md`; compiled and visually audited
  `output/pdf/model_construction_note.pdf`.
- Revision trigger: only a completed WP13 acceptance audit satisfying all
  twelve criteria in Section 15.10.
