# C31/B1A Codex Work Package

## Title

**Microscopic light-front-to-TMD renormalization, soft/rapidity subtraction, and finite ART25 scheme-adapter source closure**

## Authoritative baseline

Start from the local C30/B1 completion commit:

```text
aea2f21db0e432be3927895a56ac623b68445534
```

This commit must retain the integrated C29/B0 and Volume XX bridge geometry in its ancestry. The required C28/P1D scientific ancestor is:

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when the complete C30 baseline reproduces before any scientific change. Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote. Keep the pre-existing untracked `MSHT20_REP/` directory untouched and outside Git while redistribution permission remains unresolved. Do not push the final completion commit.

---

# 1. Why C31/B1A is the exact next package

C30 establishes the exact external ART25 definition and the exact microscopic capability boundary for the frozen rank-zero proton bridge.

The external ART25 object is executable and source audited:

```text
harpy.get_uTMDPDF(x, b, 1, mu, zeta, includeGluon=False)
```

with:

```text
returned scalar: f, not x f
vector order: (bbar,cbar,sbar,ubar,dbar,gluon,d,u,s,c,b)
u=7, d=6, ubar=3, dbar=4
mu=Q, zeta=Q^2
inverse rank-zero Fourier kernel: integral b db J0(kT b)/(2 pi)
```

The microscopic plan is frozen as `C11_PRIMARY_WITH_LATER_LEVELS_AS_CONVERGENCE_AXES`, and the bridge direction is `B1-SCHEME-ART25`.

The twelve frozen rank-zero proton points—three each for `u`, `d`, `ubar`, and `dbar`—have a nonempty kinematic intersection but an empty executable-definition intersection. C30 records:

```text
12 BRIDGE_COMMON_DOMAIN_ONLY
0 BRIDGE_DISTRIBUTION_COMPARISON_READY
adapter status SOURCE_EXPRESSION_UNAVAILABLE
adapter remainder NONZERO_UNKNOWN
external bridge shape 642 x 0
```

The empty projection is not a zero physical distribution.

The missing physics is not one generic factor. It contains two distinct maps:

```text
A. MICROSCOPIC_LF_TO_SUBTRACTED_TMD_MATCHING

   finite-basis light-front overlap/operator
       -> UV-renormalized, rapidity-renormalized,
          soft-subtracted TMD in a declared project scheme

B. RENORMALIZED_PROJECT_TO_ART25_ADAPTER

   declared project renormalized TMD
       -> exact ART25/arTeMiDe operator convention and scale prescription
```

C31 must source-audit and, where genuinely possible, construct both maps separately. It must not hide the absence of map A by proving only a relation among already-renormalized continuum TMD schemes.

---

# 2. Primary objective

Implement the chain:

```text
C11 regulated Wilson-order-zero rank-zero proton parent
    -> exact microscopic bare/operator definition
    -> exact regulator and counterterm identity
    -> explicit Wilson-line status
    -> UV renormalization
    -> zero-bin/overlap subtraction
    -> soft-factor subtraction
    -> rapidity renormalization
    -> LF-regulator-to-renormalized-project-TMD matching
    -> declared project TMD at (mu,zeta)
    -> finite project-to-ART25 convention adapter
    -> ART25 optimal/ζ-prescription scale map
    -> common source-qualified bridge object
    -> conditional C30 bridge rerun
```

Answer independently:

1. Does a source-supported, operator-identical renormalization and soft/rapidity subtraction map exist for the C11 finite-basis correlator?
2. Is the project renormalized TMD identical to, finitely related to, or incompatible with the ART25 convention?
3. Which parts are operator-scheme transformation, rapidity convention, finite hard/TMD redistribution, ζ-prescription scale choice, ordinary two-scale evolution, or nonperturbative boundary-model difference?
4. Can the twelve frozen points acquire a source-qualified microscopic vector without fitting any normalization or shape to ART25?

Do not force a positive bridge count.

---

# 3. Scientific boundary

C31 is source-audited, operator- and regulator-specific, UV/rapidity/soft explicit, finite-order explicit, rank-zero, T-even, proton-target, quark/positive-x-antiquark resolved, b-space first, validation-only, and non-inferential.

C31 is not a fit, calibration, phenomenological ratio correction, pointwise normalization, likelihood, posterior, reweighting, optimization, emulator, physical extraction, process prediction, deuteron prediction, gluon/T-odd adapter, or production promotion.

A relation between two continuum renormalized TMD schemes does not renormalize a finite-basis overlap. Tree-level Wilson identity does not establish a source-qualified physical TMD.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Read all relevant C5-C31 operator, Wilson, microscopic, matching, evolution, source, bridge, formal-volume, API, manifest, test, ADR, and roadmap files before changes. Continue autonomously until every applicable acceptance criterion is satisfied.

Do not stop for approval to inspect source/history, preserve primary papers, inspect ARTEMIDE v3.01, inspect C19-C22, inspect C11-C14, construct symbolic/numerical partonic oracles, derive source-supported conversions, run UV/rapidity/RG/threshold/gauge checks, or conditionally execute the twelve-point bridge.

