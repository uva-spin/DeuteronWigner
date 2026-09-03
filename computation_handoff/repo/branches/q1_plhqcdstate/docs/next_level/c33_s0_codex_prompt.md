# C33/S0 Codex Work Package

## Title

**Finite-basis vacuum/eikonal soft Hilbert sector, one-loop TMD soft function, and rapidity-renormalization construction**

## Authoritative baseline

Start from the local C32/R0 completion commit:

```text
0d7b94a5e86882b23a56d4c1f11900d554756a18
```

This commit must retain the complete C29/B0, Volume XX, C30/B1, C31/B1A, and C32/R0 ancestry.

The required C28/P1D scientific ancestor remains:

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when the complete C32 baseline reproduces before any scientific change.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

The pre-existing untracked source directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git while redistribution permission remains unresolved.

Do not push the final completion commit.

---

# 1. Why C33/S0 is the exact next package

C32 creates the distinct:

```text
C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION
```

root without relabeling or mutating the historical C11 regulated model density.

The completed operator contains:

```text
fundamental staple
transverse closure
modified-delta rapidity-regulator plan
vacuum-soft definition
inverse-square-root soft allocation
zero-bin convention
```

and reduces exactly to the C11 parent at tree level.

The tree reduction is an executed result on twelve nonzero PLAN-A parents:

```text
u, d, ubar, dbar
x = 0.03, 0.10, 0.30
```

with:

```text
future matrix = C11 parent
past matrix = C11 parent
link-even matrix = C11 parent
link-odd matrix = 0
forward-reduction residual = 0
maximum matrix/scalar residual = 0
```

C32 also freezes:

```text
the exact C7 three-resolution finite-basis trajectory
a common spacelike off-shell partonic IR prescription
covariant-gauge checks at xi_g = 0, 1, 2
the modified-delta rapidity-regulator plan
twenty-five one-loop graph/counterterm/mixing statuses
typed delta/plus/regular distribution algebra
Mellin and quark-number oracles
```

The decisive result is:

```text
C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED
```

The C11/C32 collinear basis is a baryon-number-one finite light-front Hilbert space. It contains no vacuum Hilbert sector in which the four-eikonal-line Wilson soft operator can be evaluated.

Consequently:

```text
microscopic one-loop unsubtracted correlator:
    unavailable beyond tree level

microscopic soft factor:
    tree value 1
    one-loop structurally unavailable

zero-bin/overlap closure:
    unavailable

UV renormalization:
    unavailable

rapidity renormalization:
    unavailable

LF-to-project matching:
    unavailable

q <- q, q <- g, q <- qbar, nonsinglet, singlet channels:
    unresolved at one loop

first omitted order:
    O(alpha_s)

remainder:
    NONZERO_UNKNOWN

microscopic export:
    empty-not-zero

bridge:
    12 BRIDGE_COMMON_DOMAIN_ONLY
    0 comparison-ready

failed projection:
    642 x 0
```

C33 must construct a separate vacuum/eikonal soft root. It must not force vacuum physics into the baryon-number-one C11 state and must not import a continuum soft factor while labeling it a finite-basis microscopic calculation.

---

# 2. Central formal correction

The microscopic regulated TMD requires two distinct Hilbert/provenance roots over a shared regulator base:

\[
\mathcal H_{\rm coll}^{B=1}
\quad\text{and}\quad
\mathcal H_{\rm soft}^{B=0}.
\]

The regulated operator belongs to the structured product:

\[
\mathcal H_{\rm TMD}^{\rm reg}
=
\mathcal H_{\rm coll}^{B=1}
\widehat\otimes_{\mathfrak R_{\rm joint}}
\mathcal H_{\rm soft}^{B=0},
\]

where the fiber product over \(\mathfrak R_{\rm joint}\) means that the two sectors carry compatible records for:

```text
gauge group and representation
Wilson geometry
rapidity regulator
UV convention
transverse coordinate b
Fourier convention
measurement
boundary conditions
overlap/zero-bin map
renormalization scales
```

It does not mean that the vacuum soft factor is a component of the proton wave function.

Define the joint regulator identity:

\[
\mathfrak R_{\rm joint}
=
\left(
\mathfrak R_{\rm coll},
\mathfrak R_{\rm soft},
\mathcal C_{\rm overlap},
\mathcal C_{\rm scheme}
\right).
\]

C33 must determine whether a scientifically valid compatibility map exists between the C32 collinear regulator and a newly constructed finite soft regulator.

---

# 3. Primary objective

Implement the chain:

```text
C32 completed staple geometry
    -> distinct B=0 vacuum/eikonal soft root
    -> finite soft-gluon basis
    -> four eikonal color sources
    -> modified-delta rapidity regulator
    -> tree-level vacuum soft factor
    -> one-loop virtual and real soft contributions
    -> UV renormalization of the soft operator
    -> rapidity renormalization
    -> Collins-Soper/rapidity anomalous-dimension oracle
    -> finite-basis-to-continuum soft matching
    -> regulator/basis trajectory
    -> soft-collinear compatibility and overlap interface
    -> exact gate for resuming the C32 microscopic collinear calculation
```

The quark soft factor is:

\[
S_{\rm soft}^{\rm reg}
(b;\mu,\delta^+,\delta^-)
=
\frac{1}{N_c}
\langle\Omega_{\rm soft}|
\operatorname{Tr}
\left[
S_n^\dagger(b)
S_{\bar n}(b)
S_{\bar n}^\dagger(0)
S_n(0)
\right]
|\Omega_{\rm soft}\rangle_{\rm reg}.
\]

At one loop:

\[
S_{\rm soft}^{\rm reg}
=
1+a_s S_{\rm soft}^{(1),\rm reg}
+\mathcal O(a_s^2).
\]

C33 must determine rather than assume:

```text
whether a finite B=0 basis can represent the required vacuum and one-soft-gluon states;
whether the eikonal auxiliary/color sector can be represented independently of the baryon state;
whether the modified-delta rapidity regulator is implementable in that basis;
whether real and virtual soft contributions reproduce the target rapidity structure;
whether the finite basis produces additional UV, IR, endpoint, or zero-mode terms;
whether those terms are counterterms or power corrections;
whether a common soft-collinear overlap map exists;
whether a universal state-independent soft factor results.
```

---

# 4. Scientific boundary

C33 is:

```text
vacuum-sector specific
eikonal-operator specific
fundamental-representation quark soft sector
B=0
one-loop targeted
modified-delta rapidity regulated
UV explicit
rapidity explicit
finite-basis explicit
zero-mode explicit
basis-trajectory aware
state independent
validation only
non-inferential
```

C33 is not:

