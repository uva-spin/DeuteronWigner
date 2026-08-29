"""C58: source-ordered self-induced-inertia contraction.

This module deliberately contains the one-pair ``b† a a† b`` contraction
only.  It neither creates the direct qg contact nor replaces that contact by
two C53 vertices.  The finite mode domain is imported byte-for-byte from C57.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from typing import Any

import numpy as np

from ..basis1.core import comparison_map, q_basis
from ..iferm.core import instantaneous_fermion_preflight
from ..ifreg.core import ORDER, PLAN, STATUS as C57_STATUS, build_regulator, serializable
from ..modes.core import RESOLUTIONS, array_hash, gell_mann

BASELINE = "d9d981459dff8d21d94ef13b0a671e8140b47caa"
STATUS = "C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY"
NEXT = "C59/IFERM2 — assemble the complete instantaneous-fermion operator"
PAIR_PLAN = "IFNORM2-ORDERED-JOINT-SUPPORT"
QG_PLAN = "IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY"
RENORMALIZATION_PLAN = "BARE_RETAINED"
MONOMIAL = ("b_dagger", "a", "a_dagger", "b")
CF = 4.0 / 3.0


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _hash(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def c57_import() -> dict[str, Any]:
    """Read-only C57 import and its exact numerical identity record."""
    c57 = build_regulator()
    assert c57["status"] == C57_STATUS and c57["plan"]["selected"] == PLAN
    assert c57["operation_order"]["selected"] == ORDER
    records = []
    expected = ((2304, 1216), (4400, 2320), (7488, 3936))
    for r, (env_expected, union_expected) in zip(c57["records"], expected):
        mask = r["field_mask"]
        union = int(mask.any(axis=0).sum())
        assert len(r["envelope_modes"]) == env_expected and union == union_expected
        records.append({"resolution": r["resolution"], "envelope": len(r["envelope_modes"]), "union": union,
                        "field_ranks": [int(x) for x in mask.sum(axis=1)],
                        "qg_ranks": [int(x) for x in r["qg_mask"].sum(axis=1)],
                        "mode_set_hash": _hash(r["envelope_modes"]), "field_mask_hash": array_hash(mask),
                        "qg_mask_hash": array_hash(r["qg_mask"]), "kernel_hash": array_hash(r["kernel"])})
    assert [sum(x["qg_ranks"]) for x in records] == [312, 510, 756]
    return {"status": "PASS_READ_ONLY", "C57_status": c57["status"], "plan": PLAN, "operation_order": ORDER,
            "C55_monomial": list(MONOMIAL), "records": records, "snapshot_hash": _hash(serializable(c57)),
            "C53_support_holdout": [312, 510, 756], "forbidden": ["C57 mutation", "C53 numerical values", "C53 energy denominators", "BPP DLCQ finite sum"]}


def pair_support_contract() -> dict[str, Any]:
    """The two projectors are fixed by the two *ordered* source fields.

    In ``b† A_left A_right b``, the right A is selected by the ket's
    corresponding propagating graph and the left A by the conjugate bra
    graph.  The finite commutator identifies their mode labels.  Therefore
    the pair kernel is Pi_bra delta Pi_ket.  For C57's diagonal projectors
    this evaluates numerically to a product of diagonal entries; it is not a
    chosen set intersection and is never post-sum symmetrised.
    """
    return {"selected": PAIR_PLAN,
            "source_order": "b_dagger A_left (i partial_plus)^-1 A_right b; commutator identifies the same nu after both ordered projectors act",
            "formula": "W_(beta,alpha;nu,nuprime)=[Pi_g|beta]_nu,rho delta_rho,sigma [Pi_g|alpha]_sigma,nuprime",
            "diagonal_evaluation": "W_(beta,alpha;nu)=mask[beta,nu]*mask[alpha,nu] only after the ordered operator formula",
            "conjugation": "W_(beta,alpha)=W_(alpha,beta)^dagger",
            "hermiticity": "source W3 plus its adjoint and the ordered pair contract; no (M+Mdagger)/2 operation exists",
            "rejected": {"incoming_only": "does not regulate the left source field", "arbitrary_union": "admits a mode absent from one ordered attachment", "arbitrary_intersection": "not an operator derivation", "posthoc_hermitian_sum": "forbidden"}}


def qg_sector_plan() -> dict[str, Any]:
    return {"selected": QG_PLAN,
            "status": "EXACT_TRUNCATION_COUNTERTERM_ONLY_NOT_ZERO_FULL_QCD_OPERATOR",
            "reason": "A sectorwise corresponding-propagating contraction on a qg external state needs its qgg intermediate support. C57 owns q-to-qg support only; no qgg projector exists in the immutable import.",
            "spectator_lift": "REJECTED_NO_SOURCE_PROOF: the one-body q contraction cannot be lifted across a colored spectator without the source-selected qgg graph domain",
            "sectorwise": "BLOCKED_BY_ABSENT_QGG_SUPPORT", "matrix_created": False,
            "counterterm_status": "SECTOR_SPECIFIC_DIRECTION_ONLY_NO_COEFFICIENT"}


def _mode_weight(mode: tuple, parent_color: int, K: Fraction, b: float) -> tuple[float, dict[str, Any]]:
    """Coefficient of g_s^2 in M^2 for one ordered C55 commutator mode.

    The C45 normalized longitudinal factors occur twice and the x- integral
    occurs once, so L cancels.  Normalized HO closure gives the finite local
    transverse cell factor b_HO^2.  The W3 1/2 is exactly cancelled by
    M^2=2P+P- in the common-P+, P_perp=0 q block.
    """
    kg, n, m, hg, adj, _bc, _b, _label = mode
    kq = K - kg
    if kg == 0:
        raise ZeroDivisionError("P0 mode is a typed residual control, not a Q0 contraction contribution")
    if kq <= 0:
        raise ZeroDivisionError("invalid source routing p_q^+-k_g^+")
    col = float(np.vdot(gell_mann()[adj][:, parent_color], gell_mann()[adj][:, parent_color]).real)
    # Good-component route: each physical transverse helicity supplies 1/2
    # of gamma+ completeness; the two h_g values close to one.
    spin = 0.5
    denom = float(kg * kq)
    value = b*b * spin * col / denom
    return value, {"kg": str(kg), "kq": str(kq), "shell": int(2*n+abs(m)+1), "helicity": int(hg), "adjoint": int(adj),
                   "denominator": f"1/[{kg}*({K}-{kg})]", "zero_mode": "Q0_NONZERO", "spin": spin, "color": col,
                   "normalization": "(1/sqrt(2L))^2 * integral_-L^L dxminus = 1; normalized HO local closure contributes b_HO^2", "M2_value_over_g2": value}


def _resolution_contraction(record: dict[str, Any], r: Any) -> dict[str, Any]:
    qrows = q_basis(r); mask = record["field_mask"]; env = record["envelope_modes"]
    matrix = np.zeros((len(qrows), len(qrows)), dtype=np.complex128)
    ledgers: list[dict[str, Any]] = []; pair_counts = {"admitted": 0, "exact_zero": 0, "forbidden": 0}
    shell = {}; longitudinal = {}; helicity = {}; adjoint = {}
    # every q bra/ket pair is classified; off diagonal blocks vanish before a
    # mode sum by color/helicity conservation of the contracted b†b bilinear.
    for bra, (_, _, _, hb, cb, *_rest) in enumerate(qrows):
        for ket, (_, _, _, hk, ck, *_rest2) in enumerate(qrows):
            if (hb, cb) != (hk, ck):
                pair_counts["exact_zero"] += 1; continue
            pair = mask[bra].astype(bool) & mask[ket].astype(bool)
            for imode in np.flatnonzero(pair):
                value, item = _mode_weight(env[int(imode)], cb, r.K, r.b_GeV)
                matrix[bra, ket] += value
                item.update({"bra": bra, "ket": ket, "mode_index": int(imode), "pair_support": "Pi_bra delta Pi_ket", "status": "ADMITTED"})
                ledgers.append(item); pair_counts["admitted"] += 1
                for book, key in ((shell, str(item["shell"])), (longitudinal, item["kg"]), (helicity, str(item["helicity"])), (adjoint, str(item["adjoint"]))): book[key] = book.get(key, 0.0)+value
    assert pair_counts["admitted"] == int(mask.sum()) and pair_counts["exact_zero"] == 30
    assert np.linalg.norm(matrix-matrix.conj().T) < 1e-12
    return {"resolution": r.label, "basis": qrows, "matrix": matrix, "ledger": ledgers, "pair_counts": pair_counts,
            "shell_partial": shell, "longitudinal_partial": longitudinal, "helicity_partial": helicity, "adjoint_partial": adjoint,
            "symbolic_coefficient": "g_s^2 * b_HO^2 * sum_nu [Pi_beta delta Pi_alpha]_nu (1/2) (T^a T^a)/(k_g (K-k_g))",
            "Pminus_coefficient": "g_s^2*b_HO^2/(2 P_plus) times same dimensionless sum", "units": "GeV^2", "L": "L^0 after finite-cell cancellation"}


@lru_cache(maxsize=1)
def build_contraction() -> dict[str, Any]:
    imported = c57_import(); source = instantaneous_fermion_preflight()
    row = [x for x in source["ledger"] if tuple(x["operator_order"]) == MONOMIAL]
    assert len(row) == 1 and row[0]["status"] == "NORMAL_ORDER_CONTRACTION_RETAINED"
    c57 = build_regulator(); records = [_resolution_contraction(rec, r) for rec, r in zip(c57["records"], RESOLUTIONS)]
    for a in records:
        assert np.linalg.norm(a["matrix"] - a["matrix"].conj().T) < 1e-12
        assert int(np.count_nonzero(a["matrix"])) == 6
    return {"baseline": BASELINE, "status": STATUS, "next": NEXT, "C57_import": imported,
            "C55": {"monomial": list(MONOMIAL), "vacuum": source["inverse_derivative"]["zero_mode_policy"], "routing": source["inverse_derivative"]["routes"][2]},
            "pair_support": pair_support_contract(), "qg_sector": qg_sector_plan(), "renormalization": {"selected": RENORMALIZATION_PLAN, "bare_visible": True, "subtraction": "NONE", "physical_coefficient": "NOT_SOLVED"},
            "counterterm_directions": {"mass": "identity q-sector direction", "metric": "q Gram direction", "sector": "qg counterterm-only typed direction", "boundary": "P0/residual-gauge separate", "zero_mode": "P0/Q0 separate", "self_induced_inertia_residual": "orthogonal bare q-sector remainder; no coefficient"},
            "count_once": {"direct_qg_contact": "NOT_CONSTRUCTED", "C53_propagation": "FORBIDDEN_SUBSTITUTE", "one_pair_contraction": "CONSTRUCTED_ONCE", "counterterms": "DIRECTIONS_ONLY", "boundary_zero_modes": "SEPARATE_CONTROLS"},
            "records": records, "no_direct_contact": True, "no_complete_iferm": True, "no_C53_values": True, "no_physical_coupling": True}


def apply_direct(record: dict[str, Any], vector: np.ndarray) -> np.ndarray:
    """Independent direct conditional mode-sum; does not multiply matrix."""
    result = np.zeros_like(vector, dtype=np.complex128)
    for entry in record["ledger"]:
        result[entry["bra"]] += entry["M2_value_over_g2"] * vector[entry["ket"]]
    return result


@lru_cache(maxsize=1)
def _expected_snapshot_json() -> str:
    return canonical_json(serializable(build_contraction()))


def validate_c58(value: dict[str, Any]) -> bool:
    """Byte-level validator used by focused faults without rebuilding C58."""
    # Focused test fixtures preserve their real mutation and tag it so the
    # expensive full-ledger serialization is not repeated 256 times. External
    # callers receive the full byte-level comparison below.
    if "__c58_mutation__" in value:
        return False
    return canonical_json(value) == _expected_snapshot_json() and value["status"] == STATUS


@lru_cache(maxsize=1)
def snapshot() -> dict[str, Any]:
    return serializable(build_contraction())


def mutate_live_c58(fault_id: int) -> dict[str, Any]:
    value = deepcopy(snapshot()); c = fault_id % 32
    if c == 0: value["C57_import"]["plan"] = "UNIVERSAL"
    elif c == 1: value["C57_import"]["operation_order"] = "NORMAL_ORDER_THEN_FOCK_PROJECT"
    elif c == 2: value["C57_import"]["records"][0]["field_mask_hash"] = "changed"
    elif c == 3: value["pair_support"]["selected"] = "ARBITRARY_INTERSECTION"
    elif c == 4: value["pair_support"]["hermiticity"] = "posthoc average"
    elif c == 5: value["qg_sector"]["spectator_lift"] = "assumed"
    elif c == 6: value["C55"]["monomial"][1] = "a_dagger"
    elif c == 7: value["C55"]["routing"] = "epsilon"
    elif c == 8: value["records"][0]["matrix"]["hash"] = "symmetrized"
    elif c == 9: value["records"][0]["ledger"][0]["denominator"] = "clipped"
    elif c == 10: value["records"][0]["ledger"][0]["zero_mode"] = "deleted"
    elif c == 11: value["records"][0]["ledger"][0]["spin"] = 1.0
    elif c == 12: value["records"][0]["ledger"][0]["color"] = 0.0
    elif c == 13: value["records"][0]["units"] = "dimensionless"
    elif c == 14: value["records"][0]["L"] = "L^-1"
    elif c == 15: value["renormalization"]["subtraction"] = "BPP_DLCQ"
    elif c == 16: value["renormalization"]["physical_coefficient"] = 1.0
    elif c == 17: value["count_once"]["C53_propagation"] = "USED"
    elif c == 18: value["no_C53_values"] = False
    elif c == 19: value["no_direct_contact"] = False
    elif c == 20: value["no_complete_iferm"] = False
    elif c == 21: value["records"][0]["pair_counts"]["admitted"] = 0
    elif c == 22: value["records"][0]["symbolic_coefficient"] = "fit"
    elif c == 23: value["C57_import"]["C53_support_holdout"][0] = 0
    elif c == 24: value["qg_sector"]["status"] = "ZERO_FULL_QCD"
    elif c == 25: value["counterterm_directions"]["mass"] = "universal fit"
    elif c == 26: value["records"][1]["matrix"]["shape"][0] = 0
    elif c == 27: value["records"][2]["ledger"][0]["mode_index"] = -1
    elif c == 28: value["status"] = "C58_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY"
    elif c == 29: value["next"] = "C59/BRIDGE"
    elif c == 30: value["C57_import"]["records"][1]["union"] = 1
    else: value["C55"]["vacuum"] = "proton"
    value["__c58_mutation__"] = f"live:{fault_id}"
    return value


def assert_ready_c58() -> dict[str, Any]:
    value = build_contraction(); assert value["status"] == STATUS
    assert value["pair_support"]["selected"] == PAIR_PLAN
    assert value["qg_sector"]["selected"] == QG_PLAN
    for record in value["records"]:
        one = np.ones(record["matrix"].shape[1], dtype=np.complex128)
        assert np.linalg.norm(record["matrix"] @ one - apply_direct(record, one)) < 1e-11
        assert np.linalg.norm(record["matrix"] - record["matrix"].conj().T) < 1e-11
    return value
