# C42/M0C Codex Work Package

## Title

**Source-derived replacement of the C40 toy substrate: regulator-identical light-front QCD Hamiltonian, SU(3) quark–gluon vertex, constrained and zero-mode completion, spacelike Wilson operator, bilocal TMD measurement, partonic renormalization conditions, and basis-overlap refinement**

## Authoritative baseline

Start from the clean local C41 completion commit:

```text
cbef8d0223b228901f0b16f678e37b90364a1526
```

Its immediate scientific parent is:

```text
f30596d39d9b38ab62b1749bb103c71460987753
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor f30596d39d9b38ab62b1749bb103c71460987753 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C38_PARTONIC_STRUCTURAL_SCAFFOLD_ONLY
C39_FINITE_BASIS_ONE_LOOP_INCOMPLETE
C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY
C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL
```

and the exact C41 audit:

```text
0 of 16 required C40 objects:
    REGULATOR_IDENTICAL_EXECUTABLE

16 of 16:
    EXECUTABLE_TOY_NOT_PHYSICS_IDENTICAL
```

The fixed physical regulator architecture remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Purpose

C42 replaces the sixteen audited C40 toy objects with source-derived, regulator-identical descendants.

C40 remains immutable as:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

Its arrays continue to test:

```text
serialization
shape discipline
linear-algebra plumbing
readiness-gate behavior
fault detection
```

They may not enter a physical one-loop calculation.

C42 must not merely add source citations to the C40 formulas. It must derive new operators from the selected light-front QCD action, the fixed spacelike Wilson geometry, and the declared finite basis.

The strongest allowed status is:

```text
C42_SOURCE_DERIVED_PARTONIC_OPERATOR_SUBSTRATE_READY
```

Only after that status is earned may the actual one-loop calculation resume in:

```text
C43/R2B
```

---

# 2. Fixed scientific decisions

Do not reopen:

```text
physical TMD scheme:
    O4-SPACELIKE-COLLINS-JMY

partonic calculation scope:
    rank-zero T-even quark nonsinglet pilot

matching probe:
    nonhadronic color-fundamental q and qg sectors

soft ownership:
    universal B=0 soft factor outside the hadron TTN

hadronic parent:
    C11 remains separate and is not a matching external state

historical negative control:
    C35 finite-delta modified-delta Ward defect

historical method oracle:
    C40 m0b numerical substrate
```

C42 does not calculate:

```text
the complete one-loop correlator
the physical matching kernel
a proton TMD
an ART25 comparison
a fit or inference result
```

---

# 3. Nonnegotiable evidence standard

For every physical object, C42 must provide the complete chain:

```text
primary-source equation
    -> project convention map
    -> symbolic expression
    -> finite-basis matrix element
    -> generated numerical array
    -> independent numerical check
    -> content hash
```

A source reference without a derivation is insufficient.

A derivation without an applied numerical operator is insufficient.

An applied numerical toy with arbitrary coefficients is insufficient.

Every object must record:

```text
source locator
equation number or derivation section
gauge
field normalization
light-front convention
color normalization
basis normalization
IR prescription
spacelike direction
path ordering
perturbative order
symbolic-expression hash
generator-code hash
array hash
shape
dtype
nnz
units
basis-order hash
independent residual
```

---

# 4. Primary authorities

Read and hash-lock the exact repository copies of the relevant primary sources.

At minimum audit:

```text
Brodsky, Pauli, Pinsky, hep-ph/9705477
    light-front field quantization, QCD Hamiltonian, Fock-state
    normalization, canonical and instantaneous interactions

Belitsky, Ji, Yuan, hep-ph/0208038
    transverse gauge link at light-cone infinity and residual-gauge
    completion of TMD operators in light-cone gauge

Ji, Ma, Yuan, hep-ph/0404183
    selected off-light-cone/spacelike TMD definition, soft subtraction,
    finite-rapidity variables, and one-loop factorization convention
```

Also read the exact C36 source locks for:

```text
selected spacelike Wilson directions
soft allocation
rapidity invariant
selected-to-project conversion
endpoint and transverse-path conventions
```

Use C7-C14 only as methodological ancestors where the new derivation proves identical:

```text
field normalization
basis normalization
color action
operator ordering
gauge
external-state identity
regulator
```

Create:

```text
docs/next_level/c42_primary_source_manifest.json
docs/next_level/c42_derivation_authority_manifest.json
```

---

# 5. Audit-driven replacement map

