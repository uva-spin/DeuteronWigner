# C401-C410 Repository Handoff

This is the continuation handoff for the DeuteronWigner C401-C410 sequence.
The canonical source checkout is `/Users/dustin/work/DeuteronWigner`; this
file is the published continuation view at:

<https://github.com/uva-spin/DeuteronWigner/tree/main/computation_handoff/repo>

The source commit represented here is recorded in `CURRENT_SOURCE_COMMIT.txt`.
The source checkout and accepted Git history remain authoritative; this tree
must be refreshed after every accepted phase or material scientific commit.

## Current state

- Canonical branch: `main`
- Accepted source commit: `51d3919e4660f5709cc7bb94c576c8ec17c9de14`
- Subject: `Merge C410 C117 I2 retained aggregation boundary`
- C410 phase commit: `0ddf6554d6bce1445dfd3a7de72ecaac9d8bcc49`
- C410 is an ancestor of the accepted source commit: YES
- C411 phase commit, branch, directory, or semantic record: ABSENT
- The canonical checkout had a pre-existing tracked modification to
  `handoff/ROADMAP.md` at audit time.

## Accepted C401-C410 chain

| Phase | Phase commit | Merge commit | Parent/baseline | Date | Paths |
|---|---|---|---|---:|---:|
| C401 | `aa3ea7aad6b0632b11b1ff9ca0f777ad48f9c5d4` | `fce8842e5ddc6660c735b7f69723f63c9bff7073` | `ada80920fb51617333c9b87a40d6538a0b0de915` | 2026-08-30 | 38 |
| C402 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| C403 | `146e8beba4132ba5b7d54d2a6dff25575af0e1fa` | `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1` | `fce8842e5ddc6660c735b7f69723f63c9bff7073` | 2026-08-30 | 41 |
| C404 | `abd29c805f678ebcfad9494a76c789a7adac7270` | `6e7601881256d17fe14767d203cb4742143051c2` | `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1` | 2026-08-30 | 39 |
| C405 | `0b99ab7d57a5d90d21df8ca7343b866eea7ea276` | `4dbb0b8bbadc540f0da2337c46040afb971fffc1` | `6e7601881256d17fe14767d203cb4742143051c2` | 2026-08-30 | 48 |
| C406 | `58c092f0e74a03a6500ae859c8921c8392ff285b` | `4f932604483701d18158164288674cea82a07b3f` | `4dbb0b8bbadc540f0da2337c46040afb971fffc1` | 2026-08-30 | 45 |
| C407 | `55b5d7fe5114abf8446e5b0031ccfbae5eff39a3` | `eb606e4974de17074d1eee0ed006448acc797602` | `4f932604483701d18158164288674cea82a07b3f` | 2026-08-31 | 44 |
| C408 | `6b3fd1c846f9afb23f6d6cc46f48fef89811712b` | `ab0af6587131a2846425e9bb19cfdc784b9f0bdb` | `6da320adf775956e26e860e294c08e047c66c024` | 2026-08-31 | 49 |
| C409 | `bbabb756db5310350941b001142f7142af78b68c` | `160eb887f393177170b4c3486cea27b41968dfce` | `ab0af6587131a2846425e9bb19cfdc784b9f0bdb` | 2026-09-01 | 46 |
| C410 | `0ddf6554d6bce1445dfd3a7de72ecaac9d8bcc49` | `51d3919e4660f5709cc7bb94c576c8ec17c9de14` | `160eb887f393177170b4c3486cea27b41968dfce` | 2026-09-01 | 50 |

C402 has no accepted phase commit or merge record in the reconstructed
repository. C403 records its science-lock artifacts as external to the
reconstructed repository.

## Scientific progression

The following are source-authority distinctions, not merely test outcomes.

- **C401:** Added the first six complete numerical C396 mass-direction apply
  paths: `D_q,K = dH_K/d(mu_q,K^2)` and
  `D_g,K = dH_K/d(delta_mu_g,K^2)` at K9, K11, and K13. These are sparse,
  CSR, and matrix-free source operators. The full 57-row C396 map remained
  incomplete.
- **C402:** External science-lock decision selected `I2_density_projector`
  as the next lawful frontier and kept `ct_sector` fail-closed. No numerical
  phase implementation is present.
- **C403:** Added the exact finite internal-member axis theorem
  `2*n + abs(m) <= Nmax - 2` and the transverse HO kernel
  `I[a,b;r] = integral(phi_a* phi_b |phi_r|^2)`. These are source primitives,
  not a complete C117 action.
- **C404:** Added nonzero-transfer `kappa`, exact qq/qg/gq/gg color factors,
  and diagonal `I4` spin/polarization selection. The result is a factorized
  algebraic primitive, not an operator binding.
- **C405:** Made the source current topology explicit through the four ordered
  products qq, qg, gq, and gg. Cross-sector parity zeros are source-derived;
  unavailable same-sector blocks remain unavailable, not zero.
- **C406:** Added the one-gluon normal-order descendant and executable mixed
  qg/gq kernels while retaining source order and Hermitian reversal.
- **C407:** Added finite longitudinal intermediate axes and explicit quark and
  gluon weights. Missing or incomplete weights are rejected; no defaults are
  inserted.
- **C408:** Closed the q-sector `JqJq` I4 route and the exact I2 qg multiplier
  `1`, assembling source-routed qq, qg, and gq product blocks.
- **C409:** Added the qg-to-qg `JgJg` branch with exactly two source
  derivatives and no extra C119/C124 derivative factor. The source scales
  cancel as `(L/pi)^2 * (pi/L)^2 = 1`.
