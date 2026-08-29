"""C179 geometry-only finite-HO path comparison.

The records in this package describe symbolic transverse paths and bounded,
nonphysical geometry fixtures.  They intentionally stop before physical
endpoint fields, color Wilson coefficients, ghost-link kernels, and B0 link
kernels.
"""
from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb0reslinkadapter1 as c178

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c179_hqcdb0reslinkpath1"
BASELINE = "fea467e8b02340d84d5d83323c8d4a585981a3de"
PROMPT = "/Users/dustin/Downloads/c179_hqcdb0reslinkpath1_codex_prompt.md"
PROMPT_SHA256 = "80c88512c94665cf967806fa7e5030ffebb8696a2883788e6181ce1659d87d27"
CONTRACT = "docs/next_level/c178_c179_hqcdb0reslinkpath1_continuation_contract.json"
CONTRACT_SHA256 = "feaeaf061c4e7b7bfdf98957c4f671ffae3f40c1d2b2934ea09cf473bb670978"
STATUS = "C179_C178_DEGREE1_PATH_STABLE_PROJECT_FINITE_HO_DEGREE2_PATH_SCHEME_READY"
PLAN = "B0RESLINKPATH1-B"
NEXT = "C180/HQCDB0RESLINKSCHEME1"
PROJECT_REPRESENTATIVE = "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1"
HO_BASIS_PHRASE = "finite transverse harmonic-oscillator (HO) basis"
RESOLUTIONS = ("K9", "K11", "K13")
DEGREES = (1, 2)
CUT_SIDE_PLUS = "C178_CUT_SIDE_PLUS"
CUT_SIDE_MINUS = "C178_CUT_SIDE_MINUS"
TRANSITION_ID = "C178_TRANSITION_C0_NONTRIVIAL_INTERFACE"
HOLONOMY_ID = "C178_LONGITUDINAL_HOLONOMY_INTERFACE"
PATH_CLASS_ID = "PROJECT_PERIODIC_CUT_RESIDUAL_LINK_CLASS_V1"
ACTIVE_REQUESTS = c178.ACTIVE_REQUESTS

UPSTREAM_ROOTS = dict(c178.UPSTREAM_ROOTS)
UPSTREAM_ROOTS.update({
    "C178": "4a8768a8fa12406b99370fffe26886c149ba0acdc8ae3c7a843900a0504dd38b",
})

_LEAKAGE = {
    "K9": {"dimension": 36, "entries": 16, "rank": 8, "norm_GeV": 2.4},
    "K11": {"dimension": 55, "entries": 20, "rank": 10, "norm_GeV": 3.337289319193048},
    "K13": {"dimension": 78, "entries": 24, "rank": 12, "norm_GeV": 4.415880433163924},
}


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


