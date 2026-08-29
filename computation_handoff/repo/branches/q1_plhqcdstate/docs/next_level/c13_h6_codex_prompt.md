# C13/H6 Codex Work Package

## Explicit two-gluon and sea-gluon Fock sectors, first-order support completion, and second-order non-Abelian Wilson convergence

You are beginning **C13/H6** for the DeuteronWigner project.

This package extends the validated microscopic H5 Wilson calculation by adding the explicit Fock sectors that C12 identified as missing:

\[
|qqqgg\rangle,
\qquad
|qqqu\bar u g\rangle,
\qquad
|qqqd\bar d g\rangle.
\]

The package has two linked purposes:

1. replace the C12 induced first-order antiquark and active-gluon Wilson channels by explicit microscopic Fock support, while retaining controlled explicit-versus-induced comparison and visible remainders;
2. perform the first strict second-order non-Abelian Wilson-line convergence benchmark, comparing Dyson and Magnus representations **only for channels whose required Fock support is actually present**.

C13 remains a finite-basis, validation-only microscopic calculation. It is not a physical or matched TMD, an all-orders Wilson result, a nuclear object, an evolution input, an inference model, or a process prediction.

---

# 1. Authoritative baseline

The authoritative physics baseline is the completed C12 commit:

```text
5c368cae780e76fc029a6db765f04167f1e09ac0
```

A documentation-only descendant is acceptable only when:

- the C12 commit above is in its ancestry;
- the working tree is clean before implementation begins;
- the complete C12 baseline reproduces exactly;
- no production physics, accepted artifact, or pinned prior manifest has changed.

Do **not** use `origin/main` as the scientific baseline when it lacks the local C3--C12 history.

Before modifying code, reproduce and record:

```text
910 existing tests
11 C12 builders/validators
36/36 evidence rows
162/162 atlas pages
294 C12 requirements
124/124 C12 negative injections
all earlier C3--C11 injection suites
216 accepted production reductions
all eight authoritative artifacts byte-identical
production provenance and default composition unchanged
C3/C4 analytic pilots unchanged
C5/C6 sign, cut, color, and soft-overlap oracles unchanged
C7--C11 microscopic state and GTMD oracles unchanged
```

If the checked-out commit is a documentation-only descendant, verify the ancestry and reproduce the same baseline before continuing.

Nothing in C13 may be pushed to a remote repository.

---

# 2. Normative sources

Read and use the available formalism sources under `references/`, especially:

```text
algebraic_geometric_next_level_model_note_revised.tex
volume_i_regulated_light_front_foundations.tex
volume_ii_common_nucleon_gtmd_overlaps.tex
volume_iii_dynamical_wilson_lines.tex
volume_vii_concrete_microscopic_nucleon_hamiltonian.tex
volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
volume_ix_dynamical_gluon_fock_sectors.tex
volume_x_light_sea_chiral_pcac_antiquark_gtmds.tex
volume_xi_microscopic_nonzero_transfer_gtmds.tex
```

Also read completely:

```text
docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c12_*manifest*.json
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
handoff/ROADMAP.md
```

Record every normative source path, SHA-256 hash, availability status, and role in:

```text
docs/next_level/c13_normative_source_integration.json
```

If a requested source is absent, do not invent its contents. Record the absence and use the indispensable equations in this work package plus the available APIs and reports.

---

# 3. Scientific boundary

C12 established a regulated first-order microscopic Wilson parent with:

- explicit `qqqg` support for active quark channels;
- induced `qqqq-qbar-g` support with remainders 0.018 and 0.021 for active antiquarks;
- induced `qqqgg` support with remainder 0.026 for active gluons;
- higher Wilson orders unavailable.

C13 must convert the first-order antiquark and active-gluon channels to explicit Fock support and then test second-order Wilson convergence where the enlarged state genuinely permits it.

The declared H6 Hilbert space is

\[
\begin{aligned}
\mathcal H_{\mathrm{H6}}={}&
\mathcal H_{qqq}
\oplus
\mathcal H_{qqqg}
\oplus
\mathcal H_{qqqu\bar u}
\oplus
\mathcal H_{qqqd\bar d}
\\
&\oplus
\mathcal H_{qqqgg}
\oplus
\mathcal H_{qqqu\bar u g}
\oplus
\mathcal H_{qqqd\bar d g}.
\end{aligned}
\]

Use stable internal sector labels, for example:

```text
QQQ
QQQG
QQQUUBAR
QQQDDBAR
QQQGG
QQQUUBARG
QQQDDBARG
```

or an equivalent typed scheme.

The central normalized state is

\[
|N,\Lambda\rangle
=
\sum_{\nu\in\mathcal F_{\mathrm{H6}}}
|\Psi_\nu^\Lambda\rangle,
\qquad
\sum_\nu P_\nu=1.
\]

This is still a finite resolution Hamiltonian-EFT state. Do not call it a physical continuum nucleon.

---

# 4. Primary objectives

C13 is complete only when all of the following are implemented and validated.

## 4.1 Explicit `qqqgg` sector

Implement a physical two-gluon Fock sector with:

- positive longitudinal support for both gluons;
- two-gluon helicity and transverse-mode labels;
- total \(J^z\), \(L_z\), and regulator identity;
- exact three-quark antisymmetry;
- exact combined bosonic exchange symmetry of the two gluons;
- complete SU(3) singlet multiplicity;
- center-of-mass and Lawson diagnostics;
- exact source/target sector identity for all operators.

