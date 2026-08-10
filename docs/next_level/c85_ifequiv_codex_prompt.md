# C85/IFEQUIV Codex Work Package

## Title

**Historical-versus-regenerated C82 equivalence closure: commit-pinned reconstruction, canonical scientific-record root, field-level runtime-hash diagnosis, descendant reconstruction guard, and C86 persisted-snapshot handoff**

## Authoritative baseline

Start from the clean local C84 completion commit:

```text
c3ae3656ece71a60d86e8b2133ab32018ee0b353
```

Before changing tracked files, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
test "$(git rev-parse HEAD)" = "c3ae3656ece71a60d86e8b2133ab32018ee0b353"
```

The following pre-existing untracked paths must remain untouched and outside Git:

```text
MSHT20_REP/
docs/next_level/c69_qgembed5_codex_prompt.md
```

Do not add, modify, remove, rename, stage, or consume either path as scientific authority.

Read completely and preserve the committed continuation contract:

```text
docs/next_level/c85_ifequiv_contract.md
```

If that contract freezes exact status names, schemas, APIs, or a narrower
scientific boundary, preserve them. This prompt supplies the reconstruction,
comparison, and canonical-root plan; it does not authorize weakening the
committed contract.

The baseline is authoritative only when it contains and reproduces:

```text
C82_SOURCE_DERIVED_IFCONTACT_AGGREGATION_BRIDGE_READY

C83_IFCONTACT_SHARED_COORDINATE_INCOMPLETE

C84_IFCOORD2_MATERIALIZATION_INCOMPLETE
```

and the exact C84 finding:

```text
the C82 scientific bridge remains unchanged;

the historical C82 runtime report and a clean regenerated C82
runtime carry different authenticated bridge/index hashes;

the C82 runtime payload is metadata-oriented and does not itself
persist the complete logical pair-coordinate record domain;

therefore C84 cannot certify a complete immutable snapshot as
equivalent to the historical C82 result;

no coefficient-times-kernel product, contact matrix/action,
physical coupling, counterterm, C53 contribution, or C58
contribution was created.
```

The historical C82 completion commit is:

```text
8e47231ab565f0f729d335b39aa98881176ba166
```

Verify every actual historical hash, regenerated hash, source/API
fingerprint, root/index field, package input, logical coefficient record,
and reconstruction command from the repository. This prompt is not
numerical authority.

Create a local completion commit. Do not push.

---

# 1. Scientific classification of the C84 obstruction

C85 must distinguish three different objects:

```text
A. the C82 scientific bridge:
       logical pair-coordinate identities, projected coefficients,
       statuses, bounds, factor ownership, and ancestry;

B. a C82 runtime-package instance:
       index/root, source/API fingerprints, paths, environment
       records, serializer metadata, and instance-level hashes;

C. descendant documentation and handoff state:
       roadmap, formalism index, prompts, reports, current HEAD,
       and other append-only or mutable descendant files.
```

A difference in object B or C does not prove a difference in object A.

Conversely, equal counts and prose do not prove scientific equivalence.

C85 must determine whether the historical and regenerated C82 routes
produce the same complete canonical scientific record stream.

No external source is required for this task. Commit-pinned Git objects,
the exact C82 source, upstream package roots, and deterministic logical
records are the authority.

A fail-closed result is required if:

```text
the C82 completion commit cannot reconstruct a deterministic
scientific record stream;

historical and regenerated scientific record streams differ;

the runtime-root mismatch cannot be localized to explicit fields;

or a canonical scientific root cannot be defined without omitting
a scientifically meaningful record.
```

Do not treat a changed current commit hash, absolute path, timestamp,
environment string, roadmap hash, or descendant API fingerprint as a
scientific mismatch unless it changes the logical record domain.

---

# 2. Descendant qualifications

Do not alter historical C82, C83, or C84 files.

Create explicit descendant qualifications:

```text
C82_SOURCE_DERIVED_IFCONTACT_AGGREGATION_BRIDGE_READY
    -> C82_SCIENTIFIC_BRIDGE_VALID_RUNTIME_INSTANCE_IDENTITY_UNRESOLVED

C84_IFCOORD2_MATERIALIZATION_INCOMPLETE
    -> exact cause:
       historical/regenerated C82 runtime identity mismatch prevents
       certification of a persisted snapshot.
```

These qualifications must not prejudge whether the mismatch is scientific
or metadata-only.

Create:

```text
docs/next_level/c85_descendant_qualification.json
```

---

# 3. Exact purpose and stopping point

C85 must produce:

```text
a clean reconstruction of C82 at its historical completion commit;

