# C401 science-lock amendment: C128 longitudinal-partition defect

**Baseline science lock:** `C401_C396_REDUCED_NUMERICAL_FORWARD_MAP_SCIENCE_LOCK_V1.md`
**Accepted repository baseline:** `ada80920fb51617333c9b87a40d6538a0b0de915`
**Amendment status:** `SOURCE_FORMULA_ROUTE_RETAINED_HISTORICAL_C128_NUMERIC_ROUTE_SUPERSEDED_FOR_MASS_DIRECTIONS`

## Finding

The first C401 implementation audit compared the historical C128 numerical
partition helper with the exact C45/C47 positive-mode partition construction.
For resolution label `K2=N` with physical longitudinal resolution
\(K=N/2\), the source-qualified partitions satisfy

\[
  k_q + k_g = K,
  \qquad
  x_q = \frac{k_q}{K},
  \qquad
  x_g = \frac{k_g}{K},
  \qquad
  x_q+x_g=1.
\]

The historical private helper `free2.core._partitions` falls back to

\[
 k_q^{\rm hist}=\frac{N-2i-1}{2},\qquad
 x_q^{\rm hist}=\frac{N-2i-1}{N},\qquad
 x_g^{\rm hist}=\frac{2(i+1)}{N}.
\]

For \(i=0,\ldots,(N-3)/2\), this gives

\[
 k_q^{\rm hist}+k_g=K+\frac12,
 \qquad
 x_q^{\rm hist}+x_g=1+\frac1N.
\]

The correct C47 quark mode and fraction are smaller by \(1/2\) and \(1/N\),
respectively.  The historical gluon mode and gluon fraction are correct.

## Consequences

The defect materially changes the historical C128 quark-mass derivative
\(\partial M_0^2/\partial m_q^2\) on every qg basis state and also changes
the qg transverse kinetic denominator.  It does not materially change
\(\partial M_0^2/\partial m_g^2\); any byte-level differences in the latter
at K11/K13 are floating-point reciprocal-order roundoff below the declared
comparison tolerance.

This is an implementation defect in a historical numerical helper.  It does
not alter the action-level C43 formula or the exact C45/C47 partition
authority.  It also does not retroactively change the accepted claim tier of
the C144 smoke path: C144 uses an explicitly nonphysical ID-derived fixture
rule and does not numerically evaluate the C128 partition fractions.  The C144
path remains diagnostic rather than source-faithful.

## Amended acceptance rule

The V1 phrase

> finite differences of the source C128 free operator agree

is replaced by:

> finite differences of an independent implementation of the C43/C47 source
> mass functional agree with the analytic mass-direction operators at
> multiple step sizes; the historical C128 numerical implementation is
> compared separately and its quark-fraction mismatch is exposed.

C401 must not silently edit or re-root C128.  It introduces a versioned
adapter using the exact C47 fractions while retaining C128 only for the
accepted q/qg direct-sum dimensions and partition-major block ownership.

## Scope and nonclaims

This amendment authorizes the first six K-local mass-direction apply paths.
It does not certify the full historical C128 free operator, whose qg
transverse kinetic term remains affected.  It does not select a mass value,
fix a counterterm, evaluate physical rank, or activate the C396 Hamiltonian.
