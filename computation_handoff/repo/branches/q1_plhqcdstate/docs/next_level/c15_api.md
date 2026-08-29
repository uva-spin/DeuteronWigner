# C15/N0 validation API

`deuteron_wigner.nuclear.n0` is the isolated NN-only spin-1 nuclear
validation root. `plans()` exposes AV18, Norfolk, H7-dynamics variation, and
analytic-oracle branches as mutually exclusive members. Wave-source bytes
are hashed into the correlated proton/neutron member identity.

`recoil()` is the sole zero-skewness spectator-preserving nuclear recoil
authority. `build_state()` loads the declared S/D radial amplitudes and
constructs three normalized deuteron-helicity amplitudes. `spectral_amplitude`
retains the joint target/nucleon 6x6 helicity space. `projector_registry()`
provides the complete nine-dimensional U/L/T/LL/LT/TT target basis.

`deuteron_parent()` returns 6x6 quark, antiquark, or gluon parents at Wilson
orders zero, one, or two. Gluons retain four ordered links and independent
f/d identities. `reductions`, `b1_report`, `current_report`, `tagged_report`,
`cp_report`, and `ttn_report` are common-parent validation closures.

N0 exports no physical deuteron, nuclear Wilson, matching, evolution,
process, inference, or production object.
