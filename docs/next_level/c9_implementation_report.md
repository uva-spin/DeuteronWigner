# C9/H2 implementation report

C9 enlarges the isolated microscopic state to the direct sum
\(\mathcal H_{qqq}\oplus\mathcal H_{qqqg}\). The three tower points have
dimensions \(4+6\), \(7+10\), and \(10+14\). Every \(qqqg\) state records
positive longitudinal support, gluon helicity, orbital label, antisymmetric
three-quark identity, CM policy, and one of the two independent
octet-times-adjoint singlet multiplicities.

H2-PLAN-A uses resolution-refitted induced confinement; H2-PLAN-B uses zero
confinement. Both use the same reduced canonical quark--gluon vertex and its
generated adjoint, instantaneous-fermion and instantaneous-gluon partners,
sector-indexed mass/vertex counterterms, and a typed truncation discrepancy.
The C8 effective color-spin route is read-only and mutually exclusive.

The sector-3 counterterm is solved nonlinearly at every resolution to retain
the validation pole \(M^2=0.7744\ {\rm GeV}^2\). Sector-4, vertex,
instantaneous, and coupling parameters flow explicitly. The Jacobian exposes
one deliberate null direction rather than hiding it with another fitted
observable. A second vertex point, nonzero-transfer currents, gluon
probability, and rotational diagnostic remain holdouts.

The Hamiltonian-owned current contains valence, \(qqqg\)-attachment,
instantaneous, vertex-counterterm, and shared-normalization pieces. A
commuting-generator Ward benchmark closes from propagating, two
instantaneous, and counterterm contributions and fails with a signed residual
when any is omitted. This is not a non-Abelian Slavnov--Taylor proof.

Dense, matrix-free Krylov, and coupled-sector TTN calculations are compared.
The TTN contains an explicit Fock-root edge and retains color outer
multiplicity. Nested Rayleigh--Ritz spaces obey the variational bound, while
low rank misses \(qqqg\) probability and gluon/OAM information. Full bond
reproduces the exact state.

The exported finite-basis ledgers close probability, longitudinal momentum,
and canonical \(J^z\). They are regulator- and truncation-dependent
microscopic diagnostics, not PDFs, GTMDs, TMDs, or a matched QCD spin
decomposition.

Finite Feshbach elimination records the induced valence component and a
nonzero orthogonal remainder. Thus explicit \(qqqg\) is equivalent only to
the induced operator plus that remainder. The Wilson adapter reuses C5/C6
path/cut/color/link concepts, returns exactly zero absorption for a discrete
off-shell spectrum, ignores numerical epsilon as physical support, and can
activate only under a separately declared spectral rule. Its highest status
is `MICROSCOPIC_WILSON_INPUT_INTERFACE_VALIDATED`, never `WILSON_READY`.

C9 covers 157 stable requirements and detects 83 ordered negative
injections. It remains `C9_H2_VALIDATION_ONLY` and has no path to production,
nuclear, evolution, process, or inference roots.
