# C164/HQCDLFGLOCATOR2 implementation report

Status: `C164_HQCDLFGLOCATOR2_DEPENDENCY_LOCATOR_INCOMPLETE`
Plan: `LFGLOCATOR2-D`
Next continuation: `C165/HQCDLFGDEP`

The C163 baseline was authenticated at commit `ecc821959af764f660a669ab059411b889e712ba`.
The eight locally authenticated C140 PDFs were hash-checked before indexing. The
implementation uses PyMuPDF for page text/layout and local rendering hashes and
records both zero-based PDF indices and source-specific printed-page labels.

The final C164 package root is
`6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2`.
The runtime loader checks this root and the status in
`data/runtime/c164_hqcdlfglocator2/manifest.json`.

Evidence summary:

- 8 source PDFs, 206 indexed pages, and 25 bounded descriptor lexicons.
- 442 candidate locator records were retained before selection.
- 8 object-level locators passed page, printed-page, section, equation-label,
  bounding-box, anchor, page/render/object-hash, and visual checks.
- The 8 accepted objects are limited to RI/SMOM, MOMq, and step-scaling source
  roles. They do not constitute complete C43 target expressions.
- Terminal descriptor counts are 8 dependency-locator incomplete, 13 exact
  compatible final objects absent from the local PDF set, and 4 source-role
  mismatches.
- The signed-mass/coupling gate remains closed: no complete dependency graph,
  source-to-project coordinate adapter, target program, expression capsule, or
  numerical target was created.

The source-role audit keeps physical-input reviews, beta/running, step scaling,
scheme conversion, projectors, and direct target coefficients distinct. No PDG
value was consumed, no external source was downloaded, and no formula was
completed from memory, plots, or rounded tables. C134 remains quarantined and
the inherited untracked C157 test remains untouched.

Validation includes the targeted C153–C164 regression boundary, two isolated
clean builds, fresh-process restart/query-order checks, sharding-equivalent
manifest checks, safe-loading/no-recomputation checks, visual locator holdouts,
and 384 live mutation probes. C165 is a dependency-locator continuation because
the first remaining authoritative object is closure of the dependency graphs
for the eight accepted locators.
