# C14/H7 Codex Work Package

## Explicit three-gluon and sea–two-gluon Fock sectors, complete second-order Wilson support, and all-species non-Abelian convergence

You are beginning **C14/H7** for the DeuteronWigner project.

C13/H6 established a seven-sector microscopic state with explicit first-order Wilson support for quarks, antiquarks, and gluons, together with a strict second-order quark benchmark based on the explicit `QQQGG` sector. C13 correctly refused second-order antiquark and active-gluon requests because the required `QQQQ-QBAR-GG` and `QQQGGG` sectors were absent.

C14/H7 must add those missing sectors and close the declared second-order Wilson-support problem for all three partonic species:

\[
q,\qquad \bar q,\qquad g.
\]

The package has four linked purposes:

1. add complete, symmetry-correct `QQQGGG`, `QQQUUBARGG`, and `QQQDDBARGG` sectors to the microscopic Hamiltonian and tensor-network state;
2. provide explicit second-order Wilson support for active antiquarks and active gluons, while preserving the already validated quark second-order route;
3. compare strict Dyson and strict Magnus representations through order two in the fundamental, anti-fundamental, and adjoint/two-link operator classes;
4. complete the second-order cut, color, soft-overlap, gauge-closure, tensor-network, and explicit-versus-induced validation needed before microscopic spin-1 nuclear composition begins.

C14 remains a finite-basis, validation-only microscopic calculation. It is **not** a physical or matched TMD, an all-orders Wilson result, a continuum-QCD proof, a nuclear object, an evolution input, an inference model, or a process prediction.

Do not optimize for quickness. Completeness, physical correctness, auditable identities, and reproducibility are the objectives. Continue autonomously until every acceptance criterion is satisfied. Install routine local dependencies when the environment permits. Do not stop to request approval for ordinary local inspection, testing, or non-destructive tooling. Do not push the final commit.

---

# 1. Authoritative baseline

The authoritative scientific baseline is the completed C13 commit:

```text
ecec89b3847b8bdb4fa1736fb95b6ae37a8f946e
```

A documentation-only descendant is acceptable only when:

- the C13 commit above is in its ancestry;
- the working tree is clean before implementation begins;
- the complete C13 baseline reproduces exactly;
- no production physics, accepted artifact, or pinned prior manifest has changed.

Do **not** use `origin/main` as the scientific baseline when it lacks the local C3–C13 history.

Before modifying code, read the machine-readable C13 regression report and reproduce every recorded value. At minimum, verify and record:

```text
927 existing tests
all C13 acceptance builders and architecture validators
36/36 evidence rows
162/162 atlas pages
336 C13 requirements
148/148 C13 negative injections
all earlier C3–C12 injection suites
all 15 C13 generated JSON artifacts byte-identical on rebuild
216 accepted production reductions
all eight authoritative artifacts byte-identical
production provenance and default composition unchanged
C3/C4 analytic pilots unchanged
C5/C6 path, pole, cut, color, and soft-overlap oracles unchanged
C7–C12 microscopic state, GTMD, and Wilson oracles unchanged
```

Use `docs/next_level/c13_regression_report.json` and the generated C13 manifests as the source of truth if a count above is represented more precisely there.

Nothing in C14 may be pushed to a remote repository.

---

# 2. Normative sources

