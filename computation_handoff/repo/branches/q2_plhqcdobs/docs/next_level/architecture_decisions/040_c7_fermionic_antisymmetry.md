# ADR 040: Fermionic antisymmetry strategy

**Decision:** Apply an exact signed permutation representation and its
antisymmetrizer before Hamiltonian matrix assembly.

**Reason:** Exchange signs are structural constraints, not coefficients that
may be repaired after diagonalization.

**Status:** Implemented for three- and four-fermion retained sectors.
