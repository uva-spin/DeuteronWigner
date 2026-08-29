# C41/R2B regulator-identity gate: Branch B fail-closed correction

C41 audited every C40 numerical object before evaluating a one-loop diagram.
All 16 required objects are executable but classified
`EXECUTABLE_TOY_NOT_PHYSICS_IDENTICAL`, not
`REGULATOR_IDENTICAL_EXECUTABLE`.  The C40 code supplies deterministic
coordinate arrays and internal algebra checks, but not source-derived
light-front Hamiltonian, SU(3) vertex, constrained sector, finite-basis
spacelike Wilson operator, physical counterterm conditions, bilocal
measurement, or refinement map in the fixed C36 scheme.

Accordingly C41 does not construct a dressed probe, bare residual,
counterterm solution, continuum result, soft/overlap subtraction, or matching
kernel.  Each is serialized explicitly as empty-not-zero/not-executed rather
than inferred.  The exact result is
`C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL`; the next targeted package is
C42/M0C, not a relaxation of the regulator-identity requirement.

The 128 C41 mutation tests operate on live C40 numerical arrays and confirm
that altered numerical inputs fail the C40 readiness gate.  They are integrity
controls only, not evidence that the arrays are physical.
