# C117 Renormalization Recovery: Literature Study and Autonomous Completion Roadmap

## Executive decision

The C258 stop should be treated as the end of the **repository-only authority
search**, not the end of the scientific program.

The next phase is a human-authorized authority-recovery branch that may:

1. perform a broad but primary-source-only literature study;
2. classify the exact four C117 subtraction directions;
3. define a project intermediate renormalization scheme when no published
   scheme fixes the finite parts directly;
4. calculate the conversion/matching target;
5. solve the four coefficients at K9/K11/K13;
6. validate scheme, scale, regulator, symmetry, and resolution dependence;
7. resume the physical-input and Hamiltonian-binding chain;
8. proceed automatically to PennyLane physical activation after the existing
   activation gate closes.

No paper is expected to tabulate the four finite-C43 C117 coefficients. The
literature supplies the **renormalization architecture** and continuum target
definitions. The project still has to construct the finite-C43 adapter and
solve the four-dimensional affine matching problem.

## Starting authority

```text
C258 job:
C258/HQCDRIQUARKFIXEDKV2CURRENTTARGETAUDIT1

C258 completion commit:
ad81b2d61c97c9eb4624189df2713193673a4580

C258 package root:
b690bad5e4e47c39e5a9c482c26d673ac6eb6a5531df7806664d35c71098e897

C258 blocker:
ABSENT_INDISPENSABLE_AUTHORITY

missing object:
authenticated renormalization target capsule fixing four C117
instantaneous-current complement subtraction coefficients
```

The new branch is a **human-authorized prospective continuation**, not a
retrospective claim that C258 already contained the missing authority.

## Literature conclusions

### Rome–Southampton / RI-MOM

Martinelli et al. provide the generic method: choose amputated off-shell Green
functions, choose projectors, and impose renormalization conditions at a
specified scale. For a mixing basis the result is a matrix problem.

### RI/SMOM

Sturm et al. replace exceptional momentum subtraction by symmetric,
nonexceptional kinematics and construct conversion factors to MSbar.
Lehner and Sturm explicitly construct matrix RI/SMOM schemes for operator
bases with mixing and show that further schemes can be defined by choosing
projectors and finite amplitudes.

### Finite subtraction coefficients and Ward identities

Donini et al. explicitly study finite lattice subtraction coefficients and
show that projected RI conditions and Ward-identity determinations can agree
at large virtuality in the continuum and chiral limits. This is the closest
methodological precedent for the C117 problem.

### Nonperturbative running

Arthur et al. show that operator-mixing matrices can be evolved
nonperturbatively through continuum step-scaling matrices. This supplies the
path from a lower matching scale to a perturbative conversion window.

### Gauge-invariant alternatives

Recent GIRS work constructs gauge-invariant coordinate-space schemes and
conversion matrices to MSbar for mixing four-quark bases. Gradient-flow
schemes provide another gauge-invariant intermediate framework. These are
valuable holdouts when a gauge-fixed RI/SMOM definition is unstable or
difficult to adapt, but they are not automatically the best primary scheme
for a gauge-fixed light-front Hamiltonian current complement.

### Light-front truncation

Light-front renormalization literature establishes that Fock-space truncation
can require sector-dependent counterterms and bare parameters, and that Ward
identities or matching conditions are needed to fix them. Similarity
renormalization and corrected light-front Hamiltonian work likewise emphasize
that regulator-induced symmetry breaking requires counterterms whose finite
parts are fixed by equivalence, coherence, or renormalization conditions.

## Central mathematical form

Let the four C117 complement operators be

```text
Delta H_a^C117,  a = 1,...,4
```

and let the renormalized finite-basis current or Hamiltonian response be

\[
\Gamma_R^{(K)}
=
\Gamma_{\mathrm{calc}}^{(K)}
+
\sum_{a=1}^{4} c_a^{(K)}\,\Gamma_a^{(K)}.
\]

For four projectors \(\mathcal P_i\) and a named renormalization point
\(\mathcal K_\star\), impose

\[
\left.
\mathcal P_i\Gamma_R^{(K)}
\right|_{\mathcal K_\star}
=
t_i^{\mathcal S}(\mu),
\qquad i=1,\ldots,4.
\]

This gives

\[
M_{ia}^{(K)} c_a^{(K)} = b_i^{(K)},
\]

where

