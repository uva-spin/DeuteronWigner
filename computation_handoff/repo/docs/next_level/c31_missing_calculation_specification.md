# Missing C11 regulator-specific LF-to-TMD calculation

The bridge requires a calculation not currently present in the sources or
repository.

## Operator and regulators

Compute the same rank-zero proton quark bilocal used by the C11 finite-basis
overlap, retaining its longitudinal, transverse/OAM, infrared, endpoint,
state-normalization, flavor, and positive-x antiquark conventions. Introduce a
declared staple Wilson line, rapidity regulator, and target project
square-root-soft prescription without replacing the C11 basis regulator by a
continuum regulator through assumption.

Freeze a partonic quark external state with momentum, helicity, flavor, gauge,
off-shellness or another common IR regulator, basis regulator, Wilson
direction, μ, and ζ. The C11-regulated and project-scheme computations must use
the same IR regulator or an independently proved IR conversion.

## Required contributions

At the first nontrivial order calculate quark self energy, the bilocal vertex,
real emission, Wilson attachments and self energy, the soft graph, zero-bin or
overlap subtraction, UV and rapidity counterterms, Hamiltonian/basis
counterterms, instantaneous light-front terms, and endpoint/basis-regulator
terms. Determine operator mixing and regulator power corrections rather than
absorbing them into normalization.

## Required closure

The extracted state-independent matching kernel must demonstrate:

- cancellation of common IR dependence in the matching difference;
- UV-pole cancellation after renormalization;
- rapidity-pole cancellation after soft/rapidity subtraction;
- gauge-parameter independence;
- quark number and tree-level normalization;
- charge-conjugation relations for positive-x antiquarks;
- μ and ζ anomalous dimensions;
- threshold consistency;
- convergence as the finite longitudinal/transverse basis is enlarged;
- a visible first omitted order and regulator-power remainder.

Only after these tests pass may the formal project-to-ART25 adapter and scale
maps be applied to a microscopic numerical vector.
