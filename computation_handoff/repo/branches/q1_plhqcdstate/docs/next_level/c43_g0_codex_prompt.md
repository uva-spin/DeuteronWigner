# C43/G0 Codex Work Package

## Title

**Primary-source closure and complete light-front-gauge QCD action for the finite-basis \(q/qg\) TMD-matching sector**

## Authoritative baseline

Start from the clean local C42/M0C completion commit:

```text
4c8ab287218c185509226d933c9b5585abcc4f45
```

Its immediate scientific parent is:

```text
cbef8d0223b228901f0b16f678e37b90364a1526
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor cbef8d0223b228901f0b16f678e37b90364a1526 HEAD
```

The baseline is authoritative only when it reproduces:

```text
C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY
    with every C40 numerical object retained as method-oracle only;

C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL;

C42_GAUGE_FIXED_ACTION_INCOMPLETE;

all sixteen C41 replacement rows:
    ABSENT_BLOCKING.
```

The fixed physical TMD architecture remains:

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

# 1. Exact purpose

C43 must remove the prior source-authority obstruction and derive one internally consistent gauge-fixed QCD action at the exact scope needed for later finite-basis \(q/qg\) matching.

C43 is not a numerical Hamiltonian package and is not a one-loop matching package.

Its positive endpoint is:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION
```

That status means:

```text
the primary sources are present and hash locked;
one gauge realization is selected;
the light-front canonical action is explicitly derived;
dynamical and constrained fields are identified;
inverse longitudinal derivatives and zero modes are defined;
instantaneous interactions are derived;
residual gauge transformations and the transverse link are defined;
the Ji-Ma-Yuan spacelike Wilson path is compatible with that action;
a finite-basis projection contract is complete.
```

It does **not** mean that Hamiltonian matrices, Wilson matrices, bilocal-measurement matrices, counterterm matrices, or a matching coefficient have been calculated.

When the positive gate passes, the next package is:

> **C44/HQCD — project the source-derived action into the physical finite basis and construct the regulator-identical \(q/qg\) Hamiltonians and SU(3) vertices**

---

# 2. Why C43 must be source-first

C42 stopped because the repository contained the Ji–Ma–Yuan source but not the two primary authorities explicitly required by the C42 contract:

```text
hep-ph/9705477
    Brodsky–Pauli–Pinsky

hep-ph/0208038
    Belitsky–Ji–Yuan
```

Those papers are public. Their absence from the local repository is not a reason to redesign the physics.

C43 is explicitly authorized to obtain and hash-lock public arXiv sources and source archives.

However, simply downloading the two missing PDFs is not enough. The broad Brodsky–Pauli–Pinsky review and the Belitsky–Ji–Yuan transverse-link analysis do not by themselves constitute one unique finite-basis canonical action. C43 must also lock a focused light-front-QCD action authority and prove that all retained conventions are compatible.

---

# 3. Mandatory primary-source bundle

Obtain exact official arXiv versions, preserving both PDF and TeX/source archive when available.

## 3.1 Required sources

```text
hep-ph/9705477v1
S. J. Brodsky, H.-C. Pauli, S. S. Pinsky
Quantum Chromodynamics and Other Field Theories on the Light Cone

Role:
    broad light-front-QCD, Fock-space, Hamiltonian, finite-volume,
    normalization, and renormalization authority
```

```text
hep-ph/0011372v2
P. P. Srivastava, S. J. Brodsky
Light-Front-Quantized QCD in Light-Cone Gauge:
The Doubly Transverse Gauge Propagator

Role:
    focused Dirac-constraint, gauge-field, propagator,
    interaction-Hamiltonian, and instantaneous-interaction authority
```

```text
hep-ph/0208038v2
A. V. Belitsky, X. Ji, F. Yuan
Final State Interactions and Gauge Invariant Parton Distributions

Role:
    residual gauge field and transverse gauge link at light-cone infinity
```

```text
hep-ph/0404183v1
X. Ji, J.-P. Ma, F. Yuan
QCD Factorization for Semi-Inclusive Deep-Inelastic Scattering
at Low Transverse Momentum

Role:
    fixed spacelike/off-light-cone TMD operator, soft subtraction,
    finite-rapidity geometry, and factorization convention
