# C7/H0 API

All public objects are under `deuteron_wigner.microscopic.h0`.

| API | Responsibility |
|---|---|
| `OscillatorScale`, `HamiltonianScale`, `EndpointRegulator` | Non-interchangeable scale and regulator identities |
| `HamiltonianResolution` | Exact \(K,N_{\max}\), boundary conditions, scales, regulator, stable ID |
| `reference_resolution()` | Reproducible finite benchmark resolution |
| `lf_invariant_mass_squared()` | Convention check for \(2p^+p^- -p_T^2\) |
| `PartonBasisState` | Exact species, flavor, color representation, mode, HO, helicity, charge |
| `FockSectorSpec`, `ManyBodyBasisState`, `PhysicalFockBasis` | Typed sectors, exact gates, and retained finite basis |
| `reference_basis()` | Proton/neutron \(J^z=\pm\tfrac12\) H0 benchmark basis |
| `ColorSingletBasis` | Complete SU(3) invariant nullspace, recoupling, residuals |
| `emitted_gluon_color_amplitudes()` | Explicit \(t^a\) action projected on both \(qqqg\) singlets |
| `PermutationBasis` | Signed regular representation and fermion antisymmetrizer |
| `CenterOfMassPolicy` | CM factorization, Lawson spectra, intrinsic drift |
| `HamiltonianTerm` | Typed term contract with sector, scale, provenance, approximation metadata |
| `FreeInvariantMassTerm` | H-A matrix-free/assembled free invariant-mass operator and quadrature oracle |
| `ReducedCanonicalVertexTerm` | H-B emission term and generated adjoint absorption |
| `H0Readiness` | Explicit validated/unavailable capability ceiling |
| `require_isolation()`, `provenance_graph()` | Downstream reachability gate and H0 provenance |

Example:

```python
from deuteron_wigner.microscopic.h0 import (
    FreeInvariantMassTerm, reference_basis, reference_resolution
)

resolution = reference_resolution(N_max=8, b=0.4)
basis = reference_basis(resolution, "qqq")
matrix = FreeInvariantMassTerm.for_sector("qqq").assemble(basis)
```

The example returns a validation matrix only. It must not be interpreted as a
physical proton Hamiltonian or be connected to production TMD roots.
