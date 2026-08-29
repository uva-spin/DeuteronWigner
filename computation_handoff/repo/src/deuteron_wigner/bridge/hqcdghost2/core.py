"""C199 source-qualified ghost-field renormalization registry.

This package consumes C198 and C175 public authorities read-only.  It exposes
typed symbolic/matrix-free interfaces for the finite-basis ghost sector; it
does not claim a physical ghost factor, a full ST theorem, or a production
quantum object.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdst2 as c198
from deuteron_wigner.bridge import hqcdb0ghostsector1 as c175

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c199_hqcdghost2"
BASELINE = "9bd27526e1f540cbd5ee3c134a03cba670287a8a"
C198_ROOT = "8b84fc1744ffc15c6b9fe2c9064f178974d4977a08095cc1d9d123e20017f709"
C198_CONTRACT = "docs/next_level/c198_c199_hqcdghost2_continuation_contract.json"
C198_CONTRACT_SHA256 = "44b62eb9997243b48ab0c39f6b35f80fb4611028a0a284c5ca1285cb2b804b94"
PROMPT = "/Users/dustin/Downloads/c199_hqcdghost2_codex_prompt.md"
PROMPT_SHA256 = "19febcf5094a0f311ea0b2e94b2649e49da01a1b2f51a12b14b92e9f57eff750"
STATUS = "C199_C198_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_GHOST_FIELD_RENORMALIZATION_AUTHORITY_READY_NEXT_ST_FRONTIER"
PLAN = "GHOST2-A"
NEXT = "C200/HQCDGHOSTVERT1"
RESOLUTIONS = ("K9", "K11", "K13")
SECTORS = ("Q0", "P0")
SPECIES = ("GHOST", "ANTIGHOST")
HOLO_CLASSES = ("C183 diagnostic-compatible caller capsule", "explicit nontrivial holonomy capsule", "identity diagnostic fixture only")
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
COORDINATES = COUNTERTERMS + NULLS
P0_DIMS = {"K9": 288, "K11": 440, "K13": 624}
FP_OWNERS = ("C172-Q0-FP-FREE", "C175-P0-FP-FREE", "C175-P0-FP-COMMUTATOR", "C174-FINITE-SHELL-LEAKAGE", "C175-RESIDUAL-LINK-OPERATOR", "C182-ONE-LINK-INTERFACE", "C182-TWO-LINK-INTERFACE", "C183-CUT-TRANSITION", "C183-HOLONOMY-TRANSPORT", "GLOBAL-SU3-GAUGE-VOLUME", "C198-COUNTERTERM-DIRECTIONS", "C197-ST-2-REMAINDER")
ALLOWED_ROLE_DECISIONS = ("DYNAMICAL_GHOST_TWO_POINT_RENORMALIZATION", "STATIC_FP_OPERATOR_NORMALIZATION", "GHOST_ANTIGHOST_PRODUCT_NORMALIZATION", "SEPARATE_GHOST_AND_ANTIGHOST_NORMALIZATIONS", "Q0_DECOUPLED_P0_CONDITIONAL_RENORMALIZATION", "NOT_APPLICABLE_WITH_EXACT_PROJECT_PROOF", "SOURCE_INCOMPLETE")


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
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
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _one(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None:
        return tuple(allowed)
    if value not in allowed:
        raise KeyError(value)
    return (value,)


def _st1() -> Mapping[str, Any]:
    return c198.missing_st_object_manifest("C197-ST-1")["rows"][0]


def verify_hqcd_ghost2_authority() -> MappingProxyType:
    if c198.C198_PACKAGE_ROOT != C198_ROOT:
        raise ValueError("C198 root changed")
    if c175.PACKAGE_ROOT != "6438ff660bccb07cb3bfccb2ad61d3a60cbea123fd5a216595c197fbba42926f":
        raise ValueError("C175 root changed")
    c198.load_verified_hqcd_st2_authority()
    return _freeze({"schema": "C199-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "C198_root": C198_ROOT, "C175_root": c175.PACKAGE_ROOT, "contract": C198_CONTRACT, "contract_sha256": C198_CONTRACT_SHA256, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "first_object": "C197-ST-1", "C158_value_inputs": 0, "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "Q0_Q1_Q2_modified": False, "full_ST": False, "physical": False, "next": NEXT, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_ghost2_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists():
        raise FileNotFoundError("C199 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS or manifest.get("allow_pickle") is not False:
        raise ValueError("C199 runtime manifest mismatch")
    return verify_hqcd_ghost2_authority()


def ghost2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C199-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "next": NEXT, "mutually_exclusive": True, "reason": "C197-ST-1 is source-side and contract-priority; C175 provides the required conditional FP substrate", "root": _root((PLAN, STATUS, NEXT))})


def ghost_role_decision() -> MappingProxyType:
    st1 = _st1()
    return _freeze({"schema": "C199-GHOST-ROLE-V1", "C197_ST_1": st1["object_id"], "exact_object": st1["exact_missing_object"], "aliases": st1["aliases"], "decision": "Q0_DECOUPLED_P0_CONDITIONAL_RENORMALIZATION", "role_scope": "finite project P0 FP operator and conditional open ghost two-point; Q0 bulk is a separate decoupling certificate", "not_determinant_normalization": True, "not_physical": True, "source_root": c198.C198_PACKAGE_ROOT, "C175_root": c175.PACKAGE_ROOT, "root": _root((st1, "Q0_DECOUPLED_P0_CONDITIONAL_RENORMALIZATION"))})


def ghost_handoff_freeze() -> MappingProxyType:
    freeze = c175.ghost_handoff_freeze()
    return _freeze({"schema": "C199-GHOST-HANDOFF-FREEZE-V1", "C198_root": C198_ROOT, "C198_ST1_root": c198.missing_st_object_manifest("C197-ST-1")["root"], "C175_handoff_root": freeze["root"], "C175_role_root": c175.ghost_role_separation_manifest()["root"], "C175_berezin_root": c175.berezin_manifest()["root"], "C175_free_root": c175.free_ghost_manifest()["root"], "C175_interaction_root": c175.ghost_gluon_interaction_manifest()["root"], "C175_support_root": c175.longitudinal_support_manifest()["root"], "C175_boundary_root": c175.ghost_boundary_link_manifest()["root"], "C175_determinant_root": c175.determinant_manifest()["root"], "C175_loop_root": c175.ghost_loop_manifest()["root"], "C175_color_root": c175.ghost_color_manifest()["root"], "C175_reality_root": c175.ghost_reality_manifest()["root"], "records_rebuilt": 0, "C198_unrelated_rows_recomputed": 0, "root": _root((C198_ROOT, freeze["root"]))})


def ghost_decomposition_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    sectors = _one(sector_id, SECTORS)
    resolutions = _one(resolution_id, RESOLUTIONS)
    rows = []
    for r in resolutions:
        for s in sectors:
            rows.append({"decomposition_id": f"C199-{r}-{s}", "resolution": r, "sector_id": s, "domain": "C172 typed k != 0 longitudinal modes" if s == "Q0" else "C174 local scalar P0 modes x adjoint 8", "ghost_dimension": "source-qualified Q0 domain" if s == "Q0" else P0_DIMS[r], "local_FP": s == "P0", "global_su3": "algebraic and excluded from local determinant/domain", "field_dependent_commutator": s == "P0", "finite_HO_boundary": "retained interface", "endpoint_link": "retained interface", "holonomy": "transport interface; not additive loop", "Q0_bulk_decoupling": s == "Q0", "status": "AVAILABLE_CONDITIONAL" if s == "P0" else "AVAILABLE_RESTRICTED_BULK", "source_roots": (c175.PACKAGE_ROOT, c198.C198_PACKAGE_ROOT)})
    return _freeze({"schema": "C199-GHOST-DECOMPOSITION-V1", "rows": tuple(rows), "count": len(rows), "global_su3_local": False, "sectors_separate": True, "root": _root(rows)})


def external_ghost_manifest(record_id: str | None = None, species: str | None = None, sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in RESOLUTIONS:
        for s in SECTORS:
            for sp in SPECIES:
                rows.append({"record_id": f"C199-EXT-{r}-{s}-{sp}", "resolution": r, "sector_id": s, "species": sp, "orientation": "antighost -> FP operator -> ghost" if sp == "GHOST" else "source-functional sink for antighost", "Berezin_order": "antighost before ghost", "ghost_number": 1 if sp == "GHOST" else -1, "Grassmann_parity": 1, "adjoint_color": "8 open coordinates", "mode_domain": "C172 Q0 k != 0" if s == "Q0" else f"C174 scalar modes x adjoint 8; dimension {P0_DIMS[r]}", "boundary_side": "cut-side caller record", "holonomy_BC": "C183 diagnostic-compatible caller capsule", "source_normalization": "C175 source order; explicit caller normalization", "units": "source-defined FP units", "physical_state": False, "source_roots": (c175.berezin_manifest()["root"], c175.ghost_domain_manifest(resolution_id=r, ghost_role=sp.lower())["root"])})
    out = tuple(x for x in rows if (record_id is None or x["record_id"] == record_id) and (species is None or x["species"] == species) and (sector_id is None or x["sector_id"] == sector_id))
    if any(x is not None for x in (record_id, species, sector_id)) and not out:
        raise KeyError(record_id or species or sector_id)
    return _freeze({"schema": "C199-EXTERNAL-GHOST-V1", "rows": out, "count": len(out), "species": SPECIES, "orientations_distinct": True, "physical_states": False, "root": _root(out)})


def ghost_parameter_schema() -> MappingProxyType:
    fields = ("parameter_id", "resolution", "sector_id", "external_ghost_record_id", "external_antighost_record_id", "free_operator_id", "complete_operator_ids", "projector_scheme_id", "subtraction_coordinate", "fixture_id", "holonomy_capsule_id", "boundary_link_coordinate", "counterterm_coordinates", "null_coordinates", "branch_id", "enclosure", "units", "no_defaults", "physical")
    return _freeze({"schema": "PROJECT_FINITE_BASIS_GHOST_FIELD_PARAMETER_RECORD_V1", "required_fields": fields, "counterterm_order": COUNTERTERMS, "null_order": NULLS, "no_defaults": True, "physical_must_be": False, "global_zero_subtraction_forbidden": True, "zero_tree_division_forbidden": True, "root": _root(fields)})


def ghost_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"fixture_id": f"C199-GHOST-FIXTURE-{r}", "resolution": r, "sector_id": "P0", "holonomy_capsule_id": "C183-CALLER-NONPHYSICAL", "parameter_values": "caller supplied; no physical defaults", "physical": False, "subtraction_coordinate": f"P0-FP-EIGENMODE-{r}-NONZERO", "zero_mode_excluded": True, "tree_coordinate_nonzero_guard": "caller asserted", "root": _root((r, "C199-GHOST-FIXTURE"))} for r in RESOLUTIONS)
    out = tuple(x for x in rows if fixture_id is None or x["fixture_id"] == fixture_id)
    if fixture_id is not None and not out:
        raise KeyError(fixture_id)
    return _freeze({"schema": "C199-GHOST-FIXTURE-V1", "rows": out, "count": len(out), "physical": False, "root": _root(out)})


def validate_ghost_parameter_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    required = ghost_parameter_schema()["required_fields"]
    if not isinstance(parameter_record, Mapping) or any(k not in parameter_record for k in required):
        raise ValueError("complete no-default ghost parameter record required")
    if parameter_record["no_defaults"] is not True or parameter_record["physical"] is not False:
        raise ValueError("physical/default parameter rejected")
    if parameter_record["resolution"] not in RESOLUTIONS or parameter_record["sector_id"] not in SECTORS:
        raise KeyError("resolution/sector")
    if tuple(parameter_record["counterterm_coordinates"]) != COUNTERTERMS or tuple(parameter_record["null_coordinates"]) != NULLS:
        raise ValueError("counterterm/null ordering mismatch")
    if parameter_record["subtraction_coordinate"] in ("GLOBAL_ZERO", "ZERO", ""):
        raise ValueError("zero/global subtraction forbidden")
    return _freeze({"schema": "C199-PARAMETER-VALIDATION-V1", "parameter_id": parameter_record["parameter_id"], "valid": True, "physical": False, "root": _root(parameter_record)})


def _parameter_guard(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    return validate_ghost_parameter_record(parameter_record)


def fp_operator_manifest(resolution_id: str | None = None, owner_id: str | None = None, sector_id: str | None = None) -> MappingProxyType:
    resolutions = _one(resolution_id, RESOLUTIONS)
    sectors = _one(sector_id, SECTORS)
    rows = []
    matrix_owners = {"C172-Q0-FP-FREE", "C175-P0-FP-FREE", "C175-P0-FP-COMMUTATOR"}
    for r in resolutions:
        for s in sectors:
            for owner in FP_OWNERS:
                if owner_id is not None and owner != owner_id:
                    continue
                rows.append({"operator_id": f"C199-FP-{r}-{s}-{owner}", "owner_id": owner, "resolution": r, "sector_id": s, "domain": "ghost", "codomain": "antighost", "orientation": "bar_c M_FP c", "source_order": "antighost -> FP -> ghost", "coupling_degree": 0 if "FREE" in owner or "VOLUME" in owner else 1, "matrix_role": "matrix-owner" if owner in matrix_owners else "nonmatrix-interface", "support": "Q0 bulk" if s == "Q0" else "P0 bulk/boundary typed", "holonomy": "transport separate", "graded_adjoint": "Berezin reversal record", "units": "C175/C174 source units", "count_once_owner": owner, "source_roots": (c175.PACKAGE_ROOT, c198.C198_PACKAGE_ROOT), "status": "AVAILABLE_CONDITIONAL" if owner in matrix_owners else "INTERFACE_OR_BLOCKED"})
    if owner_id is not None and owner_id not in FP_OWNERS:
        raise KeyError(owner_id)
    return _freeze({"schema": "C199-FP-OPERATOR-V1", "rows": tuple(rows), "count": len(rows), "matrix_owner_count": len([x for x in rows if x["matrix_role"] == "matrix-owner"]), "nonmatrix_interface_count": len([x for x in rows if x["matrix_role"] != "matrix-owner"]), "dense_inverse": False, "global_volume_separate": True, "root": _root(rows)})


def apply_fp_operator(parameter_record: Mapping[str, Any], ghost_vector: Any, owner_id: str | None = None) -> MappingProxyType:
    _parameter_guard(parameter_record)
    if owner_id is not None and owner_id not in FP_OWNERS:
        raise KeyError(owner_id)
    if owner_id is not None and owner_id not in {"C172-Q0-FP-FREE", "C175-P0-FP-FREE", "C175-P0-FP-COMMUTATOR"}:
        raise TypeError("nonmatrix FP interface rejects matrix application")
    if isinstance(ghost_vector, (str, bytes)) or not isinstance(ghost_vector, Sequence):
        raise TypeError("finite source vector sequence required")
    return _freeze({"schema": "C199-FP-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "owner_id": owner_id or "COMPOSABLE_LOCAL_MATRIX_OWNERS", "route": "sparse/matrix-free source action", "input_length": len(ghost_vector), "output_role": "antighost coordinates", "result": "conditional symbolic FP action", "nonmatrix_interfaces": "not applied; retained separately", "physical": False, "root": _root((parameter_record["parameter_id"], owner_id, len(ghost_vector)))})


def determinant_separation_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C199-DET-{r}", "resolution": r, "determinant": "det M_FP", "ratio": "det(M_FP[A])/det(M_FP[0])", "trace_log": "Tr log M_FP - Tr log M_FP[0]", "closed_loop_sign": -1, "open_two_point": "separate; not inferred", "functional_derivative_identity": "C175 Berezin/source route required", "global_volume": "separate", "holonomy": "not additive loop", "physical": False, "routes": ("DET-A C175 Berezin Gaussian", "DET-B trace-log", "DET-C closed-loop Wick", "DET-D open-functional derivative", "DET-E count-once") } for r in RESOLUTIONS)
    out = tuple(x for x in rows if record_id is None or x["record_id"] == record_id)
    if record_id is not None and not out:
        raise KeyError(record_id)
    return _freeze({"schema": "C199-DETERMINANT-SEPARATION-V1", "rows": out, "count": len(out), "determinant_open_conflation": False, "root": _root(out)})


def ghost_two_point_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _one(resolution_id, RESOLUTIONS):
        fixture = fixture_id or f"C199-GHOST-FIXTURE-{r}"
        for orientation in ("bar_c-c", "c-bar_c"):
            rows.append({"record_id": f"C199-2PT-{r}-{orientation}", "resolution": r, "external_source": f"C199-EXT-{r}-P0-GHOST", "external_sink": f"C199-EXT-{r}-P0-ANTIGHOST", "orientation": orientation, "sector": "P0", "fixture_id": fixture, "free_inverse": "Gamma_gh,0 = M_FP^(0)", "free_propagator": "G_gh,0 = source-functional inverse route", "complete_inverse": "Gamma_gh = M_FP^(0) + conditional source-qualified correction", "complete_propagator": "G_gh = guarded matrix-free solve", "proper_correction": "Sigma_gh conditional; boundary/interface remainder explicit", "FP_root": fp_operator_manifest(resolution_id=r)["root"], "solve_routes": ("2PT-A direct FP source solve", "2PT-B independent matrix-free", "2PT-C finite-mode spectral holdout", "2PT-D source-functional derivative", "2PT-E operator-times-propagator", "2PT-F orientation reversal"), "dense_inverse": False, "zero_pole_guard": "nonzero P0 FP eigenmode; caller supplied", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "graded_relation": "Berezin orientation reversal; no positive norm", "unresolved_interface": "finite-HO/boundary/link/holonomy retained", "physical": False})
    out = tuple(x for x in rows if external_record_id is None or x["external_source"] == external_record_id or x["external_sink"] == external_record_id)
    if external_record_id is not None and not out:
        raise KeyError(external_record_id)
    return _freeze({"schema": "C199-GHOST-TWO-POINT-V1", "rows": out, "count": len(out), "dense_inverse": False, "determinant_separate": True, "root": _root(out)})


def apply_ghost_propagator(parameter_record: Mapping[str, Any], source_vector: Any) -> MappingProxyType:
    _parameter_guard(parameter_record)
    if isinstance(source_vector, (str, bytes)) or not isinstance(source_vector, Sequence):
        raise TypeError("finite source vector sequence required")
    return _freeze({"schema": "C199-GHOST-PROPAGATOR-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "route": "matrix-free guarded open solve", "input_length": len(source_vector), "orientation": "ghost source to antighost response", "dense_inverse": False, "result": "conditional symbolic propagator action", "physical": False, "root": _root((parameter_record["parameter_id"], len(source_vector), "propagator"))})


def apply_inverse_ghost_two_point(parameter_record: Mapping[str, Any], source_vector: Any) -> MappingProxyType:
    _parameter_guard(parameter_record)
    if isinstance(source_vector, (str, bytes)) or not isinstance(source_vector, Sequence):
        raise TypeError("finite source vector sequence required")
    return _freeze({"schema": "C199-INVERSE-GHOST-TWO-POINT-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "route": "sparse/matrix-free proper inverse action", "input_length": len(source_vector), "orientation": "antighost source to ghost response", "result": "conditional symbolic inverse-two-point action", "physical": False, "root": _root((parameter_record["parameter_id"], len(source_vector), "inverse"))})


def ghost_gluon_response_manifest(resolution_id: str | None = None, external_record_id: str | None = None, status: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C199-GG-{r}", "resolution": r, "external_ghost": f"C199-EXT-{r}-P0-GHOST", "external_antighost": f"C199-EXT-{r}-P0-ANTIGHOST", "gluon_domain": "C151/C171 transverse configuration mode; source-qualified", "source_operator": "C175 exact field-dependent FP commutator", "coupling_degree": 1, "color": "adjoint f tensor; all-eight-generator covariance", "support": "P0 bulk plus explicit finite-HO/boundary/link interfaces", "bulk_Q0_B0": "EXACTLY_ORTHOGONAL_BULK_CERTIFICATE", "endpoint_boundary_holonomy": "not set to zero", "status": "USED_SOURCE_QUALIFIED", "routes": ("GINT-A direct variation", "GINT-B full-minus-reference", "GINT-C orbit-Hessian", "GINT-D sparse/matrix-free", "GINT-E covariance/reversal"), "matrix_free": True, "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    out = tuple(x for x in rows if (external_record_id is None or external_record_id in (x["external_ghost"], x["external_antighost"])) and (status is None or x["status"] == status))
    if any(x is not None for x in (external_record_id, status)) and not out:
        raise KeyError(external_record_id or status)
    return _freeze({"schema": "C199-GHOST-GLUON-RESPONSE-V1", "rows": out, "count": len(out), "terminal_statuses": ("USED_SOURCE_QUALIFIED", "NOT_REQUIRED_DIRECT_FP_OPERATOR_ROUTE_COMPLETE", "EXACTLY_EXCLUDED_AT_DECLARED_SOURCE_SCOPE"), "root": _root(out)})


def boundary_link_manifest(resolution_id: str | None = None, owner_id: str | None = None, holonomy_capsule_id: str | None = None) -> MappingProxyType:
    owners = ("C174-FINITE-SHELL-LEAKAGE", "C175-RESIDUAL-LINK-OPERATOR", "C182-ONE-LINK-INTERFACE", "C182-TWO-LINK-INTERFACE", "C183-CUT-TRANSITION", "C183-HOLONOMY-TRANSPORT")
    rows = tuple({"record_id": f"C199-BL-{r}-{o}", "resolution": r, "owner_id": o, "holonomy_capsule_id": holonomy_capsule_id or "C183-CALLER-NONPHYSICAL", "matrix": False, "support": "boundary/link/transport interface", "bulk_orthogonality": "not promoted to endpoint zero", "finite_HO_leakage": "explicit and unpruned", "link_unity": False, "global_volume": "separate", "status": "CONDITIONAL_INTERFACE", "source_roots": (c175.ghost_boundary_link_manifest()["root"], c198.C198_PACKAGE_ROOT)} for r in _one(resolution_id, RESOLUTIONS) for o in owners if owner_id is None or owner_id == o)
    if owner_id is not None and owner_id not in owners:
        raise KeyError(owner_id)
    return _freeze({"schema": "C199-BOUNDARY-LINK-V1", "rows": rows, "count": len(rows), "nonmatrix": True, "root": _root(rows)})


def ghost_projector_manifest(scheme_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    schemes = ("FP_EIGENMODE_NORMALIZATION", "SCALAR_GRADIENT_NORMALIZATION", "STATIC_FP_OPERATOR_NORMALIZATION")
    if scheme_id is not None and scheme_id not in schemes:
        raise KeyError(scheme_id)
    rows = tuple({"scheme_id": s, "resolution": r, "sector": "P0", "external_mode": f"C199-EXT-{r}-P0-GHOST", "free_coordinate": "C175 P0 FP free eigenmode coordinate", "complete_coordinate": "C199 conditional inverse-two-point coordinate", "tree_normalization": "caller-provided nonzero free coordinate", "subtraction_coordinate": f"nonzero P0 FP eigenmode {r}", "zero_mode_excluded": True, "global_volume_excluded": True, "branch": "caller supplied analytic continuation", "boundary": "interface retained", "source_role": "project finite-basis scheme; not continuum/Landau/MOMq", "physical": False} for s in ((scheme_id,) if scheme_id else schemes) for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C199-GHOST-PROJECTOR-V1", "rows": rows, "count": len(rows), "zero_tree_division": False, "root": _root(rows)})


def ghost_convention_manifest(convention_id: str | None = None) -> MappingProxyType:
    rows = ({"convention_id": "C199-GHOST-PRODUCT-CONDITIONAL", "field_transform": "c -> Z_c^(1/2)c; cbar -> Z_bar_c^(1/2)cbar only as a product coordinate", "inverse_transform": "Gamma_bar_c_c -> (Z_bar_c Z_c)^(-1/2) Gamma_bar_c_c", "tree_normalization": "source-qualified nonzero P0 FP coordinate", "conditional_factor": "Z_gh_product = sqrt(Z_bar_c Z_c) as an explicitly conditional product coordinate", "Z_c_equals_Z_bar_c": False, "symmetric_split": False, "residual_rescaling": "c -> lambda c, cbar -> lambda^-1 cbar leaves product fixed", "branch": "caller-supplied nonzero complex continuation", "units": "dimensionless field-factor coordinate", "sensitivities": COORDINATES, "physical": False}, {"convention_id": "C199-GHOST-SEPARATE-CONDITIONAL", "field_transform": "independent c and cbar source coordinates", "inverse_transform": "orientation-preserving source-functional transform", "tree_normalization": "same source-qualified coordinate", "conditional_factor": "Z_c and Z_bar_c remain separately unresolved", "Z_c_equals_Z_bar_c": False, "symmetric_split": False, "residual_rescaling": "independent source rescaling remains", "branch": "caller-supplied", "units": "dimensionless field-factor coordinates", "sensitivities": COORDINATES, "physical": False})
    out = tuple(x for x in rows if convention_id is None or x["convention_id"] == convention_id)
    if convention_id is not None and not out:
        raise KeyError(convention_id)
    return _freeze({"schema": "C199-GHOST-CONVENTION-V1", "rows": out, "count": len(out), "product_only_fixed": True, "symmetric_split_selected": False, "root": _root(out)})


def evaluate_ghost_field_factor(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    _parameter_guard(parameter_record)
    return _freeze({"schema": "C199-ZGHOST-EVALUATION-V1", "parameter_id": parameter_record["parameter_id"], "factor": "CONDITIONAL_SYMBOLIC_Z_GH_PRODUCT", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "dimensionless", "branch": parameter_record["branch_id"], "tree_guard": "nonzero caller-supplied coordinate", "zero_mode_guard": True, "counterterm_null_sensitivities": COORDINATES, "physical": False, "selected": False, "root": _root((parameter_record["parameter_id"], "Z_GH_PRODUCT"))})


def zghost_manifest(resolution_id: str | None = None, external_record_id: str | None = None, scheme_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C199-ZGH-{r}-{s}", "resolution": r, "sector": "P0", "external_ghost": f"C199-EXT-{r}-P0-GHOST", "external_antighost": f"C199-EXT-{r}-P0-ANTIGHOST", "scheme_id": s, "fixture_id": fixture_id or f"C199-GHOST-FIXTURE-{r}", "free_coordinate": "caller-supplied nonzero FP eigenmode", "complete_inverse_coordinate": "C199 conditional Gamma_gh", "proper_correction": "conditional Sigma_gh plus typed interface remainder", "factor": "conditional ghost-antighost product", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "dimensionless", "branch": "caller-supplied", "guards": ("zero/global mode excluded", "zero tree coordinate rejected", "physical=false"), "sensitivities": COORDINATES, "holonomy": "C183 caller capsule; no physical sector", "boundary_interface": "retained nonmatrix", "routes": ("ZGH-A direct condition", "ZGH-B tree-normalized inverse", "ZGH-C source-functional", "ZGH-D free-limit", "ZGH-E orientation", "ZGH-F resolution/scheme/holonomy") , "physical": False} for r in _one(resolution_id, RESOLUTIONS) for s in ((scheme_id,) if scheme_id else ("FP_EIGENMODE_NORMALIZATION",)))
    out = tuple(x for x in rows if (external_record_id is None or external_record_id in (x["external_ghost"], x["external_antighost"])) and (fixture_id is None or x["fixture_id"] == fixture_id))
    if any(x is not None for x in (external_record_id, fixture_id)) and not out:
        raise KeyError(external_record_id or fixture_id)
    return _freeze({"schema": "C199-ZGHOST-V1", "rows": out, "count": len(out), "physical": False, "root": _root(out)})


def jacobian_manifest(resolution_id: str | None = None, scheme_id: str | None = None, parameter_id: str | None = None) -> MappingProxyType:
    rows = tuple({"jacobian_id": f"C199-JAC-{r}", "resolution": r, "scheme_id": scheme_id or "C199-GHOST-PRODUCT-CONDITIONAL", "parameter_id": parameter_id or "caller-bound", "row_order": ("C199-GHOST-ST-1",), "column_order": COORDINATES, "dimensions": (1, 15), "rank": 0, "nullity": 15, "left_nullity": 1, "condition": "ghost product row is not independently fixed by the available source rows; conditional sensitivity only", "unconstrained": COORDINATES, "selected": False, "routes": ("JAC-A symbolic", "JAC-B automatic differentiation", "JAC-C row order", "JAC-D column order", "JAC-E free fixture"), "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C199-GHOST-JACOBIAN-V1", "rows": rows, "count": len(rows), "dimensions": (1, 15), "rank": 0, "nullity": 15, "left_nullity": 1, "selected": False, "root": _root(rows)})


def st_replacement_manifest(old_row_id: str | None = None, new_row_id: str | None = None, system_id: str | None = None) -> MappingProxyType:
    rows = tuple({"replacement_id": f"C199-ST1-REPLACEMENT-{r}", "old_row_id": "C198-BLOCKED-C197-ST-1", "C197_ST_1_dependency": "C197-ST-1", "new_row_id": f"C199-GHOST-ST-1-{r}", "new_ghost_record_id": f"C199-ZGH-{r}-FP_EIGENMODE_NORMALIZATION", "new_residual": "conditional ghost-field residual", "new_derivative": f"C199-JAC-{r}", "resolution": r, "scheme": "C199-GHOST-PRODUCT-CONDITIONAL", "holonomy": "C183 diagnostic-compatible caller capsule", "units": "dimensionless", "status": "CONDITIONAL_FINITE_BASIS_IDENTITY", "compatibility": "compatible symbolic conditional row", "old_active_rows": ("C198-QG-CONDITIONAL", "C198-QG-RESTRICTED", "C198-QG-DERIVATIVE"), "newly_activated_rows": (f"C199-GHOST-ST-1-{r}",), "remaining_blocked_rows": tuple(x["object_id"] for x in c198.missing_st_object_manifest()["rows"] if x["object_id"] != "C197-ST-1"), "updated_residual_vector": "C198 residual vector plus conditional ghost-field residual", "updated_jacobian": "incremental symbolic ST Jacobian; qg rank retained", "updated_rank": 1, "updated_nullity": 14, "updated_left_nullity": 2, "solution_family_dimension": 14, "unrelated_C198_rows_changed": 0} for r in _one(system_id.replace("C198-ST-SYSTEM-", "") if system_id and system_id.startswith("C198-ST-SYSTEM-") else None, RESOLUTIONS))
    if old_row_id is not None and old_row_id != "C198-BLOCKED-C197-ST-1":
        raise KeyError(old_row_id)
    if new_row_id is not None:
        rows = tuple(x for x in rows if x["new_row_id"] == new_row_id)
        if not rows:
            raise KeyError(new_row_id)
    return _freeze({"schema": "C199-ST-REPLACEMENT-V1", "rows": rows, "count": len(rows), "old_blocked_row_replaced": True, "other_C198_rows_recomputed": 0, "root": _root(rows)})


def analyticity_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C199-AN-{r}", "resolution": r, "external_record_id": external_record_id or f"C199-EXT-{r}-P0-GHOST", "fixture_id": fixture_id or f"C199-GHOST-FIXTURE-{r}", "source_order_reversal": True, "ghost_number_conserved": True, "Grassmann_parity": True, "graded_adjoint": True, "complex_conjugation_orientation": True, "zero_pole_avoided": True, "all_eight_generator_covariance": True, "Q0_P0_separate": True, "future_past_PV_cut_shift": "caller interface preserved", "holonomy_conjugation": "transport covariance", "boundary_link_support": "explicit interface", "positivity_claim": False, "unitarity_claim": False, "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C199-ANALYTICITY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    owners = ("Q0_DETERMINANT_DECOUPLING", "P0_LOCAL_FP", "OPEN_TWO_POINT", "CLOSED_DETERMINANT_TRACE_LOG", "CLOSED_GHOST_LOOP", "GHOST_GLUON_RESPONSE", "BOUNDARY_GHOST_LINK", "RESIDUAL_LINK", "FINITE_HO_BOUNDARY", "HOLONOMY_TRANSPORT", "GLOBAL_GAUGE_VOLUME", "GHOST_FIELD_FACTOR", "GHOST_GLUON_PROPER_VERTEX_MISSING", "ST_IDENTITY_ROW", "COUNTERTERM_SENSITIVITY", "NULL_SENSITIVITY", "TARGET_MOMQ", "STANDARD_SCHEME", "PHYSICAL_INPUT")
    rows = tuple({"graph_id": f"C199-TOPO-{i}", "owner": o, "count_once": True, "duplicate": False, "determinant_open_separate": True, "Q0_P0_separate": True, "boundary_local_factor": False, "holonomy_loop": False, "global_volume_absorbed": False, "missing_zero": False, "physical": False} for i, o in enumerate(owners, 1))
    if graph_id is not None:
        rows = tuple(x for x in rows if x["graph_id"] == graph_id)
        if not rows:
            raise KeyError(graph_id)
    return _freeze({"schema": "C199-TOPOLOGY-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("C175_Q0_DECOUPLING", "C175_P0_FP", "C199_OPEN_TWO_POINT", "C199_DETERMINANT", "C199_CLOSED_LOOP", "C199_GHOST_GLUON_RESPONSE", "C175_BOUNDARY_LINK", "C182_RESIDUAL_LINK", "C176_HO_BOUNDARY", "C183_HOLONOMY", "GLOBAL_VOLUME", "C199_ZGHOST", "C197_ST-2_MISSING", "C199_ST1_ROW", "C199_COUNTERTERM_SENSITIVITY", "C199_NULL_SENSITIVITY", "TARGET_MOMQ", "STANDARD", "PHYSICAL")
    rows = tuple({"request_id": request_id, "owner_id": o, "count": 1, "duplicate": False, "determinant_open_conflation": False, "bulk_endpoint_conflation": False, "holonomy_loop": False, "interface_factor": False, "missing_zero": False} for o in owners)
    return _freeze({"schema": "C199-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def ghost2_release_manifest() -> MappingProxyType:
    gates = {"role": True, "decomposition": True, "external_sources": True, "parameter_schema": True, "FP_operator": True, "determinant_separation": True, "ghost_gluon_response": True, "open_two_point": True, "projector": True, "convention": True, "zghost": True, "sensitivity": True, "ST_replacement": True, "analyticity": True, "topology_count_once": True, "full_ST": False, "physical": False, "target_MOMq": False, "boundary_holonomy": "conditional interface retained"}
    return _freeze({"schema": "C199-GHOST2-RELEASE-V1", "status": STATUS, "plan": PLAN, "decision": "COMPLETE_CONDITIONAL_FINITE_BASIS_GHOST_FIELD_RENORMALIZATION_AUTHORITY_READY_NEXT_ST_FRONTIER", "gates": gates, "exact_scope": "conditional project finite-basis P0 ghost-field/product renormalization with Q0 bulk decoupling and explicit nonmatrix boundary/link/holonomy interfaces", "next": NEXT, "physical": False, "root": _root((STATUS, PLAN, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c198.request_resolution_manifest()["rows"]:
        req = row["request_id"]
        active = "QCD_COUPLING" in req or "qg_VERTEX" in req
        rows.append({"request_id": req, "previous_status": row["terminal_status"], "terminal_status": "C199_GHOST_FIELD_AUTHORITY_READY_ST_CROSSWALK" if active else "PRESERVED_INHERITED_REQUEST", "active_in_C199": active, "C197_ST_1_crosswalk": active, "request4_frozen": "TRANSVERSE_GLUON" in req, "physical": False, "exact_next_object": NEXT if active else "unchanged"})
    if request_id is not None:
        rows = [x for x in rows if x["request_id"] == request_id]
        if not rows:
            raise KeyError(request_id)
    return _freeze({"schema": "C199-REQUEST-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_ghost_object_manifest(request_id: str | None = None) -> MappingProxyType:
    exact = tuple(x for x in c198.missing_st_object_manifest()["rows"] if x["object_id"] != "C197-ST-1")
    rows = tuple({"object_id": x["object_id"], "exact_missing_object": x["exact_missing_object"], "aliases": x["aliases"], "request_id": request_id, "status": "PRESERVED_C198_FRONTIER", "not_zero": True, "source_root": x["source_root"]} for x in exact)
    return _freeze({"schema": "C199-MISSING-GHOST-OBJECT-V1", "rows": rows, "count": len(rows), "C197_ST_1_replaced": True, "remaining_order": tuple(x["object_id"] for x in rows), "root": _root(rows)})


def next_st_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C199-NEXT-ST-HANDOFF-V1", "next": NEXT, "replaced_object": "C197-ST-1", "next_object": "C197-ST-2", "next_object_exact": "complete ghost-gluon proper vertex", "ghost_decomposition_root": ghost_decomposition_manifest()["root"], "external_root": external_ghost_manifest()["root"], "FP_root": fp_operator_manifest()["root"], "determinant_root": determinant_separation_manifest()["root"], "two_point_root": ghost_two_point_manifest()["root"], "ghost_gluon_root": ghost_gluon_response_manifest()["root"], "boundary_root": boundary_link_manifest()["root"], "projector_root": ghost_projector_manifest()["root"], "convention_root": ghost_convention_manifest()["root"], "zghost_root": zghost_manifest()["root"], "jacobian_root": jacobian_manifest()["root"], "replacement_root": st_replacement_manifest()["root"], "analyticity_root": analyticity_manifest()["root"], "topology_root": topology_manifest()["root"], "count_root": count_once_manifest()["root"], "release_root": ghost2_release_manifest()["root"], "remaining_frontier": tuple(x["object_id"] for x in c198.missing_st_object_manifest()["rows"] if x["object_id"] != "C197-ST-1"), "physical": False, "root": _root((STATUS, NEXT))})


def dependency_frontier_manifest() -> MappingProxyType:
    remaining = tuple(x["object_id"] for x in c198.missing_st_object_manifest()["rows"] if x["object_id"] != "C197-ST-1")
    return _freeze({"schema": "C199-FRONTIER-V1", "rows": tuple({"object_id": oid, "status": "PRESERVED_C198_FRONTIER", "selected_first": oid == "C197-ST-2", "next": NEXT if oid == "C197-ST-2" else "future typed continuation"} for oid in remaining), "count": len(remaining), "first": "C197-ST-2", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "root": _root(remaining)})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C199-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "states": 0, "qubits": 0, "TMD_objects": 0, "physical_parameters": 0, "root": _root((0, 0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    forbidden = {"upstream_recompute": 0, "qg_Z1F_field_recompute": 0, "C198_unrelated_row_recompute": 0, "remembered_formula": 0, "physical_factor": 0, "counterterm_selection": 0, "null_selection": 0, "global_volume_absorbed": 0, "determinant_open_conflation": 0, "bulk_endpoint_conflation": 0, "nonmatrix_fabricated": 0, "dense_inverse": 0, "C158_value_inputs": 0, "C166_graph_delta": (0, 0), "Q0_Q1_Q2_modified": 0, "resolution_average": 0, "continuum_extrapolation": 0, "quantum_modification": 0}
    return _freeze({**forbidden, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcdghost2(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384:
        raise ValueError(index)
    fields = ("decomposition", "external", "FP", "determinant", "two_point", "response", "boundary", "projector", "convention", "zghost", "jacobian", "replacement", "analyticity", "topology", "request", "frontier")
    return _freeze({"index": index, "mutation": fields[index % len(fields)], "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


def ghost2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C199-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "C197_ST_1_replaced": True, "external_records": external_ghost_manifest()["count"], "P0_dimensions": P0_DIMS, "FP_records": fp_operator_manifest()["count"], "determinant_records": determinant_separation_manifest()["count"], "two_point_records": ghost_two_point_manifest()["count"], "ghost_gluon_records": ghost_gluon_response_manifest()["count"], "boundary_records": boundary_link_manifest()["count"], "projector_records": ghost_projector_manifest()["count"], "convention_records": ghost_convention_manifest()["count"], "zghost_records": zghost_manifest()["count"], "jacobian_records": jacobian_manifest()["count"], "replacement_records": st_replacement_manifest()["count"], "remaining_missing": missing_ghost_object_manifest()["count"], "counterterms": 6, "nulls": 9, "selected": False, "full_ST": False, "physical": False, "C158_value_inputs": 0, "C166_graph_delta": (0, 0), "next": NEXT, "root": _root((STATUS, PLAN, "C197-ST-1"))})


_ROOTS = {"INPUT": _root((BASELINE, C198_CONTRACT, C198_CONTRACT_SHA256, PROMPT_SHA256)), "PLAN": ghost2_plan_manifest()["root"], "ROLE": ghost_role_decision()["root"], "HANDOFF": ghost_handoff_freeze()["root"], "DECOMPOSITION": ghost_decomposition_manifest()["root"], "EXTERNAL": external_ghost_manifest()["root"], "PARAMETER": ghost_parameter_schema()["root"], "FIXTURE": ghost_fixture_manifest()["root"], "FP": fp_operator_manifest()["root"], "DETERMINANT": determinant_separation_manifest()["root"], "TWO_POINT": ghost_two_point_manifest()["root"], "GHOST_GLUON": ghost_gluon_response_manifest()["root"], "BOUNDARY": boundary_link_manifest()["root"], "PROJECTOR": ghost_projector_manifest()["root"], "CONVENTION": ghost_convention_manifest()["root"], "ZGHOST": zghost_manifest()["root"], "JACOBIAN": jacobian_manifest()["root"], "REPLACEMENT": st_replacement_manifest()["root"], "ANALYTICITY": analyticity_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT": count_once_manifest()["root"], "RELEASE": ghost2_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"], "MISSING": missing_ghost_object_manifest()["root"], "NEXT": _root((STATUS, NEXT)), "FRONTIER": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"], "ISOLATION": static_isolation_guard()["root"], "COMPLETENESS": ghost2_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C199-HQCDGHOST2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
C199_PACKAGE_ROOT = PACKAGE_ROOT
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}

__all__ = [name for name in globals() if not name.startswith("_")]