a clean reconstruction of the C82 logical bridge under the current
descendant repository;

an optional third reconstruction using historical C82 source bytes
inside the current environment;

a canonical scientific-record schema;

record, pair, resolution, and aggregate scientific digests;

a field-level comparison of historical and regenerated runtime
root/index objects;

a typed explanation of every differing field;

a canonical authority decision;

a descendant reconstruction guard that prevents current mutable
files from changing historical scientific reconstruction;

a builder-only canonical scientific-stream interface for C86;

and a C86/IFPERSIST2 import contract.
```

C85 must not:

```text
persist the complete pair-coordinate snapshot intended for C86;

multiply a projected coefficient by a C80 kernel;

construct a contact matrix or action;

select a physical coupling or counterterm;

add C53 or C58;

or assemble the complete instantaneous-fermion operator.
```

The preferred favorable status is:

```text
C85_C82_SCIENTIFIC_PAYLOAD_EQUIVALENCE_READY
```

If `c85_ifequiv_contract.md` freezes another exact spelling, preserve it
and record a semantic alias.

The favorable continuation is:

> **C86/IFPERSIST2 — materialize and authenticate the complete pair-coordinate snapshot against the immutable C85 scientific root, with an upstream-free public import API**

---

# 4. Mandatory repository audit

Read completely the actual repository equivalents of:

```text
C82:
    implementation report;
    readiness report;
    runtime report;
    runtime root/index;
    factor-ownership records;
    coordinate-map records;
    projected-coefficient records;
    deterministic reconstruction;
    public/lazy constructor;
    source/API fingerprints;
    tests and validator;

C83:
    C82 import audit;
    shared-coordinate no-go;
    C84 contract;

C84:
    implementation report;
    historical/regenerated hash comparison;
    materialization audit;
    C85 contract;

upstream identities consumed by C82:
    C77/C74 projection authority;
    C78 support/witness authority;
    C80 coordinate schema;
    exact package/root identities.
```

Inventory tracked and runtime paths:

```bash
git ls-files 'docs/next_level/c82*'
git ls-files 'docs/next_level/c83*'
git ls-files 'docs/next_level/c84*'
git ls-files 'src/deuteron_wigner/**/ifagg*'
git ls-files 'tests/*c82*' 'tests/*c83*' 'tests/*c84*'
find data/runtime -maxdepth 3 -type f | sort
```

Create:

```text
docs/next_level/c85_derivation_authority_manifest.json
docs/next_level/c85_input_fidelity_audit.json
```

---

# 5. Controlled reconstruction environments

Create clean temporary detached Git worktrees or equivalent immutable
archives for at least:

```text
HIST:
    C82 completion commit
    8e47231ab565f0f729d335b39aa98881176ba166;

DESC:
    current C84 baseline
    c3ae3656ece71a60d86e8b2133ab32018ee0b353.
```

A third route is strongly preferred:

```text
PINNED:
    historical C82 source and tracked input bytes from the C82
    completion commit, executed under the current C85 environment.
```

Use a controlled execution environment:

```text
TZ=UTC;
LC_ALL=C;
PYTHONHASHSEED=0;
SOURCE_DATE_EPOCH fixed to the C82 commit time where supported;
same Python executable and dependency set for compared routes;
clean runtime directories;
no pre-existing generated payloads.
```

Record all environment differences, but do not automatically include them
in the scientific record root.

Create:

```text
docs/next_level/c85_reconstruction_environment_manifest.json
docs/next_level/c85_git_worktree_reconstruction_plan.json
```

Do not modify either temporary worktree's tracked files merely to force a
match.

---

# 6. Historical C82 reconstruction

Inside the historical C82 worktree:

1. verify the exact commit and clean status;
2. run the original C82 tests, builder, and validator using the historical
   commands;
3. generate a completely fresh runtime;
4. repeat the build at least twice;
5. record all runtime/index/root hashes;
6. compare them with every C82 hash frozen in the historical tracked
   reports/manifests.

Classify:

```text
HISTORICAL_RUNTIME_EXACTLY_REPRODUCED;

HISTORICAL_SCIENCE_REPRODUCED_RUNTIME_INSTANCE_DIFFERS;

HISTORICAL_C82_RECONSTRUCTION_NONDETERMINISTIC;

