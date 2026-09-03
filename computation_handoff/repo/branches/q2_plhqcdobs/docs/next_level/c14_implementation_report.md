# C14/H7 implementation report

## Scope and inheritance

C14 extends the immutable C13/H6 validation root; it does not alter C13 or
the accepted phenomenological production model. The H7 Hilbert space adds
`QQQGGG`, `QQQUUBARGG`, and `QQQDDBARGG` to the seven inherited sectors.
The three ten-branch tower dimensions are 140, 227, and 314.

This implementation is a regulated finite-basis validation calculation. Its
color bases are reproducible representation/nullspace certificates at the
declared multiplicities, not stored ambient-space tensors. It is neither a
continuum-QCD calculation nor a phenomenological calibration.

## Color, statistics, and dynamics

The `QQQGGG` certificate retains 22 singlets: four symmetric, four
antisymmetric, and seven copies of the two-dimensional mixed S3 irrep. Each
sea--two-gluon sector retains 28 singlets split into 14 symmetric and 14
antisymmetric two-gluon-color channels. Symmetric, antisymmetric, and mixed
color sectors couple only to matching spin-orbital permutation irreps, so the
total gluon state is bosonic. The exact signed quark representation and
anti-fundamental antiquark identity remain explicit.

The ten-block Hamiltonian retains C13 links and adds typed three-gluon,
quark/antiquark emission, pair-conversion, and spectator-lifted chiral
routes. Every block has a generated adjoint. Unsupported interactions remain
typed unavailable rather than numerical zeros. Exact, matrix-free Krylov,
full-bond, and reduced-bond routes are compared. Full bond is exact; a
reduced bond loses 43% of the antiquark and 49% of the gluon order-two Wilson
signals while retaining a small energy error, demonstrating that energy
alone is not a convergence criterion.

At each resolution the mass-squared condition is refitted to 0.7744 and the
charge residual closes. Bare, counterterm, induced, and discrepancy flows
remain separate; one Jacobian null direction and unfitted second-order
antiquark/gluon holdouts are retained.

## Wilson, cuts, soft overlap, and gauge completion

Quark, antiquark, and active-gluon Wilson orders one and two are explicitly
supported. Order three fails closed even though `QQQGGG` exists, because the
cubic operator, cut, soft, and contact completion is absent.

Strict Dyson and Magnus polynomials agree through order two for fundamental,
anti-fundamental, adjoint, and ordered two-link classes. The two-link ledger
keeps left-left, right-right, left-right, and right-left topologies distinct.
The commutator ablation is nonzero, while composition, reversal, conjugation,
and piecewise-path checks close. The defect relative to an exact exponential
scales cubically, as required for an order-two truncation.

The cut ledger preserves two single-cut surfaces and the real double-cut
intersection without a squared delta or physical numerical epsilon. The
finite-volume residual is 3.8e-6. Fundamental, anti-fundamental, adjoint, and
ordered-two-link square-root-soft ledgers close exactly at strict order two;
missing and duplicate terms retain signed residuals.

The finite gauge ledger closes only with sequential, three- and four-gluon,
instantaneous-fermion/gluon, pair-conversion, chiral, counterterm, current,
residue, and regulator/zero-mode pieces. This is explicitly not full
Slavnov--Taylor or BRST closure.

## Operator and provenance boundary

Order-resolved quark and antiquark 4x4 helicity parents and the full gluon
target/field-index parent are retained before antiunitary link-even/odd
projection. Sivers and Boer--Mulders projectors remain distinct. All four
ordered gluon link pairs and independent f/d color channels are retained;
no process mixture is assigned.

Feshbach elimination relates explicit H7 sectors to transformed H6
Hamiltonian/operator descriptions with visible remainders (0.0024 for the
antiquark benchmark and 0.0037 for the gluon benchmark). This is an
equivalence-with-remainder relation, never an additive model component.

The package contains 390 stable requirements and 184 ordered negative
injections. The assumption compiler rejects mixed H7 plans, explicit plus
induced double counting, Wilson order three, and nuclear/matching/evolution/
process/inference/production requests.

## Remaining gates

UV finite matching, a physical TMD scheme, the continuum soft function,
Collins--Soper evolution, process factors, nuclear composition, and
inference remain unavailable. H7 adds no route to the 216-production-route
registry and changes none of the eight authoritative artifacts.

The exact next package is **C15/N0 -- matched spin-1 nuclear light-front
state and microscopic deuteron GTMD composition**, beginning with a
normalized NN spin-1 state, Hamiltonian-consistent one- and two-body
operators, complete nucleon helicity-matrix exports, correlated proton/
neutron microscopic members, and strict separation of partonic Wilson
rescattering from coherent nuclear propagation.
