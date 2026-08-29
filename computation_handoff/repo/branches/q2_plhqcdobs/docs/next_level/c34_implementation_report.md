# C34/S0A implementation report

## Scientific result

C34/S0A reaches the rigorous fail-closed outcome

```text
C34_SOFT_ONE_LOOP_INCOMPLETE
```

and therefore follows **Branch G** of the authoritative C34 work package.  The
exact continuation is

```text
C35/S0C — targeted unresolved soft-diagram and counterterm completion
```

This result is not a failed numerical run and it is not an assertion that the
one-loop soft coefficient vanishes.  C34 establishes that the repository has
enough information to preserve the exact C33 tree root, type the one-loop
calculation, derive the four-line color and pole structure, and transcribe the
source-qualified continuum modified-delta target.  It does **not** have enough information to
define a unique, gauge-complete, regulator-specific finite-cell contraction.
Consequently, every unavailable finite-basis value remains an explicit
`UNRESOLVED_BLOCKING`/empty-not-zero quantity.

No continuum coefficient has been relabeled as a finite-basis result.  No
microscopic proton TMD has been exported, the twelve-point bridge has not been
rerun, and no fit, likelihood, posterior, calibration, optimization,
reweighting, emulator, process promotion, inference route, or production route
has been created.

## Baseline and source authority

The resolved C34 starting point is the clean local C33 completion HEAD

```text
e0b34c74e8f39c9d42cf49cc598f1533d9353a7e
```

with the pre-existing, intentionally untracked `MSHT20_REP/` directory outside
Git.  The required C32 and C28 ancestors remain ancestry requirements of the
C34 regression gate.  Exact baseline reproduction, final test counts, builder
counts, validator results, artifact hashes, and isolation checks are recorded
in `docs/next_level/c34_regression_report.json`; this narrative deliberately
does not duplicate mutable aggregate counts.