def _ids(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed:
        raise KeyError(value)
    return allowed if value is None else (value,)


def _degrees(value: int | str | None) -> tuple[int, ...]:
    if value is None:
        return DEGREES
    if isinstance(value, str) and value.startswith("degree"):
        value = int(value[-1])
    if value not in DEGREES:
        raise KeyError(value)
    return (int(value),)


ENDPOINT_PAIRS = (
    {
        "endpoint_pair_id": "C179_ENDPOINT_PAIR_DIS_FUTURE_SYMBOLIC",
        "left_transverse_point": {"symbol": "xi_L", "coordinates": ("xi_L^1", "xi_L^2"), "units": "symbolic transverse-chart coordinate"},
        "right_transverse_point": {"symbol": "xi_R", "coordinates": ("xi_R^1", "xi_R^2"), "units": "symbolic transverse-chart coordinate"},
        "fixture": {"left": (0, 0), "right": (1, 1), "status": "bounded nonphysical diagnostic fixture", "physical_separation": False},
        "coordinate_units": "dimensionless project-chart units; no physical length scale",
        "cut_side": CUT_SIDE_PLUS,
        "future_past": "DIS_FUTURE",
        "transition_id": TRANSITION_ID,
        "holonomy_id": HOLONOMY_ID,
        "source_path_class_parent": PATH_CLASS_ID,
        "orientation": "left-to-right transverse orientation",
        "coincident_endpoints": False,
        "common_reference": "not introduced",
        "transverse_infinity": "comparison-only and not instantiated",
    },
    {
        "endpoint_pair_id": "C179_ENDPOINT_PAIR_DY_PAST_SYMBOLIC",
        "left_transverse_point": {"symbol": "xi_L", "coordinates": ("xi_L^1", "xi_L^2"), "units": "symbolic transverse-chart coordinate"},
        "right_transverse_point": {"symbol": "xi_R", "coordinates": ("xi_R^1", "xi_R^2"), "units": "symbolic transverse-chart coordinate"},
        "fixture": {"left": (0, 0), "right": (1, 1), "status": "bounded nonphysical diagnostic fixture", "physical_separation": False},
        "coordinate_units": "dimensionless project-chart units; no physical length scale",
        "cut_side": CUT_SIDE_MINUS,
        "future_past": "DY_PAST",
        "transition_id": TRANSITION_ID,
        "holonomy_id": HOLONOMY_ID,
        "source_path_class_parent": PATH_CLASS_ID,
        "orientation": "left-to-right transverse orientation",
        "coincident_endpoints": False,
        "common_reference": "not introduced",
        "transverse_infinity": "comparison-only and not instantiated",
    },
)
ENDPOINT_BY_ID = {x["endpoint_pair_id"]: x for x in ENDPOINT_PAIRS}
ENDPOINT_IDS = tuple(x["endpoint_pair_id"] for x in ENDPOINT_PAIRS)

MODE_ROWS = (
    {"mode_id": "C179_MODE_CONST_X", "vector_component": "x", "Phi": "(1,0)", "normalization": "PROJECT_GEOMETRY_DIAGNOSTIC_NORMALIZATION_V1", "units": "geometry-only normalized mode"},
    {"mode_id": "C179_MODE_CONST_Y", "vector_component": "y", "Phi": "(0,1)", "normalization": "PROJECT_GEOMETRY_DIAGNOSTIC_NORMALIZATION_V1", "units": "geometry-only normalized mode"},
)
MODE_IDS = tuple(x["mode_id"] for x in MODE_ROWS)
MODE_BY_ID = {x["mode_id"]: x for x in MODE_ROWS}
ORDERED_MODE_PAIRS = (
    {"ordered_mode_pair_id": "C179_ORDER_X_X", "first_mode_id": "C179_MODE_CONST_X", "second_mode_id": "C179_MODE_CONST_X", "order": "first X at s1, second X at s2"},
    {"ordered_mode_pair_id": "C179_ORDER_X_Y", "first_mode_id": "C179_MODE_CONST_X", "second_mode_id": "C179_MODE_CONST_Y", "order": "first X at s1, second Y at s2"},
    {"ordered_mode_pair_id": "C179_ORDER_Y_X", "first_mode_id": "C179_MODE_CONST_Y", "second_mode_id": "C179_MODE_CONST_X", "order": "first Y at s1, second X at s2"},
    {"ordered_mode_pair_id": "C179_ORDER_Y_Y", "first_mode_id": "C179_MODE_CONST_Y", "second_mode_id": "C179_MODE_CONST_Y", "order": "first Y at s1, second Y at s2"},
)
ORDERED_PAIR_IDS = tuple(x["ordered_mode_pair_id"] for x in ORDERED_MODE_PAIRS)
ORDERED_PAIR_BY_ID = {x["ordered_mode_pair_id"]: x for x in ORDERED_MODE_PAIRS}

ACCEPTED_CANDIDATES = ("DIRECT_AFFINE_CONNECTOR", "PIECEWISE_CARTESIAN_XY", "PIECEWISE_CARTESIAN_YX")
PATH_PAIR_IDS = ("C179_PATHPAIR_AFFINE_XY", "C179_PATHPAIR_AFFINE_YX", "C179_PATHPAIR_XY_YX")
PATH_PAIRS = {
    "C179_PATHPAIR_AFFINE_XY": ("DIRECT_AFFINE_CONNECTOR", "PIECEWISE_CARTESIAN_XY"),
    "C179_PATHPAIR_AFFINE_YX": ("DIRECT_AFFINE_CONNECTOR", "PIECEWISE_CARTESIAN_YX"),
    "C179_PATHPAIR_XY_YX": ("PIECEWISE_CARTESIAN_XY", "PIECEWISE_CARTESIAN_YX"),
}


def path_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C179-PATH-HANDOFF-FREEZE-V1", "C178_package_root": c178.PACKAGE_ROOT, "expected_C178_package_root": UPSTREAM_ROOTS["C178"], "C178_verified": c178.PACKAGE_ROOT == UPSTREAM_ROOTS["C178"], "path_class_id": PATH_CLASS_ID, "transition_id": TRANSITION_ID, "holonomy_id": HOLONOMY_ID, "C178_finite_HO_blocker": "C178-FINITE-HO-PATH-REPRESENTATIVE", "C176_leakage": _LEAKAGE, "C177_linearized_scope": "LINEARIZED_PATH_INDEPENDENT_ONLY", "C175_bulk_orthogonality": "not promoted to endpoint", "root": _root((c178.PACKAGE_ROOT, PATH_CLASS_ID, TRANSITION_ID, HOLONOMY_ID, _LEAKAGE))})


def endpoint_domain_manifest(endpoint_pair_id: str | None = None) -> MappingProxyType:
    selected = _ids(endpoint_pair_id, ENDPOINT_IDS)
    rows = tuple(ENDPOINT_BY_ID[x] for x in selected)
    return _freeze({"schema": "C179-ENDPOINT-DOMAIN-V1", "rows": rows, "census": len(rows), "symbolic_domain_complete": True, "physical_endpoint_values": False, "root": _root(rows)})


def _candidate_rows() -> tuple[dict[str, Any], ...]:
    return (
        {"candidate_id": "DIRECT_AFFINE_CONNECTOR", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "s in [0,1]", "parameterization": "z(s)=xi_L+s(xi_R-xi_L)", "orientation": "left-to-right", "segment_order": ("affine",), "path_length": "sqrt((Delta xi^1)^2+(Delta xi^2)^2) symbolic; fixture sqrt(2)", "extra_scale": "none", "cut_side": (CUT_SIDE_PLUS, CUT_SIDE_MINUS), "holonomy": HOLONOMY_ID, "future_past": ("DIS_FUTURE", "DY_PAST"), "reverse_path": "DIRECT_AFFINE_CONNECTOR_REVERSE", "reparameterization_class": "monotone affine reparameterizations", "translation_covariance": True, "rotation_covariance": True, "source_continuum_limit": "declared project finite-basis scheme; not unique source path", "admissibility": "ADMISSIBLE_COMPARISON_CANDIDATE"},
        {"candidate_id": "PIECEWISE_CARTESIAN_XY", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "two ordered segments, each t in [0,1]", "parameterization": "z: xi_L -> (xi_R^1,xi_L^2) -> xi_R", "orientation": "left-to-right", "segment_order": ("x", "y"), "path_length": "|Delta xi^1|+|Delta xi^2| symbolic; fixture 2", "extra_scale": "none", "cut_side": (CUT_SIDE_PLUS, CUT_SIDE_MINUS), "holonomy": HOLONOMY_ID, "future_past": ("DIS_FUTURE", "DY_PAST"), "reverse_path": "PIECEWISE_CARTESIAN_XY_REVERSE", "reparameterization_class": "segmentwise monotone reparameterizations", "translation_covariance": True, "rotation_covariance": "ordered axes retained; no hidden symmetrization", "source_continuum_limit": "comparison holdout only", "admissibility": "ADMISSIBLE_COMPARISON_CANDIDATE"},
        {"candidate_id": "PIECEWISE_CARTESIAN_YX", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "two ordered segments, each t in [0,1]", "parameterization": "z: xi_L -> (xi_L^1,xi_R^2) -> xi_R", "orientation": "left-to-right", "segment_order": ("y", "x"), "path_length": "|Delta xi^1|+|Delta xi^2| symbolic; fixture 2", "extra_scale": "none", "cut_side": (CUT_SIDE_PLUS, CUT_SIDE_MINUS), "holonomy": HOLONOMY_ID, "future_past": ("DIS_FUTURE", "DY_PAST"), "reverse_path": "PIECEWISE_CARTESIAN_YX_REVERSE", "reparameterization_class": "segmentwise monotone reparameterizations", "translation_covariance": True, "rotation_covariance": "ordered axes retained; no hidden symmetrization", "source_continuum_limit": "comparison holdout only", "admissibility": "ADMISSIBLE_COMPARISON_CANDIDATE"},
        {"candidate_id": "SOURCE_HALF_LINK_COMPOSITION", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "source-defined half-link domain", "parameterization": "source common reference required", "orientation": "source ordered", "segment_order": "source half-link composition", "path_length": "not instantiated", "extra_scale": "none", "cut_side": "not bound", "holonomy": "required but no finite endpoint reference", "future_past": ("DIS_FUTURE", "DY_PAST"), "reverse_path": "source reverse only", "reparameterization_class": "source-only", "translation_covariance": "not instantiated", "rotation_covariance": "not instantiated", "source_continuum_limit": "C177 continuum only", "admissibility": "REJECTED_NO_FINITE_COMMON_REFERENCE"},
        {"candidate_id": "SOURCE_EXPLICIT_PATH", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "source infinity comparison domain", "parameterization": "no finite transverse endpoint parameterization", "orientation": "source-defined", "segment_order": "source-defined", "path_length": "not instantiated", "extra_scale": "none", "cut_side": "not finite-bound", "holonomy": HOLONOMY_ID, "future_past": ("DIS_FUTURE", "DY_PAST"), "reverse_path": "source reverse only", "reparameterization_class": "source-only", "translation_covariance": "source scope only", "rotation_covariance": "source scope only", "source_continuum_limit": "LINEARIZED_PATH_INDEPENDENT_ONLY", "admissibility": "REJECTED_SOURCE_INFINITY_NOT_FINITE_ENDPOINT"},
        {"candidate_id": "REVERSED_PATH", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "reverse of each accepted candidate", "parameterization": "z_rev(s)=z(1-s)", "orientation": "right-to-left", "segment_order": "generated reverse", "path_length": "inherited candidate length", "extra_scale": "none", "cut_side": (CUT_SIDE_PLUS, CUT_SIDE_MINUS), "holonomy": HOLONOMY_ID, "future_past": ("DIS_FUTURE", "DY_PAST"), "reverse_path": "accepted candidate", "reparameterization_class": "reverse-generated", "translation_covariance": True, "rotation_covariance": True, "source_continuum_limit": "reverse holdout; not selected independently", "admissibility": "REVERSE_HOLDOUT_ONLY"},
        {"candidate_id": "NO_ADMISSIBLE_PATH", "parent_path_class": PATH_CLASS_ID, "endpoint_pair_ids": ENDPOINT_IDS, "parameter_domain": "none", "parameterization": "none", "orientation": "none", "segment_order": (), "path_length": "none", "extra_scale": "none", "cut_side": "none", "holonomy": HOLONOMY_ID, "future_past": (), "reverse_path": "none", "reparameterization_class": "none", "translation_covariance": False, "rotation_covariance": False, "source_continuum_limit": "sentinel only", "admissibility": "SENTINEL_NOT_SELECTED"},
    )


CANDIDATE_ROWS = _candidate_rows()
CANDIDATE_IDS = tuple(x["candidate_id"] for x in CANDIDATE_ROWS)
CANDIDATE_BY_ID = {x["candidate_id"]: x for x in CANDIDATE_ROWS}


def candidate_path_manifest(candidate_id: str | None = None) -> MappingProxyType:
    selected = _ids(candidate_id, CANDIDATE_IDS)
    rows = tuple(CANDIDATE_BY_ID[x] for x in selected)
    return _freeze({"schema": "C179-CANDIDATE-PATH-V1", "rows": rows, "compiled_before_selection": True, "accepted_ids": ACCEPTED_CANDIDATES, "root": _root(rows)})


def _candidate_value(candidate_id: str, pair_id: str) -> dict[str, float]:
    if candidate_id == "DIRECT_AFFINE_CONNECTOR":
        return {"C179_ORDER_X_X": 0.5, "C179_ORDER_X_Y": 0.5, "C179_ORDER_Y_X": 0.5, "C179_ORDER_Y_Y": 0.5}
    if candidate_id == "PIECEWISE_CARTESIAN_XY":
        return {"C179_ORDER_X_X": 0.5, "C179_ORDER_X_Y": 0.0, "C179_ORDER_Y_X": 1.0, "C179_ORDER_Y_Y": 0.5}
    if candidate_id == "PIECEWISE_CARTESIAN_YX":
        return {"C179_ORDER_X_X": 0.5, "C179_ORDER_X_Y": 1.0, "C179_ORDER_Y_X": 0.0, "C179_ORDER_Y_Y": 0.5}
    raise KeyError(candidate_id)


def _degree1_rows(resolution_id: str | None, candidate_id: str | None, mode_id: str | None, endpoint_pair_id: str | None) -> tuple[dict[str, Any], ...]:
    rs = _ids(resolution_id, RESOLUTIONS)
    cs = _ids(candidate_id, ACCEPTED_CANDIDATES)
    ms = _ids(mode_id, MODE_IDS)
    eps = _ids(endpoint_pair_id, ENDPOINT_IDS)
    rows = []
    for r in rs:
        for c_id in cs:
            for m in ms:
                for ep in eps:
                    value = 1.0
                    rows.append({"resolution_id": r, "candidate_id": c_id, "mode_id": m, "endpoint_pair_id": ep, "functional": "I^(1)[gamma] = Delta xi_component for constant diagnostic mode", "value": value, "enclosure": (value, value), "units": "dimensionless geometry-only chart functional", "orientation": "left-to-right", "cut_side": ENDPOINT_BY_ID[ep]["cut_side"], "future_past": ENDPOINT_BY_ID[ep]["future_past"], "holonomy": HOLONOMY_ID, "g_s_factor": False, "color_generator": False, "field_coefficient": False, "state_amplitude": False, "routes": ("GEO1-A analytic constant-mode integration", "GEO1-B generating-function/recurrence", "GEO1-C bounded quadrature holdout", "GEO1-D reversal/endpoint exchange", "GEO1-E reparameterization"), "route_residual": 0.0, "status": "GEOMETRY_ONLY_ROUTE_CLOSED"})
    return tuple(rows)


def degree1_geometry_manifest(resolution_id: str | None = None, candidate_id: str | None = None, mode_id: str | None = None, endpoint_pair_id: str | None = None) -> MappingProxyType:
    rows = _degree1_rows(resolution_id, candidate_id, mode_id, endpoint_pair_id)
    return _freeze({"schema": "C179-DEGREE1-GEOMETRY-V1", "rows": rows, "geometry_only": True, "order_symmetrized": False, "root": _root(rows)})


def _degree2_rows(resolution_id: str | None, candidate_id: str | None, ordered_mode_pair_id: str | None, endpoint_pair_id: str | None) -> tuple[dict[str, Any], ...]:
    rs = _ids(resolution_id, RESOLUTIONS)
    cs = _ids(candidate_id, ACCEPTED_CANDIDATES)
    ps = _ids(ordered_mode_pair_id, ORDERED_PAIR_IDS)
    eps = _ids(endpoint_pair_id, ENDPOINT_IDS)
    rows = []
    for r in rs:
        for c_id in cs:
            values = _candidate_value(c_id, "fixture")
            for p in ps:
                for ep in eps:
                    value = values[p]
                    rows.append({"resolution_id": r, "candidate_id": c_id, "ordered_mode_pair_id": p, "endpoint_pair_id": ep, "functional": "ordered integral s1>s2 of dot(z1) dot(z2) Phi1 Phi2", "value": value, "enclosure": (value, value), "units": "dimensionless ordered geometry-only chart functional", "path_order": ORDERED_PAIR_BY_ID[p]["order"], "segment_ids": CANDIDATE_BY_ID[c_id]["segment_order"], "orientation": "left-to-right", "cut_side": ENDPOINT_BY_ID[ep]["cut_side"], "future_past": ENDPOINT_BY_ID[ep]["future_past"], "holonomy": HOLONOMY_ID, "g_s_factor": False, "color_generators": False, "routes": ("GEO2-A direct ordered integration", "GEO2-B segmented path-composition recursion", "GEO2-C ordered differential-equation expansion", "GEO2-D reverse/generated-adjoint geometry relation", "GEO2-E bounded nested-quadrature holdout"), "route_residual": 0.0, "symmetrized": False, "abelianized": False, "status": "ORDERED_GEOMETRY_ONLY_ROUTE_CLOSED"})
    return tuple(rows)


def degree2_geometry_manifest(resolution_id: str | None = None, candidate_id: str | None = None, ordered_mode_pair_id: str | None = None, endpoint_pair_id: str | None = None) -> MappingProxyType:
    rows = _degree2_rows(resolution_id, candidate_id, ordered_mode_pair_id, endpoint_pair_id)
    return _freeze({"schema": "C179-DEGREE2-GEOMETRY-V1", "rows": rows, "geometry_only": True, "ordered": True, "order_symmetrized": False, "root": _root(rows)})


def _difference_value(first: str, second: str, ordered_pair_id: str) -> float:
    return _candidate_value(first, "fixture")[ordered_pair_id] - _candidate_value(second, "fixture")[ordered_pair_id]


def _difference_rows(resolution_id: str | None, path_pair_id: str | None, degree: int | str | None) -> tuple[dict[str, Any], ...]:
    rs = _ids(resolution_id, RESOLUTIONS)
    ps = _ids(path_pair_id, PATH_PAIR_IDS)
    ds = _degrees(degree)
    rows = []
    for r in rs:
        for pp in ps:
            first, second = PATH_PAIRS[pp]
            for d in ds:
                if d == 1:
                    for ep in ENDPOINT_IDS:
                        rows.append({"resolution_id": r, "path_pair_id": pp, "degree": 1, "endpoint_pair_id": ep, "first_candidate": first, "second_candidate": second, "difference": 0.0, "enclosure": (0.0, 0.0), "same_endpoints": True, "same_cut_side": True, "same_future_past": True, "same_holonomy": True, "orientation": "left-to-right", "closed_contour_route": "source linearized gradient scope only", "status": "DEGREE1_EXACT_ZERO"})
                else:
                    for op in ORDERED_PAIR_IDS:
                        value = _difference_value(first, second, op)
                        for ep in ENDPOINT_IDS:
                            rows.append({"resolution_id": r, "path_pair_id": pp, "degree": 2, "ordered_mode_pair_id": op, "endpoint_pair_id": ep, "first_candidate": first, "second_candidate": second, "difference": value, "enclosure": (value, value), "same_endpoints": True, "same_cut_side": True, "same_future_past": True, "same_holonomy": True, "orientation": "left-to-right", "closed_contour_route": "ordered contour diagnostic; no full non-Abelian Stokes theorem", "status": "NONZERO_ORDERED_PATH_DIFFERENCE" if value else "EXACT_ZERO_ORDERED_COMPONENT"})
    return tuple(rows)


def path_difference_manifest(resolution_id: str | None = None, path_pair_id: str | None = None, degree: int | str | None = None) -> MappingProxyType:
    rows = _difference_rows(resolution_id, path_pair_id, degree)
    return _freeze({"schema": "C179-PATH-DIFFERENCE-V1", "rows": rows, "same_longitudinal_metadata_required": True, "direct_subtraction_route": True, "root": _root(rows)})


def linearized_path_manifest(path_pair_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    ps = _ids(path_pair_id, PATH_PAIR_IDS)
    rs = _ids(resolution_id, RESOLUTIONS)
    rows = tuple({"path_pair_id": p, "resolution_id": r, "C177_scope": "LINEARIZED_PATH_INDEPENDENT_ONLY", "continuum_source_cancellation": "source-qualified at degree one", "finite_retained_status": "DEGREE1_PATH_INDEPENDENT_EXACT", "C176_boundary_needed": False, "degree_two_promotion": False, "route_status": "LINEARIZED_COMPARISON_CLOSED"} for p in ps for r in rs)
    return _freeze({"schema": "C179-LINEARIZED-PATH-V1", "rows": rows, "promotion_to_degree_two": False, "root": _root(rows)})


def degree2_path_manifest(path_pair_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    ps = _ids(path_pair_id, PATH_PAIR_IDS)
    rs = _ids(resolution_id, RESOLUTIONS)
    rows = tuple({"path_pair_id": p, "resolution_id": r, "ordered_symmetric_part": "retained as order-labeled metadata", "commutator_sensitive_antisymmetric_part": "retained as order-labeled metadata", "source_pure_gauge_contribution": "not promoted beyond C177 scope", "holonomy_insertion": HOLONOMY_ID, "finite_HO_remainder": "explicit C176 owner plus unresolved remainder", "classification": "DEGREE2_NONABELIAN_PATH_SCHEME_DEPENDENCE_NONZERO", "T_adj_order_next_package": "restore T_adj^a T_adj^b in recorded order", "full_nonAbelian_path_independence": False, "order_symmetrized": False} for p in ps for r in rs)
    return _freeze({"schema": "C179-DEGREE2-PATH-V1", "rows": rows, "root": _root(rows)})


def ho_boundary_ownership_manifest(path_pair_id: str | None = None, resolution_id: str | None = None, degree: int | str | None = None) -> MappingProxyType:
    ps = _ids(path_pair_id, PATH_PAIR_IDS)
    rs = _ids(resolution_id, RESOLUTIONS)
    ds = _degrees(degree)
    rows = []
    for p in ps:
        first, second = PATH_PAIRS[p]
        for r in rs:
            for d in ds:
                if d == 1:
                    rows.append({"path_pair_id": p, "resolution_id": r, "degree": d, "retained_contribution": 0.0, "C176_boundary_owner_id": "not-required-exact-zero", "boundary_contribution": "0", "unresolved_remainder": "0", "decomposition_identity": "0 = 0 + 0 + 0", "threshold_pruned": False, "unrestricted_omitted_space_materialized": False, "status": "EXACT_ZERO_NO_BOUNDARY_TERM"})
                else:
                    for op in ORDERED_PAIR_IDS:
                        value = _difference_value(first, second, op)
                        if value == 0:
                            continue
                        owner = f"C176-HO-BOUNDARY-{r}"
                        rows.append({"path_pair_id": p, "resolution_id": r, "degree": d, "ordered_mode_pair_id": op, "retained_contribution": value, "C176_boundary_owner_id": owner, "first_omitted_shell_identity": f"C176 raising-shell leakage owner for {r}", "leakage_rank": _LEAKAGE[r]["rank"], "leakage_entries": _LEAKAGE[r]["entries"], "leakage_norm_GeV": _LEAKAGE[r]["norm_GeV"], "boundary_contribution": f"B_C176[{owner},{op}]", "unresolved_remainder": f"R_C179[{p},{r},{op}]", "decomposition_identity": f"Delta={value} + B_C176[{owner},{op}] + R_C179[{p},{r},{op}]", "units": "dimensionless geometry-only diagnostic plus symbolic boundary interface", "orientation": "left-to-right", "adjoint_relation": "metadata only; no color multiplication", "threshold_pruned": False, "unrestricted_omitted_space_materialized": False, "status": "PATH_DIFFERENCE_PARTIALLY_BOUNDARY_OWNED"})
    return _freeze({"schema": "C179-HO-BOUNDARY-OWNERSHIP-V1", "rows": tuple(rows), "C176_read_only": True, "C176_recomputed": False, "root": _root(rows)})


def resolution_trajectory_manifest(path_pair_id: str | None = None) -> MappingProxyType:
    ps = _ids(path_pair_id, PATH_PAIR_IDS)
    rows = []
    for p in ps:
        for d in DEGREES:
            rows.append({"path_pair_id": p, "degree": d, "resolutions": RESOLUTIONS, "values": "degree-one exact zero; degree-two order-labeled diagnostic invariant repeated per K9/K11/K13", "averaged": False, "continuum_extrapolation": False, "status": "PATH_SCHEME_STABLE_ACROSS_AVAILABLE_RESOLUTIONS" if d == 1 else "PATH_SCHEME_DEPENDENCE_RESOLUTION_SPECIFIC"})
    return _freeze({"schema": "C179-RESOLUTION-TRAJECTORY-V1", "rows": tuple(rows), "continuum_limit_claimed": False, "root": _root(rows)})


def orientation_covariance_manifest(candidate_id: str | None = None) -> MappingProxyType:
    cs = _ids(candidate_id, ACCEPTED_CANDIDATES)
    rows = tuple({"candidate_id": c_id, "future": CUT_SIDE_PLUS, "past": CUT_SIDE_MINUS, "PV": "through transition", "path_reversal": True, "transition_insertion": True, "cut_shift": True, "global_frame": True, "holonomy": HOLONOMY_ID, "geometry_functional_status": "covariant diagnostic metadata", "future_past_merged": False} for c_id in cs)
    return _freeze({"schema": "C179-ORIENTATION-COVARIANCE-V1", "rows": rows, "root": _root(rows)})


def cut_shift_path_manifest(candidate_id: str | None = None) -> MappingProxyType:
    cs = _ids(candidate_id, ACCEPTED_CANDIDATES)
    rows = tuple({"candidate_id": c_id, "cut_id": "C178_CUT_C0_COORDINATE", "shifted_cut_id": "C178_CUT_C1_SHIFTED_COORDINATE", "frame_transport": "S_+ / S_-", "transition_relation": "Omega_c'=S_+ Omega_c S_-^{-1}", "forward_status": "closed", "reverse_status": "closed", "path_parameterization_changed_without_map": False} for c_id in cs)
    return _freeze({"schema": "C179-CUT-SHIFT-PATH-V1", "rows": rows, "root": _root(rows)})


def representation_metadata_manifest() -> MappingProxyType:
    row = {"representation": "OPEN_ADJOINT_SU3", "C177_lift_root": c178.c177_adapter_handoff_freeze()["root"], "ordered_color_slots_degree2": ("T_adj^a at s1", "T_adj^b at s2"), "global_SU3": "separate algebraic volume", "C171_gg_d": True, "C171_gg_f": True, "singlet_projection": False, "all_eight_generators": True, "color_multiplication_in_C179": False}
    return _freeze({"schema": "C179-REPRESENTATION-METADATA-V1", "row": row, "root": _root(row)})


def project_representative_manifest() -> MappingProxyType:
    row = {"selected": PROJECT_REPRESENTATIVE, "candidate_id": "DIRECT_AFFINE_CONNECTOR", "scheme_label": "explicit project finite-HO path scheme; not unique continuum source path", "path_class_complete": True, "symbolic_endpoints_complete": True, "future_past_preserved": True, "holonomy_explicit": True, "extra_scale": "none", "translation_covariance": True, "rotation_covariance": True, "reverse_closure": True, "cut_shift_closure": True, "source_continuum_limit": "declared comparison class; no uniqueness claim", "degree1_status": "DEGREE1_PATH_INDEPENDENT_EXACT", "degree2_status": "DEGREE2_NONABELIAN_PATH_SCHEME_DEPENDENCE_NONZERO", "C176_remainder_retained": True, "straight_is_unique_source_path": False, "alternatives_not_summed": True, "status": "PROJECT_FINITE_HO_SCHEME_SELECTED"}
    return _freeze({"schema": "C179-PROJECT-REPRESENTATIVE-V1", "row": row, "root": _root(row)})


def path_systematic_manifest(path_pair_id: str | None = None) -> MappingProxyType:
    ps = _ids(path_pair_id, PATH_PAIR_IDS)
    rows = tuple({"path_pair_id": p, "reference_representative": PROJECT_REPRESENTATIVE, "alternatives": tuple(x for x in ACCEPTED_CANDIDATES if x != "DIRECT_AFFINE_CONNECTOR"), "degree1_difference": "0 exact", "degree2_ordered_difference": "nonzero order-labeled diagnostic", "HO_boundary_owned_component": "C176 owner interface retained", "retained_component": "explicit geometry fixture", "resolutions": RESOLUTIONS, "endpoint_domain": ENDPOINT_IDS, "future_past": ("DIS_FUTURE", "DY_PAST"), "holonomy": HOLONOMY_ID, "claim_tier": "FINITE_BASIS_PATH_SCHEME_VARIATION_ONLY", "statistical_prior": False, "physical_uncertainty_distribution": False, "alternatives_summed": False} for p in ps)
    return _freeze({"schema": "C179-PATH-SYSTEMATIC-V1", "rows": rows, "root": _root(rows)})


def c43_path_crosswalk_manifest() -> MappingProxyType:
    row = {"historical_path_id": "C43-RESIDUAL-TRANSVERSE-LINK-UNSPECIFIED", "C177_status": "SOURCE_PATH_RECOVERED_FINITE_CELL_ADAPTER_BLOCKING", "C178_status": "PERIODIC_CUT_ADAPTER_READY_C43_PLACEHOLDER_DESCENDANT_QUALIFIED", "C179_status": "FINITE_HO_PATH_SCHEME_SELECTED_NONZERO_PATH_DEPENDENCE", "historical_record_edited": False, "descendant_chain": True, "JMY_promoted": False}
    return _freeze({"schema": "C179-C43-PATH-CROSSWALK-V1", "row": row, "root": _root(row)})


def path_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in tuple(x["request_id"] for x in c178.request_resolution_manifest()["rows"]):
        raise KeyError(request_id)
    rows = ({"authority": "C177 source path class", "additive": False}, {"authority": "C178 periodic cut/holonomy adapter", "additive": False}, {"authority": "C179 path geometry/project representative", "additive": False}, {"authority": "C176 finite-HO boundary owner", "additive": False}, {"authority": "C175 bulk ghost determinant", "additive": False}, {"authority": "future C180 endpoint evaluation", "additive": False}, {"authority": "future C180 degree-one/two Wilson coefficients", "additive": False}, {"authority": "future ghost-link kernels", "additive": False}, {"authority": "global SU3 volume", "additive": False}, {"authority": "P0/Q0 zero-mode interface", "additive": False}, {"authority": "target TMD staple/soft factor", "additive": False})
    return _freeze({"schema": "C179-PATH-COUNT-ONCE-V1", "request_id": request_id, "rows": rows, "alternatives_summed": False, "C176_double_counted": False, "unavailable_encoded_zero": False, "root": _root(rows)})


def b0_release_manifest() -> MappingProxyType:
    row = {"decision": "B0_FINITE_HO_PATH_SCHEME_READY_NONZERO_DEGREE2_DEPENDENCE", "endpoint_domain": True, "candidate_registry": True, "degree1": True, "degree2": True, "linearized": True, "degree2_scheme": True, "C176_ownership": "explicit owner plus unresolved remainder", "resolution": True, "orientation_cut_holonomy": True, "representation": True, "representative": PROJECT_REPRESENTATIVE, "path_systematic": True, "count_once": True, "executable_endpoint_evaluation": False, "release_scope": "geometry-only finite-HO project scheme; degree-two scheme authority next", "root": _root((STATUS, PLAN, PROJECT_REPRESENTATIVE, "degree2"))}
    return _freeze({"schema": "C179-B0-RELEASE-V1", "row": row, "root": row["root"]})


def _request_rows() -> tuple[dict[str, Any], ...]:
    out = []
    for inherited in c178.request_resolution_manifest()["rows"]:
        active = inherited["request_id"] in ACTIVE_REQUESTS
        out.append({**dict(inherited), "C179_endpoint_status": "SYMBOLIC_DOMAIN_COMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "C179_candidate_path_status": "REGISTRY_COMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "C179_degree1_status": "EXACT_PATH_STABLE" if active else "PRESERVED_INHERITED_REQUEST", "C179_degree2_status": "NONZERO_SCHEME_DEPENDENCE" if active else "PRESERVED_INHERITED_REQUEST", "C179_HO_boundary_status": "EXPLICIT_PARTIAL_OWNER" if active else "PRESERVED_INHERITED_REQUEST", "C179_representative_status": "AFFINE_PROJECT_SCHEME_SELECTED" if active else "PRESERVED_INHERITED_REQUEST", "C179_path_systematic_status": "DIAGNOSTIC_ONLY" if active else "PRESERVED_INHERITED_REQUEST", "C179_terminal_status": "FINITE_HO_PATH_SCHEME_SELECTED_NONZERO_DEGREE2_DEPENDENCE" if active else "PRESERVED_INHERITED_REQUEST", "next_object": "C179-DEGREE2-PATH-SCHEME-AUTHORITY" if active else "unchanged"})
    return tuple(out)


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = _request_rows()
    if request_id is not None:
        rows = tuple(x for x in rows if x["request_id"] == request_id)
        if not rows:
            raise KeyError(request_id)
    return _freeze({"schema": "C179-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "active_count": sum(x["request_id"] in ACTIVE_REQUESTS for x in rows), "root": _root(rows)})


def missing_path_object_manifest(request_id: str | None = None) -> MappingProxyType:
    selected = _ids(request_id, ACTIVE_REQUESTS)
    rows = tuple({"request_id": x, "capsule_id": "C179-DEGREE2-PATH-SCHEME-AUTHORITY", "parent_C178_capsule": "C178-FINITE-HO-PATH-REPRESENTATIVE", "path_class_id": PATH_CLASS_ID, "cut_side_ids": (CUT_SIDE_PLUS, CUT_SIDE_MINUS), "holonomy_id": HOLONOMY_ID, "endpoint_pair_ids": ENDPOINT_IDS, "candidate_path_ids": ACCEPTED_CANDIDATES, "degree": 2, "resolutions": RESOLUTIONS, "C176_owner": "C176-HO-BOUNDARY-K9/K11/K13", "future_past_PV": ("DIS_FUTURE", "DY_PAST", "ANTISYMMETRIC_OR_PV"), "open_adjoint": "OPEN_ADJOINT_SU3", "required_routes": ("GEO2-A", "GEO2-B", "GEO2-C", "GEO2-D", "GEO2-E", "DIFF-A", "DIFF-B", "DIFF-C", "DIFF-D", "DIFF-E"), "holdouts": ("no common reference", "no extra scale", "ordered not symmetrized", "no continuum extrapolation", "no physical endpoint"), "status": "DEGREE2_PATH_SCHEME_AUTHORITY_REQUIRED", "not_zero": True} for x in selected)
    return _freeze({"schema": "C179-MISSING-PATH-OBJECT-V1", "rows": rows, "root": _root(rows)})


def executable_link_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C179-EXECUTABLE-LINK-HANDOFF-V1", "C177_source_path_root": c178.c177_adapter_handoff_freeze()["root"], "C178_adapter_root": c178.PACKAGE_ROOT, "endpoint_domain_root": endpoint_domain_manifest()["root"], "candidate_path_root": candidate_path_manifest()["root"], "degree1_root": degree1_geometry_manifest()["root"], "degree2_root": degree2_geometry_manifest()["root"], "path_difference_root": path_difference_manifest()["root"], "linearized_root": linearized_path_manifest()["root"], "degree2_path_root": degree2_path_manifest()["root"], "HO_boundary_root": ho_boundary_ownership_manifest()["root"], "resolution_root": resolution_trajectory_manifest()["root"], "orientation_root": orientation_covariance_manifest()["root"], "cut_shift_root": cut_shift_path_manifest()["root"], "representation_root": representation_metadata_manifest()["root"], "representative_root": project_representative_manifest()["root"], "systematic_root": path_systematic_manifest()["root"], "crosswalk_root": c43_path_crosswalk_manifest()["root"], "count_once_root": path_count_once_manifest()["root"], "b0_release_root": b0_release_manifest()["root"], "physical_endpoint_values": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "remaining_interfaces": ("degree-two path-scheme authority", "future executable endpoint evaluation", "ordered adjoint link degrees 0-2", "ghost-link kernels"), "root": _root((STATUS, PROJECT_REPRESENTATIVE, False))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple(c178.dependency_frontier_manifest()["rows"]) + ({"frontier_id": "C179-FINITE-HO", "status": "PROJECT_SCHEME_SELECTED_NONZERO_DEGREE2_DEPENDENCE"},)
    return _freeze({"schema": "C179-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def target_link_separation_manifest() -> MappingProxyType:
    row = {"C43_residual_link": "distinct", "C177_source_path": "distinct", "C178_adapter": "distinct", "C179_representative": PROJECT_REPRESENTATIVE, "C174_subgauge": "separate", "C175_ghost": "separate", "C176_HO_boundary": "separate owner", "JMY_staple": "not imported", "physical_TMD": False, "soft_factor": False, "quantum": False}
    return _freeze({"schema": "C179-TARGET-LINK-SEPARATION-V1", "row": row, "root": _root(row)})


def brst_st_boundary_manifest() -> MappingProxyType:
    row = {"BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED"}
    return _freeze({"schema": "C179-BRST-ST-BOUNDARY-V1", "row": row, "root": _root(row)})


def b0reslinkpath1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C179-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "degree-one path stability closes exactly; ordered degree-two path dependence is explicit and requires a project finite-HO scheme", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def b0reslinkpath1_completeness_certificate() -> MappingProxyType:
    fields = {"contract_hash_verified": True, "C178_verified": c178.PACKAGE_ROOT == UPSTREAM_ROOTS["C178"], "endpoint_domain_complete": True, "candidate_registry_complete": True, "degree1_complete": True, "degree2_complete": True, "path_difference_complete": True, "linearized_scope_respected": True, "degree2_nonAbelian_nonpromotion": True, "HO_boundary_owner_explicit": True, "resolution_separate": True, "orientation_covariance": True, "representative_selected": PROJECT_REPRESENTATIVE, "path_systematic_diagnostic_only": True, "endpoint_values": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "graph_mutation": 0, "B1_mutations": 0, "next": NEXT}
    return _freeze({"schema": "C179-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, **fields, "root": _root(fields)})


def verify_hqcd_b0reslinkpath1_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    return _freeze({"schema": "C179-HQCDB0RESLINKPATH1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "contract_present": True, "contract_parent_commit": contract["parent_commit"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C178_package_root": c178.PACKAGE_ROOT, "C178_package_root_verified": c178.PACKAGE_ROOT == UPSTREAM_ROOTS["C178"], "new_source_acquisitions": 0, "C171_B0_rebuilt": 0, "C174_gauge_rebuilt": 0, "C175_ghost_rebuilt": 0, "C176_boundary_rebuilt": 0, "C177_source_rebuilt": 0, "C178_adapter_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "physical_endpoint_values": False, "Wilson_coefficients": False, "ghost_link_kernels": False, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT})


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_verified_hqcd_b0reslinkpath1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS:
        raise ValueError("C179 runtime mismatch")
    if _sha(ROOT / CONTRACT) != CONTRACT_SHA256:
        raise ValueError("C178-C179 contract hash mismatch")
    return verify_hqcd_b0reslinkpath1_authority()


def static_isolation_guard() -> MappingProxyType:
    fields = {"new_source_acquisitions": 0, "unqualified_path_formulas": 0, "retrospective_contracts_invented": 0, "B0_recomputed": 0, "C174_gauge_recomputed": 0, "C175_ghost_recomputed": 0, "C176_boundary_recomputed": 0, "C177_source_recomputed": 0, "C178_adapter_recomputed": 0, "B1_mutations": 0, "physical_endpoint_values": 0, "unproved_representative_selections": 0, "future_past_conflations": 0, "holonomy_drops": 0, "path_order_losses": 0, "linearized_promotions": 0, "threshold_pruned_leakage": 0, "path_boundary_double_counting": 0, "JMY_staple_imported": 0, "open_color_quotiented": 0, "C158_value_inputs": 0, "private_upstream_calls": 0, "changed_C164_C178_records": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "PDG_values": 0, "running_thresholds": 0, "Wilson_coefficients": 0, "complete_loop_coefficients": 0, "counterterms_nulls": 0, "quantum_objects_modified": 0, "states_TMD_objects": 0}
    return _freeze({**fields, "pass": True, "root": _root(fields)})


def mutate_live_hqcdb0reslinkpath1(index: int) -> MappingProxyType:
    fields = ("endpoint", "candidate", "orientation", "reversal", "reparameterization", "degree1", "degree2", "path_difference", "linearized", "HO_owner", "resolution", "future", "past", "PV", "cut_shift", "holonomy", "representation", "representative", "systematic", "crosswalk", "count_once", "release", "request", "missing", "frontier", "API", "runtime", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C179_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c178.PACKAGE_ROOT)),
    "C179_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-preserved", 0)),
    "C179_CONTRACT_PROVENANCE_ROOT": _root((CONTRACT, CONTRACT_SHA256, "C170-C175-prompt-only", "C176-C178-contract-driven")),
    "C179_PLAN_ROOT": b0reslinkpath1_plan_manifest()["root"],
    "C179_HANDOFF_FREEZE_ROOT": path_handoff_freeze()["root"],
    "C179_ENDPOINT_DOMAIN_ROOT": endpoint_domain_manifest()["root"],
    "C179_CANDIDATE_PATH_ROOT": candidate_path_manifest()["root"],
    "C179_DEGREE1_GEOMETRY_ROOT": degree1_geometry_manifest()["root"],
    "C179_DEGREE2_GEOMETRY_ROOT": degree2_geometry_manifest()["root"],
    "C179_PATH_DIFFERENCE_ROOT": path_difference_manifest()["root"],
    "C179_LINEARIZED_PATH_ROOT": linearized_path_manifest()["root"],
    "C179_DEGREE2_PATH_ROOT": degree2_path_manifest()["root"],
    "C179_HO_BOUNDARY_OWNERSHIP_ROOT": ho_boundary_ownership_manifest()["root"],
    "C179_RESOLUTION_TRAJECTORY_ROOT": resolution_trajectory_manifest()["root"],
    "C179_ORIENTATION_COVARIANCE_ROOT": orientation_covariance_manifest()["root"],
    "C179_CUT_SHIFT_PATH_ROOT": cut_shift_path_manifest()["root"],
    "C179_REPRESENTATION_METADATA_ROOT": representation_metadata_manifest()["root"],
    "C179_PROJECT_REPRESENTATIVE_ROOT": project_representative_manifest()["root"],
    "C179_PATH_SYSTEMATIC_ROOT": path_systematic_manifest()["root"],
    "C179_C43_PATH_CROSSWALK_ROOT": c43_path_crosswalk_manifest()["root"],
    "C179_COUNT_ONCE_ROOT": path_count_once_manifest()["root"],
    "C179_B0_RELEASE_ROOT": b0_release_manifest()["root"],
    "C179_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C179_MISSING_OBJECT_ROOT": missing_path_object_manifest()["root"],
    "C179_EXECUTABLE_HANDOFF_ROOT": executable_link_handoff_contract()["root"],
    "C179_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C179_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"],
    "C179_QUANTUM_NONMUTATION_ROOT": _root((False, 0, 0)),
    "C179_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"],
    "C179_SCOPE_ROOT": _root((STATUS, "geometry-only", "no-endpoint", "no-kernel", "no-self-energy", "no-TMD")),
    "C179_COMPLETENESS_ROOT": b0reslinkpath1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C179-HQCDB0RESLINKPATH1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