The raw SU(3) invariant multiplicity is

\[
\dim\operatorname{Inv}_{SU(3)}
\left(3^{\otimes3}\otimes8\otimes8\right)=6.
\]

Derive this from common nullspaces of the total color generators rather than hard-coding six basis vectors.

The six channels arise schematically from:

- \(1_{qqq}\otimes1_{gg}\);
- the two independent \(8_{qqq}\) multiplicities combined with the two independent \(8_{gg}\) multiplicities;
- \(10_{qqq}\otimes\overline{10}_{gg}\).

The physical basis must retain the correct **combined** two-gluon exchange symmetry. Color-antisymmetric gluon channels are admissible only when compensated by the spin-orbital-mode part so that the full two-gluon state is bosonic.

A basis that simply symmetrizes color and discards the antisymmetric color channels is incomplete.

## 4.2 Explicit `qqqq-qbar-g` sectors

Implement separate `uubar-g` and `ddbar-g` sectors with:

- four-quark exact antisymmetry before operator assembly;
- direct positive-x antiquark identity;
- anti-fundamental antiquark color action;
- one adjoint gluon with explicit helicity and orbital labels;
- complete SU(3) singlet multiplicity;
- center-of-mass and regulator identity;
- exact flavor, charge, baryon, momentum, and \(J^z\) ledgers.

The raw SU(3) invariant multiplicity is

\[
\dim\operatorname{Inv}_{SU(3)}
\left(3^{\otimes4}\otimes\bar3\otimes8\right)=8.
\]

Derive the eight-dimensional invariant subspace from the total generators. Do not treat a baryon-meson cluster times a gluon as the complete color basis.

Both light-pair flavors must use the same formal machinery while retaining distinct flavor and assumption identities.

## 4.3 Coupled H6 Hamiltonian

Extend the H3 Hamiltonian to the seven-sector block operator

\[
\mathcal M_{\mathrm{H6},r}^{2}
=
\left(\mathcal M_{\alpha\beta,r}^{2}\right)_
{\alpha,\beta\in\mathcal F_{\mathrm{H6}}},
\qquad
\mathcal M_{\alpha\beta,r}^{2}
=
\left(\mathcal M_{\beta\alpha,r}^{2}\right)^\dagger.
\]

At minimum include typed, generated-adjoint interfaces for:

```text
QQQG <-> QQQGG
QQQUUBAR <-> QQQUUBARG
QQQDDBAR <-> QQQDDBARG
QQQGG <-> QQQUUBARG
QQQGG <-> QQQDDBARG
```

The last two represent a declared `g <-> q qbar` conversion in the presence of the spectator gluon.

Also include the spectator-lifted chiral interaction where H3 PLAN-A requires it:

```text
QQQG <-> QQQUUBARG
QQQG <-> QQQDDBARG
```

when allowed by the selected H6 assumption plan.

Every block must retain:

- Hamiltonian-owned coupling identity;
- emitting or converting parton slot;
- color intertwiner and outer multiplicity;
- longitudinal and transverse conservation;
- helicity and \(J^z\) selection;
- fermion signs and two-gluon exchange signs;
- endpoint, zero-mode, and regulator policy;
- generated Hermitian partner;
- approximation and provenance status.

Unsupported blocks must be explicitly absent for a named physical or truncation reason. They may not remain silently undefined.

## 4.4 Canonical non-Abelian partners

For the reduced second-order gauge benchmark, include typed contributions representing the required distinction among:

- sequential quark-gluon emissions;
- three-gluon emission or absorption;
- instantaneous-fermion terms;
- instantaneous-gluon terms;
- required contact or seagull partners at the declared truncation;
- vertex and sector counterterms.

This is not a request for a complete continuum Slavnov-Taylor implementation. It is a finite-basis, second-order non-Abelian consistency benchmark. The strongest possible status is:

```text
SECOND_ORDER_NONABELIAN_WILSON_BENCHMARKED
```

not `FULL_NONABELIAN_GAUGE_CLOSURE`.

---

# 5. Assumption plans

Compile at least the following immutable and mutually exclusive plans.

## H6-PLAN-A

```text
explicit QQQGG
explicit QQQUUBARG and QQQDDBARG
resolution-refitted induced confinement
canonical qg and g<->q qbar couplings
owned chiral interaction inherited from H3 PLAN-A
instantaneous and contact partners
second-order quark Wilson benchmark enabled
```

## H6-PLAN-B

```text
explicit QQQGG
explicit QQQUUBARG and QQQDDBARG
zero confinement
canonical qg and g<->q qbar couplings
chiral interaction disabled
instantaneous and contact partners
second-order quark Wilson benchmark enabled
```

## H5-REFERENCE

```text
read-only C12 parent
induced first-order antiquark/gluon channels
no explicit H6 sectors
no second-order Wilson claim
```

The three plans may be compared. They may never be added together.

The C12 induced operators and the new explicit sectors are mutually exclusive within one state description unless an explicit Feshbach matching relation and subtraction are selected.

---

# 6. Sector-dependent renormalization

Implement a resolution-indexed H6 renormalization datum

