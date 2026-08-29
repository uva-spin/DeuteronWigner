# C45/MODES Codex Work Package

## Title

**Source-qualified finite light-front mode projection: longitudinal box and measure, normalized two-dimensional oscillator basis, light-front spinor/polarization overlaps, and global-color/zero-mode treatment for the colored matching module**

## Authoritative baseline

Start from the clean local C44/HQCD completion commit:

```text
3786f003122b9e6b16abe697025c99d9b37de401
```

Its immediate scientific parent is:

```text
fbcd6ee0cf838db34d4bb1f45396d1435a14cb87
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor fbcd6ee0cf838db34d4bb1f45396d1435a14cb87 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION

C44_MODE_PROJECTION_INCOMPLETE
```

and preserves the C44 conclusion that C43 supplies a complete action-level interface but not the four finite-projection contracts needed for unique matrices:

```text
1. finite longitudinal cell length, measure, and boundary phase;

2. normalized two-dimensional harmonic-oscillator modes and the
   coordinate/momentum-space phase convention;

3. source-to-basis light-front spinor and gluon-polarization overlap maps;

4. global-color and zero-mode projection for a colored matching probe.
```

The fixed physical TMD architecture remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

The selected action remains:

```text
G0-LIGHT-FRONT-GAUGE

A^+ = A_- = 0
x^+ is light-front time
antisymmetric/PV inverse partial^+ on the nonzero-mode domain
explicit zero-mode projector
retained residual transverse Wilson link
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

and its integer-\(K\) arrays may not be reused as physical modes.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C45 closes the four missing projection contracts and creates a source-derived one-particle mode library.

C45 must produce actual normalized numerical mode evaluations, Gram matrices, overlap kernels, color projectors, and zero-mode projectors. It must not yet construct the physical \(q/qg\) Hamiltonian, canonical interaction matrices, instantaneous-interaction matrices, Ji–Ma–Yuan Wilson matrices, or bilocal TMD measurement matrices.

The strongest allowed status is:

```text
C45_SOURCE_DERIVED_MODE_PROJECTION_READY
```

That status means:

```text
the finite longitudinal box and measure are unambiguous;
the stored K convention and physical momentum fractions are reconciled;
the normalized 2D-HO basis and Fourier phases are fixed;
the light-front spinor and transverse-polarization overlaps are executable;
the colored matching probe has a source-supported global-color interpretation;
the ordinary and constrained zero-mode projectors are explicit;
the one-particle mode library is ready for action projection.
```

When the gate passes, the next package is:

> **C46/HQCD — source-derived physical \(q/qg\) bases, free Hamiltonians, exact SU(3) \(q\leftrightarrow qg\) vertex, instantaneous/constrained operators, residual-boundary terms, and basis-comparison maps**

C45 does not calculate a one-loop TMD or matching coefficient.

---

# 2. Scientific boundary

C45 is:

```text
source-first
mode-projection specific
one-particle and color-module specific
physical half-integer-K trajectory specific
light-front-gauge specific
deterministic
validation-only
```

C45 is not:

```text
a Hamiltonian diagonalization
a q/qg interaction calculation
a physical proton state
a complete colored physical Hilbert state
a JMY Wilson-line matrix calculation
a bilocal TMD calculation
a counterterm solution
a one-loop calculation
an ART25 comparison
a fit or inference package
```

Do not fill missing contracts with common BLFQ conventions unless their exact source, normalization, and map to C43 are recorded.

---

# 3. Nonnegotiable evidence standard

Every positive mode or projector must descend through:

```text
primary-source equation
    -> C43 convention conversion
    -> symbolic formula
    -> deterministic numerical evaluator
    -> numerical overlap/projector
    -> independent check
    -> content hash
```

For every generated object record:

```text
source locator
exact source version
C43 convention-map ID
boundary condition
box/measure convention
normalization
Fourier phase
basis ordering
resolution
shape
dtype
units
generator-code hash
array hash
independent residual
```

A conventional-looking formula without an exact normalization map remains unavailable.

---

# 4. Required source authorities

Reuse the C43 source locks:

```text
hep-ph/9705477v1
    Brodsky–Pauli–Pinsky

hep-ph/0011372v2
    Srivastava–Brodsky

hep-ph/0208038v2
    Belitsky–Ji–Yuan

hep-ph/0404183v1
    Ji–Ma–Yuan

hep-th/0008096v1
    Heinzl methodological audit

arXiv:1005.4305
    Gao transverse-link audit