Read and use every available relevant formalism source under `references/`, especially:

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
docs/next_level/c13_implementation_report.md
docs/next_level/c13_api.md
docs/next_level/c13_*manifest*.json
docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c11_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c9_implementation_report.md
handoff/ROADMAP.md
```

Record every normative source path, SHA-256 hash, availability status, and role in:

```text
docs/next_level/c14_normative_source_integration.json
```

If a requested source is absent, do not invent its contents. Record the absence and use the indispensable equations in this work package together with the available APIs, reports, ADRs, and manifests.

---

# 3. Scientific boundary inherited from C13

C13 established the regulated seven-sector state

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

Its three tower dimensions are 72, 115, and 158. It retains six `QQQGG` color singlets and eight singlets in each sea–gluon sector, with complete quark antisymmetry and combined two-gluon bosonic symmetry.

C13 support is:

| Species | Wilson order 1 | Wilson order 2 |
|---|---|---|
| quark | explicit `QQQG` | explicit `QQQGG` |
| antiquark | explicit `QQQQ-QBAR-G` | unavailable |
| gluon | explicit `QQQGG` | unavailable |

C13 also established:

- strict Dyson/Magnus agreement through order two for the supported quark channel;
- path composition and reversal;
- cubic scaling of the order-two truncation and unitarity defects;
- separate one-cut surfaces and a real double-cut intersection;
- exact second-order square-root-soft subtraction;
- finite gauge closure only when sequential, three-gluon, instantaneous, contact, counterterm, and current pieces are included together;
- no claim of full Slavnov–Taylor closure.

C14 must preserve every C13 result while adding the missing explicit support.

---

# 4. H7 Hilbert space and stable sector identities

The declared H7 state space is

\[
\begin{aligned}
\mathcal H_{\mathrm{H7}}={}&
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
\mathcal H_{qqqd\bar d g}
\\
&\oplus
\mathcal H_{qqqggg}
\oplus
\mathcal H_{qqqu\bar u gg}
\oplus
\mathcal H_{qqqd\bar d gg}.
\end{aligned}
\]

Use stable typed labels, for example:

```text
QQQ
QQQG
QQQUUBAR
QQQDDBAR
QQQGG
QQQUUBARG
QQQDDBARG
QQQGGG
QQQUUBARGG
QQQDDBARGG
```

or an equivalent versioned scheme.

The normalized state is

\[
|N,\Lambda\rangle
=
\sum_{\nu\in\mathcal F_{\mathrm{H7}}}
|\Psi_\nu^\Lambda\rangle,
\qquad
\sum_\nu P_\nu=1.
\]

Every sector must retain:

- positive longitudinal support;
- full intrinsic transverse-mode identity;
- parton flavor, color representation, helicity, and orbital labels;
- total \(J^z\) and target identity;
- exact fermion permutation representation;
- exact gluon permutation representation;
- center-of-mass and Lawson status;
- regulator, resolution, zero-mode, and endpoint identity;
- assumption-plan and microscopic-member identity.

No new sector may be represented as an existing color-singlet cluster multiplied by one or two free gluons.

---

# 5. Exact SU(3) and permutation targets

## 5.1 `QQQGGG`: 22 color singlets

The raw color-singlet multiplicity is

\[
\dim\operatorname{Inv}_{SU(3)}
\left(3^{\otimes3}\otimes8^{\otimes3}\right)=22.
\]

This number must be derived from common nullspaces of the total SU(3) generators, not from 22 hard-coded tensors.

Useful decomposition checks are

\[
3^{\otimes3}=1\oplus8_\rho\oplus8_\lambda\oplus10,
\]

and

\[
\begin{aligned}
8^{\otimes3}={}&
2\cdot1
\oplus8\cdot8
\oplus4\cdot10
\oplus4\cdot\overline{10}
\oplus6\cdot27
\\
&\oplus2\cdot35
\oplus2\cdot\overline{35}
\oplus64.
\end{aligned}
\]

The three-gluon color space must also be decomposed under \(S_3\). The expected singlet-space content is:

```text
4 fully symmetric color singlets        [3]
4 fully antisymmetric color singlets    [1,1,1]
7 copies of the two-dimensional mixed irrep [2,1]
```

Thus the mixed sector contributes 14 states and

\[
4+4+2\times7=22.
\]

Equivalent representation checks are

\[
\operatorname{Sym}^3(8)
=
1\oplus8\oplus10\oplus\overline{10}\oplus27\oplus64,
\]

\[
\wedge^3(8)
=
1\oplus8\oplus10\oplus\overline{10}\oplus27,
\]

and

\[
\mathbb S_{[2,1]}(8)
=
3\cdot8\oplus10\oplus\overline{10}
\oplus2\cdot27\oplus35\oplus\overline{35}.
\]

The complete three-gluon wave function must be bosonic:

- symmetric color couples to symmetric spin–orbital–mode structure;
- antisymmetric color couples to antisymmetric spin–orbital–mode structure;
- mixed color couples to mixed spin–orbital–mode structure through an explicit \(S_3\) Clebsch map selecting the total symmetric component.

Do not discard the antisymmetric or mixed color sectors merely because color alone is not symmetric.

## 5.2 `QQQQ-QBAR-GG`: 28 color singlets per flavor

For each of `QQQUUBARGG` and `QQQDDBARGG`, the raw singlet multiplicity is

\[
\dim\operatorname{Inv}_{SU(3)}
\left(3^{\otimes4}\otimes\bar3\otimes8^{\otimes2}\right)=28.
\]

The five-parton color decomposition may be checked as

\[
3^{\otimes4}\otimes\bar3
=
3\cdot1
\oplus8\cdot8
\oplus4\cdot10
\oplus2\cdot\overline{10}
\oplus3\cdot27
\oplus35.
\]

Using

\[
\operatorname{Sym}^2(8)=1\oplus8_s\oplus27,
\]

and

\[
\wedge^2(8)=8_a\oplus10\oplus\overline{10},
\]

the color-singlet space splits into:

```text
14 two-gluon-color-symmetric singlets
14 two-gluon-color-antisymmetric singlets
```

The full two-gluon state must remain bosonic:

- symmetric color is paired with symmetric spin–orbital–mode structure;
- antisymmetric color is paired with antisymmetric spin–orbital–mode structure.

The four-quark subsystem must retain the exact signed \(S_4\) antisymmetrizer before Hamiltonian or operator assembly. The antiquark must use the anti-fundamental generator

\[
T_{\bar3}^a=-(T_3^a)^T.
\]

## 5.3 Mandatory color and statistics tests

For all new sectors, test:

- total-generator annihilation;
- orthonormality;
- exact multiplicity counts;
- deterministic phase conventions;
- recoupling unitarity;
- all required permutation-projector identities;
- quark antisymmetry under exchanges across apparent cluster partitions;
- two- and three-gluon total bosonic symmetry;
- correct anti-fundamental antiquark action;
- failure when any color channel or permutation irrep is removed.

---

# 6. H7 Hamiltonian and interaction blocks

Extend the C13 seven-block Hamiltonian to a ten-block Hermitian operator. At minimum, implement typed blocks and generated adjoints for the physically supported interactions:

```text
QQQGG       <-> QQQGGG
QQQUUBARG   <-> QQQUUBARGG
QQQDDBARG   <-> QQQDDBARGG
QQQGGG      <-> QQQUUBARGG
QQQGGG      <-> QQQDDBARGG
QQQGG       <-> QQQUUBARGG   [PLAN-A spectator-lifted chiral route where supported]
QQQGG       <-> QQQDDBARGG   [PLAN-A spectator-lifted chiral route where supported]
```

Also retain every C13 block and its identity.

Each interaction must declare whether it is generated by:

- quark or antiquark gluon emission/absorption;
- a three-gluon canonical vertex;
- a four-gluon/contact interaction;
- canonical \(g\leftrightarrow q\bar q\) conversion;
- a spectator-lifted chiral interaction;
- an instantaneous-fermion term;
- an instantaneous-gluon term;
- an induced operator from eliminated sectors;
- a sector or vertex counterterm;
- a declared truncation-discrepancy operator.

Every matrix element must retain:

- source and target sector;
- emitting/absorbing parton identity;
- color multiplicity and recoupling channel;
- longitudinal and transverse conservation;
- helicity and \(J^z\) selection;
- fermion and boson exchange signs;
- regulator, zero-mode, endpoint, and normalization identity;
- assumption plan and provenance.

Unsupported blocks must be represented as typed `UNAVAILABLE_WITH_REASON`, not silently set to zero.

Hermiticity, matrix-free/assembled equality, exact/Krylov agreement, and generated-adjoint closure are mandatory.

---

# 7. H7 assumption plans and renormalization trajectory

Define immutable H7 branches descending from the C13 plans, for example:

```text
H7-PLAN-A
    explicit all ten sectors
    resolution-refitted induced confinement
    canonical qg, 3g, 4g/contact, and pair-conversion blocks
    instantaneous partners
    spectator-lifted chiral blocks
    no duplicate induced higher-Fock correction