Do not contact authors, alter ARTEMIDE/ART25, alter microscopic Hamiltonians or C11, fit an adapter, use bridge residuals to choose a scheme, add normalization, construct inference, reweight members, promote readiness, modify production, or push.

---

# 5. Normative repository sources

Read completely and hash-audit at least:

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c6_implementation_report.md
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c11_regression_report.json
docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md

docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c19_matching_basis.json
docs/next_level/c19_matching_fit_manifest.json
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_coefficient_library.json
docs/next_level/c20_matching_fit_manifest.json
docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_anomalous_dimension_library.json
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_multiq_grid.json
docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_smallb_capability_matrix.json
docs/next_level/c22_m3_multiq_capability_matrix.json
docs/next_level/c22_accuracy_manifest.json

docs/next_level/c25_art25_reproduction_source_plan.json
docs/next_level/c25_art25_member_schema.json
docs/next_level/c27_art25_joint_member_map.json
docs/next_level/c27_distribution_reproduction_manifest.json
docs/next_level/c28_implementation_report.md
docs/next_level/c28_theory_ensemble_factor_manifest.json
docs/next_level/c28_lowqt_source_reproducibility_contract.json
docs/next_level/c29_implementation_report.md
docs/next_level/c29_operator_crosswalk.json
docs/next_level/c29_scheme_scale_adapter_manifest.json
docs/next_level/c29_frozen_bridge_grid.json
docs/next_level/c29_discrepancy_interface.json
docs/next_level/c29_constraint_role_split.json
docs/next_level/c30_implementation_report.md
docs/next_level/c30_api.md
docs/next_level/c30_art25_tmd_definition_manifest.json
docs/next_level/c30_art25_flavor_convention_manifest.json
docs/next_level/c30_art25_scale_scheme_trace.json
docs/next_level/c30_microscopic_tmd_definition_manifest.json
docs/next_level/c30_microscopic_source_plan.json
docs/next_level/c30_bridge_scheme_selection.json
docs/next_level/c30_finite_scheme_adapter_library.json
docs/next_level/c30_common_bridge_domain.json
docs/next_level/c30_distribution_bridge_capability_matrix.json
docs/next_level/c30_unresolved_physics_gaps.md

references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/volume_xix_source_qualified_process_inputs.tex
references/volume_xx_source_reproducible_bridge_geometry.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

The Volume XVI PDF is normative. If its TeX source remains absent, record that absence and do not invent it.

Create `docs/next_level/c31_normative_source_integration.json`.

---

# 6. Required primary-source audit

Preserve used papers/packages under `data/raw/c31_sources/` with exact versions and SHA-256 hashes. Audit at least:

```text
arXiv:1111.4996   low-qT factorization and TMD definition
arXiv:1210.2100   equality of EIS and Collins definitions
arXiv:1511.05590  universal soft function and modified-delta regulator
arXiv:1604.07869  unpolarized TMD renormalization/matching through NNLO
arXiv:1707.07606  rapidity-renormalization theorem
arXiv:1706.01473  ζ-prescription and arTeMiDe convention
arXiv:1803.11089  double-scale evolution and optimal TMD
arXiv:1705.07167  relations among CSS, Collins, and SCET formalisms
arXiv:1202.0814   rapidity renormalization group
arXiv:1602.01829  rapidity-renormalized soft/beam functions
arXiv:2503.11201v2 ART25 source convention
arXiv:2205.04714  BLFQ proton T-even overlap calculation
arXiv:1911.03840  regulator-specific LaMET-to-TMD factorization
arXiv:2201.08401  continuum/lattice TMD scheme relation
```

LaMET and BLFQ sources are methodology/comparison references, not direct C11 matching unless operator and regulator identity genuinely match.

Classify each source as `DIRECT_OPERATOR_AUTHORITY`, `CONTINUUM_SCHEME_RELATION_AUTHORITY`, `REGULATOR_MATCHING_METHODOLOGY`, `MODEL_OVERLAP_COMPARISON_ONLY`, or `IRRELEVANT_TO_REQUIRED_ADAPTER`.

Create:

```text
docs/next_level/c31_primary_source_manifest.json
docs/next_level/c31_source_relevance_matrix.json
```

---

# 7. Immutable C30 baseline

Before edits reproduce:

```text
1,149 tests
30 builders
36/36 evidence rows
162/162 atlas pages
1,600 requirements
1,520/1,520 injections
C28/C29/C30 validators
deterministic JSON regeneration
12 frozen points: 3 each u,d,ubar,dbar
12 BRIDGE_COMMON_DOMAIN_ONLY
0 BRIDGE_DISTRIBUTION_COMPARISON_READY
C11_PRIMARY_WITH_LATER_LEVELS_AS_CONVERGENCE_AXES
B1-SCHEME-ART25
SOURCE_EXPRESSION_UNAVAILABLE
NONZERO_UNKNOWN remainder
all 642 external identities
642 x 0 unavailable projection
15 convergence axes, no executable TMD convergence
13 discrepancies: 2 auditable, 11 NONZERO_UNKNOWN
216 production routes
eight authoritative artifacts byte-identical
```