```

Obtain and hash-lock official arXiv PDF/source bundles for the finite-basis method authorities needed to close the transverse and longitudinal projection, including at minimum:

```text
arXiv:0905.1411
    Hamiltonian light-front field theory in a basis function approach

arXiv:1311.2980
    Introduction to Basis Light-Front Quantization Approach to QCD
    Bound State Problems
```

Audit additional primary BLFQ sources only when required to obtain an exact equation, normalization, center-of-mass prescription, or overlap formula.

Store new source material under:

```text
data/raw/c45_sources/
```

or, when repository policy keeps binaries outside Git, commit exact version, path, size, SHA-256, source-archive hash, and deterministic acquisition command.

Classify each source as:

```text
LONGITUDINAL_COMPACTIFICATION_AUTHORITY
TWO_DIMENSIONAL_HO_AUTHORITY
LIGHT_FRONT_SPINOR_AUTHORITY
TRANSVERSE_POLARIZATION_AUTHORITY
GLOBAL_COLOR_CONSTRAINT_AUTHORITY
ZERO_MODE_PROJECTION_AUTHORITY
METHOD_ONLY
NOT_PROJECT_CONVENTION_IDENTICAL
```

Create:

```text
docs/next_level/c45_primary_source_manifest.json
docs/next_level/c45_source_relevance_matrix.json
```

---

# 5. Four-contract gate

Create an exact four-row contract table:

```text
LONGITUDINAL_CELL_AND_MEASURE
TRANSVERSE_2D_HO_AND_PHASE
SPINOR_POLARIZATION_OVERLAP
GLOBAL_COLOR_ZERO_MODE_PROJECTION
```

Every row must contain:

```text
source authority
equation locators
source convention
C43/project convention
conversion
symbolic implementation
numerical validation
holdout
status
```

Allowed statuses:

```text
SOURCE_COMPLETE_EXECUTABLE
SOURCE_COMPLETE_REQUIRES_LIMIT
CONFLICT_REQUIRES_DECISION
ABSENT_BLOCKING
```

The positive C45 gate requires all four rows to be:

```text
SOURCE_COMPLETE_EXECUTABLE
```

Create:

```text
docs/next_level/c45_projection_contract_matrix.json
```

---

# 6. Longitudinal compactification contract

Derive the finite longitudinal domain from the selected source and C43 conventions.

The contract must explicitly define:

```text
coordinate interval in x^-
its total length
integration measure
Fourier phase
field boundary phase
fermion boundary condition
gluon boundary condition
allowed p^+ eigenvalues
one-particle normalization
Kronecker-delta convention
total P^+ convention
stored resolution K
partonic fraction x
continuum/large-box limit
```

Do not hard-code any of the common alternatives

```text
p^+ = pi k/L
p^+ = 2 pi k/L
x = k/K
x = k/(2K)
```

without deriving the result from the exact project Fourier and box conventions.

## 6.1 Resolve the existing \(K\)/\(x_{\min}\) ambiguity

The inherited C32 records contain both:

```text
K = 9/2, 11/2, 13/2
```

and:

```text
x_min = 1/18.
```

C45 must determine the exact relation among:

```text
the mode label k
the stored K
the total physical P^+
the box length
the smallest retained fermion mode
the physical momentum fraction x
```

For every resolution, verify the declared \(x_{\min}\) or issue a typed correction/supersession. Do not silently choose the relation that reproduces the stored number.

## 6.2 Symbolic versus numerical box length

Determine whether the absolute cell length \(L\):

```text
cancels from all dimensionless basis matrix elements;
remains as an explicit regulator parameter;
or must be fixed numerically by another project scale.
```

Do not select a numerical \(L\) for convenience.

## 6.3 Zero/nonzero longitudinal subspaces

Construct explicit projectors:

\[
P_0,\qquad Q_0=1-P_0,
\]

consistent with the C43 inverse-\(\partial^+\) definition.

Verify:

```text
boundary phase
orthonormality
completeness on the retained nonzero-mode subspace
inverse-derivative action
PV/antisymmetric Hermiticity property
large-box behavior
```

Create:

```text
docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_validation.json
```

---

# 7. Physical longitudinal mode tables

Using the resolved convention, generate the actual allowed quark and gluon longitudinal modes for the physical trajectory:

```text
K = 9/2
K = 11/2
K = 13/2
```

or the corrected C43 trajectory when the source audit requires a typed supersession.

Retain:

```text
mode quantum number
boundary phase
p^+
fraction x
zero-mode flag
field species
normalization
resolution
```

Required checks:

```text
positive support
exact rational momentum conservation
fermion half-integer pattern
gluon nonzero-integer pattern
total-K identities
x_min identity
no accidental gluon zero mode
```

Create:

```text
docs/next_level/c45_longitudinal_mode_manifest.json
```

---

# 8. Normalized two-dimensional oscillator basis

Transcribe the exact source-normalized two-dimensional harmonic-oscillator basis.

Define separately:

```text
momentum-space mode
coordinate-space mode
radial index n
angular/OAM index m
oscillator scale b_HO
normalization measure
Laguerre-polynomial convention
azimuthal phase
Fourier-transform phase
coordinate-space oscillator length
```

Do not assume that two sources use the same overall phase.

The exact relation between momentum- and coordinate-space modes must be derived under the project Fourier convention.

## 8.1 Truncation

Derive the exact \(N_{\max}\) truncation rule and its many-body interpretation.

Do not hard-code:

```text
2n + |m| + 1 <= Nmax
```

unless that is the exact selected-source/project rule.

## 8.2 Numerical evaluator

Implement stable evaluators and quadrature for:

```text
momentum-space mode values
coordinate-space mode values
radial overlaps
angular/OAM overlaps
Fourier transforms
basis changes between different b_HO and Nmax
```

Required checks:

```text
orthonormality
radial normalization
angular momentum eigenvalue
coordinate/momentum Fourier round trip
phase identity
oscillator expectation values
Gauss-Laguerre or independent quadrature agreement
```

Create:

```text
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_ho_validation.json
```

---

# 9. Transverse-mode tables and overlap kernels

Generate source-derived mode tables at the physical trajectory:

```text
(Nmax,b_HO) = (8,0.40 GeV)
(Nmax,b_HO) = (10,0.45 GeV)
(Nmax,b_HO) = (12,0.50 GeV)
```

only after verifying these values from the C43/C32 contract.

Construct numerical overlap matrices between adjacent resolutions:

\[
O^{\perp}_{r'r}
=
\langle n'm';b_{r'}|nm;b_r\rangle.
\]

These are one-particle mode overlaps, not the final q/qg comparison maps.

Report:

```text
shape
rank
singular values
normalization remainder
truncation remainder
phase convention
```

Create:

```text
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_transverse_overlap_report.json
```

---

# 10. Light-front spinor contract

Use the C43 gamma-matrix, metric, good-component, and field-normalization conventions.

Select and source one explicit light-front spinor phase convention.

Define:

```text
u_lambda(p)
v_lambda(p)
good-component projector
bad-component reconstruction used by C43
spinor normalization
completeness
charge conjugation
light-front helicity phase
```

Do not combine spinors from one convention with gamma matrices or state normalization from another.

Implement executable spinor arrays at frozen nonzero momenta and masses.

Required checks:

```text
Dirac equation
u-bar u normalization
v-bar v normalization
completeness
good-component projector
gamma-plus current normalization
charge conjugation
helicity orthogonality
phase continuity under transverse rotations
```

Create:

```text
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_light_front_spinor_validation.json
```

---

# 11. Transverse-gluon polarization contract

Derive the physical transverse polarization vectors from the same C43 gauge convention.

Define:

```text
epsilon_lambda^mu(k)
lambda = +/-1
A^+ = 0 condition
k dot epsilon = 0
normalization
complex conjugation
helicity phase
transverse completeness
constrained A^- component
zero-mode domain
```

Do not retain only a two-component Euclidean vector when the source-to-operator map needs the complete four-vector and constrained component.

Implement executable polarization arrays.

Required checks:

```text
gauge condition
transversality
normalization
helicity orthogonality
completeness at selected scope
conjugation
rotation phase
compatibility with v dot A for a spacelike JMY direction
```

Create:

```text
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_gluon_polarization_validation.json
```

---

# 12. Source-to-basis spinor/polarization overlap map

Construct the reusable local overlap kernels required by C46.

At minimum define executable functions for:

```text
quark mode overlap
gluon mode overlap
free kinetic bilinear
canonical local spinor-polarization numerator
good/bad-component insertion
constrained A^- insertion
transverse OAM selection
```

The canonical local numerator may be represented schematically as

\[
\bar u_{\lambda'}(p')\gamma^\mu
\epsilon_\mu^*(k,h)u_\lambda(p),
\]

but the committed implementation must follow the exact C43 Hamiltonian expression and normalization.

Required checks:

```text
direct four-component evaluation
good-component reduced evaluation
helicity-selection identities
rotation covariance
massless and finite-mass controlled limits
conjugation
source-to-basis phase consistency
```

C45 does not multiply this kernel by SU(3), longitudinal conservation, or assemble a \(q\to qg\) Hamiltonian matrix.

Create:

```text
docs/next_level/c45_spinor_polarization_overlap.json
docs/next_level/c45_overlap_kernel_validation.json
```

---

# 13. Colored matching-module decision

A perturbative colored matching probe is not a gauge-invariant physical finite-volume state. C45 must define its mathematical status explicitly.

Compile mutually exclusive plans:

## 13.1 `OPEN_COLOR_AMPUTATED_MODULE`

The q and qg probes are open-color external modules used to calculate amputated, gauge-fixed partonic matrix elements. The global Gauss-law zero mode is not misrepresented as a physical-state constraint on those open external indices.

Requirements:

```text
source authority
global generator action
Ward/BRST or gauge-fixed covariance scope
separation from the physical Hilbert space
external-color normalization
relation to the finite-volume zero-mode constraint
```

## 13.2 `STATIC_ANTI_FUNDAMENTAL_CLOSURE`

Pair the dynamical total-color triplet with a nondynamical anti-fundamental reference source to form a global singlet, then prove factorization of the reference source from the matching operator.

## 13.3 `GAUGE_DRESSED_COLOR_PROBE`

Use a source-defined dressed colored probe and prove its relation to the selected partonic matching calculation.

## 13.4 `COLORED_PROBE_UNAVAILABLE`

No source-supported treatment closes.

Select exactly one plan. Do not imply that a colored matching probe is a physical asymptotic state.

Create:

```text
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
```

---

# 14. Exact \(3\otimes8\to3\) color projector

After selecting the colored-module plan, construct the exact color-only projector needed by C46.

Use:

\[
3\otimes8=3\oplus\bar6\oplus15.
\]

Construct total generators:

\[
T_{\rm tot}^a
=
T_q^a\otimes I_8
+
I_3\otimes F_g^a.
\]

Derive the triplet projector from the exact Casimir spectrum or an equivalent source-qualified construction.

Required checks:

```text
Hermiticity
idempotence
rank 3
C2 = 4/3 on the image
orthogonality to 6bar and 15
total-generator covariance
canonical-emission color tensor lies in the image
basis-rotation invariance
```

This is a color projector only. C45 does not construct the full qg basis.

Create:

```text
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_qg_triplet_validation.json
```

---

# 15. Zero-mode projection contract for the colored module

Apply the C43 zero-mode policy to the selected colored-module plan.

Retain separate projectors/statuses for:

```text
ordinary nonzero longitudinal modes
gluon k^+=0 mode
constrained fermion zero mode
global color/Gauss-law zero mode
residual transverse gauge zero mode
Wilson-endpoint zero mode
```

For each define one of:

```text
PROJECTED_OUT_WITH_SOURCE_PROOF
RETAINED_AS_CONSTRAINED_VARIABLE
RETAINED_AS_EXTERNAL_MODULE_LABEL
CANCELS_WITH_DECLARED_BOUNDARY_TERM
UNRESOLVED_BLOCKING
```

Required identities:

```text
P0^2 = P0
Q0^2 = Q0
P0 Q0 = 0
inverse partial-plus acts only on Q0
global generator treatment matches the selected colored-module plan
boundary and residual-gauge zero modes are not silently discarded
```

Create:

```text
docs/next_level/c45_zero_mode_projection_contract.json
docs/next_level/c45_zero_mode_projection_validation.json
```

---

# 16. One-particle mode library

Create a deterministic runtime library containing:

```text
longitudinal quark mode tables
longitudinal gluon mode tables
momentum-space 2D-HO evaluations
coordinate-space 2D-HO evaluations
transverse overlap matrices
light-front spinor arrays
transverse-gluon polarization arrays
spinor/polarization overlap-kernel test arrays
qg triplet color projector
zero-mode projectors
```

Heavy arrays may live under:

```text
data/runtime/c45_modes/
```

Commit an inventory with:

```text
runtime path
shape
dtype
units
basis-order hash
array hash
generator command
```

Create:

```text
docs/next_level/c45_numerical_object_inventory.json
```

The library must contain no Hamiltonian or interaction matrix.

---

# 17. Projection-ready interface for C46

Define the exact interface by which C46 will combine:

```text
longitudinal mode factors
transverse oscillator overlaps
spinor/polarization kernels
SU(3) color projector
zero-mode projectors
```

into many-body basis states and action matrix elements.

The interface must specify:

```text
index ordering
block quantum numbers
normalization factors
units
coupling-power factoring
selection rules
error/remainder propagation
```

Create:

```text
docs/next_level/c45_c46_projection_interface.json
```

---

# 18. End-to-end source-to-mode test

Implement a test that begins with source and C43 convention records and regenerates the C45 library.

It must:

```text
derive the longitudinal momentum spectrum
verify the K/x relation
generate normalized HO modes
Fourier transform them
generate spinors
generate polarizations
evaluate overlap kernels
construct the qg triplet projector
construct zero-mode projectors
reproduce all numerical hashes
```

It must fail when:

```text
the longitudinal interval changes
the boundary phase changes
the Fourier convention changes
x is changed from the derived K relation
the HO normalization changes
the HO Fourier phase changes
a spinor phase is changed inconsistently
a polarization loses transversality
the qg projector is replaced by the full product space
the global-color plan is omitted
a zero-mode projector is removed
a C40 mode array is substituted
```

---

# 19. Focused mutation tests

Create at least 160 focused live mutations.

Include:

```text
change the longitudinal measure
change the box length relation
change the fermion boundary phase
permit a gluon zero mode
change the K-to-x relation
change the HO Laguerre convention
change the azimuthal phase
change the Fourier phase
change b_HO units
change a gamma matrix
change a spinor normalization
change a helicity phase
change a polarization component
change the constrained A^- component
change a Gell-Mann generator
change an adjoint generator
replace the triplet projector
change the global-color plan
drop the zero-mode projector
replace overlap integration by center sampling
```

Every mutation must fail a concrete normalization, convention, projector, or source-identity test.

Do not inflate the count with identifier-only dispatch.

---

# 20. Readiness gate

Issue:

```text
C45_SOURCE_DERIVED_MODE_PROJECTION_READY
```

only when:

```text
all four projection-contract rows are SOURCE_COMPLETE_EXECUTABLE;
the longitudinal cell and measure are fixed;
the K/x convention is reconciled;
the physical longitudinal mode tables are generated;
the normalized 2D-HO basis and phases are fixed;
transverse overlaps are executable;
light-front spinors are source consistent;
gluon polarizations are source consistent;
the source-to-basis overlap kernel closes;
one colored matching-module plan is selected;
the qg color-triplet projector closes;
the zero-mode projection contract closes;
the deterministic one-particle library reproduces;
the C46 projection interface is complete;
the end-to-end source-to-mode test passes.
```

Do not issue:

```text
C45_PHYSICAL_QG_BASIS_VALIDATED
C45_HQCD_MATRIX_VALIDATED
C45_CANONICAL_QG_VERTEX_VALIDATED
C45_JMY_WILSON_MATRIX_VALIDATED
C45_ONE_LOOP_MATCHING_VALIDATED
```

---

# 21. Exact no-go branches

## A. Longitudinal convention remains incomplete

```text
C45_LONGITUDINAL_PROJECTION_INCOMPLETE
```

Next:

> **C46/LONG0 — finite longitudinal cell, \(K\), boundary phase, and inverse-\(\partial^+\) projection closure**

## B. Transverse oscillator contract remains incomplete

```text
C45_TRANSVERSE_HO_PROJECTION_INCOMPLETE
```

Next:

> **C46/HO2D — normalized 2D-HO functions, Fourier phases, truncation, and overlap completion**

## C. Spinor/polarization map remains incomplete

```text
C45_SPINOR_POLARIZATION_MAP_INCOMPLETE
```

Next:

> **C46/SPIN1 — source-to-basis light-front spinor and transverse-polarization overlap completion**

## D. Colored probe or zero-mode treatment remains incomplete

```text
C45_COLORED_ZERO_MODE_PROJECTION_INCOMPLETE
```

Next:

> **C46/COLORZ — open-color matching module, global Gauss law, triplet projector, and zero-mode completion**

## E. All four contracts close

```text
C45_SOURCE_DERIVED_MODE_PROJECTION_READY
```

Next:

> **C46/HQCD — source-derived physical \(q/qg\) bases, Hamiltonians, canonical SU(3) vertex, and constrained operators**

---

# 22. Required deliverables

Create at least:

```text
docs/next_level/c45_implementation_report.md
docs/next_level/c45_api.md

