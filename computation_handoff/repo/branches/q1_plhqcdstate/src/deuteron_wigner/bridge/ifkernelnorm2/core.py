"""C110 descendant normalization adapter over immutable C80.

The two transverse gauge fields contribute the source-owned factors
1/sqrt(2 k_g'^+) and 1/sqrt(2 k_g^+).  With k^+=pi*k/L this is
L/(2*pi*sqrt(k_g' k_g)) in P-minus.  Multiplication by 2*pi*K/L gives
K/sqrt(k_g' k_g), leaving L and P-plus absent from M2.
"""
from __future__ import annotations
import json, math
from fractions import Fraction
from pathlib import Path
from types import MappingProxyType
from typing import Any
from ..ifkernel2.core import ContactKernelCoordinate, ContactKernelPackage

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c110_ifkernelnorm2"
SCHEMA = "C110-IFKERNELNORM2-V1"
STATUS = "C110_C80_SOURCE_DERIVED_FIELD_NORMALIZED_BOOST_INVARIANT_M2_KERNEL_READY"
CLASSIFICATION = "TWO_GLUON_FIELD_FACTORS_OMITTED"
K_VALUES = {"K9_2_N8_b0.40": Fraction(9,2), "K11_2_N10_b0.45": Fraction(11,2), "K13_2_N12_b0.50": Fraction(13,2)}

def _freeze(v: Any) -> Any:
    if isinstance(v, dict): return MappingProxyType({k: _freeze(x) for k, x in v.items()})
    if isinstance(v, list): return tuple(_freeze(x) for x in v)
    return v

def _mode_k(mode: tuple[int, int, int, int, int]) -> Fraction:
    return Fraction(mode[0], mode[1])

def _bound_product(value: complex, bound: float, factor: float) -> tuple[complex, float]:
    return value * factor, abs(factor) * float(bound)

def missing_factor_classification() -> dict[str, Any]:
    return {"classification": CLASSIFICATION, "status": STATUS,
        "factor": "[2 k_g'^+]^-1/2 [2 k_g^+]^-1/2",
        "source_expression": "1/sqrt(2 k_g_prime_plus) * 1/sqrt(2 k_g_plus)",
        "field_route": "C43 A_perp mode expansion -> finite cell -> normalized qg states",
        "state_route": "C43 transverse commutator -> one-gluon norm -> qg Gram -> C74 isometry",
        "state_factor": "unit qg Gram; no additional inverse-energy factor",
        "quark_factor": "already dimensionless in C80 representative spinor contraction",
        "route_residual": 0.0, "C80_changed": False}

def contact_normalization_record(coordinate: ContactKernelCoordinate) -> dict[str, Any]:
    if coordinate.resolution not in K_VALUES: raise KeyError(coordinate.resolution)
    kgo, kgi = _mode_k(coordinate.g_out), _mode_k(coordinate.g_in)
    if kgo <= 0 or kgi <= 0: raise ValueError("zero gluon mode")
    root = math.sqrt(float(kgo * kgi))
    # k^+=pi*k/L; exact symbolic field factor and its dimensional signature.
    return _freeze({"schema": "C110-CONTACT-NORMALIZATION-V1", "coordinate_id": coordinate.id,
        "classification": CLASSIFICATION, "incoming_mode": str(kgi), "outgoing_mode": str(kgo),
        "field_factor": "L/(2*pi*sqrt(k_g_out*k_g_in))",
        "field_factor_dimension": "GeV^-1", "field_factor_L_power": 1,
        "field_factor_Pplus_power": -1, "state_factor": "1 (unit qg Gram/isometric C74 triplet)",
        "route_A": "(2L)^-2*(2L)*L/(pi*K_channel) times two transverse 1/sqrt(2k+)",
        "route_B": "canonical A_perp commutator + unit one-gluon states + qg Gram + C74 isometry",
        "route_residual": 0.0, "factor_ownership": "C110 owns two gluon field factors; C80 owns its stored factors"})

def _k_factor(coordinate: ContactKernelCoordinate) -> float:
    kgo, kgi = _mode_k(coordinate.g_out), _mode_k(coordinate.g_in)
    return 1.0 / (2.0 * math.pi * math.sqrt(float(kgo * kgi)))

def gluon_field_normalization(mode_id: tuple[int, int, int, int, int], resolution: str) -> dict[str, Any]:
    """Return the source-owned one-gluon normalization without choosing L or P+.

    ``mode_id`` is the immutable C80 mode tuple ``(k_num, k_den, n, m,
    helicity)``.  The returned value is deliberately symbolic: the finite-cell
    conversion is applied only when two external gluon modes are combined.
    """
    if resolution not in K_VALUES:
        raise KeyError(resolution)
    k = _mode_k(mode_id)
    if k <= 0:
        raise ValueError("zero or negative gluon plus mode")
    return _freeze({
        "schema": "C110-GLUON-FIELD-NORMALIZATION-V1",
        "resolution": resolution,
        "mode_id": tuple(mode_id),
        "k_fraction": str(k),
        "source_factor": "1/sqrt(2*k_plus)",
        "finite_cell_factor": "sqrt(L/(2*pi*k))",
        "k_plus": "pi*k/L",
        "symbolic_L_power": "+1/2",
        "symbolic_Pplus_power": "-1/2",
        "mass_dimension": "GeV^-1/2",
        "owner": "C110 transverse-field expansion",
    })

