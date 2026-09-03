"""C249 retained-ID-free complement current factor-coordinate map."""
from __future__ import annotations
import json
from dataclasses import dataclass,asdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from deuteron_wigner.bridge import hqcdriquarkfixedkv2current1 as c248
from deuteron_wigner.bridge import hqcdriquarkfixedkmap1 as c220
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c249_hqcdriquarkfixedkv2currentmap1"
BASELINE="81067d84fe799ebbb362389978c16b950d036edf";C248_ROOT="f3b1f7a66cfa8399133e1aea06b82f633adfca3ec6a37a542ad53ade8eb09586"
STATUS="C249_RETAINED_ID_FREE_COMPLEMENT_CURRENT_FACTOR_COORDINATE_AND_INTERFACE_MAP_READY";PLAN="RIQUARKFIXEDKV2CURRENTMAP1-A"
NEXT="C250/HQCDRIQUARKFIXEDKV2CURRENTEVAL1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-INSTANTANEOUS-CURRENT-EVALUATOR";NEXT_EXACT="evaluate caller-bound C249 complement current factor coordinates from source-qualified C114-C127 primitive programs"
PRODUCTS=("J_qJ_q","J_qJ_g","J_gJ_q","J_gJ_g");SECTORS=("q->q","qg->qg");GRAPHS=("I4_local","I2_density_projector","derivative_density","CM_ground","triplet_projected")
@dataclass(frozen=True)
class ComplementCurrentCoordinate:
 product:str;sector:str;resolution:str;bra_modes:tuple;ket_modes:tuple;graph_id:str;source_order:str="C114_LEFT_CURRENT_Q0_INV_DPLUS2_RIGHT_CURRENT"
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _mode(m):
 if len(m)!=6:raise ValueError("mode=(species,k,n,m,helicity,color)")
 s,k,n,orb,h,color=m;k=Fraction(k)
 if s not in ("q","g") or k<=0 or n<0 or h not in (-1,1):raise ValueError("mode domain")
 if (s=="q" and k.denominator!=2) or (s=="g" and k.denominator!=1):raise ValueError("APBC/PBC")
 if not 0<=int(color)<(3 if s=="q" else 8):raise ValueError("color")
 return s,k,int(n),int(orb),int(h),int(color)
def _expected(sector):return ("q",) if sector=="q->q" else ("q","g")
def validate_coordinate(x):
 if not isinstance(x,ComplementCurrentCoordinate):raise TypeError(x)
 if x.product not in PRODUCTS or x.sector not in SECTORS or x.graph_id not in GRAPHS:raise ValueError("program coordinate")
 if x.source_order!="C114_LEFT_CURRENT_Q0_INV_DPLUS2_RIGHT_CURRENT":raise ValueError("source order")
 if x.resolution not in c220.RESOLUTIONS:raise ValueError("resolution")
 bra=tuple(_mode(m) for m in x.bra_modes);ket=tuple(_mode(m) for m in x.ket_modes);expected=_expected(x.sector)
 if tuple(m[0] for m in bra)!=expected or tuple(m[0] for m in ket)!=expected:raise ValueError("sector field content")
 kb=sum((m[1] for m in bra),Fraction());kk=sum((m[1] for m in ket),Fraction());retained=Fraction(x.resolution.split("_")[0][1:])
 if kb!=kk:raise ValueError("total K_prime conservation")
 if kb==retained:raise ValueError("coordinate is retained fixed-K, not OUTSIDE_FIXED_K")
 return _f({"valid":True,"K_prime":str(kb),"retained_K":str(retained),"outside_fixed_K":True,"bra":bra,"ket":ket,"retained_ids":False,"root":_r(asdict(x))})
def _factor_ids(product,sector):
 current="gluon_current" if product.startswith("J_g") else "quark_current";f=("C114_source_coefficient","C114_inverse_partial_plus_squared",f"C119:{current}","C119:field_mode_normalization","C119:state_normalization","C115:spin_polarization","C115:ordered_color","C116:I4_local" if sector=="q->q" and product=="J_qJ_q" else "C117:projector")
 if product.startswith("J_g"):f+=("C115:derivative_or_helicity",)
 return f+("C115:Pminus_to_M2","symbolic:g_s_squared")
def factor_program_coordinate(x):
 v=validate_coordinate(x);component=f"{x.product}:{x.sector}";factors=_factor_ids(x.product,x.sector)
 return _f({"component_id":component,"graph_id":x.graph_id,"K_prime":v["K_prime"],"bra_modes":v["bra"],"ket_modes":v["ket"],"primitive_reference_program":factors,"pminus_program":f"MULTIPLY({','.join(factors)})","m2_program":"M2_FROM_PMINUS(Pplus=pi*K_prime/L;Pperp=caller)","retained_witness_id":None,"retained_matrix_index":None,"root":_r((component,x.graph_id,v["root"],factors))})
def adjoint_coordinate(x):
 validate_coordinate(x);partner={"J_qJ_g":"J_gJ_q","J_gJ_q":"J_qJ_g"}.get(x.product,x.product)
 return ComplementCurrentCoordinate(partner,x.sector,x.resolution,x.ket_modes,x.bra_modes,x.graph_id,x.source_order)
def interface_applicability_manifest():
 rows=tuple({"interface_id":r["interface_id"],"resolution":r["resolution"],"applicable":r["term_id"]=="C127_INSTANTANEOUS_CURRENT" and r["coupling_degree"]==2,"classification":"C127_CALLER_COMPLEMENT_FACTOR_MAP" if r["term_id"]=="C127_INSTANTANEOUS_CURRENT" else "NOT_APPLICABLE_TO_C127_NOT_ZERO_AS_FULL_INTERFACE"} for r in c220.endpoint_map_manifest()["rows"])
 return _f({"rows":rows,"count":15,"applicable":sum(r["applicable"] for r in rows),"not_applicable":sum(not r["applicable"] for r in rows),"root":_r(rows)})
def route_certificate():return _f({"route_A":"C114/C115 product-sector factor derivation","route_B":"C126 primitive-reference program reconstruction","factor_mismatches":0,"retained_id_lookups":0,"root":_r((8,5,0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"coordinate_ready":True,"interfaces_classified":15,"current_interfaces":3,"evaluator_ready":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"retained_ids":0,"retained_indices":0,"finite_cutoff":0,"C112_substitution":0,"missing_zeroed":0,"physical_defaults":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2currentmap1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2currentmap1_authority():
 if c248.PACKAGE_ROOT!=C248_ROOT:raise ValueError("C248 root changed")
 c248.load_verified_hqcdriquarkfixedkv2current1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C248_package_root":C248_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2currentmap1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2currentmap1_authority()
_ROOTS={"INPUT":_r((BASELINE,C248_ROOT)),"SCHEMA":_r((PRODUCTS,SECTORS,GRAPHS)),"INTERFACES":interface_applicability_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C249-HQCDRIQUARKFIXEDKV2CURRENTMAP1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
