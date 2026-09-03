"""Source authority for C410 retained-current aggregation and vacuum routing.

C410 closes two mechanical boundaries left by C409:

* the ``J_g K J_g`` pair/vacuum contribution in the external one-quark
  sector is routed to the already-declared vacuum direction rather than being
  silently set to zero or inserted as a sector-dependent identity shift; and
* the four source-ordered current products are assembled exactly once into a
  K-local retained connected current-square shape.

The resulting shape is not promoted to the RI/SMOM-normalized C117 coordinate
operator.  C260 still records the finite-C43 adapter and operator normalization
as unavailable, not zero.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

STATUS = (
    "C410_C117_I2_Q_SECTOR_VACUUM_ROUTING_AND_RETAINED_CONNECTED_"
    "CURRENT_SQUARE_AGGREGATION_READY_C260_OPERATOR_NORMALIZATION_UNAVAILABLE"
)
ROOT = Path(__file__).resolve().parents[4]

_SOURCE_PATHS = {
    "C114": "src/deuteron_wigner/bridge/icurrent/core.py",
    "C117": "src/deuteron_wigner/bridge/icreg2/core.py",
    "C119": "src/deuteron_wigner/bridge/icnorm3/core.py",
    "C129": "src/deuteron_wigner/bridge/gnorm/core.py",
    "C131": "src/deuteron_wigner/bridge/hqcd4/core.py",
    "C136": "src/deuteron_wigner/bridge/hqcdid3/core.py",
    "C192": "src/deuteron_wigner/bridge/hqcdb1qgggcurr1/core.py",
    "C259": "src/deuteron_wigner/bridge/hqcdc117renormdesign1/core.py",
    "C260": "src/deuteron_wigner/bridge/hqcdc117rismom1/core.py",
    "C274": "src/deuteron_wigner/bridge/hqcdc117renormh1/core.py",
    "C408": "src/deuteron_wigner/bridge/c408_c117_i2_weight_routing_closure/jqjq.py",
    "C409": "src/deuteron_wigner/bridge/c409_c117_i2_derivative_density_reconciliation/jgjg.py",
}

_REQUIRED_SNIPPETS = {
    "C114": (
        "vacuum\":\"retained as control, not silently dropped",
        "P^-_IC = -(g_s^2/2)",
        "j_a^+ = J_q,a^+ + J_g,a^+",
    ),
    "C117": (
        '"expression":"sum_{r in R_graph} w_r phi_r*(x) phi_r(x)"',
        '"gs2":"factored"',
        "component assembly is deferred",
    ),
    "C119": (
        'factor_id=="state_normalization"',
        'factor_id=="field_mode_normalization"',
        '"g_s_squared":"factored"',
    ),
    "C129": (
        '"G4_DOUBLE_CONTRACTION_VACUUM"',
        '"destination":"vacuum c-number"',
        '"bare_matrix_included":False',
    ),
    "C131": (
        '"status":"NONMATRIX_EXCLUDED_FROM_FIXED_PARTICLE_P_R_H_P_R"',
        '"identity_shift_required":False',
    ),
    "C136": (
        '"equation":"P_R vacuum direction P_R = 0"',
        '"role":"VACUUM_DIRECTION_EXCLUDED"',
    ),
    "C192": (
        '"terminal":"GLUON_PAIR_CREATION"',
        '"terminal":"GLUON_PAIR_ANNIHILATION"',
        '"pattern":"normal ordering descendants"',
    ),
    "C259": (
        '"mass_dimension":"Hamiltonian mass-squared direction; coefficient convention deferred to C260"',
        '"coupling_order":"g_s^2 factored"',
    ),
    "C260": (
        '"matrix":"M^(K)(mu,S) UNAVAILABLE_NOT_ZERO_C262"',
        '"normalization":"C117 operator/source normalization and g_s^2 ownership retained"',
    ),
    "C274": (
        '"formula":"H_R(theta,c)=sum_owner H_owner,R(theta)+sum_i=1^4 c_i O_C117,i,R"',
        '"derivative":f"dH/dc_{i+1}=O_C117_{i+1},R"',
    ),
    "C408": (
        "source_routed_jqjq_direct_sum_csr",
        "source_routed_J_qJ_q_product_block_paths",
    ),
    "C409": (
        "jgjg_qg_csr",
        "pair/vacuum branches and the common C117 normalization remain unavailable, not zero",
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
        "schema": "C410-SOURCE-HASH-AUDIT-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "all_pass": True,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def vacuum_routing_authority() -> Mapping[str, Any]:
    payload = {
        "schema": "C410-C117-I2-Q-SECTOR-JGJG-VACUUM-ROUTING-AUTHORITY-V1",
        "status": STATUS,
        "source_product": "J_g K J_g:q->q",
        "external_gluon_number": 0,
        "number_preserving_branch": "NOT_APPLICABLE_NO_EXTERNAL_GLUON",
        "pair_creation_branch": "SOURCE_PRESENT_C192",
        "pair_annihilation_branch": "SOURCE_PRESENT_C192_HERMITIAN_PARTNER",
        "source_ordered_vacuum_product": (
            "I_q tensor <0_g|J_g(-q) K(q) J_g(q)|0_g>; disconnected from the "
            "external quark because both currents contain gluon fields only"
        ),
        "full_source_vacuum_cnumber_claimed_zero": False,
        "full_source_pair_branch_discarded": False,
        "project_owner": "C129/C131/C136 vacuum direction",
        "project_rule": "P_R vacuum direction P_R = 0",
        "retained_connected_status": (
            "EXACT_ZERO_AFTER_EXPLICIT_VACUUM_DIRECTION_ROUTING_AND_CONNECTED_PROJECTION"
        ),
        "identity_shift_inserted": False,
        "C131_identity_shift_required": False,
        "C117_coordinate_absorbs_vacuum_direction": False,
        "unavailable_as_zero": False,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def aggregation_authority() -> Mapping[str, Any]:
    products = (
        {
            "ordinal": 0,
            "product": "J_qJ_q",
            "owner": "C408 source-routed direct-sum primitive",
            "multiplicity": 1,
        },
        {
            "ordinal": 1,
            "product": "J_qJ_g",
            "owner": "C408/C406 mixed-current source order",
            "multiplicity": 1,
        },
        {
            "ordinal": 2,
            "product": "J_gJ_q",
            "owner": "C408/C406 Hermitian source-order partner",
            "multiplicity": 1,
        },
        {
            "ordinal": 3,
            "product": "J_gJ_g",
            "owner": "C409 qg primitive plus C410 q-sector vacuum projection",
            "multiplicity": 1,
        },
    )
    payload = {
        "schema": "C410-C117-I2-RETAINED-CONNECTED-AGGREGATION-AUTHORITY-V1",
        "status": STATUS,
        "source_identity": (
            "(J_q+J_g) K (J_q+J_g) = J_qKJ_q + J_qKJ_g + "
            "J_gKJ_q + J_gKJ_g"
        ),
        "products": products,
        "product_count": len(products),
        "mixed_orders_kept_separate": True,
        "factor_two_substitution_used": False,
        "Hermitian_reverse_averaged_posthoc": False,
        "source_common_coefficient": "-1/2",
        "source_common_coefficient_applied_once": True,
        "g_s_squared_factored": True,
        "c_C117_1_applied": False,
        "vacuum_direction_counted_in_retained_matrix": False,
        "source_product_count_once_structure_closed": True,
        "complete_target_aggregation_closed": False,
        "absolute_C260_operator_normalization_closed": False,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def scientific_boundary_record() -> Mapping[str, Any]:
    payload = {
        "schema": "C410-SCIENTIFIC-BOUNDARY-V1",
        "status": STATUS,
        "closed": (
            "J_gJ_g q-sector pair/vacuum branch routed to the nonmatrix vacuum owner",
            "exact retained connected q-sector zero after explicit vacuum subtraction",
            "all four source-ordered current products aggregated once",
            "mixed orders retained as a Hermitian-adjoint pair",
            "source -1/2 coefficient applied once with g_s^2 factored",
            "three K-local retained connected aggregate shape primitives",
            "c_C117_1 and physical g_s values not required to define a derivative shape",
        ),
        "open": (
            "C260/C262 finite-C43 operator-normalization and wavepacket adapter",
            "route-reconciled field/state/M2 normalization in the C117 scheme",
            "promotion of the retained shape to O_C117_1,R",
            "the physical value of c_C117_1",
            "physical rank, fit, and activation",
        ),
        "source_routed_product_block_primitive_paths": 12,
        "retained_connected_aggregate_shape_paths": 3,
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
    "vacuum_routing_authority",
    "aggregation_authority",
    "scientific_boundary_record",
]
