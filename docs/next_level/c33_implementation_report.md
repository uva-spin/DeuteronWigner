# C33/S0 implementation report

## Outcome

C33 creates the distinct validation root
`C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT`. Its baryon number is exactly
zero, and it shares neither a state vector nor a probability normalization
with the baryon-number-one C32 collinear root
`C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION`. The vacuum soft factor is therefore
not a component of the historical C11 proton state.

The primary realization plan is frozen as `S0-FB-EIKONAL-FOCK`: a direct
vacuum plus one-soft-gluon basis with four nondynamical eikonal color sources.
The B=0 root, vacuum normalization, basis schema, four-line operator, singlet
color trace, and tree identity close structurally. In particular,

\[
S_{\rm FB}^{(0)}(b)=\frac{1}{N_c}\operatorname{Tr}\mathbf 1=1,
\qquad C_F=\frac{4}{3}.
\]

No regulator-specific one-loop matrix element has been calculated. Every
one-loop soft coefficient and counterterm remains `NONZERO_UNKNOWN`; the
continuum papers are target or methodological oracles only. UV and rapidity
renormalization, the finite-basis trajectory and conversion, the C32/C33
regulator compatibility test, and the zero-bin validation therefore remain
open. The exact outcome is:

```text
C33_SOFT_TREE_LEVEL_ONLY
```

The C32 continuation gate is false. The exact next package is:

> **C34/S0A — one-loop soft diagram, counterterm, and rapidity-renormalization completion**

## Baseline and integrity

The authoritative starting commit is
`0d7b94a5e86882b23a56d4c1f11900d554756a18`; the required C28 scientific
ancestor is `52678312906bf5cc0bb8664e2486d5d676a6b723`.

The pre-C33 record contains 1,167 passing tests and passing C28, C29, C30,
C31, and C32 validators. It also records 32 C32 builders, 38/38 evidence rows,
164/164 atlas pages, 1,940 C32 requirements, 1,840/1,840 C32 injections, and
88 named C32 fault modes. These are baseline counts, not post-C33 counts.

The completed pre-Volume-XXI C33 record contains 1,196 passing tests, 33
builders, 39/39 evidence rows, 165/165 atlas pages, 2,140 C33 requirements,
2,040/2,040 C33 negative injections, and 92 named C33 fault modes.

## Post-completion Volume XXI integration

The subsequently supplied normative source is preserved byte-for-byte as
`references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex`
with SHA-256
`613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4`.
All 65 stable `V21.*` requirements are extracted in source order and mapped to
explicit C31, C32, and C33 evidence in
`docs/next_level/c33_volume_xxi_requirement_crosswalk.json`.
The integration also records Volume XXI's 18 benchmark families
`XXI-A`--`XXI-R`, 53 formal acceptance criteria, and minimum 2,040 ordered
negative-test contract separately from the original 2,140 C33 package
requirements.

The post-integration repository record contains 1,197 passing tests. The C33
builder and validator now hash-audit Volume XXI and enforce the complete
crosswalk without changing the 2,140 C33 package-requirement count or any
scientific output.

The mapping distinguishes requirements closed at the declared C33 structural
scope, requirements satisfied by an explicit fail-closed status, and
requirements that remain assigned to C34 or later stages. It does not convert
an unavailable one-loop value into a completed result. Volume XXI independently
confirms the two-root architecture, the exact tree boundary, the prohibition on
placing the soft vacuum inside proton normalization, and the admissibility of
the `C33_SOFT_TREE_LEVEL_ONLY` branch. It therefore leaves the continuation
gate false and C34/S0A unchanged.

Historical C11 remains a `REGULATED_MODEL_DENSITY`; C32 remains its distinct
operator-completion descendant and retains the exact twelve-parent tree
reduction. The frozen bridge roles and holdouts, `NO_JOINT_MEASURE`, all 642
ART25 member identities and source covariance, the 216-route registry, and
all eight authoritative artifacts remain outside the C33 soft calculation.
`MSHT20_REP/` is untouched and outside Git.

## Structural soft root

The implementation anchor is
`src/deuteron_wigner/bridge/s0/core.py`. Its records are frozen,
content-addressed, and serialized canonically. The structural contract has:

- a B=0 vacuum root and unit-normalized `|Omega>` state;
- a vacuum-plus-one-gluon mode schema carrying both `n` and `nbar` rapidity
  regions, transverse indices, polarization, adjoint color, boundary identity,
  normalization, and explicit zero-mode status;
- three nested resolution records with the exact support and dimensions shown
  below;
- exact zero modes excluded from the ordinary cells but retained as a separate
  unresolved control and holdout rather than a silent zero;
- no fixed-total-K baryon constraint and no proton-state membership.

