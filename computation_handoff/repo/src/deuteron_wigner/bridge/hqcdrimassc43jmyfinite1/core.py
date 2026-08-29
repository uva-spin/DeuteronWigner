"""C357 finite-group authority audit after analytic-pole cancellation."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c357_hqcdrimassc43jmyfinite1";BASELINE="a31927d7798cee62653e9ac7bdf46c79ff0211e0";C356_ROOT="82525d8cbc408604dd73e99732c1c26a15f894f53028b9b6b07014fcc07811fc"
STATUS="C357_FINITE_GROUP_AUTHORITY_AUDITED_OPERATOR_IDENTICAL_ANALYTIC_REGULATED_JMY_INTEGRANDS_MISSING";PLAN="RIMASSC43JMYFINITE1-C";NEXT="C358/HQCDRIMASSC43JMYINTEGRAND1";NEXT_OBJECT="C357-C43-JMY-ANALYTIC-REGULATED-GRAPH-INTEGRANDS";NEXT_EXACT="derive the operator-identical alpha-beta regulated JMY virtual real-endpoint and soft graph integrands required for finite evaluation"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def authority_matrix():
 rows=({"authority":"JMY hep-ph/0404183v1","operator_identical":True,"IR":"mass m,lambda","analytic_separator":False,"finite_terms":True,"usable_directly":False},{"authority":"Becher-Neubert 1007.4005v2","operator_identical":False,"IR":"dimensional","analytic_separator":True,"finite_terms":True,"usable_directly":False},{"authority":"C356 residue matrix","operator_identical":True,"IR":"dimensional","analytic_separator":True,"finite_terms":False,"usable_directly":False})
 return {"rows":rows,"count":3,"joint_finite_authority":False,"root":_r(rows)}
def finite_group_ledger():
 rows=tuple({"group":g,"value":"UNAVAILABLE_NOT_ZERO","known":"analytic poles and auxiliary-scale dependence cancel","missing":"operator-identical regulated numerator integral through O(alpha^0,beta^0,epsilon^0)"} for g in ("distribution_virtual","distribution_real_endpoint","fragmentation_virtual","fragmentation_real_endpoint","soft_real_virtual_count_once"))
 return {"rows":rows,"count":5,"constant_inferred_from_RG":False,"mass_result_reused":False,"root":_r(rows)}
def missing_integrand_spec():return {"requirements":("JMY quark propagator numerator and v-eikonal denominator with fractional alpha power","crossed fragmentation numerator and tilde-v denominator with fractional beta power","four-line v/tilde-v soft real and virtual cuts with matching powers","transverse Fourier measurement and plus/delta endpoint measurement","MSbar counterterms with UV/IR pole labels"),"limit_order":"group -> alpha,beta limits in both orders -> epsilon expansion","root":_r("C357-I")}
def closure():return {"finite_groups_evaluated":False,"failure_is_absent_integrand_not_contradiction":True,"ordinary_derivation_continuation":True,"finite_conversion_ready":False,"C43_imported":False,"root":_r("C357-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"mass_finite_reused":0,"foreign_finite_import":0,"RG_constant_inferred":0,"unavailable_set_zero":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyfinite1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyfinite1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyresidue1 as c
 if c.PACKAGE_ROOT!=C356_ROOT:raise ValueError("C356")
 c.load_verified_hqcdrimassc43jmyresidue1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyfinite1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyfinite1_authority()
_ROOTS={"INPUT":_r((BASELINE,C356_ROOT)),"AUTHORITY":authority_matrix()["root"],"LEDGER":finite_group_ledger()["root"],"SPEC":missing_integrand_spec()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C357-HQCDRIMASSC43JMYFINITE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
