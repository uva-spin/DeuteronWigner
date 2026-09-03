# C64/QGTM2 Codex Work Package

## Title

**Exact Talmi–Moshinsky artifact and support-certificate integrity completion: per-block canonical expressions, threshold-free support hashes, certified numerical arrays, basis-order manifests, deterministic runtime paths, and read-only import closure**

## Authoritative baseline

Start from the clean local C63/QGEMBED2 fail-closed completion commit:

```text
be7c1c7f085ae06829b99b31eee2ca2d39056129
```

Its immediate scientific parent is the C62 exact-algebra completion:

```text
cfe1680c381b9531a88e27571e3898a75f6ba784
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor cfe1680c381b9531a88e27571e3898a75f6ba784 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY

C63_QGEMBED_C62_IMPORT_INCOMPLETE
```

and the exact C63 blocker:

```text
C62 scientific identities reproduced:
    selected plan QGTM-CIRCULAR-LADDER-PRIMARY;
    exact global polar/circular convention;
    exact x-weighted TM construction;
    historical CM-ground subthreshold residues
        4,032 / 15,840 / 48,048
        all exact m-selection zeros;
    genuine small nonzeros = 0;
    unresolved residues = 0.

C62 read-only import artifacts missing:
    per-block canonical expression hashes;
    per-block exact-support hashes;
    certified numerical arrays;
    per-entry or blockwise numerical error bounds;
    row- and column-basis-order hashes;
    deterministic runtime artifact paths;
    sufficient inventory records for a read-only downstream rebuild.

C63 consequence:
    C63 cannot regenerate C62 internally while simultaneously claiming
    that C62 was consumed read-only;
    no CM-ground/triplet physical embedding or downstream support audit
    was performed.
```

Verify every statement from the committed C62 and C63 records rather than relying on this prompt.

The exact C62 scientific convention remains immutable:

\[
|n,m\rangle_{\rm polar}
=
(-1)^n
\left|
n+\max(m,0),\,
n+\max(-m,0)
\right\rangle_{\rm circ},
\qquad
L_z=N_+-N_-.
\]

The physical trajectory remains:

```text
(K,Nmax,bHO/GeV)
  = (9/2,8,0.40)
  = (11/2,10,0.45)
  = (13/2,12,0.50).
```

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C64 is an **artifactization and import-integrity package**, not a new Talmi–Moshinsky derivation.

C62 established the mathematics but did not freeze enough concrete output for a later package to consume it read-only. C64 must therefore create a descendant artifact layer that is generated from the immutable C62 code and contracts.

C64 must not:

```text
silently edit or reinterpret C62 historical artifacts;

claim that a C64-owned artifact was already present in C62;

change the global polar/circular phase;

change a coefficient or exact-zero status;

change a longitudinal partition, shell, basis order, or rotation;

fit an expression to historical quadrature;

or reconstruct C62 inside C65 after declaring C64 read-only.
```

The correct ownership is:

```text
C62:
    source-derived exact HO/TM algebra and coefficient API;

C64:
    complete materialized, content-addressed, certified artifact
    realization of that immutable C62 algebra;

C65:
    read-only consumer of C64 artifacts for the exact physical qg
    embedding.
```

A C64 artifact is valid only when it can be regenerated independently from the C62 source contracts and compared coefficient-by-coefficient with the C62 exact API.

---

# 2. Exact purpose

C64 must produce:

```text
a complete inventory of every C62 exact TM block required by the
physical trajectory;

canonical row- and column-basis manifests for every block;

one threshold-free exact coefficient-status object for every block;

canonical exact-expression records for every exact nonzero
coefficient;

per-block expression and support hashes;

deterministic exact-zero certificate summaries and hashes;

certified numerical sparse arrays descending from the exact
expressions;

per-entry or rigorously aggregated error bounds sufficient for
downstream isometry and round-trip certification;

deterministic runtime paths and reconstruction commands;

complete block, shell, longitudinal-partition, resolution, and
basis-order ancestry;

two-pass and clean-environment byte-for-byte reconstruction;

an end-to-end C62-API-to-C64-artifact equivalence test;

an immutable C65/QGEMBED3 read-only import contract.
```

C64 must not construct:

```text
the CM-ground physical qg injection;

the full color-triplet qg embedding;

a historical-basis physical adapter;

C52/C53/C57/C58 descendant-impact decisions;

C60 endpoint or witness support;

a direct-contact value or matrix;

a complete instantaneous-fermion operator.
```

The strongest allowed positive status is:

```text
C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY
```

The exact positive continuation is:

> **C65/QGEMBED3 — construct the exact CM-ground and color-triplet physical \(qg\) embedding and close descendant impact using the immutable C64 artifact bundle**

---

# 3. Scientific and software boundary

C64 is:

```text
exact-artifact specific;
C62-descendant specific;
finite-shell and longitudinal-partition resolved;
threshold free;
basis-order explicit;
numerically certified;
content addressed;
deterministic;
read-only-import enabling.
```

C64 is not:

```text
a new basis convention;

a change of physical regulator;

a change of C62 exact algebra;

a support-threshold tuning package;

a physical qg embedding;

a projected operator calculation;

a fit or renormalization calculation.
```