docs/next_level/c45_primary_source_manifest.json
docs/next_level/c45_source_relevance_matrix.json
docs/next_level/c45_projection_contract_matrix.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_validation.json
docs/next_level/c45_longitudinal_mode_manifest.json

docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_ho_validation.json
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_transverse_overlap_report.json

docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_light_front_spinor_validation.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_gluon_polarization_validation.json
docs/next_level/c45_spinor_polarization_overlap.json
docs/next_level/c45_overlap_kernel_validation.json

docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_qg_triplet_validation.json

docs/next_level/c45_zero_mode_projection_contract.json
docs/next_level/c45_zero_mode_projection_validation.json

docs/next_level/c45_numerical_object_inventory.json
docs/next_level/c45_c46_projection_interface.json

docs/next_level/c45_readiness_report.json
docs/next_level/c45_source_sufficiency_decision.json
docs/next_level/c45_no_go_decision_tree.json
docs/next_level/c45_missing_calculation_specification.md
docs/next_level/c45_regression_report.json
```

Add source files under:

```text
src/deuteron_wigner/bridge/modes/
```

or the repository-equivalent package.

Add focused tests for:

```text
longitudinal modes
2D-HO modes
spinors and polarizations
color and zero modes
end-to-end projection readiness
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 23. Acceptance criteria

