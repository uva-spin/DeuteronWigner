"""Frozen source authority for the C408 weight/routing closure.

C408 narrows two over-broad C407 blockers without selecting a physical
coefficient.  First, C116 and C126 agree that ``J_qJ_q:q->q`` uses the exact
``I4_local`` spatial route, while C125's product-only helper assigns I2 to all
``J_qJ_q`` programs.  C408 records that conflict and follows the more specific
program/sector authorities C116/C126.

Second, the C124/C126 witness descendant assigns the exact symbolic member
multiplier ``1`` to ``I2_density_projector`` members.  This closes the member
multiplier for the I2 routes only.  It does not bind the common C114/C119
normalization, target aggregation, ``g_s^2`` or ``c_C117_1``.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

STATUS = (
    "C408_C117_I2_C124_C126_MEMBER_WEIGHT_AND_JQJQ_I4_ROUTING_CLOSED_"
    "SOURCE_ROUTED_PRODUCT_BLOCK_PRIMITIVES_READY_FULL_C117_ACTION_UNAVAILABLE"
)
ROOT = Path(__file__).resolve().parents[4]

_SOURCE_PATHS = {
    "C45": "src/deuteron_wigner/bridge/modes/core.py",
    "C47": "src/deuteron_wigner/bridge/basis1/core.py",
    "C116": "src/deuteron_wigner/bridge/icho2/core.py",
    "C117": "src/deuteron_wigner/bridge/icreg2/core.py",
    "C119": "src/deuteron_wigner/bridge/icnorm3/core.py",
    "C124": "src/deuteron_wigner/bridge/icmembers/core.py",
    "C125": "src/deuteron_wigner/bridge/icdomain2/core.py",
    "C126": "src/deuteron_wigner/bridge/icsum3/core.py",
    "C249": "src/deuteron_wigner/bridge/hqcdriquarkfixedkv2currentproj1/core.py",
    "C403": "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/spatial.py",
    "C406": "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/mixed_kernel.py",
    "C407": "src/deuteron_wigner/bridge/c407_c117_i2_same_species_descendants/jqjq_qg.py",
}

_REQUIRED_SNIPPETS = {
    "C116": (
        'used=("I4_local",) if p=="J_qJ_q" and s=="q->q"',
        'return "AVAILABLE_SOURCE_QUALIFIED" if program["program"]=="J_qJ_q:q->q"',
    ),
    "C117": (
        "sum_{r in R_graph} w_r phi_r*(x) phi_r(x)",
        "(partial+ eigenvalue)_r w_r phi_r*(x) phi_r(x)",
    ),
    "C124": (
        'return f"pi*{mode[\'k\']}/L" if c["graph"] == "derivative_density" else "1"',
        '"factor_ownership": "member identities only; no numerical factors"',
    ),
    "C125": (
        'return "I2_density_projector" if product in ("J_qJ_q", "J_qJ_g") else "derivative_density"',
    ),
    "C126": (
        '"C116:I4_local" if sector == "q->q" and product == "J_qJ_q" else "C117:projector"',
        'return "1"',
    ),
    "C249": (
        "SUM_CALLER_R(w_r*phi_r^*(x;b_HO)*phi_r(x;b_HO))",
    ),
    "C407": (
        "explicit weights ``w_r``",
        "source_authorized_graph_member_weights",
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
            snippet for snippet in _REQUIRED_SNIPPETS.get(owner, ()) if snippet not in text
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
        "schema": "C408-SOURCE-HASH-AUDIT-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "all_pass": True,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def routing_authority_record() -> Mapping[str, Any]:
    payload = {
        "schema": "C408-JQJQ-Q-SECTOR-GRAPH-ROUTING-AUTHORITY-V1",
        "status": STATUS,
        "program": "J_qJ_q:q->q",
        "authorities": (
            {
                "owner": "C116",
                "route": "I4_local only",
                "specificity": "product_and_sector",
                "status": "SOURCE_QUALIFIED",
            },
            {
                "owner": "C126",
                "route": "C116:I4_local",
                "specificity": "product_and_sector",
                "status": "SOURCE_QUALIFIED",
            },
            {
                "owner": "C125",
                "route": "I2_density_projector",
                "specificity": "product_only_helper",
                "status": "CONFLICTING_OVERBROAD_HELPER",
            },
        ),
        "C408_route": "I4_local",
        "decision_rule": (
            "use the two agreeing product-and-sector authorities C116/C126; "
            "do not mutate historical C125"
        ),
        "historical_C125_modified": False,
        "C403_I2_substituted_into_q_sector": False,
        "routing_conflict_closed": True,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def i2_member_weight_authority() -> Mapping[str, Any]:
    payload = {
        "schema": "C408-C117-I2-C124-C126-MEMBER-WEIGHT-AUTHORITY-V1",
        "status": STATUS,
        "graph": "I2_density_projector",
        "programs": ("J_qJ_q:qg->qg", "J_qJ_g:qg->qg", "J_gJ_q:qg->qg"),
        "C117_abstract_expression": "sum_r w_r phi_r^* phi_r",
        "C124_descendant_member_multiplier": "1",
        "C126_value_program_member_multiplier": "1",
        "C249_generic_adapter": "caller-weighted generic interface retained",
        "C408_scope": (
            "exact C124/C126 source-descendant member multiplier after the C407 longitudinal, "
            "helicity and color contractions have been evaluated independently"
        ),
        "unit_multiplier_is_physical_coefficient": False,
        "common_current_normalization_bound": False,
        "target_count_once_aggregation_bound": False,
        "g_s_squared_bound": False,
        "c_C117_1_bound": False,
        "C407_broad_weight_blocker_superseded_for_listed_I2_programs": True,
        "derivative_density_weight_closed": False,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def derivative_density_conflict_record() -> Mapping[str, Any]:
    payload = {
        "schema": "C408-DERIVATIVE-DENSITY-COUNT-CONFLICT-V1",
        "status": STATUS,
        "product": "J_gJ_g:qg->qg",
        "facts": (
            "C119 gluon_current already contains pi*k_c/L",
            "C119 also lists a derivative_or_helicity pi*k_c/L leaf",
            "C124 derivative_density assigns pi*k/L as the member multiplier",
            "C406/C407 source-derived gluon descendants already contain both current momenta",
        ),
        "risk": "multiplying all historical derivative leaves would over-count ordered derivatives",
        "numerical_derivative_density_action": None,
        "smallest_missing_object": (
            "one source-qualified product-level derivative-count and normalization descendant "
            "reconciling C119, C124/C126 and C406/C407"
        ),
        "unavailable_not_zero": True,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def scientific_boundary_record() -> Mapping[str, Any]:
    payload = {
        "schema": "C408-SCIENTIFIC-BOUNDARY-V1",
        "status": STATUS,
        "closed": (
            "J_qJ_q:q->q graph routing through C116/C126 I4_local",
            "C124/C126 exact unit I2 member multiplier for three qg I2 programs",
            "source-routed J_qJ_q q-sector I4 transverse-mode sum",
            "source-routed J_qJ_q qg-sector unit-member sum",
            "source-routed mixed-current qg unit-member sums",
            "sparse and independent matrix-free direct-sum product-block primitives",
        ),
        "open": (
            "J_gJ_g derivative-density derivative-count reconciliation",
            "J_gJ_g q-sector number-changing branches",
            "route-reconciled finite-cell/field/state/M2 normalization",
            "complete C125 target aggregation and count-once multiplicity",
            "g_s^2 and c_C117_1 values",
        ),
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
    "routing_authority_record",
    "i2_member_weight_authority",
    "derivative_density_conflict_record",
    "scientific_boundary_record",
]