The artifact format must preserve the exact distinction among:

```text
ZERO_BY_EXACT_SHELL_RULE;

ZERO_BY_EXACT_M_RULE;

ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION;

NONZERO_EXACT_ALGEBRAIC.
```

No later consumer should need a floating tolerance to recover exact support.

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_mode_manifest.json

docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_qg_basis_manifest.json

docs/next_level/c60_exact_zero_semantics.json

docs/next_level/c61_implementation_report.md
docs/next_level/c61_missing_calculation_specification.md

docs/next_level/c62_implementation_report.md
docs/next_level/c62_derivation_authority_manifest.json
docs/next_level/c62_input_fidelity_audit.json
docs/next_level/c62_exact_representation_plan.json
docs/next_level/c62_exact_representation_decision.json
docs/next_level/c62_polar_ho_wavefunction_contract.json
docs/next_level/c62_circular_ladder_contract.json
docs/next_level/c62_polar_circular_phase_contract.json
docs/next_level/c62_exact_polar_cartesian_map.json
docs/next_level/c62_exact_two_mode_rotation.json
docs/next_level/c62_one_dimensional_bracket_contract.json
docs/next_level/c62_exact_circular_tm_contract.json
docs/next_level/c62_exact_polar_tm_contract.json
docs/next_level/c62_exact_expression_contract.json
docs/next_level/c62_algebraic_field_manifest.json
docs/next_level/c62_exact_tm_block_manifest.json
docs/next_level/c62_exact_tm_block_validation.json
docs/next_level/c62_tm_residue_ledger.json
docs/next_level/c62_tm_residue_reconciliation_report.json
docs/next_level/c62_certified_tm_export.json
docs/next_level/c62_precision_stability_report.json
docs/next_level/c62_api_contract.json
docs/next_level/c62_api_validation.json
docs/next_level/c62_provisional_descendant_impact.json
docs/next_level/c62_numerical_object_inventory.json
docs/next_level/c62_readiness_report.json

docs/next_level/c63_implementation_report.md
docs/next_level/c63_input_fidelity_audit.json
docs/next_level/c63_c62_import_report.json
docs/next_level/c63_missing_calculation_specification.md
docs/next_level/c63_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Read the implementation sources under the repository-equivalent of:

```text
src/deuteron_wigner/bridge/qgtm/
```

and identify the exact C62 public APIs and internal coefficient generators.

Create:

```text
docs/next_level/c64_derivation_authority_manifest.json
docs/next_level/c64_input_fidelity_audit.json
```

---

# 5. Freeze C62 source ownership

Before materializing one block, freeze:

```text
the C62 completion commit;

the exact source-file hashes for the polar/circular phase,
two-mode rotation, one-dimensional bracket, and polar TM
coefficient generators;

the exact public API signatures;

the exact coefficient-status vocabulary;

the exact basis-order generation functions;

the exact longitudinal-partition identities;

the exact algebraic expression representation;

the exact residue classifications.
```

Create a source fingerprint covering every executable C62 dependency needed to regenerate the blocks.

C64 must fail when:

```text
a C62 source file changes;

a public API signature changes;

the exact representation plan changes;

the phase formula changes;

the coefficient-status vocabulary changes;

the basis generator changes;

or the algebraic canonicalization changes.
```

Create:

```text
docs/next_level/c64_c62_source_fingerprint.json
docs/next_level/c64_c62_api_fingerprint.json
```

---

# 6. Complete block census

Enumerate every exact TM block required by the physical trajectory.

A block identity must include at least:

```text
resolution ID;

K;

Nmax;

bHO;

longitudinal-partition ID;

k_q and k_g;

x_q and x_g as exact rationals;

total transverse shell;

total m or the exact angular-momentum block label;

input/raw basis family;

output relative/CM basis family;

matrix orientation;

C62 expression-plan ID.
```

Do not infer the block census from runtime files that do not yet exist.

Derive it from the committed C45/C47/C62 basis and partition generators.

For each resolution report:

```text
longitudinal-partition count;

shell-block count;

m-block count;

matrix count;

total row-state count;

total column-state count;

candidate coefficient count;

exact-zero count;

exact-nonzero count.
```

Create:

```text
docs/next_level/c64_exact_tm_block_census.json
docs/next_level/c64_block_coverage_report.json
```

A positive gate requires complete coverage of every C62 coefficient required for the later CM-ground embedding.

---

# 7. Canonical block identifiers

Define a deterministic block identifier from canonical scientific fields, not from array position or filesystem order.

For example:

```text
C64:QGTM2:
RES=<resolution_id>:
PART=<partition_id>:
SHELL=<N_total>:
M=<m_total>:
ORIENT=<raw_to_relcm_or_inverse>
```

Use the repository naming conventions where available.

The ID must remain stable under:

```text
parallel execution;

filesystem traversal order;

Python dictionary order;

temporary-directory changes;

runtime destination changes.
```

Create:

```text
docs/next_level/c64_block_identity_contract.json
```

---

# 8. Row- and column-basis manifests

For every block, materialize canonical ordered row and column basis records.

Each basis record must retain:

```text
basis ID;

side: row or column;

polar labels;

circular occupations;

total shell;

m;

longitudinal-partition ID;

raw q/g labels or relative/CM labels;

CM labels where present;

basis-order index;

source ancestry.
```

Serialize the records canonically.

Compute:

```text
row_basis_sha256;

column_basis_sha256;

combined_basis_order_sha256.
```

A block is not importable without all three hashes.

Required checks:

```text
no duplicate basis ID;

no missing basis ID;

index sequence complete;

basis-order reconstruction independent of hash-table order;

row and column counts equal the C62 block declaration;

exact shell and m labels agree.
```

Create:

```text
docs/next_level/c64_basis_order_contract.json
docs/next_level/c64_basis_order_manifest.json
docs/next_level/c64_basis_order_validation.json
```

---

# 9. Canonical exact coefficient record

For every candidate coefficient in a block, define a canonical record containing:

```text
block ID;

row basis ID;

column basis ID;

terminal exact status;

selection-rule ancestry;

exact construction-expression record;

exact reduced-expression record when nonzero;

expression-plan ID;

C62 source-function fingerprint.
```

The canonical construction expression must be deterministic and must not depend on pretty printing.

Acceptable representations include:

```text
a project-native exact AST;

a normalized sparse binomial/factorial/radical term list;

a canonical AlgebraicNumber coefficient representation;

or another exact deterministic representation already guaranteed by
the C62 contract.
```

A raw `str(expr)`, pretty-printed LaTeX, or version-unstable object repr is not sufficient by itself.

For exact zeros, retain a canonical zero certificate rather than omitting the coefficient from the expression-level hash.

Create:

```text
docs/next_level/c64_exact_coefficient_record_contract.json
docs/next_level/c64_exact_zero_certificate_contract.json
```

---

# 10. Per-block expression hash

Compute a per-block expression hash over the ordered coefficient records:

\[
H_{\rm expr}^{(B)}
=
\operatorname{SHA256}
\left[
\operatorname{canonical}
\left(
(\mathrm{rowID},\mathrm{colID},\mathrm{status},
 \mathrm{exactRecord})
\right)_{\rm ordered}
\right].
\]

This hash must include:

```text
exact zeros;

exact nonzeros;

basis IDs;

coefficient status;

construction and reduced expression identities;

block orientation.
```

It must not depend on:

```text
floating numerical evaluation;

sparse storage;

thresholds;

runtime paths;

compression timestamps.
```

Also compute a package-level Merkle root or ordered aggregate hash over all block expression hashes.

Create:

```text
docs/next_level/c64_expression_hash_manifest.json
docs/next_level/c64_expression_merkle_report.json
```

---

# 11. Per-block exact-support artifact

Materialize a threshold-free support/status artifact for every block.

It must encode every candidate coefficient's terminal status, not merely a Boolean nonzero mask.

Use a deterministic status code table such as:

```text
0 = ZERO_BY_EXACT_SHELL_RULE;
1 = ZERO_BY_EXACT_M_RULE;
2 = ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION;
3 = NONZERO_EXACT_ALGEBRAIC.
```

Use the actual C62 vocabulary and stable codes.

The support artifact may be represented as:

```text
a dense compact integer status array;

a sparse nonzero structure plus complete exact-zero rule tables;

or another lossless deterministic representation.
```

It must be possible to reconstruct one terminal status for every row/column pair without invoking C62.

Compute:

```text
status_artifact_sha256;

boolean_nonzero_support_sha256;

zero_certificate_sha256;

support_aggregate_sha256.
```

The Boolean support is a derived export. The status artifact is authoritative.

Create:

```text
docs/next_level/c64_exact_support_artifact_contract.json
docs/next_level/c64_exact_support_hash_manifest.json
docs/next_level/c64_support_reconstruction_report.json
```

---

# 12. Exact nonzero expression table

Materialize the canonical exact expression for every `NONZERO_EXACT_ALGEBRAIC` entry.

The table must be keyed by:

```text
block ID;

row basis ID;

column basis ID.
```

The table must allow C65 to:

```text
retrieve an exact expression;

verify its expression hash;

evaluate it at arbitrary precision;

recover its exact support without a threshold.
```

Do not require C65 to call the C62 coefficient generator.

Heavy expression tables may remain outside Git under the C64 runtime root, but their content hashes, record counts, schemas, and paths must be committed.

Create:

```text
docs/next_level/c64_exact_expression_table_manifest.json
docs/next_level/c64_exact_expression_table_validation.json
```

---

# 13. Certified numerical export plans

Compile mutually exclusive numerical-certification plans.

## 13.1 `QGTM2-ARB-DIRECTED-INTERVAL`

Evaluate exact expressions with an Arb-compatible or equivalent directed-rounding interval backend.

Export a midpoint and rigorous radius.

## 13.2 `QGTM2-EXACT-RADICAL-BOUND`

Use exact rational/radical bounds and directed rounding to produce a rigorous enclosure.

## 13.3 `QGTM2-DUAL-BACKEND-CONSERVATIVE-BOUND`

Use two genuinely independent arbitrary-precision backends plus a mathematically justified conservative enclosure that is guaranteed to contain the exact value.

This plan is valid only when the guarantee is explicit; numerical agreement alone is not an error certificate.

