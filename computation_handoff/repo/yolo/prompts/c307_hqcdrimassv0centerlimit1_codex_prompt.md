# C307/HQCDRIMASSV0CENTERLIMIT1 Codex Work Package

Define and validate the one-sided or symmetric finite-part value of C293 `V₀` at the source subtraction point `u=v=1/2`.

Start from C306 in `AUTOPILOT_STATE.json`; frozen root `acf0dc63172ddf5959561c6deb2af33b5d748f93cd31889fdf37f1daac8f500e`. Verify/load C306. Evaluate the C303 AST along `v-u=±delta` at fixed N, derive divergent coefficients, compare one-sided branches under the source sawtooth convention, and test symmetric average/subtraction before and after `N→∞`. Cross-check the recovered finite part against the `potSU3.ps` center/minimum normalization without treating the plot as exact beyond its vector resolution. Publish the chosen project reduced-model branch prescription only if it is symmetry compatible and fully explicit; otherwise preserve the branch family. Never claim C43 matching.

Choose one `RIMASSV0CENTERLIMIT1-A` through `-F`; A-D continue, E/F require certified blocker protocol. Publish branch AST, asymptotics, subtraction, plot parity, limit family, covariance, residual, release and isolation APIs. Run cumulative tests, 384 mutations, deterministic builds, safe reload, protected paths and quantum nonmutation. Commit once, never push, create one next contract/prompt, atomically advance state, and continue.
