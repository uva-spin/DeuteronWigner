# C78/IFSUPPORT2 Codex Work Package

## Title

**Exact source-ordered direct instantaneous-fermion contact support from the immutable C77 physical \(qg\) embedding: absorption/emission endpoints, retained-\(q\) intermediate witnesses, symbolic projected-cancellation closure, and C79 contact-matrix handoff**

## Authoritative baseline

Start from the clean local C77 completion commit:

```text
5a117fa29442195a52f67da6fa00368a28a13e8f
```

Before changing tracked files, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
test "$(git rev-parse HEAD)" = "5a117fa29442195a52f67da6fa00368a28a13e8f"
```

The following pre-existing untracked paths must remain untouched and outside Git:

```text
MSHT20_REP/
docs/next_level/c69_qgembed5_codex_prompt.md
```

Do not add, modify, remove, rename, stage, or consume either path as scientific authority.

The baseline is authoritative only when it contains and reproduces:

```text
C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE
C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
C59_IFERM_CONTACT_SUPPORT_INCOMPLETE
C60_IFSUPPORT_QG_EMBEDDING_INCOMPLETE
C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY
```

and the exact inherited result:

```text
C77:
    project-owned canonical raw and relative/CM identities;
    deterministic global ordering;
    explicit n_CM and m_CM;
    raw -> relative/CM identity orientation;
    733 C64 blocks;
    171,153 exact statuses;
    67,920 residue certificates;
    9,321 raw transverse identities;
    9,321 relative/CM transverse identities;
    CM-ground counts 112 / 225 / 396;
    authenticated factorized CM-ground/triplet embedding package;
    zero CM-excited, anti-sextet, and 15 leakage;
    no direct-contact support, value, or matrix.
```

Verify all actual identities, counts, hashes, dimensions, support classes,
and public operations through the committed C77 package. This prompt is not
numerical authority.

Create a local completion commit. Do not push.

---

# 1. Scientific purpose and stopping point

C78 must construct the exact **support relation** for the normal-ordered
direct instantaneous-fermion contact monomial

\[
b^\dagger a^\dagger a b
\]

in the retained physical \(qg\) sector.

The required source-ordered structure is

\[
|qg\rangle_{\rm ket}
\longrightarrow
|q\rangle_{\rm intermediate}
\longrightarrow
|qg\rangle_{\rm bra},
\]

with the intermediate quark, field ordering, inverse-derivative channel,
color ordering, zero-mode policy, and finite-HO graph-selection ancestry
kept explicit.

C78 must answer:

```text
Which physical qg ket states have source-allowed absorption endpoints?

Which retained q intermediate states can witness those endpoints?

Which physical qg bra states have source-allowed emission endpoints
from the same intermediate?

Which bra/intermediate/ket triples survive exact projection?

Which projected pairs are exact zeros by selection or exact symbolic
cancellation?

Which projected pairs have at least one nonzero independent symbolic
contact-kernel coefficient?
```

C78 must not evaluate:

```text
the contact numerator;
the inverse-partial-plus denominator;
a finite-cell normalization;
the physical coupling;
P-minus or M-squared contact values;
a direct-contact matrix;
a counterterm coefficient;
the complete instantaneous-fermion operator.
```

The strongest positive status is:

```text
C78_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
```

Its exact continuation is:

> **C79/IFCONTACT2 — evaluate the source-derived direct \(b^\dagger a^\dagger a b\) instantaneous-fermion contact matrix on the immutable C78 support, without substituting C53 sequential propagation or C58 self-induced inertia**

---

# 2. Authority policy

Use external primary authority only for genuine imported physics:

```text
the C55 instantaneous-fermion operator and normal-ordering rule;
the physical meaning of the inverse derivative;
the source coefficient and field ordering;
any later physical normalization or renormalization condition.
```

Use exact project-derived authority for:

```text
canonical endpoint and witness IDs;
basis ordering;
support graphs;
symbolic kernel labels;
projection through C77;
exact cancellation of project-owned basis coefficients;
runtime serialization and public APIs.
```

Do not demand an external paper for a repository-specific witness ID,
adjacency ordering, sparse support representation, or canonical path hash.

C57's selected finite-HO graph regulator is an already declared project
regulator with source-supported graph-selection logic. Preserve its status
and limitations. Do not relabel it as BPP DLCQ or a universal field
projector.

---

# 3. Mandatory inputs

Read completely the actual repository equivalents of:

```text
C55:
    source locks;
    instantaneous-fermion operator;
    normal-ordering contract;
    16 field choices / 14 non-vacuum monomials;
    direct b-dagger a-dagger a b contact identity;
    distinction from sequential C53 propagation;
    retained one-pair contraction semantics;

