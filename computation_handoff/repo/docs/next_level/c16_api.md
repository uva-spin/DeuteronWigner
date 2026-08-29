# C16/N1 validation API

`deuteron_wigner.nuclear.n1` extends the C15 types with an isolated
`NN + NNPI` finite-resolution state. `ThreeBodyCoordinates`,
`diagonal_recoil`, and `transition_recoil` are the authoritative three-body
coordinate and transfer interfaces. `basis_tower`, `build_hamiltonian`, and
`hamiltonian_report` expose the coupled exact/matrix-free benchmark.

`pion_parent` is an explicitly analytic, unmatched spin-zero oracle.
`operator_report` retains nucleon-active, pion-active, and coherent transition
blocks. `subtraction_report` implements internal + exchange - overlap.
`current_report`, `coherent_report`, `overlap_report`, and `cp_report` close
the finite continuity, helicity-pilot, parton/nuclear matching, and derived
partial-trace benchmarks. `parent_report` retains 6x6 parents for all five
species and Wilson orders 0--2. `compile_plan` rejects missing subtraction,
missing coherent overlap, mixed theories, and downstream use.

No N1 object is physical, matched, evolved, process-qualified, inferred, or
production reachable.
