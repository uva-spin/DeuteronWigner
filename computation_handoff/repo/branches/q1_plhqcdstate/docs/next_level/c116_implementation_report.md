# C116/ICHO2 implementation report

Status: `C116_ICHO2_KERNEL_CLASS_INCOMPLETE`.

The five C115 IDs are frozen exactly: `I4_local`,
`I2_density_projector`, `derivative_density`, `CM_ground`, and
`triplet_projected`. All eight C115 programs map exhaustively to those
classes. `I4_local` has a two-route exact finite Laguerre/Gamma and
Cartesian-generating-function spatial expression with zero route residual;
C80 reuse is limited to that spatial integral only.

The four graph/projector classes require finite-shell internal projectors
that are not present in the authenticated source chain. No continuum
completeness, threshold, C57/C58 regulator, or zero substitution was used.
One program (`J_qJ_q:q->q`) is terminal at the spatial-class level; the
remaining seven remain blocking, so no current component or complete block
is assembled. Sole continuation: `C117/ICREG2`.
