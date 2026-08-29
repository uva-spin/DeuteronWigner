# C68/QGCOLOR-RUNTIME Codex Work Package

## Title

**Immutable runtime closure for the exact C66 triplet isometry: canonical basis and expression records, certified \(U_3\), \(U_3^\dagger\), and \(P_3\) arrays, hash-verifying read-only API, deterministic inventory, and C69 physical-embedding import contract**

## Authoritative baseline

Start from the clean local C67/QGEMBED4 fail-closed completion commit:

```text
7a30916b1dd1a91603b7ab3def7408ceb70f7991
```

The required scientific ancestor is the positive C66 completion:

```text
8f8240ff2c5cb2615ee68ba10331b9732dd84ca6
```

The required exact-TM artifact ancestor remains:

```text
6f74663f3a70e853940665c30b1561766b6b75a3
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 8f8240ff2c5cb2615ee68ba10331b9732dd84ca6 HEAD
git merge-base --is-ancestor 6f74663f3a70e853940665c30b1561766b6b75a3 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY

C66_SOURCE_DERIVED_TRIPLET_ISOMETRY_ARTIFACT_READY

C67_QGEMBED_C66_IMPORT_INCOMPLETE
```

and the exact C67 finding:

```text
C64 import:
    immutable read-only import passes;
    733 exact TM blocks;
    171,153 exact coefficient statuses;
    67,920 residue certificates;

C66 scientific result:
    exact C53-convention 24 x 3 triplet isometry exists;
    U3 = E_src / sqrt(C_F);
    exact Gram normalization;
    all-eight-generator intertwining;
    rank-three image projector;
    zero anti-sextet and 15 leakage;

C66 downstream runtime gap:
    no hash-verifying read-only loader;
    no immutable-array interface;
    no complete runtime inventory;
    no committed array hashes;
    no committed numerical-bound hashes;
    calling C66 build() would regenerate the object and violates
    C67 read-only import semantics;

C67 consequence:
    no physical qg embedding;
    no direct-contact support;
    no descendant-impact audit.
```

Verify every statement from the committed C66 and C67 source, reports, tests, and manifests rather than relying on this prompt.

The exact C66 scientific identity is immutable:

\[
U_3=\frac{E_{\rm src}}{\sqrt{C_F}},
\qquad
C_F=\frac43,
\qquad
U_3^\dagger U_3=I_3,
\qquad
P_3=U_3U_3^\dagger .
\]

The C53 product-color row order, retained-triplet column order, generator signs, column phases, normalization, support statuses, and projector convention must remain exactly those established by C66.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Scientific correction and ownership

C68 is an **artifactization and read-only import package**, not a new SU(3) derivation.

C66 owns the scientific result:

```text
the source-derived exact triplet isometry;
its normalization;
its intertwiner identities;
its projector;
its representation leakage tests.
```

C68 owns the complete downstream runtime realization of that immutable result:

```text
canonical exact records;
content hashes;
certified numerical arrays and bounds;
deterministic runtime paths;
a loader that verifies and returns immutable objects;
a complete inventory;
and an import contract for C69.
```

C68 must not:

```text
change one C66 exact entry;

change one row or column basis identity;

choose a new column phase;

renormalize raw_emission_E;

factor a 24 x 24 projector to redefine U3;

use numerical QR, SVD, or eigendecomposition to choose the triplet
basis;

silently edit C66 historical artifacts;

or claim that a C68 runtime file was already present in C66.
```

A C68 artifact is valid only when it is regenerated from the immutable C66 constructors and compared entry-by-entry and invariant-by-invariant with the C66 exact result.

---

# 2. Execution mandate

The missing objects identified by C67 are concrete and finite:

```text
a complete exact runtime bundle for the 72 U3 entries;

certified numerical U3, U3-dagger, and P3 arrays;

committed basis, expression, support, array, and bound hashes;

deterministic relative paths;

a complete numerical-object inventory;

a hash-verifying read-only loader;

immutable returned arrays;

and a C69 import contract.
```

C68 must complete those objects in this package.

Do not split the work into another metadata-only preparatory package unless a concrete scientific inconsistency in the C66 exact result is found. Missing convenience prose, a preferred filename, or a desire for an additional summary is not a valid no-go.

---

# 3. Exact purpose

C68 must produce:

```text
a frozen fingerprint of every C66 source/API dependency needed to
regenerate the color artifact;

canonical product-color row and retained-triplet column basis
manifests;

a complete 72-entry exact status table;

a complete exact-expression table for all nonzero U3 entries;

exact-zero certificates for every zero U3 entry;

canonical expression, status, support, basis, and aggregate hashes;

materialized exact or canonical records for E_src, the Gram matrix,
the triplet basis adapter, U3, U3-dagger, and P3;

certified numerical arrays with explicit error bounds;

deterministic runtime paths and reconstruction commands;

a complete runtime and object inventory;

a read-only API that verifies every hash and regenerates nothing;

independent read-only embedding, projection, and projector actions;

complete C66-to-C68 entry and invariant equivalence;

serial, clean, repeated, restart, and supported parallel
reconstruction closure;

a C69/QGEMBED5 import contract;

and a dry import preflight proving that the exact C67 import blocker
is resolved without constructing the physical qg embedding.
```

