# DeuteronWigner C401-C410 Repository Handoff

This is a read-only reconstruction of the authoritative scientific and repository handoff for phases C401 through C410. It is based on repository files and Git history, not lost conversation context.

## 1. CURRENT REPOSITORY STATE

- `pwd`: `/Users/dustin/work/DeuteronWigner`
- `git rev-parse --show-toplevel`: `/Users/dustin/work/DeuteronWigner`
- `git branch --show-current`: `main`
- `git rev-parse HEAD`: `51d3919e4660f5709cc7bb94c576c8ec17c9de14`
- `git show -s --format='%H%n%s%n%P' HEAD`:

  ```text
  51d3919e4660f5709cc7bb94c576c8ec17c9de14
  Merge C410 C117 I2 retained aggregation boundary
  160eb887f393177170b4c3486cea27b41968dfce 0ddf6554d6bce1445dfd3a7de72ecaac9d8bcc49
  ```

- `git status --porcelain=v1 --untracked-files=no`:

  ```text
   M handoff/ROADMAP.md
  ```

  This is a pre-existing tracked worktree modification. No files were changed during the audit that produced this handoff.

- Commit `51d3919e4660f5709cc7bb94c576c8ec17c9de14` exists: **YES**
- C410 phase commit `0ddf6554d6bce1445dfd3a7de72ecaac9d8bcc49` exists: **YES**
- C410 phase commit is an ancestor of `HEAD`: **YES**
- C411 appears in reachable refs: **NO**
- C411 appears in reachable commit subjects: **NO**
- C411 appears in branch names: **NO**
- C411 phase directory exists: **NO**
- C411 next-level record exists: **NO**

The repository-wide literal search found no semantic C411 record. Apparent substring hits inside hashes are not C411 records.

## 2. C401-C410 COMMIT CHAIN

Merge commits have no net path changes relative to their first parent; the path counts below are the committed paths in each phase commit.

| Phase | Descriptive title | Phase commit | Separate merge commit | Parent/baseline | Branch | Date | Paths | In `HEAD` |
|---|---|---|---|---|---|---:|---:|---|
| C401 | First numerical C396 mass directions | `aa3ea7aad6b0632b11b1ff9ca0f777ad48f9c5d4` | `fce8842e5ddc6660c735b7f69723f63c9bff7073` | `ada80920fb51617333c9b87a40d6538a0b0de915` | `codex/c401-c396-mass-directions` | 2026-08-30 10:43:15 -04:00 | 38 | YES |
| C402 | `ct_sector` / C117 numerical-frontier science lock | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** |
| C403 | C117 I2 numerical primitive | `146e8beba4132ba5b7d54d2a6dff25575af0e1fa` | `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1` | `fce8842e5ddc6660c735b7f69723f63c9bff7073` | `codex/c403-c117-i2-numerical-primitive` | 2026-08-30 13:26:39 -04:00 | 41 | YES |
| C404 | C117 I2 longitudinal/color primitives | `abd29c805f678ebcfad9494a76c789a7adac7270` | `6e7601881256d17fe14767d203cb4742143051c2` | `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1` | `codex/c404-c117-i2-longitudinal-color-primitive` | 2026-08-30 14:51:48 -04:00 | 39 | YES |
| C405 | C117 I2 current-topology embedding boundary | `0b99ab7d57a5d90d21df8ca7343b866eea7ea276` | `4dbb0b8bbadc540f0da2337c46040afb971fffc1` | `6e7601881256d17fe14767d203cb4742143051c2` | `codex/c405-c117-i2-current-topology-embedding` | 2026-08-30 18:20:23 -04:00 | 48 | YES |
| C406 | C117 I2 gluon normal-order descendant | `58c092f0e74a03a6500ae859c8921c8392ff285b` | `4f932604483701d18158164288674cea82a07b3f` | `4dbb0b8bbadc540f0da2337c46040afb971fffc1` | `codex/c406-c117-i2-gluon-normal-order-descendant` | 2026-08-30 21:39:34 -04:00 | 45 | YES |
| C407 | C117 I2 same-species descendants | `55b5d7fe5114abf8446e5b0031ccfbae5eff39a3` | `eb606e4974de17074d1eee0ed006448acc797602` | `4f932604483701d18158164288674cea82a07b3f` | `codex/c407-c117-i2-same-species-descendants` | 2026-08-31 15:28:58 -04:00 | 44 | YES |
| C408 | C117 I2 weight and transverse routing | `6b3fd1c846f9afb23f6d6cc46f48fef89811712b` | `ab0af6587131a2846425e9bb19cfdc784b9f0bdb` | `6da320adf775956e26e860e294c08e047c66c024` | `codex/c408-c117-i2-weight-routing-closure` | 2026-08-31 22:48:53 -04:00 | 49 | YES |
| C409 | C117 I2 `JgJg` derivative-density reconciliation | `bbabb756db5310350941b001142f7142af78b68c` | `160eb887f393177170b4c3486cea27b41968dfce` | `ab0af6587131a2846425e9bb19cfdc784b9f0bdb` | `codex/c409-c117-i2-derivative-density-reconciliation` | 2026-09-01 14:02:51 -04:00 | 46 | YES |
| C410 | C117 I2 retained aggregation boundary | `0ddf6554d6bce1445dfd3a7de72ecaac9d8bcc49` | `51d3919e4660f5709cc7bb94c576c8ec17c9de14` | `160eb887f393177170b4c3486cea27b41968dfce` | `codex/c410-c117-i2-retained-aggregation-boundary` | 2026-09-01 23:04:53 -04:00 | 50 | YES |

