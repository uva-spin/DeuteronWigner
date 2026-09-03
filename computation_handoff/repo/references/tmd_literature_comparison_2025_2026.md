# Spin-1 quark and gluon TMD literature comparison

## Sources

1. J. Poudel, A. Bacchetta, J.-P. Chen, and N. Santiesteban,
   "Experimental study of tensor structure function of deuteron,"
   *Eur. Phys. J. A* **61**, 81 (2025),
   DOI: 10.1140/epja/s10050-025-01558-w.
2. X. Xie, D.-Y. Chen, and Z. Lu,
   "Gluon TMDs for tensor polarized deuteron in a spectator model,"
   arXiv:2603.15224v1 (2026).

Local immutable copies are under `data/raw/literature/`.

## Executive comparison

EPJ A 61:81 is an experimental/formalism review. It does not publish a
numerical deuteron quark-TMD calculation. Its central value for this project
is the longitudinal-tensor SIDIS cross section and the five tensor structure
functions in Eqs. (5a)-(5e). It also fixes the inclusive convention

\[
b_1(x)=\frac12\sum_{q,\bar q}e_q^2\,\delta q(x).
\]

After translating its parity-reduced notation,
\(\delta q=q^0-\tfrac12(q^{+1}+q^{-1})\). This is the same helicity
difference stored internally as `deltaT_f1`.

Xie, Chen, and Lu provide an operator parametrization and spectator-model
calculation for the complete leading-twist spin-1 gluon TMD basis. Their
Table I contains 19 functions. Six are T-odd and vanish in their tree-level
calculation; the remaining 13 are evaluated. Their input is a direct
deuteron-gluon-spin-1-spectator vertex fitted to the nNNPDF1.0 deuteron
unpolarized gluon PDF at \(Q_0=2\) GeV. It is not a convolution of nucleon
gluon TMDs with a deuteron wave function. In this project the paper is used
only to compare correlator decompositions, tensor structures, ranks, names,
and projector results. Its spectator model is not adopted as a physics
input or phenomenological baseline.

## Quark structure-function map

| Published structure function | Twist | Published TMD content | Project status |
|---|---:|---|---|
| \(F_{U(LL),T}\) | 2 | \(\mathcal C[f_{1LL}D_1]\) | Implemented as the convention-safe `deltaT` rank-zero SIDIS structure, up to an explicit \(S_{LL}\leftrightarrow\delta_T\) normalization adapter |
| \(F_{U(LL),L}\) | 2 | \(0\) | Consistent; no longitudinal-photon term is generated |
| \(F_{U(LL)}^{\cos\phi_h}\) | 3 | \(h_{LL}H_1^\perp\), \(f_{1LL}\widetilde D^\perp\), \(f_{LL}^{\perp}D_1\), \(h_{1LL}^{\perp}\widetilde H\) | Not implemented |
| \(F_{U(LL)}^{\cos2\phi_h}\) | 2 | \(h_{1LL}^{\perp}H_1^\perp\) with rank-2 weight | Not implemented |
| \(F_{L(LL)}^{\sin\phi_h}\) | 3 | \(e_{LL}H_1^\perp\), \(f_{1LL}\widetilde G^\perp\), \(g_{LL}^{\perp}D_1\), \(h_{1LL}^{\perp}\widetilde E\) | Not implemented |

The present `rank_zero_sidis_structure` is therefore a faithful implementation
of Eq. (5a)'s radial W term, not of the complete longitudinal-tensor SIDIS
cross section in Eq. (4).

## Complete leading-twist quark and antiquark map

The definite-rank classification follows Eqs. (11)-(20) and Table I of
T. van Daal, arXiv:1612.06585. Antiquarks carry the same operator basis.

| Target channel | Unpolarized quark \(\gamma^+\) | Longitudinal quark \(\gamma^+\gamma_5\) | Transverse quark \(i\sigma^{i+}\gamma_5\) |
|---|---|---|---|
| U | \(f_1\) (0) | - | \(h_1^\perp\) (1, T-odd) |
| L | - | \(g_1\) (0) | \(h_{1L}^\perp\) (1) |
| T | \(f_{1T}^\perp\) (1, T-odd) | \(g_{1T}\) (1) | \(h_1\) (0), \(h_{1T}^\perp\) (2) |
| LL | \(f_{1LL}\) (0) | - | \(h_{1LL}^\perp\) (1, T-odd) |
| LT | \(f_{1LT}\) (1) | \(g_{1LT}\) (1, T-odd) | \(h_{1LT}\) (0, T-odd), \(h_{1LT}^\perp\) (2, T-odd) |
| TT | \(f_{1TT}\) (2) | \(g_{1TT}\) (2, T-odd) | \(h_{1TT}\) (1, T-odd), \(h_{1TT}^\perp\) (3, T-odd) |

There are 18 quark TMDs and 18 antiquark TMDs; nine in each set are T-odd.
The four ordinary collinear limits are \(f_1,g_1,h_1,f_{1LL}\).
\(h_{1LT}\) is the important exception: it has rank zero but no collinear
PDF because hermiticity and time reversal force its integral to vanish.

The code representations are `leading_twist_quark_registry(Species.QUARK)`
and `leading_twist_quark_registry(Species.ANTIQUARK)`.