C68 must not construct:

```text
the C64 CM-ground kinematic embedding;

the full kinematic-times-color physical qg embedding;

C47/C52/C53/C57/C58 descendant-impact decisions beyond confirming
the inherited C66 C53-impact status;

C60 endpoint or witness relations;

a direct-contact value or matrix;

a complete instantaneous-fermion operator;

a Wilson/TMD or matching object.
```

The strongest positive status is:

```text
C68_SOURCE_DERIVED_TRIPLET_RUNTIME_ARTIFACTS_READY
```

The exact positive continuation is:

> **C69/QGEMBED5 — construct the exact CM-ground and color-triplet physical \(qg\) embedding and close descendant impact using immutable C64 and C68 runtime packages**

---

# 4. Mandatory inputs

Inventory and read every tracked C66 artifact and implementation source using commands equivalent to:

```bash
git ls-files 'docs/next_level/c66*'
git ls-files 'src/deuteron_wigner/**/qgcolor2*'
git ls-files 'scripts/*c66*'
git ls-files 'tests/*c66*'
```

Read completely the actual repository equivalents of:

```text
docs/next_level/c66_implementation_report.md
docs/next_level/c66_derivation_authority_manifest.json
docs/next_level/c66_input_fidelity_audit.json

the exact SU(3) generator manifest;
the product-color basis manifest;
the retained-triplet basis manifest;
the triplet basis adapter;
the source color-emission map;
the exact Gram result;
the normalization decision;
the exact triplet-isometry record;
the isometry validation;
the intertwiner validation;
the exact triplet-projector record;
the projector validation;
the expression/status/support records;
the numerical-certification records, if present;
the C53 impact decision;
the C67 import contract;
the C66 readiness report;

the C66 implementation code and public constructors;
the C66 builder and validator;
the C66 focused tests.
```

Use actual filenames. Do not invent an absent C66 artifact and then treat its absence as a new scientific obstruction.

Read completely:

```text
docs/next_level/c67_implementation_report.md
docs/next_level/c67_missing_calculation_specification.md
docs/next_level/c67_readiness_report.json
```

when present.

Create:

```text
docs/next_level/c68_derivation_authority_manifest.json
docs/next_level/c68_input_fidelity_audit.json
```

---

# 5. Freeze the C66 source and API fingerprint

Before materializing one runtime array, freeze:

```text
the C66 completion commit;

the exact source-file hashes for:
    SU(3) generators;
    product-basis construction;
    retained-triplet basis;
    E_src;
    Gram normalization;
    U3;
    intertwiner checks;
    P3;

the exact public constructor signatures;

the exact row and column basis generators;

the exact entry-status vocabulary;

the exact expression representation and canonicalization;

the exact C53 convention hashes consumed by C66;

the exact C66 C53-impact decision.
```

Create:

```text
docs/next_level/c68_c66_source_fingerprint.json
docs/next_level/c68_c66_api_fingerprint.json
docs/next_level/c68_serializer_version_contract.json
```

C68 must fail when any frozen scientific source or serializer identity changes without a declared supersession.

---

# 6. Select the artifact schema

Freeze one deterministic schema version for the C68 package.

The schema must define:

```text
scientific object identities;

row and column basis records;

exact entry statuses;

exact-expression serialization;

exact-zero certificates;

numerical midpoint and error-bound representation;

array dtype and endianness;

relative runtime paths;

hash calculation;

aggregate package hash;

read-only loader behavior.
```

Create:

```text
docs/next_level/c68_artifact_schema_contract.json
```

The schema must not use version-unstable object `repr`, locale-dependent formatting, machine-specific paths, or archive timestamps as scientific identity.

---

# 7. Canonical row and column basis manifests

Materialize the exact ordered 24-row product-color basis and the exact ordered 3-column retained-triplet basis.

Each row record must retain:

```text
row index;

fundamental color ID;

adjoint color ID;

C53/C66 product-basis ancestry;

basis-order source;

canonical row ID.
```

Each column record must retain:

```text
column index;

retained-triplet basis ID;

canonical fundamental-basis relation;

phase/permutation adapter ancestry;

canonical column ID.
```

Compute:

```text
row_basis_sha256;

column_basis_sha256;

combined_basis_order_sha256.
```

Required checks:

```text
24 unique ordered rows;

3 unique ordered columns;

no duplicate or missing basis ID;

complete index ranges;

basis reconstruction independent of dictionary and filesystem order;

exact equality with the C66 basis records.
```

Create:

```text
docs/next_level/c68_triplet_basis_order_manifest.json
docs/next_level/c68_triplet_basis_order_validation.json
```

