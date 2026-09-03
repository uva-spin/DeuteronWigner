# C40/M0B Codex Work Package

## Title

**Executable finite-basis partonic operator substrate: concrete q/qg bases, Hamiltonians, spacelike Wilson matrices, constrained sectors, counterterm linear systems, distributional measurements, and refinement maps**

## Authoritative baseline

Start from the clean local C39 correction commit whose abbreviated hash is:

```text
79804d3
```

Resolve and record the full hash before editing:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 16f7eb1 HEAD
```

The baseline is authoritative only when it contains the C39 descendant supersession:

```text
C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY
    ->
C38_PARTONIC_STRUCTURAL_SCAFFOLD_ONLY
```

and the outcome:

```text
C39_FINITE_BASIS_ONE_LOOP_INCOMPLETE
```

Required historical ancestry includes the C36 spacelike-regulator selection and the C35 modified-delta no-go.

Do not use `origin/main` when the local branch is ahead of the remote.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Purpose

C40 is not another architecture or metadata package.

C40 must create the actual numerical objects that C38 claimed but did not contain.

The code audit established that the current `m0a` layer has only metadata/scalar records. It lacks:

```text
state vectors
q and qg basis arrays
Hamiltonian matrices
matrix-free Hamiltonian actions
q -> qg vertex matrices
generated adjoints
instantaneous operators
constrained and zero-mode operators
spacelike Wilson insertion matrices
endpoint/transverse-boundary matrices
counterterm equation matrices
distributional measurement matrices
refinement/prolongation maps
```

C40 must materialize those objects and apply them to nonzero vectors.

The package stops before the physical one-loop correlator and matching difference.

The strongest possible status is:

```text
C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY
```

The next calculation, only after that status is earned, is:

```text
C41/R2B
    finite-basis one-loop spacelike quark correlator,
    universal soft/overlap subtraction,
    partonic renormalization,
    and state-independent matching difference
```

---

# 2. Fixed scientific decisions

Do not reopen these choices:

```text
rapidity/operator scheme:
    O4-SPACELIKE-COLLINS-JMY

partonic ownership:
    nonhadronic color-fundamental matching probe

sectors:
    |q> and |qg>

soft ownership:
    universal B=0 soft factor outside the hadron TTN

historical microscopic parent:
    C11 remains a regulated finite-basis model density

historical correction:
    C38 is structural scaffold only
```

C40 must not:

```text
calculate or fabricate the one-loop matching kernel
apply anything to the proton
rerun the ART25 bridge
fit counterterms to hadronic or ART25 quantities
create a likelihood, posterior, optimizer, reweighting, emulator, or process route
```

---

# 3. Evidence standard

The following statements are mandatory:

```text
a manifest is not a matrix
an interface is not an operator
a status string is not a calculation
a basis descriptor is not a basis array
a pilot record is not an applied numerical identity
```

A capability is executable only when the repository contains either:

1. committed numerical arrays; or
2. a deterministic generator that reconstructs those arrays byte-for-byte.

Every executable object must have:

```text
shape
dtype
basis ordering
units/convention
nonzero norm where physically required
content hash
deterministic reconstruction command
application to a nonzero vector
independent check
```

A readiness gate may not inspect status labels alone.

---

# 4. Minimal deliverables

Keep the package narrow. Do not create dozens of empty manifests or thousands of identifier-only injections.

Required code:

```text
src/deuteron_wigner/bridge/m0b/
    basis.py
    hamiltonian.py
    vertices.py
    wilson.py
    constrained.py
    counterterms.py
    distributions.py
    refinement.py
    readiness.py