### Normalization issue to keep explicit

The paper writes target tensor polarization as \(T_{\parallel\parallel}\) and
the named distribution \(f_{1LL}\). The code stores

\[
\delta_T f=f^{\Lambda=0}
-\frac12(f^{\Lambda=+1}+f^{\Lambda=-1}).
\]

No numerical comparison should identify these without an explicit
polarization-tensor normalization adapter. Ratios currently labeled
`deltaT_over_U` are convention-safe helicity differences, not automatically
the experimental coefficient multiplying \(T_{\parallel\parallel}\).
The standard \(S_{LL}\) eigenvalues give the exact adapter
\(f_{1LL}=-(2/3)\delta_T f\), now implemented in `conventions.py`.

## Complete leading-twist gluon map

Ranks below are the rank of the explicit symmetric-traceless transverse
momentum tensor in Eqs. (7)-(12).

| Target channel | Unpolarized gluon | Circular gluon | Linear gluon |
|---|---|---|---|
| U | \(f_1\) (0) | - | \(h_1^\perp\) (2) |
| L | - | \(g_1\) (0) | \(h_{1L}^\perp\) (2, T-odd) |
| T | \(f_{1T}^\perp\) (1, T-odd) | \(g_{1T}\) (1) | \(h_1\) (1, T-odd), \(h_{1T}^\perp\) (3, T-odd) |
| LL | \(f_{1LL}\) (0) | - | \(h_{1LL}^\perp\) (2) |
| LT | \(f_{1LT}\) (1) | \(g_{1LT}\) (1, T-odd) | \(h_{1LT}\) (1), \(h_{1LT}^\perp\) (3) |
| TT | \(f_{1TT}\) (2) | \(g_{1TT}\) (2, T-odd) | \(h_{1TT}\) (0), \(h_{1TT}^\perp\) (2), \(h_{1TT}^{\perp\perp}\) (4) |

This table is represented by `leading_twist_gluon_registry()`.

## Direct comparison with the current project

### Agreement

- The `U/L/T/LL/LT/TT` target-channel organization matches exactly.
- The current `deltaT_f1` gluon placeholder maps to the LL trace structure
  \(f_{1LL}\), modulo the tensor-normalization adapter required for quarks.
- The project treats gauge links as part of the correlator identity and keeps
  quark and gluon operators separate.
- The paper's \(h_{1TT}\) has rank zero and a nonzero collinear limit. This is
  the gluon double-helicity-flip or "gluon transversity" channel highlighted
  in the project brief.

### Missing

- No numerical gluon TMD or GTMD boundary model is connected to the nuclear
  convolution.
- The transverse gluon-index correlator now has an explicit Cartesian
  trace/circular/linear split and basis matrices for all U, L, T, LL, LT,
  and TT sectors of Eqs. (7)-(12). Synthetic compose/project tests recover
  every independent coefficient.
- In two transverse dimensions the matrices multiplying \(f_{1TT}\) and
  \(h_{1TT}^{\perp}\) are identical up to sign. The correlator therefore
  projects \(f_{1TT}-h_{1TT}^{\perp}\), matching the combination explicitly
  reported in Appendix A, rather than pretending the two coefficients are
  separately identifiable from \(\Phi^{ij}\).
- No rank-1 through rank-4 Fourier-Bessel machinery is connected to the TMD
  registry.
- No quark \(h_{1LL}^{\perp}\) or Collins fragmentation input exists, so the
  leading \(\cos2\phi_h\) tensor modulation cannot yet be calculated.
- Twist-3 quark distributions and tilde fragmentation correlators in Eqs.
  (5c) and (5e) are absent.
- Gauge-link-generated T-odd gluon functions remain absent, consistently
  with the tree-level spectator paper.

## Physics distinction and use boundary

The project's one-body nuclear convolution and the 2026 spectator model
describe different mechanisms:

- The convolution resolves proton and neutron partons embedded in a
  light-front deuteron wave function.
- The spectator model couples the deuteron directly to an off-shell gluon
  and a colored spin-1 spectator with a fitted continuous mass spectrum.

The spectator-model numerical curves are not project baselines. Only the
paper's operator-level correlator and resulting TMD decomposition are used
for comparison. The project's gluon results must instead be generated from
its own nucleonic, coherent, exchange-current, and non-nucleonic mechanism
layers.

For collinear \(h_{1TT}^g\), the simple one-body nucleon baseline should
vanish because a spin-1/2 nucleon cannot support the required two-unit
hadron-helicity flip. This makes the channel a useful null test of the
project's mechanism separation, independently of the spectator model.

## Recommended implementation order

1. Add explicit \(S_{LL}\), \(S_{LT}\), and \(S_{TT}\) convention adapters.
2. Implement the quark rank-2 \(h_{1LL}^{\perp}\) projector and
   \(F_{U(LL)}^{\cos2\phi_h}\).
3. Completed: transverse-index bases and synthetic inversion tests cover
   all six target sectors, with the TT identifiability relation explicit.
4. Compare every independently derived project gluon correlator coefficient
   with Eqs. (7)-(12), including signs, factors of \(M\), ranks, and T parity.
5. Generate numerical gluon TMDs only from the project's declared nuclear
   mechanisms and externally justified nucleon inputs.
