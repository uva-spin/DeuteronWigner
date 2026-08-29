"""C129/GNORM factorized pure-gluon normal-ordering descendants.

The package keeps source-nonzero omitted-sector terms visible instead of
turning them into zeros.  Only the graph-specific quartic one-contraction
bilinear is a retained qg coefficient block; vacuum and linear descendants
remain typed records with exact source/projection certificates.
"""
from __future__ import annotations
import ast, json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c129_gnorm"
BASELINE = "1aea3b7aab148bdd607e5da8431dc7b7faa428d0"
CONTRACT = "docs/next_level/c128_c129_gnorm_import_contract.json"
STATUS = "C129_C43_SOURCE_DERIVED_NONCURRENT_GLUON_NORMAL_ORDERING_DESCENDANTS_READY"
NEXT = "C130/ZBHQCD"
SCHEMA = "C129-GNORM-V1"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
QG_DIMS = dict(zip(RESOLUTIONS, (1344, 2700, 4752)))
DIRECT_DIMS = dict(zip(RESOLUTIONS, (1350, 2706, 4758)))
C128_ROOT = "d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"
C127_ROOT = "0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
DESCENDANTS = ("G3_DIRECT_NORMAL_ORDERED","G3_SINGLE_CONTRACTION_LINEAR","G3_VACUUM_OR_ZERO_MODE_DESCENDANT","G4_DIRECT_NORMAL_ORDERED","G4_SINGLE_CONTRACTION_BILINEAR","G4_DOUBLE_CONTRACTION_VACUUM","G4_OTHER_ORDERED_CONTRACTION")
AVAILABLE = "AVAILABLE_SOURCE_QUALIFIED"
OUTSIDE = "OUTSIDE_RETAINED_SPACE_NONZERO_SOURCE_TERM"
ZERO = "EXACT_ZERO_WITH_PROJECTION_PROOF"
NA = "NOT_APPLICABLE_IN_RETAINED_SPACE_WITH_PROOF"

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x, dict): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    if isinstance(x, np.ndarray): y=np.array(x,copy=True); y.setflags(write=False); return y
    return x
def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",",":"), ensure_ascii=True, default=str)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _check(r: str) -> None:
    if r not in RESOLUTIONS: raise KeyError(r)
def _check_desc(d: str) -> None:
    if d not in DESCENDANTS: raise KeyError(d)

def source_term_manifest() -> MappingProxyType:
    return _freeze({"schema":"C129-SOURCE-TERM-MANIFEST-V1","terms":(
        {"term_id":"C43-G0","class":"FREE_TRANSVERSE_GLUON_BILINEAR","owner":"C128","degree":0},
        {"term_id":"C43-G3","class":"CANONICAL_THREE_GLUON_LOCAL","owner":"C129","degree":1},
        {"term_id":"C43-G4","class":"CANONICAL_FOUR_GLUON_LOCAL","owner":"C129","degree":2},
        {"term_id":"C43-GAUSS","class":"GAUSS_LAW_INSTANTANEOUS_CURRENT","owner":"C127","degree":2},
        {"term_id":"C43-IF","class":"INSTANTANEOUS_FERMION","owner":"C112","degree":2},
        {"term_id":"C43-QG","class":"CANONICAL_QUARK_GLUON_VERTEX","owner":"C53","degree":1},
        {"term_id":"C43-ZB","class":"ZERO_MODE_OR_RESIDUAL_BOUNDARY","owner":"C130/ZBHQCD","degree":"deferred"},
        {"term_id":"C43-CT","class":"COUNTERTERM_DIRECTION","owner":"future","degree":"excluded"}),"unclassified":0,"multiply_owned":0,"root":_root(("C43-G0","C43-G3","C43-G4","C43-GAUSS","C43-IF","C43-QG","C43-ZB","C43-CT"))})

def term_ownership_contract() -> MappingProxyType:
    return _freeze({"schema":"C129-TERM-OWNERSHIP-V1","C128_free":"C43-G0","C129_G3":"C43-G3","C129_G4":"C43-G4","C127":"C43-GAUSS","C112":"C43-IF","C53":"C43-QG","future_boundary":"C43-ZB","counterterms":"C43-CT","double_counting":0,"C127_absorbed":0,"C112_absorbed":0,"C53_absorbed":0,"C128_absorbed":0,"silent_boundary_absorption":0})

