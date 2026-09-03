# C3 analytic-pilot API

`ZeroSkewnessFrame` constructs compatible incoming, average, and outgoing
`MomentumFiber` objects. `IntrinsicConfiguration` validates support, closure,
constituent identity, active slot, sector, member, and phase.

`SymmetricXiZeroRecoil.apply` is the single recoil authority and returns a
typed `RecoilResult`. `OverlapKernel` is an `AMP` map with diagonal sector,
explicit active and spectator rules, complete operator and fiber identities,
and Wilson order zero. `AnalyticOverlapEvaluator` consumes every pilot state
and returns an immutable, non-production `OverlapResult`.

States are `PointState`, `GaussianScalarState`, `SpinorOAMState`, and
`ThreeQuarkColorState`. `PilotReductionBridge` uses a separate C2-native
validation registry. `pilot_provenance_graph` and `require_isolated` prove
that pilot ancestry is unreachable from accepted production.