Read:

```text
docs/next_level/c41_c40_substrate_fidelity_audit.json
```

Do not infer or rename its sixteen rows.

Create an exact one-to-one replacement table:

```text
C40 object ID
C41 fidelity reason
C42 replacement ID
primary source
derivation ID
numerical bundle
independent check
final fidelity status
```

Allowed C42 row statuses:

```text
REGULATOR_IDENTICAL_EXECUTABLE
SOURCE_DERIVED_BUT_NUMERICALLY_UNRESOLVED
SOURCE_ORACLE_ONLY
ABSENT_BLOCKING
```

A positive C42 gate requires all sixteen required rows to be:

```text
REGULATOR_IDENTICAL_EXECUTABLE
```

Create:

```text
docs/next_level/c42_c40_replacement_crosswalk.json
```

---

# 6. Gauge and canonical-action authority

Use the exact gauge convention already fixed by C36-C41.

If no finite-basis gauge is explicitly fixed, do not invent one silently. Compile and decide before deriving matrices:

```text
M0C-LIGHT_FRONT-GAUGE
    A^+ = 0 with complete constrained A^-, instantaneous interactions,
    residual-gauge boundary conditions, transverse gauge link, and
    zero-mode policy

M0C-COVARIANT-GAUGE
    complete indefinite-metric/BRST field space with ghosts and
    covariant propagating modes

M0C-GAUGE-UNAVAILABLE
```

For a light-front Hamiltonian basis, `M0C-LIGHT_FRONT-GAUGE` is preferred only when every required constrained, boundary, and zero-mode contribution can be derived from the same source-normalized action.

Create the gauge-fixed action and canonical Hamiltonian density symbolically from:

\[
\mathcal L_{\rm QCD}
=
-\frac14F_{\mu\nu}^aF^{a\mu\nu}
+
\bar\psi(i\gamma^\mu D_\mu-m)\psi
+
\mathcal L_{\rm gf}
+
\mathcal L_{\rm ghost},
\]

with the selected terms specialized according to the chosen gauge.

Store:

```text
dynamical fields
constrained fields
canonical momenta
equal-x+ commutators/anticommutators
mode expansions
gauge constraints
boundary conditions
zero-mode constraints
Hamiltonian terms through the order required for q/qg matching
```

Create:

```text
docs/next_level/c42_gauge_plan.json
docs/next_level/c42_light_front_action_derivation.md
docs/next_level/c42_hamiltonian_term_ledger.json
```

If the gauge-fixed action is incomplete, stop with:

```text
C42_GAUGE_FIXED_ACTION_INCOMPLETE
```

---

# 7. Source-derived finite-basis modes

Construct new C42 q and qg bases from the actual project longitudinal and transverse mode functions.

Do not reuse the C40 coordinate recipes as physical modes.

For every resolution retain:

```text
K
longitudinal boundary condition
positive quark modes
positive nonzero gluon modes
Nmax
bHO
2D harmonic-oscillator radial and angular labels
helicity
flavor
fundamental quark color
adjoint gluon color
center-of-mass policy
zero-mode policy
normalization measure
```

Generate the basis vectors by integrating the source-normalized field modes.

Required numerical checks:

```text
Gram matrix from actual mode overlaps
orthonormality
free light-front momentum reconstruction
free invariant mass
color metric
helicity metric
resolution comparison
```

If the C40 resolutions \(K=17,23,31\) are not compatible with the exact project boundary convention, preserve them as method-oracle resolutions and create corrected physical resolutions with a typed comparison. Do not force source formulas onto incompatible labels.

Create:

```text
docs/next_level/c42_source_derived_basis_manifest.json
docs/next_level/c42_basis_normalization_report.json
```

---

# 8. Free light-front Hamiltonians

Derive:

\[
P^-_{0,q},
\qquad
P^-_{0,qg}
\]

from the source-normalized QCD action and project them onto the C42 bases.

Construct:

```text
Hq_source
Hqg_source
```

as sparse matrices and independent matrix-free actions.

Required checks:

```text
Hermiticity
free dispersion
mass-IR dependence
basis normalization
assembled/matrix-free agreement
independent direct diagonal-element evaluation
resolution behavior
```

No hand-selected off-diagonal texture is allowed.

Create:

```text
docs/next_level/c42_free_hamiltonian_derivation.json
docs/next_level/c42_free_hamiltonian_validation.json
```

---

# 9. Canonical SU(3) q -> qg vertex

