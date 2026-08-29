# C142/HQCDFIELD implementation report

Baseline: `98007c6a171701ef60382f5f9b2e0b9d5fcb7a15`

Contract: `docs/next_level/c141_c142_hqcdfield_import_contract.json`
Contract SHA-256: `cfbede74feaa1809839ed543d5a4db93b7d57f55e1f9a3a044687d04c82b82b7`

C142 selects **FIELD-A** and closes the permitted forward-quark source
authority with status
`C142_C141_SOURCE_DERIVED_C43_NONZERO_MODE_QUARK_FIELD_SOURCE_MAP_READY`.
The vacuum claim is limited to the C43 nonzero-mode perturbative Fock
reference state; it is not the interacting QCD vacuum and is distinct from
the C33 TMD soft vacuum.

Each resolution has six source modes: longitudinal (K/2), antiperiodic
half-integer boundary, transverse (n=m=0) CM ground, good helicity
(-1,+1), and fundamental colors (0,1,2). The source-to-q map is the
authenticated identity in the C47 q-sector order, with unit source and q
metrics, rank six, zero kernel/cokernel, and exact source span. Route F-A
field insertion and Route F-B canonical Gram reconstruction have zero
mismatches. The sink is the exact adjoint.

The finite-(x^+) anticommutator closes onto the finite-resolution
longitudinal/Fourier and transverse-HO projector kernel, not a continuum
delta. A canonical bare quark field has direct q support; direct qg support
is excluded by field particle content and is reserved for C53/C131
Hamiltonian propagation. All eight residual-color generator intertwiners
have zero residual.

Flavor remains a generic unresolved light-quark source with no invented u/d
copies. The canonical antiquark algebra is documented, but no retained
antiquark Hilbert space or antiquark Hamiltonian block is fabricated.
Zero-mode, boundary, residual-gauge, counterterm, omitted-interface, and
nine-dimensional-nullspace boundaries remain explicit.

No resolvent, propagator, self-energy, mass projector, (Z_q), physical
parameter, legacy capsule, counterterm, state, spectrum, or downstream
object is created. The next object is the forward-quark two-point handoff:
C143/HQCD2PTQ.
