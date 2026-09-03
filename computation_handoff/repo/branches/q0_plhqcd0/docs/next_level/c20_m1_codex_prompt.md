# C20/M1 Codex Work Package

## Title

**C20/M1 — Source-Audited Perturbative Coefficient Library, Controlled External Matrix-Element Constraints, and Physical-Scheme LF-to-QCD Step-Scaling Pilot**

## Authoritative baseline

Use the completed C19/M0 commit as the scientific and regression baseline:

```text
22a092e7472f113ae018f9ff94373af03c99ce8d
```

A documentation-only descendant is acceptable only if this commit remains in its ancestry and the complete C19 baseline reproduces before any C20 code changes.

Do not use `origin/main` as the authority if it does not contain the local C19 history.

## Required normative sources

Read completely before implementation:

```text
references/volume_v_matching_evolution_factorization.tex
references/volume_xv_delta_delta_six_quark_hidden_color.tex
references/volume_xii_microscopic_wilson_second_order.tex
references/volume_xi_microscopic_nonzero_transfer_gtmds.tex
references/algebraic_geometric_next_level_model_note_revised.tex
references/model_construction_note.tex

docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c19_matching_basis.json
docs/next_level/c19_scheme_manifest.json
docs/next_level/c19_step_scaling_manifest.json
docs/next_level/c19_small_b_ope_manifest.json
docs/next_level/c19_evolution_manifest.json
```

If a named source has moved, locate its indexed replacement and record the exact path and SHA-256 hash. Do not invent absent formalism content. If a primary-source coefficient or external matrix element cannot be obtained in a reproducible form, preserve the corresponding operator entry as explicitly unavailable.

## Primary objective

Replace C19's analytic coefficient and matching oracles, where justified, by a **source-audited perturbative coefficient library** and a **controlled external-matrix-element/step-scaling constraint layer** acting on the existing closed 540-dimensional LF and QCD operator bases.

The package must establish the executable chain

```text
C18 microscopic LF operator matrix elements
    -> C19 complete matching basis and scheme identities
    -> source-audited perturbative coefficient records
    -> controlled local-current / external / lattice matrix-element constraints
    -> shared LF-to-QCD matching map with holdouts
    -> regulator step scaling and covariance
    -> scheme-qualified validation operators at a reference scale
```

C20 remains validation-only. It must not claim a complete physical TMD extraction, all-order evolution, a physical Collins-Soper kernel, process factorization, W+Y, global inference, or production readiness.

## Completeness over quickness

Do not optimize for a short implementation. Continue autonomously until every acceptance criterion is satisfied.

Routine local dependency installation, symbolic-algebra tooling, numerical quadrature tooling, and source retrieval are permitted when the environment allows them. Do not stop merely to ask permission for ordinary non-destructive work. If an external source cannot be fetched, continue with all other requirements and record the exact unavailable source and blocked operator entries.

## Immutable baseline gates

Before modifying code, reproduce and record:

```text
1,029 existing tests
all C19 builders and validators
36/36 evidence rows
162/162 atlas pages
830 C19 requirements
480 C19 ordered negative injections
540 LF matching-basis entries
540 QCD matching-basis entries
492 executable C19 entries
48 explicitly unavailable C19 entries
216 accepted production routes
all eight authoritative production artifacts byte-identical
all pinned C15-C19 manifests byte-identical
```

The 540-entry basis cardinality and stable operator identities are immutable. An entry may change from `UNAVAILABLE` to executable only if C20 supplies a complete source-audited coefficient record, convention conversion, operator/twist proof, tests, and provenance. No executable C19 entry may silently become unavailable.

## Physics that must not be changed

Do not change:

