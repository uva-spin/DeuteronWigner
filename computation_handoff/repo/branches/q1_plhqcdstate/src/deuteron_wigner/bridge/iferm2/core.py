"""C59: preserve C58 and fail closed before an unqualified qg contact.

C58 closes only the one-pair commutator.  C55's direct ``b† a† a b`` term is
symbolic, and C57's graph projector is q->qg canonical support, explicitly
not a direct-contact qg-bra/qg-ket support.  This module proves that boundary
and deliberately makes no direct-contact or complete IF matrix.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import json
from typing import Any

from ..iferm.core import instantaneous_fermion_preflight
from ..ifnorm2.core import PAIR_PLAN, QG_PLAN, STATUS as C58_STATUS, build_contraction, serializable
from ..ifreg.core import PLAN as C57_PLAN, build_regulator

BASELINE = "43bf2493ec020a130bbf4cb576a851adc5b5e0cf"
STATUS = "C59_IFERM_CONTACT_SUPPORT_INCOMPLETE"
NEXT = "C60/IFSUPPORT — source-ordered q-intermediate support and graph-selection closure"
MONOMIAL = ("b_dagger", "a_dagger", "a", "b")

def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)

def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()

def import_c58_read_only() -> dict[str, Any]:
    """Verify the immutable C58 package without reusing its values as contact input."""
    value = build_contraction()
    assert value["status"] == C58_STATUS
    assert value["pair_support"]["selected"] == PAIR_PLAN
    assert value["qg_sector"]["selected"] == QG_PLAN
    records=[]
    for rec, expected in zip(value["records"], (4216, 8330, 14484)):
        matrix=rec["matrix"]
        assert matrix.shape == (6,6) and int((matrix != 0).sum()) == 6
        assert len(rec["ledger"]) == expected
        records.append({"resolution":rec["resolution"], "shape":list(matrix.shape), "nnz":int((matrix != 0).sum()),
                        "mode_count":len(rec["ledger"]), "array_hash":serializable(matrix)["hash"],
                        "expression_hash":sha256(rec["symbolic_coefficient"].encode()).hexdigest(),
                        "basis_order_hash":sha256(canonical_json(rec["basis"]).encode()).hexdigest()})
    return {"status":"PASS_READ_ONLY", "C58_status":value["status"], "pair_support_plan":PAIR_PLAN,
            "qg_sector_plan":QG_PLAN, "bare_plan":value["renormalization"]["selected"],
            "qg_status":value["qg_sector"]["status"], "records":records,
            "import_hash":digest(serializable(value)), "prohibitions":["rescale", "subtraction", "C58 qg lift", "C53 propagation"]}

def direct_contact_source_ledger() -> list[dict[str, Any]]:
    c55=instantaneous_fermion_preflight()
    rows=[x for x in c55["ledger"] if tuple(x["operator_order"]) == MONOMIAL]
    assert len(rows)==1 and rows[0]["status"] == "DIRECT_RETAINED_OPERATOR"
    row=rows[0]
    return [{"id":"C55-W3-DIRECT-A_DAGGER-A", "C55_operator_order":list(MONOMIAL),
             "normal_order_ancestry":"original normal-ordered a_dagger a branch; distinct from the C58 a a_dagger commutator",
             "color_order":row["color_order"], "inverse_derivative_argument":row["inverse_derivative_argument"],
             "routing":row["routing"], "retained_block":"qg_to_qg", "coupling_order":"g_s^2",
             "status":"DIRECT_QG_CONTACT_REQUIRED", "hermitian_partner":"must be derived from full source W3 ordering"}]

def support_audit() -> dict[str, Any]:
    c57=build_regulator()
    assert c57["plan"]["selected"] == C57_PLAN
    return {"status":STATUS, "selected":"IFERM2-DIRECT-CONTACT-SUPPORT-UNAVAILABLE",
            "C57_scope":"C57 conditional masks are induced by canonical q-to-qg emission support and explicitly predate/no-direct-contact construction.",
            "missing_contract":"No source-qualified ordered map assigns the left and right C55 a_dagger/a fields to a qg bra/ket pair and a retained q intermediate before the source terms are summed.",
            "why_not_common_q":"qg_mask.T @ qg_mask would be an arbitrary algebraic common-support construction unless the missing ordered direct-contact embedding is first derived.",
            "why_not_full_qg":"the full C47 qg basis exists but TBP graph selection forbids promoting it to direct-contact support by convenience.",
            "why_not_C53":"C53 numerical entries, singular values, and energy denominators are forbidden and cannot define support.",
            "C57_qg_support_ranks":[[int(x["qg_support_rank"]) for x in r["parents"]] for r in c57["records"]],
            "zero_mode":"P0/Q0 and residual boundary controls remain separate; no denominator is evaluated before support exists."}

@lru_cache(maxsize=1)
def preflight() -> dict[str, Any]:
    imported=import_c58_read_only(); ledger=direct_contact_source_ledger(); support=support_audit()
    return {"baseline":BASELINE, "status":STATUS, "next":NEXT, "C58_import":imported,
            "direct_source_ledger":ledger, "support_audit":support,
            "kernel_audit":{"status":"NOT_EVALUATED_AFTER_SUPPORT_BLOCKER", "finite_four_HO_kernel":False,
                            "plane_wave_contact_kernel":False, "Pminus_to_M2":False},
            "preserved_blocks":{"q_to_q":"C58_READ_ONLY", "q_to_qg":"EXACT_ZERO_BY_GLUON_NUMBER_PARITY",
                                "qg_to_q":"EXACT_ZERO_BY_GLUON_NUMBER_PARITY", "qg_to_qg":"DIRECT_CONTACT_REQUIRED_NOT_CONSTRUCTED; qg_SII_COUNTERTERM_ONLY"},
            "count_once":{"direct_contact":"REQUIRED_NOT_CONSTRUCTED", "C58_contraction":"READ_ONLY_IMPORTED",
                          "C53_propagation":"FORBIDDEN_SUBSTITUTE", "qg_SII":"COUNTERTERM_ONLY_NOT_ZERO_FULL_QCD",
                          "boundary_zero_modes":"SEPARATE"},
            "no_direct_contact_matrix":True, "no_complete_iferm_matrix":True, "no_C53_values":True,
            "no_physical_coefficient":True}

def validate_c59(value: dict[str, Any]) -> bool:
    return canonical_json(value)==canonical_json(serializable(preflight())) and value["status"]==STATUS

def snapshot() -> dict[str, Any]: return serializable(preflight())

def mutate_live_c59(fault_id:int) -> dict[str, Any]:
    value=deepcopy(snapshot()); c=fault_id%16
    if c==0: value["C58_import"]["records"][0]["array_hash"]="bad"
    elif c==1: value["C58_import"]["pair_support_plan"]="union"
    elif c==2: value["C58_import"]["qg_status"]="ZERO_FULL_QCD"
    elif c==3: value["direct_source_ledger"][0]["C55_operator_order"][1]="a"
    elif c==4: value["direct_source_ledger"][0]["normal_order_ancestry"]="C58 commutator"
    elif c==5: value["support_audit"]["selected"]="IFERM2-COMMON-Q-INTERMEDIATE-PROJECTOR"
    elif c==6: value["support_audit"]["why_not_C53"]="C53 numerical values allowed"
    elif c==7: value["kernel_audit"]["finite_four_HO_kernel"]=True
    elif c==8: value["preserved_blocks"]["q_to_qg"]="NONZERO"
    elif c==9: value["count_once"]["C53_propagation"]="USED"
    elif c==10: value["count_once"]["qg_SII"]="ZERO"
    elif c==11: value["no_direct_contact_matrix"]=False
    elif c==12: value["no_complete_iferm_matrix"]=False
    elif c==13: value["no_C53_values"]=False
    elif c==14: value["no_physical_coefficient"]=False
    else: value["next"]="C60/HQCD3"
    return value

def assert_fail_closed_c59() -> dict[str, Any]:
    value=preflight(); assert value["status"]==STATUS
    assert value["C58_import"]["qg_sector_plan"]==QG_PLAN
    assert value["support_audit"]["selected"]=="IFERM2-DIRECT-CONTACT-SUPPORT-UNAVAILABLE"
    assert value["no_direct_contact_matrix"] and value["no_complete_iferm_matrix"]
    return value