```

## 3.2 Required supporting audits

Audit, but do not silently promote, at least:

```text
hep-th/0008096v1
T. Heinzl
Light-Cone Quantization: Foundations and Applications

Role:
    finite-volume, canonical-quantization, inverse-derivative,
    and zero-mode methodology; not a substitute for the QCD action
```

```text
1005.4305
J.-H. Gao
Derivation of the Gauge Link in Light Cone Gauge

Role:
    independent transverse-link and boundary-prescription cross-check
```

If the mandatory sources do not uniquely determine a zero-mode or boundary prescription at the required scope, locate and lock the additional primary authority rather than filling the gap from memory.

## 3.3 Acquisition rules

Store raw source material under:

```text
data/raw/c43_sources/
```

If repository policy forbids committing large source binaries, keep them ignored but commit:

```text
arXiv identifier and exact version
official title and authors
downloaded filename
SHA-256
byte size
PDF page count
source-archive SHA-256
deterministic download command
local required path
license/source metadata
```

Prefer source TeX for equation extraction. Do not use OCR when TeX or parsed PDF text is available.

Third-party mirrors are not source authority unless their bytes are checked against the official arXiv version.

Create:

```text
docs/next_level/c43_primary_source_manifest.json
docs/next_level/c43_source_relevance_matrix.json
```

---

# 4. Source-sufficiency gate

Before deriving the action, construct a source-sufficiency table with rows for:

```text
light-front coordinate and metric convention
spinor projectors
dynamical and constrained fermion fields
gauge condition
Dirac constraints
canonical brackets
gluon mode expansion
fermion mode expansion
free propagators
inverse partial-plus prescription
canonical q-q-g vertex
three-gluon term
four-gluon term
instantaneous fermion interaction
instantaneous gluon/current interaction
ghost status
zero-mode status
residual gauge transformations
boundary conditions at light-cone infinity
transverse gauge link
spacelike Ji-Ma-Yuan Wilson direction
soft/collinear operator compatibility
finite-volume/basis projection
```

Every row must have:

```text
primary source
exact locator
source convention
project convention
conversion equation
scope
unresolved issue
```

Allowed row statuses:

```text
SOURCE_COMPLETE_AND_COMPATIBLE
SOURCE_COMPLETE_REQUIRES_CONVENTION_MAP
METHOD_ONLY
CONFLICT_REQUIRES_DECISION
ABSENT_BLOCKING
```

Do not begin a positive derivation while a required row remains `ABSENT_BLOCKING`.

Create:

```text
docs/next_level/c43_source_sufficiency_matrix.json
```

---

# 5. Select one gauge realization

Compile exactly:

```text
G0-LIGHT-FRONT-GAUGE
G0-COVARIANT-GAUGE
G0-UNAVAILABLE
```

The expected primary candidate is:

```text
G0-LIGHT-FRONT-GAUGE
```

but it may be selected only if the complete declared-scope constraint, boundary, and zero-mode structure can be written from the locked sources.

Do not write merely “\(A^+=0\)” without resolving the project’s \(n,\bar n,+,-\) convention.

The selection record must state:

```text
which component is set to zero
the gauge-fixing vector
the residual gauge freedom
the light-cone pole prescription
the inverse-derivative prescription
the boundary condition
the zero-mode projector
ghost status
the relation to the spacelike JMY Wilson direction
```

If the selected light-front action employs a doubly transverse propagator or an additional Lorentz condition, record its precise operator meaning and source scope.

Create:

```text
docs/next_level/c43_gauge_plan.json
docs/next_level/c43_gauge_convention_map.json
```

---

# 6. Freeze project conventions

Map every source to the existing project convention:

\[
v^\pm=\frac{v^0\pm v^3}{\sqrt2},
\qquad
g^{\mu\nu}=\operatorname{diag}(1,-1,-1,-1),
\qquad
n\cdot\bar n=1.
\]

Explicitly record:

```text
x+ as light-front time
which vector contracts to v+
which vector contracts to v-
partial-plus and partial-minus
gamma-plus and gamma-minus
A-plus and A-minus
integration measure
Fourier phase
covariant-derivative sign
SU(3) generator normalization
```

Do not inherit ambiguous notation from any paper.

Create machine-checkable identities for:

\[
n^2=\bar n^2=0,
\qquad
n\cdot\bar n=1,
\qquad
v^2=2v^+v^- - \mathbf v_T^2.
\]

Create:

```text
docs/next_level/c43_light_front_conventions.json
```

---

# 7. Derive the gauge-fixed action

Begin from:

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

using the project conventions.

Derive, rather than merely quote:

```text
the gauge-fixed Lagrangian
canonical momenta at fixed x+
primary and secondary constraints
Dirac constraint matrix
Dirac brackets or equivalent reduced phase-space brackets
dynamical fields
constrained fields
free Hamiltonian density
interaction Hamiltonian density through the q/qg one-loop scope
```

The declared completeness scope is:

```text
one external quark
qg intermediate/real states
rank-zero T-even nonsinglet bilocal operator
terms required through O(g^2)
the selected spacelike Wilson insertion
```

It is not a claim of a complete nonperturbative QCD Hamiltonian for every Fock sector.

Create:

```text
references/c43_light_front_qcd_gauge_action.tex
docs/next_level/c43_action_derivation_manifest.json
```

---

# 8. Fermion constraint

Define the good and bad spinor components from source-derived projectors:

\[
\psi=\psi_+ + \psi_-.
\]

Derive the constraint equation for \(\psi_-\), including:

```text
mass term
transverse covariant derivative
inverse longitudinal derivative
gauge-field coupling
boundary/zero-mode term
```

Specify exactly:

```text
the domain of the inverse derivative
the excluded or retained zero-mode subspace
the boundary kernel
Hermiticity/anti-Hermiticity convention
```

Substitute the constraint back into the action and identify:

```text
free fermion Hamiltonian
canonical q-q-g vertex contributions
instantaneous-fermion interaction
contact/operator terms relevant at O(g^2)
```

Create:

```text
docs/next_level/c43_fermion_constraint_derivation.json
```

---

# 9. Gauge-field constraint and Gauss law

Derive the constrained gauge component from the non-Abelian Gauss law.

Retain:

```text
quark color current
gluon color current
non-Abelian self-interaction
inverse longitudinal derivatives
boundary contribution
zero-mode contribution
```

Substitution into the action must identify:

```text
propagating transverse gluons
canonical q-q-g interaction
three-gluon and four-gluon interactions
instantaneous color-current interaction
additional constrained/contact terms
```

At the C43 \(q/qg\) nonsinglet scope, classify each term as:

```text
REQUIRED_AT_O_G2
REQUIRED_AS_COUNTERTERM_OR_WARD_PARTNER
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF
OUTSIDE_SCOPE_BUT_RETAINED
UNRESOLVED_BLOCKING
```

Create:

```text
docs/next_level/c43_gauge_constraint_derivation.json
docs/next_level/c43_hamiltonian_term_ledger.json
```

Do not infer non-applicability from a missing Fock sector alone.

---

# 10. Canonical brackets and mode expansions

Derive source-normalized equal-\(x^+\) relations for:

```text
dynamical quark fields
transverse gluon fields
color indices
helicity/polarization indices
```

Write the continuum mode expansions with explicit:

```text
longitudinal measure
transverse measure
creation and annihilation normalization
spinor normalization
polarization completeness
color normalization
```

Derive the free propagators and verify the exact transversality or gauge identities appropriate to the selected action.

These mode expansions are the authority for C44 numerical matrix elements.

Create:

```text
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_free_propagator_checks.json
```

---

# 11. Inverse longitudinal derivatives

Define executable symbolic kernels for:

\[
\frac{1}{\partial^+},
\qquad
\frac{1}{(\partial^+)^2},
\]

or the exact component implied by the convention map.

Compile and decide among source-supported boundary prescriptions:

```text
RETARDED
ADVANCED
ANTISYMMETRIC_OR_PV
SOURCE_SPECIFIC_OTHER
UNAVAILABLE
```

Retain separately:

```text
nonzero-mode action
zero-mode projector
boundary term
Hermiticity property
momentum-space pole prescription
```

The choice must be compatible with:

```text
canonical Hamiltonian
residual gauge transformation
transverse link
future/past TMD path
```

Create:

```text
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
```

---

# 12. Residual gauge freedom and transverse link

Use the Belitsky–Ji–Yuan source to derive the residual gauge transformation at light-cone infinity and the necessary transverse gauge link.

Record:

```text
boundary condition
advanced/retarded/PV relation
transverse field at infinity
endpoint transformation
future/past path difference
transverse-link orientation
composition with the spacelike longitudinal segment
```

Verify symbolically that the complete bilocal path transforms covariantly.

The transverse link is an operator component, not a gauge-choice status string.

Use the independent gauge-link derivation source only as a cross-check.

Create:

```text
docs/next_level/c43_residual_gauge_derivation.json
docs/next_level/c43_transverse_link_derivation.json
docs/next_level/c43_operator_gauge_covariance_report.json
```

---

# 13. Zero-mode contract

Separate:

```text
fermion constrained zero modes
gluon longitudinal zero modes
transverse residual-gauge zero modes
global color/constraint zero modes
Wilson-endpoint zero modes
```

For each define one of:

```text
RETAINED_DYNAMICAL
SOLVED_CONSTRAINED
EXCLUDED_WITH_SOURCE_PROOF_AND_BOUNDARY_CONDITION
CANCELS_WITH_DECLARED_BOUNDARY_TERM
UNRESOLVED_BLOCKING
```

If finite-volume \(A^+=0\) cannot be imposed globally because of a gauge zero mode, do not hide this fact. State the attainable gauge and the impact on the finite-basis projection.

The positive C43 gate requires a complete policy at the declared perturbative q/qg scope; it does not require solving nonperturbative vacuum structure beyond that scope.

Create:

```text
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json
```

---

# 14. Spacelike Ji–Ma–Yuan operator compatibility

Import the C36 spacelike directions and operator geometry read-only.

Demonstrate that the selected gauge-fixed field content supports:

\[
W_v(x,\infty)
=
P\exp\left[
ig\int_0^\infty ds\,v\cdot A^a(x+sv)T^a
\right],
\qquad
v^2<0,
\]

together with the required transverse closure.

Record:

```text
v components in project light-front coordinates
v dot A in terms of dynamical and constrained fields
future/past orientation
endpoint and transverse-link composition
finite-rapidity invariant
order of the large-length and rapidity limits
```

Do not set the spacelike Wilson line to unity merely because one light-front component of \(A^\mu\) is gauge fixed.

Create:

```text
docs/next_level/c43_jmy_action_compatibility.json
```

---

# 15. Bilocal-operator compatibility contract

C43 need not construct numerical bilocal measurement matrices.

It must show that the action and boundary contract support the selected rank-zero quark operator:

\[
\bar\psi(-z/2)\gamma^+
W_v^\dagger(-z/2,\infty)
W_v(\infty,z/2)
\psi(z/2)
\Big|_{z^+=0}.
\]

Record:

```text
field components entering the operator
Wilson segments
transverse closure
gauge transformation
Hermitian conjugation
future/past relation
positive-x antiquark charge conjugation
tree local-current limit
```

Create:

```text
docs/next_level/c43_bilocal_operator_compatibility.json
```

---

# 16. Finite-basis projection contract

C43 must define how the source action is to be projected in C44.

Use the actual project regulator, not the C40 toy dimensions.

Audit and freeze:

```text
physical longitudinal K values
fermion half-integer boundary convention
gluon nonzero-integer boundary convention
transverse 2D oscillator basis
Nmax
bHO
mass-IR regulator
center-of-mass policy
color basis
helicity basis
zero-mode policy
endpoint regulator
```

The historical C7/C32 physical regulator trajectory and the C40 toy \(K=17,23,31\) substrate must remain distinct.

Define the matrix-element interfaces for:

```text
Hq
Hqg
V_qg<-q
instantaneous fermion
instantaneous gluon/current
constrained term
boundary term
zero-mode term
spacelike Wilson emission
bilocal measurement
counterterm operators
```

Do not generate the numerical matrices in C43.

Create:

```text
docs/next_level/c43_finite_basis_projection_contract.json
docs/next_level/c43_physical_resolution_plan.json
```

---

# 17. Symbolic and operator-level validation

Implement executable symbolic checks for:

```text
light-front metric identities
spinor projector identities
canonical bracket consistency
fermion constraint substitution
Gauss-law substitution
Hermiticity of the Hamiltonian density
SU(3) generator convention
propagator/gauge transversality
inverse-derivative Hermiticity
residual-gauge endpoint cancellation
transverse-link covariance
spacelike-Wilson gauge covariance
tree bilocal local-current limit
```

Construct a term-completeness ledger and perform symbolic ablations.

Removing each required term must create a nonzero residual in the appropriate identity.

These are action-level tests, not numerical matrix-element tests.

---

# 18. Focused fault testing

Create at least 128 focused mutations of source, convention, constraint, and boundary objects.

Include:

```text
remove a mandatory PDF/source archive
change an arXiv version
change n dot nbar
swap plus and minus
change the covariant-derivative sign
change a spinor projector
omit the fermion constraint
omit the gauge constraint
change the inverse-derivative boundary prescription
drop the zero-mode projector
remove the instantaneous fermion term
remove the instantaneous color-current term
remove the transverse link
remove an endpoint transformation
set v lightlike
set v dot A to zero by hand
change an SU(3) normalization
replace a source locator with a review-only locator
alias the C40 toy action to the C43 action
```

Every mutation must fail a concrete source-sufficiency, symbolic, or gauge-covariance check.

Do not inflate the count with identifier-only dispatch.

---

# 19. Readiness gate

Issue:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION
```