HISTORICAL_C82_RECORDED_HASH_UNREPRODUCIBLE.
```

Do not declare the historical root authoritative merely because it appears
in prose. It must either reproduce or be explicitly qualified.

Create:

```text
docs/next_level/c85_historical_c82_reconstruction_report.json
```

---

# 7. Current descendant reconstruction

Under the current C84/C85 source tree, run the C82 scientific route and
runtime builder in a clean directory.

Record:

```text
current source/API fingerprints;
upstream package roots;
runtime root/index;
logical counts;
pair-coordinate iteration order;
coefficient/status/bound identities;
ancestry identities.
```

Do not compare only top-level hashes.

Create:

```text
docs/next_level/c85_descendant_c82_reconstruction_report.json
```

The current route is a comparison route. It does not supersede the
historical route merely because it is newer.

---

# 8. Canonical scientific-record schema

Define one canonical logical record schema for C82 scientific equivalence.

Each record must include every scientifically meaningful field, including
the actual repository equivalents of:

```text
schema version for the scientific record only;
resolution ID;
supported-pair ID;
physical bra and ket IDs;
canonical C80 coordinate ID;
C80 exact coordinate-equivalence ID;
projected-coefficient exact-record/expression identity;
coefficient real and imaginary midpoint;
certified absolute bound;
interval convention and precision;
terminal coefficient status;
factor-ownership identity;
witness multiplicity;
reversible witness/endpoint/projection ancestry digest.
```

Exclude from the scientific-record serialization unless they alter one of
those fields:

```text
absolute filesystem path;
wall-clock timestamp;
current descendant HEAD;
temporary worktree path;
host name;
process ID;
shard execution order;
roadmap or formalism-index current bytes;
narrative report path;
environment display string.
```

The exclusion must be explicit and justified field by field.

Create:

```text
docs/next_level/c85_scientific_record_schema.json
docs/next_level/c85_scientific_record_schema_validation.json
```

---

# 9. Canonical ordering and Merkle-style roots

Stream the complete logical scientific domain in the frozen order:

```text
resolution;
physical pair order;
canonical C80 coordinate/equivalence order;
canonical record ID.
```

Compute:

```text
per-record digest;
ordered per-pair digest;
per-resolution digest;
aggregate C82 scientific bridge root.
```

The aggregate scientific root must bind:

```text
the canonical scientific schema;
the exact upstream scientific package roots;
the complete record stream;
the count-once and ancestry semantics.
```

It must not bind mutable descendant prose or machine-local paths.

Compute the scientific root independently for HIST, DESC, and PINNED.

Create:

```text
docs/next_level/c85_scientific_root_manifest.json
docs/next_level/c85_scientific_root_validation.json
```

Report exact logical record counts by resolution. Do not assume one record
per supported pair.

---

# 10. Exhaustive scientific equivalence

Compare HIST and DESC, and HIST and PINNED when available, for every logical
record.

Require explicit counts for:

```text
missing/extra pairs;
missing/extra records;
pair-order differences;
coordinate-ID differences;
equivalence-ID differences;
coefficient exact-record differences;
coefficient midpoint differences;
bound differences;
status differences;
factor-ownership differences;
witness multiplicity differences;
ancestry differences.
```

A favorable result requires every scientific mismatch count to be zero.

Create:

```text
docs/next_level/c85_exhaustive_scientific_equivalence_report.json
```

A sampled comparison is insufficient.

---

# 11. Runtime root/index field-level diff

Parse the historical tracked runtime report, the historical regenerated
runtime, and the descendant regenerated runtime into typed fields.

For every differing hash or field, classify it as one of:

```text
SCIENTIFIC_PAYLOAD_DIFFERENCE;

SCIENTIFIC_INPUT_ROOT_DIFFERENCE;

SOURCE_OR_API_FINGERPRINT_DIFFERENCE;

SERIALIZER_OR_SCHEMA_DIFFERENCE;

DESCENDANT_DOCUMENTATION_DIFFERENCE;

CURRENT_HEAD_OR_GIT_METADATA_DIFFERENCE;

ABSOLUTE_PATH_OR_ENVIRONMENT_DIFFERENCE;

TIMESTAMP_OR_NONDETERMINISTIC_METADATA_DIFFERENCE;

SHARD_OR_FILE_LAYOUT_DIFFERENCE_WITH_EQUAL_LOGICAL_CONTENT;

