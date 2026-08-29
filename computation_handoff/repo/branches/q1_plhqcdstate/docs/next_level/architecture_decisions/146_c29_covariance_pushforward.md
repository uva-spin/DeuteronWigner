# ADR 146: covariance pushforward

Decision: linear maps act on the exact anomaly factor; nonlinear maps evaluate
all 642 joint members and recenter empirically. No marginal reshuffling,
diagonal replacement, ridge, or clipping is permitted. This preserves the
source covariance and visible null space.
