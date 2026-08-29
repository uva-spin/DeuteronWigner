"""C105 direct-contact authority (fail-closed until C104 coefficients are numeric)."""
from .core import (
    STATUS, C104_PACKAGE_ROOT, load_verified_qg_direct_contact_authority,
    verify_qg_direct_contact_authority, direct_contact_pair_entry,
    factor_ownership_contract,
)

__all__ = ["STATUS", "C104_PACKAGE_ROOT", "load_verified_qg_direct_contact_authority",
           "verify_qg_direct_contact_authority", "direct_contact_pair_entry",
           "factor_ownership_contract"]
