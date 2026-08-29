# ADR 216: Apply modified-delta damping inside the finite Wilson operator

Status: draft; implemented as an analytic C35/S0C operator oracle and no-go.

## Question

How does the modified-delta regulator act on a finite Wilson segment, and what
gauge claim is permitted at finite delta?

## Decision

For mode frequency `omega`, positive `delta`, and length `L`, place damping
inside the path integral and use

```text
I_L = [exp((-delta+i*omega)*L)-1]/(-delta+i*omega),
I_infinity = 1/(delta-i*omega).
```

Record the explicit finite-delta Ward bulk defect.  Set
`gauge_property_at_finite_delta=False` and
`gauge_property_restored_only_in_delta_limit=True`, following the source's
regulator-removal and power-delta prescription.  Do not call the analytic
damping factor a gauge-complete finite-mode operator.

## Physics basis and alternatives

The source places exponential suppression along the Wilson line and warns
that finite-delta regulated lines do not retain the original Wilson gauge
properties.  Applying damping after integration, treating it as metadata, or
declaring a zero Ward defect by taking the target limit before the finite
calculation would define a different or incomplete regulator.

Classification: source-defined operator action and source-defined gauge
limitation.

## Consequences

- Modified delta can be tested analytically without authorizing a graph sum.
- A positive route needs a gauge-restoring completion or a gauge-complete
  alternative with an operator-level conversion.
- Delta rescaling follows ADR 211.

## Affected evidence

- `ModifiedDeltaDampingOperator`
- `docs/next_level/c35_modified_delta_operator.json`
- `docs/next_level/c35_modified_delta_mode_action_report.json`
- `docs/next_level/c35_vertex_ward_report.json`

## Revision trigger

C36/O4 derives and validates finite-regulator gauge closure for modified delta
or an explicit conversion, including endpoint, boundary, zero-mode, and
remainder terms.
