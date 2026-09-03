# ADR 049: Bond-dimension convergence

**Decision:** Use nested symmetry-allowed Rayleigh--Ritz subspaces at fixed
bond capacity and compare energy, overlap, current, and OAM errors.

**Reason:** SVD compression alone is not a variational solver. Nested spaces
provide a testable variational upper bound and monotone capacity sequence.

**Status:** H-TN benchmark only; no full-QCD entanglement claim.
