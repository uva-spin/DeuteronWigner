# Native DataProcessor CDF1 diagnostic

## Outcome

The public `VladimirovAlexey/artemide-DataProcessor` repository provides enough
information for an unambiguous, author-independent native CDF1 diagnostic. The
current public checkout is commit `9f9dda71b69dd26e288be189a396736827cfeed3`
on `master`. The repository contains explicit ART25 history at commit
`761f3fcdd3701c5cf69e822f9ffbbd5db394fc58` (`ART25 update`), including the
dataset list and cut function used here.

The public CDF1 file and the separately supplied copy are byte-identical, with
SHA-256 `c0a178d9579017a7de91abf63df667d1bb3009253ce15b56fe428d32fc430c81`.
Its file history consists of the initial 2020 commit and the 2024 data-library
update. It was loaded only through `DataProcessor.DataSet.LoadCSV`.

## Dataset and ART25 selection

The native loader returns `CDF1`, reference `hep-ex/0001021`, process type DY,
50 points, one 3.9% normalization error, one uncorrelated error per point, no
point-to-point correlated errors, and `isNormalized=False`. Complete metadata
for every point is in `c27_cdf1_dataset_manifest.json`.

The public ART25 `cutFunc` retains 33 points, `CDF1.0` through `CDF1.32`. This
is therefore an exact application of the public ART25 selection, not a guessed
cut and not the fallback `CURRENT_PUBLIC_DATAPROCESSOR_SMOKE_TEST` case.

The diagnostic point is `CDF1.0`:

- process `[1, 1, -1, 3]`;
- sqrt(s) = 1800 GeV, or s = 3,240,000 GeV²;
- qT bin `[0, 0.5]` GeV, representative qT = 0.25 GeV;
- Q bin `[66, 116]` GeV, representative Q = 91 GeV;
- rapidity input `[-1000, 1000]`, representative rapidity 0, with the sentinel
  clipped by ARTEMIDE to physical support;
- no fiducial cuts;
- experimental value `3.35`, uncorrelated uncertainty `0.54`;
- theory factor `2 GeV⁻¹`, equal to the inverse qT-bin width.

## Native calculation

The calculation uses the exact C27 source chain: unchanged ARTEMIDE v3.01,
unchanged ART25 constants and model, `MSHT20_REP` DataVersion 3, both MAPFF
DataVersion 1 sets, and the central/mean ART25 technical record.

`DataProcessor.harpyInterface.ComputeXSec(point, method="default")` calls the
native bin-integrated `harpy.DY.xSecList`, then applies the point's theory
factor. The raw bin integral is `1.7197438402188676`; multiplying by 2 gives
the native value `3.4394876804377352`, with zero residual. The difference from
the experimental central value is `+0.0894876804377352`, or 2.671274% of the
experimental value.

All 33 retained CDF1 points were also calculated successfully. The first-point
values for stochastic Lambda members 1, 599, and the frozen diagnostic member
321 are respectively `3.455911539864455`, `3.437806816902704`, and
`3.4343708608644095`; their complete joint PDF/FF/NP identities are recorded.

## Observable semantics

The returned value is an absolute, qT-bin-averaged cross section in pb/GeV. It
is integrated over qT, Q², and physical rapidity before application of the
inverse-qT-bin-width theory factor. It is not a bin-center prediction and the
dataset is not theory-normalized. `includeCuts=False`, so no fiducial lepton
cuts are applied.

The executed path is the leading-power resummed TMD W term with its N4LO hard
coefficient and ARTEMIDE electroweak normalization. It contains no fixed-order
Y term and no W+Y matching. ARTEMIDE v3.01 was compiled in fast/approximate
integration mode: minimum six-section qT integration, G7 rapidity integration,
and special adaptive treatment of the Z region in the Q integral; the
non-qT relative tolerance from the constants is 1e-3.

The separately evaluated bin-center differential oracle is
`0.002541444993382964`. It is deliberately not compared numerically with the
bin-integrated result because the observables differ.

## Comparison and determinism

None of the three immutable C27 DY validation points matches CDF1.0: their
center-of-mass energies and binless definitions differ. No C27 benchmark was
changed, and no invalid integrated-versus-center comparison was made.

Two serial calls, a clean-process ARTEMIDE reinitialization, and the separate
C27-style restart calculation all have zero residual. The native adapter also
agrees exactly with the independent raw-engine-bin-integral times the stored
theory factor.

## Remaining limitation

The public repository suffices for this native diagnostic. It does not provide
an author-frozen expected output or tolerance, and the explicit public ART25
DataProcessor commit postdates the fit payload. Therefore an email to Valentin
is not necessary to establish that the public native calculation works. Email
would only be needed to obtain a frozen author reference or an explicit
attestation of the original historical environment and expected tolerance.
