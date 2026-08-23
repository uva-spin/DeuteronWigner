# C175/HQCDB0GHOSTSECTOR1 implementation report

Starting commit: `66081dc2d58954d0e8a03f7caccaa495f03acd70`.

The expected committed contract `docs/next_level/c174_c175_hqcdb0ghostsector1_continuation_contract.json` was absent. No retrospective contract was created; the supplied prompt is the sole C175 authority. The C170, C171, C172, C173, and C174 prompt-only provenance chain is preserved.

This package consumes C174 scalar, vector, FP, boundary, link, global-volume,
open-color, and PV records through the public API. It adds no C166 graph nodes
or edges, does not rebuild C171 B0 or C174 gauge records, and leaves B1,
Q0/Q1/Q2, C158 values, physical inputs, and quantum objects untouched.

The local ghost and antighost domains are independent Grassmann copies of the
C174 scalar P0 modes times adjoint color, with dimensions 288, 440, and 624
per species for K9, K11, and K13. Global SU(3) directions remain outside the
local determinant. The Berezin convention is `bar_c M c`, with antighost
before ghost and ghost numbers +1/-1; no positive norm, probability, state, or
qubit is defined.

The free operator is the immutable C174 reference FP operator, exposed via
sparse and per-color matrix-free actions and a local solve interface. The
field-dependent interaction is the exact C174 projected commutator term
`-g_s P_scalar div_perp([A_perp,omega])`, with the C45-derived adjoint
structure tensor, derivative orientation, finite-shell leakage, and residual
link kept explicit. Target-gauge ghost vertices are not imported.

The coordinate, finite-Fourier, operator-preimage, and source-topology routes
prove exact bulk orthogonality between P0 residual ghosts and the retained C151
/ C171 Q0 B0 source. The endpoint/link route is not zero and remains a
nonmatrix boundary interface. Determinant, trace-log, Berezin, and ordered
Wick-kernel descriptions are provided without evaluating a physical loop or
assembling a self-energy.

Selected plan: `B0GHOSTSECTOR1-H`.

Status: `C175_C174_LOCAL_P0_GHOST_AUTHORITY_READY_RETAINED_Q0_B0_SOURCE_ORTHOGONAL`.

The first remaining object is the explicit residual-link/basis-boundary
operator, so exactly one continuation is selected: `C176/HQCDB0RESLINK1`.
One local completion commit is required; nothing is pushed.