C402 is not reconstructible as an accepted repository phase. C403 records four external C402 artifacts:

- `C402_CT_SECTOR_AND_C117_FRONTIER_SCIENCE_LOCK.md`
- `C402_C117_NUMERICAL_READINESS_AUDIT.json`
- `C402_NEXT_NUMERICAL_FRONTIER.json`
- `C402_SOURCE_EVIDENCE_HASHES.json`

They are identified as `GOVERNING_C402_SCIENCE_LOCK_EXTERNAL_TO_RECONSTRUCTED_REPO`.

Principal implementation, evidence, and acceptance records:

- C401: implementation in `src/deuteron_wigner/bridge/c401_c396_mass_directions/`, with `tests/test_c401_c396_mass_directions.py`. Evidence includes `C401_C396_REDUCED_NUMERICAL_FORWARD_MAP_SCIENCE_LOCK_V1.md`, `C401_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md`, `binding_update_summary.json`, and `sparse_matrix_free_validation.json`. Acceptance was 14 focused + 4 source-authority + 26 C400.S2 = 44 passed, 0 failed. An additional 381-test source run passed; a separate pre-existing dependency run had 67 failures and 65 passes.
- C402: no implementation directory, phase commit, merge record, or accepted test record can be established. Tests: **UNKNOWN**.
- C403: implementation in `src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/`, with `tests/test_c403_c117_i2_numerical_primitive.py`. Evidence includes `C403_C117_I2_NUMERICAL_PRIMITIVE_SCIENCE_LOCK.md`, `support_theorem_certificate.json`, and `spatial_kernel_validation.json`. Required groups were 16 focused + 14 C401 regression + 26 C400.S2 regression; an additional 4-test C45/C47 source regression passed. One optional C62 test failed because a pre-existing C53 runtime artifact was missing.
- C404: implementation in `src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/`, with `tests/test_c404_c117_i2_longitudinal_color_primitive.py`. Evidence includes `C404_C117_I2_LONGITUDINAL_COLOR_PRIMITIVE_SCIENCE_LOCK.md`, `factorization_stress_validation.json`, and `triplet_color_spin_validation.json`. Selected acceptance: 84 passed, 0 failed.
- C405: implementation in `src/deuteron_wigner/bridge/c405_c117_i2_current_topology_embedding/`, with `tests/test_c405_c117_i2_current_topology_embedding.py`. Evidence includes `C405_C117_I2_CURRENT_TOPOLOGY_EMBEDDING_SCIENCE_LOCK.md`, `current_pair_grammar.json`, `conditional_kernel_validation.json`, and `cross_sector_zero_certificates.json`. Selected acceptance: 108 passed, 0 failed.
- C406: implementation in `src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/`, with `tests/test_c406_c117_i2_gluon_normal_order_descendant.py`. Evidence includes `C406_C117_I2_GLUON_NORMAL_ORDER_DESCENDANT_SCIENCE_LOCK.md`, `gluon_normal_order_authority.json`, and `mixed_kernel_validation.json`. Selected acceptance: 136 passed, 0 failed.
- C407: implementation in `src/deuteron_wigner/bridge/c407_c117_i2_same_species_descendants/`, with `tests/test_c407_c117_i2_same_species_descendants.py`. Evidence includes `C407_C117_I2_SAME_SPECIES_DESCENDANT_SCIENCE_LOCK.md`, `intermediate_axis_inventory.json`, `same_species_descendant_inventory.json`, and `scientific_boundary.json`. Selected acceptance: 162 passed, 0 failed. The separate `6da320ad...` compatibility hotfix restored Python 3.9 compatibility and became the C408 baseline.
- C408: implementation in `src/deuteron_wigner/bridge/c408_c117_i2_weight_routing_closure/`, with `tests/test_c408_c117_i2_weight_routing_closure.py`. Evidence includes `C408_C117_I2_WEIGHT_ROUTING_CLOSURE_SCIENCE_LOCK.md`, `routing_authority.json`, `q_sector_i4_validation.json`, and `jqjq_product_block_validation.json`. Selected acceptance: 192 passed, 0 failed.
- C409: implementation in `src/deuteron_wigner/bridge/c409_c117_i2_derivative_density_reconciliation/`, with `tests/test_c409_c117_i2_derivative_density_reconciliation.py`. Required live acceptance: 221 passed, 0 failed; 195 were replayable in the reconstructed snapshot. Evidence includes `C409_C117_I2_DERIVATIVE_DENSITY_RECONCILIATION_SCIENCE_LOCK.md`, `derivative_count_authority.json`, `jgjg_qg_validation.json`, and `scale_power_reconciliation.json`.
- C410: implementation in `src/deuteron_wigner/bridge/c410_c117_i2_retained_aggregation_boundary/`, with `tests/test_c410_c117_i2_retained_aggregation_boundary.py`. Required live acceptance: 276 passed, 0 failed. Evidence includes `C410_C117_I2_RETAINED_AGGREGATION_BOUNDARY_SCIENCE_LOCK.md`, `aggregation_authority.json`, `retained_aggregation_validation.json`, `vacuum_routing_authority.json`, and `normalization_boundary.json`.

