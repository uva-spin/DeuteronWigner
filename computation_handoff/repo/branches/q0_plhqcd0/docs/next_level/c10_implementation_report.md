# C10/H3 implementation report

C10 extends the isolated common microscopic state to `QQQ + QQQG +
QQQUUBAR + QQQDDBAR`. The three towers have sector dimensions
`4+6+9+9`, `7+10+15+15`, and `10+14+21+21`. The light-pair sectors are
distinct positive-support active-antiquark spaces, not negative-x copies.

All three \(3^4\otimes\bar3\) singlets and the anti-fundamental generator are
inherited from the complete C7 color nullspace. Exact signed S4
antisymmetrization is imposed on the four-quark subsystem before assembly.
Canonical \(g\leftrightarrow u\bar u,d\bar d\) blocks retain flavor, helicity,
OAM, fermion sign, and color multiplicity and are paired with generated
adjoints. PLAN-A adds an owned isovector pseudoscalar/derivative chiral
interaction; PLAN-B disables it. Explicit and induced sea routes fail closed.

Sector-indexed mass, pair, chiral, and vertex parameters flow at three
resolutions. The shared pole closes at \(M^2=0.7744\), while a Jacobian null
direction and all frozen holdouts remain visible. The C9 vector Ward
benchmark remains closed.

The finite-basis PCAC identity contains one-body axial, pair axial, chiral
exchange, pseudoscalar density, induced pion-pole, current counterterm,
regulator, and basis-truncation entries. Its sum closes, and removal of every
nonzero required contribution produces a signed residual. This is not a
continuum chiral-symmetry proof or an explicit physical pion state.

Exact, Krylov, and four-branch TTN solutions are compared. Full bond
reconstructs the exact state; low bonds can have reasonable energy while
losing all sea-flavor, antiquark-OAM, and PCAC-sensitive content.
Probability, valence flavor, charge, baryon number, momentum, and canonical
\(J^z\) ledgers close.

Direct positive-x antiquark slots generate regulated GTMD/TMD/PDF/current
routes for `ubar` and `dbar` from the same state identity as quark and gluon
parents. They carry explicit UV, link-shortening, rapidity/soft, evolution,
and process limitations and are not physical distributions.

Feshbach elimination transforms vector, axial, pseudoscalar, and antiquark
operators and retains a nonzero remainder and norm kernel. The antiquark
Wilson handoff preserves flavor and all three color multiplicities, returns
zero absorption without physical support, and never issues `WILSON_READY`.

C10 covers 210 stable requirements and detects 90 ordered injections. It is
validation-only and unreachable from production, nuclear, evolution,
process, or inference roots.
