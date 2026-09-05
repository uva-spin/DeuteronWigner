# Neff and Feldmeier: deuteron Wigner function and short-range correlations

Last updated: 2026-07-23

Source: `../../1610.04066v1.pdf`

Citation:

T. Neff and H. Feldmeier, "The Wigner function and short-range correlations in the deuteron,"
arXiv:1610.04066 [nucl-th]. The local PDF is the 15-page version dated January 19, 2018.

## Why this paper matters to DeuteronWigner

The paper demonstrates how a matrix-valued deuteron Wigner transform unifies coordinate-space,
momentum-space, angular, and spin-tensor information. It supplies:

- a clean density-operator definition of the Wigner matrix;
- exact coordinate and momentum marginals;
- a practical Gaussian-basis evaluation strategy;
- explicit separation of spin-resolved and spin-averaged reductions;
- a physical interpretation of negative and oscillatory Wigner regions;
- useful diagnostics for short-range and tensor correlations;
- a warning that high momentum need not imply short distance for nonlocal interactions.

Its calculation is instant-form and three-dimensional. It is not directly the light-front,
transverse nuclear Wigner kernel required by `Deuteron_GTMD.pdf`. Its role is to guide the
algebra, tests, qualitative expectations, and wave-function diagnostics.

## Definitions

For a density operator \(\hat\rho\), the three-dimensional Wigner transform is

\[
W(\mathbf r,\mathbf p)=\frac{1}{(2\pi)^3}
\int d^3s\,
\left\langle\mathbf r+\frac{\mathbf s}{2}\middle|\hat\rho\middle|
\mathbf r-\frac{\mathbf s}{2}\right\rangle e^{-i\mathbf p\cdot\mathbf s}.
\]

Equivalently in momentum representation,

\[
W(\mathbf r,\mathbf p)=\frac{1}{(2\pi)^3}
\int d^3\kappa\,
\left\langle\mathbf p+\frac{\boldsymbol\kappa}{2}\middle|\hat\rho\middle|
\mathbf p-\frac{\boldsymbol\kappa}{2}\right\rangle
e^{i\boldsymbol\kappa\cdot\mathbf r}.
\]

The sign pairing is therefore:

- coordinate off-diagonality \(\mathbf s\) uses \(e^{-i\mathbf p\cdot\mathbf s}\);
- momentum off-diagonality \(\boldsymbol\kappa\) uses
  \(e^{+i\boldsymbol\kappa\cdot\mathbf r}\).

For deuteron spin \(S=1\), the most informative object is a matrix in spin-projection space:

\[
W_{M_S M'_S}(\mathbf r,\mathbf p)=\frac{1}{(2\pi)^3}
\int d^3s\,
\left\langle\mathbf r+\frac{\mathbf s}{2};SM_S\middle|\hat\rho\middle|
\mathbf r-\frac{\mathbf s}{2};SM'_S\right\rangle
e^{-i\mathbf p\cdot\mathbf s}.
\]

The paper uses the unpolarized total-angular-momentum density operator

\[
\hat\rho=\frac{1}{2J+1}\sum_M |\Psi;JM\rangle\langle\Psi;JM|.
\]

Even after averaging over total \(J\) orientation, the spin-resolved Wigner components can retain
correlations between \(M_S\) and the directions of \(\mathbf r\) and \(\mathbf p\).

## Exact marginal identities

The implementation-relevant identities are

\[
\rho_{M_S}(\mathbf r)=\int d^3p\,W_{M_SM_S}(\mathbf r,\mathbf p),
\qquad
n_{M_S}(\mathbf p)=\int d^3r\,W_{M_SM_S}(\mathbf r,\mathbf p).
\]

The full off-diagonal coordinate density matrix can be reconstructed:

\[
\rho_{M_SM'_S}(\mathbf r;\mathbf r')
=\int d^3p\,
W_{M_SM'_S}\!\left(\frac{\mathbf r+\mathbf r'}2,\mathbf p\right)
e^{i\mathbf p\cdot(\mathbf r-\mathbf r')}.
\]

After tracing over spin,

\[
W(\mathbf r,\mathbf p)=\sum_{M_S}W_{M_SM_S}(\mathbf r,\mathbf p).
\]

For an unpolarized state it depends on \(r=|\mathbf r|\), \(p=|\mathbf p|\), and
\(\cos\vartheta=\hat{\mathbf r}\cdot\hat{\mathbf p}\). The angle-reduced function is

\[
W(r,p)=8\pi^2\int_{-1}^{1}d(\cos\vartheta)\,
W(r,p,\cos\vartheta).
\]

With this convention,

\[
\rho(r)=\int dp\,p^2W(r,p),\qquad
n(p)=\int dr\,r^2W(r,p).
\]

These identities should inspire exact numerical unit tests for the light-front transverse Wigner
kernel, with measures and Fourier factors adjusted to the selected light-front convention.

## Deuteron wave function and tensor structure

The instant-form wave function couples \(L=0,2\) and \(S=1\) to \(J=1\):

\[
\langle\mathbf r;SM_S|\Psi;JM\rangle
=\sum_{LM_L}
\langle LM_L,SM_S|JM\rangle\,
\psi_{JL}(r)Y_{LM_L}(\hat{\mathbf r}).
\]

The \(D\)-wave component and its interference with the \(S\)-wave generate spin-space tensor
correlations. The paper finds:

- low momenta, approximately \(p\lesssim1\ \mathrm{fm}^{-1}\), show little spin-shape
  correlation;
- the strongest tensor anisotropy occurs in the intermediate region around
  \(p\sim1.5\ \mathrm{fm}^{-1}\), where the \(S\)-wave has a node and the \(D\)-wave becomes
  relatively dominant;
- still higher momentum contributions are more localized but show less tensor anisotropy.

This suggests targeted diagnostics for our LF helicity-density implementation:

1. Decompose results into \(S\)-\(S\), \(S\)-\(D\), \(D\)-\(S\), and \(D\)-\(D\) terms.
2. Verify that tensor-density signals are driven primarily by interference and \(D\)-wave terms.
3. Examine contributions by internal-momentum bands instead of only integrated observables.

The exact momentum scales will change with convention and wave-function input, so these are
qualitative diagnostics, not hard-coded thresholds.

## Wigner negativity and interference

The Wigner function is a quasi-distribution and may be negative. The paper's most important
interpretive result is that short-range correlations are not a positive high-momentum component
simply added to a positive low-momentum background. Interference is essential.

A two-Gaussian model writes

\[
\psi=\alpha_1\psi_1+\alpha_2\psi_2
\]

with a broad, long-range Gaussian and a narrow, short-range Gaussian of opposite relative sign.
The density and Wigner function contain two diagonal terms plus an interference term:

\[
W=W_{11}+W_{22}+W_{12}.
\]

The diagonal Gaussian Wigner functions are positive. The cross term is larger than the direct
short-range contribution in important regions and produces:

- the short-distance correlation hole through cancellation;
- the intermediate-momentum node/dip;
- negative regions of partial distributions;
- oscillations approximately following \(rp=\mathrm{constant}\).

Therefore:

- do not enforce pointwise positivity on the nuclear Wigner quasi-distribution;
- do enforce positive semidefiniteness on the density matrix before Wigner transformation;
- retain off-diagonal/interference terms in wave-function-component decompositions;
- do not interpret additive Wigner-region integrals as observable probabilities unless the
  phase-space smearing is physically adequate.

## Gaussian-basis strategy

The authors expand each radial component in Gaussians,

\[
\psi_{JL}(r)=\sum_k r^L e^{-r^2/(2a_k)}\psi^{JL}_k,
\]

using a geometric width grid \(a_k=a_0\,2^k\). This makes the Wigner integral analytic term by
term. For a pure \(S\)-wave basis pair with widths \(a_m,a_n\), the result contains

\[
\exp\left[
-\frac{2r^2}{a_m+a_n}
-2i\frac{a_m-a_n}{a_m+a_n}\mathbf r\cdot\mathbf p
-\frac{2a_ma_n}{a_m+a_n}p^2
\right].
\]

The complex phase from unequal widths creates the oscillatory interference. Pairing the conjugate
terms cancels imaginary parts, leaving real oscillations. When one width is much larger than the
other, the phase approaches \(e^{\pm2i\mathbf r\cdot\mathbf p}\). Angular integration produces
\(\sin(2rp)/(rp)\).

Possible use in this project:

- fit or transform supplied radial wave functions to a controlled Gaussian basis;
- use analytic Gaussian overlap integrals as a reference backend;
- compare against a direct numerical quadrature backend;
- use the analytic single-Gaussian result as a normalization and Fourier-sign fixture.

The paper's full \(L>0\) analytic construction uses solid and tripolar spherical harmonics,
Clebsch-Gordan coefficients, and Wigner \(6j/9j\) recoupling. Reproducing that machinery is not
automatically necessary for the first LF implementation. It is valuable if Gaussian analytic
evaluation becomes the chosen production strategy.

## Partial phase-space diagnostics

The paper defines partial momentum distributions by integrating over selected distance ranges,

\[
n_{\lessgtr}(p)=
\int_{r\lessgtr r_{\mathrm{sep}}}dr\,r^2W(r,p),
\]

and partial coordinate densities by selected momentum ranges,

\[
\rho_{\lessgtr}(r)=
\int_{p\lessgtr p_{\mathrm{sep}}}dp\,p^2W(r,p).
\]

These partial objects may be negative and are diagnostic decompositions, not probabilities.
They show:

- for the local AV8' interaction, small-distance regions account for the sufficiently
  high-momentum tail;
- the low-momentum region is dominated by large-distance pairs;
- high-momentum contributions become negative at small distance and create the correlation hole
  through cancellation;
- SRG softening suppresses the high-momentum shoulder and oscillations while leaving the
  low-momentum Wigner region nearly unchanged.

Analogous LF diagnostics could integrate over selected \(p_T\), \(y\), or transverse-position
ranges. They should be clearly labeled as quasi-distribution diagnostics.

## Crucial warning: high momentum is not synonymous with short distance

The local AV8' interaction gives a comparatively clean correlation between high momentum and
short distance. The nonlocal N3LO regulator alters the wave function even at larger distances and
generates high-momentum components there. High momentum is mathematically tied to rapid
variation or curvature, not uniquely to small separation.

Consequences for DeuteronWigner:

- comparisons between AV18/CD-Bonn/chiral wave functions must distinguish physical
  short-range structure from regulator/nonlocality effects;
- "SRC contribution" should not be defined solely by a momentum cut;
- wave-function or interaction dependence is a genuine model uncertainty;
- any coordinate-momentum localization statement must be checked through the Wigner kernel,
  not inferred from a marginal alone.

## Angular correlations

The full scalar Wigner function depends strongly on the angle between \(\mathbf r\) and
\(\mathbf p\):

- parallel or antiparallel configurations show strong oscillations and larger high-momentum
  contributions;
- perpendicular configurations are smoother and dominated by low momentum;
- SRG softening strongly reduces the high-momentum oscillations.

The paper relates the interference pattern to \(\mathbf r\cdot\mathbf p\). For our transverse
kernel, an analogous diagnostic is the azimuthal dependence on
\(\mathbf R_T\cdot\mathbf p_T\), including harmonics generated by \(S\)-\(D\) interference and
spin-tensor projections.

## Relationship to the planned LF nuclear Wigner kernel

The project brief proposes

\[
W^N_{\Lambda'\Lambda}(y,p_T,R_T)
=\int\frac{d^2\Delta_T}{(2\pi)^2}
e^{-i\Delta_T\cdot R_T}
\rho^N_{\Lambda'\Lambda}(y,p_T,\Delta_T),
\]

where the off-forward density is an overlap of LF wave functions shifted by recoil factors.

Structural correspondences:

| Neff-Feldmeier object | Planned project object |
|---|---|
| \(W_{M_SM'_S}(\mathbf r,\mathbf p)\) | \(W^N_{\Lambda'\Lambda}(y,p_T,R_T)\), with retained nucleon spin indices when needed |
| Coordinate off-diagonal density matrix | LF off-forward wave-function overlap |
| Fourier variable \(\mathbf s\leftrightarrow\mathbf p\) | \(\Delta_T\leftrightarrow R_T\) for nuclear transverse imaging |
| Spin trace | \(U,L,T,LL,LT,TT\) helicity/tensor projections |
| Coordinate and momentum marginals | \(R_T\), \(p_T\), helicity, and ultimately GTMD marginal tests |
| \(S\)-\(D\) interference | Tensor-polarized LF density and \(\delta_T\rho^N\) |

Non-correspondences that must not be blurred:

- instant-form relative momentum \(p\) is not the LF pair \((y,p_T)\);
- three-dimensional separation \(\mathbf r\) is not simply transverse \(R_T\);
- canonical spin projection \(M_S\) is not LF helicity;
- the paper has no Melosh rotation, LF Jacobian, active-constituent recoil mapping, or partonic
  gauge link;
- its nuclear Wigner transform is not a QCD partonic Wigner distribution and not a TMD
  \(b_{\mathrm{TMD}}\)-space transform.

## Proposed tests derived from this reference

These can be implemented before production physics inputs are complete:

1. **Gaussian positivity fixture:** a single normalized Gaussian \(S\)-wave produces a positive
   analytic Wigner function whose coordinate and momentum marginals are exact.
2. **Two-Gaussian interference fixture:** opposite-sign broad and narrow components produce
   negative/oscillatory cross terms while the underlying density matrix remains positive.
3. **Hermiticity/reality test:** conjugate basis-pair contributions cancel imaginary parts for a
   Hermitian density operator.
4. **Marginal reconstruction test:** integrate the Wigner kernel to recover diagonal momentum or
   transverse-position densities within a stated tolerance.
5. **Off-diagonal reconstruction test:** inverse-transform the Wigner representation to recover
   the starting density matrix.
6. **Component audit:** separately track \(S\)-\(S\), \(S\)-\(D\), \(D\)-\(S\), and \(D\)-\(D\)
   contributions; their sum must reproduce the full result.
7. **Rotation/azimuth test:** the unpolarized reduction depends only on allowed scalar products;
   tensor channels carry only the expected harmonics.
8. **No false positivity test:** allow negative Wigner values while requiring the pre-transform
   helicity density matrix to be positive semidefinite.
9. **Interaction sensitivity test:** compare local and nonlocal wave-function inputs before
   labeling high-\(p_T\) strength as short range.

## Implementation implications

- Keep a matrix-valued kernel until the final requested spin projection. Premature spin tracing
  discards tensor information.
- Preserve complex amplitudes internally even when a final scalar reduction is real.
- Store wave-function component labels so interference can be inspected.
- Build exact measure and Fourier-normalization tests before fitting physical data.
- Consider a Gaussian-expansion reference backend, but do not commit to it until LF spin rotations
  and available AV18/CD-Bonn inputs are assessed.
- Treat Wigner plots as diagnostics of quantum interference, not probability heat maps.