## 3. SCIENTIFIC PROGRESSION

The project distinguishes source-derived zero from unavailable/missing, symbolic descriptors from numerical apply paths, test fixtures from physical authority, source operator shape from selected Hamiltonian coefficient, and numerical path count from physical response rank.

### C401

- **A — Missing object:** the first executable numerical portion of the C396 Hamiltonian forward map: the two mass-squared directions absent from C400.S2.
- **B — Added object:** (D_{q,K}=\partial H_K/\partial\mu_{q,K}^2) and (D_{g,K}=\partial H_K/\partial\delta\mu_{g,K}^2), emitted as canonical block ledgers, COO/CSR matrices, and independent matrix-free `LinearOperator` paths.
- **C — Coordinates/resolutions:** `mu_q,K^2` and `delta_mu_g,K^2` at K9, K11, and K13. The q⊕qg dimensions are 1350, 2706, and 4758.
- **D — Object class:** numerical sparse/matrix-free source operator, not a full C396 map.
- **E — Newly possible:** six complete K-local C396 apply paths, two directions at each resolution.
- **F — Incomplete:** remaining C396 coordinates, `ct_sector` semantics, C117 coefficient selection, normalization, physical rank, fit, and activation. The C128 historical partition defect was documented and corrected in the C401 adapter; C128 itself was not rewritten.

### C402

- **A — Missing object:** the meaning of the C396 `ct_sector` coordinate and the next lawful C117 numerical frontier.
- **B — Added object:** an externally referenced science-lock decision selecting `I2_density_projector` as the next frontier, with fail-closed primitive fallback.
- **C — Coordinates/resolutions:** the `ct_sector` ownership question and the C117 I2 direction. No accepted resolution-specific implementation is present.
- **D — Object class:** symbolic ownership/frontier selection only.
- **E — Newly possible:** a definite next implementation target rather than arbitrary completion of `ct_sector`.
- **F — Incomplete:** all numerical C117 action paths, finite-C43 normalization, and the complete C396 map. The accepted C402 commit and test evidence are **UNKNOWN**.

### C403

