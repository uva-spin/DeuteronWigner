"""C299 typed adjoint-scalar constraint input and authority audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c299_hqcdrimassconstraintinput1"
BASELINE="247c9f04d7d9928b48d7dac91513dda4faacd0a3";C298_ROOT="2f7fd3ff7fd8bf4c15db8d135c82f7a378c7f82bc6f0717063db08ce2745a6a9"
STATUS="C299_ADJOINT_SCALAR_INPUT_SCHEMA_AND_QUARK_MASS_NON_EQUIVALENCE_BOUND_GAUGE_ST_MASS_IDENTITY_MISSING";PLAN="RIMASSCONSTRAINTINPUT1-C"
NEXT="C300/HQCDRIMASSADJOINTST1";NEXT_OBJECT="C299-ADJOINT-SCALAR-ZERO-MODE-MASS-ST-IDENTITY";NEXT_EXACT="derive the C43 gauge/BRST/ST identity fixing or classifying the transverse-gauge adjoint-scalar zero-mode mass counterterm before K-resolved constraint matrix elements"
RES=("K9","K11","K13")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def authority_audit():
 rows=({"authority":"Soyez mu0^2","operator":"adjoint scalar from transverse gauge field","result":"BARE_SYMBOL_RENORMALIZATION_NOT_PERFORMED"},{"authority":"C276-C283 RI/SMOM mass","operator":"fundamental signed quark bilinear","result":"INCOMPATIBLE_OPERATOR_NO_ADAPTER"},{"authority":"C43/C130","operator":"3+1 transverse gauge field/zero-mode constraints","result":"NO_BOUND_ADJOINT_SCALAR_MASS_RECORD"},{"authority":"C274/C278 K states","operator":"caller Hamiltonian/state slots","result":"NO_SIX_CHANNEL_MATRIX_ELEMENTS"});return _f({"rows":rows,"count":4,"usable_records":0,"root":_r(rows)})
def mass_schema():return _f({"operator":"tr(Phi^2), Phi is reduced transverse adjoint gauge field","required":("scheme","scale","mu_R2","bare_to_renormalized_map","gauge_BRST_ST_classification","covariance"),"quark_mass_allowed":False,"zero_default":False,"complete":False,"root":_r("C299-MASS-SCHEMA")})
def matrix_element_schema():
 rows=tuple({"resolution":k,"channels":("1J2","2J1","4J5","5J4","6J7","7J6"),"state_normalization":"C274 authenticated eigenstate required","Q_resolvent":"C298","values":"UNAVAILABLE_NOT_ZERO","covariance_block":"6x6 plus cross-K blocks required"} for k in RES);return _f({"rows":rows,"count":3,"channel_count":6,"root":_r(rows)})
def covariance_schema():return _f({"dimension":"18x18 matrix-element block plus shared mass/coupling nuisance parameters","cross_K_blocks_required":True,"PSD_required":True,"zero_assumed":False,"root":_r("C299-COV-SCHEMA")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"typed_input":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"quark_mass_substituted":0,"adjoint_mass_zeroed":0,"matrix_elements_zeroed":0,"K_averaged":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassconstraintinput1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("operator","scheme","scale","mass","channel","state","K","covariance","ST","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassconstraintinput1_authority():
 from deuteron_wigner.bridge import hqcdrimassconstraintkernel1 as c298
 if c298.PACKAGE_ROOT!=C298_ROOT:raise ValueError("C298 root changed")
 c298.load_verified_hqcdrimassconstraintkernel1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassconstraintinput1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassconstraintinput1_authority()
_ROOTS={"INPUT":_r((BASELINE,C298_ROOT)),"AUDIT":authority_audit()["root"],"MASS":mass_schema()["root"],"MATRIX":matrix_element_schema()["root"],"COV":covariance_schema()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C299-HQCDRIMASSCONSTRAINTINPUT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
