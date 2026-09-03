# C70/QGCOLOR4 Codex Work Package

## Title

**Complete immutable package contract for the C68 triplet runtime: source/API fingerprints, authenticated `index.json`, read-only exact-record loaders, aggregate inventory verification, and C71 physical-embedding handoff**

## Authoritative baseline

Start from the clean baseline recorded by the C69 import preflight:

```text
031ac09fe3aeac19f281255ae2a0f014092485e8
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
test "$(git rev-parse HEAD)" = "031ac09fe3aeac19f281255ae2a0f014092485e8"
```

Proceed only when this baseline contains and reproduces:

```text
C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY

C66_SOURCE_DERIVED_TRIPLET_ISOMETRY_ARTIFACT_READY

C67_QGEMBED_C66_IMPORT_INCOMPLETE

C68_SOURCE_DERIVED_TRIPLET_ISOMETRY_RUNTIME_READY
```

and the exact C69 preflight finding:

```text
individual C68 numerical arrays:
    present and individually hash checked;

C68 package-level import contract:
    incomplete;

missing package-level requirements:
    no complete source fingerprint;
    no complete public-API fingerprint;
    no authenticated index.json;
    no read-only status loader;
    no read-only exact-expression loader;
    no read-only exact-zero-certificate loader;
    no aggregate package-root verification;
    no complete runtime-inventory verification;

consequence:
    C69 cannot consume C68 as one complete immutable package without
    bypassing its public API or regenerating scientific objects;

not performed:
    no CM-ground kinematic embedding;
    no full color-triplet qg embedding;
    no descendant-impact audit;
    no contact support or contact matrix.
```

Verify the actual repository state and every C68 artifact rather than treating this prompt as numerical authority.

The exact scientific color object remains immutable:

\[
U_3=\frac{E_{\rm src}}{\sqrt{C_F}},
\qquad
C_F=\frac43,
\qquad
U_3^\dagger U_3=I_3,
\qquad
P_3=U_3U_3^\dagger .
\]

The following C66/C68 identities must not change:

```text
the 24 ordered product-color rows;

the 3 ordered retained-triplet columns;

all 72 U3 terminal statuses;

every exact U3 expression and exact-zero certificate;

the source-emission map E_src;

the exact Gram matrix;

the triplet basis adapter;

U3, U3-dagger, and P3;

all-eight-generator intertwining;

rank-three projector closure;

zero anti-sextet and 15 leakage;

the preserved C53-impact decision.
```

The C64 exact-TM package remains read-only and unchanged.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Scientific correction and descendant ownership

C68 successfully materialized the correct scientific payload, but its status overstated downstream package import readiness.

The distinction is:

```text
C66:
    owns the exact source-derived triplet-isometry science;

C68:
    owns the first materialized numerical and exact-record payload;

C70:
    owns the complete authenticated package contract that makes the
    unchanged payload consumable through one immutable public API.
```

C70 must create a descendant package. It must not silently rewrite history or claim that the missing package-level contract was already present in C68.

C70 may copy the C68 payload byte-for-byte into a C70-owned runtime root when needed to form one self-contained package. It may instead reference verified C68 payload paths only if the result is genuinely self-contained under a single authenticated index and the C71 loader never needs to call a C68 builder or infer an external path.

The preferred design is a small C70-owned self-contained runtime package because the color payload is finite and small.

C70 must not:

```text
rederive U3;

renormalize U3;

change a row or column basis order;

choose a new column phase;

factor P3 to regenerate U3;

relabel raw_emission_E as U3;

change any exact status, expression, or zero certificate;

change any certified midpoint or bound except for a byte-identical
copy into the descendant package;

or construct the physical qg embedding.
```

---

# 2. Execution mandate

The C69 blocker is concrete and finite. C70 must close it in this package.

Required closure:

```text
source fingerprints;

API fingerprints;

an authenticated package index;

a package aggregate/root hash;

read-only loaders for all exact records;

complete inventory verification;

immutable returned objects;

a no-regeneration guard;

complete C68-to-C70 equivalence;

and a passing C71-style import preflight.
```

Do not split this into another metadata-only preparatory package unless an actual mismatch in the C66/C68 scientific payload is discovered.

A desire for another summary file, preferred naming, alternate directory layout, or additional prose is not a valid no-go.

---

# 3. Exact purpose

C70 must produce:

```text
a frozen fingerprint of every C66/C68 scientific and runtime source
required to define the package;

a frozen fingerprint of every public C70 import API and return
schema;

one deterministic package schema;

one complete self-contained runtime root;

an authenticated canonical index.json;

a sidecar hash or equivalent noncircular authentication of
index.json;

one package aggregate/root identity;

complete row and column basis manifests;

the full 72-entry exact status domain;

complete exact-expression and exact-zero-certificate records;

all certified numerical arrays and error bounds;

one complete runtime inventory;

hash-verifying read-only loaders for every exact and numerical
object;

one frozen package object that exposes the complete payload without
regeneration or API bypass;

complete entry/object/action equivalence with C66/C68;

deterministic reconstruction;

a C71/QGEMBED6 import contract;

and a dry C71 preflight with the immutable C64 and C70 packages.
```

C70 must not construct:

```text
the C64 CM-ground kinematic embedding;

the complete physical qg embedding;

C47/C52/C53/C57/C58 descendant-impact decisions beyond preserving
the inherited C68/C66 C53-impact record;

C60 endpoint or witness relations;

a contact value or matrix;

a complete instantaneous-fermion operator;

a Wilson/TMD or matching object.
```

The strongest positive status is:

```text
C70_SOURCE_DERIVED_TRIPLET_PACKAGE_IMPORT_READY
```

The exact positive continuation is:

> **C71/QGEMBED6 — construct the exact CM-ground and color-triplet physical \(qg\) embedding and close descendant impact using immutable C64 and C70 packages**

---

# 4. Mandatory inputs and repository inventory

Inventory the actual C66, C68, and C69-preflight state:

```bash
git ls-files 'docs/next_level/c66*'
git ls-files 'docs/next_level/c68*'
git ls-files 'src/deuteron_wigner/**/qgcolor2*'
git ls-files 'src/deuteron_wigner/**/qgcolor_runtime*'
git ls-files 'scripts/*c66*'
git ls-files 'scripts/*c68*'
git ls-files 'tests/*c66*'
git ls-files 'tests/*c68*'
find data/runtime -maxdepth 3 -type f | sort
```

Read completely the actual repository equivalents of:

```text
C66 implementation, source authority, SU(3), basis, source-emission,
Gram, normalization, exact-isometry, intertwiner, projector,
support/expression, certification, C53-impact, readiness, and
determinism records;

C68 implementation, source/API or partial fingerprint records,
artifact schema, basis manifests, 72-entry status domain,
expression and zero-certificate records, array and bound records,
runtime paths, inventory, loaders, equivalence checks, C53-impact
preservation, C69 import contract, readiness, and determinism
records;

the C66 and C68 implementation modules, builders, validators, and
tests;

the C69 preflight output or handoff record that identified the
package-level omissions.
```

Use actual filenames. Do not invent a missing preferred filename and then treat the naming difference as a scientific obstruction.

Create:

```text
docs/next_level/c70_derivation_authority_manifest.json
docs/next_level/c70_input_fidelity_audit.json
```

---

# 5. Freeze the scientific-source fingerprint

Create one complete fingerprint over every source that can change the scientific payload.

At minimum include the exact hashes and roles of code that defines:

```text
the C53/C66 SU(3) generators;

the product-color basis;

the retained-triplet basis and adapter;

E_src;

the exact Gram normalization;

U3;

U3-dagger;

P3;

entry statuses;

exact expressions;

zero certificates;

numerical certification;

the C68 payload builder.
```

Every source record must include:

```text
repository-relative path;

SHA-256;

scientific role;

public symbols used;

schema/version identity;

whether it is construction authority or validation only.
```

Compute one canonical aggregate source fingerprint.

Create:

```text
docs/next_level/c70_source_fingerprint_manifest.json
docs/next_level/c70_source_fingerprint_validation.json
```

The package must fail when one construction-authority source hash changes.

---

# 6. Freeze the public-API fingerprint

Fingerprint the complete public import surface.

Include at minimum:

```text
public module path;

exported symbol name;

fully qualified function or class name;

call signature;

return type/schema;

immutability contract;

hash-verification behavior;

failure behavior;

no-regeneration guarantee.
```

The public C70 API must not rely on undocumented access to module globals or private builder functions.

Compute one canonical API fingerprint over the ordered public surface.

Create:

```text
docs/next_level/c70_api_fingerprint_manifest.json
docs/next_level/c70_api_fingerprint_validation.json
```

A signature or return-schema change requires descendant supersession.

---

# 7. Deterministic package schema

Freeze one package schema version.