Derive the canonical quark–gluon interaction from the same QCD Hamiltonian.

Use the exact generator convention:

\[
T^a=\frac{\lambda^a}{2},
\qquad
\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab},
\qquad
C_F=\frac43,
\]

or the exact equivalent convention already frozen by the project.

Construct:

\[
V^{\rm QCD}_{qg\leftarrow q}
\]

by evaluating the field-mode matrix element, including:

```text
spinor numerator
gluon polarization
longitudinal normalization
transverse oscillator overlap
fundamental SU(3) generator
momentum conservation
fermionic sign
mass-IR dependence
```

Generate the absorption matrix as the adjoint.

Required checks:

```text
pointwise continuum-mode vertex oracle
all eight SU(3) generator actions
Casimir identities
color-generator covariance
helicity selection
longitudinal conservation
transverse-overlap quadrature
adjoint closure
nonzero action on physical probe vectors
```

Create:

```text
docs/next_level/c42_qg_vertex_derivation.json
docs/next_level/c42_qg_vertex_validation.json
```

The C40 vertex remains a toy regression comparator only.

---

# 10. Constrained and instantaneous sectors

Derive from the same gauge-fixed action:

```text
instantaneous-fermion operator
instantaneous-gluon operator
constrained-field operator
contact terms
residual-gauge boundary operator
```

For every term, provide:

```text
source equation
constraint solution
operator ordering
basis matrix element
numerical matrix or exact proof of non-applicability
```

Allowed statuses:

```text
REGULATOR_IDENTICAL_EXECUTABLE_NONZERO
REGULATOR_IDENTICAL_EXECUTABLE_ZERO_BY_EXACT_PROOF
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF
ABSENT_BLOCKING
```

Construct an operator-level Ward or current-conservation identity using the source-derived propagating and constrained terms.

Required ablations:

```text
remove canonical vertex
remove instantaneous fermion
remove instantaneous gluon
remove constrained term
remove boundary term
```

Every required removal must give a signed nonzero defect.

Create:

```text
docs/next_level/c42_constrained_sector_derivation.json
docs/next_level/c42_ward_identity_report.json
```

---

# 11. Zero modes and residual gauge fields

Treat separately:

```text
gluon k^+=0 modes
constrained fermion zero modes
residual transverse gauge fields at infinity
Wilson-endpoint zero modes
```

For each, derive one of:

```text
retained numerical sector
exact constrained solution
proved power-suppressed/excluded contribution
blocking unresolved term
```

Historical absence from the basis is not a proof of zero.

The transverse gauge link required by the selected gauge must be represented as an operator, not a status record.

Create:

```text
docs/next_level/c42_zero_mode_derivation.json
docs/next_level/c42_residual_gauge_boundary_report.json
```

---

# 12. Regulator-identical spacelike Wilson operator

Use the exact C36 Ji–Ma–Yuan spacelike path, not a generic finite segment.

Store the source-defined:

```text
spacelike direction v
v^2 < 0
conjugate direction
rapidity invariant
future/past orientation
longitudinal segment
transverse closure
endpoint/junction structure
path and anti-path ordering
limit order
```

Derive:

\[
W_v^{(1)}
=
ig\int ds\,v\cdot A^a(x+sv)T^a
\]

from the same gauge-fixed mode expansion used by the Hamiltonian.

Construct actual matrices for:

```text
longitudinal spacelike emission
conjugate/absorption
transverse gauge-link emission
endpoint/junction contact
constrained-field contribution to v dot A
```

Required checks:

```text
direct path quadrature
analytic mode-integral oracle
path reversal
conjugation
color covariance
finite-rapidity dependence
transverse displacement phase
endpoint continuity
residual-gauge transformation
controlled large-length/off-light-cone limit
```

Create:

```text
docs/next_level/c42_spacelike_wilson_derivation.json
docs/next_level/c42_spacelike_wilson_validation.json
```

The C40 Wilson matrices remain method oracles and cannot be rescaled into the C42 result.

---

# 13. Source-derived bilocal TMD measurement

Construct the rank-zero quark bilocal operator in the fixed selected scheme:

\[
\bar\psi(-z/2)\gamma^+
W_v^\dagger(-z/2,\infty)
W_v(\infty,z/2)
\psi(z/2)
\Big|_{z^+=0},
\]

with the exact C36 path and soft-allocation convention.

Materialize finite-basis measurement operators for:

