# C149/HQCDMPROJ implementation report

Status: `C149_C148_SOURCE_DERIVED_SIGNED_MASS_AND_KINETIC_PROJECTOR_AUTHORITY_READY`.

C149 consumes the C148 full-spinor authority read-only. It validates an
explicit caller-supplied off-shell subtraction record and constructs a
contact-safe inverse on the finite C148 source image through direct,
equation-of-motion, and block/constraint routes. Constraint-field contacts,
C112/C127 Hamiltonian terms, composite-source contractions, zero-mode
interfaces, and the unavailable antiquark term remain separately ledgered.

The eight-tensor inventory and rank-eight dual Gram are explicit. Kinetic
and signed- `m_q` projectors have unit signal response and annihilate the
declared nuisance tensors through dual-Gram, analytic, response, and free
holdout routes. Kinetic `A_minus`, `A_plus`, and `A_perp` structures remain
separate; no single `Z_q` coefficient is inferred.

Null-space sensitivity is prospective only: rank 2 with nine unresolved
coordinates. The conditional `Z_q^FB`/`m_R^FB` interface is published with
no subtraction default, physical scale, parameter solution, counterterm, or
preferred representative. The next continuation is `C150/HQCDZQMASS`.
