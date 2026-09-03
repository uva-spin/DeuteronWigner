# C161/HQCDMATCHIR4 implementation report

C161 consumed the sole committed continuation contract
`docs/next_level/c160_c161_hqcdmatchir4_continuation_contract.json` and
verified the frozen C160, C159, and C158 package roots.  The unrelated
`tests/test_c134_hqcdtarget.py::test_four_capsules_and_adapters` expectation
failure (expected 4, observed 115) was quarantined before C161 science.  Its
dependency surface imports only the C134 target package and does not reach
C158--C161; C134 was not modified.

The selected plan is `MATCHIR4-B`.  C159 supplies 25 immutable target
descriptors and a safe 17-opcode grammar, but its source-qualified descriptors
explicitly lack numerical source expressions and constants.  C161 therefore
records all 25 as `SOURCE_EXPRESSION_INCOMPLETE`, produces no target value,
and creates no invented formula or constant.  Exact symbolic adapters are
published for `g_s`, `g_s^2`, `alpha_s`, `a_s`, `V_B`, `Z_1F`, `g_R`,
`g_R/g_s`, signed `m_R`, and `m_R^2`, including derivative and sign guards.

Finite-basis data are imported through the immutable C158 public API with an
explicit common record, coupling record, and fixture.  Common-state and IR
schemas, frozen atlas metadata, explicit remainder envelopes, and all
fail-closed cancellation/conversion/bracket gates are present, but no
numerical target-dependent authority is claimed.  K9/K11/K13, all four
fixtures, active `N_f`, and the C155 u/d block identity remain separate.

The sole evidence-driven continuation is `C162/HQCDLFGNUM3`, whose contract
requests completion of the missing source-qualified target binding.  The full
adaptive matching grid, physical scale selection, physical inputs, running,
thresholds, inverse matching, counterterms, null representatives, quantum
objects, states, and TMD/process objects remain untouched.