Do not modify C11-C14 parents, C19-C22 historical records, frozen grid/roles, ART25 members, C28 covariance, C30 matrices in place, production, or artifacts.

---

# 8. Required architecture

Extend typed systems with immutable objects equivalent to:

```text
MicroscopicBareOperatorId
MicroscopicRegulatorId
MicroscopicCountertermId
MicroscopicWilsonCompletionId
UVRenormalizationRecord
SoftFactorDefinition
SoftSubtractionRecord
ZeroBinOverlapRecord
RapidityRegulatorRecord
RapidityRenormalizationRecord
PartonicExternalStateId
IRRegulatorRecord
PartonicMatrixElementRecord
PartonicMatchingCondition
PartonicMatchingOracle
LFToTMDMatchingId
LFToTMDMatchingKernel
LFToTMDMatchingRemainder
LFToTMDMatchingCapability
RenormalizedTMDSchemeId
RenormalizedTMDDefinition
FiniteTMDSchemeTransformation
HardFactorCompanionTransformation
ZetaPrescriptionRecord
OptimalTMDScaleMap
TwoScaleEvolutionMap
SchemeVersusScaleDecomposition
AdapterSourceTerm
AdapterSourceCoverage
AdapterSufficiencyDecision
C31BridgeExecutionGate
C31BridgeCapabilityMatrix
C31ClosureReport
```

Objects must be immutable, content addressed, deterministic, explicit about operator/regulator/UV/rapidity/soft/order/domain/remainder, independent of ART25 fit data, and unreachable from inference/production.

---

# 9. Three-layer identity decomposition

Represent separately:

```text
Layer I:  F_LF^reg
          C11 finite-basis overlap/operator; not a renormalized TMD.

Layer II: F_project(x,b;mu,zeta)
          UV/rapidity-renormalized, soft-subtracted project TMD.

Layer III:F_ART25^opt
          ARTEMIDE convention plus optimal/ζ-prescription scale map.
```

Required maps:

```text
F_project = Z_LF->project ⊗ F_LF^reg + R_LF->project
F_ART25   = Z_project->ART25 ⊗ F_project + R_project->ART25
```

Do not collapse these maps. Create `docs/next_level/c31_three_layer_identity_manifest.json`.

---

# 10. Microscopic bare-operator audit

Trace the C11 rank-zero object from code to stored scalar. Record bilocal/overlap operator, fields, spectators, Wilson content/order, gauge, basis/longitudinal/transverse/endpoint regulators, UV/IR cutoffs, state/operator normalization, antiquark convention, b transform, momentum, target, and flavor.

Classify it as:

```text
BARE_BILOCAL_OPERATOR_MATRIX_ELEMENT
GAUGE_FIXED_WAVEFUNCTION_OVERLAP
TREE_LEVEL_TMD_LIMIT
REGULATED_MODEL_DENSITY
OTHER
```

Audit whether C12-C14 add link-even Wilson, soft, or counterterm content relevant to rank-zero T-even structure. Wilson-order-zero future/past equality is not a physical subtracted TMD beyond tree level.

Create:

```text
docs/next_level/c31_microscopic_bare_operator_manifest.json
docs/next_level/c31_microscopic_regulator_manifest.json
docs/next_level/c31_microscopic_wilson_soft_audit.json
```

---

# 11. Renormalization-component ledger

For the microscopic-to-project map, create a complete ledger:

```text
quark field renormalization
bilocal operator UV renormalization
Wilson-line self energy
Wilson-line endpoint/cusp terms
soft factor
square-root soft allocation
zero-bin or overlap subtraction
rapidity regulator
rapidity counterterm
rapidity anomalous dimension
UV anomalous dimension
Hamiltonian/basis counterterms
regulator conversion
operator mixing
power corrections
```

For every component record requirement, current presence, source paper, locator, operator/regulator identity, implemented order, source status, numerical status, and blocking status.

Allowed statuses:

```text
SOURCE_COMPLETE
SOURCE_PARTIAL
PROJECT_VALIDATION_ORACLE_ONLY
ANALOGOUS_REGULATOR_ONLY
SOURCE_EXPRESSION_UNAVAILABLE
NOT_APPLICABLE_WITH_PROOF
```

Create:

```text
docs/next_level/c31_renormalization_component_ledger.json
docs/next_level/c31_source_sufficiency_matrix.json
```

No missing term may be silently called zero.

---

# 12. Project renormalized-TMD definition audit

Trace the exact project scheme declared by Volume XVI and C19-C22. Record:

```text
operator definition
Wilson staple
soft-factor definition
square-root allocation
rapidity regulator
UV scheme
rapidity scheme
mu/zeta convention
canonical line
CS-kernel convention
Fourier normalization
matching coefficients
hard-factor companion convention
threshold history
```