Use a deterministic runtime root such as:

```text
data/runtime/c70_qgcolor4/
```

The package schema must define:

```text
control files;

payload files;

canonical relative paths;

basis record schemas;

entry-status schema;

exact-expression schema;

zero-certificate schema;

numerical midpoint and bound schema;

array dtype and endianness;

inventory schema;

index schema;

hash algorithm and canonical serialization;

loader behavior;

allowed and forbidden files.
```

Create:

```text
docs/next_level/c70_package_schema_contract.json
docs/next_level/c70_serializer_version_contract.json
```

Do not use:

```text
machine-specific absolute paths;

locale-dependent formatting;

Python object repr as identity;

filesystem traversal order;

archive timestamps;

or mutable dictionary order.
```

---

# 8. Self-contained payload

Materialize or copy byte-for-byte into the C70 package every object required by C71:

```text
24-row basis manifest;

3-column basis manifest;

72-entry terminal-status table;

derived Boolean support;

exact nonzero expressions;

exact-zero certificates;

E_src midpoint and bounds;

Gram midpoint and bounds;

triplet adapter midpoint and bounds;

U3 midpoint and bounds;

U3-dagger midpoint and bounds;

P3 midpoint and bounds;

required basis permutations;

object metadata;

C53-impact preservation record.
```

When copying a C68 payload, require:

```text
source C68 path;

source C68 SHA-256;

C70 destination path;

destination SHA-256;

byte-identical result.
```

Do not recompute a payload value merely because copying it is inconvenient.

Create:

```text
docs/next_level/c70_payload_copy_equivalence_report.json
docs/next_level/c70_payload_completeness_report.json
```

---

# 9. Canonical `index.json`

Create one canonical:

```text
data/runtime/c70_qgcolor4/index.json
```

The index must include:

```text
package schema version;

scientific status;

scientific-source fingerprint;

public-API fingerprint;

serializer identity;

certification identity;

ordered basis hashes;

ordered payload entries;

for every payload entry:
    relative path;
    scientific object ID;
    role;
    schema;
    file size;
    SHA-256;
    shape or record count;
    dtype/endianness where relevant;
    exact-object hash;
    status/support/expression/bound identities where relevant;

expected payload-file count;

allowed control-file list;

C66 and C68 ancestry identities;

C53-impact preservation status.
```

The index must not contain its own hash.

Serialize canonically and deterministically.

Create:

```text
docs/next_level/c70_index_schema_contract.json
docs/next_level/c70_index_content_manifest.json
```

---

# 10. Authenticate `index.json`

Use a noncircular authentication design.

Required minimum:

```text
data/runtime/c70_qgcolor4/index.sha256
```

containing the exact SHA-256 of the canonical bytes of `index.json`.

Also commit a tracked package-root manifest containing:

```text
expected index SHA-256;

expected scientific-source fingerprint;

expected API fingerprint;

expected schema version;

expected payload count;

expected package status.
```

The package aggregate/root identity is the authenticated `index.json` hash because the index contains every payload hash and every package fingerprint.

Create:

```text
docs/next_level/c70_package_root_manifest.json
docs/next_level/c70_index_authentication_report.json
```

The loader must verify the root manifest, `index.sha256`, and the actual `index.json` bytes before trusting any payload path or hash.

---

# 11. Complete runtime inventory verification

The authenticated index is the authoritative inventory.

Verify:

```text
every indexed payload exists;

every indexed payload hash matches;

every indexed file size matches;

every declared shape, dtype, and record count matches;

every required scientific object has exactly one payload;

every file under the package root is either:
    index.json;
    index.sha256;
    or an indexed payload;

no extra or orphan file exists;

no duplicate path exists;

no duplicate scientific object ID exists;

no unbounded numerical value exists;

no status, expression, or zero-certificate record is missing.
```

Create:

```text
docs/next_level/c70_runtime_inventory_report.json
docs/next_level/c70_runtime_inventory_validation.json
```

A positive gate requires:

```text
missing = 0;

extra = 0;

orphan = 0;

duplicate_path = 0;

duplicate_object = 0;

hash_mismatch = 0;

schema_mismatch = 0;

unbounded_numerical_entry = 0.
```

---

# 12. Read-only basis loaders

Create public hash-verifying loaders for:

```text
the complete package metadata;

the ordered 24-row product-color basis;

the ordered 3-column retained-triplet basis;

the required basis permutations.
```

Return:

```text
frozen dataclasses;

tuples;

mapping proxies;

or equivalent immutable structures.
```

