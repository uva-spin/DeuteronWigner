# C60/IFSUPPORT Codex Work Package

## Title

**Source-ordered retained-\(q\) intermediate support for the direct instantaneous-fermion contact: canonical endpoint incidence maps, physical \(qg\) embeddings, witness-preserving graph selection, Hermitian bra–ket composition, and support-only closure**

## Authoritative baseline

Start from the clean local C59/IFERM2 fail-closed completion commit:

```text
3174722ee1fc2d0045ee10273b4338f335b262b9
```

Its immediate scientific parent is:

```text
43bf2493ec020a130bbf4cb576a851adc5b5e0cf
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 43bf2493ec020a130bbf4cb576a851adc5b5e0cf HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY

C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY

C59_IFERM_CONTACT_SUPPORT_INCOMPLETE
```

and the exact C59 result:

```text
C58 import:
    read-only and verified;

q-sector self-induced-inertia:
    6 x 6 primitive at every physical resolution;
    six nonzero entries;
    admitted modes:
        4,216 / 8,330 / 14,484;

qg self-induced-inertia:
    IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY;
    unchanged;

direct contact source:
    exactly one retained C55 b-dagger a-dagger a b term;

missing object:
    source-ordered
    qg-ket -> retained-q-intermediate -> qg-bra
    embedding required by the TBP corresponding-propagating-graph rule;

explicitly rejected substitutes:
    qg_mask.T @ qg_mask;
    the full physical qg basis;
    C53 numerical values;

not created:
    no direct qg contact;
    no complete instantaneous-fermion operator;
    no downstream local-QCD object.
```

Verify every value, hash, support identity, basis order, and status from the committed C59 and inherited C58/C57 records rather than relying on this prompt.

The fixed architecture remains:

```text
TMD scheme:
    O4-SPACELIKE-COLLINS-JMY

gauge/action:
    G0-LIGHT-FRONT-GAUGE
    A^+ = A_- = 0
    x^+ is light-front time
    antisymmetric/PV inverse partial^+ on Q0
    explicit zero-mode projector
    retained residual transverse gauge link

longitudinal cell:
    -L <= x^- <= L
    p^+ = pi k/L
    P^+ = pi K/L
    L remains symbolic

physical trajectory:
    (K,Nmax,bHO/GeV)
      = (9/2,8,0.40)
      = (11/2,10,0.45)
      = (13/2,12,0.50)

retained physical space:
    H_q
    plus
    H_qg^(3,CM=0)

physical q dimension:
    6 at every resolution, subject to manifest verification

physical qg dimensions:
    1,344 / 2,700 / 4,752,
    subject to exact manifest verification

canonical q <-> qg operator:
    C53 source derived;
    read-only;
    numerical values, singular values, and energy denominators are
    forbidden as C60 construction inputs

direct instantaneous-fermion source:
    C55 exact normal-ordered b-dagger a-dagger a b term
    at order g_s^2

self-induced-inertia:
    C58 read-only q-sector primitive
    and qg highest-sector counterterm-only status
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All historical C47 canonical tuple values and attempted mass/transverse metadata remain diagnostic-only and forbidden as physical or support-construction inputs.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C59 correctly rejected an unlabeled mask product.

A numerical or Boolean expression resembling

\[
M_{\rm qg\to q}^{T} M_{\rm qg\to q}
\]

is not, by itself, the source-ordered contact support. Such a product may erase:

```text
which endpoint is emission and which is absorption;

which retained q state is the intermediate witness;

which C43/C55 operator ordering generated the path;

which raw qg component entered the physical CM-clean state;

which color, helicity, OAM, longitudinal, and zero-mode decisions
made each endpoint legal;

whether two ordered source terms are conjugate or merely combined;

whether a zero is structural, projected, or an accidental numerical
cancellation.
```

C60 may use typed relation composition only **after** independently deriving the endpoint incidence maps and retaining every intermediate witness and source-order label.

The central object is not a fitted contact mask. It is a source-owned relation:

\[
\mathfrak S_R
\subset
\mathcal B_{qg,R}^{\rm bra}
\times
\mathcal B_{q,R}^{\rm int}
\times
\mathcal B_{qg,R}^{\rm ket}
\times
\mathcal O_{\rm contact},
\]

where \(\mathcal O_{\rm contact}\) labels the exact ordered C55 source term or its source-required Hermitian partner.

Only after this witnessed relation closes may C61 evaluate a contact kernel.

---

# 2. Exact purpose

C60 resolves only the support and embedding obstruction exposed by C59.

C60 must create:

```text
the exact direct-contact source topology and ordered endpoint roles;

the retained intermediate-q basis and its source meaning;

the raw product-qg basis required at each endpoint;

the exact embedding of physical CM-clean triplet qg states into the
raw product basis;

a source-derived canonical absorption incidence relation
    qg_ket -> q_int;

a separately derived canonical emission incidence relation
    q_int -> qg_bra;

a proof or exact failure of their source-adjoint relation;

a witness-preserving ordered composition for every direct-contact
bra/ket pair;

a typed distinction among structural reachability, exact projected
endpoint support, and accidental evaluated zeros;

the TBP graph-selection decision at the direct-contact topology;

Hermitian-conjugation, count-once, CM, triplet, zero-mode,
basis-rotation, and resolution-comparison diagnostics;

an immutable C61/IFCONTACT import contract.
```

C60 must not evaluate:

```text
the direct-contact spinor numerator;

the direct-contact inverse-partial-plus denominator;

the direct-contact finite-cell normalization;

the direct-contact P-minus or M-squared value;

a direct-contact sparse matrix;

