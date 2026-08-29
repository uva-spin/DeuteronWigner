# C144/HQCDOPAPI implementation report

Resolved baseline: `204b2823a1c237ad8e0ceea88bdf932763c3cb50` (HEAD).

Status: `C144_C143_SOURCE_DERIVED_PUBLIC_PARAMETERIZED_C131_OPERATOR_API_READY`.
Selected plan: `OPAPI-A`.

C144 audits C143's over-specified record boundary and replaces it with two
mutually exclusive coordinate representations:

- `ORIGINAL_DIRECTION_BASIS` with eleven explicit directions;
- `C136_IDENTIFIED_PLUS_NULL_BASIS` with `phi_mass`, `phi_coupling`, and
  nine explicit null coordinates.

Mixed records, partial null vectors, implicit zeros, and duplicate
counterterm specifications are rejected. Four deterministic fixtures are
explicitly loaded by ID only: `FIXTURE-FREE`, `FIXTURE-INTERACTING-A`,
`FIXTURE-INTERACTING-B-NULL-SHIFT`, and `FIXTURE-MASS-SIGN`. They are
nonphysical diagnostic points, not defaults, fits, anchors, or nullspace
solutions.

The unchanged C131 public component authorities are exposed through three
independent routes: sparse owner assembly, matrix-free owner actions, and
independent q/qg block assembly. Route mismatches, derivative mismatches,
unit mismatches, and Hermiticity defects are zero for all fixtures and
resolutions. Exact `m_q^2=(m_q)^2` chain-rule metadata is retained.

Only the shifted operator preflight `zI-M²` is exposed. No inverse,
resolvent, self-energy, state, spectrum, physical parameter, counterterm,
or downstream object is created. The A/B null-shift fixtures preserve the
identified coordinates while allowing matrix-valued null directions to
change the operator; no representative is preferred.

Continuation: `C145/HQCD2PTQ2`.