---

# 8. Complete exact \(U_3\) entry domain

Enumerate all:

\[
24\times3=72
\]

candidate entries.

Every entry receives exactly one terminal C66-owned status, using the actual vocabulary established by C66, such as:

```text
ZERO_BY_EXACT_GENERATOR_STRUCTURE;

ZERO_BY_EXACT_BASIS_SELECTION;

NONZERO_EXACT_RATIONAL;

NONZERO_EXACT_RADICAL;

NONZERO_EXACT_IMAGINARY_RADICAL.
```

Do not hard-code the zero or nonzero count.

For every entry retain:

```text
row ID;

column ID;

terminal status;

exact-zero reason or exact expression;

source-color-map ancestry;

Gram-normalization ancestry;

triplet-basis-adapter ancestry;

C66 constructor fingerprint.
```

Create:

```text
docs/next_level/c68_triplet_entry_domain.json
docs/next_level/c68_triplet_entry_status_validation.json
```

A positive gate requires:

```text
candidate entries = 72;

missing statuses = 0;

duplicate statuses = 0;

undecidable statuses = 0.
```

---

# 9. Canonical exact-expression and zero-certificate records

For every exact nonzero \(U_3\) entry, materialize a deterministic canonical exact-expression record.

For every exact zero, materialize a deterministic exact-zero certificate.

Acceptable expression representations include:

```text
a project-native exact AST;

a normalized rational/radical/i term list;

a locked canonical SymPy serialization;

or the exact stable representation already established by C66.
```

A raw pretty-printed string is insufficient unless its serializer and canonicalization are explicitly frozen and validated.

Every record must support:

```text
exact equality;

exact zero testing;

arbitrary-precision evaluation;

content hashing;

source ancestry.
```

Create:

```text
docs/next_level/c68_triplet_exact_expression_manifest.json
docs/next_level/c68_triplet_zero_certificate_manifest.json
docs/next_level/c68_triplet_expression_validation.json
```

---

# 10. Expression and support hashes

Compute hashes over the complete ordered 72-entry domain.

The expression hash must include:

```text
row and column IDs;

terminal status;

exact nonzero expression or exact-zero certificate;

normalization and basis-adapter identity.
```

The support hash must be threshold free.

Compute at least:

```text
expression_sha256;

status_sha256;

boolean_support_sha256;

zero_certificate_sha256;

basis_order_sha256;

aggregate_triplet_package_sha256.
```

Create:

```text
docs/next_level/c68_triplet_expression_hash_manifest.json
docs/next_level/c68_triplet_support_hash_manifest.json
docs/next_level/c68_triplet_aggregate_hash_report.json
```

No hash may depend on numerical thresholding, sparse pruning, runtime path, or temporary execution order.

---

# 11. Materialize exact companion objects

Materialize canonical exact records for the complete C66 color package required by C69:

```text
E_src:
    24 x 3;

Gram matrix:
    3 x 3;

triplet basis adapter:
    3 x 3 or the exact committed shape;

U3:
    24 x 3;

U3-dagger:
    3 x 24;

P3:
    24 x 24;

any exact product/triplet basis permutations required by the C66
import contract.
```

Each object must retain:

```text
shape;

row and column basis identities;

exact expression/status ancestry;

object hash;

relation to U3;

source fingerprint.
```

Create:

```text
docs/next_level/c68_exact_color_object_manifest.json
docs/next_level/c68_exact_color_object_validation.json
```

Do not materialize a numerically refactored substitute.

---

# 12. Numerical certification plan

Prefer reusing the already validated generic certification and deterministic-array infrastructure from C64 when it is scientifically generic and does not consume C64 TM values.

Compile and select one plan:

```text
QGCOLOR-RUNTIME-DIRECTED-INTERVAL;

QGCOLOR-RUNTIME-EXACT-RADICAL-BOUND;

QGCOLOR-RUNTIME-GENERIC-C64-CERTIFIER;

QGCOLOR-RUNTIME-CERTIFICATION-UNAVAILABLE.
```

A positive gate requires a mathematically justified enclosure for every exact nonzero.

Numerical agreement between two ordinary floating evaluations is not, by itself, a rigorous error bound.

Create:

```text
docs/next_level/c68_numerical_certification_plan.json
docs/next_level/c68_numerical_certification_decision.json
docs/next_level/c68_precision_and_rounding_contract.json
```

---

# 13. Certified numerical arrays

Export deterministic numerical arrays and absolute error bounds for:

```text
E_src;

Gram;

triplet basis adapter;

U3;

U3-dagger;

P3;

required basis permutations.
```

Use deterministic uncompressed `.npy` files or an equivalently stable repository format. Do not use timestamp-bearing archives unless their determinism is explicitly controlled.

For each array record:

```text
shape;

dtype;

endianness;

working precision;

rounding convention;

midpoint hash;

error-bound hash;

basis-order hashes;

exact-object hash.
```

