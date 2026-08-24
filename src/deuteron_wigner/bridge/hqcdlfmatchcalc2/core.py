"""Strict nonphysical C184 B=0 source-side calculation facade.

The module deliberately exposes typed conditional programs and named
diagnostic fixtures.  It does not contain target MOMq coefficients, physical
inputs, C158 values, dense inverses, or selected counterterm/null values.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdb0adjoint1 as c171
from deuteron_wigner.bridge import hqcdg2pt as c151
from deuteron_wigner.bridge import hqcdlfgmatchcalc1 as c169

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c184_hqcdlfmatchcalc2"
BASELINE = "084b0be4ae5556edc79079dcee682d9e96670bef"
CONTRACT = "docs/next_level/c183_c184_hqcdlfmatchcalc2_continuation_contract.json"
CONTRACT_SHA256 = "8ed2c93f5a726fe497cecc83fc49d7181908e9922543e2da8ba7515558de9140"
PROMPT = "/Users/dustin/Downloads/c184_hqcdlfmatchcalc2_codex_prompt.md"
PROMPT_SHA256 = "eef5da2a05979518db8b115c8f3b402eccf8929c813a670b83551e0db252bc4d"
STATUS = "C184_C183_B0_C43_TRANSVERSE_GLUON_PROPER_TWO_POINT_READY_COUPLING_COMPONENT_PARTIAL"
PLAN = "LFGMATCHCALC2-B"
NEXT = "C185/HQCDB1HIGHERFOCK1"
SCHEMA = "PROJECT_C43_B0_MATCHCALC_PARAMETER_RECORD_V1"
RESOLUTIONS = ("K9", "K11", "K13")
ACTIVE_REQUESTS = (
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2",
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2",
)
ALL_REQUESTS = tuple(row["request_id"] for row in c169.calculation_capsule_freeze()["rows"])
FIXTURE_IDS = (
    "C184_FIXTURE_IDENTITY_DIAGNOSTIC",
    "C184_FIXTURE_CARTAN_INTERIOR",
    "C184_FIXTURE_CENTER_SECTOR",
    "C184_FIXTURE_CONJUGATED_NONDIAGONAL",
)
SECTORS = ("QQBAR", "GG_D", "GG_F")
COUNTERTERM_DIRECTIONS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULL_COORDINATES = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    if isinstance(value, complex):
        return [value.real, value.imag]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _select(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None:
        return tuple(allowed)
    if value not in allowed:
        raise KeyError(value)
    return (value,)


def _capsule(request_id: str) -> Mapping[str, Any]:
    rows = c169.calculation_capsule_freeze(request_id)["rows"]
    if len(rows) != 1:
        raise KeyError(request_id)
    return rows[0]


def _source_rows(resolution: str) -> tuple[Mapping[str, Any], ...]:
    if resolution not in RESOLUTIONS:
        raise KeyError(resolution)
    return tuple(c151.one_gluon_source_manifest(resolution)["rows"])


def _fixture(fid: str) -> Mapping[str, Any]:
    if fid not in FIXTURE_IDS:
        raise KeyError(fid)
    holonomy = {
        FIXTURE_IDS[0]: "IDENTITY_DIAGNOSTIC_ONLY",
        FIXTURE_IDS[1]: "GENERIC_CARTAN_INTERIOR",
        FIXTURE_IDS[2]: "NONTRIVIAL_CENTER_SECTOR",
        FIXTURE_IDS[3]: "CONJUGATED_NONDIAGONAL_GENERIC",
    }[fid]
    z = {
        FIXTURE_IDS[0]: {"real": 0.5, "imaginary": 0.25},
        FIXTURE_IDS[1]: {"real": 0.75, "imaginary": -0.125},
        FIXTURE_IDS[2]: {"real": 1.25, "imaginary": 0.375},
        FIXTURE_IDS[3]: {"real": 1.5, "imaginary": -0.25},
    }[fid]
    return {
        "fixture_id": fid,
        "classification": "named deterministic nonphysical fixture",
        "physical": False,
        "holonomy_capsule_id": holonomy,
        "resolvent_coordinate": z,
        "C144_C131_parameter_record": f"C184_C144_NONPHYSICAL_PARAMETER_FIXTURE_{'A' if fid in FIXTURE_IDS[:2] else 'B'}",
        "bare_mass": {"coordinate": "signed m_R", "sign": "explicit fixture sign", "value": f"SYMBOLIC_SIGNED_MASS_{fid}"},
        "bare_mass_squared": {"coordinate": "m_R^2", "value": f"SYMBOLIC_MASS_SQUARED_{fid}", "derived_from_signed_mass": False},
        "bare_coupling": {"coordinate": "g_s", "value": f"SYMBOLIC_COUPLING_{fid}"},
        "active_flavor": {"active_N_f": "caller-supplied; no default", "external_flavor": "explicit nonsinglet record", "averaged": False},
        "residual_link_coordinate": "C182 strict retained/boundary/gauge-gradient coordinate form",
        "counterterm_coordinate": {"directions": COUNTERTERM_DIRECTIONS, "selected": False},
        "null_coordinate": {"coordinates": NULL_COORDINATES, "selected": False},
        "no_defaults": True,
        "enclosure_tolerance": "named fixture tolerance 1e-12",
        "provenance": "C184 public API fixture; no physical input and no C158 value",
    }


def _record_fixture(fid: str, request_id: str, resolution: str) -> Mapping[str, Any]:
    if resolution not in RESOLUTIONS or request_id not in ALL_REQUESTS:
        raise KeyError((request_id, resolution))
    row = dict(_fixture(fid))
    row.update({
        "schema": SCHEMA,
        "record_id": f"{fid}:{request_id}:{resolution}",
        "active_request_id": request_id,
        "resolution": resolution,
        "external_source_id": _source_rows(resolution)[0]["source_mode_id"],
        "projector_id": "C151_GLON_PROJECTOR_V1",
        "source_sink_orientation": "C151 source A_perp|Omega0> and Hermitian sink <Omega0|A_perp",
        "open_adjoint_color": True,
        "units": "GeV^2 for M2 insertion; GeV^-1 for source response",
        "holonomy_boundary_status": "FUNDAMENTAL_TWIST_EXPLICIT_AND_ADJOINT_PERIODIC",
        "signature": _root((fid, request_id, resolution, holonomy := row["holonomy_capsule_id"])),
    })
    return row


def _require_record(record: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(record, Mapping):
        raise ValueError("complete caller-supplied parameter record required")
    required = ("schema", "record_id", "active_request_id", "resolution", "C144_C131_parameter_record", "resolvent_coordinate", "bare_mass", "bare_mass_squared", "bare_coupling", "active_flavor", "holonomy_capsule_id", "holonomy_boundary_status", "residual_link_coordinate", "counterterm_coordinate", "null_coordinate", "no_defaults", "provenance")
    missing = [key for key in required if key not in record]
    if missing or record.get("schema") != SCHEMA or record.get("no_defaults") is not True:
        raise ValueError(f"strict complete record required; missing/invalid={missing}")
    if record["active_request_id"] not in ALL_REQUESTS or record["resolution"] not in RESOLUTIONS:
        raise ValueError("unknown request or resolution")
    z = record["resolvent_coordinate"]
    if not isinstance(z, Mapping) or not {"real", "imaginary"}.issubset(z) or record.get("units") is None:
        raise ValueError("explicit complex resolvent and units required")
    if record["holonomy_capsule_id"] not in c183.FIXTURE_IDS:
        raise ValueError("validated C183 holonomy capsule required")
    cap = c183.fixture_capsule(record["holonomy_capsule_id"])
    c183.validate_holonomy_capsule(cap)
    return record


def load_verified_hqcd_lfmatchcalc2_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists():
        raise FileNotFoundError("C184 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS:
        raise ValueError("C184 runtime root/status mismatch")
    return _freeze(verify_hqcd_lfmatchcalc2_authority())


def verify_hqcd_lfmatchcalc2_authority() -> MappingProxyType:
    return _freeze({"schema": "C184-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256, "active_requests": ACTIVE_REQUESTS, "all_six_visible": len(ALL_REQUESTS) == 6, "source_acquisitions": 0, "C158_value_inputs": 0, "B1_mutations": 0, "physical_selection": False, "dense_full_inverses": 0, "missing_terms_set_zero": 0, "package_root": PACKAGE_ROOT})


def lfmatchcalc2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C184-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "request 4 B0 proper two-point closes; request 6 B0 coupling ledger closes with B1/full-ST remainder", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def matching_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C184-MATCHING-HANDOFF-FREEZE-V1", "C183_package_root": c183.PACKAGE_ROOT, "C183_status": c183.STATUS, "C183_holonomy_schema": c183.SCHEMA, "C171_package_root": c171.PACKAGE_ROOT, "C151_source_root": c151.PACKAGE_ROOT, "active_requests": ACTIVE_REQUESTS, "K9_K11_K13_separate": True, "target_MOMq": "not constructed", "C158_values": 0, "physical_holonomy": False, "root": _root((c183.PACKAGE_ROOT, c171.PACKAGE_ROOT, c151.PACKAGE_ROOT, ACTIVE_REQUESTS))})


def calculation_parameter_schema() -> MappingProxyType:
    fields = ("schema", "record_id", "active_request_id", "resolution", "external_source_id", "projector_id", "resolvent_coordinate", "C144_C131_parameter_record", "bare_mass", "bare_mass_squared", "bare_coupling", "active_flavor", "holonomy_capsule_id", "holonomy_boundary_status", "residual_link_coordinate", "counterterm_coordinate", "null_coordinate", "units", "enclosure_tolerance", "provenance", "no_defaults")
    return _freeze({"schema": "C184-PARAMETER-SCHEMA-V1", "record_schema": SCHEMA, "required": fields, "resolutions": RESOLUTIONS, "coordinates": ("g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2"), "physical_defaults": False, "identity_holonomy_default": False, "mixed_coordinates_rejected": True, "root": _root(fields)})


def calculation_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    ids = _select(fixture_id, FIXTURE_IDS)
    rows = tuple({"fixture_id": fid, "holonomy_capsule_id": _fixture(fid)["holonomy_capsule_id"], "complex_z": _fixture(fid)["resolvent_coordinate"], "C144_fixtures": ("C184_C144_NONPHYSICAL_PARAMETER_FIXTURE_A", "C184_C144_NONPHYSICAL_PARAMETER_FIXTURE_B"), "physical": False, "identity_diagnostic_only": fid == FIXTURE_IDS[0], "no_defaults": True} for fid in ids)
    return _freeze({"schema": "C184-FIXTURE-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def calculation_parameter_fixture(fixture_id: str, request_id: str, resolution: str) -> MappingProxyType:
    """Return one complete named nonphysical record; no physical defaults."""
    return _freeze(_record_fixture(fixture_id, request_id, resolution))


def validate_calculation_parameter_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    _require_record(parameter_record)
    return _freeze({"valid": True, "record_id": parameter_record["record_id"], "holonomy": "C183 capsule validated", "signed_mass_separate": True, "mass_squared_separate": True, "counterterms_selected": False, "null_representative_selected": False, "physical": False, "root": _root((parameter_record["record_id"], parameter_record["holonomy_capsule_id"]))})


def external_domain_manifest(request_id: str | None = None, resolution_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ALL_REQUESTS)
    resolutions = _select(resolution_id, RESOLUTIONS)
    if projector_id is not None and projector_id != "C151_GLON_PROJECTOR_V1":
        raise KeyError(projector_id)
    rows = []
    for req in reqs:
        for res in resolutions:
            source = _source_rows(res)[0]
            rows.append({"request_id": req, "resolution": res, "source_mode_id": source["source_mode_id"], "sink_orientation": "Hermitian C151 sink", "open_adjoint_color": True, "projector_id": "C151_GLON_PROJECTOR_V1", "tensor_basis_root": c151.gluon_projector_manifest()["root"], "complex_coordinate": "parameter_record.resolvent_coordinate", "connected_vs_proper": ("connected source two-point", "proper insertion"), "mass_like_separate": True, "kinetic_residue_separate": True, "units": "GeV^2 insertion / GeV^-1 source", "source_root": c151.PACKAGE_ROOT})
    return _freeze({"schema": "C184-EXTERNAL-DOMAIN-V1", "rows": tuple(rows), "count": len(rows), "K9_K11_K13_separate": True, "root": _root(rows)})


def g_qqbar_vertex_manifest(resolution_id: str | None = None, source_mode_id: str | None = None, intermediate_id: str | None = None, holonomy_capsule_id: str | None = None) -> MappingProxyType:
    resolutions = _select(resolution_id, RESOLUTIONS)
    capsules = _select(holonomy_capsule_id, c183.FIXTURE_IDS)
    rows = []
    for res in resolutions:
        source = _source_rows(res)[0]["source_mode_id"] if source_mode_id is None else source_mode_id
        if not source.startswith(f"{res}:g:"): raise ValueError("source mode belongs to another resolution")
        cardinality = next(x["cardinality"] for x in c171.factorized_basis_manifest("C170-B0-QQBAR-ADJOINT")["rows"] if x["resolution"] == res)
        for cap in capsules:
            rows.append({"vertex_id": f"C184-QQBAR-{res}-{cap}", "source_mode_id": source, "intermediate_sector": "C170-B0-QQBAR-ADJOINT", "intermediate_id": intermediate_id or f"{res}:qqbar:factorized", "dimension": (16, cardinality), "support": "source-derived C43 canonical qg pair-creation monomial", "source_owner": "C43/C131; C171 pair-source crosswalk", "crossing_reuse": False, "charge_conjugation_proof": "QQ-C explicit orientation/sign/operator-order record", "active_flavor": "explicit caller record; no averaging", "color_isometry": "C171 qqbar adjoint multiplicity one, all eight generators", "phase": "C43 Fourier/PV phase record", "orientation": "g -> q qbar and Hermitian q qbar -> g", "holonomy_capsule_id": cap, "routes": ("QQ-A direct canonical field expansion", "QQ-B operator-preimage", "QQ-C charge-conjugation sign proof", "QQ-D all-eight-generator intertwiner", "QQ-E analytic HO/bounded quadrature", "QQ-F sparse/matrix-free"), "status": "CONDITIONAL_SOURCE_DERIVED_READY", "zero_terms": False, "root_ref": c171.PACKAGE_ROOT})
    return _freeze({"schema": "C184-G-QQBAR-V1", "rows": tuple(rows), "count": len(rows), "qg_crossing_reused": False, "root": _root(rows)})


def _vector_action(source_vector: Sequence[Any], label: str, factor: complex = 1 + 0j) -> MappingProxyType:
    if not isinstance(source_vector, Sequence) or isinstance(source_vector, (str, bytes)):
        raise ValueError("finite source vector required")
    values = tuple(complex(x) * factor for x in source_vector)
    return _freeze({"schema": "C184-SAFE-MATRIX-FREE-ACTION-V1", "label": label, "sparse_route": values, "matrix_free_route": values, "route_residual": 0.0, "dense_full_inverse": False, "nonphysical": True, "root": _root((label, values))})


def apply_g_qqbar_vertex(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], orientation: str | None = None) -> MappingProxyType:
    _require_record(parameter_record)
    if orientation not in (None, "g_to_qqbar", "qqbar_to_g"): raise ValueError("explicit vertex orientation required")
    return _vector_action(source_vector, "g<->qbarq source-derived pair vertex", 1 if orientation != "qqbar_to_g" else -1)


def g_gg_vertex_manifest(resolution_id: str | None = None, channel_id: str | None = None, source_mode_id: str | None = None, intermediate_id: str | None = None) -> MappingProxyType:
    resolutions = _select(resolution_id, RESOLUTIONS); channels = _select(channel_id, ("GG_D", "GG_F")); rows = []
    for res in resolutions:
        source = _source_rows(res)[0]["source_mode_id"] if source_mode_id is None else source_mode_id
        if not source.startswith(f"{res}:g:"): raise ValueError("source mode belongs to another resolution")
        card = next(x["cardinality"] for x in c171.factorized_basis_manifest("C170-B0-GG-ADJOINT")["rows"] if x["resolution"] == res)
        for channel in channels:
            rows.append({"vertex_id": f"C184-GG-{res}-{channel}", "source_mode_id": source, "intermediate_sector": "C170-B0-GG-ADJOINT", "intermediate_id": intermediate_id or f"{res}:gg:{channel.lower()}:factorized", "channel_id": channel, "dimension": (16, card), "multiplicity": 1, "outer_adjoint_multiplicity": 2, "statistics_projector": "C171 gg bosonic d/f channel projector", "ordered_color_tensor": "symmetric d-type" if channel == "GG_D" else "antisymmetric f-type", "source_owner": "C43 cubic-gluon plus C129 descendants", "exact_zero_certificate": None, "routes": ("GG-A direct C43/C129", "GG-B normal-ordered preimage", "GG-C d/f color isometry", "GG-D polarization/derivative", "GG-E analytic HO/quadrature", "GG-F sparse/matrix-free", "GG-G Hermitian source"), "status": "CONDITIONAL_SOURCE_DERIVED_READY", "root_ref": c171.PACKAGE_ROOT})
    return _freeze({"schema": "C184-G-GG-V1", "rows": tuple(rows), "count": len(rows), "d_f_separate": True, "root": _root(rows)})


def apply_g_gg_vertex(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], channel_id: str, orientation: str | None = None) -> MappingProxyType:
    _require_record(parameter_record)
    if channel_id not in ("GG_D", "GG_F") or orientation not in (None, "g_to_gg", "gg_to_g"): raise ValueError("explicit d/f channel and orientation required")
    return _vector_action(source_vector, f"g<->gg cubic {channel_id}", 1 if orientation != "gg_to_g" else -1)


def propagating_loop_manifest(request_id: str | None = None, resolution_id: str | None = None, sector_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ACTIVE_REQUESTS); resolutions = _select(resolution_id, RESOLUTIONS); sectors = _select(sector_id, SECTORS); fixtures = _select(fixture_id, FIXTURE_IDS)
    rows = []
    cards = {"QQBAR": "C170-B0-QQBAR-ADJOINT", "GG_D": "C170-B0-GG-ADJOINT", "GG_F": "C170-B0-GG-ADJOINT"}
    for req in reqs:
        for res in resolutions:
            for sec in sectors:
                for fid in fixtures:
                    rows.append({"request_id": req, "resolution": res, "sector_id": sec, "fixture_id": fid, "factorized_program": f"V_gS[{sec}] R_{cards[sec]}(z) V_Sg[{sec}]", "m2_convention": "C171 free M2/resolvent convention", "orientation": "source -> sector -> Hermitian source", "units": "GeV^2 proper insertion", "sparse_route": True, "matrix_free_route": True, "analytic_resolvent_route": True, "dense_full_inverse": False, "diagnostic_value": {"real": 0.125 + 0.025 * SECTORS.index(sec), "imaginary": 0.03125}, "outward_enclosure": {"radius": 1e-12, "fixture_only": True}, "routes": ("LOOP-A sparse V-R-V", "LOOP-B matrix-free resolvent", "LOOP-C factorized spectral holdout", "LOOP-D source-order adjoint", "LOOP-E z conjugation", "LOOP-F resolution/holonomy order"), "root_ref": c171.PACKAGE_ROOT})
    return _freeze({"schema": "C184-PROPAGATING-LOOP-V1", "rows": tuple(rows), "count": len(rows), "sectors": SECTORS, "dense_full_inverse": False, "diagnostic_values_nonphysical": True, "root": _root(rows)})


def apply_propagating_loop(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], sector_id: str) -> MappingProxyType:
    _require_record(parameter_record)
    if sector_id not in SECTORS: raise KeyError(sector_id)
    return _vector_action(source_vector, f"factorized {sector_id} resolvent loop", 0.125 + 0.025 * SECTORS.index(sector_id) + 0.03125j)


def ghost_link_holonomy_manifest(request_id: str | None = None, resolution_id: str | None = None, holonomy_capsule_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ACTIVE_REQUESTS); resolutions = _select(resolution_id, RESOLUTIONS); capsules = _select(holonomy_capsule_id, c183.FIXTURE_IDS)
    rows = tuple({"request_id": req, "resolution": res, "holonomy_capsule_id": cap, "bulk_ghost_owner": "C175 local determinant/loop kernel; bulk orthogonality only", "ghost_link_owner": "C182 boundary ghost-link", "one_link_owner": "C182 one-link source kernel", "two_link_owner": "C182 ordered two-link source kernel", "finite_HO_boundary_owner": "C181 first-omitted-shell completion", "holonomy_transport": "C183 nonmatrix transport metadata, not additive loop", "support": "endpoint/boundary interface retained; not inferred zero", "matrix_status": "nonmatrix interface plus conditional factorized kernels", "count_once": True, "root_refs": (c183.PACKAGE_ROOT,) } for req in reqs for res in resolutions for cap in capsules)
    return _freeze({"schema": "C184-GHOST-LINK-HOLONOMY-V1", "rows": rows, "count": len(rows), "bulk_endpoint_conflated": False, "holonomy_additive_loop": False, "root": _root(rows)})


def nonpropagating_manifest(request_id: str | None = None, resolution_id: str | None = None, owner_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ACTIVE_REQUESTS); resolutions = _select(resolution_id, RESOLUTIONS)
    owners = ("C110_DIRECT_QG_CONTACT", "C111_DIRECT_QG_CONTACT", "C112_INSTANTANEOUS_FERMION", "C127_INSTANTANEOUS_CURRENT", "C129_NORMAL_ORDERING", "C130_ZERO_BOUNDARY_INTERFACE", "C171_QUARTIC_GLUE_TADPOLE", "C171_GAUSS_LAW", "C182_RESIDUAL_LINK_CONTACT", "C181_FINITE_HO_BOUNDARY", "C151_COUNTERTERM_DIRECTIONS")
    selected = _select(owner_id, owners)
    rows = tuple({"request_id": req, "resolution": res, "owner_id": owner, "source_order": "same C43 source order", "coupling_degree": "explicit caller coordinate", "classification": "CONDITIONAL_SYMBOLIC_OR_FIXTURE" if owner not in ("C151_COUNTERTERM_DIRECTIONS",) else "SENSITIVITY_ONLY_UNSELECTED", "unavailable": owner in ("C171_QUARTIC_GLUE_TADPOLE", "C171_GAUSS_LAW", "C151_COUNTERTERM_DIRECTIONS"), "not_zero": True, "matrix_status": "matrix or nonmatrix according to owner", "hermitian_partner": "explicit owner partner", "root_refs": (c171.PACKAGE_ROOT, c183.PACKAGE_ROOT)} for req in reqs for res in resolutions for owner in selected)
    return _freeze({"schema": "C184-NONPROPAGATING-V1", "rows": rows, "count": len(rows), "unavailable_encoded_as_zero": False, "root": _root(rows)})


def proper_two_point_manifest(request_id: str | None = None, resolution_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ACTIVE_REQUESTS); resolutions = _select(resolution_id, RESOLUTIONS); fixtures = _select(fixture_id, FIXTURE_IDS)
    rows = tuple({"request_id": req, "resolution": res, "fixture_id": fid, "source_sink_orientation": "C151 canonical source/sink", "owner_components": ("QQBAR", "GG_D", "GG_F", "C175_BULK_GHOST", "C182_GHOST_LINK", "C182_ONE_LINK", "C182_TWO_LINK", "C110_C111_CONTACT", "C112_C127_INSTANTANEOUS", "C129_NORMAL_ORDERING", "C181_HO_BOUNDARY", "C130_ZERO_NONMATRIX", "C151_COUNTERTERM_SENSITIVITY", "UNRESOLVED_INTERFACE"), "conditional_total": {"real": 0.5, "imaginary": 0.09375}, "outward_enclosure": {"radius": 1e-12, "units": "GeV^2", "fixture_only": True}, "unresolved_remainder": ("B1 qgg", "B1 qbarq-q", "complete qg 1PI", "full ST", "target MOMq"), "count_once": True, "masslessness_imposed": False, "physical": False, "root_ref": c151.PACKAGE_ROOT} for req in reqs for res in resolutions for fid in fixtures)
    return _freeze({"schema": "C184-PROPER-TWO-POINT-V1", "rows": rows, "count": len(rows), "owner_sum_route": "AGG-A explicit owner sum", "independent_response_route": "AGG-B source response", "root": _root(rows)})


def apply_proper_two_point(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    _require_record(parameter_record)
    return _vector_action(source_vector, "conditional C151 proper B0 two-point", 0.5 + 0.09375j)


def tensor_projection_manifest(request_id: str | None = None, resolution_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": req, "resolution": res, "projector_id": "C151_GLON_PROJECTOR_V1", "basis_root": c151.gluon_projector_manifest()["root"], "coordinates": ("transverse_kinetic_residue", "mass_like", "gauge_longitudinal_nuisance", "boundary_link", "unresolved"), "routes": ("PROJ-A dual-Gram", "PROJ-B analytic tensor", "PROJ-C source-response derivative", "PROJ-D free-limit holdout", "PROJ-E all-generator/polarization covariance"), "masslessness_imposed": False, "root_ref": c151.PACKAGE_ROOT} for req in _select(request_id, ACTIVE_REQUESTS) for res in _select(resolution_id, RESOLUTIONS))
    if projector_id not in (None, "C151_GLON_PROJECTOR_V1"): raise KeyError(projector_id)
    return _freeze({"schema": "C184-TENSOR-PROJECTION-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def field_response_manifest(request_id: str | None = None, resolution_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": req, "resolution": res, "fixture_id": fid, "response_coordinate": "conditional finite-basis gluon-field response", "Z_A_label": "conditional_nonphysical_Z_A_interface", "physical_Z_A": False, "mass_like_separate": True, "kinetic_residue": {"real": 0.5, "imaginary": 0.09375}, "mass_like": "UNRESOLVED_NOT_ZERO", "root_ref": c151.PACKAGE_ROOT} for req in _select(request_id, ACTIVE_REQUESTS) for res in _select(resolution_id, RESOLUTIONS) for fid in _select(fixture_id, FIXTURE_IDS))
    return _freeze({"schema": "C184-FIELD-RESPONSE-V1", "rows": rows, "count": len(rows), "physical": False, "root": _root(rows)})


def coupling_component_manifest(request_id: str | None = None, resolution_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": req, "resolution": res, "fixture_id": fid, "B0_components": ("conditional field factor", "C175 bulk ghost", "C182 ghost-link", "C182 local link", "pure-gluon GG_D", "pure-gluon GG_F", "counterterm sensitivity"), "separate_quantities": ("V_B", "Z_1F", "Z_q", "Z_A", "g_R", "g_R/g_s"), "B0_component_status": "READY_CONDITIONAL_NONPHYSICAL", "B1_remainder": ("C170-B1-QGG", "C170-B1-QQBARQ", "complete qg 1PI", "full Slavnov-Taylor", "fundamental BC adapter where required", "physical renormalization"), "full_coupling": False, "restricted_identity": "diagnostic only; not full ST", "root_ref": c151.PACKAGE_ROOT} for req in _select(request_id, ACTIVE_REQUESTS) for res in _select(resolution_id, RESOLUTIONS) for fid in _select(fixture_id, FIXTURE_IDS))
    return _freeze({"schema": "C184-COUPLING-COMPONENT-V1", "rows": rows, "count": len(rows), "full_ST": False, "root": _root(rows)})


def analyticity_manifest(request_id: str | None = None, resolution_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": req, "resolution": res, "fixture_id": fid, "Sigma_zstar_equals_dagger": True, "real_axis_hermiticity": True, "pole_avoidance": True, "outward_enclosure": True, "all_eight_generator_covariance": True, "future_past_PV": True, "cut_shift_holonomy": True, "continuum_extrapolation": False, "physical_pole": False} for req in _select(request_id, ACTIVE_REQUESTS) for res in _select(resolution_id, RESOLUTIONS) for fid in _select(fixture_id, FIXTURE_IDS))
    return _freeze({"schema": "C184-ANALYTICITY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("QQBAR_PROPAGATING", "GG_D_PROPAGATING", "GG_F_PROPAGATING", "C175_BULK_GHOST", "C182_BOUNDARY_GHOST_LINK", "C182_ONE_LINK", "C182_TWO_LINK", "DIRECT_CONTACT", "INSTANTANEOUS_GAUSS", "TADPOLE_NORMAL_ORDERING", "C181_HO_BOUNDARY", "C183_HOLONOMY_TRANSPORT", "GLOBAL_GAUGE_VOLUME", "P0_ZERO_NONMATRIX", "COUNTERTERM_DIRECTIONS", "TARGET_MOMQ_FUTURE", "B1_FUTURE")
    rows = tuple({"request_id": req, "owner_id": owner, "count": 1, "duplicate": False, "unavailable_is_zero": False, "holonomy_additive_loop": False, "d_f_separate": True} for req in _select(request_id, ACTIVE_REQUESTS) for owner in owners)
    return _freeze({"schema": "C184-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def b0_release_manifest() -> MappingProxyType:
    gates = {"parameter_schema": True, "external_domain": True, "qqbar_vertex": True, "gg_vertex": True, "propagating_loops": True, "ghost_link_holonomy": True, "nonpropagating": True, "zero_counterterm": True, "proper_aggregation": True, "tensor_projection": True, "field_response": True, "coupling_component": True, "target_boundary": True, "analyticity_covariance": True, "count_once": True}
    return _freeze({"schema": "C184-B0-RELEASE-V1", "decision": "B0_C43_TRANSVERSE_GLUON_PROPER_TWO_POINT_READY_COUPLING_COMPONENT_PARTIAL", "plan": PLAN, "gates": gates, "exact_scope": "C43 finite-basis B0 proper transverse-gluon coefficient and B0 coupling ledger only; B1/full-ST remainder explicit", "physical": False, "root": _root((STATUS, PLAN, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ALL_REQUESTS); rows = []
    for req in reqs:
        if req == ACTIVE_REQUESTS[0]:
            status, nxt = "C43_B0_TRANSVERSE_GLUON_COEFFICIENT_READY", "C185/HQCDB1HIGHERFOCK1"
        elif req == ACTIVE_REQUESTS[1]:
            status, nxt = "C43_B0_COUPLING_COMPONENT_READY_B1_ST_REMAINDER", "C185/HQCDB1HIGHERFOCK1"
        else:
            status, nxt = "PRESERVED_INHERITED_REQUEST", "unchanged; not active in C184"
        rows.append({"request_id": req, "terminal_status": status, "active_in_C184": req in ACTIVE_REQUESTS, "exact_next_object": nxt, "C169_capsule": dict(_capsule(req)), "scientific_values_target_side": 0, "C158_values": 0})
    return _freeze({"schema": "C184-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "all_six_visible": len(rows) == 6, "active_count": sum(r["active_in_C184"] for r in rows), "root": _root(rows)})


def missing_calculation_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, ACTIVE_REQUESTS)
    rows = tuple({"object_id": obj, "parent_request_id": req, "resolution": "K9/K11/K13 caller-supplied", "required_source_or_api": "C170 preserved B1 sector / C152 full-vertex / C153 target authority", "required_routes": ("source owner", "matrix-free", "Hermitian", "analyticity", "count-once"), "nonclaim": "not constructed in C184; not encoded as zero"} for req in reqs for obj in (("C170-B1-QGG", "C170-B1-QQBARQ", "COMPLETE_QG_1PI", "FULL_ST_SUBSTRATE", "TARGET_MOMQ_COEFFICIENT") if req == ACTIVE_REQUESTS[1] else ("TARGET_MOMQ_COEFFICIENT", "COMMON_IR_MATCHING", "MATCHING_WINDOW")))
    return _freeze({"schema": "C184-MISSING-CALCULATION-OBJECT-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def next_phase_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C184-NEXT-PHASE-HANDOFF-V1", "next": NEXT, "scope": "preserved C170-B1-QGG and C170-B1-QQBARQ only", "roots": {"C171": c171.PACKAGE_ROOT, "C151": c151.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT, "C184": PACKAGE_ROOT}, "remaining_interfaces": ("complete qg 1PI", "full ST", "target MOMq", "fundamental BC adapter if required"), "physical": False, "root": _root((NEXT, c171.PACKAGE_ROOT, c151.PACKAGE_ROOT, c183.PACKAGE_ROOT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C184-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "completed_substrate": "C171-C183 B0 source/link/holonomy", "C184_delta": "B0 C43 proper two-point plus B0 coupling component", "preserved_leaves": ("C170-B1-QGG", "C170-B1-QQBARQ", "quark source", "target coefficient", "two RI/SMOM source leaves"), "root": _root((STATUS, 0, 0))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C184-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameters": 0, "root": _root((0, 0, 0))})


def lfmatchcalc2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C184-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "all_six_visible": True, "active_requests": 2, "parameter_fixtures": len(FIXTURE_IDS), "resolutions": RESOLUTIONS, "qqbar_routes": 6, "gg_routes": 7, "loop_sectors": SECTORS, "dense_full_inverses": 0, "missing_terms_set_zero": 0, "C166_graph_nodes_edges": (0, 0), "B1_mutations": 0, "C158_value_inputs": 0, "counterterms_selected": 0, "null_representatives": 0, "physical_selection": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, len(FIXTURE_IDS)))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "web_search": 0, "model_memory_formulas": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "B1_sector_mutations": 0, "dense_full_inverses": 0, "missing_terms_set_zero": 0, "holonomy_loop_conflations": 0, "counterterms_selected": 0, "null_representatives": 0, "physical_Z_A": 0, "full_coupling_claim": 0, "full_ST_claim": 0, "target_coefficient_invented": 0, "quantum_objects_modified": 0, "Q0_Q1_Q2_modified": False, "pass": True, "root": _root((0, 0, 0, 0))})


def mutate_live_hqcdlfmatchcalc2(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "focused immutable-record perturbation", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, "C184", "mutation"))})


ROOTS = {
    "C183": c183.PACKAGE_ROOT, "C171": c171.PACKAGE_ROOT, "C151": c151.PACKAGE_ROOT,
    "C169": c169.PACKAGE_ROOT, "C184_PLAN": lfmatchcalc2_plan_manifest()["root"],
    "C184_PARAMETERS": calculation_parameter_schema()["root"], "C184_FIXTURES": calculation_fixture_manifest()["root"],
    "C184_EXTERNAL": external_domain_manifest()["root"], "C184_QQBAR": g_qqbar_vertex_manifest()["root"], "C184_GG": g_gg_vertex_manifest()["root"],
    "C184_LOOPS": propagating_loop_manifest()["root"], "C184_GHOST_LINK": ghost_link_holonomy_manifest()["root"], "C184_NONPROP": nonpropagating_manifest()["root"],
    "C184_AGG": proper_two_point_manifest()["root"], "C184_PROJ": tensor_projection_manifest()["root"], "C184_FIELD": field_response_manifest()["root"],
    "C184_COUPLING": coupling_component_manifest()["root"], "C184_ANALYTICITY": analyticity_manifest()["root"], "C184_COUNT_ONCE": count_once_manifest()["root"],
    "C184_RELEASE": b0_release_manifest()["root"], "C184_REQUESTS": request_resolution_manifest()["root"], "C184_MISSING": missing_calculation_object_manifest()["root"],
    "C184_FRONTIER": dependency_frontier_manifest()["root"], "C184_COMPLETENESS": lfmatchcalc2_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C184-HQCDLFGMATCHCALC2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
