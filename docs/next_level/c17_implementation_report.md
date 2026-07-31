# C17/N2 implementation report

C17 replaces the finite-only N1 transition oracle with a continuum-calibrated
`NNPI` validation system while preserving every C16 and production artifact.
The complete `pn pi0`, `pp pi-`, and `nn pi+` charge basis is retained with
charge +1, isospin zero, J-parity 1+, odd pion orbital parity, and explicit
delta-energy continuum normalization. The threshold spectral density has the
correct square-root opening; the physical cut is exactly absent below
threshold and appears above it. Principal-value self energy, pole shift,
derivative, and residue are separately reported.

A neutral finite-volume map at 32, 64, 128, and 256 levels converges toward
the continuum normalization and first moment without putting a numerical
epsilon into operator identity. Calibration records pole, transition,
charge/isospin, and current constraints separately from seven holdouts. One
Jacobian null direction remains explicit; no TMD output is used in the fit.

The declared-order exchange-current certificate maps each retained
Hamiltonian interaction to its gauged attachment. The finite continuity
identity closes component by component and in `NN -> NN`, `NN -> NNPI`,
`NNPI -> NN`, `NNPI -> NNPI`, and all three charge blocks. Charge, magnetic,
quadrupole, angular-condition, and GTMD/current residuals are independently
recorded. Ablations expose the defect caused by omitting each contribution.

Internal-nucleon, exchange-pion, overlap, induced-Hamiltonian, and
induced-current terms are varied along a four-point separator trajectory.
Their matched variation is below the declared tolerance. The explicit and
Feshbach-induced descriptions are certified as equivalent only with the
Hamiltonian, vector, axial/pseudoscalar, EMT, pion-partonic, transition, and
norm-kernel operators transformed together; a visible truncation remainder
is retained.

The pion-active parent remains unmatched and validation-only. A coherent
continuum pilot combines charge and helicity amplitudes before tracing, and
the corresponding reduction has a nonnegative Choi spectrum. The nuclear
TTN preserves continuum-level identity; the full-bond result closes against
the exact Krylov result, while low bond dimensions visibly lose transition,
current, and tensor information.

C17 covers 614 stable requirements and 340 ordered negative injections. It
does not claim a complete chiral EFT, physical pion or deuteron TMD,
diffractive/Glauber matching, light-front-to-QCD matching, evolution,
process factorization, inference, or production readiness. DeltaDelta,
compact six-quark, and hidden-color sectors are not represented at N2.