only when:

```text
all mandatory source PDFs and source archives are present and hash locked;
the source-sufficiency matrix has no required ABSENT_BLOCKING row;
one gauge realization is selected;
all project conventions are unambiguous;
the gauge-fixed action is explicitly derived;
fermion and gauge constraints are explicitly solved at declared scope;
instantaneous interactions are derived;
canonical brackets and mode expansions are defined;
inverse derivatives and boundary prescriptions are defined;
residual gauge transformations and transverse link are defined;
zero modes have complete declared-scope statuses;
the JMY spacelike path is compatible with the action;
the bilocal operator is gauge-covariant;
the finite-basis projection contract is complete;
all symbolic and ablation checks pass.
```

Do not issue:

```text
REGULATOR_IDENTICAL_EXECUTABLE_MATRIX
C43_LIGHT_FRONT_HAMILTONIAN_MATRIX_VALIDATED
C43_QG_VERTEX_MATRIX_VALIDATED
C43_ONE_LOOP_MATCHING_VALIDATED
C43_MICROSCOPIC_PROTON_TMD_EXPORTED
```

---

# 20. Exact no-go branches

## A. Public source acquisition remains incomplete

```text
C43_PRIMARY_SOURCE_LOCK_INCOMPLETE
```

Next:

> **C44/SRC0 — exact primary-source acquisition and equation-locator closure**