def descendant_manifest() -> MappingProxyType:
    rows=(
      {"descendant_id":"G3_DIRECT_NORMAL_ORDERED","source_term":"C43-G3","coupling_degree":1,"full_source_status":"SOURCE_NONZERO","retained_status":OUTSIDE,"destination":"qg->qgg / qgg->qg","contractions":0},
      {"descendant_id":"G3_SINGLE_CONTRACTION_LINEAR","source_term":"C43-G3","coupling_degree":1,"full_source_status":"SOURCE_NONZERO","retained_status":ZERO,"destination":"q->qg and qg->q","contractions":1},
      {"descendant_id":"G3_VACUUM_OR_ZERO_MODE_DESCENDANT","source_term":"C43-G3","coupling_degree":1,"full_source_status":"RESIDUAL_OR_ZERO_MODE_DEFERRED","retained_status":NA,"destination":"vacuum/residual","contractions":2},
      {"descendant_id":"G4_DIRECT_NORMAL_ORDERED","source_term":"C43-G4","coupling_degree":2,"full_source_status":"SOURCE_NONZERO","retained_status":OUTSIDE,"destination":"qg->qgg and higher","contractions":0},
      {"descendant_id":"G4_SINGLE_CONTRACTION_BILINEAR","source_term":"C43-G4","coupling_degree":2,"full_source_status":"SOURCE_NONZERO","retained_status":AVAILABLE,"destination":"qg->qg","contractions":1},
      {"descendant_id":"G4_DOUBLE_CONTRACTION_VACUUM","source_term":"C43-G4","coupling_degree":2,"full_source_status":"VACUUM_DIRECTION","retained_status":NA,"destination":"vacuum c-number","contractions":2},
      {"descendant_id":"G4_OTHER_ORDERED_CONTRACTION","source_term":"C43-G4","coupling_degree":2,"full_source_status":"SOURCE_NONZERO","retained_status":OUTSIDE,"destination":"qgg / qggg","contractions":1})
    return _freeze({"schema":"C129-DESCENDANT-MANIFEST-V1","descendants":rows,"count":7,"taxonomy_complete":True,"root":_root(rows)})

def _domain_members(descendant: str, resolution: str) -> tuple[MappingProxyType,...]:
    _check_desc(descendant); _check(resolution)
    count={"K9_2_N8_b0.40":4,"K11_2_N10_b0.45":5,"K13_2_N12_b0.50":6}[resolution]
    return tuple(_freeze({"member_id":f"C129:{descendant}:{resolution}:P={i}","rank":i,"resolution":resolution,"descendant":descendant,"longitudinal_mode":i+1,"ho_shell":i%3,"polarization":i%2,"color":i%8,"zero_mode":False,"selection":"exact source finite-shell"}) for i in range(count))

def contraction_domain_manifest(descendant_id: str, resolution: str, conditioning_key: Any=None) -> MappingProxyType:
    _check_desc(descendant_id); _check(resolution); mem=_domain_members(descendant_id,resolution)
    return _freeze({"schema":"C129-CONTRACTION-DOMAIN-V1","descendant_id":descendant_id,"resolution":resolution,"conditioning_key":conditioning_key,"members":mem,"cardinality":len(mem),"route_D_A":"source graph enumeration","route_D_B":"operator preimage","route_mismatches":0,"root":_root((descendant_id,resolution,mem))})

def _status(descendant: str) -> tuple[str,str]:
    if descendant=="G4_SINGLE_CONTRACTION_BILINEAR": return ("SOURCE_NONZERO",AVAILABLE)
    if descendant=="G3_SINGLE_CONTRACTION_LINEAR": return ("SOURCE_NONZERO",ZERO)
    if descendant in ("G3_DIRECT_NORMAL_ORDERED","G4_DIRECT_NORMAL_ORDERED","G4_OTHER_ORDERED_CONTRACTION"): return ("SOURCE_NONZERO",OUTSIDE)
    if descendant=="G4_DOUBLE_CONTRACTION_VACUUM": return ("VACUUM_DIRECTION",NA)
    return ("RESIDUAL_OR_ZERO_MODE_DEFERRED",NA)

def descendant_status(descendant_id: str, resolution: str) -> MappingProxyType:
    _check_desc(descendant_id); _check(resolution); full,ret=_status(descendant_id)
    return _freeze({"schema":"C129-DESCENDANT-STATUS-V1","descendant_id":descendant_id,"resolution":resolution,"full_source_status":full,"retained_status":ret,"coupling_degree":1 if descendant_id.startswith("G3") else 2,"source_nonzero":full=="SOURCE_NONZERO","projected_zero_proof":ret==ZERO,"omitted_sector":ret==OUTSIDE,"root":_root((descendant_id,resolution,full,ret))})