## 13.4 `QGTM2-NUMERICAL-CERTIFICATION-UNAVAILABLE`

Exact expressions and support may be materialized, but required numerical bounds cannot be supplied.

Select exactly one primary plan before exporting arrays.

Do not label:

```text
difference between 128-bit and 256-bit values;

agreement between two ordinary floating evaluations;

or a residual against C47 quadrature
```

as a rigorous error bound without a proof.

Create:

```text
docs/next_level/c64_numerical_certification_plan.json
docs/next_level/c64_numerical_certification_decision.json
```

---

# 14. Certified sparse numerical arrays

For each block, export deterministic sparse arrays containing only exact nonzeros.

Use a deterministic format that avoids timestamp-dependent archives.

A recommended block directory is:

```text
data/runtime/c64_qgtm2/<block_id>/
    indptr.npy
    indices.npy
    data_real.npy
    data_imag.npy
    abs_error.npy
```

or a repository-equivalent deterministic representation.

For every stored nonzero, retain:

```text
row index;

column index;

rounded complex value;

rigorous absolute error bound;

exact expression hash;

exact status.
```

Exact zeros must not appear as small numerical values.

Compute independent hashes for:

```text
indptr;

indices;

data_real;

data_imag;

abs_error;

combined sparse block.
```

Create:

```text
docs/next_level/c64_certified_sparse_array_contract.json
docs/next_level/c64_certified_array_hash_manifest.json
```

---

# 15. Precision and bound policy

Freeze:

```text
working precision;

rounding mode;

output dtype;

midpoint/radius convention;

complex-error convention;

underflow and overflow policy;

serialization endianness;

NaN/Inf prohibition.
```

A recommended default export is:

```text
float64 complex midpoint represented by separate real/imag arrays;

float64 or higher-precision absolute error bound guaranteed to cover
both exact-to-high-precision evaluation and high-precision-to-float64
rounding.
```

The certification backend may retain a higher-precision internal record.

Required checks:

```text
the exact value lies inside every exported interval;

precision doubling preserves support;

precision doubling produces nested or mutually consistent intervals;

all nonzero intervals exclude zero when a nonzero certificate is
claimed;

no exact zero is exported through interval evaluation;

all isometry residuals are bounded by propagated entry errors.
```

Create:

```text
docs/next_level/c64_precision_and_rounding_contract.json
docs/next_level/c64_precision_stability_report.json
docs/next_level/c64_error_bound_validation.json
```

---

# 16. Runtime artifact paths

Define one deterministic runtime root:

```text
data/runtime/c64_qgtm2/
```

Every block must have a committed relative-path record for:

```text
row basis manifest;

column basis manifest;

status artifact;

exact expression table;

sparse indices;

sparse pointers;

numerical real values;

numerical imaginary values;

error bounds;

block metadata.
```

Paths must be relative to the repository root.

Do not commit machine-specific absolute paths.

The inventory must record the exact generator command required to recreate every block and the complete package.

Create:

```text
docs/next_level/c64_runtime_path_manifest.json
docs/next_level/c64_reconstruction_command_manifest.json
```

---

# 17. Per-block metadata record

Every block metadata record must include:

```text
schema version;

block ID;

resolution ID;

longitudinal-partition ID;

shell/m block labels;

orientation;

shape;

row count;

column count;

candidate coefficient count;

exact-zero counts by class;

exact-nonzero count;

row/column/basis hashes;

expression hash;

support hashes;

sparse-array hashes;

error-bound hashes;

runtime paths;

generator command;

C62 source fingerprint;

C64 generation commit placeholder or descendant identity.
```

The commit cannot contain its own final hash. Use a declared descendant-completion identity strategy consistent with earlier packages.

Create:

```text
docs/next_level/c64_block_metadata_manifest.json
```

---

# 18. Package-level inventory

Create a complete package inventory with one row per runtime artifact.

The inventory must support:

```text
lookup by block ID;

lookup by resolution and partition;

lookup by artifact type;

verification of expected file size;

verification of SHA-256;

verification of shape and dtype;

detection of missing, duplicated, or orphaned files.
```

Create:

```text
docs/next_level/c64_numerical_object_inventory.json
docs/next_level/c64_runtime_completeness_report.json
```

A positive gate requires:

```text
missing artifact count = 0;

duplicate artifact identity count = 0;

orphan artifact count = 0;

unhashed artifact count = 0.
```

---

# 19. Complete coefficient-by-coefficient equivalence

For every block and every candidate coefficient:

1. Evaluate or classify it through the C62 exact public API.
2. Read the corresponding C64 artifact record.
3. Compare:
   - basis IDs;
   - exact status;
   - exact construction-expression record;
   - exact reduced-expression identity;
   - support decision;
   - numerical interval where nonzero.

Require exact equality for symbolic/status records.

Require the C62 arbitrary-precision numerical evaluation to lie inside the C64 certified interval.

Create:

```text
docs/next_level/c64_c62_coefficient_equivalence_report.json
```

A sampled comparison is insufficient. The complete physical-trajectory coefficient domain must be checked.

---

# 20. Block-action equivalence

Implement a read-only C64 block action that loads only the materialized artifact bundle.

Compare it against an independent direct C62 exact-generator action on:

```text
every basis vector for tractable blocks;

deterministic complex superpositions;

random normalized complex vectors;

all blocks and resolutions;

multiple higher-precision evaluations.
```

The C64 action must not call the C62 coefficient API.

The direct C62 route must not load the C64 sparse arrays.

Compare with propagated numerical error bounds.

Create:

```text
docs/next_level/c64_block_action_api.json
docs/next_level/c64_block_action_equivalence_report.json
```

---

# 21. Exact block invariants

Using the exact expressions and statuses, verify inherited C62 block properties:

```text
shell conservation;

m conservation;

rank and nullity;

exact nonzero counts;

exact row and column norm identities;

exact or algebraically certified unitarity/isometry;

inverse orientation;

basis-order independence.
```

Then verify that the certified numerical arrays satisfy the same properties within propagated bounds.

Create:

```text
docs/next_level/c64_exact_block_invariant_report.json
docs/next_level/c64_certified_block_invariant_report.json
```

Do not replace an exact invariant with a numerical tolerance when exact records are available.

---

# 22. Historical residue artifactization

Materialize the C62 residue reconciliation as an importable, content-addressed artifact.

For every one of the historical:

```text
4,032 / 15,840 / 48,048
```

residues retain:

```text
historical basis IDs;

historical value;

exact block ID;

exact row/column IDs;

exact status ZERO_BY_EXACT_M_RULE;

exact zero-certificate hash;

historical threshold decision;

C62 expression/support ancestry.
```

Compute per-resolution and aggregate hashes.

Create:

```text
docs/next_level/c64_residue_certificate_manifest.json
docs/next_level/c64_residue_certificate_validation.json
```

C65 must be able to verify the residue classification without re-running the historical quadrature or C62 algebra.

---

# 23. Basis-order compatibility for C65

Construct a C65-facing basis-order crosswalk covering:

```text
raw q/g polar input basis;

relative/CM output basis;

shell/m block order;

full per-partition order;

full per-resolution order.
```

The crosswalk must permit deterministic assembly of CM-ground columns in C65 without guessing block concatenation order.

Record:

```text
global row offset;

global column offset;

block-local index;

global basis ID;

partition ID;

shell/m block ID.
```

Create:

```text
docs/next_level/c64_c65_basis_crosswalk.json
docs/next_level/c64_c65_basis_crosswalk_validation.json
```

---

# 24. Read-only import API

Create a C64-owned API equivalent to:

```python
list_tm_blocks(
    resolution_id: str | None = None,
    longitudinal_partition_id: str | None = None,
) -> tuple[TMBlockArtifactRecord, ...]

load_tm_block_metadata(
    block_id: str,
) -> TMBlockArtifactRecord

load_tm_block_support(
    block_id: str,
) -> ExactTMStatusArtifact

load_tm_block_exact_expressions(
    block_id: str,
) -> ExactTMExpressionTable

load_tm_block_certified_sparse(
    block_id: str,
) -> CertifiedSparseTMBlock

apply_tm_block(
    block_id: str,
    vector,
) -> CertifiedVectorResult
```

The import API must:

```text
verify hashes before returning data;

return immutable/read-only arrays;

expose exact statuses separately from numerical values;

expose basis-order manifests;

expose error bounds;

never call the C62 coefficient generator.
```

Create:

```text
docs/next_level/c64_api_contract.json
docs/next_level/c64_api_validation.json
```

---

# 25. C65/QGEMBED3 import contract

Define the exact contract by which C65 will consume:

```text
the C62 source fingerprint through the C64 package;

the complete block census;

block identities;

row and column basis manifests;

basis-order hashes and global crosswalk;

per-block exact status artifacts;

per-block expression hashes;

exact nonzero expression tables;

certified sparse numerical blocks and error bounds;

residue certificates;

runtime paths and generator commands;

package aggregate hashes;

block-action API.
```

C65 must verify every hash before constructing a CM-ground column or physical embedding.

C65 may not:

```text
call C62 to regenerate a missing block;

change a basis order;

introduce a threshold;

replace an exact expression with a historical quadrature value;

or continue when a runtime artifact is absent.
```

Create:

```text
docs/next_level/c64_c65_qgembed3_import_contract.json
```

---

# 26. Deterministic reconstruction

Run at least:

```text
two consecutive full artifact builds in the same environment;

one clean temporary-runtime rebuild;

one serial build;

one declared parallel/sharded build, when parallel generation is
supported;

one restart/resume build from a partial valid runtime tree.
```

Require byte-identical final artifacts and manifests.

A restart may reuse a block only after all source, basis, expression, support, and array hashes pass.

Do not use nondeterministic archive timestamps.

Create:

```text
docs/next_level/c64_deterministic_reconstruction_report.json
docs/next_level/c64_restart_parallel_report.json
```

---

# 27. Environment and dependency lock

Record the exact environment needed to reproduce canonical expressions and certified arrays:

```text
Python version;

SymPy or project-AST version;

interval/certification backend version;

NumPy version;

endianness;

relevant locale and hash-seed settings;

parallelism settings.
```

Canonical exact expression hashes must be either:

```text
independent of these versions by project-native serialization;

or explicitly tied to a locked serializer version.
```

