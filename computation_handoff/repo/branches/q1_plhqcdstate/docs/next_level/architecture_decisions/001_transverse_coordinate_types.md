# ADR-001: Distinct transverse coordinate types

Status: proposed for C1

Decision: represent partonic `kT`, GTMD `DeltaT`, `bDelta`, TMD `bTMD`,
nuclear `DeltaNT`, `pT`, `RT`, and measured `qT` as different immutable
types, including radial variants, units and conjugate-pair metadata. Fourier
maps accept only their declared pair.

Rationale: these coordinates belong to different fibers and enter different
Fourier kernels and recoil maps. Numeric equality does not make them
interchangeable. The existing `BDelta`/`BTMD` split proves feasibility but
does not cover radial or nuclear/process APIs.

Alternatives rejected: one generic vector with a string tag (runtime and
serialization errors remain easy); one universal `b` alias (current audit
shows high-risk ambiguity).

Consequence: legacy functions require zero-cost adapters. C1 must demonstrate
unchanged oracle hashes and injected cross-coordinate failures.