Distinguish:

```text
formal scheme declaration
implemented validation oracle
source-qualified executable object
physical covariance-bearing object
```

Formal equations do not prove that C11 has been matched into that scheme.

Create:

```text
docs/next_level/c31_project_tmd_definition_manifest.json
docs/next_level/c31_project_scheme_implementation_gap.json
```

---

# 13. ART25/arTeMiDe scheme audit

Trace the exact ART25 operator and scale convention from the ART25 paper, ARTEMIDE v3.01 source, constants, optimal-TMD implementation, ζ-prescription implementation, evolution source, matching source, and hard-factor source.

Separate:

```text
operator renormalization scheme
rapidity-renormalization scheme
soft-factor convention
MS-bar convention
optimal-TMD boundary definition
ζ-prescription scale curve
ordinary evolution to (mu,zeta)
nonperturbative FNP model
CS-kernel model
```

A ζ-prescription is not automatically a finite operator-scheme transformation.

Create:

```text
docs/next_level/c31_art25_operator_scheme_manifest.json
docs/next_level/c31_art25_optimal_scale_manifest.json
docs/next_level/c31_scheme_versus_scale_decomposition.json
```

---

# 14. Continuum scheme-equivalence audit

Use primary sources to determine the exact relation among Collins-style, EIS/modified-delta, ARTEMIDE, project square-root-soft, and relevant RRG/SCET TMD definitions.

For every pair record:

```text
operator equality
UV convention difference
rapidity convention difference
finite factor
hard-factor companion transformation
scale map
perturbative order
proof status
domain
source locator
```

If two definitions are equal after convention alignment, record:

```text
OPERATOR_SCHEME_IDENTICAL_AFTER_CONVENTION_ALIGNMENT
```

If the relation is only cross-section-level, do not promote it to individual-TMD equality.

If a finite factor Z is used, require cross-section invariance:

```text
H^SB F1^SB F2^SB = H^SA F1^SA F2^SA + O(a_s^(N+1))
```

Create:

```text
docs/next_level/c31_continuum_scheme_equivalence_matrix.json
docs/next_level/c31_hard_tmd_companion_transformation.json
```

---

# 15. Partonic matching strategy

A regulator-specific microscopic matching kernel may be established only through operator-identical partonic calculations or an all-order theorem explicitly covering the microscopic regulator.

Compile and select one strategy before bridge execution:

```text
P-A DIRECT_SOURCE
    A primary source gives the exact C11-regulator matching.

P-B REGULATOR_EQUIVALENCE
    A proved map identifies the C11 regulator with a covered regulator.

P-C PARTONIC_DIFFERENCE
    Compute the same partonic matrix element in:
        (i) the microscopic regulator/operator;
        (ii) the target renormalized TMD scheme;
    extract the IR-finite difference.

P-D TREE_LEVEL_ONLY
    Establish only the tree-level operator limit.

P-E UNAVAILABLE
    No scientifically complete route exists.
```

Create `docs/next_level/c31_lf_to_tmd_matching_strategy.json`.

---

# 16. Partonic external-state requirements

When using a partonic matching calculation, freeze:

```text
external quark momentum
spin/helicity
flavor
off-shellness or other IR regulator
gauge
UV regulator
rapidity regulator
basis regulator
Wilson direction
soft-factor convention
zero-bin convention
mu
zeta
```

The microscopic and continuum calculations must share the same IR regulator or have a proved IR conversion.

At each declared order include, where required:

```text
quark self energy
operator vertex
real emission
Wilson-line attachment
Wilson-line self energy
soft graph
zero-bin/overlap subtraction
UV counterterm
rapidity counterterm
Hamiltonian counterterm
instantaneous light-front terms
endpoint/basis regulator terms
```

Required tests:

```text
IR cancellation in matching difference
UV-pole cancellation after renormalization
rapidity-pole cancellation after subtraction
gauge-parameter independence
quark-number normalization
flavor universality where proven
quark/antiquark charge-conjugation relation
mu anomalous dimension
zeta anomalous dimension
threshold consistency
tree-level limit
```

Create:

```text
docs/next_level/c31_partonic_external_state_manifest.json
docs/next_level/c31_partonic_diagram_ledger.json
docs/next_level/c31_partonic_matching_oracle.json
```

---

# 17. Tree-level status discipline

At tree level, Wilson line -> identity, soft factor -> 1, UV factor -> 1, and rapidity factor -> 1 may hold for a declared partonic benchmark.

This permits at most:

```text
TREE_LEVEL_OPERATOR_LIMIT_VALIDATED
```

unless the finite-basis regulator, normalization, and power corrections are also source qualified.

Tree-level identity must not automatically issue:

```text
MICROSCOPIC_RENORMALIZED_TMD_READY
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

The first omitted order and nonzero-unknown remainder remain visible.

Create `docs/next_level/c31_tree_level_limit_report.json`.

---

# 18. LF-to-project matching kernel

Only when the selected strategy passes, implement:

```text
F_project_q(x,b;mu,zeta)
  = sum_j integral_x^1 dz/z
      Z_LF->project_(q<-j)(x/z,b;Lambda_LF,mu,zeta)
      F_LF,reg_j(z,b;Lambda_LF)
    + R_q
