# C4 normative-source integration audit

After C4’s initial completion, the authoritative TeX sources for Volumes 0,
I, II, and III became available. They were read and mapped back onto every C4
object, benchmark, route, and negative test. Volume V was inspected only for
interface awareness because matching and evolution are outside C4. Volume 0
and Volume IV TeX remain unavailable.

The audit confirmed the central C4 construction: explicit positive-x
antiquarks, explicit-gluon sectors, empty-active-set zero theorems, the single
symmetric recoil map, a diagonal adjoint gluon core without physical `f/d`
assignment, separate quark and gluon moments, honest regulated routes, and
Feshbach explicit-versus-induced exclusion.

The Volume 0 audit confirms that C4 keeps amplitude, matching, and reduction
maps distinct, uses decorated momentum fibers and path identities, and treats
route equality as a regulated validation square rather than nominal physical
equality. Its current provenance representation is the required typed graph
with explicit alternatives, exclusions, and remainder nodes; it is not yet a
general executable cellular 2-complex.

Four numerical/API gaps and one documentation/provenance gap were corrected:

1. `ProductGaussianState` now has the analytic normalization appropriate to
   the `n-1` independent intrinsic transverse momenta. The closure quadratic
   form has determinant `n`, and every sector’s normalization oracle returns
   one.
2. Every gluon parent now records an ordered two-link identity and explicit
   `DIAGONAL_ADJOINT` color status.
3. Route results now distinguish their regulated analytic status from the
   missing matching morphisms. TMD routes record UV and rapidity/soft matching;
   GPD, PDF, and current routes record link-shortening and UV matching.
4. The gluon trace, antisymmetric-helicity, and symmetric-traceless
   polarization projectors are executable typed operations with a matrix
   reconstruction test.
5. The C4 source audit now records explicitly that its replacement edges and
   remainder nodes instantiate the needed finite benchmark relation but do
   not constitute the complete Volume 0 `Provenance2Complex`.

The machine-readable evidence is
`c4_normative_source_integration.json`. Historical baseline records were not
rewritten: they correctly state that the volumes were unavailable during the
initial C4 run.

C4 remains a validation implementation of Volume II Benchmarks E--F and
common regulated route closure. It does not satisfy or claim the complete
Volume II predictive-microscopic acceptance list, which additionally requires
a solved and converged microscopic Hamiltonian, complete twist-two GTMD
projectors, Wigner/OAM/spin-orbit routes, physical matching, and predictive
observables.