H7-PLAN-B
    explicit all ten sectors
    zero confinement
    canonical qg, 3g, 4g/contact, and pair-conversion blocks
    instantaneous partners
    chiral interaction disabled

H6-REFERENCE
    read-only C13 seven-sector theory
    no explicit QQQGGG or QQQQ-QBAR-GG
```

The plans are complete alternatives. They may be compared but not added.

Implement a resolution-dependent H7 renormalization datum containing at least:

\[
\mathfrak R_r^{\mathrm{H7}}
=
\left(
\mathcal R_r,
\theta_{\nu,r}^{\mathrm{bare}},
\delta\theta_{\nu,r},
\delta g_r,
\delta g_{3g,r},
\delta g_{4g,r},
\{\mathcal C_i\},
\mathcal S_r,
\mathcal Z_r,
\Delta_r
\right).
\]

At every tower point:

- refit the same declared mass and charge conditions;
- retain the existing C13 holdouts;
- add only the minimum conditions needed to identify the new sector/vertex trajectory;
- leave at least one second-order antiquark and one second-order gluon observable unfitted;
- retain Jacobian null directions rather than hiding them through additional fitted observables;
- report bare, counterterm, induced, and discrepancy flows separately.

Do not calibrate the new sectors to reproduce C13’s unavailable channels or to force a desired Wilson amplitude.

---

# 8. Ten-branch symmetry-adapted tensor network

Extend the microscopic state network to ten Fock branches with raw color multiplicities:

```text
QQQ          1
QQQG         2
QQQUUBAR     3
QQQDDBAR     3
QQQGG        6
QQQUUBARG    8
QQQDDBARG    8
QQQGGG      22
QQQUUBARGG  28
QQQDDBARGG  28
```

The network must retain:

- the Fock-root edge;
- all color outer multiplicities;
- \(S_3\) three-gluon symmetry labels;
- \(S_2\) two-gluon symmetry labels;
- exact quark permutation representation;
- antiquark anti-fundamental identity;
- gluon and antiquark helicities;
- longitudinal/transverse/OAM labels;
- total \(J^z\);
- regulator, resolution, plan, and microscopic-member identity.

Required solver hierarchy:

1. exact Hermitian diagonalization at the supported benchmark sizes;
2. matrix-free Krylov solution;
3. exact full-bond tensorization;
4. variational coupled-sector TTN optimization at multiple bond capacities.

Full bond must reproduce the exact state. Reduced-bond studies must report separately:

- energy;
- state overlap/principal angles;
- probabilities of all ten sectors;
- second-order antiquark Wilson norm;
- second-order active-gluon Wilson norm;
- quark order-two reference norm;
- Dyson–Magnus difference;
- commutator-sensitive color components;
- cut weights;
- OAM interference;
- soft-overlap cancellation;
- finite gauge-closure residual.

At least one reduced-bond state must reproduce the energy reasonably while visibly losing a real second-order antiquark or gluon Wilson feature.

---

# 9. Wilson-order/Fock-order capability manifest

Create a machine-readable capability manifest covering every species, Wilson order, Fock sector, operator representation, and attachment topology.

After C14 passes, the intended support table is:

| Species | Wilson order 1 | Wilson order 2 | Wilson order 3 |
|---|---|---|---|
| quark | explicit | explicit via `QQQGG` | unavailable in C14 |
| antiquark | explicit | explicit via `QQQQ-QBAR-GG` | unavailable |
| gluon | explicit | explicit via `QQQGGG` | unavailable |

The existence of `QQQGGG` is **necessary but not sufficient** for a third-order quark calculation. C14 does not implement the strict cubic Wilson polynomial, third-order cuts, cubic soft subtraction, or all required operator/contact terms. Therefore every Wilson-order-three request must fail closed.

Each route must be classified as one of:

```text
EXPLICIT_FOCK_SUPPORTED
INDUCED_OPERATOR_SUPPORTED_WITH_REMAINDER
UNAVAILABLE_AT_THIS_FOCK_ORDER
UNAVAILABLE_AT_THIS_WILSON_ORDER
UNAVAILABLE_MISSING_OPERATOR_COMPLETION
```

No route may infer support from the mere presence of a sector name.

---

# 10. Strict second-order Wilson dynamics for all species

Reuse the C5/C6/C12/C13 path, pole, cut, ordered-link, color, phase-budget, and soft-overlap APIs. Do not create a parallel Wilson type system.

For each supported operator representation, construct the strict Dyson polynomial

\[
U_D^{[2]}
=
I+U^{(1)}+U_D^{(2)},
\]

with

\[
U_D^{(2)}
=
\int_{s_1>s_2}
 ds_1 ds_2\,
\mathcal K(s_1)\mathcal K(s_2),
\]

and the strict Magnus polynomial

\[
\Omega_1=\int ds\,\mathcal K(s),
\]

\[
\Omega_2
=
\frac12
\int_{s_1>s_2}
 ds_1 ds_2
[\mathcal K(s_1),\mathcal K(s_2)],
\]

\[
U_M^{[2]}
=
I+\Omega_1+\frac12\Omega_1^2+\Omega_2.
\]

Require

\[
U_D^{[2]}-U_M^{[2]}=\mathcal O(g^3)
\]

for:

- the fundamental quark representation;
- the anti-fundamental antiquark representation;
- the adjoint representation;
- the ordered two-link active-gluon operator, including left-left, right-right, and left-right insertion topologies.

A strict order-two Dyson result may not be compared with a fully exponentiated Magnus operator containing uncontrolled higher orders.

Mandatory tests:

- commuting and noncommuting color fields;
- fundamental/anti-fundamental conjugation;
- adjoint commutator algebra;
- an independently multiplied piecewise-constant path oracle;
- path composition;
- path reversal and antiunitary mapping;
- order-two unitarity and cubic defect scaling;
- coupling-order scaling;
- nonzero failure when \(\Omega_2\) is removed;
- no aliasing of ordered gluon links or insertion topologies.

---

# 11. Matrix-level second-order link-odd parents

C14 must act on the complete H4/H5 microscopic helicity matrices, not on separately fitted scalar functions.

Construct strict order-resolved matrices

\[
\mathcal M_a
=
\mathcal M_a^{(0)}
+
\mathcal M_a^{(1)}
+
\mathcal M_a^{(2)},
\qquad
a=q,\bar q,g.
\]

For quarks and antiquarks, retain complete \(4\times4\) target–parton helicity matrices before projection.

For gluons, retain:

- the complete target-helicity matrix;
- transverse field indices;
- gluon-helicity representation;
- all four ordered link pairs;
- independent \(f\)- and \(d\)-type color channels;
- trace, circular/helicity, and symmetric-traceless/linear polarization sectors;
- both original `QQQG` color multiplicities and all relevant higher-sector multiplicities.

Construct link-even and link-odd matrices only after the complete antiunitary future/past transformation.

Sivers and Boer–Mulders projections must remain distinct matrix projectors. Do not impose any proportionality.

The second-order outputs must retain:

- species/flavor;
- proton/neutron member;
- H7 assumption plan;
- exact or TTN solver identity;
- kinematics and recoil;
- Wilson representation and order;
- ordered path/link identity;
- cut identity;
- Fock-support certificate;
- color multiplicity and \(f/d\) class;
- soft/rapidity status;
- ultraviolet matching status.

---

# 12. Second-order color algebra

For the fundamental representation, retain

\[
T^aT^b
=
\frac{1}{2N_c}\delta^{ab}I
+
\frac12d^{abc}T^c
+
\frac{i}{2}f^{abc}T^c.
\]

For antiquarks use

\[
\bar T^a=-(T^a)^T
\]

and derive the ordered products rather than copying the quark result.

For adjoint Wilson lines, use explicit adjoint generators and test

\[
[F^a,F^b]=if^{abc}F^c
\]

under the project convention.

For active-gluon correlators:

- preserve the ordered pair of adjoint links;
- preserve which insertions occur on the left or right link;
- keep Wilson ordering independent of final \(f/d\) projection;
- reconstruct the \(f/d\) subspace and report any orthogonal residual;
- refuse a default \(f+d\) mixture or process color weight.

Color identities must close separately in every relevant microscopic color-multiplicity block.

---

# 13. Two-step spectral support and cut ledger

Extend the C13 two-step spectral rule to explicit second-order antiquark and active-gluon channels.

For denominators

\[
D_1^{-1}=(x_1+i0\sigma_1)^{-1},
\qquad
D_2^{-1}=(x_2+i0\sigma_2)^{-1},
\]

separate:

- principal-value/principal-value terms;
- the first single-cut surface;
- the second single-cut surface;
- the real double-cut intersection;
- distinct ordered intermediate channels;
- equivalent eikonal and light-front-resolvent descriptions.

Do not form a squared delta distribution. If singular surfaces coincide, require an explicit finite-volume, regulator, or subtraction prescription.

The cut ledger must:

- count equivalent descriptions once through an executable two-cell;
- preserve physically distinct cuts even when denominators coincide numerically;
- retain species, Fock sector, attachment topology, path orientation, and intermediate-state identity;
- reject duplicate unqualified support;
- converge from a finite-volume/discretized sequence to an analytic continuum oracle.

Numerical \(\epsilon\) remains a convergence device and may not enter physical result identity or create below-threshold support.

---

# 14. Second-order soft and rapidity overlap for all representations

Reuse and extend the strict square-root-soft expansion

\[
S^{-1/2}
=
1-rac12aS^{(1)}
+
a^2
\left[
\frac38(S^{(1)})^2
-
\frac12S^{(2)}
\right]
+
\mathcal O(a^3).
\]

At second order,

\[
\begin{aligned}
W_{\rm sub}^{(2)}={}&
W_{\rm unsub}^{(2)}
-
\frac12S^{(1)}W^{(1)}
\\
&+
\left[
\frac38(S^{(1)})^2
-
\frac12S^{(2)}
\right]W^{(0)}
+
R_{\rm rap}^{(2)}W^{(0)}
+
Z_{\rm UV}^{(2)}W^{(0)}.
\end{aligned}
\]

Implement separate typed soft-overlap identities for:

- fundamental quarks;
- anti-fundamental antiquarks;
- adjoint active-gluon links;
- the ordered two-link gluon geometry.

Required analytic checks:

```text
correct subtraction              -> rapidity derivative closes
missing S1*W1                    -> signed nonzero residual
missing S2                       -> signed nonzero residual
duplicate first-order term       -> over-subtraction
duplicate second-order term      -> over-subtraction
wrong representation soft factor -> nonzero residual
swapped gluon link geometry      -> identity mismatch
Dyson and Magnus routes          -> same strict order-two subtracted result
```

Ultraviolet finite matching, a physical TMD scheme, Collins–Soper evolution, and process factors remain unresolved and nonzero in status.

---

# 15. Finite gauge-closure benchmark

Extend the C13 finite gauge benchmark to the new sectors and all second-order species channels.

The closure ledger must include, where required:

- sequential emissions/absorptions;
- three-gluon vertices;
- four-gluon/contact terms;
- instantaneous-fermion terms;
- instantaneous-gluon terms;
- pair-conversion attachments;
- spectator-lifted chiral attachments;
- vertex and sector counterterms;
- Hamiltonian-consistent currents;
- wave-function/residue normalization;
- regulator and zero-mode terms.

Removing any nonzero required piece must produce a signed residual.

The benchmark may issue a status such as

```text
H7_FINITE_SECOND_ORDER_GAUGE_BENCHMARKED
```

but must never issue

```text
FULL_NONABELIAN_SLAVNOV_TAYLOR_CLOSURE
```

unless the complete ghost, BRST, nonlinear field, regulator-restoration, and all-sector identities have actually been implemented and proved. C14 does not attempt that proof.

---

# 16. Explicit-versus-induced H7 comparison

Perform a controlled Feshbach elimination of the new H7 sectors into the H6 space.

For \(P=\mathcal H_{\mathrm{H6}}\) and \(Q\) the three new sectors,

\[
H_{\rm eff}(E)
=
PHP
+
PHQ(E-QHQ)^{-1}QHP,
\]

and every Wilson/current/GTMD operator must transform consistently:

\[
O_{\rm eff}(E',E)
=
P[1+\omega^\dagger(E')]O[1+\omega(E)]P.
\]

The provenance relation is

```text
H7 explicit QQQGGG / QQQQ-QBAR-GG sectors
    EQUIVALENT_TO