a complete instantaneous-fermion operator;

a counterterm coefficient;

a propagating self-energy.
```

The strongest allowed status is:

```text
C60_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
```

When that gate passes, the exact next package is:

> **C61/IFCONTACT — evaluate the source-derived direct \(qg\to qg\) instantaneous-fermion contact on the immutable C60 witnessed support, then assemble the complete operator with read-only C58**

---

# 3. Scientific boundary

C60 is:

```text
support-only;
graph-selection specific;
source ordered;
fixed-K and finite-HO specific;
physical qg embedding aware;
CM and color-triplet aware;
witness preserving;
coefficient free;
deterministic;
validation only.
```

C60 is not:

```text
a contact-amplitude calculation;

a support inferred from matrix magnitudes;

a product of anonymous masks;

a use of the full qg basis by default;

a use of C53 numerical nonzeros as construction authority;

a second-order propagating calculation;

a physical renormalization calculation.
```

A support record may be nonempty even when a later exact contact matrix element vanishes through the source kernel. Conversely, a structurally possible raw path may disappear after exact physical-basis projection. C60 must keep these layers distinct.

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_boundary_prescription_decision.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_qg_triplet_basis_manifest.json
docs/next_level/c47_physical_basis_validation.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c50_plane_wave_operator_derivation.json
docs/next_level/c50_operator_ordering_report.json
docs/next_level/c50_arbitrary_mode_vertex_evaluator.json

docs/next_level/c52_component_domain_ledger.json
docs/next_level/c52_colorless_component_matrices.json
docs/next_level/c52_numerical_object_inventory.json

docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_count_once_report.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c55_instantaneous_fermion_operator_contract.json
docs/next_level/c55_normal_ordering_contract.json
docs/next_level/c55_operator_monomial_ledger.json
docs/next_level/c55_physical_block_classification.json
docs/next_level/c55_contact_propagating_count_once.json

docs/next_level/c57_operation_order_contract.json
docs/next_level/c57_regulator_plan_decision.json
docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_conditional_mode_support.json
docs/next_level/c57_fock_space_projector.json
docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_canonical_support_validation.json
docs/next_level/c57_mode_ancestry_ledger.json
docs/next_level/c57_numerical_object_inventory.json
docs/next_level/c57_readiness_report.json

docs/next_level/c58_bra_ket_support_contract.json
docs/next_level/c58_pair_support_decision.json
docs/next_level/c58_hermiticity_support_report.json
docs/next_level/c58_local_self_energy_count_once.json
docs/next_level/c58_c59_import_contract.json
docs/next_level/c58_readiness_report.json

docs/next_level/c59_implementation_report.md
docs/next_level/c59_input_fidelity_audit.json
docs/next_level/c59_direct_contact_source_ledger.json
docs/next_level/c59_direct_contact_component_contract.json
docs/next_level/c59_missing_calculation_specification.md
docs/next_level/c59_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c60_derivation_authority_manifest.json
docs/next_level/c60_input_fidelity_audit.json
```

---

# 5. Source hierarchy and exact scope of TBP graph selection

Reuse the source locks and role decisions from C57.

Audit the exact Tang–Brodsky–Pauli and later source statements for the direct-contact topology:

```text
what is meant by the corresponding propagating graph;

whether support is defined at the operator-monomial, raw Fock-state,
projected basis-state, or evaluated-amplitude level;

whether both endpoint canonical attachments are required;

whether ordered Hermitian partner terms carry separate support;

whether a graph excluded by truncation is removed from the bare
instantaneous operator or represented through a sector counterterm;

whether the rule refers to the intermediate state before or after
CM and color projection.
```

Do not extend a statement about self-induced inertia automatically to the direct contact without an explicit topology audit.

Classify source statements as:

```text
DIRECT_CONTACT_GRAPH_SELECTION_AUTHORITY;

CANONICAL_ENDPOINT_SELECTION_AUTHORITY;

FINITE_BASIS_PROJECTOR_AUTHORITY;

NORMAL_ORDERING_AUTHORITY;

METHOD_COMPARISON_ONLY;

NOT_CONTACT_SUPPORT_IDENTICAL.
```

Create:

```text
docs/next_level/c60_source_role_matrix.json
docs/next_level/c60_graph_selection_source_audit.json
```

---

# 6. Freeze construction and holdouts

Before building an incidence edge, freeze:

```text
the exact C55 retained b-dagger a-dagger a b source term;

its ordered gluon annihilation and creation roles;

its Hermitian partner identity, when separately present;

the C43 canonical q <-> qg endpoint operator;

the C45 mode, Fourier, helicity, polarization, and color phases;

the C47 raw product, intrinsic/CM, CM-ground, and triplet basis orders;

the C57 corresponding-propagating operation order;

the C57 fixed-K conditional-regulator identity;

the C58 ordered-joint-support logic as an analogy only;

the exact zero-mode and boundary policy.
```

Freeze holdouts before construction:

```text
one qg ket with exactly one retained q witness;

one qg ket with multiple retained q witnesses;

one qg ket with raw product paths but no physical projected endpoint;

one qg ket excluded by K or Jz;

one qg ket excluded by CM projection;

one qg ket excluded by triplet projection;

one qg ket containing an exact zero-mode candidate;

one qg bra/ket pair with one common q witness;

one pair with multiple common witnesses;

one pair with no common witness;

one ordered source term and its Hermitian partner;

one pair for which an anonymous-mask product would lose source order;

one C53-support holdout per resolution;

one adjacent-resolution support-comparison holdout.
```

No failed holdout may be moved into construction after inspection.