UNRESOLVED_DIFFERENCE.
```

Identify the exact source path and producer function for each difference.

Create:

```text
docs/next_level/c85_runtime_root_field_diff.json
docs/next_level/c85_runtime_hash_cause_report.md
```

Do not use the phrase "metadata only" without enumerating the differing
fields and proving that the canonical scientific records are unchanged.

---

# 12. Historical-hash decision tree

Apply this decision logic.

## Route A — historical runtime reproduces exactly

When the clean C82 worktree reproduces the recorded historical runtime
root/index:

```text
retain the historical runtime root as historical authority;
retain the C85 scientific root as the cross-instance scientific
equivalence authority;
explain all descendant runtime differences.
```

## Route B — historical runtime instance differs, science reproduces

When repeated clean historical builds agree with one another and the
complete scientific record stream is stable, but the old tracked runtime
hash does not reproduce:

```text
qualify the old runtime-instance hash as
HISTORICAL_RUNTIME_INSTANCE_HASH_UNREPRODUCIBLE;

do not invalidate the C82 science automatically;

create a descendant canonical scientific root from the exact C82
completion source and immutable upstream roots;

require HIST, DESC, and PINNED scientific roots to agree before a
positive C85 result.
```

## Route C — historical builds are nondeterministic

Fail closed. Identify every nondeterministic field and producer.

## Route D — scientific records differ

Fail closed regardless of equal counts or similar prose.

Create:

```text
docs/next_level/c85_canonical_authority_decision.json
```

---

# 13. Descendant historical-reconstruction guard

When scientific equivalence closes, implement a C85-owned reconstruction
guard that allows later builders to reconstruct the canonical C82
scientific stream from exact historical authority.

The guard must bind:

```text
C82 completion commit;
historical C82 source-file hashes;
historical upstream scientific roots;
scientific-record schema;
canonical ordering;
expected scientific root;
expected record counts.
```

It must not read current mutable descendant versions of:

```text
C82 source files that changed after completion;
ROADMAP.md;
formalism_volume_index.md;
later prompts or reports;
current HEAD as scientific input.
```

The guard may use:

```text
a detached temporary worktree;
git-show/git-archive bytes;
or a content-addressed retained source bundle generated from Git
objects.
```

Do not distribute font files or unrelated binaries.

Create:

```text
docs/next_level/c85_historical_reconstruction_guard_contract.json
docs/next_level/c85_historical_reconstruction_guard_validation.json
```

---

# 14. Canonical builder-only scientific-stream API

Implement under:

```text
src/deuteron_wigner/bridge/ifequiv/
```

or the exact repository-equivalent package.

Provide builder/validation operations equivalent to:

```python
reconstruct_canonical_c82_scientific_stream()

verify_canonical_c82_scientific_root()

iterate_canonical_c82_pair_coordinate_records(
    resolution=None,
    pair_start=None,
    pair_stop=None,
)

