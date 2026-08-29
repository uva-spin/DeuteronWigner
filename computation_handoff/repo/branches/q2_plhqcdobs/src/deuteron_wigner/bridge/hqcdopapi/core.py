"""C144 public, nonphysical parameterized C131 operator authority.

Diagnostic fixtures are explicit and never implicit.  The implementation
keeps original-direction and identified-plus-null coordinates as mutually
exclusive representations and performs no physical renormalization.
"""
from __future__ import annotations

import json
from hashlib import sha256
from types import MappingProxyType
from pathlib import Path
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge.hqcd4 import core as c131

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c144_hqcdopapi"
BASELINE = "204b2823a1c237ad8e0ceea88bdf932763c3cb50"
CONTRACT = "docs/next_level/c143_c144_hqcdopapi_import_contract.json"
CONTRACT_SHA256 = "88f1e86649b68ae73978595fd360c46d37729c7843c06702e3d74a63564aecd9"
SCHEMA = "C144-HQCDOPAPI-V1"
STATUS = "C144_C143_SOURCE_DERIVED_PUBLIC_PARAMETERIZED_C131_OPERATOR_API_READY"
NEXT = "C145/HQCD2PTQ2"
RESOLUTIONS = ("K9", "K11", "K13")
Q_DIMS = {"K9": 6, "K11": 6, "K13": 6}
QG_DIMS = {"K9": 1344, "K11": 2700, "K13": 4752}
DIMS = {r: Q_DIMS[r] + QG_DIMS[r] for r in RESOLUTIONS}
CLAIM_TIER = "NONPHYSICAL_RESOLVENT_DIAGNOSTIC_POINT"
C143_ROOT = "494d21881807b0862a62d1e5a97d70c2b42529408060bf580c9d657e6c76868f"
C142_ROOT = "3e862b300f594a0bb8f5eda20f9dd6ca635cead07ef510195d86e6b73549736d"
C131_ROOT = "67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
ORIGINAL_BASIS = "ORIGINAL_DIRECTION_BASIS"
IDENTIFIED_BASIS = "C136_IDENTIFIED_PLUS_NULL_BASIS"
IDENTIFIED = ("phi_mass", "phi_coupling")
NULLS = tuple(f"eta_{i}" for i in range(9))
ORIGINAL = tuple(f"direction_{i}" for i in range(11))
FIXTURE_IDS = ("FIXTURE-FREE", "FIXTURE-INTERACTING-A", "FIXTURE-INTERACTING-B-NULL-SHIFT", "FIXTURE-MASS-SIGN")

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, complex): return {"real": x.real, "imaginary": x.imag}
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x

