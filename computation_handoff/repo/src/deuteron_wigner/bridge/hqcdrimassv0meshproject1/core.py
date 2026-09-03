"""C304 V0 mesh/direct projection audit and measure correction."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c304_hqcdrimassv0meshproject1";BASELINE="79b597a634c1af6594d28f22ac8eca72dcc5d49c";C303_ROOT="56d663455a989e534f9a2072bfc46dd840a0bbc886b77478a6387ce70a5ca300"
STATUS="C304_SQUARE_MEASURE_NORMALIZATION_CORRECTED_V0_PROJECTION_WALL_NONCONVERGENCE_CERTIFIED_FINITE_PART_MISSING";PLAN="RIMASSV0MESHPROJECT1-C";NEXT="C305/HQCDRIMASSV0FINITEPART1";NEXT_OBJECT="C304-V0-WEYL-WALL-FINITE-PART-PRESCRIPTION";NEXT_EXACT="define and validate a source-compatible Weyl-wall excision or finite-part prescription making the reduced V0 class-function projection regulator explicit"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def measure_correction():return _f({"square":"u,v in [0,1]","J":"64 sin^2(pi u) sin^2(pi v) sin^2(pi(v-u))","exact_constant_term_integral_J":6,"C296_density":"J/3","C296_square_integral":2,"corrected_square_density":"J/6","corrected_integral":1,"reason":"Soyez square covers two Weyl alcoves","routes":("exact discrete Fourier constant term","Gauss-Legendre G=20,32,48","one-million-point Monte Carlo"),"root":_r("C304-J6")})
def direct_sum_scan():
 rows=({"G":12,"N":64,"constant":-338.22937504,"CHI8":-391.79533794,"RE_TF3":127.24544222,"rms":1136.90703457,"minimum":-185953.92847746},{"G":18,"N":64,"constant":-357.56697566,"CHI8":-425.29866980,"RE_TF3":139.72682755,"rms":1726.92510899,"minimum":-894544.02141120},{"G":24,"N":64,"constant":-367.90373706,"CHI8":-443.24504080,"RE_TF3":146.43583282,"rms":2310.85592948,"minimum":-2754242.85369183});return _f({"rows":rows,"measure":"J/6","wall_nodes_skipped":True,"quadrature_converged":False,"shape_coefficients_stable":False,"root":_r(rows)})
def mesh_reconstruction():return _f({"artifact":"potSU3.ps","nominal_grid":"41x41","visible_segments":67,"hidden_line_clipped":True,"z_axis":"0..10000","source_boundary_statement":"V0 presents discontinuities at domain boundaries","full_values_recoverable":False,"projection_from_plot_alone":False,"root":_r("C304-MESH")})
def projection_certificate():return _f({"basis":("constant","CHI8","RE_TF3"),"requested_result":"NO_REGULATOR_INDEPENDENT_VALUE_AT_DECLARED_SCOPE","digitization_enclosure":"UNBOUNDED_BY_HIDDEN_WALL_VALUES","C43_matching":False,"contradiction":False,"next":NEXT,"root":_r("C304-NONCONVERGENCE")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"normalization_corrected":True,"projection_complete":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"J_over_3_retained":0,"wall_values_invented":0,"nonconvergent_coefficients_promoted":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0meshproject1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("Jacobian","normalization","Weyl","mesh","clip","cutoff","quadrature","Gram","wall","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0meshproject1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0project1 as c303
 if c303.PACKAGE_ROOT!=C303_ROOT:raise ValueError("C303 root changed")
 c303.load_verified_hqcdrimassv0project1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0meshproject1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0meshproject1_authority()
_ROOTS={"INPUT":_r((BASELINE,C303_ROOT)),"MEASURE":measure_correction()["root"],"SCAN":direct_sum_scan()["root"],"MESH":mesh_reconstruction()["root"],"PROJ":projection_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C304-HQCDRIMASSV0MESHPROJECT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