The authoritative Volume XXI source is

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
SHA-256 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4
```

Volume XXI supplies the operator architecture, required regulator identities,
renormalization and overlap conditions, benchmark families, and no-go logic.
It explicitly does not supply a finite-basis one-loop coefficient.  The C33
primary-source lock reaches the same conclusion: every retained continuum,
rapidity, zero-bin, auxiliary-field, finite-regulator-method, or light-front
comparison source is marked `NOT_OPERATOR_REGULATOR_IDENTICAL` to the selected
C33 finite-cell root.

## Preserved exact results

C34 preserves, without reinterpretation, the two-root identity

```text
C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION       B = 1
C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT    B = 0
```

The roots share neither a state vector nor a probability normalization.  The
vacuum soft factor is not a component of the C11 proton wave function.

The selected C33 realization remains

```text
S0-FB-EIKONAL-FOCK
```

and its exact tree identities remain

\[
  S_{\rm FB}^{(0)}(b_T)=1,
  \qquad
  C_F=\frac{N_c^2-1}{2N_c}=\frac43 .
\]

The C34 resolution and four-line records are not parallel hand-written copies.
The builder reads `c33_soft_basis_trajectory_plan.json`,
`c33_four_line_operator_manifest.json`, and
`c33_eikonal_denominator_report.json`, preserves each inherited record hash,
and executes a field-by-field comparison with
`default_four_line_operator()`.  Basepoint and representation spelling changes
(`b`/`bT`, `ANTI_FUNDAMENTAL`/`CONJUGATE_FUNDAMENTAL`) are explicit adapters,
not silent aliases.  The C33 descriptors declare nested support, but no
refinement map has been proved.

The ordered quark soft operator remains

\[
 S_{q,\mathrm{soft}}^{\mathrm{bare}}(b_T)
 =\frac1{N_c}
 \langle\Omega|\operatorname{Tr}[
 S_n^\dagger(b_T)S_{\bar n}(b_T)
 S_{\bar n}^\dagger(0)S_n(0)]|\Omega\rangle .
\]

The four stored line identities are:

| Order | Line | Representation/action | Ordering | Pole component |
|---:|---|---|---|---|
| 1 | \(S_n^\dagger(b_T)\) | conjugate fundamental | anti-path ordered | \(k^-+i\delta^-\) |
| 2 | \(S_{\bar n}(b_T)\) | fundamental | path ordered | \(k^+-i\delta^+\) |
| 3 | \(S_{\bar n}^\dagger(0)\) | conjugate fundamental | anti-path ordered | \(k^++i\delta^+\) |
| 4 | \(S_n(0)\) | fundamental | path ordered | \(k^--i\delta^-\) |

The table records the C33 single-gluon denominator convention.  It does not
silently fix the still-missing normalization of the lightlike vectors, line
parameterization, emission/absorption numerator signs, or finite-cell mode
functions.

## What C34 could derive safely

### Symbolic eikonal current

The one-gluon current can be typed at the operator level as

\[
 J_a^\mu(k;b_T)
 =g\sum_{\ell=1}^{4}
 \mathcal T_{\ell}^{a}\,\sigma_\ell\,v_\ell^\mu
 e^{i k_T\cdot x_{\ell T}}
 D_\ell(k;\delta^\pm,i0),
\]

where line identity, color action, conjugation, path order, transverse
basepoint, momentum component, and modified-delta pole sign descend from the
C33 records.  This is a valid symbolic operator contract.  It is not a
numerical eikonal vertex because the repository does not define the cell basis
functions, their measure, normalized gauge-field modes, or the full path
parameterization required to evaluate

\[
 \langle g^a_{\lambda,\nu}|J\!\cdot\!A|\Omega\rangle .
\]

In particular, a Ward residual cannot be promoted from the exact tree-level
path identity to a finite-delta, finite-cell one-loop result.

### Exact nonsingular transverse-cell phase

C34 implements one deliberately limited analytic cell operation: the
normalized rectangular-cell average of the nonsingular Fourier phase,

\[
 \overline P_C(b_T)
 =\frac{1}{\Delta k_x\Delta k_y}
   \int_{k_{x,0}}^{k_{x,1}}\!dk_x
   \int_{k_{y,0}}^{k_{y,1}}\!dk_y\,
   e^{i(k_xb_x+k_yb_y)}.
\]

It has the exact \(b_T=0\) value one and is evaluated with a stable analytic
exponential-difference expression rather than center sampling.  This validates
only the transverse phase for a typed rectangular cell.  The C34 example cell
and frozen quadrature *plan* do not generate the complete R1-R3 mode
collections, do not integrate an eikonal pole, and do not close mode
normalization or completeness.  Their statuses remain blocking.

### Continuum modified-delta target transcription

The source-qualified continuum expression can be transcribed independently of
the finite-basis claim.  In the convention of arXiv:1511.05590v2,

\[
 a_s=\frac{\alpha_s}{4\pi}=\frac{g_s^2}{(4\pi)^2},
 \qquad
 \widetilde S
 =\exp\!\left[a_s C_F\left(S^{[1]}+a_sS^{[2]}+\cdots\right)\right].
\]

Writing

\[
 B=\frac{b_T^2}{4},
 \qquad \delta=\pm\delta^+\delta^-,
 \qquad
 L_0=\ln\!\left(B|\delta^+\delta^-|e^{2\gamma_E}\right),
\]

the unexpanded one-loop coefficient is

\[
 S^{[1]}
 =-4\,\mu^{2\epsilon}B^\epsilon\Gamma(-\epsilon)
 \left[L_0-\psi(-\epsilon)-\gamma_E\right].
\]

With the source's modified minimal-subtraction normalization, its expansion is

\[
 S^{[1]}
 =-\frac4{\epsilon^2}
 +2L_\mu^2
 -\frac{2d^{(1,1)}}{C_F}
  \left(\frac1\epsilon+L_\mu\right)l_\delta
 +\frac{\pi^2}{3}
 +\mathcal O(\epsilon),
\]

where \(d^{(1,1)}=2C_F=\Gamma_0/2\),
\(L_\mu=\ln(\mu^2B e^{2\gamma_E})\), and
\(l_\delta=\ln(\mu^2/|\delta^+\delta^-|)\).  Thus the full
order-\(a_s\) soft correction carries the prefactor \(a_sC_F\).  C34 keeps
that prefactor separate from the dimensionless source coefficient; it does not
hide \(C_F\) inside an ambiguously normalized `one_loop_coefficient` field.

The source component formulas define the following analytic checks for an
independent reconstruction:

- cancellation of the fractional
  \((\delta^+\delta^-)^{-\epsilon}\) terms between the virtual and
  real/mirror/conjugate assembly;
- dependence only on \(|\delta^+\delta^-|\) after complete assembly;
- linearity in the rapidity logarithm;
- agreement between the unexpanded expression and its Laurent expansion;
- future/past equality of the T-even continuum target.

In C34 both graph-level reconstruction and the direct scalar-integral
reconstruction remain unexecuted.  The artifact is a transcription of the
source's final Eqs. (11)--(13), not an independent oracle, so the two-route
continuum-oracle validation gate is not issued.  Even after these
checks close, they validate the continuum target convention only.  Dimensional
regularization and \(\overline{\mathrm{MS}}\) are not the C33 finite-cell UV
regulator.

## Why the finite-basis coefficient cannot be evaluated

The three C33 resolution records provide support counts and nominal extents,
but not a complete executable mode basis.  The stored `implicit_mode_collection_sha256`
is the hash of each resolution descriptor; it is not the hash of a generated
mode collection.  No repository object supplies:

- complete R1-R3 cell boundaries, quadrature nodes, or numerical weights;
- the map from `transverse_index` to a two-dimensional \(k_T\) cell;
- the meaning of \(\omega\) and its relation to \(k^\pm\), rapidity, and
  \(k_T\);
- a mass-shell relation, virtual spectral representation, or light-front
  energy denominator;
- normalized mode functions, commutators, or a finite-cell completeness
  relation;
- polarization four-vectors or a gauge-complete polarization metric;
- a gauge-fixed B=0 action, free Hamiltonian, covariant propagator projection,
  BRST/Krein completion, or equivalent light-front instantaneous kernel;
- a partition of unity between the separately counted \(n\)- and
  \(\bar n\)-rapidity regions;
- a parameterized finite-volume representation of the lightlike and
  transverse-at-infinity Wilson segments;
- an operator action of the modified-delta exponential damping on those
  finite modes;
- an explicit constrained zero-mode sector;
- finite-cutoff renormalization conditions or a finite-basis-to-
  \(\overline{\mathrm{MS}}\) conversion.

The two stored physical transverse polarizations are particularly important.
They do not by themselves provide the covariant-gauge completeness required to
compare \(\xi_g=0,1,2\).  Adding covariant unphysical modes and ghosts, or
switching to a light-front physical-polarization representation with its
instantaneous and boundary terms, is a consequential regulator definition.
It cannot be inferred from a Hilbert-space dimension.

The light-front normalization also requires explicit completion.  The project
uses \(v^\pm=(v^0\pm v^3)/\sqrt2\), while the C33 implementation associates
the Minkowski tuple \(n=(1,0,0,1)\) directly with \(n\!\cdot k=k^-\).
Without a stored rescaling of \(n,\bar n\) and \(\delta^\pm\), this leaves a
\(\sqrt2\) normalization ambiguity in an absolute finite-cell coefficient.

## Status of all eighteen one-loop slots

The finite-basis status policy is deliberately conservative:

| C33/C34 contribution | C34 finite-basis status | Reason |
|---|---|---|
| `N_NBAR_EXCHANGE` | `UNRESOLVED_BLOCKING` | Continuum topology is nonzero; finite-cell propagator and measure are absent. |
| `CONJUGATE_LINE_EXCHANGE` | `UNRESOLVED_BLOCKING` | Conjugation relation is typed, but no matrix element exists. |
| `SAME_DIRECTION_LINE_EXCHANGE` | `UNRESOLVED_BLOCKING` | A target-DR scaleless/zero statement does not determine the cutoff-regulated term. |
| `REAL_ONE_SOFT_GLUON` | `UNRESOLVED_BLOCKING` | No normalized cell modes, cut measure, or cell integration. |
| `VIRTUAL_ONE_SOFT_GLUON` | `UNRESOLVED_BLOCKING` | No virtual spectral/energy-denominator prescription. |
| `WILSON_LINE_SELF_ENERGY` | `UNRESOLVED_BLOCKING` | Possible finite-cutoff logarithmic or power divergence is uncalculated. |
| `CUSP_ENDPOINT` | `UNRESOLVED_BLOCKING` | Finite junction geometry and counterterm are undefined. |
| `TRANSVERSE_CLOSURE` | `UNRESOLVED_BLOCKING` | The path is required structurally, but its finite-volume realization is absent. |
| `AUXILIARY_FIELD_SELF_ENERGY` | `UNRESOLVED_BLOCKING` | Mutual plan exclusion makes non-applicability a plausible future proof, but no C34 regulator-specific proof record closes this ledger slot. |
| `SOFT_VACUUM_ENERGY` | `UNRESOLVED_BLOCKING` | Normalized-vacuum cancellation requires the missing finite Hamiltonian/action proof. |
| `LIGHT_FRONT_INSTANTANEOUS` | `UNRESOLVED_BLOCKING` | Its value or non-applicability depends on the unchosen gauge-complete representation. |
| `GAUGE_FIXING` | `UNRESOLVED_BLOCKING` | No finite-basis covariant propagator/BRST completion exists. |
| `GHOST` | `UNRESOLVED_BLOCKING` | Connected \(O(g^2)\) vertex counting suggests a future non-applicability proof, but the required finite-basis gauge-fixed action has not been stored. |
| `ZERO_MODE` | `UNRESOLVED_BLOCKING` | Exact zero modes are excluded but explicitly not assigned zero. |
| `BASIS_BOUNDARY` | `UNRESOLVED_BLOCKING` | No boundary mode functions or refinement map. |
| `RAPIDITY_COUNTERTERM` | `UNRESOLVED_BLOCKING` | Cannot be extracted before the bare finite-basis rapidity dependence exists. |
| `UV_COUNTERTERM` | `UNRESOLVED_BLOCKING` | Cannot be solved before cutoff divergences are separated. |
| `RESIDUAL_LINE_MASS_COUNTERTERM` | `UNRESOLVED_BLOCKING` | Direct finite-cutoff lines may carry a power/length divergence; no non-applicability proof exists. |

Thus all eighteen machine-readable C34 contribution statuses remain
`UNRESOLVED_BLOCKING`.  `AUXILIARY_FIELD_SELF_ENERGY` and `GHOST` are the two
strongest candidates for later `NOT_APPLICABLE_WITH_PROOF` decisions, but C34
does not issue either decision without its missing scope/action proof.

No complete contribution is assigned `CANCELS_WITH_DECLARED_PARTNER` merely
because one divergent subpiece cancels in the continuum source.  No complete
contribution is assigned `TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO`
without an actual finite-regulator evaluation.

The bookkeeping separates four nonadditive layers.  Thirteen direct operator
terms form the unresolved primary bare-component set; the zero-mode term is a
separate control whose result must be resolved before any later assembly
decision; the auxiliary-field self energy is an alternative route and is not
added; UV, rapidity, and residual-line-mass decisions are not bare graphs.
Nine counterterm objects have their own `C34.CT.*` identifiers and depend on
unresolved bare structures.  Because no mode/cut calculation has
been performed, the cut ledger stores only candidate topology roles: every
physical real/virtual branch remains `UNRESOLVED_BLOCKING`, the assembled real
and virtual sets are empty, and no physical count-once result is claimed.

## Renormalization, trajectory, and zero-bin consequences

Because the bare finite-basis coefficient is unavailable, the following are
also unavailable rather than zero:

- proof of the required state independence of the soft UV counterterm;
- the modified-delta rapidity counterterm;
- the renormalized finite-basis soft factor;
- the finite-basis rapidity anomalous dimension and Collins-Soper convention
  value;
- gauge-parameter and cusp-consistency residuals;
- the finite-basis-to-continuum conversion, inverse, and round trip;
- the one-loop R1-R3 trajectory and extrapolation;
- the soft-side numerical zero-bin limit.

The nominal R1-R3 sequence changes energy support, rapidity window,
transverse extent, zero-mode scale, and cell counts simultaneously.  It has no
stored refinement maps.  It therefore cannot separate UV logarithms, finite
constants, volume/IR effects, rapidity-window effects, transverse
discretization, zero modes, endpoints, and numerical quadrature.  Moreover, a
required resolution holdout leaves too few calculated points for even a
log-plus-finite-plus-power trajectory.  A separately varied regulator grid is
required.

C34 freezes a provisional, source-independent modified-delta probe schedule
that varies \(\delta^+\) with \(\delta^-\) fixed and vice versa.  Its two
holdouts are also one-axis-at-a-time points; there is no diagonal combined
holdout.  These probes are numerical regulator controls, not physical
parameters, and none has been evaluated.  Likewise, only the quadrature method
family and nominal orders are frozen.  Missing tolerances, subdivision limits,
contour prescription, pole-cell partition, normalized cell functions, and
singular subtraction make the execution plan incomplete.

The C32/C33 compatibility interface remains a typed contract rather than an
executed equality.  In particular, the C32 spacelike off-shell IR plan is not
automatically covered by the dimensional-IR soft/zero-bin equivalence in
arXiv:hep-ph/0702022.  The C34 soft-side object can be named and typed, but its
one-loop value is empty-not-zero, and the C32 continuation gate remains false.

## Validation and isolation

The authoritative validation details are in
`docs/next_level/c34_regression_report.json` and the deterministic C34
validation output.  The scientific acceptance conditions for this narrative
are:

- C33 tree/root/basis/path identities are unchanged;
- Volume XXI and every primary source retain their exact hashes and roles;
- all unavailable one-loop values serialize as null or an explicit unresolved
  status, never as numerical zero;
- the continuum target is marked non-identical to the finite regulator;
- all positive one-loop, renormalization, conversion, trajectory, zero-bin,
  and continuation gates remain false;
- C11, C32, C33, the bridge, ART25 identities and covariance, the 216-route
  production registry, and the authoritative artifacts remain unchanged;
- `MSHT20_REP/` remains untouched and outside Git.

The machine-readable C34 coverage contains 300 individually described and
evidenced C34 records: 53 acceptance criteria, 65 Volume XXI requirements, 18
benchmark families, 42 required architecture objects, 18 contribution slots,
24 holdouts, and 80 distinct fault modes.  The 2,140 inherited C33 requirements
remain a separate regression suite; no fabricated cumulative count is
asserted.  Likewise the 2,040 inherited C33 injections remain separate from
the 2,240 C34 injection instances.  Each C34 instance executes a content-hash-
verified semantic control-state mutation and validates the observed diagnostic
against the expected one; identifier-only dispatch is not used as evidence.

## Exact next action

C35/S0C must first complete the regulator definition, not fit a coefficient.
It must choose and source one gauge-complete realization, materialize its
normalized finite-cell modes and quadrature, parameterize every Wilson
segment, implement the modified-delta operator, calculate the real/virtual
pair kernels and boundary/zero-mode controls, and only then solve UV and
rapidity counterterms.  The complete calculation specification is in
`docs/next_level/c34_missing_calculation_specification.md`.