The structural dimensions count one vacuum plus two rapidity regions times the
energy, rapidity, and transverse cells, two transverse polarizations, and eight
adjoint colors:

| Rank | `(N_omega,N_y,N_perp)` | `(omega_min,omega_max,Y_max,L_perp,rho_0)` | `dim(H_soft^(1))` |
| --- | --- | --- | --- |
| 1 | `(4,6,5)` | `(0.01,4,3,8,0.001)` | 3,841 |
| 2 | `(8,12,10)` | `(0.005,8,6,16,0.0005)` | 30,721 |
| 3 | `(12,18,15)` | `(0.0033333333333333335,12,9,24,0.0003333333333333333)` | 103,681 |

The boundary tuple is
`FINITE_CELL/PERIODIC/TRANSVERSE_CLOSED/COVARIANT`, and the zero-mode policy is
`EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL` with `AUDIT_REQUIRED`. These resolutions establish a
deterministic basis-trajectory contract. They do not constitute an evaluated
continuum trajectory, an interacting-Hamiltonian completeness result, or
one-loop data.

The four stored Wilson paths are, in trace order,
`S_n^dagger(b)`, `S_nbar(b)`, `S_nbar^dagger(0)`, and `S_n(0)`. Fundamental and
anti-fundamental actions, `P`/`ANTI_P` ordering, future orientation,
lightlike/infinity segments, transverse closure, the `1/N_c` singlet
projector, line conjugation, and path order are explicit. Removing a line,
conjugate action, ordering record, or transverse closure fails closed.

The modified-delta record keeps `delta+` and `delta-` distinct and derives the
eikonal delta and `i0` signs from Wilson orientation, Fourier convention,
momentum flow, covariant-derivative sign, and line conjugation. The finite basis
is explicitly forbidden from masquerading as the rapidity regulator. This is a
sign and identity contract, not a one-loop rapidity-renormalization result.

## One-loop fail-closed result

The runtime ledger contains explicit slots for all eighteen required classes:

```text
N_NBAR_EXCHANGE
CONJUGATE_LINE_EXCHANGE
SAME_DIRECTION_LINE_EXCHANGE
REAL_ONE_SOFT_GLUON
VIRTUAL_ONE_SOFT_GLUON
WILSON_LINE_SELF_ENERGY
CUSP_ENDPOINT
TRANSVERSE_CLOSURE
AUXILIARY_FIELD_SELF_ENERGY
SOFT_VACUUM_ENERGY
LIGHT_FRONT_INSTANTANEOUS
GAUGE_FIXING
GHOST
ZERO_MODE
BASIS_BOUNDARY
RAPIDITY_COUNTERTERM
UV_COUNTERTERM
RESIDUAL_LINE_MASS_COUNTERTERM
```

Each entry is `STRUCTURALLY_UNRESOLVED`, blocking, and has expression
`NONZERO_UNKNOWN`. This is not a declaration that any graph vanishes. It means

\[
S_{\rm FB}^{\rm bare}
=1+a_s\,\mathrm{NONZERO\_UNKNOWN}+\mathcal O(a_s^2).
\]

The UV counterterm, rapidity counterterm, renormalized soft factor, rapidity
anomalous dimension, Collins-Soper kernel, finite-basis-to-continuum conversion,
gauge residuals, rapidity residuals, inverse conversion, and round-trip residual
are consequently unavailable rather than zero. The basis trajectory status is
`SOFT_TRAJECTORY_UNAVAILABLE`.

The auxiliary-field route is retained as `SOURCE_ORACLE_ONLY`. It is neither
proved Minkowski/light-front and modified-delta equivalent nor added to the
direct result. The modified-delta continuum result is also
`SOURCE_ORACLE_ONLY` and is never labeled a finite-basis evaluation.

## Soft-collinear and zero-bin interface

The typed regulator pair connects the C32 B=1 and C33 B=0 roots without
sharing their state spaces. Wilson geometry and b-space measurement can be
compared structurally. The one-loop rapidity-regulator and overlap checks cannot
close without the missing finite-basis matrix elements, so the exact status is

```text
SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED
```

The map

\[
\operatorname{ZERO\_BIN}:\operatorname{COLL}_{\rm C32}
\longrightarrow\operatorname{SOFT\_LIMIT}_{\rm C33}
\]

has a typed, count-once interface, but its status is
`DEFINED_NOT_VALIDATED`: C32 one-loop collinear coefficients do not exist and
the common-off-shell IR implementation has not been shown equivalent to the
C33 soft limit. The zero-bin gate and the C32 continuation gate are false.

This qualification is essential because arXiv:hep-ph/0702022 proves the
soft/zero-bin equivalence for the examples studied when dimensional
regularization regulates the IR and explicitly warns that off-shellness does
not preserve that equivalence. C32 freezes spacelike off-shell partonic IR
states, so C33 requires a new operator-identical calculation or a proved
conversion; the paper cannot close the interface by citation.

