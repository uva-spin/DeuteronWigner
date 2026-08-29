"""C112 direct-sum bare instantaneous-fermion block."""
from .core import (
    STATUS, load_verified_bare_instantaneous_fermion_authority,
    verify_bare_instantaneous_fermion_authority,
    instantaneous_fermion_sector_manifest, q_self_induced_inertia_block,
    qg_direct_contact_block, bare_instantaneous_fermion_sparse_matrix,
    bare_instantaneous_fermion_sparse_bounds,
    apply_bare_instantaneous_fermion, cross_sector_zero_certificate,
    counterterm_direction_manifest, instantaneous_fermion_block_ancestry,
    factor_ownership_contract,
)
__all__ = ["STATUS", "load_verified_bare_instantaneous_fermion_authority",
           "verify_bare_instantaneous_fermion_authority", "instantaneous_fermion_sector_manifest",
           "q_self_induced_inertia_block", "qg_direct_contact_block",
           "bare_instantaneous_fermion_sparse_matrix", "bare_instantaneous_fermion_sparse_bounds",
           "apply_bare_instantaneous_fermion", "cross_sector_zero_certificate",
           "counterterm_direction_manifest", "instantaneous_fermion_block_ancestry",
           "factor_ownership_contract"]