\[
\mathfrak R_r^{\mathrm{H6}}
=
\left(
\mathcal R_r,
\theta_{3,r},
\theta_{4g,r},
\theta_{5u,r},
\theta_{5d,r},
\theta_{5gg,r},
\theta_{6ug,r},
\theta_{6dg,r},
\delta\theta_r,
\{\mathcal C_i\},
\mathcal S_r,
\Delta_r
\right).
\]

At every resolution, refit the declared shared conditions rather than freezing the previous resolution's bare parameters.

Mandatory calibration conditions include:

\[
M_N^2=0.7744\;\mathrm{GeV}^2,
\qquad
F_1^p(0)=1,
\qquad
F_1^n(0)=0,
\]

plus:

- the inherited H2 Ward condition;
- the inherited H3 PCAC condition;
- one declared first-order sea-gluon or two-gluon vertex condition;
- one declared second-order ordered-color condition.

Keep the following as holdouts:

- a second two-gluon vertex point;
- a second sea-gluon vertex point;
- one nonzero-transfer current component;
- one two-gluon probability or momentum observable;
- one sea-gluon OAM observable;
- one second-order Wilson matrix element;
- one rotational or multiplet diagnostic.

Do not hide Jacobian null directions by fitting additional unrelated observables. Export the Jacobian, singular spectrum, identifiable combinations, and remaining null space.

Sector-dependent bare masses and couplings are resolution-dependent renormalization data, not different physical parton properties.

---

# 7. Exact, Krylov, and tensor-network state solutions

For every small H6 benchmark block, compare:

1. exact Hermitian diagonalization;
2. matrix-free Krylov solution;
3. exact full-bond tensorization;
4. variational symmetry-adapted TTN optimization.

The state tensor network must have explicit branches for:

```text
QQQ
QQQG
QQQUUBAR
QQQDDBAR
QQQGG
QQQUUBARG
QQQDDBARG
```

and must retain:

- Fock-sector identity;
- all color outer multiplicities \(1,2,3,6,8,8\);
- two-gluon exchange parity;
- four-quark permutation representation;
- antiquark anti-fundamental identity;
- gluon helicities;
- pair flavor;
- \(L_z\), \(J^z\), longitudinal, transverse, regulator, and plan labels.

Full bond must reproduce the exact state and every tested operator matrix element.

Finite-bond convergence must be reported separately for:

\[
\begin{array}{l}
P_{qqqgg},
P_{u\bar ug},
P_{d\bar dg},
\langle x_{gg}\rangle,
\langle x_{\bar ug}\rangle,
\langle x_{\bar dg}\rangle,\\
L_{gg},
L_{\bar qg},
\text{first-order antiquark Wilson norm},
\text{first-order gluon Wilson norm},\\
\text{second-order quark Wilson norm},
\text{Dyson--Magnus difference},
\text{soft-overlap residual},
\text{current/PCAC/Ward residuals}.
\end{array}
\]

At least one deliberately low-rank network must retain an accurate energy while visibly losing one of:

- a `qqqgg` color multiplicity;
- a `qqqq-qbar-g` color multiplicity;
- the non-Abelian commutator signal;
- an antiquark or gluon first-order Wilson amplitude;
- a second-order OAM interference.

A low-rank state that erases the only sector supporting the requested Wilson observable is not converged for that observable.

---

# 8. Replacement of C12 induced first-order channels

C12 reported:

```text
ubar first-order channel: induced, remainder 0.018
dbar first-order channel: induced, remainder 0.021
gluon first-order channel: induced qqqgg, remainder 0.026
```

C13 must construct the corresponding explicit matrix elements from:

```text
QQQUUBARG
QQQDDBARG
QQQGG
```

and compare each with the immutable C12 induced route.

The required provenance relations are scoped and typed:

```text
C12_INDUCED_UBAR_WILSON
    EQUIVALENT_TO
C13_EXPLICIT_UBAR_G_SECTOR + transformed operator + remainder

C12_INDUCED_DBAR_WILSON
    EQUIVALENT_TO
C13_EXPLICIT_DBAR_G_SECTOR + transformed operator + remainder

C12_INDUCED_GLUON_WILSON
    EQUIVALENT_TO
C13_EXPLICIT_QQQGG_SECTOR + transformed operator + remainder
```

After the explicit-support gates pass, the C13 validation root may issue:

```text
FIRST_ORDER_UBAR_EXPLICIT_FOCK_SUPPORTED
FIRST_ORDER_DBAR_EXPLICIT_FOCK_SUPPORTED
FIRST_ORDER_GLUON_EXPLICIT_FOCK_SUPPORTED
```

These statuses do not require numerical equality to the induced C12 oracle. Any difference must be decomposed into:

- finite Fock-space remainder;
- operator transformation;
- basis and regulator difference;
- numerical error;
- genuine dynamics.

Never fit the explicit sectors to reproduce the C12 induced numbers.

C12 remains immutable and reachable only as a benchmark or comparison object.

---

# 9. Wilson-order/Fock-order support manifest

Create one authoritative support manifest covering every species and Wilson order.

At minimum, C13 should establish:

| Species/channel | Wilson order 1 | Wilson order 2 |
|---|---|---|
| active quark | explicit `qqqg` | explicit `qqqgg` benchmark |
| active antiquark | explicit `qqqq-qbar-g` | unavailable without `qqqq-qbar-gg` or a matched induced operator |
| active gluon | explicit `qqqgg` | unavailable without `qqqggg` or a matched induced operator |