C57:
    operation order;
    CORRESPONDING_PROPAGATING_GRAPH_PROJECT;
    IFREG-CORRESPONDING-PROPAGATING-SUPPORT;
    conditional field-mode support;
    canonical support validation;
    mode ancestry;
    zero-mode and boundary controls;

C58:
    IFNORM2-ORDERED-JOINT-SUPPORT;
    Pi_bra delta Pi_ket ordering;
    q-sector self-induced-inertia result;
    admitted-mode ledger;
    qg counterterm-only scope;
    exact separation from the direct contact;

C59/C60:
    exact missing endpoint/witness requirement;
    prohibited qg_mask.T @ qg_mask shortcut;
    prohibited full-qg-basis substitution;
    prohibited C53-value substitution;
    exact projected-cancellation requirement;

C77:
    authority policy;
    canonical raw, relative/CM, CM-ground, q, qg, and triplet bases;
    physical-to-raw embedding and raw-to-physical projection;
    exact support membership;
    component ancestry;
    public package/API;
    descendant-impact report.
```

Use C53 only as a read-only endpoint-support holdout after C78 construction
objects are frozen. Do not use C53 numerical matrix elements to define the
contact support.

Create:

```text
docs/next_level/c78_derivation_authority_manifest.json
docs/next_level/c78_input_fidelity_audit.json
```

---

# 4. Freeze imported scientific objects

Consume the C77 physical embedding through its authenticated public API.

Freeze:

```text
C77 package/root identity;
all three resolution identities;
physical q basis identities;
physical qg triplet basis identities;
raw qg component identities;
physical-to-raw embedding identities;
raw-to-physical projection identities;
exact support classes;
component expressions and certified bounds;
C55 operator/ordering identity;
C57 regulator/operation-order identity;
C58 ordered-joint-support identity.
```

Issue:

```text
C78_INPUTS_FROZEN_COMPLETE
```

in:

```text
docs/next_level/c78_input_freeze.json
```

After this freeze, do not reopen package-authority sufficiency unless a
named public operation actually fails a hash, identity, or immutability
check.

---

# 5. Independent physical spaces

Construct immutable manifests for the spaces used by the contact support:

```text
physical qg ket basis;
raw qg ket component basis;
retained physical q intermediate basis;
raw qg bra component basis;
physical qg bra basis.
```

Every retained \(q\) intermediate record must expose the exact fields
required by the C55/C57 source chain, including as applicable:

```text
resolution;
longitudinal mode/fraction;
quark helicity;
transverse-HO identity;
fundamental color;
zero-mode status;
boundary identity;
canonical q basis ID.
```

Every qg endpoint record must expose:

```text
physical qg ID;
raw qg component ID;
quark mode;
gluon mode;
quark and gluon helicities;
fundamental and adjoint colors;
transverse and longitudinal identities;
C77 embedding coefficient identity;
exact support status;
certified bound identity.
```

Do not infer missing labels from array position.

Create:

```text
docs/next_level/c78_contact_space_manifest.json
docs/next_level/c78_contact_space_validation.json
```

---

# 6. Source-ordered absorption endpoint relation

Construct the exact structural relation

\[
\mathcal A_R
\subset
\mathcal H_{q,R}
\times
\mathcal H^{\rm phys}_{qg,R},
\]

where \((i,k)\in\mathcal A_R\) means that physical qg ket \(k\) has at
least one exact raw component on which the source-ordered \(a b\) side of
the C55 direct contact reaches retained quark intermediate \(i\).

For every raw absorption path record:

```text
physical ket ID;
raw ket component ID;
annihilated gluon mode;
incoming quark mode;
retained q intermediate ID;
operator-field order;
longitudinal conservation;
helicity selection;
transverse-mode selection;
ordered color action;
zero-mode/boundary status;
C57 graph-selection status;
C77 component ancestry;
symbolic contact-kernel ID.
```

The symbolic kernel ID must distinguish every independent source-defined
kernel coordinate that could carry a distinct contact value in C79.

Do not use C53 values or a numerical threshold.

Create:

```text
docs/next_level/c78_absorption_endpoint_relation.json
docs/next_level/c78_absorption_endpoint_validation.json
```

---

# 7. Source-ordered emission endpoint relation

Construct independently

\[
\mathcal E_R
\subset
\mathcal H^{\rm phys}_{qg,R}
\times
\mathcal H_{q,R},
\]

where \((b,i)\in\mathcal E_R\) means that retained quark intermediate \(i\)
has a source-allowed \(b^\dagger a^\dagger\) endpoint into physical qg bra
\(b\).

Derive this relation from the C55 operator ordering and exact C77
components. Do not merely copy the absorption Boolean relation.

Then validate the expected adjoint/support relation when and only when it
follows from the frozen source contract.

Record:

```text
physical bra ID;
raw bra component ID;
created gluon mode;
outgoing quark mode;
retained q intermediate ID;
operator-field order;
selection identities;
ordered color action;
C57 graph-selection status;
C77 component ancestry;
symbolic contact-kernel ID.
```

Create:

```text
docs/next_level/c78_emission_endpoint_relation.json
docs/next_level/c78_emission_endpoint_validation.json
```

---

# 8. Exact intermediate-witness relation

Construct the source-ordered ternary relation

\[
\mathcal W_R
=
\left\{
(b,i,k):
(b,i)\in\mathcal E_R,\,
(i,k)\in\mathcal A_R
\right\}.
\]

A witness record must retain both raw endpoint paths and one shared retained
quark intermediate identity.

It must also retain:

```text
bra and ket physical IDs;
bra and ket raw-component IDs;
intermediate q ID;
operator ordering;
gluon creation/annihilation identities;
ordered color-generator identity;
longitudinal inverse-derivative channel label;
C57 corresponding-propagating graph identity;
C58 ordered Pi_bra delta Pi_ket ancestry;
independent symbolic kernel ID;
exact endpoint coefficient product.
```

Do not replace this relation by:

```text
qg_mask.T @ qg_mask;
full qg adjacency;
an unordered set intersection;
C53 sequential propagation;
C58 q-sector self-induced inertia.
```

Create:

```text
docs/next_level/c78_intermediate_witness_relation.json
docs/next_level/c78_intermediate_witness_validation.json
```

---

# 9. Symbolic projected-cancellation closure

The existence of a raw witness is not by itself proof that a projected
physical matrix element is structurally nonzero.

For each physical pair \((b,k)\), assemble an exact symbolic coefficient
vector over **independent contact-kernel labels**:

\[
\mathbf c_{bk}
=
\left(c_{bk}^{(\kappa)}\right)_\kappa .
\]

Each coefficient is the exact sum of the relevant C77 bra/ket embedding
coefficients, color factors, source-order signs, and exact projectors for
one kernel label \(\kappa\).

Do not assign numerical values to the contact kernels.

Classify:

```text
ZERO_BY_OPERATOR_MONOMIAL;
ZERO_BY_LONGITUDINAL_SELECTION;
ZERO_BY_HELICITY_SELECTION;
ZERO_BY_TRANSVERSE_SELECTION;
ZERO_BY_COLOR_SELECTION;
ZERO_BY_ZERO_MODE_OR_BOUNDARY_POLICY;
ZERO_BY_NO_RETAINED_Q_INTERMEDIATE;
ZERO_BY_C57_GRAPH_SELECTION;
ZERO_BY_EXACT_PROJECTED_CANCELLATION;
NONZERO_SYMBOLIC_CONTACT_KERNEL_SUPPORT;
UNDECIDABLE_BLOCKING.
```

A pair has nonzero support when at least one exact symbolic coefficient is
nonzero after all exact source-declared relations among kernel labels are
applied.

Do not merge distinct kernel labels merely to manufacture cancellation.
Do not split source-identical labels merely to avoid cancellation.

Create:

```text
docs/next_level/c78_symbolic_contact_support.json
docs/next_level/c78_projected_cancellation_report.json
docs/next_level/c78_exact_contact_support_validation.json
```

A positive gate requires:

```text
UNDECIDABLE_BLOCKING = 0.
```

---

# 10. Low-shell support pilot

Before full-scale support assembly, execute one nontrivial lowest-shell
pilot containing:

```text
one physical qg ket;
one retained q intermediate;
one physical qg bra;
one exact source-allowed witness;
one exact selection-rule zero;
one exact projected-cancellation zero when available;
one nonzero symbolic kernel coefficient;
complete C55/C57/C58/C77 ancestry.
```

Create:

```text
docs/next_level/c78_low_shell_contact_support_pilot.json
```

A failure must be classified at the endpoint, witness, kernel-label, or
projection-cancellation stage—not as a generic authority failure.

---

# 11. Count-once and source-order closure

Report for each resolution:

```text
physical qg ket count;
physical qg bra count;
retained q intermediate count;
raw absorption-path count;
raw emission-path count;
unique absorption edges;
unique emission edges;
unique witness triples;
unique supported physical pairs;
zero pairs by each exact class;
symbolic kernel-label count;
duplicate witness count;
missing ancestry count;
undecidable count.
```

Every witness must have exactly one ancestry:

```text
C55 direct contact
 -> C57 graph-selection rule
 -> C77 physical ket component
 -> retained q intermediate
 -> C77 physical bra component
 -> C78 symbolic kernel label
 -> physical support status.
