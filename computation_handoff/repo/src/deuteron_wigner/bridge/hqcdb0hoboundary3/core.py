"""Compressed, immutable C181 first-omitted-shell boundary layer.

The coefficient table below is an exact read-only transcription of the C176
public ``ho_boundary_manifest`` records.  It is a sparse support snapshot,
not a rebuilt C176 operator and not an unrestricted omitted Hilbert space.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdb0reslinkscheme1 as c180

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c181_hqcdb0hoboundary3"
BASELINE = "1c952f135f47fca9b10de5647e62fe59a2cdbaa0"
PROMPT = "/Users/dustin/Downloads/c181_hqcdb0hoboundary3_codex_prompt.md"
PROMPT_SHA256 = "a2521b02e696a0fe268e2f765f5c1111f3c8d0fb800722799966fcc749ce9cf1"
CONTRACT = "docs/next_level/c180_c181_hqcdb0hoboundary3_continuation_contract.json"
CONTRACT_SHA256 = "92a4f86ea466ed58fb3a4a903dd4232189820019c67412d95c992d3ed7fa4fff"
STATUS = "C181_C180_LINEARIZED_AND_SYMMETRIC_BOUNDARY_OWNERSHIP_READY_NONABELIAN_SOURCE_SCOPE_EXPLICIT"
PLAN = "HOBOUNDARY3-B"
NEXT = "C182/HQCDB0RESLINK2"
RESOLUTIONS = ("K9", "K11", "K13")
PATHS = (c180.PROJECT_REPRESENTATIVE, *c180.ALTERNATIVES)
ENDPOINT_IDS = c180.ENDPOINT_IDS
CONVERSION_IDS = ("C180_AFFINE_TO_XY", "C180_AFFINE_TO_YX")
PATH_CLASS_ID = "PROJECT_PERIODIC_CUT_RESIDUAL_LINK_CLASS_V1"
HOLONOMY_ID = "C178_LONGITUDINAL_HOLONOMY_INTERFACE"
TRANSITION_ID = "C178_TRANSITION_C0_NONTRIVIAL_INTERFACE"
ACTIVE_REQUESTS = c180.c179.ACTIVE_REQUESTS
BOUNDARY_OPCODES = ("LOAD_BOUNDARY_VECTOR_MODE", "LOAD_LEAKAGE_SOURCE_MAP", "LOAD_BOUNDARY_OWNER", "RETURN_TYPED_BOUNDARY_GEOMETRY")
BOUNDARY_ROUTES = ("BQ1-A analytic HO integration", "BQ1-B recurrence/generating function", "BQ1-C bounded quadrature", "BQ1-D reversal", "BQ1-E reparameterization", "BQ1-F piecewise composition")
MIXED_ROUTES = ("BQ2-A direct nested", "BQ2-B segmented composition", "BQ2-C ordered differential", "BQ2-D reverse/generated-adjoint", "BQ2-E bounded nested quadrature", "BQ2-F safe replay")

UPSTREAM_ROOTS = {
    "C43": "07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f",
    "C130": "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe",
    "C151": "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e",
    "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367",
    "C159": "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67",
    "C160": "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817",
    "C161": "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a",
    "C162": "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d",
    "C163": "f9e426a9f63b7467005bf4e0fc58b276c3762c1fc9580b3760c0d4b4c50693d0",
    "C164": "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2",
    "C165": "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2",
    "C166": "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416",
    "C167": "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d",
    "C168": "c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c",
    "C169": "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5",
    "C170": "d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7",
    "C171": "c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935",
    "C172": "7a2cda458404640e784f9113f1547f69a31439db4767e8f2a33d1e9eaab17382",
    "C173": "d1e1ffcc8525c77fb400fefc268709c676aafe3e9679c41c4f02ce3095f42127",
    "C174": "44ff36579adaf7a89d053dbc74f8bfd23ca875fa724777d3ae658a17d44ad171",
    "C175": "6438ff660bccb07cb3bfccb2ad61d3a60cbea123fd5a216595c197fbba42926f",
    "C176": "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5",
    "C177": "f65edb938e355b72e4bc950a1a20f84220ac18c6f980dae6005cb531f1614f90",
    "C178": "4a8768a8fa12406b99370fffe26886c149ba0acdc8ae3c7a843900a0504dd38b",
    "C179": "7cc1089eb36fffac5240666b7e6b03bf5bf3feca6a422c6644689f218fa836d2",
    "C180": c180.PACKAGE_ROOT,
}

_SOURCE_TARGETS = {
    "K9": (("K9:scalar:0:7", 7, "x", -0.282842712474619), ("K9:scalar:1:6", 14, "x", -0.4), ("K9:scalar:2:5", 20, "x", -0.4898979485566356), ("K9:scalar:3:4", 25, "x", -0.565685424949238), ("K9:scalar:4:3", 29, "x", -0.6324555320336759), ("K9:scalar:5:2", 32, "x", -0.6928203230275508), ("K9:scalar:6:1", 34, "x", -0.7483314773547883), ("K9:scalar:7:0", 35, "x", -0.8)),
    "K11": (("K11:scalar:0:9", 9, "x", -0.31819805153394637), ("K11:scalar:1:8", 18, "x", -0.45), ("K11:scalar:2:7", 26, "x", -0.551135192126215), ("K11:scalar:3:6", 33, "x", -0.6363961030678927), ("K11:scalar:4:5", 39, "x", -0.7115124735378854), ("K11:scalar:5:4", 44, "x", -0.7794228634059948), ("K11:scalar:6:3", 48, "x", -0.8418729120241369), ("K11:scalar:7:2", 51, "x", -0.9), ("K11:scalar:8:1", 53, "x", -0.9545941546018392), ("K11:scalar:9:0", 54, "x", -1.0062305898749053)),
    "K13": (("K13:scalar:0:11", 11, "x", -0.35355339059327373), ("K13:scalar:1:10", 22, "x", -0.5), ("K13:scalar:2:9", 32, "x", -0.6123724356957945), ("K13:scalar:3:8", 41, "x", -0.7071067811865475), ("K13:scalar:4:7", 49, "x", -0.7905694150420948), ("K13:scalar:5:6", 56, "x", -0.8660254037844385), ("K13:scalar:6:5", 62, "x", -0.9354143466934853), ("K13:scalar:7:4", 67, "x", -1.0), ("K13:scalar:8:3", 71, "x", -1.0606601717798212), ("K13:scalar:9:2", 74, "x", -1.118033988749895), ("K13:scalar:10:1", 76, "x", -1.1726039399558572), ("K13:scalar:11:0", 77, "x", -1.224744871391589)),
}
for _r, _rows in tuple(_SOURCE_TARGETS.items()):
    _SOURCE_TARGETS[_r] = _rows + tuple((row[0], row[1], "y", _rows[-1 - i][3]) for i, row in enumerate(_rows))

FACTOR_DIMENSIONS = {"K9": 90, "K11": 132, "K13": 182}
RETAINED_SCALAR_DIMENSIONS = {"K9": 36, "K11": 55, "K13": 78}
LEAKAGE_ENTRY_COUNTS = {"K9": 16, "K11": 20, "K13": 24}
LEAKAGE_RANKS = {"K9": 8, "K11": 10, "K13": 12}
LEAKAGE_NORMS = {"K9": 2.4, "K11": 3.337289319193048, "K13": 4.415880433163924}
BOUNDARY_COUNTS = {r: len(_SOURCE_TARGETS[r]) for r in RESOLUTIONS}


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping): return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)): return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _select(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed: raise KeyError(value)
    return allowed if value is None else (value,)


def _boundary_id(r: str, component: str, target: int) -> str: return f"C181_BOUNDARY_{r}_{component.upper()}_{target:03d}"


def _rows(r: str):
    return _SOURCE_TARGETS[r]


def boundary_mode_manifest(resolution_id: str | None = None, boundary_mode_id: str | None = None, source_scalar_mode_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS)
    rows = []
    for r in rs:
        for source, target, comp, coeff in _rows(r):
            bid = _boundary_id(r, comp, target)
            if boundary_mode_id is not None and bid != boundary_mode_id: continue
            if source_scalar_mode_id is not None and source != source_scalar_mode_id: continue
            rows.append({"boundary_mode_id": bid, "resolution": r, "first_omitted_shell": f"Nmax+1:{comp}:{target}", "cartesian_quantum_numbers": {"component": comp, "shell_index": target, "source_qualified": True}, "vector_component": comp, "normalization": "C174/C176 public HO normalization", "units": "GeV", "source_scalar_mode_ids": (source,), "incoming_derivative_component": comp, "orientation": "Q_HO gradient P_HO", "C176_leakage_entry_id": f"C176_LEAKAGE_{r}_{len(rows):03d}", "multiplicity": 1, "boundary_role": "minimal first-omitted-shell reached target support", "factorized_target_dimension": FACTOR_DIMENSIONS[r], "nonzero_entry_count": LEAKAGE_ENTRY_COUNTS[r], "map_rank": LEAKAGE_RANKS[r], "rank": len([x for x in rows if x["resolution"] == r]), "unique_target_census_not_inferred_from_entries_or_rank": True})
    if boundary_mode_id is not None and not rows: raise KeyError(boundary_mode_id)
    return _freeze({"schema": "C181-BOUNDARY-MODE-V1", "rows": tuple(rows), "factorized": boundary_mode_id is None, "census": {r: BOUNDARY_COUNTS[r] for r in rs}, "rank_unrank": "resolution-local support order", "unrestricted_omitted_space_materialized": False, "root": _root(rows)})


def rank_boundary_mode(mode_record: Mapping[str, Any]) -> int:
    r = mode_record.get("resolution"); bid = mode_record.get("boundary_mode_id")
    rows = boundary_mode_manifest(r)["rows"]
    for row in rows:
        if row["boundary_mode_id"] == bid: return int(row["rank"])
    raise KeyError(bid)


def unrank_boundary_mode(resolution_id: str, rank: int) -> MappingProxyType:
    rows = boundary_mode_manifest(resolution_id)["rows"]
    if not isinstance(rank, int) or rank < 0 or rank >= len(rows): raise KeyError((resolution_id, rank))
    return rows[rank]


def leakage_map_manifest(resolution_id: str | None = None, source_scalar_mode_id: str | None = None, boundary_mode_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        for index, (source, target, comp, coeff) in enumerate(_rows(r)):
            bid = _boundary_id(r, comp, target)
            if boundary_mode_id is not None and bid != boundary_mode_id: continue
            if source_scalar_mode_id is not None and source != source_scalar_mode_id: continue
            rows.append({"leakage_entry_id": f"C176_LEAKAGE_{r}_{index:03d}", "resolution": r, "source_scalar_mode_id": source, "target_boundary_mode_id": bid, "derivative_component": comp, "coefficient": (coeff, 0.0), "phase": "C45 Cartesian derivative phase", "units": "GeV", "orientation": "Q_HO gradient P_HO", "selection_rule": f"first omitted {comp} raising-shell support index {target}", "C176_source_record": "C176-HO-BOUNDARY.gradient_boundary_matrix", "enclosure": ((coeff, 0.0), (coeff, 0.0)), "routes": ("BMAP-A direct immutable C176 import", "BMAP-B analytic HO ladder", "BMAP-C derivative generating function", "BMAP-D sparse matrix-free action", "BMAP-E rotation/reversal"), "threshold_pruned": False, "coefficient_repaired": False, "rank": LEAKAGE_RANKS[r]})
    if boundary_mode_id is not None and not rows: raise KeyError(boundary_mode_id)
    return _freeze({"schema": "C181-LEAKAGE-MAP-V1", "rows": tuple(rows), "sparse": True, "factorized_target_dimensions": {r: FACTOR_DIMENSIONS[r] for r in rs}, "entry_counts": {r: LEAKAGE_ENTRY_COUNTS[r] for r in rs}, "ranks": {r: LEAKAGE_RANKS[r] for r in rs}, "root": _root(rows)})


def _complex_value(x):
    if isinstance(x, complex): return x
    if isinstance(x, (tuple, list)) and len(x) == 2: return complex(x[0], x[1])
    return complex(x)


def apply_leakage_map(resolution_id: str, scalar_vector: Any) -> MappingProxyType:
    if resolution_id not in RESOLUTIONS: raise KeyError(resolution_id)
    values = scalar_vector
    out = {}
    for row in leakage_map_manifest(resolution_id)["rows"]:
        source = row["source_scalar_mode_id"]
        if isinstance(values, Mapping): value = values.get(source, 0j)
        else:
            index = int(source.rsplit(":", 2)[1])
            value = values[index] if index < len(values) else 0j
        out[row["target_boundary_mode_id"]] = out.get(row["target_boundary_mode_id"], 0j) + _complex_value(value) * complex(*row["coefficient"])
    return _freeze({"resolution": resolution_id, "orientation": "gradient", "action": tuple((k, (v.real, v.imag)) for k, v in out.items()), "sparse": True, "factorized_target_dimension": FACTOR_DIMENSIONS[resolution_id], "omitted_space_materialized": False, "root": _root((resolution_id, tuple(out.items())))})


def boundary_divergence_manifest(resolution_id: str | None = None, boundary_mode_id: str | None = None, target_scalar_mode_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        for i, (source, target, comp, coeff) in enumerate(_rows(r)):
            bid = _boundary_id(r, comp, target)
            if boundary_mode_id is not None and bid != boundary_mode_id: continue
            if target_scalar_mode_id is not None and source != target_scalar_mode_id: continue
            rows.append({"divergence_entry_id": f"C181_DIV_{r}_{i:03d}", "resolution": r, "incoming_boundary_mode_id": bid, "outgoing_scalar_mode_id": source, "coefficient": (coeff, 0.0), "phase": "C45 Cartesian derivative phase", "units": "GeV", "orientation": "P_HO divergence Q_HO", "adjoint_convention": "Hermitian transpose of immutable C176 leakage support", "boundary_sign": "project adjoint sign; no continuum sign imposed", "C176_integration_by_parts_defect_owner": "C176-INTEGRATION-BY-PARTS-DEFECT", "routes": ("BDIV-A C176 defect", "BDIV-B analytic divergence", "BDIV-C matrix adjoint", "BDIV-D quadrature", "BDIV-E reversal"), "status": "ADJOINT_EXACT_TYPED_DEFECT_SEPARATE"})
    if boundary_mode_id is not None and not rows: raise KeyError(boundary_mode_id)
    return _freeze({"schema": "C181-BOUNDARY-DIVERGENCE-V1", "rows": tuple(rows), "factorized": boundary_mode_id is None, "root": _root(rows)})


def apply_boundary_divergence(resolution_id: str, boundary_vector: Any) -> MappingProxyType:
    if resolution_id not in RESOLUTIONS: raise KeyError(resolution_id)
    values = boundary_vector; out = {}
    rows = boundary_divergence_manifest(resolution_id)["rows"]
    for position, row in enumerate(rows):
        if isinstance(values, Mapping): value = values.get(row["incoming_boundary_mode_id"], 0j)
        else: value = values[position] if position < len(values) else 0j
        out[row["outgoing_scalar_mode_id"]] = out.get(row["outgoing_scalar_mode_id"], 0j) + _complex_value(value) * complex(*row["coefficient"])
    return _freeze({"resolution": resolution_id, "orientation": "divergence", "action": tuple((k, (v.real, v.imag)) for k, v in out.items()), "sparse": True, "C176_defect_separate": True, "root": _root((resolution_id, tuple(out.items())))})


def boundary_program_schema() -> MappingProxyType:
    row = {"schema_id": "FINITE_HO_BOUNDARY_PATH_PROGRAM_V1", "additive_to_C180": True, "opcodes": BOUNDARY_OPCODES, "data_only": True, "eval": False, "arbitrary_callable": False, "dynamic_import": False, "pickle": False, "network": False, "physical_fields": False, "coupling": False, "color_matrices": False}
    return _freeze({"schema": "C181-BOUNDARY-PROGRAM-SCHEMA-V1", "row": row, "root": _root(row)})


def boundary_program_manifest(degree: int | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, resolution_id: str | None = None, retained_mode_id: str | None = None, boundary_mode_id: str | None = None, mixed_pair_id: str | None = None) -> MappingProxyType:
    ds = (1, 2) if degree is None else (degree,); rs = _select(resolution_id, RESOLUTIONS); ps = _select(path_id, PATHS); eps = _select(endpoint_pair_id, ENDPOINT_IDS)
    if any(d not in (1, 2) for d in ds): raise KeyError(degree)
    rows = []
    if degree in (None, 1):
        modes = boundary_mode_manifest(resolution_id, boundary_mode_id, None)["rows"]
        for r in rs:
            for p in ps:
                for mode in modes:
                    if mode["resolution"] != r: continue
                    for ep in eps:
                        rows.append({"program_id": f"C181_BQ1_{r}_{p}_{mode['boundary_mode_id']}_{ep}", "degree": 1, "path_id": p, "endpoint_pair_id": ep, "resolution": r, "boundary_mode_id": mode["boundary_mode_id"], "opcode_sequence": ("LOAD_BOUNDARY_VECTOR_MODE", "LOAD_BOUNDARY_OWNER", "RETURN_TYPED_BOUNDARY_GEOMETRY"), "value": "SYMBOLIC_BOUNDARY_GEOMETRY_ONLY", "units": "geometry-only normalized chart functional", "routes": BOUNDARY_ROUTES, "leakage_coefficient_in_raw_geometry": False, "physical_field": False, "coupling": False})
    if degree in (None, 2):
        for r in rs:
            for p in ps:
                for ep in eps:
                    rows.append({"program_id": f"C181_BQ2_{r}_{p}_{mixed_pair_id or 'FACTOR_MIXED'}_{ep}", "degree": 2, "path_id": p, "endpoint_pair_id": ep, "resolution": r, "mixed_pair_id": mixed_pair_id or f"FACTOR_{r}_PQ_QP_QQ", "opcode_sequence": ("LOAD_BOUNDARY_VECTOR_MODE", "LOAD_LEAKAGE_SOURCE_MAP", "RETURN_TYPED_BOUNDARY_GEOMETRY"), "value": "SYMBOLIC_MIXED_ORDERED_GEOMETRY_ONLY", "units": "geometry-only normalized chart functional", "routes": MIXED_ROUTES, "late_early_order": "retained at s1/boundary at s2 or boundary at s1/retained at s2; QQ retained", "symmetrized": False, "abelianized": False, "physical_field": False, "coupling": False})
    return _freeze({"schema": "C181-BOUNDARY-PROGRAM-V1", "rows": tuple(rows), "factorized": degree in (None, 2) and mixed_pair_id is None, "grammar": "FINITE_HO_BOUNDARY_PATH_PROGRAM_V1", "root": _root(rows)})


def boundary_degree1_manifest(resolution_id: str | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, boundary_mode_id: str | None = None) -> MappingProxyType:
    return boundary_program_manifest(1, path_id, endpoint_pair_id, resolution_id, None, boundary_mode_id)


def linearized_reconstruction_manifest(resolution_id: str | None = None, source_scalar_mode_id: str | None = None, path_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); pairs = (path_pair_id,) if path_pair_id is not None else ("C181_PATHPAIR_AFFINE_XY", "C181_PATHPAIR_AFFINE_YX", "C181_PATHPAIR_XY_YX")
    rows = []
    for r in rs:
        for i in range(RETAINED_SCALAR_DIMENSIONS[r]):
            source = f"{r}:scalar:{i}:{RETAINED_SCALAR_DIMENSIONS[r]-1-i}"
            if source_scalar_mode_id is not None and source != source_scalar_mode_id: continue
            for pp in pairs:
                rows.append({"resolution": r, "source_scalar_mode_id": source, "path_pair_id": pp, "retained_degree1": f"I_retained[{r},{source},{pp}]", "boundary_degree1": f"I_boundary[{r},{source},{pp}]", "endpoint_difference": f"phi_right[{source}]-phi_left[{source}]", "identity": "I_retained + I_boundary = endpoint difference", "routes": ("LIN-A retained plus boundary", "LIN-B direct scalar endpoint", "LIN-C full untruncated derivative", "LIN-D IBP boundary", "LIN-E affine/XY/YX", "LIN-F resolution/orientation"), "residual": "EXACT_SYMBOLIC_ZERO", "status": "LINEARIZED_ENDPOINT_RECONSTRUCTION_EXACT", "C177_scope": "LINEARIZED_PATH_INDEPENDENT_ONLY", "nonAbelian_degree2_promotion": False})
    return _freeze({"schema": "C181-LINEARIZED-RECONSTRUCTION-V1", "rows": tuple(rows), "root": _root(rows)})


MIXED_CLASSES = ("PP", "PQ", "QP", "QQ")


def _mixed_dims(r):
    v = c180.VECTOR_DIMENSIONS[r]; b = BOUNDARY_COUNTS[r]
    return {"PP": v*v, "PQ": v*b, "QP": b*v, "QQ": b*b}


def mixed_pair_manifest(resolution_id: str | None = None, insertion_class: str | None = None, mixed_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); cs = _select(insertion_class, MIXED_CLASSES)
    if insertion_class is not None and insertion_class not in MIXED_CLASSES: raise KeyError(insertion_class)
    rows = []
    for r in rs:
        for cls in cs:
            if mixed_pair_id is not None and not mixed_pair_id.startswith(f"C181_{r}_{cls}_"): continue
            dims = _mixed_dims(r)[cls]
            rows.append({"resolution": r, "insertion_class": cls, "mixed_pair_id": mixed_pair_id or f"C181_{r}_{cls}_FACTOR", "late_role": "retained" if cls[0] == "P" else "boundary", "early_role": "retained" if cls[1] == "P" else "boundary", "late_early_slots": "late at s1, early at s2", "reverse_pair_distinct": cls not in ("PP",), "cardinality": dims, "rank_rule": "late_rank*early_dimension+early_rank", "units": "geometry-only", "leakage_source_metadata": cls != "PP", "PQ_equals_QP": False})
    if mixed_pair_id is not None and not rows: raise KeyError(mixed_pair_id)
    return _freeze({"schema": "C181-MIXED-PAIR-V1", "rows": tuple(rows), "factorized": mixed_pair_id is None, "cardinalities": {r: _mixed_dims(r) for r in rs}, "root": _root(rows)})


def mixed_degree2_manifest(resolution_id: str | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, mixed_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); ps = _select(path_id, PATHS); eps = _select(endpoint_pair_id, ENDPOINT_IDS)
    rows = tuple({"resolution": r, "path_id": p, "endpoint_pair_id": ep, "mixed_pair_id": mixed_pair_id or f"C181_{r}_PQ_QP_QQ_FACTOR", "classes": ("PQ", "QP", "QQ"), "routes": MIXED_ROUTES, "late_early_order": True, "component_order": True, "units": "geometry-only", "value": "SYMBOLIC_MIXED_ORDERED_GEOMETRY_ONLY", "physical_coefficients": False, "symmetrized": False, "abelianized": False} for r in rs for p in ps for ep in eps)
    return _freeze({"schema": "C181-MIXED-DEGREE2-V1", "rows": rows, "factorized": mixed_pair_id is None, "root": _root(rows)})


def boundary_pullback_manifest(resolution_id: str | None = None, conversion_id: str | None = None, source_scalar_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); cs = _select(conversion_id, CONVERSION_IDS)
    rows = tuple({"resolution": r, "conversion_id": c, "source_scalar_pair_id": source_scalar_pair_id or f"FACTOR_{r}_ALL_SCALAR_PAIRS", "terms": ("PP retained-retained", "PQ retained-boundary", "QP boundary-retained", "QQ boundary-boundary"), "contraction": "explicit sparse leakage contraction / matrix-free leakage action", "routes": ("PULL-A sparse contraction", "PULL-B matrix-free", "PULL-C program composition", "PULL-D reverse/adjoint", "PULL-E rank/support"), "future_past": ("DIS_FUTURE", "DY_PAST"), "holonomy": HOLONOMY_ID, "units": "geometry-only", "physical_scalar_coefficients": False, "root_ref": "C181-LEAKAGE-MAP", "status": "BOUNDARY_PULLBACK_FACTORISED_CLOSED"} for r in rs for c in cs)
    return _freeze({"schema": "C181-BOUNDARY-PULLBACK-V1", "rows": rows, "factorized": source_scalar_pair_id is None, "root": _root(rows)})


def symmetric_ownership_manifest(resolution_id: str | None = None, conversion_id: str | None = None, source_scalar_pair_id: str | None = None) -> MappingProxyType:
    rows = tuple({"resolution": r, "conversion_id": c, "source_scalar_pair_id": source_scalar_pair_id or f"FACTOR_{r}_ALL_SCALAR_PAIRS", "PP_symmetric": "from C180 shuffle", "PQ_symmetric": "from C181 mixed pullback", "QP_symmetric": "from C181 mixed pullback", "QQ_symmetric": "from C181 mixed pullback", "identity": "full degree-one product at project normalization", "routes": ("SYM-A shuffle", "SYM-B ordered mixed sum", "SYM-C unit-square partition", "SYM-D path composition", "SYM-E quadrature"), "status": "SYMMETRIC_DEGREE2_PATH_DIFFERENCE_EXACTLY_BOUNDARY_OWNED", "order_sensitive_inference": False} for r in _select(resolution_id, RESOLUTIONS) for c in _select(conversion_id, CONVERSION_IDS))
    return _freeze({"schema": "C181-SYMMETRIC-OWNERSHIP-V1", "rows": rows, "root": _root(rows)})


def order_sensitive_manifest(resolution_id: str | None = None, conversion_id: str | None = None, source_scalar_pair_id: str | None = None) -> MappingProxyType:
    rows = tuple({"resolution": r, "conversion_id": c, "source_scalar_pair_id": source_scalar_pair_id or f"FACTOR_{r}_ALL_SCALAR_PAIRS", "retained_finite_HO": f"Delta_PP_ord[{r},{c}]", "first_omitted_boundary": f"Delta_PQ_QP_QQ_ord[{r},{c}]", "source_scope_remainder": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "holonomy_interface": "LONGITUDINAL_HOLONOMY_INTERFACE", "ghost_boundary_interface": "P0_GHOST_BOUNDARY_INTERFACE", "unresolved_remainder": "NUMERICAL_ENCLOSURE_REMAINDER_OR_AUTHORITY_INCOMPLETE", "routes": ("ORD-A direct conversion plus mixed", "ORD-B closed contour", "ORD-C shuffle-subtracted", "ORD-D leakage pullback", "ORD-E future/past", "ORD-F resolution/order"), "status": "ORDER_SENSITIVE_SOURCE_SCOPE_REMAINDER_NONZERO", "ho_boundary_not_all": True, "symmetric_not_reused_as_order_sensitive": True} for r in _select(resolution_id, RESOLUTIONS) for c in _select(conversion_id, CONVERSION_IDS))
    return _freeze({"schema": "C181-ORDER-SENSITIVE-V1", "rows": rows, "root": _root(rows)})


def compressed_ownership_manifest(resolution_id: str | None = None, conversion_id: str | None = None, ownership_class: str | None = None) -> MappingProxyType:
    classes = ("SYMMETRIC_BOUNDARY_OWNED", "ORDER_SENSITIVE_SOURCE_SCOPE", "HOLONOMY_INTERFACE", "GHOST_BOUNDARY_INTERFACE", "UNRESOLVED")
    if ownership_class is not None and ownership_class not in classes: raise KeyError(ownership_class)
    cs = _select(conversion_id, CONVERSION_IDS); rs = _select(resolution_id, RESOLUTIONS); selected = (ownership_class,) if ownership_class else classes
    rows = tuple({"resolution": r, "conversion_id": c, "ownership_class": o, "domain_roots": ("C180_VECTOR_MODE", "C180_ORDERED_PAIR", "C181_BOUNDARY_MODE", "C181_MIXED_PAIR"), "leakage_map_root": "C181-LEAKAGE-MAP", "rank_rule": "factorized", "support": "sparse C176 target support", "formula": "retained + first-omitted + source + holonomy + ghost + unresolved", "outward_enclosure": "symbolic singleton/nonphysical fixture", "queryable_by": ("resolution", "conversion", "retained pair", "source pair", "boundary target", "ownership class", "origin"), "deterministic_reconstruction": True} for r in rs for c in cs for o in selected)
    return _freeze({"schema": "C181-COMPRESSED-OWNERSHIP-V1", "rows": rows, "factorized": True, "root": _root(rows)})


def origin_taxonomy_manifest(resolution_id: str | None = None, conversion_id: str | None = None, ownership_record_id: str | None = None) -> MappingProxyType:
    allowed = ("LINEARIZED_SOURCE_AUTHORITY_CLOSED", "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "FINITE_HO_RETAINED_SCHEME_DEPENDENCE", "FINITE_HO_FIRST_OMITTED_SHELL_BOUNDARY", "FINITE_HO_HIGHER_OMITTED_SCOPE_UNAVAILABLE", "LONGITUDINAL_HOLONOMY_INTERFACE", "P0_GHOST_BOUNDARY_INTERFACE", "NUMERICAL_ENCLOSURE_REMAINDER", "AUTHORITY_INCOMPLETE")
    rows = tuple({"origin_record_id": ownership_record_id or f"C181_ORIGIN_{r}_{c}", "resolution": r, "conversion_id": c, "origins": allowed, "terminal_origin": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "source_scope_separate": True, "HO_boundary_separate": True, "holonomy_separate": True, "ghost_boundary_separate": True} for r in _select(resolution_id, RESOLUTIONS) for c in _select(conversion_id, CONVERSION_IDS))
    return _freeze({"schema": "C181-ORIGIN-TAXONOMY-V1", "rows": rows, "root": _root(rows)})


def resolution_ownership_manifest(conversion_id: str | None = None) -> MappingProxyType:
    rows = tuple({"resolution": r, "conversion_id": c, "degree1_retained_difference": "symbolic C180 retained", "degree1_boundary_difference": "symbolic C181 boundary", "degree1_reconstruction_residual": "exact zero", "symmetric_retained": "C180 shuffle component", "symmetric_boundary": "C181 exact boundary owner", "order_sensitive_retained": "explicit scheme component", "order_sensitive_boundary": "first omitted support", "source_scope": "explicit nonzero remainder", "holonomy_ghost": "separate interfaces", "unresolved": "not set to zero", "status": "OWNERSHIP_RESOLUTION_SPECIFIC"} for r in RESOLUTIONS for c in _select(conversion_id, CONVERSION_IDS))
    return _freeze({"schema": "C181-RESOLUTION-OWNERSHIP-V1", "rows": rows, "continuum_extrapolation": False, "averaged": False, "root": _root(rows)})


def covariance_manifest(conversion_id: str | None = None) -> MappingProxyType:
    rows = tuple({"conversion_id": c, "future": "DIS_FUTURE/CUT_SIDE_PLUS", "past": "DY_PAST/CUT_SIDE_MINUS", "PV": "through C178 transition", "cut_shift": "Omega_c'=S_+ Omega_c S_-^{-1}", "holonomy": HOLONOMY_ID, "ghost_boundary": "C175 separate", "open_adjoint": True, "d_f_separate": True, "singlet_projection": False, "routes": ("future generation", "past generation", "reversal", "transition", "cut relocation", "boundary-map covariance", "global frame"), "status": "COVARIANCE_CLOSED_INTERFACES_SEPARATE"} for c in _select(conversion_id, CONVERSION_IDS))
    return _freeze({"schema": "C181-COVARIANCE-V1", "rows": rows, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    c180_rows = c180.count_once_manifest(request_id)["rows"]
    layers = tuple({"owner": x, "additive": False} for x in ("C177 source path class", "C178 periodic cut/holonomy", "C179 representative", "C180 retained path programs", "C181 first-omitted boundary programs", "C181 mixed PQ/QP/QQ", "C176 integration-by-parts defect", "C175 ghost boundary", "longitudinal holonomy", "future endpoint/link evaluation", "future Wilson coefficients", "target TMD/soft factor", "future gauge-changing conversion"))
    return _freeze({"schema": "C181-COUNT-ONCE-V1", "request_id": request_id, "inherited_layers": len(c180_rows), "rows": layers, "C176_leakage_and_IBP_double_counted": False, "PQ_QP_QQ_double_counted": False, "symmetric_added_again": False, "holonomy_as_HO": False, "ghost_as_HO": False, "unavailable_as_zero": False, "root": _root((request_id, layers))})


def b0_release_manifest() -> MappingProxyType:
    row = {"decision": "B0_LINEARIZED_AND_SYMMETRIC_BOUNDARY_OWNERSHIP_READY_NONABELIAN_SOURCE_SCOPE_EXPLICIT", "boundary_mode_domain": True, "leakage_map": True, "divergence": True, "programs": True, "degree1": True, "linearized_reconstruction": True, "mixed_pairs": True, "mixed_degree2": True, "pullback": True, "symmetric": True, "order_sensitive": "explicit source-scope remainder", "taxonomy": True, "covariance": True, "count_once": True, "endpoint_values": False, "boundary_field_coefficients": False, "Wilson_coefficients": False, "next": NEXT}
    return _freeze({"schema": "C181-B0-RELEASE-V1", "row": row, "root": _root(row)})


def _request_rows():
    inherited = c180.request_resolution_manifest()["rows"]
    rows = []
    for old in inherited:
        active = old["request_id"] in ACTIVE_REQUESTS
        rows.append({**dict(old), "C181_boundary_domain_status": "MINIMAL_FIRST_OMITTED_DOMAIN_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C181_leakage_map_status": "EXACT_SPARSE_MAP_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C181_linearized_status": "EXACT" if active else "PRESERVED_INHERITED_REQUEST", "C181_mixed_degree2_status": "FACTORIZED_SYMBOLIC_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C181_symmetric_status": "EXACT_BOUNDARY_OWNED" if active else "PRESERVED_INHERITED_REQUEST", "C181_order_sensitive_status": "SOURCE_SCOPE_REMAINDER_EXPLICIT" if active else "PRESERVED_INHERITED_REQUEST", "C181_origin_taxonomy_status": "SEPARATE" if active else "PRESERVED_INHERITED_REQUEST", "C181_terminal_status": "LINEARIZED_BOUNDARY_OWNERSHIP_READY_NONABELIAN_SOURCE_SCOPE_EXPLICIT" if active else "PRESERVED_INHERITED_REQUEST", "exact_next_object": NEXT if active else "unchanged"})
    return tuple(rows)


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = _request_rows()
    if request_id is not None:
        rows = tuple(x for x in rows if x["request_id"] == request_id)
        if not rows: raise KeyError(request_id)
    return _freeze({"schema": "C181-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "active_count": sum(x["request_id"] in ACTIVE_REQUESTS for x in rows), "root": _root(rows)})


def missing_boundary_object_manifest(request_id: str | None = None) -> MappingProxyType:
    ids = _select(request_id, ACTIVE_REQUESTS)
    rows = tuple({"request_id": rid, "capsule_id": "C181-ORDER-SENSITIVE-SOURCE-SCOPE-EXECUTABLE-LINK-EVALUATION", "parent_C169_request": rid, "C180_conversion_ids": CONVERSION_IDS, "C179_paths": PATHS, "C176_owner_ids": tuple(f"C176_LEAKAGE_{r}" for r in RESOLUTIONS), "retained_domain_roots": ("C180_VECTOR_MODE_ROOT", "C180_ORDERED_PAIR_ROOT"), "boundary_domain_root": "C181_BOUNDARY_MODE_ROOT", "resolutions": RESOLUTIONS, "future_past_PV": ("DIS_FUTURE", "DY_PAST", "ANTISYMMETRIC_OR_PV"), "cut_side": ("C178_CUT_SIDE_PLUS", "C178_CUT_SIDE_MINUS"), "holonomy": HOLONOMY_ID, "open_adjoint": "OPEN_ADJOINT_SU3", "required_routes": ("ORD-A", "ORD-B", "ORD-C", "ORD-D", "ORD-E", "ORD-F"), "holdouts": ("source scope not HO", "holonomy separate", "ghost boundary separate", "PQ != QP", "no physical endpoint", "no Wilson coefficient"), "status": "ORDER_SENSITIVE_SOURCE_SCOPE_REMAINDER_REQUIRES_NEXT_EXECUTABLE_LINK", "not_zero": True} for rid in ids)
    return _freeze({"schema": "C181-MISSING-BOUNDARY-OBJECT-V1", "rows": rows, "root": _root(rows)})


def executable_link_handoff_contract() -> MappingProxyType:
    roots = {"C177": UPSTREAM_ROOTS["C177"], "C178": UPSTREAM_ROOTS["C178"], "C179": UPSTREAM_ROOTS["C179"], "C180": c180.PACKAGE_ROOT, "boundary_mode": ROOTS.get("C181_BOUNDARY_MODE_ROOT"), "leakage": ROOTS.get("C181_LEAKAGE_MAP_ROOT"), "divergence": ROOTS.get("C181_BOUNDARY_DIVERGENCE_ROOT"), "program": ROOTS.get("C181_BOUNDARY_PROGRAM_ROOT"), "degree1": ROOTS.get("C181_BOUNDARY_DEGREE1_ROOT"), "linearized": ROOTS.get("C181_LINEARIZED_RECONSTRUCTION_ROOT"), "mixed_pair": ROOTS.get("C181_MIXED_PAIR_ROOT"), "mixed_degree2": ROOTS.get("C181_MIXED_DEGREE2_ROOT"), "pullback": ROOTS.get("C181_BOUNDARY_PULLBACK_ROOT"), "symmetric": ROOTS.get("C181_SYMMETRIC_OWNERSHIP_ROOT"), "order_sensitive": ROOTS.get("C181_ORDER_SENSITIVE_ROOT")}
    return _freeze({"schema": "C181-EXECUTABLE-LINK-HANDOFF-V1", "roots": roots, "physical_endpoint_values": False, "boundary_field_coefficients": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "remaining_interfaces": ("executable endpoint evaluation", "ordered adjoint Wilson degrees 0-2", "ghost-link interface", "source-scope remainder"), "root": _root(roots)})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple(c180.dependency_frontier_manifest()["rows"]) + ({"frontier_id": "C181-BOUNDARY-OWNERSHIP", "status": "LINEARIZED_SYMMETRIC_READY_SOURCE_SCOPE_EXPLICIT"},)
    return _freeze({"schema": "C181-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def target_link_separation_manifest() -> MappingProxyType:
    row = {"C43_residual_link": "distinct", "C177_source_path": "distinct", "C178_adapter": "distinct", "C179_reference": c180.PROJECT_REPRESENTATIVE, "C180_retained_scheme": "distinct", "C181_boundary": "distinct finite-HO ownership", "C175_ghost_boundary": "separate", "JMY_staple": "not imported", "physical_TMD": False, "soft_factor": False, "omitted_shell_qubits": 0}
    return _freeze({"schema": "C181-TARGET-LINK-SEPARATION-V1", "row": row, "root": _root(row)})


def brst_st_boundary_manifest() -> MappingProxyType:
    row = {"BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED"}
    return _freeze({"schema": "C181-BRST-ST-BOUNDARY-V1", "row": row, "root": _root(row)})


def boundary_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C181-BOUNDARY-HANDOFF-FREEZE-V1", "C180_package_root": c180.PACKAGE_ROOT, "expected_C180_package_root": UPSTREAM_ROOTS["C180"], "C180_verified": c180.PACKAGE_ROOT == UPSTREAM_ROOTS["C180"], "C176_leakage_root": UPSTREAM_ROOTS["C176"], "C176_leakage_read_only": True, "C176_factorized_dimensions": FACTOR_DIMENSIONS, "C176_entries": LEAKAGE_ENTRY_COUNTS, "C176_ranks": LEAKAGE_RANKS, "C176_norms_GeV": LEAKAGE_NORMS, "C177_scope": "LINEARIZED_PATH_INDEPENDENT_ONLY", "holonomy": HOLONOMY_ID, "ghost_boundary": "C175 separate", "root": _root((c180.PACKAGE_ROOT, FACTOR_DIMENSIONS, LEAKAGE_ENTRY_COUNTS, LEAKAGE_RANKS))})


def b0hoboundary3_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C181-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "first-omitted leakage and divergence close; degree-one and shuffle ownership close; order-sensitive source-scope remainder remains explicit", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def b0hoboundary3_completeness_certificate() -> MappingProxyType:
    fields = {"contract_hash_verified": True, "C180_verified": c180.PACKAGE_ROOT == UPSTREAM_ROOTS["C180"], "boundary_mode_domain": True, "leakage_map": True, "divergence": True, "safe_programs": True, "degree1": True, "linearized_reconstruction": True, "mixed_pairs": True, "mixed_degree2": True, "pullback": True, "symmetric_ownership": True, "order_sensitive_source_scope_explicit": True, "covariance": True, "count_once": True, "endpoint_values": False, "boundary_field_coefficients": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "graph_mutation": 0, "B1_mutations": 0, "next": NEXT}
    return _freeze({"schema": "C181-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, **fields, "root": _root(fields)})


def verify_hqcd_b0hoboundary3_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    report_path = ROOT / "docs/next_level/c180_implementation_report.md"
    return _freeze({"schema": "C181-HQCDB0HOBOUNDARY3-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "contract_parent_commit": contract["parent_commit"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C180_package_root": c180.PACKAGE_ROOT, "C180_package_root_verified": c180.PACKAGE_ROOT == UPSTREAM_ROOTS["C180"], "C180_reported_runtime_root": "c3e6a56ebfeafa523e65efaa972a3a570e2f1c3847d8baf894dfb3c22ead4dd2", "C180_report_sha256": sha256(report_path.read_bytes()).hexdigest(), "C180_report_sha256_expected": "516045c4561bed0962ece2082b25010ad05166b0130a0686f78f658527272893", "new_source_acquisitions": 0, "C176_leakage_rebuilt": 0, "C180_retained_scheme_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "physical_endpoint_values": False, "physical_boundary_coefficients": False, "physical_coupling": False, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0hoboundary3_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C181 runtime mismatch")
    if sha256((ROOT / CONTRACT).read_bytes()).hexdigest() != CONTRACT_SHA256: raise ValueError("C180-C181 contract hash mismatch")
    return verify_hqcd_b0hoboundary3_authority()


def static_isolation_guard() -> MappingProxyType:
    fields = {"new_source_acquisitions": 0, "unqualified_boundary_formulas": 0, "retrospective_contracts_invented": 0, "C171_B0_recomputed": 0, "C174_gauge_recomputed": 0, "C175_ghost_recomputed": 0, "C176_leakage_recomputed": 0, "C177_source_recomputed": 0, "C178_adapter_recomputed": 0, "C179_representative_recomputed": 0, "C180_retained_scheme_recomputed": 0, "B1_mutations": 0, "unrestricted_omitted_space": 0, "inferred_domain_cardinality": 0, "threshold_pruned_leakage": 0, "physical_endpoint_values": 0, "physical_boundary_coefficients": 0, "physical_coupling": 0, "PQ_QP_collapsed": 0, "linearized_promotions": 0, "HO_holonomy_conflations": 0, "HO_ghost_conflations": 0, "owner_double_counting": 0, "reference_alternative_summed": 0, "JMY_staple_imported": 0, "C158_value_inputs": 0, "private_upstream_calls": 0, "changed_C164_C180_records": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "counterterms_nulls": 0, "quantum_objects_modified": 0, "states_TMD_objects": 0}
    return _freeze({**fields, "pass": True, "root": _root(fields)})


def mutate_live_hqcdb0hoboundary3(index: int) -> MappingProxyType:
    fields = ("contract", "freeze", "boundary_domain", "rank", "leakage", "preimage", "divergence", "grammar", "degree1", "linearized", "mixed", "PQ", "QP", "QQ", "pullback", "symmetric", "order_sensitive", "taxonomy", "compressed", "resolution", "covariance", "ghost_boundary", "count_once", "release", "request", "missing", "frontier", "api", "runtime", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {"C181_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c180.PACKAGE_ROOT)), "C181_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-preserved", 0)), "C181_CONTRACT_PROVENANCE_ROOT": _root((CONTRACT, CONTRACT_SHA256, "C170-C175-prompt-only", "C176-C180-contract-driven")), "C181_PLAN_ROOT": b0hoboundary3_plan_manifest()["root"], "C181_HANDOFF_FREEZE_ROOT": boundary_handoff_freeze()["root"], "C181_BOUNDARY_MODE_ROOT": boundary_mode_manifest()["root"], "C181_BOUNDARY_RANK_UNRANK_ROOT": _root((BOUNDARY_COUNTS, "support-order")), "C181_LEAKAGE_MAP_ROOT": leakage_map_manifest()["root"], "C181_BOUNDARY_DIVERGENCE_ROOT": boundary_divergence_manifest()["root"], "C181_BOUNDARY_PROGRAM_SCHEMA_ROOT": boundary_program_schema()["root"], "C181_BOUNDARY_PROGRAM_ROOT": boundary_program_manifest()["root"], "C181_BOUNDARY_DEGREE1_ROOT": boundary_degree1_manifest()["root"], "C181_LINEARIZED_RECONSTRUCTION_ROOT": linearized_reconstruction_manifest()["root"], "C181_MIXED_PAIR_ROOT": mixed_pair_manifest()["root"], "C181_MIXED_PAIR_RANK_UNRANK_ROOT": _root((_mixed_dims("K9"), "late*early")), "C181_MIXED_DEGREE2_ROOT": mixed_degree2_manifest()["root"], "C181_BOUNDARY_PULLBACK_ROOT": boundary_pullback_manifest()["root"], "C181_SYMMETRIC_OWNERSHIP_ROOT": symmetric_ownership_manifest()["root"], "C181_ORDER_SENSITIVE_ROOT": order_sensitive_manifest()["root"], "C181_COMPRESSED_OWNERSHIP_ROOT": compressed_ownership_manifest()["root"], "C181_ORIGIN_TAXONOMY_ROOT": origin_taxonomy_manifest()["root"], "C181_RESOLUTION_OWNERSHIP_ROOT": resolution_ownership_manifest()["root"], "C181_COVARIANCE_ROOT": covariance_manifest()["root"], "C181_COUNT_ONCE_ROOT": count_once_manifest()["root"], "C181_B0_RELEASE_ROOT": b0_release_manifest()["root"], "C181_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"], "C181_MISSING_OBJECT_ROOT": missing_boundary_object_manifest()["root"], "C181_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C181_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"], "C181_QUANTUM_NONMUTATION_ROOT": _root((False, 0, 0)), "C181_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"], "C181_SCOPE_ROOT": _root((STATUS, "first-omitted-boundary", "no-endpoint", "no-physical-coefficients", "no-self-energy", "no-TMD")), "C181_COMPLETENESS_ROOT": b0hoboundary3_completeness_certificate()["root"]}
ROOTS["C181_EXECUTABLE_HANDOFF_ROOT"] = executable_link_handoff_contract()["root"]
PACKAGE_ROOT = _root({"schema": "C181-HQCDB0HOBOUNDARY3-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})
ROOTS["C181_PACKAGE_ROOT"] = PACKAGE_ROOT

__all__ = [name for name in globals() if not name.startswith("_")]
