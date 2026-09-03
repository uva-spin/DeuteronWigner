# ART25 request delta after official MAPFF acquisition

To: Valentin Moos (`vmoos@nycu.edu.tw`), Ignazio Scimemi (`ignazios@ucm.es`), Alexey Vladimirov (`alexeyvl@ucm.es`), and Pia Zurita (`marzurit@ucm.es`)

Dear ART25 authors,

We have now obtained the official DataVersion 1 `MAPFF10NNLOPIp` and `MAPFF10NNLOKAp` archives from CERN, hash-locked all 201 members of each, and verified that every released ART25 FF index resolves exactly. Please confirm that these DataVersion 1 archives are byte-identical to those used in ART25.

The remaining reproduction inputs are:

1. the exact `MSHT20_REP` archive used by ART25, with `.info`, members 0–999, SHA-256 checksums, generation provenance, license, and ordering; or the exact deterministic generator state including the input Hessian DataVersion, algorithm/commit, transform matrix, seeds, normalization, eigenvector order, clipping rules, and official validation checksum;
2. source-owned frozen outputs and exact commands/configurations for the requested DY, SIDIS, CS, TMDPDF, pion-TMDFF, and kaon-TMDFF benchmark points, including observable definitions, bin integration, units, integration mode, and tolerances;
3. confirmation of the DataProcessor commit and the 642 stochastic plus two technical-row semantics.

The public 65-member `MSHT20nnlo_as118` Hessian set has not been substituted or generically converted. This draft has not been sent.