- the C18 microscopic nucleon or deuteron parents;
- any Hamiltonian, Fock-sector amplitude, current, Wilson phase, nuclear sector, or hidden-color basis;
- the accepted phenomenological production model;
- any authoritative numerical parent or correlator;
- C19 coordinate, rank, scheme, link, color, member, or operator identities;
- the distinction among UV renormalization, rapidity renormalization, soft subtraction, finite-scheme conversion, LF-to-QCD matching, and truncation discrepancy;
- the distinction between twist-2 and multiparton twist-3 bases;
- quark versus gluon representations;
- direct positive-x antiquark identity;
- ordered gluon links and independent f/d color classes;
- resolved nuclear-sector ancestry.

Do not introduce:

- one matching normalization per named TMD;
- one transverse width per TMD;
- fitted coefficient functions chosen only to improve a final curve;
- a twist-2 coefficient in a twist-3 channel;
- a quark coefficient copied to a gluon channel;
- a quark Collins-Soper or matching object copied to a gluon object without a proven representation relation at the implemented order;
- a target-polarization-dependent short-distance coefficient unless the operator basis genuinely requires it;
- a physical coefficient inferred only from a plot or secondary review when the primary formula is unavailable;
- silent interpolation across unsupported endpoint, flavor-threshold, rank, link, or scheme regions.

---

# A. Source-audited coefficient library

## A1. Core coefficient record

Implement a versioned object such as:

```text
PerturbativeCoefficientRecord
```

Each record must contain at least:

```text
coefficient_id
source_operator_id
target_operator_id
parton_source
parton_target
flavor_structure
singlet_or_nonsinglet_block
target_channel
parton_polarization
transverse_rank
twist
Wilson_link_class
ordered_gluon_link_pair
f_or_d_color_class
UV_scheme
rapidity_scheme
soft_partition
Fourier_convention
reference_mass_convention
alpha_s_normalization
color_factor_convention
implemented_order
first_nonzero_order
x_or_z_distribution_type
plus_distribution_definition
endpoint_delta_terms
log_mu_structure
log_zeta_structure
threshold_history
source_citation
source_equation_or_table
source_page_or_section
source_file_hash
transcription_hash
independent_oracle
status
known_remainder
```

Allowed statuses must include at least:

```text
AUDITED_IMPLEMENTED
AUDITED_BY_SYMMETRY_IMPLEMENTED
AUDITED_NOT_IMPLEMENTED
PRIMARY_SOURCE_UNAVAILABLE
SCHEME_CONVERSION_UNAVAILABLE
WRONG_TWIST_FOR_REQUEST
UNAVAILABLE_AT_THIS_ORDER
EXPLORATORY_ONLY
```

A coefficient is not executable merely because its function name resembles an implemented channel.

## A2. Primary-source audit discipline

For every implemented coefficient:

1. identify the primary paper or official source;
2. record the exact equation, table, appendix, or repository location;
3. store the local source hash or a stable source manifest;
4. record all conventions required to translate it into the C19 scheme;
5. derive or document the finite convention adapter;
6. implement an independent symbolic or numerical oracle;
7. test endpoint distributions, logarithms, color factors, and moments;
8. record the perturbative and power remainder.

Secondary reviews may aid discovery but cannot be the sole authority for an implemented coefficient when a primary derivation exists.

If a formula must be transcribed manually from a PDF, require two independent checks: one symbolic/analytic and one numerical or moment-level. Store the transcription provenance.

## A3. Initial supported coefficient families

Audit and implement only where primary-source and scheme information is sufficient:

```text
rank-zero unpolarized quark matching
rank-zero unpolarized gluon matching
quark and gluon helicity matching
quark transversity matching
linearly polarized gluon matching
spin-1 LL rank-zero matching where the short-distance operator is identical
nonsinglet quark blocks
singlet quark-gluon mixing blocks
local vector, axial, tensor-if-available, and EMT moment adapters
```

For every family, store the actual implemented order rather than assuming a universal order.

The spin-1 target label may change the hadronic matrix element but not the short-distance coefficient when the same QCD operator is involved. This equivalence must be represented by an explicit operator-level proof or adapter, not by copying data under a new name.

## A4. T-odd and multiparton channels

The following remain unavailable unless C20 obtains and implements the correct audited multiparton coefficient basis:

```text
Sivers / Qiu-Sterman matching
Boer-Mulders chiral-odd twist-three matching
quark-gluon-quark worm-gear genuine terms
tri-gluon f-type matching
tri-gluon d-type matching
T-odd tensor-polarized multiparton matching
```

C20 must build or update the coefficient-status matrix for these channels, preserving their distinct twist-three and color bases. It must not make them executable by substituting a twist-two coefficient.

Physical T-odd coefficients may remain among the 48 unavailable entries. This is acceptable and preferable to a false completion claim.

## A5. Distributional implementation

Implement typed distribution objects for:

```text
delta(1-z)
plus distributions
regular z-dependent terms
endpoint logarithms
convolution kernels
matrix-valued singlet kernels
```

Tests must verify:

- action on constant, polynomial, and analytic benchmark functions;
- plus-distribution subtraction conventions;
- endpoint-integrability;
- Mellin moments;
- convolution associativity within tolerance;
- scheme-adapter covariance;
- no sampling artifact at z=1.

A numerical grid approximation may be used only with an explicit quadrature/distribution manifest and an independent analytic oracle.

---

# B. Coefficient-level renormalization and consistency tests

## B1. Tree and first-nonzero-order limits

Every coefficient family must reproduce its declared tree-level or first-nonzero-order limit. A coefficient that starts beyond tree level must report a structural zero at lower order rather than an absent implementation.

## B2. Renormalization-group consistency

At the implemented perturbative order, test that the coefficient logarithms are compatible with the stored anomalous dimensions and collinear kernels. The package must distinguish:

```text
exact all-order identity
identity through implemented order
known higher-order remainder
finite-order defect
```

A nonzero finite-order defect must remain visible and cannot be removed by fitting a matching parameter.

## B3. Moment and sum-rule checks

Where applicable, verify:

- conserved nonsinglet moments;
- singlet momentum conservation;
- helicity moments at the supported order;
- transversity nonsinglet structure;
- gluon convention `H^g = x g`;
- vector-current quark-minus-antiquark signs;
- axial quark-plus-antiquark signs;
- EMT quark/antiquark/gluon weighting;
- target-polarization independence of the coefficient when dictated by operator identity.

## B4. Scheme covariance

Transform the coefficient library and matched operators between the two C19 declared validation schemes. Round-trip the full operator block, not just one scalar function.

The finite transformation must act consistently on:

```text
coefficient matrices
renormalized operators
soft/rapidity partition
matching map
local moments
accuracy manifest
```

A transformation applied only to TMD values must fail.

---

# C. External and lattice matrix-element constraint layer

## C1. Typed external bundle

Implement a versioned object such as:

```text
ExternalMatrixElementBundle
```

with fields including:

```text
bundle_id
source_type          # lattice, continuum, experiment, synthetic oracle
source_citation
source_hash
observable_or_operator_id
external_state_identity
kinematics
lattice_spacing_or_regulator
volume_or_continuum_status
renormalization_scheme
renormalization_scale
rapidity_scheme_if_relevant
matching_formula
covariance
correlation_group
systematic_components
continuum_extrapolation_status
finite-volume_status
interpolation_status
usage_role           # calibration, diagnostic, holdout
```

No external number may enter the fit without a declared scheme conversion and covariance or explicit covariance-unavailable status.

## C2. Required external-constraint routes

Implement and validate:

1. local-current and EMT constraints already available from the microscopic state;
2. a synthetic exact external-matrix-element oracle for end-to-end testing;
3. at least one controlled imported continuum or lattice-style step-scaling bundle if a reproducible primary-source table or data release is available;
4. a fail-closed path when the external source is not scheme-compatible or lacks required covariance.

Do not claim a physical lattice constraint merely because a synthetic bundle has the same shape.

If no suitable machine-readable external data can be reproduced, complete the ingestion and validation interface, mark the physical bundle unavailable, and retain C20 as an audited infrastructure result.

## C3. External scheme conversion

Any external bundle must be converted into the same operator and scheme basis as the C19 matching map. Store:

```text
source scheme
intermediate scheme if any
target C19 scheme
conversion order
conversion uncertainty
operator-mixing matrix
threshold history
```

A lattice quasi-TMD, pseudo-distribution, TMD wave function, local moment, or Collins-Soper observable cannot be consumed as though it were already the same renormalized TMD operator.

## C4. Covariance and shared constraints

Use the complete covariance when available. Shared systematics across operator channels or resolutions must be represented through common nuisance directions or a joint covariance matrix.

The same external constraint may not be counted once as a local moment and again as an independent matched TMD datum unless the ancestry graph certifies independence.

---

# D. Shared matching fit and step-scaling trajectory

## D1. Shared parameter ownership

Retain the C19 rule that matching parameters belong to operator-mixing channels, regulator counterterms, finite scheme conversions, or low-dimensional discrepancy operators.

No parameter may be owned by a named TMD.

## D2. Overconstrained matching

Use more independent matching conditions than shared parameters. C19 used five parameters, eight conditions, and three holdouts. C20 may refine the parameterization only when the coefficient/source audit demonstrates a need.

For every plan record:

```text
number of parameters
number of independent calibration conditions
Jacobian rank
singular values
null directions
prior or naturalness assumptions
holdout set
condition-number diagnostics
```

A hidden null direction must be reported, not removed by adding a TMD-specific fit parameter.

## D3. Matching plans

At minimum compile mutually exclusive plans such as:

```text
M1-PLAN-PERT
    source-audited perturbative coefficients
    local-current anchoring
    regulator step scaling
    no external lattice bundle

M1-PLAN-EXT
    source-audited perturbative coefficients
    local-current anchoring
    compatible external/lattice matrix-element bundle
    regulator step scaling

M1-PLAN-HYBRID
    source-audited perturbative coefficients
    local-current anchoring
    external bundle where compatible
    low-dimensional shared discrepancy operator
    regulator step scaling
```

The plans may be compared but never summed. The matching route is part of the assumption bundle and may not be selected separately for each observable after inspecting results.

## D4. Step-scaling system

Using the C18/C19 resolution tower, construct