## Primary-source locks

Four C31 source locks are reused byte-for-byte:

```text
arXiv:1511.05590v2  data/raw/c31_sources/1511.05590.pdf
dda565928e2a52997da094a156b286b31741184e47398d2efaa801a9a97e573d

arXiv:1604.07869v3  data/raw/c31_sources/1604.07869.pdf
11013c71a5ef19d7aadc85469cf509f0481f3df4207cf40f5da89321f1c73c93

arXiv:1707.07606v2  data/raw/c31_sources/1707.07606.pdf
ea49b6eb8309341084b0ee7d9a14e57ee000112f0497260b5d1f68e386877367

arXiv:1202.0814v2   data/raw/c31_sources/1202.0814.pdf
866b388227d1f78f757c0ab82bf199721a81a2efc522f79eafe512e5dd4a9173
```

Seven additional public PDFs are preserved under `data/raw/c33_sources/` and
remain outside Git:

```text
arXiv:1604.00392v1  1604.00392.pdf
6a0cd0f3c64d06c69a09c62151196113650daee09b4953b948b420cb5af364e9

arXiv:1612.07740v1  1612.07740.pdf
c7cf8b1ae96a42f4ac47739c675ee25b64735eea85e3d358f1132e9adf626aa2

arXiv:1711.00543v1  1711.00543.pdf
2fe48ae02205ab71a15022b64894119bf63953f7c5da80e5f1475a617b41bab3

arXiv:2002.09408v2  2002.09408.pdf
5e328c3cd67cdffb99aead25513e60cbb05f4a30f002475a17fe9026e197b3d8

arXiv:2312.04315v3  2312.04315.pdf
171278778c2d5f8da64f46119dbeb417a23f305ccb4512ba229ff172ea651d75

arXiv:2412.12645v1  2412.12645.pdf
c95b8dc6175eb7315607f348c19b5c68de779291a79c49bc3cae85d726695e12

arXiv:hep-ph/0702022v1  hep-ph-0702022.pdf
6e310c86c8c315ee57dcf7c1d14ec3a057164f7bac1f10ead474fb66c6fcd96f
```

## Source relevance and locators

The source classifications describe authority for the continuum target or a
method. Every paper is `NOT_OPERATOR_REGULATOR_IDENTICAL` to the direct C33
finite-basis root. In particular, operator/modified-delta agreement at the
continuum level does not provide the absent finite-basis sum, counterterms, or
trajectory.