```text
a modification of the proton state
a fitted soft factor
an ART25 model fit
a hadronic ratio correction
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
a complete collinear one-loop calculation
a completed LF-to-project matching kernel
a process prediction
a deuteron prediction
a gluon soft-sector generalization
a T-odd process package
a production promotion
```

The continuum soft factor may be used as a target oracle. It may not be relabeled as the result of the finite-basis vacuum construction.

---

# 5. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C5-C33 Wilson, soft-overlap, Hamiltonian, regulator, matching, evolution, bridge, formal-volume, source, API, manifest, test, ADR, and roadmap files before changing the repository.

Continue autonomously until every applicable C33 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect source code and complete git histories;
- preserve additional primary papers and ancillaries;
- derive analytic one-loop soft expressions;
- construct a B=0 finite soft basis;
- implement eikonal color-source spaces;
- construct auxiliary-field and direct-Wilson-line oracles;
- run basis, rapidity, UV, gauge, and continuum trajectories;
- compare finite-basis and continuum soft objects;
- generate deterministic manifests and negative controls.

Do not:

- contact authors;
- alter C11, C32, ARTEMIDE, or ART25;
- insert the soft vacuum into the proton wave function;
- fit a soft factor to ART25 members or process data;
- use bridge residuals to tune the regulator;
- import a continuum soft factor as the finite-basis result;
- create a likelihood or posterior;
- execute a new process bridge;
- promote physical or inference status;
- modify production;
- push the completion commit.

---

# 6. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 6.1 Wilson, pole, cut, and soft-overlap sources

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c5_api.md
docs/next_level/c5_benchmark_manifest.json

docs/next_level/c6_implementation_report.md
docs/next_level/c6_api.md
docs/next_level/c6_benchmark_manifest.json

docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
```

These are finite-order validation and sign/color/overlap oracles. They are not automatically a vacuum TMD soft function.

## 6.2 Microscopic and regulator sources

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c11_regression_report.json
```

## 6.3 Matching, evolution, and continuum sources

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
```

## 6.4 Bridge and C32 sources

```text
docs/next_level/c29_implementation_report.md
docs/next_level/c29_frozen_bridge_grid.json
docs/next_level/c29_constraint_role_split.json
docs/next_level/c29_cross_root_member_relation.json
docs/next_level/c29_no_double_counting_contract.json

docs/next_level/c30_implementation_report.md
docs/next_level/c30_common_bridge_domain.json
docs/next_level/c30_distribution_bridge_capability_matrix.json

docs/next_level/c31_implementation_report.md
docs/next_level/c31_three_layer_identity_manifest.json
docs/next_level/c31_microscopic_bare_operator_manifest.json
docs/next_level/c31_renormalization_component_ledger.json
docs/next_level/c31_continuum_scheme_equivalence_matrix.json
docs/next_level/c31_source_sufficiency_decision.json

docs/next_level/c32_implementation_report.md
docs/next_level/c32_api.md
docs/next_level/c32_normative_source_integration.json
docs/next_level/c32_operator_completion_manifest.json
docs/next_level/c32_c11_tree_reduction_report.json
docs/next_level/c32_operator_identity_decision.json
docs/next_level/c32_regulator_plan_manifest.json
docs/next_level/c32_partonic_external_state_plan.json
docs/next_level/c32_gauge_plan.json
docs/next_level/c32_rapidity_plan.json
docs/next_level/c32_partonic_diagram_ledger.json
docs/next_level/c32_counterterm_ledger.json
docs/next_level/c32_distributional_result_library.json
docs/next_level/c32_microscopic_soft_factor.json
docs/next_level/c32_soft_sector_capability_report.json
docs/next_level/c32_source_sufficiency_decision.json
docs/next_level/c32_no_go_decision_tree.json
docs/next_level/c32_missing_calculation_specification.md
docs/next_level/c32_distribution_bridge_capability_matrix.json
docs/next_level/c32_unresolved_physics_gaps.md
```

## 6.5 Formal sources

```text
references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/volume_xix_source_qualified_process_inputs.tex
references/volume_xx_source_reproducible_bridge_geometry.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

If Volume XXI exists, read and hash-audit it. If it is absent, record the absence and do not invent its contents.

Create:

```text
docs/next_level/c33_normative_source_integration.json
```

---

# 7. Required primary-source audit

Reuse the C31/C32 source locks and preserve any additional source under:

```text
data/raw/c33_sources/
```

with exact version and SHA-256 identity.

Audit at least:

```text
arXiv:1511.05590
    universal TMD soft function and modified-delta rapidity regulator

arXiv:1604.07869
    unpolarized TMD definition, soft subtraction, and matching

arXiv:1707.07606
    rapidity-divergence renormalization theorem

arXiv:1202.0814
    rapidity renormalization group

arXiv:1604.00392
    exponential/rapidity-regulator comparison

arXiv:hep-ph/0702022
    soft versus zero-bin subtraction and count-once logic

arXiv:2312.04315
    auxiliary one-dimensional field representation of TMD Wilson lines
    and a lattice-calculable soft object

arXiv:2412.12645
    exploratory auxiliary-field lattice measurement of the TMD soft function

arXiv:2002.09408
    auxiliary-field Wilson-line renormalization and scheme conversion

arXiv:1711.00543
    one-loop renormalization of nonlocal Wilson-line operators

arXiv:1612.07740
    Wilson loops in light-front quantization, used only as a
    light-front-vacuum methodological comparison
```

Classify every source as:

```text
TARGET_SOFT_FUNCTION_AUTHORITY
RAPIDITY_RENORMALIZATION_AUTHORITY
ZERO_BIN_AUTHORITY
AUXILIARY_FIELD_METHOD_AUTHORITY
FINITE_REGULATOR_METHOD_AUTHORITY
LIGHT_FRONT_VACUUM_COMPARISON_ONLY
NOT_OPERATOR_REGULATOR_IDENTICAL
```

The auxiliary-field and lattice papers supply a representation and methodology. They do not automatically prove equivalence to the C33 finite-basis regulator.

Create:

```text
docs/next_level/c33_primary_source_manifest.json
docs/next_level/c33_source_relevance_matrix.json
```

---

# 8. Immutable C32 baseline

Before edits, reproduce and record:

