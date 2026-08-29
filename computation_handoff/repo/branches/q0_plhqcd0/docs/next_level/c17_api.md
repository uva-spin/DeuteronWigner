# C17/N2 validation API

`deuteron_wigner.nuclear.n2` extends the immutable C16/N1 root with a typed
continuum `NNPI` channel, a neutral finite-volume spectral map, calibrated
transition kernel, pole/residue diagnostics, and a Hamiltonian-to-current
attachment certificate. `channels`, `spectral_density`, `self_energy`,
`finite_volume_report`, and `calibration_report` expose those interfaces.

`current_certificate` enumerates every retained N2 Hamiltonian term and its
exchange-current attachment. `continuity_report` gives component ablations
and all `NN`/`NNPI` and charge-channel blocks. `separator_report` tests the
internal/exchange/overlap/induced partition. `feshbach_report` compares
explicit and induced pion representations only when all operators are
transformed consistently.

`pion_active_report`, `coherent_report`, `cp_report`, and
`tensor_network_report` validate the unmatched pion-active, coherent
continuum, completely-positive reduction, and continuum-aware TTN routes.
`compile_plan` permits exactly one validation plan and rejects downstream
physical use. No N2 object is matched, evolved, process-qualified, inferred,
or production reachable.