Every exact zero must be stored as literal zero.

Every claimed nonzero interval must exclude zero.

Create:

```text
docs/next_level/c68_certified_color_array_contract.json
docs/next_level/c68_certified_color_array_hash_manifest.json
docs/next_level/c68_error_bound_validation.json
docs/next_level/c68_precision_stability_report.json
```

---

# 14. Certified invariant closure

Using only the materialized numerical arrays and their bounds, validate:

\[
U_3^\dagger U_3=I_3,
\]

\[
P_3=U_3U_3^\dagger,
\qquad
P_3^\dagger=P_3,
\qquad
P_3^2=P_3,
\]

\[
\operatorname{rank}P_3=3,
\qquad
\operatorname{Tr}P_3=3,
\]

and the C66 intertwiner identities for all eight generators.

Also validate:

```text
triplet preservation;

zero anti-sextet leakage;

zero 15 leakage;

read-only embed/project round trips;

precision stability.
```

The exact C66 records remain the authority; numerical residuals must lie inside propagated certification bounds.

Create:

```text
docs/next_level/c68_certified_color_invariant_report.json
```

Do not repair a residual through reorthogonalization, clipping, symmetrization, or projector refactorization.

---

# 15. Deterministic runtime root and paths

Use the deterministic runtime root:

```text
data/runtime/c68_qgcolor_runtime/
```

Materialize relative-path records for at least:

```text
row_basis.json;

column_basis.json;

entry_status.npy or equivalent;

entry_support.npy or equivalent;

exact_expressions.jsonl or equivalent;

zero_certificates.jsonl or equivalent;

E_src_real.npy;
E_src_imag.npy;
E_src_abs_error.npy;

Gram_real.npy;
Gram_imag.npy;
Gram_abs_error.npy;

triplet_adapter_real.npy;
triplet_adapter_imag.npy;
triplet_adapter_abs_error.npy;

U3_real.npy;
U3_imag.npy;
U3_abs_error.npy;

U3_dagger_real.npy;
U3_dagger_imag.npy;
U3_dagger_abs_error.npy;

P3_real.npy;
P3_imag.npy;
P3_abs_error.npy;

permutation arrays or records;

metadata.json.
```

Use actual repository conventions when superior, but every path must be committed, relative, deterministic, and hash verified.

Create:

```text
docs/next_level/c68_runtime_path_manifest.json
docs/next_level/c68_reconstruction_command_manifest.json
```

---

# 16. Complete runtime inventory

Create one inventory row per runtime artifact.

Each row must record:

```text
relative path;

schema and object type;

shape or record count;

dtype;

file size;

basis hashes;

expression/status/support hashes;

array hash;

error-bound hash;

generator command;

C66 source fingerprint.
```

The inventory must detect:

```text
missing artifacts;

duplicate artifact identities;

orphan runtime files;

unhashed files;

shape or dtype mismatches;

path mismatches.
```

Create:

```text
docs/next_level/c68_numerical_object_inventory.json
docs/next_level/c68_runtime_completeness_report.json
```

A positive gate requires all error counts to be zero.

---

# 17. Hash-verifying read-only API

Create a C68-owned import package under the repository-equivalent of:

```text
src/deuteron_wigner/bridge/qgcolor_runtime/
```

Provide APIs equivalent to:

```python
load_triplet_runtime_metadata()

load_triplet_row_basis()

load_triplet_column_basis()

load_triplet_entry_statuses()

load_exact_triplet_expressions()

load_certified_source_emission() -> CertifiedMatrix

load_certified_triplet_isometry() -> CertifiedMatrix

load_certified_triplet_adjoint() -> CertifiedMatrix

load_certified_triplet_projector() -> CertifiedMatrix

embed_triplet_color_to_product(
    triplet_vector,
    precision=None,
) -> CertifiedVectorResult

project_product_color_to_triplet(
    product_vector,
    precision=None,
) -> CertifiedVectorResult

apply_triplet_projector(
    product_vector,
    precision=None,
) -> CertifiedVectorResult
```

The loader must:

```text
verify every required hash before returning data;

return immutable/read-only arrays;

expose exact statuses independently from numerical values;

expose basis orders and error bounds;

call no C66 build() or scientific constructor;

call no C53 physical vertex generator;

regenerate no missing artifact;

fail closed on an absent, changed, writable, or untracked required
runtime object.
```

Create:

```text
docs/next_level/c68_api_contract.json
docs/next_level/c68_api_validation.json
```

---

# 18. C66-to-C68 complete equivalence

Compare the complete C68 artifact domain against the immutable C66 constructors.

For every one of the 72 \(U_3\) entries compare:

```text
row and column IDs;

terminal exact status;

exact expression or zero certificate;

support decision;

arbitrary-precision value;

certified interval.
```

Also compare complete exact and numerical forms of:

```text
E_src;

Gram;

triplet basis adapter;

U3-dagger;

P3;

basis permutations.
```

