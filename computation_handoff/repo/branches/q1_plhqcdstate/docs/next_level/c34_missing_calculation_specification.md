# Missing C34 finite-basis one-loop soft calculation

## Exact no-go and continuation

C34/S0A ends at

```text
C34_SOFT_ONE_LOOP_INCOMPLETE
```

because a complete, gauge-consistent one-loop coefficient cannot be formed in
the declared C33 finite-cell regulator.  The exact continuation is

```text
C35/S0C — targeted unresolved soft-diagram and counterterm completion
```

The missing object is

\[
 S_{\rm FB}^{\rm bare}
 (b_T;\mathfrak R_{\rm soft},\delta^+,\delta^-,\xi_g)
 =1+a_s C_F\,s_{\rm FB}^{[1],\rm bare}
 +\mathcal O(a_s^2),
\]

where C35 must either retain the displayed \(C_F\) outside
\(s_{\rm FB}^{[1]}\), or define a different convention explicitly and provide
an exact conversion.  C34 has no numerical value for
\(s_{\rm FB}^{[1],\rm bare}\).  Missing is not zero.

## 1. Complete the regulator before integrating

The existing C33 records fix a root, state count, nominal support, and operator
identity.  C35 must add a versioned, content-addressed **regulator
realization** without mutating those historical records.

### 1.1 Light-front and metric normalization

Freeze explicitly:

- metric signature;
- \(v^\pm=(v^0\pm v^3)/\sqrt2\);
- normalized \(n^\mu,\bar n^\mu\) and \(n\!\cdot\bar n\);
- whether \(n\!\cdot k=k^-\), \(\sqrt2 k^-\), or a rescaled component;
- the corresponding rescaling of Wilson parameters and \(\delta^\pm\);
- Fourier phase and \(d^2k_T/(2\pi)^2\) normalization;
- \(D_\mu=\partial_\mu-igA_\mu\) and generator conventions;
- \(a_s=\alpha_s/(4\pi)=g_s^2/(4\pi)^2\) and the placement of \(C_F\).

This removes the current \(\sqrt2\) and coefficient-normalization ambiguity.

### 1.2 Gauge-complete B=0 dynamics

Choose one, and only one, primary realization:

1. a covariant-gauge finite-cell action with all four gauge polarizations,
   indefinite/Krein metric, BRST condition, Faddeev-Popov sector, and a proved
   physical projection; or
2. a light-front/physical-polarization Hamiltonian with its exact gauge pole
   prescription, constrained fields, instantaneous kernels, transverse
   boundary links, and a proof that it reproduces the target covariant result;
   or
3. an explicitly projected covariant propagator/contraction formulation proven
   equivalent to the finite-cell Hilbert realization.

The existing two-transverse-polarization count cannot be used simultaneously
as an unproved covariant \(\xi_g=0,1,2\) basis.  The chosen realization must
define the free action or Hamiltonian, vacuum normalization, propagator or
energy denominators, commutators, state metric, ghost treatment, and all
instantaneous/constrained contributions.

### 1.3 Executable mode cells

For each R1-R3 resolution, and any added R4 or axis-isolation grids, store or
deterministically generate:

- every cell's lower and upper boundaries;
- quadrature nodes and weights;
- basis function \(\phi_\nu(k)\);
- phase-space measure and Jacobian;
- the definition of \(\omega\);
- the relation among \(\omega,y,k^+,k^-,k_T\);
- on-shell dispersion for cut states;
- the virtual spectral or light-front energy-denominator prescription;
- the two-dimensional map from transverse indices to \(k_T\);
- polarization vectors and completeness relation;
- adjoint-color normalization;
- the finite-volume boundary condition and allowed momenta;
- normalization
  \(\int_{C_\nu}d\Pi(k)|\phi_\nu(k)|^2=1\);
- an exact refinement/injection map between successive grids.

The present descriptor hashes must not be described as hashes of these modes.
A new mode-collection hash must cover the actual generated content.

