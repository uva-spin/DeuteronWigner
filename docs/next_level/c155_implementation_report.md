# C155/HQCDFLAVOR2 implementation report

Status: `C155_C154_SOURCE_DERIVED_ISOSYMMETRIC_UD_FLAVOR_LIFT_AND_MUD_ADAPTER_READY`.

The source chain classifies the C131/C142 object as a
`SINGLE_UNIDENTIFIED_FLAVOR_TEMPLATE`. Its retained QCD owners are flavor
diagonal and flavor blind in the external field label. Plan `FLAVOR2-B`
therefore publishes a reversible (u/d) direct-sum adapter without changing
any C43--C154 root or summing/averaging the historical block.

The mass coordinates are (m_l=(m_u+m_d)/2) and
\(\delta m=(m_d-m_u)/2\), with \(M=m_l I+\delta m\tau_3\),
\(\tau_3=\operatorname{diag}(-1,+1)\) in ordered `(u,d)` fibers. The
declared isosymmetric model subspace has (m_u=m_d=m_l); this does not claim
physical strong-isospin breaking is zero. The authenticated C154
\(m_{ud}^{\overline{MS}}\) capsule maps one-for-one to (m_l), with no
factor of two and pure-QCD/QED-subtracted semantics.

The lift doubles dimensions to `(2700, 5412, 9516)` for K9/K11/K13, has exact
zero cross-flavor blocks, and projects/round-trips exactly to each original
fiber. External flavor-copy count is kept separate from active (N_f), sea
flavors, threshold running, and QED charges. Numerical running, matching
windows, and physical targets are not executed in C155.

Next continuation: `C156/HQCDMATCHGRID2`.
