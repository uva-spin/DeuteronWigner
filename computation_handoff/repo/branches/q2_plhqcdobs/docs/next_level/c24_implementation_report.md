# C24/P1 source-qualification implementation report

C24 starts from exact commit
`0f6495107effda70ca406e8a44e365f3a8080198`; the C23 baseline reproduced with
1,095 passing tests before implementation. The scientific C22Q ancestor is
`a1527fec32c07865de34d14dc1345ca9e816fac8`.

## What was implemented

The new `process.p1` layer provides immutable source locks, one authoritative
thirteen-gate source evaluator, a separate six-gate physical-input evaluator,
complete failed-gate diagnostics, minimal T-even family audits, NN-only scope
enforcement, and 880 ordered negative injections. It is validation-only and
has no route to likelihood, inference, posterior, or production code.

Sixteen required primary papers, the Zenodo 15006449 metadata, the exact
ARTEMIDE 3.01 archive, and Zenodo 20638667 metadata for the current 3.03
comparison were preserved under `data/raw/c24_sources` and SHA-256 audited.
The 3.01 archive's upstream MD5 is also locked. ARTEMIDE 3.03 was audited as a
distinct current release and was not substituted.

The unpolarized quark Born coefficient is source-qualified at its declared LO
scope from Eq. (4.8) of arXiv:1111.4996, with an explicit delta endpoint,
x-space and Mellin checks, and a supersession link to—not an overwrite of—the
C22 prototype. LL, helicity, transversity, and gluon coefficient records remain
operator-specifically unavailable. This does not qualify a process chain.

## Qualification result

The process tier remains 438 analytic eligible, 102 not process eligible, 0
source eligible, and 0 physical eligible. This is the scientifically required
result: the ARTEMIDE release does not contain the ART25 constants or its 500
declared replicas; no compatible CS covariance, two-hadron member bundle, or
TMDPDF/TMDFF joint-member bundle is reproducible from the preserved release.
CuTe-MCFM 10.3 and SIDIS N3LO ancillaries are not locked locally.

DY and SIDIS candidates were fully gate-audited but not executed. No
source-level W+Y residual is reported because constructing one would mix
incomplete or synthetic inputs. The C23 analytic W+Y records remain immutable.
Inclusive b1, tagged DIS, and rank-0/rank-2 heavy-pair DIS have explicit
unavailable/conditional decisions. NN is never promoted to a complete
deuteron matched total.

## Regression and next action

The production registry remains 216 routes and all eight authoritative
artifacts retain their exact hashes. Rebuilds are deterministic. The exact
next task is ART25 ancillary closure: acquire the official constants plus 500
correlated members, lock their provenance, reproduce frozen DY and SIDIS
points with ARTEMIDE 3.01, and only then re-run the source gate.