```text
1,167 tests
32 builders
38/38 evidence rows
164/164 atlas pages
1,940 C32 requirements
1,840/1,840 C32 negative injections
88 named C32 fault modes

C28-C32 validators passing
deterministic C32 regeneration

operator:
    C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION

historical parent:
    C11 remains REGULATED_MODEL_DENSITY

tree reduction:
    12 nonzero PLAN-A parents
    u, d, ubar, dbar
    x = 0.03, 0.10, 0.30
    matrix residual 0
    scalar residual 0

frozen collinear regulator trajectory:
    K=9/2,  Nmax=8,  bHO=0.40 GeV
    K=11/2, Nmax=10, bHO=0.45 GeV
    K=13/2, Nmax=12, bHO=0.50 GeV

partonic IR plan:
    spacelike off-shell quarks
    p = 5 and 10 GeV
    p^2 = -0.04 and -0.09 GeV^2

gauge checks:
    xi_g = 0, 1, 2

rapidity plan:
    modified-delta

one-loop ledger:
    25 contributions
    none silently zero

distribution algebra:
    delta, plus, regular, lower-limit-plus, convolution, Mellin
    quark-number residual at roundoff

decisive status:
    C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED

bridge:
    12 BRIDGE_COMMON_DOMAIN_ONLY
    0 ready
    failed projection 642 x 0
    preserved source factor 642 x 11
    rank 10
    nullity 1

integrity:
    216 production routes
    eight authoritative artifacts byte-identical
    NO_JOINT_MEASURE
    no fit, inference, process promotion, or physical claim
```

Do not proceed if this baseline does not reproduce.

C33 must not modify:

- historical C11;
- the C32 operator-completion identity;
- the exact C32 tree reduction;
- the frozen C32 collinear regulator and partonic plans;
- the C29-C32 bridge grid, role split, and holdouts;
- ART25 members or source covariance;
- production registry or authoritative artifacts.

Create a new soft-sector root and explicit compatibility edges.

---

# 9. Required architecture

Implement or extend immutable objects equivalent to:

```text
SoftRootId
VacuumHilbertId
VacuumStateId
VacuumSectorPlan

SoftBasisId
SoftBasisResolution
SoftMomentumMode
SoftGluonMode
SoftZeroModePolicy
SoftBoundaryCondition
SoftContinuumTrajectory

EikonalSourceId
EikonalDirection
EikonalColorSpace
EikonalAuxiliaryField
EikonalPathOperator
FourLineSoftOperator

SoftRapidityRegulator
SoftUVRegulator
SoftIRRegulator
SoftMeasurement
SoftFourierConvention

BareSoftFactor
SoftVirtualContribution
SoftRealContribution
SoftSelfEnergyContribution
SoftCuspEndpointContribution
SoftTransverseClosureContribution
SoftInstantaneousContribution
SoftZeroModeContribution

SoftUVCounterterm
SoftRapidityCounterterm
RenormalizedSoftFactor
SoftRapidityAnomalousDimension
SoftCollinsSoperKernel

SoftContinuumOracle
SoftRegulatorMatching
SoftRegulatorRemainder
SoftBasisTrajectoryReport

SoftCollinearRegulatorPair
SoftCollinearCompatibilityMap
SoftCollinearOverlapInterface
ZeroBinCompatibilityGate

SoftTensorNetworkPlan
SoftAuxiliaryFieldOracle

C33SoftCapabilityMatrix
C33ClosureReport
```

Every object must be:

- immutable after construction;
- content addressed;
- deterministic in serialization;
- explicit about B=0 vacuum identity;
- explicit about color and Wilson geometry;
- explicit about rapidity, UV, IR, and basis regulators;
- explicit about perturbative order;
- explicit about source and target soft schemes;
- state independent;
- unable to consume ART25 members, data, or bridge residuals;
- unreachable from inference and production.

---

# 10. Two-root TMD regulator identity

Define:

```text
COLLINEAR_ROOT:
    C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION
    B = 1

SOFT_ROOT:
    C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT
    B = 0
```

The roots share no state vector and no probability normalization.

They are connected only by typed records:

```text
same gauge group
same parton representation
same Wilson directions
same transverse coordinate
same rapidity-regulator convention or proved conversion
same UV target scheme or proved conversion
same measurement
same zero-bin/overlap convention
```

The full regulated TMD is a composition:

\[
F_{\rm TMD}^{\rm reg}
=
\operatorname{REN}
\left[
\operatorname{COLL}_{B=1}
\ominus
\operatorname{OVERLAP}
\right]
\otimes
\operatorname{SOFT}_{B=0}^{-1/2}.
\]

It is not a sum of vacuum and baryon probabilities.

Create:

```text
docs/next_level/c33_two_root_tmd_identity.json
docs/next_level/c33_soft_collinear_provenance_graph.json
```

---

# 11. Soft-sector realization plans

Compile mutually exclusive plans:

```text
S0-FB-EIKONAL-FOCK

    A direct finite soft-gluon Fock-space realization:
        |Omega> plus one-soft-gluon states at one loop;
    four non-dynamical eikonal color sources;
    direct Wilson-line operator evaluation.

S0-AUXILIARY-EIKONAL

    A local extended-theory realization in which each Wilson line is
    represented by a one-dimensional auxiliary field; the vacuum soft
    operator becomes a product of local endpoint operators and auxiliary
    propagators.

S0-CONTINUUM-ORACLE-ONLY

    The source-qualified modified-delta continuum soft function is used
    only as the target oracle. This plan cannot issue a microscopic
    finite-basis soft status.

S0-UNAVAILABLE
```

Select one primary microscopic plan before calculating numerical residuals.

The direct and auxiliary routes may be implemented as independent oracles. They are not additive soft factors.

Selection criteria:

```text
operator identity
rapidity-regulator compatibility
finite-basis realizability
vacuum-sector completeness
color trace
one-loop calculability
basis trajectory
gauge closure
target-oracle comparison
minimum synthetic input
```

Create:

```text
docs/next_level/c33_soft_sector_plan_manifest.json
docs/next_level/c33_soft_sector_plan_selection.json
```

---

# 12. Finite vacuum Hilbert sector

Construct a B=0 soft Hilbert space distinct from the C7/C11 baryonic basis.

At one-loop scope it must contain, at minimum:

\[
\mathcal H_{\rm soft}^{(1)}
=
\operatorname{span}
\left\{
|\Omega\rangle,
|g^a_{\lambda,\nu}\rangle
\right\},
\]

where \(\nu\) identifies the frozen soft momentum mode.

Every soft-gluon mode records:

```text
k+ and k- or equivalent energy/rapidity coordinates
kT
polarization
adjoint color
rapidity bin
transverse-basis index
boundary condition
zero-mode status
normalization
```

The soft basis must support both n- and nbar-directed rapidity regions. It must not inherit the C7 fixed total-K baryon constraint.

Freeze at least three nested soft resolutions. A possible typed resolution tuple is:

\[
\Lambda_{\rm soft}
=
(N_\omega,N_y,N_\perp,
\omega_{\min},\omega_{\max},
Y_{\max},L_\perp,
\rho_0,\mathcal B_{\rm soft}).
\]

The exact implementation may use:

```text
finite-volume momentum modes
oscillator transverse modes
quadrature-defined orthonormal cells
another source-audited finite basis
```

