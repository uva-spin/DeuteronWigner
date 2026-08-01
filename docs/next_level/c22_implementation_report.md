# C22/M3 implementation report

C22/M3 adds a validation-only, operator-level twist-two small-\(b_{\rm TMD}\)
layer between C20 reference matching, C21 two-scale evolution, and the future
process compiler specified by Volume XVII. It does not execute a hard factor,
fragmentation function, W+Y construction, likelihood, or production route.

The immutable C21 baseline reproduced from descendant commit `ad3fa2a`: 1,053
tests passed; the 492/48 C20 matching and 438/102 C21 evolution splits remain
unchanged; the Q grid remains 1.6, 2, 3, 4, 5, 10, 20, and 100 GeV with the
4.18 GeV threshold; the production registry remains 216; and all eight
authoritative artifacts retain their accepted hashes.

## Implemented physics and mathematics

The code provides immutable, content-addressed endpoint distributions with
separate delta, regular, and logarithmic plus terms. The lower-limit plus
prescription is implemented analytically rather than with an endpoint cutoff.
Independent quadrature and Mellin-moment routes test the algebra. A preserved
HPL record supports validated real weight-zero, weight-one, and selected
weight-two words while rejecting unsupported branches.

Source-hashed declared-order coefficient records cover unpolarized quark and
gluon, helicity quark and gluon, nonsinglet transversity, rank-two linearly
polarized gluons, singlet off-diagonal blocks, and same-local-operator spin-1
LL matrix elements. Pretzelosity is recorded as a zero twist-two coefficient
through the demonstrated order, never as a vanishing physical TMD. The
repository executes only its explicit order-one distribution expressions.
Although higher-order primary papers are preserved, their presence is not
misrepresented as ingestion of their complete N3LO formulae or ancillaries.

The polarized path carries an explicit Larin/HVBM gamma5 record, finite axial
conversion, singlet/nonsinglet distinction, and anomaly status. Typed
nonsinglet, singlet quark/gluon, helicity, transversity, and LL evolution
blocks preserve operator identity. Rank-zero through rank-three maps store the
Bessel order, Fourier phase, reference mass, and error components separately.
Route-A/route-B discrepancies remain nonzero and below the declared first
omitted-order scale.

All 540 inherited operator identities receive an M3 record. The classification
does not invent metadata absent from C19: it records the inherited deterministic
coefficient-family mapping and retains the source limitation. Resolved NN,
NNPI, DeltaDelta, cluster, hidden-color, transition/interference, coherent
pilot, and matched-total ancestry remains explicit. Two hidden-color rotations
leave complete observables invariant while individual components change.

## Limits retained deliberately

No exact multiparton matching has been created for Sivers/Qiu--Sterman,
Boer--Mulders, genuine worm gears, f- or d-type tri-gluon functions, or
tensor-polarized T-odd channels. Spin-1 gluon double-flip remains unavailable
until both its coefficient and evolution kernel are reconciled in the project
scheme. Many-body operators without a proven common local operator retain an
operator-specific unavailable status. The physical Collins--Soper input and
large-\(b\) boundary remain C21 bottlenecks.

The accuracy label is limited by order-one coefficient, collinear, and nuclear
blocks and by the exploratory/unavailable nonperturbative CS kernel. It is not
upgraded by the existence of N3LO source papers.
