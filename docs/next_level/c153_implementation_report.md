# C153/HQCDMATCHFB implementation report

Status: `C153_C152_SOURCE_DERIVED_COMPONENTWISE_FINITE_BASIS_MATCHING_AUTHORITY_READY`.

C153 publishes componentwise matching records for quark field, signed quark
mass, transverse gluon field, qg vertex dressing, and QCD coupling. Every
record carries an explicit target scheme, C43 gauge, (N_f), scale,
kinematics, common-IR identity, regulator scheme, and perturbative order.

The six requested arXiv authorities are hash/locator locked as
methodological or target/conversion authorities without consuming numeric
inputs. Common-IR differences are retained symbolically; finite-cell, HO,
UV, Fock, zero-mode, boundary, spectral-distance, and perturbative remainder
terms remain separate. RI/SMOM, MOMq, and MSbar adapters are gated
individually and no Landau-gauge formula is silently applied to C43.

Conversion, inverse, projected-ratio, round-trip, and cocycle interfaces are
componentwise and fixed-regulator only. K9/K11/K13 are not called a
continuum trajectory. Nullspace and counterterm sensitivity remain
prospective, and no physical input or standard-scheme value is consumed.
The next continuation is `C154/HQCDPHYSINPUT2`.
