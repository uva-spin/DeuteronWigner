# Common controlled-limit audit

`src/deuteron_wigner/controlled_limits.py` evaluates six limits through the
actual retained-spin light-front parent and named projectors:

1. a zero neutron boundary makes all 18 spin-1 quark TMDs equal the retained
   proton contribution;
2. a zero proton boundary does the neutron analogue;
3. a pure-S radial input makes the SD, DS, and DD parent correlators vanish;
4. at \(y=1/2,p_T=0\), Melosh rotations equal the identity/no-Melosh result;
5. exact-zero quark mechanism inputs leave every quark correlator component
   unchanged;
6. an empty gluon mechanism ledger leaves the complete `(3,3,2,2)` parent
   unchanged.

The analytic fixture assigns a distinct deterministic value to every
spin-half nucleon TMD component. The resulting parent comparison uses the
public 18-name spin-1 correlator basis, preventing a representative-function
test from standing in for the complete basis.

Exact-isospin and controlled-CSB behavior for \(u,d,\bar u,\bar d\) remains
covered by `tests/test_nucleon_inputs.py` and `tests/test_csb_inputs.py`.

Reproduce with:

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python \
  scripts/audit_controlled_limits.py
```

The artifact is `outputs/validation/controlled_limits.audit.json`. All six
checks currently have zero maximum absolute residual against a
\(2\times10^{-11}\) tolerance.