```

Create:

```text
docs/next_level/c78_contact_support_ancestry_ledger.json
docs/next_level/c78_count_once_report.json
```

---

# 12. C57, C58, and C53 reconciliation

After C78 support objects and hashes are frozen:

## C57

Independently compare endpoint support with the inherited C57 holdouts:

```text
canonical positions:
    312 / 510 / 756;

conditional mode unions:
    1,216 / 2,320 / 3,936;

candidate envelopes:
    2,304 / 4,400 / 7,488.
```

Use the actual committed counts as authority if they differ from this
prompt.

Classify differences as:

```text
IDENTICAL;
BASIS_ID_ADAPTER_ONLY;
EXACT_CERTIFICATE_SUPERSESSION_NO_SUPPORT_CHANGE;
SUPPORT_REBUILD_REQUIRED;
UNRESOLVED.
```

## C58

Verify that C78 does not alter:

```text
IFNORM2-ORDERED-JOINT-SUPPORT;
4,216 / 8,330 / 14,484 admitted modes;
the 6 x 6 six-nonzero q-sector primitive;
the qg counterterm-only scope.
```

The direct contact is a separate operator block.

## C53

Compare endpoint support only as a post-construction holdout. Confirm that
the direct contact remains distinct from a pair of propagated C53 vertices.

Create:

```text
docs/next_level/c78_c57_reconciliation.json
docs/next_level/c78_c58_separation_report.json
docs/next_level/c78_c53_non_substitution_report.json
```

---

# 13. Public support API and runtime package

Use:

```text
src/deuteron_wigner/bridge/ifsupport2/
data/runtime/c78_ifsupport2/
```

or repository-equivalent paths.

Provide immutable public operations equivalent to:

```python
load_iferm_contact_support_package(resolution)

