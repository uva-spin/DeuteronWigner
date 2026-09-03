# ADR 211: Fix the normalized light-front convention and delta rescaling

Status: draft; implemented as an exact C35/S0C convention oracle.

## Question

Which null-vector normalization, plus/minus components, Fourier sign, and
rapidity-parameter rescaling govern C35 objects?

## Decision

Fix metric `(+---)`,

```text
v+/-=(v0+/-v3)/sqrt(2),
n=(1,0,0,1)/sqrt(2),
nbar=(1,0,0,-1)/sqrt(2),
n.nbar=1,
n.k=k-,  nbar.k=k+,
k^2=2*k+*k--kT^2,
A(x)=integral[d4k/(2pi)^4] exp(-i k.x) A(k).
```

Under `n -> lambda*n` and `nbar -> lambda^-1*nbar`, require
`delta- -> lambda*delta-` and `delta+ -> lambda^-1*delta+`.  The product
`delta+*delta-` is invariant.  Convert the source's `n.nbar=2` delta
parameters to the project convention by dividing each by `sqrt(2)`.

## Physics basis and alternatives

This convention follows directly from the declared light-front component
definition and removes the inherited `sqrt(2)` ambiguity.  Alternatives with
`n.nbar=2` or an opposite Fourier phase are legitimate only as separately
typed conventions with explicit conversion; silent mixing is forbidden.

Classification: exact kinematic and convention constraint.

## Consequences

- Propagator, on-shell, Wilson-line pole, and modified-delta identities have
  one normalization.
- Line-to-pole signs remain derived from paths and Fourier convention.
- The convention oracle does not imply a gauge-mode basis or gauge closure.

## Affected evidence

- `LightFrontConvention` and `RapidityRegulatorRescaling` in
  `src/deuteron_wigner/bridge/s0c/core.py`
- `docs/next_level/c35_light_front_convention.json`
- `docs/next_level/c35_null_vector_regulator_rescaling.json`
- convention, rescaling, and injected-sign tests

## Revision trigger

Only an explicit versioned convention migration with analytic conversions for
all Wilson, rapidity, coordinate, matching, and historical regression objects
may supersede this choice.
