# Draft ART25 source-material request

To: Valentin Moos (`vmoos@nycu.edu.tw`), Ignazio Scimemi (`ignazios@ucm.es`), Alexey Vladimirov (`alexeyvl@ucm.es`), and Pia Zurita (`marzurit@ucm.es`)

Dear ART25 authors,

We are reproducing ART25 with the exact ARTEMIDE v3.01 engine and the official `Models/ART25` payload introduced at commit `9ca8159e00ff2df159ab2ce4d7ffb13589af0c71`. The model code, constants file, and 642 stochastic member records have been recovered and hash-validated. To complete an exact source-level reproduction, could you please provide or identify:

1. the exact `MSHT20_REP`, `MAPFF10NNLOPIp`, and `MAPFF10NNLOKAp` LHAPDF-format sets used by `ART25_main.atmde`, including all members, metadata, license/citation, and checksums;
2. the intended ARTEMIDE v3.01 and DataProcessor commits (we infer `d873dc9...` and paper-era DataProcessor `761f3fc...`);
3. a small frozen machine-readable benchmark with exact inputs and outputs for one DY point, one SIDIS pion point, one SIDIS kaon point, and one CS/TMDPDF/TMDFF point, plus integration settings and tolerances;
4. confirmation that the released file's 642 stochastic rows supersede the “500 replicas” prose, and that its two technical rows mean initialization and central/mean respectively;
5. any required private data tables or normalization/cut conventions needed to reproduce the published component chi-squared values.

We will preserve the joint member identity and will not independently resample the NP, PDF, or FF components. This draft has not been sent.