but the normalization, completeness relation, UV/IR support, and continuum trajectory must be explicit.

Create:

```text
docs/next_level/c33_vacuum_hilbert_manifest.json
docs/next_level/c33_soft_basis_manifest.json
docs/next_level/c33_soft_zero_mode_policy.json
docs/next_level/c33_soft_basis_trajectory_plan.json
```

---

# 13. Eikonal color-source sector

Represent the four Wilson lines separately from the dynamical soft-gluon Fock space.

For a quark soft function retain:

```text
fundamental n line at b
anti-fundamental conjugate n line at b
fundamental nbar line at 0
anti-fundamental conjugate nbar line at 0
future/past orientation
path ordering
transverse closure
color trace
```

The eikonal color space must have a declared singlet trace projector.

The operator must reduce to the identity at zero coupling:

\[
\mathcal S^{(0)}=1.
\]

Required color checks:

```text
C_F = 4/3
singlet trace normalization
line reversal
Hermitian conjugation
future/past T-even equality
no implicit f/d gluon color class
```

Create:

```text
docs/next_level/c33_eikonal_color_space.json
docs/next_level/c33_four_line_operator_manifest.json
docs/next_level/c33_eikonal_path_reversal_report.json
```

---

# 14. Auxiliary-field representation oracle

When scientifically implementable, construct a separate auxiliary-field oracle.

Represent a Wilson line along \(v^\mu\) using a one-dimensional color field with a frozen action/propagator equivalent to eikonal transport.

Record:

```text
auxiliary field statistics
color representation
direction vector
boundary conditions
mass/residual-energy counterterm
endpoint operators
path-segment composition
piecewise-path junctions
rapidity relation
UV conversion
```

Use this route to test:

```text
direct Wilson operator versus auxiliary propagator
path composition
orientation reversal
endpoint renormalization
piecewise transverse closure
```

The auxiliary-field result is a methodological oracle unless its Minkowski/light-front and modified-delta identities are proved.

Create:

```text
docs/next_level/c33_auxiliary_field_soft_oracle.json
docs/next_level/c33_auxiliary_direct_equivalence_report.json
```

---

# 15. Modified-delta rapidity regulator in the soft sector

Implement the same declared modified-delta rapidity convention as the C32 target plan, or an explicit intermediate conversion.

Every eikonal denominator must be derived from:

```text
Wilson orientation
Fourier convention
momentum flow
covariant derivative convention
delta+ or delta- regulator
i0 prescription
```

Do not insert a regulator sign by hand.

Record:

```text
n-line regulator
nbar-line regulator
future/past orientation
complex conjugation
boost/rapidity transformation
delta+ delta- dependence
regulator-removal order
```

Required checks:

- regulator reverses correctly under line conjugation;
- the T-even soft factor is future/past invariant;
- the bare soft factor contains the expected rapidity dependence;
- a finite numerical epsilon is never stored as physical support;
- the finite-basis cutoff is not silently identified with the rapidity regulator.

Create:

```text
docs/next_level/c33_soft_rapidity_regulator_manifest.json
docs/next_level/c33_eikonal_denominator_report.json
```

---

# 16. Complete one-loop soft contribution ledger

At order \(a_s\), audit and calculate every required soft-sector contribution.

The ledger must include, where required:

```text
exchange between n and nbar lines
exchange between conjugate lines
same-direction line exchange
real one-soft-gluon contribution
virtual one-soft-gluon contribution
Wilson-line self energies
cusp/endpoints
transverse-closure segments
auxiliary-field self energy
soft vacuum-energy term
instantaneous light-front contribution
gauge-fixing contribution
ghost contribution or proved absence
zero-mode contribution
basis-boundary contribution
rapidity counterterm
UV counterterm
residual-energy/line-mass counterterm
```

For every contribution record:

```text
diagram ID
line pair
real/virtual status
color factor
gauge dependence
UV dependence
IR dependence
rapidity dependence
basis dependence
b dependence
source or derivation
symbolic expression
numerical implementation
cancellation partners
```

No absent contribution may be assigned zero without proof.

Create:

```text
docs/next_level/c33_soft_diagram_ledger.json
docs/next_level/c33_soft_counterterm_ledger.json
docs/next_level/c33_soft_dependency_graph.json
```

---

# 17. Bare finite-basis soft factor

Calculate:

\[
S_{\rm FB}^{\rm bare}
(b;\Lambda_{\rm soft},\delta^\pm,\xi_g)
=
1+a_s S_{\rm FB}^{(1),\rm bare}
+\mathcal O(a_s^2).
\]

Retain separately:

```text
real
virtual
line self energy
cusp/endpoint
transverse closure
instantaneous
zero mode
basis boundary
```

Required checks:

- tree value exactly one;
- \(S(b=0)\) behavior is recorded in the source convention;
- Hermitian conjugation;
- future/past equality for the T-even soft factor;
- transverse-rotation covariance;
- color-singlet normalization;
- real/virtual count once;
- basis completeness at each resolution;
- no physical numerical epsilon;
- direct and auxiliary-field agreement where both are available.

Create:

```text
docs/next_level/c33_bare_soft_factor.json
docs/next_level/c33_bare_soft_oracle_report.json
```

---

# 18. UV renormalization of the soft operator

Separate:

```text
Wilson-line self-energy renormalization
cusp/endpoint renormalization
auxiliary-line residual-mass renormalization
vacuum-energy subtraction
operator UV factor
```

Define the target UV convention explicitly.

Extract:

\[
S_{\rm FB}^{\rm UV-ren}
=
Z_S^{\rm UV}
S_{\rm FB}^{\rm bare}.
\]

Required closure:

- UV poles or cutoff logarithms are identified;
- the finite-basis UV trajectory is explicit;
- the counterterm is state independent;
- the remaining UV anomalous dimension agrees with the target soft operator at the declared order;
- linear/power divergences are not hidden in logarithmic factors;
- transverse-link endpoint terms are counted once.

Create:

```text
docs/next_level/c33_soft_uv_renormalization.json
docs/next_level/c33_soft_uv_anomalous_dimension_report.json
```

---

# 19. Rapidity renormalization and Collins-Soper kernel

Define a rapidity-renormalized soft object using the source-qualified convention.

Record separately:

```text
bare rapidity dependence
rapidity counterterm
rapidity-renormalized soft factor
rapidity anomalous dimension
Collins-Soper/D-function convention
mu dependence
```

The exact derivative convention must be source located.

Schematically:

\[
S_{\rm FB}^{\rm ren}
=
Z_S^{\rm UV}
R_S^{\rm rap}
S_{\rm FB}^{\rm bare}.
\]

Required checks:

