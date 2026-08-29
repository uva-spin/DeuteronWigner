"""C110 source-derived field-normalized, boost-invariant C80 kernel."""
from .core import (
    STATUS, load_verified_ifkernel_normalization_authority,
    verify_ifkernel_normalization_authority, missing_factor_classification,
    contact_normalization_record, corrected_pminus_kernel_record,
    corrected_m2_kernel_record, verify_contact_boost_covariance,
    gluon_field_normalization, qg_state_normalization,
    normalization_ancestry,
)
__all__ = ["STATUS", "load_verified_ifkernel_normalization_authority",
           "verify_ifkernel_normalization_authority", "missing_factor_classification",
           "contact_normalization_record", "corrected_pminus_kernel_record",
           "corrected_m2_kernel_record", "verify_contact_boost_covariance",
           "gluon_field_normalization", "qg_state_normalization",
           "normalization_ancestry"]
