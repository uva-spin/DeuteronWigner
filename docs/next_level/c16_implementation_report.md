# C16/N1 implementation report

C16 adds a normalized `NN + NNPI` validation state on the immutable C15
root. The three tower dimensions are 30, 52, and 78. The fine state has
`Z_NN = 0.8915758315` and `Z_NNPI = 0.1084241685`; these are resolution
diagnostics, not measured probabilities. The complete charge basis contains
`pn pi0`, `pp pi-`, and `nn pi+`, coupled to charge +1, isospin zero, and
J-parity 1+ with the required odd orbital parity.

One typed three-body recoil authority handles active nucleons and pions; a
separate number-changing map handles transitions. The coupled Hamiltonian is
Hermitian, has generated adjoints, and agrees between exact and matrix-free
Krylov solutions. One null direction and unfitted transition, pion, tensor,
and current holdouts remain visible.

Nucleon-active, analytic pion-active, and Hermitian transition operators form
the common N1 parent. The pion oracle has no independent deuteron
normalization and is explicitly unmatched. Internal-nucleon and exchange
pion regions use an executable overlap projector; missing and duplicate
subtractions give opposite signed defects.

The Hamiltonian-consistent current contains nucleon, pion-in-flight,
transition, contact, induced, counterterm, regulator, and truncation pieces.
The finite continuity ledger closes only with all pieces. A helicity-resolved
coherent small-x pilot combines amplitudes before tracing and is explicitly
not physical shadowing. Partonic Wilson and nuclear coherent mechanisms have
independent identities and a count-once overlap subtraction.

Complete 6x6 deuteron parents are retained for u, d, ubar, dbar, and gluons
at Wilson orders 0, 1, and 2. Full-bond TTN results equal exact results; the
lowest bond has a 0.11% norm error while losing 44--56% of pion, transition,
tensor, current, or coherent signals. C16 covers 516 requirements and 308
ordered negative injections.

This remains a finite-basis validation package. It does not provide a
physical pion distribution, complete chiral nuclear EFT, complete exchange
currents, physical shadowing/Glauber dynamics, matching, evolution, process
factorization, or inference.
