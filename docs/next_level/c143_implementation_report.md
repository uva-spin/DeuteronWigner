# C143/HQCD2PTQ implementation report

Status: `C143_HQCD2PTQ_PARAMETERIZED_OPERATOR_INCOMPLETE`

The frozen C142 authority is consumed only through its public source-field
surface.  The selected plan is `2PTQ-D`: a parameterized operator/resolvent
boundary with no caller-supplied diagnostic parameter record.  No numerical
mass, coupling, counterterm, null-space representative, PDG value, or
physical width is present, so Routes A (direct sparse), B (retained block
identity), and C (public matrix-free) are fail-closed and have zero calls.

The structural source embedding is complete for the q-followed-by-qg direct
sum: `(1350,6)`, `(2706,6)`, and `(4758,6)` with an identity q block and zero
direct qg rows.  This is not a propagator, self-energy, mass projector, or
`Z_q`.  The nine C136 null coordinates remain unresolved and none is set to
zero.  The C142 perturbative reference vacuum, generic flavor scope,
canonical antiquark algebra, zero-mode/boundary scope, and residual-color
intertwiner are preserved.

The public parameter schema requires all bare inputs, six counterterm IDs,
and nine null coordinates, each explicitly caller supplied with claim tier
`NONPHYSICAL_RESOLVENT_DIAGNOSTIC_POINT`, units, scope, provenance, and
`no_default=true`; no defaults or numerical records are generated here.
`z` is an analytic complex GeV² query coordinate, never a physical width.

Continuation: `C144/HQCDOPAPI`, for the immutable operator/resolvent API
boundary.  No expanded domain or downstream physics object was created.
