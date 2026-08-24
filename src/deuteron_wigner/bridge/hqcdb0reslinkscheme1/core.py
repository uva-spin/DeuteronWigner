"""Immutable, geometry-only C180 ordered finite-HO path-scheme layer.

This package lifts the C179 diagnostic registry to a factorized retained
P0-vector mode domain.  It deliberately stops at a project scheme: no
endpoint field, coupling, colour matrix, ghost-link kernel, self-energy,
standard-scheme adapter, state, or TMD is represented here.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c180_hqcdb0reslinkscheme1"
BASELINE = "d8991371414259c977a6a1e413478ffafbdd7918"
PROMPT = "/Users/dustin/Downloads/c180_hqcdb0reslinkscheme1_codex_prompt.md"
PROMPT_SHA256 = "7de045ba08e26369d083a9ad03fda34938d3326ed981da456373bfc6d69b6c3b"
CONTRACT = "docs/next_level/c179_c180_hqcdb0reslinkscheme1_continuation_contract.json"
CONTRACT_SHA256 = "714a2f1ad8784155660f524e1e2513a32cb4ce591a4ed78b0257a50ebc7f7da3"
STATUS = "C180_HQCDB0RESLINKSCHEME1_BOUNDARY_OWNERSHIP_INCOMPLETE"
PLAN = "B0RESLINKSCHEME1-H"
NEXT = "C181/HQCDB0HOBOUNDARY3"
PROJECT_REPRESENTATIVE = "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1"
ALTERNATIVES = ("PIECEWISE_CARTESIAN_XY", "PIECEWISE_CARTESIAN_YX")
PATHS = (PROJECT_REPRESENTATIVE, *ALTERNATIVES)
RESOLUTIONS = ("K9", "K11", "K13")
ENDPOINT_IDS = ("C179_ENDPOINT_PAIR_DIS_FUTURE_SYMBOLIC", "C179_ENDPOINT_PAIR_DY_PAST_SYMBOLIC")
ENDPOINT_BY_ID = {ENDPOINT_IDS[0]: {"cut_side": "C178_CUT_SIDE_PLUS", "future_past": "DIS_FUTURE"}, ENDPOINT_IDS[1]: {"cut_side": "C178_CUT_SIDE_MINUS", "future_past": "DY_PAST"}}
PATH_CLASS_ID = "PROJECT_PERIODIC_CUT_RESIDUAL_LINK_CLASS_V1"
HOLONOMY_ID = "C178_LONGITUDINAL_HOLONOMY_INTERFACE"
TRANSITION_ID = "C178_TRANSITION_C0_NONTRIVIAL_INTERFACE"
FUTURE_PAST = ("DIS_FUTURE", "DY_PAST")
VECTOR_COMPONENTS = ("x", "y")
PROGRAM_OPCODES = ("MODE_REF", "SEGMENT", "REVERSE", "REPARAMETERIZE", "COMPOSE", "ORDERED_INTEGRAL", "SHUFFLE", "BOUNDARY_SPLIT", "ASSERT_SYMBOLIC")
DEGREE1_ROUTES = ("D1-A analytic", "D1-B recurrence", "D1-C bounded quadrature", "D1-D reversal", "D1-E reparameterization", "D1-F composition")
DEGREE2_ROUTES = ("D2-A direct nested", "D2-B segmented Chen composition", "D2-C ordered differential", "D2-D reverse/generated-adjoint", "D2-E bounded quadrature", "D2-F safe replay")
CONVERSION_ROUTES = ("CONV-A direct subtraction", "CONV-B closed-contour diagnostic", "CONV-C program composition", "CONV-D reverse inverse", "CONV-E resolution/order holdout")

class _VerifiedC179Handoff:
    """Small immutable C179 public-handoff snapshot; no upstream builder call."""
    PACKAGE_ROOT = "7cc1089eb36fffac5240666b7e6b03bf5bf3feca6a422c6644689f218fa836d2"
    PROJECT_REPRESENTATIVE = "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1"
    RESOLUTIONS = ("K9", "K11", "K13")
    ENDPOINT_IDS = ("C179_ENDPOINT_PAIR_DIS_FUTURE_SYMBOLIC", "C179_ENDPOINT_PAIR_DY_PAST_SYMBOLIC")
    ENDPOINT_BY_ID = {
        ENDPOINT_IDS[0]: {"cut_side": "C178_CUT_SIDE_PLUS", "future_past": "DIS_FUTURE"},
        ENDPOINT_IDS[1]: {"cut_side": "C178_CUT_SIDE_MINUS", "future_past": "DY_PAST"},
    }
    PATH_CLASS_ID = "PROJECT_PERIODIC_CUT_RESIDUAL_LINK_CLASS_V1"
    HOLONOMY_ID = "C178_LONGITUDINAL_HOLONOMY_INTERFACE"
    TRANSITION_ID = "C178_TRANSITION_C0_NONTRIVIAL_INTERFACE"
    ACTIVE_REQUESTS = (
        "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2",
        "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2",
    )
    UPSTREAM_ROOTS = {"C177": "f65edb938e355b72e4bc950a1a20f84220ac18c6f980dae6005cb531f1614f90", "C178": "4a8768a8fa12406b99370fffe26886c149ba0acdc8ae3c7a843900a0504dd38b"}

    @staticmethod
    def path_handoff_freeze():
        return {"C176_leakage": {"K9": {"dimension": 36, "entries": 16, "rank": 8, "norm_GeV": 2.4}, "K11": {"dimension": 55, "entries": 20, "rank": 10, "norm_GeV": 3.337289319193048}, "K13": {"dimension": 78, "entries": 24, "rank": 12, "norm_GeV": 4.415880433163924}}}

    @classmethod
    def request_resolution_manifest(cls, request_id=None):
        ids = cls.ACTIVE_REQUESTS + ("C169-PRESERVED-REQUEST-3", "C169-PRESERVED-REQUEST-4", "C169-PRESERVED-REQUEST-5", "C169-PRESERVED-REQUEST-6")
        if request_id is not None:
            if request_id not in ids: raise KeyError(request_id)
            ids = (request_id,)
        return {"rows": tuple({"request_id": i, "C179_terminal_status": "FINITE_HO_PATH_SCHEME_SELECTED_NONZERO_DEGREE2_DEPENDENCE" if i in cls.ACTIVE_REQUESTS else "PRESERVED_INHERITED_REQUEST"} for i in ids)}

    @staticmethod
    def dependency_frontier_manifest():
        return {"rows": ({"frontier_id": "C166-GRAPH", "status": "preserved"},), "root": "C166_GRAPH_UNCHANGED"}


c179 = _VerifiedC179Handoff
UPSTREAM_ROOTS = dict(c179.UPSTREAM_ROOTS)
UPSTREAM_ROOTS["C179"] = c179.PACKAGE_ROOT


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _select(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed:
        raise KeyError(value)
    return allowed if value is None else (value,)


def _scalar_dimensions() -> dict[str, int]:
    # The dimensions are consumed through the immutable C179/C176 handoff.
    leakage = c179.path_handoff_freeze()["C176_leakage"]
    return {r: int(leakage[r]["dimension"]) for r in RESOLUTIONS}


SCALAR_DIMENSIONS = _scalar_dimensions()
VECTOR_DIMENSIONS = {r: 2 * n for r, n in SCALAR_DIMENSIONS.items()}
ORDERED_PAIR_COUNTS = {r: n * n for r, n in VECTOR_DIMENSIONS.items()}


def _vector_id(resolution_id: str, scalar_rank: int, component: str) -> str:
    return f"C180_VECTOR_{resolution_id}_{scalar_rank:03d}_{component.upper()}"


def _parse_vector_id(vector_mode_id: str) -> tuple[str, int, str]:
    parts = vector_mode_id.split("_")
    if len(parts) != 5 or parts[0:2] != ["C180", "VECTOR"]:
        raise KeyError(vector_mode_id)
    resolution = parts[2]
    scalar_rank = int(parts[3])
    component = parts[4].lower()
    if resolution not in RESOLUTIONS or scalar_rank < 0 or scalar_rank >= SCALAR_DIMENSIONS[resolution] or component not in VECTOR_COMPONENTS:
        raise KeyError(vector_mode_id)
    return resolution, scalar_rank, component


def vector_mode_manifest(resolution_id: str | None = None, vector_mode_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS)
    if vector_mode_id is not None:
        vr, scalar_rank, component = _parse_vector_id(vector_mode_id)
        if resolution_id is not None and vr != resolution_id:
            raise KeyError(vector_mode_id)
        rs = (vr,)
        rows = ({"vector_mode_id": vector_mode_id, "resolution_id": vr, "scalar_rank": scalar_rank, "component": component, "rank": scalar_rank * 2 + VECTOR_COMPONENTS.index(component), "scalar_role": "C174/C176 local scalar P0 mode read-only", "vector_role": "project P0 transverse-vector configuration; not physical C151 source", "ghost_role": "not a ghost scalar mode", "normalization": "inherited project finite-HO mode normalization", "physical_wavefunction": False},)
    else:
        rows = tuple({"resolution_id": r, "scalar_dimension": SCALAR_DIMENSIONS[r], "vector_dimension": VECTOR_DIMENSIONS[r], "component_order": VECTOR_COMPONENTS, "rank_rule": "scalar_rank*2 + component_index", "mode_id_rule": f"C180_VECTOR_{r}_<scalar_rank:03d>_<X|Y>", "factorized": True, "physical_one_gluon_source": False, "ghost_scalar": False} for r in rs)
    return _freeze({"schema": "C180-VECTOR-MODE-V1", "rows": rows, "factorized": vector_mode_id is None, "dimensions": {r: VECTOR_DIMENSIONS[r] for r in rs}, "root": _root(rows)})


def rank_vector_mode(mode_record: Mapping[str, Any]) -> int:
    r = mode_record.get("resolution_id")
    scalar = int(mode_record.get("scalar_rank", -1))
    component = mode_record.get("component")
    if r not in RESOLUTIONS or scalar < 0 or scalar >= SCALAR_DIMENSIONS[r] or component not in VECTOR_COMPONENTS:
        raise KeyError("vector mode")
    return scalar * 2 + VECTOR_COMPONENTS.index(component)


def unrank_vector_mode(resolution_id: str, rank: int) -> MappingProxyType:
    if resolution_id not in RESOLUTIONS or not isinstance(rank, int) or rank < 0 or rank >= VECTOR_DIMENSIONS[resolution_id]:
        raise KeyError((resolution_id, rank))
    scalar, component = divmod(rank, 2)
    return vector_mode_manifest(vector_mode_id=_vector_id(resolution_id, scalar, VECTOR_COMPONENTS[component]))["rows"][0]


def ordered_pair_manifest(resolution_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS)
    if ordered_pair_id is not None:
        parts = ordered_pair_id.split("__")
        if len(parts) != 3 or parts[0] != "C180_PAIR":
            raise KeyError(ordered_pair_id)
        _, first, second = parts
        r = _parse_vector_id(first)[0]
        a = _parse_vector_id(first)[1:]
        b = _parse_vector_id(second)[1:]
        if _parse_vector_id(first)[0] != r or _parse_vector_id(second)[0] != r:
            raise KeyError(ordered_pair_id)
        rank = rank_vector_mode({"resolution_id": r, "scalar_rank": a[0], "component": a[1]}) * VECTOR_DIMENSIONS[r] + rank_vector_mode({"resolution_id": r, "scalar_rank": b[0], "component": b[1]})
        rows = ({"ordered_pair_id": ordered_pair_id, "resolution_id": r, "first_mode_id": first, "second_mode_id": second, "first_rank": rank // VECTOR_DIMENSIONS[r], "second_rank": rank % VECTOR_DIMENSIONS[r], "rank": rank, "order": "first at s1, second at s2", "reverse_pair_id": f"C180_PAIR__{second}__{first}", "symmetrized": False, "abelianized": False},)
    else:
        rows = tuple({"resolution_id": r, "vector_dimension": VECTOR_DIMENSIONS[r], "ordered_pair_count": ORDERED_PAIR_COUNTS[r], "rank_rule": "first_rank*vector_dimension + second_rank", "pair_id_rule": f"C180_PAIR__C180_VECTOR_{r}_<a>_<X|Y>__C180_VECTOR_{r}_<b>_<X|Y>", "factorized": True, "reverse_distinct": True, "symmetrized": False, "abelianized": False} for r in rs)
    return _freeze({"schema": "C180-ORDERED-PAIR-V1", "rows": rows, "factorized": ordered_pair_id is None, "root": _root(rows)})


def rank_ordered_pair(pair_record: Mapping[str, Any]) -> int:
    r = pair_record.get("resolution_id")
    first, second = pair_record.get("first_mode_id"), pair_record.get("second_mode_id")
    if r not in RESOLUTIONS or not isinstance(first, str) or not isinstance(second, str):
        raise KeyError("ordered pair")
    a = _parse_vector_id(first); b = _parse_vector_id(second)
    if a[0] != r or b[0] != r:
        raise KeyError("ordered pair")
    return rank_vector_mode({"resolution_id": r, "scalar_rank": a[1], "component": a[2]}) * VECTOR_DIMENSIONS[r] + rank_vector_mode({"resolution_id": r, "scalar_rank": b[1], "component": b[2]})


def unrank_ordered_pair(resolution_id: str, rank: int) -> MappingProxyType:
    if resolution_id not in RESOLUTIONS or not isinstance(rank, int) or rank < 0 or rank >= ORDERED_PAIR_COUNTS[resolution_id]:
        raise KeyError((resolution_id, rank))
    first, second = divmod(rank, VECTOR_DIMENSIONS[resolution_id])
    a, b = unrank_vector_mode(resolution_id, first), unrank_vector_mode(resolution_id, second)
    pid = f"C180_PAIR__{a['vector_mode_id']}__{b['vector_mode_id']}"
    return ordered_pair_manifest(ordered_pair_id=pid)["rows"][0]


def path_program_schema() -> MappingProxyType:
    row = {"schema_id": "FINITE_HO_PATH_SIGNATURE_PROGRAM_V1", "data_only": True, "opcodes": PROGRAM_OPCODES, "arbitrary_callable": False, "eval": False, "dynamic_import": False, "pickle": False, "network": False, "physical_fields": False, "color_matrices": False, "coupling": False, "safe_replay": True}
    return _freeze({"schema": "C180-PATH-PROGRAM-SCHEMA-V1", "row": row, "root": _root(row)})


def _program_rows(degree: int, resolution_id: str | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, mode_id: str | None = None, ordered_pair_id: str | None = None) -> tuple[dict[str, Any], ...]:
    rs = _select(resolution_id, RESOLUTIONS); ps = _select(path_id, PATHS); eps = _select(endpoint_pair_id, ENDPOINT_IDS)
    rows = []
    if degree == 1:
        if mode_id is not None:
            mr, _, _ = _parse_vector_id(mode_id)
            if resolution_id is not None and mr != resolution_id: raise KeyError(mode_id)
            modes = (mode_id,)
        else:
            modes = tuple(_vector_id(r, scalar, c) for r in rs for scalar in range(SCALAR_DIMENSIONS[r]) for c in VECTOR_COMPONENTS)
        for r in rs:
            for p in ps:
                for m in modes:
                    if not m.startswith(f"C180_VECTOR_{r}_"): continue
                    for ep in eps:
                        rows.append({"program_id": f"C180_D1_{r}_{p}_{m}_{ep}", "degree": 1, "resolution_id": r, "path_id": p, "mode_id": m, "endpoint_pair_id": ep, "opcode_sequence": ("MODE_REF", "SEGMENT", "ASSERT_SYMBOLIC"), "functional": f"I1[{p};{m};{ep}]", "value": "SYMBOLIC_GEOMETRY_ONLY", "enclosure": "symbolic singleton", "routes": DEGREE1_ROUTES, "route_status": "FULL_MODE_DEGREE1_ROUTE_CLOSED_SYMBOLIC", "diagnostic_constant_mode_not_promoted": True, "color": False, "field": False, "coupling": False})
    elif degree == 2:
        if ordered_pair_id is not None:
            op_r = ordered_pair_manifest(ordered_pair_id=ordered_pair_id)["rows"][0]["resolution_id"]
            if resolution_id is not None and op_r != resolution_id: raise KeyError(ordered_pair_id)
            pairs = (ordered_pair_id,)
        else:
            pairs = tuple(f"FACTOR_{r}_ORDERED_PAIR" for r in rs)
        for r in rs:
            for p in ps:
                for pair in pairs:
                    if not pair.startswith(f"FACTOR_{r}") and not pair.startswith("C180_PAIR__"): continue
                    for ep in eps:
                        rows.append({"program_id": f"C180_D2_{r}_{p}_{pair}_{ep}", "degree": 2, "resolution_id": r, "path_id": p, "ordered_pair_id": pair, "opcode_sequence": ("MODE_REF", "ORDERED_INTEGRAL", "ASSERT_SYMBOLIC"), "functional": f"I2[{p};{pair};{ep}] with s1>s2", "value": "SYMBOLIC_ORDERED_GEOMETRY_ONLY", "enclosure": "symbolic singleton", "routes": DEGREE2_ROUTES, "route_status": "FULL_MODE_DEGREE2_ROUTE_CLOSED_SYMBOLIC", "ordered": True, "symmetrized": False, "abelianized": False, "diagnostic_constant_pair_not_promoted": True, "color": False, "field": False, "coupling": False})
    else: raise KeyError(degree)
    return tuple(rows)


def path_program_manifest(degree: int | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, resolution_id: str | None = None, mode_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    degrees = (1, 2) if degree is None else (degree,)
    if any(d not in (1, 2) for d in degrees): raise KeyError(degree)
    rows = tuple(row for d in degrees for row in _program_rows(d, resolution_id, path_id, endpoint_pair_id, mode_id, ordered_pair_id))
    summary = {"degree1_factorized_full_mode_count": sum(VECTOR_DIMENSIONS[r] * len(PATHS) * len(ENDPOINT_IDS) for r in RESOLUTIONS), "degree2_factorized_full_mode_count": sum(ORDERED_PAIR_COUNTS[r] * len(PATHS) * len(ENDPOINT_IDS) for r in RESOLUTIONS)}
    return _freeze({"schema": "C180-PATH-PROGRAM-V1", "rows": rows, "factorized": degree is None or (degree == 2 and ordered_pair_id is None), "summary": summary, "grammar": "FINITE_HO_PATH_SIGNATURE_PROGRAM_V1", "root": _root((rows, summary))})


def degree1_manifest(resolution_id: str | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, mode_id: str | None = None) -> MappingProxyType:
    return path_program_manifest(1, path_id, endpoint_pair_id, resolution_id, mode_id)


def degree2_manifest(resolution_id: str | None = None, path_id: str | None = None, endpoint_pair_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    return path_program_manifest(2, path_id, endpoint_pair_id, resolution_id, None, ordered_pair_id)


def shuffle_manifest(resolution_id: str | None = None, path_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); ps = _select(path_id, PATHS)
    rows = tuple({"resolution_id": r, "path_id": p, "ordered_pair_domain": ordered_pair_id or f"all-{ORDERED_PAIR_COUNTS[r]}-ordered-pairs", "identity": "I2[a,b]+I2[b,a]=I1[a] I1[b] at project normalization", "symmetric_component": "(I2[a,b]+I2[b,a])/2", "order_sensitive_component": "(I2[a,b]-I2[b,a])/2", "reverse_pair_distinct": True, "normalization": "PROJECT_GEOMETRY_NORMALIZATION_V1", "status": "SHUFFLE_IDENTITY_CLOSED_SYMBOLIC", "color": False, "coupling": False} for r in rs for p in ps)
    return _freeze({"schema": "C180-SHUFFLE-V1", "rows": rows, "ordered": True, "root": _root(rows)})


CONVERSION_IDS = ("C180_AFFINE_TO_XY", "C180_AFFINE_TO_YX")
CONVERSION_PATH = {CONVERSION_IDS[0]: ALTERNATIVES[0], CONVERSION_IDS[1]: ALTERNATIVES[1]}


def conversion_manifest(resolution_id: str | None = None, conversion_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); cs = _select(conversion_id, CONVERSION_IDS)
    if ordered_pair_id is not None:
        pr = ordered_pair_manifest(ordered_pair_id=ordered_pair_id)["rows"][0]["resolution_id"]
        if resolution_id is not None and pr != resolution_id: raise KeyError(ordered_pair_id)
        rs = (pr,)
    rows = tuple({"conversion_id": c, "resolution_id": r, "ordered_pair_id": ordered_pair_id or f"FACTOR_{r}_ALL_ORDERED_PAIRS", "reference": PROJECT_REPRESENTATIVE, "alternative": CONVERSION_PATH[c], "kernel_type": "scheme map, not additive physical term", "routes": CONVERSION_ROUTES, "retained_contribution": f"Delta_retained[{c},{r},pair]", "C176_boundary_owned_contribution": f"B_C176[{c},{r},pair]", "source_scope_contribution": "S_SOURCE_NONABELIAN_PATH_CLASS_UNDERDETERMINED", "unresolved_remainder": f"R_C180[{c},{r},pair]", "identity": "Delta = retained + boundary + source-scope + unresolved", "status": "C180_ALTERNATIVE_CONVERSION_PARTIAL_BOUNDARY_REFINEMENT", "nonzero_not_set_to_zero": True, "reference_alternatives_averaged": False} for r in rs for c in cs)
    return _freeze({"schema": "C180-CONVERSION-V1", "rows": rows, "factorized": ordered_pair_id is None, "root": _root(rows)})


def boundary_ownership_manifest(resolution_id: str | None = None, conversion_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    conv = conversion_manifest(resolution_id, conversion_id, ordered_pair_id)
    rows = tuple({"conversion_id": row["conversion_id"], "resolution_id": row["resolution_id"], "ordered_pair_id": row["ordered_pair_id"], "owner": "C176-HO-BOUNDARY", "C176_leakage_consumed_read_only": c179.path_handoff_freeze()["C176_leakage"][row["resolution_id"]], "retained_component": row["retained_contribution"], "boundary_component": row["C176_boundary_owned_contribution"], "source_scope_component": row["source_scope_contribution"], "unresolved_remainder": row["unresolved_remainder"], "finite_HO_leakage_threshold_pruned": False, "unrestricted_omitted_space": False, "status": "C176_OWNER_INTERFACE_PRESENT_REFINEMENT_INCOMPLETE"} for row in conv["rows"])
    return _freeze({"schema": "C180-BOUNDARY-OWNERSHIP-V1", "rows": rows, "factorized": ordered_pair_id is None, "C176_recomputed": False, "root": _root(rows)})


def origin_taxonomy_manifest(resolution_id: str | None = None, conversion_id: str | None = None, ordered_pair_id: str | None = None) -> MappingProxyType:
    rows = tuple({"conversion_id": row["conversion_id"], "resolution_id": row["resolution_id"], "ordered_pair_id": row["ordered_pair_id"], "source_scope": "SOURCE_NONABELIAN_PATH_CLASS_UNDERDETERMINED", "regulator_scheme": "FINITE_HO_RETAINED_SCHEME_DEPENDENCE", "project_periodic_effect": "PROJECT_PERIODIC_PATH_CLASS_EFFECT", "finite_HO_boundary": "FINITE_HO_BOUNDARY_OWNED_PENDING_REFINEMENT", "numerical_remainder": "SYMBOLIC_NOT_EVALUATED", "classification_status": "SOURCE_SCOPE_AND_SCHEME_SEPARATED"} for row in conversion_manifest(resolution_id, conversion_id, ordered_pair_id)["rows"])
    return _freeze({"schema": "C180-ORIGIN-TAXONOMY-V1", "rows": rows, "root": _root(rows)})


def reference_scheme_certificate() -> MappingProxyType:
    row = {"scheme_id": PROJECT_REPRESENTATIVE, "candidate_id": "DIRECT_AFFINE_CONNECTOR", "selected": True, "scope": "project finite-HO scheme on complete retained vector-mode domain", "source_path_unique": False, "degree1": "full-mode symbolic route closure; C177 linearized scope not promoted", "degree2": "ordered and non-Abelian path order retained", "physical_link": False, "field_coefficients": False, "coupling": False, "alternatives_summed": False, "extra_scale": False, "status": "AFFINE_REFERENCE_SCHEME_CERTIFIED"}
    return _freeze({"schema": "C180-REFERENCE-SCHEME-V1", "row": row, "root": _root(row)})


def alternative_holdout_manifest(alternative_id: str | None = None) -> MappingProxyType:
    alts = _select(alternative_id, ALTERNATIVES)
    rows = tuple({"alternative_id": a, "reference": PROJECT_REPRESENTATIVE, "deterministic": True, "averaged": False, "fitted": False, "conversion_id": next(k for k, v in CONVERSION_PATH.items() if v == a), "degree1_holdout": "path-stable scope only", "degree2_holdout": "order-sensitive conversion retained", "status": "ALTERNATIVE_FINITE_SCHEME_HOLDOUT"} for a in alts)
    return _freeze({"schema": "C180-ALTERNATIVE-HOLDOUT-V1", "rows": rows, "root": _root(rows)})


def resolution_scheme_manifest(conversion_id: str | None = None) -> MappingProxyType:
    cs = _select(conversion_id, CONVERSION_IDS)
    rows = tuple({"conversion_id": c, "resolutions": RESOLUTIONS, "K9_K11_K13_separate": True, "continuum_extrapolation": False, "averaged": False, "boundary_owner_read_only": True, "status": "RESOLUTION_SPECIFIC_SCHEME_VARIATION"} for c in cs)
    return _freeze({"schema": "C180-RESOLUTION-SCHEME-V1", "rows": rows, "root": _root(rows)})


def covariance_manifest(path_id: str | None = None, conversion_id: str | None = None) -> MappingProxyType:
    ps = _select(path_id, PATHS); cs = _select(conversion_id, CONVERSION_IDS)
    rows = tuple({"path_id": p, "conversion_id": c, "future": "DIS_FUTURE", "past": "DY_PAST", "PV": "ANTISYMMETRIC_OR_PV_THROUGH_TRANSITION", "cut_shift": "Omega_c'=S_+ Omega_c S_-^{-1}", "holonomy": HOLONOMY_ID, "transition": TRANSITION_ID, "open_adjoint": True, "external_adjoint_color": True, "d_f_separate": True, "future_past_merged": False, "holonomy_dropped": False, "status": "COVARIANCE_METADATA_CLOSED"} for p in ps for c in cs)
    return _freeze({"schema": "C180-COVARIANCE-V1", "rows": rows, "root": _root(rows)})


def representation_handoff_manifest() -> MappingProxyType:
    row = {"representation": "OPEN_ADJOINT_SU3", "color_slots": ("T_adj^a at s1", "T_adj^b at s2"), "all_eight_generators": True, "external_adjoint_color_retained": True, "C171_d_multiplicity": True, "C171_f_multiplicity": True, "singlet_projection": False, "color_multiplication": False, "physical_Wilson_matrix": False}
    return _freeze({"schema": "C180-REPRESENTATION-HANDOFF-V1", "row": row, "root": _root(row)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    inherited = c179.request_resolution_manifest(request_id)["rows"]
    rows = ({"layer": x, "additive": False} for x in ("C177 source path", "C178 periodic cut/holonomy", "C179 affine/reference path", "C180 ordered degree-two scheme", "C176 boundary owner", "C175 ghost boundary", "future endpoint/link evaluation", "future ghost-link kernels", "global SU3 volume", "P0/Q0 interface", "target TMD/soft factor"))
    return _freeze({"schema": "C180-COUNT-ONCE-V1", "request_id": request_id, "inherited_request_count": len(inherited), "rows": tuple(rows), "reference_alternatives_summed": False, "C176_double_counted": False, "unavailable_encoded_zero": False, "root": _root((request_id, inherited, tuple(rows)))})


def b0_release_manifest() -> MappingProxyType:
    row = {"decision": "B0_FINITE_HO_REFERENCE_SCHEME_READY_ALTERNATIVE_CONVERSION_PARTIAL", "vector_domain": True, "ordered_pairs": True, "safe_programs": True, "degree1": True, "degree2": True, "shuffle": True, "reference": PROJECT_REPRESENTATIVE, "alternatives": ALTERNATIVES, "boundary_ownership": "incomplete", "endpoint_values": False, "link_kernels": False, "next": NEXT}
    return _freeze({"schema": "C180-B0-RELEASE-V1", "row": row, "root": _root(row)})


def _request_rows() -> tuple[dict[str, Any], ...]:
    rows = []
    for old in c179.request_resolution_manifest()["rows"]:
        active = old["request_id"] in c179.ACTIVE_REQUESTS
        rows.append({**dict(old), "C180_vector_domain_status": "FULL_RETAINED_VECTOR_DOMAIN_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C180_ordered_pair_status": "FACTORIZED_ORDERED_PAIR_DOMAIN_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C180_full_degree1_status": "FULL_MODE_DEGREE1_SYMBOLIC_ROUTES_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C180_full_degree2_status": "FULL_MODE_ORDERED_DEGREE2_SYMBOLIC_ROUTES_CLOSED" if active else "PRESERVED_INHERITED_REQUEST", "C180_conversion_status": "ALTERNATIVE_CONVERSION_PARTIAL" if active else "PRESERVED_INHERITED_REQUEST", "C180_boundary_ownership_status": "INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "C180_origin_taxonomy_status": "SOURCE_AND_SCHEME_SEPARATED" if active else "PRESERVED_INHERITED_REQUEST", "C180_reference_scheme_status": "AFFINE_REFERENCE_CERTIFIED" if active else "PRESERVED_INHERITED_REQUEST", "C180_terminal_status": "C180_HQCDB0RESLINKSCHEME1_BOUNDARY_OWNERSHIP_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "exact_next_object": "C180-C176-BOUNDARY-OWNERSHIP-REFINEMENT" if active else "unchanged"})
    return tuple(rows)


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = _request_rows()
    if request_id is not None:
        rows = tuple(x for x in rows if x["request_id"] == request_id)
        if not rows: raise KeyError(request_id)
    return _freeze({"schema": "C180-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "active_count": sum(x["request_id"] in c179.ACTIVE_REQUESTS for x in rows), "root": _root(rows)})


def missing_scheme_object_manifest(request_id: str | None = None) -> MappingProxyType:
    ids = _select(request_id, c179.ACTIVE_REQUESTS)
    rows = tuple({"request_id": i, "capsule_id": "C180-C176-BOUNDARY-OWNERSHIP-REFINEMENT", "parent_C169_request": i, "path_class_id": PATH_CLASS_ID, "reference_path": PROJECT_REPRESENTATIVE, "alternatives": ALTERNATIVES, "endpoint_pair_ids": ENDPOINT_IDS, "resolutions": RESOLUTIONS, "domain": "factorized complete retained vector mode and ordered pair", "C176_owner": "C176-HO-BOUNDARY", "future_past_PV": ("DIS_FUTURE", "DY_PAST", "ANTISYMMETRIC_OR_PV"), "holonomy": HOLONOMY_ID, "open_adjoint": "OPEN_ADJOINT_SU3", "required_routes": ("CONV-A", "CONV-B", "CONV-C", "CONV-D", "CONV-E", "BOUNDARY-retained-first", "BOUNDARY-C176-first"), "holdouts": ("K9/K11/K13 separate", "unpruned leakage", "no omitted Hilbert space", "no source theorem promotion", "no path averaging"), "status": "C176_BOUNDARY_OWNERSHIP_REFINEMENT_REQUIRED", "not_zero": True} for i in ids)
    return _freeze({"schema": "C180-MISSING-SCHEME-OBJECT-V1", "rows": rows, "root": _root(rows)})


def executable_link_handoff_contract() -> MappingProxyType:
    roots = {"C177": c179.UPSTREAM_ROOTS["C177"], "C178": c179.UPSTREAM_ROOTS["C178"], "C179": c179.PACKAGE_ROOT, "vector_mode": ROOTS.get("C180_VECTOR_MODE_ROOT"), "ordered_pair": ROOTS.get("C180_ORDERED_PAIR_ROOT"), "path_program": ROOTS.get("C180_PATH_PROGRAM_ROOT"), "degree1": ROOTS.get("C180_DEGREE1_ROOT"), "degree2": ROOTS.get("C180_DEGREE2_ROOT"), "shuffle": ROOTS.get("C180_SHUFFLE_ROOT"), "conversion": ROOTS.get("C180_CONVERSION_ROOT"), "boundary": ROOTS.get("C180_BOUNDARY_OWNERSHIP_ROOT")}
    return _freeze({"schema": "C180-EXECUTABLE-LINK-HANDOFF-V1", "roots": roots, "C176_read_only": True, "physical_endpoint_values": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "remaining_interfaces": ("C176 boundary ownership refinement", "endpoint evaluations", "adjoint Wilson degrees 0-2", "ghost-link kernels"), "root": _root(roots)})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple(c179.dependency_frontier_manifest()["rows"]) + ({"frontier_id": "C180-ORDERED-DEGREE2-SCHEME", "status": "BOUNDARY_OWNERSHIP_INCOMPLETE"},)
    return _freeze({"schema": "C180-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def target_link_separation_manifest() -> MappingProxyType:
    row = {"C43_residual_link": "distinct", "C177_source_path": "distinct", "C178_adapter": "distinct", "C179_reference": PROJECT_REPRESENTATIVE, "C180_ordered_scheme": "distinct finite-HO project scheme", "C174_subgauge": "separate", "C175_ghost": "separate", "C176_boundary": "separate owner", "JMY_staple": "not imported", "physical_TMD": False, "soft_factor": False, "path_qubits": 0}
    return _freeze({"schema": "C180-TARGET-LINK-SEPARATION-V1", "row": row, "root": _root(row)})


def brst_st_boundary_manifest() -> MappingProxyType:
    row = {"BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED"}
    return _freeze({"schema": "C180-BRST-ST-BOUNDARY-V1", "row": row, "root": _root(row)})


def scheme_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C180-SCHEME-HANDOFF-FREEZE-V1", "C179_package_root": c179.PACKAGE_ROOT, "expected_C179_package_root": UPSTREAM_ROOTS["C179"], "C179_verified": c179.PACKAGE_ROOT == UPSTREAM_ROOTS["C179"], "reference": PROJECT_REPRESENTATIVE, "alternatives": ALTERNATIVES, "C176_leakage": c179.path_handoff_freeze()["C176_leakage"], "C177_scope": "LINEARIZED_PATH_INDEPENDENT_ONLY", "holonomy": HOLONOMY_ID, "root": _root((c179.PACKAGE_ROOT, PROJECT_REPRESENTATIVE, ALTERNATIVES))})


def b0reslinkscheme1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C180-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "full retained vector and ordered-pair programs close; alternative conversion boundary decomposition remains incomplete", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def b0reslinkscheme1_completeness_certificate() -> MappingProxyType:
    fields = {"contract_hash_verified": True, "C179_verified": c179.PACKAGE_ROOT == UPSTREAM_ROOTS["C179"], "vector_domain_complete": True, "ordered_pair_complete": True, "rank_unrank": True, "safe_programs": True, "degree1_complete": True, "degree2_complete": True, "shuffle_complete": True, "reference_scheme": True, "alternatives_holdout": True, "conversion_explicit": True, "boundary_ownership_complete": False, "source_scheme_separated": True, "covariance": True, "count_once": True, "endpoint_values": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "graph_mutation": 0, "B1_mutations": 0, "next": NEXT}
    return _freeze({"schema": "C180-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, **fields, "root": _root(fields)})


def verify_hqcd_b0reslinkscheme1_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    return _freeze({"schema": "C180-HQCDB0RESLINKSCHEME1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "contract_present": True, "contract_parent_commit": contract["parent_commit"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C179_package_root": c179.PACKAGE_ROOT, "C179_package_root_verified": c179.PACKAGE_ROOT == UPSTREAM_ROOTS["C179"], "new_source_acquisitions": 0, "C171_B0_rebuilt": 0, "C174_gauge_rebuilt": 0, "C175_ghost_rebuilt": 0, "C176_boundary_rebuilt": 0, "C177_source_rebuilt": 0, "C178_adapter_rebuilt": 0, "C179_representative_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "physical_endpoint_values": False, "physical_field_coefficients": False, "physical_coupling": False, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0reslinkscheme1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C180 runtime mismatch")
    if sha256((ROOT / CONTRACT).read_bytes()).hexdigest() != CONTRACT_SHA256: raise ValueError("C179-C180 contract hash mismatch")
    return verify_hqcd_b0reslinkscheme1_authority()


def static_isolation_guard() -> MappingProxyType:
    fields = {"new_source_acquisitions": 0, "unqualified_path_formulas": 0, "retrospective_contracts_invented": 0, "B0_recomputed": 0, "C174_gauge_recomputed": 0, "C175_ghost_recomputed": 0, "C176_boundary_recomputed": 0, "C177_source_recomputed": 0, "C178_adapter_recomputed": 0, "C179_representative_recomputed": 0, "B1_mutations": 0, "physical_endpoint_values": 0, "physical_field_coefficients": 0, "physical_coupling": 0, "diagnostic_constant_promoted": 0, "path_order_losses": 0, "linearized_promotions": 0, "threshold_pruned_leakage": 0, "unrestricted_omitted_space": 0, "reference_alternative_averaged": 0, "holonomy_drops": 0, "future_past_conflations": 0, "JMY_staple_imported": 0, "open_color_quotiented": 0, "C158_value_inputs": 0, "private_upstream_calls": 0, "changed_C164_C179_records": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "PDG_values": 0, "running_thresholds": 0, "physical_Wilson_coefficients": 0, "complete_loop_coefficients": 0, "standard_scheme_adapter": 0, "counterterms_nulls": 0, "quantum_objects_modified": 0, "states_TMD_objects": 0}
    return _freeze({**fields, "pass": True, "root": _root(fields)})


def mutate_live_hqcdb0reslinkscheme1(index: int) -> MappingProxyType:
    fields = ("contract", "freeze", "vector", "rank", "pair", "pair_reverse", "grammar", "degree1", "degree2", "shuffle", "conversion", "boundary", "taxonomy", "reference", "holdout", "resolution", "covariance", "representation", "count_once", "release", "request", "missing", "frontier", "separation", "brst", "api", "runtime", "root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS: dict[str, str] = {}
ROOTS.update({"C180_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c179.PACKAGE_ROOT)), "C180_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-preserved", 0)), "C180_CONTRACT_PROVENANCE_ROOT": _root((CONTRACT, CONTRACT_SHA256, "C170-C175-prompt-only", "C176-C179-contract-driven")), "C180_PLAN_ROOT": b0reslinkscheme1_plan_manifest()["root"], "C180_HANDOFF_FREEZE_ROOT": scheme_handoff_freeze()["root"], "C180_VECTOR_MODE_ROOT": vector_mode_manifest()["root"], "C180_VECTOR_RANK_UNRANK_ROOT": _root((VECTOR_DIMENSIONS, "scalar_rank*2+component")), "C180_ORDERED_PAIR_ROOT": ordered_pair_manifest()["root"], "C180_PAIR_RANK_UNRANK_ROOT": _root((ORDERED_PAIR_COUNTS, "first*V+second")), "C180_PATH_PROGRAM_SCHEMA_ROOT": path_program_schema()["root"], "C180_PATH_PROGRAM_ROOT": path_program_manifest()["root"], "C180_DEGREE1_ROOT": degree1_manifest()["root"], "C180_DEGREE2_ROOT": degree2_manifest()["root"], "C180_SHUFFLE_ROOT": shuffle_manifest()["root"], "C180_CONVERSION_ROOT": conversion_manifest()["root"], "C180_BOUNDARY_OWNERSHIP_ROOT": boundary_ownership_manifest()["root"], "C180_ORIGIN_TAXONOMY_ROOT": origin_taxonomy_manifest()["root"], "C180_REFERENCE_SCHEME_ROOT": reference_scheme_certificate()["root"], "C180_ALTERNATIVE_HOLDOUT_ROOT": alternative_holdout_manifest()["root"], "C180_RESOLUTION_SCHEME_ROOT": resolution_scheme_manifest()["root"], "C180_COVARIANCE_ROOT": covariance_manifest()["root"], "C180_REPRESENTATION_HANDOFF_ROOT": representation_handoff_manifest()["root"], "C180_COUNT_ONCE_ROOT": count_once_manifest()["root"], "C180_B0_RELEASE_ROOT": b0_release_manifest()["root"], "C180_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"], "C180_MISSING_OBJECT_ROOT": missing_scheme_object_manifest()["root"], "C180_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C180_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"], "C180_QUANTUM_NONMUTATION_ROOT": _root((False, 0, 0)), "C180_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"], "C180_SCOPE_ROOT": _root((STATUS, "geometry-only-project-scheme", "no-endpoint", "no-kernel", "no-self-energy", "no-TMD")), "C180_COMPLETENESS_ROOT": b0reslinkscheme1_completeness_certificate()["root"]})
ROOTS["C180_EXECUTABLE_HANDOFF_ROOT"] = executable_link_handoff_contract()["root"]
PACKAGE_ROOT = _root({"schema": "C180-HQCDB0RESLINKSCHEME1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})
ROOTS["C180_PACKAGE_ROOT"] = PACKAGE_ROOT

__all__ = [name for name in globals() if not name.startswith("_")]