\[
M_{ia}^{(K)}
=
\left.
\mathcal P_i\Gamma_a^{(K)}
\right|_{\mathcal K_\star},
\qquad
b_i^{(K)}
=
t_i^{\mathcal S}
-
\left.
\mathcal P_i\Gamma_{\mathrm{calc}}^{(K)}
\right|_{\mathcal K_\star}.
\]

A valid four-condition scheme requires:

```text
rank M^(K) = 4;
stable singular values;
acceptable condition number;
the same continuum scheme semantics at K9/K11/K13;
explicit finite-basis adapter;
explicit source, unit, sign, and orientation conventions;
and a conversion or matching path to a standard/physical scheme.
```

The four target values need not be directly measured observables. They may be
the defining finite targets of an intermediate scheme, provided the scheme is
explicitly labeled and matched onward.

## Preferred strategy

Primary candidate:

```text
PROJECT_C117_RI_SMOM_V1
```

Use symmetric nonexceptional kinematics, a specified gauge, an exact
four-operator basis, four dual projectors, and either:

```text
tree-normalized target values;
continuum one-loop target values in a named RI/SMOM variant;
or a Ward/ST-constrained target plus enough independent RI/SMOM rows to
reach rank four.
```

Required holdouts:

```text
alternative RI/SMOM projector family;
Ward/ST hybrid;
GIRS or short-distance coordinate-space scheme;
scheme-scale variation;
K9/K11/K13 resolution variation.
```

A zero target is allowed only when it is a **scheme condition on a proven
unwanted mixing projection**, not because the coefficient is unknown.

## Package sequence

### C259/HQCDC117RENORMDESIGN1

Purpose:

```text
extract and classify the exact four C117 directions;
audit all C250-C258 projectors and target schemas;
acquire and hash-lock the primary literature corpus;
construct candidate RI/SMOM, Ward/ST-hybrid, and GIRS schemes;
build symbolic 4x4 response matrices;
select a primary scheme only after rank and conditioning tests.
```

No coefficient is selected.

Possible outcomes:

```text
C117_RI_SMOM_SCHEME_DESIGN_READY
C117_WARD_RISMOM_HYBRID_DESIGN_READY
C117_GIRS_SCHEME_DESIGN_READY
C117_OPERATOR_BASIS_OR_PROJECTOR_INCOMPLETE
C117_NO_FULL_RANK_RENORMALIZATION_SCHEME
```

### C260/HQCDC117RISMOM1

Purpose:

```text
define exact symmetric kinematics;
define gauge, scale, masses/flavors, source order, and four projectors;
construct the continuum operator basis;
derive the target vector and tree matrix;
prove full-rank duality;
publish PROJECT_C117_RI_SMOM_V1.
```

If the C259-selected scheme is different, use the exact selected package name.

### C261/HQCDC117CONTTARGET1

Purpose:

```text
calculate the continuum projected target amplitudes;
derive the RI/SMOM-to-MSbar or other standard conversion matrix;
preserve evanescent/operator-basis conventions;
publish perturbative uncertainty and scheme dependence.
```

A tree-normalized scheme may begin with tree targets, but a standard-scheme
conversion is still required before physical interpretation.

### C262/HQCDC117C43ADAPTER1

Purpose:

```text
map the continuum external kinematics and operator basis into the finite C43
cell and finite-HO basis;
use the existing wavepacket, Abel-regulator, current-projector, and omitted-
sector infrastructure;
construct M^(K) and b^(K) for K9/K11/K13;
prove source, unit, sign, boundary, and count-once compatibility.
```

### C263/HQCDC117SOLVE1

Purpose:

```text
solve the four coefficients at each resolution;
propagate target and numerical uncertainty;
publish singular values, condition numbers, correlations, and enclosures;
retain all scheme and scale labels.
```

No resolution average is allowed.

### C264/HQCDC117VALID1

Purpose:

```text
check Ward/BRST/ST compatibility;
check regulator and subtraction-scale dependence;
check K9/K11/K13 trajectories;
compare at least two legitimate scheme/projector variants;
test whether activation observables are scheme independent within the declared
accuracy;
test the alternative hypothesis that any direction is irrelevant.
```

### C265/HQCDC117STANDARDMATCH1

Purpose:

```text
complete step scaling/running and standard-scheme conversion;
bind active-flavor and threshold conventions;
produce the authenticated standard-coordinate C117 record.
```

