# C407 complete Python 3.9 compatibility hotfix

- Timestamp: `2026-08-31T22:19:01Z`
- Merged C407 head before hotfix: `eb606e4974de17074d1eee0ed006448acc797602`
- Canonical runtime: `Python 3.9.6`

Two runtime-compatibility defects were repaired: the module-level PEP 604 type alias was replaced with `typing.Union`, and `int.bit_count()` was replaced by a small nonnegative population-count helper based on `bin(value).count('1')`. Neither change alters the mathematical or numerical definition of C407.

Validation: **164 passed, 0 failed**, plus a clean Python 3.9 compile/static audit and a generator smoke run preserving the C407 scientific invariants.
