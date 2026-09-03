# C34 unresolved physics gaps

C34/S0A preserves the complete C33 B=0 soft architecture and transcribes the
source-qualified continuum modified-delta target, but it does not complete an
independent direct-integral reconstruction and does not produce a finite-basis
one-loop soft coefficient.  The exact status is

```text
C34_SOFT_ONE_LOOP_INCOMPLETE
```

and the exact next package is **C35/S0C — targeted unresolved soft-diagram and
counterterm completion**.

## Classification of what is known

### Exact

- The soft root has baryon number zero and is separate from the B=1 C32/C11
  proton state.
- The quark soft operator has four ordered fundamental/conjugate Wilson lines
  and a singlet `Tr/Nc` projection.
- \(C_F=4/3\) and \(S_{\rm FB}^{(0)}=1\).
- The C33 modified-delta single-gluon pole components and conjugation signs are
  stored.
- The direct finite-Fock, auxiliary-field, and continuum-oracle plans are
  mutually exclusive and nonadditive.
- Exact zero modes have not been assigned zero.

### Source-qualified continuum information

- arXiv:1511.05590v2 supplies the modified-delta continuum NLO soft factor in
  dimensional regularization.
- Its convention is
  \(a_s=\alpha_s/(4\pi)=g_s^2/(4\pi)^2\), with full one-loop prefactor
  \(a_sC_F\), \(B=b_T^2/4\), \(\delta=\pm\delta^+\delta^-\),
  \(L_\mu=\ln(\mu^2B e^{2\gamma_E})\), and
  \(l_\delta=\ln(\mu^2/|\delta^+\delta^-|)\).
- The continuum result supports checks of UV poles, \(b_T\) logarithms,
  rapidity-log linearity, finite constants, fractional-power cancellation, and
  future/past equality.
- Rapidity-renormalization, zero-bin, finite-regulator-method, light-front
  vacuum, and auxiliary-field references supply definitions or methodological
  comparisons.

Every retained primary source is nevertheless
`NOT_OPERATOR_REGULATOR_IDENTICAL` to the C33 finite-cell realization.  The
continuum target is not the microscopic answer.

### Model/regulator choices not yet made

- the gauge-complete finite-cell action or Hamiltonian;
- exact cell shapes, modes, weights, and dispersion;
- the finite-volume representation of lightlike infinity and transverse
  closure;
- the operator action of modified-delta damping on finite modes;
- the soft IR prescription and its C32 overlap relation;
- the constrained zero-mode sector;
- finite-cutoff renormalization conditions and MSbar conversion;
- independently variable regulator trajectories.

These are not nuisance parameters.  They define the operator and regulator in
which the requested coefficient would be calculated.

## Detailed unresolved gaps

1. **The stored basis is not executable.**  R1-R3 record counts and nominal
   support but no cell boundaries, nodes, weights, basis functions, mode
   collection, or refinement maps.  The field named
   `implicit_mode_collection_sha256` hashes the resolution descriptor itself,
   not generated modes.  C34 adds a typed illustrative rectangular cell and an
   exact nonsingular transverse-phase average, but not the complete mode
   collections or singular quadrature.

2. **Mode kinematics are undefined.**  The relation among \(\omega\), rapidity,
   \(k^+\), \(k^-\), and \(k_T\) is absent.  There is no mass-shell condition
   for cut modes or spectral/energy-denominator rule for virtual modes.

3. **The rapidity-region count lacks a partition.**  The basis counts separate
   \(n\) and \(\bar n\) regions, but no partition of unity or overlap removal
   says whether those labels cover or duplicate momentum space.

4. **Gauge completeness is unresolved.**  Two physical transverse
   polarizations cannot alone validate covariant \(\xi_g=0,1,2\) calculations.
   No BRST/Krein/ghost completion, covariant projected propagator, or complete
   light-front instantaneous formulation exists.

5. **Light-front normalization is ambiguous.**  The global project convention
   uses \(v^\pm=(v^0\pm v^3)/\sqrt2\), while the C33 direction tuple and pole
   labels do not store the compensating normalization of \(n,\bar n\) and
   \(\delta^\pm\).

6. **The current numerator is incomplete.**  Basepoints, representations,
   ordering, and pole signs are stored, but normalized path tangents,
   emission/absorption signs, conjugate generator action, and complete segment
   phases are not executable objects.

7. **Transverse closure is structural only.**  A label for the segment at
   infinity does not define its path in a periodic finite volume, its junction
   limit, or its endpoint counterterm.

