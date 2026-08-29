# C30/B1 implementation report

## Scientific result

C30 closes the **definition and capability audit** for the requested rank-zero
proton `u`, `d`, `ubar`, and `dbar` distribution bridge. It does not close a
numerical cross-root bridge. The external ART25 distribution is executable and
source-audited, but no source-qualified finite conversion from the selected
microscopic operator to the ART25 TMD scheme exists in the repository or the
integrated formalism. Consequently all twelve frozen comparison points are
`BRIDGE_COMMON_DOMAIN_ONLY`; none is
`BRIDGE_DISTRIBUTION_COMPARISON_READY`.

This fail-closed result prevents a regulated Wilson-order-zero microscopic
parent from being mislabeled as a renormalized, soft-subtracted, rapidity-
qualified ART25 TMD. No identity adapter, zero discrepancy, or numerical
residual was invented.

## Exact external definition

The ART25 side is the proton unpolarized quark TMDPDF returned by
`harpy.get_uTMDPDF(x,b,1,mu,zeta,includeGluon=False)`. It is `f`, not `x f`.
The Python vector order is

`(bbar,cbar,sbar,ubar,dbar,gluon,d,u,s,c,b)`,

so the audited indices are `u=7`, `d=6`, `ubar=3`, and `dbar=4`. C30 selects
explicit `mu=Q` and `zeta=Q^2`. The evolved object is formed from the optimal
OPE/FNP distribution and the rapidity-evolution factor. The rank-zero inverse
Fourier convention is `integral b db J0(kT b)/(2 pi)`. These statements and
their source locators are machine-readable in the ART25 definition, flavor,
and scale manifests.

## Selected microscopic and bridge plans

The microscopic plan is frozen as
`C11_PRIMARY_WITH_LATER_LEVELS_AS_CONVERGENCE_AXES`. C11 supplies the primary
same-operator parent; later C12--C14 levels are separate convergence and
physics axes, not additive values or silent replacements. The bridge plan is
`B1-SCHEME-ART25`: ART25 is held fixed and the microscopic object would be
converted into that scheme.

The adapter records its perturbative order, direction, regulator, UV,
rapidity, soft, threshold, domain, inverse, round-trip, RG, rapidity, and
remainder requirements. Its status is `SOURCE_EXPRESSION_UNAVAILABLE`, its
remainder is `NONZERO_UNKNOWN`, and execution fails closed. This is the only
scientifically defensible status supported by the current sources.

## Common domain and covariance

The twelve C29 rank-zero proton distribution points—three each for `u`, `d`,
`ubar`, and `dbar`—were retained without changing their frozen roles. Their
kinematic intersection is nonempty, but their executable definition
intersection is empty. The external ensemble retains all 642 ordered member
identities and is represented on the unavailable bridge coordinates by an
array of shape `642 x 0`. This is an empty projection, not a zero physical
distribution. No covariance direction is removed, regularized, or paired to a
microscopic assumption member.

## Convergence and uncertainty

Fifteen microscopic convergence axes are recorded, including spatial and
momentum resolution, Fock content, Wilson order, solver residuals, Fourier
quadrature, and tensor-network bond dimension. No TMD convergence sequence is
claimed executable because no scheme-qualified microscopic TMD vector exists.
In particular, energy convergence is explicitly forbidden as a proxy for TMD
convergence, and TTN bond dimension is a deterministic truncation coordinate,
not a statistical replica.

Thirteen discrepancy classes remain separate. Two have source-auditable
information; eleven are nonzero-unknown. Missing matching, scheme conversion,
evolution, Wilson content, nuclear structure, numerical convergence, or
large-b information is never absorbed into ART25 covariance.

## Validation and isolation

The implementation supplies frozen typed records, deterministic builders,
machine-readable capability and discrepancy manifests, 1,600 requirement
rows, and 1,520 ordered injected-failure controls. The controls cover scheme,
scale, flavor, rank, link, color, target, provenance, member pairing,
double-counting, zero-unknown discrepancy, energy-proxy, and status-promotion
failures. C30 creates no fit, likelihood, posterior, optimizer, reweighting,
emulator, process execution, or production route. The production registry
remains 216 routes and all eight authoritative artifacts remain unchanged.

## Reproduction

```bash
PYTHONPATH=src python3 scripts/build_c30_manifests.py 1149
PYTHONPATH=src python3 scripts/validate_c30.py
PYTHONPATH=src python3 -m pytest -q
```

Runtime-only empty-coordinate storage is reconstructed at
`data/runtime/c30_bridge/c30_empty_distribution_bridge.npz`.

## Exact next scientific requirement

A later work package must provide a cited, operator-identical microscopic TMD
renormalization and soft/rapidity subtraction calculation plus a finite,
order-qualified conversion to the ART25 convention. It must then export
converged u, d, ubar, and dbar distributions at the frozen points and quantify
the adapter remainder. Until those inputs exist, numerical cross-root
residuals, calibration, and inference remain unavailable.
