"""C105 C104-to-C80 boundary audit.

The committed C104 payload intentionally stores symbolic coefficient programs,
not evaluated projected coefficients.  C105 therefore refuses to form a
kernel product until a numeric/bounded coefficient authority is supplied.
"""
from __future__ import annotations
from hashlib import sha256
from pathlib import Path
from typing import Any
import json

from ..ifpersist4.core import (
    manifest as _c104_manifest, programs as _c104_programs,
    canonical_record, LOGICAL, COUNTS,
)
from ..ifkernel2.core import ContactKernelPackage

ROOT = Path(__file__).resolve().parents[4]
C104_PACKAGE_ROOT = "42d3dc72def67806245875cf8c9fdfd1d801b212716e6735ade0763b4b2028de"
STATUS = "C105_BLOCKED_C104_PROJECTED_COEFFICIENT_VALUES_UNAVAILABLE"
RESOLUTIONS = tuple(COUNTS)

def _canon(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)

def _digest(v: Any) -> str:
    return sha256(_canon(v).encode()).hexdigest()

def _audit_program(p: dict[str, Any]) -> dict[str, Any]:
    expr = p["program"]["coefficient_expression"]
    return {"pair": p["pair"], "logical_count": int(p["program"]["cardinality"]),
            "expression": expr, "expression_root": _digest(expr),
            "numeric_value_present": False, "bound_present": False,
            "status": "SYMBOLIC_ONLY"}

def load_verified_qg_direct_contact_authority() -> dict[str, Any]:
    """Verify upstream roots and return a frozen fail-closed authority record."""
    m = _c104_manifest()
    if m.get("C104_PACKAGE_ROOT") != C104_PACKAGE_ROOT:
        raise ValueError("C104 package root mismatch")
    # C80 is authenticated by its own immutable package loader.
    c80 = ContactKernelPackage()
    ps = _c104_programs()
    # C104 stores a symbolic expression per pair program, but no evaluated
    # coefficient value or enclosure for any of its logical leaves.
    missing = len(ps)
    return {
        "schema": "C105-IFCONTACT5-AUTHORITY-V1", "status": STATUS,
        "C104_PACKAGE_ROOT": C104_PACKAGE_ROOT,
        "C80_input_freeze": c80.input_freeze(),
        "pairs": sum(COUNTS.values()), "logical_records": sum(LOGICAL.values()),
        "coefficient_values_missing": missing,
        "coefficient_value_policy": "C104 symbolic expression only; no numeric value or enclosure",
        "products_formed": 0, "C80_kernel_values_consumed": 0,
        "physical_coupling_consumed": 0, "C58_values_consumed": 0,
        "C53_values_consumed": 0,
    }

def verify_qg_direct_contact_authority() -> dict[str, Any]:
    a = load_verified_qg_direct_contact_authority()
    return {"status": a["status"], "pass": False,
            "blocker": "C104 projected coefficient authority has no numeric values or certified bounds",
            "pairs": a["pairs"], "logical_records": a["logical_records"],
            "coefficient_values_missing": a["coefficient_values_missing"],
            "products_formed": 0}

def factor_ownership_contract() -> dict[str, Any]:
    return {"C104": ["projected coefficient", "bra conjugation", "multiplicity", "coordinate identity"],
            "C80": ["W3 kernel", "finite-cell normalization", "spin/polarization", "ordered color", "four-HO", "Pminus-to-M2", "factored g_s^2"],
            "unowned": [], "double_owned": [], "physical_g_s": "forbidden"}

def direct_contact_pair_entry(pair_id: str, resolution: str) -> dict[str, Any]:
    """Fail closed; an entry cannot be evaluated from symbolic C104 data."""
    if (pair_id, resolution) not in _c104_programs():
        raise KeyError((pair_id, resolution))
    raise RuntimeError("C105 blocked: C104 projected coefficient value/bound unavailable; refusing coefficient-times-kernel product")

def audit_summary() -> dict[str, Any]:
    ps = _c104_programs()
    byres = {r: {"pairs": 0, "logical_records": 0, "symbolic_only": 0} for r in RESOLUTIONS}
    for p in ps.values():
        r = p["pair"]["resolution"]; byres[r]["pairs"] += 1
        byres[r]["logical_records"] += int(p["program"]["cardinality"]); byres[r]["symbolic_only"] += 1
    return {"status": STATUS, "resolutions": byres, "total_pairs": len(ps),
            "total_logical_records": sum(x["logical_records"] for x in byres.values()),
            "coordinate_totality": "NOT_REACHED", "aggregation": "NOT_REACHED"}
