# C40/M0B executable finite-basis operator substrate

C40 supersedes no historical code.  It preserves the C39 correction that
classifies C38 as `C38_PARTONIC_STRUCTURAL_SCAFFOLD_ONLY`, and supplies a
separate executable `m0b` package for the fixed `O4-SPACELIKE-COLLINS-JMY`
color-fundamental matching probe.

The package deterministically generates three finite resolutions, `(K,Nq,Nqg)
= (17,4,8), (23,6,12), (31,8,16)`.  Each contains complex coordinate vectors,
positive Gram matrices, free assembled Hamiltonians and independent stencil
actions, canonical color/helicity q-to-qg emission and its generated adjoint,
five applied constrained-sector operators, direct finite-path quadrature for
the spacelike Wilson emission, a ten-element counterterm basis and numerical
coefficient system, distributional measurement matrices, and coordinate
refinement maps.  Runtime arrays are regenerated as deterministic `.npy`
bundles into ignored `data/runtime/c40_m0b/`; their hashes and schemas are
committed in the inventory.

The counterterm RHS and solution are explicitly synthetic machinery checks,
not a physical bare one-loop result.  No one-loop correlator, matching kernel,
proton TMD, ART25 bridge, fit, likelihood, inference object, or production
route is created.

The end-to-end gate evaluates actual complex-vector applications and fails for
metadata, scalars, empty arrays, or zero required matrices.  Its companion
fault suite applies 96 focused mutations to numerical objects.  The exact
outcome is `C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY`.