Use statuses only from:

```text
EXPLICIT_FOCK_SUPPORTED
INDUCED_OPERATOR_SUPPORTED_WITH_REMAINDER
UNAVAILABLE_AT_THIS_FOCK_ORDER
```

Do not label antiquark or active-gluon second-order Wilson channels complete in C13.

A requested Wilson order with insufficient Fock support must fail before numerical evaluation.

---

# 10. Strict second-order Wilson representations

Reuse the C5/C6 path, pole, cut, link, color, and soft-overlap types. Do not create a parallel Wilson identity system.

Let the existing convention-derived anti-Hermitian line generator be

\[
\mathcal K_\eta(s)
\]

for path orientation \(\eta\). Do not hard-code an independent sign for \(g\), \(i\), or the path orientation.

## 10.1 Strict Dyson expansion

Implement

\[
U_{D,\eta}^{[2]}
=
I
+
U_{D,\eta}^{(1)}
+
U_{D,\eta}^{(2)},
\]

with

\[
U_{D,\eta}^{(1)}
=
\int ds_1\,\mathcal K_\eta(s_1),
\]

\[
U_{D,\eta}^{(2)}
=
\int_{s_1>s_2}
ds_1\,ds_2\,
\mathcal K_\eta(s_1)
\mathcal K_\eta(s_2).
\]

The implementation must remain strictly truncated at second order. It may not accidentally include higher powers through a generic matrix exponential.

## 10.2 Strict Magnus expansion

Implement

\[
\Omega_1
=
\int ds_1\,\mathcal K_\eta(s_1),
\]

\[
\Omega_2
=
\frac12
\int_{s_1>s_2}
ds_1\,ds_2\,
[
\mathcal K_\eta(s_1),
\mathcal K_\eta(s_2)
],
\]

and the strict second-order reconstruction

\[
U_{M,\eta}^{[2]}
=
I+
\Omega_1+
\frac12\Omega_1^2+
\Omega_2.
\]

Do not compare a strict Dyson truncation to a fully exponentiated Magnus object that contains uncontrolled higher orders.

## 10.3 Required equivalence

For one common state, operator, path, regulator, and spectral rule, demonstrate

\[
U_{D,\eta}^{[2]}
-
U_{M,\eta}^{[2]}
=
\mathcal O(g^3)
\]

through explicit coefficient comparison and numerical scaling with the benchmark coupling.

The comparison must include:

- a commuting-field oracle where \(\Omega_2=0\);
- a noncommuting SU(3) oracle where the commutator is essential;
- a piecewise-constant path with an independently evaluated ordered matrix product;
- path composition through second order;
- path reversal;
- unitarity through the declared truncation order.

Required identities include

\[
U_{\gamma^{-1}}^{[2]}
=
\left(U_\gamma^{[2]}\right)^\dagger
+
\mathcal O(g^3),
\]

and

\[
\left(U_\gamma^{[2]}\right)^\dagger
U_\gamma^{[2]}
=
I+
\mathcal O(g^3).
\]

Removing \(\Omega_2\) in the noncommuting benchmark must produce a nonzero, signed residual.

---

# 11. Second-order color algebra

For two ordered gluon insertions on a fundamental line, retain the full product

\[
T^aT^b
=
\frac{1}{2N_c}\delta^{ab}I
+
\frac12 d^{abc}T^c
+
\frac{i}{2}f^{abc}T^c.
\]

The implementation must distinguish:

- ordered products \(T^aT^b\) and \(T^bT^a\);
- commutator and anticommutator sectors;
- singlet, \(d\)-type, and \(f\)-type components;
- the two-gluon color multiplicities in the microscopic state;
- Wilson-link order versus color-contraction identity.

Do not collapse the second-order result into one fitted scalar phase.

For the adjoint and mixed sectors, use the existing C6 color utilities where applicable and add only the missing typed recoupling data.

Required color benchmarks include:

- exact SU(3) generator identities;
- reconstruction of the ordered product;
- zero \(f\cdot d\);
- correct response under link reversal;
- nonzero orthogonal residual for a tensor outside the declared subspace;
- preservation of all six `qqqgg` singlets and all eight `qqqq-qbar-g` singlets.

---

# 12. Second-order spectral and cut dynamics

Reuse the C12 analytic continuum and finite-volume spectral-support infrastructure.

For a two-step ordered amplitude, implement a declared two-variable spectral representation such as

\[
\mathcal A_{\eta}^{(2)}(E_i)
=
\int dE_1\,dE_2\,
\frac{
\rho(E_1,E_2)N_\eta(E_1,E_2)
}{
(E_i-E_1+i0\sigma_\eta)
(E_i-E_2+i0\sigma_\eta)
},
\]

or an equivalent ordered resolvent construction derived from the existing API.

The imaginary part must be decomposed into explicit single-cut surfaces:

\[
\begin{aligned}
\operatorname{Im}\mathcal A_\eta^{(2)}
={}&
-\sigma_\eta\pi
\int dE_1\,dE_2\,
\rho N
\\
&\times
\left[
\delta(E_i-E_1)
\operatorname{PV}\frac{1}{E_i-E_2}
+
\operatorname{PV}\frac{1}{E_i-E_1}
\delta(E_i-E_2)
\right],
\end{aligned}
\]