The separate \(n\)- and \(\bar n\)-rapidity-region labels require a partition
of unity or a signed overlap subtraction.  Merely summing both copies is not a
count-once prescription.

### 1.4 Wilson path realization

Parameterize every path segment:

\[
 x_\ell^\mu(s),\qquad \dot x_\ell^\mu(s),
\]

including its finite representation of lightlike infinity, transverse
closure, junctions, orientation, path order, conjugation, and endpoint limit.
Derive every emission and absorption vertex from

\[
 ig\int ds\,\dot x_\ell\!\cdot A^a(x_\ell(s))T_\ell^a
\]

and apply the modified-delta damping at the operator level.  The result must
recover the four stored single-gluon pole signs and must also fix the numerator
signs, phases, tangent normalization, and conjugate generator action.

### 1.5 IR, rapidity, UV, and zero-mode regulators

Keep four distinct roles:

- finite-basis UV/volume truncation;
- a declared soft IR prescription;
- operator-level modified-delta rapidity regulation;
- numerical quadrature control.

Define how the soft IR prescription enters the C32 spacelike-off-shell
soft-limit comparison.  Do not claim automatic equivalence from a pure-DR
zero-bin theorem.

Materialize the exact-zero-mode control as a constrained sector, analytic
boundary distribution, or proved non-applicability.  It must test its effect
on the Ward identity, rapidity logarithm, line self energy, endpoint term, and
finite conversion constant.

## 2. Calculate the one-gluon current

Construct

\[
 J_a^\mu(k;b_T)
 =g\sum_{\ell=1}^4
 \mathcal T_\ell^a\sigma_\ell v_\ell^\mu
 e^{ik_T\cdot x_{\ell T}}
 D_\ell(k;\delta^\pm,i0)
\]

from the parameterized lines, not from manually entered pole signs.  Then
compute true cell integrals

\[
 V^a_{\lambda\nu}
 =\int_{C_\nu}d\Pi(k)\,
 \phi_\nu^*(k)\,
 \epsilon_{\lambda\mu}^*(k)
 J_a^\mu(k;b_T).
\]

Required operator checks are:

- exact zero-coupling limit;
- fundamental/conjugate color action and \(C_F=4/3\);
- emission/absorption conjugation;
- future/past path reversal;
- \(k_\mu J^\mu\) including finite-\(\delta\) terms and the ordered
  \(\delta\to0\) limit;
- cell normalization and finite-span completeness;
- direct matrix versus sparse/matrix-free action;
- no physical numerical epsilon.

## 3. Resolve every one-loop contribution

The following table is the exact C35 starting queue.

