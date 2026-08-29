"""C54 fail-closed local-HQCD source-fidelity audit."""

from .core import (STATUS, c53_read_only_import, local_projection_preflight,
    C113_STATUS, local_qcd_term_inventory, bare_term_completeness_decision,
    missing_term_manifest, direct_sum_basis_manifest,
    load_verified_local_qcd_term_authority, verify_local_qcd_term_authority,
    coupling_order_contract, counterterm_direction_manifest,
    free_m2_sparse_matrix, canonical_vertex_coefficient_sparse_matrix,
    instantaneous_fermion_coefficient_sparse_matrix, order_gs2_term_manifest,
    bare_polynomial_manifest, apply_free_m2,
    apply_canonical_vertex_coefficient, apply_order_gs2_coefficient)

__all__ = ["STATUS", "C113_STATUS", "c53_read_only_import", "local_projection_preflight",
    "local_qcd_term_inventory", "bare_term_completeness_decision", "missing_term_manifest",
    "direct_sum_basis_manifest", "load_verified_local_qcd_term_authority",
    "verify_local_qcd_term_authority", "coupling_order_contract",
    "counterterm_direction_manifest", "free_m2_sparse_matrix",
    "canonical_vertex_coefficient_sparse_matrix", "instantaneous_fermion_coefficient_sparse_matrix",
    "order_gs2_term_manifest", "bare_polynomial_manifest", "apply_free_m2",
    "apply_canonical_vertex_coefficient", "apply_order_gs2_coefficient"]
