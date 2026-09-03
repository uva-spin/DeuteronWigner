# ADR 020: distinct quark and gluon local moments

Status: accepted.

Positive-x quark and antiquark vector currents use the net combination
`integral(H^q - H^qbar)`. Quark momentum uses the x-weighted sum. The gluon
benchmark stores `H^g=xg`, so its energy-momentum moment is `integral H^g`.

A gluon vector-number current, a quark convention applied to `H^g=xg`, or a
gluon convention applied to a quark fails closed. No normalization may be
inserted after reduction to force closure.