- regulator dependence cancels from the renormalized object at the declared order;
- the extracted rapidity anomalous dimension is independent of the vacuum basis resolution up to the declared remainder;
- the \(\mu\) derivative of the rapidity anomalous dimension agrees with the cusp anomalous dimension;
- future/past equality;
- gauge-parameter independence;
- rapidity scale/path consistency;
- no nonperturbative Collins-Soper model is fitted.

Create:

```text
docs/next_level/c33_soft_rapidity_renormalization.json
docs/next_level/c33_soft_rapidity_anomalous_dimension.json
docs/next_level/c33_soft_collins_soper_kernel_oracle.json
```

---

# 20. Continuum modified-delta target oracle

Evaluate the source-qualified one-loop continuum soft function in the same:

```text
Wilson geometry
fundamental representation
modified-delta regulator
UV convention
b convention
mu
rapidity convention
```

The target oracle must retain analytic logarithms and finite constants separately.

Use at least two independent routes:

```text
source expression
independent symbolic or direct integral reconstruction
```

Create:

```text
docs/next_level/c33_continuum_soft_oracle.json
docs/next_level/c33_continuum_soft_validation_report.json
```

Do not promote C19-C22 validation polynomials to the target soft expression unless their exact source identity is independently established.

---

# 21. Finite-basis-to-continuum soft matching

Extract a soft-regulator conversion:

\[
S_{\rm cont}^{\rm ren}
=
Z_{\rm FB\to cont}^{S}
S_{\rm FB}^{\rm ren}
+
R_{\rm FB\to cont}^{S}.
\]

At one loop:

\[
Z_{\rm FB\to cont}^{S}
=
1+a_s Z_{S}^{(1)}
+\mathcal O(a_s^2).
\]

The conversion must be:

```text
vacuum state independent
hadron independent
ART25-member independent
gauge independent
explicit in the finite soft regulator
explicit in first omitted order
```

Separate:

```text
logarithmic cutoff conversion
finite conversion constant
power-suppressed basis remainder
endpoint remainder
zero-mode remainder
numerical remainder
```

Required checks:

- inverse/round-trip;
- UV anomalous dimension;
- rapidity anomalous dimension;
- gauge independence;
- \(b\)-space dependence;
- resolution independence within the declared trajectory;
- no fit to ART25 or the bridge.

Create:

```text
docs/next_level/c33_soft_regulator_matching_library.json
docs/next_level/c33_soft_regulator_roundtrip_report.json
docs/next_level/c33_soft_regulator_remainder.json
```

---

# 22. Soft-basis continuum trajectory

Run at least three nested soft-basis resolutions.

Determine separately:

```text
UV logarithms
IR sensitivity
rapidity-window sensitivity
finite-volume effects
transverse-basis truncation
zero-mode sensitivity
endpoint/junction effects
quadrature error
```

Fit only analytically predicted regulator structures.

Allowed statuses:

```text
SOFT_CONTINUUM_TRAJECTORY_RESOLVED
SOFT_LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN
SOFT_FINITE_BASIS_ONLY
SOFT_NONUNIVERSAL_TRAJECTORY
SOFT_TRAJECTORY_UNAVAILABLE
```

Create:

```text
docs/next_level/c33_soft_basis_trajectory.json
docs/next_level/c33_soft_continuum_extrapolation.json
docs/next_level/c33_soft_power_correction_manifest.json
```

---

# 23. Soft-collinear compatibility and overlap interface

C33 must not claim that a valid soft sector automatically completes the microscopic TMD.

Construct a typed compatibility record between:

```text
C32 collinear regulator
C33 soft regulator
```

Audit:

```text
same Wilson geometry
same rapidity convention
same transverse measurement
same b coordinate
same UV target scheme
same external-state IR prescription where needed
same gauge convention
same overlap-region definition
same regulator-removal order
```

Define the zero-bin/overlap interface without calculating unavailable collinear one-loop coefficients.

The interface must specify:

\[
\operatorname{ZERO\_BIN}
:
\operatorname{COLL}_{\rm C32}
\rightarrow
\operatorname{SOFT\_LIMIT}_{\rm C33}.
\]

Required statuses:

```text
SOFT_COLLINEAR_REGULATORS_IDENTICAL
SOFT_COLLINEAR_EXACT_CONVERSION
SOFT_COLLINEAR_COMPATIBLE_AT_DECLARED_ORDER
SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED
SOFT_COLLINEAR_INCOMPATIBLE
```

Create:

```text
docs/next_level/c33_soft_collinear_regulator_pair.json
docs/next_level/c33_soft_collinear_compatibility_report.json
docs/next_level/c33_zero_bin_interface_contract.json
```

A valid C33 soft factor is necessary but not sufficient for the C32 LF-to-project matching.

---

# 24. Tensor-network and future quantum representation

Represent the finite soft root with an explicit tensor-network plan where appropriate.

The soft tensor network must retain:

```text
vacuum root
soft-gluon mode
adjoint color
polarization
rapidity cell
transverse cell
four eikonal color legs
singlet trace
```

Bond dimension is a deterministic numerical/truncation axis.

Do not infer a statistical ensemble from soft-bond alternatives.

The operator may be compiled into a later quantum circuit using:

```text
vacuum plus one-gluon register
eikonal color-source registers
controlled emission/absorption gates
singlet trace projection
```

but C33 does not perform quantum fitting.

Create:

```text
docs/next_level/c33_soft_tensor_network_manifest.json
docs/next_level/c33_soft_quantum_interface_contract.json
```

---

# 25. Conditional C32 continuation gate

C33 does not rerun the twelve-point ART25 bridge.

It may issue:

```text
C33_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING
```

only when all of the following pass:

```text
vacuum Hilbert construction
four-line operator
tree normalization
one-loop bare soft factor
UV renormalization
rapidity renormalization
gauge independence
continuum soft oracle
finite-basis trajectory
soft-regulator matching
soft-collinear compatibility
zero-bin interface contract
```

When this gate passes, the next package may resume the C32 one-loop collinear correlator and matching calculation.

Create:

```text
docs/next_level/c33_c32_continuation_gate.json
```

The microscopic proton export remains empty in C33.

The bridge remains:

```text
12 BRIDGE_COMMON_DOMAIN_ONLY
0 BRIDGE_DISTRIBUTION_COMPARISON_READY
```

unless a later package completes the collinear and matching layers.

---

# 26. Remainder and uncertainty separation

Keep separate:

```text
soft perturbative truncation
soft UV-regulator remainder
soft IR-regulator remainder
rapidity-window remainder
transverse-basis remainder
finite-volume remainder
zero-mode remainder
endpoint/cusp remainder
transverse-closure remainder
auxiliary-field representation remainder
soft-regulator conversion remainder
soft-collinear compatibility remainder
zero-bin-interface remainder
numerical integration remainder
```