canonical_c82_pair_digest(bra_id, ket_id, resolution)
```

This interface is for C86 materialization and validation. It is not yet the
upstream-free public persisted loader.

Requirements:

```text
verify historical source/input hashes before yielding records;
yield deterministic frozen records;
reconstruct the expected scientific root;
call no C80 kernel-value multiplication;
add no g_s^2;
form no contact matrix.
```

Create:

```text
docs/next_level/c85_canonical_stream_api_contract.json
docs/next_level/c85_canonical_stream_api_validation.json
```

---

# 15. C86/IFPERSIST2 import contract

Define the exact contract by which C86 consumes:

```text
the C85 canonical scientific root;
the exact scientific-record schema;
the canonical ordering;
the historical reconstruction guard;
the builder-only canonical stream;
the expected pair and record counts;
the per-pair digest semantics;
the bound C77/C74/C78/C80/C82 scientific identities.
```

C86 must:

```text
persist every canonical logical record;
authenticate shards, pair digests, record digests, index, and root;
compare the persisted snapshot exhaustively with the C85 stream;
expose an upstream-free public loader.
```

C86 must not decide again which C82 runtime-instance root is authoritative.

Create:

```text
docs/next_level/c85_c86_ifpersist2_import_contract.json
```

---

# 16. Determinism and independence checks

Run:

```text
two historical reconstructions;
two descendant reconstructions;
two PINNED reconstructions when supported;
serial and deterministic sharded scientific-root construction;
restart/resume root construction.
```

Require:

```text
byte-identical canonical scientific schema;
identical logical record counts;
identical record/pair/resolution/aggregate scientific digests;
identical authority decision;
identical tracked reports.
```

The runtime package-instance hashes may differ only through fields already
typed in the root-diff report.

Create:

```text
docs/next_level/c85_deterministic_reconstruction_report.json
docs/next_level/c85_resource_and_scaling_report.json
```

---

# 17. Isolation and negative controls

Prove the canonical scientific root is unchanged by mutations of excluded
instance metadata:

```text
temporary path;
host name;
timestamp;
process ID;
current descendant commit;
roadmap bytes;
formalism-index bytes;
shard order;
environment display string.
```

Require failure for mutations of included scientific fields:

```text
upstream scientific root;
pair ID;
coordinate ID;
equivalence ID;
coefficient exact record;
coefficient midpoint;
coefficient bound;
terminal status;
factor ownership;
witness multiplicity;
ancestry digest;
canonical order;
scientific schema version.
```

Poison:

```text
C80 numerical kernel values;
C53 values/propagators;
C58 values;
physical coupling and counterterm interfaces.
```

The C85 scientific root must remain independent of those values.

Create at least **384 focused live mutations**.

Create:

```text
docs/next_level/c85_isolation_report.json
docs/next_level/c85_regression_report.json
```

---

# 18. Readiness and continuation decisions

Select exactly one branch.

## 18.1 Favorable branch

Issue the exact positive status frozen by the C85 contract, with preferred
semantic identity:

```text
C85_C82_SCIENTIFIC_PAYLOAD_EQUIVALENCE_READY
```

Required:

```text
the historical C82 source route reconstructs deterministically;
the complete canonical scientific record schema is frozen;
HIST and DESC scientific roots agree;
PINNED agrees when available;
all exhaustive scientific mismatch counts are zero;
every runtime-root difference is typed;
the canonical authority decision is explicit;
the historical reconstruction guard passes;
the canonical builder-only stream reproduces the scientific root;
the C86 import contract is complete;
determinism, isolation, and mutations pass.
```

Next:

> **C86/IFPERSIST2 — complete authenticated persisted pair-coordinate snapshot and upstream-free public import**

## 18.2 Historical reconstruction unreproducible

```text
C85_C82_HISTORICAL_RECONSTRUCTION_INCOMPLETE
```

Use when the exact C82 completion source cannot generate a deterministic
scientific stream or the recorded historical authority cannot be
reconciled.

Next:

> **C86/IFHIST — repair only the specifically identified historical source/input/runtime reconstruction defect**

## 18.3 Scientific payload mismatch

```text
C85_C82_SCIENTIFIC_PAYLOAD_MISMATCH
```

Next:

> **C86/IFSCIDIFF — repair only the specifically identified pair, coordinate, coefficient, bound, status, factor-ownership, or ancestry mismatch**

## 18.4 Runtime-hash cause unresolved

```text
C85_C82_RUNTIME_HASH_CAUSE_UNRESOLVED
```

Next:

> **C86/IFROOTDIFF — localize only the unresolved root/index producer or serialization difference**

## 18.5 Canonical stream API incomplete

```text
C85_IFEQUIV_CANONICAL_STREAM_INCOMPLETE
```

Next:

> **C86/IFSTREAM — repair only the historical guard, canonical ordering, digest, iterator, or builder-only API defect**

Do not issue a persisted-import, coefficient-times-kernel, contact-matrix,
complete-instantaneous-fermion, counterterm-solved, local-QCD, TMD,
matching, inference, or production status.

---

# 19. Essential deliverables

Create at least:

```text
docs/next_level/c85_implementation_report.md
docs/next_level/c85_derivation_authority_manifest.json
docs/next_level/c85_input_fidelity_audit.json
docs/next_level/c85_descendant_qualification.json

docs/next_level/c85_reconstruction_environment_manifest.json
docs/next_level/c85_git_worktree_reconstruction_plan.json
docs/next_level/c85_historical_c82_reconstruction_report.json
docs/next_level/c85_descendant_c82_reconstruction_report.json

docs/next_level/c85_scientific_record_schema.json
docs/next_level/c85_scientific_record_schema_validation.json
docs/next_level/c85_scientific_root_manifest.json
docs/next_level/c85_scientific_root_validation.json
docs/next_level/c85_exhaustive_scientific_equivalence_report.json

docs/next_level/c85_runtime_root_field_diff.json
docs/next_level/c85_runtime_hash_cause_report.md
docs/next_level/c85_canonical_authority_decision.json

