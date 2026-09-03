"""C111 bare qg direct-contact factorized operator authority."""
from .core import (
    STATUS, load_verified_qg_direct_contact_authority,
    verify_qg_direct_contact_authority, direct_contact_pair_entry,
    direct_contact_entry, direct_contact_entry_ancestry,
    direct_contact_sparse_matrix, direct_contact_sparse_bounds,
    apply_direct_contact, verify_source_ordered_hermiticity,
    factor_ownership_contract, count_once_certificate,
)
__all__ = ["STATUS", "load_verified_qg_direct_contact_authority",
           "verify_qg_direct_contact_authority", "direct_contact_pair_entry",
           "direct_contact_entry", "direct_contact_entry_ancestry",
           "direct_contact_sparse_matrix", "direct_contact_sparse_bounds",
           "apply_direct_contact", "verify_source_ordered_hermiticity",
           "factor_ownership_contract", "count_once_certificate"]
