# C41/R2B Codex Work Package

## Title

**One-loop finite-basis spacelike nonsinglet quark TMD: real/virtual execution, partonic renormalization, universal soft/overlap subtraction, distributional reconstruction, and state-independent matching**

## Authoritative baseline

Start from the clean local C40/M0B completion commit:

```text
f30596d39d9b38ab62b1749bb103c71460987753
```

Its authoritative starting ancestor is:

```text
79804d314555a58740b451c621940f48f28dc709
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 79804d314555a58740b451c621940f48f28dc709 HEAD
```

The baseline is valid only when it contains and reproduces:

```text
C39_FINITE_BASIS_ONE_LOOP_INCOMPLETE

C38_PARTONIC_STRUCTURAL_SCAFFOLD_ONLY

C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY
```

and the C40 numerical inventory, runtime bundles, focused mutation tests, and readiness gate pass.

Required historical ancestry includes:

```text
C36/O4:
    O4-SPACELIKE-COLLINS-JMY selected

C35/S0C:
    modified-delta finite-cell no-go retained

C32/R0:
    exact twelve-parent C11 tree reduction
```

Do not use `origin/main` when the local branch is ahead of the remote.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Scientific status entering C41

C40 has supplied actual deterministic numerical objects at three resolutions:

```text
K = 17:
    Nq = 4
    Nqg = 8

K = 23:
    Nq = 6
    Nqg = 12

K = 31:
    Nq = 8
    Nqg = 16
```

The executable substrate includes:

```text
q and qg basis arrays
Gram matrices
assembled and matrix-free free Hamiltonians
nonzero canonical q -> qg vertex and generated adjoint
five nonzero constrained-sector operators
nonzero spacelike Wilson matrices
separate longitudinal, endpoint, and transverse Wilson components
a ten-operator counterterm basis and numerical coefficient matrix
distributional measurement matrices
refinement and comparison maps
deterministic runtime-array bundles
```

C40 establishes numerical executability only. It does not itself establish:

```text
complete one-loop operator identity
physical one-loop counterterm coefficients
continuum-minus-finite-basis matching
soft/overlap cancellation
state-independent matching
a proton TMD
a bridge result
```

C41 must verify that the C40 substrate is source-derived and regulator-identical at the required order before using it. Executability is necessary but not sufficient.

---

# 2. Fixed physical decisions

Do not reopen these choices:

```text
physical rapidity/operator scheme:
    O4-SPACELIKE-COLLINS-JMY

pilot matching sector:
    rank-zero, T-even, quark nonsinglet

matching probes:
    C40 nonhadronic color-fundamental q and qg sectors

common IR:
    the exact mass-regulator plan inherited through C38/C40

soft ownership:
    universal B=0 soft factor outside the hadron TTN

finite-basis hadron parent:
    C11 remains separate and is not used as the matching probe

historical negative control:
    C35 finite-delta modified-delta Ward defect
```

C41 targets the diagonal nonsinglet coefficient:

```text
q <- q
```

and the charge-conjugate antiquark relation.

The following remain outside the positive scope unless independently calculated:

```text
q <- g
q <- qbar
full quark singlet mixing
gluon TMD matching
T-odd matching
spin-1 tensor matching
```

Do not promote a nonsinglet result to complete physical `u`, `d`, `ubar`, and `dbar` matching.

---

# 3. Primary objective

Use the C40 numerical substrate to calculate the same one-loop partonic TMD in:

```text
A. the selected continuum spacelike Collins/JMY scheme;

B. the finite-basis light-front regulator with the same spacelike
   Wilson geometry and common mass IR prescription.
```

Then extract the nonsinglet regulator conversion:

\[
F_{q,\mathrm{NS}}^{\mathrm{selected}}
=
Z_{q\leftarrow q,\mathrm{NS}}^{\mathrm{FB}\to\mathrm{selected}}
\otimes_x
F_{q,\mathrm{NS}}^{\mathrm{FB,reg}}
+
R_{\mathrm{NS}}.
\]