```

Equivalent organization is acceptable when repository conventions require it.

Required documentation:

```text
docs/next_level/c40_implementation_report.md
docs/next_level/c40_api.md
docs/next_level/c40_numerical_object_inventory.json
docs/next_level/c40_readiness_report.json
docs/next_level/c40_regression_report.json
docs/next_level/c40_missing_calculation_specification.md
```

Required tests:

```text
tests/test_c40_m0b_basis.py
tests/test_c40_m0b_operators.py
tests/test_c40_m0b_distributions.py
tests/test_c40_m0b_readiness.py
```

Heavy arrays may be generated under a content-addressed runtime directory, but their schemas and hashes must be committed.

---

# 5. Concrete finite-basis probe spaces

Construct at least three explicit finite resolutions.

Use the fixed C36/C38 light-front and spacelike-path conventions. The exact mode choices must be source- and code-derived, not arbitrary labels.

For every resolution construct:

```text
OneQuarkBasis
QuarkGluonBasis
```

with explicit basis tables and coefficient spaces.

## 5.1 One-quark basis

Every basis state must retain:

```text
flavor
fundamental color
helicity
longitudinal mode
transverse radial mode
transverse angular/OAM mode
external probe label
IR-mass label
resolution
```

Generate actual normalized vectors:

\[
|q_i\rangle \in \mathbb C^{N_q}.
\]

Required numerical objects:

```text
basis-state table
Gram matrix G_q
identity/coordinate vectors
free one-quark invariant-mass array
```

Required checks:

```text
N_q > 0
G_q Hermitian
G_q positive definite on the retained basis
normalization residual
orthogonality residual
nontrivial comparison across resolutions
```

## 5.2 qg basis

Every qg basis state must retain:

```text
quark mode
gluon mode
quark helicity
gluon polarization/helicity
fundamental quark color
adjoint gluon color
longitudinal momentum partition
transverse/OAM labels
total-momentum identity
zero-mode status
resolution
```

Generate actual normalized vectors:

\[
|qg_\alpha\rangle \in \mathbb C^{N_{qg}}.
\]

Required checks:

```text
N_qg > 0
G_qg Hermitian
normalization and orthogonality
positive longitudinal support
total momentum conservation
zero-mode policy
```

Do not project the matching probe onto a baryonic color singlet.

---

# 6. Executable free Hamiltonians

Construct actual sparse matrices or equivalent linear operators:

\[
H_q^{(0)} \in \mathbb C^{N_q\times N_q},
\qquad
H_{qg}^{(0)} \in \mathbb C^{N_{qg}\times N_{qg}}.
\]

Required properties:

```text
Hermitian
finite
nontrivial spectrum
basis ordering explicit
mass-IR dependence explicit
resolution dependence explicit
```

Provide both:

```text
assembled sparse-matrix action
matrix-free action
```

Test them on deterministic random complex vectors:

\[
\|H_{\rm assembled}v-H_{\rm matrix-free}v\| < \epsilon.
\]

A list of diagonal energies without an operator application is insufficient.

---

# 7. Canonical q <-> qg vertex

Construct the actual sparse emission matrix:

\[
V_{qg\leftarrow q}
\in
\mathbb C^{N_{qg}\times N_q},
\]

and its generated adjoint:

\[
V_{q\leftarrow qg}
=
V_{qg\leftarrow q}^{\dagger}.
\]

The matrix elements must derive from:

```text
the selected light-front interaction
fundamental color generators
helicity structure
longitudinal conservation
transverse overlap
normalization
fermion sign
endpoint regulator where applicable
```

Required evidence:

```text
at least one nonzero matrix element
matrix norm
adjoint residual
color-factor oracle
momentum-conservation rejection
helicity-selection rejection
assembled versus direct element calculation
application to a nonzero |q> vector producing a nonzero qg vector
```

Do not reuse a C9 matrix without proving the partonic color, normalization, basis, and regulator identities.

---

# 8. Instantaneous, constrained, boundary, and zero-mode operators

Construct actual matrices or matrix-free actions for every term required by the selected light-front formulation:

```text
V_inst_fermion
V_inst_gluon
V_constrained
V_boundary
V_zero_mode
```

For each term, one of the following is required:

```text
EXECUTABLE_NONZERO_OPERATOR
EXECUTABLE_ZERO_OPERATOR_WITH_EXACT_DERIVATION
NOT_APPLICABLE_WITH_OPERATOR-LEVEL_PROOF
UNRESOLVED_BLOCKING
```

A metadata field containing one of these labels is not enough. The corresponding numerical object or proof test must exist.

Required ablation test:

```text
construct the declared Ward/commuting-generator pilot
apply the full operator to a nonzero vector
remove each required term one at a time
verify a signed nonzero defect
```

If any required term remains `UNRESOLVED_BLOCKING`, the final readiness gate must remain false.

---

# 9. Spacelike Wilson insertion matrix

Materialize the first-order selected C36 spacelike Wilson operator:

\[
W_v^{(1)}
=
ig\int ds\,v\cdot A^a(x+sv)t^a.
\]

Construct the actual matrix:

\[
W_{qg\leftarrow q}^{(1)}
\in
\mathbb C^{N_{qg}\times N_q}.
\]

The matrix element must use the finite-basis mode functions and path integration. It may not be a stored continuum denominator.

Retain separate numerical components for:

```text
longitudinal spacelike segment
conjugate/absorption segment
transverse closure
endpoint/junction contribution
```

Required evidence:

```text
at least one nonzero Wilson matrix element
path-orientation reversal
Hermitian-conjugate relation
fundamental color action
finite-rapidity dependence
transverse-phase dependence
endpoint ablation defect
independent direct quadrature or analytic mode-overlap oracle
application to a nonzero q vector
```

---

# 10. Partonic operator and counterterm bases

Construct numerical matrices for the counterterm operator basis:

```text
O_mass
O_field
O_vertex
O_inst_fermion
O_inst_gluon
O_bilocal
O_Wilson
O_endpoint
O_transverse
O_basis
```

C40 does not solve the physical one-loop counterterm values because the complete bare one-loop residuals belong to C41.

It must, however, construct the executable linear-system assembler:

\[
A_{\rm CT}\,c_{\rm CT}=r_{\rm bare},
\]

where:

```text
A_CT is numerically generated from partonic renormalization conditions
c_CT is the counterterm coefficient vector
r_bare is supplied later by the C41 bare calculation
```

Required evidence now:

```text
A_CT has actual nonzero entries
shape and rank are reported
nullspace is reported
condition number is reported
left/right test vectors are explicit
a nontrivial analytic or synthetic benchmark RHS is solved
the benchmark solution is independently checked
```

The synthetic benchmark validates the equation machinery only. It must not be reported as the physical counterterm solution.

---

# 11. Executable distributional measurement operators

Construct numerical linear functionals or matrices acting on finite-\(K\) coefficient vectors.

Required operators include finite-basis representations of:

```text
regular x-bin/test-function action
delta(1-x) endpoint action
[1/(1-x)]_+ action
[ln(1-x)/(1-x)]_+ action
Mellin moments
convolution with a frozen test kernel
```

Represent the action as, for example:

\[
M_r^{(K)}\,f_K
=
\langle F_K,\varphi_r\rangle.
\]

Required evidence:

```text
actual matrices/weight arrays
rank and nullspace
support 0 < x <= 1
constant-test-function plus-distribution identity
quark-number moment
endpoint identity
independent direct-sum check
application to nonzero coefficient vectors
```

Do not use the twelve ART25 bridge points as an \(x\) grid.

Do not use an arbitrary spline.

---

# 12. Explicit refinement and comparison maps

For adjacent resolutions construct sparse maps:

\[
P_{r\to r+1},
\qquad
R_{r+1\to r}.
\]

At minimum provide maps for:

```text
one-quark basis
qg basis
distributional coefficient/test-function space
```

Required checks:

```text
shape compatibility
normalization preservation
longitudinal-support consistency
moment preservation
R P identity on the retained coarse subspace, within tolerance
operator-consistency pilot:
    H_{r+1} P approximately P H_r
