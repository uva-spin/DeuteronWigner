# C310/HQCDRIMASSSHAPETAIL1 Codex Work Package

Derive and subtract the logarithmic `N` tails in the `CHI8` and `RE_TF3` full-Gram coefficients before epsilon extrapolation.

Start from C309 in `AUTOPILOT_STATE.json`; frozen root `0236468d261bf81f3efc380d5af7dce7540f0cde6bc11ebac42e7e1d7467c5eb`. Verify/load C309. Extend fixed-epsilon scans to larger N and multiple quadrature windows, derive tail coefficients from the C303 AST or enclose over fit families, subtract them separately in both shape channels, and publish fixed-epsilon finite remainders with correlated tail covariance. Do not guess exact rational coefficients, reverse the N/epsilon limit order, impose plot normalization on shape channels, or claim C43 matching.

Choose one `RIMASSSHAPETAIL1-A` through `-F`; A-D continue, E/F require certified blocker protocol. Publish tail derivation, scans, fit windows, fixed-epsilon remainders, covariance, residual, release and isolation APIs. Run cumulative tests, 384 mutations, deterministic builds, safe reload, protected paths and quantum nonmutation. Commit once, never push, create one next contract/prompt, atomically advance state, and continue.