Require exact identity for symbolic/status records.

Require every C66 high-precision value to lie inside the C68 certified interval.

Create:

```text
docs/next_level/c68_c66_entry_equivalence_report.json
docs/next_level/c68_c66_object_equivalence_report.json
```

A sampled comparison is insufficient.

---

# 19. Independent runtime-action equivalence

Implement two disjoint routes.

## Route A: direct C66 action

Construct or apply the exact C66 scientific object without loading C68 runtime arrays.

## Route B: read-only C68 action

Load and apply only the immutable C68 runtime package.

Compare on:

```text
all three triplet basis vectors;

all twenty-four product-color basis vectors;

deterministic complex superpositions;

random normalized complex vectors;

triplet and complement holdouts.
```

Require agreement within certified propagated bounds.

The C68 route must not call C66.

Create:

```text
docs/next_level/c68_runtime_action_equivalence_report.json
```

---

# 20. Preserve the C66 C53-impact decision

Import the C66 C53-impact result read-only.

Verify that runtime materialization does not change:

```text
the C53 full-product route;

the C53 reduced-triplet route;

the physical canonical vertex values;

the generated adjoint;

the support ancestry;

the basis covariance decision.
```

C68 may strengthen artifact provenance and downstream importability. It may not reopen or silently promote the C53 physics result.

Create:

```text
docs/next_level/c68_c53_impact_preservation_report.json
```

If the C66 impact status is incomplete or internally inconsistent, record the exact blocker rather than assuming the favorable branch.

---

# 21. C69/QGEMBED5 import contract

Define the immutable contract by which C69 consumes:

```text
the C68 aggregate package hash;

the exact row and column basis manifests;

the complete 72-entry status/support domain;

the exact-expression and zero-certificate hashes;

the certified E_src, Gram, adapter, U3, U3-dagger, and P3 arrays;

all numerical error bounds;

all runtime relative paths;

the complete inventory;

the C53-impact preservation status;

the read-only embed/project/projector API.
```

C69 must verify every hash before combining the C68 color map with the C64 CM-ground kinematic embedding.

C69 may not:

```text
call C66 build();

renormalize raw_emission_E;

factor P3;

choose new column phases;

change a basis order;

regenerate a missing C68 file;

or bypass the read-only API.
```

Create:

```text
docs/next_level/c68_c69_qgembed5_import_contract.json
```

---

# 22. Resolve the C67 import blocker by dry preflight

Perform a C69-style read-only import preflight that:

```text
loads C64 through its existing immutable API;

loads C68 through the new immutable API;

verifies both package aggregate hashes;

verifies all required runtime paths;

verifies immutable array flags;

verifies the C64 and C68 basis metadata needed for later
kinematic/color composition;

does not construct a CM-ground or full physical qg embedding.
```

The preflight must prove that the exact C67 blocker:

```text
C67_QGEMBED_C66_IMPORT_INCOMPLETE
```

is superseded by the C68 runtime package.

Create:

```text
docs/next_level/c68_c67_blocker_supersession_report.json
docs/next_level/c68_c69_import_preflight.json
```

Do not promote the physical embedding itself.

---

# 23. Deterministic reconstruction

Run at least:

```text
two consecutive complete C68 builds;

one clean temporary-runtime build;

one serial build;

one supported parallel/sharded build, when the builder supports it;

one restart/resume build from a partially complete valid runtime
tree.
```

Require byte-identical final artifacts and manifests.

A restart may reuse an artifact only when all source, basis, expression, support, numerical, and bound hashes pass.

Create:

```text
docs/next_level/c68_deterministic_reconstruction_report.json
docs/next_level/c68_restart_parallel_report.json
docs/next_level/c68_environment_manifest.json
```

---

# 24. Count-once and provenance

Report:

```text
candidate U3 entries = 72;

materialized statuses;

exact-zero count by class;

exact-nonzero count by class;

exact-expression count;

zero-certificate count;

certified numerical U3 entry count;

companion exact-object count;

runtime-artifact count;

basis-record count;

missing count;

duplicate count;

orphan count;

unhashed count;

hash-mismatch count;

unbounded numerical-entry count;

unresolved-impact count.
```

Every \(U_3\) entry must have exactly one ancestry path:

```text
C53 convention
    ->
C66 E_src/Gram/normalization/basis adapter
    ->
C66 exact U3 entry
    ->
C68 status/expression certificate
    ->
C68 certified numerical entry
    ->
runtime path and hashes
    ->
read-only loader.
```

Create:

```text
docs/next_level/c68_artifact_ancestry_ledger.json
docs/next_level/c68_count_once_report.json
```

A positive gate requires every error and unresolved count to be zero.

---

# 25. Isolation and poisoning controls

Prove C68 construction is unchanged when:

```text
C53 physical vertex numerical matrices are poisoned;

raw_emission_E numerical values are poisoned after the exact C66
source relation is frozen;

stored C53 24 x 24 projector values are poisoned after their
holdout identities are frozen;

all C47 canonical tuple values are poisoned;

all C50/C52 physical values are poisoned;

all C57/C58 numerical objects are poisoned;

all C64 TM runtime arrays are inaccessible except for the final
C69 import preflight;

ART25 files are inaccessible.
```

The build must fail when:

```text
a C66 source or API fingerprint changes;

a row or column basis record changes;

an exact U3 entry changes;

an entry status or zero certificate changes;

a column phase or normalization changes;

an expression or support hash changes;

an error bound is removed;

a runtime path is absent;

an array hash changes;

the loader calls C66 build();

the loader regenerates a missing artifact;

an imported array is writable;

the package aggregate hash changes.
```

Create:

```text
docs/next_level/c68_isolation_report.json
```

---

# 26. End-to-end C66-source-to-C68-runtime test

Implement an end-to-end test that begins from the immutable C66 source and exact contracts, not from prebuilt C68 files.

It must:

```text
verify C66 fingerprints;

construct the exact row and column basis manifests;

enumerate all 72 entries;

materialize statuses, expressions, and zero certificates;

materialize E_src, Gram, adapter, U3, U3-dagger, and P3 records;

compute every hash;

select and execute the numerical-certification plan;

write all deterministic runtime arrays and bounds;

write the complete inventory;

load all objects through the read-only C68 API;

compare every entry and companion object with C66;

compare direct and runtime actions;

validate all invariants within certified bounds;

preserve the C66 C53-impact result;

run the C69 import preflight;

rebuild every artifact byte-for-byte.
```

It must fail when:

```text
one of the 72 entries is omitted;

an exact zero is absent from the status/hash domain;

an exact nonzero expression is missing;

a numerical threshold defines support;

a basis order is inferred by the consumer;

a numerical entry lacks a bound;

a runtime path is unrecorded;

the read-only loader regenerates data;

the C69 preflight would need to call C66;

an artifact or hash changes.
```

---

# 27. Focused mutation tests

Create at least **256 focused live mutations** of actual source fingerprints, basis records, exact entries, statuses, arrays, bounds, paths, or loader behavior.

Include mutations of:

```text
C66 source hash;

C66 API signature;

row basis ID;

column basis ID;

basis order;

U3 exact entry;

entry status;

zero certificate;

normalization ancestry;

column phase;

expression hash;

support hash;

E_src entry;

Gram entry;

adapter entry;

U3-dagger entry;

P3 entry;

numerical midpoint;

error bound;

dtype;

endianness;

runtime path;

array hash;

aggregate hash;

read-only flag;

loader regeneration guard;

C53-impact status;

C69 import-contract field;

restart reuse decision.
```

Every mutation must fail a concrete source, basis, exact-status, expression, normalization, certification, path, import, impact, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 28. Readiness gate

Issue:

```text
C68_SOURCE_DERIVED_TRIPLET_RUNTIME_ARTIFACTS_READY
```

only when:

```text
the full C67 baseline reproduces;

the C67 import no-go remains explicit and is superseded only by the
new C68 package;

the C66 positive scientific status remains unchanged;

all C66 source/API fingerprints are frozen;

the exact 24-row and 3-column basis manifests exist and match C66;

all 72 candidate entries have exact terminal statuses;

every exact nonzero has a canonical expression;

every exact zero has a canonical certificate;

expression, status, support, basis, and aggregate hashes exist;

E_src, Gram, adapter, U3, U3-dagger, and P3 exact records exist;

one rigorous numerical-certification plan is selected;

every exact nonzero has a certified numerical enclosure;

all required numerical arrays and bounds are materialized;

all runtime paths and hashes are committed;

the runtime inventory has no missing, duplicate, orphan, unhashed,
or unbounded artifact;

the read-only API verifies all hashes;

returned arrays are immutable;

the loader calls no C66 or C53 scientific builder;

the loader regenerates nothing;

complete entry and object equivalence with C66 passes;

independent runtime actions agree within bounds;

all exact and certified invariants close;

the C66 C53-impact status is preserved;

the C69 import contract is complete;

the C69 read-only import preflight passes;

the C67 blocker supersession is explicit;

serial, clean, repeated, restart, and supported parallel
reconstruction pass;

count-once and provenance close;

poisoning controls pass;

the end-to-end test passes.
```

Do not issue:

```text
C68_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY;

C68_IFERM_CONTACT_SUPPORT_READY;

C68_DIRECT_IFERM_CONTACT_READY;

C68_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C68_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY.
```

---

# 29. Exact no-go branches

## A. C66 source or API fingerprint is incomplete

```text
C68_QGCOLOR_RUNTIME_SOURCE_FINGERPRINT_INCOMPLETE
```

Next:

> **C69/QGCOLOR-SRC2 — exact C66 source, API, serializer, and dependency fingerprint closure**