Wilson-consistency pilot:
    W_{r+1} P approximately P_qg W_r
```

If exact refinement is impossible, report the nonzero remainder and keep readiness false when the missing relation is required for C41.

A list of resolution labels is not a refinement map.

---

# 13. Runtime object bundle

For every resolution produce a deterministic runtime bundle containing at least:

```text
q_basis_table
qg_basis_table
G_q
G_qg
H_q
H_qg
V_qg_q
V_q_qg
instantaneous/constrained/boundary/zero-mode operators
W_qg_q
counterterm operator matrices
A_CT
distributional measurement matrices
refinement maps
```

Use `.npz`, sparse matrix serialization, or another deterministic numerical format.

The committed inventory must record:

```text
relative runtime path
content hash
shape
dtype
nnz
basis-order hash
generator command
```

A bundle containing only JSON metadata fails.

---

# 14. Numerical readiness test

Implement one end-to-end readiness test that performs actual linear algebra.

It must be equivalent in substance to:

```python
q = build_one_quark_basis(resolution)
qg = build_qg_basis(resolution)

psi_q = deterministic_nonzero_q_vector(q)
psi_qg_from_vertex = V_qg_q @ psi_q
psi_qg_from_wilson = W_qg_q @ psi_q

assert norm(psi_qg_from_vertex) > 0
assert norm(psi_qg_from_wilson) > 0