Create:

```text
docs/next_level/c60_calculation_plan.json
docs/next_level/c60_holdout_plan.json
```

---

# 7. Distinguish four support layers

C60 must implement four noninterchangeable support layers.

## 7.1 Raw monomial path support

A source-owned canonical endpoint monomial can connect a raw product \(qg\) state to a raw \(q\) state before physical projection.

Status:

```text
RAW_PATH_ALLOWED;
RAW_PATH_EXACT_ZERO;
RAW_PATH_OUTSIDE_RETAINED_SPACE;
RAW_PATH_BLOCKING.
```

## 7.2 Physical-basis component support

A physical \(qg\) basis state has nonzero exact embedding coefficient on one or more raw product states participating in a raw path.

This is not yet a canonical endpoint amplitude.

## 7.3 Exact projected endpoint support

After summing all source-owned raw contributions and applying the physical embedding, the canonical endpoint map is structurally or symbolically nonzero.

This layer must distinguish:

```text
NONZERO_BY_EXACT_SOURCE_EXPRESSION;

ZERO_BY_SELECTION_RULE;

ZERO_BY_EXACT_PROJECTED_CANCELLATION;

NUMERICALLY_UNDECIDABLE_BLOCKING.
```

A floating value below a tolerance is not an exact zero.

## 7.4 Evaluated matrix-value support

This is the nonzero pattern of an evaluated C53 matrix. It is a holdout only and is not a C60 construction input.

Create:

```text
docs/next_level/c60_support_layer_contract.json
docs/next_level/c60_exact_zero_semantics.json
```

Select and record which support layer the TBP direct-contact rule requires.

---

# 8. Retained intermediate-\(q\) basis

Construct the exact retained intermediate-\(q\) basis:

\[
\mathcal B_{q,R}^{\rm int}.
\]

Do not assume it is identical to the external physical \(q\) basis merely because the dimensions agree.

Audit:

```text
total K;

longitudinal mode;

transverse HO mode;

quark helicity;

fundamental color;

Jz;

zero-mode status;

CM convention;

normalization;

source role as an intermediate state.
```

Allowed decisions:

```text
INTERMEDIATE_Q_EQUALS_PHYSICAL_Q_WITH_PROOF;

INTERMEDIATE_Q_IS_A_PROPER_SUBSPACE;

INTERMEDIATE_Q_REQUIRES_A_DISTINCT_EMBEDDING;

INTERMEDIATE_Q_BASIS_INCOMPLETE.
```

Construct explicit maps between any raw, canonical, and physical \(q\) basis representations.

Create:

```text
docs/next_level/c60_intermediate_q_basis_manifest.json
docs/next_level/c60_intermediate_q_basis_validation.json
```

---

# 9. Raw and physical \(qg\) endpoint spaces

Construct and distinguish:

```text
raw single-particle q tensor g product basis;

fixed-K many-body qg basis;

x-scaled intrinsic/CM qg basis;

CM-ground qg basis;

full 3 tensor 8 product-color qg basis;

retained total-color-triplet qg basis;

canonically reachable qg endpoint subspace.
```

Create explicit typed maps:

\[
J_{qg,R}^{\rm phys\to raw},
\qquad
P_{qg,R}^{\rm raw\to phys},
\]

or the exact nonorthogonal/generalized-metric equivalents.

Required checks:

```text
basis order;

Gram metric;

adjoint relation;

normalization;

rank and nullity;

K and Jz bookkeeping;

CM-ground identity;

triplet identity;

basis-rotation covariance;

no silent removal of raw components.
```

Do not use a physical qg row index as though it were a one-gluon field mode.

Create:

```text
docs/next_level/c60_qg_endpoint_space_manifest.json
docs/next_level/c60_physical_qg_embedding_contract.json
docs/next_level/c60_physical_qg_embedding_validation.json
```

---

# 10. Source-derived absorption endpoint relation

Derive the canonical absorption endpoint:

\[
qg_{\rm ket}
\longrightarrow
q_{\rm int}.
\]

Begin from the exact source canonical operator and its annihilation ordering. Do not obtain absorption by transposing a C53 mask.

For every source path retain:

```text
physical qg ket ID;

raw qg component ID;

intermediate q ID;

canonical source-term ID;

annihilated gluon mode;

incoming and intermediate longitudinal modes;

quark and gluon helicities;

OAM and transverse labels;

ordered color action;

CM and triplet ancestry;

zero-mode status;

exact support status.
```

Construct an immutable typed incidence relation:

\[
\mathfrak A_R
\subset
\mathcal B_{q,R}^{\rm int}
\times
\mathcal B_{qg,R}^{\rm ket}
\times
\mathcal O_{\rm abs}.
\]

A sparse Boolean representation is permitted only as a serialization of the full witnessed records.

Create:

```text
docs/next_level/c60_absorption_endpoint_relation.json
docs/next_level/c60_absorption_endpoint_validation.json
```

---

# 11. Source-derived emission endpoint relation

Independently derive:

\[
q_{\rm int}
\longrightarrow
qg_{\rm bra}.
\]

Do not define emission by transposing the absorption incidence relation unless the source-adjoint derivation first proves that equality.

For every source path retain the corresponding emission identities and exact support status.

Construct:

\[
\mathfrak E_R
\subset
\mathcal B_{qg,R}^{\rm bra}
\times
\mathcal B_{q,R}^{\rm int}
\times
\mathcal O_{\rm em}.
\]

Required checks:

```text
source operator ordering;

basis and phase convention;

K and Jz conservation;

raw/physical embedding;

CM and triplet preservation;

zero-mode policy;

color covariance;

structural-zero classification.
```

