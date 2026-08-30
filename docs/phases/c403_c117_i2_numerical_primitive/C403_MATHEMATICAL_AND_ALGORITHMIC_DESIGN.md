# C403 Mathematical and Algorithmic Design

## 1. Implemented package

```text
src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/
    axis.py
    spatial.py
    bindings.py
    __init__.py
```

The package is intentionally a versioned descendant adapter. It does not edit or re-root C45, C47, C62, C114, C115, C116, C117, C119, C124, C400.S2, or C401.

## 2. Finite-axis algorithm

### Inputs

- resolution label `K9`, `K11`, or `K13`;
- species `QUARK` or `GLUON`;
- C47 positive longitudinal partition;
- C45 one-particle HO label `(n,m)`;
- helicity `-1` or `+1`;
- fundamental or adjoint color index.

### Ordering

The candidate member rank uses the C124-compatible order:

```text
partition → transverse HO mode → helicity → color
```

The candidate axis retains both exact statuses:

```text
ADMITTED_MEMBER
REJECTED_NOT_APPLICABLE
```

No candidate is removed by a floating magnitude threshold.

### Support decision

```python
shell = 2*n + abs(m)
admitted = shell <= Nmax - 2
```

The highest C45 one-particle shell `Nmax-1` is exactly rejected. For admitted modes, `witness_record()` evaluates the exact C62 coefficient and compares it symbolically with the closed-form witness. For rejected modes, the product-shell impossibility is the exact proof and no numerical C62 call is required.

### Pagination

`member_page()` exposes bounded pages without materializing every color/helicity member at once. `member_by_rank()` and `member_rank()` provide deterministic rank identity.

## 3. Spatial-kernel algorithm

The external matrix basis in C403 is the C47 intrinsic/relative qg HO basis.  The one-quark external C45 basis and full target-sector embedding remain outside this primitive.  No omitted external-sector matrix element is classified as zero.

### Exact radial moments

`_laguerre_coefficients()` returns exact `Fraction` coefficients for generalized Laguerre polynomials. `_convolve()` multiplies the four finite polynomials. `radial_moment_fraction()` then applies exact factorial moments under `e^{-2z}`.

### Element evaluator

`i2_spatial_element()` validates all three modes against the admitted shell and returns the real analytic element. The exact angular rule is applied before the radial calculation.

### Independent quadrature

`i2_spatial_element_quadrature()` uses SciPy generalized Gauss--Laguerre nodes and weights after `t=2z`. The code path is independent of the exact polynomial convolution.

### Sparse and matrix-free routes

- `single_member_kernel_csr()` constructs a CSR representation.
- `apply_single_member_kernel()` reevaluates analytic elements directly and does not multiply by the cached dense/CSR matrix.
- `weighted_spatial_kernel_csr()` and `apply_weighted_spatial_kernel()` require an explicit nonempty finite weight map.

Canonical duplicate modes in the weight mapping are rejected even when supplied once as an `HOMode` and once as a tuple. No default weighting exists.

## 4. Evidence generation

`tools/generate_c403_c117_i2_numerical_primitive.py` generates:

```text
input_freeze.json
axis_summary.json
support_theorem_certificate.json
support_witness_rows.json
spatial_kernel_inventory.json
spatial_kernel_validation.json
c396_coordinate_binding_inventory.json
binding_update_summary.json
scientific_nonclaims.json
blocker_or_completion.json
release.json
implementation_report.md
generation_result.json
```

`generation_result.json` is excluded from its own artifact hash list. External output directories are normalized to `<EXTERNAL_OUTPUT_DIRECTORY>` so clean-build comparisons do not depend on absolute paths.

## 5. Validation design

### Exact support validation

Every partition/species/mode row is checked with exact SymPy algebra or an exact shell-impossibility proof. The certificate must report:

```text
row_count = 1774
admitted_witness_rows = 1466
rejected_shell_rows = 308
all_exact_matches = true
maximum_numeric_residual = 0
```

### Spatial validation

- exact ground-state identity;
- exact radial cancellation case;
- analytic versus independent quadrature on nine representative internal modes;
- sparse versus independent matrix-free action;
- Hermiticity and PSD for all 139 single-member matrices;
- `b_HO^2` scaling;
- fail-closed aggregate weights.

### C396 boundary validation

The C401 57-row inventory is overlaid, not replaced. Only the three `c_C117_1` rows receive primitive paths. Their `numerical_apply_path` remains `null`, the complete path count remains six, and all coefficients remain unselected and not zeroed.

## 6. Complexity

Let `d_K` be the admitted external HO dimension and `r_K=d_K` the number of admitted internal modes. Dense construction is `O(r_K d_K^2)` across an inventory, with maximum `d_K=66`. This is small enough for exhaustive Hermiticity/PSD checks at the retained K values.

The full color/helicity member axis is exposed by rank/page rather than materialized in memory. Exact support verification scales with partition count times species count times candidate transverse modes and contains 1774 rows at the retained resolutions.

## 7. Safety and scope

The implementation does not import:

- C64 runtime status arrays;
- C80 contact-kernel values;
- C144 fixture values;
- physical couplings;
- physical coefficients;
- minimum-norm representatives.

The only numerical outputs are source-derived support witnesses and transverse-HO spatial primitives. Complete current-current assembly remains fail-closed.
