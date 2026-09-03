# C306/HQCDRIMASSV0FINITEEVAL1 Codex Work Package

Evaluate the C305 ordered `N→∞` then `ε→0` coefficient family with convergence and path-dependence enclosures.

Start from C305 in `AUTOPILOT_STATE.json`; frozen root `bd276d6c64b573f7ccf791e22e5251cd16f9f871b27cada4caf07de32b4bc173`. Verify/load C305. Execute the exact C303 three-sum AST with `V_N-V_N(1/2,1/2)`, corrected `J/6`, symmetric three-root excision, and constant/CHI8/RE_TF3 Gram solve. At fixed epsilon extrapolate multiple N sequences with interval tails, then extrapolate epsilon. Test reversed and simultaneous paths as scheme holdouts; publish correlated numerical/quadrature/tail/path covariance. If limits fail, preserve the coefficient family rather than inventing a point. All outputs remain reduced-model benchmarks, not C43 matching.

Choose one `RIMASSV0FINITEEVAL1-A` through `-F`; A-D continue, E/F require certified blocker protocol. Publish executable evaluator, convergence tables, enclosures, Gram conditioning, coefficient family, covariance, residual, release and isolation APIs. Run cumulative tests, 384 mutations, deterministic builds, safe reload, protected paths and quantum nonmutation. Commit once, never push, create one next contract/prompt, atomically advance state, and continue.
