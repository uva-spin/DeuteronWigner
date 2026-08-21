# C163/HQCDLFGSOURCE implementation report

Baseline `a3e704bb7b5a75655fd89b79301b34a47c927194` and the committed
C162-to-C163 contract were verified before implementation. The contract SHA-256
is `8dd3d3d99a8fff97b5ce3bb19672e6e81ca5992d3b761ea640e9437b6ee44703`.

## Result

C163 closes with `C163_HQCDLFGSOURCE_LOCATOR_INCOMPLETE`, plan `LFGSOURCE-D`.
All 25 descriptors have exactly one terminal crosswalk record with terminal
status `SOURCE_LOCATOR_INCOMPLETE`. There are eight present, hash-verified
local C140 PDFs, zero authenticated descriptor locators, zero source-expression
capsules, zero dependency graphs, zero target programs, and zero target values.
The exact first missing object for each descriptor is the printed-page label,
one-based PDF page index, and equation/table/appendix/source-code object for
the requested coefficient, followed by all definition and dependency
locators. Per-descriptor request capsules are provided by
`missing_source_request_manifest()`.

## Artifact and role boundary

The canonical `source_artifact_inventory()` and `source_version_manifest()`
record the local path, SHA-256, file size, PDF page count, PDF metadata, title,
authors, declared version/date, and scientific role for each artifact. The
PDFs are ignored local cache files and were not downloaded or replaced in
C163. PDF/printed-page relation remains explicitly unverified for descriptor
binding. The two PDG reviews are prohibited for current target descriptors;
the RI/SMOM, MOMq, beta-function, and ALPHA papers remain scheme/method or
running authorities, not silently promoted to C43 light-front-gauge target
coefficients.

The signed-mass and QCD-coupling source gate is separately reported and is
closed: neither family has the required exact source object, complete
expression/dependency chain, coordinate, gauge/scheme role, active-N_f record,
or source-faithful capsule.

## Preservation and isolation

C131--C162 roots are frozen. The C158/C160 regression boundary passed in the
targeted boundary suite. The unrelated pre-existing C134 expectation failure
remains quarantined and was not repaired. The preserved untracked inherited
C157 test was not modified. C158 is neither imported as a value nor
recomputed. C163 performs no target execution, matching, common-IR test,
remainder, positive bracket, running, threshold, physical-input, parameter,
Q0/Q1/Q2, or quantum-state operation.

## Public package

The package is `deuteron_wigner.bridge.hqcdlfgsource`; its runtime manifest is
under `data/runtime/c163_hqcdlfgsource/`. Public records are immutable and
fail closed. No network, dynamic import, callable/eval/pickle, hidden build,
or repair path is present. The next continuation is exactly
`C164/HQCDLFGLOCATOR2`, for resolving exact locators inside the present source
artifacts.