At one loop:

\[
Z_{q\leftarrow q,\mathrm{NS}}^{\mathrm{FB}\to\mathrm{selected}}
=
\delta(1-x)
+
a_s Z_{qq,\mathrm{NS}}^{(1)}
+
\mathcal O(a_s^2).
\]

The kernel must be derived from a common-IR partonic difference. It must not be obtained from:

```text
a proton-level ratio
an ART25/microscopic ratio
the twelve frozen bridge coordinates
a fitted normalization
a fitted x- or b-dependent correction
```

---

# 4. Calculation-first discipline

C41 is not another broad architecture package.

Do not create large families of metadata-only classes.

Every new scientific claim must correspond to:

```text
an evaluated array
an applied operator
a solved linear system
a distributional functional
a cancellation residual
a trajectory result
or an exact fail-closed diagnostic
```

The following statements remain mandatory:

```text
a manifest is not a matrix
an interface is not an operator
a source transcription is not an independent reconstruction
an executable toy is not automatically regulator-identical physics
```

---

# 5. Required source and code audit

Before evaluating the one-loop coefficient, audit every C40 runtime object against its derivation.

For each of:

```text
Hq
Hqg
V_qg_q
V_q_qg
instantaneous-fermion operator
instantaneous-gluon operator
constrained operator
boundary operator
zero-mode operator
Wilson longitudinal matrix
Wilson endpoint matrix
Wilson transverse matrix
counterterm operator basis
distributional measurement matrices
refinement maps
```

record:

```text
source or first-principles formula
normalization convention
basis ordering
color action
helicity action
momentum conservation
spacelike-direction dependence
IR-mass dependence
perturbative order
independent numerical check
```

Allowed audit statuses:

```text
REGULATOR_IDENTICAL_EXECUTABLE
EXECUTABLE_METHOD_ORACLE_ONLY
EXECUTABLE_TOY_NOT_PHYSICS_IDENTICAL
ABSENT_BLOCKING
```

The one-loop calculation may consume only `REGULATOR_IDENTICAL_EXECUTABLE` objects.

If a required C40 object is merely a deterministic toy or method oracle, issue:

```text
C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL
```

and specify the exact correction package.

Create:

```text
docs/next_level/c41_c40_substrate_fidelity_audit.json
```

---

# 6. Freeze numerical calculation points

Read the exact C36-C40 manifests and freeze before evaluation:

```text
external quark momenta
IR masses
u and d probe labels
both quark helicities
charge-conjugate antiquark probes
finite-rapidity vectors and invariant
future/past orientation
mu values
bT points
K = 17, 23, 31
all associated Nmax/bHO/basis identities
distributional test functions
counterterm renormalization conditions
holdouts
```

Do not invent missing numerical values.

If an essential value is absent, fail closed and name the absent record.

Create:

```text
docs/next_level/c41_calculation_plan.json
docs/next_level/c41_holdout_plan.json
```

---

# 7. Perturbative finite-basis state construction

Use light-front Hamiltonian perturbation theory in the C40 probe space.

For each external one-quark probe \(|q_i\rangle\), construct the first-order qg component:

\[
|\delta q_i\rangle_{qg}
=
G_{qg}(E_i)\,
V_{qg\leftarrow q}\,
|q_i\rangle,
\]

where the finite-basis resolvent is defined with the frozen energy-denominator prescription:

\[
G_{qg}(E_i)
=
\left(E_i-H_{qg}^{(0)}+i0\right)^{-1},
\]

or the exact light-front mass-squared analogue stored by the project.

Retain separately:

```text
canonical propagating qg component
instantaneous-fermion contribution
instantaneous-gluon contribution
constrained contribution
boundary contribution
zero-mode contribution
counterterm contribution
```

Construct the normalized dressed probe through \(O(g^2)\), including the wave-function normalization term required by probability/current normalization.

Required checks:

```text
direct solve versus spectral sum
assembled versus matrix-free resolvent action
Hermitian-conjugate relation
mass-IR dependence
normalization through declared order
nonzero qg probability at nonzero coupling
zero-coupling limit
```

Create:

```text
docs/next_level/c41_dressed_partonic_probe.json
docs/next_level/c41_resolvent_validation.json
```

---

# 8. Tree and one-loop bilocal measurement

Construct the finite-basis TMD measurement from the C40 distributional operators and the selected bilocal quark operator.

At tree level require:

\[
F_{\rm FB}^{(0)}(x,b_T)
=
\delta(1-x)
\]

in the exact finite-basis functional sense.

At \(O(g^2)\), calculate separately:

```text
wave-function normalization
real qg contribution
virtual quark self energy
bilocal operator vertex
canonical qg interference
spacelike Wilson interference
Wilson conjugate/absorption term
Wilson self-energy/two-insertion term
endpoint/cusp contribution
transverse-closure contribution
instantaneous terms
constrained term
boundary term
zero-mode term
counterterm insertions
```

The second-order Wilson contribution may be constructed from the two ordered first-order insertions and the qg intermediate sector only when the exact path-ordering and completeness identity proves that this is complete at the declared one-loop scope.

If a required direct second-order Wilson/contact operator is absent, keep the corresponding contribution blocking.

Create:

```text
docs/next_level/c41_finite_basis_bare_tmd.json
docs/next_level/c41_one_loop_contribution_ledger.json
```

Allowed contribution statuses:

```text
CALCULATED_NONZERO
CALCULATED_ZERO_BY_EXACT_IDENTITY
CANCELS_WITH_DECLARED_PARTNER
NOT_APPLICABLE_WITH_OPERATOR_PROOF
UNRESOLVED_BLOCKING
```

---

# 9. Real qg contribution

Calculate the real contribution using the normalized qg basis and the C40 measurement matrices.

Required ingredients:

```text
canonical q -> qg amplitude
operator-emission amplitude
spacelike Wilson-emission amplitude
their interference
finite-K x measurement
bT phase
mass-IR dependence
helicity/color sums
```

Required checks:

```text
direct basis sum versus matrix formulation
positive-support condition
total longitudinal momentum conservation
color-factor oracle
helicity selection
endpoint behavior
refinement across K
```

Create:

```text
docs/next_level/c41_real_qg_result.json
```

---

# 10. Virtual contribution

Calculate the virtual contribution using:

```text
qg resolvent
self-energy insertion
operator vertex correction
Wilson virtual/two-insertion contribution
instantaneous partners
boundary and zero-mode terms
counterterm insertions
```

Required checks:

```text
spectral sum versus matrix resolvent
principal-value/imaginary prescription
Hermiticity
mass-IR dependence
zero-coupling limit
cut/count-once relation to the real sector
```

Create:

```text
docs/next_level/c41_virtual_q_result.json
docs/next_level/c41_real_virtual_count_once_report.json
```

A numerical epsilon may be a convergence control but may not become physical support.

---

# 11. Solve the physical partonic counterterm system

Use the actual bare one-loop residual vector to solve:

\[
A_{\rm CT}\,c_{\rm CT}
=
r_{\rm bare}.
\]

The C40 synthetic solution is only a machinery test and must not be reused as a physical result.

Retain separate coefficients for:

```text
mass
field
canonical vertex
instantaneous partners
bilocal operator
spacelike Wilson line
endpoint/cusp
transverse closure
basis boundary
sector truncation
```

Report:

```text
A_CT rank
nullity
condition number
bare residual vector
solution
holdout residuals
resolution dependence
IR dependence
finite-rapidity dependence
```

Every renormalization condition must be partonic.

Do not use proton observables, ART25, or target continuum finite constants to fit these coefficients.

Create:

```text
docs/next_level/c41_counterterm_solution.json
docs/next_level/c41_counterterm_holdout_report.json
```

If the physical system is underdetermined, keep null directions explicit and issue the exact counterterm no-go.