```

Every kernel record must contain source/target operator, microscopic regulator, external-state IR regulator, partonic channel, flavor structure, implemented and omitted orders, distributional terms, UV/rapidity/basis logs, mixing, source or derivation hash, domain, power corrections, and remainder.

The kernel must be state independent. It must not be obtained by dividing ART25 hadron values by microscopic hadron values.

Create:

```text
docs/next_level/c31_lf_to_project_matching_library.json
docs/next_level/c31_lf_to_project_matching_remainder.json
docs/next_level/c31_lf_matching_capability_matrix.json
```

---

# 19. Project-to-ART25 adapter

After both objects are renormalized TMDs, implement:

```text
F_ART25_q = Z_project->ART25_q ⊗ F_project_q + R_scheme_q
```

Factor the map into:

```text
operator-scheme conversion
MS-bar convention alignment
rapidity-scheme conversion
soft-factor finite redistribution
hard-factor companion conversion
scale relocation
ζ-prescription map
ordinary two-scale evolution
threshold map
```

Do not combine these into one opaque multiplier.

Required checks:

```text
Z_A->B ⊗ Z_B->A = 1 + O(a_s^(N+1))
hard x TMD x TMD cross-section invariance
mu RG consistency
zeta RG consistency
CS-kernel convention consistency
threshold round trip
flavor/antiquark relations
source/member independence
```

Create:

```text
docs/next_level/c31_project_to_art25_adapter_library.json
docs/next_level/c31_project_to_art25_roundtrip_report.json
docs/next_level/c31_project_to_art25_rg_report.json
docs/next_level/c31_project_to_art25_remainder.json
```

---

# 20. Adapter independence from ART25 fit data

The adapter is an operator-level perturbative object. It must not depend on:

```text
ART25 Lambda member
ART25 FNP parameters
MSHT20_REP member
MAPFF member
the 1,209 ART25 data points
the ART25 chi2
the twelve bridge residuals
```

Required checks:

- same adapter for all 642 members;
- same light-quark adapter where universality is proven;
- no point-dependent normalization;
- no x/b/Q spline fitted to source members;
- no calibration/holdout use in construction.

Create `docs/next_level/c31_adapter_independence_report.json`.

---

# 21. Conditional microscopic renormalized export

Only if the LF-to-project matching gate passes, export `u`, `d`, `ubar`, and `dbar` at the twelve frozen points through:

```text
C11 parent
    -> LF-to-project matching
    -> project renormalized TMD
    -> project-to-ART25 adapter
    -> ART25 (mu=Q,zeta=Q^2) convention