The double-cut intersection contributes to the appropriate real component and must be represented separately.

Do not create a squared delta distribution. Coincident singular surfaces require an explicit regulator, finite-volume rule, or subtraction prescription.

The cut ledger must distinguish:

```text
FIRST_ORDER_EIKONAL_CUT
FIRST_ORDER_LF_RESOLVENT_CUT
SECOND_ORDER_CUT_SURFACE_1
SECOND_ORDER_CUT_SURFACE_2
SECOND_ORDER_DOUBLE_CUT_INTERSECTION
DISTINCT_ADDITIVE_CHANNEL
EQUIVALENT_COUNT_ONCE
```

Equivalent descriptions of one physical support region are counted once. Distinct ordered channels remain additive even when denominators happen to coincide numerically.

A finite numerical epsilon remains a convergence oracle and may not enter a physical result identity.

---

# 13. Matrix-level second-order action

Apply the strict second-order Wilson operator to the **complete C11 microscopic helicity matrices**, not to independently projected scalar TMDs.

For the supported quark benchmark, construct

\[
\mathcal M_q^{[\eta],[2]}
=
\mathcal M_q^{(0)}
+
\mathcal M_{q,\eta}^{(1)}
+
\mathcal M_{q,\eta}^{(2)}.
\]

Form link-even and link-odd matrices only after the complete antiunitary transformation:

\[
\mathcal M_{\rm odd}^{[2]}
=
\frac12
\left[
\mathcal M^{[+],[2]}
-
\Theta^{-1}
\mathcal M^{[-],[2]}
\Theta
\right].
\]

The antiunitary adapter must retain:

- complex conjugation;
- incoming/outgoing fiber exchange;
- path inversion and ordered-link reversal;
- target and parton helicity phases;
- transverse-momentum transformation;
- color representation and multiplicity;
- microscopic state and plan identity;
- Wilson and Fock order.

Do not construct the second-order link-odd result by subtracting arrays distinguished only by a `FUTURE` or `PAST` label.

At least one second-order quark Sivers-like and Boer--Mulders-like matrix projection must be evaluated from the same common rescattering operator and shown to remain distinct.

Do not claim physical second-order antiquark or active-gluon link-odd matrices when their required Fock sectors are absent.

---

# 14. Exact zero and ablation tests

The second-order supported signal must vanish under each applicable removal:

```text
coupling -> 0
continuum/cut support removed
required QQQGG sector removed
required Lz interference removed
commutator term removed in a channel whose signal is commutator-owned
future/past average applied to a link-odd projection
required color multiplicity removed
required instantaneous/contact partner removed
```

Removing a term not owned by the chosen benchmark must not create a false failure. Every ablation must record its ownership and expected sign.

The first-order explicit antiquark and gluon channels must retain all C12 zero limits.

---

# 15. Second-order soft and rapidity overlap

Extend the C6/C12 square-root-soft bookkeeping to strict second order.

For

\[
S
=
1+aS^{(1)}+a^2S^{(2)}+\mathcal O(a^3),
\]

use

\[
S^{-1/2}
=
1
-\frac12aS^{(1)}
+a^2
\left[
\frac38\left(S^{(1)}\right)^2
-\frac12S^{(2)}
\right]
+\mathcal O(a^3).
\]

The strict second-order subtracted boundary contains

\[
\begin{aligned}
W_{\rm sub}^{(2)}
={}&
W_{\rm unsub}^{(2)}
-
\frac12S^{(1)}W^{(1)}
\\
&+
\left[
\frac38\left(S^{(1)}\right)^2
-
\frac12S^{(2)}
\right]W^{(0)}
+
R_{\rm rap}^{(2)}W^{(0)}
+
Z_{\rm UV}^{(2)}W^{(0)},
\end{aligned}
\]

with any additional convention-dependent mixed terms represented explicitly.

Provide an analytic rapidity-log benchmark in which:

```text
correct first- and second-order subtraction -> declared rapidity derivative closes
missing S1*W1 subtraction -> nonzero signed residual
missing S2 subtraction -> nonzero signed residual
duplicate first-order subtraction -> signed over-subtraction
duplicate second-order subtraction -> signed over-subtraction
Dyson and Magnus routes -> identical subtracted result through order 2
```

This does **not** complete a physical TMD scheme. The following remain unresolved:

```text
UV_FINITE_MATCHING_REQUIRED
PHYSICAL_TMD_SCHEME_NOT_ASSIGNED
CONTINUUM_SOFT_FUNCTION_INCOMPLETE
NO_COLLINS_SOPER_EVOLUTION
NO_PROCESS_FACTOR_APPLIED
```

---

# 16. Common-state gauge and Ward diagnostics

Extend the finite-basis gauge-consistency diagnostics to the new sectors.

At minimum, test:

- total color-generator annihilation in every new sector;
- current conservation and inherited Abelianized Ward closure after the new sectors are included;
- required sequential, three-gluon, instantaneous, contact, and counterterm contributions in the reduced second-order benchmark;
- regulator and zero-mode consistency across every contribution;
- path-derivative or ordered-emission identities where supported by the present API.

Decompose the residual into owned pieces, for example:

```text
SEQUENTIAL_QG
THREE_GLUON
INSTANTANEOUS_FERMION
INSTANTANEOUS_GLUON
CONTACT_OR_SEAGULL
VERTEX_COUNTERTERM
SECTOR_COUNTERTERM
CURRENT_ATTACHMENT
REGULATOR
BASIS_TRUNCATION
MISSING_FOCK_SUPPORT
```

