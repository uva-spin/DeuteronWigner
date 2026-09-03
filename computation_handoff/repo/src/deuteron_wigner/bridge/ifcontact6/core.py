"""C108 C107×C80 boundary.

C107 coefficients are executable, but C80's public M² conversion retains
P_plus symbolically.  C108 refuses to choose P_plus or emit a numerical
contact operator until that missing source-owned input is authenticated.
"""
from __future__ import annotations
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifcoeffbind.core import load_verified_coefficient_binding_authority
from ..ifkernel2.core import ContactKernelPackage

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C108_IFCONTACT6_M2_PPLUS_AUTHORITY_INCOMPLETE"
SCHEMA = "C108-IFCONTACT6-V1"
C104_PACKAGE_ROOT = "42d3dc72def67806245875cf8c9fdfd1d801b212716e6735ade0763b4b2028de"

def _freeze(v: Any) -> Any:
    if isinstance(v, dict): return MappingProxyType({k: _freeze(x) for k, x in v.items()})
    if isinstance(v, list): return tuple(_freeze(x) for x in v)
    return v

def load_verified_qg_direct_contact_authority() -> Any:
    c107 = load_verified_coefficient_binding_authority()
    c80 = ContactKernelPackage()
    return _freeze({"schema": SCHEMA, "status": STATUS,
        "C104_PACKAGE_ROOT": C104_PACKAGE_ROOT,
        "C107_status": c107["status"], "C107_pairs": c107["counts"]["pairs"],
        "C107_logical_records": c107["counts"]["logical_records"],
        "C80_input_freeze": c80.input_freeze(),
        "C80_M2_conversion": "2*P_plus*(Pminus_coefficient); P_perp^2=0",
        "P_plus_value": None, "P_plus_bound": None,
        "products_formed": 0, "contact_entries": 0,
        "C58_values": 0, "C53_values": 0, "physical_coupling": 0})

def verify_qg_direct_contact_authority() -> dict[str, Any]:
    a = load_verified_qg_direct_contact_authority()
    return {"status": STATUS, "pass": False, "authority": a,
            "blocker": "C80 M2 conversion is symbolic in P_plus and no authenticated finite P_plus value/bound exists",
            "coordinate_totality": "not evaluated to operator closure",
            "products_formed": 0, "contact_entries": 0,
            "next_required": "source-owned P_plus convention/value or symbolic-operator contract before C109"}
