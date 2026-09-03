"""Frozen source authority for the C407 same-species contraction layer."""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

STATUS = (
    "C407_C117_I2_SAME_SPECIES_LONGITUDINAL_DESCENDANTS_AND_CALLER_CONDITIONED_"
    "JQJQ_QG_COMPOSITION_READY_GRAPH_WEIGHTS_AND_JGJG_TRANSVERSE_DESCENDANT_UNRESOLVED"
)
ROOT = Path(__file__).resolve().parents[4]

_SOURCE_PATHS = {
    "C45": "src/deuteron_wigner/bridge/modes/core.py",
    "C47": "src/deuteron_wigner/bridge/basis1/core.py",
    "C114": "src/deuteron_wigner/bridge/icurrent/core.py",
    "C115": "src/deuteron_wigner/bridge/icho/core.py",
    "C117": "src/deuteron_wigner/bridge/icreg2/core.py",
    "C119": "src/deuteron_wigner/bridge/icnorm3/core.py",
    "C125": "src/deuteron_wigner/bridge/icdomain2/core.py",
    "C403": "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/spatial.py",
    "C404_LONG": "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/longitudinal.py",
    "C404_COLOR": "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/color_spin.py",
    "C406_NORMAL": "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/normal_order.py",
    "C406_ROUTING": "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/routing.py",
}

_REQUIRED_SNIPPETS = {
    "C114": (
        "P^-_IC = -(g_s^2/2)",
        "Q0 excludes exactly zero transferred plus momentum",
    ),
    "C115": (
        "delta_{lambda',lambda}",
        "T^a_{c'c}",
        "acts on ordered c field",
    ),
    "C117": (
        "sum_{r in R_graph} w_r phi_r*(x) phi_r(x)",
        "(partial+ eigenvalue)_r w_r phi_r*(x) phi_r(x)",
    ),
    "C119": (
        "delta_helicity * T^a_(cprime,c) * (2L)^(-1)",
        "-f^(abc) * delta_polarization * (pi*k_c/L) * (2L)^(-1)",
    ),
    "C125": (
        'return "I2_density_projector" if product in ("J_qJ_q", "J_qJ_g") else "derivative_density"',
    ),
    "C406_NORMAL": (
        "return -(bra + ket)",
        "return -(bra + ket) / (2.0 * sqrt(bra * ket))",
    ),
}


@lru_cache(maxsize=1)
def source_hash_audit() -> Mapping[str, Any]:
    rows = []
    for owner, relative in _SOURCE_PATHS.items():
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        text = path.read_text(encoding="utf-8")
        missing = tuple(snippet for snippet in _REQUIRED_SNIPPETS.get(owner, ()) if snippet not in text)
        if missing:
            raise ValueError(f"{owner} source authority changed: {missing}")
        rows.append(
            {
                "owner": owner,
                "path": relative,
                "sha256": sha256(path.read_bytes()).hexdigest(),
                "required_snippets_verified": len(_REQUIRED_SNIPPETS.get(owner, ())),
                "pass": True,
            }
        )
    payload = {
        "schema": "C407-SOURCE-HASH-AUDIT-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "all_pass": True,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def scientific_boundary_record() -> Mapping[str, Any]:
    payload = {
        "schema": "C407-SCIENTIFIC-BOUNDARY-V1",
        "status": STATUS,
        "closed": (
            "finite same-species longitudinal intermediate axes at K9/K11/K13",
            "Q0 nonzero-transfer exclusion",
            "quark one-body current-current longitudinal weight up to common normalization",
            "gluon one-body current-current longitudinal weight using the C406 descendant",
            "fundamental and adjoint Casimir contractions",
            "caller-conditioned J_qJ_q qg-sector I2 numerical composition interface",
        ),
        "open": (
            "source-authorized C117 I2 graph-member weights for J_qJ_q",
            "J_qJ_q q-sector I4-local transverse kernel",
            "J_gJ_g derivative-density transverse descendant and derivative-count reconciliation",
            "J_gJ_g q-sector pair/vacuum branches",
            "route-reconciled finite-cell, field, state, and M2 normalization",
            "target count-once aggregation",
            "g_s^2 and c_C117_1 values",
        ),
        "complete_C117_action": False,
        "complete_C396_numerical_apply_paths": 6,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = ["STATUS", "source_hash_audit", "scientific_boundary_record"]
