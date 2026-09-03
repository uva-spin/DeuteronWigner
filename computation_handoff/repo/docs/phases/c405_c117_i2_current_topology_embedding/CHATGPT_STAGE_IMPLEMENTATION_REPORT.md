# C405 ChatGPT-stage implementation report

## Objective

Advance the first C117 `I2_density_projector` direction from the C403/C404 finite-axis, spatial, longitudinal, color, and spin primitives to a source-audited current-order, normalization-boundary, and direct-sum-embedding layer without inventing the still-missing product-specific normal-ordering map or a complete numerical C117 action.

## Accepted baseline

`6e7601881256d17fe14767d203cb4742143051c2` — local merge of C404.

## Implemented source modules

- `topology.py`: hash-locks C114, C115, C117, C119, C124--C127, C190, C192, C193, C249, and C250; records graph-class conflicts, incomplete current-pair programs, derivative-factor overlap risks, C192 source-field ordering, and the missing external-leg normal-ordering map.
- `derivative_order.py`: enumerates the complete finite BRA/KET candidate family for the C192-fixed source derivative field, with exact rational partition kernels and explicit adjoint reversal. The candidate axis represents the unresolved map from source field to external qg leg; it is not ambiguity about which source field is differentiated.
- `normalization.py`: constructs a literal C114/C119 scale ledger and an audit-only symbolic requirement program. The C119 gluon derivative mode factor is extracted exactly once; duplicate derivative multiplication is explicitly forbidden. No numerical prefactor is inferred.
- `conditioned.py`: combines the accepted C403/C404 primitives into caller-conditioned qg stress-test kernels with sparse, independently evaluated matrix-free, and source-order-adjoint routes.
- `embedding.py`: implements exact q-plus-qg direct-sum mechanics while requiring both surviving diagonal blocks and preserving the unavailable q block as unavailable rather than zero.
- `bindings.py` and `closure.py`: update the three K-local `c_C117_1` boundary records without increasing the complete numerical action count.

## Source reconciliation

The audit establishes:

- 13 frozen source files pass SHA-256 verification;
- 4 ordered current products and 8 diagonal product/sector programs;
- 3 C115/C125 graph-class conflicts;
- 8 C119 program rows that contain only one of the two required ordered current identities;
- 4 left-gluon program rows with derivative-factor overlap risk;
- 8 C126 program-level single-current references;
- C190 records an incomplete Gauss-current split;
- C192 closes the ordered gluon source-field slots, fixes the derivative on the second source field, retains `J_q K J_g` and `J_g K J_q` separately, and forbids a factor-two merge;
- C192 does not map its differentiated source field to an external BRA/KET gluon after product-specific normal ordering;
- C250 repairs the two-current identity grammar but does not provide product-specific normal ordering;
- C127 and C193 provide symbolic ownership but zero finite numerical matrix actions;
- C125 supplies a one-member/one-target count-once identity, while the C405-kernel-to-C125 witness/target map remains unbound.

## Numerical results

- 27 explicit ordered derivative-assignment rows across K9, K11, and K13;
- 27 conditional qg stress-test kernels;
- maximum sparse/matrix-free residual below `2e-11`;
- maximum source-order-adjoint residual below `2e-11`;
- direct-sum sparse/direct residual exactly zero in the validation fixtures;
- exact C114 q-to-qg and qg-to-q zero blocks retained;
- 0 complete numerical prefactors;
- 0 source-qualified product-topology rows;
- 0 complete numerical C117 apply paths;
- 6 complete numerical C396 apply paths, unchanged from C401.

## Scientific boundary

The conditional tensor products are classified as stress-test kernels, not operator bindings. The q-sector diagonal action, product-specific normal-ordering descendant, field/state/finite-cell normalization ownership, source phase and contraction sign, target aggregation, and C405-to-C125 witness map remain unavailable. No coefficient, physical state, current prescription, rank, fit, resolution average, or activation decision is made.

## Validation

The selected local profile reports 108 passing tests and no failures. Python compilation passes. Seventeen generated files are byte-identical across two independent clean builds. Git patch application, fresh-copy generation, and fresh-copy tests are package-level acceptance checks.
