# Member-level joint-density positivity

`src/deuteron_wigner/joint_positivity.py` audits each member as a complete
target-helicity by parton-spin density matrix. It reports minimum eigenvalues
and violating-point counts without clipping or rejecting fitted members.

The current full-correlator gluon wave-function ensemble contains AV18,
CD-Bonn, NV-Ia, NV-Ib, NV-IIa, and NV-IIb. For proton impulse, neutron
impulse, and their total at nine transverse momenta, the audit covers 162
full `(3,3,2,2)` matrices. All six members are compatible at the declared
\(10^{-10}\) tolerance; the global minimum eigenvalue is
0.11496746205104823.

The interpolated gluon wave envelope is intentionally **not** audited as a
joint density. It stores pointwise named-projection envelopes rather than
correlated member-level matrices, so reconstructing an envelope matrix would
mix extrema from different wave functions. The implementation has an
explicit refusal for both incomplete projection sets and complete named
projections lacking correlated matrices.

Artifacts:

- `outputs/validation/gluon_wave_joint_positivity.json`
- `outputs/validation/gluon_wave_joint_positivity.csv`

The correlated JAMDiFF audit simultaneously replaces \(h_1\) and the
member-matched WW \(h_{1L}^{\perp}\) contribution. All 968 members pass
across six waves, four light flavors, impulse/model totals, and nine
transverse knots; the global minimum eigenvalue is
0.0007710673852289834.

The BPV20 audit reconstructs the full density with every one of 500 Sivers
members. It reports 296 tree-level positivity tensions, with global minimum
-0.047073230070895346, but does not clip, discard, or condition the released
fit because this bound is not scheme independent for the soft-subtracted
evolved TMD.

At \(x_N=0.01,Q=5\) GeV, the default inclusive gluon-shadowing central,
50%-low, and 50%-high members are propagated as complete matrices. All 27
matrix points pass; the minimum eigenvalue is 7.235473394089106.

WP8 joint positivity is verified for every implemented ensemble whose
members define reconstructible correlated full densities. Pointwise
projection envelopes are deliberately outside this claim and retain a
machine-enforced refusal. No unimplemented or nonexistent gluon fit is
silently treated as an audited ensemble.

Additional artifacts:

- `outputs/validation/jamdiff_joint_positivity.json`
- `outputs/validation/jamdiff_joint_positivity.csv`
- `outputs/validation/gluon_shadowing_joint_positivity.json`
- `outputs/parent_tmds/uncertainty/bpv20_replica_positivity.validation.json`
