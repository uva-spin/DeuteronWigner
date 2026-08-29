# ADR 155: Freeze the source-audited ART25 distribution definition

**Decision.** Use the native rank-zero proton `get_uTMDPDF` b-space object,
with explicit `mu=Q`, `zeta=Q^2`, audited flavor indices, and `f` rather than
`x f`. Preserve the native ART25 scheme unchanged.

**Reason.** A bridge is meaningful only if the external object is identified
from the executed source path rather than inferred from a TMD name.