H6 induced second-order operators
    + transformed observables
    + visible remainder
```

It is never an additive relation.

C13 did not provide an authoritative second-order antiquark/gluon number. Do not fit the H7 explicit channels to any invented target. The induced H6 comparator is a validation object generated by the declared elimination, and any nonzero remainder remains visible.

Within the H7 validation root, explicit support may replace the previous `UNAVAILABLE_AT_THIS_FOCK_ORDER` status only after all color, statistics, operator, cut, soft, gauge, and convergence gates pass.

---

# 17. Provenance two-complex and assumption compiler

Extend the existing compiler and provenance structures rather than creating parallel graphs.

Required 0-cells include:

- all ten sector spaces;
- exact/Krylov/TTN states;
- Wilson-order-one and Wilson-order-two operators;
- soft and cut objects;
- explicit and induced descriptions;
- H7 plans and readiness results.

Required 1-cells include:

- sector emission/absorption;
- three- and four-gluon interactions;
- pair conversion;
- projection;
- matching/subtraction;
- elimination;
- explicit replacement;
- Wilson handoff.

Required 2-cells include:

- explicit/induced equivalence plus remainder;
- count-once cut relations;
- soft-overlap subtraction;
- path-composition equivalence;
- Dyson/Magnus strict-order equivalence;
- gauge-completion relations.

A nontrivial unresolved cycle must be reported as an audit signal. It may not be assigned a physical amplitude automatically.

The `AssumptionBundle -> PredictionPlan` compiler must reject:

- H7 explicit sectors selected with their induced H6 replacements;
- PLAN-A and PLAN-B selected together;
- Wilson-order-three requests;
- second-order requests missing operator completion even when a sector exists;
- nuclear, matching, evolution, process, or inference requests from H7 validation objects.

---

# 18. Required H7 outputs and statuses

Create versioned state, Wilson, color, cut, soft, gauge, and convergence bundles containing at least:

```text
H7MicroscopicStateBundle
H7ColorPermutationManifest
H7RenormalizationTrajectory
H7TensorNetworkManifest
H7WilsonSupportManifest
H7DysonMagnusManifest
H7SpectralCutManifest
H7SoftOverlapManifest
H7GaugeClosureManifest
H7ExplicitInducedComparison
H7ConvergenceManifest
H7PredictionPlanManifest
```

Permissible qualified statuses include:

```text
H7_TEN_SECTOR_STATE_VALIDATED
H7_QQQGGG_COLOR_PERMUTATION_VALIDATED
H7_SEA_TWO_GLUON_COLOR_PERMUTATION_VALIDATED
SECOND_ORDER_QUARK_EXPLICIT_FOCK_SUPPORTED
SECOND_ORDER_ANTIQUARK_EXPLICIT_FOCK_SUPPORTED
SECOND_ORDER_GLUON_EXPLICIT_FOCK_SUPPORTED
STRICT_DYSON_MAGNUS_ORDER_TWO_VALIDATED
SECOND_ORDER_CUT_LEDGER_VALIDATED
SECOND_ORDER_SOFT_OVERLAP_BENCHMARKED
H7_FINITE_SECOND_ORDER_GAUGE_BENCHMARKED
H7_TTN_OBSERVABLE_CONVERGENCE_VALIDATED
```

Forbidden statuses include:

```text
PHYSICAL_NUCLEON
PHYSICAL_GTMD
PHYSICAL_TMD
ALL_ORDERS_WILSON
WILSON_ORDER_THREE_READY
FULL_SLAVNOV_TAYLOR_CLOSURE
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_READY
```

Every output must retain the unresolved statuses:

```text
UV_FINITE_MATCHING_REQUIRED
PHYSICAL_TMD_SCHEME_NOT_ASSIGNED
CONTINUUM_SOFT_FUNCTION_INCOMPLETE
NO_COLLINS_SOPER_EVOLUTION
NO_PROCESS_FACTOR_APPLIED
NO_NUCLEAR_COMPOSITION_APPLIED
```

---

# 19. Benchmark families

Implement at least the following benchmark families with stable identifiers.

## H7-A: color multiplicity and permutation

- 22 `QQQGGG` singlets;
- 4 symmetric, 4 antisymmetric, 7 mixed \(S_3\) copies;
- 28 singlets in each sea–two-gluon sector;
- 14 symmetric and 14 antisymmetric two-gluon color channels;
- total-generator annihilation;
- recoupling unitarity;
- exact quark and gluon statistics.

## H7-B: ten-block Hamiltonian

- Hermiticity;
- generated adjoints;
- assembled/matrix-free equality;
- exact/Krylov agreement;
- supported and unsupported block identities.

## H7-C: renormalization flow

- common mass/charge conditions;
- new sector/vertex flow;
- visible Jacobian null directions;
- unfitted second-order antiquark/gluon holdouts.

## H7-D: ten-branch TTN

- full-bond exact reconstruction;
- variational energy bounds;
- color/permutation retention;
- observable-sensitive reduced-bond failure.

## H7-E: anti-fundamental second-order Wilson algebra

- strict Dyson/Magnus equality through order two;
- conjugation from the fundamental representation;
- future/past reversal;
- direct positive-x antiquark identity.

## H7-F: adjoint and two-link second-order Wilson algebra

- all four ordered link pairs;
- left-left, right-right, and left-right insertion topologies;
- strict Dyson/Magnus equality;
- separate \(f/d\) channels;
- no implicit process mixture.

## H7-G: second-order cut support

- two single-cut surfaces;
- real double-cut intersection;
- finite-volume convergence;
- no below-threshold absorption;
- no physical numerical epsilon;
- no squared delta.

## H7-H: second-order soft overlap

- fundamental, anti-fundamental, adjoint, and two-link identities;
- exact rapidity-derivative closure;
- signed missing/duplicate-term residuals.

## H7-I: finite gauge closure

- all required propagating, instantaneous, contact, counterterm, and current pieces;
- signed ablation residuals;
- explicit nonclaim of full Slavnov–Taylor closure.

## H7-J: explicit/induced comparison

- Feshbach Hamiltonian and operator equivalence;
- visible remainder;
- fail-closed double counting.

## H7-K: order-by-order microscopic matrices

- complete quark/antiquark/gluon matrix parents;
- link-even/link-odd reconstruction;
- distinct Sivers/Boer–Mulders projections;
- ordered-link and \(f/d\) closure.

## H7-L: multi-axis convergence

- basis and resolution;
- Fock content;
- exact/Krylov/full-bond/reduced-bond;
- spectral discretization;
- path quadrature;
- Gram conditioning;
- soft and gauge residuals.

## H7-M: downstream gates

- production unreachable;
- nuclear composition unavailable;
- LF-to-QCD matching unavailable;
- evolution/process/inference unavailable;
- Wilson order three unavailable.

---

# 20. Mandatory negative injections

Create at least **168 ordered H7-specific negative injections** with stable IDs and deterministic diagnostics. The suite must include, but is not limited to:

### Color and permutation

- 21 instead of 22 `QQQGGG` singlets;
- lost symmetric, antisymmetric, or mixed \(S_3\) sector;
- mixed color coupled without the symmetric \(S_3\) Clebsch;
- 27 instead of 28 sea–two-gluon singlets;
- wrong 14/14 exchange split;
- color-only bosonic symmetrization;
- broken four-quark antisymmetry;
- wrong antiquark generator;
- singlet cluster times free gluons;
- nonunitary recoupling;
- phase-unstable color serialization.

### Hamiltonian and renormalization

- missing generated adjoint;
- wrong sector identity;
- broken longitudinal/transverse conservation;
- wrong fermion or boson exchange sign;
- duplicate explicit and induced interaction;
- frozen new-sector counterterm across resolutions;
- extra fitted observable hiding the null direction;
- calibration to an invented C13 second-order target;
- mismatched regulator or zero-mode policy.

### TTN

- missing Fock-root edge;
- merged color multiplicities;
- erased \(S_3\) or \(S_2\) irrep identity;
- full-bond state not exact;
- variational energy below exact;
- nonnested bond spaces presented as monotonic;
- energy-only convergence claim after Wilson-signal loss;
- unreported discarded symmetry block.

### Wilson order and representation

- false Wilson-order-three readiness;
- anti-fundamental copied from quark without conjugation;
- missing Magnus commutator;
- strict Dyson compared with fully exponentiated Magnus;
- order leakage from \(g^3\) or higher;
- wrong adjoint generator sign;
- swapped or unordered gluon links;
- merged left-left/right-right/left-right topology;
- implicit \(f+d\) mixture;
- process color weight without process map.

### Spectral and cuts

- numerical epsilon used as physical support;
- absorption below threshold;
- duplicate equivalent cut;
- accidental deduplication of distinct cuts;
- squared delta;
- missing double-cut intersection;
- wrong future/past sign;
- lost intermediate-state identity;
- nonconvergent finite-volume rule declared complete.

### Soft and rapidity

- missing \(S^{(1)}W^{(1)}\);
- missing \(S^{(2)}\);
- duplicate first- or second-order subtraction;
- quark soft factor used for adjoint link;
- wrong ordered-link soft geometry;
- rapidity derivative nonzero but status marked closed;
- unresolved UV term set to zero;
- physical scheme assigned without matching.

### Gauge closure

- omitted sequential term;
- omitted three-gluon term;
- omitted four-gluon/contact term;
- omitted instantaneous-fermion term;
- omitted instantaneous-gluon term;
- omitted pair-conversion attachment;
- omitted current/counterterm contribution;
- full Slavnov–Taylor status issued from the finite benchmark.

### Provenance and downstream gates

- explicit and induced sectors selected together;
- PLAN-A and PLAN-B combined;
- rollback edge missing;
- unresolved provenance cycle ignored;
- H7 result inserted into the 216-route registry;
- accepted artifact modified;
- nuclear composition attempted;
- evolution attempted;
- process map attempted;
- inference or calibration attempted;
- production promotion attempted;
- normative source mutated.

Every negative injection must fail before or at the correct typed boundary with a structured diagnostic. A downstream numerical mismatch is not an adequate substitute for a fail-closed architecture test.

---

# 21. Regression and isolation requirements

C14 must preserve the complete C13 baseline and every prior scientific artifact.

Mandatory final gates:

```text
all existing C13 tests plus new C14 tests pass
all named acceptance builders and validators pass
36/36 evidence rows pass
162/162 atlas pages pass
all C3–C13 injections remain passing
at least 168/168 C14 injections pass
216 production routes unchanged
all eight authoritative artifacts byte-identical
all pinned C5/C6/C7–C13 manifests unchanged unless explicitly regenerated as C14 descendants
production provenance and composition unchanged
C3/C4 analytic pilots immutable
C11 H4 parent immutable
C12 H5 parent immutable
C13 H6 parent and 15 manifests immutable
```

The H7 graph must remain disconnected from:

- accepted production;
- deuteron/nuclear composition;
- LF-to-QCD matching;
- TMD evolution;
- process factorization;
- inference and calibration.

No accepted phenomenological number may be used as a hidden calibration target for H7.

---

# 22. Required deliverables

Create at least:

```text
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
docs/next_level/c14_requirement_coverage.json
docs/next_level/c14_injection_manifest.json
docs/next_level/c14_regression_report.json
docs/next_level/c14_normative_source_integration.json
docs/next_level/c14_color_permutation_manifest.json
docs/next_level/c14_sector_tower_manifest.json
docs/next_level/c14_renormalization_trajectory.json
docs/next_level/c14_tensor_network_manifest.json
docs/next_level/c14_wilson_support_manifest.json
docs/next_level/c14_dyson_magnus_manifest.json
docs/next_level/c14_spectral_cut_manifest.json
docs/next_level/c14_soft_overlap_manifest.json
docs/next_level/c14_gauge_closure_report.json
docs/next_level/c14_explicit_induced_comparison.json
docs/next_level/c14_convergence_manifest.json
docs/next_level/c14_prediction_plan_manifest.json
```

Also update:

```text
handoff/ROADMAP.md
```

with:

- the final local commit;
- the exact supported/unsupported Wilson-order table;
- all unresolved physics gaps;
- the exact recommended next package.

All generated JSON must be deterministic, schema checked, and byte-identical when rebuilt from the same commit and environment.

---

# 23. Final acceptance criteria

C14/H7 is complete only when all of the following are true:

1. The exact C13 baseline reproduces before edits.
2. The H7 ten-sector state is implemented with nontrivial increasing tower dimensions.
3. `QQQGGG` has exactly 22 color singlets with the declared \(S_3\) decomposition.
4. Each sea–two-gluon sector has exactly 28 singlets with the declared 14/14 exchange split.
5. Complete quark antisymmetry and gluon bosonic symmetry close before operator assembly.
6. The ten-block Hamiltonian is Hermitian and its matrix-free and assembled actions agree.
7. Exact, Krylov, full-bond TTN, and variational TTN routes are compared.
8. The renormalization trajectory retains visible parameter flow and null directions.
9. Second-order quark support remains explicit and unchanged in meaning.
10. Second-order antiquark support is explicit through `QQQQ-QBAR-GG`.
11. Second-order active-gluon support is explicit through `QQQGGG`.
12. Wilson-order-three requests fail closed.
13. Strict Dyson and Magnus polynomials agree through order two in fundamental, anti-fundamental, adjoint, and two-link classes.
14. Path composition, reversal, and order-two unitarity defects close with cubic scaling.
15. The second-order cut ledger separates single and double cuts without squared deltas or physical epsilon.
16. Second-order soft-overlap cancellation closes separately for each representation/link geometry.
17. The finite gauge benchmark closes only with all declared pieces and is not mislabeled as full Slavnov–Taylor closure.
18. Complete quark, antiquark, and gluon order-resolved helicity/tensor parents are generated.
19. Sivers and Boer–Mulders remain distinct projections of one kernel.
20. Gluon ordered links and \(f/d\) channels remain independent.
21. Explicit-versus-induced comparison uses transformed operators and retains a visible remainder.
22. Full-bond TTN reproduces exact second-order observables.
23. Reduced-bond loss of a Wilson-sensitive feature is visible and reported.
24. Every required convergence axis is reported separately.
25. The assumption compiler rejects incompatible branches and unsupported orders.
26. All C14 negative injections are detected with stable diagnostics.
27. Every prior regression and immutable artifact remains unchanged.
28. No physical, matched, nuclear, evolution, process, inference, or production readiness is claimed.
29. All documentation and machine-readable manifests are complete and deterministic.
30. A clean local commit is created and not pushed.

Do not declare C14 complete unless every criterion above is satisfied.

---

# 24. Expected final response

The final Codex response must report concisely but quantitatively:

- starting and final commits;
- clean working-tree and push status;
- complete test/builder/evidence/atlas counts;
- requirement and injection counts;
- H7 tower dimensions;
- exact color multiplicities and permutation residuals;
- Hamiltonian, Krylov, TTN, and renormalization residuals;
- second-order support table for \(q,\bar q,g\);
- Dyson/Magnus residuals by representation;
- spectral, cut-ledger, soft-overlap, color, and gauge residuals;
- explicit-versus-induced remainder norms;
- all preserved immutable artifacts;
- unresolved matching, nuclear, evolution, process, and inference gates;
- the exact recommended next package.

The expected next package, if all H7 gates pass, is:

> **C15/N0 — matched spin-1 nuclear light-front state and microscopic deuteron GTMD composition**, beginning with a normalized `NN` spin-1 state, Hamiltonian-consistent one- and two-body operators, complete nucleon helicity-matrix exports, correlated proton/neutron microscopic members, and a strict separation between partonic Wilson rescattering and coherent nuclear propagation.

If H7 reveals an essential unresolved second-order support or gauge-completion defect, the final response must instead identify the exact microscopic package required before nuclear composition. Do not force the roadmap to N0 merely because it was anticipated.
