# First C117 action: exploratory finite-C43 bridge

Status: **Lane-A exploratory implementation; not a physical C117 activation**.

## Purpose

C410 supplies the source-reduced first C117 I2 retained-connected shape

    S^(C410)_(1,K) = -1/2 (B_K^qq + B_K^qg + B_K^gq + B_K^gg)

at K9, K11, and K13. C411 still lacks the source-qualified finite-C43
field/state/wave-packet normalization and RI/SMOM-to-finite-basis mixing
certificate. The exploratory bridge makes those unresolved factors explicit
parameters so a response calculation can proceed without treating a missing
factor as zero or as a physical default.

For caller-supplied nonzero real numbers n_K and m_K, the action is

    D^(exp)_(1,K) = n_K m_K S^(C410)_(1,K).

Here n_K is the residual finite-C43 normalization and m_K is the coefficient
of the only source direction currently available from C410. The four-by-four
C260 container is not interpreted as evidence that generic four-direction
mixing is required. The remaining three source directions stay explicitly
unavailable.

## Conversion ownership

The declared symmetric light-front convention gives

    δM² = 2P⁺δP⁻,   P⁺ = πK/L,   2P⁺ = πK₂/L,

where L is the current executable half-cell length and K₂ = 9, 11, 13. The
helper `pminus_to_m2_factor` evaluates this exact factor only when a caller
supplies L > 0. It is not applied to the C410 shape, whose current source label
is already `GeV^2`; the unresolved question of whether an upstream source
factor has already consumed the conversion remains owned by the strict C411
certificate route.

## Claim boundary and checks

Every exploratory record is marked `EXPLORATORY`, `physical=false`,
`C411_certificate_supplied=false`, and `hamiltonian_activation=false`. The
implementation consumes the live C410 matrices, preserves the C410 -1/2,
keeps g_s² factored, and checks dimensions, finite inputs, Hermiticity, sparse
action, and matrix-free agreement at all three resolutions. It does not select
c_C117,1, a physical state/current, a fit, a response rank, or a GTMD
observable.

The next scientific step remains the source-level normalization derivation and
the K9 state-to-observable response. This bridge is a usable exploratory
substrate for that calculation, not evidence that the C411 physical gate has
closed.