```

Every output retains microscopic plan, resolution, Fock content, Wilson order, operator, regulator, matching kernel, renormalization record, soft/rapidity record, scheme adapter, scale map, flavor, point, value, and all remainders.

No free normalization is permitted.

Create:

```text
docs/next_level/c31_microscopic_renormalized_tmd_export.json
docs/next_level/c31_microscopic_renormalized_execution_report.json
```

When the gate fails, create deterministic empty-coordinate records rather than zero-valued TMDs.

---

# 22. Conditional C30 bridge rerun

Only when both maps pass:

```text
MICROSCOPIC_LF_TO_SUBTRACTED_TMD_MATCHING
RENORMALIZED_PROJECT_TO_ART25_ADAPTER
```

rerun the C30 bridge on the immutable twelve-point grid.

Preserve all 642 external members, covariance rank and null space, C29/C30 roles and holdouts, `NO_JOINT_MEASURE`, data ancestry, no-double-counting plan, and discrepancy separation.

Allowed diagnostics remain pointwise/relative residuals, member percentiles, whitened residuals, null-space residuals, and convergence summaries. They are not likelihoods or probabilities.

Create:

```text
docs/next_level/c31_distribution_bridge_rerun.json
docs/next_level/c31_distribution_bridge_capability_matrix.json
docs/next_level/c31_distribution_bridge_closure_report.json
```

Do not modify C30 historical matrices.

---

# 23. Remainder and uncertainty discipline

Keep separate:

```text
microscopic regulator power correction
LF-to-project matching truncation
soft-subtraction truncation
rapidity-renormalization truncation
project-to-ART25 finite conversion truncation
two-scale evolution truncation/path ambiguity
threshold uncertainty
C11/C14 parent/Fock difference
Wilson-order truncation
basis and TTN truncation
large-b boundary difference
external ART25 covariance
external model discrepancy
numerical integration
```

Unknown remains `NONZERO_UNKNOWN`. No remainder may be absorbed into ART25 covariance, and no scheme remainder may be estimated from cross-root hadron residuals.

Create:

```text
docs/next_level/c31_adapter_remainder_budget.json
docs/next_level/c31_adapter_uncertainty_separation.json
```

---

# 24. Source sufficiency and no-go records

C31 must support a scientifically useful negative result.

When no source or derivation covers the C11 operator/regulator, issue:

```text
NO_SOURCE_QUALIFIED_LF_TO_TMD_MATCHING
```

with an exact missing-calculation specification:

```text
required bare operator
required regulator
required partonic external state
required diagrams
required counterterms
required soft and rapidity factors
required matching conditions
required convergence trajectory
```

When continuum scheme equivalence closes but microscopic matching does not, record:

```text
PROJECT_TO_ART25_ADAPTER_READY
MICROSCOPIC_LF_TO_TMD_MATCHING_UNAVAILABLE
BRIDGE_STILL_COMMON_DOMAIN_ONLY
```

Create:

```text
docs/next_level/c31_source_sufficiency_decision.json
docs/next_level/c31_missing_calculation_specification.md
```

---

# 25. Holdouts

Freeze holdouts before symbolic or numerical adapter construction. Reserve at least:

```text
one UV-pole coefficient
one rapidity-pole coefficient
one soft-factor constant
one x-space distributional term
one Mellin moment
one mu-evolution point
one zeta-evolution point
one threshold-crossing point
one inverse/round-trip point
one gauge-parameter cancellation
one quark/antiquark relation
one u bridge point
one d bridge point
one ubar bridge point
one dbar bridge point
one small-b point
one large-b/domain-boundary point
one C11/C14 parent comparison
one ART25-member-independence check
one tree-level-only negative control
one analogous-regulator negative control
```

Do not move a failed holdout into adapter construction.

---

# 26. Required benchmark families

Implement at least:

```text
B1A-A three-layer identity
B1A-B microscopic bare operator
B1A-C renormalization ledger
B1A-D project TMD definition
B1A-E ART25 definition and optimal-scale decomposition
B1A-F continuum scheme equivalence
B1A-G matching-strategy decision
B1A-H partonic external state and diagrams
B1A-I tree-level discipline
B1A-J LF-to-project kernel
B1A-K project-to-ART25 adapter
B1A-L hard/TMD cross-section invariance
B1A-M adapter independence
B1A-N conditional microscopic export
B1A-O conditional bridge rerun
B1A-P remainder separation
B1A-Q source-sufficiency/no-go decision
B1A-R deterministic isolation
```

---

# 27. Negative injections

Create at least **1,680 ordered C31 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## Layer identity

- finite-basis overlap called renormalized TMD;
- project TMD identified with ART25 without audit;
- ζ prescription called operator renormalization;
- evolution called finite scheme conversion;
- FNP model called soft factor;
- CS kernel copied into boundary.

## Microscopic operator

- Wilson order zero called all-order staple;
- gauge choice omitted;
- endpoint/basis cutoff omitted;
- operator normalization omitted;
- antiquark copied from quark;
- C11 replaced by C14 silently;
- C11 and C14 added.

## Renormalization ledger

- field or bilocal UV factor omitted;
- soft factor omitted or counted twice;
- zero-bin omitted;
- rapidity factor omitted;
- Hamiltonian counterterm omitted;
- missing component set to zero;
- analogous regulator accepted as exact.

## Source authority

- paper title accepted without equation;
- LaMET matching copied to C11;
- BLFQ model result treated as soft-subtracted TMD;
- continuum scheme theorem treated as LF-regulator matching;
- figure digitized;
- source version/hash omitted.

## Partonic matching

- different IR regulators used without conversion;
- IR dependence left in coefficient;
- gauge dependence left;
- real/Wilson/soft/instantaneous graph omitted;
- rapidity or UV pole left;
- external state changed after holdout freeze.

## Tree level

- tree-level identity promoted to full matching;
- first omitted order set to zero;
- tree-level adapter used at large b without remainder;
- tree-level result called physical TMD.

## Continuum adapter

- MS-bar convention mismatch hidden;
- finite factor used without hard companion;
- inverse adapter absent;
- round-trip failure hidden;
- scale evolution mixed into finite factor;
- ζ line selected from best residual;
- quark factor copied to gluon;
- flavor dependence invented.

## Adapter fitting

- adapter fitted to twelve points;
- point-dependent normalization;
- x/b ratio fitted to ART25 mean;
- ART25 chi2 used;
- Lambda/MSHT/MAPFF dependence;
- holdout used in construction.

## Export and covariance

- unmatched microscopic value exported;
- failed point imputed;
- empty projection treated as zero;
- external member dropped;
- null space regularized silently;
- ART25 covariance inflated;
- cross-root indices paired;
- residual called likelihood or p-value.

## Remainders

- regulator correction merged with scheme remainder;
- large-b mismatch absorbed into adapter;
- Fock truncation absorbed into ART25 band;
- missing Y absorbed into adapter;
- unknown discrepancy set to zero.

## Readiness and integrity

- process bridge executed;
- source/physical status promoted;
- deuteron claim;
- T-odd/gluon adapter activated;
- calibration/posterior/reweighting/emulator created;
- C30 historical matrix overwritten;
- raw MSHT grids committed;
- production registry or authoritative artifact mutated;
- nondeterministic manifest.

---

# 28. Deliverables

Create at least:

```text
docs/next_level/c31_implementation_report.md
docs/next_level/c31_api.md
docs/next_level/c31_requirement_coverage.json
docs/next_level/c31_normative_source_integration.json
docs/next_level/c31_primary_source_manifest.json
docs/next_level/c31_source_relevance_matrix.json