Removing each required nonzero component must produce a signed residual.

Passing this benchmark may issue:

```text
H6_SECOND_ORDER_GAUGE_CONSISTENCY_BENCHMARKED
```

but not `FULL_SLAVNOV_TAYLOR_CLOSURE`.

---

# 17. Provenance two-complex

Extend the provenance structure with explicit 0-, 1-, and 2-cells for:

- C12 induced versus C13 explicit first-order antiquark support;
- C12 induced versus C13 explicit first-order gluon support;
- Dyson versus Magnus second-order representation;
- sequential versus three-gluon ordered contributions;
- explicit higher sector versus Feshbach-induced operator plus remainder;
- eikonal versus LF-resolvent cut descriptions;
- first- and second-order soft-overlap subtraction;
- mutually exclusive H6 assumption plans.

Required two-cell semantics include:

```text
EQUIVALENT_WITH_REMAINDER
EQUIVALENT_COUNT_ONCE
REPLACES_WITHIN_SCOPE
MUTUALLY_EXCLUSIVE
SUBTRACTS_OVERLAP
COMMUTES_TO_DECLARED_ORDER
```

A nontrivial unresolved cycle must be reported as an audit failure or open relation. It may not be assigned a numerical amplitude.

---

# 18. Required software objects

Reuse existing formal APIs and add only the missing H6 types. The implementation should provide objects equivalent to:

```text
H6SectorSpec
TwoGluonExchangeSymmetry
H6ColorBasis
H6Hamiltonian
H6RenormalizationTrajectory
H6MicroscopicStateBundle
H6TensorNetworkManifest
WilsonFockSupportManifest
StrictDysonOrder2
StrictMagnusOrder2
DysonMagnusComparison
SecondOrderSpectralRule
SecondOrderCutLedger
SecondOrderColorDecomposition
SecondOrderSoftOverlap
ExplicitInducedWilsonComparison
H6GaugeClosureManifest
H6ConvergenceManifest
```

Do not duplicate C1 path identities, C3 recoil, C5 pole/cut types, C6 color and soft types, C8 TTN core, C10 state ledgers, or C11 helicity-matrix parents.

---

# 19. Required benchmark families

Implement at least the following benchmark families.

## H6-A: SU(3) singlet multiplicities

Verify by generator nullspaces:

```text
QQQGG       -> 6 singlets
QQQUUBARG   -> 8 singlets
QQQDDBARG   -> 8 singlets
```

Test orthonormality, deterministic phases, recoupling, and deliberate removal of every independent channel.

## H6-B: particle statistics

Verify exact three- and four-quark antisymmetry and complete two-gluon bosonic exchange symmetry, including color-antisymmetric channels paired with antisymmetric spin-space factors.

## H6-C: coupled-Hamiltonian Hermiticity

Test all new sector-changing blocks, generated adjoints, matrix-free action, and deterministic random complex superpositions.

## H6-D: renormalization trajectory

Fit the same declared conditions at several resolutions, export parameter flow, Jacobian spectrum, naturalness combinations, and holdout residuals.

## H6-E: exact/Krylov/TTN agreement

Verify exact and full-bond equality and observable-sensitive reduced-bond convergence across all seven branches.

## H6-F: explicit first-order antiquark support

Compare explicit `uubar-g` and `ddbar-g` Wilson matrices with the immutable C12 induced channels without fitting one to the other.

## H6-G: explicit first-order active-gluon support

Compare the explicit `qqqgg` route with the immutable C12 induced active-gluon route.

## H6-H: commuting Dyson/Magnus oracle

Verify \(\Omega_2=0\), strict order-two equivalence, path reversal, and unitarity.

## H6-I: noncommuting Dyson/Magnus oracle

Use noncommuting SU(3) generators and demonstrate the necessity of \(\Omega_2\).

## H6-J: piecewise-constant ordered path

Compare strict Dyson and Magnus expansions with an independently expanded ordered matrix product.

## H6-K: second-order spectral cuts

Test analytic and finite-volume support, threshold zeros, single-cut surfaces, double-cut bookkeeping, and rejection of numerical-epsilon physics.

## H6-L: second-order matrix-level Wilson action

Apply the operator to the complete H4 quark helicity matrix and test exact link reversal, OAM ownership, and distinct Sivers-like/Boer--Mulders-like projections.

## H6-M: second-order soft overlap

Test the square-root-soft expansion, rapidity cancellation, and signed missing/duplicate subtraction residuals.

## H6-N: common-state gauge consistency

Test the required sequential, three-gluon, instantaneous, contact, current, and counterterm contributions.

## H6-O: explicit/induced Feshbach comparison

Eliminate each new sector in a finite benchmark, transform the operator, retain the nonzero remainder, and prevent simultaneous explicit and induced selection.

## H6-P: support and readiness gates

Verify that first-order `q/qbar/g` support is explicit while second-order antiquark and gluon channels remain unavailable at this Fock order.

---

# 20. Mandatory negative injections

Add at least **144 stable C13 negative injections** with deterministic IDs and ordered diagnostics.

The injection suite must include, at minimum:

## Baseline and identity

