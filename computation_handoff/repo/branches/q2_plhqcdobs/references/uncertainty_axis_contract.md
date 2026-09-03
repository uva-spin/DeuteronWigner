# Independent uncertainty-axis contract

The project carries seven distinct uncertainty axes:

- wave-function choice;
- internal LF quadrature;
- external interpolation/grid;
- Fourier/tensor transform;
- PDF/TMD fit members;
- evolution/profile choice;
- nuclear-mechanism response.

`src/deuteron_wigner/uncertainty_axes.py` assigns every ensemble exactly one
axis, a statistical interpretation, stable member IDs, a central member,
source, and the dimensions across which member identity is correlated.

A `SeparatedUncertaintyLedger` refuses to produce a joint covariance. Such a
covariance is permitted only through `JointProbabilityInput`, which requires
an explicit set of axes, parameter labels, source, and a finite symmetric
positive-semidefinite covariance matrix. The project currently has no such
published joint probability across wave, fit, evolution, and nuclear inputs,
so the refusal is the physically correct result.

This does not prevent side-by-side sensitivity or uncertainty bands. It
prevents those bands from being combined as independent Gaussian errors or
as a sample covariance over heterogeneous scenario members.

Reproduce the seven-axis catalog and refusal evidence with:

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python \
  scripts/audit_uncertainty_axes.py
```

Artifact: `outputs/validation/uncertainty_axes.audit.json`.

