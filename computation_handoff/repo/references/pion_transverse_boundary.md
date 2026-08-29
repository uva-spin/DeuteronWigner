# Pion transverse boundary and nuclear recoil

The first non-Gaussian transverse pion scenario uses the Vpion19
nonperturbative factor from A. Vladimirov, JHEP 10 (2019) 090,
arXiv:1907.10356. The vendored arTeMiDe source provides the central values
\((a_1,a_2,a_3)=(0.173426,0.482789,2.15172)\) and 100 replica triples:

\[
F_{\rm NP}^{\pi}(z,b)=
\exp\left[-{(a_1+(1-z)^2a_2)b^2\over
\sqrt{1+a_3b^2}}\right].
\]

This factor is normalized to one at \(b=0\). It is only the fitted
nonperturbative boundary, not the complete evolved pion TMD. Vpion19
originally used JAM18 collinear input and BSV19 evolution. Combining the
factor with JAM21 is therefore an explicit input-transfer scenario, not a
refit.

The nuclear transverse momentum is not assigned by this pion-internal
factor. The Miller Sullivan integrand is retained before its \(q_T\)
integration and composed according to

\[
\boldsymbol{k}_{T,D}=\boldsymbol{k}_{T,q/\pi}
z\boldsymbol{q}_{T,\pi/D}.
\]

Consequently its impact-space kernel contains
\(J_0(zbq_{T,\pi/D})\). Tests prove that both the nuclear splitting and the
full convolution reduce to the validated collinear results at \(b=0\).
This avoids replacing the two physically distinct transverse motions with
one arbitrary Gaussian.

Two evolution routes are retained:

1. `EvolvedTransversePionScenario` is the original one-loop diagnostic.
2. `Vpion19ArtemidePionTMD` uses the vendored fit-native Vpion19 model,
   NNLO small-\(b\) coefficients, and BSV19 NNNLO evolution. Its dedicated
   constants restore hadron 2 and the two-hadron arTeMiDe grid.

The official LHAPDF archive no longer distributes JAM18. Earlier attempted
local JAM18 downloads were CERN error HTML and are rejected. The maintained
JAM21 member 0 is therefore substituted explicitly in
`build/artemide/const-Vpion19-native`. This native route is order-consistent
at the perturbative matching/evolution level but remains non-production
because the Vpion19 nonperturbative parameters were not refitted with JAM21
and no fixed-order \(Y\) term is present.

`NativeEvolvedTransversePionScenario` composes the full native pion TMD with
the same exact \(J_0(zbq_T)\) nuclear recoil kernel. It does not multiply a
second evolution factor or collapse pion-internal and nuclear transverse
motion into one width. All 101 Vpion19 member identities have been evaluated
at \(Q=5\) GeV and the central nuclear boundary is finite on the audited
\(b\) grid. The nuclear convolution now propagates all 100 physical Vpion19
members, rather than applying intrinsic-profile bands only before the
nuclear kernel. The Miller splitting is Fock normalized by
\(1/(1+N_\pi)=0.97915215\), consistently with the retained NN and NNπ
nucleon sectors.

At \(x_N=0.1,Q=5\) GeV the native pion term is assembled with the separately
validated AV18 retained-NN recoil in
`nnpi_native_combined_av18_x010.csv`. Its figure separates the total
scenario from the native-pion component so the Vpion19 q16/q84 band remains
visible. This is a controlled low-\(k_T\) W-term scenario, not a production
claim: JAM21 is still an unrefitted substitute and the fixed-order Y term is
absent. No native tensor-pion TMD profile is sourced, so a transverse
\(f_{1LL}^{\pi}\) curve is deliberately not manufactured.

The newer JAM 2023 simultaneous pion
TMD analysis (arXiv:2302.01192) is preferred in principle, but its paper
does not publish the 25-parameter replica ensemble or a callable grid.

```text
PYTHONPATH=src python -m pytest -q tests/test_pion_tmd.py
/Users/dustin/miniforge3/bin/python3.9 tools/prepare_vpion19_artemide.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_native_pion_tmd_scenario.py
```

Persistent outputs:

- `outputs/figures/pion/native_vpion19_jam21_bspace.csv`
- `outputs/figures/pion/native_vpion19_jam21_bspace_members.csv`
- `outputs/figures/pion/native_vpion19_jam21_bspace.validation.json`
- `outputs/figures/pion/nnpi_native_combined_av18_x010.csv`
- `outputs/figures/pion/nnpi_native_combined_av18_x010.pdf`
