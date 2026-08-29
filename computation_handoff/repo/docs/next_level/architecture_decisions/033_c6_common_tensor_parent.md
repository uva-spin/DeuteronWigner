# ADR 033: Common tensor before projection

**Decision:** Store one AMP-class tensor with target-helicity,
active-gluon-helicity, transverse, and three-adjoint color axes. Apply color
and polarization projectors only afterward as RED maps.

**Reason:** Separate fitted/projector-specific kernels would destroy common
state ancestry and prevent reconstruction tests.

**Status:** Validation-only factorized analytic parent.
