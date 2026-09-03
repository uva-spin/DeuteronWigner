# C309/HQCDRIMASSV0GRAMEVAL1 Codex Work Package

Evaluate the C305 full corrected-measure class-function Gram coefficients using the C308 center and mode-tail subtraction with regulator covariance.

Start from C308 in `AUTOPILOT_STATE.json`; frozen root `b4035029133db4f2264ff6b8ed367fb3e6857ba348ce6aee37d25229fa243371`. Verify/load C308. Apply the symmetric branch finite part and subtract `9(log N)^2-24logN`, propagate the center remainder interval, integrate with corrected `J/6` over symmetric excisions, and solve the constant/CHI8/RE_TF3 Gram system across N, epsilon, and quadrature windows. Publish interval coefficients, conditioning, residual and full covariance; compare visible PostScript mesh only as a digitization holdout. These are reduced-model benchmark shapes, never C43 coefficients.

Choose one `RIMASSV0GRAMEVAL1-A` through `-F`; A-D continue, E/F require certified blocker protocol. Publish evaluator, scans, Gram, coefficients, covariance, mesh parity, residual, release and isolation APIs. Run cumulative tests, 384 mutations, deterministic builds, safe reload, protected paths and quantum nonmutation. Commit once, never push, create one next contract/prompt, atomically advance state, and continue.