Create:

```text
docs/next_level/c64_environment_manifest.json
docs/next_level/c64_serializer_version_contract.json
```

Changing a serializer version without supersession must fail the import gate.

---

# 28. Count-once and provenance

Report:

```text
expected block count;

materialized block count;

expected candidate coefficient count;

materialized status count;

exact nonzero expression count;

certified numerical nonzero count;

exact-zero certificate count;

basis-record count;

runtime-artifact count;

missing count;

duplicate count;

orphan count;

hash mismatch count.
```

Every materialized coefficient must have exactly one ancestry path:

```text
C62 source fingerprint
 -> block ID
 -> basis pair
 -> exact status/expression
 -> certified numerical entry where nonzero
 -> runtime artifact hash.
```

Create:

```text
docs/next_level/c64_artifact_ancestry_ledger.json
docs/next_level/c64_count_once_report.json
```

A positive gate requires all error counts to be zero.

---

# 29. Isolation and poisoning controls

Prove that C64 construction is unchanged when:

```text
all historical C47 quadrature values are poisoned;

all historical argmax phases are poisoned;

the historical 1e-12 threshold changes;

all C47 canonical tuples are poisoned;

all C50/C52/C53 numerical matrices are poisoned;

all C57/C58 numerical objects are poisoned;

all ART25 files are inaccessible.
```

The build must fail when:

```text
a C62 source fingerprint changes;

a C62 exact status changes;

a basis-order record changes;

a coefficient expression changes;

a support artifact changes;

a runtime path is missing;

an array hash changes;

an error bound is removed;

the certification backend changes without supersession;

a threshold is introduced;

a consumer attempts to call C62 through the C64 import API.
```

Create:

```text
docs/next_level/c64_isolation_report.json
```

---

# 30. End-to-end C62-source-to-C64-artifact test

Implement an end-to-end test that begins from the immutable C62 source contracts—not from prebuilt C64 files.

It must:

```text
verify C62 source fingerprints;

derive the complete block census;

construct row and column basis manifests;

enumerate every coefficient;

materialize exact status and expression records;

compute per-block and aggregate hashes;

select the numerical-certification plan;

export certified sparse arrays and error bounds;

write deterministic runtime paths and metadata;

load all artifacts through the C64 read-only API;

compare every coefficient against C62;

compare block actions;

verify exact and certified invariants;

verify residue certificates;

verify the C65 basis crosswalk;

rebuild all artifacts byte-for-byte.
```

It must fail when:

```text
a required block is omitted;

a zero coefficient is absent from the status hash domain;

a nonzero expression is absent;

a basis manifest is reordered;

an exact status is inferred from magnitude;

a numerical value has no bound;

a runtime path is unrecorded;

C65 would need to call C62;

an artifact is regenerated inside the read-only loader;

a hash or byte sequence changes.
```

---

# 31. Focused mutation tests

Create at least **256 focused live mutations** of actual source fingerprints, basis records, expressions, statuses, arrays, bounds, paths, or import objects.

Include mutations of:

```text
C62 source hash;

phase formula identity;

longitudinal partition;

block ID;

shell label;

m label;

matrix orientation;

row basis ID;

column basis ID;

basis order;

coefficient status;

zero certificate;

exact expression term;

expression hash;

support hash;

CSR indptr;

CSR index;

numerical real value;

numerical imaginary value;

error bound;

working precision;

serializer version;

runtime path;

generator command;

residue certificate;

package Merkle root;

C65 basis crosswalk;

read-only array flag;

restart reuse decision.
```

Every mutation must fail a concrete source, exact-status, expression, basis, certification, path, count-once, import, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 32. Readiness gate

Issue:

```text
C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY
```

only when:

```text
the full C63 baseline reproduces;

the C63 import no-go remains explicit;

the C62 positive scientific status remains unchanged;

all C62 source fingerprints are frozen;

the complete required block census exists;

every block has canonical row and column basis manifests;

every block has basis-order hashes;

every candidate coefficient has one exact terminal status;

every block has an expression hash covering zeros and nonzeros;

every block has a threshold-free support/status artifact and hash;

every exact nonzero has a canonical exact-expression record;

one rigorous numerical-certification plan is selected;

every exact nonzero has a certified numerical value and error bound;

all numerical arrays have deterministic paths and hashes;

all block metadata and package inventories are complete;

all 4,032 / 15,840 / 48,048 residue certificates are materialized;

every coefficient agrees with the C62 exact API;

block actions agree within certified bounds;

exact and certified block invariants close;

the C65 basis crosswalk is complete;

the read-only import API verifies hashes and calls no C62 generator;

the C65 import contract is complete;

two-pass, clean, serial/parallel, and restart reconstruction passes;

count-once and provenance close;

poisoning controls pass;

the end-to-end source-to-artifact test passes.
```

Do not issue:

```text
C64_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY;

C64_IFERM_CONTACT_SUPPORT_READY;

C64_DIRECT_IFERM_CONTACT_READY;

C64_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C64_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY.
```

---

# 33. Exact no-go branches

## A. C62 source or API fingerprint is incomplete

```text
C64_QGTM2_C62_SOURCE_FINGERPRINT_INCOMPLETE
```

