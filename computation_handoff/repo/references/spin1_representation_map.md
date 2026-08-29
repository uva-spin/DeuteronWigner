# Spin-1 representation map

## Physical Hilbert spaces

The target space is the spin-1 light-front helicity space
\(\mathcal H_D=\mathrm{span}\{|+1\rangle,|0\rangle,|-1\rangle\}\).
Quark leading-twist operators act in a two-state quark-helicity space;
gluon operators act in the two-dimensional physical transverse-polarization
space. The stored parent correlators are therefore:

- quark: one \(3\times3\) target matrix for \(\gamma^+\), one for
  \(\gamma^+\gamma_5\), and two for
  \(i\sigma^{i+}\gamma_5\);
- gluon: a \(3\times3\times2\times2\) joint target/transverse-gluon matrix.

These are computational objects in `Spin1QuarkCorrelator` and the gluon
correlator arrays. Named TMDs are coefficients of their covariant basis;
they are not independently generated distributions.

## Target irreducible decomposition

`spin_one_basis()` decomposes Hermitian target matrices as

\[
\mathbf 1\oplus L\oplus(T_x,T_y)\oplus LL
\oplus(LT_x,LT_y)\oplus(TT_x,TT_y).
\]

The dimensions \(1+1+2+1+2+2=9\) span all Hermitian \(3\times3\)
matrices. They correspond to unpolarized, vector-longitudinal,
vector-transverse, tensor-longitudinal, mixed tensor, and transverse tensor
target polarization. `project_matrix()` uses trace-orthogonal contraction;
the quark/gluon Gram projectors independently reconstruct the same
coefficients.

The project `LL` matrix is opposite in sign to the physical Trento
\(S_{LL}\) convention. The explicit adapters for \(f_{1LL}\) and
\(h_{1LL}^{\perp}\) are therefore required and tested. This is a convention
map, not a model sign choice.

## Transverse geometry

The transverse plane carries \(SO(2)\). `symmetric_traceless.py` constructs
rank-\(r\) irreducible harmonics through \(r=4\). A named coefficient of
rank \(r\) multiplies the corresponding harmonic and has a physical
modulation proportional to \((k_T/M_D)^rF_r\). Positive-rank coefficients
can be finite at the origin only as basis coefficients; their physical
tensor modulation vanishes there.

The epsilon-rotated harmonics distinguish polar and axial structures.
This is essential for the quark \(i\sigma^{i+}\gamma_5\) convention and
exposed the corrected rank-three \(h_{1TT}^{\perp}\) rotation. For gluons,
the transverse \(2\times2\) matrix decomposes into trace (unpolarized),
antisymmetric/circular, and symmetric-traceless/linear polarization.

## Discrete symmetries and gauge links

- Hermiticity is target-matrix Hermiticity and initial/final interchange
  off forward.
- Parity is the tested light-front helicity reflection, not a bare
  two-dimensional \(k_T\) reflection.
- Time reversal relates future- and past-pointing gauge links. Exactly nine
  quark functions change sign. Gluon T-odd entries remain explicit open
  mechanism slots; no common phase is assigned.
- At fixed nonzero \(k_T\), the gluon TT sector has a structural
  \(f_{1TT}-h_{1TT}^{\perp}\) identifiability combination. The software
  exposes this combination rather than imposing a prior to split it.

## Composition and computational role

Proton, neutron, wave-component, and nuclear-mechanism correlators form a
typed direct sum before observable projection. This representation
organization provides concrete benefits:

1. symmetry acts once on parent matrices rather than independently on every
   named TMD;
2. mechanism sums reconstruct exactly at matrix level;
3. positivity is tested as eigenvalue positivity in the joint spin space;
4. Gram rank/condition checks expose unidentifiable combinations;
5. transverse-rank transforms select \(J_r\), preventing use of \(J_0\) for
   rank-one or rank-two functions.

No nontrivial topology is currently used. The implemented forward central
parents have no demonstrated winding, gauge patch, bundle obstruction, or
global sign ambiguity. Introducing topological terminology without such an
object would not constrain the physics. PennyLane is likewise unnecessary
for these finite matrices because analytic Clebsch--Gordan and eigenvalue
calculations already provide exact benchmarks; it becomes relevant only if
a new many-sector quantum-state parameterization yields an independently
testable correlation structure.

## Authoritative files and tests

- `src/deuteron_wigner/spin.py`
- `src/deuteron_wigner/symmetric_traceless.py`
- `src/deuteron_wigner/quark_correlator.py`
- `src/deuteron_wigner/gluon_correlator.py`
- `src/deuteron_wigner/registry.py`
- `tests/test_quark_correlator.py`
- `tests/test_gluon_correlator_basis.py`
- `tests/test_quark_symmetries.py`
- `tests/test_joint_spin_positivity.py`

