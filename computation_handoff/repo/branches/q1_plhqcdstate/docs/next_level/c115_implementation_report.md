# C115/ICHO implementation report

Status: `C115_ICHO_TRANSVERSE_KERNEL_INCOMPLETE`.

All eight diagonal programs are frozen with explicit source monomial,
normal-ordering, longitudinal, spin, color, projection, regulator,
normalization, ancestry, and Hermitian-partner fields. The source-insertion
and canonical-bracket routes agree symbolically for both the good-quark and
transverse-gluon currents. The finite-cell C114 longitudinal factor remains
unchanged.

No operator-identical C80 spatial reuse was claimed. The five required
current-specific HO/projector classes lack authenticated exact finite-shell
expressions and graph-specific regulator records, so all eight diagonal
components remain `UNAVAILABLE_BLOCKING`; none is serialized as zero. The
complete sparse and matrix-free block APIs fail closed. The sole continuation
is `C116/ICHO2`.