---

# 12. Renormalized finite-basis collinear object

Assemble the finite-basis renormalized object with the exact operator ordering:

\[
F_{\rm FB}^{\rm ren}
=
\operatorname{REN}_{\rm FB}
\left[
F_{\rm FB}^{\rm bare}
+
F_{\rm inst}
+
F_{\rm constr}
+
F_{\rm boundary}
+
F_{\rm zero}
+
F_{\rm CT}
\right].
\]

Required checks:

```text
UV/cutoff closure
mass-IR structure
finite-rapidity identity
Ward/count-once closure
quark-number moment
charge conjugation
future/past equality for T-even rank zero
resolution dependence
```

Create:

```text
docs/next_level/c41_finite_basis_renormalized_tmd.json
docs/next_level/c41_finite_basis_closure_report.json
```

---

# 13. Continuum selected-scheme oracle

Calculate or independently reconstruct the same mass-regulated one-loop nonsinglet quark TMD in the selected spacelike Collins/JMY scheme.

Retain:

```text
tree term
real quark emission
virtual self energy
bilocal vertex
spacelike Wilson attachments
Wilson self energy
endpoint/cusp terms
universal soft factor
UV renormalization
finite-rapidity dependence
```

Represent the result distributionally:

\[
F_{\rm selected}^{(1)}
=
c_\delta(b_T)\delta(1-x)
+
c_+(b_T)\left[\frac{1}{1-x}\right]_+
+
c_{\log +}(b_T)
\left[\frac{\ln(1-x)}{1-x}\right]_+
+
f_{\rm reg}(x,b_T).
\]

Require two genuinely independent routes:

```text
source-exact expression
graph-level or scalar-integral reconstruction
```

Required checks:

```text
mass-IR dependence
Mellin moments
quark-number moment
gauge independence after subtraction
finite-rapidity derivative
future/past equality
```

Create:

```text
docs/next_level/c41_continuum_selected_tmd.json
docs/next_level/c41_continuum_oracle_validation.json
```

A source transcription alone is insufficient.

---

# 14. Distributional reconstruction

Use the C40 measurement matrices to evaluate the finite-basis result on the frozen test-function basis.

Reconstruct only the identifiable components:

```text
delta endpoint
plus term
log-plus term
regular-support component
Mellin moments
convolution action
```

Report:

```text
measurement-matrix rank
nullspace
condition number
identified coefficients or functional representation
holdout test-function residuals
refinement residuals
```

When the system is rank deficient, preserve the result as a distribution functional. Do not force a unique analytic decomposition.

Create:

```text
docs/next_level/c41_distributional_reconstruction.json
docs/next_level/c41_distributional_rank_report.json
```

---

# 15. Universal soft and overlap subtraction

Use the selected C36 universal B=0 spacelike soft factor outside the hadron TTN.

Apply the selected soft allocation and overlap convention exactly once.

Keep separate:

```text
unsubtracted collinear object
universal soft factor
soft-allocation power
overlap/zero-bin term
UV conversion
finite-rapidity dependence
```

Required controls:

```text
missing soft
duplicate soft
wrong soft power
missing overlap
duplicate overlap
wrong rapidity value
wrong bT convention
```

Required positive checks:

```text
count-once closure
gauge/Ward closure
common mass-IR consistency
finite-rapidity consistency
```

Create:

```text
docs/next_level/c41_soft_overlap_execution.json
docs/next_level/c41_soft_overlap_count_once_report.json
```

Do not assume cancellation from a source statement when the finite-basis overlap object has not been evaluated.

---

# 16. Extract the nonsinglet matching kernel

Only after the continuum and finite-basis sides are renormalized, soft/overlap subtracted, and use the same mass IR, calculate:

\[
Z_{qq,\mathrm{NS}}^{(1)}
=
F_{\rm selected,NS}^{(1),\rm ren}
-
F_{\rm FB,NS}^{(1),\rm ren}.
\]

The result must be:

```text
IR finite
gauge independent
external-probe independent
flavor independent for u/d nonsinglet probes
charge-conjugation consistent
explicit in the finite-basis regulator
explicit in finite rapidity
distributionally defined
```

Create:

```text
docs/next_level/c41_nonsinglet_matching_kernel.json
docs/next_level/c41_matching_remainder.json
```

If any required cancellation fails, serialize an empty-not-zero kernel.

---

# 17. State-independence and universality tests

Test the candidate kernel across:

```text
u and d probes
both helicities
at least two external momenta
at least two IR masses
quark and charge-conjugate antiquark probes
K = 17, 23, 31
an alternate normalized probe vector or wave packet
a simple composite toy state not used in extraction
```

The kernel may depend on regulator and resolution. It may not depend irreducibly on the probe state.

If it does, issue:

```text
STATE_DEPENDENT_MODEL_MAP
```

and do not call it matching.

Create:

```text
docs/next_level/c41_state_independence_report.json
docs/next_level/c41_flavor_antiquark_report.json
```

---

# 18. Refinement and trajectory

Use the C40 refinement maps to compare the one-loop object and candidate kernel across resolutions.

Test:

\[
R F_{K'} \approx F_K,
\]

\[
R Z_{K'} P \approx Z_K,
\]

in the exact functional/operator sense supported by the implementation.

Separate:

```text
K dependence
transverse-basis dependence
basis UV/IR effects
IR-mass dependence
finite-rapidity dependence
endpoint/boundary effects
zero-mode effects
numerical quadrature
```

Do not fit more trajectory coefficients than independent points support.

Allowed statuses:

```text
NONSINGLET_TRAJECTORY_RESOLVED
LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN
FINITE_BASIS_NONSINGLET_ONLY
NONIDENTIFIABLE_TRAJECTORY
TRAJECTORY_UNAVAILABLE
```

Create:

```text
docs/next_level/c41_matching_trajectory.json
docs/next_level/c41_trajectory_holdout_report.json
```

---

# 19. Selected-to-project conversion

If and only if the nonsinglet selected-scheme matching closes, execute the read-only C36 conversion to the project renormalized scheme.

Retain separately:

```text
operator conversion
UV convention
rapidity convention
soft allocation
hard-factor companion
scale relocation
ordinary evolution
```

Required checks:

```text
inverse
round trip
hard x TMD x TMD invariance at declared scope
mu RG
rapidity RG
first omitted order
```

Create:

```text
docs/next_level/c41_selected_to_project_execution.json
docs/next_level/c41_conversion_roundtrip_report.json
```

No ART25 member or fit parameter may enter.

---

# 20. Channel boundary and stopping point

C41 must explicitly report:

```text
q <- q nonsinglet
q <- qbar
q <- g
quark singlet
```

The expected positive scope is the nonsinglet diagonal channel.

Even if the nonsinglet result closes, C41 must not issue complete physical flavor matching or a proton TMD.

The strongest intended status is:

```text
C41_NONSINGLET_MATCHING_VALIDATED
```

The exact next package is then:

> **C42/MIX0 — color-fundamental gluon and antiquark probes, q<-g/q<-qbar channel calculation, and complete quark-singlet matching matrix**

Only after the complete channel matrix closes may a later package apply the kernel to microscopic proton states.

---

# 21. Numerical evidence and tests

Add focused tests of actual calculated objects.

Create at least 128 concrete numerical mutations, including:

```text
change a real qg matrix element
change a virtual energy denominator
drop a Wilson interference term
drop a constrained-sector term
drop a zero-mode term
break a counterterm row
reuse the C40 synthetic counterterm solution
remove an endpoint distribution
replace a plus distribution by a cutoff
break the mass-IR equality
break a refinement map
change an external probe
inject gauge dependence
duplicate soft subtraction
remove overlap subtraction
force a rank-deficient reconstruction to a unique solution
```

Each fault must alter an actual numerical result and trigger a failing closure or readiness assertion.

---

# 22. Required deliverables

Create at least:

```text
docs/next_level/c41_implementation_report.md
docs/next_level/c41_api.md
docs/next_level/c41_c40_substrate_fidelity_audit.json
docs/next_level/c41_calculation_plan.json
docs/next_level/c41_holdout_plan.json

docs/next_level/c41_dressed_partonic_probe.json
docs/next_level/c41_resolvent_validation.json

docs/next_level/c41_finite_basis_bare_tmd.json
docs/next_level/c41_one_loop_contribution_ledger.json
docs/next_level/c41_real_qg_result.json
docs/next_level/c41_virtual_q_result.json
docs/next_level/c41_real_virtual_count_once_report.json

docs/next_level/c41_counterterm_solution.json
docs/next_level/c41_counterterm_holdout_report.json

docs/next_level/c41_finite_basis_renormalized_tmd.json
docs/next_level/c41_finite_basis_closure_report.json

docs/next_level/c41_continuum_selected_tmd.json
docs/next_level/c41_continuum_oracle_validation.json

docs/next_level/c41_distributional_reconstruction.json
docs/next_level/c41_distributional_rank_report.json

docs/next_level/c41_soft_overlap_execution.json
docs/next_level/c41_soft_overlap_count_once_report.json

docs/next_level/c41_nonsinglet_matching_kernel.json
docs/next_level/c41_matching_remainder.json
docs/next_level/c41_state_independence_report.json
docs/next_level/c41_flavor_antiquark_report.json

docs/next_level/c41_matching_trajectory.json
docs/next_level/c41_trajectory_holdout_report.json

docs/next_level/c41_selected_to_project_execution.json
docs/next_level/c41_conversion_roundtrip_report.json

docs/next_level/c41_channel_status.json
docs/next_level/c41_source_sufficiency_decision.json
docs/next_level/c41_no_go_decision_tree.json
docs/next_level/c41_missing_calculation_specification.md
docs/next_level/c41_regression_report.json
```

Heavy arrays may remain under a content-addressed runtime directory. Commit their schemas, hashes, shapes, basis ordering, and deterministic reconstruction commands.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

---

# 23. Acceptance criteria

C41 is complete only when:

1. The full C40 baseline reproduces.
2. The C38/C39 readiness correction remains intact.
3. The C36 spacelike scheme remains fixed.
4. The C40 substrate fidelity audit is complete.
5. No method-only or toy object is consumed as regulator-identical physics.
6. Calculation points and holdouts are frozen before evaluation.
7. Dressed q and qg probe amplitudes are calculated.
8. Resolvent and spectral/direct routes agree.
9. Every required one-loop finite-basis contribution receives an explicit status.
10. Real qg contributions are calculated or fail closed.
11. Virtual contributions are calculated or fail closed.
12. Wilson, endpoint, and transverse contributions are explicit.
13. Instantaneous, constrained, boundary, and zero-mode contributions are explicit.
14. The physical counterterm RHS is calculated.
15. The C40 synthetic counterterm solution is not reused.
16. Counterterm rank, nullspace, solution, and holdouts are reported.
17. The renormalized finite-basis object is assembled only after counterterms exist.
18. The continuum selected-scheme result has two independent routes.
19. Endpoint distributions and Mellin moments are exact.
20. Distributional reconstruction reports rank and nullspace.
21. A rank-deficient result is not forced into a unique analytic form.
22. Universal soft and overlap subtractions are counted once.
23. The continuum and finite-basis calculations use the same mass IR.
24. The matching difference is IR finite when claimed.
25. The matching difference is gauge independent when claimed.
26. The candidate kernel is probe independent when called matching.
27. u/d flavor universality and antiquark charge conjugation are tested.
28. q<-q, q<-qbar, q<-g, and singlet statuses remain separate.
29. A nonsinglet result is not promoted to full physical flavor matching.
30. Refinement maps are applied to the calculated one-loop objects.
31. No trajectory is overfit.
32. Selected-to-project conversion is executed only after matching closes.
33. Hard-factor companion checks are explicit.
34. No proton TMD is exported.
35. No ART25 bridge calculation is executed.
36. No ART25 member, data, chi2, or residual enters the derivation.
37. No free normalization is introduced.
38. No fit, likelihood, posterior, reweighting, emulator, process, or production route is created.
39. Historical roots, `NO_JOINT_MEASURE`, 216 production routes, and authoritative artifacts remain unchanged.
40. `MSHT20_REP/` remains untouched and outside Git.
41. All runtime arrays and manifests reproduce deterministically.
42. At least 128 focused mutations of live numerical objects are detected.
43. The working tree is clean except for the pre-existing untracked directory.
44. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken regulator identity, common-IR cancellation, distributional rank, or state independence to obtain a coefficient.

---

# 24. Exact outcome branches

## Branch A: nonsinglet matching closes

```text
C41_NONSINGLET_MATCHING_VALIDATED
```

Next:

> **C42/MIX0 — q<-g, q<-qbar, and complete quark-singlet matching-channel construction**

## Branch B: C40 substrate is executable but not regulator-identical

```text
C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL
```

Next:

> **C42/M0C — source-derived correction of the affected Hamiltonian, constrained, Wilson, measurement, or refinement operators**

## Branch C: finite-basis one-loop contribution remains incomplete

```text
C41_FINITE_BASIS_ONE_LOOP_INCOMPLETE
```

Next:

> **C42/R2C — targeted unresolved real, virtual, Wilson, constrained, or boundary contribution completion**

## Branch D: counterterm system remains unresolved

```text
C41_PARTONIC_COUNTERTERM_SYSTEM_UNRESOLVED
```

Next:

> **C42/CT1 — physical one-loop partonic renormalization-condition and counterterm closure**

## Branch E: soft/overlap cancellation fails

```text
C41_SOFT_OVERLAP_CLOSURE_FAILED
```

Next:

> **C42/Z1 — selected-spacelike soft/collinear overlap completion**

## Branch F: distributional reconstruction is insufficient

```text
C41_DISTRIBUTIONAL_RECONSTRUCTION_UNRESOLVED
```

Next:

> **C42/X1 — finite-K endpoint, plus-distribution, and convolution completion**

## Branch G: state-independent matching fails

```text
C41_STATE_INDEPENDENT_MATCHING_UNAVAILABLE
```

Next:

> **C42/O2B — finite-basis operator/regulator redesign for universal matching**

## Branch H: trajectory remains unresolved

```text
C41_NONSINGLET_TRAJECTORY_UNRESOLVED
```

Next:

> **C42/R1B — nonsinglet matching trajectory and power-correction completion**

---

# 25. Final Codex response

Report:

- full starting and final commits;
- source and derivation fidelity of every C40 numerical operator;
- frozen calculation points and holdouts;
- dressed-probe norms and resolvent residuals;
- every one-loop finite-basis contribution and status;
- real and virtual values and count-once residuals;
- physical counterterm system rank, nullity, conditioning, solution, and holdouts;
- renormalized finite-basis TMD functional;
- continuum selected-scheme distributional coefficients and independent-oracle residuals;
- distributional reconstruction rank, nullspace, coefficients/functionals, and holdouts;
- soft/overlap subtraction residuals;
- nonsinglet matching kernel or exact empty-not-zero status;
- IR, gauge, Ward, sum-rule, and rapidity residuals;
- u/d, helicity, IR-mass, momentum, antiquark, and alternate-probe state-independence tests;
- refinement and trajectory results;
- selected-to-project conversion status;
- q<-q, q<-qbar, q<-g, nonsinglet, and singlet channel statuses;
- exact next branch;
- focused numerical mutation count;
- confirmation that no proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an executable substrate, a source transcription, a synthetic counterterm solution, a rank-deficient functional, or a nonsinglet-only result as complete physical quark TMD matching.