absorption_endpoints(physical_qg_ket_id, resolution)

emission_endpoints(physical_qg_bra_id, resolution)

contact_witnesses(physical_qg_bra_id, physical_qg_ket_id, resolution)

contact_support_status(physical_qg_bra_id, physical_qg_ket_id, resolution)

contact_symbolic_coefficients(
    physical_qg_bra_id,
    physical_qg_ket_id,
    resolution,
)
```

Return exact IDs, source-order ancestry, symbolic kernel labels, exact
coefficients, and support status.

Do not expose a contact numerical value or matrix action.

Create one authenticated C78 runtime index/root as part of this package.
Do not defer package integrity to another package.

Create:

```text
docs/next_level/c78_api_contract.json
docs/next_level/c78_api_validation.json
docs/next_level/c78_runtime_inventory.json
docs/next_level/c78_deterministic_reconstruction_report.json
```

---

# 14. Isolation and negative controls

Prove C78 construction is independent of:

```text
C53 numerical vertex values;
C58 numerical q-sector primitive values;
the historical C57 1e-12 threshold;
historical C47 quadrature residues;
a full-qg-basis adjacency;
qg_mask.T @ qg_mask;
a sequential propagator or energy denominator;
ART25 files.
```

Required failures include:

```text
swapped operator order;
bra/ket union instead of ordered joint support;
wrong retained q intermediate;
wrong color-generator order;
wrong gluon creation/annihilation identity;
zero-mode admission;
threshold-based support;
merged independent kernel labels;
split source-identical kernel labels;
dropped exact cancellation;
duplicate witness;
missing C77 ancestry;
C53-value substitution;
C58-self-energy substitution.
```

Create at least **320 focused live mutations** of actual endpoint, witness,
kernel-label, coefficient, projection, and support records.

Create:

```text
docs/next_level/c78_isolation_report.json
docs/next_level/c78_regression_report.json
```

---

# 15. Readiness and continuation decisions

Select exactly one branch.

## 15.1 Favorable branch

Issue:

```text
C78_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
```

Required:

```text
absorption and emission relations complete;
retained-q intermediate identities complete;
witness relation complete;
symbolic kernel-label basis complete;
projected cancellation complete;
no undecidable pair;
C57 compatible without required support rebuild;
C58 separation preserved;
C53 non-substitution proved.
```

Next:

> **C79/IFCONTACT2 — evaluate the direct instantaneous-fermion contact matrix on the C78 support**

## 15.2 C57/C58 support supersession required

Issue:

```text
C78_IFERM_CONTACT_SUPPORT_READY_IFREG_SUPERSESSION_REQUIRED
```

Next:

> **C79/IFREG4 — rebuild the corresponding-propagating support and self-induced-inertia ancestry from C77/C78 before contact evaluation**

## 15.3 Endpoint mapping incomplete

Issue:

```text
C78_IFSUPPORT_ENDPOINT_RELATION_INCOMPLETE
```

Next:

> **C79/IFENDPOINT — repair the specifically identified absorption/emission endpoint defect**

## 15.4 Intermediate witness incomplete

Issue:

```text
C78_IFSUPPORT_INTERMEDIATE_WITNESS_INCOMPLETE
```

Next:

> **C79/IFWITNESS — repair the specifically identified retained-q or source-order witness defect**

## 15.5 Symbolic cancellation incomplete

Issue:

```text
C78_IFSUPPORT_PROJECTED_CANCELLATION_INCOMPLETE
```

Next:

> **C79/IFCANCEL — complete the exact symbolic kernel module and projected-cancellation classification**

Do not issue a physical-contact-ready, complete-instantaneous-fermion, TMD,
matching, or production status.

---

# 16. Essential deliverables

Create at least:

```text
docs/next_level/c78_implementation_report.md
docs/next_level/c78_derivation_authority_manifest.json
docs/next_level/c78_input_fidelity_audit.json
docs/next_level/c78_input_freeze.json

