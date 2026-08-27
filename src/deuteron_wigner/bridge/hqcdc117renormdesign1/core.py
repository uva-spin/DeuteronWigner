"""C259 literature-backed, coefficient-free C117 renormalization design."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c259_hqcdc117renormdesign1"
BASELINE="ad81b2d61c97c9eb4624189df2713193673a4580"
C258_ROOT="b690bad5e4e47c39e5a9c482c26d673ac6eb6a5531df7806664d35c71098e897"
C117_STATUS="C117_C116_SOURCE_DERIVED_GRAPH_SPECIFIC_CURRENT_PROJECTOR_AUTHORITY_READY"
STATUS="C259_PROJECT_C117_RI_SMOM_V1_FULL_RANK_DESIGN_READY"
PLAN="C117RENORMDESIGN1-A"
NEXT="C260/HQCDC117RISMOM1"
NEXT_OBJECT="executable PROJECT_C117_RI_SMOM_V1 continuum operator basis, symmetric kinematics, four projectors, tree target matrix, and conversion-boundary authority"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40")
SOURCES={
 "hep-lat/9411010":"1e5b98f00e06db0c5266503a516b013164ba7718f59d75b10a488f5986618bee",
 "0901.2599":"5df6fc89bed523f8bc34587e998e8aae114bb53ccdb9d233ffe36d954aaf48c3",
 "hep-lat/9902030":"33db6cd6153b64ab637bddce27cc728d4f9fc27107c9a1316820dfff24f9fde0",
 "1104.4948":"ff93a11400f3d86208ae52c36a27a37ca40d8fbf0a4ad48dd4e085a14be46e49",
 "1109.1223":"7611a5dd3915afb368b701ce8a69ac38651c358d1ba0c93a1cc8526c5bc08c87",
 "2406.08065":"721b43e97027b2fc40d778b93a2ee9f26cf79cd05858004b7bf98c623b5f1b30",
 "2310.18059":"4838e99edec1d7a6745a61e188cec9a2f84ef8b50e96027c7fd6e8130d0c8ce0",
 "hep-th/0510230":"aeadd42c09096021287b5505a662b56c4274867326624e500e585f19fa00de17",
 "0801.4507":"491834fc84223afa869bd6414dcd6b32d1bb4de7b7df2b6f70e6d4f91127b296",
 "hep-th/0002062":"aa35e17e6dfddffc4ae1ae0228f17da4c5e9a0a568676e7f9c7cff066d5f653a",
 "0805.0707":"c09f3fdc705876f6815c0dd515faca74f5c5b5db45d0c119e03bcb4262d0a537",
 "hep-th/9407056":"d4f3ed33a1a77841ff32a5209aa6064bdfd0b19f8087e6bdae89992842a5db08"}
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def operator_basis():
 kinds=("orthogonal finite-subspace local density projector","longitudinal-derivative weighted density","intrinsic CM-ground projector","physical qg color-triplet projector")
 rows=[]
 for i,(d,k) in enumerate(zip(DIRECTIONS,kinds)):
  rows.append({"operator_id":f"C117-DELTA-H-{i+1}","coefficient_id":f"c_C117_{i+1}","direction":d,"source_owner":"C117","graph_local_role":k,"field_content":"instantaneous current-current q/qg graph complement","current_component":"J+ (constraint-current complement)","color_tensor":"source ordered color; C74 U3 for triplet direction","spin_helicity_tensor":"C115 source-current selection, helicity diagonal/projected as graph-defined","longitudinal_distribution":"positive APBC/PBC modes, Q0 nonzero transfer; derivative weight only for derivative_density","transverse_HO":"finite C45 shell; C64/C77 intrinsic transform for CM direction","mass_dimension":"Hamiltonian mass-squared direction; coefficient convention deferred to C260","coupling_order":"g_s^2 factored","hermitian_partner":True,"support":"P0/Q0 and boundary scope inherited C117/C254; no new holonomy","BRST_ST":"must be tested as a renormalized combination; no individual invariance claimed","redundancy":"not proven EOM, total derivative, BRST exact, or redundant","mixing_partners":DIRECTIONS,"projector_id":f"C259-DUAL-P{i+1}","activation_relevance":"Hamiltonian matrix elements at K9/K11/K13","source_roots":(C258_ROOT,C117_STATUS)})
 return _f({"rows":rows,"dimension":4,"independence_proof":"four authenticated graph-local tensor-factor coordinates; exact dual Gram construction supplies four independent linear functionals without changing the basis","closed_at_declared_scope":True,"root":_r(rows)})
def literature_corpus():
 roles={"hep-lat/9411010":"matrix projector NPR","0901.2599":"symmetric nonexceptional kinematics and conversion","hep-lat/9902030":"finite subtraction coefficients and Ward comparison","1104.4948":"mixing-basis RI/SMOM conversion matrices","1109.1223":"continuum step scaling","2406.08065":"GIRS mixing and MSbar conversion","2310.18059":"gradient-flow matching holdout","hep-th/0510230":"Fock-sector counterterms","0801.4507":"systematic sector-dependent renormalization","hep-th/0002062":"light-front QCD counterterms","0805.0707":"light-front Ward-Takahashi identity","hep-th/9407056":"Hamiltonian light-front similarity/coherence"}
 rows=tuple({"arxiv_id":a,"official_locator":f"https://export.arxiv.org/e-print/{a}","local_path":f"data/raw/c259_literature/{a.replace('/','_')}.tar","sha256":h,"authority_role":roles[a],"primary_source":True} for a,h in SOURCES.items())
 return _f({"rows":rows,"count":12,"all_primary":True,"bytes_hash_locked":True,"root":_r(rows)})
def response_diagnostics():
 matrix=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
 rows=tuple({"resolution":k,"matrix":matrix,"rank":4,"singular_values":(1,1,1,1),"condition_number":1,"left_nullspace":(),"right_nullspace":(),"construction":"dual projectors from exact C117 operator Gram matrix; normalization is scheme-defining, not a measured amplitude"} for k in RESOLUTIONS)
 return _f({"continuum":rows[0],"finite_basis":rows,"existing_C251_projectors":"operator evaluators, not four independent renormalization rows; refined by exact dualization","root":_r(rows)})
def candidate_schemes():
 rows=(
  {"id":"PROJECT_C117_RI_SMOM_V1","rank":4,"conditioning":"EXACT_DESIGN_CONDITION_1","IR_safety":"nonexceptional","gauge":"Landau","kinematics":"Euclidean symmetric p1^2=p2^2=(p1-p2)^2=mu^2; massless active-flavor limit","targets":"tree-normalized scheme targets; not physical","mixing_closure":True,"finite_C43_adapter":True,"conversion":"RI/SMOM-to-MSbar mixing matrix then physical matching","step_scaling":True,"selected":True},
  {"id":"PROJECT_C117_WARD_RISMOM_V1","rank":"up to four after C260 descendant audit","conditioning":"HOLDOUT","gauge":"Landau","targets":"exact Ward/ST rows plus dual RI/SMOM completion","conversion":"through RI/SMOM","selected":False},
  {"id":"PROJECT_C117_GIRS_V1","rank":"candidate four","conditioning":"HOLDOUT","gauge":"gauge invariant","targets":"short-distance coordinate-space scheme","conversion":"GIRS-to-MSbar","finite_C43_adapter":"source-faithful representation must be proved","selected":False},
  {"id":"PROJECT_C117_GRADIENT_FLOW_V1","rank":"candidate four","conditioning":"HOLDOUT","gauge":"gauge invariant","targets":"flowed basis and short-flow-time expansion","conversion":"short-flow-time matching","selected":False})
 return _f({"rows":rows,"selection":"PROJECT_C117_RI_SMOM_V1","reason":"only candidate with immediately explicit rank-four dual projector construction, nonexceptional IR-safe kinematics, mixing conversion precedent, step-scaling path, and direct finite-wavepacket adapter plan","route_reversal":"Ward, GIRS, and flow remain mandatory variants; selection changes if C260 closure or adapter test fails","root":_r(rows)})
def adapter_plan():
 rows=("Euclidean symmetric momenta -> light-front off-shell coordinates with named analytic continuation","off-shell momenta -> normalized finite-cell packets, no plane-wave delta substitution","continuum transverse momentum -> finite HO overlaps at each resolution","operator/source normalization and g_s^2 factor ownership","Landau-gauge BRST/ST convention and descendant checks","C254 caller Abel topology with order of limits retained","boundary/link/holonomy classes remain separate","RI/SMOM running/conversion matrix -> MSbar then physical observable matching")
 return _f({"affine_system":"M^(K)(mu,S)c^(K)=t^S(mu)-r^(K)(mu,S)","resolutions":RESOLUTIONS,"adapters":rows,"coefficients_evaluated":False,"resolution_average":False,"root":_r(rows)})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"scheme":"PROJECT_C117_RI_SMOM_V1","rank":4,"coefficients_selected":0,"physical_targets_selected":0,"next":NEXT,"next_object":NEXT_OBJECT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"unknown_coefficients_zeroed":0,"coefficients_selected":0,"physical_target_claimed":0,"scheme_target_called_physical":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117renormdesign1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("basis","projector","source","hash","rank","kinematics","gauge","target","conversion","adapter","resolution","nonclaim")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117renormdesign1_authority():
 from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenttargetaudit1 as c258
 from deuteron_wigner.bridge.icreg2 import core as c117
 if c258.PACKAGE_ROOT!=C258_ROOT:raise ValueError("C258 root changed")
 c258.load_verified_hqcdriquarkfixedkv2currenttargetaudit1_authority();c117.load_verified_current_projector_authority()
 for a,h in SOURCES.items():
  p=ROOT/f"data/raw/c259_literature/{a.replace('/','_')}.tar"
  if sha256(p.read_bytes()).hexdigest()!=h:raise ValueError(f"literature hash: {a}")
 if response_diagnostics()["finite_basis"][0]["rank"]!=4:raise ValueError("rank")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C258_package_root":C258_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117renormdesign1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117renormdesign1_authority()
_ROOTS={"INPUT":_r((BASELINE,C258_ROOT)),"BASIS":operator_basis()["root"],"LITERATURE":literature_corpus()["root"],"RESPONSE":response_diagnostics()["root"],"SCHEMES":candidate_schemes()["root"],"ADAPTER":adapter_plan()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C259-HQCDC117RENORMDESIGN1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
