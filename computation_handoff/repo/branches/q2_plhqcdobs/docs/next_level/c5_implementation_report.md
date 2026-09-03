# C5 implementation report

## Scope

C5 adds a dynamical but validation-only one-gluon Wilson-line and
light-front-cut pilot above the immutable C4 common-parent boundary. It is
not a fitted TMD, soft-subtracted QCD correlator, nuclear rescattering model,
evolution input, or process prediction.

The implemented chain is:

`C3 SpinorOAMState -> BareWilsonSegment -> derived eikonal pole ->
LFResolventTerm + CutLedger -> OneGluonPilotKernel ->
AntiunitaryLinkReversal -> link-even/link-odd correlators -> distinct RED
projectors`.

## Origin of the imaginary part

For a path with stored orientation `eta`, Fourier convention
`exp(-i l·x)`, covariant derivative `D=partial+igA`, and gluon momentum into
the eikonal line, the code derives

`1/(v·l-i0 eta) = PV(1/(v·l)) + i eta pi delta(v·l)`.

The absorptive pilot term is nonzero only when all of the following exist:

1. a nonzero one-gluon coupling;
2. declared physical cut support in the cut ledger;
3. nonzero `Lz=0` and `|Lz|=1` amplitude blocks;
4. the identified OAM interference kernel.

Removing any item gives exact zero. No imaginary coefficient or fitted width
is accepted. Direct finite-epsilon integration is a separate convergence
oracle; `epsilon_is_physical` is structurally false and epsilon never enters
the result envelope.

## Benchmarks

- **C5-A:** future/past PV equality, opposite distributional cuts, path
  inversion/composition, and finite-epsilon convergence.
- **C5-B:** an off-shell discrete LF state has exactly zero absorption; only a
  declared continuum/finite-volume rule produces cut weight.
- **C5-C:** future/past link reversal, exact zero limits, analytic OAM
  interference, and distinct Sivers-like and Boer–Mulders-like projections.
- **C5-D:** `C_F=4/3`, `C_A=3`, `f·d=0`, ordered two-link preservation, and
  restricted pilot Ward closure.
- **C5-E:** duplicate physical support fails without an explicit relation and
  is counted once with `EQUIVALENT_COUNT_ONCE`.

Exact residuals are generated in `c5_benchmark_manifest.json`.

## Isolation and limitations

C5 has a disjoint validation provenance graph with only read-only ancestry to
the C3 state definition. It cannot enter the accepted 216-route registry,
production provenance root, nuclear composition, QCD evolution, or a `PROC`
map. The cut equivalence/subtraction relations are executable finite
two-cells, but this does not complete the general Volume 0
`Provenance2Complex`.

The still-unresolved Volume III work includes non-Abelian Wilson-line
resummation, independent dynamical active-gluon ordered-link `f/d` channels,
soft/rapidity overlap accounting, full all-sector Ward closure, and matching
to a closed QCD operator basis.