docs/next_level/c78_contact_space_manifest.json
docs/next_level/c78_contact_space_validation.json
docs/next_level/c78_absorption_endpoint_relation.json
docs/next_level/c78_absorption_endpoint_validation.json
docs/next_level/c78_emission_endpoint_relation.json
docs/next_level/c78_emission_endpoint_validation.json
docs/next_level/c78_intermediate_witness_relation.json
docs/next_level/c78_intermediate_witness_validation.json

docs/next_level/c78_symbolic_contact_support.json
docs/next_level/c78_projected_cancellation_report.json
docs/next_level/c78_exact_contact_support_validation.json
docs/next_level/c78_low_shell_contact_support_pilot.json

docs/next_level/c78_contact_support_ancestry_ledger.json
docs/next_level/c78_count_once_report.json
docs/next_level/c78_c57_reconciliation.json
docs/next_level/c78_c58_separation_report.json
docs/next_level/c78_c53_non_substitution_report.json

docs/next_level/c78_api_contract.json
docs/next_level/c78_api_validation.json
docs/next_level/c78_runtime_inventory.json
docs/next_level/c78_deterministic_reconstruction_report.json
docs/next_level/c78_isolation_report.json
docs/next_level/c78_readiness_report.json
docs/next_level/c78_regression_report.json
```

Create exactly one next-package contract corresponding to the selected
branch.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

Do not add or modify the old untracked C69 prompt.

---

# 17. Acceptance criteria

C78 is complete only when:

1. Baseline `5a117fa29442195a52f67da6fa00368a28a13e8f` reproduces.
2. Both required untracked paths remain untouched.
3. C55/C57/C58/C77 historical artifacts remain unchanged.
4. C77 public embedding package verifies.
5. Inputs are frozen before support construction.
6. Physical qg endpoint and retained q spaces are explicit.
7. Absorption relation is source ordered.
8. Emission relation is independently derived and validated.
9. Every witness has one shared retained q intermediate.
10. No unordered adjacency shortcut is used.
11. Direct contact remains distinct from C53 propagation.
12. Direct contact remains distinct from C58 self-induced inertia.
13. Every independent contact-kernel label is explicit.
14. Exact source-declared kernel relations are enforced.
15. Projected cancellation is performed symbolically.
16. Support uses no numerical threshold.
17. No pair remains undecidable.
18. The low-shell support pilot closes.
19. Count-once and ancestry close.
20. C57 reconciliation is typed.
21. C58 separation is preserved.
22. The immutable support API and runtime package reconstruct deterministically.
23. Isolation and at least 320 focused mutations pass.
24. No contact value, denominator, normalization, matrix, counterterm, complete instantaneous-fermion operator, TMD, matching, fit, inference, or production object is created.
25. `NO_JOINT_MEASURE`, 216 routes, 642 ART25 identities, and authoritative artifacts remain unchanged.
26. The working tree is clean except for the two pre-existing untracked paths.
27. A local completion commit is created and not pushed.

Do not weaken source ordering, exact endpoint identity, retained-intermediate
identity, symbolic kernel separation, projected-cancellation logic, or
threshold-free support to open the gate.

---

# 18. Final Codex response

Report:

- starting and final commits;
- untouched untracked paths;
- C77 package root and imported dimensions;
- C55/C57/C58 identities consumed;
- physical qg and retained q basis dimensions;
- absorption and emission raw-path/edge counts;
- witness-triple counts;
- symbolic kernel-label counts;
- supported physical-pair counts;
- exact-zero counts by class;
- projected-cancellation counts;
- undecidable count;
- low-shell support pilot;
- C57 positions/unions/envelopes and differences;
- C58 separation and unchanged mode/primitive status;
- C53 non-substitution result;
- ancestry and duplicate/missing counts;
- deterministic reconstruction;
- isolation and mutation results;
- exact readiness/no-go/supersession status;
- exact next branch;
- confirmation that no contact value or matrix, complete instantaneous-fermion operator, TMD/matching, fit, inference, or production object was created;
- confirmation that nothing was pushed.