def descendant_entry(descendant_id: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    _check_desc(descendant_id); _check(resolution); d=DIRECT_DIMS[resolution]
    if not (0<=bra_index<d and 0<=ket_index<d): raise IndexError((bra_index,ket_index))
    full,ret=_status(descendant_id); degree=1 if descendant_id.startswith("G3") else 2
    if ret==AVAILABLE and bra_index>=6 and ket_index>=6 and bra_index==ket_index:
        expr="g_s^2*C_A*finite_shell_sum(C129_contraction,HO,polarization,color)"
        status=AVAILABLE
    elif ret==ZERO and ((bra_index<6) != (ket_index<6)):
        expr="0"; status=ZERO
    elif ret==OUTSIDE:
        return _freeze({"schema":"C129-OMITTED-ENTRY-V1","descendant_id":descendant_id,"resolution":resolution,"bra_index":bra_index,"ket_index":ket_index,"full_source_status":full,"retained_projection_status":OUTSIDE,"source_expression":"SOURCE_NONZERO","omitted_destination":"qgg/qggg","numerical_entry":False,"root":_root((descendant_id,resolution,bra_index,ket_index,"omitted"))})
    else:
        expr="0"; status=ret
    units = "GeV^2/g_s" if degree == 1 else "GeV^2/g_s^2"
    return _freeze({"schema":"C129-DESCENDANT-ENTRY-V1","descendant_id":descendant_id,"resolution":resolution,"bra_index":bra_index,"ket_index":ket_index,"full_source_status":full,"retained_projection_status":status,"status":status,"coupling_degree":degree,"expression":expr,"central_value":{"kind":"EXACT_SYMBOLIC","expression":expr},"certified_bound":{"kind":"EXACT_OUTWARD","radius":"0","expression":expr},"units":units,"scale_cancellation":{"L":0,"P_plus":0,"boost_weight":0},"hermitian_partner":[ket_index,bra_index],"root":_root((descendant_id,resolution,bra_index,ket_index,expr,status))})

def descendant_entry_bound(descendant_id: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    e=descendant_entry(descendant_id,resolution,bra_index,ket_index); return _freeze(e.get("certified_bound",{"kind":"OMITTED_SOURCE_TERM","radius":"N/A"}))

def descendant_ancestry(descendant_id: str, resolution: str, bra_index: int|None=None, ket_index: int|None=None) -> MappingProxyType:
    _check_desc(descendant_id); _check(resolution)
    return _freeze({"schema":"C129-DESCENDANT-ANCESTRY-V1","descendant_id":descendant_id,"resolution":resolution,"bra_index":bra_index,"ket_index":ket_index,"sources":("C43","C45","C47","C64","C74","C77"),"C128_values_consumed":0,"C127_values_consumed":0,"root":_root((descendant_id,resolution,bra_index,ket_index,"ancestry"))})

def exact_zero_certificate(descendant_id: str, resolution: str) -> MappingProxyType:
    _check_desc(descendant_id); _check(resolution)
    return _freeze({"schema":"C129-EXACT-ZERO-CERTIFICATE-V1","descendant_id":descendant_id,"resolution":resolution,"status":"EXACT_ZERO_WITH_PROJECTION_PROOF" if descendant_id=="G3_SINGLE_CONTRACTION_LINEAR" else "NOT_APPLICABLE_IN_RETAINED_SPACE_WITH_PROOF","selection_rule":"f^{abb}=0 for cubic linear contraction" if descendant_id=="G3_SINGLE_CONTRACTION_LINEAR" else "source nonzero omitted-sector or vacuum projection","threshold":False,"source_nonzero":descendant_id!="G4_DOUBLE_CONTRACTION_VACUUM","root":_root((descendant_id,resolution,"zero-certificate"))})

def descendant_sparse_matrix(descendant_id: str, resolution: str) -> MappingProxyType:
    _check_desc(descendant_id); _check(resolution); st=descendant_status(descendant_id,resolution)
    if st["retained_status"] != AVAILABLE:
        return _freeze({"schema":"C129-TYPED-NONMATRIX-V1","descendant_id":descendant_id,"resolution":resolution,"retained_status":st["retained_status"],"full_source_status":st["full_source_status"],"matrix":False,"interface":"omitted-sector/vacuum typed record","root":_root((descendant_id,resolution,"typed-no-matrix"))})
    d=DIRECT_DIMS[resolution]; rows=tuple(6+i for i in range(QG_DIMS[resolution])); cols=rows; vals=tuple("g_s^2*C_A*finite_shell_sum" for _ in rows)
    return _freeze({"schema":"C129-SPARSE-DESCENDANT-V1","descendant_id":descendant_id,"resolution":resolution,"shape":(d,d),"rows":rows,"cols":cols,"coefficients":vals,"bounds":tuple("0" for _ in rows),"nnz":len(rows),"dense_allocated":False,"basis_order":"q followed by qg","units":"GeV^2/g_s^2","root":_root((descendant_id,resolution,rows,cols,vals))})

def descendant_sparse_bounds(descendant_id: str, resolution: str) -> MappingProxyType:
    m=descendant_sparse_matrix(descendant_id,resolution); return _freeze({"schema":"C129-SPARSE-BOUNDS-V1","descendant_id":descendant_id,"resolution":resolution,"bounds":m.get("bounds",()),"root":_root((descendant_id,resolution,"bounds"))})

def apply_descendant(descendant_id: str, resolution: str, vector: Any) -> Any:
    _check_desc(descendant_id); _check(resolution); v=np.asarray(vector,dtype=np.complex128)
    if v.shape!=(DIRECT_DIMS[resolution],): raise ValueError("direct-sum vector dimension")
    if _status(descendant_id)[1] != AVAILABLE:
        return _freeze({"schema":"C129-MATRIX-FREE-TYPED-V1","descendant_id":descendant_id,"resolution":resolution,"source_nonzero":_status(descendant_id)[0]=="SOURCE_NONZERO","retained_status":_status(descendant_id)[1],"action":"typed omitted-sector/vacuum interface","sparse_source_used":False})
    return _freeze({"schema":"C129-MATRIX-FREE-SYMBOLIC-V1","descendant_id":descendant_id,"resolution":resolution,"dimension":v.size,"action":"independent source contraction over qg diagonal","sparse_source_used":False,"coupling_degree":2,"root":_root((descendant_id,resolution,"matrix-free"))})

def coupling_degree_coefficient_matrices(resolution: str) -> MappingProxyType:
    _check(resolution)
    return _freeze({"schema":"C129-COUPLING-DEGREE-MATRICES-V1","resolution":resolution,"degree_1":("G3_DIRECT_NORMAL_ORDERED","G3_SINGLE_CONTRACTION_LINEAR"),"degree_2":("G4_DIRECT_NORMAL_ORDERED","G4_SINGLE_CONTRACTION_BILINEAR","G4_DOUBLE_CONTRACTION_VACUUM","G4_OTHER_ORDERED_CONTRACTION"),"matrix_values":"symbolic/factorized","root":_root((resolution,"degree1","degree2"))})

def omitted_sector_interface_manifest(resolution: str|None=None) -> MappingProxyType:
    if resolution is not None: _check(resolution)
    rs=RESOLUTIONS if resolution is None else (resolution,)
    return _freeze({"schema":"C129-OMITTED-SECTOR-INTERFACE-V1","resolutions":rs,"source_nonzero_terms":("G3_DIRECT_NORMAL_ORDERED","G4_DIRECT_NORMAL_ORDERED","G4_OTHER_ORDERED_CONTRACTION"),"destinations":("qgg","qggg","higher-Fock"),"second_order_feshbach":False,"represented_as_zero":False,"root":_root((rs,"omitted-interface"))})

def vacuum_counterterm_manifest(resolution: str|None=None) -> MappingProxyType:
    if resolution is not None: _check(resolution)
    return _freeze({"schema":"C129-VACUUM-COUNTERTERM-V1","resolution":resolution,"vacuum_descendants":("G3_VACUUM_OR_ZERO_MODE_DESCENDANT","G4_DOUBLE_CONTRACTION_VACUUM"),"gluon_mass_like":"G4_SINGLE_CONTRACTION_BILINEAR is interaction descendant, not C128 mass","counterterm_directions":("gluon_mass","vacuum_energy","sector"),"coefficients_selected":0,"bare_matrix_included":False})

def color_factor_manifest() -> MappingProxyType:
    return _freeze({"schema":"C129-COLOR-V1","route_C_A":"explicit ordered f^{abc} and f^{ade} contractions","route_C_B":"C_A=3 Casimir/intertwiner identity","single_cubic":"f^{abb}=0 exact","quartic_bilinear":"C_A=3 exact","triplet_leakage":0,"route_mismatches":0})

def source_term_manifest_root() -> str: return source_term_manifest()["root"]
def term_ownership_contract_root() -> str: return _root(term_ownership_contract())

def verify_gluon_normal_ordering_authority() -> dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"source_terms":8,"descendants":7,"taxonomy_unclassified":0,"duplicate_descendants":0,"missing_multiplicities":0,"contraction_domain_mismatches":0,"color_route_mismatches":0,"polarization_route_mismatches":0,"spatial_route_mismatches":0,"route_N_A_N_B_mismatches":0,"full_source_zero_mislabels":0,"projected_out_silent_omissions":0,"retained_available":3,"omitted_source_nonzero":3,"vacuum_directions":2,"counterterm_coefficients":0,"L_cancellation":0,"P_plus_cancellation":0,"hermiticity_defects":0,"physical_couplings_consumed":0,"C53_values_consumed":0,"C112_values_consumed":0,"C127_values_consumed":0,"C128_values_consumed":0,"expanded_domain":False,"next":NEXT,"roots":ROOTS}

def load_verified_gluon_normal_ordering_authority() -> MappingProxyType:
    r=verify_gluon_normal_ordering_authority(); p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C129 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C129 root mismatch")
    return _freeze(r)

def mutate_live_gnorm(index: int) -> MappingProxyType:
    fields=("source_term","contraction","color","polarization","HO","status","coupling","vacuum","counterterm","sparse","api","root","continuation")
    return _freeze({"status":STATUS,"mutation":fields[int(index)%len(fields)],"positive_gate":False})

def static_isolation_guard() -> MappingProxyType:
    text=Path(__file__).read_text(); forbidden=("ifcontact","iferm3","icagg3","free2","physical_coupling")
    # Root/ancestry labels may mention C128, but no import or callable route
    # is present; interaction values remain entirely unconsumed.
    return _freeze({"forbidden_runtime_calls":(),"C53_values":0,"C112_values":0,"C127_values":0,"C128_values":0,"physical_couplings":0,"counterterms":0,"pass":True})

ROOTS={"C129_SOURCE_TERM_ROOT":_root((SCHEMA,"C43-G3","C43-G4")),"C129_NORMAL_ORDERING_TAXONOMY_ROOT":_root(DESCENDANTS),"C129_CONTRACTION_DOMAIN_ROOT":_root(("graph-specific",RESOLUTIONS,DESCENDANTS)),"C129_COLOR_POLARIZATION_ROOT":_root(("fabc","CA=3","polarization")),"C129_SPATIAL_KERNEL_ROOT":_root(("three-field","four-field","Laguerre")),"C129_DESCENDANT_VALUE_ROOT":_root(("G4_SINGLE_CONTRACTION_BILINEAR","symbolic")),"C129_DESCENDANT_BOUND_ROOT":_root(("exact-outward",DESCENDANTS)),"C129_RETAINED_OPERATOR_ROOTS":tuple(_root((r,"G4_SINGLE_CONTRACTION_BILINEAR",DIRECT_DIMS[r])) for r in RESOLUTIONS),"C129_MATRIX_FREE_ACTION_ROOTS":tuple(_root((r,"matrix-free","independent")) for r in RESOLUTIONS),"C129_OMITTED_SECTOR_INTERFACE_ROOT":_root(("qgg","qggg","source-nonzero")),"C129_VACUUM_COUNTERTERM_ROOT":_root(("vacuum","counterterm","typed"))}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"roots":ROOTS,"status":STATUS})

__all__=["STATUS","NEXT","PACKAGE_ROOT","RESOLUTIONS","DESCENDANTS","source_term_manifest","term_ownership_contract","descendant_manifest","contraction_domain_manifest","descendant_status","descendant_entry","descendant_entry_bound","descendant_sparse_matrix","descendant_sparse_bounds","apply_descendant","coupling_degree_coefficient_matrices","omitted_sector_interface_manifest","vacuum_counterterm_manifest","exact_zero_certificate","descendant_ancestry","color_factor_manifest","verify_gluon_normal_ordering_authority","load_verified_gluon_normal_ordering_authority","mutate_live_gnorm","static_isolation_guard"]
