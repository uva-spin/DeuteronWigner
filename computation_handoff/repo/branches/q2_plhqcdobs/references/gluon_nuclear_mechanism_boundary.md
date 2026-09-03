# Non-impulse gluon nuclear mechanism boundary

Last updated: 2026-07-26

`src/deuteron_wigner/gluon_nuclear_mechanisms.py` composes non-impulse
contributions directly as spin-1 target-helicity by gluon-transverse-index
matrices of shape `(3,3,2,2)`. It retains separate ledger entries for
coherent shadowing, antishadowing, off-shell response, meson exchange, and
non-nucleonic structure. Every entry has an independent source, evidence
class, validity domain, uncertainty description, and switch.

## Implemented nonzero components

The only source-backed builder is inclusive gluon shadowing. It uses the
configured diffractive input and deuteron longitudinal coherence factor, but
acts only on the target-unpolarized \(U\) projection and the trace
\(\delta_T^{ij}\) gluon polarization. This is the part constrained by an
inclusive gluon diffractive response.

It does **not** apply the same response to:

- target \(L,T,LL,LT,TT\) sectors;
- circularly polarized gluons;
- linearly polarized gluons;
- gluon T-odd color structures.

Those responses require polarized/tensor diffractive inputs or an explicit
model component. Leaving their corrections zero is a configuration state,
recorded as unconstrained, and is not a claim of physical absence.

An inclusive gluon antishadowing builder uses the same sector restriction.
Its normalization is not copied from the quark enhancement: callers supply
an `AntishadowingInput` constructed from the configured gluon momentum
density and shadowing loss. The restored fraction and uncertainty remain
explicit.

Named diffractive uncertainty functions propagate as complete Hermitian
correlator members in a separate uncertainty ledger. Member identity is
retained; the code neither invents a covariance nor reduces named scenarios
to independent pointwise errors.

## Composition and refusal rules

The mechanism map has one slot per physical mechanism, preventing duplicate
anonymous additions. A configured input must carry the mechanism identity
expected by its slot. Inputs outside their declared validity return an exact
zero contribution. Wrong shapes, nonfinite values, non-Hermitian matrices,
unknown labels, and mechanism mismatches are rejected.

The total reconstructs exactly as proton impulse plus neutron impulse plus
all five named corrections. This layer does not yet provide numerical gluon
off-shell, pion, or hidden-color terms, nor polarized/tensor shadowing: no
defensible spin-resolved source has been promoted for those sectors.