- wrong baseline ancestry;
- changed authoritative artifact;
- changed 216-route registry;
- changed C12 manifest;
- missing state or plan identity;
- mixed H6 plans;
- production promotion.

## Color and statistics

- missing one of six `qqqgg` singlets;
- missing one of eight `qqqq-qbar-g` singlets;
- merged outer multiplicities;
- singlet-`qqq` times two free gluons;
- baryon-meson cluster times free gluon treated as complete;
- wrong anti-fundamental generator;
- broken four-quark antisymmetry;
- broken two-gluon bosonic exchange symmetry;
- discarded antisymmetric gluon-color channel without compensating mode symmetry;
- wrong recoupling phase.

## Hamiltonian and renormalization

- missing generated adjoint;
- wrong sector source/target;
- wrong parton emitter;
- broken longitudinal conservation;
- wrong \(J^z\);
- wrong fermion sign;
- wrong gluon exchange sign;
- reused counterterm across incompatible sectors;
- frozen renormalization coefficient across the tower;
- hidden Jacobian null direction;
- fit to a withheld Wilson observable.

## First-order explicit replacement

- explicit and induced antiquark selected together;
- explicit and induced gluon selected together;
- C12 remainder dropped;
- explicit state fitted to match C12 induced number;
- antiquark copied from quark;
- active gluon copied from scalar quark channel;
- missing positive-x antiquark slot;
- missing ordered adjoint identity.

## Wilson/Fock order

- second-order antiquark declared explicit without `qqqq-qbar-gg`;
- second-order active gluon declared explicit without `qqqggg`;
- second-order quark run without `qqqgg`;
- unsupported Wilson order evaluated instead of failing;
- induced operator used without visible remainder;
- missing support status.

## Dyson and Magnus

- hard-coded pole or path sign;
- strict Dyson compared with a full exponential;
- higher-order terms leaking into the order-two object;
- missing \(\Omega_2\) for noncommuting fields;
- wrong commutator sign;
- lost path ordering;
- swapped ordered links;
- failed path reversal;
- failed path composition;
- failed order-two unitarity;
- wrong coupling-scaling order;
- Dyson/Magnus comparison with different state or regulator identity.

## Spectral and cut dynamics

- numerical epsilon marked physical;
- support created below threshold;
- duplicate equivalent cut without a two-cell;
- distinct cuts incorrectly deduplicated;
- squared delta distribution;
- double-cut intersection treated as a single imaginary cut;
- missing ordered cut surface;
- wrong future/past cut sign;
- spectral rule identity lost;
- finite-volume sequence not convergent.

## Color decomposition

- \(T^aT^b\) and \(T^bT^a\) aliased;
- commutator and anticommutator merged;
- wrong \(f\) normalization;
- wrong \(d\) normalization;
- nonzero injected \(f\cdot d\) accepted;
- orthogonal color residual discarded;
- link order inferred from color class;
- process color weight inserted without process map.

## Matrix-level action

- scalar TMD projected before Wilson action;
- incomplete antiunitary reversal;
- lost target helicity;
- lost active-parton helicity;
- lost OAM block;
- Sivers and Boer--Mulders projectors aliased;
- universal fitted phase;
- future/past arrays merely subtracted by label;
- full-bond and exact identities mixed.

## Soft and rapidity

- missing \(-\frac12S^{(1)}W^{(1)}\);
- missing \(-\frac12S^{(2)}W^{(0)}\);
- missing \(\frac38(S^{(1)})^2W^{(0)}\);
- duplicate first-order subtraction;
- duplicate second-order subtraction;
- unresolved UV matching set to zero;
- physical TMD scheme declared complete;
- evolution attempted on unmatched object.

## Gauge and Ward

- sequential contribution removed;
- three-gluon contribution removed;
- instantaneous-fermion contribution removed;
- instantaneous-gluon contribution removed;
- contact/seagull contribution removed;
- vertex counterterm removed;
- regulator mismatch among contributions;
- zero-mode policy mismatch;
- full Slavnov--Taylor status issued from the finite benchmark.

## Downstream gates

- nuclear composition attempted;
- LF-to-QCD matching declared complete;
- Collins--Soper evolution attempted;
- physical SIDIS/DY/process map applied;
- inference/calibration attempted;
- accepted production artifact modified.

The final injection manifest must contain no duplicate IDs, no unstable ordering, and a clear expected diagnostic for every fault.

---

# 21. Immutable regression gates

C13 is accepted only when all prior gates remain passing and unchanged:

```text
all pre-existing tests plus new C13 tests
11 or more builders/validators, with all passing
36/36 evidence rows
162/162 atlas pages
all C3--C12 injections passing
216 accepted production routes exactly unchanged
all eight authoritative files byte-identical
production provenance and default composition unchanged
C3/C4 analytic pilots unchanged
C5/C6 oracles unchanged
C7--C12 microscopic manifests unchanged unless explicitly versioned as C13 descendants
```

The accepted production model must not import or execute C13 code.

---

# 22. Required documentation and machine-readable deliverables

Create at least:

