# ADR-004: Hierarchical quark/gluon-to-nuclear matching

Status: proposed for Stage A

Decision: encode the hierarchy as explicit composable maps:
renormalized partonic operator → nucleon matrix element → LF nuclear amplitude
→ positive nuclear correlator/response → reduction → process observable.
QCD scheme matching and nuclear composition remain distinct map classes.

Rationale: scale separation is physical. Nuclear impulse, off-shell,
shadowing, meson and non-nucleonic mechanisms cannot substitute for missing
partonic matching, nor may one mechanism silently replace another.

Consequence: preserve the accepted response ordering exactly. A provenance
complex records additions, replacements, exclusions and required inputs.
Double application of matching or nuclear response is a type/provenance error.