- **A — Missing object:** finite internal-member axis admissibility and the transverse harmonic-oscillator spatial kernel for C117 I2.
- **B — Added objects:** the exact axis theorem (2n+|m|\le N_{\max}-2), and (I[a,b;r]=\int\phi_a^*(x)\phi_b(x)|\phi_r(x)|^2dx), validated by exact rational Laguerre sums and independent Gauss-Laguerre quadrature.
- **C — Coordinates/resolutions:** C45/C47/C62 source bases and the qg intrinsic/relative external basis at K9/K11/K13. The q-sector external embedding was not assembled.
- **D — Object class:** source numerical primitives, not a C117 aggregate operator or complete coordinate action.
- **E — Newly possible:** executable transverse spatial kernels and exact admissibility/exclusion decisions for I2.
- **F — Incomplete:** q-sector embedding, C114/C115/C119 normalization/current factors, spin/color completion, target aggregation, and `c_C117,1`.

### C404

- **A — Missing object:** nonzero longitudinal transfer, color factors, spin/polarization selection, and qg partition structure.
- **B — Added objects:** \(\kappa(p',p)=0\) for equal modes and \([k_q(p')-k_q(p)]^{-2}\) otherwise; exact color factors qq (4/3), qg (-3/2), gq (-3/2), gg (3); and diagonal `I4` selection.
- **C — Coordinates/resolutions:** C117 I2 qg longitudinal/color source factors at K9/K11/K13.
- **D — Object class:** factorized algebraic source primitive/stress-test composition, explicitly not yet an operator binding.
- **E — Newly possible:** exact nonzero-transfer routing and color/spin factor evaluation.
- **F — Incomplete:** product-specific normal ordering, external factors, source phases, q-sector block, target aggregation, normalization, `g_s^2`, and `c_C117,1`.

### C405

- **A — Missing object:** source current topology and ordered product structure in (P^-_{\mathrm{IC}}=-g_s^2\!\int[Kj^+][Kj^+]/2), (j=J_q+J_g).
- **B — Added object:** explicit qq, qg, gq, and gg product grammar, caller-conditioned kernels, and source-derived cross-sector zeros. q→qg and qg→q vanish by even-gluon parity; q→q is unavailable, not zero.
- **C — Coordinates/resolutions:** all K9/K11/K13 I2 q and qg source blocks.
- **D — Object class:** caller-conditioned adapter/interface and topology stress test, not a complete operator binding.
- **E — Newly possible:** explicit BRA/KET derivative assignments and separate qg/gq orderings.
- **F — Incomplete:** source product descendants, finite-cell/field/state normalization, C405-to-C125 target mapping, q-sector block, Hermitian completion, `g_s^2`, and `c_C117,1`.

### C406

