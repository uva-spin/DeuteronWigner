# Q0/PLHQCD0 read-only closure audit

Audited baseline: `b094fb8cb1046aea0062468d73826ea25eab6116`.
The backend and scientific files were not modified during the audit. Missing
acceptance evidence was added separately after the read-only pass.

1. **Final Q0 status:** `Q0_CLOSED_POSITIVE`.

2. **Q0 package root:**
   `2848cb692ce20cf21f654107acbcf9ed1a803cdd1c968f576c8271ae27df3b9c`.

3. **Q0 prompt SHA-256:**
   `docs/next_level/q0_plhqcd0_codex_prompt.md` —
   `d587fd2c2cd95f8e8d5b31dc97bf0b1de57ed02b4bb212bde8984bad233cd19b`.

4. **Q0 inaugural import contract:**
   `docs/next_level/q0_plhqcd0_import_contract.json` —
   `783cfd8c6acc00ce0c6d03facf0b1f87a9fcf8026a1eb629aaf80b5944e54dd6`.

5. **Authority roots:** all positive and self-verifying.

   - C131: `67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4`
   - C142: `3e862b300f594a0bb8f5eda20f9dd6ca635cead07ef510195d86e6b73549736d`
   - C144: `cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635`
   - C148: `6152c0baadfa1254a94945bffd7b3540d737b2789b40bc23d9e5d490ac544592`
   - C149: `8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0`
   - C150: `2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a`

6. **Environment:** Python 3.11.15; PennyLane 0.38.0; Lightning 0.38.0;
   NumPy 1.26.4; SciPy 1.17.1; `lightning.qubit`; `shots=None`;
   `complex128`; macOS 14.5 arm64. Wires are `0,1,...,n-1`; bitstrings are
   big-endian, with wire 0 as the leftmost bit.

7. **Dimensions and encoding:**

   | Resolution | Physical | Padded | Qubits | Basis/wire order |
   |---|---:|---:|---:|---|
   | K9 | 1350 | 2048 | 11 | `q followed by qg`, wire 0 leftmost |
   | K11 | 2706 | 4096 | 12 | `q followed by qg`, wire 0 leftmost |
   | K13 | 4758 | 8192 | 13 | `q followed by qg`, wire 0 leftmost |

8. **Padding spectral bound and energy:** all 12 fixture/resolution pairs
   have padding spectral bound `0.0` and padding energy `0.0`. The lowest
   physical eigenvalues are:

   | Fixture | K9 | K11 | K13 |
   |---|---:|---:|---:|
   | `FIXTURE-FREE` | 0.010000000000000002 | 0.010000000000000002 | 0.010000000000000002 |
   | `FIXTURE-INTERACTING-A` | 0.5751850941379817 | 0.5751850941379817 | 0.5751850941379817 |
   | `FIXTURE-INTERACTING-B-NULL-SHIFT` | 0.6551746124531777 | 0.6551746124531777 | 0.6551746124531777 |
   | `FIXTURE-MASS-SIGN` | 0.5751850941379817 | 0.5751850941379817 | 0.5751850941379817 |

9. **Lowest physical/padded separation:** `0.010000000000000002` from the
   padded zero eigenvalue. Maximum principal-angle/projector or leakage
   residual: `0.0`.

10. **Maximum sparse-versus-matrix-free residual:**
    `1.1102230246251565e-16`.

11. **Maximum native-versus-encoded residual:** `0.0`.

12. **Maximum classical-versus-PennyLane expectation residual:** `0.0`.

13. **Maximum derivative-parity residual:** `3.469446951953614e-18`.

14. **Maximum `P_padding` for every physical holdout:** `0.0` for all
    `FIXTURE-FREE`, `FIXTURE-INTERACTING-A`,
    `FIXTURE-INTERACTING-B-NULL-SHIFT`, and `FIXTURE-MASS-SIGN` holdouts at
    K9, K11, and K13.

15. **Reproducibility:** two-clean-build `12/12`; restart `3/3`; sharded-build
    `12/12`; fixture-order pass; state-order pass; API-query-order pass.
    Forward/reverse digests matched respectively at
    `42d7262e79218d58a1ab6b6727e32193c314d0d09da85e85644c6c9a929ee16c`,
    `cd23dd654cd6e3cf14fd4891dfc9b24334b90f77e4058408a48df1baf5adcff0`, and
    `a004fb026b0b1847127c2ab6cb0a28da2c7968d82bd75be04139ac96efd93bd0`.

16. **Safety:** safe-loading pass; `allow_pickle=False` boundary pass;
    no-build-if-missing pass; no-repair-if-missing pass; no-network pass.

17. **Focused live mutations:** exactly `2304` probes, `2304` passes
    (`384` each for C131, C142, C144, C148, C149, and C150).

18. **Runtime census:** C131 1 file/341 bytes; C142 1/286; C144 1/462;
    C148 1/944; C149 1/889; C150 1/966; Q0 persisted runtime 0/0.
    Runtime manifest hashes and package roots are recorded in the JSON audit.

19. **Q1 continuation:**
    `docs/next_level/q1_plhqcdstate_codex_prompt.md` —
    `48e4ae3c4ed6c8f5aa7e2c10f9bc63b8b7a71e19f83fe2ac94307c0892cc0afc`.
    Contract:
    `docs/next_level/q1_plhqcdstate_import_contract.json` —
    `bc13b8ec6a44ed4750b94eb23da10f6ef3c566c487a1785ce8e67056180a7b98`.

20. **C151 isolation:** no C151 file was consumed and no C151 authority was
    imported. The Q0 static import guard passed.
