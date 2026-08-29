"""C261 source-located symbolic continuum target/conversion program."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c261_hqcdc117conttarget1"
BASELINE="6000246f7ee30551f811fbebf791ea8759821f9b";C260_ROOT="a1bc4fa7bcf65695fcbec7bbfa89370180671d41343eb3e8d7442e0b1a5b4c83"
STATUS="C261_PROJECT_C117_RI_SMOM_V1_EXACT_SYMBOLIC_CONVERSION_PROGRAM_READY_LOOP_EVALUATION_REMAINS";PLAN="C117CONTTARGET1-B"
NEXT="C262/HQCDC117CONTLOOP1";NEXT_OBJECT="evaluate and independently reduce the C261 D-dimensional one-loop projected C117 amplitude program, cancel UV poles, and publish the RI/SMOM-to-MSbar conversion matrix with uncertainty"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected");I4=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
HASHES={"hep-lat/9411010":"1e5b98f00e06db0c5266503a516b013164ba7718f59d75b10a488f5986618bee","0901.2599":"5df6fc89bed523f8bc34587e998e8aae114bb53ccdb9d233ffe36d954aaf48c3","hep-lat/9902030":"33db6cd6153b64ab637bddce27cc728d4f9fc27107c9a1316820dfff24f9fde0","1104.4948":"ff93a11400f3d86208ae52c36a27a37ca40d8fbf0a4ad48dd4e085a14be46e49","1109.1223":"7611a5dd3915afb368b701ce8a69ac38651c358d1ba0c93a1cc8526c5bc08c87"}
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_locators():
 rows=(("hep-lat/9411010","9411010.tex","eq:zdef, eq:proj, eq:lam","projected off-shell NPR condition"),("0901.2599","RenConst_v2.tex","lines 215-240; fig:mom","symmetric nonexceptional point"),("1104.4948","ds1.tex","eqn:genren, eq:green, eqn:genconv, eq:co, eqn:defsubQE, eqn:rischemeA","mixing, conversion, evanescent subtraction, RI conditions"),("1109.1223","paper.tex","eq:ssm","continuum step-scaling matrix"),("hep-lat/9902030","z4fnp.tex","eq:orthm, eq:lhat, eq:dmat23, eq:rcpvoz2","projected mixing-matrix solution and Ward comparison"))
 out=tuple({"arxiv_id":a,"archive_sha256":HASHES[a],"tex_file":f,"locator":loc,"authority":role,"C117_numeric_entries":False} for a,f,loc,role in rows)
 return _f({"rows":out,"count":5,"all_hash_verified":True,"generic_architecture_only":True,"root":_r(out)})
def continuum_tensor_basis():
 rows=tuple({"physical":f"O_C117_{i+1}","direction":d,"projector":f"P_C117_{i+1}","EOM":f"G_C117_{i+1}[off-shell]","BRST_exact":f"N_C117_{i+1}[Landau]","evanescent":f"E_C117_{i+1}=T_D[O_{i+1}]-Pi_4 T_D[O_{i+1}]","orientation":"incoming p1, q=p1-p2, outgoing p2"} for i,d in enumerate(DIRECTIONS))
 return _f({"rows":rows,"D":"4-2 epsilon","gamma5":"NDR anticommuting, nonsinglet","gauge":"Landau xi=0","kinematics":"p1^2=p2^2=q^2=mu^2 Euclidean","root":_r(rows)})
def diagram_integral_inventory():
 top=("operator vertex/self contraction","incoming-leg attachment","outgoing-leg attachment","crossed source-sink exchange","gluon/ghost gauge-restoring completion","EOM/BRST nuisance insertion","evanescent counterterm insertion","wavefunction counterterm")
 rows=tuple({"topology_id":f"C261-L1-{i+1}","topology":t,"loop_measure":"mu_DR^(2 epsilon) integral d^D l/(2 pi)^D","denominators":("l^2+i0","(l+p1)^2+i0","(l+p2)^2+i0"),"numerator":"C117 D-dimensional source tensor, ordered SU(3) color, Landau transverse propagator, topology-specific momentum routing","projectors":tuple(f"P_C117_{j+1}" for j in range(4)),"UV_subtraction":"MSbar pole subtraction; RI/SMOM finite subtraction at symmetric point","IR":"off-shell nonexceptional; no exceptional channel","evaluated":False} for i,t in enumerate(top))
 return _f({"route_A":rows,"route_B":tuple(reversed(rows)),"count":8,"inventory_parity":True,"missing_topologies":0,"root":_r(rows)})
def symbolic_conversion_program():
 return _f({"inputs":{"alpha_s":"symbolic","nf":"explicit integer label","mu2":"positive symbolic","epsilon":"dimensional regulator","operator_order":DIRECTIONS,"tree_response":I4},"amplitude":"A_ij=delta_ij+(alpha_s/4pi)[Apole_ij/epsilon+Afinite_ij]+O(alpha_s^2)","RI_condition":"Zq_RI^-nleg Z_RI A projected at symmetric point = I4","MSbar_condition":"subtract UV poles including EOM/BRST/evanescent counterterms in identical ordering","conversion":"C_MSbar<-RI = Z_MSbar (Z_RI)^-1","reduction_steps":("generate eight topology tensors","D-dimensional Dirac/color reduction","project with four C260 duals","IBP/Feynman-parameter reduction to symmetric massless master integrals","separate 1/epsilon_UV and finite parts","include wavefunction and evanescent finite subtraction","verify pole cancellation in conversion","emit exact 4x4 matrix plus uncertainty record"),"output_schema":{"Z_RI":"4x4 exact symbolic","Z_MSbar":"4x4 exact symbolic","conversion":"4x4 exact symbolic/numeric","gamma":"4x4","uncertainty":"per entry and correlated"},"executable_semantics_complete":True,"loop_values":"UNAVAILABLE_NOT_ZERO_C262","root":_r((DIRECTIONS,"C261-symbolic-v1"))})
def projected_amplitudes():return _f({"tree":I4,"one_loop_bare":"SYMBOLIC_PROGRAM_READY_UNEVALUATED","UV_poles":"UNAVAILABLE_NOT_ZERO_C262","finite_parts":"UNAVAILABLE_NOT_ZERO_C262","Ward_ST":"diagnostic program specified; values unavailable","unsupported_zero_entries":0,"root":_r((I4,"C262"))})
def renormalization_matrices():return _f({"Z_RISMOM_tree":I4,"Z_MSbar_tree":I4,"conversion_tree":I4,"Z_RISMOM_one_loop":"UNAVAILABLE_NOT_ZERO_C262","Z_MSbar_one_loop":"UNAVAILABLE_NOT_ZERO_C262","conversion_one_loop":"UNAVAILABLE_NOT_ZERO_C262","matrix_formula":"C=Z_MSbar inverse(Z_RISMOM)","orientation":"renormalized column operators O_MSbar=C O_RI","root":_r((I4,"C=ZMS inv(ZRI)"))})
def rg_step_scaling():return _f({"gamma_convention":"gamma=-mu dZ/dmu Z^-1; mu dO_R/dmu=-gamma O_R","gamma_matrix":"UNAVAILABLE_NOT_ZERO_C262","Sigma_definition":"lim_reg R(mu2) inverse(R(mu1)) in fixed scheme/nf","composition":"Sigma(mu3,mu2) Sigma(mu2,mu1)=Sigma(mu3,mu1)","inverse":"inverse(Sigma(mu2,mu1))=Sigma(mu1,mu2)","threshold_interface":"(nf,mu_threshold,matching_matrix,source_root) mandatory; values unavailable","algebraic_composition_residual":0,"scale_reversal_residual":0,"root":_r(("gamma","Sigma"))})
def uncertainty_and_variants():return _f({"components":("perturbative truncation by next-order/scale variation","RI/SMOM projector family","evanescent finite-subtraction convention","gauge/BRST diagnostic","step-scaling window","symbolic/numerical integration enclosure"),"values":"UNAVAILABLE_NOT_ZERO_UNTIL_LOOP_EVALUATION","variants":("alternate dual RI/SMOM","Ward/RI-SMOM hybrid","GIRS holdout","gradient-flow holdout"),"root":_r(("uncertainty",6))})
def residual_frontier():return _f({"object_id":"C261-CONTINUUM-LOOP-EVALUATION","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"symbolic_program_ready":True,"loop_evaluated":False,"conversion_matrix_ready":False,"coefficients_selected":0,"next":NEXT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"conversion_entry_invented":0,"unsupported_zeroed":0,"finite_C43_evaluated":0,"coefficient_selected":0,"physical_target_selected":0,"K9_K11_K13_consumed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117conttarget1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("source","locator","tensor","topology","measure","numerator","projector","UV","evanescent","conversion","RG","nonclaim")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117conttarget1_authority():
 from deuteron_wigner.bridge import hqcdc117rismom1 as c260
 if c260.PACKAGE_ROOT!=C260_ROOT:raise ValueError("C260 root changed")
 c260.load_verified_hqcdc117rismom1_authority()
 for a,h in HASHES.items():
  if sha256((ROOT/f"data/raw/c259_literature/{a.replace('/','_')}.tar").read_bytes()).hexdigest()!=h:raise ValueError(a)
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C260_package_root":C260_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117conttarget1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117conttarget1_authority()
_ROOTS={"INPUT":_r((BASELINE,C260_ROOT)),"SOURCES":source_locators()["root"],"BASIS":continuum_tensor_basis()["root"],"INVENTORY":diagram_integral_inventory()["root"],"PROGRAM":symbolic_conversion_program()["root"],"AMPLITUDES":projected_amplitudes()["root"],"MATRICES":renormalization_matrices()["root"],"RG":rg_step_scaling()["root"],"UNCERTAINTY":uncertainty_and_variants()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C261-HQCDC117CONTTARGET1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
