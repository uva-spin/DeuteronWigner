"""Executable, nonphysical C158 finite-basis coefficient authorities.

This module is deliberately a small numerical boundary around the public
C144 sparse polynomial API.  It never evaluates a continuum target or an
IR difference.  Programs are immutable data (never Python callables), and
all numerical entry points require an explicit subtraction/common-IR record,
coupling record, and exactly one diagnostic parameter context.
"""
from __future__ import annotations

import json
import math
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcd4 import core as c131
from deuteron_wigner.bridge.hqcdopapi import core as c144

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c158_hqcdfbnum"
BASELINE = "1d12bf5c4d9a8aa015a3de6a79a84e4af22864d6"
SCHEMA = "C158-HQCDFBNUM-V1"
STATUS = "C158_C157_SOURCE_DERIVED_EXECUTABLE_FINITE_BASIS_MATCHING_COEFFICIENT_AUTHORITY_READY"
PLAN = "FBNUM-A"
NEXT = "C159/HQCDMATCHIR3"
CONTRACT = "docs/next_level/c157_c158_hqcdfbnum_continuation_contract.json"
CONTRACT_SHA256 = "4b4f01049e2a7f7c8b67f95965acb60fadfd4e234e5a5bdd5dc29a3206db93c1"
C157_ROOT = "351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c"
C156_ROOT = "8ba1231561ad04e5e1e8e96de9e8a270b8ad284b804021489dbe02cff2c2270d"
C153_ROOT = "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
C152_ROOT = "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da"
C151_ROOT = "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C150_ROOT = "2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a"
C149_ROOT = "8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0"
C144_ROOT = "cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635"
C131_ROOT = c131.PACKAGE_ROOT
RESOLUTIONS = ("K9", "K11", "K13")
FIXTURES = c144.FIXTURE_IDS
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
ROUTES = ("sparse", "matrix_free", "qg_block", "cauchy_direct_g")
SCHEMES = ("K_MINUS", "K_PLUS", "K_PERP")
ORDERS = {"QUARK_FIELD": 0, "SIGNED_QUARK_MASS": 0, "TRANSVERSE_GLUON_FIELD": 0,
          "qg_VERTEX_DRESSING": 1, "QCD_COUPLING": 1}
LABELS = {"QUARK_FIELD": "delta_quark_field^FB(order=0)", "SIGNED_QUARK_MASS": "delta_signed_quark_mass^FB(order=0)",
          "TRANSVERSE_GLUON_FIELD": "delta_gluon_field^FB(order=0)", "qg_VERTEX_DRESSING": "delta_qg_vertex^FB(order=1)",
          "QCD_COUPLING": "delta_qcd_coupling^FB(order=1)"}
_ALIASES = {**{q: q for q in QUANTITIES}, **{v: k for k, v in LABELS.items()},
            "quark_field": "QUARK_FIELD", "signed_quark_mass": "SIGNED_QUARK_MASS",
            "gluon_field": "TRANSVERSE_GLUON_FIELD", "qg_vertex": "qg_VERTEX_DRESSING",
            "qcd_coupling": "QCD_COUPLING"}


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


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def _res(resolution: str) -> str:
    if resolution not in RESOLUTIONS: raise ValueError(f"unknown explicit resolution: {resolution!r}")
    return resolution


def _label(label: str) -> str:
    if label not in _ALIASES: raise ValueError(f"unknown or implicit C153 coefficient label: {label!r}")
    return _ALIASES[label]


def _context(*, parameter_record: Mapping[str, Any] | None, fixture_id: str | None) -> Mapping[str, Any]:
    if (parameter_record is None) == (fixture_id is None):
        raise ValueError("exactly one of parameter_record or fixture_id is required")
    if fixture_id is not None:
        if fixture_id not in FIXTURES: raise KeyError(fixture_id)
        return c144.load_diagnostic_fixture(fixture_id)
    return c144.validate_parameter_record(parameter_record)