Do not return mutable lists or dictionaries as the authoritative object.

Create validation for:

```text
basis count;

basis order;

basis IDs;

basis hashes;

immutability;

round-trip serialization.
```

---

# 13. Read-only status loader

Create a public loader for the full 72-entry terminal-status domain.

It must:

```text
verify the package root first;

verify the status payload hash;

return all 72 entries;

retain row and column IDs;

retain exact terminal status;

retain support ancestry;

retain source-expression or zero-certificate identity;

return an immutable object.
```

The status loader must expose exact support independently of numerical arrays.

It must not calculate status from:

```text
abs(U3) > tolerance;

sparse storage;

a reconstructed generator;

or an expression evaluator.
```

Create:

```text
docs/next_level/c70_status_loader_contract.json
docs/next_level/c70_status_loader_validation.json
```

---

# 14. Read-only exact-expression loader

Create a public loader for every exact nonzero expression.

It must:

```text
verify package root and payload hash;

return canonical exact records;

retain row/column IDs;

retain expression hash;

retain normalization and basis-adapter ancestry;

support exact equality and arbitrary-precision evaluation;

return immutable objects.
```

The loader may parse a canonical AST or locked exact serialization, but it must not call a C66 constructor to regenerate expressions.

Create:

```text
docs/next_level/c70_expression_loader_contract.json
docs/next_level/c70_expression_loader_validation.json
```

---

# 15. Read-only zero-certificate loader

Create a public loader for every exact-zero certificate.

It must:

```text
verify package root and payload hash;

return the complete zero-entry domain;

retain row/column IDs;

retain exact zero class and proof ancestry;

retain certificate hash;

return immutable objects.
```

No zero certificate may be inferred from numerical magnitude.

Create:

```text
docs/next_level/c70_zero_certificate_loader_contract.json
docs/next_level/c70_zero_certificate_loader_validation.json
```

---

# 16. Read-only numerical-object loaders

Create public loaders for:

```text
E_src;

Gram;

triplet adapter;

U3;

U3-dagger;

P3;

required permutation arrays;

all associated absolute-error arrays.
```

Every numerical loader must:

```text
verify the package root;

verify object and bound hashes;

verify shape, dtype, and basis order;

set NumPy arrays non-writeable;

expose midpoint and bound together;

expose exact-object identity;

regenerate nothing.
```

A user must not be able to obtain an authoritative midpoint without its bound through the package API.

Create:

```text
docs/next_level/c70_numerical_loader_contract.json
docs/next_level/c70_numerical_loader_validation.json
```

---

# 17. Frozen package object

Create one public top-level operation equivalent to:

```python
load_triplet_runtime_package() -> TripletRuntimePackage
```

The returned package must be a frozen object exposing:

```text
package metadata;

package root hash;

source fingerprint;

API fingerprint;

basis manifests;

entry statuses;

exact expressions;

zero certificates;

certified numerical objects;

inventory;

C53-impact status.
```

Loading this object must verify the complete package.

No consumer should need to:

```text
open index.json manually;

access a private path;

call a builder;

call C66;

call C68 build();

or infer which files belong to the package.
```

Create:

```text
docs/next_level/c70_package_object_contract.json
docs/next_level/c70_package_object_validation.json
```

---

# 18. Strict no-regeneration guard

Instrument and test the public import package so that it cannot call:

```text
C66 build();

C68 build();

the C66 exact U3 constructor;

the C53 physical vertex builder;

raw_emission_E normalization;

P3 factorization;

a fallback artifact writer.
```

The loader must fail closed when a required file is missing or altered.

There must be no:

```text
build-if-missing;

repair-if-missing;

download-if-missing;

recompute-if-hash-fails;

or permissive warning mode.
```

Create:

```text
docs/next_level/c70_no_regeneration_report.json
```

---

# 19. Complete C68-to-C70 equivalence

Compare all C70 payloads with the C68/C66 authority.

For every one of the 72 entries compare:

```text
row ID;

column ID;

terminal status;

support;

exact expression or zero certificate;

numerical midpoint;

numerical bound.
```

Also compare:

```text
basis manifests;

E_src;

Gram;

triplet adapter;

U3;

U3-dagger;

P3;

permutations;

C53-impact record.
```

Require exact identity for exact records and byte identity for copied payloads.

Require the inherited exact value to remain inside each certified interval.

Create:

```text
docs/next_level/c70_c68_entry_equivalence_report.json
docs/next_level/c70_c68_object_equivalence_report.json
```

A sampled comparison is insufficient.

---

# 20. Package-level invariant validation

Using only the C70 public package object and read-only loaders, verify:

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

and the inherited representation properties:

```text
rank(P3) = 3;

trace(P3) = 3;

all-eight-generator intertwining;

triplet preservation;

zero anti-sextet leakage;

zero 15 leakage;

embed/project round trips.
```

The validation route must not call C66 or a C68 builder.

Create:

```text
docs/next_level/c70_package_invariant_report.json
```

---

# 21. Package API

Provide public operations equivalent to:

```python
load_triplet_runtime_package()

load_package_index()

load_product_color_basis()

load_retained_triplet_basis()

load_triplet_entry_statuses()

load_exact_triplet_expressions()

load_triplet_zero_certificates()

load_certified_source_emission()

load_certified_triplet_isometry()

load_certified_triplet_adjoint()

load_certified_triplet_projector()

embed_triplet_color_to_product(
    vector,
    precision=None,
)

project_product_color_to_triplet(
    vector,
    precision=None,
)

apply_triplet_projector(
    vector,
    precision=None,
)
```

Create:

```text
docs/next_level/c70_api_contract.json
docs/next_level/c70_api_validation.json
```

The API validator must compare the actual public surface with the frozen API fingerprint.

---

# 22. C71/QGEMBED6 import contract

Define the immutable contract by which C71 consumes:

```text
the C70 package-root hash;

the authenticated index;

the source/API fingerprints;

the complete basis manifests;

the 72-entry status domain;

the exact-expression and zero-certificate domains;

certified E_src, Gram, adapter, U3, U3-dagger, and P3;

all bounds;

the complete verified inventory;

the preserved C53-impact status;

the public frozen package object;

the embed/project/projector actions.
```

C71 must verify the C70 package root before combining it with C64.

C71 may not:

```text
call C66;

call a C68 builder;

call a C70 builder;

open unindexed runtime files;

infer status from magnitude;

factor P3;

renormalize U3;

or choose new column phases.
```

Create:

```text
docs/next_level/c70_c71_qgembed6_import_contract.json
```

---

# 23. Dry C71 import preflight

Run a dry preflight that:

```text
loads C64 through its immutable API;

loads C70 through the new package API;

verifies both package roots;

verifies all required runtime paths and inventories;

verifies all source/API fingerprints;

verifies immutable arrays and exact records;

verifies the basis metadata required for later kinematic/color
composition;

does not construct a CM-ground or full physical qg embedding.
```

The preflight must prove that the C69 blocker is resolved.

Create:

```text
docs/next_level/c70_c69_blocker_supersession_report.json
docs/next_level/c70_c71_import_preflight.json
```

---

# 24. Deterministic reconstruction

Run at least:

```text
two consecutive complete package builds;

one clean temporary-runtime build;

one serial build;

one supported parallel/sharded build when supported;

one restart/resume build from a partially complete valid package.
```

Require byte-identical payloads, `index.json`, `index.sha256`, manifests, and aggregate root identity.

A restart may reuse a file only when its source, schema, exact-object, payload, and bound hashes pass.

Create:

```text
docs/next_level/c70_deterministic_reconstruction_report.json
docs/next_level/c70_restart_parallel_report.json
docs/next_level/c70_environment_manifest.json
```

---

# 25. Count-once and provenance

Report:

```text
candidate U3 entries = 72;

status records;

exact nonzero expressions;

exact-zero certificates;

basis records;

certified numerical objects;

bound arrays;

indexed payloads;

control files;

missing files;

extra files;

orphan files;

duplicate paths;

duplicate object IDs;

hash mismatches;

schema mismatches;

writable returned arrays;

mutable returned exact records;

unbounded numerical entries;

unresolved-impact entries.
```

Every scientific object must have one ancestry path:

```text
C53 convention
    ->
C66 scientific object
    ->
C68 payload identity
    ->
C70 indexed payload
    ->
authenticated package root
    ->
read-only public loader.
```

Create:

```text
docs/next_level/c70_artifact_ancestry_ledger.json
docs/next_level/c70_count_once_report.json
```

A positive gate requires every error count to be zero.

---

# 26. Isolation and poisoning controls

Prove C70 package construction is unchanged when:

```text
C53 physical vertex numerical values are poisoned;

raw_emission_E numerical values are poisoned after the inherited
exact relation is frozen;

stored C53 24 x 24 projectors are poisoned;

all C47/C50/C52/C57/C58 numerical objects are poisoned;

all C64 arrays are inaccessible except during the final C71
preflight;

ART25 files are inaccessible.
```

The package must fail when:

```text
a scientific-source fingerprint changes;

an API signature changes;

index.json changes;

index.sha256 changes;

an indexed path changes;

an unindexed file appears;

an indexed file disappears;

a basis record changes;

a status changes;

an expression changes;

a zero certificate changes;

a midpoint or bound changes;

a returned array is writable;

a returned exact object is mutable;

a loader invokes a builder;

the package root changes.
```

Create:

```text
docs/next_level/c70_isolation_report.json
```

---

# 27. End-to-end source-to-package test

Implement an end-to-end test that begins from the immutable C66/C68 authorities, not from a pre-existing C70 package.

It must:

```text
verify source and API fingerprints;

construct or copy the self-contained payload;

verify byte identity with C68;

write the basis, status, expression, zero-certificate, numerical,
bound, and inventory payloads;

construct canonical index.json;

construct index.sha256;

construct the tracked package-root manifest;

load the package through the public C70 API;

verify every indexed payload;

compare every entry and companion object with C68/C66;

run package-only invariants and actions;

run the C71 import preflight with C64;

rebuild every file byte-for-byte.
```

It must fail when:

```text
one of the 72 statuses is omitted;

an exact expression or zero certificate is omitted;

index.json is not authenticated;

a payload is absent from the index;

an extra file exists;

a numerical value lacks a bound;

the loader bypasses the index;

the loader calls a builder;

the consumer must infer a basis order;

or a hash changes.
```

---

# 28. Focused mutation tests

Create at least **320 focused live mutations** of actual package objects.

Include mutations of:

```text
scientific-source hash;

API signature;

schema version;

index field;

index byte;

index.sha256;

package-root manifest;

payload relative path;

file size;

payload SHA-256;

object ID;

row basis ID;

column basis ID;

basis order;

entry status;

exact expression;

zero certificate;

support hash;

E_src value;

Gram value;

adapter value;

U3 value;

U3-dagger value;

P3 value;

numerical bound;

dtype;

endianness;

inventory row;

extra runtime file;

missing runtime file;

read-only flag;

frozen-record flag;

no-regeneration guard;

C53-impact status;

C71 import-contract field;

restart reuse decision.
```

Every mutation must fail a concrete source, API, index, inventory, basis, exact-record, certification, immutability, import, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 29. Readiness gate

Issue:

```text
C70_SOURCE_DERIVED_TRIPLET_PACKAGE_IMPORT_READY
```

only when:

```text
the full baseline reproduces;

the C69 import finding remains explicit;

the C66 and C68 scientific payload remains unchanged;

all scientific-source fingerprints exist and verify;

the public-API fingerprint exists and verifies;

one deterministic package schema is frozen;

the complete self-contained payload exists;

all copied payloads are byte-identical to C68;

canonical index.json exists;

index.json is authenticated before use;

the package-root manifest exists;

the package aggregate/root identity covers every payload hash and
every package fingerprint;

the inventory has no missing, extra, orphan, duplicate, unhashed,
unbounded, or schema-mismatched object;

the basis loaders are complete and immutable;

the 72-entry status loader is complete and immutable;

the exact-expression loader is complete and immutable;

the exact-zero-certificate loader is complete and immutable;

all numerical loaders verify midpoints and bounds and return
non-writeable arrays;

the frozen top-level package object verifies the complete package;

the no-regeneration guard closes;

complete C68/C66 equivalence passes;

package-only invariants and actions pass;

the C71 import contract is complete;

the C71 dry preflight with C64 and C70 passes;

the C69 blocker supersession is explicit;

serial, clean, repeated, restart, and supported parallel
reconstruction pass;

count-once and provenance close;

poisoning controls pass;

the end-to-end test passes.
```

Do not issue:

```text
C70_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY;

C70_IFERM_CONTACT_SUPPORT_READY;

C70_DIRECT_IFERM_CONTACT_READY;

C70_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C70_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY.
```

---

# 30. Exact no-go branches

## A. Scientific-source or API fingerprint incomplete

```text
C70_QGCOLOR_PACKAGE_FINGERPRINT_INCOMPLETE
```

Next:

> **C71/QGCOLOR-SRC3 — exact source, API, serializer, and dependency fingerprint closure**

## B. Index authentication incomplete