## B. Source conventions cannot be reconciled

```text
C43_GAUGE_CONVENTION_INCOMPATIBLE
```

Next:

> **C44/G1 — choose and derive a single alternative gauge/action convention**

## C. Fermion or gauge constraints remain incomplete

```text
C43_CANONICAL_CONSTRAINT_SYSTEM_INCOMPLETE
```

Next:

> **C44/G2 — Dirac-constraint and instantaneous-interaction completion**

## D. Residual boundary or transverse link remains incomplete

```text
C43_RESIDUAL_GAUGE_BOUNDARY_INCOMPLETE
```

Next:

> **C44/B0 — boundary prescription and transverse gauge-link completion**

## E. Zero-mode policy remains incomplete

```text
C43_ZERO_MODE_CONTRACT_INCOMPLETE
```

Next:

> **C44/Z3 — perturbative finite-volume zero-mode and global gauge-constraint completion**

## F. JMY operator is incompatible with the selected action

```text
C43_JMY_ACTION_COMPATIBILITY_FAILED
```

Next:

> **C44/O6 — alternative gauge-covariant implementation of the fixed spacelike operator**

## G. All action gates close

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION
```

Next:

> **C44/HQCD — source-derived physical finite-basis Hamiltonians, SU(3) \(q\to qg\) vertex, and constrained operators**

---

# 21. Required deliverables

Create at least:

```text
docs/next_level/c43_implementation_report.md
docs/next_level/c43_api.md

