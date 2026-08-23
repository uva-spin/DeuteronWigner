# C174/HQCDB0RESGAUGE2 implementation report

Status: `C174_C173_PROJECT_FINITE_CELL_P0_SUBGAUGE_READY_EXPLICIT_GHOST_SECTOR_REQUIRED`

Plan: `B0RESGAUGE2-B`
Next: `C175/HQCDB0GHOSTSECTOR1`

C174 starts from `dde187bc92e75ea54199bb79b54f170829992afb`. The expected
committed C173-to-C174 contract is absent, so no retrospective contract was
invented. Prompt-only provenance for C170, C171, C172, and C173 is preserved.
The unrelated pre-existing `handoff/ROADMAP.md` modification was preserved.

C173's arXiv Eq. (52) source record and its infinite-line/periodic-cell
nonidentity remain unchanged. C174 acquired no source and did not retry the
invalid endpoint substitution.

The scalar residual parameter domain is independent of the physical gluon
polarization space. For K9, K11, and K13 it has 36, 55, and 78 local Cartesian
finite-shell modes respectively, generated from the authenticated C45 spatial
HO span. Global SU(3) is an eight-dimensional algebraic kernel outside the
normalizable HO domain. The role-qualified P0 vector configuration view has
two Cartesian components per scalar mode and is distinct from the C151
physical one-gluon source space.

The finite-HO gradient uses the exact recurrence
`d_i = b_HO/sqrt(2) (a_i - a_i^dagger)`. Circular-ladder recombination and the
Cartesian/generating-function recurrence agree exactly. The divergence is the
negative adjoint, with independent integration-by-parts and finite-quadrature
holdouts. Gradient/divergence ranks are 36, 55, and 78 in each resolution;
the local scalar kernel and cokernel are zero, while the vector kernel has
dimension 36, 55, and 78. Raising-shell leakage is explicitly nonzero and is
never threshold-pruned.

Candidates were compiled before selection. The selected project-owned orbit
functional is `ORBIT_MINIMUM_FUNCTIONAL`, named
`PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1`. Its first variation gives the
projected transverse-divergence constraint and its second variation gives the
finite free Hessian plus the non-Abelian field-dependent commutator term. It
is not called the continuum PV, MOMq, RI/SMOM, or Landau gauge.

The P0 FP operator is derived through direct variation, the finite
scalar/vector matrix Jacobian, and the orbit Hessian. Its reference operator
has full local rank per color, with the eight global SU(3) directions kept
outside the local matrix. The full non-Abelian operator is
`FIELD_DEPENDENT_LOCAL_FP`; no numerical ghost loop or determinant evaluation
was performed. The exact next package is therefore the explicit P0
ghost/antighost sector.

The local determinant, global SU(3) volume, stabilizer, finite-shell boundary,
large/Gribov sectors, and open-adjoint color are separate. The external
adjoint coordinate is retained and no singlet projection or adjoint-dimension
division is made. Q0 projectors, FP authority, determinant scope, and the
antisymmetric/PV inverse are unchanged. The residual link remains explicit
and is not set to unity; its project-scheme endpoint operator remains a
boundary-interface capsule.

P0 Gauss/color covariance is checked structurally for g, q-qbar adjoint,
gg-d, and gg-f with all eight generators, while C171 sources, projectors,
free operators, resolvents, and structural interaction owners are read-only.
Unavailable interaction coefficients remain unavailable, not zero. Count-once
records keep Q0, P0, global volume, future ghosts, constraints,
instantaneous/direct/normal-ordering terms, finite-shell leakage, link terms,
and target ghosts separate. BRST and full Slavnov--Taylor closure remain
unproved; six counterterm directions and nine null coordinates remain
unselected.

No C158 value, private builder, physical input, running, threshold, matching
window, complete self-energy, qg vertex, coupling, standard adapter, quantum
object, state, TMD, or production object was created. C166 graphs, C171 B0
objects, preserved B1 sectors, and all C164-C173 records remain unchanged.