## B. Basis, expression, or support materialization is incomplete

```text
C68_QGCOLOR_RUNTIME_EXACT_ARTIFACT_INCOMPLETE
```

Next:

> **C69/QGCOLOR-EXPR2 — complete basis manifests, 72-entry status domain, exact expressions, zero certificates, and hashes**

## C. Numerical certification is incomplete

```text
C68_QGCOLOR_RUNTIME_NUMERICAL_CERTIFICATION_INCOMPLETE
```

Next:

> **C69/QGCOLOR-CERT2 — directed bounds, certified arrays, and invariant-error propagation closure**

## D. Runtime inventory or loader is incomplete

```text
C68_QGCOLOR_RUNTIME_IMPORT_INCOMPLETE
```

Next:

> **C69/QGCOLOR-RUNTIME2 — deterministic paths, complete inventory, immutable loader, and reconstruction closure**

## E. C66/runtime equivalence fails

```text
C68_QGCOLOR_RUNTIME_EQUIVALENCE_FAILED
```

Next:

> **C69/QGCOLOR-XCHECK2 — exact-entry, companion-object, action, and invariant reconciliation**

## F. Runtime closure succeeds

```text
C68_SOURCE_DERIVED_TRIPLET_RUNTIME_ARTIFACTS_READY
```

Next:

> **C69/QGEMBED5 — exact physical \(qg\) embedding and descendant-impact closure**

---

# 30. Required deliverables

Create at least:

```text
docs/next_level/c68_implementation_report.md
docs/next_level/c68_api.md
docs/next_level/c68_derivation_authority_manifest.json
docs/next_level/c68_input_fidelity_audit.json

docs/next_level/c68_c66_source_fingerprint.json
docs/next_level/c68_c66_api_fingerprint.json
docs/next_level/c68_serializer_version_contract.json
docs/next_level/c68_artifact_schema_contract.json

docs/next_level/c68_triplet_basis_order_manifest.json
docs/next_level/c68_triplet_basis_order_validation.json
docs/next_level/c68_triplet_entry_domain.json
docs/next_level/c68_triplet_entry_status_validation.json

docs/next_level/c68_triplet_exact_expression_manifest.json
docs/next_level/c68_triplet_zero_certificate_manifest.json
docs/next_level/c68_triplet_expression_validation.json
docs/next_level/c68_triplet_expression_hash_manifest.json
docs/next_level/c68_triplet_support_hash_manifest.json
docs/next_level/c68_triplet_aggregate_hash_report.json

docs/next_level/c68_exact_color_object_manifest.json
docs/next_level/c68_exact_color_object_validation.json

docs/next_level/c68_numerical_certification_plan.json
docs/next_level/c68_numerical_certification_decision.json
docs/next_level/c68_precision_and_rounding_contract.json
docs/next_level/c68_certified_color_array_contract.json
docs/next_level/c68_certified_color_array_hash_manifest.json
docs/next_level/c68_error_bound_validation.json
docs/next_level/c68_precision_stability_report.json
docs/next_level/c68_certified_color_invariant_report.json

docs/next_level/c68_runtime_path_manifest.json
docs/next_level/c68_reconstruction_command_manifest.json
docs/next_level/c68_numerical_object_inventory.json
docs/next_level/c68_runtime_completeness_report.json

docs/next_level/c68_api_contract.json
docs/next_level/c68_api_validation.json
docs/next_level/c68_c66_entry_equivalence_report.json
docs/next_level/c68_c66_object_equivalence_report.json
docs/next_level/c68_runtime_action_equivalence_report.json
docs/next_level/c68_c53_impact_preservation_report.json

docs/next_level/c68_c69_qgembed5_import_contract.json
docs/next_level/c68_c67_blocker_supersession_report.json
docs/next_level/c68_c69_import_preflight.json

docs/next_level/c68_deterministic_reconstruction_report.json
docs/next_level/c68_restart_parallel_report.json
docs/next_level/c68_environment_manifest.json
docs/next_level/c68_artifact_ancestry_ledger.json
docs/next_level/c68_count_once_report.json
docs/next_level/c68_isolation_report.json

docs/next_level/c68_readiness_report.json
docs/next_level/c68_source_sufficiency_decision.json
docs/next_level/c68_no_go_decision_tree.json
docs/next_level/c68_missing_calculation_specification.md
docs/next_level/c68_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/qgcolor_runtime/
```

or the repository-equivalent package.

Add focused tests for:

```text
C66 source/API fingerprints;
basis manifests;
72-entry status domain;
exact expressions and zero certificates;
expression/support hashes;
companion exact objects;
numerical certification;
certified invariants;
runtime paths and inventory;
immutable read-only API;
complete C66 equivalence;
independent runtime actions;
C53-impact preservation;
C69 import preflight;
restart and deterministic reconstruction;
end-to-end source-to-runtime closure.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All committed JSON and every runtime artifact must reconstruct byte-for-byte.

---

# 31. Acceptance criteria

C68 is complete only when:

1. The full C67 baseline reproduces.
2. The C67 fail-closed status remains explicit.
3. The C66 positive scientific status remains unchanged.
4. C53, C64, C66, and C67 historical artifacts remain byte-identical.
5. C40 remains method-oracle only.
6. C68 does not redefine \(U_3\).
7. `raw_emission_E` is not relabeled \(U_3\).
8. \(P_3\) is not factored numerically to choose columns.
9. No numerical QR/SVD/eigensolver defines phases.
10. Every C66 scientific source file has a frozen hash.
11. Every required C66 API has a frozen signature.
12. The serializer and artifact schema are explicit.
13. The exact 24-row basis manifest exists.
14. The exact 3-column basis manifest exists.
15. Row, column, and combined basis hashes exist.
16. All 72 candidate entries are materialized.
17. Every entry has one exact terminal status.
18. Every exact nonzero has one canonical expression.
19. Every exact zero has one canonical certificate.
20. Exact zeros remain in the expression/status hash domain.
21. Expression, status, support, zero-certificate, and aggregate hashes exist.
22. Exact E_src, Gram, adapter, U3, U3-dagger, and P3 records exist.
23. One rigorous numerical-certification plan is selected.
24. Numerical agreement alone is not mislabeled a rigorous bound.
25. Every exact nonzero has a certified enclosure.
26. Every claimed nonzero enclosure excludes zero.
27. Exact zeros are stored as literal zeros.
28. Every numerical and error array has a committed hash.
29. Every required runtime artifact has a deterministic relative path.
30. Every runtime artifact has a generator command.
31. The runtime inventory has no missing, duplicate, orphan, unhashed, or unbounded object.
32. Every C68 exact entry agrees with C66.
33. Every C66 high-precision value lies in the C68 certified interval.
34. Every companion object agrees with C66.
35. The C68 runtime actions call no C66 builder.
36. Direct C66 and read-only C68 actions agree within bounds.
37. \(U_3^\dagger U_3=I_3\) closes exactly and numerically within bounds.
38. \(P_3=U_3U_3^\dagger\) closes.
39. Projector and intertwiner invariants close.
40. Anti-sextet and 15 leakage remain zero.
41. The C66 C53-impact result is preserved.
42. The read-only API verifies every hash.
43. Imported arrays are immutable.
44. The loader regenerates nothing.
45. The loader fails on a missing or changed runtime artifact.
46. The C69 import contract is complete.
47. The C69 import preflight passes without physical embedding construction.
48. The C67 import blocker has an explicit descendant supersession record.
49. Two consecutive builds are byte-identical.
50. A clean-runtime build is byte-identical.
51. Serial and supported parallel builds agree.
52. Restart accepts only fully verified artifacts.
53. Every entry and artifact has complete ancestry.
54. Duplicate, missing, orphan, hash-mismatch, undecidable, unbounded, and unresolved-impact counts are zero.
55. Static and runtime poisoning controls pass.
56. At least 256 focused live mutations are detected.
57. No CM-ground/full physical \(qg\) embedding is created.
58. No descendant support or operator status is promoted beyond resolving the import blocker.
59. No endpoint relation, witness relation, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
60. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
61. `MSHT20_REP/` remains untouched and outside Git.
62. The working tree is clean except for the pre-existing untracked directory.
63. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken exact basis identity, entry completeness, expression canonicalization, numerical certification, runtime-path integrity, immutable loader semantics, or C66 equivalence to open the gate.

---

# 32. Final Codex response

Report:

- full starting and final commits;
- exact C66 source/API fingerprints;
- serializer, schema, and certification backend versions;
- product-row and triplet-column basis hashes;
- 72-entry status counts by exact class;
- exact-nonzero expression and exact-zero certificate counts;
- expression, status, support, zero-certificate, basis, and aggregate hashes;
- exact companion-object shapes and hashes;
- selected numerical-certification plan;
- working precision, output dtypes, rounding policy, and error-bound convention;
- certified array shapes, nnz values, hashes, and maximum error bounds;
- runtime paths and generator commands;
- missing, duplicate, orphan, unhashed, unbounded, and hash-mismatch counts;
- complete C66 entry and object-equivalence results;
- direct-versus-runtime action residuals and propagated bounds;
- exact and certified normalization, projector, intertwiner, and leakage results;
- C53-impact preservation result;
- read-only API validation;
- C67 blocker-supersession and C69 import-preflight results;
- serial, clean, repeated, parallel, and restart deterministic results;
- ancestry and count-once results;
- isolation and poisoning results;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no physical \(qg\) embedding, descendant support promotion, endpoint/witness relation, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an in-memory C66 reconstruction, an unhashed \(U_3\), a writable imported array, an array without certified bounds, a loader that calls `build()`, a numerically refactored projector, or a consumer-inferred basis order as a complete immutable C66 runtime package.