```text
C70_QGCOLOR_PACKAGE_INDEX_INCOMPLETE
```

Next:

> **C71/QGCOLOR-INDEX — canonical index, sidecar authentication, and package-root closure**

## C. Exact-record loaders incomplete

```text
C70_QGCOLOR_PACKAGE_EXACT_RECORD_IMPORT_INCOMPLETE
```

Next:

> **C71/QGCOLOR-RECORDS — status, expression, zero-certificate, basis, and immutable-record loader closure**

## D. Inventory or numerical loader incomplete

```text
C70_QGCOLOR_PACKAGE_RUNTIME_IMPORT_INCOMPLETE
```

Next:

> **C71/QGCOLOR-INVENTORY — aggregate inventory, numerical/bound loader, immutability, and no-regeneration closure**

## E. C68/C70 equivalence fails

```text
C70_QGCOLOR_PACKAGE_EQUIVALENCE_FAILED
```

Next:

> **C71/QGCOLOR-XCHECK3 — payload, exact-record, action, invariant, and package-root reconciliation**

## F. Package closure succeeds

```text
C70_SOURCE_DERIVED_TRIPLET_PACKAGE_IMPORT_READY
```

Next:

> **C71/QGEMBED6 — exact physical \(qg\) embedding and descendant-impact closure**

---

# 31. Required deliverables

Create at least:

```text
docs/next_level/c70_implementation_report.md
docs/next_level/c70_api.md
docs/next_level/c70_derivation_authority_manifest.json
docs/next_level/c70_input_fidelity_audit.json

docs/next_level/c70_source_fingerprint_manifest.json
docs/next_level/c70_source_fingerprint_validation.json
docs/next_level/c70_api_fingerprint_manifest.json
docs/next_level/c70_api_fingerprint_validation.json

docs/next_level/c70_package_schema_contract.json
docs/next_level/c70_serializer_version_contract.json
docs/next_level/c70_payload_copy_equivalence_report.json
docs/next_level/c70_payload_completeness_report.json

docs/next_level/c70_index_schema_contract.json
docs/next_level/c70_index_content_manifest.json
docs/next_level/c70_package_root_manifest.json
docs/next_level/c70_index_authentication_report.json

docs/next_level/c70_runtime_inventory_report.json
docs/next_level/c70_runtime_inventory_validation.json

docs/next_level/c70_status_loader_contract.json
docs/next_level/c70_status_loader_validation.json
docs/next_level/c70_expression_loader_contract.json
docs/next_level/c70_expression_loader_validation.json
docs/next_level/c70_zero_certificate_loader_contract.json
docs/next_level/c70_zero_certificate_loader_validation.json
docs/next_level/c70_numerical_loader_contract.json
docs/next_level/c70_numerical_loader_validation.json
docs/next_level/c70_package_object_contract.json
docs/next_level/c70_package_object_validation.json
docs/next_level/c70_no_regeneration_report.json

docs/next_level/c70_c68_entry_equivalence_report.json
docs/next_level/c70_c68_object_equivalence_report.json
docs/next_level/c70_package_invariant_report.json

docs/next_level/c70_api_contract.json
docs/next_level/c70_api_validation.json
docs/next_level/c70_c71_qgembed6_import_contract.json
docs/next_level/c70_c69_blocker_supersession_report.json
docs/next_level/c70_c71_import_preflight.json

docs/next_level/c70_deterministic_reconstruction_report.json
docs/next_level/c70_restart_parallel_report.json
docs/next_level/c70_environment_manifest.json
docs/next_level/c70_artifact_ancestry_ledger.json
docs/next_level/c70_count_once_report.json
docs/next_level/c70_isolation_report.json

docs/next_level/c70_readiness_report.json
docs/next_level/c70_source_sufficiency_decision.json
docs/next_level/c70_no_go_decision_tree.json
docs/next_level/c70_missing_calculation_specification.md
docs/next_level/c70_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/qgcolor4/
```

or the repository-equivalent package.

Use the deterministic runtime root:

```text
data/runtime/c70_qgcolor4/
```

Add focused tests for:

```text
source and API fingerprints;
package schema;
self-contained payload;
authenticated index;
package root;
complete inventory;
basis loaders;
status loader;
expression loader;
zero-certificate loader;
numerical loaders;
immutable package object;
no-regeneration guards;
complete C68 equivalence;
package-only invariants/actions;
C71 import preflight;
restart and deterministic reconstruction;
end-to-end source-to-package closure.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All committed JSON and every runtime artifact must reconstruct byte-for-byte.

---

# 32. Acceptance criteria

C70 is complete only when:

1. The exact baseline `031ac09fe3aeac19f281255ae2a0f014092485e8` reproduces.
2. The C69 import finding remains explicit.
3. C66/C68 scientific identities remain unchanged.
4. C53, C64, C66, C67, and C68 historical artifacts remain byte-identical.
5. C40 remains method-oracle only.
6. No physical \(qg\) embedding is constructed.
7. No contact support, value, or matrix is constructed.
8. No \(U_3\) entry is rederived or renormalized.
9. No basis phase or order changes.
10. Complete scientific-source fingerprints exist.
11. Complete public-API fingerprints exist.
12. One deterministic schema is frozen.
13. One self-contained C70 runtime package exists.
14. Every copied payload is byte-identical to C68.
15. Every payload has one scientific object ID.
16. Every payload appears exactly once in `index.json`.
17. `index.json` is canonical.
18. `index.json` is authenticated before payload use.
19. The package-root manifest agrees with `index.sha256`.
20. The authenticated index covers every payload hash.
21. The authenticated index covers source/API/schema identities.
22. No required payload is missing.
23. No unindexed or orphan file exists.
24. No duplicate path or object ID exists.
25. Every shape, dtype, size, and record count verifies.
26. All 24 row-basis records load read-only.
27. All 3 column-basis records load read-only.
28. All 72 statuses load read-only.
29. Every exact nonzero expression loads read-only.
30. Every exact-zero certificate loads read-only.
31. Exact support is independent of numerical magnitude.
32. Every midpoint is coupled to a verified bound.
33. Every numerical array is non-writeable.
34. Every exact record and metadata object is immutable.
35. The top-level package object verifies the full package.
36. No public loader calls a builder.
37. No public loader regenerates a missing file.
38. Missing or altered files fail closed.
39. Every C70 entry agrees with C68/C66.
40. Every companion object agrees with C68/C66.
41. Package-only isometry/projector/intertwiner invariants close.
42. The inherited C53-impact status is preserved.
43. The C71 import contract is complete.
44. The C71 dry preflight passes using only C64 and C70 public APIs.
45. The C69 blocker has an explicit descendant supersession.
46. Two consecutive builds are byte-identical.
47. A clean build is byte-identical.
48. Serial and supported parallel builds agree.
49. Restart reuses only fully verified files.
50. Every object has complete ancestry.
51. Missing, extra, orphan, duplicate, hash-mismatch, schema-mismatch, writable, mutable, unbounded, and unresolved counts are zero.
52. Static and runtime poisoning controls pass.
53. At least 320 focused live mutations are detected.
54. No descendant physics status is promoted beyond package import readiness.
55. No endpoint/witness relation, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
56. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
57. `MSHT20_REP/` remains untouched and outside Git.
58. The working tree is clean except for the pre-existing untracked directory.
59. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken source/API fingerprints, index authentication, inventory completeness, exact-record loaders, numerical-bound coupling, immutability, or no-regeneration semantics to open the gate.

---

# 33. Final Codex response

Report:

- starting and final commits;
- exact C66/C68 scientific identities preserved;
- scientific-source and public-API aggregate fingerprints;
- schema and serializer versions;
- C70 runtime root;
- payload and control-file counts;
- 24-row and 3-column basis hashes;
- 72-entry status counts by class;
- exact-expression and zero-certificate counts;
- authenticated `index.json` hash;
- package aggregate/root hash;
- indexed, missing, extra, orphan, duplicate, unhashed, schema-mismatched, and unbounded counts;
- numerical object shapes, dtypes, hashes, and maximum bounds;
- immutable basis/status/expression/zero-certificate/numerical loader results;
- top-level package-object validation;
- no-regeneration guard results;
- complete C68/C66 entry and object equivalence;
- package-only isometry, projector, intertwiner, and leakage results;
- C53-impact preservation;
- C69 blocker-supersession result;
- C71 import-preflight result;
- repeated, clean, serial, parallel, and restart determinism;
- ancestry and count-once results;
- isolation and poisoning results;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no physical \(qg\) embedding, descendant support promotion, endpoint/witness relation, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe individually hash-checked arrays without an authenticated package index, an unverified `index.json`, a loader that omits exact statuses/expressions/zero certificates, a writable returned object, an incomplete inventory, or a loader that calls a builder as a complete immutable triplet runtime package.