| Contribution | C34 status | Missing calculation/proof |
|---|---|---|
| `N_NBAR_EXCHANGE` | `UNRESOLVED_BLOCKING` | Cell-integrated \(n\)-\(\bar n\) pair kernel with color, gauge, real/virtual, and rapidity support. |
| `CONJUGATE_LINE_EXCHANGE` | `UNRESOLVED_BLOCKING` | Conjugate pair kernel and Hermitian/path-reversal equality. |
| `SAME_DIRECTION_LINE_EXCHANGE` | `UNRESOLVED_BLOCKING` | Finite-regulator evaluation; target scalelessness is insufficient. |
| `REAL_ONE_SOFT_GLUON` | `UNRESOLVED_BLOCKING` | On-shell cut measure, cell integration, and \(b_T\) measurement. |
| `VIRTUAL_ONE_SOFT_GLUON` | `UNRESOLVED_BLOCKING` | Virtual spectral/energy denominator and contour prescription. |
| `WILSON_LINE_SELF_ENERGY` | `UNRESOLVED_BLOCKING` | Logarithmic versus power/length divergence and subtraction. |
| `CUSP_ENDPOINT` | `UNRESOLVED_BLOCKING` | Junction kernels and endpoint counterterms. |
| `TRANSVERSE_CLOSURE` | `UNRESOLVED_BLOCKING` | Finite transverse-at-infinity path contribution. |
| `AUXILIARY_FIELD_SELF_ENERGY` | `UNRESOLVED_BLOCKING` | Supply a regulator-scope non-applicability proof for the unselected, nonadditive auxiliary plan, or an explicitly separate auxiliary cross-check. |
| `SOFT_VACUUM_ENERGY` | `UNRESOLVED_BLOCKING` | Connected/disconnected cancellation in the normalized finite vacuum. |
| `LIGHT_FRONT_INSTANTANEOUS` | `UNRESOLVED_BLOCKING` | Calculate in an LF realization or prove non-applicability of the chosen covariant realization. |
| `GAUGE_FIXING` | `UNRESOLVED_BLOCKING` | Gauge-complete propagator/action and \(\xi_g\) cancellation. |
| `GHOST` | `UNRESOLVED_BLOCKING` | Store the finite-basis gauge-fixed action and connected-\(O(g^2)\) vertex-counting proof before issuing non-applicability. |
| `ZERO_MODE` | `UNRESOLVED_BLOCKING` | Constrained zero-mode/control calculation. |
| `BASIS_BOUNDARY` | `UNRESOLVED_BLOCKING` | Boundary kernels and refinement sensitivity. |
| `RAPIDITY_COUNTERTERM` | `UNRESOLVED_BLOCKING` | Extract only after bare \(\delta^+\), \(\delta^-\) dependence is calculated. |
| `UV_COUNTERTERM` | `UNRESOLVED_BLOCKING` | Solve after cutoff log/power/cusp/endpoint structures are separated. |
| `RESIDUAL_LINE_MASS_COUNTERTERM` | `UNRESOLVED_BLOCKING` | Determine finite-cutoff line-length divergence or prove absence. |

For every calculated entry store the complete line/cut/cell ancestry,
symbolic-expression hash, generated-code hash, color factor, gauge dependence,
UV/IR/rapidity support, cancellation partner, and independent oracle.

All eighteen C34 machine statuses are currently `UNRESOLVED_BLOCKING`.
Auxiliary self energy and the connected ghost term are proof candidates, not
current non-applicability decisions.

Assemble the result independently by:

1. expansion and vacuum contraction of the Wilson operator; and
2. a cell-resolved cut/spectral construction.

The two routes must agree before `C34_FINITE_BASIS_SOFT_ONE_LOOP_VALIDATED` can
ever be superseded into a positive descendant status.

Do not decide physical real/virtual branches from the topology name.  The C34
cut ledger contains candidate topology roles only.  C35 must derive each branch
from the executed cut prescription, keep the direct and separate-control bare
terms disjoint from the auxiliary route and from counterterms, and then prove
count-once agreement.  Counterterm IDs must remain disjoint from graph IDs.

## 4. Use the continuum result only as a target

Reproduce the source convention

\[
 \widetilde S=\exp[a_sC_F(S^{[1]}+\cdots)],
 \qquad a_s=\frac{\alpha_s}{4\pi}=\frac{g_s^2}{(4\pi)^2},
\]

and

\[
 S^{[1]}=-4\mu^{2\epsilon}B^\epsilon\Gamma(-\epsilon)
 [L_0-\psi(-\epsilon)-\gamma_E],
 \qquad B=\frac{b_T^2}{4},
 \qquad \delta=\pm\delta^+\delta^-,
 \qquad L_0=\ln(B|\delta|e^{2\gamma_E}).
\]

Use (L_\mu=\ln(\mu^2B e^{2\gamma_E})\),
(l_\delta=\ln(\mu^2/|\delta^+\delta^-|)\), and
(d^{(1,1)}=2C_F=\Gamma_0/2\) when checking the source Laurent expansion.

Perform both a source transcription and an independent scalar-integral or
symbolic reconstruction.  Verify the cancellation of fractional rapidity
powers, the Laurent expansion, rapidity-log derivative, color/cusp
normalization, and future/past equality.

This target does not define finite-cell weights, power divergences, zero-mode
remainders, or finite conversion constants.  It may test the final C35 result;
it may not generate it.