docs/next_level/c43_primary_source_manifest.json
docs/next_level/c43_source_relevance_matrix.json
docs/next_level/c43_source_sufficiency_matrix.json

docs/next_level/c43_gauge_plan.json
docs/next_level/c43_gauge_convention_map.json
docs/next_level/c43_light_front_conventions.json

references/c43_light_front_qcd_gauge_action.tex
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json

docs/next_level/c43_fermion_constraint_derivation.json
docs/next_level/c43_gauge_constraint_derivation.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_free_propagator_checks.json

docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json

docs/next_level/c43_residual_gauge_derivation.json
docs/next_level/c43_transverse_link_derivation.json
docs/next_level/c43_operator_gauge_covariance_report.json

docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json

docs/next_level/c43_jmy_action_compatibility.json
docs/next_level/c43_bilocal_operator_compatibility.json

docs/next_level/c43_finite_basis_projection_contract.json
docs/next_level/c43_physical_resolution_plan.json

docs/next_level/c43_readiness_report.json
docs/next_level/c43_source_sufficiency_decision.json
docs/next_level/c43_no_go_decision_tree.json
docs/next_level/c43_missing_calculation_specification.md
docs/next_level/c43_regression_report.json
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated records must reproduce byte-for-byte.

---

# 22. Acceptance criteria