docs/next_level/c31_three_layer_identity_manifest.json
docs/next_level/c31_microscopic_bare_operator_manifest.json
docs/next_level/c31_microscopic_regulator_manifest.json
docs/next_level/c31_microscopic_wilson_soft_audit.json

docs/next_level/c31_renormalization_component_ledger.json
docs/next_level/c31_source_sufficiency_matrix.json
docs/next_level/c31_project_tmd_definition_manifest.json
docs/next_level/c31_project_scheme_implementation_gap.json
docs/next_level/c31_art25_operator_scheme_manifest.json
docs/next_level/c31_art25_optimal_scale_manifest.json
docs/next_level/c31_scheme_versus_scale_decomposition.json

docs/next_level/c31_continuum_scheme_equivalence_matrix.json
docs/next_level/c31_hard_tmd_companion_transformation.json
docs/next_level/c31_lf_to_tmd_matching_strategy.json
docs/next_level/c31_partonic_external_state_manifest.json
docs/next_level/c31_partonic_diagram_ledger.json
docs/next_level/c31_partonic_matching_oracle.json
docs/next_level/c31_tree_level_limit_report.json

docs/next_level/c31_lf_to_project_matching_library.json
docs/next_level/c31_lf_to_project_matching_remainder.json
docs/next_level/c31_lf_matching_capability_matrix.json
docs/next_level/c31_project_to_art25_adapter_library.json
docs/next_level/c31_project_to_art25_roundtrip_report.json
docs/next_level/c31_project_to_art25_rg_report.json
docs/next_level/c31_project_to_art25_remainder.json
docs/next_level/c31_adapter_independence_report.json

docs/next_level/c31_microscopic_renormalized_tmd_export.json
docs/next_level/c31_microscopic_renormalized_execution_report.json
docs/next_level/c31_distribution_bridge_rerun.json
docs/next_level/c31_distribution_bridge_capability_matrix.json
docs/next_level/c31_distribution_bridge_closure_report.json

docs/next_level/c31_adapter_remainder_budget.json
docs/next_level/c31_adapter_uncertainty_separation.json
docs/next_level/c31_source_sufficiency_decision.json
docs/next_level/c31_missing_calculation_specification.md