Unknown remains:

```text
NONZERO_UNKNOWN
```

No soft remainder may be absorbed into ART25 covariance or the microscopic hadron state.

Create:

```text
docs/next_level/c33_soft_uncertainty_budget.json
docs/next_level/c33_soft_remainder_separation.json
```

---

# 27. Scientifically valid no-go outcomes

C33 must support rigorous negative results.

## 27.1 Vacuum-basis obstruction

Issue:

```text
C33_FINITE_VACUUM_HILBERT_UNAVAILABLE
```

when no finite B=0 basis can represent the required one-loop soft modes and Wilson operator.

## 27.2 Wilson-geometry obstruction

Issue:

```text
C33_FOUR_LINE_OPERATOR_NOT_REALIZABLE
```

when the finite basis cannot represent the four-line staple geometry and transverse closure.

## 27.3 Rapidity obstruction

Issue:

```text
C33_SOFT_RAPIDITY_RENORMALIZATION_UNRESOLVED
```

when the modified-delta dependence cannot be isolated and renormalized.

## 27.4 Regulator-compatibility obstruction

Issue:

```text
C33_SOFT_COLLINEAR_REGULATORS_INCOMPATIBLE
```

when the C32 collinear and C33 soft sectors lack a common overlap or conversion map.

## 27.5 Continuum-trajectory obstruction

Issue:

```text
C33_SOFT_CONTINUUM_TRAJECTORY_UNRESOLVED
```

when logarithmic, finite, and power-suppressed basis effects cannot be separated.

## 27.6 Tree-level-only status

Issue:

```text
C33_SOFT_TREE_LEVEL_ONLY
```

when \(S^{(0)}=1\) closes but the one-loop soft calculation does not.

Every no-go status must include an exact missing-calculation specification.

Create:

```text
docs/next_level/c33_source_sufficiency_decision.json
docs/next_level/c33_no_go_decision_tree.json
docs/next_level/c33_missing_calculation_specification.md
```

---

# 28. Holdouts

Freeze holdouts before basis tuning, analytic simplification, counterterm selection, or continuum fitting.

Reserve at least:

```text
one n-nbar exchange coefficient
one same-direction line contribution
one real soft term
one virtual soft term
one Wilson self-energy term
one cusp/endpoint term
one transverse-closure term
one soft UV counterterm
one rapidity counterterm
one gauge-parameter value
one delta+ variation
one delta- variation
one b point
one b -> 0 controlled limit
one auxiliary/direct equivalence point
one alternate soft resolution
one rapidity-window point
one zero-mode policy control
one continuum-oracle coefficient
one anomalous-dimension coefficient
one soft-regulator round trip
one soft-collinear compatibility check
one zero-bin-interface check
one quark-state-independence control
one ART25-member-independence control
```

No failed holdout may be moved into derivation or trajectory fitting.

---

# 29. Required benchmark families

Implement at least:

## S0-A: immutable baseline and two-root identity

- C32 B=1 collinear root;
- C33 B=0 soft root;
- no state/probability mixing.

## S0-B: soft-sector plan selection

- direct Fock;
- auxiliary;
- continuum oracle;
- mutually exclusive.

## S0-C: finite vacuum Hilbert space

- vacuum;
- one-gluon states;
- color/polarization;
- rapidity/transverse modes.

## S0-D: eikonal color and four-line geometry

- fundamental trace;
- path ordering;
- transverse closure;
- reversal.

## S0-E: rapidity regulator

- modified delta;
- signs;
- line conjugation;
- regulator-removal order.

## S0-F: complete soft diagram ledger

- real;
- virtual;
- self energy;
- cusp;
- transverse;
- instantaneous;
- zero mode;
- counterterms.

## S0-G: bare soft factor

- tree one;
- one-loop assembly;
- direct/auxiliary comparison.

## S0-H: soft UV renormalization

- line;
- cusp;
- endpoint;
- vacuum;
- anomalous dimension.

## S0-I: soft rapidity renormalization

- bare dependence;
- counterterm;
- rapidity anomalous dimension;
- CS-kernel convention.

## S0-J: gauge and link closure

- xi_g;
- future/past;
- Hermitian conjugation;
- color singlet.

## S0-K: continuum modified-delta oracle

- source expression;
- independent reconstruction;
- logarithms and constants.

## S0-L: finite-basis soft matching

- inverse;
- round trip;
- state independence;
- no ART25 fitting.

## S0-M: soft-basis trajectory

- three or more resolutions;
- logarithmic;
- finite;
- power terms.

## S0-N: zero modes and endpoints

- explicit policy;
- sensitivity;
- no silent omission.

## S0-O: soft-collinear compatibility

- shared measurement;
- rapidity;
- UV;
- overlap;
- conversion.

## S0-P: zero-bin interface

- typed map;
- count once;
- no premature collinear result.

## S0-Q: continuation gate

- soft ready or exact no-go;
- no microscopic export yet.

## S0-R: deterministic isolation

- no proton-state mutation;
- no fit;
- no production change.

---

# 30. Negative injections

Create at least **2,040 ordered C33 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## Root identity

- vacuum soft state inserted into proton Fock normalization;
- B=0 and B=1 roots aliased;
- soft factor called a proton probability;
- C11 historical state mutated;
- C32 operator root overwritten.

## Vacuum basis

- no vacuum state;
- one-gluon normalization wrong;
- adjoint color dropped;
- polarization dropped;
- n and nbar rapidity regions aliased;
- fixed total-K baryon constraint copied into the soft root;
- zero-mode policy omitted;
- basis completeness assumed from one resolution.

## Eikonal geometry

- one Wilson line omitted;
- conjugate line omitted;
- transverse closure omitted;
- path ordering omitted;
- wrong fundamental/anti-fundamental action;
- color trace normalization wrong;
- future/past sign inserted by hand;
- f/d gluon color class incorrectly introduced.

## Rapidity regulator

- finite basis called the rapidity regulator;
- delta+ and delta- aliased;
- wrong i0 sign;
- line conjugation fails;
- regulator removed before real/virtual combination;
- numerical epsilon stored as physical support;
- ζ prescription confused with bare rapidity regulation.

## Diagram ledger

- n-nbar exchange omitted;
- real contribution omitted;
- virtual contribution omitted;
- line self energy omitted;
- cusp term omitted;
- endpoint term omitted;
- transverse-link term omitted;
- instantaneous term omitted;
- ghost term silently omitted;
- zero mode silently zeroed;
- counterterm omitted.

## Soft factor

- continuum result copied as finite-basis result;
- tree value not one;
- soft factor counted twice;
- inverse-square-root allocation wrong;
- real/virtual double counted;
- vacuum energy mixed with operator renormalization;
- hadron dependence introduced.

