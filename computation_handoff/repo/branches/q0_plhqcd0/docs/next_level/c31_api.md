# C31/B1A API

The source-closure contract is implemented in
`deuteron_wigner.bridge.b1a.core` using immutable dataclasses.

- `MicroscopicBareOperatorId` and `MicroscopicRegulatorId` prevent a regulated
  overlap from being labeled a renormalized TMD.
- `RenormalizationComponent` records source authority, order, and blocking
  status for every UV, soft, rapidity, regulator, and counterterm component.
- `RenormalizedTMDDefinition` keeps the project and ART25 definitions distinct.
- `FiniteTMDSchemeTransformation` stores the finite operator relation, inverse,
  hard companion, order, member independence, and remainder.
- `ScaleMap` distinguishes optimal-boundary choice, ζ prescription, and
  two-scale evolution from operator-scheme conversion.
- `MatchingCapability` and `C31BridgeExecutionGate` require all UV, rapidity,
  soft, IR, gauge, and state-independence gates before bridge execution.

The API contains no numerical fallback, fit, likelihood, optimizer, inference,
process, or production route.