C45 is complete only when:

1. The full C44 baseline reproduces.
2. The C44 no-go remains explicit.
3. C43 action/gauge conventions remain unchanged.
4. C40 remains method-oracle only.
5. Exact finite-basis method sources are hash locked.
6. The longitudinal interval and measure are source qualified.
7. Fermion and gluon boundary phases are explicit.
8. Allowed \(p^+\) values are derived from those phases.
9. The relation among \(L,p^+,K,P^+,x\) is explicit.
10. The inherited \(K/x_{\min}\) records are reconciled or superseded visibly.
11. No arbitrary numerical box length is chosen.
12. \(P_0\) and \(Q_0\) are executable.
13. The PV inverse derivative acts on the correct subspace.
14. Physical quark and gluon longitudinal mode tables exist.
15. The normalized 2D-HO functions are source exact.
16. Momentum/coordinate Fourier phases are fixed.
17. The \(N_{\max}\) rule is source exact.
18. HO orthogonality and Fourier round trips close.
19. Physical transverse overlap matrices exist.
20. Light-front spinors use one consistent convention.
21. Spinor normalization, completeness, and current identities close.
22. Gluon polarizations satisfy gauge, transversality, and completeness identities.
23. The constrained polarization component is explicit.
24. Source-to-basis overlap kernels close by independent routes.
25. One colored matching-module plan is selected.
26. The probe is not mislabeled as a physical colored asymptotic state.
27. The exact \(3\otimes8\to3\) projector closes.
28. Global color and zero-mode treatments are compatible.
29. Residual-boundary and Wilson-endpoint zero modes are not silently discarded.
30. The deterministic one-particle mode library reproduces.
31. The C46 interface is complete.
32. At least 160 live mutations are detected.
33. No physical q/qg Hamiltonian or interaction matrix is created.
34. No JMY Wilson or bilocal matrix is created.
35. No one-loop coefficient or matching kernel is created.
36. No proton TMD or ART25 bridge is created.
37. No fit, inference, process, or production route is created.
38. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
39. `MSHT20_REP/` remains untouched and outside Git.
40. The working tree is clean except for the pre-existing untracked directory.
41. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not choose a familiar basis convention, colored-state interpretation, or zero-mode prescription merely to open the gate.

---

# 24. Final Codex response

Report:

- full starting and final commits;
- every new primary source, exact version, path, size, and SHA-256;
- four-contract matrix statuses;
- longitudinal interval, measure, field boundary phases, and momentum spectrum;
- exact relation among \(L,p^+,K,P^+\), and \(x\);
- reconciliation of the inherited \(x_{\min}\);
- physical longitudinal mode counts by resolution and species;
- 2D-HO formulas, normalization, truncation, and Fourier phase;
- transverse mode counts and overlap-matrix residuals;
- spinor convention and validation residuals;
- polarization convention and validation residuals;
- overlap-kernel residuals;
- selected colored-module plan;
- global Gauss-law treatment;
- qg triplet-projector rank, Casimir, covariance, and idempotence residuals;
- zero-mode projector statuses and residuals;
- runtime library hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no physical Hamiltonian/vertex/Wilson/bilocal matrices, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an interface-only contract, an unreconciled \(K\) convention, a generic HO formula, or an unresolved colored-state prescription as a physical finite-basis mode projection.