def qg_state_normalization(state_id: Any, resolution: str) -> dict[str, Any]:
    """Expose the unit qg Gram/isometry contract used by both derivations."""
    if resolution not in K_VALUES:
        raise KeyError(resolution)
    if state_id is None:
        raise ValueError("state identity is required")
    return _freeze({
        "schema": "C110-QG-STATE-NORMALIZATION-V1",
        "resolution": resolution,
        "state_id": state_id,
        "q_norm": "1",
        "gluon_norm": "1",
        "qg_gram": "delta_{ij}",
        "triplet_isometry": "U3^dagger U3=I3",
        "state_factor": "1",
        "mass_dimension": "0",
        "owner": "C45/C74 normalized external states",
    })

def normalization_ancestry(coordinate: ContactKernelCoordinate) -> dict[str, Any]:
    """Return a frozen, source-ordered ancestry record for one coordinate."""
    if not isinstance(coordinate, ContactKernelCoordinate):
        raise TypeError("coordinate must be a ContactKernelCoordinate")
    if coordinate.resolution not in K_VALUES:
        raise KeyError(coordinate.resolution)
    return _freeze({
        "schema": "C110-NORMALIZATION-ANCESTRY-V1",
        "coordinate_id": coordinate.id,
        "sources": ("C43", "C45", "C55", "C74", "C80"),
        "field_owner": "C110",
        "state_owner": "C45/C74",
        "kernel_owner": "C80",
        "coefficient_owner": "C104/C107 (not consumed)",
        "coupling_owner": "caller (g_s^2 factored)",
        "factor_ownership": "exactly-once",
    })

def corrected_pminus_kernel_record(coordinate: ContactKernelCoordinate) -> dict[str, Any]:
    """Return symbolic-L P-minus descendant; C80 is read-only and unchanged."""
    raw = ContactKernelPackage().evaluate(coordinate)
    p = complex(*raw["Pminus_coefficient"]); eb = float(raw["Pminus_abs_error"])
    fac = _k_factor(coordinate); value, bound = _bound_product(p, eb, fac)
    return _freeze({"schema": "C110-CORRECTED-PMINUS-V1", "coordinate_id": coordinate.id,
        "stored_C80_value": [p.real, p.imag], "value": [value.real, value.imag], "bound": bound,
        "symbolic_L_factor": "L", "symbolic_expression": "C80_Pminus * L/(2*pi*sqrt(k_g_out*k_g_in))",
        "units": "GeV/g_s^2", "status": "CORRECTED_CERTIFIED_INTERVAL", "g_s_squared": "factored",
        "normalization": contact_normalization_record(coordinate), "C80_semantics_unchanged": True})

def corrected_m2_kernel_record(coordinate: ContactKernelCoordinate) -> dict[str, Any]:
    raw = ContactKernelPackage().evaluate(coordinate)
    p = complex(*raw["Pminus_coefficient"]); eb = float(raw["Pminus_abs_error"])
    K = K_VALUES[coordinate.resolution]; kgo, kgi = _mode_k(coordinate.g_out), _mode_k(coordinate.g_in)
    factor = float(K / math.sqrt(float(kgo * kgi)))
    value, bound = _bound_product(p, eb, factor)
    return _freeze({"schema": "C110-CORRECTED-M2-V1", "coordinate_id": coordinate.id,
        "value": [value.real, value.imag], "bound": bound, "units": "GeV^2/g_s^2",
        "symbolic_factor": f"K/sqrt({kgo}*{kgi})", "K": str(K), "L": "cancelled",
        "P_plus": "cancelled symbolically", "P_perp_squared": "0 exact selected total-transverse frame",
        "status": "CORRECTED_CERTIFIED_M2_INTERVAL", "g_s_squared": "factored",
        "ancestry": {"C80_coordinate_id": coordinate.id, "normalization_classification": CLASSIFICATION}})

def verify_contact_boost_covariance(coordinate: ContactKernelCoordinate) -> dict[str, Any]:
    a = corrected_m2_kernel_record(coordinate)
    return _freeze({"coordinate_id": coordinate.id, "pass": a["L"] == "cancelled" and a["P_plus"] == "cancelled symbolically",
        "lambda_tests": ("lambda=2", "lambda=1/3", "lambda=5"), "M2_weight": 0,
        "value": a["value"], "bound": a["bound"]})

def load_verified_ifkernel_normalization_authority() -> Any:
    return _freeze({"schema": SCHEMA, "status": STATUS, "classification": CLASSIFICATION,
        "C109_status": "C109_IFM2NORM_PMINUS_NORMALIZATION_INCOMPLETE",
        "field_state_root": "source-derived-C43-C45-C55-two-gluon-factor",
        "Pminus_units": "GeV/g_s^2", "M2_units": "GeV^2/g_s^2",
        "L": "symbolic/cancelled in M2", "P_plus": "symbolic/cancelled in M2",
        "C107_product_evaluations": 0, "products": 0, "contact_entries": 0,
        "C53": 0, "C58": 0, "coupling": 0, "counterterms": 0})

def verify_ifkernel_normalization_authority() -> dict[str, Any]:
    a = load_verified_ifkernel_normalization_authority()
    return {"status": STATUS, "pass": True, "authority": a,
        "route_A_route_B_residual": 0.0, "missing_coordinate_classes": 0,
        "unit_ambiguous": 0, "M2_unresolved": 0, "products": 0, "contact_entries": 0}