Next:

> **C65/QGTM-SRC — exact C62 source, API, serializer, and dependency fingerprint completion**

## B. The block census or basis order is incomplete

```text
C64_QGTM2_BLOCK_BASIS_INVENTORY_INCOMPLETE
```

Next:

> **C65/QGTM-BASIS — complete block enumeration, row/column basis manifests, and global crosswalk**

## C. Canonical expression serialization is incomplete

```text
C64_QGTM2_EXPRESSION_SERIALIZATION_INCOMPLETE
```

Next:

> **C65/QGTM-EXPR — project-native exact AST, coefficient record, and expression-hash completion**

## D. Exact support artifacts are incomplete

```text
C64_QGTM2_SUPPORT_CERTIFICATE_INCOMPLETE
```

Next:

> **C65/QGTM-SUPPORT — complete coefficient-status, exact-zero certificate, and support-hash materialization**

## E. Numerical certification is incomplete

```text
C64_QGTM2_NUMERICAL_CERTIFICATION_INCOMPLETE
```

Next:

> **C65/QGTM-CERT — directed interval evaluation, error bounds, and precision-stability completion**

## F. Runtime inventory or reconstruction is incomplete

```text
C64_QGTM2_RUNTIME_INTEGRITY_INCOMPLETE
```

Next:

> **C65/QGTM-RUNTIME — deterministic paths, artifact inventory, restart, and byte-reconstruction completion**

## G. C62/artifact equivalence fails

```text
C64_QGTM2_ARTIFACT_EQUIVALENCE_FAILED
```

Next:

> **C65/QGTM-XCHECK — coefficient, block-action, basis-order, and exact-invariant reconciliation**

## H. Artifact integrity closes

```text
C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY
```

Next:

> **C65/QGEMBED3 — exact physical qg embedding and descendant-impact closure**

---

# 34. Required deliverables

Create at least:

```text
docs/next_level/c64_implementation_report.md
docs/next_level/c64_api.md
docs/next_level/c64_derivation_authority_manifest.json
docs/next_level/c64_input_fidelity_audit.json

docs/next_level/c64_c62_source_fingerprint.json
docs/next_level/c64_c62_api_fingerprint.json
docs/next_level/c64_exact_tm_block_census.json
docs/next_level/c64_block_coverage_report.json
docs/next_level/c64_block_identity_contract.json

docs/next_level/c64_basis_order_contract.json
docs/next_level/c64_basis_order_manifest.json
docs/next_level/c64_basis_order_validation.json

docs/next_level/c64_exact_coefficient_record_contract.json
docs/next_level/c64_exact_zero_certificate_contract.json
docs/next_level/c64_expression_hash_manifest.json
docs/next_level/c64_expression_merkle_report.json

docs/next_level/c64_exact_support_artifact_contract.json
docs/next_level/c64_exact_support_hash_manifest.json
docs/next_level/c64_support_reconstruction_report.json
docs/next_level/c64_exact_expression_table_manifest.json
docs/next_level/c64_exact_expression_table_validation.json

docs/next_level/c64_numerical_certification_plan.json
docs/next_level/c64_numerical_certification_decision.json
docs/next_level/c64_certified_sparse_array_contract.json
docs/next_level/c64_certified_array_hash_manifest.json
docs/next_level/c64_precision_and_rounding_contract.json
docs/next_level/c64_precision_stability_report.json
docs/next_level/c64_error_bound_validation.json

docs/next_level/c64_runtime_path_manifest.json
docs/next_level/c64_reconstruction_command_manifest.json
docs/next_level/c64_block_metadata_manifest.json
docs/next_level/c64_numerical_object_inventory.json
docs/next_level/c64_runtime_completeness_report.json

docs/next_level/c64_c62_coefficient_equivalence_report.json
docs/next_level/c64_block_action_api.json
docs/next_level/c64_block_action_equivalence_report.json
docs/next_level/c64_exact_block_invariant_report.json
docs/next_level/c64_certified_block_invariant_report.json

docs/next_level/c64_residue_certificate_manifest.json
docs/next_level/c64_residue_certificate_validation.json
docs/next_level/c64_c65_basis_crosswalk.json
docs/next_level/c64_c65_basis_crosswalk_validation.json

docs/next_level/c64_api_contract.json
docs/next_level/c64_api_validation.json
docs/next_level/c64_c65_qgembed3_import_contract.json

docs/next_level/c64_deterministic_reconstruction_report.json
docs/next_level/c64_restart_parallel_report.json
docs/next_level/c64_environment_manifest.json
docs/next_level/c64_serializer_version_contract.json

docs/next_level/c64_artifact_ancestry_ledger.json
docs/next_level/c64_count_once_report.json
docs/next_level/c64_isolation_report.json

docs/next_level/c64_readiness_report.json
docs/next_level/c64_source_sufficiency_decision.json
docs/next_level/c64_no_go_decision_tree.json
docs/next_level/c64_missing_calculation_specification.md
docs/next_level/c64_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/qgtm2/
```

or the repository-equivalent package.

Add focused tests for:

```text
C62 source/API fingerprints;
block census;
basis-order manifests;
canonical coefficient serialization;
expression hashes;
exact support artifacts;
zero certificates;
numerical interval certification;
sparse array hashes;
runtime paths;
C62 coefficient equivalence;
block-action equivalence;
exact and certified invariants;
residue certificates;
C65 crosswalk;
read-only import;
restart and deterministic reconstruction;
end-to-end source-to-artifact closure.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All committed JSON and every regenerated runtime artifact must reproduce byte-for-byte.

---

# 35. Acceptance criteria

C64 is complete only when:

1. The full C63 baseline reproduces.
2. The C63 fail-closed status remains explicit.
3. The C62 positive scientific status remains unchanged.
4. C62 historical artifacts remain unchanged.
5. C43/C45/C47 historical artifacts remain unchanged.
6. C52/C53/C57/C58 historical artifacts remain unchanged.
7. C40 remains method-oracle only.
8. No historical quadrature value defines an artifact.
9. The historical \(10^{-12}\) threshold cannot change exact support.
10. No physical coupling, subtraction, counterterm, contact, or embedding is created.
11. Every required C62 source file has a frozen hash.
12. Every required C62 API has a frozen signature.
13. The serializer version is explicit.
14. The complete physical-trajectory block census exists.
15. Every block has a stable scientific ID.
16. Every block has complete row and column basis manifests.
17. Every block has row, column, and combined basis-order hashes.
18. Every candidate coefficient has one exact terminal status.
19. Exact zeros are represented in the expression-hash domain.
20. Every exact nonzero has a canonical expression record.
21. Every block has a deterministic expression hash.
22. Every block has a threshold-free status artifact.
23. Every block has support and zero-certificate hashes.
24. The package has ordered aggregate or Merkle hashes.
25. One rigorous numerical-certification plan is selected.
26. Numerical agreement alone is not mislabeled a rigorous bound.
27. Every exact nonzero has a certified numerical enclosure.
28. Every claimed nonzero enclosure excludes zero.
29. Exact zeros are not numerically evaluated into tiny entries.
30. Every sparse array has deterministic indices and pointers.
31. Every numerical and error array has a SHA-256 hash.
32. Every runtime artifact has a committed relative path.
33. Every runtime artifact has a generator command.
34. Block metadata are complete.
35. The package inventory has no missing, duplicate, orphan, or unhashed artifact.
36. Every coefficient agrees exactly with the C62 status/expression API.
37. Every C62 high-precision value lies inside the C64 certified interval.
38. C64 block actions call no C62 generator.
39. Direct C62 and read-only C64 block actions agree within bounds.
40. Exact block invariants close.
41. Certified numerical invariants close within propagated bounds.
42. All 4,032/15,840/48,048 residue certificates are materialized.
43. The C65 global basis crosswalk is complete.
44. The read-only import API verifies hashes.
45. Imported arrays are immutable.
46. The read-only import API never regenerates a missing artifact.
47. The C65 import contract is complete.
48. Two consecutive builds are byte-identical.
49. A clean runtime rebuild is byte-identical.
50. Serial and declared parallel builds agree.
51. Restart/reuse accepts only fully verified blocks.
52. Environment and dependency identities are recorded.
53. Every artifact has complete ancestry.
54. Duplicate, missing, orphan, and hash-mismatch counts are zero.
55. Static and runtime poisoning controls pass.
56. End-to-end source-to-artifact reconstruction passes.
57. At least 256 focused live mutations are detected.
58. No CM-ground/triplet physical embedding is claimed.
59. No descendant support or operator status is promoted.
60. No endpoint relation, witness relation, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
61. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
62. `MSHT20_REP/` remains untouched and outside Git.
63. The working tree is clean except for the pre-existing untracked directory.
64. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken expression canonicalization, exact-support completeness, numerical certification, basis-order integrity, runtime-path completeness, or read-only import semantics to open the gate.

---

# 36. Final Codex response

Report:

- full starting and final commits;
- exact C62 source and API fingerprints;
- serializer and certification backend versions;
- block counts by resolution, partition, shell, and \(m\);
- candidate, exact-zero-by-class, and exact-nonzero coefficient counts;
- row/column basis counts and basis-order hashes;
- per-block and aggregate expression hashes;
- per-block support, Boolean-support, and zero-certificate hashes;
- exact-expression table record counts and hashes;
- selected numerical-certification plan;
- working precision, output dtype, rounding policy, and error-bound convention;
- sparse array shapes, nnz, hashes, and maximum certified errors;
- runtime paths and generator commands;
- missing, duplicate, orphan, and unhashed artifact counts;
- complete C62 coefficient-equivalence result;
- block-action residuals and propagated bounds;
- exact and certified block-invariant residuals;
- residue-certificate counts and hashes for 4,032/15,840/48,048 entries;
- C65 basis-crosswalk counts and hashes;
- read-only API validation;
- serial, parallel, clean, restart, and two-pass deterministic results;
- environment and dependency identities;
- ancestry and count-once results;
- isolation and poisoning results;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no physical qg embedding, descendant support promotion, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an in-memory C62 recomputation, an unhashed expression table, a support mask without exact statuses, a numerical array without certified bounds, a basis order inferred by a consumer, a machine-specific path, or a loader that silently regenerates missing data as a complete read-only exact-TM artifact package.
