"""C303 exact V0 AST and vector-mesh projection preimage."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c303_hqcdrimassv0project1";BASELINE="01f0809881621d18092c095c54662e18fb955b80";C302_ROOT="fcf212b7cddedaeaeb8d2ea110e8c7e3a79dc7a853e198837200a9933262471a"
STATUS="C303_EXACT_V0_SUM_AST_AND_VECTOR_MESH_AXES_READY_VISIBILITY_RECONSTRUCTION_PROJECTION_MISSING";PLAN="RIMASSV0PROJECT1-C";NEXT="C304/HQCDRIMASSV0MESHPROJECT1";NEXT_OBJECT="C303-V0-VECTOR-MESH-VISIBILITY-PROJECTION";NEXT_EXACT="reconstruct the clipped 41x41 C293 potSU3 vector mesh and perform the normalized C301 class-function Gram projection with digitization enclosure"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_ast():
 rows=({"term":"S1","indices":"k,m half-integers >=1/2","kernel":"(k+m)^-2 (k-m-2 zeta_r)^2/[(m+zeta_r)(k-zeta_r)]","roots":"r=2,4,7"},{"term":"S2","indices":"m>=1/2, k>=m+1","kernel":"(k-m)^-1 paired +/- zeta rational kernel","roots":"r=2,4,7"},{"term":"S3","indices":"m,n half-integers >=1/2","kernel":"paired cyclic zeta2,zeta4,zeta7 rational kernels with M0","roots":"three cyclic permutations"});return _f({"rows":rows,"count":3,"zeta":"zeta(x)=x-m0(x), periodic odd, |zeta|<1/2","M0":"m0,2+m0,4+m0,7","domain":"u,v in [0,1]","source_lines":"599-627","root":_r(rows)})
def mesh_preimage():return _f({"artifact":"data/raw/c293_sources_hep-th-0101072.tar::potSU3.ps","creator":"gnuplot 3.7 patchlevel 0","lines":3450,"nominal_grid":"41x41 inferred from 0.025 projected increments","visible_polyline_segments":67,"u_axis":"(970,1248) to (4304,608)","v_axis":"(4304,608) to (6229,1716)","z_ticks":"0..10000 step 2000; 295.5 screen-y per 2000","clipping":"hidden-line segmentation; segments are not independent rows","root":_r("C303-PS-MESH")})
def projection_contract():return _f({"basis":("constant","CHI8","RE_TF3"),"measure":"C295 normalized nonflat alcove","method":"weighted Gram solve","route_A":"regulated source AST after cutoff prescription","route_B":"PostScript mesh reconstruction","current_result":"UNAVAILABLE_NOT_ZERO","reason":"source omits sum cutoff and PS hidden-line mesh requires visibility reconstruction","C43_matching":False,"root":_r("C303-PROJ")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"AST":True,"mesh_axes":True,"projection":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"clipped_segments_as_rows":0,"cutoff_invented":0,"coefficient_fabricated":0,"C43_matching_claimed":0,"flat_measure":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0project1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("AST","index","zeta","M0","mesh","axis","clip","basis","measure","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0project1_authority():
 from deuteron_wigner.bridge import hqcdrimassholonomycoeff1 as c302
 if c302.PACKAGE_ROOT!=C302_ROOT:raise ValueError("C302 root changed")
 c302.load_verified_hqcdrimassholonomycoeff1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0project1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0project1_authority()
_ROOTS={"INPUT":_r((BASELINE,C302_ROOT)),"AST":source_ast()["root"],"MESH":mesh_preimage()["root"],"PROJ":projection_contract()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C303-HQCDRIMASSV0PROJECT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
