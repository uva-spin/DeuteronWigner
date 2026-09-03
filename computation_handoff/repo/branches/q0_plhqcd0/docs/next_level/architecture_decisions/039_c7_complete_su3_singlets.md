# ADR 039: Complete SU(3) singlet multiplicities

**Decision:** Compute common nullspaces of all total SU(3) generators instead
of selecting one convenient color contraction.

**Reason:** The retained \(qqq\), \(qqqg\), and \(qqqq\bar q\) sectors contain
1, 2, and 3 independent singlets. Omitting multiplicity channels invalidates
closure and vertex tests.

**Status:** Implemented with generator, orthonormality, recoupling, rank, and
content-hash diagnostics.