Create:

```text
docs/next_level/c60_emission_endpoint_relation.json
docs/next_level/c60_emission_endpoint_validation.json
```

---

# 12. Endpoint source-adjoint relation

Derive the exact relation between \(\mathfrak A_R\) and \(\mathfrak E_R\).

Allowed outcomes:

```text
EMISSION_IS_SOURCE_ADJOINT_OF_ABSORPTION;

ORDERED_ENDPOINTS_FORM_A_CONJUGATE_PAIR;

ENDPOINT_SUPPORTS_DIFFER_BY_DECLARED_BOUNDARY_OR_ZERO_MODE_TERM;

ENDPOINT_ADJOINT_RELATION_INCOMPLETE.
```

The proof must retain:

```text
source-term conjugation;

phase reversal;

color-generator adjoint;

helicity/polarization conjugation;

basis-map adjoint;

CM and triplet phase;

zero-mode and boundary status.
```

Do not repair a mismatch by replacing either incidence map with the union or intersection of both.

Create:

```text
docs/next_level/c60_endpoint_adjoint_contract.json
docs/next_level/c60_endpoint_adjoint_validation.json
```

---

# 13. Ordered contact topology and intermediate witnesses

Read the exact C55 direct-contact source term.

For each ordered term \(o\), define the witnessed support:

\[
\mathfrak S_R^{(o)}
=
\left\{
(\beta,i,\alpha,o):
(\beta,i,o_{\rm em})\in\mathfrak E_R,\;
(i,\alpha,o_{\rm abs})\in\mathfrak A_R,\;
(o_{\rm em},o_{\rm abs})\text{ match }o
\right\}.
\]

Here:

```text
alpha:
    physical qg ket ID;

beta:
    physical qg bra ID;

i:
    retained q-intermediate ID;

o:
    exact ordered direct-contact source term.
```

Do not existentially eliminate \(i\) before provenance and count-once closure.

Multiple intermediate \(q\) witnesses for one qg bra–ket pair are distinct source paths, not duplicates.

Create:

```text
docs/next_level/c60_contact_witness_relation.json
docs/next_level/c60_intermediate_witness_ledger.json
```

---

# 14. Direct-contact support plans

Compile mutually exclusive plans after the endpoint maps exist.

## 14.1 `IFSUPPORT-SOURCE-ORDERED-WITNESS-RELATION`

The direct contact is supported precisely by the exact ordered endpoint relation with retained intermediate-\(q\) witnesses.

## 14.2 `IFSUPPORT-COMMON-RETAINED-Q-RELATION`

The source audit proves that only existence of a common retained \(q\) witness matters and that ordered endpoint distinctions collapse without loss.

This may be selected only with an explicit equivalence proof.

## 14.3 `IFSUPPORT-FULL-SOURCE-ALLOWED-QG-BLOCK`

The TBP rule does not constrain this direct contact at the declared scope.

This requires a source-level exemption.

## 14.4 `IFSUPPORT-UNAVAILABLE`

No unique support follows from the source and basis chain.

Do not select a plan by:

```text
matrix density;

expected Hermiticity;

agreement with C53 numerical support;

smoothness across resolutions;

or ease of implementation.
```

Create:

```text
docs/next_level/c60_contact_support_plan.json
docs/next_level/c60_contact_support_decision.json
```

---

# 15. Bra–ket support relation

After selecting the plan, derive the physical bra–ket support relation:

\[
\mathcal S_R(\beta,\alpha).
\]

Retain:

```text
all intermediate witnesses;

all ordered source terms;

all exact endpoint statuses;

all CM and triplet ancestry;

all zero-mode and boundary decisions.
```

Allowed pair statuses:

```text
SUPPORTED_WITH_ONE_WITNESS;

SUPPORTED_WITH_MULTIPLE_WITNESSES;

EXACTLY_FORBIDDEN_BY_ENDPOINT_SELECTION;

EXACTLY_FORBIDDEN_BY_NO_COMMON_INTERMEDIATE;

EXACTLY_FORBIDDEN_BY_SOURCE_ORDER;

EXACTLY_FORBIDDEN_BY_CM_OR_TRIPLET_PROJECTION;

EXACTLY_FORBIDDEN_BY_ZERO_MODE_POLICY;

SUPPORT_UNAVAILABLE_BLOCKING.
```

Construct both:

```text
a full witnessed relation;

a derived Boolean qg-bra/qg-ket adjacency for C61 preselection.
```

The Boolean adjacency is not the authority; it is a lossier export of the witnessed relation.

Create:

```text
docs/next_level/c60_bra_ket_support_contract.json
docs/next_level/c60_bra_ket_support_manifest.json
```

---

# 16. Boolean relation composition versus linear operator algebra

Create an explicit audit comparing:

```text
typed existential composition of source-owned endpoint relations;

Boolean multiplication of fully labeled incidence matrices;

ordinary integer matrix multiplication;

a Gram matrix of endpoint amplitudes;

qg_mask.T @ qg_mask;

a linear orthogonal projector onto a canonical image.
```

These are not generally the same object.

If a Boolean incidence product reproduces the witnessed support after all labels and ordering are retained, record that as a derived representation—not as the source derivation.

Prohibit:

```text
using multiplicity as an amplitude;

using a support relation as a Hamiltonian matrix;

calling a relation adjacency an orthogonal projector;

discarding witness multiplicity before count once;

using a linear Gram matrix to define graph selection.
```

Create:

```text
docs/next_level/c60_boolean_linear_support_audit.json
docs/next_level/c60_forbidden_mask_product_control.json
```