8. **The finite-cell modified-delta operator is absent.**  C33 stores the
   expected single-gluon denominator signs, not the exponentially damped
   Wilson operator acting on the finite modes.

9. **All eighteen ledger slots remain blocking.**  Exchange, real, virtual,
   self-energy, cusp, transverse, vacuum, instantaneous, gauge, zero-mode,
   boundary, UV, rapidity, and residual-line-mass terms have no
   regulator-specific value or proof.  Auxiliary self energy is a future
   non-applicability candidate because the auxiliary plan is unselected and
   nonadditive.  A connected ghost graph is also a future order-counting proof
   candidate in ordinary covariant QCD.  C34 promotes neither candidate because
    the regulator-scope proof and finite-basis gauge-fixed action are absent.

    Their identities do not define one additive sum.  The direct bare terms
    and separate zero-mode control are distinct from the nonadditive auxiliary
    route, while UV, rapidity, and residual-line-mass counterterms are derived
    objects with separate IDs.  Physical cut branches are also unresolved;
    structural ID uniqueness is not yet a count-once proof.

10. **Target scalelessness cannot be transferred.**  Same-direction exchange
    or a lightlike-line self energy that is scaleless in dimensional
    regularization may become a logarithmic or power term under a finite
    cutoff.  No such term is assigned zero.

11. **UV renormalization is unavailable.**  The finite basis has no defined
    UV scale map or conditions separating logarithmic, cusp, endpoint,
    transverse, residual-mass, vacuum, and power divergences.

12. **Rapidity renormalization is unavailable.**  Bare \(\delta^+\) and
    \(\delta^-\) dependence has not been calculated, so no rapidity
    counterterm, rapidity anomalous dimension, or finite-basis Collins-Soper
    value can be extracted.

    C34 has frozen independent one-axis-at-a-time plus and minus probes and
    holdouts, but none has been evaluated.  A fixed-ratio diagonal scan would
    not resolve the missing independent dependence.

13. **The continuum target is not yet an independent oracle.**  Its source
    expression and normalization form a useful DR/MSbar target, but both the
    graph-level reconstruction and the direct scalar-integral reconstruction
    are unexecuted.  It also contains neither
    the C33 cutoff powers nor its zero-mode, endpoint, or finite-volume terms.

14. **The finite-basis conversion is unavailable.**  With no finite-side
    coefficient, the conversion kernel, finite constant, inverse, round trip,
    and remainder decomposition are empty-not-zero.

15. **The trajectory is underdetermined.**  R1-R3 change multiple axes at once
    and have no proven refinement maps.  Holding out one resolution leaves too
    few points for a log-plus-finite-plus-power model, let alone separate
    rapidity, volume, transverse, zero-mode, endpoint, and quadrature effects.

16. **Zero modes remain a scientific control.**  Their contribution to Ward
    closure, line self energy, rapidity logarithms, endpoints, and the finite
    conversion constant is unknown.

17. **The auxiliary route remains methodological.**  Existing auxiliary/lattice
    sources use Euclidean or spacelike lines and different UV/rapidity
    regulation.  Their Minkowski lightlike modified-delta identity is unproved.

18. **The C32/C34 overlap is not executable.**  The C32 momentum soft limit,
    finite-boundary conversion, and off-shell-IR relation are uncalculated.
    Pure-DR soft/zero-bin equivalence does not automatically close this map.

19. **The C32 continuation gate remains false.**  A named soft-side limit with
    no one-loop value does not authorize the subsequent collinear matching
    calculation.

20. **No observable status follows from C34.**  There is no microscopic proton
    TMD export, no deuteron process result, no bridge rerun, and no inference or
    production promotion.

## Required evidence for closure

The gaps close only with calculated, content-addressed evidence for:

- normalized gauge-complete cell modes and quadrature;
- direct versus spectral/cut current and coefficient agreement;
- all regulator-specific diagram/counterterm statuses;
- gauge, path, Hermitian, future/past, and rotational closure;
- UV and rapidity counterterm inverses;
- cusp and rapidity-anomalous-dimension consistency;
- zero-mode and boundary controls;
- an axis-separated trajectory with holdouts;
- finite-basis-to-continuum inverse and round trip;
- an executable soft-side zero-bin object.

The operational details and acceptance conditions are specified in
`docs/next_level/c34_missing_calculation_specification.md`.  Exact regression
and artifact-preservation results belong to
`docs/next_level/c34_regression_report.json`; they are not inferred from this
physics status note.
