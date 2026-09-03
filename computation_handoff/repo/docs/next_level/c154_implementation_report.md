# C154/HQCDPHYSINPUT2 implementation report

Status: `C154_HQCDPHYSINPUT2_FLAVOR_IDENTITY_INCOMPLETE`.

Plan `PHYSINPUT2-B` is selected. The authenticated PDG 2026 source cache
provides the standard coordinates (m_{ud}^{\overline{MS}}(2 GeV,N_L=4)=3.397
\pm0.045\,MeV) (p.6, Eq.60.4) and
\(\alpha_s(m_Z^2)=0.1180\pm0.0009\) (p.42, Eq.9.25). Their source hashes,
locators, schemes, scales, active flavors, uncertainty semantics, and
positive branches are retained as immutable capsules.

The C131 mass direction remains `GENERIC_LIGHT_QUARK` in the authenticated
C131/C142 chain. It has not been identified with (m_{ud}), (m_u), or
(m_d); no proxy or QCD+QED assumption is made. C153 exposes no numerical
matching-window records, so no inverse finite-basis target or physical solve
is fabricated. Mass/coupling covariance is `MARGINAL_INPUTS_ONLY`, never a
fabricated zero. Nine null coordinates and six counterterm directions remain
explicit and unselected.

The exact continuation is `C155/HQCDFLAVOR2`.