### C266/HQCDPHYSBIND4

Purpose:

```text
resume the C213-C215 physical-input map;
bind the C117 solution and every remaining adapter;
close Hamiltonian-relevant counterterm/null directions or prove irrelevance.
```

### C267/HQCDRENHAMILTONIAN1 and descendants

Purpose:

```text
construct the renormalized K9 Hamiltonian;
construct K11/K13 holdout Hamiltonians;
run Hermiticity, ownership, BRST, leakage, units, and resolution gates;
issue the exact PennyLane physical-activation continuation.
```

The exact number of downstream jobs remains evidence-driven. The phase order
should remain fixed.

## Autonomous authority-recovery policy

Replace the old immediate stop on `ABSENT_INDISPENSABLE_AUTHORITY` with:

```text
AUTHORITY_RECOVERY_RESEARCH
```

when all of the following hold:

```text
the missing object is a renormalization prescription or external target;
the operator basis and projectors are sufficiently identified;
no exact inconsistency is present;
a project-defined intermediate scheme could lawfully fix the finite parts;
and matching to a standard/physical scheme is possible in principle.
```

In this mode the agent is authorized to:

```text
perform broad primary-source literature search;
acquire official TeX/source/PDF and hash-lock it;
define a clearly labeled project intermediate scheme;
derive conversion and matching calculations;
compare multiple schemes;
and continue without human relay.
```

It must still stop for:

```text
no full-rank condition exists for the four directions;
operator mixing cannot be closed because the basis is incomplete;
the finite-C43 adapter is proven nonexistent;
continuum and finite-basis source-qualified derivations contradict;
or the physical Hamiltonian depends on an unfixed direction after all
renormalization and matching routes are exhausted.
```

## Literature corpus to authenticate

Primary methodological corpus:

1. G. Martinelli et al., “A General Method for Non-Perturbative
   Renormalization of Lattice Operators,” arXiv:hep-lat/9411010.
2. C. Sturm et al., “Renormalization of quark bilinear operators in a
   momentum-subtraction scheme with a nonexceptional subtraction point,”
   arXiv:0901.2599.
3. A. Donini et al., “Non-Perturbative Renormalization of Lattice
   Four-Fermion Operators without Power Subtractions,”
   arXiv:hep-lat/9902030.
4. C. Lehner and C. Sturm, “Matching factors for Delta S=1 four-quark
   operators in RI/SMOM schemes,” arXiv:1104.4948.
5. R. Arthur et al., “Opening the Rome-Southampton window for operator
   mixing matrices,” arXiv:1109.1223.
6. M. Constantinou et al., “Gauge-invariant renormalization of four-quark
   operators,” arXiv:2406.08065.
7. M. Black et al., “Using Gradient Flow to Renormalise Matrix Elements for
   Meson Mixing and Lifetimes,” arXiv:2310.18059.
8. J.-F. Mathiot, V. A. Karmanov, and A. V. Smirnov,
   “Non-perturbative renormalization in Light Front Dynamics with Fock space
   truncation,” arXiv:hep-th/0510230.
9. V. A. Karmanov, J.-F. Mathiot, and A. V. Smirnov,
   “Systematic renormalization scheme in light-front dynamics with Fock space
   truncation,” arXiv:0801.4507.
10. S. A. Paston, V. A. Franke, and E. V. Prokhvatilov,
    “Constructing the light-front QCD Hamiltonian,” arXiv:hep-th/0002062.
11. J. A. O. Marinho et al., “Light-front Ward-Takahashi Identity for
    Two-Fermion Systems,” arXiv:0805.0707.
12. R. J. Perry, “Hamiltonian Light-Front Field Theory and Quantum
    Chromodynamics,” arXiv:hep-th/9407056.

## Required one-time scientific authorization

The human authorization should state:

> The project may define and use an explicitly labeled intermediate
> finite-basis renormalization scheme for the four C117 finite subtraction
> directions, provided the scheme has four independent conditions, respects
> the authenticated operator and symmetry structure, includes a conversion or
> matching path to a standard or physical scheme, preserves scheme dependence
> as a systematic, and is never presented as uniquely fixed by the bare action.

This authorization is sufficient for the agent to continue through the
research, design, matching, solve, validation, and activation phases without
returning merely because a published source does not tabulate the four
finite-C43 coefficients.