- **A — Missing object:** one-gluon normal-order descendant of the gluon current and the mixed qg/gq kernel.
- **B — Added object:** from (J_g=-fA\partial A), the descendant factor (-(k_{\mathrm{bra}}+k_{\mathrm{ket}})F^a), with (f^{abb}=0) commutator cancellation, and the routed coefficient (-(k_{\mathrm{bra}}+k_{\mathrm{ket}})F/(2\sqrt{k_{\mathrm{bra}}k_{\mathrm{ket}}})). Mixed products collapse to \(\kappa[-k_g(p')-k_g(p)]\).
- **C — Coordinates/resolutions:** qg mixed products and q-sector mixed blocks at K9/K11/K13.
- **D — Object class:** numerical mixed source primitives and routing descendants.
- **E — Newly possible:** executable mixed qg/gq kernels with explicit source order.
- **F — Incomplete:** same-species qq and gg contractions, full normalization, target aggregation, (P^-\to M^2) normalization, `g_s^2`, and `c_C117,1`.

### C407

- **A — Missing object:** finite longitudinal intermediate axes and same-species one-body weights.
- **B — Added objects:** (w_q=C_F/(r-k)^2) and (w_g=C_A(r-k)^{-2}(k+r)^2/(4kr)), with (C_F=4/3), (C_A=3), across 154 validated rows.
- **C — Coordinates/resolutions:** q and qg external modes at K9/K11/K13, including conditioned qg (J_qJ_q) composition.
- **D — Object class:** numerical conditional primitives/interface; missing or incomplete weights are rejected and no default weights are supplied.
- **E — Newly possible:** source-routed one-body weighted descendants with finite-axis closure.
- **F — Incomplete:** source-authorized graph-member weights, q-sector qq I4, gg derivative density, gg q-sector pair/vacuum branch, normalization, target count-once aggregation, `g_s^2`, and `c_C117,1`.

### C408

- **A — Missing object:** q-sector (J_qJ_q:q\to q) closure and the exact qg member multiplier.
- **B — Added objects:** the q-sector `I4_local` route through C116/C126, exact I2 qg member multiplier (1), and source-routed qq, qg, and gq product blocks.
- **C — Coordinates/resolutions:** q-sector q→q and qg-sector products at K9/K11/K13.
- **D — Object class:** source-routed product-block primitives and partial aggregate assembly, not the retained four-product aggregate.
- **E — Newly possible:** nine source-routed product-block paths and a closed q-sector qq route.
- **F — Incomplete:** qg gg branch, especially its derivative-count conflict; full normalization; target aggregation; `g_s^2`; and `c_C117,1`.

### C409

- **A — Missing object:** qg→qg (J_gJ_g) derivative-density branch.
- **B — Added object:** three qg (J_gJ_g) source-routed primitives. C114 supplies exactly two longitudinal derivatives, one per current; C406/C407 already contain both. The source scales cancel as ((L/\pi)^2(\pi/L)^2=1), with no extra C119/C124 derivative factor.
- **C — Coordinates/resolutions:** qg→qg source branch at K9/K11/K13.
- **D — Object class:** numerical source product primitive.
- **E — Newly possible:** all four source-ordered product blocks in the qg sector, with the gluon color factor counted once.
- **F — Incomplete:** q-sector gg pair/vacuum handling, normalization, target count-once aggregation, `g_s^2`, and `c_C117,1`.

### C410

- **A — Missing object:** retained connected four-product aggregate and explicit routing of the q-sector gluon vacuum branch.
- **B — Added object:** (J_K^{\mathrm{ret}}=B_K^{qq}+B_K^{qg}+B_K^{gq}+B_K^{gg}) and (S_K^{(410)}=-\frac12(B_K^{qq}+B_K^{qg}+B_K^{gq}+B_K^{gg})). The stored shape applies (-1/2) exactly once and leaves (g_s^2) factored.
- **C — Coordinates/resolutions:** retained q⊕qg I2 aggregate at K9/K11/K13, with shapes 1350×1350, 2706×2706, and 4758×4758.
- **D — Object class:** retained aggregate operator shape, not a normalized C117 coordinate operator.
- **E — Newly possible:** one retained connected aggregate shape per resolution, with source-order decomposition, Hermitian mixed terms, and explicit vacuum routing.
- **F — Incomplete:** finite-C43 source-to-target adapter, field/external-state/wave-packet normalization, (P^-\to M^2) normalization, `c_C117,1`, numerical `g_s^2` selection, physical rank, fit, and activation.

## 4. NUMERICAL FRONTIER LEDGER

| Phase | Complete numerical C117 actions | Complete numerical C396 actions | Source primitives/shapes added | Full C117 I2? | Full C396 map? |
|---|---:|---:|---|---|---|
| C401 | 0 | 6 | (D_q,D_g) at K9/K11/K13 | NO | NO |
| C402 | UNKNOWN; inherited frontier 0 | inherited 6 | External frontier selection only | NO | NO |
| C403 | 0 | 6 | Axis theorem and transverse spatial kernel | NO | NO |
| C404 | 0 | 6 | Transfer, color, spin, factorized longitudinal primitives | NO | NO |
| C405 | 0 | 6 | Ordered current topology and conditioned product kernels | NO | NO |
| C406 | 0 | 6 | Mixed qg/gq normal-order descendants | NO | NO |
| C407 | 0 | 6 | Same-species axes and q/g weights | NO | NO |
| C408 | 0 | 6 | Nine source-routed product-block paths | NO | NO |
| C409 | 0 | 6 | Twelve source-routed product-block paths | NO | NO |
| C410 | 0 | 6 | Twelve product primitives plus three retained aggregate shapes | NO | NO |

The authoritative count change occurred at C401:

- C400.S2: 0 complete numerical C396 apply paths.
- C401: 6 complete numerical C396 apply paths.
- C403–C410: still 6.

Later phases add C117 I2 source primitives and aggregate shapes; they do not complete a C117 coordinate action or all 57 symbolic C396 rows. Six numerical paths are not a physical response rank.

## 5. C410 FINAL SCIENCE STATE

The retained aggregate is established for K9, K11, and K13 as

\[
S_K^{(410)}=-\frac12(B_K^{qq}+B_K^{qg}+B_K^{gq}+B_K^{gg}).
\]

Supporting records are `aggregation_authority.json`, `count_once_aggregation.json`, `retained_aggregation_validation.json`, and `src/deuteron_wigner/bridge/c410_c117_i2_retained_aggregation_boundary/aggregate.py`.

- All four source-ordered products occur exactly once: **YES**. Product count is four; multiplicity is one; omitted and duplicate counts are zero.
- (B_K^{qg}) and (B_K^{gq}) remain distinct: **YES**. Mixed orders are retained separately.
- ((B_K^{qg})^\dagger=B_K^{gq}): **YES**. The maximum mixed-source-order adjoint residual is zero.
- Mixed terms are not replaced by a factor of two: **YES**. `factor_two_substitution_used` is false and no product row has an extra factor of two.
- The full-source gluon pair/vacuum branch can be nonzero: **YES**. The unequal-mode witness has summed norm squared (3.0); equal-momentum cancellation gives zero.
- Disconnected vacuum contribution is excluded from the retained connected Hamiltonian matrix by source-derived routing: **YES**. C129/C131/C136 routing projects the vacuum direction out of the retained connected matrix. It is not arbitrary zero fill and no identity shift is added.
- (g_s^2) is included in the stored C410 operator shape: **NO**. It remains factored.
- (c_{\mathrm{C117},1}) is selected: **NO**. It is explicitly unselected and outside the stored normalization capsule.
- C410 shape units are GeV²: **QUALIFIED YES**. The source-reduced shape carries the Hamiltonian mass-squared scale, but the authoritative unit statement is `GeV^2 times the unresolved C260 finite-C43 operator-normalization adapter`.

Therefore GeV² is established for the source-reduced shape, not for a completed normalized C117 physical operator.

## 6. NORMALIZATION / C411 FRONTIER

The repository does not establish a finite-C43 numerical adapter from the C410 source shape to the C117 Hamiltonian-coordinate operator.

| Object | Repository status |
|---|---|
| Finite-C43 source-to-target mixing matrix (A_K) | UNAVAILABLE / not evaluated |
| Residual normalization (N_K) | UNAVAILABLE |
| (A_K=I) | NOT ESTABLISHED |
| (N_K=1) | NOT ESTABLISHED |
| External-state normalization | UNRESOLVED |
| Field normalization | UNRESOLVED |
| Wave-packet normalization | UNRESOLVED |
| Finite-cell convention | Required by contract, not numerically instantiated |
| (P^-\to M^2) conversion | Symbolic relation exists; finite numerical conversion unresolved |
| Source/target basis hashes for the finite adapter | NOT ESTABLISHED |
| (g_s^2) ownership | Factored outside the stored C410 shape |
| (c_{\mathrm{C117},1}) | Not selected; no value established |

Relevant records include:

- `docs/next_level/c259_adapter_plan_contract.json`
- `docs/next_level/c260_finite_c43_adapter_contract.json`
- `docs/next_level/c260_tree_response_matrix_contract.json`
- `docs/next_level/c261_symbolic_conversion_program_contract.json`
- `docs/next_level/c262_numerator_audit_contract.json`
- `docs/next_level/c263_local_rismom_contract.json`
- `src/deuteron_wigner/bridge/hqcdc117rismom1/core.py`
- `src/deuteron_wigner/bridge/c410_c117_i2_retained_aggregation_boundary/normalization.py`
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/normalization_boundary.json`
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/normalization_capsule_schema.json`

C260 defines a continuum RI/SMOM scheme and a tree-level identity matrix as a scheme basis definition. That does not establish a finite-C43 numerical identity map. C262 explicitly leaves the finite-basis numerator/loop conversion unavailable, not zero.

The smallest precise missing object is:

> A source-qualified K-local C260/C262 finite-C43 adapter and operator-normalization capsule mapping the C410 retained source-reduced connected shape to the `PROJECT_C117_RI_SMOM_V1` (O_{\mathrm{C117},1,R}) insertion, including field normalization, external-state normalization, normalized finite-cell wave packets, and the (P^-\to M^2) convention.

No identity map or unit normalization should be created by assumption.

## 7. CONTRADICTION AUDIT

These historical records remain in the repository but are superseded as current status:

- **“C396 has 57 symbolic binding rows and zero complete numerical apply paths.”** Paths: `docs/phases/c400_s2_merge_closure/merge_readiness.json`, `docs/phases/c400_s2_corrective_patch/c396_binding_summary.json`, `docs/phases/c400_s2_corrective_patch/C400_S2_ACCEPTANCE_SPEC.json`, and `docs/phases/c400_s2_corrective_patch/live_integration/implementation_report.md`. Superseded by C401 `binding_update_summary.json` and `sparse_matrix_free_validation.json`, which establish six complete numerical C396 paths. It remains valid only as a C400 snapshot.

- **“C399 is a terminal blocker; lawful routes are exhausted.”** Paths: `docs/phases/c399_physical_target_capsule/c399_route_exhaustion.json`, `c399_blocker_certificate.json`, and `c399_implementation_report.md`. Superseded as a claim of terminal implementation closure by C401–C410, which opened a lawful source-derived numerical path. The physical-target/normalization blocker itself remains; C410 still reports the finite-C43 adapter as missing.

- **“Physical rank = 0.”** Paths: `docs/phases/c397_physical_state_obs/c397_rank_null.json`, `docs/phases/c398_physical_condition_acquisition/c398_rank_forecast.json`, and the corresponding C397/C398 source modules. Superseded as the current status label by C401–C410, whose authoritative status is `RANK_NOT_EVALUATED`. This does not imply a nonzero rank.

- **“Nineteen independent target capsules are required.”** Paths: `docs/phases/c399_physical_target_capsule/c399_blocker_certificate.json` and `docs/phases/c400_s2_corrective_patch/C400_S2_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md`. Superseded as the current coordinate interpretation by `docs/phases/c401_c396_mass_directions/C401_C396_COORDINATE_REDUCTION_V1.json`: nineteen raw registry slots reduce to a provisional candidate-direction structure, not nineteen independently measured physical responses. C410 still provides no physical target capsules.

- **“No forward map, no numerical Hamiltonian, no activation”** in C400 handoff records: `docs/phases/c400_s2_corrective_patch/live_integration/CHATGPT_HANDOFF_README.md` and `blocker_or_completion.json`. Superseded only for the narrow C396 mass-direction slice by C401 and for the retained source shape by C410. C117 action, physical fit, rank, and activation remain incomplete.

These records are historical evidence and were not modified.

## 8. TEST / ACCEPTANCE HISTORY

The accepted C410 live integration record supports the requested total exactly:

| Component group | Passed |
|---|---:|
| C410 focused | 55 |
| C409 regression | 29 |
| C408 regression | 28 |
| C407 regression | 28 |
| C406 regression | 24 |
| C405 regression | 21 |
| C404 regression | 15 |
| C403 regression | 16 |
| C401 regression | 14 |
| C400.S2 regression | 26 |
| C114/C115/C117/C119 regression | 12 |
| C45/C47 selected regression | 4 |
| C151 convention regression | 4 |
| **Total** | **276** |

The sum is exactly 276, with 0 failures. The repository label is `C151 convention regression`, matching the requested component.

Accepted phase-local progression:

| Phase | Accepted selected/live total |
|---|---:|
| C401 | 44 |
| C402 | UNKNOWN |
| C403 | 56 required, plus 4 source-regression tests |
| C404 | 84 |
| C405 | 108 |
| C406 | 136 |
| C407 | 162 |
| C408 | 192 |
| C409 | 221 |
| C410 | 276 |

C403’s optional C62 replay failed because a pre-existing C53 runtime artifact was absent; it was explicitly classified as outside the C403 regression. The C401 dependency discrepancy of 67 failures/65 passes was likewise recorded as pre-existing and separate from C401 acceptance.

## FILES MOST USEFUL FOR CHATGPT CONTINUATION

- `docs/phases/c401_c396_mass_directions/C401_C396_REDUCED_NUMERICAL_FORWARD_MAP_SCIENCE_LOCK_V1.md` — establishes the first six complete C396 numerical paths and coordinate reduction.
- `docs/phases/c401_c396_mass_directions/C401_C396_COORDINATE_REDUCTION_V1.json` — defines the reduced C396 coordinate ontology.
- `docs/phases/c401_c396_mass_directions/binding_update_summary.json` — records the C396 count transition from zero to six.
- `docs/phases/c403_c117_i2_numerical_primitive/C403_C117_I2_NUMERICAL_PRIMITIVE_SCIENCE_LOCK.md` — defines the C403 axis and spatial primitive.
- `docs/phases/c404_c117_i2_longitudinal_color_primitive/C404_C117_I2_LONGITUDINAL_COLOR_PRIMITIVE_SCIENCE_LOCK.md` — defines transfer and color/spin primitives.
- `docs/phases/c405_c117_i2_current_topology_embedding/C405_C117_I2_CURRENT_TOPOLOGY_EMBEDDING_SCIENCE_LOCK.md` — defines ordered source-current topology.
- `docs/phases/c406_c117_i2_gluon_normal_order_descendant/C406_C117_I2_GLUON_NORMAL_ORDER_DESCENDANT_SCIENCE_LOCK.md` — defines the gluon normal-order descendant.
- `docs/phases/c407_c117_i2_same_species_descendants/C407_C117_I2_SAME_SPECIES_DESCENDANT_SCIENCE_LOCK.md` — defines finite intermediate axes and same-species weights.
- `docs/phases/c408_c117_i2_weight_routing_closure/C408_C117_I2_WEIGHT_ROUTING_CLOSURE_SCIENCE_LOCK.md` — closes q-sector I4 and product routing.
- `docs/phases/c409_c117_i2_derivative_density_reconciliation/C409_C117_I2_DERIVATIVE_DENSITY_RECONCILIATION_SCIENCE_LOCK.md` — fixes the qg (J_gJ_g) derivative count.
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/C410_C117_I2_RETAINED_AGGREGATION_BOUNDARY_SCIENCE_LOCK.md` — final C410 scientific boundary.
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/aggregation_authority.json` — proves the four products are counted once.
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/vacuum_routing_authority.json` — distinguishes nonzero full-source vacuum from retained connected routing.
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/normalization_boundary.json` — states exactly what C410 does and does not normalize.
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/retained_aggregation_validation.json` — gives K9/K11/K13 shapes, NNZ counts, Hermiticity, and residuals.
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/live_integration/focused_tests.json` — authoritative 276-test acceptance ledger.
- `docs/next_level/c259_adapter_plan_contract.json` — defines intended adapter families without evaluated coefficients.
- `docs/next_level/c260_finite_c43_adapter_contract.json` — explicitly marks the finite-C43 adapter unavailable, not zero.
- `docs/next_level/c262_numerator_audit_contract.json` — records the unresolved continuum/numerator conversion.
- `src/deuteron_wigner/bridge/c410_c117_i2_retained_aggregation_boundary/normalization.py` — executable fail-closed boundary for the missing normalization object.

## AUTHORITATIVE C410 HANDOFF

- **Current accepted baseline:** `51d3919e4660f5709cc7bb94c576c8ec17c9de14`
- **C410 phase commit:** `0ddf6554d6bce1445dfd3a7de72ecaac9d8bcc49`
- **Accepted scientific accomplishments C401-C410:** six complete C396 mass-direction applies; C117 I2 axis, spatial, transfer, color, topology, normal-order, same-species, weight, derivative-density, and retained-aggregation source structures are implemented and validated.
- **Exact current numerical frontier:** 57 symbolic C396 rows; 6 complete numerical C396 actions; 12 source-routed product primitives; 3 retained aggregate shapes; 0 complete numerical C117 I2 actions.
- **Exact C117 status:** retained source-reduced aggregate shape exists, but the normalized C117 Hamiltonian-coordinate action does not.
- **Physical-rank status:** `RANK_NOT_EVALUATED`.
- **Fit status:** unauthorized / not performed.
- **Activation status:** `NOT_READY`.
- **Smallest remaining physics/mathematics object:** source-qualified finite-C43 C260/C262 adapter and normalization capsule, including field, state, wave-packet, and (P^-\to M^2) conventions.
- **C411 status:** **ABSENT** — no accepted commit, branch, phase directory, or semantic next-level record.
- **Recommended next operation:** authorize a new C411 phase implementing and validating that finite-C43 adapter without assuming (A_K=I), (N_K=1), or any unprovided physical normalization.
