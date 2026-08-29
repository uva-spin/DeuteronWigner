# ADR-002: Separate Amp, Dens, Match, Red and Proc maps

Status: proposed for C1

Decision: every formal map declares exactly one class, typed domain/codomain,
and compatibility contract. Cross-class composition requires a named bridge.
Density maps additionally declare positivity/complete-positivity properties;
matching maps declare input/output schemes and perturbative order.

Rationale: amplitude composition, density reduction, QCD matching, correlator
reduction and process factorization obey different mathematical laws. Treating
all as array functions permits invalid orderings and duplicate matching.

Consequence: current functions are wrapped first. Their execution order and
numerical values remain unchanged. Negative tests reject cross-class and
domain/codomain mismatch.