## 5. Solve UV and rapidity renormalization

Once the complete bare result exists, decompose

\[
 s_{\rm FB}^{[1],\rm bare}
 =A_{\rm power}(\Lambda)
 +A_{\log}\ln\Lambda
 +A_{\rm cusp}L_b^2
 +A_{\rm rap}\ln(\delta^+\delta^-)
 +A_{\rm finite}+R .
\]

Keep separate counterterms for:

- individual-line self energy;
- cusp and endpoint junctions;
- transverse closure;
- residual line mass or length divergence;
- vacuum normalization/energy where applicable;
- the composite soft operator.

Then construct

\[
 S_{\rm FB}^{\rm ren}
 =Z_S^{\rm UV}R_S^{\rm rap}S_{\rm FB}^{\rm bare}
\]

while retaining \(\delta^+\) and \(\delta^-\) independently until the
rapidity counterterm is applied.  Store the exact rapidity derivative
convention and test:

- UV cutoff cancellation up to a typed power remainder;
- rapidity-regulator cancellation;
- \(\xi_g=0,1,2\) equality;
- future/past and Hermitian closure;
- the \(\mu\) derivative against the quark cusp anomalous dimension;
- state and hadron independence.

No ART25 Collins-Soper model may enter this calculation.

The frozen C34 probes vary one rapidity regulator at a time: the plus probes
hold \(\delta^-=0.003\,\mathrm{GeV}\), and the minus probes hold
\(\delta^+=0.002\,\mathrm{GeV}\).  Their separate holdouts are
\((0.0005,0.003)\,\mathrm{GeV}\) and
\((0.002,0.00075)\,\mathrm{GeV}\), respectively.  C35 may refine this
source-independent numerical schedule only through a new versioned record; it
must not replace it with a fixed-ratio diagonal scan or interpret these
regulator probes as physical parameters.

## 6. Build a valid trajectory and conversion

R1-R3 vary several regulator axes together and do not provide stored
refinement maps.  Add axis-isolation sequences and at least one independent
holdout.  If a log-plus-finite-plus-power ansatz is required, provide enough
independent resolutions to determine it without consuming the holdout.

Separate:

- UV support;
- IR/finite volume;
- rapidity window;
- transverse discretization;
- zero-mode control;
- endpoint/transverse-junction effects;
- quadrature error.

Only then form

\[
 Z_{\rm FB\to cont}^{S,(1)}
 =S_{\rm cont}^{(1),\rm ren}-S_{\rm FB}^{(1),\rm ren}
\]

with logarithmic, finite, power, zero-mode, endpoint, transverse, and numerical
remainders separate.  Validate the inverse, round trip, holdout prediction,
gauge independence, and rapidity anomalous dimension.

## 7. Complete only the soft side of the zero-bin interface

Materialize a content-addressed joint-regulator identity containing the exact
C32 and C35 regulator, gauge, IR, rapidity, Fourier, measurement, zero-mode,
boundary, and removal-order records.  Define the soft-side limit in those
coordinates without inventing C32 collinear coefficients.

The subsequent collinear package, not C35/S0C, must calculate the C32 soft
limit and test the operator-identical compatibility square.  Missing- and
duplicate-subtraction controls must have equal and opposite nonzero residuals
when the shared overlap is nonzero.

## Completion conditions for C35/S0C

C35/S0C may close only when:

1. the mode collection is executable and content-addressed;
2. the gauge representation is complete;
3. all required direct-plan one-loop slots are calculated or have exact
   regulator-specific non-applicability proofs;
4. direct Wilson and mode/cut assemblies agree;
5. UV and rapidity counterterms close;
6. gauge, path, Hermiticity, rotation, and cusp checks pass;
7. zero modes and boundaries are controlled;
8. the regulator trajectory has a true holdout;
9. finite-basis conversion and round trip pass;
10. the soft-side zero-bin object is executable;
11. no external fit/data/bridge information entered the calculation.

Until then, the C34 no-go remains authoritative and no proton TMD or bridge
route may be activated.