## UV and rapidity renormalization

- UV logarithm left uncanceled;
- power divergence hidden in log counterterm;
- rapidity dependence left uncanceled;
- gauge dependence hidden;
- cusp anomalous dimension mismatch hidden;
- rapidity anomalous dimension fitted;
- CS kernel copied from ART25.

## Auxiliary field

- Euclidean auxiliary result treated as direct Minkowski authority;
- auxiliary residual mass omitted;
- endpoint operator omitted;
- piecewise path junction omitted;
- auxiliary/direct mismatch hidden;
- auxiliary and direct results added.

## Continuum matching

- one basis point called continuum;
- arbitrary polynomial fit;
- finite constant tuned to target;
- ART25 member used;
- bridge residual used;
- inverse adapter omitted;
- round-trip failure hidden;
- state dependence ignored.

## Soft-collinear compatibility

- different b conventions;
- different rapidity regulators without conversion;
- different UV schemes hidden;
- different measurements;
- zero-bin interface omitted;
- overlap subtracted twice;
- valid soft factor treated as complete TMD;
- C32 collinear one-loop result fabricated.

## Readiness leakage

- microscopic proton TMD exported in C33;
- bridge rerun executed;
- process bridge executed;
- likelihood produced;
- p-value reported;
- calibration performed;
- posterior sampled;
- member reweighted;
- emulator trained;
- deuteron/gluon/T-odd status promoted.

## Integrity

- C32 tree reduction changed;
- frozen bridge roles changed;
- ART25 covariance modified;
- raw MSHT files added to Git;
- production registry changed;
- authoritative artifact changed;
- nondeterministic manifest.

---

# 31. Deliverables

Create at least:

```text
docs/next_level/c33_implementation_report.md
docs/next_level/c33_api.md
docs/next_level/c33_requirement_coverage.json
docs/next_level/c33_normative_source_integration.json
docs/next_level/c33_primary_source_manifest.json
docs/next_level/c33_source_relevance_matrix.json

docs/next_level/c33_two_root_tmd_identity.json
docs/next_level/c33_soft_collinear_provenance_graph.json

docs/next_level/c33_soft_sector_plan_manifest.json
docs/next_level/c33_soft_sector_plan_selection.json

docs/next_level/c33_vacuum_hilbert_manifest.json
docs/next_level/c33_soft_basis_manifest.json
docs/next_level/c33_soft_zero_mode_policy.json
docs/next_level/c33_soft_basis_trajectory_plan.json

docs/next_level/c33_eikonal_color_space.json
docs/next_level/c33_four_line_operator_manifest.json
docs/next_level/c33_eikonal_path_reversal_report.json

docs/next_level/c33_auxiliary_field_soft_oracle.json
docs/next_level/c33_auxiliary_direct_equivalence_report.json

docs/next_level/c33_soft_rapidity_regulator_manifest.json
docs/next_level/c33_eikonal_denominator_report.json

docs/next_level/c33_soft_diagram_ledger.json
docs/next_level/c33_soft_counterterm_ledger.json
docs/next_level/c33_soft_dependency_graph.json

docs/next_level/c33_bare_soft_factor.json
docs/next_level/c33_bare_soft_oracle_report.json

docs/next_level/c33_soft_uv_renormalization.json
docs/next_level/c33_soft_uv_anomalous_dimension_report.json

docs/next_level/c33_soft_rapidity_renormalization.json
docs/next_level/c33_soft_rapidity_anomalous_dimension.json
docs/next_level/c33_soft_collins_soper_kernel_oracle.json

docs/next_level/c33_continuum_soft_oracle.json
docs/next_level/c33_continuum_soft_validation_report.json

docs/next_level/c33_soft_regulator_matching_library.json
docs/next_level/c33_soft_regulator_roundtrip_report.json
docs/next_level/c33_soft_regulator_remainder.json

docs/next_level/c33_soft_basis_trajectory.json
docs/next_level/c33_soft_continuum_extrapolation.json
docs/next_level/c33_soft_power_correction_manifest.json

docs/next_level/c33_soft_collinear_regulator_pair.json
docs/next_level/c33_soft_collinear_compatibility_report.json
docs/next_level/c33_zero_bin_interface_contract.json

docs/next_level/c33_soft_tensor_network_manifest.json
docs/next_level/c33_soft_quantum_interface_contract.json

docs/next_level/c33_c32_continuation_gate.json
docs/next_level/c33_soft_uncertainty_budget.json
docs/next_level/c33_soft_remainder_separation.json

docs/next_level/c33_source_sufficiency_decision.json
docs/next_level/c33_no_go_decision_tree.json
docs/next_level/c33_missing_calculation_specification.md

docs/next_level/c33_holdout_report.json
docs/next_level/c33_injection_manifest.json
docs/next_level/c33_regression_report.json
docs/next_level/c33_unresolved_physics_gaps.md
```

Add ADRs for:

- two-root collinear/soft Hilbert architecture;
- vacuum B=0 versus baryonic B=1 identity;
- direct eikonal-Fock versus auxiliary-field representation;
- soft rapidity-regulator authority;
- soft zero-mode policy;
- finite-basis soft UV renormalization;
- rapidity-renormalized soft factor and CS-kernel convention;
- finite-basis-to-continuum soft conversion;
- soft-collinear compatibility;
- zero-bin interface without premature matching;
- soft tensor-network and quantum-circuit interface;
- exact continuation and no-go branches.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy soft-mode arrays, symbolic expressions, basis trajectories, and tensor-network tensors may remain outside Git under a declared content-addressed runtime directory. Commit their schemas, hashes, dimensions, mode order, and deterministic reconstruction commands.

---

# 32. Acceptance criteria

C33/S0 is complete only when:

