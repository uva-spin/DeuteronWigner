# C401 — first numerical C396 mass-direction implementation

Status: `C396_FIRST_SIX_K_LOCAL_NUMERICAL_BINDINGS_READY_DIAGNOSTIC_ONLY`
Accepted baseline: `ada80920fb51617333c9b87a40d6538a0b0de915`
Physical fit: forbidden
Physical rank: not evaluated
Activation: not ready

## Implemented numerical directions

C401 implements two source-owned mass-squared derivative directions at each of K9, K11, and K13:

\[D_{q,K}=\partial H_K/\partial\mu_{q,K}^2,\qquad D_{g,K}=\partial H_K/\partial\delta\mu_{g,K}^2.\]

On the q sector their exact values are 1 and 0.  On each qg longitudinal partition they are \(1/x_q\) and \(1/x_g\), with fractions taken from the exact C45/C47 partition authority.

The operator inventory contains **6** complete K-local apply rows. Each direction has a serialized COO record, an actual SciPy CSR representation, a SciPy LinearOperator, and an independent matrix-free block action.

## Resolution records

| Label | Exact K | Nmax | bHO | q dim | qg dim | direct dim |
|---|---:|---:|---:|---:|---:|---:|
| K9 | 9/2 | 8 | 0.4 GeV | 6 | 1344 | 1350 |
| K11 | 11/2 | 10 | 0.45 GeV | 6 | 2700 | 2706 |
| K13 | 13/2 | 12 | 0.5 GeV | 6 | 4752 | 4758 |

## Historical C128 partition defect discovered

The historical private C128 partition helper does not satisfy the C47 identities for the quark mode: it shifts \(k_q\) by \(+1/2\), \(x_q\) by \(+1/K_2\), and gives \(x_q+x_g=1+1/K_2\).  The gluon fraction is unchanged.

Affected resolutions: K9, K11, K13.  The historical C128 files were not edited.  C401 uses a versioned source-corrected adapter and records the mismatch explicitly.

This defect affects the historical qg quark-mass derivative and qg transverse kinetic denominator. It does not materially affect the historical gluon-mass derivative.

## Validation

- Sparse/CSR/LinearOperator/matrix-free route agreement: `True`.
- Independent source-formula finite differences: `True`.
- Historical quark-fraction defect exposed: `True`.
- Historical gluon fraction unchanged at material tolerance: `True`.

## C396 frontier update

The C400.S2 inventory contained 57 symbolic K-local rows and zero complete numerical apply paths. C401 now records **6** complete numerical apply paths.  The full C396 forward map remains unavailable.

The next source-ordered operator frontier is `ct_sector`, followed by the four C117 insertions and then owner-by-owner classification of the nine source-null directions.

## Scientific boundary

No physical mass, counterterm, state, current, covariance, likelihood, rank, or activation decision is made in this implementation.
