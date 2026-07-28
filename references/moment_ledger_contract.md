# Support-aware moment ledger

`src/deuteron_wigner/moment_ledger.py` represents number, momentum,
helicity, tensor, and transversity moments with explicit species, flavor,
mechanism, source, tabulated \(x\) interval, and endpoint completion.

The ledger always permits a clearly labeled partial integral. It permits a
conservation or sum-rule audit only when either:

1. the numerical table spans exactly \(0\le x\le1\); or
2. the requested observable has an explicit finite endpoint correction with
   source and uncertainty.

An endpoint correction for one moment does not close another: for example, a
number correction cannot silently complete a momentum moment. The sum-rule
auditor also consumes an explicit entry selection, so a total mechanism
cannot be added together with its proton/neutron components.

The current AV18 NNπ production parent table has 37 points over
\(0.001\le x_N\le0.95\). `scripts/audit_parent_moment_coverage.py` extracts
the complete collinear correlator for \(u,d,\bar u,\bar d\), projects
\(f_1,g_1,f_{1LL},h_1\), keeps proton, neutron, and total mechanisms
separate, and writes 60 number, momentum, helicity, tensor, and transversity
entries. Endpoint completions use local integrable power fits only when the
serialized parent reaches \(x_N\le0.01\) and \(x_N\ge0.9\), has a stable
endpoint sign, and passes adjacent fit-window variation. The variation is
stored as a model sensitivity, not a statistical covariance.

Number conservation is applied to \(q-\bar q\) before the low-\(x\) fit;
separate sea-number integrals are not required to converge. The per-nucleon
AV18 valence sum is 3.00735 against 3 within the declared 0.03
endpoint/grid tolerance.

An endpoint-aware AV18/CT18 grid includes
\(\bar b,\bar c,\bar s,\bar u,\bar d,d,u,s,c,b,g\). Its total momentum is
1.001566 against 1 with endpoint-window sensitivity 0.000176 and tolerance
0.002. A separate retained-spin BDSSV24 parent supplies the gluon helicity
moment, \(0.43502\), with 0.00254 endpoint-window sensitivity. The
gluon tensor local twist-two moment uses its required \(x\) weight and is
\(3.06955\times10^{-7}\), with \(2.36372\times10^{-8}\) endpoint
sensitivity. Applying a quark-like \(x^0\) tensor moment to the gluon is
explicitly disallowed.

The ledger contains 69 primary quark/gluon entries plus the separately
serialized 11-parton momentum audit. Individual sea-number integrals are
allowed to remain divergent because no conservation law requires them;
valence combinations are the physical number sum rules. Numerical
non-impulse components retain their own pion momentum, tensor, and
hidden-color sum-rule audits. Mechanisms without a sourced numerical input
remain explicit provenance-labeled zero baselines and acquire no invented
global moment. On this declared scope the WP8 global-moment requirement is
verified.

Artifact: `outputs/validation/av18_parent_moment_coverage.json`.
