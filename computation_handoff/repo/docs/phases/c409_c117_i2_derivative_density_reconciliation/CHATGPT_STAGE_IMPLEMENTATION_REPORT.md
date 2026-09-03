# ChatGPT-stage C409 implementation report

C409 was implemented against the reconstructed C408 surface frozen at local
merge baseline `ab0af6587131a2846425e9bb19cfdc784b9f0bdb`.

The implementation resolves the number-preserving `J_gJ_g:qg->qg`
derivative-count conflict. It proves that the two source derivatives are
already contained in the product of the two C406 current descendants used by
C407, excludes overlapping C119/C124/C126 derivative factors, builds the
reduced transverse density-member sum, and assembles three K-local qg
product-block primitives.

The ChatGPT-stage focused suite passes 29 tests. Sparse and independently
written matrix-free actions agree at K9, K11, and K13. Hermiticity,
factorwise positivity, exact rational reconstruction, single-counted `C_A`,
fail-closed q-sector handling, and Python 3.9 compatibility are tested.

No physical coefficient, complete C117 action, rank, fit, activation, merge,
or push is claimed.