```text
docs/next_level/c13_implementation_report.md
docs/next_level/c13_api.md
docs/next_level/c13_requirement_coverage.json
docs/next_level/c13_injection_manifest.json
docs/next_level/c13_regression_report.json
docs/next_level/c13_normative_source_integration.json
docs/next_level/c13_color_multiplicity_manifest.json
docs/next_level/c13_renormalization_trajectory.json
docs/next_level/c13_tensor_network_manifest.json
docs/next_level/c13_explicit_induced_wilson_comparison.json
docs/next_level/c13_wilson_fock_support_manifest.json
docs/next_level/c13_dyson_magnus_manifest.json
docs/next_level/c13_second_order_cut_manifest.json
docs/next_level/c13_second_order_soft_manifest.json
docs/next_level/c13_gauge_closure_report.json
docs/next_level/c13_convergence_manifest.json
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

only when appropriate and without altering pinned source files.

Every JSON output must be deterministic and machine readable.

---

# 23. Readiness statuses

C13 may issue only narrowly scoped validation statuses such as:

```text
H6_QQQGG_BASIS_VALIDATED
H6_SEA_GLUON_BASES_VALIDATED
H6_COUPLED_HAMILTONIAN_BENCHMARKED
H6_RENORMALIZATION_FLOW_BENCHMARKED
H6_TTN_CONVERGENCE_VALIDATED
FIRST_ORDER_Q_QBAR_G_EXPLICIT_FOCK_SUPPORT_VALIDATED
SECOND_ORDER_QUARK_DYSON_MAGNUS_BENCHMARKED
SECOND_ORDER_QUARK_SPECTRAL_CUT_BENCHMARKED
SECOND_ORDER_SOFT_OVERLAP_BENCHMARKED
H6_SECOND_ORDER_GAUGE_CONSISTENCY_BENCHMARKED
```

C13 must not issue:

```text
PHYSICAL_NUCLEON_EIGENSTATE
PHYSICAL_GTMD
PHYSICAL_TMD
MATCHED_TMD
ALL_ORDERS_WILSON_READY
FULL_SLAVNOV_TAYLOR_CLOSURE
SECOND_ORDER_ANTIQUARK_READY
SECOND_ORDER_GLUON_READY
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_READY
```

---

# 24. Acceptance criteria

C13/H6 is complete only when:

1. The exact C12 baseline reproduces before edits.
2. The `qqqgg` invariant subspace has derived multiplicity six.
3. Each `qqqq-qbar-g` invariant subspace has derived multiplicity eight.
4. Exact quark antisymmetry and two-gluon bosonic exchange symmetry pass.
5. The enlarged Hamiltonian is Hermitian and matrix-free/assembled actions agree.
6. Sector-dependent renormalization is refit along at least three tower points.
7. Exact, Krylov, and full-bond TTN states agree within declared tolerances.
8. Reduced-bond observable loss is visible and separately reported.
9. First-order antiquark channels use explicit `qqqq-qbar-g` support.
10. The first-order active-gluon channel uses explicit `qqqgg` support.
11. C12 induced routes remain immutable comparison objects with visible remainders.
12. The Wilson/Fock support manifest honestly marks second-order antiquark and gluon channels unavailable.
13. Strict Dyson and strict Magnus order-two objects agree through \(\mathcal O(g^2)\).
14. The noncommuting benchmark requires the Magnus commutator term.
15. Path composition, reversal, and order-two unitarity close.
16. The second-order spectral rule has correct threshold, sign, and finite-volume convergence.
17. The cut ledger counts equivalent support once and distinct support separately.
18. The matrix-level second-order action consumes the complete H4 parent.
19. Second-order Sivers-like and Boer--Mulders-like projections remain distinct.
20. Every declared zero and ablation limit closes.
21. The second-order soft-overlap benchmark cancels the declared rapidity dependence.
22. Missing and duplicate soft subtractions produce signed residuals.
23. The finite-basis gauge-consistency residual closes only with all owned contributions.
24. The provenance two-complex contains explicit/induced, Dyson/Magnus, cut, and soft-overlap relations.
25. At least 144 C13 negative injections are detected correctly.
26. All prior tests, builders, evidence, atlas, and injections remain passing.
27. The 216 production routes and eight authoritative artifacts remain byte-identical.
28. No downstream physical readiness status is issued.
29. Complete reports, APIs, manifests, and handoff notes are generated deterministically.
30. A final local commit is created, the working tree is clean, and nothing is pushed.

Do not declare C13 complete if any criterion is unmet.

---

# 25. Final response

The final Codex response must report:

- starting and final commits;
- push and working-tree status;
- complete test, builder, evidence, atlas, requirement, and injection counts;
- basis dimensions at every resolution;
- color multiplicities and residuals;
- antisymmetry and bosonic-exchange residuals;
- Hamiltonian, Krylov, and TTN residuals;
- parameter trajectories and remaining null directions;
- explicit-versus-induced first-order antiquark and gluon comparisons;
- Wilson/Fock support table;
- Dyson/Magnus residuals and coupling-order scaling;
- path composition, reversal, and unitarity residuals;
- spectral-cut and finite-volume residuals;
- second-order soft-overlap residuals;
- gauge-consistency residuals;
- all remaining scientific limitations;
- the exact recommended next work package.

The likely next package is one of:

```text
C14/N0:
matched spin-1 nuclear light-front state and microscopic deuteron GTMD composition
```

or, if essential second-order channels remain blocked:

```text
C14/H7:
qqqggg and qqqq-qbar-gg sectors for second-order antiquark/gluon closure
```

Choose the recommendation from the actual C13 support and convergence manifests. Do not predeclare nuclear readiness.