```text
q -> q tree matrix element
q -> q real measurement
qg -> qg real measurement
q <-> qg Wilson/operator transition
transverse displacement bT
longitudinal Fourier/test-function action
future/past T-even relation
positive-x antiquark charge conjugation
```

The distributional measurement must descend from this bilocal operator.

Do not build it by assigning desired delta/plus weights independently.

Required checks:

```text
tree delta endpoint
quark-number moment
translation covariance
Hermiticity
charge conjugation
future/past equality at T-even scope
direct coordinate-space versus basis-matrix evaluation
```

Create:

```text
docs/next_level/c42_bilocal_operator_derivation.json
docs/next_level/c42_bilocal_measurement_validation.json
```

---

# 14. Distributional finite-K functionals

Derive the discrete distribution functional from the actual longitudinal basis and bilocal Fourier transform.

Construct numerical actions for:

```text
regular test functions
delta(1-x)
lower-limit plus distribution
log-plus distribution
Mellin moments
convolution
```

Every weight must follow from:

```text
basis cell/support
quadrature measure
endpoint subtraction
test-function definition
```

Required checks:

```text
support 0 < x <= 1
constant-test-function plus identity
quark-number moment
independent direct Fourier sum
rank and nullspace
refinement across physical resolutions
```

Do not use ART25 points or arbitrary interpolation.

Create:

```text
docs/next_level/c42_distribution_functional_derivation.json
docs/next_level/c42_distribution_functional_validation.json
```

---

# 15. Physical counterterm operator basis and conditions

Derive the counterterm operators allowed by the selected gauge-fixed Hamiltonian, regulator, and bilocal operator.

At minimum audit:

```text
quark mass
quark field
canonical qg vertex
instantaneous partners
bilocal operator
spacelike Wilson line
endpoint/cusp
transverse closure
basis boundary
sector truncation
```

For each retained coefficient define a source-supported partonic renormalization condition.

Examples of acceptable condition classes include:

```text
partonic pole or invariant-mass condition
partonic residue/normalization condition
canonical vertex condition at frozen kinematics
Ward/Slavnov identity at declared scope
bilocal local-current limit
Wilson-line endpoint/length renormalization condition
```

Do not solve physical one-loop values in C42.

Construct the exact coefficient matrix generator:

\[
A_{\rm CT}^{\rm phys}
\]

from derivatives of the source-derived operators with respect to the retained coefficients.

Required checks:

```text
rank
nullspace
condition number
independent finite-difference derivative
condition independence
no proton or ART25 input
```

Create:

```text
docs/next_level/c42_counterterm_operator_derivation.json
docs/next_level/c42_counterterm_condition_system.json
```

---

# 16. Source-derived refinement and comparison maps

Do not reuse coordinate interpolation as a physical refinement map.

Construct maps from actual basis overlaps:

\[
P_{r\to r'},
\qquad
R_{r'\to r}.
\]

For changes in transverse oscillator basis, calculate overlap integrals between the two sets of normalized mode functions.

For changes in longitudinal resolution, construct the source-defined distribution-functional comparison map; do not claim exact nesting when the discrete grids are nonnested.

Required checks:

```text
Gram-metric adjoint relation
normalization preservation
quark-number moment preservation
free-Hamiltonian consistency
canonical-vertex consistency
Wilson-operator consistency
bilocal-measurement consistency
reported remainder for nonnested maps
```

Create:

```text
docs/next_level/c42_refinement_derivation.json
docs/next_level/c42_refinement_validation.json
```

---

# 17. C40 comparison and supersession

For every one of the sixteen rows, compare:

```text
C40 toy numerical object
C42 source-derived object
```

Report:

```text
shape
norm
spectrum where applicable
matrix-element differences
symmetry differences
which C40 tests remain useful
why numerical closeness does not establish identity
```

Do not fit C42 coefficients to reproduce C40 arrays.

Create a typed edge:

```text
C40 object:
    EXECUTABLE_METHOD_ORACLE_ONLY

C42 object:
    REGULATOR_IDENTICAL_EXECUTABLE
```

only when the full derivation chain closes.

Create:

```text
docs/next_level/c42_c40_comparison_report.json
docs/next_level/c42_operator_supersession_report.json
```

---

# 18. End-to-end regulator-identity test

Implement a test that begins from source equations rather than prebuilt arrays.

It must:

```text
load source/convention records
generate normalized q/qg modes
derive Hq and Hqg
derive the SU(3) qg vertex
derive constrained-sector matrices
derive the spacelike Wilson matrix
derive the bilocal measurement
derive A_CT_phys
derive refinement maps
apply every object to nonzero vectors
verify all independent identities
```

The test must fail when:

```text
a source locator is removed
a symbolic-expression hash changes
a C40 toy array is substituted
an arbitrary coefficient is inserted
a constrained term is omitted
the transverse gauge link is omitted
a counterterm condition is changed
a bilocal weight is hand edited
a refinement map is replaced by interpolation metadata
```

---

# 19. Focused fault tests

Create at least 160 focused faults operating on actual C42 derivations and arrays.

Include:

```text
change field normalization
change gamma-matrix convention
change a Gell-Mann generator
drop a color factor
change a helicity spinor
break longitudinal conservation
change oscillator normalization
remove an instantaneous term
remove the residual boundary field
drop a zero-mode control
replace v by a lightlike direction
change path order
drop transverse closure
replace Wilson matrix with C40 matrix
change bilocal Fourier phase
hand-edit a plus-distribution weight
change a counterterm condition
hide a null direction
replace an overlap refinement map with coordinate interpolation
```

Each mutation must fail an actual derivation, matrix, or identity check.

---

# 20. Readiness gate

Issue:

```text
C42_SOURCE_DERIVED_PARTONIC_OPERATOR_SUBSTRATE_READY
```

only when:

```text
all sixteen C41 audit rows are REGULATOR_IDENTICAL_EXECUTABLE
the gauge-fixed action is complete at declared scope
the q/qg modes are source normalized
Hq and Hqg are source derived
the SU(3) qg vertex is source derived
the constrained and zero-mode sectors close
the spacelike Wilson operator is source derived
the bilocal measurement is source derived
the counterterm conditions are physically defined
the refinement maps descend from basis overlaps/functionals
the end-to-end regulator-identity test passes
```

Do not issue a matching status.

---

# 21. Exact no-go branches

## A. Gauge-fixed action incomplete

```text
C42_GAUGE_FIXED_ACTION_INCOMPLETE
```

Next:

> **C43/G0 — complete light-front gauge action, constraints, residual gauge fields, and zero modes**

## B. Hamiltonian or canonical vertex incomplete

```text
C42_LIGHT_FRONT_HAMILTONIAN_DERIVATION_INCOMPLETE
```

Next:

> **C43/HQCD — source-derived q/qg Hamiltonian and SU(3) vertex completion**

## C. Constrained or zero-mode sector incomplete

```text
C42_CONSTRAINED_ZERO_MODE_SECTOR_INCOMPLETE
```

Next:

> **C43/Z2 — instantaneous, constrained, zero-mode, and transverse-boundary completion**

## D. Spacelike Wilson operator incomplete

```text
C42_SPACELIKE_WILSON_OPERATOR_INCOMPLETE
```

Next:

> **C43/W1 — finite-basis Ji–Ma–Yuan Wilson path and endpoint completion**

## E. Bilocal measurement incomplete

```text
C42_BILOCAL_MEASUREMENT_INCOMPLETE
```

Next:

> **C43/X2 — source-derived finite-K bilocal and distributional measurement completion**

## F. Counterterm conditions incomplete

```text
C42_COUNTERTERM_CONDITIONS_INCOMPLETE
```

Next:

> **C43/CT2 — partonic renormalization-condition and operator-counterterm completion**

## G. Refinement maps incomplete

```text
C42_REFINEMENT_MAP_INCOMPLETE
```

Next:

> **C43/R1C — basis-overlap and distribution-functional refinement completion**

## H. All replacements close

```text
C42_SOURCE_DERIVED_PARTONIC_OPERATOR_SUBSTRATE_READY
```

Next:

> **C43/R2B — one-loop finite-basis spacelike nonsinglet quark TMD and state-independent matching**

---

# 22. Required deliverables

Create at least:

```text
docs/next_level/c42_implementation_report.md
docs/next_level/c42_api.md

docs/next_level/c42_primary_source_manifest.json
docs/next_level/c42_derivation_authority_manifest.json
docs/next_level/c42_c40_replacement_crosswalk.json

docs/next_level/c42_gauge_plan.json
docs/next_level/c42_light_front_action_derivation.md
docs/next_level/c42_hamiltonian_term_ledger.json

docs/next_level/c42_source_derived_basis_manifest.json
docs/next_level/c42_basis_normalization_report.json
docs/next_level/c42_free_hamiltonian_derivation.json
docs/next_level/c42_free_hamiltonian_validation.json

docs/next_level/c42_qg_vertex_derivation.json
docs/next_level/c42_qg_vertex_validation.json

docs/next_level/c42_constrained_sector_derivation.json
docs/next_level/c42_ward_identity_report.json
docs/next_level/c42_zero_mode_derivation.json
docs/next_level/c42_residual_gauge_boundary_report.json

docs/next_level/c42_spacelike_wilson_derivation.json
docs/next_level/c42_spacelike_wilson_validation.json

docs/next_level/c42_bilocal_operator_derivation.json
docs/next_level/c42_bilocal_measurement_validation.json
docs/next_level/c42_distribution_functional_derivation.json
docs/next_level/c42_distribution_functional_validation.json

docs/next_level/c42_counterterm_operator_derivation.json
docs/next_level/c42_counterterm_condition_system.json

docs/next_level/c42_refinement_derivation.json
docs/next_level/c42_refinement_validation.json

docs/next_level/c42_c40_comparison_report.json
docs/next_level/c42_operator_supersession_report.json

docs/next_level/c42_readiness_report.json
docs/next_level/c42_source_sufficiency_decision.json
docs/next_level/c42_no_go_decision_tree.json
docs/next_level/c42_missing_calculation_specification.md
docs/next_level/c42_regression_report.json
```

Commit schemas and hashes for heavy runtime arrays.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

---

# 23. Acceptance criteria

C42 is complete only when:

1. The full C41 baseline reproduces.
2. C40 remains method-oracle only.
3. The fixed C36 spacelike scheme is unchanged.
4. The sixteen-row replacement crosswalk is exact.
5. Every positive object has a primary-source derivation.
6. Every positive object has a symbolic-expression hash.
7. Every positive object has a generated numerical array and hash.
8. The gauge-fixed action is complete at declared scope.
9. The finite-basis modes are source normalized.
10. The free Hamiltonians are source derived.
11. The canonical qg vertex is source derived with exact SU(3).
12. Absorption is the generated adjoint.
13. Constrained and instantaneous sectors derive from the same action.
14. Zero-mode and residual-boundary statuses are source justified.
15. The Ward identity closes only with all required terms.
16. The spacelike Wilson matrix descends from the exact C36 path.
17. Transverse closure and endpoints are explicit.
18. The bilocal measurement descends from the operator definition.
19. Distributional weights descend from the bilocal Fourier action.
20. Counterterm operators and conditions are partonic and source supported.
21. Refinement maps descend from basis overlaps or exact functionals.
22. C40 arrays are never fitted or rescaled into C42 arrays.
23. The end-to-end regulator-identity test passes.
24. At least 160 live derivation/array mutations are detected.
25. No one-loop coefficient or physical counterterm solution is fabricated.
26. No matching kernel is created.
27. No proton TMD or ART25 bridge is created.
28. No fit, inference, process, or production route is created.
29. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
30. `MSHT20_REP/` remains untouched and outside Git.
31. Runtime arrays and manifests reproduce deterministically.
32. The working tree is clean except for the pre-existing untracked directory.
33. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken source identity, gauge completion, Wilson geometry, bilocal identity, or refinement authority to open the gate.

---

# 24. Final Codex response

Report:

- full starting and final commits;
- the exact sixteen-row C40-to-C42 replacement table;
- primary sources, versions, hashes, and equation locators;
- selected gauge realization;
- gauge-fixed action and constrained-field content;
- physical resolution identities and basis dimensions;
- Gram and normalization residuals;
- free-Hamiltonian shapes, nnz, spectra, and matrix-free residuals;
- SU(3) qg-vertex shapes, nnz, norms, Casimir/color residuals, and adjoint residuals;
- instantaneous, constrained, zero-mode, and residual-boundary statuses and norms;
- Ward residual and every ablation defect;
- spacelike Wilson component shapes, norms, and independent-check residuals;
- bilocal measurement shapes and tree/current/charge-conjugation residuals;
- distribution-functional ranks, nullspaces, and moment residuals;
- counterterm operator-system shape, rank, nullity, conditioning, and condition definitions;
- refinement-map shapes and Hamiltonian/vertex/Wilson/measurement consistency residuals;
- focused fault-test results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no one-loop matching, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a deterministic numerical recipe, a source citation, or an internally consistent toy as regulator-identical QCD.