assert norm(V_q_qg - V_qg_q.conj().T) < tol
assert norm(Hq @ psi_q - Hq_linear_operator(psi_q)) < tol

ward_full = apply_full_ward_operator(psi_q)
ward_parts = apply_propagating_instantaneous_boundary_operator(psi_q)
assert abs(ward_full - ward_parts) < tol

for required_term in required_ward_terms:
    assert abs(ward_defect_when_removed(required_term, psi_q)) > defect_min

measurement = M_test @ deterministic_nonzero_distribution_vector
assert isfinite(measurement)

coarse_to_fine = P @ psi_q_coarse
assert norm(R @ coarse_to_fine - psi_q_coarse) < refinement_tol
```

The readiness test must inspect object types, shapes, nonzero norms, and applications.

It must fail if any object is replaced by:

```text
None
a status string
a scalar descriptor
an empty array
a zero matrix where a nonzero operator is required
metadata without numerical backing
```

---

# 15. Focused negative tests

Do not create thousands of identifier-only injections.

Create a focused set of at least 96 numerical or semantic faults that mutate actual objects, including:

```text
drop a q basis vector
duplicate a qg basis state
break Gram normalization
remove a nonzero vertex block
break the adjoint
change a color generator
violate momentum conservation
remove an instantaneous term
remove the boundary term
replace Wilson matrix with its metadata record
zero the Wilson matrix
reverse the spacelike path incorrectly
drop an endpoint contribution
make A_CT rank deficient
hide a counterterm null direction
drop the endpoint measurement
replace plus distribution by an endpoint cutoff
corrupt a refinement map
replace a sparse matrix by a scalar
return a zero vector from matrix-free action
change a runtime-array hash
```

Every fault must execute a concrete failing numerical or readiness assertion.

---

# 16. Readiness gate

Issue:

```text
C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY
```

only when all of the following are true at every declared readiness resolution:

```text
q basis arrays exist
qg basis arrays exist
Gram matrices close
free Hamiltonian matrices exist
matrix-free actions agree
canonical q->qg vertex is nonzero
generated adjoint closes
all required instantaneous/constrained/boundary/zero-mode terms have executable statuses
spacelike Wilson matrix is nonzero
endpoint/transverse components are explicit
counterterm operator basis and A_CT exist
distributional measurement matrices exist
refinement maps exist
runtime bundles reproduce byte-for-byte
the end-to-end numerical readiness test passes
```

If any required item is missing, issue one exact no-go status:

```text
C40_PROBE_BASIS_INCOMPLETE
C40_PARTONIC_HAMILTONIAN_INCOMPLETE
C40_QG_VERTEX_INCOMPLETE
C40_CONSTRAINED_SECTOR_INCOMPLETE
C40_SPACELIKE_WILSON_MATRIX_INCOMPLETE
C40_COUNTERTERM_LINEAR_SYSTEM_INCOMPLETE
C40_DISTRIBUTIONAL_MEASUREMENT_INCOMPLETE
C40_REFINEMENT_MAP_INCOMPLETE
```

and specify the exact next implementation branch.

Do not issue a matching, TMD, bridge, or production status.

---

# 17. Acceptance criteria

C40 is complete only when:

1. The full C39 baseline is resolved and reproduced.
2. The C38 readiness supersession remains intact.
3. The C36 spacelike regulator remains fixed.
4. The probe root is nonhadronic and color fundamental.
5. At least three actual q basis arrays exist.
6. At least three actual qg basis arrays exist.
7. Gram matrices and basis ordering are explicit.
8. Free Hamiltonian matrices exist and are applied.
9. Matrix-free actions independently agree.
10. A nonzero canonical q->qg vertex matrix exists.
11. Its generated adjoint closes.
12. Required constrained-sector operators are executable or exactly proved absent.
13. The Ward pilot is evaluated on nonzero vectors.
14. Removing every required Ward term gives a nonzero defect.
15. A nonzero spacelike Wilson matrix exists.
16. Longitudinal, endpoint, and transverse pieces are separately auditable.
17. The Wilson matrix is checked independently.
18. Counterterm operator matrices exist.
19. A numerical counterterm coefficient matrix exists.
20. Its rank, nullspace, and condition number are reported.
21. Distributional measurement matrices/functionals exist.
22. Delta, plus, Mellin, and convolution actions are tested.
23. Refinement maps exist as numerical matrices.
24. Refinement and operator-consistency tests are executed.
25. Runtime numerical bundles reproduce byte-for-byte.
26. Readiness cannot be opened by metadata-only objects.
27. No physical one-loop counterterm values are fabricated.
28. No matching kernel is created.
29. No proton TMD is exported.
30. No ART25 input or bridge calculation occurs.
31. No fit, inference, process, or production route is created.
32. Historical roots, `NO_JOINT_MEASURE`, the 216 routes, and authoritative artifacts remain unchanged.
33. `MSHT20_REP/` remains untouched and outside Git.
34. The working tree is clean except for that pre-existing untracked directory.
35. A local completion commit is created and not pushed.

---

# 18. Exact continuation

When the readiness gate passes, the next package is:

> **C41/R2B — finite-basis one-loop spacelike quark correlator, universal soft/overlap subtraction, partonic counterterm solution, and state-independent matching difference**

C41 must consume the actual C40 runtime objects.

It must not accept reconstructed metadata substitutes.

If C40 fails on a narrower object, the next package must target only that object rather than reopening the entire architecture.

---

# 19. Final Codex response

Report:

- resolved full starting and final commits;
- files and code modules created;
- selected numerical resolutions;
- q and qg dimensions;
- Gram residuals;
- Hamiltonian shapes, nnz, spectra, and matrix-free residuals;
- q->qg vertex shape, nnz, norm, and adjoint residual;
- constrained-sector operator statuses and norms;
- Ward full residual and every removal defect;
- Wilson matrix shape, nnz, norm, and independent-check residual;
- endpoint/transverse component norms;
- counterterm matrix shape, rank, nullity, and condition number;
- distributional measurement shapes, ranks, and moment residuals;
- refinement-map shapes and consistency residuals;
- runtime bundle hashes;
- focused fault-test count and results;
- exact readiness or no-go status;
- confirmation that no one-loop matching coefficient, proton TMD, ART25 bridge, fit, inference, or production action occurred;
- production/artifact integrity;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe schemas, descriptors, or status records as executable numerical infrastructure.
