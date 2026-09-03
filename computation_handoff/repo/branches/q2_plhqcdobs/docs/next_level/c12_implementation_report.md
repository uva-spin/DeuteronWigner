# C12/H5 implementation report

## Result and declared scope

C12 attaches the established C5/C6 path, pole, cut, ordered-link, color, and
soft-overlap machinery to the C11/H4 microscopic helicity-matrix parent. The
result is restricted to xi=0, Wilson order one, and a regulated finite basis.
It is not a physical or matched TMD, an all-orders Wilson calculation, an
evolved object, a nuclear result, or a process prediction.

The pre-edit baseline reproduced 893 tests, ten builders/validators, 36
evidence rows, 162 atlas pages, 285 C11 requirements, 104 C11 injections,
the 216-route registry, and all eight authoritative artifacts.

## Spectral and cut dynamics

The analytic continuum rule has threshold 1.15 in the declared validation
energy units. Its oriented imaginary part is generated directly from the
distributional identity and reverses sign between future and past paths. It
is exactly zero below threshold. Numerical epsilon is never stored or used
as physical support.

A five-level discretized-continuum sequence from 16 through 256 levels
converges monotonically; the final cut residual is 5.51201e-6. The C5 cut
ledger records the eikonal and LF-resolvent descriptions as
`EQUIVALENT_COUNT_ONCE`; a separate support channel remains additive. The
ledger closes exactly and rejects an unqualified duplicate.

## Matrix-level Wilson action

Every result consumes the complete H4 4x4 parent and retains target, species,
flavor, H3/H4 plan, state member, kinematics, recoil, solver, path, cut, and
Fock-support identities. Future and past signs derive from the stored C5
path/Fourier/coupling/momentum-flow tuple. The antiunitary adapter maps the
past operator into the common transfer frame before link-even/link-odd
decomposition.

Quark and direct positive-x antiquark link-odd matrices precede scalar
projection. Sivers and Boer-Mulders use different target/active-spin and OAM
commutator kernels; they are neither aliased nor made proportional. Coupling,
cut-support, OAM-interference, and future/past-average zero limits close.
Flavor, proton/neutron, sea, and PLAN-A/PLAN-B differences enter through the
shared H4 state rather than independent fitted phases.

Antiquarks retain anti-fundamental identity and are not copied from quarks.
Because explicit `qqqq-qbar-g` sectors are absent, their first-order channel
is classified `INDUCED_OPERATOR_SUPPORTED_WITH_REMAINDER`, with remainders
0.018 for ubar and 0.021 for dbar.

## Active gluons and soft overlap

All ordered adjoint-link pairs `[+,+]`, `[+,-]`, `[-,+]`, and `[-,-]` remain
distinct. One H4 gluon matrix supplies independent f-type and d-type color
channels and trace, circular/helicity, and linear/symmetric-traceless views:
24 typed rows in total. The SU(3) diagnostics give `f.f=24`, `d.d=40/3`, and
`f.d=0`. Both H3 gluon color outer multiplicities remain recorded. There is
no f+d default or process color weight.

The absent explicit qqqgg intermediate sector makes the gluon Wilson route
an induced operator with remainder 0.026. It is not declared microscopically
complete or all-orders ready.

At first order, one half-soft subtraction makes the rapidity derivative
exactly zero. Missing subtraction gives `(0.7,-0.1)` and duplicate
subtraction gives `(-0.7,0.1)`. UV finite matching, physical TMD scheme,
continuum soft completion, Collins-Soper evolution, and process factors stay
unresolved.

## Convergence, replacement, and readiness

Sixteen convergence axes are reported separately. Exact and full-bond TTN
link-odd norms agree exactly. Reduced bonds retain only 46% and 73% of the
OAM-sensitive Wilson amplitude, so their observable failure remains visible
even if an energy diagnostic is comparatively stable.

C5/C6 remain immutable algebraic and sign oracles. Replacement activates
only within `C12_H5_VALIDATION_ONLY` and cannot reach production. C12 adds
124 stable negative injections and 294 stable requirements.

Issued statuses explicitly qualify induced antiquark and gluon channels
with nonzero remainders. Physical TMD, matched GTMD, all-orders Wilson,
complete gauge closure, nuclear matching, LF-to-QCD matching, evolution,
process, inference, and production statuses remain forbidden.

## Reproduction

```bash
PYTHONPATH=src python scripts/build_c12_manifests.py 910
PYTHONPATH=src python scripts/validate_c12_architecture.py
PYTHONPATH=src python -m pytest -q
```
