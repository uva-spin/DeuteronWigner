# ADR 212: Separate exact real and virtual charts from an executable field basis

Status: draft; implemented as exact/geometric C35/S0C oracles.

## Question

How should real on-shell and virtual loop momentum coordinates be represented
without overstating their physical completeness?

## Decision

Use the real massless chart

```text
k+=kappa*exp(y)/sqrt(2),
k-=kappa*exp(-y)/sqrt(2),
kx=kappa*cos(phi), ky=kappa*sin(phi),
dPi=kappa*dkappa*dy*dphi/[2*(2pi)^3].
```

Use independent `(k+,k-,kx,ky)` for virtual geometry with
`d4k/(2pi)^4` and denominator `2*k+*k--kT^2+i0`.  Label the real chart
`EXECUTABLE_GEOMETRIC_CHART_NOT_GAUGE_MODE_BASIS` and the virtual contour
`UNRESOLVED_BLOCKING_NO_REGULATOR_IDENTICAL_CONTOUR`.

## Physics basis and alternatives

The real chart exactly solves positive-energy massless kinematics; the virtual
loop must retain independent components.  Reusing an on-shell chart for a
virtual loop or inferring a contour from a coordinate name would discard pole
information and is rejected.

Classification: exact real kinematics and virtual coordinate geometry;
physical virtual integration remains unresolved.

## Consequences

- Real mass-shell and Jacobian residuals can be tested exactly.
- No physical virtual cell, cut assembly, or graph coefficient is claimed.
- A later gauge realization may reuse the charts but must add modes,
  contours, partitions, and quadratures.

## Affected evidence

- `RealSoftCoordinateChart` and `VirtualSoftCoordinateChart`
- `docs/next_level/c35_real_coordinate_chart.json`
- `docs/next_level/c35_virtual_coordinate_chart.json`
- `docs/next_level/c35_real_virtual_measure_report.json`

## Revision trigger

A versioned replacement chart is required only if a selected gauge-complete
regulator cannot use these coordinates; it must preserve analytic measure and
pole-conversion tests.