C43 is complete only when:

1. The full C42 baseline reproduces.
2. The exact BPP and BJY sources are acquired and hash locked.
3. The focused Srivastava–Brodsky light-front-QCD action source is acquired and hash locked.
4. JMY remains the fixed TMD operator source.
5. Source roles are separated rather than blended.
6. One gauge realization is explicitly selected.
7. Plus/minus conventions are machine checked.
8. The gauge-fixed Lagrangian is derived.
9. Canonical momenta and constraint equations are derived.
10. Dynamical and constrained fields are explicit.
11. The fermion constraint and inverse derivative are explicit.
12. Gauss law and the constrained gauge component are explicit.
13. Canonical and instantaneous interactions are derived from the same action.
14. Ghost non-applicability, when claimed, is proved.
15. Boundary conditions and pole prescriptions are explicit.
16. Residual gauge freedom is explicit.
17. The transverse link is derived and transforms correctly.
18. Zero modes have complete declared-scope statuses.
19. The JMY spacelike line is not set to unity by gauge choice.
20. The JMY path and transverse closure are compatible with the action.
21. The bilocal operator transforms gauge covariantly.
22. The finite-basis projection contract uses physical project resolutions rather than C40 toy labels.
23. Every retained Hamiltonian term has a scope/status.
24. Symbolic constraint-substitution checks pass.
25. Hamiltonian-density Hermiticity checks pass.
26. Propagator/gauge checks pass at their source scope.
27. Required-term ablations produce nonzero defects.
28. At least 128 focused live mutations are detected.
29. No numerical QCD matrices are fabricated.
30. No one-loop coefficient or matching kernel is created.
31. No proton TMD or ART25 bridge is created.
32. No fit, inference, process, or production route is created.
33. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
34. `MSHT20_REP/` remains untouched and outside Git.
35. The working tree is clean except for the pre-existing untracked directory.
36. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken the constraint, boundary, zero-mode, or gauge-covariance requirements to open the projection gate.

---

# 23. Final Codex response

Report:

- full starting and final commits;
- every acquired source, exact arXiv version, local path, size, and SHA-256;
- source-sufficiency matrix counts;
- selected gauge realization;
- exact plus/minus and gauge-vector convention;
- gauge-fixed action and declared completeness scope;
- dynamical and constrained fields;
- fermion constraint and inverse-derivative prescription;
- gauge constraint and Gauss-law solution;
- complete Hamiltonian-term ledger;
- canonical brackets and mode expansions;
- free-propagator and gauge residuals;
- instantaneous-interaction identities;
- boundary prescription and residual-gauge status;
- transverse-link derivation and covariance residual;
- zero-mode statuses;
- JMY spacelike-action compatibility;
- bilocal-operator covariance status;
- physical finite-basis projection plan;
- focused fault-test results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no numerical Hamiltonian/Wilson/bilocal matrices, one-loop coefficient, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe possession of the papers, a broad review formula, or an incomplete constraint system as a complete gauge-fixed finite-basis QCD action.