1. The exact C32 baseline reproduces before edits.
2. Historical C11 and the C32 operator root remain unchanged.
3. A distinct B=0 soft root is created.
4. The soft root is not part of the proton-state normalization.
5. One microscopic soft-sector plan is selected before numerical comparison.
6. The finite vacuum basis is fully specified.
7. Both n and nbar rapidity regions are represented.
8. The zero-mode policy is explicit.
9. The four-line fundamental soft operator is complete.
10. Color-trace normalization is exact.
11. The tree soft factor is exactly one.
12. The modified-delta regulator signs derive from stored conventions.
13. Every required one-loop soft contribution receives an explicit status.
14. No absent contribution is silently zero.
15. A one-loop bare soft factor is calculated or fails with an exact structural status.
16. UV renormalization is explicit when claimed.
17. Rapidity renormalization is explicit when claimed.
18. Gauge dependence cancels when claimed.
19. Future/past T-even equality closes.
20. The rapidity anomalous dimension is extracted only from a valid calculation.
21. The cusp consistency relation is tested.
22. The continuum modified-delta oracle is source qualified.
23. The finite-basis result is not replaced by the continuum oracle.
24. Direct and auxiliary-field routes are distinguished.
25. Their equivalence is tested where both exist.
26. At least three soft resolutions support any trajectory claim.
27. Logarithmic, finite, and power-suppressed effects remain separate.
28. Zero-mode and endpoint effects remain visible.
29. A soft-regulator conversion is state and hadron independent when called matching.
30. No ART25 member or data enters the soft construction.
31. The soft-collinear compatibility map is explicit.
32. The zero-bin interface is explicit.
33. A valid soft sector is not mislabeled as a complete microscopic TMD.
34. C33 creates no microscopic proton export.
35. C33 does not rerun the twelve-point bridge.
36. The continuation gate is issued only after all soft and compatibility gates pass.
37. All remainder classes remain separate.
38. Unknown remainder remains nonzero-unknown.
39. The C29-C32 roles, holdouts, ancestry, and `NO_JOINT_MEASURE` remain unchanged.
40. All 642 ART25 identities and source covariance remain unchanged.
41. No fit, calibration, likelihood, posterior, optimization, reweighting, or emulator is created.
42. No process, deuteron, spin-1, gluon, T-odd, inference, or production status is promoted.
43. Every no-go result includes an exact missing-calculation specification.
44. All prior tests, builders, requirements, injections, and manifests remain passing.
45. The production registry remains exactly 216 routes.
46. All eight authoritative artifacts remain byte-identical.
47. Raw transferred source files remain outside Git absent permission.
48. Every C33 negative injection yields the expected diagnostic.
49. All C33 manifests reproduce byte-for-byte.
50. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
51. A local completion commit is created and not pushed.

C33 may complete with only a tree-level soft factor or with an exact structural no-go. A source-resolved negative result is preferable to importing the continuum soft function under the wrong regulator identity.

---

# 33. Outcome branches

## Branch A: finite-basis soft sector and rapidity renormalization close

When:

```text
C33_FINITE_BASIS_VACUUM_SOFT_SECTOR_VALIDATED
C33_SOFT_UV_RENORMALIZATION_VALIDATED
C33_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C33_SOFT_COLLINEAR_COMPATIBILITY_VALIDATED
C33_ZERO_BIN_INTERFACE_VALIDATED
```

the exact next package is:

> **C34/R0B — microscopic one-loop collinear correlator, zero-bin subtraction, UV/rapidity combination, and LF-to-project matching closure**

## Branch B: soft calculation closes but the basis trajectory does not

The exact next package is:

> **C34/S1 — soft-basis continuum trajectory, zero-mode, endpoint, and power-correction completion**

## Branch C: auxiliary-field route closes but direct finite-Fock realization does not

The exact next package is:

> **C34/S2 — auxiliary-eikonal soft root validation and conversion to the project finite-basis regulator**

## Branch D: the soft and collinear regulators are incompatible

The exact next package is:

> **C34/O3 — redesign of the microscopic collinear/soft regulator pair and overlap architecture**

## Branch E: only tree-level soft identity closes

The exact next package is:

> **C34/S0A — one-loop soft diagram, counterterm, and rapidity-renormalization completion**

## Branch F: no finite B=0 soft Hilbert construction is viable

The exact next package is:

> **C34/O4 — replace the finite-basis soft strategy with a new regulator architecture for the microscopic TMD root**

No branch automatically authorizes fitting or inference.

---

# 34. Allowed and forbidden statuses

The strongest permitted package statuses include:

```text
C33_TWO_ROOT_TMD_ARCHITECTURE_VALIDATED
C33_SOFT_SECTOR_PLAN_DECIDED
C33_FINITE_VACUUM_HILBERT_AUDITED
C33_FOUR_LINE_SOFT_OPERATOR_VALIDATED
C33_SOFT_RAPIDITY_REGULATOR_VALIDATED
C33_SOFT_DIAGRAM_LEDGER_COMPLETE
C33_CONTINUUM_SOFT_ORACLE_VALIDATED
C33_SOFT_BASIS_TRAJECTORY_AUDITED
C33_SOFT_COLLINEAR_COMPATIBILITY_DECIDED
C33_ZERO_BIN_INTERFACE_DEFINED
C33_C32_CONTINUATION_GATE_DECIDED
C33_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when every corresponding gate passes:

```text
C33_FINITE_BASIS_VACUUM_SOFT_SECTOR_VALIDATED
C33_SOFT_UV_RENORMALIZATION_VALIDATED
C33_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C33_SOFT_REGULATOR_MATCHING_VALIDATED
C33_SOFT_COLLINEAR_COMPATIBILITY_VALIDATED
C33_ZERO_BIN_INTERFACE_VALIDATED
C33_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING
```

The following remain forbidden:

```text
C33_MICROSCOPIC_PROTON_TMD_EXPORTED
BRIDGE_DISTRIBUTION_COMPARISON_READY
MICROSCOPIC_MODEL_CALIBRATED
ART25_CONSTRAINED_MICROSCOPIC_POSTERIOR
GLOBAL_LIKELIHOOD_READY
GLOBAL_INFERENCE_READY
REPLICA_REWEIGHTED
PARAMETERS_OPTIMIZED
EMULATOR_TRAINED
BRIDGE_PROCESS_READY
SOURCE_PROCESS_PROMOTED
PHYSICAL_INPUT_PROMOTED
PHYSICAL_DEUTERON_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
PHYSICAL_TODD_PROCESS_READY
PRODUCTION_READY
```

---

# 35. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- two-root collinear/soft identities;
- selected soft-sector realization plan;
- vacuum-basis dimensions and resolution trajectory;
- zero-mode and boundary policies;
- eikonal color-space and four-line operator identities;
- auxiliary-field oracle status;
- modified-delta regulator implementation;
- one-loop soft diagram and counterterm coverage;
- bare soft-factor status and values;
- UV-renormalization status and residuals;
- rapidity-renormalization status and residuals;
- rapidity anomalous dimension and CS-kernel oracle status;
- continuum modified-delta oracle residuals;
- finite-basis soft matching status, order, and remainder;
- soft-basis trajectory status;
- gauge, future/past, color, and path residuals;
- soft-collinear compatibility status;
- zero-bin-interface status;
- soft tensor-network and quantum-interface status;
- C32 continuation-gate status;
- exact no-go status when blocked;
- exact next-package branch;
- confirmation that no proton-state normalization, ART25 member, data, chi2, or bridge residual entered the soft calculation;
- confirmation that no microscopic TMD export, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a continuum oracle, an auxiliary-field methodological representation, or a tree-level vacuum identity as a completed finite-basis microscopic soft sector unless every regulator, renormalization, trajectory, and compatibility gate passes.
