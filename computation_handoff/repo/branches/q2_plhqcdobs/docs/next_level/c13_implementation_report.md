# C13/H6 implementation report

C13 enlarges the regulated microscopic state to seven sectors: QQQ, QQQG,
QQQUUBAR, QQQDDBAR, QQQGG, QQQUUBARG, and QQQDDBARG. Tower dimensions are
`4+6+9+9+12+16+16=72`, `7+10+15+15+20+24+24=115`, and
`10+14+21+21+28+32+32=158`.

The total-generator color certificates give six QQQGG singlets and eight
singlets in each sea-gluon sector. Three- and four-quark antisymmetry and
combined two-gluon bosonic symmetry close. Color-antisymmetric gluon
channels are retained with antisymmetric spin-orbital parity.

Two immutable H6 plans descend from H3 PLAN-A/B. The seven-block Hamiltonian
contains QQQG--QQQGG, sea--sea-gluon, two-gluon--sea-gluon conversion, and
PLAN-A spectator-lifted chiral blocks with generated adjoints. Hermiticity,
assembled/matrix-free action, Krylov, and full-bond TTN close. Three
resolution points refit the mass condition; one Jacobian null direction and
all holdouts remain visible. A reduced bond loses 47% of the Wilson-sensitive
observable while its energy error is only 0.0008.

The new sectors replace C12 induced first-order ubar, dbar, and gluon routes
inside the H6 validation root. Comparisons retain the immutable C12
remainders 0.018, 0.021, and 0.026 and decompose differences without fitting.
First-order q/qbar/g support is explicit. Second-order quark support is
explicit through QQQGG; second-order antiquark and gluon requests fail
because QQQQ-QBAR-GG and QQQGGG are absent.

Strict Dyson and Magnus polynomials agree through order two for commuting
and noncommuting SU(3) paths. The noncommuting oracle requires Omega2.
Path composition and reversal close, and truncation error/ unitarity scale
at cubic order. The two-step spectral rule separates both single-cut
surfaces from the real double-cut intersection; no squared delta or physical
epsilon is used. Finite-volume residual is 4.1e-6.

The strict second-order square-root-soft benchmark closes exactly. Missing
or duplicate S1-W1 and S2 terms give signed residuals. Sequential,
three-gluon, instantaneous-fermion, instantaneous-gluon, contact, vertex and
sector-counterterm, and current pieces close the finite gauge benchmark only
together. This is not full Slavnov-Taylor closure.

C13 adds 148 ordered injections and 336 requirements. Production remains
unreachable; the 216 routes and eight authoritative artifacts are unchanged.
The result is a finite-basis validation state, not a physical nucleon,
matched TMD, nuclear input, evolution object, or process prediction.

Reproduce with:

```bash
PYTHONPATH=src python scripts/build_c13_manifests.py 927
PYTHONPATH=src python scripts/validate_c13_architecture.py
PYTHONPATH=src python -m pytest -q
```