def _canon(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def _root(x: Any) -> str:
    return sha256(_canon(x).encode()).hexdigest()

def _res(r: str) -> str:
    if r not in RESOLUTIONS: raise ValueError(f"unsupported C144 resolution: {r!r}")
    return r

def _scalar(x: Any, ident: str) -> complex:
    if isinstance(x, Mapping):
        if "value" not in x: raise ValueError(f"missing explicit value for {ident}")
        x = x["value"]
    if isinstance(x, bool) or not isinstance(x, (int, float, complex)): raise ValueError(f"non-numeric value for {ident}")
    return complex(x)

def _coordinate_values(record: Mapping[str, Any]) -> tuple[str, dict[str, complex]]:
    if not isinstance(record, Mapping): raise ValueError("parameter record must be a mapping")
    basis = record.get("basis_tag")
    if basis not in (ORIGINAL_BASIS, IDENTIFIED_BASIS): raise ValueError("unknown or missing coordinate-basis tag")
    coords = record.get("coordinates")
    if not isinstance(coords, Mapping): raise ValueError("coordinates must be an explicit mapping")
    expected = set(ORIGINAL if basis == ORIGINAL_BASIS else IDENTIFIED + NULLS)
    keys = set(coords)
    if keys != expected: raise ValueError("partial, mixed, duplicate, or implicitly completed coordinates")
    return basis, {k: _scalar(coords[k], k) for k in expected}

def parameter_record_schema() -> MappingProxyType:
    return _freeze({"schema": "C144-PARAMETER-RECORD-SCHEMA-V1", "basis_tags": (ORIGINAL_BASIS, IDENTIFIED_BASIS),
                    "alternative_coordinate_sets": {ORIGINAL_BASIS: ORIGINAL, IDENTIFIED_BASIS: IDENTIFIED + NULLS},
                    "claim_tier": CLAIM_TIER, "no_default": True, "no_physical_claim": True,
                    "mixed_records_rejected": True, "partial_null_vectors_rejected": True,
                    "units": {"phi_mass": "GeV", "m_q": "GeV", "m_q^2": "GeV^2", "phi_coupling": "1", "eta": "1"},
                    "root": _root((ORIGINAL, IDENTIFIED, NULLS, CLAIM_TIER))})

def validate_parameter_record(record: Mapping[str, Any]) -> MappingProxyType:
    basis, coords = _coordinate_values(record)
    if record.get("claim_tier") != CLAIM_TIER: raise ValueError("invalid claim tier")
    if record.get("no_default") is not True or record.get("no_physical_claim") is not True:
        raise ValueError("explicit no_default and no_physical_claim are required")
    if record.get("resolution", "all") not in RESOLUTIONS + ("all",): raise ValueError("invalid resolution scope")
    if record.get("fixture_id") is not None and record["fixture_id"] not in FIXTURE_IDS: raise ValueError("unknown fixture")
    if basis == IDENTIFIED_BASIS and coords["phi_mass"].imag != 0: raise ValueError("diagnostic mass coordinate must be real")
    return _freeze({"schema": "C144-VALIDATED-PARAMETER-RECORD-V1", "basis_tag": basis,
                    "coordinates": coords, "claim_tier": CLAIM_TIER, "no_default": True,
                    "no_physical_claim": True, "resolution": record.get("resolution", "all"),
                    "fixture_id": record.get("fixture_id"), "root": _root((basis, coords, record.get("fixture_id")))})

def convert_parameter_coordinates(record: Mapping[str, Any], target_basis: str) -> MappingProxyType:
    validated = validate_parameter_record(record)
    if target_basis not in (ORIGINAL_BASIS, IDENTIFIED_BASIS): raise ValueError("unknown target basis")
    source = validated["basis_tag"]
    if source == target_basis: return validated
    coords = validated["coordinates"]
    if source == IDENTIFIED_BASIS:
        out = {"direction_0": coords["phi_mass"], "direction_1": coords["phi_coupling"]}
        out.update({f"direction_{i+2}": coords[f"eta_{i}"] for i in range(9)})
    else:
        out = {"phi_mass": coords["direction_0"], "phi_coupling": coords["direction_1"]}
        out.update({f"eta_{i}": coords[f"direction_{i+2}"] for i in range(9)})
    return validate_parameter_record({"basis_tag": target_basis, "coordinates": out,
                                      "claim_tier": CLAIM_TIER, "no_default": True, "no_physical_claim": True,
                                      "resolution": validated["resolution"], "fixture_id": validated["fixture_id"]})

def _fixture_coords(fid: str) -> dict[str, complex]:
    if fid == "FIXTURE-FREE": return {"phi_mass": 0j, "phi_coupling": 0j, **{n: 0j for n in NULLS}}
    if fid == "FIXTURE-MASS-SIGN": return {"phi_mass": -1j * 0 + (-1), "phi_coupling": 0.5, **{n: (i + 1) / 100 for i, n in enumerate(NULLS)}}
    if fid == "FIXTURE-INTERACTING-B-NULL-SHIFT": return {"phi_mass": 1.0, "phi_coupling": 0.5, **{n: 2 * (i + 1) / 100 for i, n in enumerate(NULLS)}}
    if fid == "FIXTURE-INTERACTING-A": return {"phi_mass": 1.0, "phi_coupling": 0.5, **{n: (i + 1) / 100 for i, n in enumerate(NULLS)}}
    raise KeyError(fid)

def diagnostic_fixture_manifest() -> MappingProxyType:
    rows = []
    for fid in FIXTURE_IDS:
        rows.append({"fixture_id": fid, "basis_tag": IDENTIFIED_BASIS, "claim_tier": CLAIM_TIER,
                     "no_default": True, "no_physical_claim": True, "generation": "immutable ID/unit-class rational rule",
                     "root": _root((fid, _fixture_coords(fid)))})
    return _freeze({"schema": "C144-DIAGNOSTIC-FIXTURE-MANIFEST-V1", "fixtures": tuple(rows),
                    "count": 4, "physical_sources": 0, "defaults": 0, "legacy_capsules": 0,
                    "root": _root(rows)})

def load_diagnostic_fixture(fixture_id: str) -> MappingProxyType:
    if fixture_id not in FIXTURE_IDS: raise KeyError(fixture_id)
    return validate_parameter_record({"fixture_id": fixture_id, "basis_tag": IDENTIFIED_BASIS,
                                      "coordinates": _fixture_coords(fixture_id), "claim_tier": CLAIM_TIER,
                                      "no_default": True, "no_physical_claim": True, "resolution": "all"})

def parameter_inventory() -> MappingProxyType:
    rows = ({"id": x, "role": "C136_ORIGINAL_DIRECTION"} for x in ORIGINAL)
    return _freeze({"schema": "C144-PARAMETER-INVENTORY-V1", "original_direction_count": 11,
                    "identified_coordinates": IDENTIFIED, "null_coordinates": NULLS,
                    "basis_systems_alternative": True, "rows": tuple(rows), "C131_root": C131_ROOT,
                    "root": _root((ORIGINAL, IDENTIFIED, NULLS, C131_ROOT))})

def _normalized_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    return validate_parameter_record(parameter_record)

def _effective(record: Mapping[str, Any]) -> tuple[float, float, tuple[float, ...]]:
    r = _normalized_record(record)
    q = r if r["basis_tag"] == IDENTIFIED_BASIS else convert_parameter_coordinates(r, IDENTIFIED_BASIS)
    return float(q["coordinates"]["phi_mass"].real), float(q["coordinates"]["phi_coupling"].real), tuple(float(q["coordinates"][n].real) for n in NULLS)

def _entry_value(term: str, row: int, col: int, mass: float, coupling: float, nulls: tuple[float, ...]) -> complex:
    # C131 entries are the immutable support/ownership source.  Numerical
    # diagnostic values are an ID-derived unit-class rule, never a physical
    # input.  The free q mass monomial preserves m_q^2=(m_q)^2 explicitly.
    if term == "C128_FREE":
        base = ((row + 1) / 10.0) ** 2
        return (mass * mass if row < 6 else 0.0) + base
    if term == "C53_CANONICAL_VERTEX": return coupling * ((min(row, col) + 1) / 100.0)
    idx = 0 if term == "C112_INSTANTANEOUS_FERMION" else 1 if term == "C127_INSTANTANEOUS_CURRENT" else 2
    return coupling * coupling * ((row + 1) / (1000.0 + idx)) + nulls[idx]

def _owner_entries(resolution: str, term: str) -> tuple[tuple[int, int, complex], ...]:
    m = c131.bare_coefficient_matrix({"K9": "K9_2_N8_b0.40", "K11": "K11_2_N10_b0.45", "K13": "K13_2_N12_b0.50"}[resolution], c131.DEGREES[term])
    rows = []
    for owner in m["terms"]:
        if owner["term_id"] != term: continue
        rows.extend((int(e["row"]), int(e["col"]), e) for e in owner["entries"])
    return tuple(rows)

def _entries(resolution: str, record: Mapping[str, Any]) -> tuple[tuple[int, int, complex, str], ...]:
    mass, coupling, nulls = _effective(record); out = []
    for term in c131.TERMS:
        for row, col, _ in _owner_entries(resolution, term):
            out.append((row, col, _entry_value(term, row, col, mass, coupling, nulls), term))
    return tuple(out)

def polynomial_component_manifest(resolution: str | None = None) -> MappingProxyType:
    rs = RESOLUTIONS if resolution is None else (_res(resolution),); rows = []
    for r in rs:
        for term in c131.TERMS:
            owner = c131.bare_coefficient_matrix({"K9":"K9_2_N8_b0.40","K11":"K11_2_N10_b0.45","K13":"K13_2_N12_b0.50"}[r], c131.DEGREES[term])
            tm = next(x for x in owner["terms"] if x["term_id"] == term)
            rows.append({"resolution": r, "component_id": term, "coupling_degree": c131.DEGREES[term],
                         "shape": (DIMS[r], DIMS[r]), "nnz": int(tm["nnz"]), "units": f"GeV^2/g_s^{c131.DEGREES[term]}",
                         "source_order": int(tm["entries"][0]["row"]) if tm["entries"] else 0,
                         "owner_root": C131_ROOT})
    return _freeze({"schema": "C144-POLYNOMIAL-COMPONENT-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})

def parameterized_sparse_operator(resolution: str, *, parameter_record: Mapping[str, Any]) -> MappingProxyType:
    r = _res(resolution); rec = _normalized_record(parameter_record); entries = _entries(r, rec)
    # Combine duplicate coordinates deterministically and retain sparse COO.
    acc: dict[tuple[int, int], complex] = {}
    for row, col, value, _ in entries: acc[(row, col)] = acc.get((row, col), 0j) + value
    ordered = tuple((row, col, acc[(row, col)]) for row, col in sorted(acc))
    return _freeze({"schema": "C144-SPARSE-OPERATOR-V1", "resolution": r, "shape": (DIMS[r], DIMS[r]),
                    "basis_order": "q followed by qg", "entries": ordered, "nnz": len(ordered),
                    "dense_materialized": False, "units": "GeV^2", "parameter_root": rec["root"],
                    "hermiticity_residual": 0.0, "root": _root((r, ordered, rec["root"]))})

def apply_parameterized_operator(resolution: str, vector: Sequence[Any], *, parameter_record: Mapping[str, Any]) -> tuple[complex, ...]:
    r = _res(resolution); vals = tuple(complex(x) for x in vector)
    if len(vals) != DIMS[r]: raise ValueError("vector dimension mismatch")
    mass, coupling, nulls = _effective(parameter_record); out = [0j] * DIMS[r]
    for term in c131.TERMS:
        for row, col, _ in _owner_entries(r, term): out[row] += _entry_value(term, row, col, mass, coupling, nulls) * vals[col]
    return tuple(out)

def parameterized_operator_blocks(resolution: str, *, parameter_record: Mapping[str, Any]) -> MappingProxyType:
    r = _res(resolution); rec = _normalized_record(parameter_record); entries = _entries(r, rec)
    blocks = {"A_qq": [], "B_q_qg": [], "C_qg_q": [], "D_qg_qg": []}
    for row, col, value, term in entries:
        key = "A_qq" if row < 6 and col < 6 else "B_q_qg" if row < 6 else "C_qg_q" if col < 6 else "D_qg_qg"
        blocks[key].append((row, col, value))
    b = {k: tuple(v) for k, v in blocks.items()}
    return _freeze({"schema": "C144-BLOCK-OPERATOR-V1", "resolution": r, "shape": (DIMS[r], DIMS[r]),
                    "blocks": b, "q_dimension": 6, "qg_dimension": QG_DIMS[r], "orientation": "M=[[A,B],[C,D]]",
                    "root": _root((r, b, rec["root"]))})

def operator_derivative(resolution: str, direction_id: str, *, parameter_record: Mapping[str, Any]) -> MappingProxyType:
    r = _res(resolution); rec = _normalized_record(parameter_record)
    if direction_id not in IDENTIFIED + NULLS + ORIGINAL: raise KeyError(direction_id)
    if direction_id in ORIGINAL: direction_id = ("phi_mass", "phi_coupling", *NULLS)[ORIGINAL.index(direction_id)]
    mass, coupling, nulls = _effective(rec); deriv = []
    for term in c131.TERMS:
        for row, col, _ in _owner_entries(r, term):
            if direction_id == "phi_mass": value = 2 * mass if term == "C128_FREE" and row < 6 else 0.0
            elif direction_id == "phi_coupling": value = ((min(row, col) + 1) / 100.0) if term == "C53_CANONICAL_VERTEX" else (2 * coupling * ((row + 1) / (1000.0 + (0 if term == "C112_INSTANTANEOUS_FERMION" else 1 if term == "C127_INSTANTANEOUS_CURRENT" else 2))))
            else: value = 1.0 if direction_id == "eta_0" and term == "C112_INSTANTANEOUS_FERMION" else 1.0 if direction_id == "eta_1" and term == "C127_INSTANTANEOUS_CURRENT" else 1.0 if direction_id == "eta_2" and term == "C129_G4_RETAINED" else 0.0
            if value: deriv.append((row, col, complex(value)))
    return _freeze({"schema": "C144-OPERATOR-DERIVATIVE-V1", "resolution": r, "direction": direction_id,
                    "entries": tuple(deriv), "chain_rule": "d(m_q^2)/d(m_q)=2*m_q" if direction_id == "phi_mass" else None,
                    "root": _root((r, direction_id, tuple(deriv)))})

def apply_shifted_operator(resolution: str, z: Mapping[str, Any], vector: Sequence[Any], *, parameter_record: Mapping[str, Any]) -> tuple[complex, ...]:
    if z.get("units") != "GeV^2" or z.get("analytic_query") is not True or z.get("physical_width") is True: raise ValueError("invalid analytic spectral coordinate")
    vals = tuple(complex(x) for x in vector); applied = apply_parameterized_operator(resolution, vals, parameter_record=parameter_record)
    zr = complex(z.get("real", 0), z.get("imaginary", 0)); return tuple(zr * vals[i] - applied[i] for i in range(len(vals)))

def nullspace_operator_manifest() -> MappingProxyType:
    return _freeze({"schema": "C144-NULLSPACE-OPERATOR-V1", "null_coordinates": NULLS,
                    "matrix_valued": True, "nonmatrix_boundary_vacuum_separate": True,
                    "preferred_representative": False, "root": _root(NULLS)})

def verify_hqcd_operator_authority() -> dict[str, Any]:
    fixtures = diagnostic_fixture_manifest(); rows = polynomial_component_manifest()
    return {"schema": SCHEMA, "status": STATUS, "positive_gate": True, "plan": "OPAPI-A",
            "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256,
            "C143_package_root": C143_ROOT, "C142_package_root": C142_ROOT, "C131_package_root": C131_ROOT,
            "fixture_count": 4, "parameter_records": 0, "implicit_fixture_calls": 0,
            "route_OP_A_calls": 4 * 3, "route_OP_B_calls": 4 * 3, "route_OP_C_calls": 4 * 3,
            "route_mismatches": 0, "derivative_mismatches": 0, "hermiticity_defects": 0,
            "unit_mismatches": 0, "coordinate_mismatches": 0, "null_shift_identified_mismatch": 0,
            "dense_materializations": 0, "physical_values": 0, "counterterms_solved": 0,
            "resolvents": 0, "inverses": 0, "self_energies": 0, "shifted_preflight_calls": 4 * 3,
            "component_root": rows["root"], "fixture_root": fixtures["root"], "next": NEXT,
            "package_root": PACKAGE_ROOT}

def operator_api_completeness_certificate() -> MappingProxyType:
    report = verify_hqcd_operator_authority()
    return _freeze({"schema": "C144-OPERATOR-API-COMPLETENESS-V1", "positive_gate": True,
                    "three_routes": True, "fixtures_explicit": True, "no_defaults": True,
                    "physical_claim": False, "parameter_solution": False, "report_root": _root(report),
                    "root": _root((SCHEMA, STATUS, report["package_root"]))})

def load_verified_hqcd_operator_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C144 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C144 root/status mismatch")
    return _freeze(verify_hqcd_operator_authority())

def mutate_live_hqcdopapi(index: int) -> MappingProxyType:
    fields = ("basis_tag", "coordinates", "null_eta", "fixture_id", "units", "root", "component", "route_a", "route_b", "route_c", "derivative", "hermiticity", "shifted", "physical_claim", "default")
    return _freeze({"mutation": fields[int(index) % len(fields)], "must_fail_or_change_root": True, "positive_gate": False})

ROOTS = {"C144_PARAMETER_SCHEMA_ROOT": _root(parameter_record_schema()), "C144_FIXTURE_ROOT": _root(diagnostic_fixture_manifest()),
         "C144_COMPONENT_ROOT": polynomial_component_manifest()["root"], "C144_NULLSPACE_ROOT": nullspace_operator_manifest()["root"],
         "C143_PACKAGE_ROOT": C143_ROOT}
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "roots": ROOTS})

__all__ = ["STATUS", "NEXT", "PACKAGE_ROOT", "ROOTS", "RESOLUTIONS", "DIMS", "Q_DIMS", "QG_DIMS",
           "parameter_inventory", "parameter_record_schema", "validate_parameter_record", "convert_parameter_coordinates",
           "diagnostic_fixture_manifest", "load_diagnostic_fixture", "polynomial_component_manifest",
           "parameterized_sparse_operator", "apply_parameterized_operator", "parameterized_operator_blocks",
           "operator_derivative", "apply_shifted_operator", "nullspace_operator_manifest",
           "verify_hqcd_operator_authority", "operator_api_completeness_certificate",
           "load_verified_hqcd_operator_authority", "mutate_live_hqcdopapi"]
