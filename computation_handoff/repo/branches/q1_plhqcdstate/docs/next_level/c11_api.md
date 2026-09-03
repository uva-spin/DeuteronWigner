# C11/H4 API

H4 lives in `deuteron_wigner.microscopic.h4`. It is a regulated,
zero-skewness, zeroth-Wilson-order validation layer. It does not export a
physical QCD GTMD or TMD.

## Plans and states

`compile_h4_plan` accepts only the two immutable H3 plans. `plans()` returns
H4-PLAN-A and H4-PLAN-B, which remain mutually exclusive. `H4Plan` carries
the H3 parent, correlated state bundle, resolution, recoil, grid,
quadrature, projector, path, and replacement-scope identities.

`MicroscopicMomentumFiber` decorates the established C3 `MomentumFiber`
with target, helicity, H3 member, resolution, skewness, and basis embedding.
It rejects mismatched members and representations. `MicroscopicRecoilMap`
delegates exclusively to `SymmetricXiZeroRecoil` and invokes its physical
assignment check.

## Amplitudes and parent matrices

`MicroscopicWaveFunctionEvaluator` evaluates the finite H3 coefficient
vector in the declared longitudinal/transverse mode representation and
returns value, transfer derivatives, representation, interpolation error,
and quadrature error. Exact vector and full-bond TTN use the same evaluator;
finite-bond truncation remains visible.

`MicroscopicActivePartonSelector` enforces sector support. The sole
`MicroscopicOverlapKernel` creates `GTMDHelicityMatrix` objects for `u`, `d`,
`ubar`, `dbar`, and `g`, for correlated proton and neutron members. Each
matrix retains all target/active helicity entries and has shape 4x4.
`common_parent_bundle()` returns the ten required parent matrices.

## Projectors and reductions

`QuarkGTMDProjectorBasis` and `AntiquarkGTMDProjectorBasis` label the four
F, four G, and eight H amplitudes. `GluonGTMDProjectorBasis` labels trace,
circular/helicity, and linear/symmetric-traceless sectors. All bases are
generated from normalized tensor products and their Gram matrices. Generic
rank is 16. Degenerate kinematics select an explicit rank-8 basis; no
pseudoinverse is used.

`MicroscopicReductionMap` supplies direct-forward and sequential regulated
routes from the same parent ID. `t_odd_coefficients()` returns exact zeros at
Wilson order zero.

## Diagnostics

`projector_report`, `symmetry_report`, `positivity_report`,
`current_emt_report`, `wigner_oam_report`, and `convergence_report` are the
machine-readable closure families. `replacement_manifest` confines C3/C4
replacement to the H4 validation root. `capability_snapshot` lists every
issued and prohibited readiness state.