| Source | Classification and authoritative locator | C33 use and limit |
| --- | --- | --- |
| Echevarria, Scimemi, Vladimirov, *The Universal Transverse Momentum Dependent Soft Function at NNLO*, arXiv:1511.05590v2 | `TARGET_SOFT_FUNCTION_AUTHORITY`, `RAPIDITY_RENORMALIZATION_AUTHORITY`; PDF p.2 Eq. (1), p.3 Eqs. (3)-(6), p.5 Eqs. (9)-(13), p.8 Eqs. (23)-(27) | Four-line vacuum definition, modified-delta damping/ordered poles, continuum NLO coefficient, and D-function convention; dimensional continuum oracle only. |
| Echevarria, Scimemi, Vladimirov, *Unpolarized Transverse Momentum Dependent Parton Distribution and Fragmentation Functions at next-to-next-to-leading order*, arXiv:1604.07869v3 | `TARGET_SOFT_FUNCTION_AUTHORITY`, `ZERO_BIN_AUTHORITY`; PDF pp.4-6 Eqs. (2.1)-(2.8), pp.10-12 Eqs. (3.1)-(3.10), pp.12-13 Eqs. (3.16)-(3.17) | TMD operator, `R_f`, modified-delta `Z_b=S`, soft allocation, ordered poles, and x/1-z collinear rescaling; no C33 finite-basis matrix element. |
| Vladimirov, *Structure of rapidity divergences in soft factors*, arXiv:1707.07606v2 | `RAPIDITY_RENORMALIZATION_AUTHORITY`; PDF pp.4-8 Eqs. (2.3)-(3.11), pp.10-11 Eqs. (4.1)-(4.3), Sec. 5 from p.14, Sec. 6.2 from p.23 | Singlet Wilson geometry, exponentiation, and rapidity-renormalization theorem; theorem does not supply the regulator-specific finite-basis coefficient. |
| Chiu, Jain, Neill, Rothstein, *A Formalism for the Systematic Treatment of Rapidity Logarithms in Quantum Field Theory*, arXiv:1202.0814v2 | `RAPIDITY_RENORMALIZATION_AUTHORITY`, `ZERO_BIN_AUTHORITY`; PDF pp.12-16 Eqs. (4.7)-(4.30) | Eta/nu RRG, regulator-removal order, consistency, and cusp relation; a distinct rapidity scheme, not modified delta. |
| Li, Neill, Zhu, *An Exponential Regulator for Rapidity Divergences*, arXiv:1604.00392v1 | `FINITE_REGULATOR_METHOD_AUTHORITY`, `RAPIDITY_RENORMALIZATION_AUTHORITY`; PDF pp.7-8 Eqs. (14)-(16), pp.11-12 Eqs. (36)-(39), pp.15-16 Eqs. (50)-(58) | Gauge-invariant energy/Laplace regulator and RRG consistency check; it is not the C33 modified-delta regulator. |
| Idilbi, Mehen, *On The Equivalence of Soft and Zero-Bin Subtractions*, arXiv:hep-ph/0702022v1 | `ZERO_BIN_AUTHORITY`; PDF pp.4-6 and Eq. (12), pp.10-12 Eqs. (35)-(49) | Count-once and one-loop integrand equivalence in pure DR; PDF p.4 expressly excludes off-shell IR as an automatic equivalence proof. |
| Francis, Kanamori, Lin, Morris, Zhao, *The lattice extraction of the TMD soft function using the auxiliary field representation of the Wilson line*, arXiv:2312.04315v3 | `AUXILIARY_FIELD_METHOD_AUTHORITY`, `FINITE_REGULATOR_METHOD_AUTHORITY`; PDF pp.4-7 Eqs. (6)-(27) | Complex Euclidean directions, one-loop spacelike result, `|r_a|,|r_b|>1`, finite-line ratio, and one-dimensional field representation; Collins spacelike/lattice scheme, not lightlike modified delta. |
| Francis, Kanamori, Lin, Morris, Zhao, *Measurement of the TMD soft function on the lattice using the auxiliary field representation of the Wilson line*, arXiv:2412.12645v1 | `AUXILIARY_FIELD_METHOD_AUTHORITY`, `FINITE_REGULATOR_METHOD_AUTHORITY`; PDF pp.3-6 Eqs. (1)-(16) | Exploratory lattice implementation, spacelike rapidity map and finite-line ratio; methodological measurement, not a C33 coefficient. |
| Green, Jansen, Steffens, *Improvement, generalization, and scheme conversion of Wilson-line operators on the lattice in the auxiliary field approach*, arXiv:2002.09408v2 | `AUXILIARY_FIELD_METHOD_AUTHORITY`, `FINITE_REGULATOR_METHOD_AUTHORITY`; PDF pp.1-2 Eqs. (1)-(14), p.9 Eqs. (47)-(50) | Auxiliary action, residual-mass/line renormalization, local endpoints, piecewise paths and cusps; Euclidean lattice-to-MS conversion is not C33 soft conversion. |
| Constantinou, Panagopoulos, *Perturbative Renormalization of Wilson line operators*, arXiv:1711.00543v1 | `FINITE_REGULATOR_METHOD_AUTHORITY`; PDF pp.1-2 Eq. (1), pp.5-6 Eqs. (9)-(14) | Warns that finite-cutoff Wilson lines can contain linear, logarithmic, and finite renormalization pieces; concerns lattice nonlocal fermion operators, not the four-line TMD soft operator. |
| Reinhardt, *The Wilson loop in light-front quantization*, arXiv:1612.07740v1 | `LIGHT_FRONT_VACUUM_COMPARISON_ONLY`; PDF pp.1-2, pp.10-13 (especially Eq. (76) and the static-limit discussion) | Shows LF path ordering, zero-mode caveats, and order-of-limits sensitivity in QED; not QCD, not a TMD soft function, and not a modified-delta calculation. |

The audit therefore supports the structural root, sign conventions, source
oracle, and exact no-go. It does not support importing any published continuum
or lattice value as `S_FB^(1)`.

## Isolation and reproduction

`tests/test_c33_s0.py` exercises the B=0/B=1 separation, frozen-record
immutability, basis and zero-mode guards, four-line/color/tree identities,
derived modified-delta signs, explicit fail-closed one-loop ledger, oracle
non-promotion, compatibility and continuation gates, deterministic
serialization, and negative-injection dispatch. `scripts/build_c33_manifests.py`
is the deterministic artifact builder and `scripts/validate_c33.py` is the C33
integrity validator.

Use the final pytest total supplied by the builder in place of the marked
token:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c33_s0.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c33_manifests.py 1197
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c33.py
```

No ART25 member, data point, chi2 value, bridge residual, or proton-level ratio
entered the root or its gates. C33 creates no microscopic proton TMD export and
does not rerun the twelve-point bridge. No fit, calibration, optimization,
reweighting, likelihood, posterior, emulator, process bridge, or physical,
deuteron, inference, or production status is created.