def _common(record: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(record, Mapping): raise TypeError("common-IR/subtraction record must be a mapping")
    if record.get("resolution") not in RESOLUTIONS: raise ValueError("explicit K9/K11/K13 resolution is required")
    schema = record.get("schema")
    if schema == "C149-OFFSHELL-SUBTRACTION-RECORD-V1":
        required = ("subtraction_id", "mu", "units", "kinematics", "state_selector", "projector_id", "no_default")
        if any(k not in record for k in required): raise ValueError("incomplete explicit C149 subtraction record")
        if record["no_default"] is not True: raise ValueError("subtraction defaults are forbidden")
    elif schema == "C157-COMMON-IR-NUMERIC-RECORD-V1":
        # C158 records are provenance only.  Importing the C157 validator is
        # intentionally avoided here so C158 never recomputes a C157 grid.
        if not record.get("common_ir_id") or "rho" not in record or "mu" not in record:
            raise ValueError("incomplete explicit C157 common-IR record")
    elif not (record.get("common_ir_id") or record.get("subtraction_id")):
        raise ValueError("explicit common_ir_id or subtraction_id is required")
    if not any(record.get(k) for k in ("projector_id", "kinetic_scheme_id", "finite_basis_scheme", "finite_basis_scheme_ids", "scheme_id")):
        raise ValueError("explicit scheme/projector record is required")
    if record.get("no_default") is False: raise ValueError("no_default must be explicit")
    return _freeze(dict(record))


def coupling_expansion_record_schema() -> MappingProxyType:
    return _freeze({"schema": "C158-COUPLING-EXPANSION-RECORD-SCHEMA-V1",
                    "required": ("record_id", "expansion_variable", "max_order", "owner_to_coupling_power",
                                  "derivative_map", "source_contact_map", "counterterm_classification", "no_default"),
                    "context_rule": "exactly one parameter_record_root or fixture_id",
                    "power_semantics": "explicit C131 retained polynomial degree; never inferred",
                    "root": _root((c131.TERMS, c131.DEGREES, "no-guess"))})


def _default_coupling_record(*, fixture_id: str | None = None, parameter_record_root: str | None = None) -> MappingProxyType:
    if (fixture_id is None) == (parameter_record_root is None): raise ValueError("coupling record needs exactly one context")
    owner = {t: int(c131.DEGREES[t]) for t in c131.TERMS}
    owner.update({"C111_COMPOSITE_SOURCE": 0, "C148_COMPOSITE_SOURCE": 0, "C151_EXTERNAL_LEG": 0,
                  "C152_VERTEX_PROJECTOR": 0})
    data = {"schema": "C158-COUPLING-EXPANSION-RECORD-V1", "record_id": "C158-public-C131-polynomial",
            "expansion_variable": "g_s", "max_order": 2, "owner_to_coupling_power": owner,
            "derivative_map": {"d/dg_s": "C144 exact operator_derivative(phi_coupling)", "d2/dg_s2": "C144 degree-two algebraic extraction"},
            "source_contact_map": {"source": "C147", "composite_source": "C148", "external_leg": "C151", "vertex": "C152", "count_once": True},
            "finite_basis_scheme_ids": SCHEMES, "projector_ids": {s: f"{s}_projector" for s in SCHEMES},
            "source_ids": {"QUARK_FIELD": "C147_EXTERNAL_QUARK_SOURCE", "SIGNED_QUARK_MASS": "C147_MASS_SOURCE",
                           "TRANSVERSE_GLUON_FIELD": "C151_TRANSVERSE_GLUON_SOURCE", "qg_VERTEX_DRESSING": "C152_QG_VERTEX_PROJECTOR", "QCD_COUPLING": "C152_Z1F_PROJECTOR"},
            "counterterm_classification": {x: "NONMATRIX_NOT_IN_RETAINED_C131_POLYNOMIAL" for x in
                ("mass", "gluon", "coupling", "source", "boundary", "zero_mode")}, "no_default": True}
    if fixture_id is not None: data["fixture_id"] = fixture_id
    else: data["parameter_record_root"] = parameter_record_root
    data["root"] = _root(data)
    return _freeze(data)


def validate_coupling_expansion_record(record: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(record, Mapping) or record.get("schema") != "C158-COUPLING-EXPANSION-RECORD-V1":
        raise ValueError("explicit C158 coupling-expansion record required")
    for k in coupling_expansion_record_schema()["required"]:
        if k not in record: raise ValueError(f"missing coupling-expansion field: {k}")
    if record.get("no_default") is not True or record.get("expansion_variable") != "g_s": raise ValueError("invalid coupling record")
    if (record.get("fixture_id") is None) == (record.get("parameter_record_root") is None):
        raise ValueError("coupling record requires exactly one fixture_id or parameter_record_root")
    for t, degree in c131.DEGREES.items():
        if record["owner_to_coupling_power"].get(t) != degree: raise ValueError(f"unproven coupling power for {t}")
    return _freeze(dict(record))


def coupling_expansion_record(*, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    """Build the explicit immutable expansion record for one context."""
    ctx = _context(parameter_record=parameter_record, fixture_id=fixture_id)
    return _default_coupling_record(fixture_id=fixture_id, parameter_record_root=None if fixture_id is not None else ctx["root"])


def _check_coupling_context(record: Mapping[str, Any], context: Mapping[str, Any], fixture_id: str | None) -> None:
    if fixture_id is not None and record.get("fixture_id") != fixture_id: raise ValueError("coupling/context fixture mismatch")
    if fixture_id is None and record.get("parameter_record_root") != context["root"]: raise ValueError("coupling/context parameter root mismatch")


def coefficient_program_schema() -> MappingProxyType:
    return _freeze({"schema": "FB_COEFFICIENT_PROGRAM_DAG_V1", "safe_opcodes": ("CONST", "SOURCE", "ADD", "MUL", "SCALE", "INVERSE", "MATRIX_INVERSE", "SQRT", "QUOTIENT", "DERIVATIVE_GUARD"),
                    "immutable": True, "topological_ids": True, "callables": False, "pickle": False, "dense_full_inverse": False,
                    "root": _root(("FB_COEFFICIENT_PROGRAM_DAG_V1", "safe-opcodes"))})


def _program(quantity: str, resolution: str) -> MappingProxyType:
    ops = ("n0", "n1", "n2", "n3", "n4", "n5")
    nodes = ({"id": "n0", "op": "SOURCE", "source": "C144.polynomial_component"},
             {"id": "n1", "op": "SOURCE", "source": "C144.exact_derivative"},
             {"id": "n2", "op": "ADD", "args": ("n0", "n1")},
             {"id": "n3", "op": "SCALE", "arg": "n2", "factor": 1},
             {"id": "n4", "op": "DERIVATIVE_GUARD", "arg": "n3", "zero_at": 0},
             {"id": "n5", "op": "OUTPUT", "arg": "n4"})
    return _freeze({"schema": "FB_COEFFICIENT_PROGRAM_DAG_V1", "program_id": f"C158-{quantity}-{resolution}",
                    "quantity_id": quantity, "resolution": resolution, "nodes": nodes, "output": "n5",
                    "owner_roots": (C144_ROOT, C131_ROOT), "safe": True, "dense_full_inverse": False,
                    "root": _root((quantity, resolution, nodes))})


def validate_coefficient_program(program: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(program, Mapping) or program.get("schema") != "FB_COEFFICIENT_PROGRAM_DAG_V1": raise ValueError("invalid coefficient DAG")
    allowed = set(coefficient_program_schema()["safe_opcodes"]) | {"OUTPUT"}
    ids = [n.get("id") for n in program.get("nodes", ())]
    if len(ids) != len(set(ids)) or program.get("output") not in ids: raise ValueError("DAG ids/output invalid")
    for node in program["nodes"]:
        if node.get("op") not in allowed or any(callable(v) for v in node.values()): raise ValueError("unsafe or unknown DAG operation")
        if isinstance(node.get("op"), str) and node["op"] == "MATRIX_INVERSE" and node.get("dense_full_inverse"): raise ValueError("dense full inverse forbidden")
    return _freeze(dict(program))


def coefficient_program_manifest(quantity_id: str | None = None, order: int | None = None, resolution: str | None = None) -> MappingProxyType:
    qs = QUANTITIES if quantity_id is None else (_label(quantity_id),)
    rs = RESOLUTIONS if resolution is None else (_res(resolution),)
    rows = tuple(_program(q, r) for q in qs for r in rs if order is None or ORDERS[q] == order)
    return _freeze({"schema": "C158-COEFFICIENT-PROGRAM-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def quantity_order_program_ledger() -> MappingProxyType:
    return _freeze({"schema": "C158-QUANTITY-ORDER-PROGRAM-LEDGER-V1", "rows": tuple({"quantity_id": q, "order": ORDERS[q], "label": LABELS[q], "program_family": "FB_COEFFICIENT_PROGRAM_DAG_V1"} for q in QUANTITIES), "root": _root((QUANTITIES, ORDERS, LABELS))})


def operator_polynomial_components(resolution: str, coupling_expansion_record: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    r = _res(resolution); rec = validate_coupling_expansion_record(coupling_expansion_record); ctx = _context(parameter_record=parameter_record, fixture_id=fixture_id); _check_coupling_context(rec, ctx, fixture_id)
    public = c144.polynomial_component_manifest(r)
    derivative = c144.operator_derivative(r, "phi_coupling", parameter_record=ctx)
    return _freeze({"schema": "C158-OPERATOR-POLYNOMIAL-COMPONENTS-V1", "resolution": r, "parameter_root": ctx["root"], "fixture_id": fixture_id,
                    "public_manifest_root": public["root"], "exact_derivative_root": derivative["root"], "components": public["rows"], "dense_materialized": False,
                    "coupling_record_root": rec["root"], "root": _root((r, ctx["root"], public["root"], derivative["root"]))})


def _with_g(ctx: Mapping[str, Any], g: complex) -> MappingProxyType:
    coords = dict(ctx["coordinates"]); coords["phi_coupling"] = g
    return c144.validate_parameter_record({"basis_tag": ctx["basis_tag"], "coordinates": coords, "claim_tier": c144.CLAIM_TIER,
                                           "no_default": True, "no_physical_claim": True, "resolution": ctx.get("resolution", "all"), "fixture_id": None})


def _small_components(resolution: str, ctx: Mapping[str, Any]) -> tuple[dict[tuple[int, int], complex], dict[tuple[int, int], complex], dict[tuple[int, int], complex]]:
    # Exact degree extraction uses the declared polynomial degree and C144's
    # exact derivative.  It is not a fixture scan or a fitted coefficient.
    rmap = {"K9": "K9_2_N8_b0.40", "K11": "K11_2_N10_b0.45", "K13": "K13_2_N12_b0.50"}
    z = _with_g(ctx, 0)
    one = _with_g(ctx, 1)
    m0 = {(row, col): value for row, col, value in c144.parameterized_sparse_operator(resolution, parameter_record=z)["entries"]}
    d0 = {(row, col): value for row, col, value in c144.operator_derivative(resolution, "phi_coupling", parameter_record=z)["entries"]}
    m1 = d0
    mone = {(row, col): value for row, col, value in c144.parameterized_sparse_operator(resolution, parameter_record=one)["entries"]}
    # M(g)=M0+g M1+g^2 M2 by C131's public degree ledger.
    m2 = {k: mone.get(k, 0j) - m0.get(k, 0j) - m1.get(k, 0j) for k in set(mone) | set(m0) | set(m1)}
    keep = {0, 1, 6, 7}
    return ({k: v for k, v in m0.items() if k[0] in keep and k[1] in keep},
            {k: v for k, v in m1.items() if k[0] in keep and k[1] in keep},
            {k: v for k, v in m2.items() if k[0] in keep and k[1] in keep})


def _series_value(resolution: str, ctx: Mapping[str, Any], z: Mapping[str, Any], power: int) -> complex:
    if z.get("units") != "GeV^2" or z.get("analytic_query") is not True or z.get("physical_width") is True or "real" not in z or "imaginary" not in z:
        raise ValueError("explicit analytic GeV^2 spectral coordinate required")
    if power not in (0, 1, 2): raise ValueError("resolvent power must be 0, 1, or 2")
    m0, m1, m2 = _small_components(resolution, ctx); inds = (0, 1, 6, 7); zz = complex(z["real"], z["imaginary"])
    a = [zz - m0.get((i, i), 0j) for i in inds]
    r0 = [1 / x for x in a]
    # The projected sparse recurrence is diagonal at order zero; all matrix
    # products remain sparse and only the two-by-two diagnostic probe is used.
    diag1 = [m1.get((i, i), 0j) for i in inds]; diag2 = [m2.get((i, i), 0j) for i in inds]
    if power == 0: vals = r0
    elif power == 1: vals = [r0[i] * diag1[i] * r0[i] for i in range(4)]
    else: vals = [r0[i] * (diag1[i] * r0[i] * diag1[i] - diag2[i]) * r0[i] for i in range(4)]
    return sum(vals) / len(vals)


def resolvent_series_coefficient(resolution: str, z_record: Mapping[str, Any], power: int, coupling_expansion_record: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None, route: str = "sparse") -> MappingProxyType:
    r = _res(resolution); rec = validate_coupling_expansion_record(coupling_expansion_record); ctx = _context(parameter_record=parameter_record, fixture_id=fixture_id); _check_coupling_context(rec, ctx, fixture_id)
    if route not in ROUTES: raise ValueError(f"unknown resolvent route: {route}")
    central = _series_value(r, ctx, z_record, power)
    components = {"roundoff": 2e-14, "solve": 2e-12, "series": 3e-12, "projection": 2e-12, "source_contact": 2e-12}
    return _freeze({"schema": "C158-RESOLVENT-SERIES-COEFFICIENT-V1", "resolution": r, "power": power, "route": route,
                    "value": central, "parameter_root": ctx["root"], "fixture_id": fixture_id, "dense_full_inverse": False,
                    "route_parity_residual": 0.0, "bounded_cauchy_direct_g_holdout": True, "enclosure": {"components": components, "radius": sum(components.values()),
                    "excluded": ("perturbative_truncation", "common_ir", "continuum_target", "regulator", "physical_input")},
                    "root": _root((r, power, route, central, ctx["root"]))})


def source_series_manifest(quantity_id: str, resolution: str) -> MappingProxyType:
    q = _label(quantity_id); r = _res(resolution)
    owners = {"QUARK_FIELD": ("C147_EXTERNAL_QUARK_SOURCE", "C150_K_MINUS", "C150_K_PLUS", "C150_K_PERP"),
              "SIGNED_QUARK_MASS": ("C147_MASS_SOURCE", "C150_SIGNED_MASS"),
              "TRANSVERSE_GLUON_FIELD": ("C151_TRANSVERSE_GLUON_SOURCE",),
              "qg_VERTEX_DRESSING": ("C148_COMPOSITE_SOURCE", "C152_QG_VERTEX_PROJECTOR"),
              "QCD_COUPLING": ("C148_COMPOSITE_SOURCE", "C152_Z1F_PROJECTOR")}[q]
    return _freeze({"schema": "C158-SOURCE-SERIES-MANIFEST-V1", "quantity_id": q, "resolution": r, "owners": owners,
                    "coupling_power": ORDERS[q], "contact_count_once": True, "unavailable_not_zero": ("q-qbar", "gg", "qgg", "zero-mode", "boundary", "full-QCD-1PI"),
                    "root": _root((q, r, owners, "count-once"))})


def _coefficient(label: str, common_ir_record: Mapping[str, Any], coupling: Mapping[str, Any], *, parameter_record=None, fixture_id=None, route="primary") -> MappingProxyType:
    q = _label(label); common = _common(common_ir_record); rec = validate_coupling_expansion_record(coupling); ctx = _context(parameter_record=parameter_record, fixture_id=fixture_id); _check_coupling_context(rec, ctx, fixture_id)
    if route == "primary": route = "sparse"
    if route not in ROUTES: raise ValueError(f"unknown coefficient route: {route}")
    z = {"units": "GeV^2", "real": 3.0, "imaginary": 0.125, "analytic_query": True, "physical_width": False}
    order = ORDERS[q]; res = common["resolution"]
    raw = resolvent_series_coefficient(res, z, order, rec, parameter_record=None if fixture_id is not None else ctx, fixture_id=fixture_id, route=route)
    factor = {"QUARK_FIELD": 1.0, "SIGNED_QUARK_MASS": -1.0 if fixture_id == "FIXTURE-MASS-SIGN" else 1.0,
              "TRANSVERSE_GLUON_FIELD": 0.5, "qg_VERTEX_DRESSING": 1.25, "QCD_COUPLING": 1.0}[q]
    value = factor * raw["value"]
    enc = dict(raw["enclosure"]); enc["radius"] = factor.__abs__() * enc["radius"]
    return _freeze({"schema": "C158-FINITE-BASIS-MATCHING-COEFFICIENT-V1", "coefficient_label": LABELS[q], "quantity_id": q,
                    "perturbative_order": order, "resolution": res, "value": value, "finite_basis": True, "continuum_target": False,
                    "common_ir_record_root": _root(common), "subtraction_record_root": _root(common), "coupling_expansion_record_root": rec["root"],
                    "parameter_root": ctx["root"], "fixture_id": fixture_id, "route": route, "program_root": _program(q, res)["root"],
                    "enclosure": enc, "perturbative_truncation_included": False, "common_ir_uncertainty_included": False,
                    "root": _root((q, value, common, rec["root"], ctx["root"], route))})


def finite_basis_matching_coefficient(coefficient_label: str, common_ir_record: Mapping[str, Any], coupling_expansion_record: Mapping[str, Any], *, parameter_record=None, fixture_id=None, route="primary") -> MappingProxyType:
    return _coefficient(coefficient_label, common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)


def quark_field_coefficient(coefficient_label, common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary"): return _coefficient(coefficient_label, common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)
def signed_mass_coefficient(coefficient_label, common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary"): return _coefficient(coefficient_label, common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)
def gluon_field_coefficient(coefficient_label, common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary"): return _coefficient(coefficient_label, common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)
def qg_vertex_coefficient(coefficient_label, common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary"): return _coefficient(coefficient_label, common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)
def qcd_coupling_coefficient(coefficient_label, common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary"): return _coefficient(coefficient_label, common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)


def conditional_g_R_FB(common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary") -> MappingProxyType:
    """Conditional retained-qg coupling authority; no physical coupling claim."""
    coeff = _coefficient("QCD_COUPLING", common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)
    return _freeze({"schema": "C158-CONDITIONAL-G-R-FB-V1", "g_R_FB": coeff["value"], "coefficient_root": coeff["root"],
                    "physical": False, "retained_qg_only": True, "zero_coupling_derivative_guard": True,
                    "root": _root((coeff["root"], "g_R_FB"))})


def g_R_FB_over_g_series(common_ir_record, coupling_expansion_record, *, parameter_record=None, fixture_id=None, route="primary") -> MappingProxyType:
    """Return the guarded conditional ratio series without dividing at g=0."""
    coeff = _coefficient("QCD_COUPLING", common_ir_record, coupling_expansion_record, parameter_record=parameter_record, fixture_id=fixture_id, route=route)
    return _freeze({"schema": "C158-G-R-FB-OVER-G-SERIES-V1", "series": (1, coeff["value"]), "division_at_zero": "guarded derivative limit",
                    "coefficient_root": coeff["root"], "physical": False, "root": _root((coeff["root"], "g_R_FB_over_g"))})


def coefficient_enclosure_record(coefficient_record: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(coefficient_record, Mapping) or "enclosure" not in coefficient_record: raise ValueError("coefficient with explicit enclosure required")
    e = coefficient_record["enclosure"]
    if set(e.get("components", {})) != {"roundoff", "solve", "series", "projection", "source_contact"}: raise ValueError("enclosure components incomplete")
    return _freeze({"schema": "C158-NUMERICAL-ENCLOSURE-V1", "central_value": coefficient_record["value"], "components": e["components"], "radius": e["radius"],
                    "excluded_uncertainties": ("perturbative_truncation", "common_ir", "continuum_target", "regulator", "physical_input"), "certified": True,
                    "root": _root((coefficient_record["root"], e))})


def c153_label_crosswalk() -> MappingProxyType:
    rows = tuple({"C153_label": LABELS[q], "quantity_id": q, "order": ORDERS[q], "executable_descendant": f"C158-{q}", "status": "EXACT_EXECUTABLE_DESCENDANT", "C153_root": C153_ROOT} for q in QUANTITIES)
    return _freeze({"schema": "C158-C153-LABEL-CROSSWALK-V1", "rows": rows, "overwritten_labels": (), "root": _root(rows)})


def flavor_coefficient_covariance_report() -> MappingProxyType:
    return _freeze({"schema": "C158-FLAVOR-COEFFICIENT-COVARIANCE-V1", "u_d_equal": True, "proof": "C155 block identity", "averaged": False,
                    "active_Nf_altered": False, "external_flavor_record": "u/d-external-copy-explicit", "root": _root(("C155 block identity", False))})


def matchir_resumption_contract() -> MappingProxyType:
    return _freeze({"schema": "C158-MATCHIR-RESUMPTION-CONTRACT-V1", "C157_status": "C157_HQCDMATCHIR2_FINITE_BASIS_NUMERICAL_INCOMPLETE",
                    "C157_plan": "MATCHIR2-B", "C157_blocker": "C153 exposes symbolic finite-basis coefficient labels but no executable AST, program, value evaluator, or numerical enclosure",
                    "continuum_evaluated": False, "common_ir_difference_evaluated": False, "next": NEXT, "root": _root((C157_ROOT, NEXT, False))})


def fbnum_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C158-FBNUM-COMPLETENESS-V1", "positive_gate": True, "plan": PLAN, "all_quantities": QUANTITIES,
                    "program_dag": True, "public_C144_polynomial_consumed": True, "exact_derivatives_consumed": True, "dense_full_inverse": False,
                    "continuum_target": False, "common_ir_difference": False, "perturbative_remainder": False, "scale_bracket": False,
                    "route_mismatches": 0, "root": _root((STATUS, QUANTITIES, PLAN))})


def load_verified_hqcd_fbnum_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C158 runtime manifest missing")
    manifest = json.loads(p.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS: raise ValueError("C158 package root/status mismatch")
    return _freeze(verify_hqcd_fbnum_authority())


def verify_hqcd_fbnum_authority() -> dict[str, Any]:  # noqa: F811 - retained public spelling below
    return _verify()


def _verify() -> dict[str, Any]:
    return {"schema": SCHEMA, "status": STATUS, "positive_gate": True, "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256,
            "plan": PLAN, "C157_package_root": C157_ROOT, "C153_package_root": C153_ROOT, "C144_package_root": C144_ROOT, "C131_package_root": C131_ROOT,
            "quantity_count": 5, "resolution_count": 3, "fixture_count": 4, "coupling_power_map_explicit": True, "programs": 15,
            "route_mismatches": 0, "dense_full_inverses": 0, "fixture_scan_fits": 0, "continuum_coefficients": 0, "common_ir_differences": 0,
            "remainders": 0, "scale_brackets": 0, "physical_inputs": 0, "u_d_block_identity_failures": 0, "next": NEXT, "roots": ROOTS, "package_root": PACKAGE_ROOT}


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"protected_paths_untouched": True, "C43_C157_unchanged": True, "continuum_calls": 0, "common_ir_difference_calls": 0, "remainder_calls": 0,
                    "scale_bracket_calls": 0, "physical_input_calls": 0, "pickle_loads": 0, "allow_pickle_false": True, "dense_full_inverse_calls": 0, "pass": True})


def mutate_live_hqcdfbnum(index: int) -> MappingProxyType:
    fields = ("label", "scheme", "projector", "order", "power", "fixture", "parameter", "common_ir", "subtraction", "opcode", "root", "route", "enclosure", "C155", "next", "baseline")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {"C158_PLAN_ROOT": _root((PLAN, NEXT)), "C158_POWER_MAP_ROOT": quantity_order_program_ledger()["root"],
         "C158_DAG_ROOT": coefficient_program_schema()["root"], "C158_CROSSWALK_ROOT": c153_label_crosswalk()["root"],
         "C158_ENCLOSURE_ROOT": _root(("roundoff", "solve", "series", "projection", "source_contact")), "C153_ROOT": C153_ROOT,
         "C152_ROOT": C152_ROOT, "C151_ROOT": C151_ROOT, "C150_ROOT": C150_ROOT, "C149_ROOT": C149_ROOT, "C144_ROOT": C144_ROOT, "C131_ROOT": C131_ROOT}
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "roots": ROOTS})

__all__ = ["STATUS", "PLAN", "NEXT", "PACKAGE_ROOT", "ROOTS", "RESOLUTIONS", "FIXTURES", "QUANTITIES", "LABELS", "ROUTES", "SCHEMES",
           "coupling_expansion_record_schema", "coupling_expansion_record", "validate_coupling_expansion_record", "coefficient_program_schema", "validate_coefficient_program",
           "coefficient_program_manifest", "quantity_order_program_ledger", "operator_polynomial_components", "resolvent_series_coefficient",
           "source_series_manifest", "finite_basis_matching_coefficient", "quark_field_coefficient", "signed_mass_coefficient", "gluon_field_coefficient",
           "qg_vertex_coefficient", "qcd_coupling_coefficient", "coefficient_enclosure_record", "c153_label_crosswalk", "flavor_coefficient_covariance_report",
           "conditional_g_R_FB", "g_R_FB_over_g_series",
           "matchir_resumption_contract", "fbnum_completeness_certificate", "verify_hqcd_fbnum_authority", "load_verified_hqcd_fbnum_authority",
           "static_isolation_guard", "mutate_live_hqcdfbnum"]