docs/next_level/c85_historical_reconstruction_guard_contract.json
docs/next_level/c85_historical_reconstruction_guard_validation.json
docs/next_level/c85_canonical_stream_api_contract.json
docs/next_level/c85_canonical_stream_api_validation.json
docs/next_level/c85_c86_ifpersist2_import_contract.json

docs/next_level/c85_deterministic_reconstruction_report.json
docs/next_level/c85_resource_and_scaling_report.json
docs/next_level/c85_isolation_report.json
docs/next_level/c85_readiness_report.json
docs/next_level/c85_regression_report.json
```

Add implementation under:

```text
src/deuteron_wigner/bridge/ifequiv/
```

or the exact repository-equivalent path.

Use runtime space only for temporary or content-addressed equivalence
records under:

```text
data/runtime/c85_ifequiv/
```

Do not persist the final C86 public snapshot in C85.

Create exactly one next-package contract corresponding to the selected
branch.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

Do not add or modify the old untracked C69 prompt.

---

# 20. Acceptance criteria

C85 is complete only when:

1. Baseline `c3ae3656ece71a60d86e8b2133ab32018ee0b353` reproduces.
2. Both protected untracked paths remain untouched.
3. C82/C83/C84 historical artifacts remain unchanged.
4. `c85_ifequiv_contract.md` is consumed and preserved.
5. The C82 completion commit is reconstructed in a clean detached environment.
6. Historical reconstruction is repeated.
7. Current descendant reconstruction is repeated.
8. PINNED historical-source/current-environment reconstruction is executed when feasible.
9. A complete canonical scientific-record schema is frozen.
10. The schema contains every pair-coordinate coefficient, status, bound, ownership, and ancestry field.
11. Machine-local and descendant-only metadata are explicitly excluded.
12. Per-record, pair, resolution, and aggregate scientific roots are computed.
13. Actual logical record counts are derived.
14. HIST and DESC are compared exhaustively.
15. Every scientific mismatch count is zero in the favorable branch.
16. PINNED agrees in the favorable branch when supported.
17. The historical tracked runtime hash is either reproduced or explicitly qualified.
18. Every runtime root/index difference is classified field by field.
19. No unresolved difference remains in the favorable branch.
20. The canonical authority decision is explicit.
21. The historical reconstruction guard binds exact C82 source/input bytes.
22. The guard ignores current mutable descendant prose and HEAD.
23. The canonical builder-only stream reproduces the scientific root.
24. C80 kernel values and \(g_s^2\) are absent from the scientific record.
25. No coefficient-times-kernel product is formed.
26. No persisted C86 public snapshot is claimed.
27. The C86 import contract is complete.
28. Serial, sharded, and restart scientific-root construction agrees.
29. Excluded-metadata mutations leave the scientific root unchanged.
30. Scientific-field mutations fail.
31. At least 384 focused live mutations pass.
32. No contact matrix/action, physical coupling, counterterm, C53/C58 contribution, complete instantaneous-fermion operator, local-QCD Hamiltonian, TMD/matching, fit, inference, or production object is created.
33. `NO_JOINT_MEASURE`, 216 routes, 642 ART25 identities, and authoritative artifacts remain unchanged.
34. The working tree is clean except for the two protected untracked paths.
35. A local completion commit is created and not pushed.

Do not force runtime-instance hashes to match by editing scientific records,
dropping fields, weakening digests, or copying a historical hash. Scientific
equivalence must be demonstrated independently of package-instance
metadata.

---

# 21. Final Codex response

Report:

- starting and final commits;
- untouched protected paths;
- consumed C85 contract identity;
- historical C82 completion commit;
- historical tracked runtime bridge/index hashes;
- historical regenerated hashes for both builds;
- descendant regenerated hashes;
- PINNED hashes when available;
- canonical scientific schema hash;
- actual pair-coordinate logical counts by resolution;
- record, pair, resolution, and aggregate scientific roots for every route;
- exhaustive scientific mismatch counts by category;
- exact field-level causes of runtime-root differences;
- classification of the historical recorded hash;
- canonical authority decision;
- historical reconstruction-guard hash;
- canonical stream API validation;
- C86 import-contract result;
- deterministic serial/sharded/restart results;
- isolation and mutation results;
- exact readiness/no-go status;
- exact next branch;
- confirmation that no complete persisted snapshot, coefficient-times-kernel product, contact matrix/action, physical coupling, counterterm, C53/C58 contribution, complete instantaneous-fermion operator, TMD/matching, fit, inference, or production object was created;
- confirmation that nothing was pushed.