---

# 17. Hermitian support closure

The direct-contact support must obey the conjugation implied by the source Hamiltonian.

For every witnessed path:

\[
(\beta,i,\alpha,o)
\longleftrightarrow
(\alpha,i',\beta,o^\dagger)
\]

with the exact source-defined intermediate and ordering relation.

Do not require \(i'=i\) unless proved.

Report:

```text
pair-support conjugation residual;

witness-multiplicity conjugation;

ordered-term conjugation;

CM/triplet phase covariance;

zero-mode/boundary conjugation;

unsupported asymmetric pairs.
```

Do not symmetrize the adjacency after construction.

Create:

```text
docs/next_level/c60_support_hermiticity_contract.json
docs/next_level/c60_support_hermiticity_report.json
```

---

# 18. C57 and C58 relation

Audit how the new contact endpoint maps relate to the earlier conditional regulator.

C57 constructed incoming-\(q\)-indexed \(q\to qg\) corresponding-propagating support for the self-induced-inertia contraction.

C60 must determine whether:

```text
the C57 emission support is exactly one C60 endpoint relation;

the C57 relation requires an adapter in basis or operation order;

the C57 relation is only a holdout;

or the two topologies require distinct support objects.
```

Do not reuse the C58 ordered-joint-support rule merely because both calculations require bra–ket support. C58's contraction topology and C60's direct-contact topology are distinct.

Create:

```text
docs/next_level/c60_c57_endpoint_relation_audit.json
docs/next_level/c60_c58_topology_separation_report.json
```

---

# 19. C53 support holdout

After the C60 endpoint relations are complete, compare their derived canonical endpoint support with C53.

Use only:

```text
C53 basis IDs;

entry ancestry;

exact nonzero/support classification;

hashes and counts.
```

Poison or make inaccessible:

```text
C53 numerical matrix values;

norms;

singular values;

symbolic coefficient evaluations;

energy denominators.
```

Report:

```text
C60 emission-edge count;

C60 absorption-edge count;

C53 holdout edge count;

symmetric difference;

ordering-adapter difference;

exact-zero classification difference.
```

A disagreement must be explained or block readiness. C53 agreement may validate C60 but cannot define it.

Create:

```text
docs/next_level/c60_c53_support_holdout.json
```

---

# 20. Color, CM, and triplet support checks

Support construction must preserve the exact representation chain.

For every endpoint and witnessed path verify:

```text
raw SU(3) action exists;

full-product color path lies in the source-required image;

triplet projection has nonzero exact support;

no anti-sextet or 15 component is silently relabeled triplet;

CM-ground projection is explicit;

CM-excited raw paths remain outside the physical support;

basis-rotation covariance holds.
```

Do not use a nonzero color norm as an amplitude.

Create:

```text
docs/next_level/c60_color_support_validation.json
docs/next_level/c60_cm_triplet_support_validation.json
```

---

# 21. Longitudinal, helicity, OAM, and zero-mode support

For every endpoint edge and contact witness retain:

```text
total K;

quark and gluon longitudinal modes;

quark and gluon helicities;

total Jz;

single-particle and intrinsic OAM;

HO shell;

Q0/P0 status;

exact gluon-zero-mode status;

residual-boundary status.
```

Support may be rejected only by an exact source-owned rule.

Do not use a future inverse-\(\partial^+\) numerical denominator to define support in C60. Record only whether the mode routing is defined and whether an exact excluded zero mode is already known.

Create:

```text
docs/next_level/c60_quantum_number_support_report.json
docs/next_level/c60_zero_mode_boundary_support.json
```

---

# 22. Exhaustive support-domain ledger

Enumerate every physical qg bra–ket pair at every resolution.

Every pair receives exactly one terminal support status.

Report:

```text
Cartesian qg pair count;

pairs rejected before endpoint construction;

pairs with no absorption edge;

pairs with no emission edge;

pairs with no compatible intermediate witness;

pairs with one witness;

pairs with multiple witnesses;

pairs excluded by source ordering;

pairs excluded by CM/triplet projection;

pairs excluded by zero-mode policy;

blocking pairs.
```

Also report:

```text
raw endpoint path count;

physical absorption-edge count;

physical emission-edge count;

witness count;

unique supported pair count;

duplicate witness records;

missing ancestry records.
```

A positive gate requires:

```text
duplicate witness records = 0;

missing ancestry records = 0;

blocking pairs = 0.
```

Create:

```text
docs/next_level/c60_support_domain_ledger.json
docs/next_level/c60_support_count_once_report.json
```

---

# 23. Support-only runtime API

Create APIs equivalent to:

```python
absorption_support(
    qg_ket_id,
    resolution,
) -> tuple[EndpointSupportRecord, ...]

emission_support(
    q_intermediate_id,
    resolution,
) -> tuple[EndpointSupportRecord, ...]

contact_witnesses(
    qg_bra_id,
    qg_ket_id,
    resolution,
) -> tuple[ContactWitnessRecord, ...]

contact_pair_supported(
    qg_bra_id,
    qg_ket_id,
    resolution,
) -> ContactPairSupportDecision
```

The APIs must return no physical matrix element.

They may return:

```text
exact Boolean decisions;

source-order IDs;

intermediate witness IDs;

basis/path ancestry;

exact-zero reasons;

support hashes.
```

Create:

```text
docs/next_level/c60_api_contract.json
docs/next_level/c60_api_validation.json
```

---

# 24. Physical-resolution comparison

Use the C47/C57 comparison maps to compare endpoint and pair-support relations across adjacent resolutions.

Because the spaces are nonnested, compare typed images and pullbacks rather than claiming literal subset inclusion.

Separate:

```text
longitudinal nonnesting;

HO-shell change;

bHO scale change;

raw-to-physical embedding change;

CM projection change;

triplet-basis change;

canonical reachability change;

zero-mode/boundary change;

numerical support-classification error.
```

Do not tune support rules to maximize overlap.

Create:

```text
docs/next_level/c60_support_comparison_maps.json
docs/next_level/c60_support_comparison_report.json
docs/next_level/c60_comparison_remainder_ledger.json
```

---

# 25. Isolation and poisoning controls

Prove that C60 is unchanged when:

```text
all C40 arrays are poisoned;

all historical C47 canonical tuple values and component metadata
are poisoned;

all C50 combined values are poisoned;

all C52 primitive matrix values are poisoned;

all C53 physical matrix values, norms, and singular values are poisoned;

all C58 contraction matrix values are poisoned;

ART25 files are inaccessible.
```

The build must fail when:

```text
the C55 direct-contact source term changes;

the C43 canonical endpoint ordering changes;

the C45 mode or phase hash changes;

the C47 raw-to-physical qg embedding changes;

the C57 operation-order or regulator-plan ID changes where consumed;

the intermediate-q basis changes;

the triplet isometry changes;

the zero-mode policy changes;

an endpoint relation loses source ancestry;

the support plan changes without supersession;

a witnessed relation is replaced by an anonymous mask product.
```

Create:

```text
docs/next_level/c60_isolation_report.json
```

---

# 26. C61/IFCONTACT import contract

Define the immutable contract by which C61 will consume:

```text
the selected support-plan ID;

the exact direct-contact source-order IDs;

the intermediate-q basis manifest;

the physical qg embedding maps;

the absorption endpoint relation;

the emission endpoint relation;

the endpoint-adjoint contract;

the full witnessed contact relation;

the derived qg bra–ket Boolean preselection;

the exact-zero and unsupported-pair semantics;

the color/CM/triplet and zero-mode support statuses;

the support comparison maps;

the count-once and provenance ledgers;

the API and runtime hashes.
```

C61 must verify every hash before evaluating one contact numerator or denominator.

C61 may not:

```text
change support after observing contact values;

add the full qg basis;

replace witnesses with qg_mask.T @ qg_mask;

use C53 values;

or drop intermediate-witness ancestry.
```

Create:

```text
docs/next_level/c60_c61_import_contract.json
```

---

# 27. Deterministic runtime bundles

For every resolution produce content-addressed bundles containing:

```text
intermediate-q basis records;

raw and physical qg endpoint-basis maps;

raw monomial path ledgers;

absorption endpoint relation;

emission endpoint relation;

endpoint-adjoint records;

witnessed contact relation;

derived Boolean pair adjacency;

support-domain ledger;

holdout and comparison records.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c60_ifsupport/
```

Commit an inventory containing:

```text
runtime path;

object type;

shape or record count;

dtype;

relation semantics;

support-plan ID;

source-order ID;

basis-order hash;

embedding hash;

relation hash;

generator command.
```

Create:

```text
docs/next_level/c60_numerical_object_inventory.json
```

All JSON and arrays must regenerate byte-for-byte.

---

# 28. End-to-end source-to-support test

Implement an end-to-end test that begins from the C43/C45/C47/C55/C57 contracts—not from prebuilt C60 relations.

It must:

```text
load the direct-contact source topology;

construct the intermediate-q basis;

construct raw and physical qg endpoint spaces;

derive raw absorption paths;

derive raw emission paths;

project both endpoint relations into the physical basis;

derive their source-adjoint relation;

compose ordered intermediate witnesses;

select the support plan;

derive the physical pair adjacency;

run Hermitian-support, CM, triplet, zero-mode, holdout,
count-once, poisoning, and comparison tests;

reproduce every hash.
```

It must fail when:

```text
qg_mask.T @ qg_mask is used as authority;

the full qg basis is selected without source proof;

a C53 numerical value enters;

an endpoint relation is defined as the transpose of the other without
the source-adjoint proof;

raw and physical qg states are conflated;

a conditional relation is labeled universal;

an intermediate witness is discarded before count once;

multiple witnesses are treated as duplicate amplitudes;

a numerical tolerance creates an exact zero;

an asymmetric pair is repaired by support union or matrix symmetrization;

a CM-excited or nontriplet path is silently retained;

a zero mode is silently deleted;

a runtime hash changes.
```

---

# 29. Focused mutation tests

Create at least **256 focused live mutations** of actual source-order, basis, embedding, endpoint, witness, or pair-support objects.

Include mutations of:

```text
direct-contact source-term ID;

emission/absorption endpoint role;

intermediate-q basis state;

qg raw component;

physical qg embedding coefficient support;

K;

Jz;

quark helicity;

gluon helicity;

OAM label;

HO shell;

color action;

triplet map;

CM projector;

zero-mode status;

boundary status;

endpoint exact-zero reason;

source-adjoint partner;

intermediate witness;

ordered-term compatibility;

pair-support status;

witness multiplicity;

anonymous-mask substitution;

C53-value dependency;

comparison map;

relation hash;

runtime-array hash.
```

Every mutation must fail a concrete source, basis, representation, support, conjugation, count-once, isolation, comparison, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 30. Readiness gate

Issue:

```text
C60_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
```

only when:

```text
the full C59 baseline reproduces;

the C59 no-go remains explicit;

the C58 self-induced-inertia package remains read-only;

the TBP direct-contact source scope is audited;

the required support layer is selected;

the retained intermediate-q basis is complete;

raw and physical qg endpoint spaces are distinguished;

the physical qg embedding is explicit;

the absorption endpoint relation is source derived;

the emission endpoint relation is independently source derived;

their source-adjoint relation closes or has a complete typed status;

the ordered direct-contact topology is explicit;

every support path retains an intermediate-q witness;

one source-derived support plan is selected;

the physical bra–ket support relation is complete;

no arbitrary union, intersection, full-basis substitution, or
anonymous mask product is used;

Hermitian support follows from source ordering without post-hoc repair;

C57/C58 topology relations are explicit;

the C53 support holdout closes without consuming C53 values;

CM, triplet, color, quantum-number, zero-mode, and boundary support
checks pass;

the exhaustive support domain has no duplicate, missing, or blocking
required record;

support-only APIs return no matrix values;

comparison maps execute with separated remainders;

poisoning controls pass;

the C61 import contract is complete;

runtime bundles reproduce byte-for-byte;

the end-to-end source-to-support test passes.
```

Do not issue:

```text
C60_DIRECT_IFERM_CONTACT_READY;

C60_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C60_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;

C60_PHYSICAL_MASS_RENORMALIZATION_SOLVED;

C60_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 31. Exact no-go branches

## A. Direct-contact graph-selection source scope remains incomplete

```text
C60_IFSUPPORT_SOURCE_RULE_INCOMPLETE
```

Next:

> **C61/IFRULE2 — exact TBP direct-contact topology and graph-selection-source closure**

## B. Intermediate-\(q\) basis or representation remains incomplete

```text
C60_IFSUPPORT_INTERMEDIATE_Q_BASIS_INCOMPLETE
```

Next:

> **C61/IFQSPACE — retained intermediate-quark basis, normalization, and physical embedding completion**

## C. Physical \(qg\) endpoint embedding remains incomplete

```text
C60_IFSUPPORT_QG_EMBEDDING_INCOMPLETE
```

Next:

> **C61/IFQGEMBED — raw product, intrinsic/CM, CM-ground, and triplet endpoint-map completion**

## D. Canonical endpoint incidence maps remain incomplete

```text
C60_IFSUPPORT_ENDPOINT_RELATIONS_INCOMPLETE
```

Next:

> **C61/IFENDPOINT — source-derived emission/absorption support and endpoint-adjoint completion**

## E. Ordered intermediate-witness composition remains incomplete

```text
C60_IFSUPPORT_WITNESS_COMPOSITION_INCOMPLETE
```

Next:

> **C61/IFWITNESS — source-order compatibility, intermediate witness, and bra–ket relation completion**

## F. Source-Hermitian support cannot be established

```text
C60_IFSUPPORT_HERMITICITY_INCOMPLETE
```

Next:

> **C61/IFHERM2 — conjugate endpoint ordering and Hermitian pair-support completion**

## G. Contact support closes

```text
C60_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
```

Next:

> **C61/IFCONTACT — direct-contact kernel and physical-matrix execution**

---

# 32. Required deliverables

Create at least:

```text
docs/next_level/c60_implementation_report.md
docs/next_level/c60_api.md
docs/next_level/c60_derivation_authority_manifest.json
docs/next_level/c60_input_fidelity_audit.json

docs/next_level/c60_source_role_matrix.json
docs/next_level/c60_graph_selection_source_audit.json
docs/next_level/c60_calculation_plan.json
docs/next_level/c60_holdout_plan.json

docs/next_level/c60_support_layer_contract.json
docs/next_level/c60_exact_zero_semantics.json

docs/next_level/c60_intermediate_q_basis_manifest.json
docs/next_level/c60_intermediate_q_basis_validation.json

docs/next_level/c60_qg_endpoint_space_manifest.json
docs/next_level/c60_physical_qg_embedding_contract.json
docs/next_level/c60_physical_qg_embedding_validation.json

docs/next_level/c60_absorption_endpoint_relation.json
docs/next_level/c60_absorption_endpoint_validation.json
docs/next_level/c60_emission_endpoint_relation.json
docs/next_level/c60_emission_endpoint_validation.json
docs/next_level/c60_endpoint_adjoint_contract.json
docs/next_level/c60_endpoint_adjoint_validation.json

docs/next_level/c60_contact_witness_relation.json
docs/next_level/c60_intermediate_witness_ledger.json
docs/next_level/c60_contact_support_plan.json
docs/next_level/c60_contact_support_decision.json
docs/next_level/c60_bra_ket_support_contract.json
docs/next_level/c60_bra_ket_support_manifest.json

docs/next_level/c60_boolean_linear_support_audit.json
docs/next_level/c60_forbidden_mask_product_control.json
docs/next_level/c60_support_hermiticity_contract.json
docs/next_level/c60_support_hermiticity_report.json

docs/next_level/c60_c57_endpoint_relation_audit.json
docs/next_level/c60_c58_topology_separation_report.json
docs/next_level/c60_c53_support_holdout.json

docs/next_level/c60_color_support_validation.json
docs/next_level/c60_cm_triplet_support_validation.json
docs/next_level/c60_quantum_number_support_report.json
docs/next_level/c60_zero_mode_boundary_support.json

docs/next_level/c60_support_domain_ledger.json
docs/next_level/c60_support_count_once_report.json
docs/next_level/c60_api_contract.json
docs/next_level/c60_api_validation.json

docs/next_level/c60_support_comparison_maps.json
docs/next_level/c60_support_comparison_report.json
docs/next_level/c60_comparison_remainder_ledger.json

docs/next_level/c60_isolation_report.json
docs/next_level/c60_c61_import_contract.json

docs/next_level/c60_numerical_object_inventory.json
docs/next_level/c60_readiness_report.json
docs/next_level/c60_source_sufficiency_decision.json
docs/next_level/c60_no_go_decision_tree.json
docs/next_level/c60_missing_calculation_specification.md
docs/next_level/c60_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/ifsupport/
```

or the repository-equivalent package.

Add focused tests for:

```text
source-role and topology audit;
support layers and exact-zero semantics;
intermediate-q basis;
raw/physical qg embeddings;
absorption endpoint support;
emission endpoint support;
source-adjoint relation;
ordered witness composition;
bra–ket support;
Boolean-versus-linear support;
Hermitian support;
C57/C58 topology separation;
C53 holdout isolation;
CM/triplet/color/zero-mode support;
domain count once;
support-only API;
comparison maps;
poisoning controls;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON and runtime arrays must reproduce byte-for-byte.

---

# 33. Acceptance criteria

C60 is complete only when:

1. The full C59 baseline reproduces.
2. The C59 fail-closed status remains explicit.
3. The C58 q-sector primitive and qg counterterm-only status remain immutable.
4. The C53 physical canonical vertex remains read-only.
5. The C43 action, C45 modes, and C47 physical bases remain unchanged.
6. C40 remains method-oracle only.
7. Historical C47 tuple values and metadata remain diagnostic-only.
8. No C50/C52/C53 numerical value defines support.
9. No physical coupling, subtraction, or counterterm coefficient is chosen.
10. No direct-contact matrix element is evaluated.
11. The TBP rule is audited at the direct-contact topology.
12. Source, field, Fock, endpoint, and evaluated support layers remain distinct.
13. Exact zeros are not created by floating tolerances.
14. The intermediate-q basis has a complete source status.
15. The raw qg product basis is explicit.
16. The physical CM-clean triplet qg embedding is explicit.
17. Raw and physical qg states are never conflated.
18. The absorption endpoint relation is independently derived.
19. The emission endpoint relation is independently derived.
20. Neither relation is defined from an anonymous transpose.
21. The endpoint source-adjoint relation is proved or explicitly blocking.
22. Every endpoint edge has complete source and basis ancestry.
23. Every direct-contact support record retains an intermediate-q witness.
24. Multiple witnesses are not treated as duplicate amplitudes.
25. One support plan is selected before contact evaluation.
26. No arbitrary support union or intersection is used.
27. The full qg basis is not used without source exemption.
28. `qg_mask.T @ qg_mask` is a negative control, not authority.
29. Boolean relation composition is typed and provenance preserving.
30. Relation adjacency is not called a Hamiltonian or orthogonal projector.
31. Hermitian support follows from source ordering.
32. Support is not symmetrized post hoc.
33. C57 and C58 topologies remain distinct.
34. C53 support is used only as a poisoned-value holdout.
35. The C53 support holdout closes or has a source-resolved discrepancy.
36. CM-ground identity is preserved.
37. The total-color-triplet identity is preserved.
38. No nontriplet path is silently retained.
39. K, Jz, helicity, OAM, and shell rules are exact.
40. Zero-mode and boundary statuses remain visible.
41. Every qg bra–ket pair receives one terminal support status.
42. Duplicate, missing, and blocking required support records are zero.
43. Support-only APIs return no physical coefficient.
44. Comparison maps retain longitudinal, HO, scale, CM, triplet, and zero-mode remainders.
45. Static and runtime poisoning controls pass.
46. The C61 import contract is complete.
47. Runtime bundles contain actual endpoint, witness, and pair relations.
48. End-to-end source-to-support reconstruction passes.
49. At least 256 focused live mutations are detected.
50. No direct contact, complete instantaneous-fermion operator, free/current/local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
51. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
52. `MSHT20_REP/` remains untouched and outside Git.
53. The working tree is clean except for the pre-existing untracked directory.
54. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken source ordering, intermediate-witness provenance, raw-to-physical embedding, endpoint-adjoint closure, exact-zero semantics, or C53-value independence to open the gate.

---

# 34. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C55/C57/C59 inputs consumed;
- source-role and direct-contact topology decisions;
- selected support layer and exact-zero semantics;
- intermediate-q basis dimension, labels, and relation to the physical q basis;
- raw, intrinsic/CM, CM-ground, product-color, triplet, and reachable qg dimensions;
- physical qg embedding shapes, ranks, nullities, and residuals;
- absorption endpoint path and edge counts;
- emission endpoint path and edge counts;
- endpoint source-adjoint residuals and statuses;
- ordered direct-contact source-term identities;
- intermediate-witness counts and multiplicity distributions;
- selected support plan and rejected alternatives;
- supported, forbidden, multiple-witness, zero-mode, CM, triplet, missing, duplicate, and blocking pair counts;
- Boolean-versus-linear support audit results;
- forbidden `qg_mask.T @ qg_mask` negative-control result;
- support-Hermiticity residuals;
- C57/C58 topology-relation decisions;
- C53 poisoned-value support-holdout counts and symmetric differences;
- K, Jz, helicity, OAM, shell, color, CM, triplet, zero-mode, and boundary support checks;
- adjacent-resolution comparison residuals and separated remainders;
- isolation and poisoning results;
- runtime relation and embedding hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no direct-contact kernel/value/matrix, complete instantaneous-fermion operator, free/current/local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an anonymous mask product, a full-basis default, a relation without intermediate witnesses, a C53 nonzero pattern used as construction authority, a numerically thresholded zero, or a post-hoc symmetrized adjacency as the source-derived direct-contact support.