- **C410:** Formed the retained connected aggregate shape
  `S_K^(410) = -1/2 (B_K^qq + B_K^qg + B_K^gq + B_K^gg)` for K9, K11, and
  K13. The full-source gluon pair/vacuum branch can be nonzero, but its
  disconnected vacuum contribution is excluded from the retained connected
  Hamiltonian matrix by source-derived routing.

## Numerical frontier

| Phase | Complete C117 actions | Complete C396 actions | Added source objects | Full C117 I2? | Full C396 map? |
|---|---:|---:|---|---|---|
| C401 | 0 | 6 | Two mass directions at three K resolutions | NO | NO |
| C402 | UNKNOWN; inherited 0 | inherited 6 | External frontier selection | NO | NO |
| C403 | 0 | 6 | Axis and spatial kernels | NO | NO |
| C404 | 0 | 6 | Transfer/color/spin primitives | NO | NO |
| C405 | 0 | 6 | Ordered topology and conditioned kernels | NO | NO |
| C406 | 0 | 6 | Mixed normal-order descendants | NO | NO |
| C407 | 0 | 6 | Same-species axes and weights | NO | NO |
| C408 | 0 | 6 | 9 product-block paths | NO | NO |
| C409 | 0 | 6 | 12 product-block paths | NO | NO |
| C410 | 0 | 6 | 12 product primitives + 3 aggregate shapes | NO | NO |

The complete numerical C396 count changed only at C401, from zero to six.
The six paths are not a physical response rank.

## C410 retained aggregate

The C410 authority and validation records establish:

- all four source-ordered products occur exactly once;
- qg and gq remain distinct;
- `(B_K^qg) dagger = B_K^gq`;
- no mixed-term factor of two is substituted;
- the full-source gluon pair/vacuum branch has an unequal-mode witness with
  summed norm squared `3.0`;
- equal-momentum vacuum-pair cancellation gives zero;
- disconnected vacuum routing is excluded from the retained connected matrix,
  rather than filled with an arbitrary zero or identity shift;
- `g_s^2` is factored outside the stored shape;
- `c_C117,1` is not selected.

Validated retained shapes are:

| Resolution | Shape | NNZ |
|---|---:|---:|
| K9 | 1350 x 1350 | 13,446 |
| K11 | 2706 x 2706 | 43,506 |
| K13 | 4758 x 4758 | 110,598 |

The source-reduced shape carries the qualified units `GeV^2 times the
unresolved C260 finite-C43 operator-normalization adapter`.

## Normalization / C411 frontier

The repository does not establish a finite-C43 source-to-target mixing matrix
`A_K`, residual normalization `N_K`, identity map, unit normalization,
external-state normalization, field normalization, wave-packet normalization,
finite-cell convention, source/target basis hashes, or numerical
`P^- -> M^2` conversion.

C260's continuum RI/SMOM tree-level identity is a scheme definition, not a
finite-C43 numerical adapter. C262 leaves the finite-basis numerator and loop
conversion unavailable, not zero.

The smallest missing object is a source-qualified K-local C260/C262 finite-C43
adapter and operator-normalization capsule mapping the C410 retained shape to
the `PROJECT_C117_RI_SMOM_V1` `O_C117_1,R` insertion, including field/state/
wave-packet normalization and the `P^- -> M^2` convention. Do not assume
`A_K = identity` or `N_K = 1`.

Current physical status:

- physical rank: `RANK_NOT_EVALUATED`
- fit: unauthorized / not performed
- activation: `NOT_READY`

## Acceptance

The C410 live integration record reports 276 passed and 0 failed:

```text
C410 focused                         55
C409 regression                      29
C408 regression                      28
C407 regression                      28
C406 regression                      24
C405 regression                      21
C404 regression                      15
C403 regression                      16
C401 regression                      14
C400.S2 regression                   26
C114/C115/C117/C119 regression       12
C45/C47 selected regression           4
C151 convention regression            4
total                               276
```

## Update procedure

After every accepted phase or material scientific commit on canonical `main`:

1. copy the accepted source, phase evidence, and continuation notes needed by
   independent reviewers into this published tree;
2. update `CURRENT_SOURCE_COMMIT.txt` to the accepted source commit;
3. update this handoff or its successor phase handoff;
4. refresh `REPO_CONTENTS.files`, `REPO_CONTENTS.sizes`, and
   `REPO_CONTENTS.sha256` when the published inventory changes;
5. verify the snapshot and documentation; and
6. commit and push `main`.

The published tree is not current unless its source marker identifies the
accepted source commit represented by the published tree. A handoff-only
publication commit may follow it. Never replace unavailable/missing values with zeros or
invent normalization, physical rank, fit, or activation.

## Primary evidence

- `docs/phases/c401_c396_mass_directions/`
- `docs/phases/c403_c117_i2_numerical_primitive/`
- `docs/phases/c404_c117_i2_longitudinal_color_primitive/`
- `docs/phases/c405_c117_i2_current_topology_embedding/`
- `docs/phases/c406_c117_i2_gluon_normal_order_descendant/`
- `docs/phases/c407_c117_i2_same_species_descendants/`
- `docs/phases/c408_c117_i2_weight_routing_closure/`
- `docs/phases/c409_c117_i2_derivative_density_reconciliation/`
- `docs/phases/c410_c117_i2_retained_aggregation_boundary/`
- `docs/next_level/c259_adapter_plan_contract.json`
- `docs/next_level/c260_finite_c43_adapter_contract.json`
- `docs/next_level/c262_numerator_audit_contract.json`
