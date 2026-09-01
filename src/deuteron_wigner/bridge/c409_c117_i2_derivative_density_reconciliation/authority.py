"""Frozen source authority for C409 derivative-density reconciliation.

C409 resolves one precise bookkeeping conflict for the number-preserving
``J_gJ_g:qg->qg`` descendant.  The authenticated C114/C192 source contains
one longitudinal derivative in each gluon current.  C406 evaluates the full
one-gluon current matrix element, and C407 forms the product of those two
current matrix elements together with the C114 inverse-square transfer kernel.
Consequently the additional C119 derivative leaf and the C124/C126
``derivative_density`` ``pi*k/L`` member expression are not independent
multipliers on this reduced route.

This module records that source reconciliation without modifying historical
owners or promoting the resulting product-block primitive to a complete C117
coordinate action.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

STATUS = (
    "C409_C117_I2_JGJG_DERIVATIVE_COUNT_RECONCILED_"
    "NUMBER_PRESERVING_QG_PRODUCT_BLOCK_PRIMITIVE_READY_"
    "FULL_C117_ACTION_UNAVAILABLE"
)
ROOT = Path(__file__).resolve().parents[4]

_SOURCE_PATHS = {
    "C45": "src/deuteron_wigner/bridge/modes/core.py",
    "C47": "src/deuteron_wigner/bridge/basis1/core.py",
    "C114": "src/deuteron_wigner/bridge/icurrent/core.py",
    "C115": "src/deuteron_wigner/bridge/icho/core.py",
    "C117": "src/deuteron_wigner/bridge/icreg2/core.py",
    "C119": "src/deuteron_wigner/bridge/icnorm3/core.py",
    "C124": "src/deuteron_wigner/bridge/icmembers/core.py",
    "C126": "src/deuteron_wigner/bridge/icsum3/core.py",
    "C192": "src/deuteron_wigner/bridge/hqcdb1qgggcurr1/core.py",
    "C403": "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/spatial.py",
    "C404": "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/color_spin.py",
    "C406": "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/normal_order.py",
    "C407": "src/deuteron_wigner/bridge/c407_c117_i2_same_species_descendants/descendants.py",
    "C408": "src/deuteron_wigner/bridge/c408_c117_i2_weight_routing_closure/authority.py",
}

_REQUIRED_SNIPPETS = {
    "C114": (
        "J_g,a^+(x)=-f^{abc} A_perp^b(x) partial^+ A_perp^c(x)",
        '"denominator":"L^2/(pi^2*n^2)"',
    ),
    "C119": (
        'factor_id=="gluon_current"',
        'factor_id=="derivative_or_helicity"',
        "pi*k_c/L",
    ),
    "C124": (
        "derivative_density",
        'return f"pi*{mode[\'k\']}/L"',
        '"factor_ownership": "member identities only; no numerical factors"',
    ),
    "C126": (
        "derivative_density",
        "C115:derivative_or_helicity",
    ),
    "C192": (
        '"current_expression":"- f_abc A_perp^b partial_- A_perp^c"',
        '"derivative_placement":"partial_- acts on second slot"',
        '"source minus retained"',
    ),
    "C406": (
        "c151_canonical_one_gluon_factor",
        "return -(bra + ket)",
        "vacuum_commutator_zero",
    ),
    "C407": (
        "gluon_current_pair_factor_exact",
        "same_species_weight_exact",
        "CASIMIR[species] * current / (transfer * transfer)",
    ),
    "C408": (
        "multiplying all historical derivative leaves would over-count ordered derivatives",
        "numerical_derivative_density_action\": None",
    ),
}


def _file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


@lru_cache(maxsize=1)
def source_hash_audit() -> Mapping[str, Any]:
    rows = []
    for owner, relative in _SOURCE_PATHS.items():
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        text = path.read_text(encoding="utf-8")
        missing = tuple(
            snippet
            for snippet in _REQUIRED_SNIPPETS.get(owner, ())
            if snippet not in text
        )
        if missing:
            raise ValueError("{} source authority changed: {}".format(owner, missing))
        rows.append(
            {
                "owner": owner,
                "path": relative,
                "sha256": _file_hash(path),
                "required_snippets_verified": len(_REQUIRED_SNIPPETS.get(owner, ())),
                "pass": True,
            }
        )
    payload = {
        "schema": "C409-SOURCE-HASH-AUDIT-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "all_pass": True,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def derivative_count_authority() -> Mapping[str, Any]:
    products = (
        {
            "product": "J_qJ_q",
            "source_gluon_current_count": 0,
            "source_longitudinal_derivative_count": 0,
            "C409_route": "C408_SOURCE_ROUTED_EXISTING_PRIMITIVE",
        },
        {
            "product": "J_qJ_g",
            "source_gluon_current_count": 1,
            "source_longitudinal_derivative_count": 1,
            "C409_route": "C406_FULL_ONE_GLUON_CURRENT_DESCENDANT",
        },
        {
            "product": "J_gJ_q",
            "source_gluon_current_count": 1,
            "source_longitudinal_derivative_count": 1,
            "C409_route": "C406_FULL_ONE_GLUON_CURRENT_DESCENDANT",
        },
        {
            "product": "J_gJ_g",
            "source_gluon_current_count": 2,
            "source_longitudinal_derivative_count": 2,
            "C409_route": "C407_PRODUCT_OF_TWO_C406_CURRENT_DESCENDANTS",
        },
    )
    payload = {
        "schema": "C409-C117-I2-DERIVATIVE-COUNT-AUTHORITY-V1",
        "status": STATUS,
        "source_operator": (
            "P^-_IC=-(g_s^2/2) integral [Q0(i partial+)^-1 j_a^+] "
            "[Q0(i partial+)^-1 j_a^+]"
        ),
        "source_gluon_current": "J_g^+=-f A_perp partial^+ A_perp",
        "products": products,
        "J_gJ_g_exact_source_derivative_count": 2,
        "C406_descendant_derivatives_per_gluon_current": 1,
        "C407_current_pair_derivatives": 2,
        "C119_extra_derivative_leaf_independent_on_C406_C407_route": False,
        "C124_C126_derivative_density_pi_k_over_L_independent_on_C406_C407_route": False,
        "historical_owners_modified": False,
        "reconciliation_rule": (
            "On the reduced number-preserving J_gJ_g route, use the product of the two "
            "full C406 one-gluon current descendants exactly once; do not multiply a "
            "second derivative leaf or derivative-density pi*k/L member factor."
        ),
        "generic_C124_derivative_density_replaced_globally": False,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def scale_power_reconciliation() -> Mapping[str, Any]:
    rows = (
        {
            "factor": "C114 inverse-square kernel",
            "pi_power": -2,
            "L_power": 2,
            "derivative_count": 0,
        },
        {
            "factor": "first C192/C406 gluon current",
            "pi_power": 1,
            "L_power": -1,
            "derivative_count": 1,
        },
        {
            "factor": "second C192/C406 gluon current",
            "pi_power": 1,
            "L_power": -1,
            "derivative_count": 1,
        },
    )
    net_pi = sum(int(row["pi_power"]) for row in rows)
    net_l = sum(int(row["L_power"]) for row in rows)
    payload = {
        "schema": "C409-C117-I2-JGJG-SCALE-POWER-RECONCILIATION-V1",
        "status": STATUS,
        "rows": rows,
        "source_derivative_count": sum(int(row["derivative_count"]) for row in rows),
        "net_pi_power": net_pi,
        "net_L_power": net_l,
        "dimensionless_longitudinal_subset": net_pi == 0 and net_l == 0,
        "adding_C119_derivative_leaf_would_give": {"pi_power": 1, "L_power": -1},
        "adding_C124_derivative_density_factor_would_give": {"pi_power": 1, "L_power": -1},
        "adding_both_extra_factors_would_give": {"pi_power": 2, "L_power": -2},
        "extra_factors_admitted": False,
        "complete_product_normalization": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def reduced_transverse_authority() -> Mapping[str, Any]:
    payload = {
        "schema": "C409-C117-I2-REDUCED-DERIVATIVE-DENSITY-TRANSVERSE-AUTHORITY-V1",
        "status": STATUS,
        "product": "J_gJ_g:qg->qg",
        "derivative_action": (
            "The C192 partial-plus derivatives act on longitudinal plane-wave phases; "
            "their complete number-preserving one-gluon matrix elements are already "
            "contained in the C406/C407 longitudinal descendant."
        ),
        "reduced_spatial_kernel": (
            "sum over the admitted C403 transverse density members with the exact "
            "route-specific residual multiplier one"
        ),
        "member_multiplier": 1,
        "member_multiplier_scope": (
            "C409 reduced number-preserving J_gJ_g route only, after the two source "
            "derivatives and C_A have been evaluated in the C407 longitudinal factor"
        ),
        "C124_generic_derivative_density_semantics_mutated": False,
        "C408_unit_I2_member_sum_reused": True,
        "transverse_derivative_applied_again": False,
        "color_C_A_applied_again": False,
        "physical_coefficient_selected": False,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def scientific_boundary_record() -> Mapping[str, Any]:
    payload = {
        "schema": "C409-SCIENTIFIC-BOUNDARY-V1",
        "status": STATUS,
        "closed": (
            "exactly two source longitudinal derivatives in J_gJ_g",
            "C119/C124/C126 extra derivative factors excluded on the C406/C407 reduced route",
            "exact inverse-square/derivative L and pi power cancellation",
            "reduced number-preserving qg derivative-density transverse member sum",
            "source-routed sparse and matrix-free J_gJ_g:qg->qg product-block primitive",
            "single-counted C_A color Casimir",
        ),
        "open": (
            "J_gJ_g q-sector number-changing pair and vacuum branches",
            "route-reconciled finite-cell, field, external-state and M2 normalization",
            "complete target count-once aggregation across product blocks",
            "g_s^2 and c_C117_1 values",
        ),
        "source_routed_product_block_primitive_paths": 12,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return dict(payload, root=content_root(payload))


__all__ = [
    "STATUS",
    "source_hash_audit",
    "derivative_count_authority",
    "scale_power_reconciliation",
    "reduced_transverse_authority",
    "scientific_boundary_record",
]
