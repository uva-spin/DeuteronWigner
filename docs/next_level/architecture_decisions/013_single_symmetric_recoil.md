# ADR-013: One symmetric-xi=0 recoil authority

Status: accepted for C3

`SymmetricXiZeroRecoil` is the sole pilot implementation of active and
spectator intrinsic shifts. Benchmarks and overlap evaluators consume its
result and do not reproduce formulas. The map declares a unit Jacobian and is
tested for closure, physical transfer assignment, inversion, forward identity,
and permutation covariance.
