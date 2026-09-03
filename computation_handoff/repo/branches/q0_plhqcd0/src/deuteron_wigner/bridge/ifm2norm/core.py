"""C109 audit of C80's longitudinal and dimensional semantics.

The C80 source proves cancellation of explicit L in its longitudinal factor,
but its persisted P-minus label is dimensionally inconsistent with the
four-HO factor retained in the value.  This module fails closed before any
C107×C80 product or contact assembly.
"""
from __future__ import annotations
import json
from pathlib import Path
from hashlib import sha256
from types import MappingProxyType
from typing import Any
from ..ifkernel2.core import ContactKernelPackage

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C109_IFM2NORM_PMINUS_NORMALIZATION_INCOMPLETE"
SCHEMA = "C109-IFM2NORM-V1"
C108_STATUS = "C108_IFCONTACT6_M2_PPLUS_AUTHORITY_INCOMPLETE"
C80_SCHEMA = "C80-IFKERNEL2-V1"

def _freeze(v: Any) -> Any:
    if isinstance(v, dict): return MappingProxyType({k: _freeze(x) for k, x in v.items()})
    if isinstance(v, list): return tuple(_freeze(x) for x in v)
    return v

def _hash(v: Any) -> str:
    return sha256(json.dumps(v, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()

def classify_c80_kernel_semantics() -> dict[str, Any]:
    # Public C80 input authority is inspected without evaluating a kernel.
    p = ContactKernelPackage()
    freeze = p.input_freeze()
    return {"classification": "NORMALIZATION_INCOMPLETE", "C80_schema": C80_SCHEMA,
        "declared_Pminus_units": "GeV", "observed_longitudinal": "dimensionless after L cancellation",
        "observed_spin": "dimensionless representative spinor/polarization contraction",
        "observed_color": "dimensionless ordered SU(3) factor",
        "observed_four_HO": "b_HO^2, GeV^2",
        "observed_stored_signature": "GeV^2 (from four-HO factor), not GeV P-minus",
        "declared_M2_conversion": "2*P_plus*Pminus_coefficient; P_perp^2=0",
        "P_plus": "symbolic/unbound", "L": "symbolic/unbound", "input_freeze_schema": freeze["status"],
        "C80_evaluator_calls": 0}

def load_verified_contact_m2_normalization_authority() -> Any:
    return _freeze({"schema": SCHEMA, "status": STATUS, "C108_status": C108_STATUS,
        "classification": classify_c80_kernel_semantics(),
        "convention": {"cell": "-L <= x^- <= L", "p_plus": "pi*k/L", "P_plus": "pi*K/L",
                        "K": ["9/2", "11/2", "13/2"], "fractions": "x=k/K", "L": "symbolic",
                        "M2": "2*P_plus*Pminus-P_perp^2"},
        "products": 0, "contact_entries": 0, "C107_values_for_products": 0,
        "C53_values": 0, "C58_values": 0, "physical_coupling": 0, "counterterms": 0})

def verify_contact_m2_normalization_authority() -> dict[str, Any]:
    a = load_verified_contact_m2_normalization_authority()
    return {"status": STATUS, "pass": False, "authority": a,
        "blocker": "C80 four-HO value carries GeV^2 while its P-minus schema declares GeV; source/state normalization needed to supply the missing inverse-energy factor.",
        "L_cancellation": "explicit longitudinal L cancels, but dimensional P-minus normalization does not close",
        "boost_covariance": "not established for a true P-minus object",
        "next_required": "source-qualified correction to C80 state/field normalization or exact reduced-kernel schema adapter"}

def symbolic_total_pplus(resolution: str) -> str:
    if resolution not in ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50"): raise KeyError(resolution)
    return f"pi*{ {'K9_2_N8_b0.40':'9/2','K11_2_N10_b0.45':'11/2','K13_2_N12_b0.50':'13/2'}[resolution]}/L"

def m2_kernel_record(coordinate_id: str) -> None:
    raise RuntimeError("C109 blocked: no finite M2 kernel record; P-minus normalization is incomplete")