\[
\Sigma_{r'\leftarrow r}
=
Z_{\mathrm{LF}\to\mathrm{QCD}}(r')^{-1}
Z_{\mathrm{LF}\to\mathrm{QCD}}(r).
\]

Test:

\[
\Sigma_{r''\leftarrow r'}
\Sigma_{r'\leftarrow r}
=
\Sigma_{r''\leftarrow r}
+
\delta_{r''r'r}.
\]

Report separately:

```text
perturbative truncation defect
basis/Fock mismatch
missing-operator defect
external-data uncertainty
scheme-conversion uncertainty
numerical defect
shared discrepancy contribution
```

The target of convergence is the matched operator matrix element and its moments, not bare sector probabilities.

## D5. Holdouts

Reserve at least:

- one quark matrix element not used in matching;
- one antiquark matrix element;
- one gluon or singlet matrix element;
- one deuteron tensor or nuclear-sector-resolved matrix element;
- one resolution-level step-scaling link;
- one current or EMT moment;
- one scheme-conversion round trip.

A failed holdout must revise the coefficient transcription, operator basis, scheme conversion, missing-operator model, or shared matching parameterization. It may not receive an observable-specific normalization.

---

# E. Small-b OPE upgrade

## E1. Coefficient registry integration

Replace C19 analytic OPE coefficient oracles with the audited library for every supported operator entry.

Each `SmallBOPE` result must record:

```text
coefficient_record_ids
implemented perturbative order
lowest nonzero order
source and target operator IDs
rank
twist
link/color class
scheme and scales
power remainder
matching-plan identity
external-constraint identity if used
```

## E2. Resolved target and nuclear structure

The short-distance coefficient acts on the partonic operator, while target and nuclear polarization remain in the matrix element. Verify that the same coefficient record consistently serves compatible proton, neutron, and deuteron U/L/T/LL/LT/TT channels.

Pion-active, coherent, transition, DeltaDelta, and compact operators with distinct QCD operator content must retain their own matching status. They cannot inherit the one-body nucleon coefficient merely because their final TMD name matches.

## E3. Hidden-color covariance

Apply the matching map in at least two unitary hidden-color bases. Complete six-quark and matched observables must agree. Individual hidden-color basis components may rotate.

## E4. Rank 0-3 transforms

Retain the C19 rank 0-3 Fourier-Bessel tests and rerun them with the source-audited coefficient blocks. The maximum residual must be reported by rank, not only as one aggregate value.

---

# F. Evolution boundary

C20 may reuse C19's exact and controlled finite-order evolution oracles only as validation transport for the newly matched operators.

C20 must not claim a physical Collins-Soper kernel or all-order evolution.

It must nevertheless verify that the upgraded matching layer preserves:

- exact path independence for the integrable oracle;
- the declared finite-order curl and path defect for the truncated oracle;
- quark/gluon representation separation;
- rank preservation;
- future/past link reversal;
- ordered gluon-link identity;
- f/d color separation;
- heavy-threshold continuity in the validation map;
- microscopic and nuclear member identity.

No matching parameter may be adjusted to cancel the finite-order evolution curl.

---

# G. Required analytic and numerical benchmark families

Implement at least the following benchmark families with stable IDs:

1. source-record completeness and hash audit;
2. tree/first-nonzero-order coefficient limits;
3. plus-distribution action and endpoint normalization;
4. unpolarized quark coefficient and moments;
5. unpolarized gluon and singlet-mixing coefficient block;
6. quark/gluon helicity coefficient block;
7. transversity nonsinglet coefficient block;
8. linearly polarized gluon coefficient block;
9. spin-1 LL operator-coefficient universality test;
10. coefficient RG/log consistency;
11. finite scheme transformation and full block round trip;
12. external-bundle schema, covariance, and ancestry;
13. external scheme-conversion benchmark;
14. overconstrained shared matching with holdouts;
15. three-resolution step-scaling cocycle;
16. missing-operator and discrepancy separation;
17. rank 0-3 transform closure with audited coefficients;
18. resolved nuclear impulse commutation;
19. hidden-color basis covariance;
20. twist-three/T-odd fail-closed status matrix;
21. threshold continuity;
22. exact/truncated evolution transport after matching;
23. deterministic manifest reconstruction;
24. immutable production regression.

---

# H. Mandatory negative injections

Add at least **560 new ordered C20 negative injections** with stable IDs and expected diagnostics.

The injection catalogue must include failures from all of the following families:

## H1. Source provenance

- missing source citation;
- missing equation/table reference;
- changed source hash;
- transcription hash mismatch;
- secondary source used as sole authority when a primary source is required;
- formula copied from a different scheme;
- incorrect alpha_s normalization;
- incorrect color-factor convention;
- unsupported perturbative order claim;
- source record without independent oracle.

## H2. Operator identity

- wrong source or target operator;
- quark coefficient applied to gluon;
- gluon coefficient applied to quark;
- target channel used to disguise a different operator;
- lost rank or reference mass;
- wrong Wilson link;
- lost ordered gluon-link identity;
- f/d color alias;
- direct antiquark copied from quark;
- wrong twist;
- wrong singlet/nonsinglet block.

## H3. Distributional algebra

- missing plus subtraction;
- duplicate plus subtraction;
- wrong endpoint delta term;
- grid sample used as a delta distribution;
- divergent endpoint integral accepted;
- incorrect Mellin moment;
- wrong convolution ordering;
- wrong normalization of matrix-valued kernel.

## H4. Matching parameterization

- one parameter per TMD;
- one width per TMD;
- underconstrained fit;
- hidden Jacobian null direction;
- holdout added to calibration after failure;
- discrepancy operator with no named missing physics;
- matching plan selected per observable;
- perturbative and external plans added together;
- local-current constraint counted twice.

## H5. External constraints

- missing scheme conversion;
- missing covariance;
- incompatible external operator;
- lattice quasi-object treated as a physical TMD;
- finite-volume result treated as continuum without extrapolation;
- same source counted twice through ancestry aliases;
- synthetic oracle labeled physical;
- interpolation outside source support;
- threshold history mismatch.

## H6. Step scaling

- wrong map direction;
- cocycle failure hidden by refitting;
- omitted induced operator;
- regulator level mismatch;
- bare coefficient convergence substituted for observable convergence;
- external bundle mixed across incompatible resolutions;
- matching uncertainty collapsed into numerical error.

## H7. OPE and rank

- scalar J0 transform on rank 1, 2, or 3;
- wrong Bessel phase;
- wrong mass power;
- rank-changing evolution;
- twist-two coefficient used for Sivers or Boer-Mulders;
- one-body coefficient applied to a distinct pion/coherent/compact operator without proof;
- missing power remainder;
- false small-b validity outside its domain.

## H8. Scheme and evolution

- UV/rapidity/soft pieces merged into one unnamed factor;
- missing soft subtraction;
- duplicate soft subtraction;
- unresolved finite coefficient silently set to zero;
- quark CS object copied to gluon;
- finite-order curl canceled by fit;
- link reversal broken after evolution;
- heavy-flavor threshold changed without matching;
- scheme transformed TMD but not coefficient/operator block.

## H9. Nuclear and hidden-color structure

- nuclear sectors collapsed to a scalar response;
- hidden-color basis dependence of a complete observable;
- cluster and compact contributions double counted;
- transition/interference omitted from matching basis;
- proton and neutron microscopic members mixed;
- partonic and nuclear mechanism identities erased.

## H10. Downstream leakage

- physical TMD status issued;
- physical Collins-Soper kernel status issued;
- process factorization executed;
- W+Y executed;
- global inference executed;
- production registry mutation;
- authoritative artifact mutation;
- accepted model silently replaced;
- network publication or push attempted.

---

# I. Required deliverables

Create at least:

```text
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_requirement_coverage.json
docs/next_level/c20_coefficient_library.json
docs/next_level/c20_coefficient_source_audit.json
docs/next_level/c20_external_matrix_element_manifest.json
docs/next_level/c20_matching_plan_manifest.json
docs/next_level/c20_matching_fit_report.json
docs/next_level/c20_step_scaling_manifest.json
docs/next_level/c20_small_b_ope_manifest.json
docs/next_level/c20_scheme_roundtrip_report.json
docs/next_level/c20_holdout_report.json
docs/next_level/c20_uncertainty_ledger.json
docs/next_level/c20_unavailable_operator_matrix.json
docs/next_level/c20_injection_manifest.json
docs/next_level/c20_regression_report.json
docs/next_level/c20_normative_source_integration.json
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

when appropriate.

All JSON outputs must be deterministic, machine-readable, and byte-identical on rebuild.

## I1. Coefficient library report

For each of the 540 basis entries, report:

```text
operator ID
C19 status
C20 status
coefficient records used
implemented order
source audit status
scheme conversion
external constraints
holdout status
power/truncation remainder
reason for unavailability if unavailable
```

## I2. Matching fit report

Report:

```text
shared parameter values and ownership
calibration conditions
holdouts
Jacobian and singular values
null directions
covariance
perturbative and external uncertainty components
maximum calibration residual
maximum holdout residual
plan comparisons
```

## I3. Uncertainty ledger

Separate at minimum:

```text
source transcription uncertainty
perturbative truncation
scheme conversion
external/lattice statistical covariance
external/lattice systematic covariance
finite-volume/continuum extrapolation
step-scaling cocycle defect
missing-operator discrepancy
Hamiltonian/Fock truncation
rank-transform numerical error
evolution transport defect
nuclear matching uncertainty
```

No single aggregate band may replace these ledgers.

---

# J. Acceptance criteria

C20/M1 is complete only when all of the following hold:

1. The exact C19 baseline reproduces before modifications.
2. The 540-entry LF and QCD matching bases remain identity-stable.
3. Every executable perturbative coefficient has complete primary-source provenance and an independent oracle.
4. Every unavailable coefficient remains explicitly unavailable with a precise reason.
5. No named TMD owns a matching normalization or width.
6. Supported quark, antiquark, gluon, helicity, transversity, linear-gluon, LL, and singlet coefficient blocks pass their declared-order tests.
7. T-odd and multiparton channels fail closed unless their correct audited coefficient basis is implemented.
8. Distributional endpoint, plus-prescription, and moment tests pass.
9. External matrix-element bundles preserve scheme, covariance, and ancestry.
10. Shared matching is overconstrained and all null directions are reported.
11. At least three genuine holdout classes are retained and evaluated.
12. Step-scaling cocycles close within declared component-wise residuals.
13. UV, rapidity, soft, finite-scheme, LF-to-QCD, and truncation pieces remain separate.
14. Scheme round trips close for complete operator blocks.
15. Rank 0-3 transforms pass with per-rank residuals.
16. Nonsinglet and singlet moments close at the implemented order.
17. Hidden-color complete observables remain basis invariant.
18. Resolved nuclear sectors remain explicit through matching.
19. C19 exact and truncated evolution transport tests remain intact; finite-order curl remains visible.
20. At least 560 C20 negative injections are detected with stable diagnostics.
21. All existing tests, builders, evidence rows, atlas pages, and prior injections remain passing.
22. The production registry remains exactly 216 routes.
23. All eight authoritative production artifacts remain byte-identical.
24. All pinned C15-C19 manifests remain byte-identical.
25. Every C20 JSON artifact rebuilds byte-for-byte.
26. The working tree is clean after a final local commit.
27. Nothing is pushed or published.
28. The final report states clearly that C20 is not yet physical matching, all-order evolution, process factorization, W+Y, inference, or production.

---

# K. Allowed status boundary

C20 may issue narrowly qualified statuses such as:

```text
PERTURBATIVE_COEFFICIENT_LIBRARY_SOURCE_AUDITED
SUPPORTED_TWIST2_COEFFICIENT_BLOCKS_IMPLEMENTED
EXTERNAL_MATRIX_ELEMENT_INTERFACE_VALIDATED
COMPATIBLE_EXTERNAL_BUNDLE_CONSUMED
SHARED_MATCHING_OVERCONSTRAINED
LF_TO_QCD_STEP_SCALING_WITH_AUDITED_COEFFICIENTS_VALIDATED
SMALL_B_OPE_AUDITED_AT_DECLARED_ORDER
SCHEME_ROUNDTRIP_VALIDATED
MATCHED_REFERENCE_SCALE_OPERATORS_VALIDATION_ONLY
C20_M1_VALIDATION_ONLY
```

It must not issue:

```text
PHYSICAL_TMD_MATCHING_COMPLETE
ALL_TMD_COEFFICIENTS_KNOWN
PHYSICAL_TODD_MATCHING_COMPLETE
PHYSICAL_COLLINS_SOPER_KERNEL
ALL_ORDER_EVOLUTION_READY
PROCESS_FACTORIZATION_READY
W_PLUS_Y_READY
INFERENCE_READY
PRODUCTION_READY
```

---

# L. Final response and next package

At completion, summarize:

- baseline and final commit;
- full regression status;
- coefficient families implemented and their orders;
- primary sources and audit status;
- number of executable/unavailable operator entries before and after C20;
- external or lattice bundles actually consumed;
- matching parameters, conditions, holdouts, null directions, and residuals;
- step-scaling and scheme-roundtrip residuals;
- per-rank transform residuals;
- unresolved coefficient and operator gaps;
- exact next package.

The expected next package, if C20 closes, is:

> **C21/M2 — physical anomalous-dimension and Collins–Soper-kernel library, continuum/lattice-constrained nonperturbative kernel, common multi-Q rank-aware evolution, and threshold-qualified microscopic nucleon/deuteron TMD ensembles.**

Do not push the final commit.