docs/next_level/c31_holdout_report.json
docs/next_level/c31_injection_manifest.json
docs/next_level/c31_regression_report.json
docs/next_level/c31_unresolved_physics_gaps.md
```

Add ADRs for three-layer TMD identity; Wilson-order-zero versus physical TMD; regulator-specific LF matching; continuum scheme equivalence versus microscopic matching; ζ prescription versus scheme conversion; hard-factor companion transformations; tree-level readiness discipline; adapter independence from fit data; remainder separation; and source-sufficiency/no-go status.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON must reproduce byte-for-byte. Heavy arrays may remain outside Git under a content-addressed runtime directory; commit schemas, hashes, dimensions, source order, and reconstruction commands.

---

# 29. Acceptance criteria

C31/B1A is complete only when:

1. The exact C30 baseline reproduces.
2. Required primary sources are version/hash locked.
3. The microscopic overlap, project TMD, and ART25 TMD remain distinct.
4. C11 bare/operator and regulator identities are complete.
5. Wilson-order-zero is not mislabeled as a physical staple.
6. Every required UV, soft, zero-bin, rapidity, and counterterm component is classified.
7. Missing components remain fail-closed.
8. The project TMD formal definition is separated from implementation status.
9. The ART25 operator scheme is separated from ζ prescription and FNP.
10. Continuum scheme claims use exact primary-source support.
11. Cross-section equivalence is not mislabeled individual-TMD equality.
12. Finite factors carry hard-factor companion transformations.
13. One LF matching strategy is selected before bridge execution.
14. Common IR regulation or a proved IR conversion is used.
15. Claimed matching closes UV, rapidity, IR, and gauge checks.
16. Tree-level identity remains limited.
17. First omitted orders and remainders remain visible.
18. LF matching kernels are state independent.
19. No matching coefficient is fitted to ART25.
20. Project-to-ART25 finite, scale, and evolution pieces remain separate.
21. Inverse/round-trip, RG, rapidity, and threshold statuses are explicit.
22. The adapter is independent of all 642 members and fit data.
23. No free normalization or point-dependent factor is introduced.
24. Microscopic renormalized exports exist only when LF matching passes.
25. Unavailable exports are empty rather than zero valued.
26. The bridge is rerun only when both matching layers pass.
27. All 642 external identities and covariance null spaces survive a rerun.
28. C29/C30 roles and holdouts remain frozen.
29. Remainder classes remain separate.
30. Unknown remainder remains nonzero-unknown.
31. No residual is used to construct the adapter.
32. Every insufficiency has an exact missing-calculation specification.
33. Distribution capability matrices are complete.
34. Process bridges remain unexecuted.
35. Gluon, LL, helicity, transversity, T-odd, and multiparton adapters remain fail-closed.
36. No deuteron/spin-1 prediction is claimed.
37. No fit, calibration, likelihood, posterior, optimization, reweighting, or emulator is created.
38. Data ancestry/no-double-counting remain intact.
39. Cross-root relation remains `NO_JOINT_MEASURE`.
40. All prior tests/builders/requirements/injections/manifests pass.
41. Production registry remains 216.
42. Eight authoritative artifacts remain byte-identical.
43. Raw transferred source files remain outside Git absent permission.
44. Every C31 injection yields its expected diagnostic.
45. All C31 manifests reproduce byte-for-byte.
46. Working tree is clean.
47. A local completion commit is created and not pushed.

C31 may complete with all twelve points still `BRIDGE_COMMON_DOMAIN_ONLY`. A source-resolved no-go result is preferable to an invented adapter.

---

# 30. Outcome branches

## Branch A: both matching layers close

When:

```text
MICROSCOPIC_LF_TO_SUBTRACTED_TMD_MATCHING = READY
RENORMALIZED_PROJECT_TO_ART25_ADAPTER = READY
```

and at least one flavor becomes `BRIDGE_DISTRIBUTION_COMPARISON_READY`, the next package is:

> **C32/B2 — frozen-bridge sensitivity, parameter ownership, identifiability, and discrepancy-prior readiness, still without calibration**

## Branch B: continuum adapter closes, microscopic matching does not

When:

```text
PROJECT_TO_ART25_ADAPTER_READY
MICROSCOPIC_LF_TO_TMD_MATCHING_UNAVAILABLE
```

the next package is:

> **C32/R0 — regulator-specific microscopic TMD renormalization and partonic matching calculation**

## Branch C: exact source/ancillary is identifiable but absent

> **C32/B1S — targeted source and ancillary ingestion for the microscopic matching kernel**

## Branch D: C11 lacks the operator/Wilson/soft structure needed to define matching

> **C32/O1 — microscopic subtracted-TMD operator construction with a declared rapidity regulator and soft sector**

Do not authorize inference automatically from any branch.

---

# 31. Allowed and forbidden statuses

Strong permitted package statuses include:

```text
C31_MICROSCOPIC_BARE_OPERATOR_SOURCE_AUDITED
C31_RENORMALIZATION_COMPONENT_LEDGER_COMPLETE
C31_PROJECT_TMD_DEFINITION_AUDITED
C31_ART25_OPERATOR_SCALE_DECOMPOSITION_VALIDATED
C31_CONTINUUM_SCHEME_EQUIVALENCE_AUDITED
C31_PARTONIC_MATCHING_STRATEGY_DECIDED
C31_TREE_LEVEL_OPERATOR_LIMIT_VALIDATED
C31_PROJECT_TO_ART25_ADAPTER_SOURCE_AUDITED
C31_SOURCE_SUFFICIENCY_DECISION_COMPLETE
C31_DISTRIBUTION_BRIDGE_CAPABILITY_MATRIX_COMPLETE
```

Issue only when exact gates pass:

```text
C31_LF_TO_PROJECT_MATCHING_SOURCE_AUDITED
C31_MICROSCOPIC_RENORMALIZED_TMD_EXPORT_VALIDATED
C31_PROJECT_TO_ART25_ADAPTER_VALIDATED
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

Forbidden:

```text
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

# 32. Final Codex response

Report:

- starting/final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- preserved primary sources/hashes;
- microscopic bare-operator classification and regulator identity;
- Wilson/soft/rapidity component statuses;
- project TMD definition and implementation status;
- ART25 operator/optimal-TMD/ζ-prescription decomposition;
- continuum scheme-equivalence decisions;
- hard/TMD companion transformation status;
- selected LF matching strategy;
- partonic external-state and diagram coverage;
- tree-level status;
- LF-to-project matching status/order/domain/remainder;
- project-to-ART25 adapter status/order/domain/remainder;
- round-trip, RG, rapidity, threshold, IR, UV, and gauge residuals;
- adapter member/data independence;
- microscopic renormalized export count/hashes;
- bridge point counts by flavor/status;
- external covariance rank/null-space preservation;
- remainder/discrepancy availability;
- exact source-sufficiency/no-go decision;
- exact missing-calculation specification when blocked;
- exact next-package branch;
- confirmation that no fit/calibration/likelihood/posterior/optimization/reweighting/emulator/process promotion/physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local commit;
- confirmation that nothing was pushed.

Do not describe a tree-level operator limit, continuum scheme equivalence, or formal renormalization declaration as a completed microscopic physical TMD bridge.
